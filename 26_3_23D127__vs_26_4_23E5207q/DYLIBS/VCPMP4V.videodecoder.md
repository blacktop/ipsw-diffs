## VCPMP4V.videodecoder

> `/System/Library/VideoDecoders/VCPMP4V.videodecoder`

```diff

 624.1.0.0.0
-  __TEXT.__text: 0x21658
+  __TEXT.__text: 0x20b88
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__const: 0x15550
+  __TEXT.__const: 0x15560
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__cstring: 0xa9
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0x88
   __AUTH_CONST.__auth_got: 0x208

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CBA1DEB7-00BD-3FD4-BF3D-C4594896B924
-  Functions: 304
-  Symbols:   747
+  UUID: C0931863-2379-3913-BFB3-516F2759A1B7
+  Functions: 305
+  Symbols:   749
   CStrings:  18
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ __ZNSt3__117__call_once_proxyB9foe210106INS_5tupleIJOZ15VCPMP4VRegisterE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe210106INS_5tupleIJOZ23VCPMP4VRegisterInternalE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ15VCPMP4VRegisterE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ23VCPMP4VRegisterInternalE3$_0EEEEEvPv
Functions:
~ __Z8MC_2H_1VPhiPKhiPKsiS1_ : 304 -> 268
~ __Z16InterpolateFramePhS_S_iiiiil : 4656 -> 4784
~ __Z19SetGMCWarpingParamsiiPiS_iiPd : 192 -> 180
~ __Z11GetPowerOf2i : 48 -> 44
~ __Z27GetTranslationWarpingParamsiPiS_Pd : 56 -> 48
~ __Z22GetAffineWarpingParamsiiPiS_iiPd : 660 -> 656
~ __Z8GetMVGMCiiiiiPiS_iS_S_ : 216 -> 212
~ __ZL16Get_HalfPel_LeftPhS_iiPKhh : 552 -> 548
~ __ZL18Get_HalfPel_BottomPhS_iiPKhh : 1120 -> 1040
~ _GetPredictor4MV : 372 -> 352
~ __Z12DecHeaderVOLP14CBitStreamDecoP13INSTANCE_DECO : 4672 -> 4648
~ __ZL35DefineVOPComplexityEstimationHeaderP14CBitStreamDecoP12picture_info : 3824 -> 3688
~ __Z17DecHeaderVOPshortP14CBitStreamDecoP11source_infoP12picture_info : 1416 -> 1456
~ __Z20DecHeaderVideoPacketP14CBitStreamDecoP12picture_info : 1976 -> 1972
~ __Z12EncodeUMVMVDiPtPhP15ENCUMVMVDTABLES : 160 -> 156
~ __Z19InitEncUMVMVDTablesPP15ENCUMVMVDTABLES : 304 -> 296
~ __Z22InitDecodeUMVMVDTablesPP18DECODEUMVMVDTABLES : 528 -> 512
~ __Z10idct1DC1ACPsS_jj : 1672 -> 1676
~ __Z10MPEG4_IDCTPsS_i : 1004 -> 1008
~ __Z15Y420ToY422_yuvsPhS_S_PittttiS_S_ : 232 -> 240
~ __Z15Y420ToY422_2vuyPhS_S_PittttiS_S_ : 240 -> 248
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription : 1700 -> 1552
~ __ZL29MPEG4VideoDecoder_DecodeFrameP20OpaqueVTVideoDecoderP25OpaqueVTVideoDecoderFrameP20opaqueCMSampleBufferjPj : 660 -> 648
~ __ZL13unpack_headerPPKhhS1_ : 128 -> 124
~ __ZL26unpack_DecoderSpecificInfoPPKhPPK8__CFDataS0_ : 188 -> 200
+ _OUTLINED_FUNCTION_0
~ __Z15DeringFrameFastP5framePK19PostFilterSemaphore : 1144 -> 1140
~ __Z18InitIntraPredictorPP15intra_predictort : 552 -> 308
~ __Z18KillIntraPredictorPP15intra_predictor : 140 -> 132
~ __Z28DetermineIntraPredictionModeP15intra_predictorii : 120 -> 116
~ __Z14ReconAndUpdateP15intra_predictorPsiiiii : 484 -> 480
~ _MPEG4DMPR_ReadHeaders : 808 -> 816
~ __Z13DecodeMBInteriiPsS_hP16macroblock_stuffP13INSTANCE_DECO : 1328 -> 1332
~ __ZL16ReadAVideoPacketPihP5frameS1_P13INSTANCE_DECO : 9884 -> 9348
~ __ZL21GrabBlockAndIQuantiseP16macroblock_stuffihP13INSTANCE_DECO : 1712 -> 1696
~ __ZL31DecodeBlockInterDataPartitionedPhPsS0_iiihiiP13INSTANCE_DECO : 2172 -> 2112
~ _InitInstanceGlobalsDecoGenenral : 1328 -> 1144
~ _KillInstanceGlobalsDeco : 824 -> 736
~ __Z18S_BuildGammaTablesPhS_ii : 820 -> 824
~ __Z8DrawGridP5frame : 224 -> 220
~ __Z12DecWarpingMVP14CBitStreamDeco : 720 -> 724
~ _NewBuffer_U8 : 208 -> 200
~ _NewBuffer_S16 : 212 -> 192
~ _InitFrame : 528 -> 416
~ _DelBuffer_U8 : 100 -> 92
~ _DelBuffer_S16 : 96 -> 88
~ _KillFrame : 128 -> 112
~ _SideExtendBuffer_U8 : 544 -> 556
~ _SideExtendBuffer_S16 : 1100 -> 580
~ _GetFramesYChannelDiffMAD : 592 -> 252
~ _SetBufferAllVal_S16 : 296 -> 28
~ _View_MV : 564 -> 592
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.1 : 76 -> 56
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.2 : 76 -> 56
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.3 : 76 -> 56
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.4 : 76 -> 56

```
