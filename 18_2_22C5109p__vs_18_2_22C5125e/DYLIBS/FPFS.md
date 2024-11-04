## FPFS

> `/System/Library/PrivateFrameworks/FPFS.framework/FPFS`

```diff

-2732.60.87.502.1
-  __TEXT.__text: 0x8b4158
-  __TEXT.__auth_stubs: 0x4f00
+2732.60.111.0.0
+  __TEXT.__text: 0x8bd588
+  __TEXT.__auth_stubs: 0x4f10
   __TEXT.__objc_methlist: 0x1780
   __TEXT.__ustring: 0x30
-  __TEXT.__const: 0x1ae9c
+  __TEXT.__const: 0x1aebc
   __TEXT.__gcc_except_tab: 0x520
-  __TEXT.__oslogstring: 0xdf8a
-  __TEXT.__cstring: 0x2bd06
-  __TEXT.__swift5_typeref: 0xe7af
-  __TEXT.__constg_swiftt: 0xf404
+  __TEXT.__oslogstring: 0xe05a
+  __TEXT.__cstring: 0x2bcb6
+  __TEXT.__swift5_typeref: 0xe83f
+  __TEXT.__constg_swiftt: 0xf488
   __TEXT.__swift5_builtin: 0x6f4
-  __TEXT.__swift5_reflstr: 0x922e
-  __TEXT.__swift5_fieldmd: 0x834c
+  __TEXT.__swift5_reflstr: 0x93be
+  __TEXT.__swift5_fieldmd: 0x83e8
   __TEXT.__swift5_assocty: 0x1c08
-  __TEXT.__swift5_capture: 0x140d0
+  __TEXT.__swift5_capture: 0x1416c
   __TEXT.__swift5_proto: 0x1358
   __TEXT.__swift5_types: 0x86c
   __TEXT.__swift5_mpenum: 0xfc
   __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xf4f8
+  __TEXT.__unwind_info: 0xf528
   __TEXT.__eh_frame: 0x20c94
   __TEXT.__objc_classname: 0x33f
   __TEXT.__objc_methname: 0x992e

   __DATA_CONST.__objc_selrefs: 0x24e0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x2790
-  __AUTH_CONST.__auth_ptr: 0x27b0
-  __AUTH_CONST.__const: 0x3c528
+  __AUTH_CONST.__auth_got: 0x2798
+  __AUTH_CONST.__auth_ptr: 0x2580
+  __AUTH_CONST.__const: 0x3c640
   __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x11240
+  __AUTH_CONST.__objc_const: 0x112a0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xbb8
-  __AUTH.__data: 0x1888
+  __AUTH.__objc_data: 0xad8
+  __AUTH.__data: 0x1868
   __DATA.__objc_ivar: 0x124
-  __DATA.__data: 0x62a0
-  __DATA.__bss: 0x1dc90
-  __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_data: 0x1fa0
-  __DATA_DIRTY.__data: 0xbc80
-  __DATA_DIRTY.__bss: 0x7f30
+  __DATA.__data: 0x6310
+  __DATA.__bss: 0x1da90
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x20c8
+  __DATA_DIRTY.__data: 0xbc30
+  __DATA_DIRTY.__bss: 0x8130
   __DATA_DIRTY.__common: 0x638
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24110
-  Symbols:   3444
-  CStrings:  6203
+  Functions: 24155
+  Symbols:   3443
+  CStrings:  6213
 
CStrings:
+ "backgroundActivityPaused"
+ "childrenCreating"
+ "childrenToDelete"
+ "containsDatalessChildren"
+ "containsMaterializedChildren"
+ "dependentOperations"
+ "destinationLockRegistration"
+ "detachedRoots"
+ "fetchItemMetadata"
+ "fetchParentMetadata"
+ "missing `a` baseVersion in "
+ "missing `b` baseVersion in "
+ "no destination item"
+ "parentRecursivelyDeleting"
+ "permanentlyThrottled"
+ "recursiveDeletion"
+ "source item is reconciled"
+ "sourceLockRegistration"
+ "throttledFetchMetadata"
+ "⧗canConfirmChildrenDeletion"
+ "📦 x-validation found %!{(MISSING)public}s of non-doc-tracked type %!{(MISSING)public}s while expecting %!{(MISSING)public}s: failing docID lookup"
+ "🔏  job locked out of execution %!{(MISSING)public}s by destination rules %!@(MISSING)"
+ "🔏  job locked out of execution %!{(MISSING)public}s by source rules %!@(MISSING)"
- "\n                AND item_jobs.scheduling_state_conditions & "
- "\n              )\n            OR\n              (\n                item_jobs.scheduling_state = "
- "\n           )\n LIMIT 1"
- "\n       AND (\n              (\n                item_jobs.scheduling_state = "
- "\n       AND item_jobs.scheduling_state IN "
- "\n    AND throttle.job_type = "
- "\n WHERE item_jobs.type = "
- " != 0\n                AND throttle.domain_wide_error = "
- " == 0\n              )\n            OR\n              item_jobs.scheduling_state IN "
- " as item_jobs\nLEFT JOIN "
- "_throttle AS throttle ON throttle.item_id = item_jobs.item_id\n    AND throttle.kind = "
- "lockRegistration"
- "🔏  job locked out of execution %!{(MISSING)public}s by rules %!@(MISSING)"

```
