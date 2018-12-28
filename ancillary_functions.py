def ricerchina(sse, doi_to_search):
    for dict in sse.data:
        if doi_to_search == dict["doi"]:
            return dict

def ricerchina2(data, doi_to_search):
    for dict in data:
        if doi_to_search == dict["doi"]:
            return dict
