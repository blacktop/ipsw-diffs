## AppleAVE2FW_H13C.im4p

> `Firmware/ave/AppleAVE2FW_H13C.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0xfdb94
-  __TEXT.__const: 0x22904
-  __TEXT.__cstring: 0x16417
+  __TEXT.__text: 0xff410
+  __TEXT.__const: 0x22924
+  __TEXT.__cstring: 0x16615
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211
   __DATA.__data: 0x10b0
   __DATA._rtk_mtab: 0x2b8
-  __DATA.__const: 0x3bc8
+  __DATA.__const: 0x3be0
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x1e8

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd2ee0
-  Functions: 1154
-  Symbols:   1615
-  CStrings:  2532
+  Functions: 1156
+  Symbols:   1617
+  CStrings:  2546
 
Symbols:
+ __ZN11RateControl18processRateControlExx11_S_AVE_Timejjii
+ __ZN11RateControl19updateBitsFromCAVLCExxi
+ __ZN11RateControl19updateCplxForZeroLAExd
+ __ZN21ConstantQpRateControl18processRateControlExx11_S_AVE_Timejjii
+ __ZN9BlurRatio6updateERK10FrameStatsP18RateControlContext
- __ZN11RateControl18processRateControlExii
- __ZN21ConstantQpRateControl18processRateControlExii
- __ZN9BlurRatio6updateERK10FrameStats
CStrings:
+ "%s:%d  FwHeaderWrite Overwriting sps_temporal_id_nesting_flag to true."
+ "%s:%s EncCommParams.use_CAVLC_bits %d"
+ "%s:%s EncCommParams.use_CAVLC_bits %d RCiFeature %llu, CommiFeature %llu"
+ "%s::%s Enter, bit = %lld"
+ "%s::%s cplx= %d.%03d cplxFiltered=%d.%03d"
+ "%s::%s lookahead_frames=%d"
+ "%s::%s:%d LA0 (%lld %lld) frameType %d tid %d dts %lld tscale %d past %d.%03d %d.%03d %d.%03d %d.%03d"
+ "%s::%s:%d PTS gap: interval=%lld nominal=%lld excess=%lld accumulated=%lld"
+ "./RTKit/platform/common/CDockChannel.cpp"
+ "9013.45.1"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1019"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1024"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1072"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1084"
+ "RTK_DockChannel_init"
+ "RTK_ST_OK == tStatus"
+ "Received cmd 0x%llx for invalid client:%d"
+ "handleLargePTSGap"
+ "updateBitsFromCAVLC"
+ "updateCplxForZeroLA"
- "(m_sSPS.sps_max_sub_layers_minus1 != 0) || (m_sSPS.sps_max_sub_layers_minus1 == 0 && m_sSPS.sps_temporal_id_nesting_flag == true)"
- "9013.35.1"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
```
