from flask import Flask, request
from flask_restful import Resource, Api
from suds.client import Client
import psycopg2
import sys
import json
import time

app = Flask(__name__)
api = Api(app)

connection_string = " host='localhost' dbname='postgres' user='postgres' password='P@ssw0rd'"
psql = psycopg2.connect(connection_string)
cursor = psql.cursor()

class Application(Resource):
    def post(self):
        json_data = request.json

        result = json_data["result"]
        application = json_data["application"]

        #insert to application table
        insert_string = """
              INSERT INTO application VALUES (
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s)
          """
        cursor.execute(insert_string, (\
          result["application_xid"], application["other_income_source"], application["company_phone_number"],
          application["spouse_mobile_phone"], application["employment_status"], application["loan_purpose_desc"], application["kin_gender"], application["mutation"] , \
          application["address_provinsi"], application["kin_dob"], application["dependent"], application["name_in_bank"] , application["home_status"], \
          application["address_kecamatan"], application["gender"], application["mobile_phone_2"], application["marital_status"], application["mobile_phone_1"], \
          application["loan_duration_request"], application["job_type"], application["last_education"], application["job_industry"], application["college"], \
          application["address_kodepos"], application["monthly_housing_cost"] , application["monthly_income"], application["work_kodepos"], application["job_start"], \
          application["payday"], application["address_kelurahan"] , application["job_function"], application["vehicle_ownership_1"] , application["email"], application["loan_amount_request"], \
          application["is_verification_agreed"], application["address_kabupaten"], application["monthly_expenses"], application["bank_account_number"], application["hrd_name"], \
          application["marketing_source"], application["spouse_dob"], application["major"], application["loan_purpose"] , application["instagram_username"] , application["has_whatsapp_2"], \
          application["has_whatsapp_1"], application["gpa"], application["graduation_year"], application["app_version"] , application["bank_name"] , \
          application["twitter_username"], application["number_of_employees"], application["customer"] , application["address_street_num"] , application["ktp"], application["bank_branch"], \
          application["total_current_debt"], application["kin_name"], application["fullname"] , application["landlord_mobile_phone"], application["occupied_since"], application["spouse_name"], \
          application["bbm_pin"], application["is_own_phone"], application["job_description"], application["kin_relationship"] , application["company_name"], application["has_other_income"], \
          application["other_income_amount"], application["position_employees"], application["spouse_has_whatsapp"], application["kin_mobile_phone"], application["is_courtesy_call"], \
          application["billing_office"], application["dob"], application["vehicle_type_1"] , application["company_address"], application["address_type"], application["kkbri"], \
          application["daily_transaction_kkbri" ], application["income_source"], result["status"]))

        if(result["status"] == "approve"):
            loan = json_data["loan"]

            #insert to loan table
            insert_string = """
                  INSERT INTO loan VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )
              """
            cursor.execute(insert_string, (\
                result["application_xid"], loan["loan_disbursement_amount"] , loan["initial_cashback"], \
                loan["loan_duration"], loan["first_installment_amount"], loan["cashback_earned_total"], \
                loan["loan_amount"], loan["installment_amount"]))

            if(json_data.get("eform")):
                eform = json_data["eform"]

                string_json = '{"Nama_Lengkap":"DICKY FIRMANSYAH","Jenis_Kelamin":"","Kewarganegaraan":"","Negara":"","Tempat_Lahir":"","Tanggal_Lahir":"","Nama_Ibu":"","Jenis_Identitas":"KT","Tanggal_Terbit_ID":"","Tanggal_Kadaluarsa_ID":"","No_Identitas":"1234567891234567","Pendidikan":"ZZ","Agama":"","Status_Menikah":"","Hobi":"HOBI","Address_ID":"","KodePos_ID":"","RT_ID":"","RW_ID":"","Kel_ID":"","Kec_ID":"","Kota_ID":"","Propinsi_ID":"","Alamat_Domisili":"","KodePos_Domisili":"","RT_Domisili":"","RW_Domisili":"","Kel_Domisili":"","Kec_Domisili":"","Kota_Domisili":"","Propinsi_Domisili":"","Telepon_Nasabah":"","Fax_Nasabah":"","HP_Nasabah":"","Email_Nasabah":"","Jenis_Pekerjaan":"BUMN","Nama_Kantor":"BRI","Bidang_Pekerjaan":"IT","Tahun_LamaKerja":"5","Bulan_LamaKerja":"01","Jabatan":"STAFF","NPWP":"","Alamat_Kantor":"ALAMAT","KodePos_Kantor":"16425","RT_Kantor":"","RW_Kantor":"","Kel_Kantor":"KUKUSAN KEL","Kec_Kantor":"BEJI","Kota_Kantor":"DEPOK KOT.","Propinsi_Kantor":"JAWA BARAT","TelpNo_Kantor":"","Fax_Kantor":"","Alamat_Surat":"1","Penghasilan_Perbulan":"G1","Kepemilikan_KKBRI":"Y","Transaksi_Harian":"N1","Sumber_Penghasilan":"00011","Tipe_Produk":"SU","QQ_Junio":"","Tujuan_Buka_AccNonDeposit":"T1","Mata_Uang_AccNonDeposit":"IDR","Jenis_Kartu_Accnt":"PRIV","Rek_Koran_Alamat":"","Mobile_Banking":"ON","Internet_Banking":"","Phone_Banking":"","SMS_Notifikasi":"","Limit_Notifikasi":"","Alamat_Email_Notifikasi":"","NomorHP_Fasilitas":"","Setoran":"1000000","Setoran_Terbilang":"SATU JUTA RUPIAH","Mata_Uang_Deposito":"","Pokok_Deposito":"","Pokok_Deposito_Terbilang":"","Jangka_Waktu_Deposito":"","Perpanjangan_Deposito":"","Pembayaran_Bunga_Deposito":"","Nama_Bank_Deposito_Intrs":"","Atas_Nama_Deposito_Intrs":"","Nomor_Rekening_Deposito_Intrs":"","Is_AddrIdSameAddrDom":"ON","Is_Existing_Customer":"N","Nama_Bank_NonBRI1":"","Nama_Bank_NonBRI2":"","Jenis_Rekening_NonBRI1":"","Jenis_Rekening_NonBRI2":"","Penerbit_CCNonBRI1":"","Penerbit_CCNonBRI2":"","Tipe_CCNonBRI1":"","Tipe_CCNonBRI2":"","Punya_CCBRI":"","Term_and_Condition":"1","Customer_Agreement":"1","Mata_Uang_Setoran":"IDR","Setoran_Deposito":"","Referral":"","Nama_PE":"","Code_PE":"","SID":"","Sub_rek_efek":"","Email_Nasabah_Rdn":"","Nama_Uker":"3251;UNIT JAGAKARSA CINERE","link_edit":"EFORM_SIMPEDES\/EDIT_FORM_DATA_PRIBADI_SIMPEDES_NEW"}'

                url="http://10.35.65.18/formless/public/transactionws?wsdl"
                client = Client(url)

                result_soap = client.service.sendTransaction(transactionObject=string_json)
                #result_json = json.loads(result_soap)

                return { "response" : 200, "status" : "ok", "voucher" : "DH23UQ", "application_xid" : result["application_xid"], "date" : time.strftime("%Y-%m-%d %H:%M:%S")}
            else:
                return {"response" : 200, "status" : "ok"}
        psql.commit()
    def get(self):
        return {"response" : "Hello World"}

api.add_resource(Application, '/addApp')

if __name__ == "__main__":
    app.run(port=80, host="172.18.41.154")
