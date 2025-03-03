## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-620.2.4.10.7
-  __TEXT.__text: 0xa670f8
-  __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_methlist: 0x11c4
-  __TEXT.__cstring: 0x4ba38
-  __TEXT.__const: 0x820a8
-  __TEXT.__gcc_except_tab: 0x186c
-  __TEXT.__unwind_info: 0x3a50
-  __TEXT.__eh_frame: 0x1c58
+621.1.13.10.4
+  __TEXT.__text: 0xa69430
+  __TEXT.__auth_stubs: 0x1490
+  __TEXT.__objc_methlist: 0x14e4
+  __TEXT.__const: 0xb3a98
+  __TEXT.__cstring: 0x4b952
+  __TEXT.__gcc_except_tab: 0x181c
+  __TEXT.__unwind_info: 0x35c0
+  __TEXT.__eh_frame: 0x1118
   __TEXT.__objc_classname: 0x45a
-  __TEXT.__objc_methname: 0x282e
-  __TEXT.__objc_methtype: 0x4059
+  __TEXT.__objc_methname: 0x27ee
+  __TEXT.__objc_methtype: 0x41fe
   __TEXT.__objc_stubs: 0x19e0
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x15ee8
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x15f20
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x808
+  __DATA_CONST.__objc_selrefs: 0x890
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0xa90
+  __AUTH_CONST.__auth_got: 0xa58
   __AUTH_CONST.__auth_ptr: 0x368
-  __AUTH_CONST.__const: 0x1fe00
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x3b88
+  __AUTH_CONST.__const: 0x1f9e0
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0x35d8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH.__data: 0x20
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
   __DATA.__objc_ivar: 0x250
-  __DATA.__data: 0x43b8
-  __DATA.__bss: 0x30e98
-  __DATA.__common: 0x1ed80
+  __DATA.__data: 0x1a08
+  __DATA.__bss: 0x318c8
+  __DATA.__common: 0x1ed60
   __DATA_DIRTY.__objc_data: 0xa50
-  __DATA_DIRTY.__data: 0x340
-  __DATA_DIRTY.__bss: 0x2b20
+  __DATA_DIRTY.__data: 0x420
+  __DATA_DIRTY.__bss: 0x2088
   __DATA_DIRTY.__common: 0x468
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18605
-  Symbols:   18717
-  CStrings:  9529
+  Functions: 17993
+  Symbols:   18666
+  CStrings:  9524
 
Symbols:
+ __ZN3rtc14ReceivedPacketC1ENS_9ArrayViewIKhLln4711EEERKNS_13SocketAddressENSt3__18optionalIN6webrtc9TimestampEEENS9_10EcnMarkingENS0_14DecryptionInfoE
+ __ZN6webrtc24videoDecoderTaskCompleteEPvjP10__CVBuffer
+ __ZN6webrtc24videoDecoderTaskCompleteEPvjS0_PFP10__CVBufferS0_EPFvS0_Eii
+ __ZN8mkvmuxer10IMkvWriterC2Ev
+ __ZN8mkvmuxer10IMkvWriterD2Ev
+ __ZN8mkvmuxer11SegmentInfo14set_muxing_appEPKc
+ __ZN8mkvmuxer11SegmentInfo15set_writing_appEPKc
+ __ZN8mkvmuxer5Track12set_codec_idEPKc
+ __ZN8mkvmuxer5Track15SetCodecPrivateEPKhy
+ __ZN8mkvmuxer6Tracks11kAv1CodecIdE
+ __ZN8mkvmuxer6Tracks11kVp8CodecIdE
+ __ZN8mkvmuxer6Tracks11kVp9CodecIdE
+ __ZN8mkvmuxer6Tracks12kOpusCodecIdE
+ __ZN8mkvmuxer7Segment10OutputCuesEb
+ __ZN8mkvmuxer7Segment13AddAudioTrackEiii
+ __ZN8mkvmuxer7Segment13AddVideoTrackEiii
+ __ZN8mkvmuxer7Segment26ForceNewClusterOnNextFrameEv
+ __ZN8mkvmuxer7Segment4InitEPNS_10IMkvWriterE
+ __ZN8mkvmuxer7Segment8AddFrameEPKhyyyb
+ __ZN8mkvmuxer7Segment8FinalizeEv
+ __ZN8mkvmuxer7SegmentC1Ev
+ __ZN8mkvmuxer7SegmentD1Ev
+ __ZNK6webrtc20DataChannelInterface8priorityEv
+ __ZNK8mkvmuxer7Segment16GetTrackByNumberEy
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZnamRKSt9nothrow_t
+ _atanf
+ _frexp
+ _ldexp
+ _rand_r
+ _strcat
+ _strcpy
+ _sysctlbyname
- _CFArrayAppendValue
- _CFArrayCreateMutable
- _CFDataGetTypeID
- _CFDictionaryGetTypeID
- _CFGetTypeID
- _CMBaseObjectGetDerivedStorage
- _CMDerivedObjectCreate
- _CMFormatDescriptionGetExtensions
- _VTDecoderSessionEmitDecodedFrame
- _VTDecoderSessionGetPixelBufferPool
- _VTDecoderSessionSetPixelBufferAttributes
- _VTRegisterVideoDecoder
- _VTVideoDecoderGetClassID
- __ZN3rtc14ReceivedPacketC1ENS_9ArrayViewIKhLln4711EEERKNS_13SocketAddressENSt3__18optionalIN6webrtc9TimestampEEENS_10EcnMarkingENS0_14DecryptionInfoE
- __ZN3rtc17AsyncPacketSocket30RegisterReceivedPacketCallbackEN4absl12AnyInvocableIFvPS0_RKNS_14ReceivedPacketEEEE
- __ZN6webrtc24registerWebKitVP8DecoderEv
- __ZN6webrtc24registerWebKitVP9DecoderEv
- __ZN6webrtc24videoDecoderTaskCompleteEPvjjP10__CVBuffer
- __ZN6webrtc24videoDecoderTaskCompleteEPvjjS0_PFP10__CVBufferS0_EPFvS0_Eii
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
- ___memmove_chk
- _feof
- _kCFTypeArrayCallBacks
- _kCVPixelBufferExtendedPixelsBottomKey
- _kCVPixelBufferExtendedPixelsLeftKey
- _kCVPixelBufferExtendedPixelsRightKey
- _kCVPixelBufferExtendedPixelsTopKey
CStrings:
+ " - "
+ " Seq: "
+ " ecn: "
+ " image to I420"
+ " image to I420."
+ " is not supported."
+ " last feedback: "
+ " layer "
+ " new codec "
+ "!codec_specific_info->frame_instrumentation_data.has_value()"
+ "!pt_suggester_"
+ "!race_checker1053.RaceDetected()"
+ "!race_checker127.RaceDetected()"
+ "!race_checker523.RaceDetected()"
+ "%s/%d/%d"
+ "* ack ccfb"
+ "*rtp_timestamp_last_frame_sampled_ != rtp_timestamp"
+ ", height="
+ ", row="
+ ", stream_configs: ["
+ ".\n"
+ ". Falling back to multi-encoder mode."
+ ". Send time history too small?"
+ ".CorruptionLikelihoodPermille"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/add.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/bn.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/ctx.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/div.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/exponentiation.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/gcd.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/gcd_extra.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/jacobi.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/montgomery.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/mul.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/prime.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/random.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/shift.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/sqrt.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/cipher/aead.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/cipher/cipher.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/cipher/e_aes.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/digest/digest.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/digestsign/digestsign.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/ec.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/ec_key.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/ec_montgomery.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/felem.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/oct.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/p224-64.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/p256.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/scalar.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/simple.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ecdsa/ecdsa.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/hkdf/hkdf.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/blinding.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/padding.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/rsa.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/rsa_impl.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/call/payload_type_picker.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/common_video/corruption_detection_converters.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/media/base/codec_comparators.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/audio_coding/neteq/delay_constraints.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/remote_bitrate_estimator/congestion_control_feedback_tracker.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/video_coding/svc/simulcast_to_svc_converter.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/video/corruption_detection/corruption_classifier.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/video/corruption_detection/frame_instrumentation_evaluation.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/video/corruption_detection/frame_instrumentation_generator.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/video/corruption_detection/generic_mapping_functions.cc"
+ "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/video/corruption_detection/halton_frame_sampler.cc"
+ "0123456789ABCDEF0123456789abcdef"
+ "0X"
+ "0x"
+ "11"
+ "4"
+ "6"
+ "7"
+ "9"
+ ": Allocation can't be started without setting the TURN server credentials for the user."
+ ": Attempt to start allocation with disallowed port# "
+ ": Failed to create TURN client socket"
+ ": IP address family does not match. Server: "
+ ": Missing STUN_ATTR_LIFETIME attribute in allocate success response"
+ ": Missing STUN_ATTR_LIFETIME attribute in refresh success response."
+ ": Missing STUN_ATTR_NONCE attribute in stale nonce error response."
+ ": Missing STUN_ATTR_REALM attribute in stale nonce error response."
+ ": STUN server address is incompatible."
+ ": Server IP address family does not match with local host address family type"
+ ": Socket is bound to the address:"
+ "@112@0:8{SdpVideoFormat={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}{InlinedVector<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={Storage<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={CompressedTuple<std::allocator<webrtc::ScalabilityMode>, unsigned long>=Q}(Data={Allocated=^CQ}{Inlined=[34c]})}}}16"
+ "AddLocalMapping: no transport for mid"
+ "All available dynamic PTs have been assigned"
+ "Attempt to redefine a codec mapping"
+ "Bias towards block sharpness in rate-distortion optimization of transform coefficients and (in allintra mode only) reduce block edge filtering for better sharpness (0..7), default is 0"
+ "Calculating corruption probability using scale factor."
+ "Codec type "
+ "CodecSpecificInfo must not have frame_instrumentation_data set."
+ "DEBUG: Setting RED param to "
+ "EXTRACTOR-dtls_srtp"
+ "Empty congestion control feedback packet received."
+ "Empty slice in H265 bitstream."
+ "Enable the constrained directional enhancement filter (0: false, 1: true (default), 2: disable for non-reference frames, 3: enable adaptively on frame qindex)"
+ "Error during "
+ "FATAL()"
+ "Failed to allocate cpi->sb_mul_scale"
+ "Failed to allocate encode_frame_decision.sb_params_list"
+ "Failed to allocate temporal filter buffer"
+ "Failed to convert frame instrumentation data to corruption detection message."
+ "Failed to convert sample values to filtered samples"
+ "Failed to get sample coordinates for frame."
+ "Failed to get sample values for frame"
+ "Failed to install libsrtp log handler, err="
+ "Failed to lookup send time for packet with "
+ "Failed to register PT for "
+ "Failed to uninstall libsrtp log handler, err="
+ "INF"
+ "If a resolution is specified on any encoding then it must be specified on all encodings."
+ "Incorrect StapA packet."
+ "Invalid scalability mode for H.265: "
+ "MALLOC_FAILURE"
+ "Max quant matrix flatness (0..15), default is 9 (10 for allintra mode)"
+ "MedianSendingRateFactor"
+ "Min quant matrix flatness (0..15), default is 5 (4 for allintra mode)"
+ "Missing QP for "
+ "NAN"
+ "No captured frames for RTC timestamp "
+ "No payload type found for codec"
+ "No such payload type"
+ "OVERFLOW"
+ "PASSED_NULL_PARAMETER"
+ "Received packet unorderered between feeedback. SSRC: "
+ "RecordPayloadTypes failed: "
+ "Rejected attempt to redefine mapping for PT "
+ "Reset"
+ "Rewriting simulcast config to SVC."
+ "SHOULD_NOT_HAVE_BEEN_CALLED"
+ "SRTP log: "
+ "Samples are needed to calculate a corruption score."
+ "Set WebRTC-RFC8888CongestionControlFeedback: Enable and set ECN recving mode"
+ "SetPayloadTypeSuggester can be called only once"
+ "Setting receive voice codecs. Mid is "
+ "Skipping empty NAL unit."
+ "TURN server address is incompatible."
+ "The coordinates must be in [0,1): column="
+ "The first frame of a spatial or simulcast layer is not a key frame."
+ "The framebuffer must not be nullptr"
+ "The original and compressed frame have different amounts of filtered samples."
+ "The resolution dimensions must be positive."
+ "The standard deviation for the Gaussian blur must not be negative: "
+ "The width and height to scale to must be positive: width="
+ "There must be at least one coordinate provided"
+ "T{RtpEncodingParameters={optional<unsigned int>=(?=cI)B}di{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}})B}{optional<webrtc::Resolution>=(?=c{Resolution=ii})B}B{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}BB{optional<webrtc::RtpCodec>=(?=c{RtpCodec=^^?{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}i{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{vector<webrtc::RtcpFeedback, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}^{RtcpFeedback}{__compressed_pair<webrtc::RtcpFeedback *, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}})B}},R,N"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N"
+ "Unexpected feedback ntp time delta "
+ "Using pc injected network controller factory"
+ "Using pcf injected network controller factory"
+ "Warning: Attempt to change a codec's parameters"
+ "Warning: You attempted to redefine a codec from "
+ "WebRTC source stamp 2024-11-09T04:02:55"
+ "WebRTC-DisableTlsSessionTicketKillswitch"
+ "WebRTC-MixedCodecSimulcast"
+ "WebRTC-PayloadTypesInTransport"
+ "WebRTC-QCM-Static-AV1"
+ "WebRTC-QCM-Static-VP8"
+ "WebRTC-QCM-Static-VP9"
+ "WebRTC-SetReadyToSendFalseIfSendFail"
+ "WebRTC-VP9-SvcForSimulcast"
+ "X25519MLKEM768"
+ "[%d:"
+ "_%06d.%s"
+ "audio/"
+ "av1_write_last_tile_info: output buffer full"
+ "av1_write_metadata_array: output buffer full"
+ "ccfb"
+ "cfl can't be turned on in realtime only build."
+ "chk"
+ "column < width"
+ "column >= 0"
+ "configs.size() == 1u"
+ "corruptionMeasurements"
+ "cpi_data.cx_data buffer full"
+ "cpi_data.cx_data buffer overflow"
+ "ctx->cx_data buffer full"
+ "ctx->cx_data buffer overflow"
+ "cues"
+ "disallow_redefinition_level_ > 0"
+ "enable_cdef out of range [..3]"
+ "film_grain removed from realtime only build."
+ "filtered_original_samples.size() == filtered_compressed_samples.size()"
+ "filtered_original_samples.size() > 0"
+ "filtered_original_samples[i].plane == filtered_compressed_samples[i].plane"
+ "hw.optional.arm.FEAT_DotProd"
+ "hw.optional.arm.FEAT_I8MM"
+ "hw.optional.arm.FEAT_SME2"
+ "inf"
+ "kMaxDistance >= 0"
+ "libwebm-%d.%d.%d.%d"
+ "nan"
+ "num_samples >= 1"
+ "num_temporal_layers == 3"
+ "previous_sequence_index <= 0x7FFF"
+ "previous_sequence_index >= 0"
+ "previous_sequence_index must be at most 15 bits"
+ "previous_sequence_index must not be negative"
+ "pt_suggester"
+ "row < height"
+ "row >= 0"
+ "sending.size() == rtp_streams_.size()"
+ "sequence_index_update <= 0b0111'1111"
+ "sequence_index_update >= 0"
+ "sequence_index_update must be at most 7 bits"
+ "sequence_index_update must not be negative"
+ "skip_max_allocated_scale"
+ "sn"
+ "ssimulacra2"
+ "static_qp_threshold"
+ "static_qp_threshold_override: "
+ "std_dev >= 0.0"
+ "stride >= width"
+ "totalCorruptionProbability"
+ "totalSquaredCorruptionProbability"
+ "tuning out of range [AOM_TUNE_PSNR..AOM_TUNE_SSIMULACRA2]"
+ "upper_limit"
+ "values and samples must have the same size"
+ "values.size() == samples.size()"
+ "video_receiver_info.corruption_score_count > 0"
+ "video_receiver_info.corruption_score_squared_sum.has_value()"
+ "{CodecSpecificInfo=i(CodecSpecificInfoUnion={CodecSpecificInfoVP8=BCBcB[3Q]Q[3Q]Q}{CodecSpecificInfoVP9=BBBBBCBBCQQB[8S][8S]{GofInfoVP9=Q[255C][255B][255C][255[3C]]S}C[3C]}{CodecSpecificInfoH264=iCBB})B{optional<webrtc::GenericFrameInfo>=(?=c{GenericFrameInfo=ii{InlinedVector<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={Storage<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={CompressedTuple<std::allocator<webrtc::DecodeTargetIndication>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={Storage<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={CompressedTuple<std::allocator<webrtc::CodecBufferUsage>, unsigned long>=Q}(Data={Allocated=^{CodecBufferUsage}Q}{Inlined=[64c]})}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{bitset<32UL>=Q}})B}{optional<webrtc::FrameDependencyStructure>=(?=c{FrameDependencyStructure=iii{InlinedVector<int, 10UL, std::allocator<int>>={Storage<int, 10UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={Storage<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={CompressedTuple<std::allocator<webrtc::RenderResolution>, unsigned long>=Q}(Data={Allocated=^{RenderResolution}Q}{Inlined=[32c]})}}{vector<webrtc::FrameDependencyTemplate, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}^{FrameDependencyTemplate}{__compressed_pair<webrtc::FrameDependencyTemplate *, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}}}})B}{optional<webrtc::ScalabilityMode>=(?=cC)B}{optional<absl::variant<webrtc::FrameInstrumentationSyncData, webrtc::FrameInstrumentationData>>=(?=c{variant<webrtc::FrameInstrumentationSyncData, webrtc::FrameInstrumentationData>=(DestructibleUnionImpl<webrtc::FrameInstrumentationSyncData, webrtc::FrameInstrumentationData>={FrameInstrumentationSyncData=iB}(DestructibleUnionImpl<webrtc::FrameInstrumentationData>={FrameInstrumentationData=iBdii{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}(DestructibleUnionImpl<>=)))Q})B}}16@0:8"
+ "{RtpEncodingParameters={optional<unsigned int>=(?=cI)B}di{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}})B}{optional<webrtc::Resolution>=(?=c{Resolution=ii})B}B{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}BB{optional<webrtc::RtpCodec>=(?=c{RtpCodec=^^?{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}i{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{vector<webrtc::RtcpFeedback, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}^{RtcpFeedback}{__compressed_pair<webrtc::RtcpFeedback *, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}})B}}16@0:8"
+ "{SdpVideoFormat={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}{InlinedVector<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={Storage<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={CompressedTuple<std::allocator<webrtc::ScalabilityMode>, unsigned long>=Q}(Data={Allocated=^CQ}{Inlined=[34c]})}}}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@0:8@16"
- "\tsY %d "
- "\n\tcCb"
- "\n\tcCr"
- "\n\tcY"
- "\n\tsCb %d"
- "\n\tsCr %d"
- " Failed to insert packet"
- " at target quality "
- " cng_timeout_ms="
- " combine_concealment_decision="
- " deceleration_target_level_offset_ms="
- " enable_stable_delay_mode="
- " is not registered."
- " layer_drop_mode "
- " max_consec_drop "
- " or higher."
- " packet_history_size_ms="
- " seq : "
- "!race_checker1007.RaceDetected()"
- "!race_checker126.RaceDetected()"
- "!race_checker467.RaceDetected()"
- "%% then avg_burst_loss_length must be "
- "%d %d"
- "%hu"
- ", vtError "
- "-R"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/add.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/bn.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/ctx.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/div.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/exponentiation.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/gcd.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/gcd_extra.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/jacobi.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/montgomery.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/mul.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/prime.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/random.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/shift.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/bn/sqrt.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/cipher/aead.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/cipher/cipher.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/cipher/e_aes.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/digest/digest.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/digestsign/digestsign.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/ec.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/ec_key.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/ec_montgomery.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/felem.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/oct.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/p224-64.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/p256.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/scalar.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ec/simple.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/ecdsa/ecdsa.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/hkdf/hkdf.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/blinding.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/padding.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/rsa.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/third_party/boringssl/src/crypto/fipsmodule/rsa/rsa_impl.c"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/call/fake_network_pipe.cc"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/audio_coding/acm2/acm_receiver.cc"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/audio_coding/neteq/decision_logic.cc"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/modules/remote_bitrate_estimator/congestion_control_feedback_generator.cc"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/test/network/simulated_network.cc"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/webkit_sdk/WebKit/WebKitDecoderReceiver.cpp"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/webkit_sdk/WebKit/WebKitVP8Decoder.cpp"
- "/Library/Caches/com.apple.xbs/Sources/libwebrtc/Source/ThirdParty/libwebrtc/Source/webrtc/webkit_sdk/WebKit/WebKitVP9Decoder.cpp"
- ": Missing STUN_ATTR_TURN_LIFETIME attribute in allocate success response"
- ": Missing STUN_ATTR_TURN_LIFETIME attribute in refresh success response."
- "@112@0:8{SdpVideoFormat={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}{InlinedVector<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={Storage<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={CompressedTuple<std::allocator<webrtc::ScalabilityMode>, unsigned long>=Q}(Data={Allocated=^CQ}{Inlined=[34c]})}}}16"
- "AcmReceiver::GetAudio - NetEq Failed."
- "AcmReceiver::InsertPacket "
- "AcmReceiver::SetExtraDelay "
- "Adding block observation failed\n"
- "Allocation can't be started without setting the TURN server credentials for the user."
- "Attempt to start allocation with disallowed port# "
- "Attempted to set scale_resolution_down_by and requested_resolution simultaniously."
- "Bias towards block sharpness in rate-distortion optimization of transform coefficients (0..7), default is 0"
- "CPS"
- "E %lld %lld %d %hd %d\n"
- "Enable the constrained directional enhancement filter (0: false, 1: true (default), 2: disable for non-reference frames)"
- "Error allocating denoise and model"
- "Error allocating grain table"
- "Error writing metadata OBU size"
- "Failed initialization noise state with size %d\n"
- "Failed to alloc A or AtA_inv for block_size=%d\n"
- "Failed to allocate altref buffer"
- "Failed to allocate cpi->film_grain_table"
- "Failed to allocate memory for block of size %d\n"
- "Failed to allocate noise state for channel %d\n"
- "Failed to allocate system of equations of size %d\n"
- "Failed to create TURN client socket"
- "Failed to init equation system for block_size=%d\n"
- "Failed to init lut\n"
- "Failed to set AV1E_SET_MAX_CONSEC_FRAME_DROP_CBR to "
- "For a total packet loss of "
- "IP address family does not match."
- "IP address family does not match. server: "
- "InsertPacket"
- "Libvpx VP9 encoder SVC frame drop config: "
- "Max quant matrix flatness (0..15), default is 15"
- "Min quant matrix flatness (0..15), default is 8"
- "Missing STUN_ATTR_NONCE attribute in stale nonce error response."
- "Missing STUN_ATTR_REALM attribute in stale nonce error response."
- "N"
- "NO"
- "NetEq decision logic config:"
- "Network queue: "
- "No transient suppressor created (probably disabled)"
- "Not enough flat blocks to update noise estimate\n"
- "Payload-type "
- "RID"
- "STAP-A packet too short"
- "Server IP address family does not match with local host address family type"
- "Setting output_format_request_ based on sink_wants: "
- "Setting receive voice codecs."
- "Solving combined noise equation system failed %d!\n"
- "Solving combined noise strength failed!\n"
- "Solving latest noise equation system failed %d!\n"
- "Solving latest noise strength failed!\n"
- "StapA header truncated."
- "StapA packet with incorrect NALU packet lengths."
- "TLS client read_hello_verify_request"
- "The external rate control library is not set properly for TPL pass."
- "These should always be created by VideoBroadcaster!"
- "To utilize three-pass encoding, libaom must be built with CONFIG_THREE_PASS=1 & CONFIG_AV1_DECODER=1."
- "T{RtpEncodingParameters={optional<unsigned int>=(?=cI)B}di{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}})B}{optional<webrtc::Resolution>=(?=c{Resolution=ii})B}B{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}BB{optional<webrtc::RtpCodec>=(?=c{RtpCodec=^^?{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}i{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{vector<webrtc::RtcpFeedback, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}^{RtcpFeedback}{__compressed_pair<webrtc::RtcpFeedback *, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}})B}},R,N"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}},R,N"
- "Unable read to Cr coeffs header (cCr)"
- "Unable to allocate buffer of size %d\n"
- "Unable to allocate copy of A\n"
- "Unable to allocate denoise buffers\n"
- "Unable to allocate denoise_and_model struct\n"
- "Unable to allocate flat_blocks buffer\n"
- "Unable to allocate grain table entry"
- "Unable to allocate noise PSD buffers\n"
- "Unable to allocate temp values of size %dx%d\n"
- "Unable to assign payload type to format: "
- "Unable to denoise image\n"
- "Unable to get grain parameters.\n"
- "Unable to init flat block finder\n"
- "Unable to init noise model\n"
- "Unable to open %s"
- "Unable to read (or invalid) file magic"
- "Unable to read Cb coeffs"
- "Unable to read Cb coeffs header (cCb)"
- "Unable to read Cr coeffs"
- "Unable to read Y coeffs"
- "Unable to read Y coeffs header (cY)"
- "Unable to read cb scaling points"
- "Unable to read cr scaling points"
- "Unable to read entry header. Read %d != 5"
- "Unable to read entry params. Read %d != 12"
- "Unable to read num cb points"
- "Unable to read num cr points"
- "Unable to read num y points"
- "Unable to read y scaling points"
- "Unable to realloc buffers\n"
- "Unexpected failed demuxing packet in FakeNetworkPipe, Ssrc: "
- "Unsupported block size %d\n"
- "Using injected network controller factory"
- "VP8 decoder creation failed, CMDerivedObjectCreate failed with error "
- "VP8 decoder creation failed, no decoder output"
- "VP8 decoder: CMBlockBufferGetDataPointer failed with error "
- "VP8 decoder: failed to create contiguous block buffer with error "
- "VP8 decoder: failed to get data buffer"
- "VP8 decoder: failed to get decoder from instance while decoding"
- "VP8 decoder: failed to get decoder from instance while starting"
- "VP8 decoder: invalidation failed as instance has no decoder"
- "VP9 decoder creation failed, CMDerivedObjectCreate failed with error "
- "VP9 decoder creation failed, no decoder output"
- "VP9 decoder: CMBlockBufferGetDataPointer failed with error "
- "VP9 decoder: decoder failed with error "
- "VP9 decoder: failed to create contiguous block buffer with error "
- "VP9 decoder: failed to get data buffer"
- "VP9 decoder: failed to get decoder from instance while decoding"
- "VP9 decoder: failed to get decoder from instance while starting"
- "VP9 decoder: invalidation failed as instance has no decoder"
- "WebKit VP8 decoder"
- "WebKit VP9 decoder"
- "WebRTC source stamp 2024-07-16T04:07:40"
- "WebRTC-Audio-NetEqDecisionLogicConfig"
- "WebRTC-FakeNetworkReceiveConfig"
- "WebRTC-FakeNetworkSendConfig"
- "WebRTC-LibvpxVp9Encoder-SvcFrameDropConfig"
- "WebRTC-PermuteTlsClientHello"
- "WebRTC-SetCodecPreferences-ReceiveOnlyFilterInsteadOfThrow"
- "WebRTC-TransientSuppressorForcedOff"
- "WebRTC-VoIPChannelRemixingAdjustmentKillSwitch"
- "Y"
- "`mid` attribute too long. Truncating."
- "accept_exit"
- "accept_loop"
- "allow_reordering"
- "aom_wiener_denoise_2d doesn't handle different chroma subsampling\n"
- "avg_burst_loss_length"
- "avg_burst_loss_length > min_avg_burst_loss_length"
- "block_size = %d must be > 1\n"
- "block_size = %d must be >= %d\n"
- "cng_timeout_ms"
- "combine_concealment_decision"
- "connect_exit"
- "connect_loop"
- "deceleration_target_level_offset_ms"
- "delay_standard_deviation_ms"
- "enable_cdef out of range [..2]"
- "enable_stable_delay_mode"
- "frames_to_encode >= blocks_in_first_vad_call"
- "handshake_done"
- "handshake_start"
- "it != active_transports_.end()"
- "layer_drop_mode"
- "link_capacity_kbps"
- "loss_percent"
- "max_consec_drop"
- "n"
- "num_layers_.temporal == 3"
- "p %d %d %d %d %d %d %d %d %d %d %d %d\n"
- "packet_history_size_ms"
- "packet_it != packets_in_flight_.end()"
- "packet_overhead"
- "params.lag = %d > 3\n"
- "queue_delay_ms"
- "queue_length_packets"
- "queue_time_us >= 0"
- "read_alert"
- "temporal_id < num_layers"
- "tuning out of range [AOM_TUNE_PSNR..AOM_TUNE_VMAF_SALIENCY_MAP]"
- "write_alert"
- "{CodecSpecificInfo=i(CodecSpecificInfoUnion={CodecSpecificInfoVP8=BCBcB[3Q]Q[3Q]Q}{CodecSpecificInfoVP9=BBBBBCBBCQQB[8S][8S]{GofInfoVP9=Q[255C][255B][255C][255[3C]]S}C[3C]}{CodecSpecificInfoH264=iCBB})B{optional<webrtc::GenericFrameInfo>=(?=c{GenericFrameInfo=ii{InlinedVector<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={Storage<webrtc::DecodeTargetIndication, 10UL, std::allocator<webrtc::DecodeTargetIndication>>={CompressedTuple<std::allocator<webrtc::DecodeTargetIndication>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<int, 4UL, std::allocator<int>>={Storage<int, 4UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[16c]})}}{InlinedVector<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={Storage<webrtc::CodecBufferUsage, 8UL, std::allocator<webrtc::CodecBufferUsage>>={CompressedTuple<std::allocator<webrtc::CodecBufferUsage>, unsigned long>=Q}(Data={Allocated=^{CodecBufferUsage}Q}{Inlined=[64c]})}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{bitset<32UL>=Q}})B}{optional<webrtc::FrameDependencyStructure>=(?=c{FrameDependencyStructure=iii{InlinedVector<int, 10UL, std::allocator<int>>={Storage<int, 10UL, std::allocator<int>>={CompressedTuple<std::allocator<int>, unsigned long>=Q}(Data={Allocated=^iQ}{Inlined=[40c]})}}{InlinedVector<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={Storage<webrtc::RenderResolution, 4UL, std::allocator<webrtc::RenderResolution>>={CompressedTuple<std::allocator<webrtc::RenderResolution>, unsigned long>=Q}(Data={Allocated=^{RenderResolution}Q}{Inlined=[32c]})}}{vector<webrtc::FrameDependencyTemplate, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}^{FrameDependencyTemplate}{__compressed_pair<webrtc::FrameDependencyTemplate *, std::allocator<webrtc::FrameDependencyTemplate>>=^{FrameDependencyTemplate}}}})B}{optional<webrtc::ScalabilityMode>=(?=cC)B}}16@0:8"
- "{RtpEncodingParameters={optional<unsigned int>=(?=cI)B}di{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}})B}{optional<webrtc::Resolution>=(?=c{Resolution=ii})B}B{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}BB{optional<webrtc::RtpCodec>=(?=c{RtpCodec=^^?{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}i{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{vector<webrtc::RtcpFeedback, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}^{RtcpFeedback}{__compressed_pair<webrtc::RtcpFeedback *, std::allocator<webrtc::RtcpFeedback>>=^{RtcpFeedback}}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}})B}}16@0:8"
- "{SdpVideoFormat={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__tree<std::__value_type<std::string, std::string>, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::string>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::string>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::string>, std::less<std::string>>>=Q}}}{InlinedVector<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={Storage<webrtc::ScalabilityMode, 34UL, std::allocator<webrtc::ScalabilityMode>>={CompressedTuple<std::allocator<webrtc::ScalabilityMode>, unsigned long>=Q}(Data={Allocated=^CQ}{Inlined=[34c]})}}}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}24@0:8@16"

```
