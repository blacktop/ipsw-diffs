## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Logging`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x8cc8
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x380
-  __TEXT.__const: 0x81e
-  __TEXT.__cstring: 0xd3b
-  __TEXT.__swift5_typeref: 0x2a4
+134.100.19.0.0
+  __TEXT.__text: 0x9ee0
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x3d4
+  __TEXT.__const: 0x876
+  __TEXT.__cstring: 0xaee
+  __TEXT.__swift5_typeref: 0x320
   __TEXT.__swift5_capture: 0x88
-  __TEXT.__objc_methname: 0x3dd
-  __TEXT.__constg_swiftt: 0x268
+  __TEXT.__objc_methtype: 0x459
+  __TEXT.__objc_methname: 0x5dc
+  __TEXT.__constg_swiftt: 0x2a4
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_reflstr: 0x280
-  __TEXT.__swift5_fieldmd: 0x264
+  __TEXT.__swift5_reflstr: 0x2d0
+  __TEXT.__swift5_fieldmd: 0x298
+  __TEXT.__objc_classname: 0x19a
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__objc_classname: 0x4a
-  __TEXT.__objc_methtype: 0x2ad
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__unwind_info: 0x308
   __TEXT.__eh_frame: 0x188
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x580
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x648
-  __DATA.__objc_selrefs: 0x168
-  __DATA.__objc_data: 0x588
-  __DATA.__data: 0x3d0
+  __DATA.__objc_const: 0x708
+  __DATA.__objc_selrefs: 0x178
+  __DATA.__objc_data: 0x650
+  __DATA.__data: 0x430
   __DATA.__common: 0x8
   __DATA.__bss: 0x750
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 29CEA3B2-BA74-362E-9419-7BB790FA9768
-  Functions: 279
+  UUID: 4052C1FF-EA77-3392-A353-486D1F937F23
+  Functions: 294
   Symbols:   114
-  CStrings:  160
+  CStrings:  168
 
Symbols:
+ _objc_retain_x28
- _objc_release_x28
CStrings:
+ "'. Expected format: 'subsystem/category[,subsystem/category,...]' (e.g., 'com.example.app/networking,com.example.app/database')."
+ "B32@0:8^{ktrace_target_process=i}16^@24"
+ "Invalid format for persist-signpost-handles: '"
+ "Logging.MetricKitDataCategory"
+ "_TtC7Logging21MetricKitDataCategory"
+ "enable-persist-signposts"
+ "enablePersistSignpostHandles"
+ "informWithMessage:"
+ "shouldTargetProcess:error:"
+ "subsystem == \"com.apple.metrickit.log\""

```
