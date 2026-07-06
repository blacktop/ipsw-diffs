## WellnessFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin`

```diff

-  __TEXT.__text: 0x16370c
-  __TEXT.__auth_stubs: 0x33a0
+  __TEXT.__text: 0x166c78
+  __TEXT.__auth_stubs: 0x3390
   __TEXT.__objc_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x408
-  __TEXT.__const: 0xaec0
+  __TEXT.__const: 0xb020
   __TEXT.__cstring: 0x6e55
-  __TEXT.__swift5_typeref: 0x3083
+  __TEXT.__swift5_typeref: 0x33cd
   __TEXT.__objc_classname: 0xa5d
   __TEXT.__objc_methname: 0x1685
   __TEXT.__objc_methtype: 0x784
-  __TEXT.__oslogstring: 0x6da3
-  __TEXT.__constg_swiftt: 0x40f8
-  __TEXT.__swift5_reflstr: 0x70c5
-  __TEXT.__swift5_fieldmd: 0x5ec4
-  __TEXT.__swift5_proto: 0x5d0
-  __TEXT.__swift5_types: 0x328
+  __TEXT.__oslogstring: 0x6ea3
+  __TEXT.__constg_swiftt: 0x4150
+  __TEXT.__swift5_reflstr: 0x71e5
+  __TEXT.__swift5_fieldmd: 0x600c
+  __TEXT.__swift5_proto: 0x5d4
+  __TEXT.__swift5_types: 0x32c
   __TEXT.__swift_as_entry: 0x744
-  __TEXT.__swift_as_ret: 0xae4
-  __TEXT.__swift_as_cont: 0xd68
-  __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__swift5_capture: 0x1150
+  __TEXT.__swift_as_ret: 0xae8
+  __TEXT.__swift_as_cont: 0xd6c
+  __TEXT.__swift5_assocty: 0x5d0
+  __TEXT.__swift5_capture: 0x1160
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x5618
-  __TEXT.__eh_frame: 0xf0f8
-  __DATA_CONST.__const: 0x7ab0
+  __TEXT.__unwind_info: 0x56a0
+  __TEXT.__eh_frame: 0xf188
+  __DATA_CONST.__const: 0x7b18
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__auth_got: 0x19d8
-  __DATA_CONST.__got: 0xfa0
-  __DATA_CONST.__auth_ptr: 0xd88
+  __DATA_CONST.__auth_got: 0x19d0
+  __DATA_CONST.__got: 0xf90
+  __DATA_CONST.__auth_ptr: 0xd98
   __DATA.__objc_const: 0x4cc8
   __DATA.__objc_selrefs: 0x6a8
   __DATA.__objc_data: 0x5e8
-  __DATA.__data: 0x6a50
-  __DATA.__bss: 0xb630
+  __DATA.__data: 0x6b28
+  __DATA.__bss: 0xb6b0
   __DATA.__common: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7848
+  Functions: 7898
   Symbols:   400
-  CStrings:  1630
+  CStrings:  1634
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__common : content changed
CStrings:
+ "#GenerateLoggingResponseOutput: Snippet dialog is %{sensitive}s"
+ "#GetActivitySummaryFlow: dialog is %{sensitive}s"
+ "#GetActivitySummaryFlow: snippet header model is %{sensitive}s"
+ "#GetActivitySummaryFlow: snippet model is %{sensitive}s"
+ "#GetBloodPressureFlow: snippet model is %{sensitive}s"
+ "#GetHealthQuantityFlow: In successResponseFlow intent is %{sensitive}@"
+ "#GetHealthQuantityFlow: In successResponseFlow intent response is %{sensitive}@"
+ "#GetSleepAnalysisFlow: output is %{sensitive}s"
+ "#GetSleepAnalysisFlow: snippet model is %{sensitive}s"
+ "Executing intent: %{sensitive}@"
+ "Failed to produce patternResult from response"
+ "LogPeriodIntentResponse missing date param"
+ "Received response: %{sensitive}@"
+ "Recommendation: %{sensitive}s"
+ "Recommended INDateComponentsRange: %{sensitive}@"
+ "Recommended dateInterval: %{sensitive}s"
- "#GenerateLoggingResponseOutput: Snippet dialog is %s"
- "#GetActivitySummaryFlow: dialog is %s"
- "#GetActivitySummaryFlow: snippet header model is %s"
- "#GetActivitySummaryFlow: snippet model is %s"
- "#GetBloodPressureFlow: snippet model is %s"
- "#GetHealthQuantityFlow: In successResponseFlow intent is %@"
- "#GetHealthQuantityFlow: In successResponseFlow intent response is %@"
- "#GetSleepAnalysisFlow: output is %s"
- "#GetSleepAnalysisFlow: snippet model is %s"
- "Failed to produce patternResult from response: %@"
- "LogPeriodIntentResponse missing date param: %@"
- "Recommendation: %s"

```
