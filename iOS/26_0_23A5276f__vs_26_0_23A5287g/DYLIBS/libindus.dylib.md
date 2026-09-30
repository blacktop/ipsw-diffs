## libindus.dylib

> `/usr/lib/libindus.dylib`

```diff

-92.0.0.0.0
-  __TEXT.__text: 0x13ecbc
-  __TEXT.__auth_stubs: 0x850
+93.0.0.0.0
+  __TEXT.__text: 0x13f144
+  __TEXT.__auth_stubs: 0x860
   __TEXT.__const: 0x4c70
   __TEXT.__gcc_except_tab: 0x4bf8
-  __TEXT.__cstring: 0x26be6
+  __TEXT.__cstring: 0x26dbd
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x1ca8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x528
-  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__const: 0x1d28
   __AUTH_CONST.__cfstring: 0x20
   __AUTH.__data: 0x3f8
   __DATA.__data: 0x28698
+  __DATA.__common: 0x680b1
   __DATA.__bss: 0x83d0
-  __DATA.__common: 0x68079
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 153653B0-459A-369F-B221-1E1855A2A035
+  UUID: 7874BCAE-2620-3543-8681-29366A1ED292
   Functions: 1756
-  Symbols:   5265
-  CStrings:  4010
+  Symbols:   5270
+  CStrings:  4023
 
Symbols:
+ __Z26Ga05_IsReceivingFTAEnabledv
+ __ZL18g_ReportingFTAData.3
+ __ZL18g_ReportingFTAData.4
+ __ZL18g_ReportingFTAData.5
+ __ZL18g_ReportingFTAData.6
+ __ZL18g_ReportingFTAData.7
+ __ZL18g_ReportingFTAData.8
+ __ZL18g_ReportingFTAData.9
+ __ZL25HSW_SetReceivingFTAConfigv
+ ___func__._Z26Ga05_IsReceivingFTAEnabledv
+ ___func__._ZL25HSW_SetReceivingFTAConfigv
+ _g_GNSSME_FTA_Session_Data
+ _xpc_dictionary_set_bool
- __Z26Ga05_IsRecievingFTAEnabledv
- __ZL25HSW_SetRecievingFTAConfigv
- __ZZ27Hal_ProcessFTAAnalyticsDataPhtE25PreviousComputed_FineTime
- __ZZ27Hal_ProcessFTAAnalyticsDataPhtE25PreviousComputed_GPSToWMs
- ___block_descriptor_tmp.58
- ___func__._Z26Ga05_IsRecievingFTAEnabledv
- ___func__._Z27Hal_ProcessFTAAnalyticsDataPht
- ___func__._ZL25HSW_SetRecievingFTAConfigv
Functions:
~ __Z30Hal_GetMEAnalyticsDataResponsePht : 1488 -> 1648
~ __Z27Hal_ProcessFTAAnalyticsDataPht : 576 -> 1024
~ __Z26Hal_ReportFTAAnalyticsDatav : 444 -> 604
~ ____Z26Hal_ReportFTAAnalyticsDatav_block_invoke : 344 -> 504
~ ____ZL22Hal_LogMEAnalyticsDataPht_block_invoke : 760 -> 868
~ __ZL24Gnm55_CheckRestoreStatushPKc : 896 -> 1000
~ __Z18NVIC_L5_EphBin2IntPA10_KjP13s_NVIC_IntEph : 472 -> 492
CStrings:
+ "%10u %s%c %s: %s: Success,Session-ongoing\n"
+ "%10u %s%c %s: FTA-CA, ConnMode,%u,%c, UL_SyncState,%u,%c, RAT_Ind,%u,%c, CellId,%u, SNR,%d, DupMode,%u,%c, DrxState,%u,%c, SubCarrieSpacing,%u, SimId,%u, BaseStationChanged,%c\n"
+ "%10u %s%c %s: FTA-CA,METTickMs,%u,SleepTimeSec,%8.19lf,TimeErrUSec,%10.15lf\n"
+ "%10u %s%c %s: FTA-CA,Mode,DRX,%u, Conn,%u, Dup,%u,RAT,%u,ULSync,%u,ARFCN,%u\n"
+ "%10u %s%c %s: FTA-Evnt, METtick,%u, SleepTimeSec,%10.10lf, FTA-TimeErrUSec,%10.15lf\n"
+ "%10u %s%c %s: ME_Analytics METTickMs %u-%u: L5_Best,%u,L5_Normal,%u,L5_Worst,%u,L5_Unknown,%u\n"
+ "BaseStationIDChanged"
+ "ConnectionModeChanged"
+ "DRXMode"
+ "DRXModeChanged"
+ "DuplexModeChanged"
+ "FTAErrorUSec"
+ "Ga05_IsReceivingFTAEnabled"
+ "HSW_SetReceivingFTAConfig"
+ "Jun 26 2025"
+ "L5BestDurationPercentage"
+ "L5NormalDurationPercentage"
+ "L5UnknownDurationPercentage"
+ "L5WorstDurationPercentage"
+ "RATIndChanged"
+ "ULSyncStateeChanged"
+ "v2.110.0.2025-06-14"
- "%10u %s%c %s: FTA-CA, ConnMode,%u, UL_SyncState,%u, RAT_Ind,%u, CellId,%u, SNR,%d, DupMode,%u, DrxState,%u, SubCarrieSpacing,%u, SimId,%u\n"
- "%10u %s%c %s: FTA-CA,METTickMs,%u,SleepTimeSec,%8.19lf,TimeErrSec,%10.15lf\n"
- "%10u %s%c %s: FTA-Evnt, METtick,%u, SleepTimeSec,%10.10lf, FTA-TimeErrSec,%10.15lf\n"
- "DRSState"
- "FTAErrorSec"
- "Ga05_IsRecievingFTAEnabled"
- "HSW_SetRecievingFTAConfig"
- "Jun 13 2025"
- "v2.109.0.2025-05-16"

```
