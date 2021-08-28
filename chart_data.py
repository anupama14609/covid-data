import pandas as pd 
import numpy as np 

def index():
    df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    uniqueCountryNames=pd.unique(confirmedGlobal['Country/Region'])
    contryNames,countsVal,logVals,overallCount,dataForMapGraph,maxVal=getBarData(confirmedGlobal,uniqueCountryNames)
    dataForheatMap,dateCat=getHeatMapData(confirmedGlobal,contryNames)
    datasetForLine,axisvalues=getLinebarGroupData(confirmedGlobal,uniqueCountryNames)
    context={'dateCat':dateCat,'dataForheatMap':dataForheatMap,'maxVal':maxVal,
    'dataForMapGraph':dataForMapGraph,'axisvalues':axisvalues,
    'datasetForLine':datasetForLine,'uniqueCountryNames':uniqueCountryNames,
    'contryNames':contryNames,'countsVal':countsVal,'logVals':logVals,
    'overallCount':overallCount}
    print(context)


def getBarData(confirmedGlobal,uniqueCountryNames):
    df2=confirmedGlobal[list(confirmedGlobal.columns[1:2])+list([confirmedGlobal.columns[-2]])]
    df2.columns=['Country/Region','values']
    df2=df2.sort_values(by='values',ascending=False)
    contryNames=list(df2['Country/Region'].values)
    countsVal=list(df2['values'].values)
    maxVal=max(countsVal)
    overallCount=sum(countsVal)
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal )
    dataForMapGraph=getDataforMap(uniqueCountryNames,df2)

    return (contryNames,countsVal,logVals,overallCount,dataForMapGraph,maxVal)

def getLinebarGroupData(confirmedGlobal,uniqueCountryNames):
    colNames=confirmedGlobal.columns[4:-1]
    datasetsForLine=[]
    for i in uniqueCountryNames:
        temp={}
        temp['label']=i
        temp['fill']='false'
        temp['data']=confirmedGlobal[confirmedGlobal['Country/Region']==i][colNames].sum().values.tolist()
        datasetsForLine.append(temp)
    return datasetsForLine,list(range(len(colNames)))

def getHeatMapData(confirmedGlobal,contryNames):
    df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    df3=confirmedGlobal[list(confirmedGlobal.columns[1:2])+list(list(confirmedGlobal.columns.values)[-6:-1])]
    dataForheatMap=[]
    for i in contryNames:
        try:
            tempdf=df3[df3['Country/Region']==i]
            temp={}
            temp["name"]=i
            temp["data"]=[{'x':j,'y':k} for j,k in zip(tempdf[tempdf.columns[1:]].sum().index,tempdf[tempdf.columns[1:]].sum().values)]
            dataForheatMap.append(temp)
        except:
            pass
    dateCat=list(list(confirmedGlobal.columns.values)[-6:-1])
    return dataForheatMap,dateCat

def getDataforMap(uniqueCOuntryName,df2):
    df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    dataForMap=[]
    for i in uniqueCOuntryName:
        try:
            tempdf=df3[df3['name']==i]
            temp={}
            temp["code3"]=list(tempdf['code3'].values)[0]
            temp["name"]=i
            temp["value"]=df2[df2['Country/Region']==i]['values'].sum()
            temp["code"]=list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass
    print (len(dataForMap))
    return dataForMap 

def drillDownACountry(request):
    pass 

index()

