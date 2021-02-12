
echo
echo -e $(date) "C19 Collect Data starting -----------------------------------------------"

echo -e $(date) 'Python version'
/usr/local/bin/python3 --version

echo -e $(date) 'Removing old data'
cd /Users/paulhart/Documents/Development/BC-Covid-19-Data
rm -rf COVID-19

echo -e $(date) 'Cloning data'
git clone https://github.com/CSSEGISandData/COVID-19.git

echo -e $(date) 'Creating csv data'
/usr/local/bin/python3 /Users/paulhart/Documents/Development/BC-Covid-19-Data/App/C19CollectDataMain.py
echo -e  $(date) 'Creating csv data complete'
echo 

echo -e "Add files"
cd /Users/paulhart/Documents/Development/BC-Covid-19-Data
git add --all

echo 
echo -e $(date) "Commit files"
git commit -m "Daily update $(date)"

echo 
echo -e $(date) "Push files to Github"
git push -u origin main

echo
echo -e $(date) "End C19 Collect Data complete -------------------------------------------"
