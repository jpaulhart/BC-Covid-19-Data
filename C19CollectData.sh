
echo
echo -e $(date) "C19 Collect Data starting -----------------------------------------------"

echo -e $(date) 'Python version'
/usr/local/bin/python3.8 --version

echo -e $(date) 'Removing old data'
cd /Users/paulhart/GitHubWork/BC-Covid-19-Data
rm -rf COVID-19

echo -e $(date) 'Cloning data'
git clone https://github.com/CSSEGISandData/COVID-19.git

echo -e $(date) 'Creating csv data'
/usr/local/bin/python3.8 App/C19CollectDataMain.py
echo -e  $(date) 'Creating csv data complete'
echo 

echo -e "Add files"
git add --all

echo 
echo -e $(date) "Commit files"
git commit -m "Daily update $(date)"

echo 
echo -e $(date) "Push files to Github"
git push -u origin main

echo
echo -e $(date) "End C19 Collect Data complete -------------------------------------------"
y
echo -e $(date) "Start C19 Collect Data (2)) -------------------------------------------"
echo -e
cd /Users/paulhart/Dropbox/Covid-19/C19DataDownload
pwd

echo -e $(date) 'Creating json data'
echo -e
/Users/paulhart/Dropbox/Covid-19/C19DataDownload/DerivedData/C19DataDownload/Build/Products/Debug/C19DataDownload /Users/paulhart/Dropbox/Covid-19/C19DataDownload/C19DataDownload/LocationData

echo 
echo -e $(date) "Add files"
echo -e
echo -e "Add files"
git add --all


echo 
echo -e $(date) "Commit files"
echo -e
git commit -m "Daily update $(date)"
echo -e 
echo -e  $(date) 'Creating json data complete'

echo -e
echo -e $(date) "Push files to Github"
echo -e
git push -u origin main
echo -e 

echo -e $(date) "End C19 Collect Data complete (2) -------------------------------------------"
