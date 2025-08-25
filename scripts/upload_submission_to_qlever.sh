set -e
LATEST_DATASET=$(ls -t /home/ubuntu/data/ | head -n 1)
DATASET_PATH="/home/ubuntu/data/${LATEST_DATASET}"

ln -r -s -f $DATASET_PATH /home/ubuntu/dataset.ttl

cd /home/ubuntu/kgreg
echo "Stopping current qlever instance"
qlever stop
echo "Getting data"
qlever get-data
echo "Indexing data"
qlever index --overwrite-existing
echo "Starting Qlever"
qlever start
cd -
