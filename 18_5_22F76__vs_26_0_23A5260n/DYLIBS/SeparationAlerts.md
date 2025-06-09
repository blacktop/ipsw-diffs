## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-107.0.3.0.0
-  __TEXT.__text: 0x2e7e0
-  __TEXT.__auth_stubs: 0x650
+107.0.6.0.0
+  __TEXT.__text: 0x2e818
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_methlist: 0x371c
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x152e
-  __TEXT.__oslogstring: 0x6b00
-  __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__oslogstring: 0x6a0c
+  __TEXT.__gcc_except_tab: 0x24c
+  __TEXT.__unwind_info: 0x7c8
   __TEXT.__objc_classname: 0x5c5
   __TEXT.__objc_methname: 0x8d48
   __TEXT.__objc_methtype: 0x112a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d80
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x20e0
   __AUTH_CONST.__objc_const: 0x52d8
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0x41c
   __DATA.__data: 0xba0
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 932D4756-E728-3A3C-9485-C2C141912F66
-  Functions: 999
-  Symbols:   3720
-  CStrings:  2454
+  UUID: 81AD78DF-4EF8-33AA-A355-1A14C34676BA
+  Functions: 1000
+  Symbols:   3721
+  CStrings:  2452
 
Symbols:
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table42
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE9push_backB8ne200100ERU8__strongKS2_
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
- GCC_except_table35
- GCC_except_table40
- __ZNKSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE9push_backB8ne190102ERU8__strongKS2_
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- _memcpy
CStrings:
+ "{\"msg%{public}.0s\":\"#sa #withyou no more tracked devices to find while long scan is ongoing, requesting to stop long aggressive scan\"}"
- "{\"msg%{public}.0s\":\"#sa #withyou no more devices to find, recording time of last device found for metrics\"}"
- "{\"msg%{public}.0s\":\"#sa #withyou no more sa enabled devices to find while long scan is ongoing, requesting to stop long aggressive scan\"}"
- "{\"msg%{public}.0s\":\"#sa #withyou some remaining sa enabled devices to find, requesting long aggressive scan if not already ongoing\"}"

```
