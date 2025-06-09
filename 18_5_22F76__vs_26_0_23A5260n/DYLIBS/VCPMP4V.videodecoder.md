## VCPMP4V.videodecoder

> `/System/Library/VideoDecoders/VCPMP4V.videodecoder`

```diff

 624.1.0.0.0
-  __TEXT.__text: 0x21890
+  __TEXT.__text: 0x21658
   __TEXT.__auth_stubs: 0x400
   __TEXT.__const: 0x15550
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x2c5
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__cstring: 0xa9
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0x88
   __AUTH_CONST.__auth_got: 0x208

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 142E9A38-1E18-35CF-B5A5-12F8D8186200
-  Functions: 305
-  Symbols:   749
-  CStrings:  38
+  UUID: 1543B6A9-C073-3E8D-A613-7FE29C02DD73
+  Functions: 304
+  Symbols:   747
+  CStrings:  18
 
Symbols:
+ _FigSignalErrorAtGM
+ __ZN14CBitStreamDeco8BarfBitsEj
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ15VCPMP4VRegisterE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ23VCPMP4VRegisterInternalE3$_0EEEEEvPv
- _FigSignalErrorAt3
- _OUTLINED_FUNCTION_0
- __ZN14CBitStreamDeco8PeekBitsEi
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZ15VCPMP4VRegisterE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZ23VCPMP4VRegisterInternalE3$_0EEEEEvPv
Functions:
~ __Z20InterpolateWarpedPixPhiiiiiiPiS0_S_ : 244 -> 248
- __ZN14CBitStreamDeco8PeekBitsEi
~ __ZN14CBitStreamDeco13NextStartCodeEv : 132 -> 68
~ __Z12DecHeaderVOLP14CBitStreamDecoP13INSTANCE_DECO : 4648 -> 4672
~ __Z12DecHeaderGOVP14CBitStreamDecoP13INSTANCE_DECO : 616 -> 668
~ __Z12DecHeaderVOPP14CBitStreamDecoP13INSTANCE_DECO : 1776 -> 1780
+ __ZN14CBitStreamDeco8BarfBitsEj
~ __Z22InitDecodeUMVMVDTablesPP18DECODEUMVMVDTABLES : 520 -> 528
~ _MPEG4VideoDecoder_CreateInstance : 220 -> 180
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription : 1824 -> 1700
~ __ZL29MPEG4VideoDecoder_DecodeFrameP20OpaqueVTVideoDecoderP25OpaqueVTVideoDecoderFrameP20opaqueCMSampleBufferjPj : 756 -> 660
- _OUTLINED_FUNCTION_0
~ __ZL16ReadAVideoPacketPihP5frameS1_P13INSTANCE_DECO : 9876 -> 9884
~ __Z18S_BuildGammaTablesPhS_ii : 800 -> 820
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.1 : 120 -> 76
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.2 : 120 -> 76
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.3 : 120 -> 76
~ __ZL30MPEG4VideoDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.4 : 120 -> 76
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "CFDataCreate failed"
- "CVPixelBufferLockBaseAddress failed"
- "CVPixelBufferPoolCreatePixelBuffer failed"
- "ESDS not found"
- "ESDS too large"
- "FigDerivedObjectCreate failed"
- "MPEG4 can't find its config record"
- "MPEG4DMPR_Decompress failed"
- "MPEG4VideoDecoder.cpp"
- "MPEG4VideoDecoder_CreateInstance"
- "MPEG4VideoDecoder_DecodeFrame"
- "MPEG4_GetVideoDecoderSpecificInfo"
- "config record too large"
- "createMPEG4LibInstance"
- "err"
- "frame data too large"
- "kVTAllocationFailedErr"
- "kVTVideoDecoderBadDataErr"
- "kVTVideoDecoderUnsupportedDataFormatErr"
- "nonconformant bit stream"

```
