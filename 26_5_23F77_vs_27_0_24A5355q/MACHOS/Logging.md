## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Logging`

```diff

-134.120.2.0.0
-  __TEXT.__text: 0xa0b8
-  __TEXT.__auth_stubs: 0x990
+188.0.0.0.0
+  __TEXT.__text: 0xa1b0
+  __TEXT.__auth_stubs: 0xa70
   __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x40c
-  __TEXT.__const: 0x8be
-  __TEXT.__cstring: 0xb55
-  __TEXT.__swift5_typeref: 0x326
+  __TEXT.__objc_methlist: 0x444
+  __TEXT.__const: 0x8de
+  __TEXT.__cstring: 0xc85
+  __TEXT.__swift5_typeref: 0x32c
   __TEXT.__swift5_capture: 0x88
-  __TEXT.__objc_methtype: 0x459
+  __TEXT.__objc_methtype: 0x45b
   __TEXT.__objc_methname: 0x5dc
-  __TEXT.__constg_swiftt: 0x2e0
+  __TEXT.__constg_swiftt: 0x31c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_reflstr: 0x2d0
-  __TEXT.__swift5_fieldmd: 0x2b4
-  __TEXT.__objc_classname: 0x1cb
+  __TEXT.__swift5_reflstr: 0x2b0
+  __TEXT.__swift5_fieldmd: 0x2c4
+  __TEXT.__objc_classname: 0x1fb
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x58
-  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x330
   __TEXT.__eh_frame: 0x188
-  __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x5c8
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x798
+  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_ptr: 0x1d8
+  __DATA.__objc_const: 0x828
   __DATA.__objc_selrefs: 0x178
-  __DATA.__objc_data: 0x710
-  __DATA.__data: 0x460
+  __DATA.__objc_data: 0x7d0
+  __DATA.__data: 0x488
   __DATA.__common: 0x8
   __DATA.__bss: 0x750
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3D4BBBFE-944E-3A2B-81FE-01331F10B1AC
-  Functions: 307
-  Symbols:   114
-  CStrings:  172
+  UUID: F7FE9D6E-F799-3B75-9D92-9256D9225335
+  Functions: 320
+  Symbols:   128
+  CStrings:  175
 
Symbols:
+ _objc_release_x28
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
- _objc_retain_x24
- _objc_retain_x25
- _swift_getObjCClassFromMetadata
- _swift_unknownObjectRelease_n
CStrings:
+ "File already contains logging data. The new logging data will be appended and will supersede the existing data when read by tools."
+ "Logging.StateReportingDataCategory"
+ "_TtC7Logging26StateReportingDataCategory"
+ "subsystem == \"com.apple.StateReporting.Transition\" OR subsystem == \"com.apple.StateReporting.Heartbeat\" OR subsystem == \"com.apple.StateReporting.Volatile\""
- "logging data is already present in the file"

```
