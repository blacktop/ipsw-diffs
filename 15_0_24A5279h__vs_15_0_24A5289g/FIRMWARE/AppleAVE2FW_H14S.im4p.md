## AppleAVE2FW_H14S.im4p

> `AppleAVE2FW_H14S.im4p`

```diff

 
-  __TEXT.__text: 0xd3330
-  __TEXT.__cstring: 0x12a06
-  __TEXT.__const: 0x1eb48
+  __TEXT.__text: 0xd4630
+  __TEXT.__cstring: 0x12b87
+  __TEXT.__const: 0x1ee28
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x2d0
   __TEXT.__constructor: 0x0
-  __DATA.__const: 0x28a8
-  __DATA.__data: 0x1140
+  __DATA.__const: 0x2918
+  __DATA.__data: 0x1090
   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xd03b8
   Functions: 0
-  Symbols:   1450
-  CStrings:  2261
+  Symbols:   1463
+  CStrings:  2264
 
Symbols:
+ __Z18AVE_TargetID2DevIDi
+ __ZN11AVE_DevInfo15GetDevSubIDFlagEv
+ __ZN11AVE_DevInfo17GetDevNumPerGroupEv
+ __ZN11AVE_DevInfo3GetEv
+ __ZN11AVE_DevInfo4InitEj12_E_AVE_DevIDiiyi
+ __ZN11AVE_DevInfo8GetDevIDEv
+ __ZN11AVE_DevInfo8GetSVEIDEv
+ __ZN11AVE_DevInfo9GetDevNumEv
+ __ZN20CAVECommonController14scaleHistogramEjPKjPjiii
+ __ZN20CAVECommonController15searchHistogramEjjPKjPjS2_iPiS3_
+ __ZN20CAVECommonController18resetWpContentFlagEv
+ __ZN20CAVECommonController22derive_async_wp_paramsEjjjjjj
+ __ZN7AVE_FPS11CalcOverallEv
+ __ZN7AVE_FPS3AddEPK11_S_AVE_Time
+ __ZN7AVE_FPS4CalcEPK11_S_AVE_TimeS2_i
+ __ZN7AVE_FPS4InitEiii
+ __ZN7AVE_FPS5GetRtEv
+ __ZN7AVE_FPS6CalcRtEv
+ __ZN7AVE_FPS6UpdateEiii
+ __ZN7AVE_FPS7CalcAvgEv
+ __ZN7AVE_FPS9CalcSlideEv
+ __ZN7AVE_FPSC1Ev
+ __ZN7AVE_FPSD1Ev
- __Z11AVE_FPS_AddP10_S_AVE_FPSPK11_S_AVE_Time
- __Z12AVE_FPS_InitP10_S_AVE_FPSii
- __Z13AVE_FPS_GetRtPK10_S_AVE_FPS
- __Z14AVE_FPS_CalcRtP10_S_AVE_FPS
- __Z14AVE_FPS_UninitP10_S_AVE_FPS
- __Z15AVE_FPS_CalcAvgP10_S_AVE_FPS
- __Z19AVE_FPS_CalcOverallP10_S_AVE_FPS
- __ZN20CAVECommonController22derive_async_wp_paramsEjj
- _g_iDeviceId
- _g_iSVEId
CStrings:
+ "%!s(MISSING)::%!s(MISSING) Enter %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING) Exit %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING) RCMode %!d(MISSING) fQuality %!d(MISSING) quality %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!l(MISSING)ld %!d(MISSING) - %!l(MISSING)ld %!d(MISSING) %!d(MISSING) | %!l(MISSING)ld.%!l(MISSING)ld %!l(MISSING)ld.%!l(MISSING)ld "
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) | %!d(MISSING) %!l(MISSING)ld %!d(MISSING) - %!d(MISSING) %!l(MISSING)ld %!d(MISSING) | %!d(MISSING).%!d(MISSING) %!d(MISSING).%!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) | %!d(MISSING) %!l(MISSING)ld %!d(MISSING) - %!d(MISSING) %!l(MISSING)ld %!d(MISSING) | %!d(MISSING).%!d(MISSING)  %!d(MISSING).%!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | Fail to find device capability (DevID: %!d(MISSING) DevType: %!d(MISSING) ChipType: %!d(MISSING) DevRevision: %!d(MISSING) Arch: %!d(MISSING) SVE Num: %!d(MISSING) NumPerGroup: %!d(MISSING) DevSubIDFlag: 0x%!l(MISSING)lx) ret: %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to add PTS to FPS %!p(MISSING) %!l(MISSING)ld 0x%!l(MISSING)lx %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to initialize FPS %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING).%!d(MISSING) %!d(MISSING).%!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to update FPS %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING).%!d(MISSING) %!d(MISSING).%!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | fail to update FPS %!p(MISSING) %!l(MISSING)ld 0x%!l(MISSING)lx %!p(MISSING) %!p(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to allocate memory of timestamp %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to calculate average FPS %!p(MISSING) %!p(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to calculate realtime FPS %!p(MISSING) %!p(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to calculate sliding average FPS %!p(MISSING) %!p(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong parameters %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong state %!p(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong state %!p(MISSING) %!p(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) ENC: StartCount %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING), Idle %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) Enc_Client IDs %!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld CTX %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) Enc_Client IDs %!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld CTX %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) Frame[%!l(MISSING)ld] op %!l(MISSING)lu PTS %!l(MISSING)ld | interval %!d(MISSING) %!d(MISSING) %!d(MISSING).%!d(MISSING) %!d(MISSING).%!d(MISSING) | status %!l(MISSING)ld %!l(MISSING)ld %!l(MISSING)ld | Hint %!d(MISSING) %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) StartCount %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING), HW %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) allocate bigger memory of timestamp %!p(MISSING) %!d(MISSING) %!d(MISSING) <- %!d(MISSING)"
+ "%!s(MISSING)::%!s(MISSING):%!d(MISSING) failed to allocate memory of timestamp %!p(MISSING) %!d(MISSING)"
+ "./AppleAVE2FW/Firmware/Device/Capability/AVE_DevCap.cpp"
+ "0 < fps && fps < 100000 && num >= 0"
+ "8001.94.0"
+ "AVE_DevInfo"
+ "AVE_FPS"
+ "Add"
+ "Calc"
+ "CalcAvg"
+ "CalcOverall"
+ "CalcRt"
+ "CalcSlide"
+ "Uninit"
+ "depth == 8 || depth == 10"
+ "distortion >= 0"
+ "fQuality: %!d(MISSING)"
+ "m_psTime != __null"
+ "pDevCap != __null"
+ "pDevCap->psCEntry != __null"
+ "scaleHistogram"
+ "searchHistogram"
- "%!s(MISSING) Enter %!p(MISSING)"
- "%!s(MISSING) Enter %!p(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!s(MISSING) Enter %!p(MISSING) %!p(MISSING)"
- "%!s(MISSING) Exit %!p(MISSING) %!d(MISSING)"
- "%!s(MISSING) Exit %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!s(MISSING) Exit %!p(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!l(MISSING)ld %!d(MISSING) - %!l(MISSING)ld %!d(MISSING) %!d(MISSING) | %!l(MISSING)ld.%!l(MISSING)ld %!l(MISSING)ld.%!l(MISSING)ld "
- "%!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) | %!d(MISSING) %!l(MISSING)ld %!d(MISSING) - %!d(MISSING) %!l(MISSING)ld %!d(MISSING) | %!d(MISSING).%!d(MISSING) %!d(MISSING).%!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!p(MISSING) %!d(MISSING) %!d(MISSING) | %!d(MISSING) %!l(MISSING)ld %!d(MISSING) - %!d(MISSING) %!l(MISSING)ld %!d(MISSING) | %!d(MISSING).%!d(MISSING)  %!d(MISSING).%!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to allocate memory of timestamp %!p(MISSING) %!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to calculate average FPS %!p(MISSING) %!p(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | failed to calculate realtime FPS %!p(MISSING) %!p(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong parameters %!p(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong parameters %!p(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong state %!p(MISSING)"
- "%!s(MISSING):%!d(MISSING) %!s(MISSING) | wrong state %!p(MISSING) %!p(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_FPS Init error %!p(MISSING) %!d(MISSING) %!d(MISSING) %!f(MISSING) %!f(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_FPS Init error %!p(MISSING) %!l(MISSING)ld 0x%!l(MISSING)lx %!p(MISSING) %!p(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_FPS Uninit error %!p(MISSING) %!d(MISSING) %!d(MISSING) %!f(MISSING) %!f(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_FPS Uninit error %!p(MISSING) %!l(MISSING)ld 0x%!l(MISSING)lx %!p(MISSING) %!p(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) %!s(MISSING) | AVE_FPS add error %!p(MISSING) %!l(MISSING)ld 0x%!l(MISSING)lx %!p(MISSING) %!p(MISSING) %!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) ENC: StartCount %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING), Idle %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) Enc_Client IDs %!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld CTX %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) Enc_Client IDs %!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld-%!l(MISSING)ld CTX %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) Frame[%!l(MISSING)ld] op %!l(MISSING)lu PTS %!l(MISSING)ld | interval %!d(MISSING) %!d(MISSING) %!d(MISSING) %!d(MISSING) | status %!l(MISSING)ld %!l(MISSING)ld %!l(MISSING)ld | Hint %!d(MISSING) %!d(MISSING)"
- "%!s(MISSING)::%!s(MISSING):%!d(MISSING) StartCount %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING), HW %!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)-%!d(MISSING)"
- "8001.75.0"
- "AVE_FPS_Add"
- "AVE_FPS_Calc"
- "AVE_FPS_CalcAvg"
- "AVE_FPS_CalcOverall"
- "AVE_FPS_CalcRt"
- "AVE_FPS_Init"
- "AVE_FPS_Uninit"
- "ioreporting"
- "management"
- "pDevCap->psCEntry != NULL"
- "pFPS != __null"
- "pFPS != __null && 0 < fps && fps < 100000 && num >= 0"
- "pFPS->psTime != __null"
- "rtp_crashlog"
- "syslog"
- "utestApp"

```
