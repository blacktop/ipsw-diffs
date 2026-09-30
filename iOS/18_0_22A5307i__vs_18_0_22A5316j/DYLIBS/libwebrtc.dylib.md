## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-619.1.20.10.1
-  __TEXT.__text: 0xa723c0
-  __TEXT.__auth_stubs: 0x1540
+619.1.22.10.1
+  __TEXT.__text: 0xa62460
+  __TEXT.__auth_stubs: 0x1510
   __TEXT.__objc_methlist: 0x11c4
-  __TEXT.__cstring: 0x4aeb1
-  __TEXT.__const: 0x839a8
-  __TEXT.__gcc_except_tab: 0x1844
-  __TEXT.__unwind_info: 0x3a68
+  __TEXT.__cstring: 0x4b875
+  __TEXT.__const: 0x821a8
+  __TEXT.__gcc_except_tab: 0x1854
+  __TEXT.__unwind_info: 0x3a58
   __TEXT.__eh_frame: 0x1c58
   __TEXT.__objc_classname: 0x45a
   __TEXT.__objc_methname: 0x2850
-  __TEXT.__objc_methtype: 0x4025
+  __TEXT.__objc_methtype: 0x3ff5
   __TEXT.__objc_stubs: 0x19e0
   __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x154e8
+  __DATA_CONST.__const: 0x15f68
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0xab0
+  __AUTH_CONST.__auth_got: 0xa98
   __AUTH_CONST.__auth_ptr: 0x368
-  __AUTH_CONST.__const: 0x1fec0
+  __AUTH_CONST.__const: 0x1fd30
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x3ba8
   __AUTH_CONST.__objc_intobj: 0x78

   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
   __DATA.__objc_ivar: 0x254
-  __DATA.__data: 0x4288
-  __DATA.__bss: 0x30e88
+  __DATA.__data: 0x43d8
+  __DATA.__bss: 0x31708
   __DATA.__common: 0x1ed90
   __DATA_DIRTY.__objc_data: 0xa50
-  __DATA_DIRTY.__data: 0x798
-  __DATA_DIRTY.__bss: 0x23e8
+  __DATA_DIRTY.__data: 0x328
+  __DATA_DIRTY.__bss: 0x2290
   __DATA_DIRTY.__common: 0x460
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18703
-  Symbols:   18821
+  Functions: 18553
+  Symbols:   18667
   CStrings:  0
 
Symbols:
+ _CCRandomGenerateBytes
+ __ZN3rtc10TimeMicrosEv
+ __ZN3rtc14ReceivedPacketC1ENS_9ArrayViewIKhLln4711EEERKNS_13SocketAddressENSt3__18optionalIN6webrtc9TimestampEEENS_10EcnMarkingENS0_14DecryptionInfoE
+ __ZN3rtc17AsyncPacketSocket20NotifyPacketReceivedERKNS_14ReceivedPacketE
+ __ZN3rtc17AsyncPacketSocket30RegisterReceivedPacketCallbackEN4absl12AnyInvocableIFvPS0_RKNS_14ReceivedPacketEEEE
+ __ZN3rtc17AsyncPacketSocket32DeregisterReceivedPacketCallbackEv
+ __ZN3rtc18NetworkManagerBaseC2Ev
+ __ZN3rtc18webrtc_checks_impl22UnreachableCodeReachedEv
+ __ZN6webrtc10VideoFrame7Builder22set_video_frame_bufferERKNS_13scoped_refptrINS_16VideoFrameBufferEEE
+ __ZN6webrtc10VideoFrameC1ERKNS_13scoped_refptrINS_16VideoFrameBufferEEENS_13VideoRotationEx
+ __ZN6webrtc11MediaStream11RemoveTrackENS_13scoped_refptrINS_19AudioTrackInterfaceEEE
+ __ZN6webrtc11MediaStream11RemoveTrackENS_13scoped_refptrINS_19VideoTrackInterfaceEEE
+ __ZN6webrtc11MediaStream8AddTrackENS_13scoped_refptrINS_19AudioTrackInterfaceEEE
+ __ZN6webrtc11MediaStream8AddTrackENS_13scoped_refptrINS_19VideoTrackInterfaceEEE
+ __ZN6webrtc16CreateVp8DecoderERKNS_11EnvironmentE
+ __ZN6webrtc16CreateVp8EncoderERKNS_11EnvironmentENS_18Vp8EncoderSettingsE
+ __ZN6webrtc16CreateVp9EncoderERKNS_11EnvironmentENS_18Vp9EncoderSettingsE
+ __ZN6webrtc20RtpReceiverInterface17SetFrameDecryptorENS_13scoped_refptrINS_23FrameDecryptorInterfaceEEE
+ __ZN6webrtc20RtpReceiverInterface19SetFrameTransformerENS_13scoped_refptrINS_25FrameTransformerInterfaceEEE
+ __ZN6webrtc22CreateLibaomAv1EncoderERKNS_11EnvironmentENS_24LibaomAv1EncoderSettingsE
+ __ZN6webrtc27CreatePeerConnectionFactoryEPN3rtc6ThreadES2_S2_NS_13scoped_refptrINS_17AudioDeviceModuleEEENS3_INS_19AudioEncoderFactoryEEENS3_INS_19AudioDecoderFactoryEEENSt3__110unique_ptrINS_19VideoEncoderFactoryENSA_14default_deleteISC_EEEENSB_INS_19VideoDecoderFactoryENSD_ISG_EEEENS3_INS_10AudioMixerEEENS3_INS_15AudioProcessingEEENSB_INS_19AudioFrameProcessorENSD_ISN_EEEENSB_INS_15FieldTrialsViewENSD_ISQ_EEEENSB_INS_16TaskQueueFactoryENSD_IST_EEEE
+ __ZN7cricket20IceTransportInternal25AddGatheringStateCallbackEPKvN4absl12AnyInvocableIFvPS0_EEE
+ __ZN7cricket20IceTransportInternal28RemoveGatheringStateCallbackEPKv
+ __ZNK6webrtc18EnvironmentFactory6CreateEv
+ __ZThn8_N6webrtc20RtpReceiverInterface19SetFrameTransformerENS_13scoped_refptrINS_25FrameTransformerInterfaceEEE
+ _pthread_atfork
- __ZN3rtc10LogMessage12SetLogOutputENS_15LoggingSeverityEPFvS1_PKcE
- __ZN3rtc18NetworkManagerBaseC2EPKN6webrtc15FieldTrialsViewE
- __ZN3rtc22AsyncResolverInterfaceC2Ev
- __ZN3rtc22AsyncResolverInterfaceD2Ev
- __ZN3rtc24BasicPacketSocketFactory19CreateAsyncResolverEv
- __ZN3rtc9ProxyInfoC1Ev
- __ZN3rtc9ProxyInfoD1Ev
- __ZN6webrtc10VP8Decoder6CreateEv
- __ZN6webrtc10VP8Encoder6CreateEv
- __ZN6webrtc10VP9Encoder6CreateERKN7cricket5CodecE
- __ZN6webrtc10VP9Encoder6CreateEv
- __ZN6webrtc10VideoFrame7Builder22set_video_frame_bufferERKN3rtc13scoped_refptrINS_16VideoFrameBufferEEE
- __ZN6webrtc10VideoFrameC1ERKN3rtc13scoped_refptrINS_16VideoFrameBufferEEENS_13VideoRotationEx
- __ZN6webrtc11MediaStream11RemoveTrackEN3rtc13scoped_refptrINS_19AudioTrackInterfaceEEE
- __ZN6webrtc11MediaStream11RemoveTrackEN3rtc13scoped_refptrINS_19VideoTrackInterfaceEEE
- __ZN6webrtc11MediaStream8AddTrackEN3rtc13scoped_refptrINS_19AudioTrackInterfaceEEE
- __ZN6webrtc11MediaStream8AddTrackEN3rtc13scoped_refptrINS_19VideoTrackInterfaceEEE
- __ZN6webrtc20RtpReceiverInterface17SetFrameDecryptorEN3rtc13scoped_refptrINS_23FrameDecryptorInterfaceEEE
- __ZN6webrtc20RtpReceiverInterface40SetDepacketizerToDecoderFrameTransformerEN3rtc13scoped_refptrINS_25FrameTransformerInterfaceEEE
- __ZN6webrtc22CreateLibaomAv1EncoderEv
- __ZN6webrtc27CreatePeerConnectionFactoryEPN3rtc6ThreadES2_S2_NS0_13scoped_refptrINS_17AudioDeviceModuleEEENS3_INS_19AudioEncoderFactoryEEENS3_INS_19AudioDecoderFactoryEEENSt3__110unique_ptrINS_19VideoEncoderFactoryENSA_14default_deleteISC_EEEENSB_INS_19VideoDecoderFactoryENSD_ISG_EEEENS3_INS_10AudioMixerEEENS3_INS_15AudioProcessingEEEPNS_19AudioFrameProcessorENSB_INS_15FieldTrialsViewENSD_ISP_EEEENSB_INS_16TaskQueueFactoryENSD_ISS_EEEE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZTVN6webrtc30WrappingAsyncDnsResolverResultE
- _open
- _perror
- _recvfrom
- _strdup

```
