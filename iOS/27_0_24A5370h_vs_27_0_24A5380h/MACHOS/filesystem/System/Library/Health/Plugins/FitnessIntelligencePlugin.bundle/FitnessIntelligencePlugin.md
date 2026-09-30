## FitnessIntelligencePlugin

> `/System/Library/Health/Plugins/FitnessIntelligencePlugin.bundle/FitnessIntelligencePlugin`

```diff

-  __TEXT.__text: 0x7f3a4
-  __TEXT.__auth_stubs: 0x1e40
-  __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x1168
-  __TEXT.__const: 0x15b8
+  __TEXT.__text: 0x80554
+  __TEXT.__auth_stubs: 0x1f30
+  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_methlist: 0x119c
+  __TEXT.__const: 0x15e8
   __TEXT.__cstring: 0x1b0f
-  __TEXT.__constg_swiftt: 0xbb4
-  __TEXT.__swift5_typeref: 0x12ea
+  __TEXT.__constg_swiftt: 0xbbc
+  __TEXT.__swift5_typeref: 0x130e
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x77f
   __TEXT.__swift5_fieldmd: 0x7f0
-  __TEXT.__swift5_capture: 0x10ec
+  __TEXT.__swift5_capture: 0x1110
   __TEXT.__objc_methtype: 0xb8b
-  __TEXT.__oslogstring: 0x138f
+  __TEXT.__oslogstring: 0x142f
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_proto: 0xbc
   __TEXT.__swift5_types: 0x9c
   __TEXT.__objc_classname: 0x936
   __TEXT.__objc_methname: 0x16c9
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x12d0
-  __TEXT.__eh_frame: 0x1bd8
-  __DATA_CONST.__const: 0x42c8
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__unwind_info: 0x1328
+  __TEXT.__eh_frame: 0x1d18
+  __DATA_CONST.__const: 0x4318
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__auth_got: 0xf28
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__auth_got: 0xfa0
+  __DATA_CONST.__got: 0x550
   __DATA_CONST.__auth_ptr: 0x468
-  __DATA.__objc_const: 0x15e8
-  __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_data: 0x12a0
-  __DATA.__data: 0x16f8
+  __DATA.__objc_const: 0x15f8
+  __DATA.__objc_selrefs: 0x4d0
+  __DATA.__objc_data: 0x12a8
+  __DATA.__data: 0x1708
   __DATA.__bss: 0x1790
   __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1796
-  Symbols:   232
-  CStrings:  516
+  Functions: 1813
+  Symbols:   237
+  CStrings:  520
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__objc_methname : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _notify_post
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
CStrings:
+ "[%s] A workout completed, release FitnessIntelligence os transaction"
+ "[%s] Failed to invalidate OSTransaction: %@. Sending Darwin Notification"
+ "publicState"
+ "touchWithCompletion:"

```
