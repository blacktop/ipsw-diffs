## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0x1de38
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__const: 0xdb0
-  __TEXT.__cstring: 0x1185
+1563.0.0.0.0
+  __TEXT.__text: 0x1f13c
+  __TEXT.__const: 0xda8
+  __TEXT.__cstring: 0x138c
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__unwind_info: 0x328
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xd0
-  __AUTH_CONST.__auth_got: 0x288
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
-  __DATA.__data: 0x130
-  __DATA.__bss: 0x67
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x120
   __DATA.__common: 0x2
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libETLDynamic.dylib
   - /usr/lib/libHDLCDynamic.dylib

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 2A88EB75-6174-309C-849B-D5A15370877F
+  UUID: 55F64DFA-B705-302E-BF10-A0E05570DE99
   Functions: 254
   Symbols:   412
-  CStrings:  186
+  CStrings:  200
 
Symbols:
+ __ZNSt12length_errorC1B9noe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9noe220100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9noe220100Ev
+ __ZNSt3__120__throw_length_errorB9noe220100EPKc
+ __ZNSt3__124__put_character_sequenceB9noe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
Functions:
~ _ETLLOGParseLogHeader : 88 -> 148
~ _ETLLOGParseLog : 440 -> 476
~ _ETLDMCLogFilter : 484 -> 516
~ _APPLIB_DIAG_AUDIO_PCM_14Bit_Start_Loopback : 708 -> 748
~ _APPLIB_DIAG_AUDIO_PCM_14Bit_Stop_Loopback : 708 -> 748
~ _APPLIB_DIAG_AUDIO_PCM_16Bit_Start_Loopback : 708 -> 748
~ _APPLIB_DIAG_AUDIO_PCM_16Bit_Stop_Loopback : 708 -> 748
~ _APPLIB_DIAG_AUDIO_I2S_Start_Loopback : 708 -> 748
~ _APPLIB_DIAG_AUDIO_I2S_Stop_Loopback : 708 -> 748
~ _APPLIB_DIAG_AUDIO_PCM_I2S_PASSTHROUGH_Start : 708 -> 748
~ _APPLIB_DIAG_AUDIO_PCM_I2S_PASSTHROUGH_Stop : 708 -> 748
~ _APPLIB_DIAG_AUDIO_I2S_PCM_PASSTHROUGH_Start : 708 -> 748
~ _APPLIB_DIAG_AUDIO_I2S_PCM_PASSTHROUGH_Stop : 708 -> 748
~ _APPLIB_DIAG_SEND_SMS : 712 -> 728
~ _APPLIB_DIAG_ENABLE_MT_SMS_STORE : 392 -> 412
~ __ETLDMCLoadViewFromFile : 1360 -> 1380
~ __ETLDMCParseQTraces : 864 -> 876
~ __ETLDMCParseLogCodesInternal : 1320 -> 880
~ _APPLIB_LOG_DISABLE : 628 -> 672
~ _APPLIB_FTM_LOG_ENABLE : 1752 -> 1960
~ _APPLIB_FTM_LOG_DISABLE : 928 -> 988
~ _APPLIB_LOG_GetIds : 640 -> 684
~ _APPLIB_LOG_GetMasks : 640 -> 684
~ _APPLIB_LOG_SetMasks : 448 -> 468
~ _APPLIB_ParseRDALog : 416 -> 464
~ _APPLIB_DIAG_Unlock : 856 -> 932
~ _APPLIB_DIAG_CreateICCID_EFS_File : 1272 -> 1292
~ _APPLIB_DIAG_GetICCID : 568 -> 588
~ _APPLIB_DIAG_Read_Meid : 372 -> 392
~ _APPLIB_DIAG_Read_Msl : 368 -> 388
~ _APPLIB_DIAG_Read_Otksl : 368 -> 388
~ _APPLIB_DIAG_Read_BlueToothAddr : 372 -> 392
~ _APPLIB_DIAG_Read_WiFi_MAC_Addr : 372 -> 392
~ _APPLIB_DIAG_Read_WiFi_Cal_Data : 372 -> 392
~ _APPLIB_DIAG_Read_USB2ETHERNET_MAC_Addr : 372 -> 392
~ _APPLIB_DIAG_StartProvision : 468 -> 484
~ _APPLIB_DIAG_FinishProvision : 472 -> 488
~ _DetectAndFixSpecialCharacters : 280 -> 296
~ _APPLIB_DIAG_NvItemRead : 376 -> 396
~ _APPLIB_DIAG_NvItemWrite : 404 -> 424
~ _APPLIB_DIAG_FTMNvItemRead : 520 -> 552
~ _APPLIB_DIAG_FTMNvItemWrite : 460 -> 476
~ _APPLIB_DIAG_ModeChange : 476 -> 508
~ _DetectAndStripSpecialCharacters : 248 -> 256
~ _APPLIB_DIAG_SendRawRequest : 472 -> 488
~ _APPLIB_DIAG_SetOneRx : 516 -> 548
~ _APPLIB_DIAG_Get_RSSI_Channel : 520 -> 552
~ _ETLLOGSetMask : 840 -> 848
~ _ETLLOGClearAllMasksWithRetry : 480 -> 496
~ _ETLLOGClearAllEnabledMasksWithRetry : 516 -> 528
~ _ETLEVENTProcessEvent : 696 -> 464
~ _ETLEVENTProcessEventItem : 296 -> 8
~ _ETLEVENTProcessEventItemTSLength : 304 -> 500
~ _ETLEVENTProcessHeader : 60 -> 152
~ _ETLEVENTParseReport : 208 -> 328
~ _ETLEVENTParseEventReport : 464 -> 376
~ _ETLEVENTReportFree : 132 -> 164
~ _ETLQtraceSend : 568 -> 572
~ _ETLQtraceParseResponse : 284 -> 288
~ _ETLDMCUtilCountRangesInMaskArray : 80 -> 84
~ _ETLDMCGetMatchingKeyword : 388 -> 400
~ __Z26ETLDMCDebugGetMessageRangePK26ETLMESSAGESubsystemIDRange : 1044 -> 1052
~ __Z24ETLDMCDebugGetEventRangePK13ETLEVENTRange : 1044 -> 1052
~ __Z26ETLDMCDebugGetMessageMasksP17__ETLDMCHandleTag10ETLDMCView : 1044 -> 1052
~ __Z22ETLDMCDebugGetLogCodesP17__ETLDMCHandleTag10ETLDMCViewb : 1540 -> 1544
~ __Z20ETLDMCDebugGetEventsP17__ETLDMCHandleTag10ETLDMCView : 876 -> 888
~ __Z21ETLDMCDebugGetQtracesP17__ETLDMCHandleTag10ETLDMCView : 1044 -> 1060
~ __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m -> __ZNSt3__124__put_character_sequenceB9noe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m : 824 -> 828
~ _APPLIB_DIAG_GPS_SA_RF_VERIF_MODE_SWITCH : 456 -> 476
~ _APPLIB_DIAG_GPS_GEN8_HW_CONFIG : 924 -> 1000
~ _APPLIB_FTM_GNSS_EXTERNAL_LNA : 764 -> 816
~ _APPLIB_DIAG_GPS_GEN8_StartIQTest : 528 -> 552
~ _APPLIB_DIAG_GPS_GEN8_SV_TRACK : 932 -> 1000
~ _APPLIB_DIAG_MemoryPoke_Byte : 476 -> 492
~ _APPLIB_DIAG_MemoryPoke_Word : 476 -> 492
~ _APPLIB_DIAG_MemoryPoke_DWord : 456 -> 472
~ _APPLIB_DIAG_GPS_SessionControl : 484 -> 500
~ _APPLIB_DIAG_CreateFile : 988 -> 1012
~ _APPLIB_DIAG_GetFileInfo : 988 -> 1012
~ _APPLIB_DIAG_DeleteFile : 988 -> 1012
~ _APPLIB_DIAG_WriteFile : 464 -> 484
~ _APPLIB_DIAG_ReadFile : 1064 -> 1084
~ _APPLIB_DIAG_ReadICCID_EFS_File : 1008 -> 1032
~ _ETLDMCViewLoadMessagesFromMaskArray : 304 -> 336
~ _ETLDMCViewCopyMasksToMaskArray : 252 -> 260
~ _ETLDMCLoadEventRangesFromEventsArray : 224 -> 228
~ _ETLDMCViewFree : 516 -> 520
~ _ETLDMCViewMerge : 2404 -> 2484
~ _ETLDMCViewLoadQTraces : 500 -> 504
~ _APPLIB_DIAG_FTM_SetRFMode : 808 -> 856
~ _APPLIB_DIAG_FTM_SetChannel : 808 -> 856
~ _APPLIB_DIAG_FTM_Tx_On : 620 -> 660
~ _APPLIB_DIAG_FTM_Tx_Off : 620 -> 660
~ _APPLIB_DIAG_FTM_SetWaveForm : 544 -> 580
~ _APPLIB_DIAG_FTM_SetPARange : 804 -> 852
~ _APPLIB_DIAG_FTM_SetPDM : 936 -> 996
~ _APPLIB_DIAG_FTM_ExecuteTxSweep : 720 -> 772
~ _APPLIB_DIAG_FTM_SetPDMStepSize : 720 -> 772
~ _APPLIB_DIAG_FTM_ConfigTxSweep : 1052 -> 1128
~ _APPLIB_DIAG_FTM_GetAllHDETValues : 384 -> 404
~ _APPLIB_DIAG_FTM_GetADCValue : 852 -> 920
~ _APPLIB_DIAG_FTM_SetHDETTracking : 1052 -> 1128
~ _APPLIB_DIAG_FTM_GetRxAGC : 656 -> 704
~ _APPLIB_DIAG_FTM_GetSynthState : 656 -> 704
~ _APPLIB_DIAG_FTM_SetLNARange : 804 -> 852
~ _APPLIB_DIAG_FTM_GetDVGAOffset : 808 -> 856
~ _APPLIB_DIAG_FTM_SetDVGAOffset : 804 -> 852
~ _APPLIB_DIAG_FTM_GetLNAOffset : 1052 -> 1128
~ _APPLIB_DIAG_FTM_SetLNAOffset : 1052 -> 1128
~ _APPLIB_DIAG_FTM_CDMA_API2_CALIBRATE_DVGA : 1032 -> 1128
~ _APPLIB_DIAG_FTM_CDMA_API2_CALIBRATE_LNA : 1308 -> 1452
~ _APPLIB_DIAG_FTM_SecondChainTestCall : 728 -> 780
~ _APPLIB_DIAG_FTM_SetSecondaryChain : 728 -> 780
~ _APPLIB_DIAG_FTM_ChangeFTM_BootMode : 376 -> 396
~ _APPLIB_DIAG_FTM_CDMA_API2_CALIBRATE_IM2 : 896 -> 960
~ _APPLIB_DIAG_FTM_CDMA_API2_CALIBRATE_INTELLICEIVER : 1000 -> 1088
~ _APPLIB_DIAG_FTM_DO_ENH_XO_DC_CAL : 396 -> 416
~ _APPLIB_DIAG_FTM_DO_ENH_XO_FT_CURVE_CAL : 396 -> 416
~ _APPLIB_DIAG_FTM_CDMA2000_PILOT_ACQ : 1732 -> 1940
~ _APPLIB_DIAG_FTM_CDMA2000_DEMOD_SYNC : 760 -> 812
~ _APPLIB_DIAG_FTM_CDMA2000_DEMOD_FCH : 864 -> 884
~ _APPLIB_DIAG_FTM_CDMA2000_MOD_FCH : 832 -> 856
~ _APPLIB_DIAG_FTM_CDMA2000_FTM_FWD_HHO_SC : 1588 -> 1764
~ _APPLIB_DIAG_FTM_CDMA2000_CMD_RELEASE : 756 -> 808
~ _APPLIB_DIAG_FTM_EVDO_PILOT_ACQ : 720 -> 744
~ _APPLIB_DIAG_FTM_EVDO_SYS_TIME_ACQ : 604 -> 640
~ _APPLIB_DIAG_FTM_EVDO_DEMOD_CC_MAC_FTC : 1444 -> 1600
~ _APPLIB_DIAG_FTM_EVDO_MOD_ACC : 1092 -> 1112
~ _APPLIB_DIAG_FTM_EVDO_REV_A_CONF_MAC_FOR_FWD_CC_MAC_FTC : 844 -> 916
~ _APPLIB_DIAG_FTM_EVDO_REV_A_MOD_ACC : 1380 -> 1392
~ _APPLIB_DIAG_FTM_EVDO_REV_A_DEMOD_FWD_WITH_NO_REV : 1700 -> 1884
~ _APPLIB_DIAG_FTM_EVDO_DEMOD_FWD_WITH_NO_REV : 1604 -> 1780
~ _APPLIB_DIAG_FTM_EVDO_REV_A_MOD_TRA : 856 -> 876
~ _APPLIB_DIAG_FTM_EVDO_MOD_REVERSE_TRA : 784 -> 804
~ _APPLIB_DIAG_FTM_EVDO_CMD_RELEASE : 692 -> 744
~ _APPLIB_DIAG_FTM_SetPA_DCDC_Levels : 984 -> 1072
~ _APPLIB_DIAG_FTM_TX_RX_FREQ_CAL_SWEEP : 860 -> 892
~ _APPLIB_DIAG_FTM_TX_RX_FREQ_CAL_SWEEP_PARSE : 448 -> 456
~ _APPLIB_DIAG_Get_TX_Power_Channel : 516 -> 548
~ _APPLIB_DIAG_FTM_CDMA2000_FTM_SET_REVERSE_LINK_POWER : 1340 -> 1464
~ _ETLEVENTSetMask : 564 -> 572
CStrings:
+ "Buffer Length %u for payload not enough for, need %zu\n"
+ "Buffer Length %u not enough, need %zu for full timestamp\n"
+ "Buffer Length %u not enough, need %zu for truncated timestamp\n"
+ "ETLEVENTParseReport"
+ "ETLEVENTProcessEventItemTSLength"
+ "ETLEVENTProcessHeader"
+ "ETLEVENTReportFree"
+ "ETLLOGParseLogHeader"
+ "Failed to process header\n"
+ "Freed %u, count was %u\n"
+ "Length %u\n"
+ "Length %u is greater than buffer size %u\n"
+ "Reading Event %u, length flag %u, timeLength %u, bufferLength %u\n"
+ "Warning: Buffer Length %u is greater than field length %u\n"

```
