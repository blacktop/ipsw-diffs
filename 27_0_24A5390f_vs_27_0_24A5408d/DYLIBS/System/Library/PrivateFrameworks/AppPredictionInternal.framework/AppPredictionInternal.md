## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-667.0.0.0.0
-  __TEXT.__text: 0x48e24c
-  __TEXT.__objc_methlist: 0x38e74
+671.0.2.0.0
+  __TEXT.__text: 0x48ec80
+  __TEXT.__objc_methlist: 0x38eac
   __TEXT.__const: 0x450a
-  __TEXT.__cstring: 0x59672
-  __TEXT.__oslogstring: 0x3ba49
-  __TEXT.__gcc_except_tab: 0xf48c
+  __TEXT.__cstring: 0x596b2
+  __TEXT.__oslogstring: 0x3bb49
+  __TEXT.__gcc_except_tab: 0xf4a0
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x14f2

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe580
+  __TEXT.__unwind_info: 0xe640
   __TEXT.__eh_frame: 0x262c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc080
+  __DATA_CONST.__const: 0xc0d0
   __DATA_CONST.__objc_classlist: 0x1f58
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1bf58
+  __DATA_CONST.__objc_selrefs: 0x1bf80
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x14f8
-  __DATA_CONST.__objc_arraydata: 0x12e8
+  __DATA_CONST.__objc_arraydata: 0x12f0
   __DATA_CONST.__got: 0x39c8
-  __AUTH_CONST.__const: 0x8d18
-  __AUTH_CONST.__cfstring: 0x3b1e0
+  __AUTH_CONST.__const: 0x8d58
+  __AUTH_CONST.__cfstring: 0x3b240
   __AUTH_CONST.__objc_const: 0x83ba0
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3450

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25692
-  Symbols:   46687
-  CStrings:  12394
+  Functions: 25704
+  Symbols:   46704
+  CStrings:  12400
 
Symbols:
+ -[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:completionHandler:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:completionHandler:]
+ -[ATXSpotlightLayoutSelector _showAppShortcutsEnabled]
+ -[ATXSuggestionPreprocessor isResumeConversationSuggestion:]
+ GCC_except_table479
+ GCC_except_table491
+ GCC_except_table495
+ GCC_except_table507
+ GCC_except_table511
+ GCC_except_table542
+ GCC_except_table588
+ GCC_except_table593
+ GCC_except_table622
+ GCC_except_table640
+ GCC_except_table79
+ _ATXLaunchReasonComponentWithPrefix
+ _ATXLaunchReasonContainsReason
+ ___106-[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:completionHandler:]_block_invoke
+ ___117-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:]_block_invoke
+ ___117-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:]_block_invoke_2
+ ___65-[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:]_block_invoke
+ ___83-[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:completionHandler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s72l8s56l8s64l8
+ _objc_msgSend$_showAppShortcutsEnabled
+ _objc_msgSend$isResumeConversationSuggestion:
+ _objc_msgSend$logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:completionHandler:
+ _objc_msgSend$logNotificationMetricsWithTask:completionHandler:
+ _objc_msgSend$uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:completionHandler:
+ _objc_msgSend$whitespaceCharacterSet
- -[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:]
- GCC_except_table477
- GCC_except_table490
- GCC_except_table494
- GCC_except_table506
- GCC_except_table510
- GCC_except_table541
- GCC_except_table587
- GCC_except_table592
- GCC_except_table621
- GCC_except_table639
- ___99-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:]_block_invoke_2
- ___block_descriptor_80_e8_32s40s48s56s64s_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$logNotificationMetricsWithTask:
- _objc_msgSend$uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:
CStrings:
+ "Blending: Suppressing Resume Conversation suggestion from UI surface: %{public}@"
+ "Notification metrics logging task deferred; not marking DONE"
+ "PRAGMA cache_size = -512"
+ "Returning %lu recent settings actions"
+ "SLS: [AppShortcut] Show App Shortcuts setting off; skipping generation"
+ "SuggestionsSpotlightAppShortcutsEnabled"
```
