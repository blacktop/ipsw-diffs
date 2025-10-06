## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x9c7e9c
-  __TEXT.__auth_stubs: 0x1510
-  __TEXT.__objc_methlist: 0x1130
-  __TEXT.__const: 0xb2e00
-  __TEXT.__cstring: 0x5a913
-  __TEXT.__gcc_except_tab: 0x14e0
-  __TEXT.__unwind_info: 0x43b0
+617.1.17.10.9
+  __TEXT.__text: 0x9c342c
+  __TEXT.__auth_stubs: 0x14e0
+  __TEXT.__objc_methlist: 0xf50
+  __TEXT.__const: 0xb2e10
+  __TEXT.__cstring: 0x5a475
+  __TEXT.__gcc_except_tab: 0x10dc
+  __TEXT.__unwind_info: 0x4260
   __TEXT.__eh_frame: 0x1db8
-  __TEXT.__objc_classname: 0x458
-  __TEXT.__objc_methname: 0x234e
-  __TEXT.__objc_methtype: 0x32cf
-  __TEXT.__objc_stubs: 0x18e0
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x15100
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__objc_classname: 0x40a
+  __TEXT.__objc_methname: 0x22f6
+  __TEXT.__objc_methtype: 0x3249
+  __TEXT.__objc_stubs: 0x18c0
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0x150e0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3018
-  __DATA_CONST.__objc_selrefs: 0x7c8
+  __DATA_CONST.__objc_const: 0x2b68
+  __DATA_CONST.__objc_selrefs: 0x7c0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__const: 0x1eb0
+  __AUTH_CONST.__const: 0x1ea0
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0xa98
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x230
+  __AUTH_CONST.__auth_got: 0xa80
+  __DATA.__objc_classrefs: 0x120
+  __DATA.__objc_superrefs: 0x98
+  __DATA.__objc_ivar: 0x1dc
   __DATA.__data: 0x4318
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x10
   __DATA.__common: 0x1942c
   __DATA.__bss: 0x31b98
   __DATA_DIRTY.__const: 0x1e810
-  __DATA_DIRTY.__objc_const: 0xa60
-  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA_DIRTY.__objc_const: 0x988
+  __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x798
-  __DATA_DIRTY.__bss: 0x2d10
+  __DATA_DIRTY.__bss: 0x2ce8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C27C0970-ADCD-3B32-823B-5A7F4E41B945
-  Functions: 18575
-  Symbols:   43791
-  CStrings:  9310
+  UUID: ABE07EBD-918C-37D0-8B56-DA47917213CF
+  Functions: 18522
+  Symbols:   43618
+  CStrings:  9273
 
Symbols:
+ -[RTCEncodedImage setTemporalIndex:]
+ -[RTCEncodedImage temporalIndex]
+ -[RTCVideoEncoderH264 enableL1T2ScalabilityMode]
+ -[WK_RTCLocalVideoH264H265Encoder initWithCodecInfo:scalabilityMode:]
+ GCC_except_table20
+ GCC_except_table21
+ _CFBooleanGetValue
+ _OBJC_IVAR_$_WK_RTCEncodedImage._temporalIndex
+ _OBJC_IVAR_$_WK_RTCVideoEncoderH264._enableL1T2ScalabilityMode
+ __Z20SetVTSessionPropertyP26OpaqueVTCompressionSessionPvPK10__CFStringd
+ __ZN6webrtc18createLocalEncoderERKNS_14SdpVideoFormatEbNS_27LocalEncoderScalabilityModeEU13block_pointerFvPKhmRKNS_22WebKitEncodedFrameInfoEEU13block_pointerFvS5_mE
+ __ZN6webrtc23copyPixelBufferForFrameERKNS_10VideoFrameE
+ __ZN6webrtc31createPixelBufferFromI420BufferEPKhmmmNS_16I420BufferLayoutE
+ __ZN6webrtc32createPixelBufferFromI420ABufferEPKhmmmNS_17I420ABufferLayoutE
+ __ZNK4absl16variant_internal17PerformVisitationIZN6webrtc14RTPSenderVideo13GetTemporalIdERKNS2_14RTPVideoHeaderEE16TemporalIdGetterJRKNS_7variantIJNS_9monostateENS2_17RTPVideoHeaderVP8ENS2_17RTPVideoHeaderVP9ENS2_18RTPVideoHeaderH264ENS2_27RTPVideoHeaderLegacyGenericEEEEEE3RunIJLm0EEJLm18446744073709551615EEEEhNSt3__117integral_constantIbLb1EEENS_16integer_sequenceImJXspT_EEEEDpNSK_ImXT0_EEE
+ __ZZN3rtc19webrtc_logging_impl11LogStreamerIJEE4CallIJNS0_3ValILNS0_10LogArgTypeE13ENS0_11LogMetadataEEENS4_ILS5_9EPKcEENS4_ILS5_10EPKNSt3__112basic_stringIcNSB_11char_traitsIcEENSB_9allocatorIcEEEEEESA_NS4_ILS5_7EdEESA_NS4_ILS5_1EiEEEEEvDpRKT_E1t
+ __ZZN3rtc19webrtc_logging_impl11LogStreamerIJEE4CallIJNS0_3ValILNS0_10LogArgTypeE13ENS0_11LogMetadataEEENS4_ILS5_9EPKcEENS4_ILS5_7EdEESA_SB_SA_NS4_ILS5_3ExEESA_SC_EEEvDpRKT_E1t
+ ____ZN6webrtc18createLocalEncoderERKNS_14SdpVideoFormatEbNS_27LocalEncoderScalabilityModeEU13block_pointerFvPKhmRKNS_22WebKitEncodedFrameInfoEEU13block_pointerFvS5_mE_block_invoke
+ _kCMSampleAttachmentKey_IsDependedOnByOthers
+ _kCVImageBufferTransferFunction_ITU_R_709_2
+ _kVTCompressionPropertyKey_BaseLayerFrameRateFraction
+ _objc_msgSend$enableL1T2ScalabilityMode
+ _objc_msgSend$initWithCodecInfo:scalabilityMode:
+ _objc_msgSend$setTemporalIndex:
+ _objc_msgSend$temporalIndex
+ _objc_retain_x3
- -[RTCCodecSpecificInfoH265 nativeCodecSpecificInfo]
- -[RTCCodecSpecificInfoH265 packetizationMode]
- -[RTCCodecSpecificInfoH265 setPacketizationMode:]
- -[RTCVideoDecoderH265 .cxx_destruct]
- -[RTCVideoDecoderH265 configureDecompressionSession]
- -[RTCVideoDecoderH265 dealloc]
- -[RTCVideoDecoderH265 decode:missingFrames:codecSpecificInfo:renderTimeMs:]
- -[RTCVideoDecoderH265 decodeData:size:timeStamp:]
- -[RTCVideoDecoderH265 destroyDecompressionSession]
- -[RTCVideoDecoderH265 flush]
- -[RTCVideoDecoderH265 implementationName]
- -[RTCVideoDecoderH265 init]
- -[RTCVideoDecoderH265 releaseDecoder]
- -[RTCVideoDecoderH265 resetDecompressionSession]
- -[RTCVideoDecoderH265 setAVCFormat:size:width:height:]
- -[RTCVideoDecoderH265 setCallback:]
- -[RTCVideoDecoderH265 setError:]
- -[RTCVideoDecoderH265 setVideoFormat:]
- -[RTCVideoDecoderH265 startDecodeWithNumberOfCores:]
- -[RTCVideoEncoderH265 .cxx_construct]
- -[RTCVideoEncoderH265 .cxx_destruct]
- -[RTCVideoEncoderH265 configureCompressionSession]
- -[RTCVideoEncoderH265 dealloc]
- -[RTCVideoEncoderH265 destroyCompressionSession]
- -[RTCVideoEncoderH265 encode:codecSpecificInfo:frameTypes:]
- -[RTCVideoEncoderH265 flush]
- -[RTCVideoEncoderH265 frameWasEncoded:flags:sampleBuffer:width:height:renderTimeMs:timestamp:rotation:]
- -[RTCVideoEncoderH265 implementationName]
- -[RTCVideoEncoderH265 initWithCodecInfo:]
- -[RTCVideoEncoderH265 releaseEncoder]
- -[RTCVideoEncoderH265 resetCompressionSession]
- -[RTCVideoEncoderH265 scalingSettings]
- -[RTCVideoEncoderH265 setBitrate:framerate:]
- -[RTCVideoEncoderH265 setBitrateBps:]
- -[RTCVideoEncoderH265 setCallback:]
- -[RTCVideoEncoderH265 setDescriptionCallback:]
- -[RTCVideoEncoderH265 setEncoderBitrateBps:]
- -[RTCVideoEncoderH265 setUseAnnexB:]
- -[RTCVideoEncoderH265 startEncodeWithSettings:numberOfCores:]
- -[WK_RTCLocalVideoH264H265Encoder initWithCodecInfo:]
- -[WK_RTCLocalVideoH264H265VP9Decoder initH265DecoderWithCallback:]
- GCC_except_table25
- _CFArrayCreate
- _CFDictionaryRemoveValue
- _CMVideoFormatDescriptionCreateFromHEVCParameterSets
- _CMVideoFormatDescriptionGetHEVCParameterSetAtIndex
- _OBJC_CLASS_$_WK_RTCCodecSpecificInfoH265
- _OBJC_CLASS_$_WK_RTCVideoDecoderH265
- _OBJC_CLASS_$_WK_RTCVideoEncoderH265
- _OBJC_IVAR_$_WK_RTCCodecSpecificInfoH265._packetizationMode
- _OBJC_IVAR_$_WK_RTCLocalVideoH264H265Encoder.m_h265Encoder
- _OBJC_IVAR_$_WK_RTCLocalVideoH264H265VP9Decoder.m_h265Decoder
- _OBJC_IVAR_$_WK_RTCVideoDecoderH265._callback
- _OBJC_IVAR_$_WK_RTCVideoDecoderH265._decompressionSession
- _OBJC_IVAR_$_WK_RTCVideoDecoderH265._error
- _OBJC_IVAR_$_WK_RTCVideoDecoderH265._useAVC
- _OBJC_IVAR_$_WK_RTCVideoDecoderH265._videoFormat
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._bitrateAdjuster
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._callback
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._codecInfo
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._compressionSession
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._descriptionCallback
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._encoderBitrateBps
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._height
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._mode
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._needsToSendDescription
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._nv12ScaleBuffer
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._profile
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._targetBitrateBps
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._useAnnexB
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265._width
- _OBJC_IVAR_$_WK_RTCVideoEncoderH265.framesLeft
- _OBJC_METACLASS_$_WK_RTCCodecSpecificInfoH265
- _OBJC_METACLASS_$_WK_RTCVideoDecoderH265
- _OBJC_METACLASS_$_WK_RTCVideoEncoderH265
- _VTCompressionSessionPrepareToEncodeFrames
- __OBJC_$_INSTANCE_METHODS_WK_RTCCodecSpecificInfoH265
- __OBJC_$_INSTANCE_METHODS_WK_RTCVideoDecoderH265
- __OBJC_$_INSTANCE_METHODS_WK_RTCVideoEncoderH265
- __OBJC_$_INSTANCE_VARIABLES_WK_RTCCodecSpecificInfoH265
- __OBJC_$_INSTANCE_VARIABLES_WK_RTCVideoDecoderH265
- __OBJC_$_INSTANCE_VARIABLES_WK_RTCVideoEncoderH265
- __OBJC_$_PROP_LIST_WK_RTCCodecSpecificInfoH265
- __OBJC_$_PROP_LIST_WK_RTCVideoDecoderH265
- __OBJC_$_PROP_LIST_WK_RTCVideoEncoderH265
- __OBJC_CLASS_PROTOCOLS_$_WK_RTCCodecSpecificInfoH265
- __OBJC_CLASS_PROTOCOLS_$_WK_RTCVideoDecoderH265
- __OBJC_CLASS_PROTOCOLS_$_WK_RTCVideoEncoderH265
- __OBJC_CLASS_RO_$_WK_RTCCodecSpecificInfoH265
- __OBJC_CLASS_RO_$_WK_RTCVideoDecoderH265
- __OBJC_CLASS_RO_$_WK_RTCVideoEncoderH265
- __OBJC_METACLASS_RO_$_WK_RTCCodecSpecificInfoH265
- __OBJC_METACLASS_RO_$_WK_RTCVideoDecoderH265
- __OBJC_METACLASS_RO_$_WK_RTCVideoEncoderH265
- __Z20SetVTSessionPropertyP26OpaqueVTCompressionSessionPvPK10__CFStringPK9__CFArray
- __Z31h265DecompressionOutputCallbackPvS_ijP10__CVBuffer6CMTimeS2_
- __ZN4absl16variant_internal26TypedThrowBadVariantAccessIRN6webrtc18RTPVideoHeaderH265EEET_v
- __ZN4absl17optional_internal13optional_dataIN6webrtc24FrameDependencyStructureELb0EEaSERKS4_
- __ZN6webrtc12_GLOBAL__N_116kPayloadNameH265E
- __ZN6webrtc12video_coding12_GLOBAL__N_115start_code_h265E
- __ZN6webrtc12video_coding20H265VpsSpsPpsTracker19CopyAndFixBitstreamEN3rtc9ArrayViewIKhLln4711EEEPNS_14RTPVideoHeaderE
- __ZN6webrtc18createLocalEncoderERKNS_14SdpVideoFormatEbU13block_pointerFvPKhmRKNS_22WebKitEncodedFrameInfoEEU13block_pointerFvS4_mE
- __ZN6webrtc20pixelBufferFromFrameERKNS_10VideoFrameE
- __ZN6webrtc22createLocalH265DecoderEU13block_pointerFvP10__CVBufferxxE
- __ZN6webrtc25pixelBufferFromI420BufferEPKhmmmNS_16I420BufferLayoutE
- __ZN6webrtc26pixelBufferFromI420ABufferEPKhmmmNS_17I420ABufferLayoutE
- __ZN6webrtc32CreateH265VideoFormatDescriptionEPKhm
- __ZN6webrtc32H265AnnexBBufferToCMSampleBufferEPKhmPK25opaqueCMFormatDescriptionPP20opaqueCMSampleBuffer
- __ZN6webrtc32H265CMSampleBufferToAnnexBBufferEP20opaqueCMSampleBufferbPN3rtc7BufferTIhLb0EEE
- __ZNK4absl16variant_internal17PerformVisitationIZN6webrtc14RTPSenderVideo13GetTemporalIdERKNS2_14RTPVideoHeaderEE16TemporalIdGetterJRKNS_7variantIJNS_9monostateENS2_17RTPVideoHeaderVP8ENS2_17RTPVideoHeaderVP9ENS2_18RTPVideoHeaderH264ENS2_18RTPVideoHeaderH265ENS2_27RTPVideoHeaderLegacyGenericEEEEEE3RunIJLm0EEJLm18446744073709551615EEEEhNSt3__117integral_constantIbLb1EEENS_16integer_sequenceImJXspT_EEEEDpNSL_ImXT0_EEE
- __ZNSt3__110unique_ptrI24RTCH265FrameDecodeParamsNS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__16__treeINS_12__value_typeIjN6webrtc12video_coding20H265VpsSpsPpsTracker7PpsInfoEEENS_19__map_value_compareIjS6_NS_4lessIjEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjN6webrtc12video_coding20H265VpsSpsPpsTracker7SpsInfoEEENS_19__map_value_compareIjS6_NS_4lessIjEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjN6webrtc12video_coding20H265VpsSpsPpsTracker7VpsInfoEEENS_19__map_value_compareIjS6_NS_4lessIjEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB7v160006ERKm
- __ZZN3rtc19webrtc_logging_impl11LogStreamerIJEE4CallIJNS0_3ValILNS0_10LogArgTypeE13ENS0_11LogMetadataEEENS4_ILS5_9EPKcEENS4_ILS5_10EPKNSt3__112basic_stringIcNSB_11char_traitsIcEENSB_9allocatorIcEEEEEESA_NS4_ILS5_1EiEESA_NS4_ILS5_12EPKvEEEEEvDpRKT_E1t
- ___66-[WK_RTCLocalVideoH264H265VP9Decoder initH265DecoderWithCallback:]_block_invoke
- ____ZN6webrtc18createLocalEncoderERKNS_14SdpVideoFormatEbU13block_pointerFvPKhmRKNS_22WebKitEncodedFrameInfoEEU13block_pointerFvS4_mE_block_invoke
- _kRTCVideoCodecH265Name
- _kVTCompressionPropertyKey_DataRateLimits
- _objc_msgSend$frameWasEncoded:flags:sampleBuffer:width:height:renderTimeMs:timestamp:rotation:
- _objc_msgSend$initH265DecoderWithCallback:
- _objc_msgSend$resetCompressionSession
- _objc_msgSend$setBitrateBps:
- _objc_msgSend$setEncoderBitrateBps:
CStrings:
+ "\x01"
+ "\x01a\xf0\xa1"
+ " above high loss threshold "
+ ", reducing rate from "
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__hash_table"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/array"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/deque"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/list"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/string"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/string_view"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/vector"
+ "@28@0:8@16C24"
+ "Loss "
+ "RTCVideoDecoderVTBVP9"
+ "Ti,N,V_temporalIndex"
+ "_enableL1T2ScalabilityMode"
+ "_temporalIndex"
+ "enableL1T2ScalabilityMode"
+ "initWithCodecInfo:scalabilityMode:"
+ "setTemporalIndex:"
+ "temporalIndex"
+ "{CodecSpecificInfo=i(CodecSpecificInfoUnion={CodecSpecificInfoVP8=BCBcB[3Q]Q[3Q]Q}{CodecSpecificInfoVP9=BBBBBCBBCQQB[8S][8S]{GofInfoVP9=Q[255C][255B][255C][255[3C]]S}C[3C]B}{CodecSpecificInfoH264=iCBB})B{optional<webrtc::GenericFrameInfo>=B(?={GenericFrameInfo=ii{InlinedVector<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={Storage<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={CompressedTuple<std::allocator<webrtc::DecodeTargetIndication>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={Storage<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={CompressedTuple<std::allocator<webrtc::CodecBufferUsage>, unsigned long>=Q}(Data={Allocated=^{CodecBufferUsage}Q}{Inlined=[64c]})}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{bitset<32UL>=Q}}{dummy_type=[208{empty_struct=}]})}{optional<webrtc::FrameDependencyStructure>=B(?={FrameDependencyStructure=iii{InlinedVector<int, 10UL, std::allocator<int>>={Storage<int, 10UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={Storage<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={CompressedTuple<std::allocator<webrtc::RenderResolution>, unsigned long>=Q}(Data={Allocated=^{RenderResolution}Q}{Inlined=[32c]})}}{vector<webrtc::FrameDependencyTemplate, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}^{FrameDependencyTemplate}{__compressed_pair<webrtc::FrameDependencyTemplate *, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}}}}{dummy_type=[128{empty_struct=}]})}{optional<webrtc::ScalabilityMode>=B(?=C{dummy_type=[1{empty_struct=}]})}}16@0:8"
- "\x011\x81"
- "\x01a\xf0\x91"
- " to array value: "
- "!append_vps_sps_pps || (sps != sps_data_.end() && pps != pps_data_.end())"
- ", vcpSession: "
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__hash_table"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/array"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/deque"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/list"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/string"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/string_view"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/vector"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/video_coding/h265_vps_sps_pps_tracker.cc"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/sdk/objc/components/video_codec/RTCVideoDecoderH265.mm"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/sdk/objc/components/video_codec/RTCVideoEncoderH265.mm"
- "@\"WK_RTCVideoDecoderH265\""
- "@\"WK_RTCVideoEncoderH265\""
- "Compression session failed to prepare encode frames."
- "Encode callback failed."
- "Failed to read VPS"
- "Failed to set data rate limit"
- "H265"
- "H265BufferToCMSampleBuffer CMBlockBufferCreateWithMemoryBlock failed with: "
- "H265BufferToCMSampleBuffer CMBlockBufferReplaceDataBytes failed with: "
- "H265BufferToCMSampleBuffer CMSampleBufferCreate failed with: "
- "No PPS with id "
- "No VPS with id "
- "Not enough space in H.265 codec header to insert SPS/PPS provided out-of-band."
- "RTCVideoDecoderH265"
- "Resetting compression session due to invalid pool."
- "Resolution: "
- "Unable to parse H265 encoded buffer"
- "WK_RTCCodecSpecificInfoH265"
- "WK_RTCVideoDecoderH265"
- "WK_RTCVideoEncoderH265"
- "[codecInfo.name isEqualToString:@\"H265\"]"
- "^{__CFString=}"
- "_compressionSession"
- "_nv12ScaleBuffer"
- "encodeParams->encoder"
- "frameWasEncoded:flags:sampleBuffer:width:height:renderTimeMs:timestamp:rotation:"
- "framesLeft"
- "h265 encode failed."
- "h265 encoder dropped a frame."
- "hvcC"
- "initH265DecoderWithCallback:"
- "m_h265Decoder"
- "m_h265Encoder"
- "params"
- "resetCompressionSession"
- "setBitrateBps:"
- "setEncoderBitrateBps:"
- "v60@0:8i16I20^{opaqueCMSampleBuffer=}24i32i36q40I48q52"
- "{CodecSpecificInfo=i(CodecSpecificInfoUnion={CodecSpecificInfoVP8=BCBcB[3Q]Q[3Q]Q}{CodecSpecificInfoVP9=BBBBBCBBCQQB[8S][8S]{GofInfoVP9=Q[255C][255B][255C][255[3C]]S}C[3C]B}{CodecSpecificInfoH264=iCBB}{CodecSpecificInfoH265=iB})B{optional<webrtc::GenericFrameInfo>=B(?={GenericFrameInfo=ii{InlinedVector<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={Storage<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={CompressedTuple<std::allocator<webrtc::DecodeTargetIndication>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={Storage<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={CompressedTuple<std::allocator<webrtc::CodecBufferUsage>, unsigned long>=Q}(Data={Allocated=^{CodecBufferUsage}Q}{Inlined=[64c]})}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{bitset<32UL>=Q}}{dummy_type=[208{empty_struct=}]})}{optional<webrtc::FrameDependencyStructure>=B(?={FrameDependencyStructure=iii{InlinedVector<int, 10UL, std::allocator<int>>={Storage<int, 10UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={Storage<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={CompressedTuple<std::allocator<webrtc::RenderResolution>, unsigned long>=Q}(Data={Allocated=^{RenderResolution}Q}{Inlined=[32c]})}}{vector<webrtc::FrameDependencyTemplate, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}^{FrameDependencyTemplate}{__compressed_pair<webrtc::FrameDependencyTemplate *, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}}}}{dummy_type=[128{empty_struct=}]})}{optional<webrtc::ScalabilityMode>=B(?=C{dummy_type=[1{empty_struct=}]})}}16@0:8"

```
