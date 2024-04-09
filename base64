import pandas as pd
import requests
import base64
import json
from tqdm import tqdm


# base 64
def query_chembl_by_inchikey(inchikey):
    base_url = "https://www.ebi.ac.uk/chembl/interface_api/es_proxy/es_data/get_es_data/"
    query_json = {
        "index_name": "chembl_molecule",
        "es_query": {"size": 24, "_source": ["molecule_chembl_id"], "query": {"bool": {"must": {"bool": {"boost": 1, "must": {"bool": {"must": [], "should": [{"multi_match": {"boost": 10, "fields": ["molecule_structures.standard_inchi_key"], "query": inchikey, "type": "most_fields"}}]}}}}}}}}
    query_string = base64.b64encode(json.dumps(query_json).encode('utf-8')).decode('utf-8')
    request_url = base_url + query_string
    response = requests.get(request_url)
    chembl_ids = []
    if response.status_code == 200:
        data = response.json()
        hits = data.get('es_response', {}).get('hits', {}).get('hits', [])
        for hit in hits:
            chembl_id = hit.get('_source', {}).get('molecule_chembl_id', '')
            chembl_ids.append(chembl_id)
    return chembl_ids

def process_cids_from_excel(file_path, output_file_path):
    df = pd.read_excel(file_path)
    if 'CID' not in df.columns or 'APID' not in df.columns:
        print("The Excel file does not have the required 'CID' or 'APID' columns.")
        return

    results = []

    for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing CIDs"):
        cid = row['CID']
        apid = row['APID']  # Reading APID from the row
        inchikey = fetch_inchikey_by_cid(cid)
        if inchikey:
            chembl_ids = query_chembl_by_inchikey(inchikey)
            for chembl_id in chembl_ids:
                results.append({'CID': cid, 'APID': apid, 'InChIKey': inchikey, 'ChEMBL ID': chembl_id})

    results_df = pd.DataFrame(results)
    results_df.to_excel(output_file_path, index=False)
    print(f"Results have been saved to {output_file_path}")

