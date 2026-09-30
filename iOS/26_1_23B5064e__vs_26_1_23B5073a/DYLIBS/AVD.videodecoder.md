## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 906.0.0.0.0
-  __TEXT.__text: 0x13ffc8
+  __TEXT.__text: 0x153b08
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__const: 0xbfe3
-  __TEXT.__gcc_except_tab: 0x830
-  __TEXT.__oslogstring: 0x103a4
-  __TEXT.__cstring: 0x5b53
-  __TEXT.__unwind_info: 0x1840
+  __TEXT.__const: 0xc153
+  __TEXT.__gcc_except_tab: 0x8bc
+  __TEXT.__oslogstring: 0x1035b
+  __TEXT.__cstring: 0x5bef
+  __TEXT.__unwind_info: 0x1990
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x758
-  __AUTH_CONST.__const: 0x42a0
+  __AUTH_CONST.__const: 0x4800
   __AUTH_CONST.__cfstring: 0x720
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 0C45C00D-DB0A-39C2-A5A7-189C36619747
-  Functions: 2115
-  Symbols:   5196
-  CStrings:  1993
+  UUID: 9059287E-F599-3595-BEE1-2E6EEAA1C610
+  Functions: 2245
+  Symbols:   5511
+  CStrings:  1992
 
Symbols:
+ __ZN17CAHDecHibiscusAvc11decHdrCSizeEj
+ __ZN17CAHDecHibiscusAvc11decHdrYSizeEj
+ __ZN17CAHDecHibiscusAvc11initPictureEjjb
+ __ZN17CAHDecHibiscusAvc12decodeBufferEv
+ __ZN17CAHDecHibiscusAvc12getSWRStrideEjjjj
+ __ZN17CAHDecHibiscusAvc13decHdrCStrideEv
+ __ZN17CAHDecHibiscusAvc13decHdrYStrideEv
+ __ZN17CAHDecHibiscusAvc13getTileEndCTUEjj
+ __ZN17CAHDecHibiscusAvc14decHdrCLinAddrEj
+ __ZN17CAHDecHibiscusAvc14decHdrYLinAddrEj
+ __ZN17CAHDecHibiscusAvc14populateSlicesEj
+ __ZN17CAHDecHibiscusAvc14setVPInstrFifoEj
+ __ZN17CAHDecHibiscusAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
+ __ZN17CAHDecHibiscusAvc15freeWorkBuf_PPSEPv
+ __ZN17CAHDecHibiscusAvc15freeWorkBuf_SPSEv
+ __ZN17CAHDecHibiscusAvc15getTileIdxAboveEj
+ __ZN17CAHDecHibiscusAvc15getTileStartCTUEjj
+ __ZN17CAHDecHibiscusAvc15populateAvdWorkEj
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_PPSEPvS0_S0_
+ __ZN17CAHDecHibiscusAvc16allocWorkBuf_SPSEPv
+ __ZN17CAHDecHibiscusAvc16decodeBufferSizeEv
+ __ZN17CAHDecHibiscusAvc21updateCommonRegistersEj
+ __ZN17CAHDecHibiscusAvc22populateSliceRegistersEP17AvcSliceRegistersi
+ __ZN17CAHDecHibiscusAvc23populateCommonRegistersEv
+ __ZN17CAHDecHibiscusAvc24populatePictureRegistersEv
+ __ZN17CAHDecHibiscusAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
+ __ZN17CAHDecHibiscusAvc25AvcSeqScalingListFallBackEP7sAvcSPS
+ __ZN17CAHDecHibiscusAvc25populateSequenceRegistersEv
+ __ZN17CAHDecHibiscusAvc4initEv
+ __ZN17CAHDecHibiscusAvcC2EP14CAVDAvcDecoder
+ __ZN17CAHDecHibiscusAvcD0Ev
+ __ZN17CAHDecHibiscusAvcD1Ev
+ __ZN17CAHDecHibiscusAvcD2Ev
+ __ZN17CAHDecHibiscusAvx10isLfPadDisEv
+ __ZN17CAHDecHibiscusAvx11decHdrCSizeEj
+ __ZN17CAHDecHibiscusAvx11decHdrYSizeEj
+ __ZN17CAHDecHibiscusAvx11initPictureEjjb
+ __ZN17CAHDecHibiscusAvx12decodeBufferEv
+ __ZN17CAHDecHibiscusAvx12startPictureEj
+ __ZN17CAHDecHibiscusAvx13DecodePictureEjj
+ __ZN17CAHDecHibiscusAvx13decHdrCStrideEv
+ __ZN17CAHDecHibiscusAvx13decHdrYStrideEv
+ __ZN17CAHDecHibiscusAvx13getTileEndCTUEjj
+ __ZN17CAHDecHibiscusAvx13populateTilesEv
+ __ZN17CAHDecHibiscusAvx14decHdrCLinAddrEj
+ __ZN17CAHDecHibiscusAvx14decHdrYLinAddrEj
+ __ZN17CAHDecHibiscusAvx14populateSlicesEj
+ __ZN17CAHDecHibiscusAvx14setVPInstrFifoEj
+ __ZN17CAHDecHibiscusAvx15freeWorkBuf_PPSEPv
+ __ZN17CAHDecHibiscusAvx15freeWorkBuf_SPSEv
+ __ZN17CAHDecHibiscusAvx15getTileIdxAboveEj
+ __ZN17CAHDecHibiscusAvx15getTileStartCTUEjj
+ __ZN17CAHDecHibiscusAvx15populateAvdWorkEj
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_PPSEPvS0_S0_
+ __ZN17CAHDecHibiscusAvx16allocWorkBuf_SPSEPv
+ __ZN17CAHDecHibiscusAvx16decodeBufferSizeEv
+ __ZN17CAHDecHibiscusAvx17getPPSWorkBufSizeEPvS0_
+ __ZN17CAHDecHibiscusAvx18populateClearTilesEv
+ __ZN17CAHDecHibiscusAvx20getUpscaleConvolveX0Eiii
+ __ZN17CAHDecHibiscusAvx21populateTileRegistersEP16AvxTileRegistersj
+ __ZN17CAHDecHibiscusAvx21updateCommonRegistersEj
+ __ZN17CAHDecHibiscusAvx22calc_az_left_tile_sizeEiiiiiiii
+ __ZN17CAHDecHibiscusAvx22calc_lf_left_tile_sizeEiiiiiiiii
+ __ZN17CAHDecHibiscusAvx22calc_lr_left_tile_sizeEiiiiiiiii
+ __ZN17CAHDecHibiscusAvx22getUpscaleConvolveStepEii
+ __ZN17CAHDecHibiscusAvx22ppsWorkBufSizeIncreaseEPvS0_
+ __ZN17CAHDecHibiscusAvx23populateAvxVPDependencyEv
+ __ZN17CAHDecHibiscusAvx23populateCommonRegistersEv
+ __ZN17CAHDecHibiscusAvx24populateAddressRegistersEv
+ __ZN17CAHDecHibiscusAvx24populatePictureRegistersEv
+ __ZN17CAHDecHibiscusAvx25populateSequenceRegistersEv
+ __ZN17CAHDecHibiscusAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
+ __ZN17CAHDecHibiscusAvx27populateDecryptionRegistersEv
+ __ZN17CAHDecHibiscusAvx4initEv
+ __ZN17CAHDecHibiscusAvxC2EP14CAVDAvxDecoder
+ __ZN17CAHDecHibiscusAvxD0Ev
+ __ZN17CAHDecHibiscusAvxD1Ev
+ __ZN17CAHDecHibiscusAvxD2Ev
+ __ZN17CAHDecHibiscusLgh11decHdrCSizeEj
+ __ZN17CAHDecHibiscusLgh11decHdrYSizeEj
+ __ZN17CAHDecHibiscusLgh11initPictureEjjb
+ __ZN17CAHDecHibiscusLgh12decodeBufferEv
+ __ZN17CAHDecHibiscusLgh12getSWRStrideEjjjj
+ __ZN17CAHDecHibiscusLgh12startPictureEj
+ __ZN17CAHDecHibiscusLgh13DecodePictureEj
+ __ZN17CAHDecHibiscusLgh13decHdrCStrideEv
+ __ZN17CAHDecHibiscusLgh13decHdrYStrideEv
+ __ZN17CAHDecHibiscusLgh13getTileEndCTUEjj
+ __ZN17CAHDecHibiscusLgh13populateTilesEv
+ __ZN17CAHDecHibiscusLgh14clearSegBufferEv
+ __ZN17CAHDecHibiscusLgh14decHdrCLinAddrEj
+ __ZN17CAHDecHibiscusLgh14decHdrYLinAddrEj
+ __ZN17CAHDecHibiscusLgh14populateSlicesEj
+ __ZN17CAHDecHibiscusLgh14setVPInstrFifoEj
+ __ZN17CAHDecHibiscusLgh15freeWorkBuf_PPSEPv
+ __ZN17CAHDecHibiscusLgh15freeWorkBuf_SPSEv
+ __ZN17CAHDecHibiscusLgh15getTileIdxAboveEj
+ __ZN17CAHDecHibiscusLgh15getTileStartCTUEjj
+ __ZN17CAHDecHibiscusLgh15populateAvdWorkEj
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_PPSEPvS0_S0_
+ __ZN17CAHDecHibiscusLgh16allocWorkBuf_SPSEPv
+ __ZN17CAHDecHibiscusLgh16decodeBufferSizeEv
+ __ZN17CAHDecHibiscusLgh21populateTileRegistersEP16LghTileRegisters
+ __ZN17CAHDecHibiscusLgh21updateCommonRegistersEj
+ __ZN17CAHDecHibiscusLgh23populateCommonRegistersEv
+ __ZN17CAHDecHibiscusLgh24populatePictureRegistersEv
+ __ZN17CAHDecHibiscusLgh25populateSequenceRegistersEv
+ __ZN17CAHDecHibiscusLgh4initEv
+ __ZN17CAHDecHibiscusLghC2EP14CAVDLghDecoder
+ __ZN17CAHDecHibiscusLghD0Ev
+ __ZN17CAHDecHibiscusLghD1Ev
+ __ZN17CAHDecHibiscusLghD2Ev
+ __ZN18CAHDecHibiscusHevc11decHdrCSizeEj
+ __ZN18CAHDecHibiscusHevc11decHdrYSizeEj
+ __ZN18CAHDecHibiscusHevc11initPictureEjjb
+ __ZN18CAHDecHibiscusHevc12decodeBufferEv
+ __ZN18CAHDecHibiscusHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
+ __ZN18CAHDecHibiscusHevc12getSWRStrideEjjjj
+ __ZN18CAHDecHibiscusHevc13decHdrCStrideEv
+ __ZN18CAHDecHibiscusHevc13decHdrYStrideEv
+ __ZN18CAHDecHibiscusHevc13getTileEndCTUEjj
+ __ZN18CAHDecHibiscusHevc14decHdrCLinAddrEj
+ __ZN18CAHDecHibiscusHevc14decHdrYLinAddrEj
+ __ZN18CAHDecHibiscusHevc14populateSlicesEj
+ __ZN18CAHDecHibiscusHevc14setVPInstrFifoEj
+ __ZN18CAHDecHibiscusHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
+ __ZN18CAHDecHibiscusHevc15freeWorkBuf_PPSEPv
+ __ZN18CAHDecHibiscusHevc15freeWorkBuf_SPSEv
+ __ZN18CAHDecHibiscusHevc15getTileIdxAboveEj
+ __ZN18CAHDecHibiscusHevc15getTileStartCTUEjj
+ __ZN18CAHDecHibiscusHevc15populateAvdWorkEj
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_PPSEPvS0_S0_
+ __ZN18CAHDecHibiscusHevc16allocWorkBuf_SPSEPv
+ __ZN18CAHDecHibiscusHevc16decodeBufferSizeEv
+ __ZN18CAHDecHibiscusHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
+ __ZN18CAHDecHibiscusHevc21updateCommonRegistersEj
+ __ZN18CAHDecHibiscusHevc22populateSliceRegistersEP18HevcSliceRegistersi
+ __ZN18CAHDecHibiscusHevc23populateCommonRegistersEv
+ __ZN18CAHDecHibiscusHevc24populatePictureRegistersEv
+ __ZN18CAHDecHibiscusHevc25populateSequenceRegistersEv
+ __ZN18CAHDecHibiscusHevc4initEv
+ __ZN18CAHDecHibiscusHevcD0Ev
+ __ZN18CAHDecHibiscusHevcD1Ev
+ __ZN18CAHDecHibiscusHevcD2Ev
+ __ZTI17CAHDecHibiscusAvc
+ __ZTI17CAHDecHibiscusAvx
+ __ZTI17CAHDecHibiscusLgh
+ __ZTI18CAHDecHibiscusHevc
+ __ZTS17CAHDecHibiscusAvc
+ __ZTS17CAHDecHibiscusAvx
+ __ZTS17CAHDecHibiscusLgh
+ __ZTS18CAHDecHibiscusHevc
+ __ZTV17CAHDecHibiscusAvc
+ __ZTV17CAHDecHibiscusAvx
+ __ZTV17CAHDecHibiscusLgh
+ __ZTV18CAHDecHibiscusHevc
CStrings:
+ "22:58:07"
+ "22:58:08"
+ "Oct 16 2025"
+ "int CAHDecHibiscusAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "int32_t CAHDecHibiscusAvx::getUpscaleConvolveStep(int, int)"
+ "int32_t CAHDecHibiscusAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "virtual int CAHDecHibiscusAvx::populatePictureRegisters()"
- "22:50:33"
- "22:50:34"
- "AppleAVD: %s(): Hibiscus AVD is not supported in this AppleAVD driver!!!"
- "Oct  8 2025"
- "createHibiscusAvcDecoder"
- "createHibiscusAvxDecoder"
- "createHibiscusHevcDecoder"
- "createHibiscusLghDecoder"

```
