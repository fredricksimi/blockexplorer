from django.shortcuts import render
from web3 import Web3 
from datetime import datetime
from django.http import JsonResponse
from decouple import config

def home_view(request):
    return render(request, 'mainapp/index.html')

def blocks_view(request):
    provider = config('PROVIDER')
    w3 = Web3(Web3.HTTPProvider(provider))
    latest_block = w3.eth.block_number
    Txns = []
    for blck in range(0, 21):
        block = w3.eth.get_block(latest_block - blck)
        blockitem = {
            "number" : block['number'],
            "the_hash" : block['hash'].hex() ,
            "the_time" : block['timestamp'],
            "the_gas" : block['gasUsed'],
            "converted_time" : datetime.fromtimestamp(int(block['timestamp'])).strftime('%Y-%m-%d %H:%M:%S') 
        }
        Txns.append(blockitem)
    return JsonResponse(Txns, safe=False)