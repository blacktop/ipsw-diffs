## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/Versions/A/IOMobileFramebuffer`

```diff

-  __TEXT.__text: 0x3b620
-  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__text: 0x3b0e8
+  __TEXT.__gcc_except_tab: 0x228
   __TEXT.__const: 0x1b04
-  __TEXT.__cstring: 0x95b5
+  __TEXT.__cstring: 0x9604
   __TEXT.__unwind_info: 0x888
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0xae0
+  __AUTH_CONST.__cfstring: 0xb00
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__auth_got: 0x430
   __DATA.__data: 0x24

   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 918
-  Symbols:   1234
-  CStrings:  1033
+  Functions: 919
+  Symbols:   1235
+  CStrings:  1036
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ _OUTLINED_FUNCTION_40
Functions:
~ _iomfb_timing_supports_external_sync_vrr : 192 -> 260
~ __ZN22DisplayDataBlockParser12process_bcalEPNS_12Block_HeaderE : 1264 -> 1228
~ __ZN22DisplayDataBlockParser12process_blahEPNS_12Block_HeaderE : 2460 -> 2432
~ __ZN22DisplayDataBlockParser12process_psfaEPNS_12Block_HeaderE : 816 -> 804
~ __ZN22DisplayDataBlockParser12process_qetcEPNS_12Block_HeaderE : 624 -> 600
~ __ZN22DisplayDataBlockParser12process_psfmEPNS_12Block_HeaderE : 836 -> 824
~ __ZN22DisplayDataBlockParser12process_rxtkEPNS_12Block_HeaderE : 2220 -> 2172
~ __ZN22DisplayDataBlockParser12process_upclEPNS_12Block_HeaderE : 364 -> 356
~ __ZN22DisplayDataBlockParser12process_llmtEPNS_12Block_HeaderE : 392 -> 360
~ __ZN22DisplayDataBlockParser19process_ptuc_paramsEPNS_12Block_HeaderEjb : 2824 -> 2672
~ __ZN22DisplayDataBlockParser12process_ubclEPNS_12Block_HeaderE : 796 -> 724
~ __ZN22DisplayDataBlockParser12process_dbclEPNS_12Block_HeaderE : 856 -> 812
~ __ZN22DisplayDataBlockParser12process_uftgEPNS_12Block_HeaderE : 652 -> 636
~ __ZN22DisplayDataBlockParser12process_btpbEPNS_12Block_HeaderE : 580 -> 560
~ __ZN22DisplayDataBlockParser12process_bthbEPNS_12Block_HeaderE : 560 -> 516
~ __ZN22DisplayDataBlockParser15process_lcod_v3EPNS_12Block_HeaderE : 1960 -> 1932
~ __ZN22DisplayDataBlockParser15process_lcod_v4EPNS_12Block_HeaderE : 1800 -> 1776
~ __ZN22DisplayDataBlockParser18process_pdc_cal_v5EPNS_12Block_HeaderEjb : 2416 -> 2296
~ __ZN22DisplayDataBlockParser19setup_pdc_rr_configEv : 100 -> 176
~ __ZN22DisplayDataBlockParser14process_prc_v4EPNS_12Block_HeaderE : 1416 -> 1396
~ __ZN22DisplayDataBlockParser15process_emmk_v3EPNS_12Block_HeaderE : 1260 -> 1228
~ __ZN22DisplayDataBlockParser15process_pdcc_v1EPNS_12Block_HeaderE : 1040 -> 968
~ __ZN22DisplayDataBlockParser15process_emmp_v2EPNS_12Block_HeaderE : 1092 -> 1052
~ __ZN22DisplayDataBlockParser15process_cnst_v8EPNS_12Block_HeaderE : 1568 -> 1576
~ __ZN22DisplayDataBlockParser15process_rcfg_v4EPNS_12Block_HeaderE : 1228 -> 1216
~ __ZN22DisplayDataBlockParser15process_htmp_v5EPNS_12Block_HeaderE : 1768 -> 1776
~ __ZN22DisplayDataBlockParser14process_pcs_v3EPNS_12Block_HeaderE : 1776 -> 1744
~ __ZN22DisplayDataBlockParser15process_emmp_v4EPNS_12Block_HeaderE : 1928 -> 1908
~ __ZN22DisplayDataBlockParser15process_sens_v1EPNS_12Block_HeaderE : 732 -> 716
~ __ZN22DisplayDataBlockParser16process_rtplc_v1EPNS_12Block_HeaderEP14IOMFBRTPLCData : 860 -> 808
~ __ZN22DisplayDataBlockParser15process_splx_v1EPNS_12Block_HeaderEP13IOMFBSPLXData : 380 -> 312
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI17IOMFBEMMPConfigV1EPPS3_EEvT1_S8_T0_ : 232 -> 216
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI17IOMFBEMMPConfigV1EPPS3_EEvT1_S8_T0_ : 236 -> 232
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPP17IOMFBEMMPConfigV1R16temp_bright_sortIS2_EEENS_4pairIT0_bEES9_S9_T1_ : 496 -> 504
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI17IOMFBEMMPConfigV1EPPS3_EEbT1_S8_T0_ : 1320 -> 1296
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSGSCConfigV1EPPS3_EEvT1_S8_T0_ : 228 -> 212
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSGSCConfigV1EPPS3_EEvT1_S8_T0_ : 232 -> 228
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPP20IOMFBACSSGSCConfigV1R16temp_bright_sortIS2_EEENS_4pairIT0_bEES9_S9_T1_ : 492 -> 500
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSGSCConfigV1EPPS3_EEbT1_S8_T0_ : 1260 -> 1236
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI21IOMFBACSSEMMKConfigV1EPPS3_EEvT1_S8_T0_ : 216 -> 200
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI21IOMFBACSSEMMKConfigV1EPPS3_EEvT1_S8_T0_ : 220 -> 216
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPP21IOMFBACSSEMMKConfigV1R16temp_bright_sortIS2_EEENS_4pairIT0_bEES9_S9_T1_ : 448 -> 456
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI21IOMFBACSSEMMKConfigV1EPPS3_EEbT1_S8_T0_ : 1176 -> 1152
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSPCSConfigV1EPPS3_EEvT1_S8_T0_ : 216 -> 200
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSPCSConfigV1EPPS3_EEvT1_S8_T0_ : 220 -> 216
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPP20IOMFBACSSPCSConfigV1R16temp_bright_sortIS2_EEENS_4pairIT0_bEES9_S9_T1_ : 448 -> 456
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSPCSConfigV1EPPS3_EEbT1_S8_T0_ : 1176 -> 1152
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERZ9sort_binsIiENS_6vectorIjNS_9allocatorIjEEEERKNS3_IT_NS4_IS7_EEEEEUljjE_NS_11__wrap_iterIPjEEEEvT1_SH_T0_ : 196 -> 188
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZ9sort_binsIiENS_6vectorIjNS_9allocatorIjEEEERKNS3_IT_NS4_IS7_EEEEEUljjE_NS_11__wrap_iterIPjEEEEvT1_SH_SH_OT0_NS_15iterator_traitsISH_E15difference_typeESM_PNSL_10value_typeEl : 588 -> 560
~ __ZNSt3__120__half_inplace_mergeB9fqe220106INS_17_ClassicAlgPolicyENS_8__invertIRZ9sort_binsIiENS_6vectorIjNS_9allocatorIjEEEERKNS4_IT_NS5_IS8_EEEEEUljjE_EENS_16reverse_iteratorIPjEESI_NSG_INS_11__wrap_iterISH_EEEESL_SL_EEvT1_T2_T3_T4_T5_OT0_ : 156 -> 144
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSPCSConfigV2EPPS3_EEvT1_S8_T0_ : 216 -> 200
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSPCSConfigV2EPPS3_EEvT1_S8_T0_ : 220 -> 216
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPP20IOMFBACSSPCSConfigV2R16temp_bright_sortIS2_EEENS_4pairIT0_bEES9_S9_T1_ : 448 -> 456
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI20IOMFBACSSPCSConfigV2EPPS3_EEbT1_S8_T0_ : 1176 -> 1152
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI17IOMFBEMMPConfigV2EPPS3_EEvT1_S8_T0_ : 232 -> 216
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI17IOMFBEMMPConfigV2EPPS3_EEvT1_S8_T0_ : 236 -> 232
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPP17IOMFBEMMPConfigV2R16temp_bright_sortIS2_EEENS_4pairIT0_bEES9_S9_T1_ : 496 -> 504
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyER16temp_bright_sortI17IOMFBEMMPConfigV2EPPS3_EEbT1_S8_T0_ : 1320 -> 1296
~ _OUTLINED_FUNCTION_13 : 16 -> 40
~ _OUTLINED_FUNCTION_14 : 12 -> 16
~ _OUTLINED_FUNCTION_19 : 16 -> 12
~ _OUTLINED_FUNCTION_22 : 12 -> 16
~ _OUTLINED_FUNCTION_23 : 28 -> 12
~ _OUTLINED_FUNCTION_30 : 20 -> 28
~ _OUTLINED_FUNCTION_31 : 12 -> 20
~ _OUTLINED_FUNCTION_36 : 20 -> 12
~ _OUTLINED_FUNCTION_37 : 12 -> 20
~ _OUTLINED_FUNCTION_38 : 32 -> 12
+ _OUTLINED_FUNCTION_40
~ _IOMobileFramebufferSwapActiveRegion : 244 -> 228
~ _InfoKeyInitialize : 432 -> 436
~ _kern_SwapSubtitleRegion : 156 -> 160
~ _IOMobileFramebufferOpenByName : 1552 -> 1560
~ _IOMobileFramebufferGetWirelessSurfaceWithOptions : 376 -> 396
~ _core_analytics_send_data : 748 -> 796
~ _virt_SwapEnd : 628 -> 636
~ _virt_SwapCancel : 260 -> 268
~ __ZN22DisplayDataBlockParser18setup_prox_binningEPNS_19Prox_Binning_ConfigEjPK10__CFString : 336 -> 344
~ __ZN22DisplayDataBlockParser18process_pdc_cal_v6EPNS_12Block_HeaderE : 1636 -> 1620
~ __ZN22DisplayDataBlockParser20process_pdc_param_v5EPNS_12Block_HeaderE : 1004 -> 1016
~ __ZN22DisplayDataBlockParser20process_pdc_param_v6EPNS_12Block_HeaderE : 1556 -> 1512
~ __ZN22DisplayDataBlockParser24process_irdc_device_dataEPNS_12Block_HeaderE : 392 -> 396
~ __ZN22DisplayDataBlockParser12process_prcwEPNS_12Block_HeaderEP11IOMFBCAData : 424 -> 380
~ __ZN22DisplayDataBlockParser15process_benl_v2EPNS_12Block_HeaderE : 716 -> 684
~ _ZN22DisplayDataBlockParser12process_bltsEPNS_12Block_HeaderE.cold.1 : 712 -> 572
~ _ZN22DisplayDataBlockParser12process_rdlcEPNS_12Block_HeaderE.cold.1 : 300 -> 280
CStrings:
+ "Parser i: PDC RR inheriting NR bin interp: bin_low=%u t=%g\n"
+ "vblank_duration_us"

```
