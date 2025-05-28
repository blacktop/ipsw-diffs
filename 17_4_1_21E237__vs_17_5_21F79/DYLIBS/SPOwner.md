## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-358.16.0.2.0
-  __TEXT.__text: 0x65a1c
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x8260
-  __TEXT.__cstring: 0x5c9e
+360.20.0.1.0
+  __TEXT.__text: 0x6a53c
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x87b0
+  __TEXT.__cstring: 0x601e
   __TEXT.__const: 0x370
-  __TEXT.__gcc_except_tab: 0x127c
-  __TEXT.__oslogstring: 0x61e9
+  __TEXT.__gcc_except_tab: 0x1320
+  __TEXT.__oslogstring: 0x6cd9
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x122
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x2354
+  __TEXT.__unwind_info: 0x24d8
   __TEXT.__eh_frame: 0x240
-  __TEXT.__objc_classname: 0xf7b
-  __TEXT.__objc_methname: 0x10651
-  __TEXT.__objc_methtype: 0x3108
-  __TEXT.__objc_stubs: 0x9840
+  __TEXT.__objc_classname: 0x1090
+  __TEXT.__objc_methname: 0x11105
+  __TEXT.__objc_methtype: 0x3388
+  __TEXT.__objc_stubs: 0x9da0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1e18
-  __DATA_CONST.__objc_classlist: 0x378
+  __DATA_CONST.__const: 0x1ee0
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x180
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf808
-  __DATA_CONST.__objc_selrefs: 0x3260
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_classrefs: 0x490
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_const: 0x10240
+  __DATA_CONST.__objc_selrefs: 0x3430
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0x4b8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x37f8
-  __AUTH_CONST.__const: 0xaf0
+  __AUTH_CONST.__cfstring: 0x5360
+  __AUTH_CONST.__objc_const: 0x3ac8
+  __AUTH_CONST.__const: 0xb70
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x620
-  __AUTH.__objc_data: 0xe08
-  __DATA.__objc_ivar: 0xc04
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH.__objc_data: 0xf98
+  __DATA.__objc_ivar: 0xc78
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x12a8
-  __DATA.__bss: 0x5d0
+  __DATA.__data: 0x13e8
+  __DATA.__bss: 0x5e0
   __DATA_DIRTY.__objc_data: 0x14b8
-  __DATA_DIRTY.__data: 0x200
-  __DATA_DIRTY.__bss: 0x310
+  __DATA_DIRTY.__data: 0x1f8
+  __DATA_DIRTY.__bss: 0x330
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3567
-  Symbols:   11040
-  CStrings:  4577
+  Functions: 3726
+  Symbols:   11527
+  CStrings:  4765
 
Symbols:
+ +[SPAttachmentInfo supportsSecureCoding]
+ +[SPDeviceEvent supportsSecureCoding]
+ +[SPDeviceEventFetchResult supportsSecureCoding]
+ +[SPLocalFindableConnectionMaterialMonitoringSession exportedInterface]
+ +[SPLocalFindableConnectionMaterialMonitoringSession remoteInterface]
+ +[SPPeripheralConnectionMaterial supportsSecureCoding]
+ -[SPAccessoryDiscoveryAndPairingSession initiatePairingAndLocateAccessoryWith:completion:]
+ -[SPAccessoryDiscoveryAndPairingSession initiatePairingForAccessoryWith:completion:]
+ -[SPAccessoryDiscoveryAndPairingSession pairingStatus:completion:]
+ -[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]
+ -[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]
+ -[SPAttachmentInfo .cxx_destruct]
+ -[SPAttachmentInfo attachedToDevice]
+ -[SPAttachmentInfo copyWithZone:]
+ -[SPAttachmentInfo encodeWithCoder:]
+ -[SPAttachmentInfo initWithAttachedToDevice:]
+ -[SPAttachmentInfo initWithCoder:]
+ -[SPBTFindingSession startFastAdvertisingForBeacon:completion:]
+ -[SPBTFindingSession startFindingBeacon:completion:]
+ -[SPBTFindingSession stopFastAdvertisingForBeacon:completion:]
+ -[SPBTFindingSession stopFindingBeacon:completion:]
+ -[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]
+ -[SPBeaconSharingManager revokeShare:completion:]
+ -[SPCBPeripheralManager cbQueue]
+ -[SPCBPeripheralManager centralManager]
+ -[SPCBPeripheralManager pairingAgent:peerDidCompletePairing:]
+ -[SPCBPeripheralManager pairingAgent:peerDidUnpair:]
+ -[SPCBPeripheralManager pendingPairingIdentifiers]
+ -[SPCBPeripheralManager setCbQueue:]
+ -[SPCBPeripheralManager setCentralManager:]
+ -[SPCBPeripheralManager setPendingPairingIdentifiers:]
+ -[SPDeviceEvent .cxx_destruct]
+ -[SPDeviceEvent attachmentInfo]
+ -[SPDeviceEvent copyWithZone:]
+ -[SPDeviceEvent encodeWithCoder:]
+ -[SPDeviceEvent initWithCoder:]
+ -[SPDeviceEvent initWithTimestamp:source:attachmentInfo:serialNumber:]
+ -[SPDeviceEvent serialNumber]
+ -[SPDeviceEvent setSerialNumber:]
+ -[SPDeviceEvent source]
+ -[SPDeviceEvent timestamp]
+ -[SPDeviceEventFetchResult .cxx_destruct]
+ -[SPDeviceEventFetchResult beaconEventByBeaconIdentifier]
+ -[SPDeviceEventFetchResult encodeWithCoder:]
+ -[SPDeviceEventFetchResult initWithCoder:]
+ -[SPDeviceEventFetchResult initWithResults:]
+ -[SPDeviceEventFetchResult setBeaconEventByBeaconIdentifier:]
+ -[SPDiscoveredAccessoryProductInformation isAirTag]
+ -[SPDiscoveredAccessoryProductInformation isAppleAudioAccessory]
+ -[SPDiscoveredAccessoryProductInformation setIsAirTag:]
+ -[SPDiscoveredAccessoryProductInformation setIsAppleAudioAccessory:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession .cxx_destruct]
+ -[SPLocalFindableConnectionMaterialMonitoringSession callbackQueue]
+ -[SPLocalFindableConnectionMaterialMonitoringSession init]
+ -[SPLocalFindableConnectionMaterialMonitoringSession interruptionHandler:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession invalidationHandler:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession peripheralConnectionMaterialCallback]
+ -[SPLocalFindableConnectionMaterialMonitoringSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession proxy]
+ -[SPLocalFindableConnectionMaterialMonitoringSession queue]
+ -[SPLocalFindableConnectionMaterialMonitoringSession serviceDescription]
+ -[SPLocalFindableConnectionMaterialMonitoringSession sessionInvalidatedCallback]
+ -[SPLocalFindableConnectionMaterialMonitoringSession session]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setCallbackQueue:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setPeripheralConnectionMaterialCallback:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setProxy:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setQueue:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setServiceDescription:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setSession:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession setSessionInvalidatedCallback:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession startLocalFindableConnectionMaterialMonitoringWithCompletion:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession stopLocalFindableConnectionMaterialMonitoringWithCompletion:]
+ -[SPLocalFindableConnectionMaterialMonitoringSession updatedConnectionMaterialForAccessory:connectionMaterial:]
+ -[SPLocationFetchContext reportDeviceEvents]
+ -[SPLocationFetchContext setReportDeviceEvents:]
+ -[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]
+ -[SPOwnerSession setDeviceEventUpdateBlock:]
+ -[SPOwnerSessionLocationFetch deviceEventUpdates]
+ -[SPOwnerSessionLocationFetch receivedUpdatedDeviceEvents:]
+ -[SPOwnerSessionLocationFetch setDeviceEventUpdateBlock:]
+ -[SPOwnerSessionLocationFetch setDeviceEventUpdates:]
+ -[SPPeripheralConnectionMaterial .cxx_destruct]
+ -[SPPeripheralConnectionMaterial btAddressData]
+ -[SPPeripheralConnectionMaterial btAddressWithTypeData]
+ -[SPPeripheralConnectionMaterial copyWithZone:]
+ -[SPPeripheralConnectionMaterial description]
+ -[SPPeripheralConnectionMaterial encodeWithCoder:]
+ -[SPPeripheralConnectionMaterial initWithCoder:]
+ -[SPPeripheralConnectionMaterial irkData]
+ -[SPPeripheralConnectionMaterial setBtAddressData:]
+ -[SPPeripheralConnectionMaterial setBtAddressWithTypeData:]
+ -[SPPeripheralConnectionMaterial setIrkData:]
+ -[SPScannedObject advertisementType]
+ -[SPScannedObject initWithAdvertisementType:poshNetwork:nearOwner:vendorPayload:scanDate:address:advertisement:status:ek:hint:rssi:indexInformation:acccessoryInformation:]
+ -[SPScannedObject nearOwner]
+ -[SPScannedObject poshNetwork]
+ -[SPScannedObject setAdvertisementType:]
+ -[SPScannedObject setNearOwner:]
+ -[SPScannedObject setPoshNetwork:]
+ -[SPScannedObject setVendorPayload:]
+ -[SPScannedObject vendorPayload]
+ -[SPUnauthorizedTrackingAdvertisement isPosh]
+ -[SPUnauthorizedTrackingAdvertisement networkID]
+ -[SPUnauthorizedTrackingAdvertisement setIsPosh:]
+ -[SPUnauthorizedTrackingAdvertisement setNetworkID:]
+ -[SPUnknownBeacon setIsFindMyNetwork:]
+ -[SPUnknownBeacon setIsPosh:]
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table145
+ GCC_except_table149
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table185
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table38
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table96
+ _LogCategory_LocalFindableConnectionMaterialMonitoring
+ _LogCategory_LocalFindableConnectionMaterialMonitoring.log
+ _LogCategory_LocalFindableConnectionMaterialMonitoring.onceToken
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SPAttachmentInfo
+ _OBJC_CLASS_$_SPDeviceEvent
+ _OBJC_CLASS_$_SPDeviceEventFetchResult
+ _OBJC_CLASS_$_SPLocalFindableConnectionMaterialMonitoringSession
+ _OBJC_CLASS_$_SPPeripheralConnectionMaterial
+ _OBJC_IVAR_$_SPAttachmentInfo._attachedToDevice
+ _OBJC_IVAR_$_SPCBPeripheralManager._cbQueue
+ _OBJC_IVAR_$_SPCBPeripheralManager._centralManager
+ _OBJC_IVAR_$_SPCBPeripheralManager._pendingPairingIdentifiers
+ _OBJC_IVAR_$_SPDeviceEvent._attachmentInfo
+ _OBJC_IVAR_$_SPDeviceEvent._serialNumber
+ _OBJC_IVAR_$_SPDeviceEvent._source
+ _OBJC_IVAR_$_SPDeviceEvent._timestamp
+ _OBJC_IVAR_$_SPDeviceEventFetchResult._beaconEventByBeaconIdentifier
+ _OBJC_IVAR_$_SPDiscoveredAccessoryProductInformation._isAirTag
+ _OBJC_IVAR_$_SPDiscoveredAccessoryProductInformation._isAppleAudioAccessory
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._callbackQueue
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._peripheralConnectionMaterialCallback
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._proxy
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._queue
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._serviceDescription
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._session
+ _OBJC_IVAR_$_SPLocalFindableConnectionMaterialMonitoringSession._sessionInvalidatedCallback
+ _OBJC_IVAR_$_SPLocationFetchContext._reportDeviceEvents
+ _OBJC_IVAR_$_SPOwnerSessionLocationFetch._deviceEventUpdates
+ _OBJC_IVAR_$_SPPeripheralConnectionMaterial._btAddressData
+ _OBJC_IVAR_$_SPPeripheralConnectionMaterial._btAddressWithTypeData
+ _OBJC_IVAR_$_SPPeripheralConnectionMaterial._irkData
+ _OBJC_IVAR_$_SPScannedObject._advertisementType
+ _OBJC_IVAR_$_SPScannedObject._nearOwner
+ _OBJC_IVAR_$_SPScannedObject._poshNetwork
+ _OBJC_IVAR_$_SPScannedObject._vendorPayload
+ _OBJC_IVAR_$_SPUnauthorizedTrackingAdvertisement._isPosh
+ _OBJC_IVAR_$_SPUnauthorizedTrackingAdvertisement._networkID
+ _OBJC_METACLASS_$_SPAttachmentInfo
+ _OBJC_METACLASS_$_SPDeviceEvent
+ _OBJC_METACLASS_$_SPDeviceEventFetchResult
+ _OBJC_METACLASS_$_SPLocalFindableConnectionMaterialMonitoringSession
+ _OBJC_METACLASS_$_SPPeripheralConnectionMaterial
+ _SPBeaconLocationSourceDeviceAttachedLocation
+ _SPBeaconLocationSourceDeviceDetachedLocation
+ _SPBeaconLocationSourceDeviceDetectedLocation
+ _SPBeaconTypeLocalFindable
+ _SPLocalFindableConnectionMaterialMonitoringSessionErrorDomain
+ __OBJC_$_CLASS_METHODS_SPAttachmentInfo
+ __OBJC_$_CLASS_METHODS_SPDeviceEvent
+ __OBJC_$_CLASS_METHODS_SPDeviceEventFetchResult
+ __OBJC_$_CLASS_METHODS_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_$_CLASS_METHODS_SPPeripheralConnectionMaterial
+ __OBJC_$_CLASS_PROP_LIST_SPAttachmentInfo
+ __OBJC_$_CLASS_PROP_LIST_SPDeviceEvent
+ __OBJC_$_CLASS_PROP_LIST_SPDeviceEventFetchResult
+ __OBJC_$_CLASS_PROP_LIST_SPPeripheralConnectionMaterial
+ __OBJC_$_INSTANCE_METHODS_SPAttachmentInfo
+ __OBJC_$_INSTANCE_METHODS_SPDeviceEvent
+ __OBJC_$_INSTANCE_METHODS_SPDeviceEventFetchResult
+ __OBJC_$_INSTANCE_METHODS_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_$_INSTANCE_METHODS_SPPeripheralConnectionMaterial
+ __OBJC_$_INSTANCE_VARIABLES_SPAttachmentInfo
+ __OBJC_$_INSTANCE_VARIABLES_SPDeviceEvent
+ __OBJC_$_INSTANCE_VARIABLES_SPDeviceEventFetchResult
+ __OBJC_$_INSTANCE_VARIABLES_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_$_INSTANCE_VARIABLES_SPPeripheralConnectionMaterial
+ __OBJC_$_PROP_LIST_SPAttachmentInfo
+ __OBJC_$_PROP_LIST_SPDeviceEvent
+ __OBJC_$_PROP_LIST_SPDeviceEventFetchResult
+ __OBJC_$_PROP_LIST_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_$_PROP_LIST_SPPeripheralConnectionMaterial
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBPairingAgentDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPLocalFindableConnectionMaterialMonitoringXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBPairingAgentDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPLocalFindableConnectionMaterialMonitoringXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_CBPairingAgentDelegate
+ __OBJC_$_PROTOCOL_REFS_SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol
+ __OBJC_$_PROTOCOL_REFS_SPLocalFindableConnectionMaterialMonitoringXPCProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SPAttachmentInfo
+ __OBJC_CLASS_PROTOCOLS_$_SPDeviceEvent
+ __OBJC_CLASS_PROTOCOLS_$_SPDeviceEventFetchResult
+ __OBJC_CLASS_PROTOCOLS_$_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_CLASS_PROTOCOLS_$_SPPeripheralConnectionMaterial
+ __OBJC_CLASS_RO_$_SPAttachmentInfo
+ __OBJC_CLASS_RO_$_SPDeviceEvent
+ __OBJC_CLASS_RO_$_SPDeviceEventFetchResult
+ __OBJC_CLASS_RO_$_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_CLASS_RO_$_SPPeripheralConnectionMaterial
+ __OBJC_LABEL_PROTOCOL_$_CBPairingAgentDelegate
+ __OBJC_LABEL_PROTOCOL_$_SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_SPLocalFindableConnectionMaterialMonitoringXPCProtocol
+ __OBJC_METACLASS_RO_$_SPAttachmentInfo
+ __OBJC_METACLASS_RO_$_SPDeviceEvent
+ __OBJC_METACLASS_RO_$_SPDeviceEventFetchResult
+ __OBJC_METACLASS_RO_$_SPLocalFindableConnectionMaterialMonitoringSession
+ __OBJC_METACLASS_RO_$_SPPeripheralConnectionMaterial
+ __OBJC_PROTOCOL_$_CBPairingAgentDelegate
+ __OBJC_PROTOCOL_$_SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol
+ __OBJC_PROTOCOL_$_SPLocalFindableConnectionMaterialMonitoringXPCProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SPLocalFindableConnectionMaterialMonitoringXPCProtocol
+ ___111-[SPLocalFindableConnectionMaterialMonitoringSession updatedConnectionMaterialForAccessory:connectionMaterial:]_block_invoke
+ ___114-[SPLocalFindableConnectionMaterialMonitoringSession stopLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke
+ ___114-[SPLocalFindableConnectionMaterialMonitoringSession stopLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke.67
+ ___114-[SPLocalFindableConnectionMaterialMonitoringSession stopLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke_2
+ ___114-[SPLocalFindableConnectionMaterialMonitoringSession stopLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke_2.cold.1
+ ___115-[SPLocalFindableConnectionMaterialMonitoringSession startLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke
+ ___115-[SPLocalFindableConnectionMaterialMonitoringSession startLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke.65
+ ___115-[SPLocalFindableConnectionMaterialMonitoringSession startLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke_2
+ ___115-[SPLocalFindableConnectionMaterialMonitoringSession startLocalFindableConnectionMaterialMonitoringWithCompletion:]_block_invoke_2.cold.1
+ ___116-[SPLocalFindableConnectionMaterialMonitoringSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke
+ ___116-[SPLocalFindableConnectionMaterialMonitoringSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.68
+ ___30-[SPCBPeripheralManager fetch]_block_invoke.102
+ ___32-[SPOwnerSession stopRefreshing]_block_invoke.273
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.258
+ ___35-[SPBTFindingSession updateConfig:]_block_invoke.70
+ ___35-[SPBeaconManager repairDataStore:]_block_invoke.287
+ ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.269
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.254
+ ___44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.244
+ ___44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.263
+ ___44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.239
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.291
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.292
+ ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.82
+ ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.10
+ ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.10.cold.1
+ ___47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.250
+ ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.245
+ ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.246
+ ___48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.264
+ ___48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.265
+ ___48-[SPBeaconSharingManager receivedUpdatedShares:]_block_invoke.153
+ ___49-[SPBeaconSharingManager acceptShare:completion:]_block_invoke.116
+ ___49-[SPBeaconSharingManager removeShare:completion:]_block_invoke.114
+ ___49-[SPBeaconSharingManager revokeShare:completion:]_block_invoke
+ ___49-[SPBeaconSharingManager revokeShare:completion:]_block_invoke.115
+ ___49-[SPBeaconSharingManager revokeShare:completion:]_block_invoke_2
+ ___49-[SPBeaconSharingManager stopSharing:completion:]_block_invoke.118
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.255
+ ___50-[SPBeaconSharingManager allSharesWithCompletion:]_block_invoke.124
+ ___50-[SPBeaconSharingManager declineShare:completion:]_block_invoke.117
+ ___50-[SPBeaconSharingManager requestShare:completion:]_block_invoke.113
+ ___51-[SPBTFindingSession stopFindingBeacon:completion:]_block_invoke
+ ___51-[SPBTFindingSession stopFindingBeacon:completion:]_block_invoke.77
+ ___51-[SPBTFindingSession stopFindingBeacon:completion:]_block_invoke_2
+ ___51-[SPBTFindingSession stopFindingBeacon:completion:]_block_invoke_2.cold.1
+ ___51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.260
+ ___51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.266
+ ___52-[SPBTFindingSession startFindingBeacon:completion:]_block_invoke
+ ___52-[SPBTFindingSession startFindingBeacon:completion:]_block_invoke.74
+ ___52-[SPBTFindingSession startFindingBeacon:completion:]_block_invoke_2
+ ___52-[SPBTFindingSession startFindingBeacon:completion:]_block_invoke_2.cold.1
+ ___52-[SPCBPeripheralManager pairingAgent:peerDidUnpair:]_block_invoke
+ ___52-[SPCBPeripheralManager pairingAgent:peerDidUnpair:]_block_invoke_2
+ ___54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.283
+ ___54-[SPBeaconSharingManager forceStopSharing:completion:]_block_invoke.123
+ ___54-[SPBeaconSharingManager share:recipients:completion:]_block_invoke.110
+ ___54-[SPBeaconSharingManager sharingLimitsWithCompletion:]_block_invoke.151
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.256
+ ___55-[SPBeaconSharingManager forceDeclineShare:completion:]_block_invoke.122
+ ___58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.279
+ ___59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.240
+ ___59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.275
+ ___59-[SPLocalFindableConnectionMaterialMonitoringSession proxy]_block_invoke
+ ___59-[SPLocalFindableConnectionMaterialMonitoringSession proxy]_block_invoke_2
+ ___59-[SPOwnerSessionLocationFetch receivedUpdatedDeviceEvents:]_block_invoke
+ ___60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.278
+ ___60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.284
+ ___60-[SPBeaconSharingManager removeExpiredSharesWithCompletion:]_block_invoke.150
+ ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.84
+ ___61-[SPBeaconSharingManager cleanupAllRecordsOfType:completion:]_block_invoke.119
+ ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke.129
+ ___61-[SPCBPeripheralManager pairingAgent:peerDidCompletePairing:]_block_invoke
+ ___61-[SPCBPeripheralManager pairingAgent:peerDidCompletePairing:]_block_invoke_2
+ ___62-[SPBTFindingSession stopFastAdvertisingForBeacon:completion:]_block_invoke
+ ___62-[SPBTFindingSession stopFastAdvertisingForBeacon:completion:]_block_invoke.76
+ ___62-[SPBTFindingSession stopFastAdvertisingForBeacon:completion:]_block_invoke_2
+ ___62-[SPBTFindingSession stopFastAdvertisingForBeacon:completion:]_block_invoke_2.cold.1
+ ___62-[SPBeaconSharingManager updatedCircleIdentifiers:completion:]_block_invoke.138
+ ___63-[SPBTFindingSession startFastAdvertisingForBeacon:completion:]_block_invoke
+ ___63-[SPBTFindingSession startFastAdvertisingForBeacon:completion:]_block_invoke.75
+ ___63-[SPBTFindingSession startFastAdvertisingForBeacon:completion:]_block_invoke_2
+ ___63-[SPBTFindingSession startFastAdvertisingForBeacon:completion:]_block_invoke_2.cold.1
+ ___63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.277
+ ___63-[SPBeaconSharingManager forceBreakAllSharesOfType:completion:]_block_invoke.120
+ ___63-[SPBeaconSharingManager lookForOrphanedRecordsWithCompletion:]_block_invoke.148
+ ___63-[SPCBPeripheralManager enableSystemWakesForUpdate:completion:]_block_invoke.21
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.294
+ ___64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.261
+ ___64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.242
+ ___64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.241
+ ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke.112
+ ___65-[SPBeaconSharingManager allSharesIncludingHiddenWithCompletion:]_block_invoke.126
+ ___65-[SPBeaconSharingManager forceBreakAllSharesWithUser:completion:]_block_invoke.121
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.302
+ ___66-[SPAccessoryDiscoveryAndPairingSession pairingStatus:completion:]_block_invoke
+ ___66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.243
+ ___66-[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]_block_invoke
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.260
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.260.cold.1
+ ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke.127
+ ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke_2.128
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.301
+ ___69+[SPLocalFindableConnectionMaterialMonitoringSession remoteInterface]_block_invoke
+ ___69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.271
+ ___71+[SPLocalFindableConnectionMaterialMonitoringSession exportedInterface]_block_invoke
+ ___73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.267
+ ___73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.276
+ ___74-[SPCBPeripheralManager stopSessionForUserIdentifier:bundleId:completion:]_block_invoke.18
+ ___74-[SPCBPeripheralManager stopSessionForUserIdentifier:bundleId:completion:]_block_invoke.19
+ ___74-[SPCBPeripheralManager stopSessionForUserIdentifier:bundleId:completion:]_block_invoke.20
+ ___74-[SPLocalFindableConnectionMaterialMonitoringSession interruptionHandler:]_block_invoke
+ ___74-[SPLocalFindableConnectionMaterialMonitoringSession invalidationHandler:]_block_invoke
+ ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.248
+ ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.249
+ ___75-[SPBeaconSharingManager checkDataIntegrityWithShareIdentifier:completion:]_block_invoke.146
+ ___76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.262
+ ___77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.274
+ ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.83
+ ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.80
+ ___80-[SPCBPeripheralManager successfulConnectionForPeripheral:leMAC:ltk:completion:]_block_invoke.22
+ ___80-[SPCBPeripheralManager successfulConnectionForPeripheral:leMAC:ltk:completion:]_block_invoke.22.cold.1
+ ___80-[SPCBPeripheralManager successfulConnectionForPeripheral:leMAC:ltk:completion:]_block_invoke.23
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.295
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.299
+ ___81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.273
+ ___83-[SPBeaconSharingManager downloadKeysWithCircleIdentifier:fromBookmark:completion:]_block_invoke.137
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.297
+ ___84-[SPAccessoryDiscoveryAndPairingSession initiatePairingForAccessoryWith:completion:]_block_invoke
+ ___84-[SPAccessoryDiscoveryAndPairingSession initiatePairingForAccessoryWith:completion:]_block_invoke_2
+ ___84-[SPAccessoryDiscoveryAndPairingSession initiatePairingForAccessoryWith:completion:]_block_invoke_2.cold.1
+ ___84-[SPBeaconSharingManager uploadKeysWithCircleIdentifier:isInitialUpload:completion:]_block_invoke.136
+ ___90-[SPAccessoryDiscoveryAndPairingSession initiatePairingAndLocateAccessoryWith:completion:]_block_invoke
+ ___90-[SPAccessoryDiscoveryAndPairingSession initiatePairingAndLocateAccessoryWith:completion:]_block_invoke_2
+ ___90-[SPAccessoryDiscoveryAndPairingSession initiatePairingAndLocateAccessoryWith:completion:]_block_invoke_2.cold.1
+ ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke
+ ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.86
+ ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke_2
+ ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke_2.cold.1
+ ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke
+ ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.85
+ ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke_2
+ ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke_2.cold.1
+ ___96-[SPCBPeripheralManager startSessionForUserIdentifier:bundleId:vendorIdentifierList:completion:]_block_invoke.16
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.265
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.266
+ ___LogCategory_LocalFindableConnectionMaterialMonitoring_block_invoke
+ ___block_descriptor_40_e8_32bs_e32_v24?0"NSError"8"CLLocation"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.178
+ ___block_literal_global.184
+ ___block_literal_global.191
+ ___block_literal_global.254
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.30
+ ___block_literal_global.73
+ ___block_literal_global.87
+ _btAddressDataKey
+ _btAddressWithTypeDataKey
+ _dispatch_queue_attr_make_with_qos_class
+ _irkDataKey
+ _objc_msgSend$attachedToDevice
+ _objc_msgSend$attachmentInfo
+ _objc_msgSend$beaconEventByBeaconIdentifier
+ _objc_msgSend$btAddressData
+ _objc_msgSend$btAddressWithTypeData
+ _objc_msgSend$cbQueue
+ _objc_msgSend$deviceEventUpdates
+ _objc_msgSend$hasTag:
+ _objc_msgSend$initWithAdvertisementType:poshNetwork:nearOwner:vendorPayload:scanDate:address:advertisement:status:ek:hint:rssi:indexInformation:acccessoryInformation:
+ _objc_msgSend$initWithAttachedToDevice:
+ _objc_msgSend$initWithTimestamp:source:attachmentInfo:serialNumber:
+ _objc_msgSend$initiatePairingAndLocateAccessoryWithIdentifier:completion:
+ _objc_msgSend$irkData
+ _objc_msgSend$isAirTag
+ _objc_msgSend$isFindMyNetwork
+ _objc_msgSend$isPosh
+ _objc_msgSend$networkID
+ _objc_msgSend$pairLowEnergyAccessoryWithIdentifier:completion:
+ _objc_msgSend$pairingStatus:completion:
+ _objc_msgSend$pendingPairingIdentifiers
+ _objc_msgSend$peripheralConnectionMaterialCallback
+ _objc_msgSend$peripheralConnectionMaterialForAccessoryIdentifier:completion:
+ _objc_msgSend$reportDeviceEvents
+ _objc_msgSend$revokeShare:completion:
+ _objc_msgSend$setBeaconEventByBeaconIdentifier:
+ _objc_msgSend$setBtAddressData:
+ _objc_msgSend$setBtAddressWithTypeData:
+ _objc_msgSend$setDeviceEventUpdateBlock:
+ _objc_msgSend$setDeviceEventUpdates:
+ _objc_msgSend$setIrkData:
+ _objc_msgSend$setIsAirTag:
+ _objc_msgSend$setIsFindMyNetwork:
+ _objc_msgSend$setIsPosh:
+ _objc_msgSend$setNetworkID:
+ _objc_msgSend$setReportDeviceEvents:
+ _objc_msgSend$sharedPairingAgent
+ _objc_msgSend$startFastAdvertisingForBeacon:completion:
+ _objc_msgSend$startLocalFindableAccessoryDiscoveryWithCompletion:
+ _objc_msgSend$startLocalFindableConnectionMaterialMonitoringWithCompletion:
+ _objc_msgSend$stopFastAdvertisingForBeacon:completion:
+ _objc_msgSend$stopLocalFindableAccessoryDiscoveryWithCompletion:
+ _objc_msgSend$stopLocalFindableConnectionMaterialMonitoringWithCompletion:
+ _objc_msgSend$submitDeviceEvent:source:attachedTo:completion:
+ _objc_msgSend$unpairLowEnergyAccessoryWithIdentifier:completion:
- -[SPBTFindingSession startFindingBeacons:completion:]
- -[SPBTFindingSession stopFindingBeacons:completion:]
- -[SPScannedObject initWithScanDate:address:advertisement:status:ek:hint:rssi:indexInformation:acccessoryInformation:]
- GCC_except_table112
- GCC_except_table128
- GCC_except_table130
- GCC_except_table132
- GCC_except_table134
- GCC_except_table136
- GCC_except_table138
- GCC_except_table148
- GCC_except_table152
- GCC_except_table154
- GCC_except_table159
- GCC_except_table161
- GCC_except_table164
- GCC_except_table167
- GCC_except_table170
- GCC_except_table172
- GCC_except_table181
- GCC_except_table186
- GCC_except_table191
- GCC_except_table196
- GCC_except_table41
- GCC_except_table43
- GCC_except_table47
- GCC_except_table49
- GCC_except_table57
- GCC_except_table61
- GCC_except_table63
- GCC_except_table86
- ___30-[SPCBPeripheralManager fetch]_block_invoke.91
- ___32-[SPOwnerSession stopRefreshing]_block_invoke.271
- ___33-[SPOwnerSession executeCommand:]_block_invoke.256
- ___35-[SPBTFindingSession updateConfig:]_block_invoke.68
- ___35-[SPBeaconManager repairDataStore:]_block_invoke.281
- ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.267
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.252
- ___44-[SPBeaconManager allBeaconsWithCompletion:]_block_invoke.238
- ___44-[SPBeaconManager allDuriansWithCompletion:]_block_invoke.257
- ___44-[SPBeaconManager beaconForUUID:completion:]_block_invoke.233
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.289
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.290
- ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.76
- ___46-[SPBeaconSharingManager interruptionHandler:]_block_invoke.9.cold.1
- ___47-[SPBeaconManager allBeaconsOfType:completion:]_block_invoke.244
- ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.239
- ___48-[SPBeaconManager allBeaconsOfTypes:completion:]_block_invoke.240
- ___48-[SPBeaconManager roleCategoriesWithCompletion:]_block_invoke.258
- ___48-[SPBeaconManager setRole:forBeacon:completion:]_block_invoke.259
- ___48-[SPBeaconSharingManager receivedUpdatedShares:]_block_invoke.151
- ___49-[SPBeaconSharingManager acceptShare:completion:]_block_invoke.113
- ___49-[SPBeaconSharingManager removeShare:completion:]_block_invoke.112
- ___49-[SPBeaconSharingManager stopSharing:completion:]_block_invoke.115
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.253
- ___50-[SPBeaconSharingManager allSharesWithCompletion:]_block_invoke.121
- ___50-[SPBeaconSharingManager declineShare:completion:]_block_invoke.114
- ___50-[SPBeaconSharingManager requestShare:completion:]_block_invoke.111
- ___51-[SPBeaconManager unacceptedBeaconsWithCompletion:]_block_invoke.254
- ___51-[SPBeaconManager updateBeacon:updates:completion:]_block_invoke.260
- ___52-[SPBTFindingSession stopFindingBeacons:completion:]_block_invoke
- ___52-[SPBTFindingSession stopFindingBeacons:completion:]_block_invoke.73
- ___52-[SPBTFindingSession stopFindingBeacons:completion:]_block_invoke_2
- ___52-[SPBTFindingSession stopFindingBeacons:completion:]_block_invoke_2.cold.1
- ___53-[SPBTFindingSession startFindingBeacons:completion:]_block_invoke
- ___53-[SPBTFindingSession startFindingBeacons:completion:]_block_invoke.72
- ___53-[SPBTFindingSession startFindingBeacons:completion:]_block_invoke_2
- ___53-[SPBTFindingSession startFindingBeacons:completion:]_block_invoke_2.cold.1
- ___54-[SPBeaconManager fetchUserStatsForBeacon:completion:]_block_invoke.277
- ___54-[SPBeaconSharingManager forceStopSharing:completion:]_block_invoke.120
- ___54-[SPBeaconSharingManager share:recipients:completion:]_block_invoke.108
- ___54-[SPBeaconSharingManager sharingLimitsWithCompletion:]_block_invoke.149
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.254
- ___55-[SPBeaconSharingManager forceDeclineShare:completion:]_block_invoke.119
- ___58-[SPBeaconManager connectedToBeacon:withIndex:completion:]_block_invoke.273
- ___59-[SPBeaconManager ownedDeviceKeyRecordsForUUID:completion:]_block_invoke.234
- ___59-[SPBeaconManager setKeyRollInterval:forBeacon:completion:]_block_invoke.269
- ___60-[SPBeaconManager connectionTokensForBeaconUUID:completion:]_block_invoke.272
- ___60-[SPBeaconManager fetchFirmwareVersionForBeacon:completion:]_block_invoke.278
- ___60-[SPBeaconSharingManager removeExpiredSharesWithCompletion:]_block_invoke.148
- ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.78
- ___61-[SPBeaconSharingManager cleanupAllRecordsOfType:completion:]_block_invoke.116
- ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke.126
- ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke_2.127
- ___62-[SPBeaconSharingManager updatedCircleIdentifiers:completion:]_block_invoke.136
- ___63-[SPBeaconManager setCurrentWildKeyIndex:forBeacon:completion:]_block_invoke.271
- ___63-[SPBeaconSharingManager forceBreakAllSharesOfType:completion:]_block_invoke.117
- ___63-[SPBeaconSharingManager lookForOrphanedRecordsWithCompletion:]_block_invoke.146
- ___63-[SPCBPeripheralManager enableSystemWakesForUpdate:completion:]_block_invoke.18
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.292
- ___64-[SPBeaconManager beaconingKeysForUUID:dateInterval:completion:]_block_invoke.255
- ___64-[SPBeaconManager createOwnedDeviceKeyRecordForUUID:completion:]_block_invoke.236
- ___64-[SPBeaconManager purgeOwnedDeviceKeyRecordsForUUID:completion:]_block_invoke.235
- ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke.110
- ___65-[SPBeaconSharingManager allSharesIncludingHiddenWithCompletion:]_block_invoke.123
- ___65-[SPBeaconSharingManager forceBreakAllSharesWithUser:completion:]_block_invoke.118
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.299
- ___66-[SPBeaconManager notificationBeaconForSubscriptionId:completion:]_block_invoke.237
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.258
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.258.cold.1
- ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke.124
- ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke_2.125
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.298
- ___69-[SPBeaconManager connectionTokensForBeaconUUID:criteria:completion:]_block_invoke.265
- ___73-[SPBeaconManager connectionTokensForBeaconUUID:dateInterval:completion:]_block_invoke.261
- ___73-[SPBeaconManager setWildKeyBase:interval:fallback:forBeacon:completion:]_block_invoke.270
- ___74-[SPCBPeripheralManager stopSessionForUserIdentifier:bundleId:completion:]_block_invoke.15
- ___74-[SPCBPeripheralManager stopSessionForUserIdentifier:bundleId:completion:]_block_invoke.16
- ___74-[SPCBPeripheralManager stopSessionForUserIdentifier:bundleId:completion:]_block_invoke.17
- ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.242
- ___75-[SPBeaconManager allBeaconsOfTypes:includeDupes:includeHidden:completion:]_block_invoke.243
- ___75-[SPBeaconSharingManager checkDataIntegrityWithShareIdentifier:completion:]_block_invoke.144
- ___76-[SPBeaconManager postedLocalNotifyWhenFoundNotificationForUUID:completion:]_block_invoke.256
- ___77-[SPBeaconManager setAlignmentUncertainty:atIndex:date:forBeacon:completion:]_block_invoke.268
- ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.77
- ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.74
- ___80-[SPCBPeripheralManager successfulConnectionForPeripheral:leMAC:ltk:completion:]_block_invoke.19
- ___80-[SPCBPeripheralManager successfulConnectionForPeripheral:leMAC:ltk:completion:]_block_invoke.19.cold.1
- ___80-[SPCBPeripheralManager successfulConnectionForPeripheral:leMAC:ltk:completion:]_block_invoke.20
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.296
- ___81-[SPBeaconManager allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:]_block_invoke.267
- ___83-[SPBeaconSharingManager downloadKeysWithCircleIdentifier:fromBookmark:completion:]_block_invoke.135
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.294
- ___84-[SPBeaconSharingManager uploadKeysWithCircleIdentifier:isInitialUpload:completion:]_block_invoke.134
- ___96-[SPCBPeripheralManager startSessionForUserIdentifier:bundleId:vendorIdentifierList:completion:]_block_invoke.12
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.262
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.263
- ___block_literal_global.167
- ___block_literal_global.181
- ___block_literal_global.188
- ___block_literal_global.248
- ___block_literal_global.270
- ___block_literal_global.273
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.54
- ___block_literal_global.62
- ___block_literal_global.68
- ___block_literal_global.76
- _objc_msgSend$initWithScanDate:address:advertisement:status:ek:hint:rssi:indexInformation:acccessoryInformation:
CStrings:
+ "\x1c"
+ "%\x12"
+ "-[SPAccessoryDiscoverySession startLocalFindableAccessoryDiscoveryWithCompletion] completion"
+ "-[SPAccessoryDiscoverySession startLocalFindableAccessoryDiscoveryWithCompletion] completion. Error %@"
+ "-[SPAccessoryDiscoverySession stopLocalFindableAccessoryDiscoveryWithCompletion] completion)"
+ "-[SPAccessoryDiscoverySession stopLocalFindableAccessoryDiscoveryWithCompletion] completion. Error %@"
+ "-[SPAccessoryPairingSession initiatePairingForAccessoryWith] failed %@"
+ "-[SPAccessoryPairingSession initiatePairingForAccessoryWith] succeeded!"
+ "-[SPBTFindingSession startFastAdvertising]"
+ "-[SPBTFindingSession startFastAdvertising] completion"
+ "-[SPBTFindingSession startFastAdvertising] completion. Error %{public}@"
+ "-[SPBTFindingSession start] completion. Error %{public}@"
+ "-[SPBTFindingSession stopFastAdvertising]"
+ "-[SPBTFindingSession stopFastAdvertising] completion"
+ "-[SPBTFindingSession stopFastAdvertising] completion. Error %{public}@"
+ "-[SPBTFindingSession stop] completion. Error %{public}@"
+ "-[SPBTFindingSession updateConfig] completion. Error %{public}@"
+ "-[SPLocalFindableConnectionMaterialMonitoringSession start]"
+ "-[SPLocalFindableConnectionMaterialMonitoringSession start] completion"
+ "-[SPLocalFindableConnectionMaterialMonitoringSession start] completion. Error - %@"
+ "-[SPLocalFindableConnectionMaterialMonitoringSession stop]"
+ "-[SPLocalFindableConnectionMaterialMonitoringSession stop] completion"
+ "-[SPLocalFindableConnectionMaterialMonitoringSession stop] completion. Error - %@"
+ "<%@: %p %@ %lu isFindMyNetwork: %i isPosh: %i>"
+ "<%@: %p irkData: %@ btAddressData: %@ btAddressWithTypeData: %@>"
+ "<%@: %p manufacturer: %@ model: %@ productId: %@ isAirTag: %d isAppleAudioAccessory: %d>"
+ "@\"<SPLocalFindableConnectionMaterialMonitoringXPCProtocol>\""
+ "@\"NSMutableSet\""
+ "@\"SPAttachmentInfo\""
+ "@104@0:8q16C24B28@32@40@48@56C64C68@72q80@88@96"
+ "A2538"
+ "CBPairingAgentDelegate"
+ "Marking revoke for share %@"
+ "SPAttachmentInfo"
+ "SPBTFindingSession.startFastAdvertising"
+ "SPBTFindingSession.stopFastAdvertising"
+ "SPCBPeripheralManager: pairLowEnergyAccessory completed successfully!"
+ "SPCBPeripheralManager: pairLowEnergyAccessory did complete with error %{public}@"
+ "SPCBPeripheralManager: pairingAgent:peerDidCompletePairing %{public}@"
+ "SPCBPeripheralManager: pairingAgent:peerDidUnpair %{public}@"
+ "SPCBPeripheralManager: unpairLowEnergyAccessory completed successfully!"
+ "SPCBPeripheralManager: unpairLowEnergyAccessory did complete with error %{public}@"
+ "SPDeviceEvent"
+ "SPDeviceEventFetchResult"
+ "SPLocalFindableConnectionMaterialMonitoring: Establishing XPC connection to %@"
+ "SPLocalFindableConnectionMaterialMonitoring: interruptionHandler %@"
+ "SPLocalFindableConnectionMaterialMonitoring: invalidationHandler %@"
+ "SPLocalFindableConnectionMaterialMonitoringSession"
+ "SPLocalFindableConnectionMaterialMonitoringSession.peripheralConnectionMaterialForAccessoryIdentifier"
+ "SPLocalFindableConnectionMaterialMonitoringSession.start"
+ "SPLocalFindableConnectionMaterialMonitoringSession.stop"
+ "SPLocalFindableConnectionMaterialMonitoringXPCClientProtocol"
+ "SPLocalFindableConnectionMaterialMonitoringXPCProtocol"
+ "SPOwnerSession.peripheralConnectionMaterialForAccessoryIdentifier"
+ "SPOwnerSession: Calling revokeShare:completion"
+ "SPOwnerSessionLocationFetch - received updated device events but no registered block."
+ "SPOwnerSessionLocationFetch receivedUpdatedDeviceEvents %lu."
+ "SPPeripheralConnectionMaterial"
+ "SPUnauthorizedTrackingAdvertisement %@%@ %@ posh: %i"
+ "T@\"<SPLocalFindableConnectionMaterialMonitoringXPCProtocol>\",&,N,V_proxy"
+ "T@\"NSData\",C,N,V_btAddressData"
+ "T@\"NSData\",C,N,V_btAddressWithTypeData"
+ "T@\"NSData\",C,N,V_irkData"
+ "T@\"NSData\",C,N,V_vendorPayload"
+ "T@\"NSDictionary\",C,N,V_beaconEventByBeaconIdentifier"
+ "T@\"NSMutableSet\",&,N,V_pendingPairingIdentifiers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_cbQueue"
+ "T@\"NSUUID\",R,C,N,V_attachedToDevice"
+ "T@\"SPAttachmentInfo\",R,C,N,V_attachmentInfo"
+ "T@?,C,N,V_deviceEventUpdates"
+ "T@?,C,N,V_peripheralConnectionMaterialCallback"
+ "TB,N,V_isAirTag"
+ "TB,N,V_isFindMyNetwork"
+ "TB,N,V_isPosh"
+ "TB,N,V_nearOwner"
+ "TB,N,V_reportDeviceEvents"
+ "TC,N,V_networkID"
+ "TC,N,V_poshNetwork"
+ "Tq,N,V_advertisementType"
+ "Tq,R,N,V_source"
+ "[SPAccessoryPairingSession initiatePairingAndLocateAccessoryWith:completion:]"
+ "[SPAccessoryPairingSession initiatePairingForAccessoryWith:completion:]"
+ "[SPAccessoryPairingSession pairingStatus:completion:]"
+ "[findingSessionError called from client]. Error %{public}@"
+ "_advertisementType"
+ "_attachedToDevice"
+ "_attachmentInfo"
+ "_beaconEventByBeaconIdentifier"
+ "_btAddressData"
+ "_btAddressWithTypeData"
+ "_cbQueue"
+ "_deviceEventUpdates"
+ "_irkData"
+ "_isAirTag"
+ "_nearOwner"
+ "_networkID"
+ "_pendingPairingIdentifiers"
+ "_peripheralConnectionMaterialCallback"
+ "_poshNetwork"
+ "_reportDeviceEvents"
+ "_vendorPayload"
+ "advertisementType"
+ "attachedToDevice"
+ "attachmentInfo"
+ "beaconEventByBeaconIdentifier"
+ "btAddressData"
+ "btAddressWithTypeData"
+ "cbQueue"
+ "com.apple.icloud.searchpartyd.SPLocalFindableConnectionMaterialMonitoringSession"
+ "com.apple.icloud.searchpartyd.SPLocalFindableConnectionMaterialMonitoringSession.ErrorDomain"
+ "com.apple.icloud.searchpartyd.SPLocalFindableConnectionMaterialMonitoringSession.callback"
+ "com.apple.icloud.searchpartyd.localFindableConnectionMaterialSession"
+ "com.apple.searchparty.SPCBPeerDelegate"
+ "deviceAttachedLocation"
+ "deviceDetachedLocation"
+ "deviceDetectedLocation"
+ "deviceEventUpdates"
+ "hasTag:"
+ "initWithAdvertisementType:poshNetwork:nearOwner:vendorPayload:scanDate:address:advertisement:status:ek:hint:rssi:indexInformation:acccessoryInformation:"
+ "initWithAttachedToDevice:"
+ "initWithTimestamp:source:attachmentInfo:serialNumber:"
+ "initiatePairingAndLocateAccessoryWith:completion:"
+ "initiatePairingAndLocateAccessoryWithIdentifier:completion:"
+ "initiatePairingForAccessoryWith:completion:"
+ "irkData"
+ "isAirTag"
+ "localFindable"
+ "localFindableConnectionMaterial"
+ "nearOwner"
+ "networkID"
+ "pairLowEnergyAccessoryWithIdentifier:completion:"
+ "pairingAgent:peerDidCompletePairing:"
+ "pairingAgent:peerDidFailToCompletePairing:error:"
+ "pairingAgent:peerDidRequestPairing:type:passkey:"
+ "pairingAgent:peerDidUnpair:"
+ "pairingStatus:completion:"
+ "pendingPairingIdentifiers"
+ "peripheralConnectionMaterial for %@"
+ "peripheralConnectionMaterialCallback"
+ "peripheralConnectionMaterialForAccessoryIdentifier:completion:"
+ "poshNetwork"
+ "receivedUpdatedDeviceEvents:"
+ "reportDeviceEvents"
+ "revokeShare:completion:"
+ "setAdvertisementType:"
+ "setBeaconEventByBeaconIdentifier:"
+ "setBtAddressData:"
+ "setBtAddressWithTypeData:"
+ "setCbQueue:"
+ "setDeviceEventUpdateBlock:"
+ "setDeviceEventUpdates:"
+ "setIrkData:"
+ "setIsAirTag:"
+ "setIsFindMyNetwork:"
+ "setIsPosh:"
+ "setNearOwner:"
+ "setNetworkID:"
+ "setPendingPairingIdentifiers:"
+ "setPeripheralConnectionMaterialCallback:"
+ "setPoshNetwork:"
+ "setReportDeviceEvents:"
+ "setVendorPayload:"
+ "sharedPairingAgent"
+ "startFastAdvertisingForBeacon:completion:"
+ "startFindingBeacon:completion:"
+ "startLocalFindableAccessoryDiscoveryWithCompletion:"
+ "startLocalFindableConnectionMaterialMonitoringWithCompletion:"
+ "stopFastAdvertisingForBeacon:completion:"
+ "stopFindingBeacon:completion:"
+ "stopLocalFindableAccessoryDiscoveryWithCompletion:"
+ "stopLocalFindableConnectionMaterialMonitoringWithCompletion:"
+ "submitDeviceEvent:source:attachedTo:completion:"
+ "unpairLowEnergyAccessoryWithIdentifier:completion:"
+ "updatedConnectionMaterialForAccessory:connectionMaterial:"
+ "v24@0:8@\"SPDeviceEventFetchResult\"16"
+ "v24@0:8@?<v@?@\"SPDeviceEventFetchResult\">16"
+ "v24@?0@\"NSError\"8@\"CLLocation\"16"
+ "v32@0:8@\"CBPairingAgent\"16@\"CBPeer\"24"
+ "v32@0:8@\"NSUUID\"16@\"SPPeripheralConnectionMaterial\"24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\"@\"CLLocation\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"SPPeripheralConnectionMaterial\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?q@\"NSError\">24"
+ "v40@0:8@\"CBPairingAgent\"16@\"CBPeer\"24@\"NSError\"32"
+ "v44@0:8@\"NSUUID\"16I24@\"NSUUID\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@16I24@28@?36"
+ "v48@0:8@\"CBPairingAgent\"16@\"CBPeer\"24q32@\"NSNumber\"40"
+ "v48@0:8@16@24q32@40"
+ "vendorPayload"
- "\x14\x12"
- "\x19"
- "-[SPBTFindingSession start] completion. Error %@"
- "-[SPBTFindingSession stop] completion. Error %@"
- "-[SPBTFindingSession updateConfig] completion. Error %@"
- "<%@: %p %@ %lu>"
- "<%@: %p manufacturer: %@ model: %@ productId: %@>"
- "@80@0:8@16@24@32C40C44@48q56@64@72"
- "SPUnauthorizedTrackingAdvertisement %@%@ %@"
- "TB,R,N,V_isFindMyNetwork"
- "TB,R,N,V_isPosh"
- "[findingSessionError called from client]. Error %@"
- "initWithScanDate:address:advertisement:status:ek:hint:rssi:indexInformation:acccessoryInformation:"
- "startFindingBeacons:completion:"
- "stopFindingBeacons:completion:"

```
