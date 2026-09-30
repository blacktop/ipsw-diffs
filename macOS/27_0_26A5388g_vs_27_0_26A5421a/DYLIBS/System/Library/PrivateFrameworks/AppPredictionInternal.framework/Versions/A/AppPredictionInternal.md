## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/Versions/A/AppPredictionInternal`

```diff

-667.0.0.0.0
-  __TEXT.__text: 0x511e78
-  __TEXT.__objc_methlist: 0x38a74
+671.0.1.0.1
+  __TEXT.__text: 0x512664
+  __TEXT.__objc_methlist: 0x38ab4
   __TEXT.__const: 0x5ef0
-  __TEXT.__cstring: 0x59e74
-  __TEXT.__oslogstring: 0x3adc9
-  __TEXT.__gcc_except_tab: 0x10708
+  __TEXT.__cstring: 0x59ec4
+  __TEXT.__oslogstring: 0x3aeb9
+  __TEXT.__gcc_except_tab: 0x1073c
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x1c4f

   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xf838
+  __TEXT.__unwind_info: 0xf860
   __TEXT.__eh_frame: 0x5fb4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1bdd8
+  __DATA_CONST.__objc_selrefs: 0x1be08
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1488
-  __DATA_CONST.__objc_arraydata: 0x1328
+  __DATA_CONST.__objc_arraydata: 0x1330
   __DATA_CONST.__got: 0x3b40
-  __AUTH_CONST.__const: 0x13748
-  __AUTH_CONST.__cfstring: 0x3b260
+  __AUTH_CONST.__const: 0x137e8
+  __AUTH_CONST.__cfstring: 0x3b2c0
   __AUTH_CONST.__objc_const: 0x82858
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3450

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26718
-  Symbols:   47176
-  CStrings:  12434
+  Functions: 26730
+  Symbols:   47193
+  CStrings:  12441
 
Symbols:
+ +[ATXDocumentPredictor _inspectDocumentPredictionCandidateURL:disabledTypes:]
+ -[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:completionHandler:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:completionHandler:]
+ -[ATXSpotlightLayoutSelector _showAppShortcutsEnabled]
+ -[ATXSuggestionPreprocessor isResumeConversationSuggestion:]
+ ___106-[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:completionHandler:]_block_invoke
+ ___117-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:]_block_invoke
+ ___117-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:]_block_invoke_2
+ ___65-[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:]_block_invoke
+ ___83-[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:completionHandler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e8_v12?0B8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e17_v16?0"NSArray"8l
+ __registerForNotificationMetricsBGSTJob_block_invoke
+ _objc_msgSend$_inspectDocumentPredictionCandidateURL:disabledTypes:
+ _objc_msgSend$_showAppShortcutsEnabled
+ _objc_msgSend$isResumeConversationSuggestion:
+ _objc_msgSend$logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:
+ _objc_msgSend$logNotificationMetricsWithTask:completionHandler:
+ _objc_msgSend$stopAccessingSecurityScopedResource
+ _objc_msgSend$uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:completionHandler:
- -[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:]
- ___99-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:]_block_invoke_2
- ___block_descriptor_80_e8_32s40s48s56s64s_e17_v16?0"NSArray"8l
- _objc_msgSend$logNotificationMetricsWithTask:
- _objc_msgSend$uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:
CStrings:
+ "+[ATXDocumentPredictor _inspectDocumentPredictionCandidateURL:disabledTypes:]"
+ "Blending: Suppressing Resume Conversation suggestion from UI surface: %{public}@"
+ "Notification metrics logging task deferred; not marking DONE"
+ "PRAGMA cache_size = -512"
+ "ResumeConversationIntent"
+ "Returning %lu recent settings actions"
+ "SLS: [AppShortcut] Show App Shortcuts setting off; skipping generation"
+ "SuggestionsSpotlightAppShortcutsEnabled"
- "+[ATXDocumentPredictor _isAllowedDocumentPredictionCandidate:disabledTypes:]"
```
