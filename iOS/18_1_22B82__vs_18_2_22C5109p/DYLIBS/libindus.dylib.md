## libindus.dylib

> `/usr/lib/libindus.dylib`

```diff

-77.0.0.0.0
-  __TEXT.__text: 0x13781c
+80.0.6.0.0
+  __TEXT.__text: 0x1388c8
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__gcc_except_tab: 0x4bc4
-  __TEXT.__cstring: 0x2492e
-  __TEXT.__const: 0x4600
-  __TEXT.__unwind_info: 0x1d70
+  __TEXT.__gcc_except_tab: 0x4ba8
+  __TEXT.__cstring: 0x2525a
+  __TEXT.__const: 0x4630
+  __TEXT.__unwind_info: 0x1d88
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__const: 0x4d0
   __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__auth_ptr: 0xa0
+  __AUTH_CONST.__auth_ptr: 0x98
   __AUTH_CONST.__const: 0x1d08
   __AUTH_CONST.__cfstring: 0x40
   __AUTH.__data: 0x3f8
-  __DATA.__data: 0x285e0
-  __DATA.__common: 0x63fb9
+  __DATA.__data: 0x28620
+  __DATA.__common: 0x63fd9
   __DATA.__bss: 0x83f8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager
-  - /System/Library/PrivateFrameworks/CoreGPS.framework/CoreGPS
-  - /System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1854
-  Symbols:   1954
-  CStrings:  3840
+  Functions: 1864
+  Symbols:   1962
+  CStrings:  3885
 
Symbols:
+ _analytics_send_event_lazy
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_uint64
- _TelephonyBasebandDeregisterForEvents
- _fclose
- _fopen
- _fread
CStrings:
+ "  TR "
+ "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ME_Analytics METTickMs %!u(MISSING)-%!u(MISSING): AggPow4gdBm,%!d(MISSING),Agg4gtimeS,%!u(MISSING),AggPow5gdBm,%!d(MISSING),Agg5gtimeS,%!u(MISSING),L5stateper,%!u(MISSING),NumInterfaceTeardown,%!u(MISSING),outages,%!u(MISSING),PEAidper,%!u(MISSING)\n"
+ "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ME_Analytics METTickMs %!u(MISSING)-%!u(MISSING): DutyCycle_percent,%!u(MISSING),Max_temperature_rate,%!f(MISSING)C/s,Duration_high_temperature_rate,%!f(MISSING)s,Min_temperature,%!d(MISSING)C,Max_temperature,%!d(MISSING)C\n"
+ "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): TestMode,%!u(MISSING)\n"
+ "%!s(MISSING)  %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING)  %!d(MISSING)  %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)"
+ "Agg4gtimeS"
+ "Agg5gtimeS"
+ "AggPow4gdBm"
+ "AggPow5gdBm"
+ "DD_Proc_GPS_Data:  Invalid GPS Subframe Number.  SV %!d(MISSING)  %!d(MISSING)"
+ "DD_Proc_GPS_Data:  Subframe HOW TOW Error.  SV %!d(MISSING)  TOW %!d(MISSING)"
+ "DD_Proc_GPS_Data:  Subframe Number Error.  SV %!d(MISSING)  decoded %!d(MISSING)  expected %!d(MISSING)  HOW TOW %!d(MISSING)"
+ "DD_Proc_GPS_Data:  Subframe Number Error.  SV %!d(MISSING)  decoded %!d(MISSING)  predicted %!d(MISSING)  or previous %!d(MISSING)"
+ "DD_Proc_QZSS_Data:  Invalid QZSS Subframe Number.  SV %!d(MISSING)  %!d(MISSING)"
+ "DD_Proc_QZSS_Data:  Preamble Test Fail.  SV %!d(MISSING)  Word_Mask %!x(MISSING)  Word_1 %!x(MISSING)"
+ "DD_Proc_QZSS_Data:  Subframe HOW TOW Error.  SV %!d(MISSING)  TOW %!d(MISSING)"
+ "DD_Proc_QZSS_Data:  Subframe Number Error.  SV %!d(MISSING)  decoded %!d(MISSING)  predicted %!d(MISSING)  or previous %!d(MISSING)"
+ "DD_Proc_QZSS_Data:  Subframe Number Error.  SV %!d(MISSING)  decoded %!d(MISSING)  expected %!d(MISSING)  HOW TOW %!d(MISSING)"
+ "DurationHighTempRate_0.1s"
+ "DutyCyclepercent"
+ "Enabled adding +/- 20ms TOW Error on WakeUp from Coma/Sleep"
+ "GLOrssimaxdB"
+ "GLOrssimeandB"
+ "GLOrssipercent"
+ "GNSS_HL_System_Re_Start: Deprecate SLEEP_RESTART to COMA_RESTART since Idle interval longer than %!d(MISSING) s, Idle TTicks %!d(MISSING) ms, Idle OS_Time %!d(MISSING) ms"
+ "GNSS_HL_System_Re_Start: Deprecate SLEEP_RESTART to COMA_RESTART since SUB_MS Time not achieved by the end of the previous session"
+ "GN_AGLON_Set_Clk1: FAILED: gloTauC = %!d(MISSING) <-644 or >644, Unrealistic value!"
+ "GN_AGLON_Set_Clk1: FAILED: gloTauGPS = %!d(MISSING) <-322 or >322, Unrealistic value!"
+ "GN_AGNSS_Set_Time_Model: FAILED: tA1 = %!d(MISSING)  outside +/- 10308 (300ns), Unrealistic!"
+ "GN_GPS_Initialise:  %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "GN_GPS_Set_Config: WARNING: GLONASS has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of BeiDou Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of GLONASS Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of GPS Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of Galileo Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of NavIC Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of QZSS Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Config: WARNING: Use of SBAS Over the Air decoded SV Nav Message data has been disabled"
+ "GN_GPS_Set_Test_Mode:  Illegal Test Mode  %!d(MISSING)  >  %!d(MISSING)"
+ "GN_GPS_Set_Test_Mode:  Test Mode  %!d(MISSING)  :  %!s(MISSING)"
+ "GN_GPS_Update:  Lost BB Coms for %!d(MISSING) > %!d(MISSING) ms, >>>COMA_WAKE_UP  (%!u(MISSING))"
+ "GN_GPS_Update:  WARNING:  Deprecating Time status to +/- 30ms and calling GN_GPS_Restart_Acquisition()"
+ "GN_GPS_Update:  WARNING:  Sub-ms Time Verification failed !  Exact_Bit_Sync %!d(MISSING) pass vs %!d(MISSING) fail , SF_Sync %!d(MISSING) pass vs %!d(MISSING) fail , Bit_ms_offset %!d(MISSING)"
+ "Ga05_GetIsStandaloneBeiDouSupportRequired"
+ "Get_PETestMode"
+ "L1rssimaxdB"
+ "L1rssimeandB"
+ "L1rssipercent"
+ "L5rssimaxdB"
+ "L5rssimeandB"
+ "L5rssipercent"
+ "L5statepercent"
+ "MaxTempC"
+ "MaxTempe_0.1C_s"
+ "MinTempC"
+ "NK_ARP_Calc_Slopes"
+ "NK_IntConstel_TO_IntMeas:  Large BDS-GLO Time Offset  %!d(MISSING) > 50 m"
+ "NK_IntConstel_TO_IntMeas:  Large BDS-GPS Time Offset  %!d(MISSING) m > 30 m"
+ "NK_IntConstel_TO_IntMeas:  Large GLO-GPS Time Offset  %!d(MISSING) m > 40m"
+ "NK_LSq_Cross_Check:  KF Clock bias change : "
+ "NK_Least_Obs_Equ_SV"
+ "NK_Sample_Track_Meas"
+ "NumInterfaceTeardown"
+ "Oct 16 2024"
+ "PEAidTrustedpercent"
+ "SessionDuration"
+ "TestMode 1:  Error added to Time on WakeUp of %!d(MISSING) ms"
+ "Version"
+ "^v8@?0"
+ "com.apple.gpsd.gnssme"
+ "outages"
+ "v2.36.1.2024-09-24"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): CP extended debug CFG\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): CP extended debug disabled\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): CP extended debug send failed\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ExtDbg Config not enabled\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ME extended debug CFG\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ME extended debug disabled\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ME extended debug send failed\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): ME_Analytics METTickMs %!u(MISSING)-%!u(MISSING): AggPow4gdBm,%!u(MISSING),Agg4gtimeS,%!u(MISSING),AggPow5gdBm,%!u(MISSING),Agg5gtimeS,%!u(MISSING),L5stateper,%!u(MISSING),NumInterfaceTeardown,%!u(MISSING),outages,%!u(MISSING),PEAidper,%!u(MISSING)\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): TelephonyBasebandDeregisterForEvents,failed\n"
- "%!u(MISSING) %!s(MISSING)%!c(MISSING) %!s(MISSING): TelephonyBasebandDeregisterForEvents,success\n"
- "%!s(MISSING)  %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING)  %!d(MISSING)  %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)"
- "/var/db/gpsd/zxDfP.bin"
- "/var/db/gpsd/zxDmM.bin"
- "DD_Proc_GPS_Data:  SV %!d(MISSING) Subframe Number Error - decoded %!d(MISSING)  expected %!d(MISSING) or previous %!d(MISSING)"
- "DD_Proc_QZSS_Data:  SV %!d(MISSING) Subframe Number Error - decoded %!d(MISSING)  expected %!d(MISSING) or previous %!d(MISSING)"
- "GN_AGLON_Set_Clk1: FAILED: gloTauC = %!d(MISSING) <-4295 or >4295, Unrealistic value!"
- "GN_AGLON_Set_Clk1: FAILED: gloTauGPS = %!d(MISSING) <-1074 or >1074, Unrealistic value!"
- "GN_GPS_Initialise:  %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)  %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING)  %!d(MISSING) %!d(MISSING) %!d(MISSING)"
- "GN_GPS_Set_Config: WARNING: Glonass has been disabled"
- "Gnm_SendFWExtendedDbgConfig"
- "NK_IntConstel_TO_IntMeas:  Large BDS-GLO Time Offset  %!d(MISSING)"
- "NK_IntConstel_TO_IntMeas:  Large BDS-GPS Time Offset  %!d(MISSING)"
- "NK_IntConstel_TO_IntMeas:  Large GLO-GPS Time Offset  %!d(MISSING)"
- "NK_LSq_Cross_Check:  KF Clock bias change: "
- "Sep 29 2024"
- "rb"
- "v2.31.0.2024-06-15"

```
