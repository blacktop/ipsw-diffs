## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-11305.1.0.0.0
-  __TEXT.__text: 0xf0c70
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_methlist: 0xbed8
-  __TEXT.__const: 0xfbf
-  __TEXT.__gcc_except_tab: 0x8eb8
-  __TEXT.__cstring: 0x193ad
+11523.1.0.0.0
+  __TEXT.__text: 0xf47c0
+  __TEXT.__auth_stubs: 0x1820
+  __TEXT.__objc_methlist: 0xc238
+  __TEXT.__const: 0xfaf
+  __TEXT.__gcc_except_tab: 0x91ec
+  __TEXT.__cstring: 0x197af
   __TEXT.__oslogstring: 0x3d9f
-  __TEXT.__unwind_info: 0x51e8
+  __TEXT.__unwind_info: 0x53a0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1c99
-  __TEXT.__objc_methname: 0x16206
-  __TEXT.__objc_methtype: 0x6c62
-  __TEXT.__objc_stubs: 0xe480
+  __TEXT.__objc_classname: 0x1ce2
+  __TEXT.__objc_methname: 0x169a4
+  __TEXT.__objc_methtype: 0x6f42
+  __TEXT.__objc_stubs: 0xe960
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x6738
-  __DATA_CONST.__objc_classlist: 0x688
+  __DATA_CONST.__const: 0x6850
+  __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12400
-  __DATA_CONST.__objc_selrefs: 0x4c90
+  __DATA_CONST.__objc_const: 0x12940
+  __DATA_CONST.__objc_selrefs: 0x4df0
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__objc_const: 0x6e88
+  __AUTH_CONST.__objc_const: 0x7038
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__cfstring: 0x15540
-  __AUTH_CONST.__const: 0x19f0
+  __AUTH_CONST.__cfstring: 0x15840
+  __AUTH_CONST.__const: 0x1a10
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xc38
-  __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x420
-  __DATA.__objc_superrefs: 0x640
-  __DATA.__objc_ivar: 0xcfc
-  __DATA.__data: 0x1e40
-  __DATA.__bss: 0x110
+  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH.__objc_data: 0x1f40
+  __DATA.__objc_ivar: 0xd28
+  __DATA.__data: 0x1e50
+  __DATA.__bss: 0x100
   __DATA.__common: 0x0
   __DATA_DIRTY.__objc_data: 0x2300
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1338
+  __DATA_DIRTY.__bss: 0x1350
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1E43D32-7A3B-3CE8-9B7C-A00D99C9C32D
-  Functions: 6668
-  Symbols:   21138
-  CStrings:  12288
+  UUID: 86747441-9B8C-396E-9D82-EB9A3EFFEA61
+  Functions: 6771
+  Symbols:   21449
+  CStrings:  12423
 
Symbols:
+ +[CTBootstrapState supportsSecureCoding]
+ +[CTCellularPlanQRCodeAction supportsSecureCoding]
+ +[CTPrivateNetworkCapabilities supportsSecureCoding]
+ -[CTBootstrapState bootstrapStatus]
+ -[CTBootstrapState copyWithZone:]
+ -[CTBootstrapState description]
+ -[CTBootstrapState encodeWithCoder:]
+ -[CTBootstrapState initWithCoder:]
+ -[CTBootstrapState setBootstrapStatus:]
+ -[CTCarrierSignupPlan initWithName:url:type:option:]
+ -[CTCarrierSignupPlan option]
+ -[CTCellularPlanManagerCameraScanAction performWithAppName:completionHandler:]
+ -[CTCellularPlanQRCodeAction .cxx_destruct]
+ -[CTCellularPlanQRCodeAction OID]
+ -[CTCellularPlanQRCodeAction copyWithZone:]
+ -[CTCellularPlanQRCodeAction description]
+ -[CTCellularPlanQRCodeAction encodeWithCoder:]
+ -[CTCellularPlanQRCodeAction initWithCoder:]
+ -[CTCellularPlanQRCodeAction matchingId]
+ -[CTCellularPlanQRCodeAction message]
+ -[CTCellularPlanQRCodeAction performWithCompletionHandler:]
+ -[CTCellularPlanQRCodeAction setMatchingId:]
+ -[CTCellularPlanQRCodeAction setMessage:]
+ -[CTCellularPlanQRCodeAction setOID:]
+ -[CTCellularPlanQRCodeAction setSmdpAddress:]
+ -[CTCellularPlanQRCodeAction setTitle:]
+ -[CTCellularPlanQRCodeAction smdpAddress]
+ -[CTCellularPlanQRCodeAction title]
+ -[CTDisplayPlan copyWithZone:]
+ -[CTDisplayPlanList copyWithZone:]
+ -[CTPendingPlan copyWithZone:]
+ -[CTPlan copyWithZone:]
+ -[CTPrivateNetworkCapabilities copyWithZone:]
+ -[CTPrivateNetworkCapabilities description]
+ -[CTPrivateNetworkCapabilities encodeWithCoder:]
+ -[CTPrivateNetworkCapabilities hideDataRoaming]
+ -[CTPrivateNetworkCapabilities initWithCoder:]
+ -[CTPrivateNetworkCapabilities init]
+ -[CTPrivateNetworkCapabilities isPrivateNetworkModeEnabled]
+ -[CTPrivateNetworkCapabilities isPrivateNetworkPreferredOverWifi]
+ -[CTPrivateNetworkCapabilities isPrivateNetworkSIM]
+ -[CTPrivateNetworkCapabilities setHideDataRoaming:]
+ -[CTPrivateNetworkCapabilities setIsPrivateNetworkModeEnabled:]
+ -[CTPrivateNetworkCapabilities setIsPrivateNetworkPreferredOverWifi:]
+ -[CTPrivateNetworkCapabilities setIsPrivateNetworkSIM:]
+ -[CoreTelephonyClient(Bootstrap) getBootstrapState:]
+ -[CoreTelephonyClient(CellularPlanManager) _decodeCardData:smdp:matchingID:OID:]
+ -[CoreTelephonyClient(CellularPlanManager) addQRCodePlanWith:appType:completionHandler:]
+ -[CoreTelephonyClient(CellularPlanManager) checkPreFlightEligibility:mccs:mncs:gid1s:gid2s:smdpUrl:iccidPrefix:completion:]
+ -[CoreTelephonyClient(CellularPlanManager) checkProfileEligibility:metadata:completion:]
+ -[CoreTelephonyClient(CellularPlanManager) getActionForCardData:completionHandler:]
+ -[CoreTelephonyClient(CellularPlanManager) handleTermsAndConditionsCompleted:consented:completion:]
+ -[CoreTelephonyClient(CellularPlanManager) handleUserEnteredOtp:otp:completion:]
+ -[CoreTelephonyClient(CellularPlanManager) isAutofilleSIMIdAllowedForDomain:clientBundleIdentifier:error:]
+ -[CoreTelephonyClient(CellularPlanManager) isAutofilleSIMIdAllowedForDomain:error:]
+ -[CoreTelephonyClient(CellularPlanManager) renewOneTimePassword:completion:]
+ -[CoreTelephonyClient(CellularPlanManager) retrieveDeviceIdentifier:clientBundleIdentifier:error:]
+ -[CoreTelephonyClient(CellularPlanManager) retrieveDeviceIdentifier:error:]
+ -[CoreTelephonyClient(CellularPlanManager) startPendingPlanInstallationForPlan:carrierName:completionHandler:]
+ -[CoreTelephonyClient(Data) requestSliceByUUID:completion:]
+ -[CoreTelephonyClient(PlanTransfer) getLocalDeviceIdentiferForSIMTransfer:]
+ -[CoreTelephonyClient(PrivateNetwork) getPrivateNetworkCapabilitiesForContext:completion:]
+ -[CoreTelephonyClient(PrivateNetwork) getPrivateNetworkCapabilitiesForContext:error:]
+ -[CoreTelephonyClient(PrivateNetwork) isPrivateNetworkContext:completion:]
+ -[CoreTelephonyClient(PrivateNetwork) isPrivateNetworkContext:error:]
+ -[CoreTelephonyClient(RemotePlan) transferRemotePlan:completion:]
+ -[CoreTelephonyClient(Vinyl) getEuiccData:]
+ GCC_except_table155
+ GCC_except_table168
+ GCC_except_table180
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table195
+ _CTBootstrapStatusAsString
+ _CTCellularPlanDeviceIdentifierAll
+ _CTCellularPlanDeviceIdentifierAsString
+ _CTPlanPurchaseOptionAsString
+ _OBJC_CLASS_$_CTBootstrapState
+ _OBJC_CLASS_$_CTCellularPlanQRCodeAction
+ _OBJC_CLASS_$_CTPrivateNetworkCapabilities
+ _OBJC_IVAR_$_CTBootstrapState._bootstrapStatus
+ _OBJC_IVAR_$_CTCarrierSignupPlan._option
+ _OBJC_IVAR_$_CTCellularPlanQRCodeAction._OID
+ _OBJC_IVAR_$_CTCellularPlanQRCodeAction._matchingId
+ _OBJC_IVAR_$_CTCellularPlanQRCodeAction._message
+ _OBJC_IVAR_$_CTCellularPlanQRCodeAction._smdpAddress
+ _OBJC_IVAR_$_CTCellularPlanQRCodeAction._title
+ _OBJC_IVAR_$_CTPrivateNetworkCapabilities._hideDataRoaming
+ _OBJC_IVAR_$_CTPrivateNetworkCapabilities._isPrivateNetworkModeEnabled
+ _OBJC_IVAR_$_CTPrivateNetworkCapabilities._isPrivateNetworkPreferredOverWifi
+ _OBJC_IVAR_$_CTPrivateNetworkCapabilities._isPrivateNetworkSIM
+ _OBJC_METACLASS_$_CTBootstrapState
+ _OBJC_METACLASS_$_CTCellularPlanQRCodeAction
+ _OBJC_METACLASS_$_CTPrivateNetworkCapabilities
+ __OBJC_$_CLASS_METHODS_CTBootstrapState
+ __OBJC_$_CLASS_METHODS_CTCellularPlanQRCodeAction
+ __OBJC_$_CLASS_METHODS_CTPrivateNetworkCapabilities
+ __OBJC_$_CLASS_PROP_LIST_CTBootstrapState
+ __OBJC_$_CLASS_PROP_LIST_CTCellularPlanQRCodeAction
+ __OBJC_$_CLASS_PROP_LIST_CTPrivateNetworkCapabilities
+ __OBJC_$_INSTANCE_METHODS_CTBootstrapState
+ __OBJC_$_INSTANCE_METHODS_CTCellularPlanQRCodeAction
+ __OBJC_$_INSTANCE_METHODS_CTPrivateNetworkCapabilities
+ __OBJC_$_INSTANCE_VARIABLES_CTBootstrapState
+ __OBJC_$_INSTANCE_VARIABLES_CTCellularPlanQRCodeAction
+ __OBJC_$_INSTANCE_VARIABLES_CTPrivateNetworkCapabilities
+ __OBJC_$_PROP_LIST_CTBootstrapState
+ __OBJC_$_PROP_LIST_CTCellularPlanQRCodeAction
+ __OBJC_$_PROP_LIST_CTPrivateNetworkCapabilities
+ __OBJC_CLASS_PROTOCOLS_$_CTBootstrapState
+ __OBJC_CLASS_PROTOCOLS_$_CTCellularPlanQRCodeAction
+ __OBJC_CLASS_PROTOCOLS_$_CTPrivateNetworkCapabilities
+ __OBJC_CLASS_RO_$_CTBootstrapState
+ __OBJC_CLASS_RO_$_CTCellularPlanQRCodeAction
+ __OBJC_CLASS_RO_$_CTPrivateNetworkCapabilities
+ __OBJC_METACLASS_RO_$_CTBootstrapState
+ __OBJC_METACLASS_RO_$_CTCellularPlanQRCodeAction
+ __OBJC_METACLASS_RO_$_CTPrivateNetworkCapabilities
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8un170006IS4_EENS_12basic_stringIcS2_T_EERKS8_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8un170006Ev
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8un170006EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8un170006ERKS6_S9_
+ __ZNKSt9type_infoeqB8un170006ERKS_
+ __ZNSt3__110shared_ptrIN3xpc4dictEE5resetB8un170006IS2_PFvPS2_EvEEvPT_T0_
+ __ZNSt3__110unique_ptrIN3ctu11OsLogLoggerENS_14default_deleteIS2_EEE5resetB8un170006EPS2_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvN3xpc4dictEEEEEEPvEENS_22__tree_node_destructorINS6_ISI_EEEEE5resetB8un170006EPSI_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU8__strongU13block_pointerFvP18CTStewieMessageAckP12NSDictionaryEEEEEPvEENS_22__tree_node_destructorINS6_ISL_EEEEE5resetB8un170006EPSL_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIP17__CTAssertionTypeNS_4pairIN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEEEEPvEENS_22__tree_node_destructorINS_9allocatorISG_EEEEE5resetB8un170006EPSG_
+ __ZNSt3__110unique_ptrIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_1NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_0NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZ45-[CTStewieDataClient sendMessage:completion:]E3$_2NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZ46-[CTStewieDataClient dispatchOnDelegateQueue:]E3$_1NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClient dispatchBlockToClientAsync:]E3$_0NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_2NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZ54-[CoreTelephonyClientDelegateProxy forwardInvocation:]E3$_0NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZZ32-[CTConnectionPair receiveData:]EUb_E3$_0NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__110unique_ptrIZZZ52-[CTStewieDataClient receivedData:fromConnectionId:]EUb_EUb0_E3$_3NS_14default_deleteIS1_EEED1B8un170006Ev
+ __ZNSt3__112__destroy_atB8un170006INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvN3xpc4dictEEEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8un170006INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU8__strongU13block_pointerFvP18CTStewieMessageAckP12NSDictionaryEEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8un170006INS_4pairIKP17__CTAssertionTypeNS1_IN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEEEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8un170006ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8un170006EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8un170006Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8un170006ILi0EEEPKc
+ __ZNSt3__113__tree_removeB8un170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferI19MMSEnumerationValueRNS_9allocatorIS1_EEE17__destruct_at_endB8un170006EPS1_
+ __ZNSt3__114__split_bufferIN3ctu2cf11CFSharedRefIKvEERNS_9allocatorIS5_EEE5clearB8un170006Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8un170006Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8un170006ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__116__pad_and_outputB8un170006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeIP11objc_objectN12_GLOBAL__N_115DelegateContextEEEPvEEEEE7destroyB8un170006INS_4pairIKS5_S8_EEvvEEvRSC_PT_
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8un170006Ev
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorI19MMSEnumerationValueEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIN3ctu2cf11CFSharedRefIKvEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIP11MMSMimePartEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIP9MMSHeaderEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIPK17MMSHeaderEncodingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIU8__strongP8ProtocolEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8un170006Ev
+ __ZNSt3__119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8un170006ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8un170006Ev
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8un170006EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8un170006EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8un170006EPKcm
+ __ZNSt3__123__optional_storage_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EE16__construct_fromB8un170006IRKNS_20__optional_copy_baseIS6_Lb0EEEEEvOT_
+ __ZNSt3__124__put_character_sequenceB8un170006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB8un170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__13mapIP13objc_selectorN12_GLOBAL__N_111CachePolicyENS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S4_EEEEEC1B8un170006ESt16initializer_listISA_ERKS6_
+ __ZNSt3__13mapIP13objc_selectorS2_NS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S2_EEEEEC2B8un170006ESt16initializer_listIS8_ERKS4_
+ __ZNSt3__13mapIP17__CTAssertionTypeNS_4pairIN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEENS_4lessIS2_EENS_9allocatorINS3_IKS2_SB_EEEEE16insert_or_assignB8un170006ISB_EENS3_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS2_SB_EEPNS_11__tree_nodeISN_PvEElEEEEbEERSF_OT_
+ __ZNSt3__13mapIjN12_GLOBAL__N_111ContentTypeENS_4lessIjEENS_9allocatorINS_4pairIKjS2_EEEEEC1B8un170006ESt16initializer_listIS8_ERKS4_
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU8__strongU13block_pointerFvP18CTStewieMessageAckP12NSDictionaryEEEEC2B8un170006ERKSI_
+ __ZNSt3__14pairIN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEaSB8un170006EOS8_
+ __ZNSt3__16vectorI19MMSEnumerationValueNS_9allocatorIS1_EEE16__destroy_vectorclB8un170006Ev
+ __ZNSt3__16vectorI19MMSEnumerationValueNS_9allocatorIS1_EEE7__clearB8un170006Ev
+ __ZNSt3__16vectorIN3ctu2cf11CFSharedRefIKvEENS_9allocatorIS5_EEE16__destroy_vectorclB8un170006Ev
+ __ZNSt3__16vectorIN3ctu2cf11CFSharedRefIKvEENS_9allocatorIS5_EEE7__clearB8un170006Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8un170006Em
+ __ZNSt3__16vectorIU8__strongP8ProtocolNS_9allocatorIS3_EEE16__destroy_vectorclB8un170006Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8un170006Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE18__assign_with_sizeB8un170006IPKcS6_EEvT_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8un170006IPKhS6_EENS_11__wrap_iterIPhEENS7_IS6_EET_T0_l
+ __ZNSt3__18optionalINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8un170006IRS6_vEERS7_OT_
+ __ZNSt3__1eqB8un170006INS_6vectorI18CEPlanSupportedRATNS_9allocatorIS2_EEEES5_EENS_9enable_ifIX16is_convertible_vIDTeqclsr3stdE7declvalIRKT_EEclsr3stdE7declvalIRKT0_EEEbEEbE4typeERKNS_8optionalIS7_EERKNSG_ISA_EE
+ __ZNSt3__1lsB8un170006INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
+ __ZNSt3__1rsB8un170006IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
+ __ZNSt3__1ssB8un170006IcNS_11char_traitsIcEEEEDaNS_17basic_string_viewIT_T0_EES7_
+ __ZNSt3__1ssB8un170006IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt28__throw_bad_array_new_lengthB8un170006v
+ ___106-[CoreTelephonyClient(CellularPlanManager) isAutofilleSIMIdAllowedForDomain:clientBundleIdentifier:error:]_block_invoke
+ ___106-[CoreTelephonyClient(CellularPlanManager) isAutofilleSIMIdAllowedForDomain:clientBundleIdentifier:error:]_block_invoke_2
+ ___110-[CoreTelephonyClient(CellularPlanManager) startPendingPlanInstallationForPlan:carrierName:completionHandler:]_block_invoke
+ ___123-[CoreTelephonyClient(CellularPlanManager) checkPreFlightEligibility:mccs:mncs:gid1s:gid2s:smdpUrl:iccidPrefix:completion:]_block_invoke
+ ___25-[CTConnectionPair start]_block_invoke.54
+ ___25-[CTConnectionPair start]_block_invoke.54.cold.1
+ ___39-[CoreTelephonyClientMux _connect_sync]_block_invoke.353
+ ___39-[CoreTelephonyClientMux _connect_sync]_block_invoke.354
+ ___39-[CoreTelephonyClientMux _connect_sync]_block_invoke.354.cold.1
+ ___43-[CoreTelephonyClient(Vinyl) getEuiccData:]_block_invoke
+ ___52-[CoreTelephonyClient(Bootstrap) getBootstrapState:]_block_invoke
+ ___52-[CoreTelephonyClient(Bootstrap) getBootstrapState:]_block_invoke_2
+ ___59-[CTCellularPlanQRCodeAction performWithCompletionHandler:]_block_invoke
+ ___59-[CoreTelephonyClient(Data) requestSliceByUUID:completion:]_block_invoke
+ ___65-[CoreTelephonyClient(RemotePlan) transferRemotePlan:completion:]_block_invoke
+ ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.63
+ ___69-[CoreTelephonyClient(PrivateNetwork) isPrivateNetworkContext:error:]_block_invoke
+ ___69-[CoreTelephonyClient(PrivateNetwork) isPrivateNetworkContext:error:]_block_invoke_2
+ ___74-[CoreTelephonyClient(PrivateNetwork) isPrivateNetworkContext:completion:]_block_invoke
+ ___75-[CoreTelephonyClient(PlanTransfer) getLocalDeviceIdentiferForSIMTransfer:]_block_invoke
+ ___75-[CoreTelephonyClient(PlanTransfer) getLocalDeviceIdentiferForSIMTransfer:]_block_invoke_2
+ ___76-[CoreTelephonyClient(CellularPlanManager) renewOneTimePassword:completion:]_block_invoke
+ ___78-[CTCellularPlanManagerCameraScanAction performWithAppName:completionHandler:]_block_invoke
+ ___80-[CoreTelephonyClient(CellularPlanManager) handleUserEnteredOtp:otp:completion:]_block_invoke
+ ___83-[CoreTelephonyClient(CellularPlanManager) getActionForCardData:completionHandler:]_block_invoke
+ ___83-[CoreTelephonyClient(CellularPlanManager) getActionForCardData:completionHandler:]_block_invoke_2
+ ___83-[CoreTelephonyClient(CellularPlanManager) isAutofilleSIMIdAllowedForDomain:error:]_block_invoke
+ ___83-[CoreTelephonyClient(CellularPlanManager) isAutofilleSIMIdAllowedForDomain:error:]_block_invoke_2
+ ___85-[CoreTelephonyClient(PrivateNetwork) getPrivateNetworkCapabilitiesForContext:error:]_block_invoke
+ ___85-[CoreTelephonyClient(PrivateNetwork) getPrivateNetworkCapabilitiesForContext:error:]_block_invoke_2
+ ___88-[CoreTelephonyClient(CellularPlanManager) addQRCodePlanWith:appType:completionHandler:]_block_invoke
+ ___88-[CoreTelephonyClient(CellularPlanManager) checkProfileEligibility:metadata:completion:]_block_invoke
+ ___90-[CoreTelephonyClient(PrivateNetwork) getPrivateNetworkCapabilitiesForContext:completion:]_block_invoke
+ ___98-[CoreTelephonyClient(CellularPlanManager) retrieveDeviceIdentifier:clientBundleIdentifier:error:]_block_invoke
+ ___98-[CoreTelephonyClient(CellularPlanManager) retrieveDeviceIdentifier:clientBundleIdentifier:error:]_block_invoke_2
+ ___99-[CoreTelephonyClient(CellularPlanManager) handleTermsAndConditionsCompleted:consented:completion:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e38_v24?0"CTBootstrapState"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e40_v24?0"CTDeviceIdentifier"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e50_v24?0"CTPrivateNetworkCapabilities"8"NSError"16lr32l8r40l8
+ ___block_descriptor_56_ea8_32r40r_e40_v24?0"CTDeviceIdentifier"8"NSError"16lr32l8r40l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e43_v32?0"NSString"8"NSString"16"NSError"24ls56l8s32l8s40l8s48l8
+ ___block_literal_global.1136
+ ___block_literal_global.1141
+ ___block_literal_global.1145
+ ___block_literal_global.27
+ ___block_literal_global.31
+ ___block_literal_global.33
+ ___block_literal_global.37
+ _kCTNetworkSlicingCategories
+ _kCTNetworkSlicingCategoryID
+ _kCTNetworkSlicingCategoryName
+ _kCTNetworkSlicingCategoryState
+ _kCTPhoneNumberRegistrationResponseLabelID
+ _objc_msgSend$_decodeCardData:smdp:matchingID:OID:
+ _objc_msgSend$addQRCodePlanWith:appName:appType:completionHandler:
+ _objc_msgSend$addQRCodePlanWith:appType:completionHandler:
+ _objc_msgSend$bootstrapStatus
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$canRunActivationCodeProvisioningWithCompletion:
+ _objc_msgSend$checkPreFlightEligibility:mccs:mncs:gid1s:gid2s:smdpUrl:iccidPrefix:completion:
+ _objc_msgSend$checkProfileEligibility:metadata:completion:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$getBootstrapState:
+ _objc_msgSend$getEuiccData:
+ _objc_msgSend$getLocalDeviceIdentifer:clientBundleIdentifier:completion:
+ _objc_msgSend$getPrivateNetworkCapabilitiesForContext:completion:
+ _objc_msgSend$handleTermsAndConditionsCompleted:consented:completion:
+ _objc_msgSend$handleUserEnteredOtp:otp:completion:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hideDataRoaming
+ _objc_msgSend$initWithDisplayPlans:
+ _objc_msgSend$initWithPlan:status:attributes:isPhysical:carrierName:phoneNumber:label:
+ _objc_msgSend$initWithSmdpURL:matchingID:
+ _objc_msgSend$isAutofilleSIMIdAllowedForDomain:bundleIdentifier:completion:
+ _objc_msgSend$isAutofilleSIMIdAllowedForDomain:clientBundleIdentifier:completion:
+ _objc_msgSend$isPrivateNetworkContext:completion:
+ _objc_msgSend$isPrivateNetworkModeEnabled
+ _objc_msgSend$isPrivateNetworkPreferredOverWifi
+ _objc_msgSend$isPrivateNetworkSIM
+ _objc_msgSend$localizedInfoDictionary
+ _objc_msgSend$option
+ _objc_msgSend$performWithAppName:completionHandler:
+ _objc_msgSend$renewOneTimePassword:completion:
+ _objc_msgSend$requestSliceByUUID:completion:
+ _objc_msgSend$retrieveDeviceIdentifier:clientBundleIdentifier:error:
+ _objc_msgSend$setBootstrapStatus:
+ _objc_msgSend$setHideDataRoaming:
+ _objc_msgSend$setIsPrivateNetworkModeEnabled:
+ _objc_msgSend$setIsPrivateNetworkPreferredOverWifi:
+ _objc_msgSend$setIsPrivateNetworkSIM:
+ _objc_msgSend$startPendingPlanInstallationForPlan:carrierName:completionHandler:
+ _objc_msgSend$transferRemotePlan:completion:
- GCC_except_table127
- GCC_except_table148
- GCC_except_table157
- GCC_except_table160
- GCC_except_table170
- GCC_except_table178
- GCC_except_table182
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareES3_
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB7v160006ERKS6_S9_
- __ZNKSt9type_infoeqB7v160006ERKS_
- __ZNSt3__110shared_ptrIN3xpc4dictEE5resetB7v160006IS2_PFvPS2_EvEEvPT_T0_
- __ZNSt3__110unique_ptrIN3ctu11OsLogLoggerENS_14default_deleteIS2_EEE5resetB7v160006EPS2_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvN3xpc4dictEEEEEEPvEENS_22__tree_node_destructorINS6_ISI_EEEEE5resetB7v160006EPSI_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU8__strongU13block_pointerFvP18CTStewieMessageAckP12NSDictionaryEEEEEPvEENS_22__tree_node_destructorINS6_ISL_EEEEE5resetB7v160006EPSL_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIP17__CTAssertionTypeNS_4pairIN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEEEEPvEENS_22__tree_node_destructorINS_9allocatorISG_EEEEE5resetB7v160006EPSG_
- __ZNSt3__110unique_ptrIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_1NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_0NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZ45-[CTStewieDataClient sendMessage:completion:]E3$_2NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZ46-[CTStewieDataClient dispatchOnDelegateQueue:]E3$_1NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClient dispatchBlockToClientAsync:]E3$_0NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_2NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZ54-[CoreTelephonyClientDelegateProxy forwardInvocation:]E3$_0NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZZ32-[CTConnectionPair receiveData:]EUb_E3$_0NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZZZ52-[CTStewieDataClient receivedData:fromConnectionId:]EUb_EUb0_E3$_3NS_14default_deleteIS1_EEED1B7v160006Ev
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvN3xpc4dictEEEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU8__strongU13block_pointerFvP18CTStewieMessageAckP12NSDictionaryEEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKP17__CTAssertionTypeNS1_IN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__113__tree_removeB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferI19MMSEnumerationValueRNS_9allocatorIS1_EEE17__destruct_at_endB7v160006EPS1_
- __ZNSt3__114__split_bufferIN3ctu2cf11CFSharedRefIKvEERNS_9allocatorIS5_EEE5clearB7v160006Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- __ZNSt3__116__pad_and_outputB7v160006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeIP11objc_objectN12_GLOBAL__N_115DelegateContextEEEPvEEEEE7destroyB7v160006INS_4pairIKS5_S8_EEvvEEvRSC_PT_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI19MMSEnumerationValueEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIN3ctu2cf11CFSharedRefIKvEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP11MMSMimePartEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP9MMSHeaderEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIPK17MMSHeaderEncodingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIU8__strongP8ProtocolEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB7v160006Ev
- __ZNSt3__119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EEclEPKvm
- __ZNSt3__123__optional_storage_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EE16__construct_fromB7v160006IRKNS_20__optional_copy_baseIS6_Lb0EEEEEvOT_
- __ZNSt3__124__put_character_sequenceB7v160006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__13mapIP13objc_selectorN12_GLOBAL__N_111CachePolicyENS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S4_EEEEEC1B7v160006ESt16initializer_listISA_ERKS6_
- __ZNSt3__13mapIP13objc_selectorS2_NS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S2_EEEEEC2B7v160006ESt16initializer_listIS8_ERKS4_
- __ZNSt3__13mapIP17__CTAssertionTypeNS_4pairIN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEENS_4lessIS2_EENS_9allocatorINS3_IKS2_SB_EEEEE16insert_or_assignB7v160006ISB_EENS3_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS2_SB_EEPNS_11__tree_nodeISN_PvEElEEEEbEERSF_OT_
- __ZNSt3__13mapIjN12_GLOBAL__N_111ContentTypeENS_4lessIjEENS_9allocatorINS_4pairIKjS2_EEEEEC1B7v160006ESt16initializer_listIS8_ERKS4_
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch5blockIU8__strongU13block_pointerFvP18CTStewieMessageAckP12NSDictionaryEEEEC2ERKSI_
- __ZNSt3__14pairIN8dispatch5queueEU8__strongU13block_pointerFvP7NSErrorEEaSB7v160006EOS8_
- __ZNSt3__16vectorI19MMSEnumerationValueNS_9allocatorIS1_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorI19MMSEnumerationValueNS_9allocatorIS1_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorIN3ctu2cf11CFSharedRefIKvEENS_9allocatorIS5_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIN3ctu2cf11CFSharedRefIKvEENS_9allocatorIS5_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIU8__strongP8ProtocolNS_9allocatorIS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEE6assignIPKcLi0EEEvT_S7_
- __ZNSt3__16vectorIhNS_9allocatorIhEEE6insertIPKhLi0EEENS_11__wrap_iterIPhEENS7_IS6_EET_SB_
- __ZNSt3__18optionalINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB7v160006IRS6_vEERS7_OT_
- __ZNSt3__1L19piecewise_constructE
- __ZNSt3__1eqB7v160006INS_6vectorI18CEPlanSupportedRATNS_9allocatorIS2_EEEES5_EENS_9enable_ifIX16is_convertible_vIDTeqclsr3stdE7declvalIRKT_EEclsr3stdE7declvalIRKT0_EEEbEEbE4typeERKNS_8optionalIS7_EERKNSG_ISA_EE
- __ZNSt3__1lsB7v160006INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_RKNS_8__iom_t4IcEE
- __ZNSt3__1rsB7v160006IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
- __ZNSt3__1ssB7v160006IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___25-[CTConnectionPair start]_block_invoke.53
- ___25-[CTConnectionPair start]_block_invoke.53.cold.1
- ___39-[CoreTelephonyClientMux _connect_sync]_block_invoke.350
- ___39-[CoreTelephonyClientMux _connect_sync]_block_invoke.351
- ___39-[CoreTelephonyClientMux _connect_sync]_block_invoke.351.cold.1
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.61
- ___70-[CTCellularPlanManagerCameraScanAction performWithCompletionHandler:]_block_invoke
- ___block_literal_global.10
- ___block_literal_global.1106
- ___block_literal_global.1111
- ___block_literal_global.1115
- ___block_literal_global.13
- ___block_literal_global.17
- ___block_literal_global.19
- ___block_literal_global.21
- _kCTCapabilityNetworkSlicingManaged
CStrings:
+ ", bootstrapStatus=%s"
+ ", hideDataRoaming=%d"
+ ", isPrivateNetworkModeEnabled=%d"
+ ", isPrivateNetworkPreferredOverWifi=%d"
+ ", isPrivateNetworkSIM=%d"
+ ", option=%s"
+ "11523.1"
+ "11523.1~41"
+ "??"
+ "@48@0:8@16@24@32q40"
+ "All"
+ "B48@0:8@16^@24^@32^@40"
+ "CTBootstrapAvailable"
+ "CTBootstrapNotAvailable"
+ "CTBootstrapRecommended"
+ "CTBootstrapState"
+ "CTCellularPlanQRCodeAction"
+ "CTPlanAllowPurchaseOverBootstrap"
+ "CTPlanDisallowPurchaseOverBootstrap"
+ "CTPlanPurchaseOptionDefault"
+ "CTPrivateNetworkCapabilities"
+ "LPA:1"
+ "Received callback for public add plan - results CANCEL"
+ "Received callback for public add plan - results FAIL"
+ "Received callback for public add plan - results SUCCESS"
+ "Received callback for public add plan - results UNKNOWN"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_hideDataRoaming"
+ "TB,N,V_isPrivateNetworkModeEnabled"
+ "TB,N,V_isPrivateNetworkPreferredOverWifi"
+ "TB,N,V_isPrivateNetworkSIM"
+ "Ti,N,V_bootstrapStatus"
+ "Tq,R,N,V_option"
+ "_bootstrapStatus"
+ "_decodeCardData:smdp:matchingID:OID:"
+ "_hideDataRoaming"
+ "_isPrivateNetworkModeEnabled"
+ "_isPrivateNetworkPreferredOverWifi"
+ "_isPrivateNetworkSIM"
+ "_option"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-"
+ "addQRCodePlanWith:appName:appType:completionHandler:"
+ "addQRCodePlanWith:appType:completionHandler:"
+ "bootsrtap_state"
+ "bootstrapStatus"
+ "bundleIdentifier"
+ "canRunActivationCodeProvisioningWithCompletion:"
+ "checkPreFlightEligibility:mccs:mncs:gid1s:gid2s:smdpUrl:iccidPrefix:completion:"
+ "checkProfileEligibility:metadata:completion:"
+ "com.apple"
+ "com.apple."
+ "componentsSeparatedByString:"
+ "getActionForCardData:completionHandler:"
+ "getBootstrapState:"
+ "getEuiccData:"
+ "getLocalDeviceIdentifer:clientBundleIdentifier:completion:"
+ "getLocalDeviceIdentiferForSIMTransfer:"
+ "getPrivateNetworkCapabilitiesForContext:completion:"
+ "getPrivateNetworkCapabilitiesForContext:error:"
+ "handleTermsAndConditionsCompleted:consented:completion:"
+ "handleUserEnteredOtp:otp:completion:"
+ "hasPrefix:"
+ "hideDataRoaming"
+ "initWithName:url:type:option:"
+ "isAutofilleSIMIdAllowedForDomain:bundleIdentifier:completion:"
+ "isAutofilleSIMIdAllowedForDomain:clientBundleIdentifier:completion:"
+ "isAutofilleSIMIdAllowedForDomain:clientBundleIdentifier:error:"
+ "isAutofilleSIMIdAllowedForDomain:error:"
+ "isPrivateNetworkContext:completion:"
+ "isPrivateNetworkContext:error:"
+ "isPrivateNetworkModeEnabled"
+ "isPrivateNetworkPreferredOverWifi"
+ "isPrivateNetworkSIM"
+ "kCTNetworkSlicingCategories"
+ "kCTNetworkSlicingCategoryID"
+ "kCTNetworkSlicingCategoryName"
+ "kCTNetworkSlicingCategoryState"
+ "localizedInfoDictionary"
+ "option"
+ "performWithAppName:completionHandler:"
+ "plansDidUpdate:"
+ "renewOneTimePassword:completion:"
+ "requestSliceByUUID:completion:"
+ "retrieveDeviceIdentifier:clientBundleIdentifier:error:"
+ "retrieveDeviceIdentifier:error:"
+ "setBootstrapStatus:"
+ "setHideDataRoaming:"
+ "setIsPrivateNetworkModeEnabled:"
+ "setIsPrivateNetworkPreferredOverWifi:"
+ "setIsPrivateNetworkSIM:"
+ "sim-label-id"
+ "startPendingPlanInstallationForPlan:carrierName:completionHandler:"
+ "transferRemotePlan:completion:"
+ "v24@0:8@\"CTDisplayPlanList\"16"
+ "v24@0:8@?<v@?@\"CTBootstrapState\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">16"
+ "v24@?0@\"CTBootstrapState\"8@\"NSError\"16"
+ "v24@?0@\"CTDeviceIdentifier\"8@\"NSError\"16"
+ "v24@?0@\"CTPrivateNetworkCapabilities\"8@\"NSError\"16"
+ "v32@0:8@\"CTPlan\"16@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@?<v@?@\"CTPrivateNetworkCapabilities\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"CTXPCServiceSubscriptionContext\"i@\"NSString\"@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSError\"24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
+ "v40@0:8@\"CTPlan\"16@\"NSString\"24@?<v@?Q@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v40@0:8Q16@\"NSString\"24@?<v@?@\"CTDeviceIdentifier\"@\"NSError\">32"
+ "v80@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48@\"NSString\"56@\"NSString\"64@?<v@?B@\"NSError\">72"
+ "v80@0:8@16@24@32@40@48@56@64@?72"
- "0"
- "11305.1"
- "11305.1~1"
- "kCTCapabilityNetworkSlicingManaged"

```
