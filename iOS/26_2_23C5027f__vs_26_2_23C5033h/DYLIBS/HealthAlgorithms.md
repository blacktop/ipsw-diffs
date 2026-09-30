## HealthAlgorithms

> `/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms`

```diff

 135.0.0.0.0
-  __TEXT.__text: 0x4248c
+  __TEXT.__text: 0x42500
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x13a4
   __TEXT.__const: 0xbaf9

   __TEXT.__unwind_info: 0x1430
   __TEXT.__objc_classname: 0x42a
   __TEXT.__objc_methname: 0x3da2
-  __TEXT.__objc_methtype: 0x10c9
+  __TEXT.__objc_methtype: 0x10d5
   __TEXT.__objc_stubs: 0x10c0
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0982F327-8E56-3A53-A7D3-DC3C722D7EA5
+  UUID: 01D36677-EB89-327B-A7C4-B5F0BF84B936
   Functions: 1290
   Symbols:   3865
   CStrings:  1314
Functions:
~ __ZNSt3__16vectorIN6mimosa15OpticalSampleV1ENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZNSt3__16vectorIN6mimosa11AccelSampleENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 72 -> 76
~ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em : 56 -> 60
~ __ZNSt3__16vectorIN6mimosa15OpticalSampleV2ENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__120back_insert_iteratorINS_6vectorINS_4pairIN7hal900012SubframeTypeEhEENS_9allocatorIS5_EEEEEaSB8ne200100EOS5_ : 224 -> 228
~ __ZN17health_algorithms12PPGProcessor14process_packetERKNSt3__17variantIJN6mimosa8PacketV1ENS3_8PacketV2ENS3_8PacketV3ENS3_8PacketV4ENS3_8PacketV5ENS3_8PacketV6ENS3_8PacketV7ENS3_8PacketV8ENS3_8PacketV9ENS3_9PacketV10ENS3_9PacketV11ENS3_9PacketV12EEEE : 2396 -> 2400
~ __ZN17health_algorithms12PPGProcessor20compute_accel_outputERKNSt3__17variantIJN6mimosa8PacketV1ENS3_8PacketV2ENS3_8PacketV3ENS3_8PacketV4ENS3_8PacketV5ENS3_8PacketV6ENS3_8PacketV7ENS3_8PacketV8ENS3_8PacketV9ENS3_9PacketV10ENS3_9PacketV11ENS3_9PacketV12EEEE : 1180 -> 1184
~ __ZNSt3__120back_insert_iteratorINS_6vectorIN17health_algorithms12PPGProcessor11RawPPGDatumENS_9allocatorIS4_EEEEEaSB8ne200100EOS4_ : 320 -> 324
~ -[HAFacialMetricsExporter sr_dictionaryRepresentation] : 17684 -> 17704
~ +[HAHermitNotificationAlgorithms analyzeMeasurements:forDateInterval:] : 1376 -> 1380
~ __ZN18HermitNotification9Processor4Impl7processERKNSt3__16vectorINS_8HSReportENS2_9allocatorIS4_EEEENS2_6chrono10time_pointINSA_12system_clockENSA_8durationIdNS2_5ratioILl1ELl1EEEEEEESH_ : 1028 -> 1032
~ __ZNSt3__16vectorIN6mimosa2v230OpticalSamplesV1SubpacketState5Patch6SampleENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZNSt3__16vectorIN6mimosa2v219AccelSubpacketState12SampleHeaderENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 72 -> 76
~ __ZNSt3__16vectorIN6mimosa2v230OpticalSamplesV2SubpacketState5Patch6SampleENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 72 -> 76
~ __ZN6mimosa2v17Decoder11apply_patchERKNS1_5PatchE : 2132 -> 2164
~ __ZNSt3__16vectorINS0_ItNS_9allocatorItEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 304 -> 300
~ __ZN6mimosa2v230OpticalSamplesV1SubpacketState6updateERKNS1_5PatchERKNSt3__16vectorItNS5_9allocatorItEEEE : 1008 -> 1004
~ __ZNSt3__16vectorINS0_ItNS_9allocatorItEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS0_IN6mimosa2v219AccelSubpacketState12SampleHeaderENS_9allocatorIS4_EEEENS5_IS7_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS_5arrayItLm6EEENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS_5arrayItLm9EEENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZN6mimosa2v219AccelSubpacketState6updateERKNS1_5PatchE : 888 -> 896
~ __ZNSt3__16vectorINS0_IN6mimosa2v219AccelSubpacketState12SampleHeaderENS_9allocatorIS4_EEEENS5_IS7_EEE24__emplace_back_slow_pathIJRKS7_EEEPS7_DpOT_ : 316 -> 312
CStrings:
+ "{unique_ptr<health_algorithms::PPGProcessor, std::default_delete<health_algorithms::PPGProcessor>>=\"\"{?=\"__ptr_\"^{PPGProcessor}}}"
+ "{unique_ptr<mimosa::Decoder, std::default_delete<mimosa::Decoder>>=\"\"{?=\"__ptr_\"^{Decoder}}}"
- "{unique_ptr<health_algorithms::PPGProcessor, std::default_delete<health_algorithms::PPGProcessor>>=\"__ptr_\"^{PPGProcessor}}"
- "{unique_ptr<mimosa::Decoder, std::default_delete<mimosa::Decoder>>=\"__ptr_\"^{Decoder}}"

```
