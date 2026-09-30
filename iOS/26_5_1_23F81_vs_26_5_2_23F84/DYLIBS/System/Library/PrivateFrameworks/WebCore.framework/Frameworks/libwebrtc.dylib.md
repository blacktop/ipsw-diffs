## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-  __TEXT.__text: 0xa7a044
+  __TEXT.__text: 0xa7a168
   __TEXT.__auth_stubs: 0x14d0
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xa68f8
-  __TEXT.__cstring: 0x550d1
+  __TEXT.__cstring: 0x550f8
   __TEXT.__gcc_except_tab: 0x18a0
   __TEXT.__unwind_info: 0x2840
   __TEXT.__eh_frame: 0xf08

   - /usr/lib/libobjc.A.dylib
   Functions: 18262
   Symbols:   44540
-  CStrings:  9649
+  CStrings:  9650
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ __ZN6webrtc20LegacyStatsCollector25ExtractSessionAndDataInfoEv : 5524 -> 5392
~ __ZN6webrtc20LegacyStatsCollector21AddCertificateReportsENSt3__110unique_ptrINS_19SSLCertificateStatsENS1_14default_deleteIS3_EEEE : 412 -> 680
~ __ZN6dcsctp15OutstandingData10HandleSackENS_23UnwrappedSequenceNumberIN6webrtc11StrongAliasINS_6TSNTagEjEEEENS2_9ArrayViewIKNS_9SackChunk11GapAckBlockELln4711EEEb : 304 -> 328
~ __ZN6dcsctp19RetransmissionQueue10HandleSackEN6webrtc9TimestampERKNS_9SackChunkE : 1136 -> 1180
~ __ZN6webrtc21SdpOfferAnswerHandler33UpdateTransceiversAndDataChannelsENS_13ContentSourceERKNS_27SessionDescriptionInterfaceEPS3_S5_RKNSt3__13mapINS6_12basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEPKNS_12ContentGroupENS6_4lessISD_EENSB_INS6_4pairIKSD_SG_EEEEEE : 9520 -> 9568
~ __ZN6webrtc21VideoCodecInitializer10SetupCodecERKNS_15FieldTrialsViewERKNS_18VideoEncoderConfigERKNSt3__16vectorINS_11VideoStreamENS7_9allocatorIS9_EEEE : 4836 -> 4852
~ _vp8_de_alloc_frame_buffers : 484 -> 508
CStrings:
+ "streams.size() <= kMaxSimulcastStreams"

```
