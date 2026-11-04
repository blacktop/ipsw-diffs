## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0xc8ba0
+1015.5.1.0.0
+  __TEXT.__text: 0xc9868
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0xf40
+  __TEXT.__const: 0x1d20
   __TEXT.__dlopen_cstrs: 0x158
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__cstring: 0x33e8f
+  __TEXT.__cstring: 0x341b9
   __TEXT.__oslogstring: 0x252
-  __TEXT.__unwind_info: 0x29e0
+  __TEXT.__unwind_info: 0x2a08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3078
+  __DATA_CONST.__const: 0x3108
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x7a8
-  __AUTH_CONST.__const: 0x3cf8
-  __AUTH_CONST.__cfstring: 0x7440
+  __DATA_CONST.__got: 0x7d0
+  __AUTH_CONST.__const: 0x3d00
+  __AUTH_CONST.__cfstring: 0x7480
   __AUTH_CONST.__objc_const: 0x7a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2637
-  Symbols:   4991
-  CStrings:  4476
+  Functions: 2647
+  Symbols:   5019
+  CStrings:  4490
 
Symbols:
+ GCC_except_table1612
+ GCC_except_table1616
+ GCC_except_table1811
+ GCC_except_table1814
+ GCC_except_table1817
+ GCC_except_table1821
+ GCC_except_table1986
+ GCC_except_table2236
+ GCC_except_table2544
+ GCC_except_table2549
+ GCC_except_table2558
+ GCC_except_table2615
+ GCC_except_table2618
+ GCC_except_table2619
+ _APAudioFormatCopyPreferredBidirectionalAudioFormats
+ _APAudioFormatGetSupportedTransportAudioFormatsBidirectionalAudioReceiver
+ _APAudioFormatGetSupportedTransportAudioFormatsBidirectionalAudioSender
+ _APSAPAPExtensionConvertContentTypeBBufAndMergeIntoLoudnessInfoDict
+ _APSAPAPExtensionConvertLibraryLoudnessBBufAndMergeIntoLoudnessInfoDict
+ _APSAPAPExtensionConvertLoudnessInfoDictContentTypeToBBuf
+ _APSAPAPExtensionConvertLoudnessInfoDictLibraryLoudnessToBBuf
+ _APSIsBidirectionalAudioReceiverEnabled
+ _APSIsBidirectionalAudioSenderEnabled
+ _AudioConverterReset
+ _kContentTypeDictionary_ContentTypeFlagsKey
+ _kContentTypeDictionary_ContentTypeKey
+ _kContentTypeDictionary_ContentTypeVersionKey
+ _kLoudnessInfoDictionary_ContentTypeKey
+ _kLoudnessInfoDictionary_LibraryLoudnessKey
+ _kSARPreWarmPackets_AACELD_48k_5_1
+ _kSARPreWarmPackets_AACELD_48k_7_1
+ _kSARPreWarmPackets_AACELD_48k_Stereo
+ _kSARPreWarm_AACELD_48k_5_1_Silence
+ _kSARPreWarm_AACELD_48k_5_1_pkt0
+ _kSARPreWarm_AACELD_48k_5_1_pkt1
+ _kSARPreWarm_AACELD_48k_7_1_Silence
+ _kSARPreWarm_AACELD_48k_7_1_pkt0
+ _kSARPreWarm_AACELD_48k_7_1_pkt1
+ _kSARPreWarm_AACELD_48k_Stereo_Silence
+ _kSARPreWarm_AACELD_48k_Stereo_pkt0
+ _kSARPreWarm_AACELD_48k_Stereo_pkt1
+ _sar_preWarmDecodeCallback
- GCC_except_table1610
- GCC_except_table1614
- GCC_except_table1806
- GCC_except_table1809
- GCC_except_table1812
- GCC_except_table1816
- GCC_except_table1981
- GCC_except_table2231
- GCC_except_table2534
- GCC_except_table2539
- GCC_except_table2548
- GCC_except_table2605
- GCC_except_table2608
- GCC_except_table2609
CStrings:
+ "%@ Codec pre-warm done, AudioConverterReset err=%#m\n"
+ "%@ Codec pre-warm packet %u/%u size=%u: err=%#m frameCount=%u\n"
+ "APAudioFormatCopyPreferredBidirectionalAudioFormats"
+ "APSAPAPExtensionConvertContentTypeBBufAndMergeIntoLoudnessInfoDict"
+ "APSAPAPExtensionConvertLibraryLoudnessBBufAndMergeIntoLoudnessInfoDict"
+ "APSAPAPExtensionConvertLoudnessInfoDictContentTypeToBBuf"
+ "APSAPAPExtensionConvertLoudnessInfoDictLibraryLoudnessToBBuf"
+ "ConversationalApps"
+ "MeshASQUIC"
+ "OSStatus hoseSBAR_audioHoseSetRateCallbackInternal(APSEndpointStreamAudioHoseSBARRef, uint32_t, APSAudioTransportTime, APSAudioTransportTime *, APSNetworkTime *)"
+ "PebblePlay"
+ "[%{ptr}] Finished Rate Change (receiver anchor): -> %u. (err=%d) networkTime: %1.6f(id=%llu)\n"
+ "[%{ptr}] Finished Rate Change: %u -> %u. (err=%d) networkTime: %1.6f(id=%llu)\n"
+ "terminus"
+ "void sar_preWarmCodec(APSStreamingAudioRendererRef)"
- "[%{ptr}] Finished Rate Change: %u -> %u. (err=%d)\n"
```
