

# echo PROJECT_ID
# read PROJECT_ID
# #echo "Hello $MY_NAME - hope you're well."

# echo MY_REGION
# read MY_REGION
# # echo "Hello $MY_NAME1 - hope you're well."

# echo Device
# read Device


cd $HOME/Device1/training-data-analyst/quests/iotlab/


python cloudiot_mqtt_example_json.py \
   --project_id=coe-solutions-215839\
   --cloud_region=us-central1\
   --registry_id=iotlab-registry \
   --device_id=Device1\
   --private_key_file=rsa_private.pem \
   --message_type=event \
   --algorithm=RS256 &

cd $HOME/Device2/training-data-analyst/quests/iotlab/

python cloudiot_mqtt_example_json.py \
   --project_id=coe-solutions-215839\
   --cloud_region=us-central1\
   --registry_id=iotlab-registry \
   --device_id=Device2\
   --private_key_file=rsa_private.pem \
   --message_type=event \
   --algorithm=RS256 &
