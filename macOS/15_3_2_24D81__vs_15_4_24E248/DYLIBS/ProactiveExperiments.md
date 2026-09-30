## ProactiveExperiments

> `/System/Library/PrivateFrameworks/ProactiveExperiments.framework/Versions/A/ProactiveExperiments`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x20a04
+1276.10.4.0.0
+  __TEXT.__text: 0x20858
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x20f0
-  __TEXT.__const: 0xcc
+  __TEXT.__objc_methlist: 0x2334
+  __TEXT.__const: 0xd4
   __TEXT.__gcc_except_tab: 0x5a0
   __TEXT.__cstring: 0xafe
   __TEXT.__oslogstring: 0x1b24
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x688
+  __TEXT.__unwind_info: 0x668
   __TEXT.__objc_classname: 0x380
   __TEXT.__objc_methname: 0x4182
   __TEXT.__objc_methtype: 0xc2d
   __TEXT.__objc_stubs: 0x28a0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdd0
+  __DATA_CONST.__objc_selrefs: 0xe48
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0x3f88
+  __AUTH_CONST.__objc_const: 0x3b80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x870

   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A997D4E7-7186-3EE6-9BDF-D92563F9634D
-  Functions: 788
+  UUID: D54D2689-D044-3918-822D-EA96C9D0B95A
+  Functions: 783
   Symbols:   1772
   CStrings:  1207
 
Symbols:
+ __163-[PREResponsesExperiment preResponseItemsForMessage:maximumResponses:forConversationHistory:forContext:time:withLanguage:recipientHandles:options:completionBlock:]_block_invoke.151
+ __204-[PREResponsesExperiment fullNonEditableSuggestionsListForMessage:context:additionalSenderMessages:date:keyboardLanguageID:keyboardLanguageLastChangedDate:recipients:includeDynamicSuggestions:completion:]_block_invoke.123
+ __220-[PREResponsesExperiment _responsesForMessage:maximumResponses:outgoingMessageHistory:forConversationHistory:forContext:time:withLanguage:languageLastChangedDate:recipientHandles:options:preferredLocale:completionBlock:]_block_invoke.134
+ __26-[PREResponsesClient init]_block_invoke.39
+ __29-[PREExperimentResolver init]_block_invoke.72
+ __50-[PREXPCClientHelpers _locked_establishConnection]_block_invoke.7
+ __63-[PREResponsesExperiment suggestionsForRequest:withCompletion:]_block_invoke.100
+ __63-[PREResponsesExperiment suggestionsForRequest:withCompletion:]_block_invoke.105
+ __65-[PREResponsesExperiment predictionsForRequest:heads:completion:]_block_invoke.143
+ __81-[PREResponsesExperiment registerResponse:forMessage:time:metadata:withLanguage:]_block_invoke.157
+ __85-[PREExperimentResolver getResponseSuggestionsExperimentConfig:shouldDownloadAssets:]_block_invoke.81
+ __94-[PREResponseSuggestionsExpConfig initWithNamespaceName:withTrialClient:shouldDownloadAssets:]_block_invoke.76
+ __Block_byref_object_copy_.1941
+ __Block_byref_object_dispose_.1942
+ __block_literal_global.102
+ __block_literal_global.1054
+ __block_literal_global.1165
+ __block_literal_global.125
+ __block_literal_global.137
+ __block_literal_global.1391
+ __block_literal_global.2015
+ __block_literal_global.2052
+ __block_literal_global.385
+ __block_literal_global.41
+ sharedInstance._pasExprOnceResult.1393
+ sharedInstance._pasExprOnceResult.2061
- __163-[PREResponsesExperiment preResponseItemsForMessage:maximumResponses:forConversationHistory:forContext:time:withLanguage:recipientHandles:options:completionBlock:]_block_invoke.145
- __204-[PREResponsesExperiment fullNonEditableSuggestionsListForMessage:context:additionalSenderMessages:date:keyboardLanguageID:keyboardLanguageLastChangedDate:recipients:includeDynamicSuggestions:completion:]_block_invoke.117
- __220-[PREResponsesExperiment _responsesForMessage:maximumResponses:outgoingMessageHistory:forConversationHistory:forContext:time:withLanguage:languageLastChangedDate:recipientHandles:options:preferredLocale:completionBlock:]_block_invoke.128
- __26-[PREResponsesClient init]_block_invoke.33
- __29-[PREExperimentResolver init]_block_invoke.66
- __50-[PREXPCClientHelpers _locked_establishConnection]_block_invoke.3
- __63-[PREResponsesExperiment suggestionsForRequest:withCompletion:]_block_invoke.94
- __63-[PREResponsesExperiment suggestionsForRequest:withCompletion:]_block_invoke.99
- __65-[PREResponsesExperiment predictionsForRequest:heads:completion:]_block_invoke.137
- __81-[PREResponsesExperiment registerResponse:forMessage:time:metadata:withLanguage:]_block_invoke.151
- __85-[PREExperimentResolver getResponseSuggestionsExperimentConfig:shouldDownloadAssets:]_block_invoke.75
- __94-[PREResponseSuggestionsExpConfig initWithNamespaceName:withTrialClient:shouldDownloadAssets:]_block_invoke.70
- __Block_byref_object_copy_.1955
- __Block_byref_object_dispose_.1956
- __block_literal_global.1059
- __block_literal_global.1171
- __block_literal_global.119
- __block_literal_global.131
- __block_literal_global.1399
- __block_literal_global.2023
- __block_literal_global.2060
- __block_literal_global.35
- __block_literal_global.388
- __block_literal_global.96
- sharedInstance._pasExprOnceResult.1401
- sharedInstance._pasExprOnceResult.2069

```
