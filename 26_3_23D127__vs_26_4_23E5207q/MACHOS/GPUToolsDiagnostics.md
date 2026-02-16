## GPUToolsDiagnostics

> `/System/Library/PrivateFrameworks/GPUToolsDiagnostics.framework/GPUToolsDiagnostics`

```diff

-313.2.0.0.0
-  __TEXT.__text: 0xacf4
-  __TEXT.__auth_stubs: 0x4c0
+314.9.0.0.0
+  __TEXT.__text: 0xaf74
+  __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_stubs: 0xc00
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x1434
-  __TEXT.__cstring: 0x234c
+  __TEXT.__gcc_except_tab: 0x1440
+  __TEXT.__cstring: 0x247f
   __TEXT.__objc_methname: 0x101f
   __TEXT.__objc_classname: 0x6c
   __TEXT.__objc_methtype: 0x1de
   __TEXT.__oslogstring: 0x79
   __TEXT.__unwind_info: 0x4e0
-  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E20A4571-9CBE-3250-B655-863C156276DB
-  Functions: 112
-  Symbols:   468
-  CStrings:  453
+  UUID: 901C6860-DEA0-30B8-A4E0-E7BD91B9ED6C
+  Functions: 111
+  Symbols:   465
+  CStrings:  454
 
Symbols:
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table23
+ GCC_except_table25
+ GCC_except_table29
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_6vectorImNS_9allocatorImEEEEEENS_22__unordered_map_hasherImNS_4pairIKmS5_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImSA_SE_SC_Lb1EEENS3_ISA_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_6vectorImNS_9allocatorImEEEEEENS_22__unordered_map_hasherImNS_4pairIKmS5_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImSA_SE_SC_Lb1EEENS3_ISA_EEED2Ev
+ __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorIPiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_6vectorImNS1_ImEEEEEEPvEEEEEclB9fon210106EPS9_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIN8GPUTools4Diag9CallstackENS_9allocatorIS3_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9fon210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9fon210106v
+ _objc_retain_x27
+ _objc_retain_x28
- GCC_except_table102
- GCC_except_table106
- GCC_except_table111
- GCC_except_table24
- GCC_except_table27
- GCC_except_table99
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_6vectorImNS_9allocatorImEEEEEENS_22__unordered_map_hasherImS6_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SB_S9_Lb1EEENS3_IS6_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_6vectorImNS_9allocatorImEEEEEENS_22__unordered_map_hasherImS6_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SB_S9_Lb1EEENS3_IS6_EEED2Ev
- __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_6vectorImNS1_ImEEEEEEPvEEEEEclB8nn200100EPS9_
- __ZNSt3__16vectorIN8GPUTools4Diag9CallstackENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8nn200100Ev
- __ZSt28__throw_bad_array_new_lengthB8nn200100v
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x4
- _objc_storeStrong
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9TugDK7NeNFXlDCJk5oGYOjZm0YEVbHWxHTo4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
