## WirelessCoexManager

> `/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager`

```diff

-1870.6.1.0.0
-  __TEXT.__text: 0xa8ec
-  __TEXT.__auth_stubs: 0x5d0
+1930.3.0.0.0
+  __TEXT.__text: 0xa950
   __TEXT.__objc_methlist: 0x678
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x250
-  __TEXT.__cstring: 0x1974
+  __TEXT.__gcc_except_tab: 0x25c
+  __TEXT.__cstring: 0x1982
   __TEXT.__oslogstring: 0x6e5
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x126c
-  __TEXT.__objc_methtype: 0x264
-  __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x700
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x420
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0xda8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x30
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3B0F109-4A4A-36B7-AFB9-DFFACCE59036
+  UUID: 7B5BC4B1-CB90-3595-B988-9DB41EC91CF7
   Functions: 210
-  Symbols:   771
-  CStrings:  661
+  Symbols:   772
+  CStrings:  397
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_release_x10
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"<WCMClientCallback>\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSUUID\""
- "@\"WRM_iRATProximityRecommendationLogging\""
- "@16@0:8"
- "@24@0:8@?16"
- "@24@0:8^?16"
- "@36@0:8i16@20@28"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "BWEstimation"
- "FaceTime"
- "IDS"
- "Q"
- "Q16@0:8"
- "RecommendationType"
- "T@\"NSUUID\",&,N,V_Uuid"
- "T@\"WRM_iRATProximityRecommendationLogging\",&,N,V_metrics"
- "TB,N,V_linkIsRecommended"
- "TB,N,V_linkRecommendationIsValid"
- "TQ,N,V_btRSSI"
- "Tc,N,V_nwType"
- "Ti,N,V_RecommendationType"
- "Ti,N,V_beaconPER"
- "Tq,N,V_btRetransmissionRateRx"
- "Tq,N,V_btRetransmissionRateTx"
- "Tq,N,V_btTech"
- "Tq,N,V_expectedThroughputVIBE"
- "Tq,N,V_lsmRecommendationBe"
- "Tq,N,V_packetLifetimeVIBE"
- "Tq,N,V_packetLossRateVIBE"
- "Tq,N,V_wifiCCA"
- "Tq,N,V_wifiRSSI"
- "Tq,N,V_wifiSNR"
- "UTF8String"
- "Uuid"
- "WCMAvailable"
- "WCMClientProxy"
- "WCMSetting"
- "WRMBasebandMetricsInterface"
- "WRMClientInterface"
- "WRM_UCMInterface"
- "WRM_iRATInterface"
- "WRM_iRATProximityRecommendation"
- "WRM_iRATProximityRecommendationLogging"
- "^?"
- "_RecommendationType"
- "_Uuid"
- "_beaconPER"
- "_btRSSI"
- "_btRetransmissionRateRx"
- "_btRetransmissionRateTx"
- "_btTech"
- "_expectedThroughputVIBE"
- "_expediteBBAssertionBGAppActive_sync:handler:"
- "_linkIsRecommended"
- "_linkRecommendationIsValid"
- "_lsmRecommendationBe"
- "_metrics"
- "_nwType"
- "_packetLifetimeVIBE"
- "_packetLossRateVIBE"
- "_wifiCCA"
- "_wifiRSSI"
- "_wifiSNR"
- "addAppType:"
- "addObject:"
- "addProximityLinkRecommendationType:"
- "assertCommCenterBaseBand:"
- "assertCommCenterBaseBandMode:"
- "beaconPER"
- "btRSSI"
- "btRetransmissionRateRx"
- "btRetransmissionRateTx"
- "btTech"
- "c"
- "c16@0:8"
- "checkConnection:"
- "connectToServer"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataMetricsHandler"
- "dealloc"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateKeysAndObjectsUsingBlock:"
- "expectedThroughputVIBE"
- "expediteBBAssertionBGAppActive:handler:"
- "expediteCellularForReason:reason:"
- "getCellularDataMetrics:"
- "getInstantLoad"
- "getLinkRecommendationMetrics:"
- "getMLPredictedThroughput:options:"
- "getNRPhyMetrics:"
- "getProximityLinkRecommendation:recommendation:"
- "getQSHMetrics:"
- "getStatusUpdateMessageType:"
- "getStreamingInfo:linkType:"
- "getSubscribeMessageType:"
- "getValue:"
- "getVoiceLqmValue:completionHandler:"
- "getWiFiBWEstimationMetrics:"
- "getWirelessFrequencyBandUpdatesForMIC:"
- "getWirelessRadioManagerReportLoad:loadDuration:callback:"
- "getWirelessULFrequencyBandUpdates:"
- "handleNotification::"
- "i16@0:8"
- "i20@0:8i16"
- "i24@0:8d16"
- "init"
- "initWithClientProcessId:delegate:dispatch:"
- "initWithObjectsAndKeys:"
- "intValue"
- "linkIsRecommended"
- "linkRecommendationIsValid"
- "lsmRecommendationBe"
- "mAppLists"
- "mBBAssertionBGAppActive"
- "mBtConnectedLinksObserver"
- "mClientSupportsMultipleAppTypes"
- "mConnection"
- "mDelegate"
- "mGetLinkRecommendationMetricsHandler"
- "mGetLinkRecommendationMetricsHandlerEnabled"
- "mHomeKitBTLoadFunctionPointer"
- "mIsAwdlEnabled"
- "mIsNanEnabled"
- "mIsNanRealTimeEnabled"
- "mIsRegistered"
- "mLinkPreferenceSubscriptionEnabled"
- "mLocationAssertionEnabled"
- "mLocationState"
- "mLowPowerModePeriodicWakeUpCb"
- "mNRFrequencyUpdateForMicFuncPtr"
- "mNotificationBlock"
- "mObserver"
- "mOppBtLQMObserver"
- "mOppModeObserver"
- "mProcessId"
- "mProximityGetLinkRecommendationEnabled"
- "mProximityGetLinkRecommendationHandler"
- "mProximityLinkRecommendationList"
- "mProximitySubscribeLinkRecommendationEnabled"
- "mProximitySubscribeLinkRecommendationHandler"
- "mQueue"
- "mTelephoneAssertionEnabled"
- "mTelephonyStateEnabled"
- "mULFrequencyUpdatesObserver"
- "mVoiceLqmCb"
- "mVoiceLqmCbEnabled"
- "metrics"
- "metricsHandler"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "nwType"
- "objectAtIndex:"
- "objectForKey:"
- "packetLifetimeVIBE"
- "packetLossRateVIBE"
- "processBTConnectedLinksNotification:"
- "processBTLQMNotification:"
- "processMetricsNotificationReport:"
- "processNotificationList::"
- "processNotificationListForTerminus:"
- "processOperatingModeNotification:"
- "processVoiceLqmNotification:"
- "processWRMCellDataMetrics:"
- "processWRMNrPhyMetrics:"
- "processWRMWiFiBWEstMetrics:"
- "q"
- "q16@0:8"
- "q36@0:8i16d20^?28"
- "reConnect"
- "receiveMessage:argument:"
- "registerClient:queue:"
- "registerClient:queue:notificationHandler:"
- "registerServices:"
- "registerToServer"
- "removeAllObjects"
- "removeAppType:"
- "removeObject:"
- "removeProximityLinkRecommendationType:"
- "sendBtLoad:"
- "sendMessage:argument:"
- "sendNRFrequencyUpdateForMic:"
- "sendULFrequencyUpdate:"
- "setAWDLEnabled:"
- "setBeaconPER:"
- "setBtRSSI:"
- "setBtRetransmissionRateRx:"
- "setBtRetransmissionRateTx:"
- "setBtTech:"
- "setCriticalAirPlayEnabled:estimatedDuration:criticalityPercentage:"
- "setExpectedThroughputVIBE:"
- "setLinkIsRecommended:"
- "setLinkRecommendationIsValid:"
- "setLsmRecommendationBe:"
- "setMetrics:"
- "setNANEnabled:"
- "setNANRealTimeEnabled:"
- "setNwType:"
- "setObject:forKeyedSubscript:"
- "setPacketLifetimeVIBE:"
- "setPacketLossRateVIBE:"
- "setRecommendationType:"
- "setTelephonyEnabled:"
- "setUuid:"
- "setWifiCCA:"
- "setWifiRSSI:"
- "setWifiSNR:"
- "startTimer:"
- "statusUpdateAppLinkPreference:status:"
- "statusUpdateAppType:linkType:serviceStatus:"
- "stopTimer"
- "subscribeAppType:observer:"
- "subscribeBtConnectedLinksNotification:"
- "subscribeBtLqmScoreNotification:"
- "subscribeDataLinkRecommendation:"
- "subscribeLowPowerModePeriodicWakeupNotification:"
- "subscribeMultipleAppTypes:observer:"
- "subscribeOperatingModeChangeNotification:"
- "subscribeProximityLinkRecommendation:"
- "subscribeStandaloneLinkRecommendation:"
- "subscribeVoiceLqmNotification:"
- "unregisterClient"
- "unregisterClientWithNotificationBlockRelease"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8c16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8i16B20"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8@?16i24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16I20S24"
- "v28@0:8i16@20"
- "v28@0:8i16i20B24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@?16@24"
- "v32@0:8q16@?24"
- "v36@0:8i16@20@?28"
- "v40@0:8{?=iiii}16@?32"
- "valueWithBytes:objCType:"
- "wifiCCA"
- "wifiMetricsHandler"
- "wifiRSSI"
- "wifiSNR"

```
