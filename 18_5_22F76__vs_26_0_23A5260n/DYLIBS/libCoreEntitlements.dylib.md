## libCoreEntitlements.dylib

> `/usr/lib/libCoreEntitlements.dylib`

```diff

-69.100.2.0.0
-  __TEXT.__text: 0x7cf4
+80.0.0.0.0
+  __TEXT.__text: 0x774c
   __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0x260
   __TEXT.__cstring: 0x12a7
-  __TEXT.__gcc_except_tab: 0x1f8
-  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__gcc_except_tab: 0x184
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_methname: 0x165
   __TEXT.__objc_stubs: 0x260
   __DATA_CONST.__got: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B6DB795-BBF4-3ACC-8E02-78DB781B4659
+  UUID: DB4D884E-1218-324B-8E93-1810EFEBCC37
   Functions: 105
   Symbols:   283
   CStrings:  162
Symbols:
+ GCC_except_table89
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE9push_backB8ne200100EOS1_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ _objc_release_x26
- GCC_except_table90
- __ZNKSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19CESerializedElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- _objc_release_x25
Functions:
~ _CESerializeWithOptions : 652 -> 604
~ __Z11serializeIdP11objc_objectRNSt3__16vectorI19CESerializedElementNS1_9allocatorIS3_EEEE : 1676 -> 872
~ __ZNKSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev -> __ZNSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE9push_backB8ne200100EOS1_ : 16 -> 264
~ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19CESerializedElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m -> __Z13serializeDictP12NSDictionaryRNSt3__16vectorI19CESerializedElementNS1_9allocatorIS3_EEEE : 56 -> 760
~ __Z13serializeDictP12NSDictionaryRNSt3__16vectorI19CESerializedElementNS1_9allocatorIS3_EEEE -> __ZNSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev : 1564 -> 16

```
