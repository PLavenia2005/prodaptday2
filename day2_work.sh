#!/bin/bash

echo "creating project structure"
mkdir -p project/{src,docs,scripts,backup}

echo "creating files..."
touch project/src/main.c
touch project/src/helper.c
touch project/docs/readme.txt
touch project/scripts/run.sh

echo "adding content to readme"
echo "Linux mission impossible">project/docs/readme.txt

echo "copying readme.."
cp project/docs/readme.txt project/backup/

echo "moving helper.c..."
mv project/src/helper.c project/backup/

echo "remaing main.c to app.c"
mv project/src/main.c project/src/app.c

echo "searching for app.c.."
find project -name "app.c"

echo "giving execute permission.."
chmod +x project/scripts/run.sh

echo "creating archive.."
tar -czvf project.tar.gz project


echo "extracting archive.."
mkdir recovered_project
tar -xzvf project.tar.gz -C recovered_project

echo "final structure"
find recovered_project
