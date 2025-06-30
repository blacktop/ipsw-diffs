## UARPiCloud

> `/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud`

```diff

-975.100.86.0.1
-  __TEXT.__text: 0x195a4
-  __TEXT.__auth_stubs: 0x690
+975.120.15.0.0
+  __TEXT.__text: 0x199d0
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x98c
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1a37
-  __TEXT.__oslogstring: 0x14cc
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__cstring: 0x1a92
+  __TEXT.__oslogstring: 0x1538
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__unwind_info: 0x580
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x2ed1
-  __TEXT.__objc_methtype: 0x409
-  __TEXT.__objc_stubs: 0x24a0
+  __TEXT.__objc_methname: 0x2f77
+  __TEXT.__objc_methtype: 0x47e
+  __TEXT.__objc_stubs: 0x24e0
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x6c0
+  __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1410
-  __DATA_CONST.__objc_selrefs: 0xa50
+  __DATA_CONST.__objc_const: 0x1430
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_classrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x3e0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x125
   __DATA.__bss: 0x1150
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C6A036D-89E8-3146-B984-C684963D320D
-  Functions: 636
-  Symbols:   1947
-  CStrings:  997
+  UUID: 6E415144-529A-394F-B786-EC03264D5B0C
+  Functions: 637
+  Symbols:   1957
+  CStrings:  1010
 
Symbols:
+ -[UARPiCloudAssetManager getSupportedAccessories:batchRequest:inContainer:]
+ -[UARPiCloudAssetManager handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:batchRequest:inContainer:]
+ -[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:]
+ -[UARPiCloudAssetManager remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:error:]
+ -[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:]
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestForCHIPAccessoriesMetadata:batchRequest:]
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:].cold.1
+ -[UARPiCloudManager(CHIP) processCHIPAccessoriesRecords:isComplete:productGroup:]
+ GCC_except_table8
+ _OBJC_IVAR_$_UARPiCloudAssetManager._batchedProcessingQueue
+ ___105-[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:]_block_invoke
+ ___107-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAttestationCertificates:subjectKeyIdentifier:]_block_invoke.24
+ ___108-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke
+ ___108-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke.14
+ ___108-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke.18
+ ___117-[UARPiCloudAssetManager handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:batchRequest:inContainer:]_block_invoke
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.261
+ ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.271
+ ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.263
+ ___75-[UARPiCloudAssetManager getSupportedAccessories:batchRequest:inContainer:]_block_invoke
+ ___84-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:]_block_invoke
+ ___block_descriptor_49_e8_32s40r_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8r40l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8
+ _dispatch_after
+ _objc_msgSend$databaseChangeToken
+ _objc_msgSend$handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:batchRequest:inContainer:
+ _objc_msgSend$handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:
+ _objc_msgSend$handleRemoteFetchRequestForCHIPAccessoriesMetadata:batchRequest:
+ _objc_msgSend$handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:
+ _objc_msgSend$performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:
+ _objc_msgSend$processCHIPAccessoriesRecords:isComplete:productGroup:
+ _objc_msgSend$remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:error:
+ _objc_msgSend$setConfigurationsByRecordZoneID:
+ _objc_msgSend$supportedAccessories:forProductGroup:isComplete:
- -[UARPiCloudAssetManager getSupportedAccessories:inContainer:]
- -[UARPiCloudAssetManager handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:inContainer:]
- -[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:]
- -[UARPiCloudAssetManager remoteFetchCompletionForSupportedAccessories:productGroup:error:]
- -[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:]
- -[UARPiCloudManager(CHIP) handleRemoteFetchRequestForCHIPAccessoriesMetadata:]
- -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:]
- -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:].cold.1
- -[UARPiCloudManager(CHIP) processCHIPAccessoriesRecords:productGroup:]
- GCC_except_table7
- ___107-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAttestationCertificates:subjectKeyIdentifier:]_block_invoke.18
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.259
- ___62-[UARPiCloudAssetManager getSupportedAccessories:inContainer:]_block_invoke
- ___71-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:]_block_invoke
- ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.270
- ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.262
- ___90-[UARPiCloudAssetManager remoteFetchCompletionForSupportedAccessories:productGroup:error:]_block_invoke
- ___94-[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:]_block_invoke
- ___95-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:]_block_invoke
- ___95-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:]_block_invoke.12
- _objc_msgSend$handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:inContainer:
- _objc_msgSend$handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:
- _objc_msgSend$handleRemoteFetchRequestForCHIPAccessoriesMetadata:
- _objc_msgSend$handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:
- _objc_msgSend$performRemoteFetchForSupportedAccessoriesMetadata:
- _objc_msgSend$processCHIPAccessoriesRecords:productGroup:
- _objc_msgSend$remoteFetchCompletionForSupportedAccessories:productGroup:error:
- _objc_msgSend$supportedAccessories:forProductGroup:
CStrings:
+ "\x06\x11"
+ "%s: Record Zone Fetch completed for recordZoneID: %@ changeToken:%@ error: %@ moreComing %s"
+ "%s: productGroup:%@ batchRequest:%s"
+ "-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:]"
+ "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]"
+ "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke"
+ "B28@0:8@16B24"
+ "B36@0:8^@16@24B32"
+ "NO"
+ "YES"
+ "_batchedProcessingQueue"
+ "com.apple.aam.uarpiCloudAssetManager.batched"
+ "getSupportedAccessories:batchRequest:inContainer:"
+ "handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:batchRequest:inContainer:"
+ "handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:"
+ "handleRemoteFetchRequestForCHIPAccessoriesMetadata:batchRequest:"
+ "handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:"
+ "performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:"
+ "processCHIPAccessoriesRecords:isComplete:productGroup:"
+ "q36@0:8@16B24@28"
+ "remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:error:"
+ "setConfigurationsByRecordZoneID:"
+ "supportedAccessories:forProductGroup:isComplete:"
+ "v28@0:8@16B24"
+ "v36@0:8@16@24B32"
+ "v36@0:8@16B24@28"
+ "v44@0:8@16@24B32@36"
- "\x05\x11"
- "%s: productGroup:%@"
- "-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:]"
- "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:]"
- "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:]_block_invoke"
- "getSupportedAccessories:inContainer:"
- "handleRemoteDownloadRequestForSupportedAccessoriesForProductGroup:inContainer:"
- "handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:"
- "handleRemoteFetchRequestForCHIPAccessoriesMetadata:"
- "handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:"
- "performRemoteFetchForSupportedAccessoriesMetadata:"
- "processCHIPAccessoriesRecords:productGroup:"
- "remoteFetchCompletionForSupportedAccessories:productGroup:error:"
- "supportedAccessories:forProductGroup:"

```
