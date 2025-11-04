## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13114.1.0.0.0
-  __TEXT.__text: 0xc5440
-  __TEXT.__auth_stubs: 0x1780
+13123.3.0.0.0
+  __TEXT.__text: 0xc5bdc
+  __TEXT.__auth_stubs: 0x17a0
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xdbde
-  __TEXT.__cstring: 0x12a8f
-  __TEXT.__gcc_except_tab: 0x121c0
-  __TEXT.__oslogstring: 0x209f
-  __TEXT.__unwind_info: 0x4b40
+  __TEXT.__cstring: 0x12c21
+  __TEXT.__gcc_except_tab: 0x121f0
+  __TEXT.__oslogstring: 0x21bb
+  __TEXT.__unwind_info: 0x4b50
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x3bc
-  __TEXT.__objc_methtype: 0x2f6
+  __TEXT.__objc_methtype: 0x2fa
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6f08
+  __DATA_CONST.__const: 0x6fb0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH_CONST.__const: 0x13b78
+  __AUTH_CONST.__auth_got: 0xbe0
+  __AUTH_CONST.__const: 0x13bc8
   __AUTH_CONST.__cfstring: 0x2aa0
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E1FF6BE-7165-3EED-A36D-693A3A02BC2F
+  UUID: 9C007A82-CEE4-3B2B-82C4-F84C03185A26
   Functions: 5557
-  Symbols:   12631
-  CStrings:  4685
+  Symbols:   12635
+  CStrings:  4718
 
Symbols:
+ _.str.81
+ _.str.82
+ _TelephonyUtilIsOversteerEnabled
+ __ZNK3xpc6object9to_stringEv
+ __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
+ __os_log_debug_impl
- ___TUAssertTrigger
Functions:
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 64 -> 88
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 64 -> 88
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 4 -> 252
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 700 -> 1084
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 88 -> 124
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 248 -> 480
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 28 -> 88
~ __ZN3ctu4rest15read_rest_valueIN4rest19SubscriptionContextEEEvRNSt3__16vectorIT_NS4_9allocatorIS6_EEEERKN3xpc6objectE : 1376 -> 1388
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 64 -> 88
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 540 -> 688
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 632 -> 788
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 360 -> 440
~ __ZNKSt3__120__shared_ptr_pointerIP16HelperRestServerZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI16HelperRestServerE15execute_wrappedIZNS3_11addListenerENSt3__110shared_ptrINS1_20RestDispatchListenerEEEE3$_0EEvOT_EUlvE_EEvP16dispatch_queue_sNS6_10unique_ptrISB_NS6_14default_deleteISB_EEEEENUlPvE_8__invokeESK_ : 612 -> 616
~ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI16HelperRestServerE15execute_wrappedIZNS3_11addListenerENSt3__110shared_ptrINS1_15RestXpcListenerEEEE3$_0EEvOT_EUlvE_EEvP16dispatch_queue_sNS6_10unique_ptrISB_NS6_14default_deleteISB_EEEEENUlPvE_8__invokeESK_ : 612 -> 616
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 8 -> 4
~ __ZNKSt3__120__shared_ptr_pointerIP20FeatureConfigurationNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN4rest15read_rest_valueERNSt3__18optionalINS0_6vectorINS_12PairedDeviceENS0_9allocatorIS3_EEEEEERKN3xpc6objectE : 1628 -> 1624
~ __ZNKSt3__120__shared_ptr_pointerIP14ServiceManagerZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZN3ctu4rest15read_rest_valueINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRNS2_6vectorIT_NS6_ISA_EEEERKN3xpc6objectE : 840 -> 856
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne200100IPS6_SA_EEvT_T0_m : 252 -> 256
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JNS_4pairIS7_S7_EEEEENSG_INS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_ : 216 -> 220
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 64 -> 88
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 64 -> 88
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 92 -> 116
~ __ZNKSt3__120__shared_ptr_pointerIP14AutoStartTimerNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 464 -> 532
~ __ZN21DebugAssertionHandler27handleAssertionChanged_syncEPKcbONSt3__18functionIFNS2_10shared_ptrIN3ctu4rest15AssertionHandleEEEvEEE : 992 -> 980
~ __ZNKSt3__120__shared_ptr_pointerIP21DebugAssertionHandlerZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZN12entitlements29TransferAuthorizationResponse7convertERKNS_42TransferAuthorizationViaWebServiceResponseE : 3388 -> 3396
~ __ZNKSt3__120__shared_ptr_pointerIP32MMSDataContextControllerDelegateNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__113unordered_mapI13SchedulerSpecNS_10unique_ptrIN3ctu5TimerENS_14default_deleteIS4_EEEENS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorINS_4pairIKS1_S7_EEEEE16insert_or_assignB8ne200100IS7_EENSD_INS_19__hash_map_iteratorINS_15__hash_iteratorIPNS_11__hash_nodeINS_17__hash_value_typeIS1_S7_EEPvEEEEEEbEERSE_OT_ : 1268 -> 1272
~ __ZNKSt3__120__shared_ptr_pointerIP17PeriodicSchedulerZN3ctu20SharedSynchronizableIS1_E15make_shared_ptrIS1_EENS_10shared_ptrIT_EEPS8_EUlS2_E_NS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNKSt3__120__shared_ptr_pointerIP13PersonalitiesNS_10shared_ptrIKS1_E27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __Z18isXLAT464InterfacePKc : 164 -> 180
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 624 -> 644
~ __ZN10subscriber16expectedSimCountERKNSt3__110shared_ptrIK8RegistryEE : 336 -> 340
~ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em : 56 -> 60
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 400 -> 464
~ __ZN12_GLOBAL__N_18tokenizeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_11basic_regexIcNS0_12regex_traitsIcEEEE : 2892 -> 2896
~ __ZNKSt3__111basic_regexIcNS_12regex_traitsIcEEE16__match_at_startINS_9allocatorINS_9sub_matchIPKcEEEEEEbS8_S8_RNS_13match_resultsIS8_T_EENS_15regex_constants15match_flag_typeEb : 4184 -> 4196
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE9push_backEOS2_ : 812 -> 816
~ __ZNKSt3__120__shared_ptr_pointerIPNS_13__empty_stateIcEENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
CStrings:
+ "#D DisplayStatus [isOn=%s, isLocked=%s, isCoversheetActive=%s, isPasscodeSet=%s]"
+ "#D Getting main bundle"
+ "#D Input(%s) = %f"
+ "#D Personality Info: %s - %s"
+ "#D Sending OTASP success dialogue to UI"
+ "#D ThumperID: %s, info: %p"
+ "#D [conn %p] Connection closed."
+ "#D [conn %p] Got REST message: %s"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"
+ "feth0"
+ "feth1"
+ "feth10"
+ "feth11"
+ "feth12"
+ "feth13"
+ "feth14"
+ "feth15"
+ "feth16"
+ "feth17"
+ "feth18"
+ "feth19"
+ "feth2"
+ "feth20"
+ "feth3"
+ "feth4"
+ "feth5"
+ "feth6"
+ "feth7"
+ "feth8"
+ "feth9"
+ "not active"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8@16"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@0:8@16"

```
