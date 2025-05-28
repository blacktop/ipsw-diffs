## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-356.9.0.0.0
-  __TEXT.__text: 0x64e9c
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x81b0
-  __TEXT.__cstring: 0x5c37
+358.16.0.1.0
+  __TEXT.__text: 0x65a1c
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x8260
+  __TEXT.__cstring: 0x5c9e
   __TEXT.__const: 0x370
-  __TEXT.__gcc_except_tab: 0x1204
+  __TEXT.__gcc_except_tab: 0x127c
   __TEXT.__oslogstring: 0x61e9
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x122

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x22fc
+  __TEXT.__unwind_info: 0x2354
   __TEXT.__eh_frame: 0x240
-  __TEXT.__objc_classname: 0xf47
-  __TEXT.__objc_methname: 0x10485
-  __TEXT.__objc_methtype: 0x306d
-  __TEXT.__objc_stubs: 0x9780
+  __TEXT.__objc_classname: 0xf7b
+  __TEXT.__objc_methname: 0x10651
+  __TEXT.__objc_methtype: 0x3108
+  __TEXT.__objc_stubs: 0x9840
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x1e18
-  __DATA_CONST.__objc_classlist: 0x370
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf638
-  __DATA_CONST.__objc_selrefs: 0x3210
+  __DATA_CONST.__objc_const: 0xf808
+  __DATA_CONST.__objc_selrefs: 0x3260
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_classrefs: 0x490
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x5060
-  __AUTH_CONST.__objc_const: 0x37b0
+  __AUTH_CONST.__cfstring: 0x5080
+  __AUTH_CONST.__objc_const: 0x37f8
   __AUTH_CONST.__const: 0xaf0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH.__objc_data: 0xe08
-  __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x488
-  __DATA.__objc_superrefs: 0x2c0
-  __DATA.__objc_ivar: 0xbf0
+  __DATA.__objc_ivar: 0xc04
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x1248
+  __DATA.__data: 0x12a8
   __DATA.__bss: 0x5d0
-  __DATA_DIRTY.__objc_data: 0x1468
+  __DATA_DIRTY.__objc_data: 0x14b8
   __DATA_DIRTY.__data: 0x200
   __DATA_DIRTY.__bss: 0x310
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3540
-  Symbols:   10968
-  CStrings:  4551
+  Functions: 3567
+  Symbols:   11040
+  CStrings:  4577
 
Symbols:
+ -[SPBeaconSharingManager share:recipients:shareType:completion:]
+ -[SPOwnerInterface beaconSharingSessionWithToolingSupport]
+ -[SPOwnerSession forceRePairingWithUUID:partIds:completion:]
+ -[SPRetryCount .cxx_destruct]
+ -[SPRetryCount _decayedWaitIntervalForRetryCount:]
+ -[SPRetryCount decayWaitInterval]
+ -[SPRetryCount increment]
+ -[SPRetryCount init]
+ -[SPRetryCount reset]
+ -[SPRetryCount retryCount]
+ -[SPRetryCount serialQueue]
+ -[SPRetryCount setDecayWaitInterval:]
+ -[SPRetryCount setRetryCount:]
+ -[SPRetryCount setSerialQueue:]
+ -[SPUnauthorizedTrackingAdvertisement initWithAddress:advertisementData:status:reserved:rssi:scanDate:isPosh:networkID:]
+ -[SPUnknownBeacon isFindMyNetwork]
+ -[SPUnknownBeacon isPosh]
+ GCC_except_table105
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table138
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table172
+ GCC_except_table181
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table3
+ GCC_except_table41
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table97
+ _OBJC_CLASS_$_SPRetryCount
+ _OBJC_IVAR_$_SPRetryCount._decayWaitInterval
+ _OBJC_IVAR_$_SPRetryCount._retryCount
+ _OBJC_IVAR_$_SPRetryCount._serialQueue
+ _OBJC_IVAR_$_SPUnknownBeacon._isFindMyNetwork
+ _OBJC_IVAR_$_SPUnknownBeacon._isPosh
+ _OBJC_METACLASS_$_SPRetryCount
+ __OBJC_$_INSTANCE_METHODS_SPRetryCount
+ __OBJC_$_INSTANCE_VARIABLES_SPRetryCount
+ __OBJC_$_PROP_LIST_SPRetryCount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPBeaconSharingProtocol_ToolingSupport
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPBeaconSharingProtocol_ToolingSupport
+ __OBJC_$_PROTOCOL_REFS_SPBeaconSharingProtocol_ToolingSupport
+ __OBJC_CLASS_RO_$_SPRetryCount
+ __OBJC_LABEL_PROTOCOL_$_SPBeaconSharingProtocol_ToolingSupport
+ __OBJC_METACLASS_RO_$_SPRetryCount
+ __OBJC_PROTOCOL_$_SPBeaconSharingProtocol_ToolingSupport
+ ___21-[SPRetryCount reset]_block_invoke
+ ___25-[SPRetryCount increment]_block_invoke
+ ___29-[SPLocalBeaconManager start]_block_invoke.126
+ ___30-[SPCBPeripheralManager fetch]_block_invoke.91
+ ___32-[SPOwnerSession stopRefreshing]_block_invoke.271
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.256
+ ___33-[SPRetryCount decayWaitInterval]_block_invoke
+ ___34-[SPLocalBeaconManager timerFired]_block_invoke.149
+ ___35-[SPBTFindingSession updateConfig:]_block_invoke.68
+ ___35-[SPBeaconManager repairDataStore:]_block_invoke.281
+ ___39-[SPBeaconScanningSession stopScanning]_block_invoke.68
+ ___39-[SPLocalBeaconManager beaconsChanged:]_block_invoke.135
+ ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.267
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.252
+ ___44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.238
+ ___44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.257
+ ___44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.233
+ ___44-[SPLocalBeaconManager updateStateFromNVRAM]_block_invoke.124
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.289
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.290
+ ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.76
+ ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.9
+ ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.9.cold.1
+ ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.136
+ ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.138
+ ___47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.244
+ ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.240
+ ___48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.258
+ ___48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.259
+ ___48-[SPBeaconSharingManager receivedUpdatedShares:]_block_invoke.151
+ ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke.146
+ ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke.146.cold.1
+ ___49-[SPBeaconSharingManager acceptShare:completion:]_block_invoke.113
+ ___49-[SPBeaconSharingManager removeShare:completion:]_block_invoke.112
+ ___49-[SPBeaconSharingManager stopSharing:completion:]_block_invoke.115
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.253
+ ___50-[SPBeaconSharingManager allSharesWithCompletion:]_block_invoke.121
+ ___50-[SPBeaconSharingManager declineShare:completion:]_block_invoke.114
+ ___50-[SPBeaconSharingManager requestShare:completion:]_block_invoke.111
+ ___51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.254
+ ___51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.260
+ ___51-[SPSecureLocationsManager setLocationUpdateBlock:]_block_invoke.245
+ ___52-[SPBTFindingSession stopFindingBeacons:completion:]_block_invoke.73
+ ___53-[SPBTFindingSession startFindingBeacons:completion:]_block_invoke.72
+ ___53-[SPSecureLocationsManager receivedUpdatedLocations:]_block_invoke.242
+ ___54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.277
+ ___54-[SPBeaconSharingManager forceStopSharing:completion:]_block_invoke.120
+ ___54-[SPBeaconSharingManager share:recipients:completion:]_block_invoke.108
+ ___54-[SPBeaconSharingManager sharingLimitsWithCompletion:]_block_invoke.149
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.254
+ ___54-[SPSecureLocationsManager stewieServiceStateChanged:]_block_invoke.243
+ ___55-[SPBeaconSharingManager forceDeclineShare:completion:]_block_invoke.119
+ ___55-[SPSecureLocationsManager publishLocation:completion:]_block_invoke.252
+ ___56-[SPUnknownDiscoverySession discoveredUnknownAccessory:]_block_invoke.79
+ ___57-[SPUnknownDiscoverySession stopDiscoveryWithCompletion:]_block_invoke.78
+ ___58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.273
+ ___58-[SPLocalBeaconManager beaconingStateChangedNotification:]_block_invoke.134
+ ___58-[SPUnknownDiscoverySession startDiscoveryWithCompletion:]_block_invoke.75
+ ___59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.234
+ ___59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.269
+ ___60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.272
+ ___60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.278
+ ___60-[SPBeaconSharingManager removeExpiredSharesWithCompletion:]_block_invoke.148
+ ___60-[SPOwnerSession forceRePairingWithUUID:partIds:completion:]_block_invoke
+ ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.78
+ ___61-[SPBeaconSharingManager cleanupAllRecordsOfType:completion:]_block_invoke.116
+ ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke.126
+ ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke_2.127
+ ___62-[SPBeaconSharingManager updatedCircleIdentifiers:completion:]_block_invoke.136
+ ___63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.271
+ ___63-[SPBeaconSharingManager forceBreakAllSharesOfType:completion:]_block_invoke.117
+ ___63-[SPBeaconSharingManager lookForOrphanedRecordsWithCompletion:]_block_invoke.146
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.292
+ ___63-[SPSecureLocationsManager startMonitoringFailedSubscriptions:]_block_invoke.246
+ ___63-[SPSecureLocationsManager updateLocationCacheWith:completion:]_block_invoke.251
+ ___64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.255
+ ___64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.236
+ ___64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.235
+ ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke
+ ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke.110
+ ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke_2
+ ___65-[SPBeaconSharingManager allSharesIncludingHiddenWithCompletion:]_block_invoke.123
+ ___65-[SPBeaconSharingManager forceBreakAllSharesWithUser:completion:]_block_invoke.118
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.299
+ ___65-[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]_block_invoke.244
+ ___65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke.249
+ ___66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.237
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.258
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.258.cold.1
+ ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke.124
+ ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke_2.125
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.298
+ ___68-[SPSecureLocationsManager latestLocationFromCacheForId:completion:]_block_invoke.250
+ ___69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.265
+ ___70-[SPBeaconScanningSession startScanningIncludeServiceCharacteristics:]_block_invoke.64
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.164
+ ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.167
+ ___73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.261
+ ___73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.270
+ ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.243
+ ___75-[SPBeaconSharingManager checkDataIntegrityWithShareIdentifier:completion:]_block_invoke.144
+ ___75-[SPUnknownDiscoverySession startDiscoveryWithScanRate:timeout:completion:]_block_invoke.77
+ ___76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.256
+ ___77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.268
+ ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.77
+ ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.74
+ ___79-[SPSecureLocationsManager subscribeAndFetchLocationForIds:context:completion:]_block_invoke.248
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.296
+ ___81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.267
+ ___83-[SPBeaconSharingManager downloadKeysWithCircleIdentifier:fromBookmark:completion:]_block_invoke.135
+ ___83-[SPLocalBeaconManager(KeyGeneration) generateOfflineAdvertisingKeysForReason:now:]_block_invoke.406
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.294
+ ___84-[SPBeaconSharingManager uploadKeysWithCircleIdentifier:isInitialUpload:completion:]_block_invoke.134
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.262
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.263
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.264
+ ___block_literal_global.167
+ ___block_literal_global.170
+ ___block_literal_global.175
+ ___block_literal_global.181
+ ___block_literal_global.188
+ ___block_literal_global.198
+ ___block_literal_global.248
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.415
+ ___block_literal_global.54
+ ___block_literal_global.56
+ ___block_literal_global.61
+ ___block_literal_global.63
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.76
+ _objc_msgSend$decayWaitInterval
+ _objc_msgSend$forceRePairingWithUUID:partIds:completion:
+ _objc_msgSend$increment
+ _objc_msgSend$initWithAddress:advertisementData:status:reserved:rssi:scanDate:isPosh:networkID:
+ _objc_msgSend$reset
+ _objc_msgSend$retryCount
+ _objc_msgSend$share:recipients:shareType:completion:
+ _objc_msgSend$stewieRetryCount
+ _objc_retain_x7
+ _swift_release_n
- -[SPBeaconSharingManager _decayedWaitIntervalForRetryCount:]
- -[SPOwnerSessionLocationFetch _decayedWaitIntervalForRetryCount:]
- -[SPSecureLocationsManager _decayedWaitIntervalForRetryCount:]
- GCC_except_table102
- GCC_except_table108
- GCC_except_table111
- GCC_except_table124
- GCC_except_table146
- GCC_except_table150
- GCC_except_table153
- GCC_except_table157
- GCC_except_table162
- GCC_except_table165
- GCC_except_table168
- GCC_except_table179
- GCC_except_table184
- GCC_except_table189
- GCC_except_table194
- GCC_except_table38
- GCC_except_table46
- GCC_except_table50
- GCC_except_table54
- GCC_except_table58
- GCC_except_table66
- GCC_except_table73
- GCC_except_table74
- GCC_except_table78
- GCC_except_table82
- GCC_except_table84
- GCC_except_table87
- GCC_except_table90
- GCC_except_table94
- ___29-[SPLocalBeaconManager start]_block_invoke.125
- ___30-[SPCBPeripheralManager fetch]_block_invoke.90
- ___32-[SPOwnerSession stopRefreshing]_block_invoke.268
- ___33-[SPOwnerSession executeCommand:]_block_invoke.253
- ___34-[SPLocalBeaconManager timerFired]_block_invoke.148
- ___35-[SPBTFindingSession updateConfig:]_block_invoke.67
- ___35-[SPBeaconManager repairDataStore:]_block_invoke.280
- ___39-[SPBeaconScanningSession stopScanning]_block_invoke.67
- ___39-[SPLocalBeaconManager beaconsChanged:]_block_invoke.134
- ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.264
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.249
- ___44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.237
- ___44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.256
- ___44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.232
- ___44-[SPLocalBeaconManager updateStateFromNVRAM]_block_invoke.123
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.286
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.287
- ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.75
- ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.8
- ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.8.cold.1
- ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.135
- ___46-[SPLocalBeaconManager beaconingStateChanged:]_block_invoke.137
- ___47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.243
- ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.238
- ___48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.257
- ___48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.258
- ___48-[SPBeaconSharingManager receivedUpdatedShares:]_block_invoke.148
- ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke.145
- ___48-[SPSecureLocationsManager interruptionHandler:]_block_invoke.145.cold.1
- ___49-[SPBeaconSharingManager acceptShare:completion:]_block_invoke.110
- ___49-[SPBeaconSharingManager removeShare:completion:]_block_invoke.109
- ___49-[SPBeaconSharingManager stopSharing:completion:]_block_invoke.112
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.250
- ___50-[SPBeaconSharingManager allSharesWithCompletion:]_block_invoke.118
- ___50-[SPBeaconSharingManager declineShare:completion:]_block_invoke.111
- ___50-[SPBeaconSharingManager requestShare:completion:]_block_invoke.108
- ___51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.253
- ___51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.259
- ___51-[SPSecureLocationsManager setLocationUpdateBlock:]_block_invoke.243
- ___52-[SPBTFindingSession stopFindingBeacons:completion:]_block_invoke.72
- ___53-[SPBTFindingSession startFindingBeacons:completion:]_block_invoke.71
- ___53-[SPSecureLocationsManager receivedUpdatedLocations:]_block_invoke.240
- ___54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.276
- ___54-[SPBeaconSharingManager forceStopSharing:completion:]_block_invoke.117
- ___54-[SPBeaconSharingManager share:recipients:completion:]_block_invoke.106
- ___54-[SPBeaconSharingManager sharingLimitsWithCompletion:]_block_invoke.146
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.251
- ___54-[SPSecureLocationsManager stewieServiceStateChanged:]_block_invoke.241
- ___55-[SPBeaconSharingManager forceDeclineShare:completion:]_block_invoke.116
- ___55-[SPSecureLocationsManager publishLocation:completion:]_block_invoke.250
- ___56-[SPUnknownDiscoverySession discoveredUnknownAccessory:]_block_invoke.78
- ___57-[SPUnknownDiscoverySession stopDiscoveryWithCompletion:]_block_invoke.77
- ___58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.272
- ___58-[SPLocalBeaconManager beaconingStateChangedNotification:]_block_invoke.133
- ___58-[SPUnknownDiscoverySession startDiscoveryWithCompletion:]_block_invoke.74
- ___59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.233
- ___59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.268
- ___60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.271
- ___60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.277
- ___60-[SPBeaconSharingManager removeExpiredSharesWithCompletion:]_block_invoke.145
- ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.77
- ___61-[SPBeaconSharingManager cleanupAllRecordsOfType:completion:]_block_invoke.113
- ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke.123
- ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke_2.124
- ___62-[SPBeaconSharingManager updatedCircleIdentifiers:completion:]_block_invoke.133
- ___63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.270
- ___63-[SPBeaconSharingManager forceBreakAllSharesOfType:completion:]_block_invoke.114
- ___63-[SPBeaconSharingManager lookForOrphanedRecordsWithCompletion:]_block_invoke.143
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.289
- ___63-[SPSecureLocationsManager startMonitoringFailedSubscriptions:]_block_invoke.244
- ___63-[SPSecureLocationsManager updateLocationCacheWith:completion:]_block_invoke.249
- ___64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.254
- ___64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.235
- ___64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.234
- ___65-[SPBeaconSharingManager allSharesIncludingHiddenWithCompletion:]_block_invoke.120
- ___65-[SPBeaconSharingManager forceBreakAllSharesWithUser:completion:]_block_invoke.115
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.296
- ___65-[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]_block_invoke.242
- ___65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke.247
- ___66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.236
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.255
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.255.cold.1
- ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke.121
- ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke_2.122
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.295
- ___68-[SPSecureLocationsManager latestLocationFromCacheForId:completion:]_block_invoke.248
- ___69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.264
- ___70-[SPBeaconScanningSession startScanningIncludeServiceCharacteristics:]_block_invoke.63
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.163
- ___70-[SPLocalBeaconManager notifyBeaconingKeysChangedBlockWithCompletion:]_block_invoke.165
- ___73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.260
- ___73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.269
- ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.241
- ___75-[SPBeaconSharingManager checkDataIntegrityWithShareIdentifier:completion:]_block_invoke.141
- ___75-[SPUnknownDiscoverySession startDiscoveryWithScanRate:timeout:completion:]_block_invoke.76
- ___76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.255
- ___77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.267
- ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.76
- ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.73
- ___79-[SPSecureLocationsManager subscribeAndFetchLocationForIds:context:completion:]_block_invoke.246
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.293
- ___81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.266
- ___83-[SPBeaconSharingManager downloadKeysWithCircleIdentifier:fromBookmark:completion:]_block_invoke.132
- ___83-[SPLocalBeaconManager(KeyGeneration) generateOfflineAdvertisingKeysForReason:now:]_block_invoke.405
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.291
- ___84-[SPBeaconSharingManager uploadKeysWithCircleIdentifier:isInitialUpload:completion:]_block_invoke.131
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.259
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.260
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.261
- ___block_literal_global.166
- ___block_literal_global.169
- ___block_literal_global.174
- ___block_literal_global.180
- ___block_literal_global.187
- ___block_literal_global.196
- ___block_literal_global.247
- ___block_literal_global.267
- ___block_literal_global.275
- ___block_literal_global.414
- ___block_literal_global.59
- ___block_literal_global.66
- ___block_literal_global.69
- ___block_literal_global.75
- _objc_msgSend$setStewieRetryCount:
- _objc_msgSend$share:recipients:completion:
CStrings:
+ "\a\x11"
+ "@\"SPRetryCount\""
+ "@68@0:8@16@24C32@36q44@52B60C64"
+ "Owner Play Sound Count: %u\n"
+ "Owner Play Sound Time: %u\n"
+ "Ranging Count: %u\n"
+ "Ranging Time: %u\n"
+ "SPBeaconSharingProtocol_ToolingSupport"
+ "SPRetryCount"
+ "T@\"NSString\",?,R,C"
+ "T@\"SPRetryCount\",&,N,V_retryCount"
+ "T@\"SPRetryCount\",&,N,V_stewieRetryCount"
+ "TB,R,N,V_isFindMyNetwork"
+ "TB,R,N,V_isPosh"
+ "Td,N,V_decayWaitInterval"
+ "_decayWaitInterval"
+ "_isFindMyNetwork"
+ "_isPosh"
+ "beaconSharingSessionWithToolingSupport"
+ "com.apple.SPOwner.retryCountQueue"
+ "com.apple.icloud.spowner.task.stopBTFinding"
+ "decayWaitInterval"
+ "forceRePairingWithUUID:partIds:completion:"
+ "increment"
+ "initWithAddress:advertisementData:status:reserved:rssi:scanDate:isPosh:networkID:"
+ "isFindMyNetwork"
+ "isPosh"
+ "reset"
+ "setDecayWaitInterval:"
+ "share:recipients:shareType:completion:"
+ "v40@0:8@\"NSUUID\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSUUID\"16@\"NSSet\"24Q32@?<v@?B@\"NSDictionary\">40"
- "\x04\x11"
- "Owner Play Sound Count: %d\n"
- "Owner Play Sound Time: %d\n"
- "Ranging Count: %d\n"
- "Ranging Time: %d\n"
- "TQ,N,V_stewieRetryCount"

```
