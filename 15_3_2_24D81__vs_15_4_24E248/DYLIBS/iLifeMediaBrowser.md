## iLifeMediaBrowser

> `/System/Library/PrivateFrameworks/iLifeMediaBrowser.framework/Versions/A/iLifeMediaBrowser`

```diff

-806.1.0.0.0
-  __TEXT.__text: 0x47a78
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x525c
+806.2.0.0.0
+  __TEXT.__text: 0x47b88
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__objc_methlist: 0x5aec
   __TEXT.__const: 0x380
-  __TEXT.__gcc_except_tab: 0x10ac
+  __TEXT.__gcc_except_tab: 0xe88
   __TEXT.__cstring: 0x65b0
   __TEXT.__oslogstring: 0x65
-  __TEXT.__unwind_info: 0x17c0
+  __TEXT.__unwind_info: 0x1778
   __TEXT.__objc_classname: 0x905
   __TEXT.__objc_methname: 0xd7cf
   __TEXT.__objc_methtype: 0x2259

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e28
+  __DATA_CONST.__objc_selrefs: 0x4200
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__auth_got: 0x750
   __AUTH_CONST.__const: 0x470
   __AUTH_CONST.__cfstring: 0x81e0
-  __AUTH_CONST.__objc_const: 0x80d0
+  __AUTH_CONST.__objc_const: 0x7078
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x16f8
   __DATA.__objc_ivar: 0x648

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36B6CF21-A805-3A58-BC51-F9CCF1E580E7
-  Functions: 1861
-  Symbols:   5566
+  UUID: A3A9FD1D-468A-3798-8CE3-AF954D0C0821
+  Functions: 1858
+  Symbols:   5562
   CStrings:  4996
 
Symbols:
+ +[ILMediaBrowserPreviewView _notificationsToObserve].cold.1
+ -[ILMediaBrowserPreviewView _observeAtEndNotifications:].cold.1
+ -[ILMediaObject setURL:].cold.1
+ GCC_except_table1
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP17ILMBPMRInstrumentNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP17ILMBPMRInstrumentEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__1rsB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ _memcpy
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP17ILMBPMRInstrumentNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__116__pad_and_outputB8ne180100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP17ILMBPMRInstrumentEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__1rsB8ne180100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
- __ZSt28__throw_bad_array_new_lengthB8ne180100v

```
