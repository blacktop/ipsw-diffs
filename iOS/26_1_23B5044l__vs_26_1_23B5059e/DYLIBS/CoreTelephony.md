## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13105.1.1.0.0
-  __TEXT.__text: 0x1975c4
-  __TEXT.__auth_stubs: 0x1990
-  __TEXT.__objc_methlist: 0x1b794
+13110.4.0.0.0
+  __TEXT.__text: 0x197d54
+  __TEXT.__auth_stubs: 0x19c0
+  __TEXT.__objc_methlist: 0x1b7cc
   __TEXT.__const: 0x1002
-  __TEXT.__gcc_except_tab: 0x1f8b8
-  __TEXT.__cstring: 0x1fa76
+  __TEXT.__gcc_except_tab: 0x1f8e4
+  __TEXT.__cstring: 0x1faed
   __TEXT.__oslogstring: 0x43ef
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd460
+  __TEXT.__unwind_info: 0xd478
   __TEXT.__objc_classname: 0x5a20
-  __TEXT.__objc_methname: 0x2306f
+  __TEXT.__objc_methname: 0x23164
   __TEXT.__objc_methtype: 0x7322
-  __TEXT.__objc_stubs: 0x16fa0
+  __TEXT.__objc_stubs: 0x17040
   __DATA_CONST.__got: 0xb08
-  __DATA_CONST.__const: 0x73e8
+  __DATA_CONST.__const: 0x7418
   __DATA_CONST.__objc_classlist: 0x1568
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78c8
+  __DATA_CONST.__objc_selrefs: 0x78f8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1810
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__auth_got: 0xcf8
   __AUTH_CONST.__const: 0x2078
-  __AUTH_CONST.__cfstring: 0x1dde0
-  __AUTH_CONST.__objc_const: 0x2fdf0
+  __AUTH_CONST.__cfstring: 0x1de40
+  __AUTH_CONST.__objc_const: 0x2fe20
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xac80
-  __DATA.__objc_ivar: 0x1444
+  __AUTH.__objc_data: 0xabe0
+  __DATA.__objc_ivar: 0x1448
   __DATA.__data: 0x1f88
   __DATA.__bss: 0x1a8
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x2990
+  __DATA_DIRTY.__objc_data: 0x2a30
   __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x1329
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: D2FD2EBB-9395-330B-948A-B3EFA997713B
-  Functions: 11363
-  Symbols:   38549
-  CStrings:  17209
+  UUID: 64FEF65E-1614-3EDB-9A32-80DE591E0695
+  Functions: 11369
+  Symbols:   38574
+  CStrings:  17224
 
Symbols:
+ -[CTDataConnectionAgentData initAgentDataFromCellularInternetPath]
+ -[CTLazuliSystemConfiguration networkAttributionBundleID]
+ -[CTLazuliSystemConfiguration setNetworkAttributionBundleID:]
+ -[CTXPCActivateCrossPlatformTransportRequest initWithEndpoint:from:]
+ -[CTXPCActivateCrossPlatformTransportRequest pid]
+ GCC_except_table573
+ GCC_except_table587
+ GCC_except_table590
+ GCC_except_table591
+ GCC_except_table602
+ GCC_except_table618
+ GCC_except_table641
+ GCC_except_table652
+ GCC_except_table664
+ GCC_except_table689
+ GCC_except_table690
+ GCC_except_table711
+ GCC_except_table715
+ GCC_except_table763
+ GCC_except_table767
+ GCC_except_table771
+ GCC_except_table772
+ GCC_except_table777
+ GCC_except_table788
+ GCC_except_table801
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table816
+ GCC_except_table819
+ GCC_except_table824
+ GCC_except_table829
+ GCC_except_table830
+ GCC_except_table834
+ _OBJC_IVAR_$_CTLazuliSystemConfiguration._networkAttributionBundleID
+ __CTServerConnectionCopyFaceTimeSatelliteUsagePolicy
+ __ZNSt3__110unique_ptrIZ33-[CoreTelephonyClientMux dealloc]E3$_0NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_2NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_1NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_3NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E3$_6NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZZ45-[CoreTelephonyClientMux _getAssertionTypeId]EN3$_88__invokeEPv
+ __ZZN8dispatch5asyncIZ33-[CoreTelephonyClientMux dealloc]E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_2EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_2EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_.cold.1
+ __ZZN8dispatch5asyncIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_3EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E3$_6EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZZ45-[CoreTelephonyClientMux _getAssertionTypeId]ENK3$_8clEPvE27kCTAssertionConnectionClass
+ ____CTServerConnectionCopyFaceTimeSatelliteUsagePolicy_block_invoke
+ ____ZN8dispatch9sync_implIZ54-[CoreTelephonyClientMux proxyWithQueue:errorHandler:]E3$_4EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN8dispatch9sync_implIZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]E3$_5EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN8dispatch9sync_implIZ69-[CoreTelephonyClientMux removeAssertionForInvalidationNotification:]E3$_7EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN8dispatch9sync_implIZ90-[CoreTelephonyClientMux registerBlockForInvalidationNotification:callbackQueue:callback:]E3$_9EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_2clEv_block_invoke
+ ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_2clEv_block_invoke.cold.1
+ ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_1clEv_block_invoke
+ ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_1clEv_block_invoke.cold.1
+ ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_5clEv_block_invoke
+ ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_5clEv_block_invoke.cold.1
+ _getpid
+ _kCTSatelliteDataUsagePolicy
+ _nw_parameters_create
+ _nw_path_evaluator_start
+ _objc_msgSend$activateCrossPlatformTransport:from:completion:
+ _objc_msgSend$initAgentDataFromInternetPath:
+ _objc_msgSend$initWithEndpoint:from:
+ _objc_msgSend$networkAttributionBundleID
+ _objc_msgSend$pid
+ _objc_msgSend$setNetworkAttributionBundleID:
- -[CTXPCActivateCrossPlatformTransportRequest initWithEndpoint:]
- GCC_except_table554
- GCC_except_table584
- GCC_except_table594
- GCC_except_table612
- GCC_except_table634
- GCC_except_table645
- GCC_except_table656
- GCC_except_table682
- GCC_except_table759
- GCC_except_table765
- GCC_except_table769
- GCC_except_table770
- GCC_except_table775
- GCC_except_table782
- GCC_except_table799
- GCC_except_table800
- GCC_except_table803
- GCC_except_table810
- GCC_except_table813
- GCC_except_table818
- GCC_except_table827
- GCC_except_table828
- GCC_except_table832
- __Z21CTThrowingCastIfClassI24CTLazuliGroupChatSubjectEPT_P11objc_object
- __ZNSt3__110unique_ptrIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_1NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_0NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_2NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E3$_5NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZZ45-[CoreTelephonyClientMux _getAssertionTypeId]EN3$_78__invokeEPv
- __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_.cold.1
- __ZZN8dispatch5asyncIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_2EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E3$_5EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZZ45-[CoreTelephonyClientMux _getAssertionTypeId]ENK3$_7clEPvE27kCTAssertionConnectionClass
- ____ZN8dispatch9sync_implIZ54-[CoreTelephonyClientMux proxyWithQueue:errorHandler:]E3$_3EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZN8dispatch9sync_implIZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]E3$_4EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZN8dispatch9sync_implIZ69-[CoreTelephonyClientMux removeAssertionForInvalidationNotification:]E3$_6EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZN8dispatch9sync_implIZ90-[CoreTelephonyClientMux registerBlockForInvalidationNotification:callbackQueue:callback:]E3$_8EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_1clEv_block_invoke
- ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_1clEv_block_invoke.cold.1
- ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_0clEv_block_invoke
- ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_0clEv_block_invoke.cold.1
- ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_4clEv_block_invoke
- ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_4clEv_block_invoke.cold.1
- _objc_msgSend$activateCrossPlatformTransport:completion:
CStrings:
+ ", networkAttributionBundleID = %@"
+ "13110.4"
+ "13110.4~2"
+ "T@\"NSString\",&,N,V_networkAttributionBundleID"
+ "_networkAttributionBundleID"
+ "activateCrossPlatformTransport:from:completion:"
+ "initAgentDataFromCellularInternetPath"
+ "initWithEndpoint:from:"
+ "kCTSatelliteDataUsagePolicy"
+ "kCUGetSatellitePolicyForFaceTime"
+ "kNetworkAttributionBundleID"
+ "networkAttributionBundleID"
+ "setNetworkAttributionBundleID:"
- "13105.1.1"
- "13105.1.1~1"

```
