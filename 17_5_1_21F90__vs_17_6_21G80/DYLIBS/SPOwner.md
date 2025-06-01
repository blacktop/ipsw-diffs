## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-360.20.0.1.0
-  __TEXT.__text: 0x6a53c
+361.13.0.0.0
+  __TEXT.__text: 0x6b968
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x87b0
-  __TEXT.__cstring: 0x601e
+  __TEXT.__objc_methlist: 0x8970
+  __TEXT.__cstring: 0x60be
   __TEXT.__const: 0x370
-  __TEXT.__gcc_except_tab: 0x1320
-  __TEXT.__oslogstring: 0x6cd9
+  __TEXT.__gcc_except_tab: 0x134c
+  __TEXT.__oslogstring: 0x6e34
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x122
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x24d8
+  __TEXT.__unwind_info: 0x2544
   __TEXT.__eh_frame: 0x240
-  __TEXT.__objc_classname: 0x1090
-  __TEXT.__objc_methname: 0x11105
-  __TEXT.__objc_methtype: 0x3388
-  __TEXT.__objc_stubs: 0x9da0
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1ee0
-  __DATA_CONST.__objc_classlist: 0x3a0
+  __TEXT.__objc_classname: 0x10ef
+  __TEXT.__objc_methname: 0x112c7
+  __TEXT.__objc_methtype: 0x343b
+  __TEXT.__objc_stubs: 0x9f00
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0x1f48
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10240
-  __DATA_CONST.__objc_selrefs: 0x3430
-  __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_classrefs: 0x4b8
-  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__objc_const: 0x104b8
+  __DATA_CONST.__objc_selrefs: 0x3490
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_classrefs: 0x4d0
+  __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x5360
-  __AUTH_CONST.__objc_const: 0x3ac8
+  __AUTH_CONST.__cfstring: 0x54a0
+  __AUTH_CONST.__objc_const: 0x3c78
   __AUTH_CONST.__const: 0xb70
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x628
-  __AUTH.__objc_data: 0xf98
-  __DATA.__objc_ivar: 0xc78
+  __AUTH.__objc_data: 0x1088
+  __DATA.__objc_ivar: 0xc90
   __DATA.__objc_data: 0x20
   __DATA.__data: 0x13e8
   __DATA.__bss: 0x5e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6FCDD8E1-A713-343A-AC30-814AEBEDA776
-  Functions: 3726
-  Symbols:   11527
-  CStrings:  5432
+  UUID: 9D6E0C2C-B0C8-310A-9B40-E3C496A0431A
+  Functions: 3770
+  Symbols:   11675
+  CStrings:  5481
 
Symbols:
+ +[SPAccessoryDiscoveryPairingStatusRequest supportsSecureCoding]
+ +[SPAccessoryDiscoveryPairingStatusResult supportsSecureCoding]
+ +[SPBeaconIndex supportsSecureCoding]
+ -[SPAccessoryDiscoveryAndPairingSession pairingStatusWithRequest:completion:]
+ -[SPAccessoryDiscoveryPairingStatusRequest .cxx_destruct]
+ -[SPAccessoryDiscoveryPairingStatusRequest copyWithZone:]
+ -[SPAccessoryDiscoveryPairingStatusRequest encodeWithCoder:]
+ -[SPAccessoryDiscoveryPairingStatusRequest identifier]
+ -[SPAccessoryDiscoveryPairingStatusRequest initWithCoder:]
+ -[SPAccessoryDiscoveryPairingStatusRequest initWithIdentifier:]
+ -[SPAccessoryDiscoveryPairingStatusRequest setIdentifier:]
+ -[SPAccessoryDiscoveryPairingStatusRequest setWantsLostModeInfo:]
+ -[SPAccessoryDiscoveryPairingStatusRequest wantsLostModeInfo]
+ -[SPAccessoryDiscoveryPairingStatusResult .cxx_destruct]
+ -[SPAccessoryDiscoveryPairingStatusResult copyWithZone:]
+ -[SPAccessoryDiscoveryPairingStatusResult encodeWithCoder:]
+ -[SPAccessoryDiscoveryPairingStatusResult initWithCoder:]
+ -[SPAccessoryDiscoveryPairingStatusResult initWithPairingStatus:lostModeInfo:]
+ -[SPAccessoryDiscoveryPairingStatusResult lostModeInfo]
+ -[SPAccessoryDiscoveryPairingStatusResult pairingStatus]
+ -[SPBeaconIndex copyWithZone:]
+ -[SPBeaconIndex encodeWithCoder:]
+ -[SPBeaconIndex index]
+ -[SPBeaconIndex initWithCoder:]
+ -[SPBeaconIndex initWithSequence:index:]
+ -[SPBeaconIndex sequence]
+ -[SPBeaconIndex setIndex:]
+ -[SPBeaconIndex setSequence:]
+ -[SPCBLeechScanner centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.1
+ -[SPCBLeechScanner containsOnlyNSSecureCodable:]
+ -[SPCBLeechScanner containsOnlyNSSecureCodable:].cold.1
+ -[SPCBLeechScanner containsOnlyNSSecureCodable:].cold.2
+ -[SPCBLeechScanner fixupDictionary:]
+ -[SPOwnerSession hintBasedIndexSearchForBeacon:baseIndex:hint:completion:]
+ -[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table192
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table207
+ GCC_except_table63
+ GCC_except_table73
+ _CBAdvertisementDataServiceDataKey
+ _OBJC_CLASS_$_SPAccessoryDiscoveryPairingStatusRequest
+ _OBJC_CLASS_$_SPAccessoryDiscoveryPairingStatusResult
+ _OBJC_CLASS_$_SPBeaconIndex
+ _OBJC_IVAR_$_SPAccessoryDiscoveryPairingStatusRequest._identifier
+ _OBJC_IVAR_$_SPAccessoryDiscoveryPairingStatusRequest._wantsLostModeInfo
+ _OBJC_IVAR_$_SPAccessoryDiscoveryPairingStatusResult._lostModeInfo
+ _OBJC_IVAR_$_SPAccessoryDiscoveryPairingStatusResult._pairingStatus
+ _OBJC_IVAR_$_SPBeaconIndex._index
+ _OBJC_IVAR_$_SPBeaconIndex._sequence
+ _OBJC_METACLASS_$_SPAccessoryDiscoveryPairingStatusRequest
+ _OBJC_METACLASS_$_SPAccessoryDiscoveryPairingStatusResult
+ _OBJC_METACLASS_$_SPBeaconIndex
+ _SPRemoteUIAlertTypeKey
+ _SPRemoteUIAlertTypeValueLostMode
+ _SPRemoteUILostModeAssetURLKey
+ _SPRemoteUILostModeDeviceTypeKey
+ _SPRemoteUILostModeDeviceTypePencil
+ _SPRemoteUILostModeInfoKey
+ _SPRemoteUILostModeOwnerEmailKey
+ _SPRemoteUILostModeOwnerPhoneKey
+ __OBJC_$_CLASS_METHODS_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_$_CLASS_METHODS_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_$_CLASS_METHODS_SPBeaconIndex
+ __OBJC_$_CLASS_PROP_LIST_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_$_CLASS_PROP_LIST_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_$_CLASS_PROP_LIST_SPBeaconIndex
+ __OBJC_$_INSTANCE_METHODS_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_$_INSTANCE_METHODS_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_$_INSTANCE_METHODS_SPBeaconIndex
+ __OBJC_$_INSTANCE_VARIABLES_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_$_INSTANCE_VARIABLES_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_$_INSTANCE_VARIABLES_SPBeaconIndex
+ __OBJC_$_PROP_LIST_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_$_PROP_LIST_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_$_PROP_LIST_SPBeaconIndex
+ __OBJC_CLASS_PROTOCOLS_$_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_CLASS_PROTOCOLS_$_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_CLASS_PROTOCOLS_$_SPBeaconIndex
+ __OBJC_CLASS_RO_$_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_CLASS_RO_$_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_CLASS_RO_$_SPBeaconIndex
+ __OBJC_METACLASS_RO_$_SPAccessoryDiscoveryPairingStatusRequest
+ __OBJC_METACLASS_RO_$_SPAccessoryDiscoveryPairingStatusResult
+ __OBJC_METACLASS_RO_$_SPBeaconIndex
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ ___32-[SPOwnerSession stopRefreshing]_block_invoke.277
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.262
+ ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.273
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.258
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.295
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.296
+ ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.150
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.259
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.260
+ ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.152
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.298
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.308
+ ___66-[SPAccessoryDiscoveryAndPairingSession pairingStatus:completion:]_block_invoke_2
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.264
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.264.cold.1
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.307
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.299
+ ___74-[SPOwnerSession hintBasedIndexSearchForBeacon:baseIndex:hint:completion:]_block_invoke
+ ___74-[SPOwnerSession hintBasedIndexSearchForBeacon:baseIndex:hint:completion:]_block_invoke_2
+ ___74-[SPOwnerSession hintBasedIndexSearchForBeacon:baseIndex:hint:completion:]_block_invoke_3
+ ___77-[SPAccessoryDiscoveryAndPairingSession pairingStatusWithRequest:completion:]_block_invoke
+ ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.151
+ ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.148
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.300
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.305
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.303
+ ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.154
+ ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.153
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.268
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.269
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.270
+ ___block_descriptor_40_e8_32bs_e61_v24?0"SPAccessoryDiscoveryPairingStatusResult"8"NSError"16ls32l8
+ ___block_literal_global.129
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.284
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$containsOnlyNSSecureCodable:
+ _objc_msgSend$fixupDictionary:
+ _objc_msgSend$hintBasedIndexSearchForBeacon:baseIndex:hint:completion:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithPairingStatus:lostModeInfo:
+ _objc_msgSend$initWithSequence:index:
+ _objc_msgSend$pairingStatus
+ _objc_msgSend$pairingStatusWithRequest:completion:
+ _objc_msgSend$setWantsLostModeInfo:
+ _objc_msgSend$stopFetchingUnauthorizedEncryptedPayloadWithCompletion:
+ _objc_msgSend$wantsLostModeInfo
- GCC_except_table176
- GCC_except_table185
- GCC_except_table190
- GCC_except_table195
- GCC_except_table200
- GCC_except_table45
- ___32-[SPOwnerSession stopRefreshing]_block_invoke.273
- ___33-[SPOwnerSession executeCommand:]_block_invoke.258
- ___42-[SPOwnerSession registerIntentTimerFired]_block_invoke.269
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.254
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.291
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.292
- ___45-[SPAccessoryDiscoveryAndPairingSession stop]_block_invoke.82
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.255
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.256
- ___61-[SPAccessoryDiscoveryAndPairingSession discoveredAccessory:]_block_invoke.84
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.294
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.302
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.260
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.260.cold.1
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.301
- ___78-[SPAccessoryDiscoveryAndPairingSession stopAccessoryDiscoveryWithCompletion:]_block_invoke.83
- ___79-[SPAccessoryDiscoveryAndPairingSession startAccessoryDiscoveryWithCompletion:]_block_invoke.80
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.295
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.299
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.297
- ___91-[SPAccessoryDiscoveryAndPairingSession stopLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.86
- ___92-[SPAccessoryDiscoveryAndPairingSession startLocalFindableAccessoryDiscoveryWithCompletion:]_block_invoke.85
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.264
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.265
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.266
- ___block_literal_global.272
- ___block_literal_global.275
- ___block_literal_global.280
- _objc_msgSend$pairingStatus:completion:
CStrings:
+ "@28@0:8C16Q20"
+ "SPAccessoryDiscoveryPairingStatusRequest"
+ "SPAccessoryDiscoveryPairingStatusResult"
+ "SPBeaconIndex"
+ "SPCBLeechScanner: NSDictionary key not NSSecureCodable: %@: %@!"
+ "SPCBLeechScanner: advertisementData is not NSSecureCodable!"
+ "SPCBLeechScanner: not NSSecureCodable: %@: %@!"
+ "SPOwnerSession.stopFetchingUnauthorizedEncryptedPayload"
+ "T@\"SPLostModeInfo\",R,N,V_lostModeInfo"
+ "TB,N,V_wantsLostModeInfo"
+ "Tq,R,N,V_pairingStatus"
+ "UNDER_TEST"
+ "[SPAccessoryPairingSession pairingStatusWithRequest:completion:]"
+ "_pairingStatus"
+ "_wantsLostModeInfo"
+ "alert-type"
+ "asset-url"
+ "containsOnlyNSSecureCodable:"
+ "device-type"
+ "fetchUnauthorizedEncryptedPayload %@"
+ "fixupDictionary:"
+ "hintBasedIndexSearchForBeacon:baseIndex:hint:completion:"
+ "initWithIdentifier:"
+ "initWithPairingStatus:lostModeInfo:"
+ "initWithSequence:index:"
+ "lost-mode-alert"
+ "lost-mode-info"
+ "owner-email"
+ "owner-phone"
+ "pairingStatus"
+ "pairingStatusWithRequest:completion:"
+ "pencil"
+ "setWantsLostModeInfo:"
+ "stopFetchingUnauthorizedEncryptedPayload"
+ "stopFetchingUnauthorizedEncryptedPayloadWithCompletion:"
+ "v24@?0@\"SPAccessoryDiscoveryPairingStatusResult\"8@\"NSError\"16"
+ "v32@0:8@\"SPAccessoryDiscoveryPairingStatusRequest\"16@?<v@?@\"SPAccessoryDiscoveryPairingStatusResult\"@\"NSError\">24"
+ "v44@0:8@\"NSUUID\"16@\"SPBeaconIndex\"24C32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@16@24C32@?36"
+ "wantsLostModeInfo"
- "XCTestConfigurationFilePath"
- "unauthorizedConnect %@"
- "v32@0:8@\"NSUUID\"16@?<v@?q@\"NSError\">24"

```
