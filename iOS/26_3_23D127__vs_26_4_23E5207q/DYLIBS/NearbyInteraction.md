## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`

```diff

-507.0.5.0.0
-  __TEXT.__text: 0x327a4
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x3ea8
-  __TEXT.__gcc_except_tab: 0x55c0
-  __TEXT.__cstring: 0x4d5b
-  __TEXT.__const: 0x4e0
+524.0.6.0.0
+  __TEXT.__text: 0x338d4
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x3f10
+  __TEXT.__gcc_except_tab: 0x5758
+  __TEXT.__cstring: 0x502a
+  __TEXT.__const: 0x4f0
   __TEXT.__oslogstring: 0x1365
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1f40
+  __TEXT.__unwind_info: 0x1f78
   __TEXT.__objc_classname: 0x5fc
-  __TEXT.__objc_methname: 0x8d5e
-  __TEXT.__objc_methtype: 0x1637
-  __TEXT.__objc_stubs: 0x4fa0
+  __TEXT.__objc_methname: 0x8e7f
+  __TEXT.__objc_methtype: 0x163d
+  __TEXT.__objc_stubs: 0x5040
   __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0xcb8
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d58
+  __DATA_CONST.__objc_selrefs: 0x1d88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x3f8
-  __AUTH_CONST.__cfstring: 0x5500
-  __AUTH_CONST.__objc_const: 0x7168
-  __AUTH_CONST.__objc_intobj: 0x258
+  __DATA_CONST.__objc_arraydata: 0x40
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__const: 0x418
+  __AUTH_CONST.__cfstring: 0x55e0
+  __AUTH_CONST.__objc_const: 0x71f8
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x4a0
+  __DATA.__objc_ivar: 0x4ac
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x5a0
+  __DATA.__bss: 0x5b0
   __DATA.__common: 0x153
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x70

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 560F4C00-1806-33A4-B14B-D772775EB902
-  Functions: 1457
-  Symbols:   5186
-  CStrings:  3353
+  UUID: A241E590-FD10-3276-A579-72D37B2578A4
+  Functions: 1471
+  Symbols:   5232
+  CStrings:  3380
 
Symbols:
+ +[NIDiscoveryToken(Finding_Project) generateFindingTokenWithServiceID:deviceName:]
+ +[NIPlatformInfo supportsDLTDoA]
+ +[NIPlatformInfo supportsDLTDoA].cold.1
+ -[NIDeviceCapabilities initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:]
+ -[NIDeviceCapabilities initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:]
+ -[NINearbyObject rawRange]
+ -[NINearbyObject setRawRange:]
+ -[NINearbyObject setVioMajorRelocalization:]
+ -[NINearbyObject setVioTrackingState:]
+ -[NINearbyObject vioMajorRelocalization]
+ -[NINearbyObject vioTrackingState]
+ GCC_except_table17
+ _NIPlatformSupportsDLTDOAKey
+ _OBJC_IVAR_$_NINearbyObject._rawRange
+ _OBJC_IVAR_$_NINearbyObject._vioMajorRelocalization
+ _OBJC_IVAR_$_NINearbyObject._vioTrackingState
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE18__assign_with_sizeB9foe210106IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB9foe210106IPKhS6_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB9foe210106IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9foe210106Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB9foe210106IPKmS6_EEvT_T0_m
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorItNS_9allocatorItEEE16__init_with_sizeB9foe210106IPtS5_EEvT_T0_m
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZZ32+[NIPlatformInfo supportsDLTDoA]E14supportsDLTDoA
+ __ZZ32+[NIPlatformInfo supportsDLTDoA]E9onceToken
+ ___18-[NISession pause]_block_invoke.952
+ ___32+[NIPlatformInfo supportsDLTDoA]_block_invoke
+ ___34-[NISession runWithConfiguration:]_block_invoke.945
+ ___34-[NISession runWithConfiguration:]_block_invoke.951
+ ___41-[NISession _serverConnectionInterrupted]_block_invoke.987
+ ___48-[NISession _initAndConnectToServerWithOptions:]_block_invoke.897
+ ___57-[NISession uwbSessionInterruptionReasonEnded:timestamp:]_block_invoke.1015
+ ___Block_byref_object_copy_.957
+ ___Block_byref_object_dispose_.958
+ ___block_literal_global.13
+ ___block_literal_global.1507
+ ___block_literal_global.1511
+ ___block_literal_global.1515
+ ___block_literal_global.1519
+ ___block_literal_global.1523
+ ___block_literal_global.1641
+ ___block_literal_global.1643
+ ___block_literal_global.1648
+ ___block_literal_global.1653
+ ___block_literal_global.1655
+ ___block_literal_global.1679
+ ___block_literal_global.1681
+ ___block_literal_global.17
+ ___block_literal_global.22
+ _objc_msgSend$initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:
+ _objc_msgSend$initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:
+ _objc_msgSend$reasonsPrivate
+ _objc_msgSend$supportsDLTDoA
+ _objc_msgSend$vioMajorRelocalization
+ _objc_msgSend$vioTrackingState
+ _objc_msgSend$worldTransformForObject:
- -[NIDeviceCapabilities initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:]
- -[NIDeviceCapabilities initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:]
- GCC_except_table100
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPKhS6_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne200100Em
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB8ne200100IPKmS6_EEvT_T0_m
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorItNS_9allocatorItEEE16__init_with_sizeB8ne200100IPtS5_EEvT_T0_m
- __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___18-[NISession pause]_block_invoke.949
- ___34-[NISession runWithConfiguration:]_block_invoke.942
- ___34-[NISession runWithConfiguration:]_block_invoke.948
- ___41-[NISession _serverConnectionInterrupted]_block_invoke.984
- ___48-[NISession _initAndConnectToServerWithOptions:]_block_invoke.894
- ___57-[NISession uwbSessionInterruptionReasonEnded:timestamp:]_block_invoke.1012
- ___Block_byref_object_copy_.954
- ___Block_byref_object_dispose_.955
- ___block_literal_global.10
- ___block_literal_global.1504
- ___block_literal_global.1508
- ___block_literal_global.1512
- ___block_literal_global.1516
- ___block_literal_global.1520
- ___block_literal_global.1638
- ___block_literal_global.1640
- ___block_literal_global.1645
- ___block_literal_global.1650
- ___block_literal_global.1652
- ___block_literal_global.1676
- ___block_literal_global.1678
- ___block_literal_global.20
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:
- _objc_msgSend$initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIU8ugDIFMzbLdIp2GpHcHsFaRTkVOiUhd22cII/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU8ugDIFMzbLdIp2GpHcHsFaRTkVOiUhd22cII/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "@40@0:8B16B20B24B28B32B36"
+ "DLTDOASupportedPlatform"
+ "TB,N,V_vioMajorRelocalization"
+ "Tf,N,V_rawRange"
+ "Tq,N,V_vioTrackingState"
+ "_vioMajorRelocalization"
+ "_vioTrackingState"
+ "deviceName"
+ "deviceNameData"
+ "generateFindingTokenWithServiceID:deviceName:"
+ "initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:"
+ "initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:"
+ "serviceID"
+ "serviceIDData"
+ "setVioMajorRelocalization:"
+ "setVioTrackingState:"
+ "supportsDLTDoA"
+ "vioMajorRelocalization"
+ "vioTrackingState"
- "@32@0:8B16B20B24B28"
- "initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:"
- "initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:"

```
