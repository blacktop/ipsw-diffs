## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-525.60.9.0.0
-  __TEXT.__text: 0x99d50
+525.100.35.0.0
+  __TEXT.__text: 0x9b378
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x10008
+  __TEXT.__objc_methlist: 0x101e8
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0xcfcc
-  __TEXT.__oslogstring: 0x9c2a
+  __TEXT.__cstring: 0xd39c
+  __TEXT.__oslogstring: 0x9d80
   __TEXT.__gcc_except_tab: 0xea0
-  __TEXT.__unwind_info: 0x1830
-  __TEXT.__objc_classname: 0x8de
-  __TEXT.__objc_methname: 0x3de04
-  __TEXT.__objc_methtype: 0x3fa8
-  __TEXT.__objc_stubs: 0xc900
+  __TEXT.__unwind_info: 0x186c
+  __TEXT.__objc_classname: 0x90c
+  __TEXT.__objc_methname: 0x3e102
+  __TEXT.__objc_methtype: 0x401b
+  __TEXT.__objc_stubs: 0xca20
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x12e8
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__const: 0x1358
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x201a0
-  __DATA_CONST.__objc_selrefs: 0x50b0
+  __DATA_CONST.__objc_const: 0x20830
+  __DATA_CONST.__objc_selrefs: 0x5150
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x3b30
-  __AUTH_CONST.__cfstring: 0xafa0
-  __AUTH_CONST.__objc_const: 0x1e50
+  __AUTH_CONST.__cfstring: 0xb1a0
+  __AUTH_CONST.__objc_const: 0x1ee0
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH.__objc_data: 0xe10
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x4d8
-  __DATA.__objc_superrefs: 0x220
-  __DATA.__objc_ivar: 0x218c
-  __DATA.__data: 0x660
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x21a8
+  __DATA.__data: 0x6c0
   __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0x8c0
+  __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreML.framework/CoreML
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/ContextSync.framework/ContextSync
   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6107
-  Symbols:   17461
-  CStrings:  7024
+  Functions: 6156
+  Symbols:   17604
+  CStrings:  7089
 
Symbols:
+ +[PowerUIInCarSignalMonitor monitorWithDelegate:]
+ -[PowerUIInCarSignalMonitor .cxx_destruct]
+ -[PowerUIInCarSignalMonitor carplayConnected]
+ -[PowerUIInCarSignalMonitor delegate]
+ -[PowerUIInCarSignalMonitor inCar]
+ -[PowerUIInCarSignalMonitor initWithDelegate:]
+ -[PowerUIInCarSignalMonitor log]
+ -[PowerUIInCarSignalMonitor navigationStarted]
+ -[PowerUIInCarSignalMonitor requiredFullChargeDate]
+ -[PowerUIInCarSignalMonitor sessionDidConnect:]
+ -[PowerUIInCarSignalMonitor sessionDidDisconnect:]
+ -[PowerUIInCarSignalMonitor sessionStatus]
+ -[PowerUIInCarSignalMonitor setCarplayConnected:]
+ -[PowerUIInCarSignalMonitor setDelegate:]
+ -[PowerUIInCarSignalMonitor setInCar:]
+ -[PowerUIInCarSignalMonitor setLog:]
+ -[PowerUIInCarSignalMonitor setNavigationStarted:]
+ -[PowerUIInCarSignalMonitor setSessionStatus:]
+ -[PowerUIInCarSignalMonitor setVehicleConnected:]
+ -[PowerUIInCarSignalMonitor signalID]
+ -[PowerUIInCarSignalMonitor startMonitoring]
+ -[PowerUIInCarSignalMonitor stopMonitoring]
+ -[PowerUIInCarSignalMonitor vehicleConnected]
+ -[PowerUINotificationManager handleLocationFailures:]
+ -[PowerUINotificationManager postInternalLocationFailureNotification]
+ -[PowerUINotificationManager ttrURLforLocationFailure]
+ -[PowerUISmartChargeManager clearChargeLimit].cold.1
+ -[PowerUISmartChargeManager client:setState:withHandler:].cold.2
+ -[PowerUISmartChargeManager recordAnalytics].cold.2
+ -[PowerUISmartChargeManagerUnsupported batteryGaugingStatusWithHandler:]
+ -[PowerUISmartChargeManagerUnsupported client:setChargingStatus:withHandler:]
+ -[PowerUISmartChargeManagerUnsupported client:setDEoCState:withHandler:]
+ -[PowerUISmartChargeManagerUnsupported client:setMCLState:withHandler:]
+ -[PowerUISmartChargeManagerUnsupported currentChargeLimit]
+ -[PowerUISmartChargeManagerUnsupported engageFrom:until:repeatUntil:overrideAllSignals:withHandler:]
+ -[PowerUISmartChargeManagerUnsupported isDEoCCurrentlyEnabledWithHandler:]
+ -[PowerUISmartChargeManagerUnsupported isDEoCSupportedWithHandler:]
+ -[PowerUISmartChargeManagerUnsupported isMCLCurrentlyEnabledWithHandler:]
+ -[PowerUISmartChargeManagerUnsupported isMCLSupportedWithHandler:]
+ -[PowerUISmartChargeManagerUnsupported isMCLSupported]
+ -[PowerUISmartChargeManagerUnsupported isOBCEngagedOrChargeLimitedWithHandler:]
+ _OBJC_CLASS_$_CARSessionStatus
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_PowerUIInCarSignalMonitor
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._carplayConnected
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._delegate
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._inCar
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._log
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._navigationStarted
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._sessionStatus
+ _OBJC_IVAR_$_PowerUIInCarSignalMonitor._vehicleConnected
+ _OBJC_METACLASS_$_PowerUIInCarSignalMonitor
+ _OUTLINED_FUNCTION_13
+ _PowerUILocationFailureTTRNote
+ __OBJC_$_CLASS_METHODS_PowerUIInCarSignalMonitor
+ __OBJC_$_INSTANCE_METHODS_PowerUIInCarSignalMonitor
+ __OBJC_$_INSTANCE_VARIABLES_PowerUIInCarSignalMonitor
+ __OBJC_$_PROP_LIST_PowerUIInCarSignalMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CARSessionObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CARSessionObserving
+ __OBJC_$_PROTOCOL_REFS_CARSessionObserving
+ __OBJC_CLASS_PROTOCOLS_$_PowerUIInCarSignalMonitor
+ __OBJC_CLASS_RO_$_PowerUIInCarSignalMonitor
+ __OBJC_LABEL_PROTOCOL_$_CARSessionObserving
+ __OBJC_METACLASS_RO_$_PowerUIInCarSignalMonitor
+ __OBJC_PROTOCOL_$_CARSessionObserving
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.573
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.581
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.590
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.594
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.599
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.605
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.606
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.611
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.612
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.613
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.575
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.583
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.592
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.601
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.609
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.577
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.588
+ ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_4.579
+ ___34-[PowerUISmartChargeClient status]_block_invoke.130
+ ___42-[PowerUISmartChargeClient powerLogStatus]_block_invoke.132
+ ___44-[PowerUIInCarSignalMonitor startMonitoring]_block_invoke
+ ___44-[PowerUIInCarSignalMonitor startMonitoring]_block_invoke.19
+ ___44-[PowerUIInCarSignalMonitor startMonitoring]_block_invoke.23
+ ___44-[PowerUIInCarSignalMonitor startMonitoring]_block_invoke.24
+ ___44-[PowerUISmartChargeManager handleCallback:]_block_invoke.899
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.944
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.951
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.964
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.968
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.969
+ ___46-[PowerUISmartChargeClient setChargingStatus:]_block_invoke.153
+ ___47-[PowerUISmartChargeClient fullChargeDeadline:]_block_invoke.133
+ ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.174
+ ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.175
+ ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.181
+ ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.181.cold.1
+ ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.181.cold.2
+ ___49-[PowerUISmartChargeClient batteryGaugingStatus:]_block_invoke.157
+ ___49-[PowerUISmartChargeClient batteryGaugingStatus:]_block_invoke.157.cold.1
+ ___50-[PowerUISmartChargeClient cecFullChargeDeadline:]_block_invoke.149
+ ___51-[PowerUISmartChargeClient resetEngagementOverride]_block_invoke.152
+ ___52-[PowerUILocationSignalMonitor inKnownMicrolocation]_block_invoke.182
+ ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.155
+ ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.155.cold.1
+ ___53-[PowerUINotificationManager handleLocationFailures:]_block_invoke
+ ___53-[PowerUINotificationManager handleLocationFailures:]_block_invoke_2
+ ___53-[PowerUINotificationManager handleLocationFailures:]_block_invoke_2.cold.1
+ ___57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1435
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1546
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1546.cold.1
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1546.cold.2
+ ___63-[PowerUISmartChargeClientAudioAccessories getAvailableDevices]_block_invoke.105
+ ___63-[PowerUISmartChargeClientAudioAccessories getStatusForDevice:]_block_invoke.107
+ ___64-[PowerUISmartChargeClientAudioAccessories lastActionForDevice:]_block_invoke.109
+ ___66-[PowerUISmartChargeClient legacy_client_isOBCEngagedWithHandler:]_block_invoke.139
+ ___67-[PowerUILocationSignalMonitor inTypicalChargingLocationWithError:]_block_invoke.173
+ ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.111
+ ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.111.cold.1
+ ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.150
+ ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.150.cold.1
+ ___77-[PowerUILocationSignalMonitor longChargesOccurredInLocationsNear:withError:]_block_invoke.163
+ ___77-[PowerUILocationSignalMonitor longChargesOccurredInLocationsNear:withError:]_block_invoke.167
+ ___85-[PowerUISmartChargeClientAudioAccessories engageUntil:forDevice:overrideAllSignals:]_block_invoke.104
+ ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.145
+ ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.145.cold.1
+ ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.154
+ ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.154.cold.1
+ ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.137
+ ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.137.cold.1
+ ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.135
+ ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.135.cold.1
+ ___block_descriptor_33_e19_"NSDictionary"8?0l
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_literal_global.1066
+ ___block_literal_global.1106
+ ___block_literal_global.1108
+ ___block_literal_global.1133
+ ___block_literal_global.1138
+ ___block_literal_global.1263
+ ___block_literal_global.141
+ ___block_literal_global.143
+ ___block_literal_global.148
+ ___block_literal_global.178
+ ___block_literal_global.2182
+ ___block_literal_global.2184
+ ___block_literal_global.2186
+ ___block_literal_global.904
+ __unnamed_array_storage.146
+ __unnamed_array_storage.160
+ _objc_msgSend$addSessionObserver:
+ _objc_msgSend$currentSession
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$handleLocationFailures:
+ _objc_msgSend$inCar
+ _objc_msgSend$initAndWaitUntilSessionUpdated
+ _objc_msgSend$isiPad
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$removeSessionObserver:
+ _objc_msgSend$ttrURLforLocationFailure
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.569
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.578
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.587
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.591
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.596
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.600
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.602
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.604
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.608
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.609
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.571
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.580
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.589
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.598
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.606
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.574
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.585
- ___151-[PowerUISmartChargeManager initWithDefaultsDomain:knowledgeStore:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_4.576
- ___34-[PowerUISmartChargeClient status]_block_invoke.129
- ___42-[PowerUISmartChargeClient powerLogStatus]_block_invoke.131
- ___44-[PowerUISmartChargeManager handleCallback:]_block_invoke.896
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.941
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.948
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.958
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.962
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.963
- ___46-[PowerUISmartChargeClient setChargingStatus:]_block_invoke.152
- ___47-[PowerUISmartChargeClient fullChargeDeadline:]_block_invoke.132
- ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.171
- ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.172
- ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.178
- ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.178.cold.1
- ___48-[PowerUILocationSignalMonitor isInSameTimeZone]_block_invoke.178.cold.2
- ___49-[PowerUISmartChargeClient batteryGaugingStatus:]_block_invoke.156
- ___49-[PowerUISmartChargeClient batteryGaugingStatus:]_block_invoke.156.cold.1
- ___50-[PowerUISmartChargeClient cecFullChargeDeadline:]_block_invoke.148
- ___51-[PowerUISmartChargeClient resetEngagementOverride]_block_invoke.151
- ___52-[PowerUILocationSignalMonitor inKnownMicrolocation]_block_invoke.179
- ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.154
- ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.154.cold.1
- ___57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1427
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1539
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1539.cold.1
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1539.cold.2
- ___63-[PowerUISmartChargeClientAudioAccessories getAvailableDevices]_block_invoke.104
- ___63-[PowerUISmartChargeClientAudioAccessories getStatusForDevice:]_block_invoke.106
- ___64-[PowerUISmartChargeClientAudioAccessories lastActionForDevice:]_block_invoke.108
- ___66-[PowerUISmartChargeClient legacy_client_isOBCEngagedWithHandler:]_block_invoke.138
- ___67-[PowerUILocationSignalMonitor inTypicalChargingLocationWithError:]_block_invoke.170
- ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.110
- ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.110.cold.1
- ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.149
- ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.149.cold.1
- ___77-[PowerUILocationSignalMonitor longChargesOccurredInLocationsNear:withError:]_block_invoke.160
- ___77-[PowerUILocationSignalMonitor longChargesOccurredInLocationsNear:withError:]_block_invoke.164
- ___85-[PowerUISmartChargeClientAudioAccessories engageUntil:forDevice:overrideAllSignals:]_block_invoke.103
- ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.144
- ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.144.cold.1
- ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.153
- ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.153.cold.1
- ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.136
- ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.136.cold.1
- ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.134
- ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.134.cold.1
- ___block_literal_global.1060
- ___block_literal_global.1100
- ___block_literal_global.1102
- ___block_literal_global.1127
- ___block_literal_global.1132
- ___block_literal_global.1257
- ___block_literal_global.140
- ___block_literal_global.142
- ___block_literal_global.147
- ___block_literal_global.175
- ___block_literal_global.2174
- ___block_literal_global.2176
- ___block_literal_global.2178
- ___block_literal_global.901
- __unnamed_array_storage.143
- __unnamed_array_storage.157
- _objc_msgSend$numberWithUnsignedLongLong:
CStrings:
+ " not"
+ "%@ requests state: %@, but the state is not supported!"
+ "@\"CARSessionStatus\""
+ "CARSessionObserving"
+ "Charge limit token already exists: %@"
+ "Clearing current charge limit token (%@)"
+ "Correct"
+ "Created new charge limit token: %@"
+ "Device already charged to full, likely due to battery gauging. Do not reengage charge limit."
+ "Error when opening TTR URL: %@"
+ "Have you charged here in the last month?"
+ "Help your fellow engineers! Please long-press this notification and consider filing a radar (or select 'Yes') if you've charged at this (physical) location in the last month for at least an hour, or 'No' if this is the first time or you typically charge here very briefly."
+ "Loaded charge limit token from defaults: %@"
+ "No charge sessions found on plugout, do not send analytics. Did the device restart?"
+ "PowerUIInCarSignalMonitor"
+ "Previously: %u, Now: %u"
+ "Successfully cancelled"
+ "T@\"CARSessionStatus\",&,N,V_sessionStatus"
+ "T@\"NSString\",&,V_chargeLimitToken"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_carplayConnected"
+ "TB,N,V_inCar"
+ "TB,N,V_navigationStarted"
+ "TB,N,V_vehicleConnected"
+ "User has%@ charged here before."
+ "Y-O\x02\x14#"
+ "^{__CFString=}16@0:8"
+ "_carplayConnected"
+ "_inCar"
+ "_navigationStarted"
+ "_sessionStatus"
+ "_vehicleConnected"
+ "addSessionObserver:"
+ "cancelledConnectionAttemptOnTransport:"
+ "carplayConnected"
+ "chargeLimitTokenUUID"
+ "com.apple.GeoServices.navigation.started"
+ "com.apple.GeoServices.navigation.stopped"
+ "com.apple.locationd.vehicle.connected"
+ "com.apple.locationd.vehicle.disconnected"
+ "com.apple.powerui.locationFailure"
+ "com.apple.powerui.locationTTR"
+ "com.apple.powerui.note.location"
+ "com.apple.powerui.signals"
+ "currentSession"
+ "defaultWorkspace"
+ "handleLocationFailures:"
+ "inCar"
+ "initAndWaitUntilSessionUpdated"
+ "navigationStarted"
+ "noAction"
+ "openURL:configuration:completionHandler:"
+ "postInternalLocationFailureNotification"
+ "poweruiTTR"
+ "removeSessionObserver:"
+ "session:didUpdateConfiguration:"
+ "sessionDidConnect:"
+ "sessionDidDisconnect:"
+ "sessionStatus"
+ "setCarplayConnected:"
+ "setInCar:"
+ "setNavigationStarted:"
+ "setSessionStatus:"
+ "setVehicleConnected:"
+ "startedConnectionAttemptOnTransport:"
+ "tap-to-radar://new?Title=OBC Location Error&Classification=Serious Bug&ComponentID=971083&ComponentName=PowerUI&ComponentVersion=all&Reproducible=Sometimes&Description=If you have charged here in the past, could you describe how recently and general frequency of charge sessions that are at least one hour long?"
+ "ttrURLforLocationFailure"
+ "v24@0:8@\"CARSession\"16"
+ "v32@0:8@\"CARSession\"16@\"CARSessionConfiguration\"24"
+ "vehicleConnected"
+ "yesAction"
+ "yesNoCategory"
- "Charge limit token already exists: %llu"
- "Cleared current charge limit token"
- "Created new charge limit token: %llu"
- "Loaded charge limit token from defaults: %llu"
- "TQ,V_chargeLimitToken"
- "Y-O\x02\x14\""
- "numberWithUnsignedLongLong:"

```
