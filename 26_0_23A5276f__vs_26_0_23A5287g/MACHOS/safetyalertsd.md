## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.19.0.0
-  __TEXT.__text: 0xd11b8
+64.0.21.0.0
+  __TEXT.__text: 0xd1b7c
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_stubs: 0x2de0
+  __TEXT.__objc_stubs: 0x2dc0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa84
-  __TEXT.__const: 0x9b8c
-  __TEXT.__gcc_except_tab: 0xc5b4
-  __TEXT.__cstring: 0x51db
-  __TEXT.__oslogstring: 0x33c59
+  __TEXT.__const: 0x9bd8
+  __TEXT.__gcc_except_tab: 0xc548
+  __TEXT.__cstring: 0x5009
+  __TEXT.__oslogstring: 0x340aa
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x36bd
-  __TEXT.__objc_methtype: 0x1936
+  __TEXT.__objc_methname: 0x369c
+  __TEXT.__objc_methtype: 0x1939
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x3bc8
+  __TEXT.__unwind_info: 0x3c88
   __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7f08
-  __DATA_CONST.__cfstring: 0x57c0
+  __DATA_CONST.__const: 0x8118
+  __DATA_CONST.__cfstring: 0x5660
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1160
-  __DATA.__objc_selrefs: 0xfe0
+  __DATA.__objc_selrefs: 0xfd8
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x430
-  __DATA.__bss: 0x5f0
+  __DATA.__bss: 0x530
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A76E251C-F9D2-391A-8B26-E96801DBD078
-  Functions: 3191
+  UUID: 8C6AD06A-A86D-3951-86CC-F195E313962A
+  Functions: 3241
   Symbols:   428
-  CStrings:  4374
+  CStrings:  4353
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSMutableSet
CStrings:
+ ","
+ "REGULATORY_TEST"
+ "T^{SACoreLocation=^^?@},V_clProxy"
+ "^{SACoreLocation=^^?@}"
+ "^{SACoreLocation=^^?@}16@0:8"
+ "arrayWithArray:"
+ "countrySupport"
+ "motionHarvestToggles"
+ "noCountry"
+ "senderId"
+ "v24@0:8^{SACoreLocation=^^?@}16"
+ "validateSenderId"
+ "weaTexts"
+ "{\"msg%{public}.0s\":\"#asset,#igneous,log\", \"FollowUpMessageValidTime\":\"%{private}0.3f\", \"watchHysteresis\":\"%{private}0.3f\", \"PhoneHysteresis\":\"%{private}0.3f\", \"IgnoreDuration\":\"%{private}0.3f\", \"TimeBetweenAlerts\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#asset,#igneous,sourceConfigSenderIdInvalid\"}"
+ "{\"msg%{public}.0s\":\"#asset,init\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,assetCountryName\", \"countryName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#assetConfig,currentCountryAssetConfig\", \"currentCountryAssetKey\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#assetConfig,currentCountryAssetConfig,config not found\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,getIgneousOffsetsForRegion\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,getSupportedAlertTypesForCountry\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,log\", \"supportedCountries\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#assetConfig,onAssetReceived\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#assetConfig,onAssetReceived,adding config\", \"countryName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#assetConfig,onAssetReceived,asset nil\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,onAssetReceived,invalid country\", \"countryNameId\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#assetConfig,onAssetReceived,invalid countryAsset\", \"countryAssetId\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#chsel,Safety Alerts init timedout\", \"timeout\":%{public}d, \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"isMobileAssetEnabled\":%{public}hhd, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,state\", \"isEnabled\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"inCoverageRegion\":%{private}hhd, \"isInCountry\":%{private}hhd, \"emergencyAlert\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,onAssetReceived\", \"geoChannelMapsSize\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,Voters\", \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"channelMapsSize\":%{private}d, \"isParticipating\":%{public, location:escape_only}s, \"isPhone\":%{private}d, \"isWatch\":%{private}d, \"forceOrDeferChannelUpdate\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,states\", \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#countryAsset,init\", \"fPullServerName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,#warning,readAPNConfigAsset,nilAssetDictionary\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,#warning,readAPNConfigAsset,nilConfig\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getEarthquakeSensingConfig\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getGeoChannelMaps,asset not defined\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getRollingMetrics\", \"rmSupported\":%{public}d, \"rollingPeriodSeconds\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getRollingMetrics\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,log\", \"pullpc\":%{private}d, \"appc\":%{private}d, \"efficacyParticipationPercentage\":%{private}d, \"wowControls\":%{private}d, \"pullCname\":%{private, location:escape_only}s, \"efficacyManifestFileName\":%{private, location:escape_only}s, \"codebookFileName\":%{private, location:escape_only}s, \"countrySupport\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,onAssetReceived\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readEqSensingAsset\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readEqSensingAsset\", \"toggles\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readEqSensingAsset,nil asset dictionary\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readEqSensingAsset,nil config\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readEqSensingAsset,nil eqSensing dictionary\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readMapCacheAsset,cacheRadiiKmNil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readMapCacheAsset,configIsNil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readMapCacheAsset,mapConfigNil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset\", \"efficacyManifestFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset\", \"metricPeriod\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset\", \"metrics\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset\", \"metricsData\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset\", \"rmSupport\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset,nilAssetDictionary\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readRollingMetricAsset,nilConfig\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,onAssetReceived\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggles\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#daemon,onAssetReceived\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onAssetReceived,country not known\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onCountryChangeCb\"}"
+ "{\"msg%{public}.0s\":\"#daemon,processPendingAlerts\", \"remainingInit\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport\", \"countrySupportStr\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport\", \"motionHarvestAvailable\":%{private}hhd, \"motionHarvestAllowed\":%{private}hhd, \"improveSafety\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport\"}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport,country not known\"}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport,country supported\"}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport,motion harvest only supported\"}"
+ "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport,not supported\", \"countrySupportStr\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#dbg,#countryAssetConfig,readAPNConfigAsset\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ehmd,int\", \"manifestDownloadPeriod\":%{private}d, \"manifestFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFailSafe\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"featuresSize\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"featuresSize\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"index\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"properties\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,asset nil\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,channelConfigIdObjectFailed\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,channelIdObjectFailed\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,elementIsNotDictionary\", \"index\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,feature\", \"feature\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,geometryFailed\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,invalid_features\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,noFeatureInAsset\"}"
+ "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,propertiesIdObjectFailed\"}"
+ "{\"msg%{public}.0s\":\"#ignalert,getFollowUpAlertNotificationContent,source config not found\"}"
+ "{\"msg%{public}.0s\":\"#igv,validateSenderId,not internal install\"}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,invalidFilename\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,setDownloadParameters,empty file name\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,setDownloadParameters,negative download period\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,start,empty file name\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,start,empty identifier\"}"
+ "{\"msg%{public}.0s\":\"#md,start,negative download period\", \"id\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,updateBgSysTask\"}"
+ "{\"msg%{public}.0s\":\"#mobileAsset,onAssetReceived\"}"
+ "{\"msg%{public}.0s\":\"#reg,fetchInfoForLocationReply\", \"config\":%{private, location:escape_only}@, \"info\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#reg,fetchInfoForLocationReply,onError\", \"config\":%{private, location:escape_only}@, \"info\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#reg,getCountryForLocation\"}"
+ "{\"msg%{public}.0s\":\"#reg,init\"}"
+ "{\"msg%{public}.0s\":\"#reg,updateCountryName\"}"
+ "{\"msg%{public}.0s\":\"#regTest,int\"}"
+ "{\"msg%{public}.0s\":\"#saanalytics,onAssetReceived\"}"
+ "{\"msg%{public}.0s\":\"not internal device\", \"alertLevel\":%{private, location:escape_only}s, \"purpose\":%{private, location:escape_only}s, \"class\":%{private, location:escape_only}s, \"function\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"interface\":%{private}d, \"transport\":%{private}d, \"ingressToServerTime\":\"%{private}.3f\", \"egressFromSourceTime\":\"%{private}.3f\", \"eventOriginTime\":\"%{private}.3f\", \"effectiveTime\":\"%{private}.3f\", \"expiryTime\":\"%{private}.3f\", \"advTime\":\"%{private}.3f\"}"
+ "{\"msg%{public}.0s\":\"sender id invalid\", \"alertLevel\":%{private, location:escape_only}s, \"purpose\":%{private, location:escape_only}s, \"class\":%{private, location:escape_only}s, \"function\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"interface\":%{private}d, \"transport\":%{private}d, \"ingressToServerTime\":\"%{private}.3f\", \"egressFromSourceTime\":\"%{private}.3f\", \"eventOriginTime\":\"%{private}.3f\", \"effectiveTime\":\"%{private}.3f\", \"expiryTime\":\"%{private}.3f\", \"advTime\":\"%{private}.3f\"}"
+ "{\"msg%{public}.0s\":\"senderId not found in sourceConfig\", \"alertLevel\":%{private, location:escape_only}s, \"purpose\":%{private, location:escape_only}s, \"class\":%{private, location:escape_only}s, \"function\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"interface\":%{private}d, \"transport\":%{private}d, \"ingressToServerTime\":\"%{private}.3f\", \"egressFromSourceTime\":\"%{private}.3f\", \"eventOriginTime\":\"%{private}.3f\", \"effectiveTime\":\"%{private}.3f\", \"expiryTime\":\"%{private}.3f\", \"advTime\":\"%{private}.3f\", \"senderId\":%{private}d}"
- "APPLE SAFETY ALERTS LIVABILITY TEST:"
- "C03869AF-71E2-47B7-88A6-4285CA380272"
- "Earthquake Detected! Drop, Cover, Hold On. Protect Yourself. -USGS ShakeAlert"
- "FollowUpSourceString"
- "JPN"
- "PerformanceTestSourceString"
- "Procedente de USGS Shakealerts"
- "SourceString"
- "Sourced from USGS Shakealerts"
- "T^{SACoreLocation=^^?},V_clProxy"
- "Terremoto detectado! Agachese, cubrase, sujetese. Protejase. -USGS ShakeAlert"
- "ThresholdMMI"
- "ThresholdMagnitude"
- "USA"
- "USGSFollowUp"
- "USGSTest"
- "USGSType"
- "^{SACoreLocation=^^?}"
- "^{SACoreLocation=^^?}16@0:8"
- "addConfigForIsoList:config:error:"
- "allowed"
- "awareness.caf"
- "bleFanout"
- "cacheFetchDitherSeconds"
- "codebook.json"
- "fanoutMinDensity"
- "fanoutPercent"
- "follow_up"
- "motionHarvestOnly"
- "new"
- "setWithObjects:"
- "update"
- "v24@0:8^{SACoreLocation=^^?}16"
- "{\"msg%{public}.0s\":\"#asset,#ble,readBleConfigFromFile\", \"first\":\"%{private}3f\", \"second\":\"%{private}3f\"}"
- "{\"msg%{public}.0s\":\"#asset,#igneous,log\", \"English\":%{private, location:escape_only}s, \"Spanish\":%{private, location:escape_only}s, \"sourceString\":%{private, location:escape_only}s, \"ProductionKeyLen\":%{private}llu, \"typeCount\":%{private}llu, \"performanceTestSourceString\":%{private, location:escape_only}s, \"followUpSourceString\":%{private, location:escape_only}s, \"MMI\":\"%{private}0.3f\", \"Magnitude\":\"%{private}0.3f\", \"FollowUpMessageValidTime\":\"%{private}0.3f\", \"watchHysteresis\":\"%{private}0.3f\", \"PhoneHysteresis\":\"%{private}0.3f\", \"IgnoreDuration\":\"%{private}0.3f\", \"TimeBetweenAlerts\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#asset,#igneous,readIgneousAlertConfigData\", \"type\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#assetConfig,#warning,readAPNConfigAsset,nilAssetDictionary\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,#warning,readAPNConfigAsset,nilConfig\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,getRollingMetrics\", \"rmSupported\":%{public}d, \"rollingPeriodSeconds\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#assetConfig,log\", \"pullpc\":%{private}d, \"appc\":%{private}d, \"efficacyParticipationPercentage\":%{private}d, \"wowControls\":%{private}d, \"pullCname\":%{private, location:escape_only}s, \"efficacyManifestFileName\":%{private, location:escape_only}s, \"codebookFileName\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset\", \"asset\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset,nil asset dictionary\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset,nil config\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset,nil eqSensing dictionary\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readMapCacheAsset,cacheRadiiKmNil\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readMapCacheAsset,configIsNil\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readMapCacheAsset,mapConfigNil\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset\", \"efficacyManifestFileName\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset\", \"metricPeriod\":%{public}d}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset\", \"metrics\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset\", \"metricsData\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset\", \"rmSupport\":%{public}d}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset,nilAssetDictionary\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset,nilConfig\"}"
- "{\"msg%{public}.0s\":\"#assetDefault\", \"fPullServerName\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#chsel,Safety Alerts init timedout\", \"timeout\":%{public}d, \"country\":%{public, location:escape_only}s, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"isMobileAssetEnabled\":%{public}hhd, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#chsel,addCountryConfig\", \"success\":%{public}hhd, \"country\":%{public, location:escape_only}@, \"config\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,d null\"}"
- "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,invalidArgs\"}"
- "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,isoList null\"}"
- "{\"msg%{public}.0s\":\"#chsel,channelConfigIdObjectFailed\"}"
- "{\"msg%{public}.0s\":\"#chsel,channelIdObjectFailed\"}"
- "{\"msg%{public}.0s\":\"#chsel,elementIsNotDictionary\", \"index\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#chsel,feature\", \"feature\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,features\", \"size\":%{public}d}"
- "{\"msg%{public}.0s\":\"#chsel,features,size\", \"size\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#chsel,fetchInfoForLocationReply\", \"config\":%{private, location:escape_only}@, \"info\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,fetchInfoForLocationReply,onError\", \"config\":%{private, location:escape_only}@, \"info\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,geometryFailed\"}"
- "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,state\", \"isEnabled\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"inCoverageRegion\":%{private}hhd, \"isInCountry\":%{private}hhd, \"emergencyAlert\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd, \"improveSafety\":%{private}hhd, \"isMotionHarvestAllowed\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,invalid_features\"}"
- "{\"msg%{public}.0s\":\"#chsel,loop\", \"index\":%{public}d}"
- "{\"msg%{public}.0s\":\"#chsel,noFeatureInAsset\"}"
- "{\"msg%{public}.0s\":\"#chsel,onAssetReceived\", \"asset\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,onCountrySupportChanged\", \"isSupported\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,onMotionHarvestOnlySupportChanged\", \"asset config value\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,onMotionHarvestOnlySupportChanged\", \"isSupported\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,properties\", \"properties\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,propertiesIdObjectFailed\"}"
- "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,Voters\", \"country\":%{public, location:escape_only}s, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"channelMapsSize\":%{private}d, \"isParticipating\":%{public, location:escape_only}s, \"isPhone\":%{private}d, \"isWatch\":%{private}d, \"forceOrDeferChannelUpdate\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,states\", \"country\":%{public, location:escape_only}s, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert sent successfully \"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert\", \"rootDict\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,didFailWithError\", \"errordomain\":%{public}d, \"error\":%{public}d, \"rootDict\":%{private, location:escape_only}@, \"infoDictMain\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,infoDict invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,infoDictList invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,infoDictMain invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,item1 invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,item2 invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousAlert,rootDict invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert sent successfully \"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert\", \"rootDict\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,didFailWithError\", \"errordomain\":%{public}d, \"error\":%{public}d, \"rootDict\":%{private, location:escape_only}@, \"infoDictMain\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,infoDict invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,infoDictList invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,infoDictMain invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,item1 invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,item2 invalid\"}"
- "{\"msg%{public}.0s\":\"#ctsa,sendIgneousLivabilityAlert,rootDict invalid\"}"
- "{\"msg%{public}.0s\":\"#daemon,initDeinitBleCore release\"}"
- "{\"msg%{public}.0s\":\"#daemon,initDeinitBleCore\"}"
- "{\"msg%{public}.0s\":\"#dbg,#assetConfig,onAssetReceived\", \"asset\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#dbg,#assetConfig,readAPNConfigAsset\", \"asset\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#ehmd,updateBgSysTask\"}"
- "{\"msg%{public}.0s\":\"#ibp,parse,invalid sender\"}"
- "{\"msg%{public}.0s\":\"#ibp,readAndValidateSender,not internal\"}"
- "{\"msg%{public}.0s\":\"#igdisp,postAlertThroughTelephony\"}"
- "{\"msg%{public}.0s\":\"#ignalert,getFollowUpAlertNotificationContent,usgs config not found\"}"
- "{\"msg%{public}.0s\":\"#igv,validate,not internal install\"}"
- "{\"msg%{public}.0s\":\"#md,empty file name\", \"id\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#md,empty identifier\"}"
- "{\"msg%{public}.0s\":\"#md,negative download period\", \"id\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saanalytics,onAssetReceived\", \"rmSupported\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"invalid sender\", \"alertLevel\":%{private, location:escape_only}s, \"purpose\":%{private, location:escape_only}s, \"class\":%{private, location:escape_only}s, \"function\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"interface\":%{private}d, \"transport\":%{private}d, \"ingressToServerTime\":\"%{private}.3f\", \"egressFromSourceTime\":\"%{private}.3f\", \"eventOriginTime\":\"%{private}.3f\", \"effectiveTime\":\"%{private}.3f\", \"expiryTime\":\"%{private}.3f\", \"advTime\":\"%{private}.3f\"}"
- "{\"msg%{public}.0s\":\"postAlertThroughTelephony\", \"alertLevel\":%{private, location:escape_only}s, \"purpose\":%{private, location:escape_only}s, \"class\":%{private, location:escape_only}s, \"function\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"interface\":%{private}d, \"transport\":%{private}d, \"ingressToServerTime\":\"%{private}.3f\", \"egressFromSourceTime\":\"%{private}.3f\", \"eventOriginTime\":\"%{private}.3f\", \"effectiveTime\":\"%{private}.3f\", \"expiryTime\":\"%{private}.3f\", \"advTime\":\"%{private}.3f\"}"

```
