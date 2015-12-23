# coding=utf-8
import os
import tarfile

# Маппинг методов на модуль
moduleMethodMap = {"SyncService": ['updateEntity', 'selfcareSync'],
                   'AbonentOperations': ['getAbonentIdByLogin', 'createAgreementWithDevice', 'registerDevice',
                                         'personifyDevice', 'getDealerDevices', 'getDealerAgreements', 'getDevices',
                                         'getAbonentHierarchyForSelfCare', 'getDeviceRegistrationState',
                                         'actualizeAbonentData', 'getActualizedData', 'getRegistrationData',
                                         'updateAbonentScState', 'changeDevice', 'getDealerDeviceCount',
                                         'getDeviceChangeHistory', 'changeRegData'],
                   'ApplicationOperations': ['getDealerApplication', 'getDealerApplications', 'acceptApplication',
                                             'updateApplicationPlanDate', 'rejectApplication',
                                             'closeApplicationWithoutRegistration', 'createApplication',
                                             'getTradeInApplicationForDevice', 'getDeliveryPointsBySettlement',
                                             'getCourierDeliveryPosibility'],
                   'BillingOperations': ['getBalance', 'getBalanceEx', 'getFinancialOperations', 'getServices',
                                         'getStartTariff', 'cashTransfer', 'setServiceTariff',
                                         'getCreditInformation', 'getServiceBasket'],
                   'CampaignOperations': ['getAbonentAvailableCampaigns', 'addAbonentToCampaign',
                                          'getDealerCampaigns', 'getCampaignDetail', 'getCampaigns'],
                   'CASOperations': ['checkSendPossibility', 'sendCommand'],
                   'DetailedInformation': ['getDealerDetail'], 'InformingOperations': ['sendEvent'],
                   'PartnerOperations': ['updateDealer', 'getDealerHouseOwnerObjects', 'getDealerAgentAgreements',
                                         'getDealerStatistic', 'updateDealerPublicData', 'createHouseOwnerObject',
                                         'getHoaOnConfirmationCount', 'getDealerPublicData', 'getDealerRating',
                                         'increaseDeviceView'], 'PaymentOperations': ['payServiceBasket'],
                   'ReportOperations': ['createReport', 'getReport', 'getReportList'],
                   'ValidationOperations': ['checkRegistrationPossibility', 'checkDeviceForTradeIn',
                                            'getCompatibleDeviceModels'],
                   'VoucherOperations': ['activateScratchCard', 'activatePINCode']
                   }
# Список маппинга метода на паттерн
pattern = {'updateEntity': '"Set update entity queue:"', 'selfcareSync': 'Mark entity for sync to selfcare:',
           'getAbonentIdByLogin': 'GetAbonentIdByLogin:', 'createAgreementWithDevice': 'CreateAgreementWithDevice:',
           'registerDevice': "RegisterDevice:", 'personifyDevice': "PersonifyDevice:",
           'getDealerDevices': "GetDealerDevices:", 'getDealerAgreements': "GetDealerAgreements:",
           'getDevices': "GetDevices:", 'getAbonentHierarchyForSelfCare': "GetAbonentHierarchyForSelfCare:",
           'getDeviceRegistrationState': "GetDeviceRegistrationState:",
           'actualizeAbonentData': "ActualizeAbonentData:", 'getActualizedData': "GetActualizedData:",
           'getRegistrationData': "GetRegistrationData:", 'updateAbonentScState': "UpdateAbonentScState:",
           'changeDevice': "ChangeDevice:", 'getDealerDeviceCount': "GetDealerDeviceCount:",
           'getDeviceChangeHistory': "GetDeviceChangeHistory:", 'changeRegData': "СhangeRegData:",
           'getDealerApplication': "GetDealerApplication:", 'getDealerApplications': "GetDealerApplications:",
           'acceptApplication': "AcceptApplication:", 'updateApplicationPlanDate': "UpdateApplicationPlanDate:",
           'rejectApplication': "RejectApplication:",
           'closeApplicationWithoutRegistration': "CloseApplicationWithoutRegistration:",
           'createApplication': "CreateApplication:",
           'getTradeInApplicationForDevice': "GetTradeInApplicationForDevice:",
           'getDeliveryPointsBySettlement': "GetDeliveryPointsBySettlement:",
           'getCourierDeliveryPosibility': "GetCourierDeliveryPosibility:",
           'getBalance': "GetBalance:", 'getBalanceEx': "GetBalanceEx:",
           'getFinancialOperations': "GetFinancialOperations:",
           'getServices': "GetServices:", 'getStartTariff': "GetStartTariff:", 'cashTransfer': "CashTransfer:",
           'setServiceTariff': "SetServiceTariff:", 'getCreditInformation': "GetCreditInformation:",
           'getServiceBasket': "GetServiceBasket:", 'getAbonentAvailableCampaigns': "GetAbonentAvailableCampaigns:",
           'addAbonentToCampaign': "AddAbonentToCampaign:", 'getDealerCampaigns': "GetDealerCampaigns:",
           'getCampaignDetail': "GetCampaignDetail:", 'getCampaigns': "GetCampaigns:",
           'checkSendPossibility': "Check for send command for", 'sendCommand': "Send command for",
           'getDealerDetail': "Get dealer information", 'sendEvent': "Request:", 'updateDealer': "UpdateDealer:",
           'getDealerHouseOwnerObjects': "GetDealerHouseOwnerObjects:",
           'getDealerAgentAgreements': "GetDealerAgentAgreements:",
           'getDealerStatistic': "GetDealerStatistic:", 'updateDealerPublicData': "UpdateDealerPublicData:",
           'createHouseOwnerObject': "CreateHouseOwnerObject:",
           'getHoaOnConfirmationCount': "GetHoaOnConfirmationCount:",
           'getDealerPublicData': "GetDealerPublicData:", 'getDealerRating': "GetDealerRating:",
           'increaseDeviceView': "IncreaseDeviceView:", 'payServiceBasket': "PayServiceBasket:",
           'createReport': "CreateReport:", 'getReport': "GetReport:", 'getReportList': "GetReportList:",
           'checkRegistrationPossibility': "CheckRegistrationPossibility:",
           'checkDeviceForTradeIn': "CheckDeviceForTradeIn:",
           'getCompatibleDeviceModels': "GetCompatibleDeviceModels:", 'activateScratchCard': "ActivateScratchCard:",
           'activatePINCode': "ActivatePINCode"
           }
# Статистика
stat = {}
count = {}
avrstat = {}
listarch = os.listdir(os.curdir)
for arch in listarch:
    if '.tar.gz' in arch:
        print arch
        tar = tarfile.open(name=arch, mode='r|gz')
        file = tar.extractfile(tar.next())
        for line in file.readlines():
            for method in pattern.keys():
                if line.find(pattern.get(method)) != -1:
                    if method not in stat.keys():
                        stat[method] = {}
                    stat[method][line[:16]] = stat[method].get(line[:16], 0) + 1
        file.close()
        tar.close()
for method in stat.keys():
    count = 0
    for date in stat[method].keys():
        count += stat[method][date]
    avrstat[method] = float(count) / len(stat[method].keys())
for module in moduleMethodMap.keys():
    print module
    for method in moduleMethodMap.get(module):
        print '\t' + method + ": " + str(avrstat.get(method, 0))
