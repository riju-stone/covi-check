import pickle
from flask import Flask, render_template, request
app = Flask(__name__)

# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')

# dump information to that file
regressor = pickle.load(file)

# close the file
file.close()


@app.route('/', methods=["GET", "POST"])
def infection_predict():
    if request.method == "POST":
        bp_checked = request.form.get("bp") != None
        fev_checked = request.form.get("fev") != None
        ht_checked = request.form.get("ht") != None
        alg_checked = request.form.get("alg") != None
        dc_checked = request.form.get("dc") != None
        st_checked = request.form.get("st") != None
        fat_checked = request.form.get("fat") != None
        vpep_checked = request.form.get("vpep") != None
        rn_checked = request.form.get("rn") != None
        ast_checked = request.form.get("ast") != None
        gas_checked = request.form.get("gas") != None
        fwpep_checked = request.form.get("fwpep") != None
        cld_checked = request.form.get("cld") != None
        head_checked = request.form.get("head") != None
        at_checked = request.form.get("at") != None
        wm_checked = request.form.get("wm") != None
        hd_checked = request.form.get("hd") != None
        diab_checked = request.form.get("diab") != None
        cont_checked = request.form.get("cont") != None
        sm_checked = request.form.get("sm") != None

        feature_list = [bp_checked, fev_checked, ht_checked, alg_checked, dc_checked, st_checked, fat_checked, vpep_checked, rn_checked, ast_checked,
                        gas_checked, fwpep_checked, cld_checked, head_checked, at_checked, wm_checked, hd_checked, diab_checked, cont_checked, sm_checked]

        feature_list = [1 if i == True else 0 for i in feature_list]
        feature_list = [feature_list]
        inf_prob = regressor.predict_proba(feature_list)[0][1]
        # print(inf_prob)
        inf_prob = round(inf_prob * 100)
        return render_template('index.html', inf=inf_prob)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
