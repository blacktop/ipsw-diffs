## SiriUploadWorker

> `/System/Library/ExtensionKit/Extensions/SiriUploadWorker.appex/SiriUploadWorker`

```diff

-3525.2.2.0.0
-  __TEXT.__text: 0x5f3c
-  __TEXT.__auth_stubs: 0x7a0
+3600.13.1.0.0
+  __TEXT.__text: 0x6b64
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x2d8
+  __TEXT.__const: 0x318
   __TEXT.__cstring: 0x19f
   __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methname: 0x59
+  __TEXT.__objc_methname: 0x79
   __TEXT.__objc_methtype: 0x1
   __TEXT.__constg_swiftt: 0x64
-  __TEXT.__swift5_typeref: 0xc4
-  __TEXT.__swift5_reflstr: 0x58
-  __TEXT.__swift5_fieldmd: 0x5c
-  __TEXT.__oslogstring: 0x383
+  __TEXT.__swift5_typeref: 0x100
+  __TEXT.__swift5_reflstr: 0x7e
+  __TEXT.__swift5_fieldmd: 0x68
+  __TEXT.__oslogstring: 0x413
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x30
+  __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x1d8
-  __TEXT.__eh_frame: 0x458
-  __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__auth_ptr: 0xf0
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__eh_frame: 0x480
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xf8
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_ptr: 0x100
+  __DATA.__objc_const: 0x118
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x160
+  __DATA.__data: 0x198
   __DATA.__common: 0x18
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3EB528EA-6572-33AA-A568-759A77EC78BA
-  Functions: 132
-  Symbols:   75
-  CStrings:  27
+  UUID: 2DDD869B-1309-387D-9FE7-E86738B5212D
+  Functions: 153
+  Symbols:   77
+  CStrings:  30
 
Symbols:
+ _objc_release_x24
+ _objc_release_x27
+ _swift_arrayInitWithCopy
+ _swift_retain_x28
+ _swift_runtimeSupportsNoncopyableTypes
- _objc_release_x23
- _swift_retain_n
- _swift_unknownObjectRelease
CStrings:
+ "Upload WAS bypassed- sending Unilog bypass telemetry with error %s"
+ "Upload was NOT bypassed- not sending Unilog bypass telemetry"
+ "requiresBypassTelemetry"

```
