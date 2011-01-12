cd workers
find . -name "*.pyc" -exec rm '{}' ';'
mkdir workers 
cp -R base_worker workers/
cp  README workers/
cp  worker.zip workers/
cp  exec_worker.sh workers/
zip -r ../web_interface/media/workers.zip workers
rm -r workers
echo 'The zip is now hosted at: "web_interface/media/workers"' 
