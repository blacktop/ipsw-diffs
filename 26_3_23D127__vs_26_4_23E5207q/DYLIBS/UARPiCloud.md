## UARPiCloud

> `/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud`

```diff

-1338.80.37.0.0
-  __TEXT.__text: 0x1c0f4
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0xa0c
+1345.100.155.0.0
+  __TEXT.__text: 0x1cf50
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0xa34
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x23d9
-  __TEXT.__oslogstring: 0x15d9
-  __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__cstring: 0x246b
+  __TEXT.__oslogstring: 0x16cf
+  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__unwind_info: 0x618
   __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methname: 0x2ff7
-  __TEXT.__objc_methtype: 0x4ac
-  __TEXT.__objc_stubs: 0x25c0
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x8e0
+  __TEXT.__objc_methname: 0x3161
+  __TEXT.__objc_methtype: 0x4e6
+  __TEXT.__objc_stubs: 0x2740
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa90
+  __DATA_CONST.__objc_selrefs: 0xaf8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0x17a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85F920B4-50AB-349E-919B-A6101A39F313
-  Functions: 683
-  Symbols:   2094
-  CStrings:  1086
+  UUID: 360532D3-2FA2-3832-A7CB-7D825A06A019
+  Functions: 702
+  Symbols:   2166
+  CStrings:  1108
 
Symbols:
+ -[UARPiCloudAssetManager getSupportedAccessoriesFileURL]
+ -[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:useFile:isComplete:]
+ -[UARPiCloudAssetManager remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:useFile:error:]
+ -[UARPiCloudAssetManager updateCHIPMetadataCache]
+ -[UARPiCloudContainer isDevelopmentContainer]
+ -[UARPiCloudManager getSupportedAccessoriesFileURL]
+ -[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:useFile:]
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestForCHIPAccessoriesMetadata:cache:batchRequest:useFile:]
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestForCHIPAccessoriesMetadata:cache:batchRequest:useFile:].cold.1
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]
+ -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:].cold.1
+ -[UARPiCloudManager(CHIP) processCHIPAccessoriesRecords:deleted:cache:isComplete:productGroup:useFile:]
+ -[UARPiCloudManager(CHIP) processCHIPAccessoriesRecords:deleted:cache:isComplete:productGroup:useFile:].cold.1
+ GCC_except_table33
+ GCC_except_table9
+ _OBJC_CLASS_$_UARPAccessoryMetadataStore
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _UARPStringChipRecordCacheFilepath
+ ___107-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAttestationCertificates:subjectKeyIdentifier:]_block_invoke.28
+ ___113-[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:useFile:isComplete:]_block_invoke
+ ___134-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]_block_invoke
+ ___134-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]_block_invoke.12
+ ___134-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]_block_invoke.18
+ ___134-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]_block_invoke.18.cold.1
+ ___134-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]_block_invoke.22
+ ___49-[UARPiCloudAssetManager updateCHIPMetadataCache]_block_invoke
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.323
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.324
+ ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.334
+ ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.326
+ ___92-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:useFile:]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e33_v24?0"CKRecordID"8"NSString"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e18_v16?0"CKRecord"8ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48r56r_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8r48l8s40l8r56l8
+ ___block_descriptor_82_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8s48l8r72l8s56l8
+ _objc_msgSend$clearAllMetadata
+ _objc_msgSend$code
+ _objc_msgSend$copyiCloudToken
+ _objc_msgSend$environment
+ _objc_msgSend$getSupportedAccessoriesFileURL
+ _objc_msgSend$handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:useFile:isComplete:
+ _objc_msgSend$handleRemoteFetchRequestForCHIPAccessoriesMetadata:cache:batchRequest:useFile:
+ _objc_msgSend$handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:
+ _objc_msgSend$initWithDirectory:
+ _objc_msgSend$isDevelopmentContainer
+ _objc_msgSend$performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:useFile:
+ _objc_msgSend$processCHIPAccessoriesRecords:deleted:cache:isComplete:productGroup:useFile:
+ _objc_msgSend$remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:useFile:error:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setRecordWithIDWasDeletedBlock:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$supportedAccessories:forProductGroup:useFile:isComplete:
+ _objc_msgSend$updateMetadata:deleteMetadata:
+ _objc_msgSend$updateiCloudToken:
+ _objc_retainAutoreleasedReturnValue
- -[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:]
- -[UARPiCloudAssetManager remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:error:]
- -[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:]
- -[UARPiCloudManager(CHIP) handleRemoteFetchRequestForCHIPAccessoriesMetadata:batchRequest:]
- -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]
- -[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:].cold.1
- -[UARPiCloudManager(CHIP) processCHIPAccessoriesRecords:isComplete:productGroup:]
- GCC_except_table8
- ___105-[UARPiCloudAssetManager handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:]_block_invoke
- ___107-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAttestationCertificates:subjectKeyIdentifier:]_block_invoke.24
- ___108-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke
- ___108-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke.14
- ___108-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke.18
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.320
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.321
- ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.331
- ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.323
- ___84-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:]_block_invoke
- ___block_descriptor_49_e8_32s40r_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8r40l8
- ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:
- _objc_msgSend$handleRemoteFetchRequestForCHIPAccessoriesMetadata:batchRequest:
- _objc_msgSend$handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:
- _objc_msgSend$performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:
- _objc_msgSend$processCHIPAccessoriesRecords:isComplete:productGroup:
- _objc_msgSend$remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:error:
- _objc_msgSend$supportedAccessories:forProductGroup:isComplete:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x9
CStrings:
+ "%s: Change Token expired. Restarting download with no token"
+ "%s: Invalid iCloud container %{public}@"
+ "%s: Record Deleted: %@"
+ "%s: productGroup:%@ batchRequest:%d useFile:%d"
+ "-[UARPiCloudManager getSupportedAccessoriesFileURL]"
+ "-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:useFile:]"
+ "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]"
+ "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:]_block_invoke"
+ "B40@0:8@16@24B32B36"
+ "B60@0:8@16@24@32@40B48^@52"
+ "Error serializing iCloud change token %{public}@"
+ "Failed to retrieve change token from metadata store %{public}@"
+ "clearAllMetadata"
+ "code"
+ "copyiCloudToken"
+ "environment"
+ "getSupportedAccessoriesFileURL"
+ "handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:useFile:isComplete:"
+ "handleRemoteFetchRequestForCHIPAccessoriesMetadata:cache:batchRequest:useFile:"
+ "handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:deleted:changeToken:productGroup:batchRequest:error:"
+ "initWithDirectory:"
+ "isDevelopmentContainer"
+ "performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:useFile:"
+ "processCHIPAccessoriesRecords:deleted:cache:isComplete:productGroup:useFile:"
+ "q16@0:8"
+ "remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:useFile:error:"
+ "removeAllObjects"
+ "setRecordWithIDWasDeletedBlock:"
+ "stringWithUTF8String:"
+ "supportedAccessories:forProductGroup:useFile:isComplete:"
+ "updateCHIPMetadataCache"
+ "updateMetadata:deleteMetadata:"
+ "updateiCloudToken:"
+ "v24@?0@\"CKRecordID\"8@\"NSString\"16"
+ "v32@0:8@16B24B28"
+ "v40@0:8@16@24B32B36"
+ "v48@0:8@16@24B32B36@40"
+ "v56@0:8@16@24@32B40@44B52"
- "%s: productGroup:%@ batchRequest:%s"
- "-[UARPiCloudManager performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:]"
- "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]"
- "-[UARPiCloudManager(CHIP) handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:]_block_invoke"
- "B28@0:8@16B24"
- "B36@0:8^@16@24B32"
- "handleRemoteDownloadResponseForSupportedAccessories:forProductGroup:isComplete:"
- "handleRemoteFetchRequestForCHIPAccessoriesMetadata:batchRequest:"
- "handleRemoteFetchRequestSyncForCHIPAccessoriesMetadata:productGroup:batchRequest:"
- "performRemoteFetchForSupportedAccessoriesMetadata:batchRequest:"
- "processCHIPAccessoriesRecords:isComplete:productGroup:"
- "remoteFetchCompletionForSupportedAccessories:productGroup:isComplete:error:"
- "supportedAccessories:forProductGroup:isComplete:"
- "v28@0:8@16B24"
- "v36@0:8@16@24B32"
- "v44@0:8@16@24B32@36"

```
