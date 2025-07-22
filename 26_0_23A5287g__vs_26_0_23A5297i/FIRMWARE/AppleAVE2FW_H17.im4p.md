## AppleAVE2FW_H17.im4p

> `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0x107c8c
-  __TEXT.__const: 0x24b3c
-  __TEXT.__cstring: 0x1537f
+  __TEXT.__text: 0x10be44
+  __TEXT.__const: 0x24a04
+  __TEXT.__cstring: 0x155bf
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__const: 0x34d0
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x1110
+  __DATA.__data: 0x1118
   __DATA._rtk_mtab: 0x2d0
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xccb58
-  UUID: 82140A27-64D4-37A8-9328-FAFD1FB42521
-  Functions: 1162
-  Symbols:   1647
-  CStrings:  2493
+  UUID: 52DE8B6A-E087-34E1-B87C-F4F282B7234C
+  Functions: 1161
+  Symbols:   1646
+  CStrings:  2503
 
Symbols:
+ __ZN20CAVECommonController19ProcessPixHistogramEjjjjjj
- __ZN20CAVECommonController13ResetROIFlagsEjy
- __ZN20CAVECommonController22derive_async_wp_paramsEjjjjjj
CStrings:
+ "       (%d xx) C roi_marker: 0x%x, pipborder: 0x%x"
+ "       (%d xx) L roi_marker: 0x%x pipborder: 0x%x, iBoxWidth: %d"
+ "       (%d xx) R roi_marker: 0x%x, pipborder: 0x%x"
+ " Pipe Stats F %d-%d; V %d-%d; APL: %d-%d, G:%u"
+ "%s::%s srcPicIdx %d wSum %d \tcount %d \timgDC %d \tnormDC %d"
+ "%s::%s:%d Frame %d PIP CTU (%dx%d) rect(%d, %d, %d, %d)"
+ "%s::%s:%d PIP Partial Flag %d %d %d %d"
+ "%s::%s:%d PIP ctu (%d %d)"
+ "%s::%s:%d PIP ctu (%d %d) roi_marker 0x%x, iPIPBorder 0x%x"
+ "%s::%s:%d PIP sRect (%d, %d, %dx%d)"
+ "%s::%s:%d wrong start point %d %d"
+ "9003.29.0"
+ "CPlatformEnvironment"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:684"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:689"
+ "ProcessPixHistogram"
+ "gpTimerArray[0] != 0"
+ "hevc_pps->scaling_list_data.scaling_list_dc_coef_minus8[sizeId - 2][matrixId] >= -7 && hevc_pps->scaling_list_data.scaling_list_dc_coef_minus8[sizeId - 2][matrixId] <= 247"
+ "nextCoef == ExplicitVideoScalingList8x8[mode][cmp][0]"
- " Pipe Stats F %d-%d; V %d-%d; APL: %d-%d"
- "%s::%s:%d BITBOX OVERFLOW (QPMODOFF) Frame# %d - ABR: %d HRD: %d"
- "%s::%s:%d BITBOX OVERFLOW (QPMODON) Frame# %d - ABR: %d HRD: %d qpModLevel %d"
- "9003.8.0"
- "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:686"
- "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:691"
- "ResetROIFlags"
- "derive_async_wp_params"
- "start_pt < 128"

```
