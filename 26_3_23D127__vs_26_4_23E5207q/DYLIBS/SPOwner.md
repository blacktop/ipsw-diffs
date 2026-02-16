## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-423.33.11.19.4
-  __TEXT.__text: 0x74d74
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xb0f4
-  __TEXT.__cstring: 0x66f7
+423.34.7.18.24
+  __TEXT.__text: 0x79ba0
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0xb11c
+  __TEXT.__cstring: 0x65d7
   __TEXT.__const: 0x468
-  __TEXT.__gcc_except_tab: 0x1cc8
-  __TEXT.__oslogstring: 0x7458
+  __TEXT.__gcc_except_tab: 0x1dac
+  __TEXT.__oslogstring: 0x7498
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2598
-  __TEXT.__eh_frame: 0x278
-  __TEXT.__objc_classname: 0x12ce
-  __TEXT.__objc_methname: 0x12c86
-  __TEXT.__objc_methtype: 0x3782
-  __TEXT.__objc_stubs: 0xa8a0
+  __TEXT.__unwind_info: 0x2950
+  __TEXT.__eh_frame: 0x2c0
+  __TEXT.__objc_classname: 0x135e
+  __TEXT.__objc_methname: 0x12cc7
+  __TEXT.__objc_methtype: 0x37b8
+  __TEXT.__objc_stubs: 0xa8e0
   __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__const: 0x20d8
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3af0
+  __DATA_CONST.__objc_selrefs: 0x3af8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x640
-  __AUTH_CONST.__const: 0xb78
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0xb71
   __AUTH_CONST.__cfstring: 0x5be0
-  __AUTH_CONST.__objc_const: 0x12f68
+  __AUTH_CONST.__objc_const: 0x12f78
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1038
   __DATA.__objc_ivar: 0xdec
-  __DATA.__data: 0x1488
+  __DATA.__data: 0x1478
   __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x1918
-  __DATA_DIRTY.__data: 0x1a8
+  __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x370
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6814B365-C087-356D-9DD7-A12DD9FD22A9
-  Functions: 4152
-  Symbols:   12848
-  CStrings:  5860
+  UUID: 245587F7-3249-3EB3-8141-5E7C1576B852
+  Functions: 4163
+  Symbols:   12884
+  CStrings:  5859
 
Symbols:
+ -[SPOwnerSession ownerCheckForBeaconUUID:completion:]
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table204
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.276
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.271
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.308
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.309
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.272
+ ___53-[SPOwnerSession ownerCheckForBeaconUUID:completion:]_block_invoke
+ ___53-[SPOwnerSession ownerCheckForBeaconUUID:completion:]_block_invoke.313
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.273
+ ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.213
+ ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.312
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.274
+ ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.215
+ ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.220
+ ___62-[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]_block_invoke.225
+ ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.221
+ ___63-[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]_block_invoke.224
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.311
+ ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.222
+ ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.219
+ ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.217
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.323
+ ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.214
+ ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.216
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.278
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.278.cold.1
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.322
+ ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.218
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.314
+ ___76-[SPMetadataFetchingSession executeAccessoryCommand:forBeaconId:completion:]_block_invoke.223
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.315
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.320
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.318
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.284.cold.1
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.286
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.287
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.291
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.289
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.292
+ ___block_literal_global.295
+ ___block_literal_global.299
+ _objc_msgSend$init
+ _objc_msgSend$ownerCheckForBeaconUUID:completion:
- GCC_except_table173
- GCC_except_table186
- GCC_except_table191
- GCC_except_table196
- GCC_except_table201
- ___33-[SPOwnerSession executeCommand:]_block_invoke.274
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.269
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.306
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.307
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.270
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.271
- ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.211
- ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.310
- ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.272
- ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.213
- ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.218
- ___62-[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]_block_invoke.223
- ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.219
- ___63-[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]_block_invoke.222
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.309
- ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.220
- ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.217
- ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.215
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.320
- ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.212
- ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.214
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.276
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.276.cold.1
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.319
- ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.216
- ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.311
- ___76-[SPMetadataFetchingSession executeAccessoryCommand:forBeaconId:completion:]_block_invoke.221
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.312
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.317
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.315
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.282
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.282.cold.1
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.285
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.289
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.287
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.290
- ___block_literal_global.293
- ___block_literal_global.297
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "SPOwnerSession.ownerCheckForBeaconUUID"
+ "ownerCheckForBeaconUUID %@"
+ "ownerCheckForBeaconUUID:completion:"
+ "v32@0:8@\"NSUUID\"16@?<v@?q@\"NSError\">24"

```
