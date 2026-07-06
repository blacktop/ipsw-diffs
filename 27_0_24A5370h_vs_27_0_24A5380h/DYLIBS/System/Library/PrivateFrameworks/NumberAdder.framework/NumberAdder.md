## NumberAdder

> `/System/Library/PrivateFrameworks/NumberAdder.framework/NumberAdder`

```diff

-  __TEXT.__text: 0xdd0
+  __TEXT.__text: 0xe0c
   __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0xa9
-  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__cstring: 0x149
   __TEXT.__oslogstring: 0xdf
-  __TEXT.__unwind_info: 0x148
+  __TEXT.__unwind_info: 0x138
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 35
-  Symbols:   180
+  Symbols:   177
   CStrings:  15
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ GCC_except_table21
+ ____ZN19CLConnectionDeleterclEP12CLConnection_block_invoke
+ _objc_release_x21
- GCC_except_table22
- GCC_except_table25
- __ZSt9terminatev
- ___clang_call_terminate
- ___cxa_begin_catch
- _objc_release
Functions:
~ ___19-[NumberAdder init]_block_invoke : 236 -> 224
~ ___clang_call_terminate -> __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220106Em : 20 -> 144
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220106Em -> __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220106Ev : 144 -> 24
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220106Ev -> __ZNSt3__120__throw_length_errorB9fqe220106EPKc : 24 -> 92
~ __ZNSt3__120__throw_length_errorB9fqe220106EPKc -> __ZNSt12length_errorC1B9fqe220106EPKc : 92 -> 52
~ __ZNSt12length_errorC1B9fqe220106EPKc -> ____ZL43_CLLogObjectForCategory_NumberAdder_Defaultv_block_invoke : 52 -> 48
~ ____ZL43_CLLogObjectForCategory_NumberAdder_Defaultv_block_invoke -> __ZNSt3__110unique_ptrI12CLConnection19CLConnectionDeleterE5resetB9fqe220106EPS1_ : 48 -> 128
~ __ZNSt3__110unique_ptrI12CLConnection19CLConnectionDeleterE5resetB9fqe220106EPS1_ -> ____ZN19CLConnectionDeleterclEP12CLConnection_block_invoke : 44 -> 8

```
