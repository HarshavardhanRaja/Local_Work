import argparse
import logging
import re

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions


def main(argv=None, save_main_session=True):
  """Main entry point; defines and runs the wordcount pipeline."""

  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input',
      dest='input',
      default='test.txt',
      help='Input file to process.')
  parser.add_argument(
      '--output',
      dest='output',
      default='count_2.txt',
      help='Output file to write results to.')
  parser.add_argument(
      '--runner',
      dest='runner',
      default='DirectRunner',
      # help='Output file to write results to.'
  )

  known_args, pipeline_args = parser.parse_known_args(argv)
  print(f"known_args: {known_args}")
  print(f"pipeline_args: {pipeline_args}")


  class concat_words(beam.DoFn):
    def process(self, text_tuple):
        original_value = text_tuple[0]
        new_tuple = (f"word_{original_value}", text_tuple[1])
        yield new_tuple


  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
  with beam.Pipeline(options=pipeline_options) as p:

    # Read the text file[pattern] into a PCollection.
    lines = p | ReadFromText(known_args.input)

    # Count the occurrences of each word.
    counts = (
        lines
        | 'Split' >> (
            beam.FlatMap(
                lambda x: re.findall(r'[A-Za-z\']+', x)).with_output_types(str))
        | 'PairWithOne' >> beam.Map(lambda x: (len(x), 1))
        | 'concat' >> beam.ParDo(concat_words())
        | 'GroupAndSum' >> beam.CombinePerKey(sum))

    # Format the counts into a PCollection of strings.
    def format_result(word_count):
      (word, count) = word_count
      return '%s: %s' % (word, count)

    output = counts | 'Format' >> beam.Map(format_result)


    # Write the output using a "Write" transform that has side effects.
    # pylint: disable=expression-not-assigned
    output | WriteToText(known_args.output)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  main()




