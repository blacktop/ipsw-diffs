## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-423.31.7.14.8
-  __TEXT.__text: 0x74678
+423.31.7.14.16
+  __TEXT.__text: 0x74ab8
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xb094
+  __TEXT.__objc_methlist: 0xb0c4
   __TEXT.__cstring: 0x66b7
   __TEXT.__const: 0x450
   __TEXT.__gcc_except_tab: 0x1cc8
-  __TEXT.__oslogstring: 0x7388
+  __TEXT.__oslogstring: 0x73f8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2580
+  __TEXT.__unwind_info: 0x2590
   __TEXT.__eh_frame: 0x278
   __TEXT.__objc_classname: 0x12ce
-  __TEXT.__objc_methname: 0x12c00
+  __TEXT.__objc_methname: 0x12c45
   __TEXT.__objc_methtype: 0x3750
-  __TEXT.__objc_stubs: 0xa840
+  __TEXT.__objc_stubs: 0xa880
   __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__const: 0x20d0
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ad8
+  __DATA_CONST.__objc_selrefs: 0x3ae8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xb78
   __AUTH_CONST.__cfstring: 0x5bc0
-  __AUTH_CONST.__objc_const: 0x12f20
+  __AUTH_CONST.__objc_const: 0x12f30
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1218
+  __AUTH.__objc_data: 0x1038
   __DATA.__objc_ivar: 0xde8
   __DATA.__data: 0x1478
   __DATA.__bss: 0x5d0
-  __DATA_DIRTY.__objc_data: 0x1738
+  __DATA_DIRTY.__objc_data: 0x1918
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x370
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: ADE60DA4-A143-3CDA-811E-264E321C074C
-  Functions: 4141
-  Symbols:   12821
-  CStrings:  5849
+  UUID: 6A10031B-F725-3ED6-8AB3-0EFF346C5AE1
+  Functions: 4147
+  Symbols:   12835
+  CStrings:  5853
 
Symbols:
+ -[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]
+ -[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]
+ ___33-[SPOwnerSession executeCommand:]_block_invoke.271
+ ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.266
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.303
+ ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.304
+ ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.267
+ ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.268
+ ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.205
+ ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.307
+ ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.269
+ ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.207
+ ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.212
+ ___62-[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]_block_invoke
+ ___62-[SPMetadataFetchingSession fetchiCloudIdentifier:completion:]_block_invoke.216
+ ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.213
+ ___63-[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]_block_invoke
+ ___63-[SPMetadataFetchingSession fetchCurrentPrimaryKey:completion:]_block_invoke.215
+ ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.306
+ ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.214
+ ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.211
+ ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.209
+ ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.317
+ ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.206
+ ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.208
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.273
+ ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.273.cold.1
+ ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.316
+ ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.210
+ ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.308
+ ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.309
+ ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.314
+ ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.312
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.279.cold.1
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.281
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.282
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.286
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.284
+ ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.287
+ ___block_literal_global.290
+ ___block_literal_global.294
+ _objc_msgSend$fetchCurrentPrimaryKey:completion:
+ _objc_msgSend$fetchiCloudIdentifier:completion:
- ___33-[SPOwnerSession executeCommand:]_block_invoke.269
- ___43-[SPOwnerSession beaconForUUID:completion:]_block_invoke.264
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.301
- ___44-[SPOwnerSession executeUTPlaySoundCommand:]_block_invoke.302
- ___49-[SPOwnerSession beaconForIdentifier:completion:]_block_invoke.265
- ___54-[SPOwnerSession beaconGroupForIdentifier:completion:]_block_invoke.266
- ___57-[SPMetadataFetchingSession fetchProductData:completion:]_block_invoke.203
- ___57-[SPOwnerSession fetchHawkeyeFirmwareVersion:completion:]_block_invoke.305
- ___58-[SPOwnerSession hasAccessoryWithCapabilities:completion:]_block_invoke.267
- ___59-[SPMetadataFetchingSession fetchModelNameData:completion:]_block_invoke.205
- ___61-[SPMetadataFetchingSession fetchBatteryTypeData:completion:]_block_invoke.210
- ___63-[SPMetadataFetchingSession fetchBatteryStatusData:completion:]_block_invoke.211
- ___63-[SPOwnerSession fetchUnauthorizedEncryptedPayload:completion:]_block_invoke.304
- ___64-[SPMetadataFetchingSession fetchModelColorCodeData:completion:]_block_invoke.212
- ___65-[SPMetadataFetchingSession fetchFirmwareVersionData:completion:]_block_invoke.209
- ___65-[SPMetadataFetchingSession fetchProtocolVersionData:completion:]_block_invoke.207
- ___65-[SPOwnerSession readAISMetadataFromBeaconIdentifier:completion:]_block_invoke.315
- ___66-[SPMetadataFetchingSession fetchManufacturerNameData:completion:]_block_invoke.204
- ___67-[SPMetadataFetchingSession fetchAccessoryCategoryData:completion:]_block_invoke.206
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271
- ___67-[SPOwnerSession finishBeaconGroupFuture:command:commandIssueDate:]_block_invoke.271.cold.1
- ___68-[SPOwnerSession readRawAISMetadataFromBeaconIdentifier:completion:]_block_invoke.314
- ___71-[SPMetadataFetchingSession fetchAccessoryCapabilitiesData:completion:]_block_invoke.208
- ___73-[SPOwnerSession stopFetchingUnauthorizedEncryptedPayloadWithCompletion:]_block_invoke.306
- ___80-[SPOwnerSession peripheralConnectionMaterialForAccessoryIdentifier:completion:]_block_invoke.307
- ___80-[SPOwnerSession readAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.312
- ___83-[SPOwnerSession readRawAISMetadataFromMACAddress:useOwnerControlPoint:completion:]_block_invoke.310
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.277
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.277.cold.1
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.280
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke.284
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.282
- ___98-[SPOwnerSession addBeaconChangedListener:beaconUUID:taskName:commandIdentifier:commandIssueDate:]_block_invoke_2.285
- ___block_literal_global.288
- ___block_literal_global.292
CStrings:
+ "-[SPMetadataFetchingSession fetchCurrentPrimaryKey]"
+ "SPMetadataFetchingSession.fetchCurrentPrimaryKey"
+ "fetchCurrentPrimaryKey:completion:"
+ "fetchiCloudIdentifier:completion:"

```
