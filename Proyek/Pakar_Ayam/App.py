from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# Gejala
gejala = {
    "G01": "Nafsu makan menurun",
    "G02": "Sayap terkulai",
    "G03": "Diare",
    "G04": "Mata berair",
    "G05": "Pembengkakan kepala",
    "G06": "Keluar lendir dari hidung",
    "G07": "Bulu kusam dan berdiri",
    "G08": "Kotoran putih encer",
    "G09": "Lemah dan lesu",
    "G10": "Bersin",
    "G11": "Hidung basah dan bengkak",
    "G12": "Bau tidak sedap dari hidung",
    "G13": "Jengger membiru",
    "G14": "Kematian mendadak",
    "G15": "Jalan sempoyongan",
}

# Penyakit
penyakit = {
    "P01": "Newcastle Disease",
    "P02": "Avian Influenza",
    "P03": "Gumboro",
    "P04": "Coryza",
    "P05": "Kolera Ayam",
}

# Aturan (rule base)
aturan = {
    "P01": ["G01", "G02", "G03"],
    "P02": ["G04", "G05", "G06"],
    "P03": ["G07", "G08", "G09"],
    "P04": ["G10", "G11", "G12"],
    "P05": ["G13", "G14", "G15"],
}


#Forward chaining
def diagnosa(gejala_input):
    hasil = []
    for kode_penyakit, syarat_gejala in aturan.items():
        if all(g in gejala_input for g in syarat_gejala):
            hasil.append(penyakit[kode_penyakit])
    return hasil




# Route untuk halaman utama
@app.route('/diagnosa', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_gejala = request.form.getlist("gejala")
        if selected_gejala:
            hasil_diagnosa = diagnosa(selected_gejala)
        else:
            hasil_diagnosa = []
        return render_template("index.html", gejala=gejala, hasil=hasil_diagnosa)
    
    return render_template("index.html", gejala=gejala, hasil=[])


# Route untuk halaman gejala
@app.route('/gejala', methods=['GET'])
def gejala_page():
    return render_template("gejala.html", gejala=gejala)

# Route untuk halaman penyakit
@app.route('/penyakit', methods=['GET'])
def penyakit_page():
    return render_template("penyakit.html", penyakit=penyakit)

# Route untuk halaman home
@app.route('/', methods=['GET'])
def home_page():
    return render_template("home.html")




penjelasan_gejala = {
    "G01": {
        "deskripsi": "Nafsu makan menurun",
        "penjelasan": "Ayam yang biasanya lahap makan tiba-tiba menjadi tidak tertarik pada makanan adalah tanda awal yang umum dari banyak penyakit. Bisa disebabkan oleh stres, perubahan lingkungan, infeksi bakteri atau virus, bahkan parasit. Jika dibiarkan, penurunan nafsu makan akan menyebabkan tubuh ayam lemah, berat badan turun drastis, dan sistem kekebalan menurun."
    },
    "G02": {
        "deskripsi": "Sayap terkulai",
        "penjelasan": "Sayap yang menggantung lemas menunjukkan adanya gangguan pada otot atau saraf. Ini bisa menjadi gejala penyakit seperti Newcastle Disease atau trauma fisik. Ayam akan tampak lemah, kehilangan koordinasi gerak, dan sering terlihat kesulitan menjaga keseimbangan tubuhnya."
    },
    "G03": {
        "deskripsi": "Diare",
        "penjelasan": "Tinja yang encer, terkadang berlendir atau berdarah, merupakan indikator gangguan pencernaan. Penyebabnya bisa beragam, mulai dari infeksi bakteri (seperti Salmonella), virus (seperti Avian Influenza), hingga cacingan. Diare membuat ayam kehilangan banyak cairan dan elektrolit, yang jika tidak segera ditangani bisa menyebabkan dehidrasi fatal."
    },
    "G04": {
        "deskripsi": "Mata berair",
        "penjelasan": "Air mata yang terus-menerus keluar adalah tanda iritasi atau infeksi. Bisa disebabkan oleh paparan amonia dari kotoran yang menumpuk, debu kandang, atau infeksi saluran pernapasan atas. Jika tidak ditangani, kondisi ini bisa berkembang menjadi infeksi mata yang lebih parah atau bahkan menyebabkan kebutaan."
    },
    "G05": {
        "deskripsi": "Pembengkakan kepala",
        "penjelasan": "Wajah ayam tampak membesar atau bengkak, terutama di sekitar mata dan sinus. Ini bisa disebabkan oleh infeksi bakteri seperti fowl cholera, atau sinusitis kronis. Pembengkakan ini akan menyebabkan gangguan pernapasan, penglihatan terganggu, serta menurunkan kenyamanan ayam secara drastis"
    },
    "G06": {
        "deskripsi": "Keluar lendir dari hidung",
        "penjelasan": "Lendir bening hingga kental yang keluar dari lubang hidung menandakan adanya infeksi pada saluran pernapasan. Penyakit seperti CRD (Chronic Respiratory Disease) atau Infectious Coryza adalah penyebab utamanya. Ayam akan tampak sesak, sering bersin, dan kesulitan bernapas. Jika tidak diobati, infeksi ini bisa menyebar ke bagian tubuh lainnya."
    },
    "G07": {
        "deskripsi": "Bulu kusam dan berdiri",
        "penjelasan": "Bulu ayam tampak tidak rapi, berdiri seperti menggigil, dan kehilangan kilau alaminya. Ini adalah respons tubuh ayam saat demam atau mengalami stres. Bulu berdiri membantu menjaga suhu tubuh saat tubuh mengalami perubahan suhu internal karena infeksi atau gangguan metabolik"
    },
    "G08": {
        "deskripsi": "Kotoran putih encer",
        "penjelasan": "Tinja berwarna putih yang encer bisa menandakan Pullorum Disease, infeksi bakteri serius yang sangat menular. Bisa juga menjadi tanda gangguan ginjal, di mana cairan tubuh tidak terserap sempurna. Gejala ini perlu perhatian khusus karena sering menyerang anak ayam dan bisa menyebabkan kematian massal."
    },
    "G09": {
        "deskripsi": "Lemah dan lesu",
        "penjelasan": "Ayam tampak tidak aktif, lebih sering duduk diam, enggan bergerak, dan terlihat tidak bertenaga. Kondisi ini dapat disebabkan oleh berbagai faktor, seperti infeksi sistemik, kekurangan nutrisi, dehidrasi, atau keracunan. Lemah dan lesu adalah gejala umum tapi serius yang harus segera dicari penyebabnya."
    },
    "G10": {
        "deskripsi": "Bersin",
        "penjelasan": "Ayam yang sering mengeluarkan suara bersin menandakan iritasi pada saluran napas atas. Bersin bisa disebabkan oleh debu, perubahan suhu yang drastis, atau infeksi virus seperti ILT (Infectious Laryngotracheitis). Bersin berulang sering diikuti dengan lendir dan suara napas grok-grok. Jika tidak diobati, bisa menyebabkan infeksi lebih lanjut pada paru-paru."
    },
    "G11": {
        "deskripsi": "Hidung basah dan bengkak",
        "penjelasan": "Aroma busuk yang keluar dari hidung menunjukkan infeksi berat yang menyebabkan pembusukan jaringan, biasanya oleh bakteri anaerob. Gejala ini sering ditemukan pada kasus kronis di mana lendir atau nanah terakumulasi dan tidak dikeluarkan dengan baik, memicu infeksi sekunder yang parah."
    },
    "G12": {
        "deskripsi": "Bau tidak sedap dari hidung",
        "penjelasan": "Aroma busuk yang keluar dari hidung menunjukkan infeksi berat yang menyebabkan pembusukan jaringan, biasanya oleh bakteri anaerob. Gejala ini sering ditemukan pada kasus kronis di mana lendir atau nanah terakumulasi dan tidak dikeluarkan dengan baik, memicu infeksi sekunder yang parah."
    },
    "G13": {
        "deskripsi": "Jengger membiru",
        "penjelasan": "Perubahan warna jengger dari merah cerah menjadi kebiruan menunjukkan kurangnya oksigen dalam darah (sianosis). Ini adalah gejala darurat yang sering terjadi pada penyakit pernapasan berat seperti Avian Influenza atau gagal jantung. Jengger biru harus segera ditindaklanjuti karena bisa berakibat fatal."
    },
    "G14": {
        "deskripsi": "Kematian mendadak",
        "penjelasan": "Ayam yang tiba-tiba mati tanpa gejala berarti sebelumnya adalah tanda penyakit akut dan mematikan seperti Newcastle Disease atau Avian Influenza. Bisa juga disebabkan oleh keracunan pakan atau infeksi bakteri yang sangat cepat berkembang. Deteksi dini dan isolasi sangat penting untuk mencegah penularan."
    },
    "G15": {
        "deskripsi": "Jalan sempoyongan",
        "penjelasan": "Ayam berjalan tidak stabil, tampak seperti kehilangan keseimbangan, atau bahkan terjatuh. Ini menandakan gangguan sistem saraf pusat, bisa karena infeksi seperti Marek’s Disease, keracunan, atau kekurangan vitamin B1 dan B2. Segera pisahkan ayam seperti ini untuk observasi lebih lanjut."
    }
}

@app.route('/penjelasan_gejala/<kode>')
def get_penjelasan_gejala(kode):
    gejala = penjelasan_gejala.get(kode)
    if gejala:
        return jsonify(gejala)
    else:
        return jsonify({"penjelasan": "Gejala tidak ditemukan."}), 404


if __name__ == '__main__':
    app.run(debug=True)







