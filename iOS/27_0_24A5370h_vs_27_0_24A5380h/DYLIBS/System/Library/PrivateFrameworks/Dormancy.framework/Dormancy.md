## Dormancy

> `/System/Library/PrivateFrameworks/Dormancy.framework/Dormancy`

```diff

-  __TEXT.__text: 0x6c44
+  __TEXT.__text: 0x6bc4
   __TEXT.__const: 0xa9c
   __TEXT.__constg_swiftt: 0x354
   __TEXT.__swift5_typeref: 0x2ff

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__unwind_info: 0x288
-  __TEXT.__eh_frame: 0x1e8
+  __TEXT.__eh_frame: 0x1f0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x5e8
   __AUTH_CONST.__objc_const: 0x280
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH.__data: 0x208
   __DATA.__data: 0x2b0
   __DATA.__bss: 0x1000

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 226
-  Symbols:   205
+  Symbols:   207
   CStrings:  6
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__data : content changed
Symbols:
+ _swift_task_alloc
+ _swift_task_dealloc

```
