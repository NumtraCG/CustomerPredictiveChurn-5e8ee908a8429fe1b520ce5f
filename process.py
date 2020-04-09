import json
import Connectors
import Transformations
import AutoML
try:
    CustomerPredictiveChurn_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e8ee908a8429fe1b520ce60", spark, "{'url': '/Demo/PredictiveChurnTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib3c8e0614707f7e6d2addea6ce7c33d0', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    CustomerPredictiveChurn_AutoFE = Transformations.TransformationMain.run(["5e8ee908a8429fe1b520ce60"], {"5e8ee908a8429fe1b520ce60": CustomerPredictiveChurn_DBFS}, "5e8ee908a8429fe1b520ce61", spark, json.dumps({"FE": [{"transformationsData": {"feature_label": "State"}, "feature": "State", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1902", "mean": "", "stddev": "", "min": "AK", "max": "WY", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Account_Length", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "102.02", "stddev": "39.95", "min": "1", "max": "232", "missing": "0"}}, {"transformationsData": {}, "feature": "Area_Code", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "435.91", "stddev": "41.72", "min": "408", "max": "510", "missing": "0"}}, {"transformationsData": {"feature_label": "Phone"}, "feature": "Phone", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1902", "mean": "", "stddev": "", "min": "327-3053", "max": "422-8344", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Intl_Plan"}, "feature": "Intl_Plan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1902", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "VMail_Plan"}, "feature": "VMail_Plan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1902", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "VMail_Message", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "8.04", "stddev": "13.61", "min": "0", "max": "51", "missing": "0"}}, {"transformationsData": {}, "feature": "Day_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "178.38", "stddev": "54.77", "min": "2.6", "max": "346.8", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Day_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "100.2", "stddev": "20.35", "min": "36", "max": "165", "missing": "0"}}, {"transformationsData": {}, "feature": "Day_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "30.33", "stddev": "9.31", "min": "0.44", "max": "58.96", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Eve_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "201.35", "stddev": "51.02", "min": "0.0", "max": "354.2", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Eve_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "99.89", "stddev": "20.42", "min": "0", "max": "170", "missing": "0"}}, {"transformationsData": {}, "feature": "Eve_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "17.12", "stddev": "4.34", "min": "0.0", "max": "30.11", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Night_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "201.65", "stddev": "51.49", "min": "43.7", "max": "395.0", "missing": "0"}, "transformation": ""}, {
                                                                            "transformationsData": {}, "feature": "Night_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "100.0", "stddev": "19.72", "min": "33", "max": "175", "missing": "0"}}, {"transformationsData": {}, "feature": "Night_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "9.07", "stddev": "2.32", "min": "1.97", "max": "17.77", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Intl_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "10.29", "stddev": "2.76", "min": "0.0", "max": "20.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "total_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "591.68", "stddev": "90.44", "min": "284.3", "max": "885.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Intl_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "4.47", "stddev": "2.44", "min": "0", "max": "19", "missing": "0"}}, {"transformationsData": {}, "feature": "Intl_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "2.78", "stddev": "0.75", "min": "0.0", "max": "5.4", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Total_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1902", "mean": "59.29", "stddev": "10.5", "min": "23.25", "max": "96.15", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "CustServ_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "1.55", "stddev": "1.34", "min": "0", "max": "9", "missing": "0"}}, {"transformationsData": {}, "feature": "Churn", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1902", "mean": "0.13", "stddev": "0.34", "min": "0", "max": "1", "missing": "0"}}, {"transformationsData": {"feature_label": "cluster_labels"}, "feature": "cluster_labels", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1902", "mean": "", "stddev": "", "min": "day_callers", "max": "vmailers", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "State_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "1902", "mean": "22.05", "stddev": "14.32", "min": "0.0", "max": "50.0", "missing": "0"}}, {"feature": "Phone_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "1902", "mean": "950.5", "stddev": "549.2", "min": "0.0", "max": "1901.0", "missing": "0"}}, {"feature": "Intl_Plan_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1902", "mean": "0.1", "stddev": "0.3", "min": "0", "max": "1", "missing": "0"}}, {"feature": "VMail_Plan_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1902", "mean": "0.28", "stddev": "0.45", "min": "0", "max": "1", "missing": "0"}}, {"feature": "cluster_labels_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "1902", "mean": "2.35", "stddev": "1.7", "min": "0.0", "max": "5.0", "missing": "0"}}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(CustomerPredictiveChurn_AutoFE, ["State", "Account_Length", "Area_Code", "Phone", "Intl_Plan", "VMail_Plan", "VMail_Message", "Day_Mins", "Day_Calls", "Day_Charge", "Eve_Mins",
                                                                   "Eve_Calls", "Eve_Charge", "Night_Mins", "Night_Calls", "Night_Charge", "Intl_Mins", "total_Mins", "Intl_Calls", "Intl_Charge", "Total_Charge", "CustServ_Calls", "cluster_labels"], "Churn")

except Exception as ex:
    print(ex)
