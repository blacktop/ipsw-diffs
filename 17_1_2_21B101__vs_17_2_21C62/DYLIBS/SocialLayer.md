## SocialLayer

> `/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer`

```diff

-107.200.61.2.1
-  __TEXT.__text: 0xaaf68
-  __TEXT.__auth_stubs: 0x2160
-  __TEXT.__objc_methlist: 0x4edc
+107.300.71.0.0
+  __TEXT.__text: 0xab570
+  __TEXT.__auth_stubs: 0x2130
+  __TEXT.__objc_methlist: 0x4ee4
   __TEXT.__const: 0x1d64
-  __TEXT.__gcc_except_tab: 0x1060
-  __TEXT.__cstring: 0x678d
-  __TEXT.__oslogstring: 0xc24e
+  __TEXT.__gcc_except_tab: 0xfac
+  __TEXT.__cstring: 0x67bd
+  __TEXT.__oslogstring: 0xc3c5
   __TEXT.__dlopen_cstrs: 0x352
   __TEXT.__swift5_typeref: 0xbac
   __TEXT.__constg_swiftt: 0xeb4

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x434
   __TEXT.__objc_const_ax: 0xabc
-  __TEXT.__unwind_info: 0x30c4
+  __TEXT.__unwind_info: 0x30d4
   __TEXT.__eh_frame: 0x1310
   __TEXT.__objc_classname: 0xeaa
-  __TEXT.__objc_methname: 0x1012d
-  __TEXT.__objc_methtype: 0x2724
-  __TEXT.__objc_stubs: 0xb700
+  __TEXT.__objc_methname: 0x10185
+  __TEXT.__objc_methtype: 0x2734
+  __TEXT.__objc_stubs: 0xb720
   __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0x1eb8
+  __DATA_CONST.__const: 0x1ee0
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x91e0
-  __DATA_CONST.__objc_selrefs: 0x36e8
+  __DATA_CONST.__objc_selrefs: 0x36f0
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__cfstring: 0x2ea0
   __AUTH_CONST.__objc_const: 0x2e78

   __AUTH_CONST.__auth_ptr: 0x58
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x10c0
+  __AUTH_CONST.__auth_got: 0x10a8
   __AUTH.__objc_data: 0x2138
   __AUTH.__data: 0x4e8
   __DATA.__objc_protorefs: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4795
-  Symbols:   14477
-  CStrings:  4306
+  Functions: 4804
+  Symbols:   14493
+  CStrings:  4316
 
Symbols:
+ -[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]
+ -[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]
+ -[SLDShareableContentService fetchShareableContentFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:]
+ -[SLDShareableContentService fetchShareableContentFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:].cold.1
+ -[SLDShareableContentService loadRepresentationFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:]
+ -[SLDShareableContentService presentMessageComposeSheetForSceneIdentifier:completion:]
+ -[SLDShareableContentService presentMessageComposeSheetForSceneIdentifier:completion:].cold.1
+ -[SLDShareableContentService visibleApplicationForSceneIdentifier:]
+ GCC_except_table108
+ GCC_except_table118
+ GCC_except_table133
+ GCC_except_table142
+ GCC_except_table151
+ GCC_except_table155
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table39
+ GCC_except_table82
+ GCC_except_table94
+ _OUTLINED_FUNCTION_19
+ ___154-[SLDShareableContentService loadRepresentationFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:]_block_invoke
+ ___154-[SLDShareableContentService loadRepresentationFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:]_block_invoke.cold.1
+ ___45-[SLDCloudKitSyncBase checkForAccountChanges]_block_invoke_2
+ ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.423
+ ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.486
+ ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.518
+ ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_2.425
+ ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.473
+ ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.473.cold.1
+ ___61-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecord:error:]_block_invoke.553
+ ___63-[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]_block_invoke
+ ___63-[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]_block_invoke.211
+ ___63-[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]_block_invoke.cold.1
+ ___63-[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]_block_invoke_2
+ ___63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke
+ ___63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.208
+ ___63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.208.cold.1
+ ___63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.cold.1
+ ___65-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecordZone:error:]_block_invoke.552
+ ___65-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecordZone:error:]_block_invoke_2
+ ___69-[SLDCloudKitSyncWriter syncEngine:failedToDeleteRecordWithID:error:]_block_invoke.554
+ ___86-[SLDShareableContentService presentMessageComposeSheetForSceneIdentifier:completion:]_block_invoke
+ ___86-[SLDShareableContentService presentMessageComposeSheetForSceneIdentifier:completion:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32bs_e32_v24?0"CKRecordID"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e35_v32?0q8"CKRecordID"16"NSError"24ls32l8s40l8
+ ___block_literal_global.595
+ ___block_literal_global.677
+ _objc_msgSend$checkForAccountChangesNowWithCompletion:
+ _objc_msgSend$fetchContainerInformationWithCompletion:
+ _objc_msgSend$fetchShareableContentFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:
+ _objc_msgSend$visibleApplicationForSceneIdentifier:
+ _sharedInstance.onceToken.592
+ _sharedInstance.sharedInstance.593
- -[SLDCloudKitSyncBase checkForAccountChangesNow]
- -[SLDCloudKitSyncBase checkForAccountChangesNow].cold.1
- -[SLDCloudKitSyncBase checkForAccountChangesNow].cold.2
- -[SLDShareableContentService fetchShareableContentFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:]
- -[SLDShareableContentService fetchShareableContentFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:].cold.1
- -[SLDShareableContentService loadRepresentationFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:]
- -[SLDShareableContentService presentMessageComposeSheetForSourceIdentifier:completion:]
- -[SLDShareableContentService presentMessageComposeSheetForSourceIdentifier:completion:].cold.1
- -[SLDShareableContentService visibleApplicationForSourceIdentifier:]
- GCC_except_table102
- GCC_except_table112
- GCC_except_table127
- GCC_except_table136
- GCC_except_table145
- GCC_except_table149
- GCC_except_table157
- GCC_except_table159
- GCC_except_table161
- GCC_except_table79
- GCC_except_table90
- ___138-[SLDShareableContentService loadRepresentationFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:]_block_invoke
- ___138-[SLDShareableContentService loadRepresentationFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:]_block_invoke.cold.1
- ___48-[SLDCloudKitSyncBase checkForAccountChangesNow]_block_invoke
- ___48-[SLDCloudKitSyncBase checkForAccountChangesNow]_block_invoke.208
- ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.413
- ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.476
- ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.508
- ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_2.415
- ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.463
- ___55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.463.cold.1
- ___61-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecord:error:]_block_invoke.543
- ___65-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecordZone:error:]_block_invoke.542
- ___69-[SLDCloudKitSyncWriter syncEngine:failedToDeleteRecordWithID:error:]_block_invoke.544
- ___87-[SLDShareableContentService presentMessageComposeSheetForSourceIdentifier:completion:]_block_invoke
- ___87-[SLDShareableContentService presentMessageComposeSheetForSourceIdentifier:completion:]_block_invoke.cold.1
- ___block_descriptor_56_e8_32s40r48r_e20_v24?0q8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e32_v24?0"CKRecordID"8"NSError"16lr40l8r48l8s32l8
- ___block_literal_global.585
- ___block_literal_global.668
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_msgSend$checkForAccountChangesNow
- _objc_msgSend$fetchShareableContentFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:
- _objc_msgSend$visibleApplicationForSourceIdentifier:
- _sharedInstance.onceToken.582
- _sharedInstance.sharedInstance.583
CStrings:
+ "#SLDCK Checking for account changed."
+ "#SLDCK Failed to fetch container information: %@"
+ "#SLDCK Fetching container information"
+ "#SLDCK Fetching userRecordID"
+ "#SLDCK Finished checking for account changes."
+ "#SLDCK Received accountStatus: %@, error: %@"
+ "#SLDCK Received userRecordID: %@, error: %@"
+ "Failed to find source application for scene identifier: %@ in visible applications: %@"
+ "checkForAccountChangesNowWithCompletion:"
+ "fetchContainerInformationWithCompletion:"
+ "fetchShareableContentFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:"
+ "loadRepresentationFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:"
+ "presentMessageComposeSheetForSceneIdentifier:completion:"
+ "v32@?0q8@\"CKRecordID\"16@\"NSError\"24"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@?<v@?@\"SLShareableContentLoadResult\"@\"NSError\">48"
+ "v56@0:8@16@24@32q40@?48"
+ "visibleApplicationForSceneIdentifier:"
- "checkForAccountChangesNow"
- "fetchShareableContentFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:"
- "loadRepresentationFromSourceIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:completionHandler:"
- "presentMessageComposeSheetForSourceIdentifier:completion:"
- "v48@0:8@\"NSString\"16@\"NSString\"24q32@?<v@?@\"SLShareableContentLoadResult\"@\"NSError\">40"
- "v48@0:8@16@24q32@?40"
- "visibleApplicationForSourceIdentifier:"

```
