## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-959.1.0.0.0
-  __TEXT.__text: 0x162f04
-  __TEXT.__auth_stubs: 0xe80
-  __TEXT.__const: 0xc193
-  __TEXT.__gcc_except_tab: 0x940
-  __TEXT.__oslogstring: 0x140ce
-  __TEXT.__cstring: 0x522d
-  __TEXT.__unwind_info: 0x1b08
+960.0.0.0.0
+  __TEXT.__text: 0x1513c8
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__const: 0xc013
+  __TEXT.__gcc_except_tab: 0x8b4
+  __TEXT.__oslogstring: 0x145d3
+  __TEXT.__cstring: 0x529f
+  __TEXT.__unwind_info: 0x19c0
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x748
-  __AUTH_CONST.__const: 0x4d60
+  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__const: 0x4800
   __AUTH_CONST.__cfstring: 0x660
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 5C057A16-6778-34B4-9D56-AABFF61938FD
-  Functions: 3913
-  Symbols:   10481
-  CStrings:  1977
+  UUID: EA674FBC-6372-3611-A7C9-C24D4F4109E7
+  Functions: 3771
+  Symbols:   10005
+  CStrings:  1997
 
Symbols:
+ _FigHEVCBridge_DestroyHLSfMP4ParsingInfo
+ __ZN10AV1_Syntax16frame_header_obuEv.cold.2
+ __ZN10AV1_Syntax16frame_header_obuEv.cold.3
+ __ZN10AV1_Syntax16frame_header_obuEv.cold.4
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.1
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.2
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.3
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.4
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.5
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.6
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.7
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.8
+ __ZN10AV1_Syntax19uncompressed_headerEv.cold.9
+ __ZN10AV1_Syntax20frame_size_with_refsEv.cold.1
- __ZN18CAHDecDandelionAvc11decHdrCSizeEj
- __ZN18CAHDecDandelionAvc11decHdrYSizeEj
- __ZN18CAHDecDandelionAvc11initPictureEjjb
- __ZN18CAHDecDandelionAvc11initPictureEjjb.cold.1
- __ZN18CAHDecDandelionAvc12decodeBufferEv
- __ZN18CAHDecDandelionAvc12getSWRStrideEjjjj
- __ZN18CAHDecDandelionAvc13decHdrCStrideEv
- __ZN18CAHDecDandelionAvc13decHdrYStrideEv
- __ZN18CAHDecDandelionAvc13getTileEndCTUEjj
- __ZN18CAHDecDandelionAvc14decHdrCLinAddrEj
- __ZN18CAHDecDandelionAvc14decHdrYLinAddrEj
- __ZN18CAHDecDandelionAvc14populateSlicesEj
- __ZN18CAHDecDandelionAvc14setVPInstrFifoEj
- __ZN18CAHDecDandelionAvc15copyScalingListER15AvcScalingListsR13AvcQtMatCoeffPhS4_S4_i
- __ZN18CAHDecDandelionAvc15freeWorkBuf_PPSEPv
- __ZN18CAHDecDandelionAvc15freeWorkBuf_SPSEv
- __ZN18CAHDecDandelionAvc15getTileIdxAboveEj
- __ZN18CAHDecDandelionAvc15getTileStartCTUEjj
- __ZN18CAHDecDandelionAvc15populateAvdWorkEj
- __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_
- __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.1
- __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.2
- __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.3
- __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.4
- __ZN18CAHDecDandelionAvc16allocWorkBuf_PPSEPvS0_S0_.cold.5
- __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv
- __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv.cold.1
- __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv.cold.2
- __ZN18CAHDecDandelionAvc16allocWorkBuf_SPSEPv.cold.3
- __ZN18CAHDecDandelionAvc16decodeBufferSizeEv
- __ZN18CAHDecDandelionAvc21updateCommonRegistersEj
- __ZN18CAHDecDandelionAvc22populateSliceRegistersEP17AvcSliceRegistersi
- __ZN18CAHDecDandelionAvc23populateCommonRegistersEv
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.1
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.2
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.3
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.4
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.5
- __ZN18CAHDecDandelionAvc24populatePictureRegistersEv.cold.6
- __ZN18CAHDecDandelionAvc25AvcPicScalingListFallBackEP7sAvcSPSP7sAvcPPS
- __ZN18CAHDecDandelionAvc25AvcSeqScalingListFallBackEP7sAvcSPS
- __ZN18CAHDecDandelionAvc25populateSequenceRegistersEv
- __ZN18CAHDecDandelionAvc4initEv
- __ZN18CAHDecDandelionAvc4initEv.cold.1
- __ZN18CAHDecDandelionAvcC2EP14CAVDAvcDecoder
- __ZN18CAHDecDandelionAvcD0Ev
- __ZN18CAHDecDandelionAvcD1Ev
- __ZN18CAHDecDandelionAvcD2Ev
- __ZN18CAHDecDandelionAvx10isLfPadDisEv
- __ZN18CAHDecDandelionAvx11decHdrCSizeEj
- __ZN18CAHDecDandelionAvx11decHdrYSizeEj
- __ZN18CAHDecDandelionAvx11initPictureEjjb
- __ZN18CAHDecDandelionAvx12decodeBufferEv
- __ZN18CAHDecDandelionAvx12startPictureEj
- __ZN18CAHDecDandelionAvx12startPictureEj.cold.1
- __ZN18CAHDecDandelionAvx13DecodePictureEjj
- __ZN18CAHDecDandelionAvx13decHdrCStrideEv
- __ZN18CAHDecDandelionAvx13decHdrYStrideEv
- __ZN18CAHDecDandelionAvx13getTileEndCTUEjj
- __ZN18CAHDecDandelionAvx13populateTilesEv
- __ZN18CAHDecDandelionAvx14decHdrCLinAddrEj
- __ZN18CAHDecDandelionAvx14decHdrYLinAddrEj
- __ZN18CAHDecDandelionAvx14populateSlicesEj
- __ZN18CAHDecDandelionAvx14setVPInstrFifoEj
- __ZN18CAHDecDandelionAvx15freeWorkBuf_PPSEPv
- __ZN18CAHDecDandelionAvx15freeWorkBuf_SPSEv
- __ZN18CAHDecDandelionAvx15getTileIdxAboveEj
- __ZN18CAHDecDandelionAvx15getTileStartCTUEjj
- __ZN18CAHDecDandelionAvx15populateAvdWorkEj
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.1
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.10
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.11
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.12
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.13
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.2
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.3
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.4
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.5
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.6
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.7
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.8
- __ZN18CAHDecDandelionAvx16allocWorkBuf_PPSEPvS0_S0_.cold.9
- __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv
- __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.1
- __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.2
- __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.3
- __ZN18CAHDecDandelionAvx16allocWorkBuf_SPSEPv.cold.4
- __ZN18CAHDecDandelionAvx16decodeBufferSizeEv
- __ZN18CAHDecDandelionAvx17getPPSWorkBufSizeEPvS0_
- __ZN18CAHDecDandelionAvx18populateClearTilesEv
- __ZN18CAHDecDandelionAvx20getUpscaleConvolveX0Eiii
- __ZN18CAHDecDandelionAvx21populateTileRegistersEP16AvxTileRegistersj
- __ZN18CAHDecDandelionAvx21updateCommonRegistersEj
- __ZN18CAHDecDandelionAvx22calc_az_left_tile_sizeEiiiiiiii
- __ZN18CAHDecDandelionAvx22calc_lf_left_tile_sizeEiiiiiiiii
- __ZN18CAHDecDandelionAvx22calc_lr_left_tile_sizeEiiiiiiiii
- __ZN18CAHDecDandelionAvx22getUpscaleConvolveStepEii
- __ZN18CAHDecDandelionAvx22ppsWorkBufSizeIncreaseEPvS0_
- __ZN18CAHDecDandelionAvx23populateAvxVPDependencyEv
- __ZN18CAHDecDandelionAvx23populateCommonRegistersEv
- __ZN18CAHDecDandelionAvx24populateAddressRegistersEv
- __ZN18CAHDecDandelionAvx24populateAddressRegistersEv.cold.1
- __ZN18CAHDecDandelionAvx24populatePictureRegistersEv
- __ZN18CAHDecDandelionAvx25populateSequenceRegistersEv
- __ZN18CAHDecDandelionAvx27calc_lf_above_pix_tile_sizeEiiiiiiii
- __ZN18CAHDecDandelionAvx27populateDecryptionRegistersEv
- __ZN18CAHDecDandelionAvx4initEv
- __ZN18CAHDecDandelionAvx4initEv.cold.1
- __ZN18CAHDecDandelionAvx4initEv.cold.2
- __ZN18CAHDecDandelionAvx4initEv.cold.3
- __ZN18CAHDecDandelionAvxC2EP14CAVDAvxDecoder
- __ZN18CAHDecDandelionAvxD0Ev
- __ZN18CAHDecDandelionAvxD1Ev
- __ZN18CAHDecDandelionAvxD2Ev
- __ZN18CAHDecDandelionLgh11decHdrCSizeEj
- __ZN18CAHDecDandelionLgh11decHdrYSizeEj
- __ZN18CAHDecDandelionLgh11initPictureEjjb
- __ZN18CAHDecDandelionLgh12decodeBufferEv
- __ZN18CAHDecDandelionLgh12getSWRStrideEjjjj
- __ZN18CAHDecDandelionLgh12startPictureEj
- __ZN18CAHDecDandelionLgh12startPictureEj.cold.1
- __ZN18CAHDecDandelionLgh13DecodePictureEj
- __ZN18CAHDecDandelionLgh13decHdrCStrideEv
- __ZN18CAHDecDandelionLgh13decHdrYStrideEv
- __ZN18CAHDecDandelionLgh13getTileEndCTUEjj
- __ZN18CAHDecDandelionLgh13populateTilesEv
- __ZN18CAHDecDandelionLgh14clearSegBufferEv
- __ZN18CAHDecDandelionLgh14decHdrCLinAddrEj
- __ZN18CAHDecDandelionLgh14decHdrYLinAddrEj
- __ZN18CAHDecDandelionLgh14populateSlicesEj
- __ZN18CAHDecDandelionLgh14setVPInstrFifoEj
- __ZN18CAHDecDandelionLgh15freeWorkBuf_PPSEPv
- __ZN18CAHDecDandelionLgh15freeWorkBuf_SPSEv
- __ZN18CAHDecDandelionLgh15getTileIdxAboveEj
- __ZN18CAHDecDandelionLgh15getTileStartCTUEjj
- __ZN18CAHDecDandelionLgh15populateAvdWorkEj
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.1
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.2
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.3
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.4
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.5
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.6
- __ZN18CAHDecDandelionLgh16allocWorkBuf_PPSEPvS0_S0_.cold.7
- __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv
- __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.1
- __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.2
- __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.3
- __ZN18CAHDecDandelionLgh16allocWorkBuf_SPSEPv.cold.4
- __ZN18CAHDecDandelionLgh16decodeBufferSizeEv
- __ZN18CAHDecDandelionLgh21populateTileRegistersEP16LghTileRegisters
- __ZN18CAHDecDandelionLgh21updateCommonRegistersEj
- __ZN18CAHDecDandelionLgh23populateCommonRegistersEv
- __ZN18CAHDecDandelionLgh24populatePictureRegistersEv
- __ZN18CAHDecDandelionLgh25populateSequenceRegistersEv
- __ZN18CAHDecDandelionLgh4initEv
- __ZN18CAHDecDandelionLgh4initEv.cold.1
- __ZN18CAHDecDandelionLgh4initEv.cold.2
- __ZN18CAHDecDandelionLgh4initEv.cold.3
- __ZN18CAHDecDandelionLghC2EP14CAVDLghDecoder
- __ZN18CAHDecDandelionLghD0Ev
- __ZN18CAHDecDandelionLghD1Ev
- __ZN18CAHDecDandelionLghD2Ev
- __ZN19CAHDecDandelionHevc11decHdrCSizeEj
- __ZN19CAHDecDandelionHevc11decHdrYSizeEj
- __ZN19CAHDecDandelionHevc11initPictureEjjb
- __ZN19CAHDecDandelionHevc11initPictureEjjb.cold.1
- __ZN19CAHDecDandelionHevc12decodeBufferEv
- __ZN19CAHDecDandelionHevc12getMVmemInfoEiP20_avd_client_mem_infoPj
- __ZN19CAHDecDandelionHevc12getSWRStrideEjjjj
- __ZN19CAHDecDandelionHevc13decHdrCStrideEv
- __ZN19CAHDecDandelionHevc13decHdrYStrideEv
- __ZN19CAHDecDandelionHevc13getTileEndCTUEjj
- __ZN19CAHDecDandelionHevc14decHdrCLinAddrEj
- __ZN19CAHDecDandelionHevc14decHdrYLinAddrEj
- __ZN19CAHDecDandelionHevc14populateSlicesEj
- __ZN19CAHDecDandelionHevc14setVPInstrFifoEj
- __ZN19CAHDecDandelionHevc15copyScalingListER16HevcScalingListsR14HevcQtMatCoeffjR24hevc_scaling_list_data_t
- __ZN19CAHDecDandelionHevc15freeWorkBuf_PPSEPv
- __ZN19CAHDecDandelionHevc15freeWorkBuf_SPSEv
- __ZN19CAHDecDandelionHevc15getTileIdxAboveEj
- __ZN19CAHDecDandelionHevc15getTileStartCTUEjj
- __ZN19CAHDecDandelionHevc15populateAvdWorkEj
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.1
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.10
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.2
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.3
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.4
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.5
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.6
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.7
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.8
- __ZN19CAHDecDandelionHevc16allocWorkBuf_PPSEPvS0_S0_.cold.9
- __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv
- __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv.cold.1
- __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv.cold.2
- __ZN19CAHDecDandelionHevc16allocWorkBuf_SPSEPv.cold.3
- __ZN19CAHDecDandelionHevc16decodeBufferSizeEv
- __ZN19CAHDecDandelionHevc17getTileHdrMemInfoEiP17_Tile_hdr_buffs_t
- __ZN19CAHDecDandelionHevc21updateCommonRegistersEj
- __ZN19CAHDecDandelionHevc22populateSliceRegistersEP18HevcSliceRegistersi
- __ZN19CAHDecDandelionHevc23populateCommonRegistersEv
- __ZN19CAHDecDandelionHevc24populatePictureRegistersEv
- __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.1
- __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.2
- __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.3
- __ZN19CAHDecDandelionHevc24populatePictureRegistersEv.cold.4
- __ZN19CAHDecDandelionHevc25populateSequenceRegistersEv
- __ZN19CAHDecDandelionHevc4initEv
- __ZN19CAHDecDandelionHevc4initEv.cold.1
- __ZN19CAHDecDandelionHevcD0Ev
- __ZN19CAHDecDandelionHevcD1Ev
- __ZN19CAHDecDandelionHevcD2Ev
- __ZTI18CAHDecDandelionAvc
- __ZTI18CAHDecDandelionAvx
- __ZTI18CAHDecDandelionLgh
- __ZTI19CAHDecDandelionHevc
- __ZTS18CAHDecDandelionAvc
- __ZTS18CAHDecDandelionAvx
- __ZTS18CAHDecDandelionLgh
- __ZTS19CAHDecDandelionHevc
- __ZTV18CAHDecDandelionAvc
- __ZTV18CAHDecDandelionAvx
- __ZTV18CAHDecDandelionLgh
- __ZTV19CAHDecDandelionHevc
CStrings:
+ "/Library/Caches/com.apple.xbs/A8236C58-8E6F-4E5F-AB4B-9E8CC968EA13/TemporaryDirectory.5CrZYO/Sources/AppleAVD/framework/AppleAVDFrameReceiver.cpp"
+ "21:47:15"
+ "21:47:16"
+ "21:47:17"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Invalid value of current_frame_id.\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Minimum tile width requirement not satisfied.\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Reference buffer frame ID mismatch.\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Reference buffer frame ID mismatch. %d %d %d %d\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Reference frame not valid for referencing.\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Referenced frame has incompatible color format.\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Sequence header has changed without a keyframe.\n"
+ "AppleAVD: ERROR: %{public}s(): Corrupted frame. Still pictures must be coded as shown keyframes.\n"
+ "AppleAVD: ERROR: %{public}s(): Unsupported bitstream. Buffer does not contain a showable frame.\n"
+ "AppleAVD: ERROR: %{public}s(): Unsupported bitstream. Intra only frames cannot have refresh flags 0xFF.\n"
+ "AppleAVD: ERROR: %{public}s(): Unsupported bitstream. Reference frame has invalid dimensions\n"
+ "AppleAVD: ERROR: %{public}s(): check_trailing_bits\n"
+ "AppleAVD: ERROR: %{public}s(): obu_byte_alignment\n"
+ "AppleAVD: ERROR: %{public}s(): uncompressed_header\n"
+ "AppleAVD: INFO: %{public}s(): Dandelion AVD is not supported in this AppleAVD driver!!!\n"
+ "Feb 17 2026"
+ "createDandelionAvcDecoder"
+ "createDandelionAvxDecoder"
+ "createDandelionHevcDecoder"
+ "createDandelionLghDecoder"
- "/Library/Caches/com.apple.xbs/A30A585E-04BF-43D1-A564-8C4BEA216D97/TemporaryDirectory.4xfxLW/Sources/AppleAVD/framework/AppleAVDFrameReceiver.cpp"
- "00:16:35"
- "00:16:36"
- "Feb  5 2026"

```
