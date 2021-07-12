import argparse
import logging
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
import os
import datetime

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../formal-atrium-273514-f914f1e39b28.json"

class DataIngestion:
    def parse_method(self, string_input):
        import datetime
        import pytz
        import json
        from json import dumps
        values = re.split(",", re.sub('\r\n', '', re.sub(u'"', '', string_input)))
        row = dict(zip(('tripduration', 'starttime', 'stoptime', 'startstationid', 'startstationname', 'startstationlatitude', 'startstationlongitude','stopstationid', 'stopstationname', 'stopstationlatitude', 'stopstationlongitude', 'bikeid', 'usertype', 'birthyear', 'gender'), values))
        
        for r in row:
            if(r=="starttime" or r=="stoptime"):
                a = row[r]

                if(a[2] == "-"):
                    if(len(row[r]) == 16):
                        form1="%d-%m-%Y %H:%M"
                        form2="%Y-%m-%d %H:%M"
                    elif(len(row[r]) > 19):
                        form1="%d-%m-%Y %H:%M:%S.%f"
                        form2="%Y-%m-%d %H:%M:%S.%f"
                    else:
                        form1="%d-%m-%Y %H:%M:%S"
                        form2="%Y-%m-%d %H:%M:%S"
                    row[r]=datetime.datetime.strptime(row[r], form1).strftime(form2)
                else:
                    if(len(row[r]) == 16):
                        form1="%d-%m-%Y %H:%M"
                        form2="%Y-%m-%d %H:%M"
                    elif(len(row[r]) > 19):
                        form1="%d-%m-%Y %H:%M:%S.%f"
                        form2="%Y-%m-%d %H:%M:%S.%f"
                    else:
                        form1="%d-%m-%Y %H:%M:%S"
                        form2="%Y-%m-%d %H:%M:%S"
                    row[r]=datetime.datetime.strptime(row[r], form2).strftime(form2)
                x = row[r]
                y = datetime.datetime.strptime(x, form2)
                local = pytz.timezone ("US/Eastern")
                local_dt = local.localize(y, is_dst=None)
                utc_dt = local_dt.astimezone(pytz.utc)
                row[r] = utc_dt.strftime(form2)
        return row

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', required=False, help='Input file',
                        default='gs://80088/201306-citibike-tripdata.csv')
    parser.add_argument('--output', dest='output', required=False, help='Output BQ table',
                        default='formal-atrium-273514:google1.table3')
    parser.add_argument('--pubsub', dest='pubsub', required=False, help='input pubsub topic',
                        default='projects/formal-atrium-273514/topics/stream')

    known_args, pipeline_args = parser.parse_known_args(argv)
    data_ingestion = DataIngestion()
    options = PipelineOptions(pipeline_args)
    options.view_as(SetupOptions).save_main_session = True
    p2 = beam.Pipeline(options=PipelineOptions(pipeline_args))
    p = beam.Pipeline(options=PipelineOptions(pipeline_args))
    (p 
     | 'Read File from GCS' >> beam.io.ReadFromText(known_args.input,skip_header_lines=1)
     | 'String To BigQuery Row' >> beam.Map(lambda s: data_ingestion.parse_method(s))
     | 'Write to BigQuery' >> beam.io.Write(beam.io.BigQuerySink(known_args.output,
                                            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)))
    
    
    
    
    
    p.run().wait_until_finish()
    p2.rin().ait_until_finish()
    


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()