## AudioCodecs

> `/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs`

```diff

-818.203.0.0.0
-  __TEXT.__text: 0x68f1f8
+818.204.1.0.0
+  __TEXT.__text: 0x68f344
   __TEXT.__realtime: 0x123c
   __TEXT.__const: 0x33e14c
-  __TEXT.__cstring: 0xfe6c
+  __TEXT.__cstring: 0xfe74
   __TEXT.__gcc_except_tab: 0x11fcc
-  __TEXT.__oslogstring: 0x1bb02
+  __TEXT.__oslogstring: 0x1bbc3
   __TEXT.__ustring: 0x20
   __TEXT.__unwind_info: 0xaff0
   __TEXT.__eh_frame: 0x6a8

   - /usr/lib/libc++.1.dylib
   Functions: 9826
   Symbols:   17169
-  CStrings:  3594
+  CStrings:  3598
 
Functions:
~ __ZN6mpddrc15UniDrcSelection7ProcessERKNS_15UniDrcInterfaceERKNS_12UniDrcHeaderENS_12UniDrcDomainEPNS_19UniDrcSelProcOutputE : 19272 -> 19488
~ __ZN6mpddrc15UniDrcSelection19selectDownmixMatrixERKNS_12UniDrcHeaderE : 672 -> 880
~ __ZN6mpddrc15UniDrcSelection18getSignalPeakLevelERKNS_12UniDrcHeaderEjjhjPfPb : 2536 -> 2688
~ __ZN17ACDDPAtmosDecoder35SoundCheckDictionaryPropertyHandlerEPK14__CFDictionary : 328 -> 352
~ __ZN12ACLC3Decoder10InitializeEPK27AudioStreamBasicDescriptionS2_PKvj : 3336 -> 3344
~ __ZN12ACLC3Decoder15AppendInputDataEPKvRjS2_PK28AudioStreamPacketDescription : 192 -> 204
~ _ddp_udc_int_dlb_bitbuf_read : 424 -> 332
~ _ddp_udc_int_dlb_bitbuf_read_long : 532 -> 456
~ _ddp_udc_int_exmd_unpblkaht : 2604 -> 2552
~ _ddp_udc_int_exmd_skipahtmants : 776 -> 748
~ _ddp_udc_int_jocd_process_one_frame : 30252 -> 30028
~ __ZL29aacDecoder_SignalInterruptionP20AAC_DECODER_INSTANCE : 264 -> 404
~ __ZN7lpd_dec10lpdDecoder4ReadER16TBitstreamReaderIjEiPfbP8ArithDecjb : 8380 -> 8412
~ __ZNSt3__116allocator_traitsINS_9allocatorIN7lpd_dec10lpdDecoderEEEE9constructB9foe220106IS3_JELi0EEEvRS4_PT_DpOT0_ : 472 -> 476
~ __Z23CAacDecoder_DecodeFrameP20AAC_DECODER_INSTANCEjPfii : 22336 -> 22344
CStrings:
+ "%25s:%-5d ERROR: desired effect type count (%d) exceeds request list size (%d)\n"
+ "%25s:%-5d ERROR: downmix coefficient count mismatch\n"
+ "%25s:%-5d ERROR: invalid downmix matrix dimensions %d x %d\n"
+ "LoudnessManagerV3"
```
