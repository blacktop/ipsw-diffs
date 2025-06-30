## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-735.6.0.0.0
-  __TEXT.__text: 0xc2050
+737.6.0.0.0
+  __TEXT.__text: 0xd6160
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__gcc_except_tab: 0x938
-  __TEXT.__const: 0xb7b6
-  __TEXT.__oslogstring: 0xcef4
-  __TEXT.__cstring: 0x530c
-  __TEXT.__unwind_info: 0x1664
-  __TEXT.__eh_frame: 0x268
+  __TEXT.__gcc_except_tab: 0xa78
+  __TEXT.__const: 0xb926
+  __TEXT.__oslogstring: 0xcd3d
+  __TEXT.__cstring: 0x540b
+  __TEXT.__unwind_info: 0x1850
+  __TEXT.__eh_frame: 0x2a4
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__const: 0x858
+  __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__auth_got: 0x718
   __DATA.__bss: 0x11
   __DATA.__common: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: FC4626C4-5DA3-35FB-9650-F1FDD2DA8ADA
-  Functions: 1676
-  Symbols:   3938
+  UUID: 5111F741-7F49-31DF-A1B5-B8D794E4D566
+  Functions: 1844
+  Symbols:   4297
   CStrings:  1708
 
Symbols:
+ __Z21createDaisyAvcDecoderPv
+ __Z21createDaisyAvxDecoderPv
+ __Z21createDaisyLghDecoderPv
+ __Z22createDaisyHevcDecoderPv
+ __Z27AppleAVDDecodeFrameResponsePviiiii
+ __ZN14CAHDecDaisyAvc11decHdrCSizeEj
+ __ZN14CAHDecDaisyAvc11decHdrYSizeEj
+ __ZN14CAHDecDaisyAvc11initPictureEjjb
+ __ZN14CAHDecDaisyAvc12decodeBufferEv
+ __ZN14CAHDecDaisyAvc12getSWRStrideEjjjj
+ __ZN14CAHDecDaisyAvc13decHdrCStrideEv
+ __ZN14CAHDecDaisyAvc13decHdrYStrideEv
+ __ZN14CAHDecDaisyAvc13getDecHdrSizeEjjjj
+ __ZN14CAHDecDaisyAvc13getTileEndCTUEjj
+ __ZN14CAHDecDaisyAvc14decHdrCLinAddrEj
+ __ZN14CAHDecDaisyAvc14decHdrYLinAddrEj
+ __ZN14CAHDecDaisyAvc14populateSlicesEj
+ __ZN14CAHDecDaisyAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
+ __ZN14CAHDecDaisyAvc15freeWorkBuf_PPSEPv
+ __ZN14CAHDecDaisyAvc15freeWorkBuf_SPSEv
+ __ZN14CAHDecDaisyAvc15getDecHdrStrideEjjj
+ __ZN14CAHDecDaisyAvc15getTileIdxAboveEj
+ __ZN14CAHDecDaisyAvc15getTileStartCTUEjj
+ __ZN14CAHDecDaisyAvc15populateAvdWorkEj
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_PPSEPvS0_S0_
+ __ZN14CAHDecDaisyAvc16allocWorkBuf_SPSEPv
+ __ZN14CAHDecDaisyAvc16decodeBufferSizeEv
+ __ZN14CAHDecDaisyAvc21updateCommonRegistersEj
+ __ZN14CAHDecDaisyAvc22populateSliceRegistersEP17AvcSliceRegistersi
+ __ZN14CAHDecDaisyAvc23populateCommonRegistersEv
+ __ZN14CAHDecDaisyAvc24populatePictureRegistersEv
+ __ZN14CAHDecDaisyAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
+ __ZN14CAHDecDaisyAvc25AvcSeqScalingListFallBackEP7sAvcSPS
+ __ZN14CAHDecDaisyAvc25populateSequenceRegistersEv
+ __ZN14CAHDecDaisyAvcC1EP14CAVDAvcDecoder
+ __ZN14CAHDecDaisyAvcC1Ev
+ __ZN14CAHDecDaisyAvcC2EP14CAVDAvcDecoder
+ __ZN14CAHDecDaisyAvcC2Ev
+ __ZN14CAHDecDaisyAvcD0Ev
+ __ZN14CAHDecDaisyAvcD1Ev
+ __ZN14CAHDecDaisyAvcD2Ev
+ __ZN14CAHDecDaisyAvx10isLfPadDisEv
+ __ZN14CAHDecDaisyAvx11decHdrCSizeEj
+ __ZN14CAHDecDaisyAvx11decHdrYSizeEj
+ __ZN14CAHDecDaisyAvx11initPictureEjjb
+ __ZN14CAHDecDaisyAvx11upscale_posEiii
+ __ZN14CAHDecDaisyAvx12decodeBufferEv
+ __ZN14CAHDecDaisyAvx12startPictureEj
+ __ZN14CAHDecDaisyAvx13DecodePictureEjj
+ __ZN14CAHDecDaisyAvx13decHdrCStrideEv
+ __ZN14CAHDecDaisyAvx13decHdrYStrideEv
+ __ZN14CAHDecDaisyAvx13getTileEndCTUEjj
+ __ZN14CAHDecDaisyAvx13populateTilesEv
+ __ZN14CAHDecDaisyAvx14GetTileMemInfoEPhjPP20_avd_client_mem_infoPy
+ __ZN14CAHDecDaisyAvx14decHdrCLinAddrEj
+ __ZN14CAHDecDaisyAvx14decHdrYLinAddrEj
+ __ZN14CAHDecDaisyAvx14populateSlicesEj
+ __ZN14CAHDecDaisyAvx15freeWorkBuf_PPSEPv
+ __ZN14CAHDecDaisyAvx15freeWorkBuf_SPSEv
+ __ZN14CAHDecDaisyAvx15getTileIdxAboveEj
+ __ZN14CAHDecDaisyAvx15getTileStartCTUEjj
+ __ZN14CAHDecDaisyAvx15populateAvdWorkEj
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_PPSEPvS0_S0_
+ __ZN14CAHDecDaisyAvx16allocWorkBuf_SPSEPv
+ __ZN14CAHDecDaisyAvx16decodeBufferSizeEv
+ __ZN14CAHDecDaisyAvx17getPPSWorkBufSizeEPvS0_
+ __ZN14CAHDecDaisyAvx18populateClearTilesEv
+ __ZN14CAHDecDaisyAvx20getUpscaleConvolveX0Eiii
+ __ZN14CAHDecDaisyAvx21populateTileRegistersEP16AvxTileRegisters
+ __ZN14CAHDecDaisyAvx21updateCommonRegistersEj
+ __ZN14CAHDecDaisyAvx22calc_az_left_tile_sizeEiiiiiiii
+ __ZN14CAHDecDaisyAvx22calc_lf_left_tile_sizeEiiiiiiiii
+ __ZN14CAHDecDaisyAvx22calc_lr_left_tile_sizeEiiiiiiiii
+ __ZN14CAHDecDaisyAvx22getUpscaleConvolveStepEii
+ __ZN14CAHDecDaisyAvx22ppsWorkBufSizeIncreaseEPvS0_
+ __ZN14CAHDecDaisyAvx23populateAvxVPDependencyEv
+ __ZN14CAHDecDaisyAvx23populateCommonRegistersEv
+ __ZN14CAHDecDaisyAvx24populateAddressRegistersEv
+ __ZN14CAHDecDaisyAvx24populatePictureRegistersEv
+ __ZN14CAHDecDaisyAvx25populateSequenceRegistersEv
+ __ZN14CAHDecDaisyAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
+ __ZN14CAHDecDaisyAvx27calc_lf_left_tile_info_sizeEiiiii
+ __ZN14CAHDecDaisyAvx27calc_lr_left_tile_info_sizeEiiiii
+ __ZN14CAHDecDaisyAvx27populateDecryptionRegistersEv
+ __ZN14CAHDecDaisyAvx28calc_rf_above_info_tile_sizeEiiiiii
+ __ZN14CAHDecDaisyAvxC1EP14CAVDAvxDecoder
+ __ZN14CAHDecDaisyAvxC1Ev
+ __ZN14CAHDecDaisyAvxC2EP14CAVDAvxDecoder
+ __ZN14CAHDecDaisyAvxC2Ev
+ __ZN14CAHDecDaisyAvxD0Ev
+ __ZN14CAHDecDaisyAvxD1Ev
+ __ZN14CAHDecDaisyAvxD2Ev
+ __ZN14CAHDecDaisyLgh11GetTileAddrEPhj
+ __ZN14CAHDecDaisyLgh11decHdrCSizeEj
+ __ZN14CAHDecDaisyLgh11decHdrYSizeEj
+ __ZN14CAHDecDaisyLgh11getTileAddrEPhj
+ __ZN14CAHDecDaisyLgh11initPictureEjjb
+ __ZN14CAHDecDaisyLgh12decodeBufferEv
+ __ZN14CAHDecDaisyLgh12getSWRStrideEjjjj
+ __ZN14CAHDecDaisyLgh12startPictureEj
+ __ZN14CAHDecDaisyLgh13DecodePictureEj
+ __ZN14CAHDecDaisyLgh13decHdrCStrideEv
+ __ZN14CAHDecDaisyLgh13decHdrYStrideEv
+ __ZN14CAHDecDaisyLgh13getTileEndCTUEjj
+ __ZN14CAHDecDaisyLgh13populateTilesEv
+ __ZN14CAHDecDaisyLgh14GetTileMemInfoEPhjPP20_avd_client_mem_infoPy
+ __ZN14CAHDecDaisyLgh14clearSegBufferEv
+ __ZN14CAHDecDaisyLgh14decHdrCLinAddrEj
+ __ZN14CAHDecDaisyLgh14decHdrYLinAddrEj
+ __ZN14CAHDecDaisyLgh14populateSlicesEj
+ __ZN14CAHDecDaisyLgh15freeWorkBuf_PPSEPv
+ __ZN14CAHDecDaisyLgh15freeWorkBuf_SPSEv
+ __ZN14CAHDecDaisyLgh15getTileIdxAboveEj
+ __ZN14CAHDecDaisyLgh15getTileStartCTUEjj
+ __ZN14CAHDecDaisyLgh15populateAvdWorkEj
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_PPSEPvS0_S0_
+ __ZN14CAHDecDaisyLgh16allocWorkBuf_SPSEPv
+ __ZN14CAHDecDaisyLgh16decodeBufferSizeEv
+ __ZN14CAHDecDaisyLgh21populateTileRegistersEP16LghTileRegisters
+ __ZN14CAHDecDaisyLgh21updateCommonRegistersEj
+ __ZN14CAHDecDaisyLgh23populateCommonRegistersEv
+ __ZN14CAHDecDaisyLgh24populatePictureRegistersEv
+ __ZN14CAHDecDaisyLgh25populateSequenceRegistersEv
+ __ZN14CAHDecDaisyLghC1EP14CAVDLghDecoder
+ __ZN14CAHDecDaisyLghC1Ev
+ __ZN14CAHDecDaisyLghC2EP14CAVDLghDecoder
+ __ZN14CAHDecDaisyLghC2Ev
+ __ZN14CAHDecDaisyLghD0Ev
+ __ZN14CAHDecDaisyLghD1Ev
+ __ZN14CAHDecDaisyLghD2Ev
+ __ZN15CAHDecDaisyHevc11decHdrCSizeEj
+ __ZN15CAHDecDaisyHevc11decHdrYSizeEj
+ __ZN15CAHDecDaisyHevc11initPictureEjjb
+ __ZN15CAHDecDaisyHevc12decodeBufferEv
+ __ZN15CAHDecDaisyHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
+ __ZN15CAHDecDaisyHevc12getSWRStrideEjjjj
+ __ZN15CAHDecDaisyHevc13decHdrCStrideEv
+ __ZN15CAHDecDaisyHevc13decHdrYStrideEv
+ __ZN15CAHDecDaisyHevc13getDecHdrSizeEjjjj
+ __ZN15CAHDecDaisyHevc13getTileEndCTUEjj
+ __ZN15CAHDecDaisyHevc14decHdrCLinAddrEj
+ __ZN15CAHDecDaisyHevc14decHdrYLinAddrEj
+ __ZN15CAHDecDaisyHevc14populateSlicesEj
+ __ZN15CAHDecDaisyHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
+ __ZN15CAHDecDaisyHevc15freeWorkBuf_PPSEPv
+ __ZN15CAHDecDaisyHevc15freeWorkBuf_SPSEv
+ __ZN15CAHDecDaisyHevc15getDecHdrStrideEjjj
+ __ZN15CAHDecDaisyHevc15getTileIdxAboveEj
+ __ZN15CAHDecDaisyHevc15getTileStartCTUEjj
+ __ZN15CAHDecDaisyHevc15populateAvdWorkEj
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_PPSEPvS0_S0_
+ __ZN15CAHDecDaisyHevc16allocWorkBuf_SPSEPv
+ __ZN15CAHDecDaisyHevc16decodeBufferSizeEv
+ __ZN15CAHDecDaisyHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
+ __ZN15CAHDecDaisyHevc21updateCommonRegistersEj
+ __ZN15CAHDecDaisyHevc22populateSliceRegistersEP18HevcSliceRegistersi
+ __ZN15CAHDecDaisyHevc23populateCommonRegistersEv
+ __ZN15CAHDecDaisyHevc24populatePictureRegistersEv
+ __ZN15CAHDecDaisyHevc25populateSequenceRegistersEv
+ __ZN15CAHDecDaisyHevcC1EP15CAVDHevcDecoder
+ __ZN15CAHDecDaisyHevcC1Ev
+ __ZN15CAHDecDaisyHevcC2EP15CAVDHevcDecoder
+ __ZN15CAHDecDaisyHevcC2Ev
+ __ZN15CAHDecDaisyHevcD0Ev
+ __ZN15CAHDecDaisyHevcD1Ev
+ __ZN15CAHDecDaisyHevcD2Ev
+ __ZN15CAVDHevcDecoder25isRandomAccessSkipPictureEP15HevcPictureInfoji
+ __ZTI14CAHDecDaisyAvc
+ __ZTI14CAHDecDaisyAvx
+ __ZTI14CAHDecDaisyLgh
+ __ZTI15CAHDecDaisyHevc
+ __ZTS14CAHDecDaisyAvc
+ __ZTS14CAHDecDaisyAvx
+ __ZTS14CAHDecDaisyLgh
+ __ZTS15CAHDecDaisyHevc
+ __ZTV14CAHDecDaisyAvc
+ __ZTV14CAHDecDaisyAvx
+ __ZTV14CAHDecDaisyLgh
+ __ZTV15CAHDecDaisyHevc
- GCC_except_table12
- __Z27AppleAVDDecodeFrameResponsePviiii
- __ZN15CAVDHevcDecoder25isRandomAccessSkipPictureEP15HevcPictureInfo
CStrings:
+ "07:21:36"
+ "07:21:37"
+ "AppleAVD:  Compressed buffers disabled! luma depth %d chroma format %d"
+ "AppleAVD:  Compressed buffers enabled! CompressionType:%d. luma depth %d chroma format %d"
+ "AppleAVD: %s(): show %d, showable %d, filmGrainMode = %d, params_present %d, apply_grain %d, frame %d"
+ "AppleAVD: ERROR: %s(): decode buffer at index %d is NULL!\n"
+ "AppleAVD: ERROR: Function call failed with err %d"
+ "CAHDecDaisyAvc"
+ "CAHDecDaisyAvx"
+ "CAHDecDaisyHevc"
+ "CAHDecDaisyLgh"
+ "Nov 12 2023"
+ "int CAHDecDaisyAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "int32_t CAHDecDaisyAvx::getUpscaleConvolveStep(int, int)"
+ "int32_t CAHDecDaisyAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "startPicture"
+ "virtual int CAHDecDaisyAvx::populatePictureRegisters()"
- "02:21:15"
- "02:21:16"
- "AVD_FghEnableCompressionSupport"
- "AVD_LghEnableCompressionSupport"
- "AppleAVD: %s() : buf_idx=%u pool_id %d added to release list..."
- "AppleAVD: %s(): err(%d) frame %8d - rel poolDec idx=%2d"
- "AppleAVD: AppleAVD_FghVideoDecoder ERROR: AppleAVDSetPixelBufferPool : Could not set PixelBufferPool"
- "AppleAVD: AppleAVD_FghVideoDecoder ERROR: AppleAVDSetPixelBufferPool : PixelBufferPool NULL"
- "AppleAVD: AppleAVD_FghVideoDecoder ERROR: createPixelBufferAttributesDictionary failed"
- "AppleAVD: AppleAVD_FghrnVideoDecoder CVPixelBufferPoolCreatePixelBuffer failed with err %d"
- "AppleAVD: AppleAVD_LghVideoDecoder ERROR: AppleAVDSetPixelBufferPool : Could not set PixelBufferPool"
- "AppleAVD: AppleAVD_LghVideoDecoder ERROR: AppleAVDSetPixelBufferPool : PixelBufferPool NULL"
- "AppleAVD: AppleAVD_LghVideoDecoder ERROR: createPixelBufferAttributesDictionary failed"
- "AppleAVD: Compression Support Disabled!"
- "Oct 10 2023"

```
