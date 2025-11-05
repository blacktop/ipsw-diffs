## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

-396.23.10.29.6
-  __TEXT.__text: 0x76414
+396.24.7.11.41
+  __TEXT.__text: 0x7ab54
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x8ef8
-  __TEXT.__cstring: 0x615e
+  __TEXT.__objc_methlist: 0xaddc
+  __TEXT.__cstring: 0x6457
   __TEXT.__const: 0x440
-  __TEXT.__oslogstring: 0x7288
+  __TEXT.__oslogstring: 0x74e8
   __TEXT.__gcc_except_tab: 0x1b24
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x50
-  __TEXT.__unwind_info: 0x21b0
-  __TEXT.__eh_frame: 0x250
-  __TEXT.__objc_classname: 0x11d4
-  __TEXT.__objc_methname: 0x11bc2
-  __TEXT.__objc_methtype: 0x36e2
-  __TEXT.__objc_stubs: 0xa360
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__const: 0x808
-  __DATA_CONST.__objc_classlist: 0x3f0
-  __DATA_CONST.__objc_protolist: 0x1a8
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0x22f0
+  __TEXT.__eh_frame: 0x278
+  __TEXT.__objc_classname: 0x1278
+  __TEXT.__objc_methname: 0x125c4
+  __TEXT.__objc_methtype: 0x3891
+  __TEXT.__objc_stubs: 0xa7c0
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__objc_classlist: 0x408
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35f8
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x320
+  __DATA_CONST.__objc_selrefs: 0x3978
+  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x5a0
-  __AUTH_CONST.__const: 0x2000
-  __AUTH_CONST.__cfstring: 0x57a0
-  __AUTH_CONST.__objc_const: 0x14fc0
+  __AUTH_CONST.__const: 0x2080
+  __AUTH_CONST.__cfstring: 0x5a60
+  __AUTH_CONST.__objc_const: 0x12ad8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1890
+  __AUTH.__objc_data: 0x1960
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0xd24
-  __DATA.__data: 0x14a8
-  __DATA.__bss: 0x8c0
+  __DATA.__objc_ivar: 0xdb4
+  __DATA.__data: 0x1568
+  __DATA.__bss: 0x8e0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CDC579A9-6A93-33C6-BFBE-38584267BC48
-  Functions: 3847
-  Symbols:   8255
-  CStrings:  5602
+  UUID: 2C1592A3-5368-3895-BD14-43ED65DF4F01
+  Functions: 4034
+  Symbols:   8581
+  CStrings:  5767
 
Symbols:
+ +[SPAccessoryDiscoveryAndPairingSession exportedInterface].cold.1
+ +[SPAccessoryDiscoveryAndPairingSession remoteInterface].cold.1
+ +[SPBTFindingSession exportedInterface].cold.1
+ +[SPBTFindingSession remoteInterface].cold.1
+ +[SPBeaconManagerSimpleBeaconUpdateInterface exportedInterface].cold.1
+ +[SPBeaconManagerSimpleBeaconUpdateInterface remoteInterface].cold.1
+ +[SPBeaconScanningSession exportedInterface].cold.1
+ +[SPBeaconScanningSession remoteInterface].cold.1
+ +[SPBeaconSharingManager exportedInterface].cold.1
+ +[SPBeaconSharingManager remoteInterface].cold.1
+ +[SPCBLeechScanner remoteInterface].cold.1
+ +[SPCBPeripheralManager remoteInterface].cold.1
+ +[SPCertificationAssistantSession beaconsChanges:]
+ +[SPCertificationAssistantSession unifiedBeacons:]
+ +[SPLocalFindableConnectionMaterialMonitoringSession exportedInterface].cold.1
+ +[SPLocalFindableConnectionMaterialMonitoringSession remoteInterface].cold.1
+ +[SPMetadataFetchingSession exportedInterface]
+ +[SPMetadataFetchingSession exportedInterface].cold.1
+ +[SPMetadataFetchingSession remoteInterface]
+ +[SPMetadataFetchingSession remoteInterface].cold.1
+ +[SPOwnerInterface cbPeripheralManagementSession].cold.1
+ +[SPOwnerSessionDelegatedLocation exportedInterface].cold.1
+ +[SPOwnerSessionDelegatedLocation remoteInterface].cold.1
+ +[SPOwnerSessionLocationFetch exportedInterface].cold.1
+ +[SPOwnerSessionLocationFetch remoteInterface].cold.1
+ +[SPSecureLocationsManager exportedInterface].cold.1
+ +[SPSecureLocationsManager remoteInterface].cold.1
+ +[SPSimpleBeaconContext fmcaContext]
+ +[SPUnknownDiscoverySession exportedInterface].cold.1
+ +[SPUnknownDiscoverySession remoteInterface].cold.1
+ -[SPAccessoryDiscoveryAndPairingSession accessoryProximityPairingError:]
+ -[SPAccessoryDiscoveryAndPairingSession finalizeProximityPairingForAccessoryIdentifier:configuration:completion:]
+ -[SPAccessoryDiscoveryAndPairingSession initializeProximityPairingForAccessoryIdentifier:completion:]
+ -[SPAccessoryDiscoveryAndPairingSession proximityPairingCompleted:beacons:]
+ -[SPAccessoryDiscoveryAndPairingSession proximityPairingCompletedCallback]
+ -[SPAccessoryDiscoveryAndPairingSession proximityPairingErrorCallback]
+ -[SPAccessoryDiscoveryAndPairingSession proximityPairingFinished:]
+ -[SPAccessoryDiscoveryAndPairingSession proximityPairingFinishedCallback]
+ -[SPAccessoryDiscoveryAndPairingSession setProximityPairingCompletedCallback:]
+ -[SPAccessoryDiscoveryAndPairingSession setProximityPairingErrorCallback:]
+ -[SPAccessoryDiscoveryAndPairingSession setProximityPairingFinishedCallback:]
+ -[SPBeaconObservation initWithBeaconIdentifier:type:date:location:].cold.1
+ -[SPBeaconObservation initWithBeaconIdentifier:type:date:location:].cold.2
+ -[SPCertificationAssistantBeacon .cxx_destruct]
+ -[SPCertificationAssistantBeacon accessoryProductInfo]
+ -[SPCertificationAssistantBeacon identifier]
+ -[SPCertificationAssistantBeacon initWithInternalSimpleBeacon:]
+ -[SPCertificationAssistantBeacon model]
+ -[SPCertificationAssistantBeacon name]
+ -[SPCertificationAssistantBeacon productId]
+ -[SPCertificationAssistantBeacon rawMetadata]
+ -[SPCertificationAssistantBeacon role]
+ -[SPCertificationAssistantBeacon setAccessoryProductInfo:]
+ -[SPCertificationAssistantBeacon setIdentifier:]
+ -[SPCertificationAssistantBeacon setModel:]
+ -[SPCertificationAssistantBeacon setName:]
+ -[SPCertificationAssistantBeacon setProductId:]
+ -[SPCertificationAssistantBeacon setRawMetadata:]
+ -[SPCertificationAssistantBeacon setRole:]
+ -[SPCertificationAssistantBeacon setSystemVersion:]
+ -[SPCertificationAssistantBeacon setTaskInformation:]
+ -[SPCertificationAssistantBeacon setType:]
+ -[SPCertificationAssistantBeacon setVendorId:]
+ -[SPCertificationAssistantBeacon systemVersion]
+ -[SPCertificationAssistantBeacon taskInformation]
+ -[SPCertificationAssistantBeacon type]
+ -[SPCertificationAssistantBeacon vendorId]
+ -[SPCertificationAssistantSession .cxx_destruct]
+ -[SPCertificationAssistantSession init]
+ -[SPCertificationAssistantSession queue]
+ -[SPCertificationAssistantSession registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:]
+ -[SPCertificationAssistantSession setQueue:]
+ -[SPCertificationAssistantSession setSimpleBeaconUpdateInterface:]
+ -[SPCertificationAssistantSession simpleBeaconUpdateInterface]
+ -[SPCertificationAssistantSession startUpdatingBeaconsWithContext:collectionDifference:completion:]
+ -[SPCertificationAssistantSession stopUpdatingBeaconsWithCompletion:]
+ -[SPDiscoveredAccessoryMetadata rawMetadata]
+ -[SPDiscoveredAccessoryMetadata setRawMetadata:]
+ -[SPInternalSimpleBeacon batteryPercentage]
+ -[SPInternalSimpleBeacon deviceClass]
+ -[SPInternalSimpleBeacon deviceColor]
+ -[SPInternalSimpleBeacon deviceDisplayName]
+ -[SPInternalSimpleBeacon deviceModel]
+ -[SPInternalSimpleBeacon isMine]
+ -[SPInternalSimpleBeacon lowPowerMode]
+ -[SPInternalSimpleBeacon multipartStatus]
+ -[SPInternalSimpleBeacon online]
+ -[SPInternalSimpleBeacon rawMetadata]
+ -[SPInternalSimpleBeacon setBatteryPercentage:]
+ -[SPInternalSimpleBeacon setDeviceClass:]
+ -[SPInternalSimpleBeacon setDeviceColor:]
+ -[SPInternalSimpleBeacon setDeviceDisplayName:]
+ -[SPInternalSimpleBeacon setDeviceModel:]
+ -[SPInternalSimpleBeacon setIsMine:]
+ -[SPInternalSimpleBeacon setLowPowerMode:]
+ -[SPInternalSimpleBeacon setMultipartStatus:]
+ -[SPInternalSimpleBeacon setOnline:]
+ -[SPInternalSimpleBeacon setRawMetadata:]
+ -[SPInternalSimpleBeacon setThisDevice:]
+ -[SPInternalSimpleBeacon thisDevice]
+ -[SPMetadataFetchingSession .cxx_destruct]
+ -[SPMetadataFetchingSession callbackQueue]
+ -[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]
+ -[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]
+ -[SPMetadataFetchingSession fetchBatteryStatusData:completion:]
+ -[SPMetadataFetchingSession fetchBatteryTypeData:completion:]
+ -[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]
+ -[SPMetadataFetchingSession fetchManufacturerNameData:completion:]
+ -[SPMetadataFetchingSession fetchModelColorCodeData:completion:]
+ -[SPMetadataFetchingSession fetchModelNameData:completion:]
+ -[SPMetadataFetchingSession fetchProductData:completion:]
+ -[SPMetadataFetchingSession fetchProtocolVersionData:completion:]
+ -[SPMetadataFetchingSession init]
+ -[SPMetadataFetchingSession interruptionHandler:]
+ -[SPMetadataFetchingSession invalidationHandler:]
+ -[SPMetadataFetchingSession proxy]
+ -[SPMetadataFetchingSession queue]
+ -[SPMetadataFetchingSession serviceDescription]
+ -[SPMetadataFetchingSession sessionInvalidatedCallback]
+ -[SPMetadataFetchingSession session]
+ -[SPMetadataFetchingSession setCallbackQueue:]
+ -[SPMetadataFetchingSession setProxy:]
+ -[SPMetadataFetchingSession setQueue:]
+ -[SPMetadataFetchingSession setServiceDescription:]
+ -[SPMetadataFetchingSession setSession:]
+ -[SPMetadataFetchingSession setSessionInvalidatedCallback:]
+ -[SPMonitorsWrapper _cpuType].cold.1
+ -[SPOwnerInterface certificationAssistantSession]
+ -[SPRawAccessoryMetadata networkId]
+ -[SPRawAccessoryMetadata protocolVersion]
+ -[SPRawAccessoryMetadata setNetworkId:]
+ -[SPRawAccessoryMetadata setProtocolVersion:]
+ -[SPSecureLocationsManager getAllSharedKeysWithCompletion:]
+ -[SPSecureLocationsManager getSharingKeyWithCompletion:]
+ -[SPSecureLocationsManager processIDSServiceMessage:completion:]
+ -[SPSecureLocationsManager setSharingKey:completion:]
+ LogCategory_AccessoryDiscovery.cold.1
+ LogCategory_BTFinding.cold.1
+ LogCategory_BeaconManager.cold.1
+ LogCategory_BeaconScanning.cold.1
+ LogCategory_BeaconSharing.cold.1
+ LogCategory_CBPeripheralManagement.cold.1
+ LogCategory_Crypto.cold.1
+ LogCategory_FirmwareUpdate.cold.1
+ LogCategory_LocalFindableConnectionMaterialMonitoring.cold.1
+ LogCategory_LocationFetch.cold.1
+ LogCategory_MaintenanceConnection.cold.1
+ LogCategory_OfflineAdvertising.cold.1
+ LogCategory_OwnerSession.cold.1
+ LogCategory_PowerManagement.cold.1
+ LogCategory_SecureLocations.cold.1
+ LogCategory_ServiceState.cold.1
+ LogCategory_SimpleBeaconUpdateInterface.cold.1
+ LogCategory_SystemHealth.cold.1
+ LogCategory_UnknownDiscovery.cold.1
+ LogCategory_Unspecified.cold.1
+ OBJC_IVAR_$_SPAccessoryDiscoveryAndPairingSession._proximityPairingCompletedCallback
+ OBJC_IVAR_$_SPAccessoryDiscoveryAndPairingSession._proximityPairingErrorCallback
+ OBJC_IVAR_$_SPAccessoryDiscoveryAndPairingSession._proximityPairingFinishedCallback
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._accessoryProductInfo
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._identifier
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._model
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._name
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._productId
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._rawMetadata
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._role
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._systemVersion
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._taskInformation
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._type
+ OBJC_IVAR_$_SPCertificationAssistantBeacon._vendorId
+ OBJC_IVAR_$_SPCertificationAssistantSession._queue
+ OBJC_IVAR_$_SPCertificationAssistantSession._simpleBeaconUpdateInterface
+ OBJC_IVAR_$_SPDiscoveredAccessoryMetadata._rawMetadata
+ OBJC_IVAR_$_SPInternalSimpleBeacon._batteryPercentage
+ OBJC_IVAR_$_SPInternalSimpleBeacon._deviceClass
+ OBJC_IVAR_$_SPInternalSimpleBeacon._deviceColor
+ OBJC_IVAR_$_SPInternalSimpleBeacon._deviceDisplayName
+ OBJC_IVAR_$_SPInternalSimpleBeacon._deviceModel
+ OBJC_IVAR_$_SPInternalSimpleBeacon._isMine
+ OBJC_IVAR_$_SPInternalSimpleBeacon._lowPowerMode
+ OBJC_IVAR_$_SPInternalSimpleBeacon._multipartStatus
+ OBJC_IVAR_$_SPInternalSimpleBeacon._online
+ OBJC_IVAR_$_SPInternalSimpleBeacon._rawMetadata
+ OBJC_IVAR_$_SPInternalSimpleBeacon._thisDevice
+ OBJC_IVAR_$_SPMetadataFetchingSession._callbackQueue
+ OBJC_IVAR_$_SPMetadataFetchingSession._proxy
+ OBJC_IVAR_$_SPMetadataFetchingSession._queue
+ OBJC_IVAR_$_SPMetadataFetchingSession._serviceDescription
+ OBJC_IVAR_$_SPMetadataFetchingSession._session
+ OBJC_IVAR_$_SPMetadataFetchingSession._sessionInvalidatedCallback
+ OBJC_IVAR_$_SPRawAccessoryMetadata._networkId
+ OBJC_IVAR_$_SPRawAccessoryMetadata._protocolVersion
+ _OBJC_CLASS_$_SPCertificationAssistantBeacon
+ _OBJC_CLASS_$_SPCertificationAssistantSession
+ _OBJC_CLASS_$_SPMetadataFetchingSession
+ _OBJC_METACLASS_$_SPCertificationAssistantBeacon
+ _OBJC_METACLASS_$_SPCertificationAssistantSession
+ _OBJC_METACLASS_$_SPMetadataFetchingSession
+ _SPAccessoryProximityDiscoveryAndPairingSessionErrorDomain
+ _SPBeaconTypeFindMyService
+ _SPCertificationAssistantErrorDomain
+ _SPRemoteUIAlertTypeValueProximityPairing
+ _SPRemoteUIDeviceStateKey
+ _SPRemoteUIEngravingDataKey
+ _SPRemoteUIPairingAccessoryTypeKey
+ _SPRemoteUIPairingColorKey
+ _SPRemoteUIPairingIdentifierKey
+ _SPRemoteUIPairingInfoKey
+ _SPRemoteUIUserNameKey
+ __32-[SPOwnerSession stopRefreshing]_block_invoke.311
+ __33-[SPMetadataFetchingSession init]_block_invoke.3
+ __33-[SPOwnerSession executeCommand:]_block_invoke.279
+ __35-[SPBeaconManager repairDataStore:]_block_invoke.304
+ __42-[SPOwnerSession registerIntentTimerFired]_block_invoke.303
+ __43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.267
+ __44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.228
+ __44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.261
+ __44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.223
+ __44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.343
+ __44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.344
+ __45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.196
+ __46-[SPAccessoryDiscoveryAndPairingSession proxy]_block_invoke.102
+ __47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.238
+ __48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.229
+ __48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.230
+ __48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.262
+ __48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.263
+ __49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.270
+ __51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.257
+ __51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.268
+ __51-[SPSecureLocationsManager setLocationUpdateBlock:]_block_invoke.198
+ __53-[SPSecureLocationsManager receivedUpdatedLocations:]_block_invoke.196
+ __54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.302
+ __54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.271
+ __55-[SPSecureLocationsManager publishLocation:completion:]_block_invoke.209
+ __57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.206
+ __58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.298
+ __59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.224
+ __59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.290
+ __59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.208
+ __60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.297
+ __60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.303
+ __61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.198
+ __61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.213
+ __63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.296
+ __63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.214
+ __63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.356
+ __63-[SPSecureLocationsManager startMonitoringFailedSubscriptions:]_block_invoke.200
+ __63-[SPSecureLocationsManager updateLocationCacheWith:completion:]_block_invoke.208
+ __64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.258
+ __64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.226
+ __64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.225
+ __64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.215
+ __65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.212
+ __65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.210
+ __65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.376
+ __65-[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]_block_invoke.197
+ __65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke.203
+ __66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.227
+ __66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.207
+ __67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.209
+ __67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.282
+ __67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.282.cold.1
+ __68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.373
+ __68-[SPSecureLocationsManager latestLocationFromCacheForId:completion:]_block_invoke.205
+ __69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.276
+ __71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.211
+ __73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.269
+ __73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.291
+ __73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.357
+ __75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.232
+ __75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.233
+ __76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.260
+ __77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.285
+ __78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.197
+ __79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.193
+ __79-[SPSecureLocationsManager subscribeAndFetchLocationForIds:context:completion:]_block_invoke.202
+ __80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.358
+ __80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.369
+ __81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.280
+ __83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.365
+ __89-[SPBeaconManager startUpdatingSimpleBeaconsWithContext:collectionDifference:completion:]_block_invoke.249
+ __89-[SPBeaconManager startUpdatingSimpleBeaconsWithContext:collectionDifference:completion:]_block_invoke_2.250
+ __89-[SPBeaconManager startUpdatingSimpleBeaconsWithContext:collectionDifference:completion:]_block_invoke_3.251
+ __91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.201
+ __92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.200
+ __93-[SPOwnerSession startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:]_block_invoke.332
+ __93-[SPOwnerSession startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:]_block_invoke_2.333
+ __93-[SPOwnerSession startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:]_block_invoke_3.334
+ __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.292
+ __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.293
+ __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.297
+ __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.298
+ __OBJC_$_CLASS_METHODS_SPCertificationAssistantSession
+ __OBJC_$_CLASS_METHODS_SPMetadataFetchingSession
+ __OBJC_$_INSTANCE_METHODS_SPCertificationAssistantBeacon
+ __OBJC_$_INSTANCE_METHODS_SPCertificationAssistantSession
+ __OBJC_$_INSTANCE_METHODS_SPMetadataFetchingSession
+ __OBJC_$_INSTANCE_VARIABLES_SPCertificationAssistantBeacon
+ __OBJC_$_INSTANCE_VARIABLES_SPCertificationAssistantSession
+ __OBJC_$_INSTANCE_VARIABLES_SPMetadataFetchingSession
+ __OBJC_$_PROP_LIST_SPCertificationAssistantBeacon
+ __OBJC_$_PROP_LIST_SPCertificationAssistantSession
+ __OBJC_$_PROP_LIST_SPMetadataFetchingSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPCertificationAssistantProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPCertificationAssistantProtocol
+ __OBJC_$_PROTOCOL_REFS_SPCertificationAssistantProtocol
+ __OBJC_$_PROTOCOL_REFS_SPMetadataFetchingXPCClientProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SPCertificationAssistantSession
+ __OBJC_CLASS_PROTOCOLS_$_SPMetadataFetchingSession
+ __OBJC_CLASS_RO_$_SPCertificationAssistantBeacon
+ __OBJC_CLASS_RO_$_SPCertificationAssistantSession
+ __OBJC_CLASS_RO_$_SPMetadataFetchingSession
+ __OBJC_LABEL_PROTOCOL_$_SPCertificationAssistantProtocol
+ __OBJC_LABEL_PROTOCOL_$_SPMetadataFetchingXPCClientProtocol
+ __OBJC_METACLASS_RO_$_SPCertificationAssistantBeacon
+ __OBJC_METACLASS_RO_$_SPCertificationAssistantSession
+ __OBJC_METACLASS_RO_$_SPMetadataFetchingSession
+ __OBJC_PROTOCOL_$_SPCertificationAssistantProtocol
+ __OBJC_PROTOCOL_$_SPMetadataFetchingXPCClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SPMetadataFetchingXPCClientProtocol
+ ___101-[SPAccessoryDiscoveryAndPairingSession initializeProximityPairingForAccessoryIdentifier:completion:]_block_invoke
+ ___108-[SPCertificationAssistantSession registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:]_block_invoke
+ ___113-[SPAccessoryDiscoveryAndPairingSession finalizeProximityPairingForAccessoryIdentifier:configuration:completion:]_block_invoke
+ ___33-[SPMetadataFetchingSession init]_block_invoke
+ ___44+[SPMetadataFetchingSession remoteInterface]_block_invoke
+ ___46+[SPMetadataFetchingSession exportedInterface]_block_invoke
+ ___49-[SPMetadataFetchingSession interruptionHandler:]_block_invoke
+ ___49-[SPMetadataFetchingSession invalidationHandler:]_block_invoke
+ ___50+[SPCertificationAssistantSession beaconsChanges:]_block_invoke
+ ___50+[SPCertificationAssistantSession unifiedBeacons:]_block_invoke
+ ___53-[SPSecureLocationsManager setSharingKey:completion:]_block_invoke
+ ___56-[SPSecureLocationsManager getSharingKeyWithCompletion:]_block_invoke
+ ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke
+ ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke
+ ___59-[SPSecureLocationsManager getAllSharedKeysWithCompletion:]_block_invoke
+ ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke
+ ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke
+ ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke
+ ___64-[SPSecureLocationsManager processIDSServiceMessage:completion:]_block_invoke
+ ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke
+ ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke
+ ___66-[SPAccessoryDiscoveryAndPairingSession proximityPairingFinished:]_block_invoke
+ ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke
+ ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke
+ ___69-[SPCertificationAssistantSession stopUpdatingBeaconsWithCompletion:]_block_invoke
+ ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke
+ ___72-[SPAccessoryDiscoveryAndPairingSession accessoryProximityPairingError:]_block_invoke
+ ___75-[SPAccessoryDiscoveryAndPairingSession proximityPairingCompleted:beacons:]_block_invoke
+ ___99-[SPCertificationAssistantSession startUpdatingBeaconsWithContext:collectionDifference:completion:]_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.168
+ __block_literal_global.242
+ __block_literal_global.301
+ __block_literal_global.310
+ __block_literal_global.313
+ __block_literal_global.324
+ __block_literal_global.53
+ __block_literal_global.8
+ _objc_msgSend$batteryPercentage
+ _objc_msgSend$beaconsChanges:
+ _objc_msgSend$boolValue
+ _objc_msgSend$deviceClass
+ _objc_msgSend$deviceColor
+ _objc_msgSend$deviceDisplayName
+ _objc_msgSend$deviceModel
+ _objc_msgSend$fetchHawkeyeAIS:metadataType:completion:
+ _objc_msgSend$finalizeProximityPairingForAccessoryIdentifier:configuration:completion:
+ _objc_msgSend$getAllSharedKeysWithCompletion:
+ _objc_msgSend$getSharingKeyWithCompletion:
+ _objc_msgSend$initializeProximityPairingForAccessoryIdentifier:completion:
+ _objc_msgSend$isMine
+ _objc_msgSend$lowPowerMode
+ _objc_msgSend$networkId
+ _objc_msgSend$online
+ _objc_msgSend$processIDSServiceMessage:completion:
+ _objc_msgSend$proximityPairingCompletedCallback
+ _objc_msgSend$proximityPairingErrorCallback
+ _objc_msgSend$proximityPairingFinishedCallback
+ _objc_msgSend$rawMetadata
+ _objc_msgSend$registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:
+ _objc_msgSend$setBatteryPercentage:
+ _objc_msgSend$setDeviceClass:
+ _objc_msgSend$setDeviceColor:
+ _objc_msgSend$setDeviceDisplayName:
+ _objc_msgSend$setDeviceModel:
+ _objc_msgSend$setIsMine:
+ _objc_msgSend$setLowPowerMode:
+ _objc_msgSend$setNetworkId:
+ _objc_msgSend$setOnline:
+ _objc_msgSend$setRawMetadata:
+ _objc_msgSend$setSharingKey:completion:
+ _objc_msgSend$setThisDevice:
+ _objc_msgSend$thisDevice
+ allBeaconTypes.cold.1
+ serviceSettingsChangedTrampoline.cold.1
- __32-[SPOwnerSession stopRefreshing]_block_invoke.309
- __33-[SPOwnerSession executeCommand:]_block_invoke.277
- __35-[SPBeaconManager repairDataStore:]_block_invoke.325
- __42-[SPOwnerSession registerIntentTimerFired]_block_invoke.301
- __43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.265
- __44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.249
- __44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.282
- __44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.244
- __44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.341
- __44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.342
- __45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.177
- __46-[SPAccessoryDiscoveryAndPairingSession proxy]_block_invoke.99
- __47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.259
- __48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.250
- __48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.251
- __48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.283
- __48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.284
- __49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.268
- __51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.278
- __51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.289
- __51-[SPSecureLocationsManager setLocationUpdateBlock:]_block_invoke.193
- __53-[SPSecureLocationsManager receivedUpdatedLocations:]_block_invoke.191
- __54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.323
- __54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.269
- __55-[SPSecureLocationsManager publishLocation:completion:]_block_invoke.204
- __58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.319
- __59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.245
- __59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.311
- __60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.318
- __60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.324
- __61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.179
- __63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.317
- __63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.354
- __63-[SPSecureLocationsManager startMonitoringFailedSubscriptions:]_block_invoke.195
- __63-[SPSecureLocationsManager updateLocationCacheWith:completion:]_block_invoke.203
- __64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.279
- __64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.247
- __64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.246
- __65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.374
- __65-[SPSecureLocationsManager clearLocationsForFailedSubscriptions:]_block_invoke.192
- __65-[SPSecureLocationsManager unsubscribeForIds:context:completion:]_block_invoke.198
- __66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.248
- __67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.280
- __67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.280.cold.1
- __68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.371
- __68-[SPSecureLocationsManager latestLocationFromCacheForId:completion:]_block_invoke.200
- __69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.297
- __73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.290
- __73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.312
- __73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.355
- __75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.253
- __75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.254
- __76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.281
- __77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.306
- __78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.178
- __79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.174
- __79-[SPSecureLocationsManager subscribeAndFetchLocationForIds:context:completion:]_block_invoke.197
- __80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.356
- __80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.367
- __81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.301
- __83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.363
- __89-[SPBeaconManager startUpdatingSimpleBeaconsWithContext:collectionDifference:completion:]_block_invoke.270
- __89-[SPBeaconManager startUpdatingSimpleBeaconsWithContext:collectionDifference:completion:]_block_invoke_2.271
- __89-[SPBeaconManager startUpdatingSimpleBeaconsWithContext:collectionDifference:completion:]_block_invoke_3.272
- __91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.182
- __92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.181
- __93-[SPOwnerSession startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:]_block_invoke.330
- __93-[SPOwnerSession startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:]_block_invoke_2.331
- __93-[SPOwnerSession startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:]_block_invoke_3.332
- __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.288
- __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.289
- __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.295
- __98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.296
- __block_literal_global.155
- __block_literal_global.263
- __block_literal_global.308
- __block_literal_global.311
- __block_literal_global.322
CStrings:
+ "\f"
+ "%s"
+ "-[SPAccessoryDiscoverySession finalizeProximityPairingForAccessoryIdentifier]"
+ "-[SPAccessoryDiscoverySession initializeProximityPairingForAccessoryIdentifier]"
+ "-[SPCertificationAssistantSession startUpdatingBeaconsWithContext:collectionDifference:completion:]"
+ "-[SPCertificationAssistantSession stopUpdatingBeaconsWithCompletion:]"
+ "-[SPMetadataFetchingSession fetchHawkeyeAIS]"
+ "@\"<SPMetadataFetchingXPCProtocol>\""
+ "@\"SPRawAccessoryMetadata\""
+ "SPCertificationAssistantBeacon"
+ "SPCertificationAssistantProtocol"
+ "SPCertificationAssistantSession"
+ "SPMetadataFetchingSession"
+ "SPMetadataFetchingSession.fetchHawkeyeAIS"
+ "SPMetadataFetchingSession: Establishing XPC connection to %@"
+ "SPMetadataFetchingSession: interruptionHandler %@"
+ "SPMetadataFetchingSession: invalidationHandler %@"
+ "SPMetadataFetchingXPCClientProtocol"
+ "T@\"<SPMetadataFetchingXPCProtocol>\",&,N,V_proxy"
+ "T@\"NSData\",C,N,V_networkId"
+ "T@\"NSData\",C,N,V_protocolVersion"
+ "T@\"NSNumber\",C,N,V_batteryPercentage"
+ "T@\"NSNumber\",C,N,V_isMine"
+ "T@\"NSNumber\",C,N,V_lowPowerMode"
+ "T@\"NSNumber\",C,N,V_thisDevice"
+ "T@\"NSString\",C,N,V_deviceClass"
+ "T@\"NSString\",C,N,V_deviceColor"
+ "T@\"NSString\",C,N,V_deviceDisplayName"
+ "T@\"NSString\",C,N,V_deviceModel"
+ "T@\"SPRawAccessoryMetadata\",C,N,V_rawMetadata"
+ "T@?,C,N,V_proximityPairingCompletedCallback"
+ "T@?,C,N,V_proximityPairingErrorCallback"
+ "T@?,C,N,V_proximityPairingFinishedCallback"
+ "TB,N,V_online"
+ "[accessoryProximityPairingError called from client]. Error %@"
+ "[proximityPairingCompleted called from client]. Beacons %@, Location %@"
+ "[proximityPairingFinished called from client]. Location %@"
+ "_batteryPercentage"
+ "_deviceClass"
+ "_deviceColor"
+ "_deviceDisplayName"
+ "_deviceModel"
+ "_isMine"
+ "_lowPowerMode"
+ "_networkId"
+ "_online"
+ "_proximityPairingCompletedCallback"
+ "_proximityPairingErrorCallback"
+ "_proximityPairingFinishedCallback"
+ "_rawMetadata"
+ "_thisDevice"
+ "accessoryProximityPairingError:"
+ "batteryPercentage"
+ "beaconsChanges:"
+ "boolValue"
+ "certificationAssistantSession"
+ "com.apple.SPOwner.SPCertificationAssistant.ErrorDomain"
+ "com.apple.SPOwner.SPCertificationAssistantSession"
+ "com.apple.icloud.searchpartyd.SPAccessoryProximityDiscoveryAndPairingSessionErrorDomain.ErrorDomain"
+ "com.apple.icloud.searchpartyd.SPMetadataFetchingSession"
+ "com.apple.icloud.searchpartyd.SPMetadataFetchingSession.callback"
+ "deviceClass"
+ "deviceColor"
+ "deviceDisplayName"
+ "deviceModel"
+ "fetchAccessoryCapabilitiesData:completion:"
+ "fetchAccessoryCategoryData:completion:"
+ "fetchBatteryStatusData:completion:"
+ "fetchBatteryTypeData:completion:"
+ "fetchFirmwareVersionData:completion:"
+ "fetchHawkeyeAIS:metadataType:completion:"
+ "fetchManufacturerNameData:completion:"
+ "fetchModelColorCodeData:completion:"
+ "fetchModelNameData:completion:"
+ "fetchProductData:completion:"
+ "fetchProtocolVersionData:completion:"
+ "finalizeProximityPairingForAccessoryIdentifier:configuration:completion:"
+ "findMyService"
+ "fmcaContext"
+ "getAllSharedKeysWithCompletion:"
+ "getSharingKeyWithCompletion:"
+ "initializeProximityPairingForAccessoryIdentifier:completion:"
+ "isMine"
+ "lowPowerMode"
+ "networkId"
+ "online"
+ "pairing-accessory-type"
+ "pairing-color"
+ "pairing-device-state"
+ "pairing-engraving-data"
+ "pairing-identifier"
+ "pairing-info"
+ "pairing-user-name"
+ "peripheralManager:didChannelSoundingProcedureEvent:results:error:"
+ "peripheralManager:didCloseL2CAPChannel:"
+ "peripheralManager:l2CapChannel:didReceiveData:"
+ "processIDSServiceMessage:completion:"
+ "proximity-pairing-alert"
+ "proximityPairingCompleted:beacons:"
+ "proximityPairingCompletedCallback"
+ "proximityPairingErrorCallback"
+ "proximityPairingFinished:"
+ "proximityPairingFinishedCallback"
+ "rawMetadata"
+ "registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:"
+ "setBatteryPercentage:"
+ "setDeviceClass:"
+ "setDeviceColor:"
+ "setDeviceDisplayName:"
+ "setDeviceModel:"
+ "setIsMine:"
+ "setLowPowerMode:"
+ "setNetworkId:"
+ "setOnline:"
+ "setProximityPairingCompletedCallback:"
+ "setProximityPairingErrorCallback:"
+ "setProximityPairingFinishedCallback:"
+ "setRawMetadata:"
+ "setSharingKey:completion:"
+ "setThisDevice:"
+ "startProximityAccessoryDiscoveryWithCompletion:"
+ "startUpdatingBeaconsWithContext:collectionDifference:completion:"
+ "stopAccessoryProximityDiscoveryWithCompletion:"
+ "stopUpdatingBeaconsWithCompletion:"
+ "thisDevice"
+ "unifiedBeacons:"
+ "v24@0:8@\"CLLocation\"16"
+ "v32@0:8@\"CBPeripheralManager\"16@\"CBL2CAPChannel\"24"
+ "v32@0:8@\"CLLocation\"16@\"NSArray\"24"
+ "v40@0:8@\"CBPeripheralManager\"16@\"CBL2CAPChannel\"24@\"NSData\"32"
+ "v40@0:8@\"NSUUID\"16@\"SPAccessoryPairingConfiguration\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v48@0:8@\"CBPeripheralManager\"16@\"CBCentral\"24@\"NSDictionary\"32@\"NSError\"40"
- "\t"

```
