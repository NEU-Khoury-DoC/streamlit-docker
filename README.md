# Sample App for 2024 DoC

Ultimately, this will be set up to auto-deploy a container to Fly.io. 

Right now, the `src/` directory contains a single `.py` file in which we can put some 
fun Streamlit stuff for now.


## Getting Started


1. Move into the app folder with `cd app`

2. In your preferred python environment (or you can create a new one), install the python dependencies. 

```bash
pip install -r src/requirements.txt
```

3. Run the Streamlit app locally by executing the following command (if you get an error, you may need to reload your shell/terminal for it to find the `streamlit` executable):

```bash
streamlit run src/testapp.py
```


## To Do:

- [ ] Devlop an example ML service that can perform some type of real-time inferencing. (Maybe just start off with like random number generator or something)
- [ ] Dockerize the ML App
- [ ] Automate deployment with Actions
- [ ] Find out about deploying multiple containers to Fly.io from 1 repo. Is that possible?
- [ ] Find out what the AWS equivalent of Fly.io is
