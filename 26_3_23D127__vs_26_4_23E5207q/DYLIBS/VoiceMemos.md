## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1356.0.0.0.0
-  __TEXT.__text: 0x48754
-  __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0x3de4
-  __TEXT.__gcc_except_tab: 0x1850
+1378.5.0.0.0
+  __TEXT.__text: 0x49a7c
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_methlist: 0x3e04
+  __TEXT.__gcc_except_tab: 0x1828
   __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x63d4
-  __TEXT.__oslogstring: 0x29e3
+  __TEXT.__cstring: 0x6572
+  __TEXT.__oslogstring: 0x2a33
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1988
+  __TEXT.__unwind_info: 0x1a68
   __TEXT.__objc_classname: 0x82d
-  __TEXT.__objc_methname: 0xbe71
-  __TEXT.__objc_methtype: 0x1560
-  __TEXT.__objc_stubs: 0x9040
+  __TEXT.__objc_methname: 0xbf27
+  __TEXT.__objc_methtype: 0x1576
+  __TEXT.__objc_stubs: 0x9060
   __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x1d48
+  __DATA_CONST.__const: 0x1d50
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e88
+  __DATA_CONST.__objc_selrefs: 0x2ea0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x32c0
+  __AUTH_CONST.__cfstring: 0x3340
   __AUTH_CONST.__objc_const: 0x5bb8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9240F7A7-EA27-34A0-9999-638FF6DFA48A
-  Functions: 1900
-  Symbols:   6627
-  CStrings:  3472
+  UUID: 059FA1CF-9109-36A0-92E3-A67427078628
+  Functions: 1919
+  Symbols:   6718
+  CStrings:  3486
 
Symbols:
+ +[RCQueryManager recordedOnWatchPredicate]
+ +[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]
+ -[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]
+ -[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:].cold.1
+ -[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:predicate:sortDescriptors:block:]
+ GCC_except_table114
+ GCC_except_table118
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table163
+ GCC_except_table43
+ GCC_except_table63
+ GCC_except_table74
+ GCC_except_table83
+ GCC_except_table87
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _RCCloudRecording_AudioFutureUUIDs
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB9foe210106ERKf
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke.123
+ ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke_2.124
+ ___100-[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:predicate:sortDescriptors:block:]_block_invoke
+ ___100-[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:predicate:sortDescriptors:block:]_block_invoke.cold.1
+ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke
+ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke.cold.1
+ ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke.119
+ ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke_2.120
+ ___40-[RCSSavedRecordingService serviceProxy]_block_invoke.114
+ ___51-[RCSSavedRecordingService __fetchAllAccessTokens:]_block_invoke.91
+ ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke.105
+ ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke_2.107
+ ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingExported:]_block_invoke.87
+ ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingModified:]_block_invoke.89
+ ___64-[RCSSavedRecordingService prepareToTrimCompositionAVURL:error:]_block_invoke.82
+ ___66-[RCSSavedRecordingService prepareToExportCompositionAVURL:error:]_block_invoke.77
+ ___67-[RCSSavedRecordingService prepareToPreviewCompositionAVURL:error:]_block_invoke.72
+ ___69-[RCSSavedRecordingService prepareToCaptureToCompositionAVURL:error:]_block_invoke.66
+ ___91-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]_block_invoke
+ ___91-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]_block_invoke_2
+ ___91-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]_block_invoke_2.cold.1
+ ___91-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]_block_invoke_2.cold.2
+ ___block_descriptor_41_e8_32s_e85_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"RCVoiceMemoMetadata""NSError">16ls32l8
+ ___block_descriptor_49_e8_32s40bs_e41_v24?0"RCVoiceMemoMetadata"8"NSError"16ls40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.109
+ ___block_literal_global.111
+ ___block_literal_global.57
+ ___block_literal_global.60
+ ___block_literal_global.86
+ _objc_msgSend$enumerateExistingRecordingsWithProperties:predicate:sortDescriptors:block:
+ _objc_msgSend$fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:
+ _objc_msgSend$fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:
+ _objc_msgSend$tagCSSearchableItem:entityInstanceIdentifier:typeIdentifier:displayTitle:displaySubtitle:displaySynonyms:typeDisplayName:typeDisplaySynonyms:propertyDictionary:priority:schemaIdentifier:
- -[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:].cold.1
- -[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:sortDescriptors:block:]
- GCC_except_table113
- GCC_except_table117
- GCC_except_table120
- GCC_except_table122
- GCC_except_table129
- GCC_except_table136
- GCC_except_table138
- GCC_except_table73
- GCC_except_table82
- GCC_except_table86
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100ERKf
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke.117
- ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke_2.118
- ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke.113
- ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke_2.114
- ___40-[RCSSavedRecordingService serviceProxy]_block_invoke.108
- ___51-[RCSSavedRecordingService __fetchAllAccessTokens:]_block_invoke.85
- ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke.99
- ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke_2.101
- ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingExported:]_block_invoke.81
- ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingModified:]_block_invoke.83
- ___64-[RCSSavedRecordingService prepareToTrimCompositionAVURL:error:]_block_invoke.76
- ___66-[RCSSavedRecordingService prepareToExportCompositionAVURL:error:]_block_invoke.71
- ___67-[RCSSavedRecordingService prepareToPreviewCompositionAVURL:error:]_block_invoke.66
- ___69-[RCSSavedRecordingService prepareToCaptureToCompositionAVURL:error:]_block_invoke.60
- ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke
- ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2
- ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2.cold.1
- ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2.cold.2
- ___90-[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:sortDescriptors:block:]_block_invoke
- ___90-[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:sortDescriptors:block:]_block_invoke.cold.1
- ___95+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]_block_invoke
- ___95+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32s_e85_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"RCVoiceMemoMetadata""NSError">16ls32l8
- ___block_descriptor_48_e8_32s40bs_e41_v24?0"RCVoiceMemoMetadata"8"NSError"16ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.103
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.139
- ___block_literal_global.51
- ___block_literal_global.54
- ___block_literal_global.80
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$enumerateExistingRecordingsWithProperties:sortDescriptors:block:
- _objc_msgSend$fetchMetadataForRecordingWithUUID:completionBlock:
- _objc_msgSend$tagCSSearchableItem:entityInstanceIdentifier:typeIdentifier:displayTitle:displaySubtitle:displaySynonyms:typeDisplayName:typeDisplaySynonyms:propertyDictionary:priority:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%s -- Sending service request to fetchRecordingUUIDsForExport, includeAsset: %@"
+ "+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke"
+ "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]"
+ "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]_block_invoke"
+ "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:]_block_invoke_2"
+ "-[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:predicate:sortDescriptors:block:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CIVAugCUgET5XqSdNVYZML18oAnuARs4AZJdEu0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "NO"
+ "Vv36@0:8@\"NSString\"16B24@?<v@?@\"RCVoiceMemoMetadata\"@\"NSError\">28"
+ "Vv36@0:8@16B24@?28"
+ "YES"
+ "enumerateExistingRecordingsWithProperties:predicate:sortDescriptors:block:"
+ "fetchMetadataForRecordingWithUUID:includeAsset:completionBlock:"
+ "fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:"
+ "recordedOnWatchPredicate"
+ "tagCSSearchableItem:entityInstanceIdentifier:typeIdentifier:displayTitle:displaySubtitle:displaySynonyms:typeDisplayName:typeDisplaySynonyms:propertyDictionary:priority:schemaIdentifier:"
+ "voiceMemos.recording"
- "+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]_block_invoke"
- "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]"
- "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke"
- "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2"
- "-[RCSavedRecordingsModel enumerateExistingRecordingsWithProperties:sortDescriptors:block:]_block_invoke"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"RCVoiceMemoMetadata\"@\"NSError\">24"
- "enumerateExistingRecordingsWithProperties:sortDescriptors:block:"
- "tagCSSearchableItem:entityInstanceIdentifier:typeIdentifier:displayTitle:displaySubtitle:displaySynonyms:typeDisplayName:typeDisplaySynonyms:propertyDictionary:priority:"

```
