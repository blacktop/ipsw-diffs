## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-863.1.0.0.0
-  __TEXT.__text: 0x178698
+865.0.0.0.0
+  __TEXT.__text: 0x165b4c
   __TEXT.__auth_stubs: 0xe90
-  __TEXT.__const: 0xc3cb
-  __TEXT.__gcc_except_tab: 0x9ec
-  __TEXT.__oslogstring: 0xfb9e
-  __TEXT.__cstring: 0x5f59
-  __TEXT.__unwind_info: 0x1c10
+  __TEXT.__const: 0xc25b
+  __TEXT.__gcc_except_tab: 0x960
+  __TEXT.__oslogstring: 0xfbe4
+  __TEXT.__cstring: 0x5ed5
+  __TEXT.__unwind_info: 0x1ad8
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x750
-  __AUTH_CONST.__const: 0x52c0
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__const: 0x4d60
+  __AUTH_CONST.__cfstring: 0x740
   __DATA.__common: 0x48
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E21B6516-94DF-3852-89A5-CDF4CD96FF0B
-  Functions: 2502
-  Symbols:   6168
-  CStrings:  1994
+  UUID: 22D09671-9204-37EF-B87B-871F8E43E416
+  Functions: 2376
+  Symbols:   5853
+  CStrings:  1997
 
Symbols:
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
- __ZTI14CAHDecThymeAvc
- __ZTI14CAHDecThymeAvx
- __ZTI14CAHDecThymeLgh
- __ZTI15CAHDecThymeHevc
- __ZTS14CAHDecThymeAvc
- __ZTS14CAHDecThymeAvx
- __ZTS14CAHDecThymeLgh
- __ZTS15CAHDecThymeHevc
- __ZTV14CAHDecThymeAvc
- __ZTV14CAHDecThymeAvx
- __ZTV14CAHDecThymeLgh
- __ZTV15CAHDecThymeHevc
CStrings:
+ "21:22:32"
+ "21:22:33"
+ "AppleAVD: %s(): Thyme AVD is not supported in this AppleAVD driver!!!"
+ "DefaultChromaDownsample"
+ "Jun 11 2025"
+ "createThymeAvcDecoder"
+ "createThymeAvxDecoder"
+ "createThymeHevcDecoder"
+ "createThymeLghDecoder"
- "20:32:34"
- "20:32:35"
- "Apr 22 2025"
- "int CAHDecThymeAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
- "int32_t CAHDecThymeAvx::getUpscaleConvolveStep(int, int)"
- "int32_t CAHDecThymeAvx::getUpscaleConvolveX0(int, int, int32_t)"
- "virtual int CAHDecThymeAvx::populatePictureRegisters()"

```
