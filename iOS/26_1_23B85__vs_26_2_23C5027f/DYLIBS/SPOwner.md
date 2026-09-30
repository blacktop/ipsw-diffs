## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-423.31.7.14.19
-  __TEXT.__text: 0x74aec
+423.32.10.4.2
+  __TEXT.__text: 0x74d1c
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xb0c4
-  __TEXT.__cstring: 0x66b7
+  __TEXT.__objc_methlist: 0xb0dc
+  __TEXT.__cstring: 0x66f7
   __TEXT.__const: 0x468
   __TEXT.__gcc_except_tab: 0x1cc8
-  __TEXT.__oslogstring: 0x73f8
+  __TEXT.__oslogstring: 0x7458
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2590
+  __TEXT.__unwind_info: 0x2598
   __TEXT.__eh_frame: 0x278
   __TEXT.__objc_classname: 0x12ce
-  __TEXT.__objc_methname: 0x12c45
-  __TEXT.__objc_methtype: 0x3750
-  __TEXT.__objc_stubs: 0xa880
+  __TEXT.__objc_methname: 0x12c75
+  __TEXT.__objc_methtype: 0x3782
+  __TEXT.__objc_stubs: 0xa8a0
   __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0x20d0
+  __DATA_CONST.__const: 0x20d8
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ae8
+  __DATA_CONST.__objc_selrefs: 0x3af0
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xb78
-  __AUTH_CONST.__cfstring: 0x5bc0
-  __AUTH_CONST.__objc_const: 0x12f30
+  __AUTH_CONST.__cfstring: 0x5be0
+  __AUTH_CONST.__objc_const: 0x12f38
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1038

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7E1D7E97-D776-33DE-BB28-74D33F82B883
-  Functions: 4147
-  Symbols:   12835
-  CStrings:  5853
+  UUID: 496A8B08-E5AC-36D8-B804-3FA392D63F97
+  Functions: 4150
+  Symbols:   12843
+  CStrings:  5859
 
Symbols:
+ -[SPMetadataFetchingSession executeAccessoryCommand:forBeaconId:completion:]
+ _SPMetadataFetchingSessionErrorDomain
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.274
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.269
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.306
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.307
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.270
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.271
+ ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.211
+ ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.310
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.272
+ ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.213
+ ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.218
+ ___62-[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]_block_invoke.223
+ ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.219
+ ___63-[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]_block_invoke.222
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.309
+ ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.220
+ ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.217
+ ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.215
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.320
+ ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.212
+ ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.214
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.276
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.276.cold.1
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.319
+ ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.216
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.311
+ ___76-[SPMetadataFetchingSession executeAccessoryCommand:forBeaconId:completion:]_block_invoke
+ ___76-[SPMetadataFetchingSession executeAccessoryCommand:forBeaconId:completion:]_block_invoke.221
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.312
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.317
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.315
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.282.cold.1
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.284
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.285
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.289
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.290
+ ___block_literal_global.293
+ ___block_literal_global.297
+ ___block_literal_global.53
+ _objc_msgSend$executeAccessoryCommand:forBeaconId:completion:
- ___33-[SPOwnerSession executeCommand:]_block_invoke.271
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.266
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.303
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.304
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.267
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.268
- ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.205
- ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.307
- ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.269
- ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.207
- ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.212
- ___62-[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]_block_invoke.216
- ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.213
- ___63-[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]_block_invoke.215
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.306
- ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.214
- ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.211
- ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.209
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.317
- ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.206
- ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.208
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.273
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.273.cold.1
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.316
- ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.210
- ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.308
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.309
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.314
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.312
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.279
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.279.cold.1
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.281
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.286
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.284
- ___block_literal_global.290
- ___block_literal_global.294
- ___block_literal_global.50
CStrings:
+ "-[SPMetadataFetchingSession executeAccessoryCommand]"
+ "SPMetadataFetchingSession.executeAccessoryCommand"
+ "com.apple.searchpartyd.SPMetadataFetchingSession.ErrorDomain"
+ "executeAccessoryCommand:forBeaconId:completion:"
+ "v40@0:8Q16@\"NSUUID\"24@?<v@?@\"NSData\"@\"NSError\">32"

```
