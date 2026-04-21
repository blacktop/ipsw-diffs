## Managed Background Assets Processing Pipeline

> `/System/Library/StreamingExtractorPlugins/Managed Background Assets Processing Pipeline.bundle/Managed Background Assets Processing Pipeline`

```diff

-1.5.3.0.0
-  __TEXT.__text: 0x15b08
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0xc0
-  __TEXT.__objc_methlist: 0x2c4
-  __TEXT.__const: 0x824
+1.5.5.0.0
+  __TEXT.__text: 0x125ec
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_stubs: 0x60
+  __TEXT.__objc_methlist: 0x2cc
+  __TEXT.__const: 0x698
   __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methname: 0x5dd
-  __TEXT.__objc_methtype: 0x28e
-  __TEXT.__constg_swiftt: 0x1f4
-  __TEXT.__swift5_typeref: 0x3c7
-  __TEXT.__swift5_reflstr: 0x1bc
-  __TEXT.__swift5_fieldmd: 0x1f0
-  __TEXT.__cstring: 0x1da
+  __TEXT.__objc_methname: 0x59d
+  __TEXT.__objc_methtype: 0x29e
+  __TEXT.__constg_swiftt: 0x1a8
+  __TEXT.__swift5_typeref: 0x3ac
+  __TEXT.__swift5_reflstr: 0x1a2
+  __TEXT.__swift5_fieldmd: 0x1a0
+  __TEXT.__cstring: 0x1ba
   __TEXT.__swift5_capture: 0x2d0
-  __TEXT.__oslogstring: 0xd58
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__swift_as_entry: 0x68
+  __TEXT.__oslogstring: 0xa78
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x64
-  __TEXT.__unwind_info: 0x538
-  __TEXT.__eh_frame: 0xe40
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__auth_ptr: 0x1f8
-  __DATA_CONST.__const: 0x790
+  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__eh_frame: 0xd10
+  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0x170
+  __DATA_CONST.__const: 0x700
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0x548
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x128
   __DATA.__objc_data: 0x1f0
-  __DATA.__data: 0x7a0
-  __DATA.__bss: 0x780
+  __DATA.__data: 0x6b0
+  __DATA.__bss: 0x400
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/ManagedBackgroundAssets

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B37EF9FE-D48E-3490-A3FF-E68F2844D45F
-  Functions: 336
-  Symbols:   118
-  CStrings:  164
+  UUID: 2D8D0DAA-CA40-3D4C-BEB8-8703E3D6CDB2
+  Functions: 297
+  Symbols:   116
+  CStrings:  153
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x27
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
- _OBJC_CLASS_$_NSFileManager
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x25
- _swift_beginAccess
- _swift_endAccess
CStrings:
+ "Canceling the processing pipeline with the ID “%{public}s”…"
+ "Remove current pipeline"
+ "processingTask"
- "No processing pipeline with the ID “%{public}s” was found; creating a new processing pipeline…"
- "No resumption URL is available for the processing pipeline with the ID “%{public}s”."
- "Recording an offset of %llu bytes for the processing pipeline with the ID “%{public}s”…"
- "Removing the resumption info at “%{public}s” for the processing pipeline with the ID “%{public}s”…"
- "Resuming the processing pipeline with the ID “%{public}s” at an offset of %llu bytes…"
- "Resumption info was found at “%{public}s”; reusing an existing processing pipeline…"
- "Resumption info wasn’t found at “%{public}s”; creating a new processing pipeline with the ID “%{public}s”…"
- "ResumptionInfo.plist"
- "Set delegate: %{public}s"
- "The existing processing pipeline’s ID is “%{public}s”."
- "defaultManager"
- "fileExistsAtPath:"
- "removeItemAtURL:error:"
- "resumptionInfoURL"

```
