## libindus.dylib

> `/usr/lib/libindus.dylib`

```diff

-219.0.0.0.0
-  __TEXT.__text: 0x14eef0
+221.0.0.0.0
+  __TEXT.__text: 0x14f0bc
   __TEXT.__const: 0x5540
-  __TEXT.__gcc_except_tab: 0x492c
-  __TEXT.__cstring: 0x2957f
+  __TEXT.__gcc_except_tab: 0x4928
+  __TEXT.__cstring: 0x296d0
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x2720
+  __TEXT.__unwind_info: 0x2728
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__weak_got: 0x8

   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__auth_got: 0x438
   __AUTH.__data: 0x3f8
-  __DATA.__data: 0x3b5e0
+  __DATA.__data: 0x3b5f0
   __DATA.__common: 0x5dcd1
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1898
-  Symbols:   2648
-  CStrings:  4079
+  Functions: 1900
+  Symbols:   2650
+  CStrings:  4083
 
Symbols:
+ __ZNSt3__112construct_atB9fqe220106IN4gnss6SvInfoEJS2_EPS2_EEPT_S5_DpOT0_
+ __ZNSt3__16vectorIN4gnss6SvInfoENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
Functions:
~ __Z30Hal_GetMEAnalyticsDataResponsePht : 2336 -> 2360
~ ____ZL22Hal_LogMEAnalyticsDataPht_block_invoke : 1180 -> 1252
~ __Z23GN_ABDS_Set_CNAV_Eph_ElP19GN_ABDS_CNAV_Eph_El : 2300 -> 2292
~ __Z16GN_ABDS_Set_BGTObP12GN_ABDS_BGTO : 456 -> 452
~ __Z23NK_LOS_Est_Comp_SV_PLOS10e_CTXT_SESPK15s_DB_Track_MeasP15s_Nav_Kalman_SDP15s_Nav_Kalman_WD : 2668 -> 2704
~ __Z15NK_Get_Ext_MeasjjPK15s_DB_Sys_StatusP15s_Nav_Kalman_WDP15s_Nav_Kalman_SDP15s_Process_Noise : 5948 -> 5952
~ __Z17Nav_Kalman_UpdateP15s_Nav_Kalman_SDP15s_Nav_Kalman_WDP17s_GNSS_Debug_DataP15s_DB_Track_MeasP12s_DB_SV_AzElP19s_DB_SV_State_TableP16s_DB_SV_Nav_MessP18s_DB_Acq_Aid_TableP15s_DB_ROF_AssistP13s_DB_Nav_SolnP15s_DB_Sys_StatusP15s_DB_Chan_ResetP14s_DB_Time_Sync : 20276 -> 20260
~ __Z16NK_Tunnel_AssistP15s_Nav_Kalman_SDP15s_Nav_Kalman_WD : 604 -> 608
~ ____ZN4gnss15GnssAdaptDevice17Ga06_01ReportPvtmE11e_Gnm_Error16s_Gnm_AppNavData_block_invoke.16 : 15136 -> 14844
~ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIN4gnss6SvInfoEEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m : 136 -> 144
~ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220106INS_9allocatorIN4gnss6SvInfoEEEPS3_EEvRT_T0_S8_S8_ : 252 -> 160
+ __ZNSt3__112construct_atB9fqe220106IN4gnss6SvInfoEJS2_EPS2_EEPT_S5_DpOT0_
+ __ZNSt3__16vectorIN4gnss6SvInfoENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
~ __Z13NK_Map_VectorP15s_Nav_Kalman_WDP15s_Nav_Kalman_SDP13s_DB_Nav_Soln : 4260 -> 4272
~ __Z17Hal11_HandleEventhPht : 1644 -> 1828
~ __Z22EE_Get_BDS_CNAV_IntEphhiP12s_BDS_IntEph : 2684 -> 2676
~ __Z20GNSS_Clear_DataAreasv : 9244 -> 9260
CStrings:
+ "%10u %s%c %s: L5_L1_Tuner_Stats_event: METTick %u, L5_Best %2.1f, L5_Normal %2.1f, L5_Worst %2.1f, L5_SubOptimal %2.1f, L1_Best %2.1f, L1_Normal %2.1f, L1_Worst %2.1f, L1_SubOptimal %2.1f\n"
+ "%10u %s%c %s: ME_Analytics METTickMs %u-%u: L5_Best,%u,L5_Normal,%u,L5_Worst,%u,L5_SubOptimal,%u,L1_Best,%u,L1_Normal,%u,L1_Worst,%u,L1_SubOptimal,%u\n"
+ "GN_ABDS_Set_BGTO: FAILED: A0 = %d < -2^15 or >= 2^15, Out of range!"
+ "GN_ABDS_Set_BGTO: FAILED: A1 = %d < -2^12 or >= 2^12, Out of range!"
+ "GN_ABDS_Set_CNAV_Eph_El: FAILED: ISC_B1C_d = %d <-2^11 or >=2^11, Out of range!"
+ "GN_ABDS_Set_CNAV_Eph_El: FAILED: ISC_B2a_d = %d <-2^11 or >=2^11, Out of range!"
+ "GN_ABDS_Set_CNAV_Eph_El: FAILED: TGD_B1C_p = %d <-2^11 or >=2^11, Out of range!"
+ "GN_ABDS_Set_CNAV_Eph_El: FAILED: TGD_B2a_p = %d <-2^11 or >=2^11, Out of range!"
+ "GN_ABDS_Set_CNAV_Eph_El: FAILED: dN = %d <-2^16 or >=2^16, Out of range!"
+ "GN_AGLON_Set_Eph_El: FAILED: gloTau = %d <-2^21 or >=2^21, Out of range!"
+ "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: ISC_B1C_d = %d <-2^11 or >=2^11, Out of range!"
+ "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: ISC_B2a_d = %d <-2^11 or >=2^11, Out of range!"
+ "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: TGD_B1C_p = %d <-2^11 or >=2^11, Out of range!"
+ "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: TGD_B2a_p = %d <-2^11 or >=2^11, Out of range!"
+ "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: dN = %d <-2^16 or >=2^16, Out of range!"
+ "L1BestDurationPercentage"
+ "L1NormalDurationPercentage"
+ "L1SubOptimalDurationPercentage"
+ "L1WorstDurationPercentage"
+ "L5SubOptimalDurationPercentage"
+ "v2.216.2.2026-09-01"
- "%10u %s%c %s: ME_Analytics METTickMs %u-%u: L5_Best,%u,L5_Normal,%u,L5_Worst,%u,L5_Unknown,%u\n"
- "GN_ABDS_Set_BGTO: FAILED: A0 = %d < -2^16 or >= 2^16, Out of range!"
- "GN_ABDS_Set_BGTO: FAILED: A1 = %d < -2^13 or >= 2^13, Out of range!"
- "GN_ABDS_Set_CNAV_Eph_El: FAILED: ISC_B1C_d = %d <-2^10 or >=2^10, Out of range!"
- "GN_ABDS_Set_CNAV_Eph_El: FAILED: ISC_B2a_d = %d <-2^10 or >=2^10, Out of range!"
- "GN_ABDS_Set_CNAV_Eph_El: FAILED: TGD_B1C_p = %d <-2^10 or >=2^10, Out of range!"
- "GN_ABDS_Set_CNAV_Eph_El: FAILED: TGD_B2a_p = %d <-2^10 or >=2^10, Out of range!"
- "GN_ABDS_Set_CNAV_Eph_El: FAILED: dN = %d <-2^25 or >=2^25, Out of range!"
- "GN_AGLON_Set_Eph_El: FAILED: gloDeltaTau = %d <-2^21 or >=2^21, Out of range!"
- "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: ISC_B1C_d = %d <-2^10 or >=2^10, Out of range!"
- "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: ISC_B2a_d = %d <-2^10 or >=2^10, Out of range!"
- "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: TGD_B1C_p = %d <-2^10 or >=2^10, Out of range!"
- "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: TGD_B2a_p = %d <-2^10 or >=2^10, Out of range!"
- "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: dN = %d <-2^25 or >=2^25, Out of range!"
- "L5UnknownDurationPercentage"
- "L5statepercent"
- "v2.215.1.2026-07-16"
```
