## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication`

```diff

-  __TEXT.__text: 0xc58e0
-  __TEXT.__objc_methlist: 0x6c18
+  __TEXT.__text: 0xc5ae8
+  __TEXT.__objc_methlist: 0x6c30
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x5ba4
-  __TEXT.__cstring: 0x11798
+  __TEXT.__gcc_except_tab: 0x5bb4
+  __TEXT.__cstring: 0x117b8
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2e88
+  __TEXT.__unwind_info: 0x2e90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x3b48
+  __DATA_CONST.__objc_selrefs: 0x3b58
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x8f8
-  __DATA_CONST.__got: 0x4c8
-  __AUTH_CONST.__const: 0x4b30
+  __DATA_CONST.__got: 0x4d0
+  __AUTH_CONST.__const: 0x4b60
   __AUTH_CONST.__cfstring: 0xdec0
-  __AUTH_CONST.__objc_const: 0xd098
+  __AUTH_CONST.__objc_const: 0xd0b8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0xe0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xdbc
+  __DATA.__objc_ivar: 0xdc0
   __DATA.__data: 0xd80
   __DATA.__bss: 0x4a8
   __DATA.__common: 0x48

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3498
-  Symbols:   8272
-  CStrings:  4800
+  Functions: 3501
+  Symbols:   8279
+  CStrings:  4801
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[VMUObjectIdentifier buildOriginalMetaclassMap]
+ -[VMUObjectIdentifier originalMetaclassForObjCClassWithIsa:]
+ GCC_except_table106
+ GCC_except_table149
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table174
+ GCC_except_table180
+ GCC_except_table90
+ GCC_except_table97
+ OBJC_IVAR_$_VMUObjectIdentifier._classToOriginalMetaclassMap
+ ___48-[VMUObjectIdentifier buildOriginalMetaclassMap]_block_invoke
+ ___block_descriptor_64_e8_32s_e22_v24?0r^v8"NSError"16l
+ _objc_msgSend$buildOriginalMetaclassMap
+ _objc_msgSend$originalMetaclassForObjCClassWithIsa:
- GCC_except_table157
- GCC_except_table159
- GCC_except_table168
- GCC_except_table177
CStrings:
+ "_objc_debug_original_metaclass_map"

```
