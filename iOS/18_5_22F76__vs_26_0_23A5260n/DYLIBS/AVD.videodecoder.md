## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-863.1.0.0.0
-  __TEXT.__text: 0x178698
+898.2.0.0.0
+  __TEXT.__text: 0x12902c
   __TEXT.__auth_stubs: 0xe90
-  __TEXT.__const: 0xc3cb
-  __TEXT.__gcc_except_tab: 0x9ec
-  __TEXT.__oslogstring: 0xfb9e
-  __TEXT.__cstring: 0x5f59
-  __TEXT.__unwind_info: 0x1c10
-  __DATA_CONST.__got: 0x340
+  __TEXT.__const: 0xbe4f
+  __TEXT.__gcc_except_tab: 0x7a4
+  __TEXT.__oslogstring: 0xfd66
+  __TEXT.__cstring: 0x5a35
+  __TEXT.__unwind_info: 0x16b0
+  __DATA_CONST.__got: 0x348
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x750
-  __AUTH_CONST.__const: 0x52c0
-  __AUTH_CONST.__cfstring: 0x720
-  __DATA.__common: 0x48
+  __AUTH_CONST.__const: 0x3d40
+  __AUTH_CONST.__cfstring: 0x6e0
+  __DATA.__common: 0x38
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E21B6516-94DF-3852-89A5-CDF4CD96FF0B
-  Functions: 2502
-  Symbols:   6168
-  CStrings:  1994
+  UUID: 57F779D4-0E45-36C8-A3E9-B72BDF8B6A27
+  Functions: 1981
+  Symbols:   4873
+  CStrings:  1967
 
Symbols:
+ GCC_except_table18
+ GCC_except_table21
+ _AppleAVDReleaseOneCPBWithFrameworkError
+ _FigSignalErrorAtGM
+ _PostEmitCleanUpCallBack
+ _VTDecoderSessionCleanUpAfterDecode
+ _VTTileDecoderSessionCleanUpAfterDecode
+ __Z25createNarcissusAvcDecoderPv
+ __Z25createNarcissusLghDecoderPv
+ __Z26createNarcissusHevcDecoderPv
+ __ZL18ScalePlaneBilineariiiPhiiiS_iiiPFvPtS_S_iiEPFvS_S0_ijS_iE25scaler_bilinear_buffers_t
+ __ZN8AVC_RBSP22removeNalTrailingZerosEPhi
+ __ZN8AVC_RBSP29scanNalForEmulationPreventionEPhjib
+ _kVTDecompressionPropertyKey_Paravirtualized
+ _reboot_np
- GCC_except_table13
- GCC_except_table17
- GCC_except_table22
- GCC_except_table25
- _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
- _FigSignalErrorAt3
- _GetNoSecondWriteFlag
- _GetNoSecondWriteFlagDisp
- _IOSurfaceGetAllocSize
- __Z17CreateInputBufferP22_sAppleAVDVideoContextP27_sAppleAVDInitDecoderParams
- __Z21DeleteInputRingBufferP22_sAppleAVDVideoContext
- __ZL16getVTPixelBufferP27OpaqueVTVideoDecoderSessionP25OpaqueVTVideoDecoderFramePP10__CVBufferbjj
- __ZL25CreateCompressedBitBufferji
- __ZL25DeleteCompressedBitBufferP11__IOSurface
- __ZN10LGH_Syntax13tx_mode_probsEv
- __ZN10LGH_Syntax15read_skip_probsEv
- __ZN10LGH_Syntax16read_y_mode_probEv
- __ZN10LGH_Syntax19read_partition_probEv
- __ZN10LGH_Syntax21read_inter_mode_probsEv
- __ZN10LGH_Syntax21read_intra_inter_probEv
- __ZN10LGH_Syntax27read_switchable_interp_probEv
- __ZN10RingBuffer14initRingBufferEPvmh
- __ZN10RingBuffer17requestRingBufferEmPPh
- __ZN10RingBufferC1Ev
- __ZN10RingBufferD1Ev
- __ZN10RingBufferD2Ev
- __ZN14CAHDecThymeAvc11decHdrCSizeEj
- __ZN14CAHDecThymeAvc11decHdrYSizeEj
- __ZN14CAHDecThymeAvc11initPictureEjjb
- __ZN14CAHDecThymeAvc12decodeBufferEv
- __ZN14CAHDecThymeAvc12getSWRStrideEjjjj
- __ZN14CAHDecThymeAvc13decHdrCStrideEv
- __ZN14CAHDecThymeAvc13decHdrYStrideEv
- __ZN14CAHDecThymeAvc13getTileEndCTUEjj
- __ZN14CAHDecThymeAvc14decHdrCLinAddrEj
- __ZN14CAHDecThymeAvc14decHdrYLinAddrEj
- __ZN14CAHDecThymeAvc14populateSlicesEj
- __ZN14CAHDecThymeAvc14setVPInstrFifoEj
- __ZN14CAHDecThymeAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
- __ZN14CAHDecThymeAvc15freeWorkBuf_PPSEPv
- __ZN14CAHDecThymeAvc15freeWorkBuf_SPSEv
- __ZN14CAHDecThymeAvc15getTileIdxAboveEj
- __ZN14CAHDecThymeAvc15getTileStartCTUEjj
- __ZN14CAHDecThymeAvc15populateAvdWorkEj
- __ZN14CAHDecThymeAvc16allocWorkBuf_PPSEPvS0_S0_
- __ZN14CAHDecThymeAvc16allocWorkBuf_SPSEPv
- __ZN14CAHDecThymeAvc16decodeBufferSizeEv
- __ZN14CAHDecThymeAvc21updateCommonRegistersEj
- __ZN14CAHDecThymeAvc22populateSliceRegistersEP17AvcSliceRegistersi
- __ZN14CAHDecThymeAvc23populateCommonRegistersEv
- __ZN14CAHDecThymeAvc24populatePictureRegistersEv
- __ZN14CAHDecThymeAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
- __ZN14CAHDecThymeAvc25AvcSeqScalingListFallBackEP7sAvcSPS
- __ZN14CAHDecThymeAvc25populateSequenceRegistersEv
- __ZN14CAHDecThymeAvc4initEv
- __ZN14CAHDecThymeAvcC2EP14CAVDAvcDecoder
- __ZN14CAHDecThymeAvcD0Ev
- __ZN14CAHDecThymeAvcD1Ev
- __ZN14CAHDecThymeAvcD2Ev
- __ZN14CAHDecThymeAvx10isLfPadDisEv
- __ZN14CAHDecThymeAvx11decHdrCSizeEj
- __ZN14CAHDecThymeAvx11decHdrYSizeEj
- __ZN14CAHDecThymeAvx11initPictureEjjb
- __ZN14CAHDecThymeAvx12decodeBufferEv
- __ZN14CAHDecThymeAvx12startPictureEj
- __ZN14CAHDecThymeAvx13DecodePictureEjj
- __ZN14CAHDecThymeAvx13decHdrCStrideEv
- __ZN14CAHDecThymeAvx13decHdrYStrideEv
- __ZN14CAHDecThymeAvx13getTileEndCTUEjj
- __ZN14CAHDecThymeAvx13populateTilesEv
- __ZN14CAHDecThymeAvx14decHdrCLinAddrEj
- __ZN14CAHDecThymeAvx14decHdrYLinAddrEj
- __ZN14CAHDecThymeAvx14populateSlicesEj
- __ZN14CAHDecThymeAvx14setVPInstrFifoEj
- __ZN14CAHDecThymeAvx15freeWorkBuf_PPSEPv
- __ZN14CAHDecThymeAvx15freeWorkBuf_SPSEv
- __ZN14CAHDecThymeAvx15getTileIdxAboveEj
- __ZN14CAHDecThymeAvx15getTileStartCTUEjj
- __ZN14CAHDecThymeAvx15populateAvdWorkEj
- __ZN14CAHDecThymeAvx16allocWorkBuf_PPSEPvS0_S0_
- __ZN14CAHDecThymeAvx16allocWorkBuf_SPSEPv
- __ZN14CAHDecThymeAvx16decodeBufferSizeEv
- __ZN14CAHDecThymeAvx17getPPSWorkBufSizeEPvS0_
- __ZN14CAHDecThymeAvx18populateClearTilesEv
- __ZN14CAHDecThymeAvx20getUpscaleConvolveX0Eiii
- __ZN14CAHDecThymeAvx21populateTileRegistersEP16AvxTileRegistersj
- __ZN14CAHDecThymeAvx21updateCommonRegistersEj
- __ZN14CAHDecThymeAvx22calc_az_left_tile_sizeEiiiiiiii
- __ZN14CAHDecThymeAvx22calc_lf_left_tile_sizeEiiiiiiiii
- __ZN14CAHDecThymeAvx22calc_lr_left_tile_sizeEiiiiiiiii
- __ZN14CAHDecThymeAvx22getUpscaleConvolveStepEii
- __ZN14CAHDecThymeAvx22ppsWorkBufSizeIncreaseEPvS0_
- __ZN14CAHDecThymeAvx23populateAvxVPDependencyEv
- __ZN14CAHDecThymeAvx23populateCommonRegistersEv
- __ZN14CAHDecThymeAvx24populateAddressRegistersEv
- __ZN14CAHDecThymeAvx24populatePictureRegistersEv
- __ZN14CAHDecThymeAvx25populateSequenceRegistersEv
- __ZN14CAHDecThymeAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
- __ZN14CAHDecThymeAvx27populateDecryptionRegistersEv
- __ZN14CAHDecThymeAvx4initEv
- __ZN14CAHDecThymeAvxC2EP14CAVDAvxDecoder
- __ZN14CAHDecThymeAvxD0Ev
- __ZN14CAHDecThymeAvxD1Ev
- __ZN14CAHDecThymeAvxD2Ev
- __ZN14CAHDecThymeLgh11decHdrCSizeEj
- __ZN14CAHDecThymeLgh11decHdrYSizeEj
- __ZN14CAHDecThymeLgh11initPictureEjjb
- __ZN14CAHDecThymeLgh12decodeBufferEv
- __ZN14CAHDecThymeLgh12getSWRStrideEjjjj
- __ZN14CAHDecThymeLgh12startPictureEj
- __ZN14CAHDecThymeLgh13DecodePictureEj
- __ZN14CAHDecThymeLgh13decHdrCStrideEv
- __ZN14CAHDecThymeLgh13decHdrYStrideEv
- __ZN14CAHDecThymeLgh13getTileEndCTUEjj
- __ZN14CAHDecThymeLgh13populateTilesEv
- __ZN14CAHDecThymeLgh14clearSegBufferEv
- __ZN14CAHDecThymeLgh14decHdrCLinAddrEj
- __ZN14CAHDecThymeLgh14decHdrYLinAddrEj
- __ZN14CAHDecThymeLgh14populateSlicesEj
- __ZN14CAHDecThymeLgh14setVPInstrFifoEj
- __ZN14CAHDecThymeLgh15freeWorkBuf_PPSEPv
- __ZN14CAHDecThymeLgh15freeWorkBuf_SPSEv
- __ZN14CAHDecThymeLgh15getTileIdxAboveEj
- __ZN14CAHDecThymeLgh15getTileStartCTUEjj
- __ZN14CAHDecThymeLgh15populateAvdWorkEj
- __ZN14CAHDecThymeLgh16allocWorkBuf_PPSEPvS0_S0_
- __ZN14CAHDecThymeLgh16allocWorkBuf_SPSEPv
- __ZN14CAHDecThymeLgh16decodeBufferSizeEv
- __ZN14CAHDecThymeLgh21populateTileRegistersEP16LghTileRegisters
- __ZN14CAHDecThymeLgh21updateCommonRegistersEj
- __ZN14CAHDecThymeLgh23populateCommonRegistersEv
- __ZN14CAHDecThymeLgh24populatePictureRegistersEv
- __ZN14CAHDecThymeLgh25populateSequenceRegistersEv
- __ZN14CAHDecThymeLgh4initEv
- __ZN14CAHDecThymeLghC2EP14CAVDLghDecoder
- __ZN14CAHDecThymeLghD0Ev
- __ZN14CAHDecThymeLghD1Ev
- __ZN14CAHDecThymeLghD2Ev
- __ZN14CAVDAvcDecoder29scanNalForEmulationPreventionEPhji
- __ZN15CAHDecBorageAvc11decHdrCSizeEj
- __ZN15CAHDecBorageAvc11decHdrYSizeEj
- __ZN15CAHDecBorageAvc11initPictureEjjb
- __ZN15CAHDecBorageAvc12decodeBufferEv
- __ZN15CAHDecBorageAvc12getSWRStrideEjjjj
- __ZN15CAHDecBorageAvc13decHdrCStrideEv
- __ZN15CAHDecBorageAvc13decHdrYStrideEv
- __ZN15CAHDecBorageAvc13getTileEndCTUEjj
- __ZN15CAHDecBorageAvc14decHdrCLinAddrEj
- __ZN15CAHDecBorageAvc14decHdrYLinAddrEj
- __ZN15CAHDecBorageAvc14populateSlicesEj
- __ZN15CAHDecBorageAvc14setVPInstrFifoEj
- __ZN15CAHDecBorageAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
- __ZN15CAHDecBorageAvc15freeWorkBuf_PPSEPv
- __ZN15CAHDecBorageAvc15freeWorkBuf_SPSEv
- __ZN15CAHDecBorageAvc15getTileIdxAboveEj
- __ZN15CAHDecBorageAvc15getTileStartCTUEjj
- __ZN15CAHDecBorageAvc15populateAvdWorkEj
- __ZN15CAHDecBorageAvc16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecBorageAvc16allocWorkBuf_SPSEPv
- __ZN15CAHDecBorageAvc16decodeBufferSizeEv
- __ZN15CAHDecBorageAvc21updateCommonRegistersEj
- __ZN15CAHDecBorageAvc22populateSliceRegistersEP17AvcSliceRegistersi
- __ZN15CAHDecBorageAvc23populateCommonRegistersEv
- __ZN15CAHDecBorageAvc24populatePictureRegistersEv
- __ZN15CAHDecBorageAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
- __ZN15CAHDecBorageAvc25AvcSeqScalingListFallBackEP7sAvcSPS
- __ZN15CAHDecBorageAvc25populateSequenceRegistersEv
- __ZN15CAHDecBorageAvc4initEv
- __ZN15CAHDecBorageAvcC2EP14CAVDAvcDecoder
- __ZN15CAHDecBorageAvcD0Ev
- __ZN15CAHDecBorageAvcD1Ev
- __ZN15CAHDecBorageAvcD2Ev
- __ZN15CAHDecBorageAvx10isLfPadDisEv
- __ZN15CAHDecBorageAvx11decHdrCSizeEj
- __ZN15CAHDecBorageAvx11decHdrYSizeEj
- __ZN15CAHDecBorageAvx11initPictureEjjb
- __ZN15CAHDecBorageAvx12decodeBufferEv
- __ZN15CAHDecBorageAvx12startPictureEj
- __ZN15CAHDecBorageAvx13DecodePictureEjj
- __ZN15CAHDecBorageAvx13decHdrCStrideEv
- __ZN15CAHDecBorageAvx13decHdrYStrideEv
- __ZN15CAHDecBorageAvx13getTileEndCTUEjj
- __ZN15CAHDecBorageAvx13populateTilesEv
- __ZN15CAHDecBorageAvx14decHdrCLinAddrEj
- __ZN15CAHDecBorageAvx14decHdrYLinAddrEj
- __ZN15CAHDecBorageAvx14populateSlicesEj
- __ZN15CAHDecBorageAvx14setVPInstrFifoEj
- __ZN15CAHDecBorageAvx15freeWorkBuf_PPSEPv
- __ZN15CAHDecBorageAvx15freeWorkBuf_SPSEv
- __ZN15CAHDecBorageAvx15getTileIdxAboveEj
- __ZN15CAHDecBorageAvx15getTileStartCTUEjj
- __ZN15CAHDecBorageAvx15populateAvdWorkEj
- __ZN15CAHDecBorageAvx16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecBorageAvx16allocWorkBuf_SPSEPv
- __ZN15CAHDecBorageAvx16decodeBufferSizeEv
- __ZN15CAHDecBorageAvx17getPPSWorkBufSizeEPvS0_
- __ZN15CAHDecBorageAvx18populateClearTilesEv
- __ZN15CAHDecBorageAvx20getUpscaleConvolveX0Eiii
- __ZN15CAHDecBorageAvx21populateTileRegistersEP16AvxTileRegistersj
- __ZN15CAHDecBorageAvx21updateCommonRegistersEj
- __ZN15CAHDecBorageAvx22calc_az_left_tile_sizeEiiiiiiii
- __ZN15CAHDecBorageAvx22calc_lf_left_tile_sizeEiiiiiiiii
- __ZN15CAHDecBorageAvx22calc_lr_left_tile_sizeEiiiiiiiii
- __ZN15CAHDecBorageAvx22getUpscaleConvolveStepEii
- __ZN15CAHDecBorageAvx22ppsWorkBufSizeIncreaseEPvS0_
- __ZN15CAHDecBorageAvx23populateAvxVPDependencyEv
- __ZN15CAHDecBorageAvx23populateCommonRegistersEv
- __ZN15CAHDecBorageAvx24populateAddressRegistersEv
- __ZN15CAHDecBorageAvx24populatePictureRegistersEv
- __ZN15CAHDecBorageAvx25populateSequenceRegistersEv
- __ZN15CAHDecBorageAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
- __ZN15CAHDecBorageAvx27populateDecryptionRegistersEv
- __ZN15CAHDecBorageAvx4initEv
- __ZN15CAHDecBorageAvxC2EP14CAVDAvxDecoder
- __ZN15CAHDecBorageAvxD0Ev
- __ZN15CAHDecBorageAvxD1Ev
- __ZN15CAHDecBorageAvxD2Ev
- __ZN15CAHDecBorageLgh11decHdrCSizeEj
- __ZN15CAHDecBorageLgh11decHdrYSizeEj
- __ZN15CAHDecBorageLgh11initPictureEjjb
- __ZN15CAHDecBorageLgh12decodeBufferEv
- __ZN15CAHDecBorageLgh12getSWRStrideEjjjj
- __ZN15CAHDecBorageLgh12startPictureEj
- __ZN15CAHDecBorageLgh13DecodePictureEj
- __ZN15CAHDecBorageLgh13decHdrCStrideEv
- __ZN15CAHDecBorageLgh13decHdrYStrideEv
- __ZN15CAHDecBorageLgh13getTileEndCTUEjj
- __ZN15CAHDecBorageLgh13populateTilesEv
- __ZN15CAHDecBorageLgh14clearSegBufferEv
- __ZN15CAHDecBorageLgh14decHdrCLinAddrEj
- __ZN15CAHDecBorageLgh14decHdrYLinAddrEj
- __ZN15CAHDecBorageLgh14populateSlicesEj
- __ZN15CAHDecBorageLgh14setVPInstrFifoEj
- __ZN15CAHDecBorageLgh15freeWorkBuf_PPSEPv
- __ZN15CAHDecBorageLgh15freeWorkBuf_SPSEv
- __ZN15CAHDecBorageLgh15getTileIdxAboveEj
- __ZN15CAHDecBorageLgh15getTileStartCTUEjj
- __ZN15CAHDecBorageLgh15populateAvdWorkEj
- __ZN15CAHDecBorageLgh16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecBorageLgh16allocWorkBuf_SPSEPv
- __ZN15CAHDecBorageLgh16decodeBufferSizeEv
- __ZN15CAHDecBorageLgh21populateTileRegistersEP16LghTileRegisters
- __ZN15CAHDecBorageLgh21updateCommonRegistersEj
- __ZN15CAHDecBorageLgh23populateCommonRegistersEv
- __ZN15CAHDecBorageLgh24populatePictureRegistersEv
- __ZN15CAHDecBorageLgh25populateSequenceRegistersEv
- __ZN15CAHDecBorageLgh4initEv
- __ZN15CAHDecBorageLghC2EP14CAVDLghDecoder
- __ZN15CAHDecBorageLghD0Ev
- __ZN15CAHDecBorageLghD1Ev
- __ZN15CAHDecBorageLghD2Ev
- __ZN15CAHDecKopsiaAvc11decHdrCSizeEj
- __ZN15CAHDecKopsiaAvc11decHdrYSizeEj
- __ZN15CAHDecKopsiaAvc11initPictureEjjb
- __ZN15CAHDecKopsiaAvc12decodeBufferEv
- __ZN15CAHDecKopsiaAvc12getSWRStrideEjjjj
- __ZN15CAHDecKopsiaAvc13decHdrCStrideEv
- __ZN15CAHDecKopsiaAvc13decHdrYStrideEv
- __ZN15CAHDecKopsiaAvc13getTileEndCTUEjj
- __ZN15CAHDecKopsiaAvc14decHdrCLinAddrEj
- __ZN15CAHDecKopsiaAvc14decHdrYLinAddrEj
- __ZN15CAHDecKopsiaAvc14populateSlicesEj
- __ZN15CAHDecKopsiaAvc14setVPInstrFifoEj
- __ZN15CAHDecKopsiaAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
- __ZN15CAHDecKopsiaAvc15freeWorkBuf_PPSEPv
- __ZN15CAHDecKopsiaAvc15freeWorkBuf_SPSEv
- __ZN15CAHDecKopsiaAvc15getTileIdxAboveEj
- __ZN15CAHDecKopsiaAvc15getTileStartCTUEjj
- __ZN15CAHDecKopsiaAvc15populateAvdWorkEj
- __ZN15CAHDecKopsiaAvc16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecKopsiaAvc16allocWorkBuf_SPSEPv
- __ZN15CAHDecKopsiaAvc16decodeBufferSizeEv
- __ZN15CAHDecKopsiaAvc21updateCommonRegistersEj
- __ZN15CAHDecKopsiaAvc22populateSliceRegistersEP17AvcSliceRegistersi
- __ZN15CAHDecKopsiaAvc23populateCommonRegistersEv
- __ZN15CAHDecKopsiaAvc24populatePictureRegistersEv
- __ZN15CAHDecKopsiaAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
- __ZN15CAHDecKopsiaAvc25AvcSeqScalingListFallBackEP7sAvcSPS
- __ZN15CAHDecKopsiaAvc25populateSequenceRegistersEv
- __ZN15CAHDecKopsiaAvc4initEv
- __ZN15CAHDecKopsiaAvcC2EP14CAVDAvcDecoder
- __ZN15CAHDecKopsiaAvcD0Ev
- __ZN15CAHDecKopsiaAvcD1Ev
- __ZN15CAHDecKopsiaAvcD2Ev
- __ZN15CAHDecKopsiaAvx10isLfPadDisEv
- __ZN15CAHDecKopsiaAvx11decHdrCSizeEj
- __ZN15CAHDecKopsiaAvx11decHdrYSizeEj
- __ZN15CAHDecKopsiaAvx11initPictureEjjb
- __ZN15CAHDecKopsiaAvx12decodeBufferEv
- __ZN15CAHDecKopsiaAvx12startPictureEj
- __ZN15CAHDecKopsiaAvx13DecodePictureEjj
- __ZN15CAHDecKopsiaAvx13decHdrCStrideEv
- __ZN15CAHDecKopsiaAvx13decHdrYStrideEv
- __ZN15CAHDecKopsiaAvx13getTileEndCTUEjj
- __ZN15CAHDecKopsiaAvx13populateTilesEv
- __ZN15CAHDecKopsiaAvx14decHdrCLinAddrEj
- __ZN15CAHDecKopsiaAvx14decHdrYLinAddrEj
- __ZN15CAHDecKopsiaAvx14populateSlicesEj
- __ZN15CAHDecKopsiaAvx14setVPInstrFifoEj
- __ZN15CAHDecKopsiaAvx15freeWorkBuf_PPSEPv
- __ZN15CAHDecKopsiaAvx15freeWorkBuf_SPSEv
- __ZN15CAHDecKopsiaAvx15getTileIdxAboveEj
- __ZN15CAHDecKopsiaAvx15getTileStartCTUEjj
- __ZN15CAHDecKopsiaAvx15populateAvdWorkEj
- __ZN15CAHDecKopsiaAvx16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecKopsiaAvx16allocWorkBuf_SPSEPv
- __ZN15CAHDecKopsiaAvx16decodeBufferSizeEv
- __ZN15CAHDecKopsiaAvx17getPPSWorkBufSizeEPvS0_
- __ZN15CAHDecKopsiaAvx18populateClearTilesEv
- __ZN15CAHDecKopsiaAvx20getUpscaleConvolveX0Eiii
- __ZN15CAHDecKopsiaAvx21populateTileRegistersEP16AvxTileRegistersj
- __ZN15CAHDecKopsiaAvx21updateCommonRegistersEj
- __ZN15CAHDecKopsiaAvx22calc_az_left_tile_sizeEiiiiiiii
- __ZN15CAHDecKopsiaAvx22calc_lf_left_tile_sizeEiiiiiiiii
- __ZN15CAHDecKopsiaAvx22calc_lr_left_tile_sizeEiiiiiiiii
- __ZN15CAHDecKopsiaAvx22getUpscaleConvolveStepEii
- __ZN15CAHDecKopsiaAvx22ppsWorkBufSizeIncreaseEPvS0_
- __ZN15CAHDecKopsiaAvx23populateAvxVPDependencyEv
- __ZN15CAHDecKopsiaAvx23populateCommonRegistersEv
- __ZN15CAHDecKopsiaAvx24populateAddressRegistersEv
- __ZN15CAHDecKopsiaAvx24populatePictureRegistersEv
- __ZN15CAHDecKopsiaAvx25populateSequenceRegistersEv
- __ZN15CAHDecKopsiaAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
- __ZN15CAHDecKopsiaAvx27populateDecryptionRegistersEv
- __ZN15CAHDecKopsiaAvx4initEv
- __ZN15CAHDecKopsiaAvxC2EP14CAVDAvxDecoder
- __ZN15CAHDecKopsiaAvxD0Ev
- __ZN15CAHDecKopsiaAvxD1Ev
- __ZN15CAHDecKopsiaAvxD2Ev
- __ZN15CAHDecKopsiaLgh11decHdrCSizeEj
- __ZN15CAHDecKopsiaLgh11decHdrYSizeEj
- __ZN15CAHDecKopsiaLgh11initPictureEjjb
- __ZN15CAHDecKopsiaLgh12decodeBufferEv
- __ZN15CAHDecKopsiaLgh12getSWRStrideEjjjj
- __ZN15CAHDecKopsiaLgh12startPictureEj
- __ZN15CAHDecKopsiaLgh13DecodePictureEj
- __ZN15CAHDecKopsiaLgh13decHdrCStrideEv
- __ZN15CAHDecKopsiaLgh13decHdrYStrideEv
- __ZN15CAHDecKopsiaLgh13getTileEndCTUEjj
- __ZN15CAHDecKopsiaLgh13populateTilesEv
- __ZN15CAHDecKopsiaLgh14clearSegBufferEv
- __ZN15CAHDecKopsiaLgh14decHdrCLinAddrEj
- __ZN15CAHDecKopsiaLgh14decHdrYLinAddrEj
- __ZN15CAHDecKopsiaLgh14populateSlicesEj
- __ZN15CAHDecKopsiaLgh14setVPInstrFifoEj
- __ZN15CAHDecKopsiaLgh15freeWorkBuf_PPSEPv
- __ZN15CAHDecKopsiaLgh15freeWorkBuf_SPSEv
- __ZN15CAHDecKopsiaLgh15getTileIdxAboveEj
- __ZN15CAHDecKopsiaLgh15getTileStartCTUEjj
- __ZN15CAHDecKopsiaLgh15populateAvdWorkEj
- __ZN15CAHDecKopsiaLgh16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecKopsiaLgh16allocWorkBuf_SPSEPv
- __ZN15CAHDecKopsiaLgh16decodeBufferSizeEv
- __ZN15CAHDecKopsiaLgh21populateTileRegistersEP16LghTileRegisters
- __ZN15CAHDecKopsiaLgh21updateCommonRegistersEj
- __ZN15CAHDecKopsiaLgh23populateCommonRegistersEv
- __ZN15CAHDecKopsiaLgh24populatePictureRegistersEv
- __ZN15CAHDecKopsiaLgh25populateSequenceRegistersEv
- __ZN15CAHDecKopsiaLgh4initEv
- __ZN15CAHDecKopsiaLghC2EP14CAVDLghDecoder
- __ZN15CAHDecKopsiaLghD0Ev
- __ZN15CAHDecKopsiaLghD1Ev
- __ZN15CAHDecKopsiaLghD2Ev
- __ZN15CAHDecThymeHevc11decHdrCSizeEj
- __ZN15CAHDecThymeHevc11decHdrYSizeEj
- __ZN15CAHDecThymeHevc11initPictureEjjb
- __ZN15CAHDecThymeHevc12decodeBufferEv
- __ZN15CAHDecThymeHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
- __ZN15CAHDecThymeHevc12getSWRStrideEjjjj
- __ZN15CAHDecThymeHevc13decHdrCStrideEv
- __ZN15CAHDecThymeHevc13decHdrYStrideEv
- __ZN15CAHDecThymeHevc13getTileEndCTUEjj
- __ZN15CAHDecThymeHevc14decHdrCLinAddrEj
- __ZN15CAHDecThymeHevc14decHdrYLinAddrEj
- __ZN15CAHDecThymeHevc14populateSlicesEj
- __ZN15CAHDecThymeHevc14setVPInstrFifoEj
- __ZN15CAHDecThymeHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
- __ZN15CAHDecThymeHevc15freeWorkBuf_PPSEPv
- __ZN15CAHDecThymeHevc15freeWorkBuf_SPSEv
- __ZN15CAHDecThymeHevc15getTileIdxAboveEj
- __ZN15CAHDecThymeHevc15getTileStartCTUEjj
- __ZN15CAHDecThymeHevc15populateAvdWorkEj
- __ZN15CAHDecThymeHevc16allocWorkBuf_PPSEPvS0_S0_
- __ZN15CAHDecThymeHevc16allocWorkBuf_SPSEPv
- __ZN15CAHDecThymeHevc16decodeBufferSizeEv
- __ZN15CAHDecThymeHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
- __ZN15CAHDecThymeHevc21updateCommonRegistersEj
- __ZN15CAHDecThymeHevc22populateSliceRegistersEP18HevcSliceRegistersi
- __ZN15CAHDecThymeHevc23populateCommonRegistersEv
- __ZN15CAHDecThymeHevc24populatePictureRegistersEv
- __ZN15CAHDecThymeHevc25populateSequenceRegistersEv
- __ZN15CAHDecThymeHevc4initEv
- __ZN15CAHDecThymeHevcD0Ev
- __ZN15CAHDecThymeHevcD1Ev
- __ZN15CAHDecThymeHevcD2Ev
- __ZN16CAHDecBorageHevc11decHdrCSizeEj
- __ZN16CAHDecBorageHevc11decHdrYSizeEj
- __ZN16CAHDecBorageHevc11initPictureEjjb
- __ZN16CAHDecBorageHevc12decodeBufferEv
- __ZN16CAHDecBorageHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
- __ZN16CAHDecBorageHevc12getSWRStrideEjjjj
- __ZN16CAHDecBorageHevc13decHdrCStrideEv
- __ZN16CAHDecBorageHevc13decHdrYStrideEv
- __ZN16CAHDecBorageHevc13getTileEndCTUEjj
- __ZN16CAHDecBorageHevc14decHdrCLinAddrEj
- __ZN16CAHDecBorageHevc14decHdrYLinAddrEj
- __ZN16CAHDecBorageHevc14populateSlicesEj
- __ZN16CAHDecBorageHevc14setVPInstrFifoEj
- __ZN16CAHDecBorageHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
- __ZN16CAHDecBorageHevc15freeWorkBuf_PPSEPv
- __ZN16CAHDecBorageHevc15freeWorkBuf_SPSEv
- __ZN16CAHDecBorageHevc15getTileIdxAboveEj
- __ZN16CAHDecBorageHevc15getTileStartCTUEjj
- __ZN16CAHDecBorageHevc15populateAvdWorkEj
- __ZN16CAHDecBorageHevc16allocWorkBuf_PPSEPvS0_S0_
- __ZN16CAHDecBorageHevc16allocWorkBuf_SPSEPv
- __ZN16CAHDecBorageHevc16decodeBufferSizeEv
- __ZN16CAHDecBorageHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
- __ZN16CAHDecBorageHevc21updateCommonRegistersEj
- __ZN16CAHDecBorageHevc22populateSliceRegistersEP18HevcSliceRegistersi
- __ZN16CAHDecBorageHevc23populateCommonRegistersEv
- __ZN16CAHDecBorageHevc24populatePictureRegistersEv
- __ZN16CAHDecBorageHevc25populateSequenceRegistersEv
- __ZN16CAHDecBorageHevc4initEv
- __ZN16CAHDecBorageHevcD0Ev
- __ZN16CAHDecBorageHevcD1Ev
- __ZN16CAHDecBorageHevcD2Ev
- __ZN16CAHDecKopsiaHevc11decHdrCSizeEj
- __ZN16CAHDecKopsiaHevc11decHdrYSizeEj
- __ZN16CAHDecKopsiaHevc11initPictureEjjb
- __ZN16CAHDecKopsiaHevc12decodeBufferEv
- __ZN16CAHDecKopsiaHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
- __ZN16CAHDecKopsiaHevc12getSWRStrideEjjjj
- __ZN16CAHDecKopsiaHevc13decHdrCStrideEv
- __ZN16CAHDecKopsiaHevc13decHdrYStrideEv
- __ZN16CAHDecKopsiaHevc13getTileEndCTUEjj
- __ZN16CAHDecKopsiaHevc14decHdrCLinAddrEj
- __ZN16CAHDecKopsiaHevc14decHdrYLinAddrEj
- __ZN16CAHDecKopsiaHevc14populateSlicesEj
- __ZN16CAHDecKopsiaHevc14setVPInstrFifoEj
- __ZN16CAHDecKopsiaHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
- __ZN16CAHDecKopsiaHevc15freeWorkBuf_PPSEPv
- __ZN16CAHDecKopsiaHevc15freeWorkBuf_SPSEv
- __ZN16CAHDecKopsiaHevc15getTileIdxAboveEj
- __ZN16CAHDecKopsiaHevc15getTileStartCTUEjj
- __ZN16CAHDecKopsiaHevc15populateAvdWorkEj
- __ZN16CAHDecKopsiaHevc16allocWorkBuf_PPSEPvS0_S0_
- __ZN16CAHDecKopsiaHevc16allocWorkBuf_SPSEPv
- __ZN16CAHDecKopsiaHevc16decodeBufferSizeEv
- __ZN16CAHDecKopsiaHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
- __ZN16CAHDecKopsiaHevc21updateCommonRegistersEj
- __ZN16CAHDecKopsiaHevc22populateSliceRegistersEP18HevcSliceRegistersi
- __ZN16CAHDecKopsiaHevc23populateCommonRegistersEv
- __ZN16CAHDecKopsiaHevc24populatePictureRegistersEv
- __ZN16CAHDecKopsiaHevc25populateSequenceRegistersEv
- __ZN16CAHDecKopsiaHevc4initEv
- __ZN16CAHDecKopsiaHevcD0Ev
- __ZN16CAHDecKopsiaHevcD1Ev
- __ZN16CAHDecKopsiaHevcD2Ev
- __ZN17CAHDecHibiscusAvc11decHdrCSizeEj
- __ZN17CAHDecHibiscusAvc11decHdrYSizeEj
- __ZN17CAHDecHibiscusAvc11initPictureEjjb
- __ZN17CAHDecHibiscusAvc12decodeBufferEv
- __ZN17CAHDecHibiscusAvc12getSWRStrideEjjjj
- __ZN17CAHDecHibiscusAvc13decHdrCStrideEv
- __ZN17CAHDecHibiscusAvc13decHdrYStrideEv
- __ZN17CAHDecHibiscusAvc13getTileEndCTUEjj
- __ZN17CAHDecHibiscusAvc14decHdrCLinAddrEj
- __ZN17CAHDecHibiscusAvc14decHdrYLinAddrEj
- __ZN17CAHDecHibiscusAvc14populateSlicesEj
- __ZN17CAHDecHibiscusAvc14setVPInstrFifoEj
- __ZN17CAHDecHibiscusAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
- __ZN17CAHDecHibiscusAvc15freeWorkBuf_PPSEPv
- __ZN17CAHDecHibiscusAvc15freeWorkBuf_SPSEv
- __ZN17CAHDecHibiscusAvc15getTileIdxAboveEj
- __ZN17CAHDecHibiscusAvc15getTileStartCTUEjj
- __ZN17CAHDecHibiscusAvc15populateAvdWorkEj
- __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_
- __ZN17CAHDecHibiscusAvc16allocWorkBuf_SPSEPv
- __ZN17CAHDecHibiscusAvc16decodeBufferSizeEv
- __ZN17CAHDecHibiscusAvc21updateCommonRegistersEj
- __ZN17CAHDecHibiscusAvc22populateSliceRegistersEP17AvcSliceRegistersi
- __ZN17CAHDecHibiscusAvc23populateCommonRegistersEv
- __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv
- __ZN17CAHDecHibiscusAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
- __ZN17CAHDecHibiscusAvc25AvcSeqScalingListFallBackEP7sAvcSPS
- __ZN17CAHDecHibiscusAvc25populateSequenceRegistersEv
- __ZN17CAHDecHibiscusAvc4initEv
- __ZN17CAHDecHibiscusAvcC2EP14CAVDAvcDecoder
- __ZN17CAHDecHibiscusAvcD0Ev
- __ZN17CAHDecHibiscusAvcD1Ev
- __ZN17CAHDecHibiscusAvcD2Ev
- __ZN17CAHDecHibiscusAvx10isLfPadDisEv
- __ZN17CAHDecHibiscusAvx11decHdrCSizeEj
- __ZN17CAHDecHibiscusAvx11decHdrYSizeEj
- __ZN17CAHDecHibiscusAvx11initPictureEjjb
- __ZN17CAHDecHibiscusAvx12decodeBufferEv
- __ZN17CAHDecHibiscusAvx12startPictureEj
- __ZN17CAHDecHibiscusAvx13DecodePictureEjj
- __ZN17CAHDecHibiscusAvx13decHdrCStrideEv
- __ZN17CAHDecHibiscusAvx13decHdrYStrideEv
- __ZN17CAHDecHibiscusAvx13getTileEndCTUEjj
- __ZN17CAHDecHibiscusAvx13populateTilesEv
- __ZN17CAHDecHibiscusAvx14decHdrCLinAddrEj
- __ZN17CAHDecHibiscusAvx14decHdrYLinAddrEj
- __ZN17CAHDecHibiscusAvx14populateSlicesEj
- __ZN17CAHDecHibiscusAvx14setVPInstrFifoEj
- __ZN17CAHDecHibiscusAvx15freeWorkBuf_PPSEPv
- __ZN17CAHDecHibiscusAvx15freeWorkBuf_SPSEv
- __ZN17CAHDecHibiscusAvx15getTileIdxAboveEj
- __ZN17CAHDecHibiscusAvx15getTileStartCTUEjj
- __ZN17CAHDecHibiscusAvx15populateAvdWorkEj
- __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_
- __ZN17CAHDecHibiscusAvx16allocWorkBuf_SPSEPv
- __ZN17CAHDecHibiscusAvx16decodeBufferSizeEv
- __ZN17CAHDecHibiscusAvx17getPPSWorkBufSizeEPvS0_
- __ZN17CAHDecHibiscusAvx18populateClearTilesEv
- __ZN17CAHDecHibiscusAvx20getUpscaleConvolveX0Eiii
- __ZN17CAHDecHibiscusAvx21populateTileRegistersEP16AvxTileRegistersj
- __ZN17CAHDecHibiscusAvx21updateCommonRegistersEj
- __ZN17CAHDecHibiscusAvx22calc_az_left_tile_sizeEiiiiiiii
- __ZN17CAHDecHibiscusAvx22calc_lf_left_tile_sizeEiiiiiiiii
- __ZN17CAHDecHibiscusAvx22calc_lr_left_tile_sizeEiiiiiiiii
- __ZN17CAHDecHibiscusAvx22getUpscaleConvolveStepEii
- __ZN17CAHDecHibiscusAvx22ppsWorkBufSizeIncreaseEPvS0_
- __ZN17CAHDecHibiscusAvx23populateAvxVPDependencyEv
- __ZN17CAHDecHibiscusAvx23populateCommonRegistersEv
- __ZN17CAHDecHibiscusAvx24populateAddressRegistersEv
- __ZN17CAHDecHibiscusAvx24populatePictureRegistersEv
- __ZN17CAHDecHibiscusAvx25populateSequenceRegistersEv
- __ZN17CAHDecHibiscusAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
- __ZN17CAHDecHibiscusAvx27populateDecryptionRegistersEv
- __ZN17CAHDecHibiscusAvx4initEv
- __ZN17CAHDecHibiscusAvxC2EP14CAVDAvxDecoder
- __ZN17CAHDecHibiscusAvxD0Ev
- __ZN17CAHDecHibiscusAvxD1Ev
- __ZN17CAHDecHibiscusAvxD2Ev
- __ZN17CAHDecHibiscusLgh11decHdrCSizeEj
- __ZN17CAHDecHibiscusLgh11decHdrYSizeEj
- __ZN17CAHDecHibiscusLgh11initPictureEjjb
- __ZN17CAHDecHibiscusLgh12decodeBufferEv
- __ZN17CAHDecHibiscusLgh12getSWRStrideEjjjj
- __ZN17CAHDecHibiscusLgh12startPictureEj
- __ZN17CAHDecHibiscusLgh13DecodePictureEj
- __ZN17CAHDecHibiscusLgh13decHdrCStrideEv
- __ZN17CAHDecHibiscusLgh13decHdrYStrideEv
- __ZN17CAHDecHibiscusLgh13getTileEndCTUEjj
- __ZN17CAHDecHibiscusLgh13populateTilesEv
- __ZN17CAHDecHibiscusLgh14clearSegBufferEv
- __ZN17CAHDecHibiscusLgh14decHdrCLinAddrEj
- __ZN17CAHDecHibiscusLgh14decHdrYLinAddrEj
- __ZN17CAHDecHibiscusLgh14populateSlicesEj
- __ZN17CAHDecHibiscusLgh14setVPInstrFifoEj
- __ZN17CAHDecHibiscusLgh15freeWorkBuf_PPSEPv
- __ZN17CAHDecHibiscusLgh15freeWorkBuf_SPSEv
- __ZN17CAHDecHibiscusLgh15getTileIdxAboveEj
- __ZN17CAHDecHibiscusLgh15getTileStartCTUEjj
- __ZN17CAHDecHibiscusLgh15populateAvdWorkEj
- __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_
- __ZN17CAHDecHibiscusLgh16allocWorkBuf_SPSEPv
- __ZN17CAHDecHibiscusLgh16decodeBufferSizeEv
- __ZN17CAHDecHibiscusLgh21populateTileRegistersEP16LghTileRegisters
- __ZN17CAHDecHibiscusLgh21updateCommonRegistersEj
- __ZN17CAHDecHibiscusLgh23populateCommonRegistersEv
- __ZN17CAHDecHibiscusLgh24populatePictureRegistersEv
- __ZN17CAHDecHibiscusLgh25populateSequenceRegistersEv
- __ZN17CAHDecHibiscusLgh4initEv
- __ZN17CAHDecHibiscusLghC2EP14CAVDLghDecoder
- __ZN17CAHDecHibiscusLghD0Ev
- __ZN17CAHDecHibiscusLghD1Ev
- __ZN17CAHDecHibiscusLghD2Ev
- __ZN18CAHDecHibiscusHevc11decHdrCSizeEj
- __ZN18CAHDecHibiscusHevc11decHdrYSizeEj
- __ZN18CAHDecHibiscusHevc11initPictureEjjb
- __ZN18CAHDecHibiscusHevc12decodeBufferEv
- __ZN18CAHDecHibiscusHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
- __ZN18CAHDecHibiscusHevc12getSWRStrideEjjjj
- __ZN18CAHDecHibiscusHevc13decHdrCStrideEv
- __ZN18CAHDecHibiscusHevc13decHdrYStrideEv
- __ZN18CAHDecHibiscusHevc13getTileEndCTUEjj
- __ZN18CAHDecHibiscusHevc14decHdrCLinAddrEj
- __ZN18CAHDecHibiscusHevc14decHdrYLinAddrEj
- __ZN18CAHDecHibiscusHevc14populateSlicesEj
- __ZN18CAHDecHibiscusHevc14setVPInstrFifoEj
- __ZN18CAHDecHibiscusHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
- __ZN18CAHDecHibiscusHevc15freeWorkBuf_PPSEPv
- __ZN18CAHDecHibiscusHevc15freeWorkBuf_SPSEv
- __ZN18CAHDecHibiscusHevc15getTileIdxAboveEj
- __ZN18CAHDecHibiscusHevc15getTileStartCTUEjj
- __ZN18CAHDecHibiscusHevc15populateAvdWorkEj
- __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_
- __ZN18CAHDecHibiscusHevc16allocWorkBuf_SPSEPv
- __ZN18CAHDecHibiscusHevc16decodeBufferSizeEv
- __ZN18CAHDecHibiscusHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
- __ZN18CAHDecHibiscusHevc21updateCommonRegistersEj
- __ZN18CAHDecHibiscusHevc22populateSliceRegistersEP18HevcSliceRegistersi
- __ZN18CAHDecHibiscusHevc23populateCommonRegistersEv
- __ZN18CAHDecHibiscusHevc24populatePictureRegistersEv
- __ZN18CAHDecHibiscusHevc25populateSequenceRegistersEv
- __ZN18CAHDecHibiscusHevc4initEv
- __ZN18CAHDecHibiscusHevcD0Ev
- __ZN18CAHDecHibiscusHevcD1Ev
- __ZN18CAHDecHibiscusHevcD2Ev
- __ZTI14CAHDecThymeAvc
- __ZTI14CAHDecThymeAvx
- __ZTI14CAHDecThymeLgh
- __ZTI15CAHDecBorageAvc
- __ZTI15CAHDecBorageAvx
- __ZTI15CAHDecBorageLgh
- __ZTI15CAHDecKopsiaAvc
- __ZTI15CAHDecKopsiaAvx
- __ZTI15CAHDecKopsiaLgh
- __ZTI15CAHDecThymeHevc
- __ZTI16CAHDecBorageHevc
- __ZTI16CAHDecKopsiaHevc
- __ZTI17CAHDecHibiscusAvc
- __ZTI17CAHDecHibiscusAvx
- __ZTI17CAHDecHibiscusLgh
- __ZTI18CAHDecHibiscusHevc
- __ZTS14CAHDecThymeAvc
- __ZTS14CAHDecThymeAvx
- __ZTS14CAHDecThymeLgh
- __ZTS15CAHDecBorageAvc
- __ZTS15CAHDecBorageAvx
- __ZTS15CAHDecBorageLgh
- __ZTS15CAHDecKopsiaAvc
- __ZTS15CAHDecKopsiaAvx
- __ZTS15CAHDecKopsiaLgh
- __ZTS15CAHDecThymeHevc
- __ZTS16CAHDecBorageHevc
- __ZTS16CAHDecKopsiaHevc
- __ZTS17CAHDecHibiscusAvc
- __ZTS17CAHDecHibiscusAvx
- __ZTS17CAHDecHibiscusLgh
- __ZTS18CAHDecHibiscusHevc
- __ZTV14CAHDecThymeAvc
- __ZTV14CAHDecThymeAvx
- __ZTV14CAHDecThymeLgh
- __ZTV15CAHDecBorageAvc
- __ZTV15CAHDecBorageAvx
- __ZTV15CAHDecBorageLgh
- __ZTV15CAHDecKopsiaAvc
- __ZTV15CAHDecKopsiaAvx
- __ZTV15CAHDecKopsiaLgh
- __ZTV15CAHDecThymeHevc
- __ZTV16CAHDecBorageHevc
- __ZTV16CAHDecKopsiaHevc
- __ZTV17CAHDecHibiscusAvc
- __ZTV17CAHDecHibiscusAvx
- __ZTV17CAHDecHibiscusLgh
- __ZTV18CAHDecHibiscusHevc
- _printf
- _puts
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "19:40:35"
+ "19:40:36"
+ "AppleAVD: %s called with NULL prefs ptr"
+ "AppleAVD: %s videoLayerID %d index %d"
+ "AppleAVD: %s(): Borage AVD is not supported in this AppleAVD driver!!!"
+ "AppleAVD: %s(): ERROR! Exceeded buffers to release (%d)"
+ "AppleAVD: %s(): Error allocating temp buffer for RVRAInLoopChromaFilter() \n"
+ "AppleAVD: %s(): Forcing panic due to SW timeout.\n"
+ "AppleAVD: %s(): Hibiscus AVD is not supported in this AppleAVD driver!!!"
+ "AppleAVD: %s(): Kopsia AVD is not supported in this AppleAVD driver!!!"
+ "AppleAVD: %s(): Narcissus AVD is not supported in this AppleAVD driver!!!"
+ "AppleAVD: %s(): Thyme AVD is not supported in this AppleAVD driver!!!"
+ "AppleAVD: %s(): chromaFilterHdrBuff is not allocated! \n"
+ "AppleAVD: %s(): frame %d layerpresent %d layerID %d numLayers %d \n"
+ "AppleAVD: %s(): kVTDecompressionPropertyKey_Paravirtualized - paravirtualizedSession: %d"
+ "AppleAVD: AppleAVD_FghrnDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
+ "AppleAVD: AppleAVD_FghrnDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
+ "AppleAVD: AppleAVD_H264Decoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
+ "AppleAVD: AppleAVD_H264Decoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
+ "AppleAVD: AppleAVD_H264VideoDecoder ERROR: AppleAVDSetSPSWidthHeight : Could not set SetSPSWidthHeight"
+ "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
+ "AppleAVD: AppleAVD_HEVCDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
+ "AppleAVD: AppleAVD_LghrnDecoder - ERROR setting parameter kAppleAVDPostEmitCleanUpCallBack"
+ "AppleAVD: AppleAVD_LghrnDecoder - ERROR setting parameter kAppleAVDSetParavirtualizedSession"
+ "AppleAVD: ERROR: %s(): AppleAVDCreateDecodeDeviceInternal failed: %d"
+ "AppleAVD: ERROR: %s(): AppleAVDGetParameter [kAppleAVDGetCompressedPictureBuffer] failed with %d\n"
+ "AppleAVD: ERROR: %s(): Bad input size %d > allocated size (%d)"
+ "AppleAVD: ERROR: %s(): Create CPBManager Failed"
+ "AppleAVD: ERROR: %s(): Create RVRA HDR buffer Failed"
+ "AppleAVD: ERROR: %s(): Failed to get an available buffer after %d attempts!\n"
+ "AppleAVD: ERROR: %s(): Failed with error = %d"
+ "AppleAVD: ERROR: %s(): NULL context!\n"
+ "AppleAVD: ERROR: %s(): RVRA HDR buffer map failed: %d \n"
+ "AppleAVD: ERROR: %s(): RVRA_FIRST_BACKUP_BUFF_INDEX map failed: %d \n"
+ "AppleAVD: ERROR: %s(): RVRA_SECOND_BACKUP_BUFF_INDEX map failed: %d \n"
+ "AppleAVD: ERROR: %s(): chromaFilterHdrBuffAllocated is false!\n"
+ "AppleAVD: ERROR: %s(): pluginState (%d) was already started! current: %d - requested: %d"
+ "AppleAVD: ERROR: %s: layerID %d > vps_max_layer_id %d!\n"
+ "AppleAVD: ERROR: H3H264VideoDecoder FIG: Cannot use type of %p %p"
+ "AppleAVD: ERROR: H3H264VideoDecoder FIG: cannot convert number %p %p"
+ "AppleAVD: ERROR: Parser av1_get_next_frame() function return fail!\n"
+ "AppleAVD: ERROR: VRA illegal size %u %u %u %u"
+ "AppleAVD: ERROR: m_dec_hdr_c_size:%d > size of rvra header buffer:%d "
+ "AppleAVD: INFO: %s internal build, useCompression %d"
+ "AppleAVD: INFO: Paravirtualized sessions - ineligible for compressed output!"
+ "AppleAVD: INFO: padding ineligible for compression w x h = %d %d, cw x cw = %d %d"
+ "AppleAVD: NULL sliceHeader %p or nal_header %p or ppsList %p or spsList %p"
+ "AppleAVD: Rejecting RVRA scaling ratios beyond 16x! inWidth:%d inHeight:%d outWidth:%d outHeight:%d"
+ "AppleAVD: Wrong sizeOfScalingList (%d). Should be either 16 or 64"
+ "AppleAVD: cfg1: %d %d %d %d %d %d %d %d"
+ "AppleAVD: cfg2: %d %d %d %d %d %d %d %d"
+ "AppleAVD: cfg3: %d %d %d %d %d %d %d %d"
+ "AppleAVD: parseShortTermRefPicSet parsing failure"
+ "AppleAVD: profile_idc(%d) is not valid"
+ "May 30 2025"
+ "Timeout hit while allocating a CPB - panicking!\n"
+ "Timeout hit while getting a buffer from the Buffer Pool - panicking!\n"
+ "Timeout hit while waiting for outstanding CPBs - panicking!\n"
+ "VASetParams"
+ "createBorageAvcDecoder"
+ "createBorageAvxDecoder"
+ "createBorageHevcDecoder"
+ "createBorageLghDecoder"
+ "createHibiscusAvcDecoder"
+ "createHibiscusAvxDecoder"
+ "createHibiscusHevcDecoder"
+ "createHibiscusLghDecoder"
+ "createKopsiaAvcDecoder"
+ "createKopsiaAvxDecoder"
+ "createKopsiaHevcDecoder"
+ "createKopsiaLghDecoder"
+ "createNarcissusAvcDecoder"
+ "createNarcissusHevcDecoder"
+ "createNarcissusLghDecoder"
+ "createThymeAvcDecoder"
+ "createThymeAvxDecoder"
+ "createThymeHevcDecoder"
+ "createThymeLghDecoder"
+ "deriveSpsParamsFromActiveVps"
+ "readPreferences"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "%s(): create device failed error: %d \n"
- "20:32:34"
- "20:32:35"
- "AVD response buffer"
- "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error"
- "AppleAVD: %s :%s(): bbuf size %zu < request frame size %zu !!!\n\n"
- "AppleAVD: %s internal build, useCompression %d"
- "AppleAVD: %s(): ERROR! Exeeded buffers to release (%d)"
- "AppleAVD: %s(): ERROR! Failed to get an available buffer after %d attempts!\n"
- "AppleAVD: %s(): ERROR! NULL input buffer base (%p)"
- "AppleAVD: %s(): ERROR: Create CPBManager Failed"
- "AppleAVD: %s(): ERROR: Create RVRA HDR buffer Failed"
- "AppleAVD: %s(): ERROR: CreateCompressedBitBuffer Failed"
- "AppleAVD: %s(): Request ring buffer error (%d)!\n"
- "AppleAVD: %s(): VAMapPixelBuffer failed for input buf IOSurface, err=%d"
- "AppleAVD: %s(): bad input size %d"
- "AppleAVD: %s(): taggedBufGroupArray groups = %ld groupIndex %ld"
- "AppleAVD: %s: AppleAVDWrapperFghrnDecoderSetProperty - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs"
- "AppleAVD: AVDUseCompression %d"
- "AppleAVD: AVD_AllowADSOnUnsupported %d"
- "AppleAVD: AVD_AllowBitstreamToChangeFrameDimensions %d"
- "AppleAVD: AVD_AvdFilmGrainMode %d"
- "AppleAVD: AVD_AvdOpPoint %d"
- "AppleAVD: AVD_CPBCacheBufferSizeFactor %d"
- "AppleAVD: AVD_CPBCacheNumBuffers %d"
- "AppleAVD: AVD_CheckWireLimit %d"
- "AppleAVD: AVD_CoreSelect %d"
- "AppleAVD: AVD_EnableFileDump %d"
- "AppleAVD: AVD_EnableHistogram %d"
- "AppleAVD: AVD_EnableIdleTimer %d"
- "AppleAVD: AVD_EnableSliceQpExtraction %d"
- "AppleAVD: AVD_IdleTimerNumClients %d"
- "AppleAVD: AVD_IdleTimerTimeout %d"
- "AppleAVD: AVD_InhibitADSForAVCHEVC %d"
- "AppleAVD: AVD_InhibitADSForVP9 %d"
- "AppleAVD: AVD_LogSliceHeaderLongerThan %d"
- "AppleAVD: AVD_MCacheMode %d"
- "AppleAVD: AVD_OnDemandDartMap %d"
- "AppleAVD: AVD_RejectFormatDescription %d"
- "AppleAVD: AVD_TryAllFrames %d"
- "AppleAVD: AVD_avdCoreControlPerfWeight %d"
- "AppleAVD: AppleAVD: padding ineligible for compression w x h = %d %d, cw x cw = %d %d"
- "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
- "AppleAVD: AppleAVD_H264VideoDecoder ERROR: kAppleAVDSetInputSurfaceID : Could not set IOSurfaceID"
- "AppleAVD: AppleAVD_HEVCTileDecoder ERROR: Could not get bitstream buffer"
- "AppleAVD: CFPrefs:"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n"
- "AppleAVD: ERROR: %s(): AppleAVDGetParameter [kAppleAVDGetBitstreamBuffer] failed with %d\n"
- "AppleAVD: ERROR: %s(): AppleAVDGetParameter [kAppleAVDSetInputSurfaceID] failed with %d\n"
- "AppleAVD: ERROR: %s(): ctx->pCompressedBufferBaseAddr == NULL\n"
- "AppleAVD: ERROR: %s: error creating ring buffer!\n"
- "AppleAVD: ERROR: failed to get IO Surface from buffer pool!"
- "AppleAVD: ERROR: failed to get a handle to the disp buffer pool!"
- "AppleAVD: Rejecting RVRA scaling ratios beyond 5x! inWidth:%d inHeight:%d outWidth:%d outHeight:%d"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n"
- "AppleAVD: WARNING: %s(): Timed out, waited at least %llums! m_num_buffers_outstanding=%u WAIT_TIMEOUT_NS=%llu"
- "AppleAVD: WARNING: %s(): inputBufSize: %d > %d, capping to %d!"
- "AppleAVD: decodeGetRenderTarget(BITSTREAM_SURFACE_INDEX failed"
- "AppleAVD: parseShortTermRefPicSet prasing failure"
- "AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources"
- "AppleAVD_FghrnVideoDecoder.c"
- "AppleAVD_H264VideoDecoder.c"
- "AppleAVD_HEVCVideoDecoder.c"
- "AppleAVD_LghrnVideoDecoder.c"
- "Apr 22 2025"
- "CFArrayCreate failed"
- "CFDictionaryCreate failed"
- "CFDictionaryCreate failed (once)"
- "CreateInputBuffer"
- "H3H264VideoDecoder FIG: Cannot use type of %p %p"
- "H3H264VideoDecoder FIG: cannot convert number %p %p"
- "Index %d out of bound %d"
- "NULL sliceHeader %p or nal_header %p or ppsList %p or spsList %p"
- "Parser av1_get_next_frame() function return fail!"
- "RINGBUFFER"
- "RequestedMVAV1SpatialIDs"
- "Wrong sizeOfScalingList (%d). Should be either 16 or 64"
- "h264 parsing info not set"
- "h264 requires format description"
- "hevc parsing info not set"
- "hevc requires format description"
- "int CAHDecBorageAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecHibiscusAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecKopsiaAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int CAHDecThymeAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int32_t CAHDecBorageAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecBorageAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecHibiscusAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecHibiscusAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecKopsiaAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecKopsiaAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "int32_t CAHDecThymeAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecThymeAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "kVTAllocationFailedErr"
- "kVTParameterErr"
- "kVTPropertyReadOnlyErr"
- "pic_parameter_set_id(%d) out of range [0..%d]"
- "profile_idc(%d) is not valid"
- "property is read-only"
- "requestRingBuffer"
- "seq_parameter_set_id(%d) out of range [0..%d]"
- "virtual int CAHDecBorageAvx::populatePictureRegisters()"
- "virtual int CAHDecHibiscusAvx::populatePictureRegisters()"
- "virtual int CAHDecKopsiaAvx::populatePictureRegisters()"
- "virtual int CAHDecThymeAvx::populatePictureRegisters()"

```
