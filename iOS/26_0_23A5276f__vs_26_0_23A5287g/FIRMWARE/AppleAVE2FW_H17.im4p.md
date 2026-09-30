## AppleAVE2FW_H17.im4p

> `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0x10827c
-  __TEXT.__const: 0x249ec
-  __TEXT.__cstring: 0x151c5
+  __TEXT.__text: 0x107c8c
+  __TEXT.__const: 0x24b3c
+  __TEXT.__cstring: 0x1537f
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
-  __DATA.__const: 0x33a0
+  __DATA.__const: 0x34d0
   __DATA._rtk_patchbay: 0x211
   __DATA.__data: 0x1110
   __DATA._rtk_mtab: 0x2d0

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xccb58
-  UUID: 7C0C62E5-3574-3C4E-AF93-A339012CB1BA
-  Functions: 1159
-  Symbols:   1645
-  CStrings:  2484
+  UUID: 82140A27-64D4-37A8-9328-FAFD1FB42521
+  Functions: 1162
+  Symbols:   1647
+  CStrings:  2493
 
Symbols:
+ __ZN11RateControl11updateModelER10FrameStats
+ __ZN11RateControl16applyVbvPlanningEPK10FrameStatsif
+ __ZN11RateControl18processRateControlEjii
+ __ZN11RateControl23updateBitsFromTranscodeEjjiPj
+ __ZN20CAVECommonController17GetThroughputModeEv
+ __ZN21ConstantQpRateControl18processRateControlEjii
+ __ZN25ConstantRateFactorRQModel9getQScaleEPK10FrameStatsifRA4_Kf
+ __ZN3HRD15updateHrdStatusEjPK11_S_AVE_TimefRiS3_f
+ __ZN3HRD4initEbjPK11_S_AVE_Timejff
+ __ZN7RQModel9getQScaleEPK10FrameStatsifRA4_Kf
+ __ZN9BlurRatio14calcBaseQScaleEP18RateControlContextPK10FrameStatsifRA4_Kf
- __ZN11RateControl16applyVbvPlanningEPK10FrameStatsf
- __ZN11RateControl18processRateControlEjj
- __ZN11RateControl23updateBitsFromTranscodeEjjjPj
- __ZN20CAVECommonController30MCTFClientMakeFrameCopyForMCTFEPK20_S_AVE_CompressedBufP18AVE_PICMGMT_PARAMSbb
- __ZN21ConstantQpRateControl18processRateControlEjj
- __ZN25ConstantRateFactorRQModel9getQScaleEPK10FrameStatsfRA4_Kf
- __ZN3HRD15updateHrdStatusEj11_S_AVE_TimefRiS1_f
- __ZN7RQModel9getQScaleEPK10FrameStatsfRA4_Kf
- __ZN9BlurRatio14calcBaseQScaleEP18RateControlContextPK10FrameStatsfRA4_Kf
CStrings:
+ "%s:%d %lld %d | %d %d %d"
+ "%s::%s Enter %d %d %p %d %d %d"
+ "%s::%s Exit %d %d %p %d %d %d"
+ "%s::%s:%d (%d %d) Frame[%d] %d %d %d | %d %d %d %d | %d | inter %d intra %d | %d %d %d %d %d/1000 | LRvar %d"
+ "%s::%s:%d BITBOX (%d %d) Frame[%d] %d %d %d | %d %d %d %d | %d | inter %d intra %d | %d %d %d %d %d/1000 | LRvar %d"
+ "%s::%s:%d BITBOX iIsFirstFrame %d SegmentEncoding Enabled %d totalFrames %d"
+ "%s::%s:%d Enter %d %d %d %d %d %d %d %d %d %d %d %d %d"
+ "%s::%s:%d Exit %d %d %d %d %d %d %d %d %d %d %d %d %d %d"
+ "%s::%s:%d Frame #%d idx[%d] ZeroMVBinCnt %d"
+ "%s::%s:%d Wrong parameter %d %d %d %p"
+ "%s::%s:%d bypass lrmefs %p frm %d iNum %d %lld-%d %d %d"
+ "%s::%s:%d numOfFrame %d bits %d 1stdts %lld iTimescale %d iValue %lld hrd_t_c %d t_c %d"
+ "%s::%s:%d wrong coded data header %p"
+ "9003.8.0"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:686"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:691"
+ "GetThroughputMode"
+ "hrd_time_scale == dts->iTimescale"
- "%s::%s:%d BITBOX (%d %d) Frame[%d] %d %d | %d %d %d %d | %d | inter %d intra %d | %d %d %d %d %d/1000 | LRvar %d"
- "%s::%s:%d BITBOX SegmentEncoding Enabled %d totalFrames %d"
- "%s::%s:%d ZeroMVBinCnt[%d][%d] = %d"
- "%s::%s:%d decOrder %d bits %d 1stdts %lld, dts.iTimeScale %d dts.iValue %lld hrd_t_c %d t_c %d"
- "- CRateControl::ProcessRateControl"
- "9002.91.1"
- "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:651"
- "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:653"
- "hrd_time_scale == dts.iTimescale"

```
