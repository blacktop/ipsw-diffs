## EmailFoundation

> `/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation`

```diff

-3864.200.81.2.5
-  __TEXT.__text: 0x65124
+3864.300.11.2.1
+  __TEXT.__text: 0x65520
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0x66b4
-  __TEXT.__gcc_except_tab: 0xc068
+  __TEXT.__objc_methlist: 0x6834
+  __TEXT.__gcc_except_tab: 0xc0e8
   __TEXT.__const: 0x1fa
   __TEXT.__cstring: 0x47a7
   __TEXT.__oslogstring: 0xdad

   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4ae0
+  __TEXT.__unwind_info: 0x4b38
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0xe72
-  __TEXT.__objc_methname: 0xc2a0
-  __TEXT.__objc_methtype: 0x1c0d
-  __TEXT.__objc_stubs: 0x8ac0
-  __DATA_CONST.__got: 0x748
+  __TEXT.__objc_classname: 0xe9c
+  __TEXT.__objc_methname: 0xc2a6
+  __TEXT.__objc_methtype: 0x1c4f
+  __TEXT.__objc_stubs: 0x8ae0
+  __DATA_CONST.__got: 0x750
   __DATA_CONST.__const: 0x20f8
-  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x34c0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0xa48
   __AUTH_CONST.__const: 0x1140
   __AUTH_CONST.__cfstring: 0x5580
-  __AUTH_CONST.__objc_const: 0xc348
+  __AUTH_CONST.__objc_const: 0xc5b0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x524
-  __DATA.__data: 0xea8
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x52c
+  __DATA.__data: 0xf08
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1f0
   __DATA_DIRTY.__objc_data: 0x22b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2466AFF4-A580-3711-85DA-246C5A8015F5
-  Functions: 2647
-  Symbols:   10070
-  CStrings:  4312
+  UUID: 04AB09CC-AAF8-30BF-863E-57A77C3569EF
+  Functions: 2671
+  Symbols:   10146
+  CStrings:  4317
 
Symbols:
+ +[EFCancelationToken tokenWithCancelationBlock:]
+ +[EFCancelationToken tokenWithLabel:cancelationBlock:]
+ +[_EFCancelationTokenImpl _descriptionString]
+ +[_EFCancelationTokenImpl tokenWithCancelationBlock:]
+ +[_EFCancelationTokenImpl tokenWithLabel:cancelationBlock:]
+ -[EFCancelationToken .cxx_destruct]
+ -[EFCancelationToken addCancelable:]
+ -[EFCancelationToken addCancelationBlock:]
+ -[EFCancelationToken cancel]
+ -[EFCancelationToken initWithLabel:]
+ -[EFCancelationToken init]
+ -[EFCancelationToken invoke]
+ -[EFCancelationToken isCanceled]
+ -[EFCancelationToken label]
+ -[EFCancelationToken removeAllCancelationBlocks]
+ -[EFManualCancelationToken .cxx_destruct]
+ -[EFManualCancelationToken initWithLabel:]
+ -[EFManualCancelationToken init]
+ -[EFManualCancelationToken invoke]
+ -[EFManualCancelationToken label]
+ -[_EFCancelationTokenImpl addCancelable:]
+ -[_EFCancelationTokenImpl addCancelationBlock:]
+ -[_EFCancelationTokenImpl cancel]
+ -[_EFCancelationTokenImpl isCanceled]
+ -[_EFCancelationTokenImpl removeAllCancelationBlocks]
+ _OBJC_CLASS_$__EFCancelationTokenImpl
+ _OBJC_IVAR_$_EFCancelationToken._impl
+ _OBJC_IVAR_$_EFManualCancelationToken._impl
+ _OBJC_METACLASS_$__EFCancelationTokenImpl
+ __OBJC_$_CLASS_METHODS_EFCancelationToken
+ __OBJC_$_CLASS_METHODS__EFCancelationTokenImpl
+ __OBJC_$_INSTANCE_METHODS__EFCancelationTokenImpl
+ __OBJC_$_INSTANCE_VARIABLES_EFCancelationToken
+ __OBJC_$_INSTANCE_VARIABLES_EFManualCancelationToken
+ __OBJC_$_PROP_LIST_EFCancelableToken
+ __OBJC_$_PROP_LIST_EFCancelationToken
+ __OBJC_$_PROP_LIST__EFCancelationTokenImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EFCancelableToken
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EFCancelableToken
+ __OBJC_$_PROTOCOL_REFS_EFCancelableToken
+ __OBJC_CLASS_PROTOCOLS_$_EFCancelationToken
+ __OBJC_CLASS_PROTOCOLS_$__EFCancelationTokenImpl
+ __OBJC_CLASS_RO_$__EFCancelationTokenImpl
+ __OBJC_LABEL_PROTOCOL_$_EFCancelableToken
+ __OBJC_METACLASS_RO_$__EFCancelationTokenImpl
+ __OBJC_PROTOCOL_$_EFCancelableToken
+ ___41-[_EFCancelationTokenImpl addCancelable:]_block_invoke
+ _objc_msgSend$removeAllCancelationBlocks
- +[EFManualCancelationToken _descriptionString]
- ___42-[EFManualCancelationToken addCancelable:]_block_invoke
CStrings:
+ "@\"_EFCancelationTokenImpl\""
+ "EFCancelableToken"
+ "_EFCancelationTokenImpl"
+ "_impl"
+ "v24@0:8@\"<EFCancelable>\"16"
+ "{set<long long, std::less<long long>, std::allocator<long long>>=\"__tree_\"{__tree<long long, std::less<long long>, std::allocator<long long>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{set<long long, std::less<long long>, std::allocator<long long>>=\"__tree_\"{__tree<long long, std::less<long long>, std::allocator<long long>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"

```
