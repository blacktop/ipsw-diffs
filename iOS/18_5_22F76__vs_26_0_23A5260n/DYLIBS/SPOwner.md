## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-396.35.2.11.28
-  __TEXT.__text: 0x73244
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xad24
-  __TEXT.__cstring: 0x6537
-  __TEXT.__const: 0x3e8
-  __TEXT.__gcc_except_tab: 0x1c08
-  __TEXT.__oslogstring: 0x7658
+420.30.5.14.0
+  __TEXT.__text: 0x744b0
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_methlist: 0xaecc
+  __TEXT.__cstring: 0x6617
+  __TEXT.__const: 0x448
+  __TEXT.__gcc_except_tab: 0x1bfc
+  __TEXT.__oslogstring: 0x7b38
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2558
-  __TEXT.__eh_frame: 0x278
-  __TEXT.__objc_classname: 0x124e
-  __TEXT.__objc_methname: 0x125e9
-  __TEXT.__objc_methtype: 0x3841
-  __TEXT.__objc_stubs: 0xa860
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__const: 0x2060
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__eh_frame: 0x250
+  __TEXT.__objc_classname: 0x128b
+  __TEXT.__objc_methname: 0x127f6
+  __TEXT.__objc_methtype: 0x38b9
+  __TEXT.__objc_stubs: 0xa8e0
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x20b0
+  __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39a0
+  __DATA_CONST.__objc_selrefs: 0x3a10
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x330
+  __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x640
-  __AUTH_CONST.__const: 0xb70
-  __AUTH_CONST.__cfstring: 0x5960
-  __AUTH_CONST.__objc_const: 0x12710
+  __AUTH_CONST.__auth_got: 0x638
+  __AUTH_CONST.__const: 0xb50
+  __AUTH_CONST.__cfstring: 0x5a60
+  __AUTH_CONST.__objc_const: 0x129d8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xd80
-  __DATA.__data: 0x14d0
-  __DATA.__bss: 0x5e0
-  __DATA_DIRTY.__objc_data: 0x2590
+  __AUTH.__objc_data: 0x1128
+  __DATA.__objc_ivar: 0xd94
+  __DATA.__data: 0x1478
+  __DATA.__bss: 0x5d0
+  __DATA_DIRTY.__objc_data: 0x1738
   __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__bss: 0x370
+  __DATA_DIRTY.__bss: 0x380
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D580C46C-0AEC-3E92-B03F-42BCC5FCCAC6
-  Functions: 4047
-  Symbols:   12579
-  CStrings:  5763
+  UUID: 8A7CB747-B7A6-3A08-A29C-100657D56156
+  Functions: 4089
+  Symbols:   12680
+  CStrings:  5827
 
Symbols:
+ +[SPDelegatedShareImportContext supportsSecureCoding]
+ +[SPDelegatedShareImportResult supportsSecureCoding]
+ +[SPHandle handleWithRecipient:]
+ -[SPAccessoryDiscoveryAndPairingSession accessoryDetectedForPairing]
+ -[SPAccessoryDiscoveryAndPairingSession notifyPairingAccessoryChanged:]
+ -[SPAccessoryDiscoveryAndPairingSession notifyPairingAccessoryChanged]
+ -[SPAccessoryDiscoveryAndPairingSession pairingAccessoryDetectionCallback]
+ -[SPAccessoryDiscoveryAndPairingSession setNotifyPairingAccessoryChanged:]
+ -[SPAccessoryDiscoveryAndPairingSession setPairingAccessoryDetectionCallback:]
+ -[SPAccessoryDiscoveryAndPairingSession startProximityAccessoryDiscoveryWithCompletion:]
+ -[SPAccessoryDiscoveryAndPairingSession stopProximityAccessoryDiscoveryWithCompletion:]
+ -[SPBeaconSharingManager importDelegatedShare:completion:]
+ -[SPBeaconSharingManager importSharePreview:completion:]
+ -[SPBeaconSharingManager removeImportedShare:completion:]
+ -[SPDelegatedShareImportContext .cxx_destruct]
+ -[SPDelegatedShareImportContext callbackValue]
+ -[SPDelegatedShareImportContext copyWithZone:]
+ -[SPDelegatedShareImportContext encodeWithCoder:]
+ -[SPDelegatedShareImportContext initWithCoder:]
+ -[SPDelegatedShareImportContext initWithUrl:]
+ -[SPDelegatedShareImportContext initWithUrl:callbackValue:]
+ -[SPDelegatedShareImportContext inputUrl]
+ -[SPDelegatedShareImportResult .cxx_destruct]
+ -[SPDelegatedShareImportResult authUrl]
+ -[SPDelegatedShareImportResult copyWithZone:]
+ -[SPDelegatedShareImportResult encodeWithCoder:]
+ -[SPDelegatedShareImportResult initWithAuthUrl:]
+ -[SPDelegatedShareImportResult initWithCoder:]
+ -[SPDelegatedShareImportResult initWithShare:]
+ -[SPDelegatedShareImportResult initWithShare:authUrl:]
+ -[SPDelegatedShareImportResult share]
+ -[SPOwnerSession hasAccessoryWithCapabilities:completion:]
+ -[SPSecureLocationsManager isSatelliteFeatureEnabled]
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table157
+ GCC_except_table165
+ GCC_except_table176
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table204
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table88
+ GCC_except_table90
+ _OBJC_CLASS_$_SPDelegatedShareImportContext
+ _OBJC_CLASS_$_SPDelegatedShareImportResult
+ _OBJC_IVAR_$_SPAccessoryDiscoveryAndPairingSession._notifyPairingAccessoryChanged
+ _OBJC_IVAR_$_SPAccessoryDiscoveryAndPairingSession._pairingAccessoryDetectionCallback
+ _OBJC_IVAR_$_SPDelegatedShareImportContext._callbackValue
+ _OBJC_IVAR_$_SPDelegatedShareImportContext._inputUrl
+ _OBJC_IVAR_$_SPDelegatedShareImportResult._authUrl
+ _OBJC_IVAR_$_SPDelegatedShareImportResult._share
+ _OBJC_METACLASS_$_SPDelegatedShareImportContext
+ _OBJC_METACLASS_$_SPDelegatedShareImportResult
+ _SPBeaconTaskNameFindingExperienceV2
+ _SPBeaconTaskNamePrecisionVFX
+ _SPRemoteUIAlertTypeValueSoftwareUpdate
+ _SPRemoteUIBatteryLevelKey
+ _SPRemoteUIManateeAvailabilityKey
+ _SPRemoteUIMultiDeviceDetectionKey
+ __OBJC_$_CLASS_METHODS_SPDelegatedShareImportContext
+ __OBJC_$_CLASS_METHODS_SPDelegatedShareImportResult
+ __OBJC_$_CLASS_PROP_LIST_SPDelegatedShareImportContext
+ __OBJC_$_CLASS_PROP_LIST_SPDelegatedShareImportResult
+ __OBJC_$_INSTANCE_METHODS_SPDelegatedShareImportContext
+ __OBJC_$_INSTANCE_METHODS_SPDelegatedShareImportResult
+ __OBJC_$_INSTANCE_VARIABLES_SPDelegatedShareImportContext
+ __OBJC_$_INSTANCE_VARIABLES_SPDelegatedShareImportResult
+ __OBJC_$_PROP_LIST_SPDelegatedShareImportContext
+ __OBJC_$_PROP_LIST_SPDelegatedShareImportResult
+ __OBJC_CLASS_PROTOCOLS_$_SPDelegatedShareImportContext
+ __OBJC_CLASS_PROTOCOLS_$_SPDelegatedShareImportResult
+ __OBJC_CLASS_RO_$_SPDelegatedShareImportContext
+ __OBJC_CLASS_RO_$_SPDelegatedShareImportResult
+ __OBJC_METACLASS_RO_$_SPDelegatedShareImportContext
+ __OBJC_METACLASS_RO_$_SPDelegatedShareImportResult
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.269
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.301
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.302
+ ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.197
+ ___48-[SPBeaconSharingManager receivedUpdatedShares:]_block_invoke.173
+ ___49-[SPBeaconSharingManager acceptShare:completion:]_block_invoke.128
+ ___49-[SPBeaconSharingManager removeShare:completion:]_block_invoke.126
+ ___49-[SPBeaconSharingManager revokeShare:completion:]_block_invoke.127
+ ___49-[SPBeaconSharingManager stopSharing:completion:]_block_invoke.130
+ ___50-[SPBeaconSharingManager allSharesWithCompletion:]_block_invoke.136
+ ___50-[SPBeaconSharingManager declineShare:completion:]_block_invoke.129
+ ___50-[SPBeaconSharingManager requestShare:completion:]_block_invoke.125
+ ___52-[SPBeaconSharingManager delegatedShare:completion:]_block_invoke.169
+ ___54-[SPBeaconSharingManager forceStopSharing:completion:]_block_invoke.135
+ ___54-[SPBeaconSharingManager share:recipients:completion:]_block_invoke.122
+ ___54-[SPBeaconSharingManager sharingLimitsWithCompletion:]_block_invoke.163
+ ___55-[SPBeaconSharingManager forceDeclineShare:completion:]_block_invoke.134
+ ___55-[SPBeaconSharingManager isBeaconDelegated:completion:]_block_invoke.172
+ ___56-[SPBeaconSharingManager importSharePreview:completion:]_block_invoke
+ ___56-[SPBeaconSharingManager importSharePreview:completion:]_block_invoke.165
+ ___56-[SPBeaconSharingManager importSharePreview:completion:]_block_invoke_2
+ ___57-[SPBeaconSharingManager removeImportedShare:completion:]_block_invoke
+ ___57-[SPBeaconSharingManager removeImportedShare:completion:]_block_invoke.168
+ ___57-[SPBeaconSharingManager removeImportedShare:completion:]_block_invoke_2
+ ___58-[SPBeaconSharingManager importDelegatedShare:completion:]_block_invoke
+ ___58-[SPBeaconSharingManager importDelegatedShare:completion:]_block_invoke.166
+ ___58-[SPBeaconSharingManager importDelegatedShare:completion:]_block_invoke_2
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.267
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.cold.1
+ ___60-[SPBeaconSharingManager removeExpiredSharesWithCompletion:]_block_invoke.162
+ ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.200
+ ___61-[SPBeaconSharingManager cleanupAllRecordsOfType:completion:]_block_invoke.131
+ ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke.141
+ ___62-[SPBeaconSharingManager updatedCircleIdentifiers:completion:]_block_invoke.150
+ ___63-[SPBeaconSharingManager forceBreakAllSharesOfType:completion:]_block_invoke.132
+ ___63-[SPBeaconSharingManager lookForOrphanedRecordsWithCompletion:]_block_invoke.160
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.304
+ ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke.124
+ ___65-[SPAccessoryDiscoveryAndPairingSession accessoryDiscoveryError:]_block_invoke.cold.1
+ ___65-[SPBeaconSharingManager allSharesIncludingHiddenWithCompletion:]_block_invoke.138
+ ___65-[SPBeaconSharingManager forceBreakAllSharesWithUser:completion:]_block_invoke.133
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.314
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271.cold.1
+ ___68-[SPAccessoryDiscoveryAndPairingSession accessoryDetectedForPairing]_block_invoke
+ ___68-[SPAccessoryDiscoveryAndPairingSession accessoryDetectedForPairing]_block_invoke.cold.1
+ ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke.139
+ ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke_2.140
+ ___68-[SPBeaconSharingManager stopTemporaryItemLocationShare:completion:]_block_invoke.171
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.313
+ ___71-[SPAccessoryDiscoveryAndPairingSession notifyPairingAccessoryChanged:]_block_invoke
+ ___71-[SPAccessoryDiscoveryAndPairingSession notifyPairingAccessoryChanged:]_block_invoke.cold.1
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.305
+ ___75-[SPBeaconSharingManager checkDataIntegrityWithShareIdentifier:completion:]_block_invoke.158
+ ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.198
+ ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.196
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.306
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.311
+ ___83-[SPBeaconSharingManager downloadKeysWithCircleIdentifier:fromBookmark:completion:]_block_invoke.149
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.309
+ ___84-[SPBeaconSharingManager uploadKeysWithCircleIdentifier:isInitialUpload:completion:]_block_invoke.148
+ ___87-[SPAccessoryDiscoveryAndPairingSession stopProximityAccessoryDiscoveryWithCompletion:]_block_invoke
+ ___87-[SPAccessoryDiscoveryAndPairingSession stopProximityAccessoryDiscoveryWithCompletion:]_block_invoke.199
+ ___87-[SPAccessoryDiscoveryAndPairingSession stopProximityAccessoryDiscoveryWithCompletion:]_block_invoke_2
+ ___87-[SPAccessoryDiscoveryAndPairingSession stopProximityAccessoryDiscoveryWithCompletion:]_block_invoke_2.cold.1
+ ___88-[SPAccessoryDiscoveryAndPairingSession startProximityAccessoryDiscoveryWithCompletion:]_block_invoke
+ ___88-[SPAccessoryDiscoveryAndPairingSession startProximityAccessoryDiscoveryWithCompletion:]_block_invoke.194
+ ___88-[SPAccessoryDiscoveryAndPairingSession startProximityAccessoryDiscoveryWithCompletion:]_block_invoke_2
+ ___88-[SPAccessoryDiscoveryAndPairingSession startProximityAccessoryDiscoveryWithCompletion:]_block_invoke_2.cold.1
+ ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.202
+ ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.201
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.277
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.277.cold.1
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.280
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.284
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.282
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.285
+ ___block_descriptor_48_e8_32s40bs_e50_v24?0"SPDelegatedShareImportResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e5_v8?0ls40l8s32l8w48l8
+ ___block_literal_global.168
+ ___block_literal_global.288
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SPOwner
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SPOwner
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SPOwner
+ _objc_msgSend$hasAccessoryWithCapabilities:completion:
+ _objc_msgSend$importDelegatedShare:completion:
+ _objc_msgSend$importSharePreview:completion:
+ _objc_msgSend$initWithShare:authUrl:
+ _objc_msgSend$initWithUrl:callbackValue:
+ _objc_msgSend$inputUrl
+ _objc_msgSend$isSatelliteFeatureEnabled
+ _objc_msgSend$notifyPairingAccessoryChanged
+ _objc_msgSend$pairingAccessoryDetectionCallback
+ _objc_msgSend$removeImportedShare:completion:
+ _objc_msgSend$startProximityAccessoryDiscoveryWithCompletion:
+ _objc_msgSend$stopAccessoryProximityDiscoveryWithCompletion:
- -[SPAccessoryDiscoveryAndPairingSession proximityPairingFinished:]
- -[SPAccessoryDiscoveryAndPairingSession proximityPairingFinishedCallback]
- -[SPAccessoryDiscoveryAndPairingSession setProximityPairingFinishedCallback:]
- -[SPOwnerSession invalidateRegisterIntentDispatchTimer]
- -[SPOwnerSession registerIntentTimerFired]
- -[SPOwnerSession sendRegisterIntentWithCompletion:]
- -[SPOwnerSession sendUnregisterIntentWithCompletion:]
- -[SPOwnerSession setRegisterIntentDispatchTimerWithInterval:]
- GCC_except_table100
- GCC_except_table119
- GCC_except_table131
- GCC_except_table135
- GCC_except_table137
- GCC_except_table139
- GCC_except_table141
- GCC_except_table143
- GCC_except_table145
- GCC_except_table151
- GCC_except_table155
- GCC_except_table161
- GCC_except_table166
- GCC_except_table177
- GCC_except_table180
- GCC_except_table183
- GCC_except_table185
- GCC_except_table198
- GCC_except_table203
- GCC_except_table208
- GCC_except_table213
- GCC_except_table60
- GCC_except_table64
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table80
- GCC_except_table91
- _OBJC_IVAR_$_SPAccessoryDiscoveryAndPairingSession._proximityPairingFinishedCallback
- _SPAccessoryProximityDiscoveryAndPairingSessionErrorDomain
- _SPRemoteUIUserNameKey
- ___32-[SPOwnerSession stopRefreshing]_block_invoke.290
- ___33-[SPOwnerSession executeCommand:]_block_invoke.268
- ___33-[SPOwnerSession startRefreshing]_block_invoke_6
- ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke
- ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.286
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.305
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.306
- ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.196
- ___48-[SPBeaconSharingManager receivedUpdatedShares:]_block_invoke.164
- ___49-[SPBeaconSharingManager acceptShare:completion:]_block_invoke.123
- ___49-[SPBeaconSharingManager removeShare:completion:]_block_invoke.121
- ___49-[SPBeaconSharingManager revokeShare:completion:]_block_invoke.122
- ___49-[SPBeaconSharingManager stopSharing:completion:]_block_invoke.125
- ___50-[SPBeaconSharingManager allSharesWithCompletion:]_block_invoke.131
- ___50-[SPBeaconSharingManager declineShare:completion:]_block_invoke.124
- ___50-[SPBeaconSharingManager requestShare:completion:]_block_invoke.120
- ___51-[SPOwnerSession sendRegisterIntentWithCompletion:]_block_invoke
- ___52-[SPBeaconSharingManager delegatedShare:completion:]_block_invoke.160
- ___53-[SPOwnerSession sendUnregisterIntentWithCompletion:]_block_invoke
- ___54-[SPBeaconSharingManager forceStopSharing:completion:]_block_invoke.130
- ___54-[SPBeaconSharingManager share:recipients:completion:]_block_invoke.117
- ___54-[SPBeaconSharingManager sharingLimitsWithCompletion:]_block_invoke.158
- ___55-[SPBeaconSharingManager forceDeclineShare:completion:]_block_invoke.129
- ___55-[SPBeaconSharingManager isBeaconDelegated:completion:]_block_invoke.163
- ___60-[SPBeaconSharingManager removeExpiredSharesWithCompletion:]_block_invoke.157
- ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.198
- ___61-[SPBeaconSharingManager cleanupAllRecordsOfType:completion:]_block_invoke.126
- ___61-[SPBeaconSharingManager stopRefreshingSharesWithCompletion:]_block_invoke.136
- ___61-[SPOwnerSession setRegisterIntentDispatchTimerWithInterval:]_block_invoke
- ___62-[SPBeaconSharingManager updatedCircleIdentifiers:completion:]_block_invoke.145
- ___63-[SPBeaconSharingManager forceBreakAllSharesOfType:completion:]_block_invoke.127
- ___63-[SPBeaconSharingManager lookForOrphanedRecordsWithCompletion:]_block_invoke.155
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.308
- ___64-[SPBeaconSharingManager share:recipients:shareType:completion:]_block_invoke.119
- ___65-[SPBeaconSharingManager allSharesIncludingHiddenWithCompletion:]_block_invoke.133
- ___65-[SPBeaconSharingManager forceBreakAllSharesWithUser:completion:]_block_invoke.128
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.318
- ___66-[SPAccessoryDiscoveryAndPairingSession proximityPairingFinished:]_block_invoke
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.270
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.270.cold.1
- ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke.134
- ___68-[SPBeaconSharingManager startRefreshingSharesWithBlock:completion:]_block_invoke_2.135
- ___68-[SPBeaconSharingManager stopTemporaryItemLocationShare:completion:]_block_invoke.162
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.317
- ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.309
- ___75-[SPBeaconSharingManager checkDataIntegrityWithShareIdentifier:completion:]_block_invoke.153
- ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.197
- ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.194
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.310
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.315
- ___83-[SPBeaconSharingManager downloadKeysWithCircleIdentifier:fromBookmark:completion:]_block_invoke.144
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.313
- ___84-[SPBeaconSharingManager uploadKeysWithCircleIdentifier:isInitialUpload:completion:]_block_invoke.143
- ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.200
- ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.199
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.276
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.276.cold.1
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.278
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.283
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.281
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.284
- ___block_descriptor_40_e8_32s_e20_v24?0d8"NSError"16ls32l8
- ___block_literal_global.167
- ___block_literal_global.289
- ___block_literal_global.296
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_SPOwner
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_SPOwner
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_SPOwner
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_SPOwner
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_SPOwner
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_SPOwner
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_SPOwner
- _objc_msgSend$invalidateRegisterIntentDispatchTimer
- _objc_msgSend$proximityPairingFinishedCallback
- _objc_msgSend$registerIntentDispatchTimer
- _objc_msgSend$registerIntentTimerFired
- _objc_msgSend$sendRegisterIntentWithCompletion:
- _objc_msgSend$sendUnregisterIntentWithCompletion:
- _objc_msgSend$setRegisterIntentDispatchTimer:
- _objc_msgSend$setRegisterIntentDispatchTimerWithInterval:
- _swift_release_n
CStrings:
+ "\r"
+ "-[SPAccessoryDiscoverySession startProximityAccessoryDiscovery]"
+ "-[SPAccessoryDiscoverySession startProximityAccessoryDiscovery] completion"
+ "-[SPAccessoryDiscoverySession startProximityAccessoryDiscovery] completion. Error %@"
+ "-[SPAccessoryDiscoverySession stopProximityAccessoryDiscovery]"
+ "-[SPAccessoryDiscoverySession stopProximityAccessoryDiscovery] completion)"
+ "-[SPAccessoryDiscoverySession stopProximityAccessoryDiscovery] completion. Error %@"
+ "-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke"
+ "@\"SPBeaconShare\""
+ "Imported delegated share %@ (%@)"
+ "Importing delegated share %@"
+ "Previewed delegated share for import url %@ (%@)"
+ "Previewing delegated share for import url %@"
+ "Remove imported share %@ (%@)"
+ "Removing imported share %@"
+ "SPAccessoryDiscoverySession.stopProximityAccessoryDiscovery"
+ "SPDelegatedShareImportContext"
+ "SPDelegatedShareImportResult"
+ "SPOwnerSession hasAccessoryWithCapabilities called with none."
+ "SPOwnerSession: Calling hasAccessoryWithCapabilities:completion:"
+ "SPOwnerSession: Calling importDelegatedShare:completion"
+ "SPOwnerSession: Calling importSharePreview:completion"
+ "SPOwnerSession: Calling removeImportedShare:completion"
+ "T@\"NSString\",R,C,N,V_authUrl"
+ "T@\"NSString\",R,C,N,V_callbackValue"
+ "T@\"NSString\",R,C,N,V_inputUrl"
+ "T@\"SPBeaconShare\",R,C,N,V_share"
+ "T@?,C,N,V_notifyPairingAccessoryChanged"
+ "T@?,C,N,V_pairingAccessoryDetectionCallback"
+ "[accessoryDetectedForPairing called from client]"
+ "[accessoryDetectedForPairing called from client] but `pairingAccessoryDetectionCallback` is not set"
+ "[accessoryDiscoveryError called from client] but `accessoryDiscoveryErrorCallback` is not set"
+ "[accessoryDiscoveryError called from client] but `proximityPairingErrorCallback` is not set"
+ "[notifyPairingAccessoryChanged called from client]"
+ "[notifyPairingAccessoryChanged called from client] but `notifyPairingAccessoryChanged` is not set"
+ "[proximityPairingCompleted called from client] but `proximityPairingCompletedCallback` is not set"
+ "_authUrl"
+ "_callbackValue"
+ "_inputUrl"
+ "_notifyPairingAccessoryChanged"
+ "_pairingAccessoryDetectionCallback"
+ "_share"
+ "accessoryDetectedForPairing"
+ "authUrl"
+ "callbackValue"
+ "com.apple.icloud.spowner.task.findingExperienceV2"
+ "com.apple.icloud.spowner.task.precisionVFX"
+ "handleWithRecipient:"
+ "hasAccessoryWithCapabilities:completion:"
+ "importDelegatedShare:completion:"
+ "importSharePreview:completion:"
+ "initWithAuthUrl:"
+ "initWithShare:"
+ "initWithShare:authUrl:"
+ "initWithUrl:"
+ "initWithUrl:callbackValue:"
+ "inputUrl"
+ "isSatelliteFeatureEnabled"
+ "notifyPairingAccessoryChanged"
+ "notifyPairingAccessoryChanged:"
+ "pairing-battery-level"
+ "pairing-manatee-availability"
+ "pairing-multi-device-detection"
+ "pairingAccessoryDetectionCallback"
+ "proximityPairingCompletedCallback is set"
+ "removeImportedShare:completion:"
+ "setNotifyPairingAccessoryChanged:"
+ "setPairingAccessoryDetectionCallback:"
+ "share"
+ "software-update-alert"
+ "stopProximityAccessoryDiscoveryWithCompletion:"
+ "v24@?0@\"SPDelegatedShareImportResult\"8@\"NSError\"16"
+ "v32@0:8@\"SPDelegatedShareImportContext\"16@?<v@?@\"SPDelegatedShareImportResult\"@\"NSError\">24"
+ "v32@0:8@\"SPDelegatedShareImportContext\"16@?<v@?B@\"NSError\">24"
- "SPBeaconManager registerIntentTimerFired"
- "SPOwnerSession register intent dispatch timer fired"
- "SPOwnerSession: Error scheduling intents: %@"
- "SPOwnerSession: Error stopping intent session: %@"
- "SPOwnerSession: Successfully sent RegisterIntent message (retryInterval: %f)"
- "SPOwnerSession: Successfully sent UnregisterIntent message"
- "T@?,C,N,V_proximityPairingFinishedCallback"
- "[proximityPairingFinished called from client]. Location %@"
- "_proximityPairingFinishedCallback"
- "com.apple.icloud.searchpartyd.SPAccessoryProximityDiscoveryAndPairingSessionErrorDomain.ErrorDomain"
- "invalidateRegisterIntentDispatchTimer"
- "pairing-user-name"
- "proximityPairingFinished:"
- "proximityPairingFinishedCallback"
- "registerIntentTimerFired"
- "sendRegisterIntentWithCompletion:"
- "sendUnregisterIntentWithCompletion:"
- "setProximityPairingFinishedCallback:"
- "setRegisterIntentDispatchTimerWithInterval:"
- "v24@0:8@\"CLLocation\"16"
- "v24@0:8@?<v@?d@\"NSError\">16"
- "v24@?0d8@\"NSError\"16"

```
