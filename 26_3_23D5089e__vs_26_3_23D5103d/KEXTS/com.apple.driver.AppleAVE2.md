## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-905.17.4.0.0
+905.29.1.0.0
   __TEXT.__const: 0x426a0
-  __TEXT.__cstring: 0x40309
-  __TEXT.__os_log: 0x5219a
-  __TEXT_EXEC.__text: 0x1a04dc
+  __TEXT.__cstring: 0x4041a
+  __TEXT.__os_log: 0x521d9
+  __TEXT_EXEC.__text: 0x1a05ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0x130

   __DATA_CONST.__const: 0x8b60
   __DATA_CONST.__kalloc_type: 0x4900
   __DATA_CONST.__kalloc_var: 0x2030
-  UUID: D1A83A70-6A5A-3425-BE09-6BAAB894F968
+  UUID: FFED00C0-9CD0-35A6-91CF-539BCF68A036
   Functions: 2769
   Symbols:   0
-  CStrings:  8973
+  CStrings:  8976
 
Functions:
~ __Z25AVE_CHM_SetDataInfo_FrameP10_S_AVE_CHMP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMS : 1436 -> 1440
~ __Z17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSet : 660 -> 668
~ __Z16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutjiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKc : 7768 -> 7772
~ sub_fffffe0008e5ce94 -> sub_fffffe0008e60ee4 : 316 -> 324
~ __ZN9AVE_FwImg14UninitBufImageEv : 432 -> 436
~ sub_fffffe0008ef5e28 -> sub_fffffe0008ef9e84 : 188 -> 192
~ __ZN9AVE_PSGen17AVC_GenerateSliceEyP16_S_AVE_FrameInfob : 2792 -> 2788
~ __ZN10AVE_MD_SVE8UpdateRCEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMS : 792 -> 1044
~ sub_fffffe0008f4e168 -> sub_fffffe0008f522c0 : 640 -> 644
~ sub_fffffe0008f68a60 -> sub_fffffe0008f6cbbc : 2664 -> 2656
~ sub_fffffe0008f69520 -> sub_fffffe0008f6d674 : 304 -> 308
~ sub_fffffe0008f93c68 -> sub_fffffe0008f97dc0 : 56 -> 48
CStrings:
+ "%lld %d AVE %s: %s::%s:%d %s | wrong frame QP %p %lld %p %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong frame QP %p %lld %p %d %d\n"
+ "20:14:55"
+ "905.29.1"
+ "Jan  5 2026"
+ "pUCInfo->PerFrameData.userSliceQP <= (((((-6) * ((8) - 8))) < (((-6) * ((10) - 8))) ? (((-6) * ((8) - 8))) : (((-6) * ((10) - 8)))) - 1) || pUCInfo->OutputMetaData.frameQp == pUCInfo->PerFrameData.userSliceQP"
- "20:09:34"
- "905.17.4"
- "Dec  8 2025"

```
