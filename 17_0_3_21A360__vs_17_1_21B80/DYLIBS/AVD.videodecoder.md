## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-732.5.0.0.0
-  __TEXT.__text: 0xc12ac
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__gcc_except_tab: 0x934
-  __TEXT.__oslogstring: 0xcb99
-  __TEXT.__cstring: 0x5240
-  __TEXT.__const: 0xb7a6
-  __TEXT.__unwind_info: 0x1650
+735.6.0.0.0
+  __TEXT.__text: 0xc2050
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__gcc_except_tab: 0x938
+  __TEXT.__const: 0xb7b6
+  __TEXT.__oslogstring: 0xcef4
+  __TEXT.__cstring: 0x530c
+  __TEXT.__unwind_info: 0x1664
   __TEXT.__eh_frame: 0x268
-  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__auth_got: 0x710
+  __AUTH_CONST.__auth_got: 0x718
   __DATA.__bss: 0x11
   __DATA.__common: 0x50
   __DATA_DIRTY.__const: 0x2098

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1673
-  Symbols:   3930
-  CStrings:  1640
+  Functions: 1676
+  Symbols:   3938
+  CStrings:  1663
 
Symbols:
+ _IOSurfaceSetBulkAttachments2
+ __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPooliii
+ __ZN10LGH_Syntax9init_boolEm
+ __ZN14CAVDAvxDecoder13copySeqParamsEP14avd_seq_paramsP10av1_header
+ __ZN14CAVDAvxDecoder6VAInitEv
+ __ZN14CAVDLghDecoder6VAInitEv
+ _kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality
- __ZL16find_closest_refPP15HevcPictureInfoii
- __ZN10BufferPool14initBufferPoolEPvP19__CVPixelBufferPoolii
CStrings:
+ "02:21:15"
+ "02:21:16"
+ "AppleAVD: %s(): Allocating new AppleAVDCommandBuilder\n"
+ "AppleAVD: %s(): Allocating new AppleAVDCommandBuilder failed\n"
+ "AppleAVD: %s(): Failed to map pixel buffer! - error: 0x%x\n"
+ "AppleAVD: %s(): IOSurfaceSetBulkAttachments2 returned error (0x%x)\n"
+ "AppleAVD: %s(): KVASetKEYBParams"
+ "AppleAVD: %s(): KVASetLKParams"
+ "AppleAVD: %s(): WARNING, coded size has changed!"
+ "AppleAVD: %s(): cannot find PPS"
+ "AppleAVD: %s(): clientID : %2d, #### <WARNING> frameNum:%d m_cur_pic_info->chroma_format:%d m_orig_chroma_format_idc:%d"
+ "AppleAVD: %s(): failed cmdBuilder->createDecoder!\n"
+ "AppleAVD: %s(): isRandomAccessSkipPicture skip"
+ "AppleAVD: AppleAVD_FghrnDecoder ERROR: kAppleAVDGetSequenceParams : Could not get Params"
+ "AppleAVD: ERROR: %s() - Sync Decode not enabled for FT chroma deblocking filter\n"
+ "AppleAVD: ERROR: %s(): VAInit failed"
+ "AppleAVD: ERROR: %s(): hevc - unpermitted non-VCL NAL following last VCL NAL\n"
+ "AppleAVD: ERROR: %s(): m_av1_header allocation failed"
+ "AppleAVD: ERROR: %s(): m_cur_pic_info allocation failed"
+ "AppleAVD: ERROR: %s(): m_dec_bufs allocation failed"
+ "AppleAVD: ERROR: %s(): m_dec_q allocation failed"
+ "AppleAVD: ERROR: %s(): m_disp_q allocation failed"
+ "AppleAVD: ERROR: %s(): m_out_q allocation failed"
+ "AppleAVD: ERROR: AppleAVD_H264Decoder - Non-mod16 VRA dimensions with width %d, height %d\n"
+ "AppleAVD: ERROR: AppleAVD_HEVCDecoder - Non-mod16 VRA dimensions with width %d, height %d\n"
+ "AppleAVD: WARNING: %s(): bad PPS index %d"
+ "AppleAVD: WARNING: %s(): bad SPS index %d"
+ "CAVDAvxDecoder::CAVDAvxDecoder(void *, uint32_t, bool)"
+ "CAVDLghDecoder::CAVDLghDecoder(void *, uint32_t, bool)"
+ "Oct 10 2023"
+ "VASetParams"
+ "activatePS"
+ "getCVPixelBuffer"
+ "int CAVDAvxDecoder::VAInit()"
+ "int CAVDLghDecoder::VAInit()"
+ "mapPixelBuffer"
- "17:18:56"
- "17:18:57"
- "AVD_CheckWireLimit"
- "AppleAVD: %s(): Allocating new AppleAVDCommandBuilder"
- "AppleAVD: %s(): Allocating new AppleAVDCommandBuilder failed"
- "AppleAVD: %s(): Failed to map pixel buffer! frameNum %d - error: 0x%x\n"
- "AppleAVD: %s(): clientID : %2d, #### <WARNING> frameNum:%d m_cur_pic_info.chroma_format:%d m_orig_chroma_format_idc:%d"
- "AppleAVD: %s(): failed cmdBuilder->createDecoder!"
- "AppleAVD: %s(): isRandomAccessSkipPicture fail"
- "AppleAVD: AppleAVD_H264Decoder - Non-mod16 VRA dimensions with width %d, height %d\n"
- "AppleAVD: AppleAVD_HEVCDecoder - Non-mod16 VRA dimensions with width %d, height %d\n"
- "AppleAVD: WARNING: missing reference \n"
- "Sep 30 2023"

```
