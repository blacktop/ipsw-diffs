## libFontWorkerAccess.dylib

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontWorkerAccess.dylib`

```diff

-387.0.0.0.0
-  __TEXT.__text: 0xdc24
+391.0.0.0.0
+  __TEXT.__text: 0xdc08
   __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__gcc_except_tab: 0xc78
-  __TEXT.__cstring: 0xa25
+  __TEXT.__objc_methlist: 0x128
+  __TEXT.__gcc_except_tab: 0xc7c
+  __TEXT.__cstring: 0xa23
   __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__unwind_info: 0x8f0
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methname: 0x6a7
   __TEXT.__objc_methtype: 0x230

   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0x638
   __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x1e8
+  __AUTH_CONST.__objc_const: 0x120
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x138

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1241228E-79C4-3310-93E9-987FF0BB7A56
-  Functions: 403
-  Symbols:   999
-  CStrings:  268
+  UUID: 9C6E277E-D309-3BC7-8754-3454FEF9B662
+  Functions: 412
+  Symbols:   1012
+  CStrings:  267
 
Symbols:
+ -[TFontWorkerClient initWithServiceName:].cold.1
+ _OUTLINED_FUNCTION_0
+ _Z5XTLogiPK10__CFStringz.cold.1
+ _ZN11TFontWorker19GetFontWorkerClientEv.cold.1
+ _ZN14TATSFontWorker22GetATSFontWorkerClientEv.cold.1
+ _ZN15TSessionManager22IsInstallerEnvironmentEv.cold.1
+ _ZN15TSessionManager25GetFontAssetDirectoryPathEv.cold.1
+ _ZN15TSessionManager29GetInstallationKindForFontURLEPK7__CFURL.cold.1
+ _ZN15TSessionManager29GetInstallationKindForFontURLEPK7__CFURL.cold.2
+ _ZN16TCFStringUniquer16GetStringUniquerEv.cold.1
+ _ZN16TCFStringUniquerC1Ev.cold.1
+ _ZN16TCFStringUniquerC2Ev.cold.1
+ _ZN9TCFNumber17CreateFromBooleanEb.cold.1
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102I16CFArray_iteratorIPKvES7_35CFMutableArray_back_insert_iteratorIS6_EEENS_4pairIT_T1_EESB_T0_SC_
+ __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__113__equal_rangeB8ne190102INS_17_ClassicAlgPolicyER20TCFComparatorFunctorILln1EE16CFArray_iteratorIPK10__CFStringES9_PKvNS_10__identityEEENS_4pairIT1_SE_EESE_T2_RKT3_OT0_OT4_
+ __ZNSt3__113__upper_boundB8ne190102INS_17_ClassicAlgPolicyER20TCFComparatorFunctorILln1EE16CFArray_iteratorIPK10__CFStringES9_PKvRNS_10__identityEEET1_SE_T2_RKT3_OT0_OT4_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__123__lower_bound_bisectingB8ne190102INS_17_ClassicAlgPolicyE16CFArray_iteratorIPK10__CFStringEPKvNS_10__identityE20TCFComparatorFunctorILln1EEEET0_SC_RKT1_NS_15iterator_traitsISC_E15difference_typeERT3_RT2_
+ __ZNSt3__17__mergeB8ne190102IR20TCFComparatorFunctorILln1EE16CFArray_iteratorIPKvES7_35CFMutableArray_back_insert_iteratorIS6_EEET2_T0_SB_T1_SC_SA_T_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100I16CFArray_iteratorIPKvES7_35CFMutableArray_back_insert_iteratorIS6_EEENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__equal_rangeB8ne180100INS_17_ClassicAlgPolicyER20TCFComparatorFunctorILln1EE16CFArray_iteratorIPK10__CFStringES9_PKvNS_10__identityEEENS_4pairIT1_SE_EESE_T2_RKT3_OT0_OT4_
- __ZNSt3__113__lower_boundB8ne180100INS_17_ClassicAlgPolicyE16CFArray_iteratorIPK10__CFStringES6_PKvNS_10__identityE20TCFComparatorFunctorILln1EEEET0_SC_T1_RKT2_RT4_RT3_
- __ZNSt3__113__upper_boundB8ne180100INS_17_ClassicAlgPolicyER20TCFComparatorFunctorILln1EE16CFArray_iteratorIPK10__CFStringES9_PKvRNS_10__identityEEET1_SE_T2_RKT3_OT0_OT4_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__17__mergeB8ne180100IR20TCFComparatorFunctorILln1EE16CFArray_iteratorIPKvES7_35CFMutableArray_back_insert_iteratorIS6_EEET2_T0_SB_T1_SC_SA_T_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
CStrings:
- "1"

```
