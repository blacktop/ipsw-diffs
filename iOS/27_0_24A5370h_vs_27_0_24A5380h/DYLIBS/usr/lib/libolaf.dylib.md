## libolaf.dylib

> `/usr/lib/libolaf.dylib`

```diff

-  __TEXT.__text: 0x252a1c
+  __TEXT.__text: 0x252a78
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x3a268
   __TEXT.__gcc_except_tab: 0x8b70
   __TEXT.__cstring: 0x61511
-  __TEXT.__unwind_info: 0x3420
+  __TEXT.__unwind_info: 0x3418
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x44be8
   __DATA_CONST.__weak_got: 0x8
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ __Z10PERGetBitsP6sCoderh : 432 -> 420
~ __Z13ds_NK_SummaryP9s_GN_Ptrs : 49752 -> 49832
~ __Z61lpp_transaction_process_provide_assistance_data_a_gnss_commonP30T_LASN_GNSS_CommonAssistData_sP16_LPP_TRANSACTION : 6180 -> 6176
~ __Z18GN_AGPS_Set_Eph_ElP14GN_AGPS_Eph_El : 520 -> 512
~ ____ZN4gnss15GnssAdaptDevice17setSuplLocationIdERKNS_9Emergency4Supl10LocationIdENSt3__18functionIFvNS_6ResultEEEE_block_invoke : 8616 -> 8628
~ ____ZN4gnss15GnssAdaptDevice29Ga11_18HandleSuplAsyncEventCBE13e_gnsSUPL_MsgP17u_gnsSUPL_MsgData_block_invoke.152 : 912 -> 896
~ ____ZN4gnss15GnssAdaptDevice29Ga11_18HandleSuplAsyncEventCBE13e_gnsSUPL_MsgP17u_gnsSUPL_MsgData_block_invoke_2.155 : 4480 -> 4472
~ __ZL15PEREncodeCHOICEP6sCoderPK13sASN1TypeInfoPv : 620 -> 604
~ __ZL13PEREncodeOPENP6sCoderPK13sASN1TypeInfoPv : 332 -> 316
~ __ZL15PERDecodeStructP6sCoderPK13sASN1TypeInfoPvP16tVMSOpenTypeList : 5108 -> 5008
~ __ZL23PERDecodePrimBIT_STRINGP6sCoderyP19sPERConstructedInfo : 740 -> 736
~ __ZL29PEREncodeStructRootWithOptDefP6sCoderP15tPEREncBitFieldPK3$_3Pv : 944 -> 920
~ __ZL19PEREncodeStructRootP6sCoderPK3$_3Pv : 412 -> 380
~ __Z16Debug_Log_NonVolbP8s_NV_Ram : 4928 -> 4932
~ __ZNKSt3__111__copy_implclB9fqe220106IP21ASN1T_MeasResultEUTRAS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_ : 252 -> 232
~ __ZNKSt3__111__copy_implclB9fqe220106IP25ASN1T_CellMeasuredResultsS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_ : 212 -> 208
~ __Z16Core_Get_GPS_AlmhiP12s_GPS_BinAlm : 328 -> 324
~ __Z17Core_Get_QZSS_AlmhiP12s_GPS_BinAlm : 340 -> 336
~ __Z19PP_Acq_Ass_Merge_AAP20s_Pre_Positioning_WDP18s_DB_Acq_Aid_TableP12s_DB_SV_AzEl : 2444 -> 2460
~ __Z24plc00_04GetPayloadFieldsP13s_Plc_MsgTypePK14s_Plc_MsgClassPPK11s_Plc_MsgIdP12s_Plc_Status12e_Plc_GnssHW : 252 -> 240
~ __Z18API_Set_Inhib_SVIDPbS_ : 672 -> 688
~ __Z15API_Get_UTC_CorbPd : 724 -> 736
~ __Z16API_Get_Nav_DataP15GN_GPS_Nav_DataP15GN_GPS_Dbg_Data : 10848 -> 10840
~ __Z18G5K_ME_Decode_MeasP10Cyc_bufferP11s_G5K_ME_SD : 8384 -> 8500
~ __Z24Gnm53_43ComposeMeWakeMsgPhtPj15e_Gnm_WakeMELtl : 4968 -> 4976
~ __Z26Gnm53_63UpdatePrimaryLTLNvv : 2328 -> 2336
~ __ZL26Gnm53_65GetUncertfromCounttt : 184 -> 196
~ __Z18gnssOsa_StartTimerPKcjPjPFvPvES2_j : 864 -> 880
~ __Z17gnssOsa_StopTimerPKcjj : 356 -> 352
~ __Z19plc03_06CodecFields20e_Plc_CodecOperationP12s_Plc_BufferPK18s_Plc_PayloadFieldhS1_P12s_Plc_Status : 3488 -> 3480
~ _CUCFGetOpenTypeObject : 1272 -> 1196
~ __ZL15CUCFEqualObjectP6sCoderPK13sASN1TypeInfoPvS4_ : 1644 -> 1628
~ __Z16SDLFinalizeValueP6sCoderPK13sASN1TypeInfoPv : 1016 -> 988
~ __ZL27SDLFinalizeValueStructCompsP6sCoderPK13sASN1TypeInfoPK3$_4yPva : 280 -> 264
~ __ZL20CUCFFreeObjectStructP6sCoderPK13sASN1TypeInfoPv : 392 -> 376
~ __ZL26CUCFEqualObjectStructCompsP6sCoderPK13sASN1TypeInfohPPPvS4_ : 408 -> 400
~ __Z19DD_Assist_GLON_DataiP12s_DB_SV_AzElP16s_DB_SV_Nav_MessP15s_DB_Sys_Status : 2140 -> 2144
~ __Z12VecSortAscR8Pdii : 256 -> 264
~ __Z17GM_Cross_ConstellP16s_SV_Gen_Meas_WDP16s_DB_SV_Nav_Mess : 3020 -> 3004
~ __Z17GenericIsAssignedPvPK13tSDLTypeInfoS : 432 -> 436
~ __Z18GM_Get_Best_SyncSVPK11s_Chan_MeasPK13s_Chan_StatusPK9s_Acq_AidhjPiS8_ : 1028 -> 1040
~ __Z15NK_Set_AccuracyjPhP15s_Nav_Kalman_SDP15s_Nav_Kalman_WD : 2364 -> 2360
~ __Z20G5K_ME_Poll_New_MeasP11s_G5K_ME_SDP15s_DB_Sys_StatusP13s_DB_BB_TTickP13s_DB_Raw_MeasP17s_DB_SV_SubframesPb : 4920 -> 4952
~ __Z16GncP_GetMeasDatajP17s_GncP_MeasUpdateb : 1536 -> 1540
~ __ZL26DD_Proc_Eph_Bit_ValidationhhPKjtP16s_DB_SV_Nav_Mess : 208 -> 200
~ ____ZN4gnss15GnssAdaptDevice29startEmergencyPositionRequestERKNS_9Emergency6Cplane15PositionRequestERKNS2_7ContextENSt3__18functionIFvNS_6ResultEEEE_block_invoke : 9372 -> 9388
~ __ZN4gnss15GnssAdaptDevice31Ga10_05SendSessionSummaryReportEjb18e_gnsPPDU_SessCode : 4232 -> 4216
~ __ZN4gnss15GnssAdaptDevice29Ga10_01SendMeasurementsReportEPK15s_gnsCP_MeasRes : 7800 -> 7812
~ __ZN4gnss15GnssAdaptDevice19Ga11_23GetCPSessionEjRNS_18AgnssSummaryReportE : 624 -> 616
~ ____ZN4gnss15GnssAdaptDevice32Ga10_00HandleGnsCpStatusResponseE15e_gnsCP_MsgTypeP15u_gnsCP_MsgData_block_invoke_2.201 : 7820 -> 7804
~ ____ZN4gnss15GnssAdaptDevice32Ga10_00HandleGnsCpStatusResponseE15e_gnsCP_MsgTypeP15u_gnsCP_MsgData_block_invoke_3.203 : 2188 -> 2184
~ __ZN12SuplInitRecd15ProcessSuplInitEjRK13UtaLcsExtData : 2056 -> 2052
~ __Z19lsim12_01StartTimerPFvj14e_lsimtmr_TypeEjjS_ : 988 -> 1132
~ __Z18lsim12_02StopTimerj14e_lsimtmr_Type : 1308 -> 1344
~ __Z20lsim12_05TimerExpiryP11t_MsgHeader : 1472 -> 1516
~ __ZL20DD_Proc_GAL_INAV_GSThPKtbPiS1_PbP14s_DB_Time_Sync : 644 -> 672
~ __Z17AgpsFsmStartTimerjj : 1240 -> 1252
~ __Z17DD_Proc_QZSS_DataP19s_SV_Data_Decode_SDP19s_SV_Data_Decode_WDP15s_DB_Sys_StatusP14s_DB_Time_SyncPiP16s_DB_SV_Nav_Mess : 3476 -> 3472
~ __Z39Get_UTC_Leap_Second_For_GLON_Day_4yrBlkiid : 224 -> 236
~ __Z20GncS04_72SendUpdatesb : 9664 -> 9680
~ __Z18DD_Assist_GPS_DataP19s_SV_Data_Decode_SDiP12s_DB_SV_AzElP16s_DB_SV_Nav_MessP15s_DB_Sys_Status : 2416 -> 2388
~ __Z11KFP_runMeasP12KFP_StateObjP4MeasP14Sen_Aug_FPE_WD : 4904 -> 4864
~ __Z21NK_Crude_Apx_Pos_CorePA3_iPhPA3_sS1_P7EPH_ALMPiPsPd : 14156 -> 14120
~ __ZL17DD_Submit_WeekNumhsPK16s_DB_SV_Nav_MessPA3_A8_jP14s_DB_Time_Sync : 488 -> 516
~ __ZL17DD_Submit_WeekNumhsPK16s_DB_SV_Nav_MessPA3_A8_jP14s_DB_Time_Sync : 488 -> 516
CStrings:
+ "Jun 23 2026"
- "Jun 12 2026"

```
