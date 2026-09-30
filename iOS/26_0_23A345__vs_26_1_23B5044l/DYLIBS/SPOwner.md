## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-423.30.6.9.29
-  __TEXT.__text: 0x74308
+423.31.7.14.8
+  __TEXT.__text: 0x74678
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xb03c
-  __TEXT.__cstring: 0x6687
+  __TEXT.__objc_methlist: 0xb094
+  __TEXT.__cstring: 0x66b7
   __TEXT.__const: 0x450
-  __TEXT.__gcc_except_tab: 0x1cb4
+  __TEXT.__gcc_except_tab: 0x1cc8
   __TEXT.__oslogstring: 0x7388
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2570
+  __TEXT.__unwind_info: 0x2580
   __TEXT.__eh_frame: 0x278
-  __TEXT.__objc_classname: 0x12cb
-  __TEXT.__objc_methname: 0x12b24
+  __TEXT.__objc_classname: 0x12ce
+  __TEXT.__objc_methname: 0x12c00
   __TEXT.__objc_methtype: 0x3750
-  __TEXT.__objc_stubs: 0xa7c0
+  __TEXT.__objc_stubs: 0xa840
   __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0x20c8
+  __DATA_CONST.__const: 0x20d0
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ab0
+  __DATA_CONST.__objc_selrefs: 0x3ad8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xb78
-  __AUTH_CONST.__cfstring: 0x5b80
-  __AUTH_CONST.__objc_const: 0x12ee0
+  __AUTH_CONST.__cfstring: 0x5bc0
+  __AUTH_CONST.__objc_const: 0x12f20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1218
-  __DATA.__objc_ivar: 0xde4
+  __DATA.__objc_ivar: 0xde8
   __DATA.__data: 0x1478
   __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x1738

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 12B51895-1FC8-3E5C-BE6F-A9A2E654D3EF
-  Functions: 4135
-  Symbols:   12802
-  CStrings:  5838
+  UUID: ADE60DA4-A143-3CDA-811E-264E321C074C
+  Functions: 4141
+  Symbols:   12821
+  CStrings:  5849
 
Symbols:
+ +[SPSimpleBeaconContext fmipItemContextForProductUUIDs:]
+ -[SPOwnerSession(SeparationMonitoring) publishUnificationEventForBeacons:]
+ -[SPSimpleBeaconContext initWithFetchProperties:matchingProductUUIDs:]
+ -[SPSimpleBeaconContext matchingProductUUIDs]
+ -[SPSimpleBeaconContext setMatchingProductUUIDs:]
+ GCC_except_table41
+ _OBJC_IVAR_$_SPSimpleBeaconContext._matchingProductUUIDs
+ _SPSeparationAlertUserInfoAddressKey
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.269
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.264
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.301
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.302
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.265
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.266
+ ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.203
+ ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.305
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.267
+ ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.205
+ ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.210
+ ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.211
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.304
+ ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.212
+ ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.209
+ ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.207
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.315
+ ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.204
+ ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.206
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271.cold.1
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.314
+ ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.208
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.306
+ ___74-[SPOwnerSession(SeparationMonitoring) publishUnificationEventForBeacons:]_block_invoke
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.307
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.312
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.310
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.277.cold.1
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.279
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.280
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.284
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.282
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.285
+ ___block_literal_global.288
+ ___block_literal_global.292
+ _objc_msgSend$initWithFetchProperties:matchingProductUUIDs:
+ _objc_msgSend$matchingProductUUIDs
+ _objc_msgSend$publishUnificationEventForBeacons:
+ _objc_msgSend$setMatchingProductUUIDs:
- ___33-[SPOwnerSession executeCommand:]_block_invoke.267
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.262
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.299
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.300
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.263
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.264
- ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.201
- ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.303
- ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.265
- ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.203
- ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.208
- ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.209
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.302
- ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.210
- ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.207
- ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.205
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.313
- ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.202
- ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.204
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.269
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.269.cold.1
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.312
- ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.206
- ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.304
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.305
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.310
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.308
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.275
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.275.cold.1
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.278
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.282
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.280
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.283
- ___block_literal_global.286
- ___block_literal_global.290
CStrings:
+ "SPSeparationAlertAddressKey"
+ "T@\"NSArray\",C,N,V_matchingProductUUIDs"
+ "_matchingProductUUIDs"
+ "fmipItemContextForProductUUIDs:"
+ "initWithFetchProperties:matchingProductUUIDs:"
+ "matchingProductUUIDs"
+ "publishUnificationEventForBeacons:"
+ "setMatchingProductUUIDs:"

```
