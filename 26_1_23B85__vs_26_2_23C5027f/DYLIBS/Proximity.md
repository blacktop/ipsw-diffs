## Proximity

> `/System/Library/PrivateFrameworks/Proximity.framework/Proximity`

```diff

-507.0.2.0.0
-  __TEXT.__text: 0x2f384
+507.0.4.0.0
+  __TEXT.__text: 0x2f3b4
   __TEXT.__auth_stubs: 0x930
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x1fb4

   __TEXT.__oslogstring: 0x103b
   __TEXT.__unwind_info: 0x14c0
   __TEXT.__objc_classname: 0x516
-  __TEXT.__objc_methname: 0x3ff5
-  __TEXT.__objc_methtype: 0x1449
+  __TEXT.__objc_methname: 0x3ff9
+  __TEXT.__objc_methtype: 0x1473
   __TEXT.__objc_stubs: 0x2e60
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x7a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D816555-0007-33CC-82AA-CEF7CC055564
+  UUID: 7C3A1D8D-A1CC-39E3-8BAD-B8090A2B02D4
   Functions: 1074
   Symbols:   4020
   CStrings:  1797
Functions:
~ __ZNSt3__16vectorI6RegionNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN4Rose31ResponderSuperframeRxPacketInfoENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__16vectorIN17SharingHysteresis11DeviceScoreENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 380 -> 384
~ __ZNSt3__16vectorIN17SharingHysteresis11DeviceScoreENS_9allocatorIS2_EEE18__assign_with_sizeB8ne200100IPS2_S7_EEvT_T0_l : 460 -> 464
~ __ZNSt3__16vectorIN17SharingHysteresis11DeviceScoreENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZNSt3__15dequeIN36RangeAngleSharingImportanceEstimator11MeasurementENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPN36RangeAngleSharingImportanceEstimator11MeasurementENS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__15dequeI10BtProxDataNS_9allocatorIS1_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__16vectorI10BtProxDataNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorI20NeighborMeasurementsNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 396 -> 400
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN19SingleThresholdProx9Estimator13addRSSISampleEahd : 292 -> 296
~ __ZN19SingleThresholdProx9Estimator19getRangeMeasurementEdRNS_16RangeMeasurementE : 1612 -> 1616
CStrings:
+ "T{ResponderSuperframeStats=dS{ResponderSuperframeCompleteEvent=SSCd{array<unsigned char, 8UL>=[8C]}SSSCCCCCCdCCCC{vector<Rose::ResponderSuperframeRxPacketInfo, std::allocator<Rose::ResponderSuperframeRxPacketInfo>>=^{ResponderSuperframeRxPacketInfo}^{ResponderSuperframeRxPacketInfo}{?=^{ResponderSuperframeRxPacketInfo}}}}{optional<double>=(?=cd)B}},R"
+ "v112@0:8{NeighborMeasurements={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}dBBddBiBdBB}16d104"
+ "{ResponderSuperframeStats=dS{ResponderSuperframeCompleteEvent=SSCd{array<unsigned char, 8UL>=[8C]}SSSCCCCCCdCCCC{vector<Rose::ResponderSuperframeRxPacketInfo, std::allocator<Rose::ResponderSuperframeRxPacketInfo>>=^{ResponderSuperframeRxPacketInfo}^{ResponderSuperframeRxPacketInfo}{?=^{ResponderSuperframeRxPacketInfo}}}}{optional<double>=(?=cd)B}}16@0:8"
+ "{SharingImportanceMeasurements=\"userSharingInput\"{vector<NeighborMeasurements, std::allocator<NeighborMeasurements>>=\"__begin_\"^{NeighborMeasurements}\"__end_\"^{NeighborMeasurements}\"\"{?=\"__cap_\"^{NeighborMeasurements}}}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}32@0:8Q16Q24"
+ "{deque<BtProxData, std::allocator<BtProxData>>=\"__map_\"{__split_buffer<BtProxData *, std::allocator<BtProxData *>>=\"__first_\"^^{BtProxData}\"__begin_\"^^{BtProxData}\"__end_\"^^{BtProxData}\"\"{?=\"__cap_\"^^{BtProxData}}}\"__start_\"Q\"\"{?=\"__size_\"Q}}"
+ "{unique_ptr<SharingImportanceManager, std::default_delete<SharingImportanceManager>>=\"\"{?=\"__ptr_\"^{SharingImportanceManager}}}"
+ "{unique_ptr<SingleThresholdProx::Estimator, std::default_delete<SingleThresholdProx::Estimator>>=\"\"{?=\"__ptr_\"^{Estimator}}}"
- "T{ResponderSuperframeStats=dS{ResponderSuperframeCompleteEvent=SSCd{array<unsigned char, 8UL>=[8C]}SSSCCCCCCdCCCC{vector<Rose::ResponderSuperframeRxPacketInfo, std::allocator<Rose::ResponderSuperframeRxPacketInfo>>=^{ResponderSuperframeRxPacketInfo}^{ResponderSuperframeRxPacketInfo}^{ResponderSuperframeRxPacketInfo}}}{optional<double>=(?=cd)B}},R"
- "v112@0:8{NeighborMeasurements={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}dBBddBiBdBB}16d104"
- "{ResponderSuperframeStats=dS{ResponderSuperframeCompleteEvent=SSCd{array<unsigned char, 8UL>=[8C]}SSSCCCCCCdCCCC{vector<Rose::ResponderSuperframeRxPacketInfo, std::allocator<Rose::ResponderSuperframeRxPacketInfo>>=^{ResponderSuperframeRxPacketInfo}^{ResponderSuperframeRxPacketInfo}^{ResponderSuperframeRxPacketInfo}}}{optional<double>=(?=cd)B}}16@0:8"
- "{SharingImportanceMeasurements=\"userSharingInput\"{vector<NeighborMeasurements, std::allocator<NeighborMeasurements>>=\"__begin_\"^{NeighborMeasurements}\"__end_\"^{NeighborMeasurements}\"__cap_\"^{NeighborMeasurements}}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}32@0:8Q16Q24"
- "{deque<BtProxData, std::allocator<BtProxData>>=\"__map_\"{__split_buffer<BtProxData *, std::allocator<BtProxData *>>=\"__first_\"^^{BtProxData}\"__begin_\"^^{BtProxData}\"__end_\"^^{BtProxData}\"__cap_\"^^{BtProxData}}\"__start_\"Q\"__size_\"Q}"
- "{unique_ptr<SharingImportanceManager, std::default_delete<SharingImportanceManager>>=\"__ptr_\"^{SharingImportanceManager}}"
- "{unique_ptr<SingleThresholdProx::Estimator, std::default_delete<SingleThresholdProx::Estimator>>=\"__ptr_\"^{Estimator}}"

```
