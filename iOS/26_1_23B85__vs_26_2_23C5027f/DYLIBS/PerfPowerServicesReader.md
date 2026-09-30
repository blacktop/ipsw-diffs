## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-2964.42.2.0.0
-  __TEXT.__text: 0x138070
+2964.60.10.0.0
+  __TEXT.__text: 0x1380d4
   __TEXT.__auth_stubs: 0xf30
   __TEXT.__init_offsets: 0xdc
   __TEXT.__objc_methlist: 0x12ba4

   __TEXT.__unwind_info: 0x47b8
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x199e
-  __TEXT.__objc_methname: 0x19622
-  __TEXT.__objc_methtype: 0x2771
+  __TEXT.__objc_methname: 0x19626
+  __TEXT.__objc_methtype: 0x2785
   __TEXT.__objc_stubs: 0x9860
   __DATA_CONST.__got: 0xa90
   __DATA_CONST.__const: 0x29d8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4944D489-87E9-37D8-9DFB-BE461D5D5418
+  UUID: 43CC9A73-E0DC-336F-A133-96D16721F296
   Functions: 7820
   Symbols:   21112
   CStrings:  8265
Functions:
~ __ZNSt3__16vectorINS_4pairIddEENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ -[PPSHistogram initWithDimensions:] : 2088 -> 2100
~ -[PPSHistogram indicesFor:] : 1464 -> 1472
~ -[PPSHistogram recordSample:] : 1292 -> 1296
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE7reserveEm : 232 -> 248
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE8__appendEm : 412 -> 420
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN3pps19AxisConfig_InternalENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_ : 400 -> 412
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZN3pps18Histogram_InternalC2Ev : 492 -> 484
~ __ZN3pps18Histogram_InternalC2Ejdd : 636 -> 628
~ __ZN3pps18Histogram_InternalC2ERKNSt3__16vectorINS_19AxisConfig_InternalENS1_9allocatorIS3_EEEE : 1824 -> 1812
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE18__assign_with_sizeB8ne200100IPSH_SL_EEvT_T0_l : 424 -> 436
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZN5boost9histogram4axis8variableIdNS_11use_defaultES3_NSt3__19allocatorIdEEEC2INS4_11__wrap_iterIPKdEENS0_6detail17requires_iteratorISC_vEEEET_SG_NS4_12basic_stringIcNS4_11char_traitsIcEENS5_IcEEEES6_ : 788 -> 800
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE24__emplace_back_slow_pathIJSB_EEEPSH_DpOT_ : 376 -> 380
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8ne200100IPS6_SA_EEvT_T0_l : 416 -> 420
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE24__emplace_back_slow_pathIJSG_EEEPSH_DpOT_ : 360 -> 364
~ __ZNSt3__16vectorIN5boost9histogram4axis7variantIJNS3_7regularIdNS1_11use_defaultES6_S6_EENS3_8variableIdS6_S6_NS_9allocatorIdEEEENS3_7integerIiS6_NS3_6option3bitILj1EEEEEEEENS9_ISH_EEE24__emplace_back_slow_pathIJS7_EEEPSH_DpOT_ : 356 -> 360
~ __ZNSt3__16vectorIN3pps8AxisEnumENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ ___52-[PPSTimestampConverter _systemOffsetsForTableName:]_block_invoke : 436 -> 440
~ ___54-[PPSTimestampConverter _timeZoneOffsetsForTableName:]_block_invoke : 432 -> 436
CStrings:
+ "T{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=^v^v{?=^v}},R"
+ "{unique_ptr<pps::Histogram_Internal, std::default_delete<pps::Histogram_Internal>>=\"\"{?=\"__ptr_\"^{Histogram_Internal}}}"
+ "{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=^v^v{?=^v}}16@0:8"
+ "{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=^v^v{?=^v}}24@0:8@16"
- "T{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=^v^v^v},R"
- "{unique_ptr<pps::Histogram_Internal, std::default_delete<pps::Histogram_Internal>>=\"__ptr_\"^{Histogram_Internal}}"
- "{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=^v^v^v}16@0:8"
- "{vector<std::pair<double, double>, std::allocator<std::pair<double, double>>>=^v^v^v}24@0:8@16"

```
