## AppleAVE2FW_H17.im4p

> `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0x1081f4
+  __TEXT.__text: 0x10827c
   __TEXT.__const: 0x249ec
-  __TEXT.__cstring: 0x14ec5
+  __TEXT.__cstring: 0x151c5
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
-  __DATA.__const: 0x3310
+  __DATA.__const: 0x33a0
   __DATA._rtk_patchbay: 0x211
   __DATA.__data: 0x1110
   __DATA._rtk_mtab: 0x2d0

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xccb58
-  UUID: 9523E67D-FFA5-396E-896B-A93F42F6B070
-  Functions: 1158
-  Symbols:   1641
-  CStrings:  2476
+  UUID: 7C0C62E5-3574-3C4E-AF93-A339012CB1BA
+  Functions: 1159
+  Symbols:   1645
+  CStrings:  2484
 
Symbols:
+ __ZN14CAVCController21InitFlatMbLowQPParamsEv
+ __ZN15CMCTFController11SetCollMCTFEPK14MCTF_FrameInfo
+ __ZN15CMCTFController25ResetFilterStrengthLookupEj
+ __ZN20CAVECommonController17CreateRateControlEi
+ __ZN20CAVECommonController20processLowResMeStatsEjji
+ __ZN20CAVECommonController23MCTF_SetOutputAvailableEPv
+ __ZN20CAVECommonController27MCTF_GetMaxNumNextRefFramesEv
+ __ZN20CAVECommonController29MCTF_IsFirstNoiseFramePerViewEPv
+ __ZN20CAVECommonController30MCTF_ResetFilterStrengthLookupEj
+ __ZN21ConstantQpRateControl18processRateControlEjj
+ __ZTV21ConstantQpRateControl
- __ZN14CAVCController20processLowResMeStatsEjj
- __ZN14CAVCController21InitFlatMbLowQPParamsEP13S_AVE_RCParam
- __ZN14CAVCController22prepSlicHeaderForCavlcEv
- __ZN15CHEVCController20processLowResMeStatsEjj
- __ZN15CMCTFController11SetCollMCTFEv
- __ZN20CAVECommonController17CreateRateControlEPK13S_AVE_RCParami
- __ZN20CAVECommonController24MCTF_GetNumNextRefFramesEv
CStrings:
+ "%s::%s AccCbp0Cnts: F %d, Mode %d, IB %d %d %d; cbpReset %d, %d; LowerDeltaQP %d %d totalLowQPMB %d"
+ "%s::%s Enter %d %d %d"
+ "%s::%s Exit %d %d %d"
+ "%s::%s:%d F %d final_max_delta_qp %d"
+ "%s::%s:%d F %d qp %d prevqp %d LowerDeltaQP %d totalLowQPMB %d meMem.extra.LowerDeltaQP %d meMem.extra.maxLowerDeltaQP %d IsThisFrameMarkedAsNonReference=%d"
+ "%s::%s:%d F %d ratio_PB %s%lld.%02lld P_cnt %d B_cnt %d max_delta_qp %d"
+ "%s::%s:%d FixQp: %d\n"
+ "%s::%s:%d Frame %d. num next refs: %d"
+ "%s::%s:%d SQPMod: F %d SliceType %d qp %d prevqp %d LowerDeltaQP %d totalLowQPMB %d totalLowQPMBHasCBP %d"
+ "%s::%s:%d invalid parameter"
+ "(EncCommParams.encoder_addr_entropy[i][EncCommParams.transcode_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr & 127) == 0"
+ "(EncCommParams.encoder_addr_entropy[i][EncCommParams.transcode_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
+ "9002.91.1"
+ "AVC:: encoder_addr_entropy[%d][%d].saIBuf[AVE_BufIdx_Data].iAddr:%016llx\n"
+ "CEnvironment::Instance()->GetShareBufSize() >= sizeof(union uCAveNotification) * TARGET_TO_HOST_BUFFER_SIZE"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:651"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:653"
+ "ConstantQpRateControl"
+ "EncCommParams.encoder_addr_entropy[%d][%d].saIBuf[AVE_BufIdx_Data].iAddr %016llx, size 0x%x\n"
+ "EncCommParams.encoder_addr_entropy[i + NUMBER_OF_WRDMABIN*EncCommParams.core_idx][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr != 0"
+ "EncCommParams.encoder_addr_entropy[i + NUMBER_OF_WRDMABIN*EncCommParams.core_idx][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iSize != 0"
+ "EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr != 0"
+ "EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iSize != 0"
+ "EncCommParams.encoder_addr_entropy[i][EncCommParams.transcode_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr != 0"
+ "GetMaxLowerDelatQP"
+ "HEVC:: encoder_addr_entropy[%d][%d].saIBuf[AVE_BufIdx_Data].iAddr:%016llx\n"
+ "RefSpacingB0 %d"
+ "RefSpacingB1 %d"
+ "RefSpacingP %d"
+ "Session:Num next refs:%d (DW:%d)"
+ "StaticAreaInterApply"
+ "sBufSet.saEntropyCoding[%d][%d].saIBuf[AVE_BufIdx_Data].iAddr:%016llx\n"
+ "search range: %d"
- "%s::%s AccCbp0Cnts: F %d, Mode %d, IB %d %d %d; cbpReset %d, %d; LowerDeltaQP %d %d"
- "%s::%s:%d Frame %d"
- "%s::%s:%d invalid parameter %p"
- "(EncCommParams.encoder_addr_entropy[i][EncCommParams.transcode_buffer_id] & 127) == 0"
- "(EncCommParams.encoder_addr_entropy[i][EncCommParams.transcode_buffer_id] & 63) == 0"
- "9002.78.1"
- "AVC:: encoder_addr_entropy[%d][%d]:%016llx\n"
- "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:604"
- "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:606"
- "EncCommParams.encoder_addr_entropy[%d][%d] %016llx, size 0x%x\n"
- "EncCommParams.encoder_addr_entropy[i + NUMBER_OF_WRDMABIN*EncCommParams.core_idx][EncCommParams.pipe_buffer_id] != 0"
- "EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id] != 0"
- "EncCommParams.encoder_addr_entropy[i][EncCommParams.transcode_buffer_id] != 0"
- "EncCommParams.encoder_addr_entropy_size[i + NUMBER_OF_WRDMABIN*EncCommParams.core_idx][EncCommParams.pipe_buffer_id] != 0"
- "EncCommParams.encoder_addr_entropy_size[i][EncCommParams.pipe_buffer_id] != 0"
- "HEVC:: encoder_addr_entropy[%d][%d]:%016llx\n"
- "bUseFrameDrop: %d"
- "pRCParams->RefSpacingB0 %d"
- "pRCParams->RefSpacingB1 %d"
- "pRCParams->RefSpacingP %d"
- "prepSlicHeaderForCavlc"
- "sBufSet.saEntropyCoding[%d][%d].iAddr:%016llx\n"
- "search range: %d(0 : +/-192H by +/-96V, 1 : +/-128H by +/-64V, 2 : +/-64H by +/-32V)\n"
- "uSlcHdrCnt>0 && uSlcHdrCnt<=AVE_MAX_SLICEHEADERS_WALKAROUND"
- "usageMode: %d"

```
