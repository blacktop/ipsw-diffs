## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 333.0.3.0.0
-  __TEXT.__text: 0x3ed9dc
+  __TEXT.__text: 0x3ed984
   __TEXT.__auth_stubs: 0x11280
   __TEXT.__objc_stubs: 0x9920
   __TEXT.__init_offsets: 0xa4

   __TEXT.__objc_classname: 0x5f4
   __TEXT.__cstring: 0x3323e
   __TEXT.__const: 0x9488
-  __TEXT.__gcc_except_tab: 0x2b7b8
+  __TEXT.__gcc_except_tab: 0x2b830
   __TEXT.__objc_methname: 0xebe5
   __TEXT.__oslogstring: 0x22d1f
-  __TEXT.__objc_methtype: 0x3c29
-  __TEXT.__unwind_info: 0x7af0
+  __TEXT.__objc_methtype: 0x3ccd
+  __TEXT.__unwind_info: 0x7b10
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x8958
   __DATA_CONST.__got: 0x930

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8CE770A-E99A-33D0-88A7-561D0A1D052B
-  Functions: 17133
-  Symbols:   89243
+  UUID: 71BCC9E6-955D-3CCC-8FAE-D84B019D40DD
+  Functions: 17130
+  Symbols:   89235
   CStrings:  13483
 
Symbols:
+ __ZNSt3__114__split_bufferIN4otbr4Mdns9Publisher8TxtEntryERNS_9allocatorIS4_EEE17__destruct_at_endB8ne200100EPS4_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN4otbr4Mdns9Publisher8TxtEntryEEEE7destroyB8ne200100IS5_Li0EEEvRS6_PT_
+ __ZNSt3__16vectorI18otEnergyScanResultNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE22__base_destruct_at_endB8ne200100EPS4_
+ __ZNSt3__16vectorIP15_DNSRecordRef_tNS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIP16_DNSServiceRef_tNS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
- _ZN4otbr4Mdns15PublisherMDnsSd15PublishHostImplERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_6vectorINS_10Ip6AddressENS6_ISC_EEEEONS_12OnceCallbackIFv9otbrErrorEEE.cold.2
- _ZN4otbr5agent12ThreadHelper10EnergyScanEjNSt3__18functionIFv7otErrorRKNS2_6vectorI18otEnergyScanResultNS2_9allocatorIS6_EEEEEEE.cold.1
- __ZN4otbr5agent12ThreadHelperD2Ev
- __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIhNS5_IhEEEEEELi0EEEvPT_
- __ZNSt3__114__split_bufferIN4otbr4Mdns9Publisher8TxtEntryERNS_9allocatorIS4_EEE5clearB8ne200100Ev
- __ZNSt3__16vectorI18otEnergyScanResultNS_9allocatorIS1_EEED1B8ne200100Ev
- __ZNSt3__16vectorIN4otbr10Ip6AddressENS_9allocatorIS2_EEED1B8ne200100Ev
- __ZNSt3__16vectorIP16_DNSServiceRef_tNS_9allocatorIS2_EEED1B8ne200100Ev
- __ZNSt3__19allocatorIN4otbr4Mdns9Publisher8TxtEntryEE7destroyB8ne200100EPS4_
Functions:
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2B8ne200100ESt16initializer_listIS6_E : 312 -> 320
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIjNS5_IjEEEEEENS_22__unordered_map_hasherIS7_SB_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SB_SG_SE_Lb1EEENS5_ISB_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSQ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEEbEERKT_DpOT0_ : 1076 -> 1084
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE30__emplace_hint_unique_key_argsIS7_JRKNS_4pairIKS7_S7_EEEEENSG_INS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEENS_21__tree_const_iteratorIS8_SP_lEERKT_DpOT0_ : 344 -> 336
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN5boost3anyEEENS_19__map_value_compareIS7_SA_NS_4lessIS7_EELb1EEENS5_ISA_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSL_IJEEEEEENS_4pairINS_15__tree_iteratorISA_PNS_11__tree_nodeISA_PvEElEEbEERKT_DpOT0_ : 444 -> 452
~ __ZNSt3__16__treeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4lessIS6_EENS4_IS6_EEE30__emplace_hint_unique_key_argsIS6_JRKS6_EEENS_4pairINS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEENS_21__tree_const_iteratorIS6_SJ_lEERKT_DpOT0_ : 268 -> 260
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI14InternalClientEEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSM_IJEEEEEENS_4pairINS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEEbEERKT_DpOT0_ : 444 -> 452
~ __ZNSt3__16__treeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4lessIS6_EENS4_IS6_EEE25__emplace_unique_key_argsIS6_JRKS6_EEENS_4pairINS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_ : 436 -> 444
~ __ZNKSt3__120__shared_ptr_pointerIPN6CtrXPC17ServerClientState5StateENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNSt3__16__treeINS_12__value_typeINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEP8os_log_sEENS_19__map_value_compareIS9_SC_NS_4lessIS9_EELb1EEENS6_ISC_EEE25__emplace_unique_key_argsIS9_JRKNS_21piecewise_construct_tENS_5tupleIJRKS9_EEENSN_IJEEEEEENS2_INS_15__tree_iteratorISC_PNS_11__tree_nodeISC_PvEElEEbEERKT_DpOT0_ : 412 -> 420
~ __ZNKSt3__120__shared_ptr_pointerIPN6CtrXPC6Server5StateENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvN6CtrXPC17ServerClientStateEN3xpc4dictENS9_IU13block_pointerFvhSD_EEEEEEEENS_19__map_value_compareIS7_SK_NS_4lessIS7_EELb1EEENS5_ISK_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSV_IJEEEEEENS_4pairINS_15__tree_iteratorISK_PNS_11__tree_nodeISK_PvEElEEbEERKT_DpOT0_ : 444 -> 452
~ __ZNKSt3__120__shared_ptr_pointerIPN6CtrXPC6ServerENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIP14InternalClientNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNKSt3__120__shared_ptr_pointerIPNS_3mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvN5boost3anyEEEENS_4lessIS7_EENS5_INS_4pairIKS7_SE_EEEEEENS_10shared_ptrISL_E27__shared_ptr_default_deleteISL_SL_EENS5_ISL_EEE13__get_deleterERKSt9type_info : 108 -> 124
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvN5boost3anyEEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSQ_IJEEEEEENS_4pairINS_15__tree_iteratorISF_PNS_11__tree_nodeISF_PvEElEEbEERKT_DpOT0_ : 444 -> 452
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEtEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSJ_IJEEEEEENS_4pairINS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_ : 444 -> 452
~ __ZNSt3__16vectorI12ServiceEntryNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 472 -> 476
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN5boost3anyEEENS_19__map_value_compareIS7_SA_NS_4lessIS7_EELb1EEENS5_ISA_EEE25__emplace_unique_key_argsIS7_JNS_4pairIS7_S9_EEEEENSI_INS_15__tree_iteratorISA_PNS_11__tree_nodeISA_PvEElEEbEERKT_DpOT0_ : 184 -> 196
~ __ZNSt3__16vectorI13MyServiceTypeNS_9allocatorIS1_EEE7reserveEm : 216 -> 232
~ __ZNSt3__16vectorI13MyServiceTypeNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 304 -> 308
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE13MyServiceTypeEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEERKT_ : 252 -> 256
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE13MyServiceTypeEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSO_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEEbEERKT_DpOT0_ : 632 -> 636
+ __ZNSt3__15dequeIyNS_9allocatorIyEEE7__allocB8dn200100Ev
- __ZNSt3__15dequeIyNS_9allocatorIyEEE6__sizeB8dn200100Ev
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEED2Ev : 108 -> 116
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEE17__destruct_at_endB8dn200100EPS1_NS_17integral_constantIbLb0EEE : 108 -> 116
~ __ZNSt3__16__treeINS_12__value_typeIyN2ot13appPacketInfoEEENS_19__map_value_compareIyS4_NS_4lessIyEELb1EEENS_9allocatorIS4_EEEC2ERKS8_ : 104 -> 108
+ __ZNSt3__16__treeINS_12__value_typeIyN2ot13appPacketInfoEEENS_19__map_value_compareIyS4_NS_4lessIyEELb1EEENS_9allocatorIS4_EEE12__node_allocB8dn200100Ev
~ __ZNSt3__15dequeIyNS_9allocatorIyEEEC2B8dn200100Ev : 84 -> 88
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEEC2B8dn200100Ev : 64 -> 68
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyN2ot13appPacketInfoEEEPvEENS_22__tree_node_destructorINS_9allocatorIS7_EEEEE11get_deleterB8dn200100Ev
~ __ZNSt3__15dequeIyNS_9allocatorIyEEE19__add_back_capacityEv : 736 -> 740
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEE12emplace_backIJRS1_EEEvDpOT_ : 484 -> 496
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEE12emplace_backIJS1_EEEvDpOT_ : 484 -> 496
~ __ZNSt3__114__split_bufferIPyNS_9allocatorIS1_EEE13emplace_frontIJS1_EEEvDpOT_ : 472 -> 484
~ __ZN4otbr3Ncp7RcpHost4InitEv : 288 -> 264
~ __ZNSt3__110unique_ptrIN4otbr5agent12ThreadHelperENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_ : 76 -> 196
- __ZN4otbr5agent12ThreadHelperD2Ev
+ __ZNSt3__16vectorI18otEnergyScanResultNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
~ __ZNSt3__16vectorINS_8functionIFvvEEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 276 -> 280
~ __ZNSt3__16vectorINS_8functionIFvyEEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 276 -> 280
~ __ZN4otbr4Mdns15PublisherMDnsSdC2ENSt3__18functionIFvNS0_9Publisher5StateEEEE : 452 -> 460
- __ZNSt3__16vectorIP16_DNSServiceRef_tNS_9allocatorIS2_EEED1B8ne200100Ev
~ __ZN4otbr4Mdns15PublisherMDnsSdD2Ev : 228 -> 212
~ __ZN4otbr4Mdns15PublisherMDnsSd15PublishHostImplERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_6vectorINS_10Ip6AddressENS6_ISC_EEEEONS_12OnceCallbackIFv9otbrErrorEEE : 592 -> 572
~ __ZN4otbr4Mdns15PublisherMDnsSd25ServiceInstanceResolution23HandleQueryrecordResultEP16_DNSServiceRef_tjjiPKctttPKvj : 460 -> 448
~ __ZN4otbr4Mdns9Publisher22DiscoveredInstanceInfoD1Ev : 116 -> 108
~ __ZN4otbr4Mdns15PublisherMDnsSd25ServiceInstanceResolution16FinishResolutionEv : 488 -> 468
~ __ZN4otbr4Mdns15PublisherMDnsSd16HostSubscription19HandleResolveResultEP16_DNSServiceRef_tjjiPKcPK8sockaddrj : 776 -> 760
~ __ZN4otbr4Mdns9Publisher16HostRegistrationC2ENSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS3_6vectorINS_10Ip6AddressENS7_ISB_EEEEONS_12OnceCallbackIFv9otbrErrorEEEPS1_ : 312 -> 280
~ __ZN4otbr4Mdns9Publisher16HostRegistrationD2Ev : 140 -> 120
~ __ZN4otbr4Mdns15PublisherMDnsSd21DnssdHostRegistrationD2Ev : 144 -> 128
~ __ZN4otbr4Mdns9Publisher22DiscoveredInstanceInfoC2ERKS2_ : 288 -> 300
~ __ZN4otbr4Mdns9Publisher18DiscoveredHostInfoD2Ev : 84 -> 76
- __ZNSt3__16vectorIN4otbr10Ip6AddressENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em : 68 -> 72
~ __ZNSt3__16vectorIN4otbr10Ip6AddressENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__110unique_ptrIN4otbr4Mdns15PublisherMDnsSd16HostSubscriptionENS_14default_deleteIS4_EEE5resetB8ne200100EPS4_ : 164 -> 132
~ __ZN4otbr4Mdns15PublisherMDnsSd25ServiceInstanceResolutionD2Ev : 176 -> 168
~ __ZN4otbr4Mdns9Publisher13DecodeTxtDataERNSt3__16vectorINS1_8TxtEntryENS2_9allocatorIS4_EEEEPKht : 444 -> 412
~ __ZN4otbr4Mdns9Publisher16OnServiceRemovedEjNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_ : 504 -> 480
+ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE22__base_destruct_at_endB8ne200100EPS4_
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJPKciEEEPS4_DpOT_ : 360 -> 372
~ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN4otbr4Mdns9Publisher8TxtEntryEEEPS5_EEvRT_T0_SA_SA_ : 224 -> 248
~ __ZNSt3__114__split_bufferIN4otbr4Mdns9Publisher8TxtEntryERNS_9allocatorIS4_EEED2Ev : 112 -> 116
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJPKciPKhiEEEPS4_DpOT_ : 368 -> 380
~ __ZN4otbr10TaskRunner8PushTaskENSt3__16chrono8durationIxNS1_5ratioILl1ELl1000EEEEENS1_8functionIFvvEEE : 448 -> 452
~ __ZNSt3__16vectorIN4otbr10TaskRunner11DelayedTaskENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRyRNS_6chrono8durationIxNS_5ratioILl1ELl1000EEEEENS_8functionIFvvEEEEEEPS3_DpOT_ : 348 -> 352
~ __ZN4otbr5agent12ThreadHelperC2EP10otInstancePNS_3Ncp7RcpHostE : 304 -> 312
~ __ZN4otbr5agent12ThreadHelper10EnergyScanEjNSt3__18functionIFv7otErrorRKNS2_6vectorI18otEnergyScanResultNS2_9allocatorIS6_EEEEEEE : 264 -> 244
~ __ZN4otbr5agent12ThreadHelper17ActiveScanHandlerEP18otActiveScanResult : 388 -> 392
~ __ZN4otbr5agent12ThreadHelper18EnergyScanCallbackEP18otEnergyScanResult : 284 -> 288
~ __ZNSt3__16vectorINS_8functionIFv12otDeviceRoleEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRS4_EEEPS4_DpOT_ : 280 -> 284
~ __ZNSt3__16vectorINS_8functionIFvRK24otOperationalDatasetTlvsEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_ : 276 -> 280
~ __ZN4otbr19AppendBbrTxtEntriesER10otInstanceNS_11StateBitmapERNSt3__16vectorINS_4Mdns9Publisher8TxtEntryENS3_9allocatorIS7_EEEE : 372 -> 380
~ __ZN4otbr29AppendActiveTimestampTxtEntryER10otInstanceRNSt3__16vectorINS_4Mdns9Publisher8TxtEntryENS2_9allocatorIS6_EEEE : 268 -> 272
~ __ZN4otbr11BorderAgent21PublishMeshCopServiceEv : 1988 -> 1992
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIhNS5_IhEEEEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE : 92 -> 116
- __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIhNS5_IhEEEEEELi0EEEvPT_
~ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_6vectorIhNS1_IhEEEEEEPvEEEEEclB8ne200100EPSE_ : 88 -> 116
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRA3_KcPhmEEEPS4_DpOT_ : 364 -> 368
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRA3_KcPS9_EEEPS4_DpOT_ : 344 -> 356
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJPKcPKhmEEEPS4_DpOT_ : 364 -> 368
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev : 192 -> 144
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRA3_KcRA8_KhmEEEPS4_DpOT_ : 364 -> 368
~ __ZNSt3__16vectorIN4otbr4Mdns9Publisher8TxtEntryENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRA3_KcRA2_S9_EEEPS4_DpOT_ : 344 -> 356
~ _setupBorderAgent : 668 -> 648
~ _ZN5boost10filesystem6detail8relativeERKNS0_4pathES4_PNS_6system10error_codeE.cold.1 : 44 -> 36
- _ZN4otbr4Mdns15PublisherMDnsSd15PublishHostImplERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_6vectorINS_10Ip6AddressENS6_ISC_EEEEONS_12OnceCallbackIFv9otbrErrorEEE.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1093: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1977: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1984: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1993: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2011: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2020: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/4~CBTOugBma-z51pcuF__6vY3FOXVs-FcGNDjW7Jw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2025: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16"
+ "v48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16r^{any=^{placeholder}}40"
+ "v56@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@?40{queue={object=@}}48"
+ "v64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40"
+ "v68@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40i64"
+ "v88@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}64"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}120@0:8{Ctr_form=*BSBIBSBQB[16C]BIB*B[8C]B[8C]B}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16@0:8"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}20@0:8B16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}24@0:8^v16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}24@0:8^{any=^{placeholder}}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}24@0:8^{dict={object=@}}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}24@0:8{Ctr_wed_start=*}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}32@0:8^{Ctr_generatePSKc=*@*Q}16^v24"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}32@0:8^{dict={object=@}}16r*24"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}40@0:8^{dict={object=@}}16r*24^@32"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}40@0:8r*16*24Q32"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}40@0:8{Ctr_homeThreadInfo=iiiiii}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}40@0:8{Ctr_primaryResidentInfo=BB*@}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}40@0:8{Ctr_scan=qIBBSi}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}48@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}SB}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16^{any=^{placeholder}}40"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16r*40"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}52@0:8{?=[16C][16C]SS}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}56@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}Q}16^{any=^{placeholder}}48"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}56@0:8{Ctr_generatePSKc=*@*Q}16^{any=^{placeholder}}48"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}64@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}[16C]S}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}72@0:8{Ctr_join=**SSQ[16C]BBBB}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}88@0:8{Ctr_joiner=********B}16"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8r*16"
+ "{dict={object=@}}48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{dict={object=@}}40"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1083: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1967: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1974: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1983: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2001: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2010: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/4~CATGugCfGfWo6vSeXUhQoaogegqAS87NBqMbGgI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2015: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16"
- "v48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16r^{any=^{placeholder}}40"
- "v56@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@?40{queue={object=@}}48"
- "v64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}40"
- "v68@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}40i64"
- "v88@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}40{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}64"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}120@0:8{Ctr_form=*BSBIBSBQB[16C]BIB*B[8C]B[8C]B}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}20@0:8B16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8^v16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8^{any=^{placeholder}}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8^{dict={object=@}}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8{Ctr_wed_start=*}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}32@0:8^{Ctr_generatePSKc=*@*Q}16^v24"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}32@0:8^{dict={object=@}}16r*24"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40@0:8^{dict={object=@}}16r*24^@32"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40@0:8r*16*24Q32"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40@0:8{Ctr_homeThreadInfo=iiiiii}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40@0:8{Ctr_primaryResidentInfo=BB*@}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40@0:8{Ctr_scan=qIBBSi}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}48@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}SB}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16^{any=^{placeholder}}40"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16r*40"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}52@0:8{?=[16C][16C]SS}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}56@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}Q}16^{any=^{placeholder}}48"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}56@0:8{Ctr_generatePSKc=*@*Q}16^{any=^{placeholder}}48"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}64@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}[16C]S}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}72@0:8{Ctr_join=**SSQ[16C]BBBB}16"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}88@0:8{Ctr_joiner=********B}16"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@0:8r*16"
- "{dict={object=@}}48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16{dict={object=@}}40"

```
