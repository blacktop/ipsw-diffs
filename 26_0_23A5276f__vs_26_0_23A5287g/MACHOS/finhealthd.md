## finhealthd

> `/System/Library/PrivateFrameworks/FinHealth.framework/finhealthd`

```diff

-1.8.1.45.0
-  __TEXT.__text: 0x9f74
-  __TEXT.__auth_stubs: 0x770
+1.8.1.46.0
+  __TEXT.__text: 0xb828
+  __TEXT.__auth_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__const: 0x2a2
-  __TEXT.__objc_methname: 0x33a
-  __TEXT.__oslogstring: 0x758
+  __TEXT.__const: 0x2f2
+  __TEXT.__objc_methname: 0x357
+  __TEXT.__oslogstring: 0x7d8
   __TEXT.__cstring: 0x36d
-  __TEXT.__constg_swiftt: 0x1e0
+  __TEXT.__constg_swiftt: 0x218
   __TEXT.__swift5_typeref: 0x200
   __TEXT.__swift5_reflstr: 0x197
   __TEXT.__swift5_fieldmd: 0x11c
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x54
-  __TEXT.__swift5_capture: 0x168
+  __TEXT.__swift_as_entry: 0x60
+  __TEXT.__swift_as_ret: 0x7c
+  __TEXT.__swift5_capture: 0x188
   __TEXT.__objc_classname: 0x30
   __TEXT.__objc_methtype: 0x121
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__eh_frame: 0x8b8
-  __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x460
+  __TEXT.__eh_frame: 0xba0
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0x538
-  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_selrefs: 0x168
   __DATA.__objc_data: 0x1a8
-  __DATA.__data: 0x438
+  __DATA.__data: 0x478
   __DATA.__common: 0x8
   - /System/Library/Frameworks/FinanceKit.framework/FinanceKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22D80E23-20F0-34B7-91A8-19D4383E410F
-  Functions: 324
-  Symbols:   196
-  CStrings:  133
+  UUID: 228B4353-23FA-3972-8A8B-598C8B0765BB
+  Functions: 345
+  Symbols:   202
+  CStrings:  137
 
Symbols:
+ _$s13FinHealthCore12EntityGroupsC014deleteOutdateddE11AndInsightsSaySSGyFTj
+ _$s13FinHealthCore14IncomeInsightsC6deleteyySaySSGYaKFTjTu
+ _$s13FinHealthCore14IncomeInsightsC9deleteAllyyYaKFTjTu
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sSSN
+ _$sSa11descriptionSSvg
CStrings:
+ "Clearing insights for group ids: %s"
+ "Schema updated -- Clearing all insights"
+ "delete income insights - failed with error: %@"
+ "didReceiveInsightChangeUpdate - An update is already in progress. Skipping this request"
+ "entityGroupsWriter failed to save: %@"
+ "fhAllAccess"
+ "updateInProgress"
- "Finished running predictedTransactionsWriter in overnightSync"
- "Started running predictedTransactionsWriter in overnightSync"
- "entityGroupsWriter failed"

```
