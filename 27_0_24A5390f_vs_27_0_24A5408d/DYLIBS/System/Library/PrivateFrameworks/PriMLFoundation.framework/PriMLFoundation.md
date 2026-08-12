## PriMLFoundation

> `/System/Library/PrivateFrameworks/PriMLFoundation.framework/PriMLFoundation`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x70aa4
+42.0.0.0.0
+  __TEXT.__text: 0x7571c
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x3d28
-  __TEXT.__cstring: 0x806
-  __TEXT.__swift5_typeref: 0xfa8
-  __TEXT.__swift5_fieldmd: 0x1418
-  __TEXT.__constg_swiftt: 0x1254
-  __TEXT.__swift5_reflstr: 0x1161
-  __TEXT.__oslogstring: 0x1abd
+  __TEXT.__const: 0x3ea8
+  __TEXT.__cstring: 0x882
+  __TEXT.__swift5_typeref: 0xfde
+  __TEXT.__swift5_fieldmd: 0x14b4
+  __TEXT.__constg_swiftt: 0x12d8
+  __TEXT.__swift5_reflstr: 0x11e1
+  __TEXT.__oslogstring: 0x1ccd
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_proto: 0x240
-  __TEXT.__swift5_types: 0x13c
-  __TEXT.__swift_as_entry: 0x114
-  __TEXT.__swift_as_ret: 0x124
-  __TEXT.__swift_as_cont: 0x260
-  __TEXT.__swift5_capture: 0x25c
+  __TEXT.__swift5_proto: 0x248
+  __TEXT.__swift5_types: 0x148
+  __TEXT.__swift_as_entry: 0x12c
+  __TEXT.__swift_as_ret: 0x140
+  __TEXT.__swift_as_cont: 0x294
+  __TEXT.__swift5_capture: 0x27c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x18b8
-  __TEXT.__eh_frame: 0x35e8
+  __TEXT.__unwind_info: 0x19f0
+  __TEXT.__eh_frame: 0x3a20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2730
-  __AUTH_CONST.__objc_const: 0x2350
-  __AUTH_CONST.__auth_got: 0xc88
+  __AUTH_CONST.__const: 0x28f8
+  __AUTH_CONST.__objc_const: 0x2468
+  __AUTH_CONST.__auth_got: 0xce8
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x11b0
-  __DATA.__data: 0x910
+  __AUTH.__data: 0x1258
+  __DATA.__data: 0x968
   __DATA.__bss: 0x3590
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0xcb0
+  __DATA_DIRTY.__data: 0xcc8
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1953
-  Symbols:   745
-  CStrings:  188
+  Functions: 2025
+  Symbols:   759
+  CStrings:  199
 
Symbols:
+ __DATA__TtC15PriMLFoundation14LocalStoreSink
+ __IVARS__TtC15PriMLFoundation14LocalStoreSink
+ __METACLASS_DATA__TtC15PriMLFoundation14LocalStoreSink
+ _objc_msgSend$localizedDescription
+ _swift_deallocPartialClassInstance
+ _swift_release_x9
+ _swift_retain_x26
+ _swift_task_localValueGet
+ _symbolic SaySJG
+ _symbolic _____ 15PriMLFoundation14LocalStoreSinkC
+ _symbolic _____ 15PriMLFoundation16FailedTaskResultV
+ _symbolic _____ 15PriMLFoundation20TaskExecutionContextO
+ _symbolic _____ySJG s23_ContiguousArrayStorageC
+ _symbolic _____y______pSgG s9TaskLocalC 15PriMLFoundation0A10DownloaderP
+ _type_layout_string 15PriMLFoundation16FailedTaskResultV
- _swift_release_x10
CStrings:
+ "Recipe collectionIdPrefix '%s' is not prefixed by plugin '%s'"
+ "Recipe for PFL/ETL task %s is missing `collectionIdPrefix`; falling back to plugin[:useCase]."
+ "Recipe for fedStats task %s is missing `clientIdentifier`; falling back to plugin[:useCase]."
+ "[LocalStoreSink] Failed to store task result at %s: %@"
+ "[LocalStoreSink] Stored task result under %s"
+ "[PriMLPlugin] Skipping failure sink fan-out: task.taskId '%s' is not a parseable TaskId"
+ "[PriMLPlugin] handleFailure for task %s itself failed: %@."
+ "error_description"
+ "failureSubmission"
+ "skip_crash_record_check"
+ "task_result_store_path"
```
