## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-  __TEXT.__text: 0xbb7a8
-  __TEXT.__objc_methlist: 0x69d8
+  __TEXT.__text: 0xbb97c
+  __TEXT.__objc_methlist: 0x69f0
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x586c
-  __TEXT.__cstring: 0x11268
+  __TEXT.__gcc_except_tab: 0x5884
+  __TEXT.__cstring: 0x11288
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2d98
+  __TEXT.__unwind_info: 0x2da0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3e98
+  __DATA_CONST.__const: 0x3ee8
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x39e8
+  __DATA_CONST.__objc_selrefs: 0x39f8
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x8f8
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x12f8
   __AUTH_CONST.__cfstring: 0xdae0
-  __AUTH_CONST.__objc_const: 0xcb60
+  __AUTH_CONST.__objc_const: 0xcb80
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH.__objc_data: 0x608
+  __AUTH.__objc_data: 0x1238
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xd98
+  __DATA.__objc_ivar: 0xd9c
   __DATA.__data: 0xd18
   __DATA.__bss: 0x610
   __DATA.__common: 0x108
-  __DATA_DIRTY.__objc_data: 0x1838
+  __DATA_DIRTY.__objc_data: 0xc08
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xc8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3372
-  Symbols:   11421
-  CStrings:  4725
+  Functions: 3375
+  Symbols:   11432
+  CStrings:  4726
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[VMUObjectIdentifier buildOriginalMetaclassMap]
+ -[VMUObjectIdentifier originalMetaclassForObjCClassWithIsa:]
+ GCC_except_table137
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table160
+ GCC_except_table166
+ GCC_except_table94
+ _OBJC_IVAR_$_VMUObjectIdentifier._classToOriginalMetaclassMap
+ ___48-[VMUObjectIdentifier buildOriginalMetaclassMap]_block_invoke
+ ___block_descriptor_100_e8_32s40s48bs56r64r_e10_v16?0r^v8ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_64_e8_32s_e22_v24?0r^v8"NSError"16ls32l8
+ _objc_msgSend$buildOriginalMetaclassMap
+ _objc_msgSend$originalMetaclassForObjCClassWithIsa:
- GCC_except_table143
- GCC_except_table145
- GCC_except_table154
- GCC_except_table163
- GCC_except_table82
CStrings:
+ "_objc_debug_original_metaclass_map"

```
