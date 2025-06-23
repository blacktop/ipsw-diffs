## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-420.30.5.14.0
-  __TEXT.__text: 0x744b0
+423.30.6.9.1
+  __TEXT.__text: 0x715ec
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0xaecc
-  __TEXT.__cstring: 0x6617
+  __TEXT.__objc_methlist: 0xaccc
+  __TEXT.__cstring: 0x65c7
   __TEXT.__const: 0x448
-  __TEXT.__gcc_except_tab: 0x1bfc
-  __TEXT.__oslogstring: 0x7b38
+  __TEXT.__gcc_except_tab: 0x1ba8
+  __TEXT.__oslogstring: 0x71e8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__unwind_info: 0x24b8
   __TEXT.__eh_frame: 0x250
-  __TEXT.__objc_classname: 0x128b
-  __TEXT.__objc_methname: 0x127f6
-  __TEXT.__objc_methtype: 0x38b9
-  __TEXT.__objc_stubs: 0xa8e0
+  __TEXT.__objc_classname: 0x1265
+  __TEXT.__objc_methname: 0x125d1
+  __TEXT.__objc_methtype: 0x3690
+  __TEXT.__objc_stubs: 0xa500
   __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x20b0
+  __DATA_CONST.__const: 0x2040
   __DATA_CONST.__objc_classlist: 0x408
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a10
-  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x39a0
+  __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x638
-  __AUTH_CONST.__const: 0xb50
+  __AUTH_CONST.__const: 0xb30
   __AUTH_CONST.__cfstring: 0x5a60
-  __AUTH_CONST.__objc_const: 0x129d8
+  __AUTH_CONST.__objc_const: 0x127d8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1128
-  __DATA.__objc_ivar: 0xd94
-  __DATA.__data: 0x1478
+  __DATA.__objc_ivar: 0xd84
+  __DATA.__data: 0x1418
   __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x1738
   __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__bss: 0x380
+  __DATA_DIRTY.__bss: 0x370
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8A7CB747-B7A6-3A08-A29C-100657D56156
-  Functions: 4089
-  Symbols:   12680
-  CStrings:  5827
+  UUID: 4D7D97C4-7618-3B00-AA1E-ED8BE8F121E1
+  Functions: 4044
+  Symbols:   12532
+  CStrings:  5749
 
Symbols:
+ +[SPSecureLocationsManager featureDisabledError]
+ -[SPDiscoveredAccessoryMetadata findMyVersion]
+ -[SPDiscoveredAccessoryMetadata setFindMyVersion:]
+ -[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]
+ -[SPSecureLocationsManager receivedLocationCommand:completion:].cold.1
+ -[SPSecureLocationsManager receivedLocationPayload:completion:].cold.1
+ -[SPSecureLocationsManager setLocationUpdateBlock:].cold.1
+ -[SPSecureLocationsManager shouldStartLocationMonitorWithCompletion:].cold.1
+ -[SPSecureLocationsManager startMonitoringFailedSubscriptions:].cold.1
+ -[SPSecureLocationsManager triggerStewieProactiveNotification].cold.1
+ GCC_except_table173
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table201
+ _OBJC_IVAR_$_SPDiscoveredAccessoryMetadata._findMyVersion
+ ___29-[SPLocalBeaconManager start]_block_invoke.132
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.267
+ ___34-[SPLocalBeaconManager timerFired]_block_invoke.155
+ ___39-[SPLocalBeaconManager beaconsChanged:]_block_invoke.141
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.262
+ ___44-[SPLocalBeaconManager updateStateFromNVRAM]_block_invoke.130
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.299
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.300
+ ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.142
+ ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.144
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.263
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.264
+ ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.201
+ ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke
+ ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.303
+ ___58-[SPLocalBeaconManager beaconingStateChangedNotification:]_block_invoke.140
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.265
+ ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.203
+ ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.208
+ ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.209
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.302
+ ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.210
+ ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.207
+ ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.205
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.313
+ ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.202
+ ___66-[SPSecureLocationsManager unsubscribeForId:clientApp:completion:]_block_invoke
+ ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.204
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.269
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.269.cold.1
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.312
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.170
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.172
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.173
+ ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.206
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.304
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.305
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.310
+ ___83-[SPLocalBeaconManager(KeyGeneration) generateOfflineAdvertisingKeysForReason:now:]_block_invoke.412
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.308
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.275
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.275.cold.1
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.278
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.282
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.280
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.283
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.286
+ ___block_literal_global.290
+ ___block_literal_global.421
+ _objc_msgSend$featureDisabledError
+ _objc_msgSend$fetchHawkeyeFirmwareVersion:completion:
- +[SPSecureLocationsManager exportedInterface]
- +[SPSecureLocationsManager exportedInterface].cold.1
- -[SPOwnerSession requestLiveLocationForFriend:completion:]
- -[SPOwnerSession requestLiveLocationForUUID:completion:]
- -[SPSecureLocationsManager clearCacheUpdates]
- -[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]
- -[SPSecureLocationsManager interruptionHandler:]
- -[SPSecureLocationsManager invalidationHandler:]
- -[SPSecureLocationsManager isSatelliteFeatureEnabled]
- -[SPSecureLocationsManager lastUpdatedStewieState]
- -[SPSecureLocationsManager locationUpdates]
- -[SPSecureLocationsManager receivedUpdatedLocations:]
- -[SPSecureLocationsManager setClearCacheUpdates:]
- -[SPSecureLocationsManager setLastUpdatedStewieState:]
- -[SPSecureLocationsManager setLocationUpdates:]
- -[SPSecureLocationsManager setStewieRetryCount:]
- -[SPSecureLocationsManager setStewieUpdateBlock:]
- -[SPSecureLocationsManager stewieRetryCount]
- -[SPSecureLocationsManager stewieServiceStateChanged:]
- -[SPSecureLocationsManager stewieUpdateBlock]
- GCC_except_table174
- GCC_except_table176
- GCC_except_table189
- GCC_except_table194
- GCC_except_table199
- GCC_except_table204
- _OBJC_IVAR_$_SPSecureLocationsManager._clearCacheUpdates
- _OBJC_IVAR_$_SPSecureLocationsManager._lastUpdatedStewieState
- _OBJC_IVAR_$_SPSecureLocationsManager._locationUpdates
- _OBJC_IVAR_$_SPSecureLocationsManager._stewieRetryCount
- _OBJC_IVAR_$_SPSecureLocationsManager._stewieUpdateBlock
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPSecureLocationsClientXPCProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SPSecureLocationsClientXPCProtocol
- __OBJC_$_PROTOCOL_REFS_SPSecureLocationsClientXPCProtocol
- __OBJC_CLASS_PROTOCOLS_$_SPSecureLocationsManager
- __OBJC_LABEL_PROTOCOL_$_SPSecureLocationsClientXPCProtocol
- __OBJC_PROTOCOL_$_SPSecureLocationsClientXPCProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SPSecureLocationsClientXPCProtocol
- ___29-[SPLocalBeaconManager start]_block_invoke.126
- ___32-[SPSecureLocationsManager init]_block_invoke
- ___32-[SPSecureLocationsManager init]_block_invoke_2
- ___33-[SPOwnerSession executeCommand:]_block_invoke.269
- ___34-[SPLocalBeaconManager timerFired]_block_invoke.149
- ___39-[SPLocalBeaconManager beaconsChanged:]_block_invoke.135
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.264
- ___44-[SPLocalBeaconManager updateStateFromNVRAM]_block_invoke.124
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.301
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.302
- ___45+[SPSecureLocationsManager exportedInterface]_block_invoke
- ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.136
- ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.138
- ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke
- ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke.146
- ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke.146.cold.1
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.265
- ___51-[SPSecureLocationsManager setLocationUpdateBlock:]_block_invoke
- ___51-[SPSecureLocationsManager setLocationUpdateBlock:]_block_invoke.250
- ___53-[SPSecureLocationsManager receivedUpdatedLocations:]_block_invoke
- ___53-[SPSecureLocationsManager receivedUpdatedLocations:]_block_invoke.247
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.266
- ___54-[SPSecureLocationsManager stewieServiceStateChanged:]_block_invoke
- ___54-[SPSecureLocationsManager stewieServiceStateChanged:]_block_invoke.248
- ___55-[SPSecureLocationsManager publishLocation:completion:]_block_invoke.257
- ___56-[SPOwnerSession requestLiveLocationForUUID:completion:]_block_invoke
- ___56-[SPOwnerSession requestLiveLocationForUUID:completion:]_block_invoke_2
- ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.203
- ___58-[SPLocalBeaconManager beaconingStateChangedNotification:]_block_invoke.134
- ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.267
- ___58-[SPOwnerSession requestLiveLocationForFriend:completion:]_block_invoke
- ___58-[SPOwnerSession requestLiveLocationForFriend:completion:]_block_invoke_2
- ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.205
- ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.210
- ___61-[SPSecureLocationsManager currentStewieStateWithCompletion:]_block_invoke_2
- ___61-[SPSecureLocationsManager stewiePublishStateWithCompletion:]_block_invoke_2
- ___62-[SPSecureLocationsManager triggerStewieProactiveNotification]_block_invoke
- ___62-[SPSecureLocationsManager triggerStewieProactiveNotification]_block_invoke_2
- ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.211
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.304
- ___63-[SPSecureLocationsManager receivedLocationCommand:completion:]_block_invoke_2
- ___63-[SPSecureLocationsManager receivedLocationPayload:completion:]_block_invoke_2
- ___63-[SPSecureLocationsManager startMonitoringFailedSubscriptions:]_block_invoke
- ___63-[SPSecureLocationsManager startMonitoringFailedSubscriptions:]_block_invoke.251
- ___63-[SPSecureLocationsManager updateLocationCacheWith:completion:]_block_invoke.256
- ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.212
- ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.209
- ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.207
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.314
- ___65-[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]_block_invoke
- ___65-[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]_block_invoke.249
- ___65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke.254
- ___65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke_2
- ___65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke_2.cold.1
- ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.204
- ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.206
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271.cold.1
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.313
- ___68-[SPSecureLocationsManager latestLocationFromCacheForId:completion:]_block_invoke.255
- ___68-[SPSecureLocationsManager stopMonitoringStewieStateWithCompletion:]_block_invoke_2
- ___69-[SPSecureLocationsManager shouldStartLocationMonitorWithCompletion:]_block_invoke_2
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.164
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.166
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.167
- ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.208
- ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.305
- ___75-[SPSecureLocationsManager startMonitoringStewieStateWithBlock:completion:]_block_invoke_2
- ___79-[SPSecureLocationsManager subscribeAndFetchLocationForIds:context:completion:]_block_invoke.253
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.306
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.311
- ___80-[SPSecureLocationsManager publishCurrentLocationToStewieWithReason:completion:]_block_invoke_2
- ___81-[SPSecureLocationsManager subscribeAndFetchLocationForIds:clientApp:completion:]_block_invoke_2
- ___83-[SPLocalBeaconManager(KeyGeneration) generateOfflineAdvertisingKeysForReason:now:]_block_invoke.406
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.309
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.277.cold.1
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.279
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.280
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.284
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.282
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.285
- ___block_descriptor_40_e8_32bs_e57_v24?0"SPSecureLocationsSubscriptionResult"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_literal_global.170
- ___block_literal_global.175
- ___block_literal_global.198
- ___block_literal_global.288
- ___block_literal_global.292
- ___block_literal_global.415
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SPOwner
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SPOwner
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SPOwner
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SPOwner
- _objc_msgSend$clearCacheUpdates
- _objc_msgSend$currentStewieStateWithCompletion:
- _objc_msgSend$fetchConfigFromServerWithCompletion:
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$isLocationPublishingDeviceWithCompletion:
- _objc_msgSend$isSatelliteFeatureEnabled
- _objc_msgSend$lastUpdatedStewieState
- _objc_msgSend$latestLocationFromCacheForId:completion:
- _objc_msgSend$performKeyRollWithCompletion:
- _objc_msgSend$publishCurrentLocationToStewieWithReason:completion:
- _objc_msgSend$publishLocation:completion:
- _objc_msgSend$receivedLocationCommand:completion:
- _objc_msgSend$receivedLocationPayload:completion:
- _objc_msgSend$requestLiveLocationForFriend:completion:
- _objc_msgSend$requestLiveLocationForUUID:completion:
- _objc_msgSend$setClearCacheUpdates:
- _objc_msgSend$setLastUpdatedStewieState:
- _objc_msgSend$setSharingKey:completion:
- _objc_msgSend$setStewieUpdateBlock:
- _objc_msgSend$shareCurrentKeyWithId:completion:
- _objc_msgSend$shareCurrentKeyWithId:idsHandles:completion:
- _objc_msgSend$shouldStartLocationMonitorWithCompletion:
- _objc_msgSend$simulateFeatureDisabled:completion:
- _objc_msgSend$startMonitoringStewieStateWithBlock:completion:
- _objc_msgSend$startMonitoringStewieStateWithCompletion:
- _objc_msgSend$stewiePublishStateWithCompletion:
- _objc_msgSend$stewieRetryCount
- _objc_msgSend$stewieUpdateBlock
- _objc_msgSend$stopMonitoringStewieStateWithCompletion:
- _objc_msgSend$subscribeAndFetchLocationForIds:context:completion:
- _objc_msgSend$triggerStewieProactiveNotification
- _objc_msgSend$unsubscribeForIds:context:completion:
- _objc_msgSend$updateLocationCacheWith:completion:
CStrings:
+ "SPOwnerSession.fetchFirmwareVersion"
+ "T@\"NSString\",C,N,V_findMyVersion"
+ "featureDisabledError"
+ "fetchFirmwareVersion %@"
+ "fetchHawkeyeFirmwareVersion:completion:"
+ "receivedLocationCommand called"
+ "receivedLocationPayload called"
+ "shouldStartLocationMonitor called"
+ "startMonitoringFailedSubscriptions called"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "FM_NiftyCurve"
- "Framework API: %@ currentStateWithCompletion"
- "Framework API: %@ publishCurrentLocationWithReason %ld"
- "Framework API: %@ publishStateWithCompletion "
- "Framework API: %@ startMonitoringState"
- "Framework API: %@ stopMonitoringState"
- "Framework API: %@ triggerStewieProactiveNotification "
- "Received location command"
- "Received location payload"
- "SPOwnerSession.requestLiveLocationForFriend"
- "SPOwnerSession.requestLiveLocationForUUID"
- "SPSecureLocationsClientXPCProtocol"
- "SPSecureLocationsManager %@  not notifying client since state is same as last %ld"
- "SPSecureLocationsManager %@ received updated state but no registered client block"
- "SPSecureLocationsManager %@ serviceStateChanged %ld"
- "SPSecureLocationsManager - received updated cache state and attempted to clear locations but no registered block"
- "SPSecureLocationsManager - received updated locations but no registered block"
- "SPSecureLocationsManager interruptionHandler %@"
- "SPSecureLocationsManager invalidationHandler %@"
- "SPSecureLocationsManager.clearLocationsForFailedSubscriptions"
- "SPSecureLocationsManager.hasLocationSubscribers"
- "SPSecureLocationsManager.latestKnownLocationFromCache"
- "SPSecureLocationsManager.liteLocationPublishState"
- "SPSecureLocationsManager.liteLocationServiceStateChanged"
- "SPSecureLocationsManager.publishCurrentLiteLocationWithReason"
- "SPSecureLocationsManager.receivedLocationCommand"
- "SPSecureLocationsManager.receivedLocationPayload"
- "SPSecureLocationsManager.receivedUpdatedLocations"
- "SPSecureLocationsManager.setLocationUpdateBlock"
- "SPSecureLocationsManager.startMonitoringForFailedSubscriptions"
- "SPSecureLocationsManager.startMonitoringLiteLocationState"
- "SPSecureLocationsManager.stopMonitoringLiteLocationState"
- "SPSecureLocationsManager.subscribeAndFetch"
- "SPSecureLocationsManager.subscribeAndFetchWithContext"
- "SPSecureLocationsManager.triggerStewieProactiveNotification"
- "SPSecureLocationsManager.unsubscribeWithContext"
- "SPSecureLocationsManager.updateLatestLocationCacheWith"
- "SPSecureLocationsManager: %@ - Did re-subscribed litloc update"
- "SPSecureLocationsManager: %@ - Error re-subscribing litloc update %@"
- "SPSecureLocationsManager: %@ - Will Re-subscribe liteloc due to interruption %@"
- "SPSecureLocationsManager: %@ - not re-subscribing. %@"
- "T@\"SPRetryCount\",&,N,V_stewieRetryCount"
- "T@?,C,N,V_clearCacheUpdates"
- "T@?,C,N,V_stewieUpdateBlock"
- "Tq,N,V_lastUpdatedStewieState"
- "UnsubscribeForIds %@ with context %@"
- "UnsubscribeForIds %@ with context %@ completed successfully"
- "UnsubscribeForIds %@ with context %@ failed with error %@"
- "_clearCacheUpdates"
- "_lastUpdatedStewieState"
- "_stewieRetryCount"
- "_stewieUpdateBlock"
- "clearCacheUpdates"
- "clearLocationsForFailedSubscriptions %lu"
- "clearLocationsForFailedSubscriptions:"
- "initWithDomain:code:userInfo:"
- "isSatelliteFeatureEnabled"
- "lastUpdatedStewieState"
- "latestLocationFromCache %@"
- "publishLocation "
- "publishLocation %@"
- "receivedUpdatedLocations %lu"
- "receivedUpdatedLocations:"
- "requestLiveLocationForFriend:completion:"
- "requestLiveLocationForUUID:completion:"
- "setClearCacheUpdates:"
- "setLastUpdatedStewieState:"
- "setStewieRetryCount:"
- "setStewieUpdateBlock:"
- "startMonitoringForFailedSubscriptions called"
- "startMonitoringStewieStateWithCompletion:"
- "stewieRetryCount"
- "stewieServiceStateChanged:"
- "stewieUpdateBlock"
- "subscribeAndFetchLocationForIds %@ context %@"
- "updateLatestLocationCacheWith %lu"
- "v24@0:8@?<v@?@\"SPSecureLocationsStewiePublishResult\"@\"NSError\">16"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v24@?0@\"SPSecureLocationsSubscriptionResult\"8@\"NSError\"16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"SPSecureLocation\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"SPSecureLocation\"16@?<v@?@\"NSError\">24"
- "v32@0:8q16@?<v@?@\"SPSecureLocationsStewiePublishResult\"@\"NSError\">24"
- "v40@0:8@\"NSArray\"16@\"SPSecureLocationsSubscriptionContext\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"SPSecureLocationsSubscriptionContext\"24@?<v@?@\"SPSecureLocationsSubscriptionResult\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSError\">32"

```
