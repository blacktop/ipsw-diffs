## AppleAVE2FW_H18.im4p

> `Firmware/ave/AppleAVE2FW_H18.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x1157a8
-  __TEXT.__const: 0x17064
-  __TEXT.__cstring: 0x19615
+  __TEXT.__text: 0x117224
+  __TEXT.__const: 0x17084
+  __TEXT.__cstring: 0x197f7
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211
   __DATA.__data: 0x1590
   __DATA._rtk_mtab: 0x2d0
-  __DATA.__const: 0x4710
+  __DATA.__const: 0x4728
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x6a0

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc6860
-  Functions: 1288
-  Symbols:   1791
-  CStrings:  2849
+  Functions: 1290
+  Symbols:   1793
+  CStrings:  2863
 
Symbols:
+ __ZN11RateControl18processRateControlExx11_S_AVE_Timejjii
+ __ZN11RateControl19updateBitsFromCAVLCExxi
+ __ZN11RateControl19updateCplxForZeroLAExd
+ __ZN15CMCTFController14GetRefCompInfoEbPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoS4_iPbPhS6_P17_S_AVE_CompBufExt
+ __ZN15CMCTFController17GetRefCompOutInfoEPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoiP17_S_AVE_CompBufExt
+ __ZN21ConstantQpRateControl18processRateControlExx11_S_AVE_Timejjii
+ __ZN9BlurRatio6updateERK10FrameStatsP18RateControlContext
- __ZN11RateControl18processRateControlExii
- __ZN15CMCTFController14GetRefCompInfoEbPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoS4_PbPhS6_P17_S_AVE_CompBufExt
- __ZN15CMCTFController17GetRefCompOutInfoEPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoP17_S_AVE_CompBufExt
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
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1019"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1024"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1072"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1084"
+ "RTK_DockChannel_init"
+ "RTK_ST_OK == tStatus"
+ "handleLargePTSGap"
+ "iBufAddr != 0"
+ "updateBitsFromCAVLC"
+ "updateCplxForZeroLA"
- "(m_sSPS.sps_max_sub_layers_minus1 != 0) || (m_sSPS.sps_max_sub_layers_minus1 == 0 && m_sSPS.sps_temporal_id_nesting_flag == true)"
- "9013.35.1"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
```
