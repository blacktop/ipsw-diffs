## Managed Background Assets Processing Pipeline

> `/System/Library/StreamingExtractorPlugins/Managed Background Assets Processing Pipeline.bundle/Managed Background Assets Processing Pipeline`

```diff

-1.0.35.0.0
-  __TEXT.__text: 0x9b38
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x24c
-  __TEXT.__const: 0x1fa
-  __TEXT.__cstring: 0x3ba
-  __TEXT.__objc_methname: 0x30b
-  __TEXT.__constg_swiftt: 0xe8
-  __TEXT.__swift5_typeref: 0x2a7
-  __TEXT.__swift5_reflstr: 0x100
-  __TEXT.__swift5_fieldmd: 0xf4
-  __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x8bb
-  __TEXT.__swift5_types: 0x10
+1.0.41.0.0
+  __TEXT.__text: 0x1287c
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x2c4
+  __TEXT.__const: 0x6c0
+  __TEXT.__cstring: 0x50a
+  __TEXT.__objc_methname: 0x343
+  __TEXT.__constg_swiftt: 0x1f4
+  __TEXT.__swift5_typeref: 0x37b
+  __TEXT.__swift5_reflstr: 0x18c
+  __TEXT.__swift5_fieldmd: 0x1d8
+  __TEXT.__swift5_capture: 0x2b0
+  __TEXT.__oslogstring: 0xc9b
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x28
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0x1f1
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x300
-  __TEXT.__eh_frame: 0x700
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__auth_ptr: 0xb8
-  __DATA_CONST.__const: 0x368
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__swift_as_entry: 0x68
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__unwind_info: 0x548
+  __TEXT.__eh_frame: 0xe68
+  __DATA_CONST.__auth_got: 0x5b8
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_ptr: 0x1f8
+  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x400
-  __DATA.__objc_selrefs: 0x128
-  __DATA.__objc_data: 0x100
-  __DATA.__data: 0x508
+  __DATA.__objc_const: 0x508
+  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x790
+  __DATA.__bss: 0x780
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/ManagedBackgroundAssets

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 51546A9E-9B3D-3C52-A048-4139461C5C7A
-  Functions: 162
-  Symbols:   98
-  CStrings:  145
+  UUID: 601525CA-5A13-39AC-93DC-A9E68DEF73BE
+  Functions: 329
+  Symbols:   113
+  CStrings:  170
 
Symbols:
+ _OBJC_CLASS_$_NSFileManager
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swiftEmptyDictionarySingleton
+ _objc_allocWithZone
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x8
+ _swift_allocError
+ _swift_beginAccess
+ _swift_endAccess
+ _swift_unknownObjectUnownedDestroy
+ _swift_unknownObjectUnownedInit
+ _swift_unknownObjectUnownedLoadStrong
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_willThrowTypedImpl
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "A processing pipeline couldn’t be created."
+ "ManagedBackgroundAssetsProcessingPipeline.Dispatcher"
+ "No processing pipeline with the ID "
+ "No processing pipeline with the ID “%{public}s” was found; creating a new processing pipeline…"
+ "No resumption URL is available for the processing pipeline with the ID “%{public}s”."
+ "Recording an offset of %llu bytes for the processing pipeline with the ID “%{public}s”…"
+ "Removing the resumption info at “%{public}s” for the processing pipeline with the ID “%{public}s”…"
+ "Resuming the processing pipeline with the ID “%{public}s” at an offset of %llu bytes…"
+ "Resumption info was found at “%{public}s”; reusing an existing processing pipeline…"
+ "Resumption info wasn’t found at “%{public}s”; creating a new processing pipeline with the ID “%{public}s”…"
+ "ResumptionInfo.plist"
+ "Set delegate: %{public}s"
+ "Suspending the stream pipeline…"
+ "The existing processing pipeline’s ID is “%{public}s”."
+ "The stream pipeline finished after processing %ld bytes."
+ "The stream pipeline finished."
+ "Tq,N,R"
+ "_TtC41ManagedBackgroundAssetsProcessingPipeline10Dispatcher"
+ "_TtC41ManagedBackgroundAssetsProcessingPipeline18ProcessingPipeline"
+ "currentPipelineID"
+ "defaultManager"
+ "delegateReference"
+ "fileExistsAtPath:"
+ "options"
+ "removeItemAtURL:error:"
+ "resumptionInfoURL"
- "_TtC41ManagedBackgroundAssetsProcessingPipelineP33_9456D61BDCCB6977D8ACD7548C831DE818ProcessingPipeline"

```
