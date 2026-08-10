## libindus.dylib

> `/usr/lib/libindus.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`

```diff

-217.0.0.0.0
-  __TEXT.__text: 0x150314
-  __TEXT.__const: 0x5520
+219.0.0.0.0
+  __TEXT.__text: 0x1505c0
+  __TEXT.__const: 0x5540
   __TEXT.__gcc_except_tab: 0x492c
-  __TEXT.__cstring: 0x294e4
+  __TEXT.__cstring: 0x2957f
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x1f00
+  __TEXT.__unwind_info: 0x1f08
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__weak_got: 0x8
Functions:
~ __Z13ds_NK_SummaryP9s_GN_Ptrs : 47392 -> 47260
~ __Z28GAL_Eph_Reed_Solomon_DecoderP14s_GAL_I_BinEphPttPb : 7708 -> 7704
~ __Z14API_Set_ConfigP13GN_GPS_Config : 736 -> 936
~ __Z16API_Get_Nav_DataP15GN_GPS_Nav_DataP15GN_GPS_Dbg_Data : 12644 -> 12740
~ __Z18Is_BDS_IntEph_RealPK12s_BDS_IntEph : 180 -> 224
~ __Z29GNSS_HL_System_GPS_GAL_ReInitP9s_GN_Ptrs : 396 -> 440
~ __Z24Gnm03_16HandleHWInitFailP11t_MsgHeader : 632 -> 644
~ __Z15Is_Eph_Kep_RealPK9s_Eph_Kep : 332 -> 424
~ __Z15Gnm_HalStartCnf12e_HAL_CbTypeP11u_HAL_CBRsp : 1504 -> 1548
~ __Z18Is_GAL_IntEph_RealPK12s_GAL_IntEph : 164 -> 188
~ __Z21Hal01_01HandleInitReqP11t_MsgHeader : 1680 -> 1688
~ __ZL14Hal01_Init_SPIP13t_Hal_InitReqP16s_HAL_CBInitInfoP11u_HAL_CBRsp : 520 -> 560
~ __Z18Is_GPS_BinEph_RealPK12s_GPS_BinEph : 196 -> 184
~ __Z19Is_NVIC_IntEph_RealPK13s_NVIC_IntEph : 172 -> 188
~ __Z13Hal35_InitSPIv : 1724 -> 1936
CStrings:
+ " Disabled! "
+ "#GPS+GAL OFF"
+ "#GPS+GAL ON"
+ "%10u %s%c %s: IOCreatePlugInInterfaceForService - failed after %d retries: %s\n"
+ "%10u %s%c %s: IOCreatePlugInInterfaceForService retry %d/%d\n"
+ "%10u %s%c %s: IOServiceGetMatchingService - failed after %d retries\n"
+ "%10u %s%c %s: IOServiceGetMatchingService retry %d/%d\n"
+ "Aug  3 2026"
+ "Disabled!  "
+ "Pre_Positioning:  Clearing Sleep_Sub_us_Time, time_diff %g --> %d us"
+ "v2.215.1.2026-07-16"
- "       "
- "                 "
- "  (Disabled!) "
- "  (Disabled!)  "
- " (Disabled!)  "
- " (Disabled!)      "
- "%10u %s%c %s: IOCreatePlugInInterfaceForService ,%s\n"
- "(Disabled!)  "
- "Jul  9 2026"
- "Pre_Positioning:  Clearing Sleep_Sub_us_Time, time_diff %d --> %d us"
- "v2.214.0.2026-06-03"
```
