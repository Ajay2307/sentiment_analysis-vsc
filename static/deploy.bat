git init
git add -A
git config --global user.email 'iniya.dhanu@gmail.com' 
git config --global user.name 'Dhanusha' 
git commit -m 'lets'
git remote add origin https://github.com/dhanusha-sp/finalDep.git
set /p branchname='Enter branch name:'
git branch %branchname%
git checkout %branchname%
git push -u origin %branchname%
oc login -u dhanusha -p dhanusha https://console.prod.pdcloudex.com:8443 --insecure-skip-tls-verify
oc new-app https://github.com/dhanusha-sp/finalDep.git#%branchname% -n mlpaas
oc create route edge --service=finaldep -n mlpaas
FOR /F "tokens=* USEBACKQ" %%F IN (`oc get route finaldep -o template --template {{.spec.host}} -n mlpaas`) DO (
SET var=%%F
)
ECHO https://%var%