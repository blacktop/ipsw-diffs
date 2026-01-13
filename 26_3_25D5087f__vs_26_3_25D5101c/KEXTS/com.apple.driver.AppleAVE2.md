## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-905.17.5.0.0
+905.29.1.0.0
   __TEXT.__const: 0x42680
-  __TEXT.__cstring: 0x3fec1
-  __TEXT.__os_log: 0x51e6b
-  __TEXT_EXEC.__text: 0x19fc0c
+  __TEXT.__cstring: 0x3ffd2
+  __TEXT.__os_log: 0x51eaa
+  __TEXT_EXEC.__text: 0x19fd2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0x130

   __DATA_CONST.__const: 0x99a0
   __DATA_CONST.__kalloc_type: 0x4900
   __DATA_CONST.__kalloc_var: 0x2030
-  UUID: C88E1455-D9DD-3665-917C-AFD272A75438
+  UUID: E48002D6-32C1-3859-9C79-36A1FA25D15F
   Functions: 2769
-  Symbols:   10740
-  CStrings:  8942
+  Symbols:   10741
+  CStrings:  8945
 
Symbols:
+ __ZZN10AVE_MD_SVE8UpdateRCEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMSE11_os_log_fmt_1
Functions:
~ __Z25AVE_CHM_SetDataInfo_FrameP10_S_AVE_CHMP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMS : 1436 -> 1440
~ __Z17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSet : 660 -> 668
~ __Z16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutjiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKc : 7768 -> 7772
~ __Z18AVE_BlkBuf_DestroyI16_S_AVE_FrameInfoEiP13S_AVE_TBlkBufIT_E : 316 -> 324
~ __ZN9AVE_FwImg14UninitBufImageEv : 432 -> 436
~ __Z28AVE_Work_DMV_CalcSurfaceInfoP13_S_AVE_ClientP15_S_AVE_DLB_UnitP21_S_AVE_SurfaceInfoSet : 188 -> 192
~ __ZN9AVE_PSGen17AVC_GenerateSliceEyP16_S_AVE_FrameInfob : 2792 -> 2788
~ __ZN10AVE_MD_SVE8UpdateRCEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMS : 792 -> 1044
~ __ZN10AVE_MD_SVE17CalcInputQueueNumEv : 640 -> 644
~ __Z28AVE_Work_Enc_CalcSurfaceInfoP13_S_AVE_ClientP15_S_AVE_DLB_UnitP21_S_AVE_SurfaceInfoSet : 2664 -> 2656
~ __Z32AVE_Work_Enc_CalcEUMaxInParallelP13_S_AVE_Client : 304 -> 308
~ ___chkstk_darwin_probe : 44 -> 52
CStrings:
+ "%lld %d AVE %s: %s::%s:%d %s | wrong frame QP %p %lld %p %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong frame QP %p %lld %p %d %d\n"
+ "19:25:00"
+ "905.29.1"
+ "Jan  4 2026"
+ "pUCInfo->PerFrameData.userSliceQP <= (((((-6) * ((8) - 8))) < (((-6) * ((10) - 8))) ? (((-6) * ((8) - 8))) : (((-6) * ((10) - 8)))) - 1) || pUCInfo->OutputMetaData.frameQp == pUCInfo->PerFrameData.userSliceQP"
- "23:06:48"
- "905.17.5"
- "Dec  5 2025"

```
