## Managed Background Assets Processing Pipeline

> `/System/Library/StreamingExtractorPlugins/Managed Background Assets Processing Pipeline.bundle/Managed Background Assets Processing Pipeline`

```diff

-1.5.6.0.0
-  __TEXT.__text: 0x125ec
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x60
+2.0.26.0.0
+  __TEXT.__text: 0x1e8e8
+  __TEXT.__auth_stubs: 0xe80
+  __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x2cc
-  __TEXT.__const: 0x698
+  __TEXT.__cstring: 0x2aa
+  __TEXT.__const: 0x944
   __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methname: 0x59d
+  __TEXT.__objc_methname: 0x62d
   __TEXT.__objc_methtype: 0x29e
-  __TEXT.__constg_swiftt: 0x1a8
-  __TEXT.__swift5_typeref: 0x3ac
-  __TEXT.__swift5_reflstr: 0x1a2
-  __TEXT.__swift5_fieldmd: 0x1a0
-  __TEXT.__cstring: 0x1ba
-  __TEXT.__swift5_capture: 0x2d0
-  __TEXT.__oslogstring: 0xa78
-  __TEXT.__swift5_proto: 0x20
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__swift_as_entry: 0x6c
-  __TEXT.__swift_as_ret: 0x64
-  __TEXT.__unwind_info: 0x4d0
-  __TEXT.__eh_frame: 0xd10
-  __DATA_CONST.__auth_got: 0x568
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x170
-  __DATA_CONST.__const: 0x700
+  __TEXT.__constg_swiftt: 0x21c
+  __TEXT.__swift5_typeref: 0x4c5
+  __TEXT.__swift5_reflstr: 0x23a
+  __TEXT.__swift5_fieldmd: 0x260
+  __TEXT.__swift5_capture: 0x2c0
+  __TEXT.__oslogstring: 0xf38
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift_as_entry: 0x78
+  __TEXT.__swift_as_ret: 0x80
+  __TEXT.__swift_as_cont: 0xc0
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__unwind_info: 0x638
+  __TEXT.__eh_frame: 0x11c0
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x548
-  __DATA.__objc_selrefs: 0x128
-  __DATA.__objc_data: 0x1f0
-  __DATA.__data: 0x6b0
-  __DATA.__bss: 0x400
-  __DATA.__common: 0x8
+  __DATA_CONST.__auth_got: 0x748
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__auth_ptr: 0x238
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x150
+  __DATA.__objc_data: 0x208
+  __DATA.__data: 0x8e0
+  __DATA.__bss: 0x880
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/ManagedBackgroundAssets
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelper.framework/ManagedBackgroundAssetsHelper
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CD0D4219-3028-3ABF-B124-93F28A604E70
-  Functions: 297
-  Symbols:   116
-  CStrings:  153
+  UUID: 83FCE06C-18A9-3C8B-9ADA-7CE96642AE40
+  Functions: 387
+  Symbols:   149
+  CStrings:  184
 
Symbols:
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSProcessInfo
+ ___assert_rtn
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x28
+ _proc_pidinfo
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_endAccess
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x25
+ _swift_retain_x26
+ _sysctlbyname
+ _thread_count
+ _thread_count_limit
- _objc_retain_x22
CStrings:
+ "%lu out of %lu budgeted threads are active."
+ "Jettisoning the suspended processing pipeline with the ID “%{public}s”…"
+ "No processing pipeline with the ID “%{public}s” was found; creating a new processing pipeline…"
+ "No resumption URL is available for the processing pipeline with the ID “%{public}s”."
+ "Recording an offset of %llu bytes for the processing pipeline with the ID “%{public}s”…"
+ "Removing the resumption info at “%{public}s” for the processing pipeline with the ID “%{public}s”…"
+ "Resuming the processing pipeline with the ID “%{public}s” at an offset of %llu bytes…"
+ "Resumption info at “%{public}s” for the processing pipeline with the ID “%{public}s” couldn’t be removed: %{public}@"
+ "Resumption info was found at “%{public}s”; reusing an existing processing pipeline…"
+ "Resumption info wasn’t found at “%{public}s”; creating a new processing pipeline with the ID “%{public}s”…"
+ "ResumptionInfo.plist"
+ "Set delegate: %{public}s"
+ "Starting a new processing pipeline would exceed the thread budget."
+ "The existing processing pipeline’s ID is “%{public}s”."
+ "The stream pipeline is already finished."
+ "The thread budget was exceeded."
+ "defaultManager"
+ "fileExistsAtPath:"
+ "isActive"
+ "kern.wq_max_constrained_threads"
+ "minChunkSize"
+ "processIdentifier"
+ "processInfo"
+ "removeItemAtURL:error:"
+ "resumptionInfoURL"
+ "state"
+ "tc_lim_len == sizeof(int32_t)"
+ "terminateStreamWithError(_:)"
+ "thread.c"
+ "thread_count"
+ "thread_count_limit"
+ "tid_bufc % PROC_PIDLISTTHREADS_SIZE == 0"
- "minimumChunkSize"

```
