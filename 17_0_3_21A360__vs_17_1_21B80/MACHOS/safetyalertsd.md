## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-43.0.2.0.0
-  __TEXT.__text: 0x47e14
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x1780
+43.0.9.0.1
+  __TEXT.__text: 0x52404
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x18e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0x2db9
-  __TEXT.__gcc_except_tab: 0x2084
-  __TEXT.__oslogstring: 0xf5af
-  __TEXT.__cstring: 0x2854
-  __TEXT.__objc_methname: 0x2048
+  __TEXT.__const: 0x3239
+  __TEXT.__gcc_except_tab: 0x23fc
+  __TEXT.__oslogstring: 0x10f55
+  __TEXT.__cstring: 0x29e5
+  __TEXT.__objc_methname: 0x2118
   __TEXT.__objc_classname: 0x173
   __TEXT.__objc_methtype: 0x103f
-  __TEXT.__unwind_info: 0x162c
+  __TEXT.__unwind_info: 0x1868
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x32d0
-  __DATA_CONST.__cfstring: 0x2860
+  __DATA_CONST.__const: 0x3738
+  __DATA_CONST.__cfstring: 0x2a80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1650
-  __DATA.__objc_selrefs: 0x698
-  __DATA.__objc_classrefs: 0x160
+  __DATA.__objc_selrefs: 0x6f0
+  __DATA.__objc_classrefs: 0x168
   __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x368
-  __DATA.__common: 0x38
+  __DATA.__common: 0x28
   __DATA.__bss: 0x1c0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
+  - /System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libPCITransport.dylib

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1274
-  Symbols:   304
-  CStrings:  1678
+  Functions: 1406
+  Symbols:   311
+  CStrings:  1774
 
Symbols:
+ _CFPreferencesCopyValue
+ _OBJC_CLASS_$_NSNotificationCenter
+ _SALogObjectGeneral
+ _SALogObjectWarning
+ __Z9SALogInitv
+ __xpc_event_key_name
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
- _os_log_create
CStrings:
+ "CellBroadcastSettingAMBER"
+ "CellBroadcastSettingEmergency"
+ "CellBroadcastSettingPublicSafety"
+ "CellularQuality"
+ "CellularQualityStatus"
+ "Connected"
+ "RAT"
+ "RRC"
+ "WakeOnWiFiStatus"
+ "WiFiAvailabilityStatus"
+ "WifiQuality"
+ "WoW"
+ "addObjectsFromArray:"
+ "arrayWithObjects:"
+ "cellQuality"
+ "cellRat"
+ "cellRrc"
+ "com.apple.commcenter.shared"
+ "com.apple.notifyd.matching"
+ "defaultCenter"
+ "deviceRegistrationState"
+ "isAmberAlertEnabled"
+ "isEmergencyAlertEnabled"
+ "isIphoneAnalyticsEnabled"
+ "isPublicSafetyAlertEnabled"
+ "isSignificantLocationEnabled"
+ "onAlertReceivedDuration"
+ "postNotificationName:object:"
+ "quality"
+ "rat"
+ "rrcStatus"
+ "subscribe:topic:"
+ "timeSinceRrcConnection"
+ "unsubscribe:topic:"
+ "wasRebootedDuringRollingPeriod"
+ "wifiQuality"
+ "wow"
+ "{\"msg%{public}.0s\":\"#ch,subscribe\", \"channel\":%{private, location:escape_only}s, \"channelTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ch,subscribe,Alert\"}"
+ "{\"msg%{public}.0s\":\"#ch,subscribe,invalid type\"}"
+ "{\"msg%{public}.0s\":\"#ch,unsubscribe\", \"channel\":%{private, location:escape_only}s, \"channelTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#channel,#channel,Waiting for push notifications\"}"
+ "{\"msg%{public}.0s\":\"#channel,initWithQueue\", \"isProduction\":%{public}hhd, \"type\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chmgr,addChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chmgr,isChannelListSame\", \"addList\":%{public}llu, \"removeList\":%{public}llu}"
+ "{\"msg%{public}.0s\":\"#chmgr,isChannelListSame\", \"channelSet1.size()\":%{public}lu, \"channelSet2.size()\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#chmgr,removeChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chsel,ch\", \"channelListSize,MA,\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#chsel,getChannelFromMap\", \"channelId\":%{public, location:escape_only}s, \"channelType\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,Voters\", \"country\":%{public, location:escape_only}s, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"channelMapsSize\":%{private}d, \"isParticipating\":%{public, location:escape_only}s, \"isPhone\":%{private}d, \"isWatch\":%{private}d, \"forceOrDeferChannelUpdate\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,updateLivabilityChannels,precondition failed\"}"
+ "{\"msg%{public}.0s\":\"#chsel,updateLivabilityChannels,state\", \"registerLivability\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,updateSAChannels,SA not supported on watch\"}"
+ "{\"msg%{public}.0s\":\"#chsel,updateSAChannels,precondition failed\"}"
+ "{\"msg%{public}.0s\":\"#chsel,updateSAChannels,state\", \"isSaRegisterPreCheckPass\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#commonUtils,weightedMedian,#warning,empty size\", \"isArrayEmpty\":%{private}d, \"isWeightEmpty\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#commonUtils,weightedMedian,#warning,median not found\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,weightedMedian,#warning,sumWeights invalid\", \"sumWeights\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,weightedMedian,#warning,unequal size\", \"arraySize\":%{private}d, \"weightsSize\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCompanionNearby\", \"Companion\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#daemon,#warning,onWeaDisplayedNotification,noLocation,deferAlert\", \"weaMessage\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,com.apple.notifyd.matching rebroadcast\", \"notificationName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,enableDarwinNotificationRebroadcast\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onChannelUpdate,processPendingWeaDisplayedAlert\", \"alert\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#dbg,#sa_util,isHashMatch,cmam_long_text nil\"}"
+ "{\"msg%{public}.0s\":\"#dbg,#sa_util,isHashMatch,cmam_text nil\"}"
+ "{\"msg%{public}.0s\":\"#eff,isSaCapable,biomeStatus\", \"startSeconds\":\"%{private}0.1f\", \"endSeconds\":\"%{private}0.1f\", \"subStatus\":%{private, location:escape_only}s, \"nwCellularStatus\":%{private, location:escape_only}s, \"nwWifiStatus\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#eff,metric submitted continue\", \"RAT\":%{public, location:escape_only}s, \"RRC\":%{public, location:escape_only}s, \"cellularQuality\":%{public}d, \"timeSinceRrcConnection\":\"%{public}.3f\"}"
+ "{\"msg%{public}.0s\":\"#eff,metric submitted\", \"hourOfMetricTrigger\":%{public}d, \"alertIDString\":%{public, location:escape_only}s, \"participationType\":%{public, location:escape_only}s, \"pushInterface\":%{public, location:escape_only}s, \"efficacyType\":%{public, location:escape_only}s, \"hashType\":%{public, location:escape_only}s, \"cellularConnectionStatus\":%{public, location:escape_only}s, \"maCompatibilityVersion\":%{public}d, \"maContentVersion\":%{public}d, \"wifiQuality\":%{public}d, \"WoW\":%{public}d, \"wasCellularInternetReachable\":%{public}d, \"wasChannelSubscribed\":%{public}d, \"wasSaReceived\":%{public}d, \"wasUserInSaPolygon\":%{public}d, \"wasUserInWeaPolygon\":%{public}d, \"wasWeaAlertReceived\":%{public}d, \"wasWeaDisplayed\":%{public}d, \"didWeaHavePolygon\":%{public}d, \"wasWifiInternetReachable\":%{public}d, \"wasAnyAlertReceived\":%{public}d, \"wasSaExpected\":%{public}d, \"wasRebootedDuringRollingPeriod\":%{public}d, \"saLatencyRelativeToOriginatorTime\":\"%{public}0.3f\", \"saLatencyRelativeToServerTime\":\"%{public}0.3f\", \"saLatencyFromServerIngressTime\":\"%{public}0.3f\", \"weaLatencyRelativeToOriginatorTime\":\"%{public}0.3f\", \"weaDisplayedLatencyRelativeToReceivedTime\":\"%{public}0.3f\", \"weaMinusSaTimestamp\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#eff,preparingWeaMetrics,skipGeneratedBeforeRollingPeriod\"}"
+ "{\"msg%{public}.0s\":\"#gi,#generateGlobalTileIdFromLatLonAndGridSizeInDegrees\", \"totalGridsInEachRow\":%{private}lu, \"totalGridsInEachCol\":%{private}lu, \"gridSizeInDegrees\":\"%{private}0.3f\", \"swXIndex\":%{private}lu, \"swYIndex\":%{private}lu, \"curGlobalIndex\":%{private}lu, \"multiplier\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#pullServiceProd,#warning,notPulling,noInstruction\", \"hash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#rm,#warning,emergencyAlert is disabled\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,CellularQualityStatus\", \"timestamp\":\"%{private}0.1f\", \"deviceRegistrationStatus\":%{public}d, \"quality\":%{public}d, \"RAT\":%{public}d, \"RRC\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,WakeOnWifiStatus\", \"timestamp\":\"%{private}0.1f\", \"isStarting\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,WifiQualityStatus\", \"timestamp\":\"%{private}0.1f\", \"isStarting\":%{private}hhd, \"wifiQuality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularQualityWithinWindow\", \"quality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularQualityWithinWindow,empty history\", \"quality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularQualityWithinWindow,invalid median conversion\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRatWithinWindow\", \"rat\":%{private}d, \"ratStr\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRatWithinWindow,empty history\", \"rat\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRatWithinWindow,invalid median conversion\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRrcWithinWindow\", \"rrc\":%{private}d, \"rrcStr\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRrcWithinWindow\", \"rrc\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRrcWithinWindow,empty history\", \"rrc\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,cellularRrcWithinWindow,invalid median conversion\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,fetch,CellularQualityComplete\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,fetch,wifiQualityComplete\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,fetch,wowComplete\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,findWeightedMedianOfEvents,empty events\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,timeSinceRrcChanged\", \"timeSinceRrcChanged\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,wifiQualityWithinWindow\", \"quality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,wifiQualityWithinWindow\", \"start\":\"%{private}.2f\", \"end\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,wifiQualityWithinWindow,empty history\", \"quality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,deferSavingTillFirstUnlock\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findAllValTimestamp,no val available\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findAllValTimestamp,outOfRangeArgs\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findAllValTimestamp,skipping,notReady\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findLatestEventBefore,InvalidArgs\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findLatestEventBefore,skipping,notReady\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,onFirstUnlock,skip\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findLastValueDuration,\", \"lastValueDuration\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findLastValueDuration,empty history\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findLastValueDuration,no event before timestamp\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findLatestEventBefore\", \"time\":\"%{private}.2f\", \"fStartTimeSeconds\":\"%{private}.2f\", \"fEndTimeSeconds\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,load\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,load,#warning,deferLoadingTillFirstUnlock\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd\", \"isAmberAlertEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd\", \"isEmergencyAlertEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd\", \"isPublicSafetyAlertEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saanalytics,#warning,invalidDuration\", \"durationSeconds\":%{public}d}"
- "general"
- "subscribe:"
- "unsubscribe:"
- "warning"
- "{\"msg%{public}.0s\":\"#ch,subscribe\", \"channel\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#ch,unsubscribe\", \"channel\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#channel,#channel,Waiting for push notifications\", \"fromTopic\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#channel,initWithQueue\", \"isProduction\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chmgr,addChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#chmgr,removeChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,Voters\", \"country\":%{public, location:escape_only}s, \"lsOn\":%{public, location:escape_only}s, \"telephony\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"channelMapsSize\":%{private}d, \"isParticipating\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,ch,None\"}"
- "{\"msg%{public}.0s\":\"#eff,isSaCapable,biomeStatus\", \"startSeconds\":\"%{private}0.1f\", \"endSeconds\":\"%{private}0.1f\", \"subStatus\":%{private, location:escape_only}s, \"nwStatus\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#eff,metric submitted\", \"hourOfMetricTrigger\":%{public}d, \"alertIDString\":%{public, location:escape_only}s, \"participationType\":%{public, location:escape_only}s, \"pushInterface\":%{public, location:escape_only}s, \"efficacyType\":%{public, location:escape_only}s, \"hashType\":%{public, location:escape_only}s, \"cellularConnectionStatus\":%{public, location:escape_only}s, \"maCompatibilityVersion\":%{public}d, \"maContentVersion\":%{public}d, \"wasCellularInternetReachable\":%{public}d, \"wasChannelSubscribed\":%{public}d, \"wasSaReceived\":%{public}d, \"wasUserInSaPolygon\":%{public}d, \"wasUserInWeaPolygon\":%{public}d, \"wasWeaAlertReceived\":%{public}d, \"wasWeaDisplayed\":%{public}d, \"didWeaHavePolygon\":%{public}d, \"wasWifiInternetReachable\":%{public}d, \"wasAnyAlertReceived\":%{public}d, \"wasSaExpected\":%{public}d, \"saLatencyRelativeToOriginatorTime\":\"%{public}0.3f\", \"saLatencyRelativeToServerTime\":\"%{public}0.3f\", \"saLatencyFromServerIngressTime\":\"%{public}0.3f\", \"weaLatencyRelativeToOriginatorTime\":\"%{public}0.3f\", \"weaDisplayedLatencyRelativeToReceivedTime\":\"%{public}0.3f\", \"weaMinusSaTimestamp\":\"%{public}0.3f\"}"
- "{\"msg%{public}.0s\":\"#gi,#generateTileIdFromLatLonAndGridSizeInDegrees\", \"totalGridsInEachRow\":%{public}lu, \"totalGridsInEachCol\":%{public}lu, \"gridSizeInDegrees\":\"%{public}0.3f\", \"swXIndex\":%{public}lu, \"swYIndex\":%{public}lu, \"curGlobalIndex\":%{public}lu}"

```
