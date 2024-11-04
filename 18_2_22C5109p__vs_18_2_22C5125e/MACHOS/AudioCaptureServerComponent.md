## AudioCaptureServerComponent

> `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioCaptureServerComponent.framework/AudioCaptureServerComponent`

```diff

-139.0.0.0.0
-  __TEXT.__text: 0x207cc
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__const: 0xc90
-  __TEXT.__gcc_except_tab: 0x10d4
-  __TEXT.__cstring: 0x4e3c
-  __TEXT.__oslogstring: 0x1437
-  __TEXT.__unwind_info: 0xd10
-  __DATA.__auth_got: 0x398
+140.0.0.0.0
+  __TEXT.__text: 0x2404c
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0xdd0
+  __TEXT.__gcc_except_tab: 0x1220
+  __TEXT.__cstring: 0x5185
+  __TEXT.__oslogstring: 0x1667
+  __TEXT.__unwind_info: 0xde8
+  __DATA.__auth_got: 0x3a0
   __DATA.__got: 0x90
-  __DATA.__const: 0x1ab0
-  __DATA.__data: 0x1e0
+  __DATA.__const: 0x1d98
+  __DATA.__data: 0x1f8
   __DATA.__ENDPOINTS: 0x107
   __DATA.__TIGHTBEAM: 0x28
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x160
   __DATA.__common: 0x8
   - /System/ExclaveKit/System/Library/Frameworks/SharedMemory.framework/SharedMemory
   - /System/ExclaveKit/System/Library/PrivateFrameworks/DebugExfiltration.framework/DebugExfiltration
   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
-  Functions: 694
-  Symbols:   1327
-  CStrings:  325
+  Functions: 758
+  Symbols:   1440
+  CStrings:  349
 
Symbols:
+ GCC_except_table28
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table86
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table93
+ _ZN3acs25ExclaveKitQueryClientImpl4ImplC2ENSt3__110shared_ptrINS_11ExfiltratorEEENS3_INS_10SerializerEEENS3_INS_16QueryIDGeneratorEEE.cold.1
+ _ZN3acs25ExclaveKitQueryClientImplC2ENSt3__110shared_ptrINS_11ExfiltratorEEENS2_INS_10SerializerEEE.cold.1
+ _ZNSt3__112construct_atB8fe180100IN3acs20ExclaveKitClientImplEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS3_INS1_14SerializerImplEEENS3_IN3shm12SharedMemoryEEENS3_INS1_17RealtimeShuntImplEEEEPS2_EEPT_SI_DpOT0_.cold.1
+ __Block_byref_object_copy_.24
+ __Block_byref_object_dispose_.25
+ __ZN12_GLOBAL__N_120QueryIDGeneratorImpl24FetchNextQueryIdentifierEv
+ __ZN12_GLOBAL__N_120QueryIDGeneratorImplD0Ev
+ __ZN12_GLOBAL__N_120QueryIDGeneratorImplD1Ev
+ __ZN3acs14ControllerImpl15QueryPreferenceEN2ad16basic_string_refIcNSt3__111char_traitsIcEEEES6_
+ __ZN3acs14ControllerImpl23QueryPreferenceCompleteEyNS_6StatusENSt3__18optionalIiEE
+ __ZN3acs25ExclaveKitQueryClientImpl15QueryPreferenceEN2ad16basic_string_refIcNSt3__111char_traitsIcEEEES6_
+ __ZN3acs25ExclaveKitQueryClientImpl23QueryPreferenceCompleteEyNS_6StatusENSt3__18optionalIiEE
+ __ZN3acs25ExclaveKitQueryClientImpl4ImplC2ENSt3__110shared_ptrINS_11ExfiltratorEEENS3_INS_10SerializerEEENS3_INS_16QueryIDGeneratorEEE
+ __ZN3acs25ExclaveKitQueryClientImpl4ImplD2Ev
+ __ZN3acs25ExclaveKitQueryClientImplC1ENSt3__110shared_ptrINS_11ExfiltratorEEENS2_INS_10SerializerEEE
+ __ZN3acs25ExclaveKitQueryClientImplC2ENSt3__110shared_ptrINS_11ExfiltratorEEENS2_INS_10SerializerEEE
+ __ZN3acs25ExclaveKitQueryClientImplD0Ev
+ __ZN3acs25ExclaveKitQueryClientImplD1Ev
+ __ZN3acs7Liaison15QueryPreferenceE6u8_v_sS1_P61audiocaptureserver_exclavekitclient_querypreference__result_s
+ __ZN3acs7Liaison23QueryPreferenceCompleteEy37audiocaptureserver_connectionstatus_sPK10s32__opt_sP68audiocaptureserver_userspaceclient_querypreferencecomplete__result_s
+ __ZNK3acs14SerializerImpl9SerializeEN3sec19ExfiltrationCommandEyRKN2ad16basic_string_refIcNSt3__111char_traitsIcEEEESA_
+ __ZNK3sec22SerializationProxyImpl30querypreferencemessage_marshalEPK43serializationtypes_querypreferencemessage_sPhm
+ __ZNK3sec22SerializationProxyImpl32querypreferencemessage_unmarshalEPhmNSt3__18functionIFv43serializationtypes_querypreferencemessage_sEEE
+ __ZNK3sec22SerializationProxyImpl37querypreferencemessage_marshal_sizeofEPK43serializationtypes_querypreferencemessage_s
+ __ZNKRSt3__18expectedINS_8optionalIiEEN3acs5ErrorEE5valueB8fe180100Ev
+ __ZNKSt3__13mapIyNS_7variantIJN12_GLOBAL__N_121QueryStageExfiltratedENS2_30QueryStageResolvedSuccessfullyENS2_32QueryStageResolvedUnsuccessfullyEEEENS_4lessIyEENS_9allocatorINS_4pairIKyS6_EEEEE2atERSB_
+ __ZNSt3__110__function12__value_funcIFv43serializationtypes_querypreferencemessage_sEEC2B8fe180100ERKS4_
+ __ZNSt3__110__function12__value_funcIFv43serializationtypes_querypreferencemessage_sEED2B8fe180100Ev
+ __ZNSt3__110unique_ptrIN3acs25ExclaveKitQueryClientImpl4ImplENS_14default_deleteIS3_EEE5resetB8fe180100EPS3_
+ __ZNSt3__112construct_atB8fe180100IN3acs20ExclaveKitClientImplEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS3_INS1_14SerializerImplEEENS3_IN3shm12SharedMemoryEEENS3_INS1_17RealtimeShuntImplEEEEPS2_EEPT_SI_DpOT0_
+ __ZNSt3__112construct_atB8fe180100IN3acs25ExclaveKitQueryClientImplEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS3_INS1_14SerializerImplEEEEPS2_EEPT_SD_DpOT0_
+ __ZNSt3__115allocate_sharedB8fe180100IN3acs20ExclaveKitClientImplENS_9allocatorIS2_EEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS5_INS1_14SerializerImplEEENS5_IN3shm12SharedMemoryEEENS5_INS1_17RealtimeShuntImplEEEEvEENS5_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8fe180100IN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS5_INS1_14SerializerImplEEEEvEENS5_IT_EERKT0_DpOT1_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZN3acs25ExclaveKitQueryClientImpl15QueryPreferenceEN2ad16basic_string_refIcNS_11char_traitsIcEEEESF_E3$_1ZNSA_15QueryPreferenceESF_SF_E3$_2ZNSA_15QueryPreferenceESF_SF_E3$_3EEEEJRKNS0_6__baseILNS0_6_TraitE0EJN12_GLOBAL__N_121QueryStageExfiltratedENSO_30QueryStageResolvedSuccessfullyENSO_32QueryStageResolvedUnsuccessfullyEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZN3acs25ExclaveKitQueryClientImpl15QueryPreferenceEN2ad16basic_string_refIcNS_11char_traitsIcEEEESF_E3$_1ZNSA_15QueryPreferenceESF_SF_E3$_2ZNSA_15QueryPreferenceESF_SF_E3$_3EEEEJRKNS0_6__baseILNS0_6_TraitE0EJN12_GLOBAL__N_121QueryStageExfiltratedENSO_30QueryStageResolvedSuccessfullyENSO_32QueryStageResolvedUnsuccessfullyEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZN3acs25ExclaveKitQueryClientImpl15QueryPreferenceEN2ad16basic_string_refIcNS_11char_traitsIcEEEESF_E3$_1ZNSA_15QueryPreferenceESF_SF_E3$_2ZNSA_15QueryPreferenceESF_SF_E3$_3EEEEJRKNS0_6__baseILNS0_6_TraitE0EJN12_GLOBAL__N_121QueryStageExfiltratedENSO_30QueryStageResolvedSuccessfullyENSO_32QueryStageResolvedUnsuccessfullyEEEEEEEDcT_DpT0_
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN3acs20ExclaveKitClientImplENS_9allocatorIS2_EEEC2B8fe180100IJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS7_INS1_14SerializerImplEEENS7_IN3shm12SharedMemoryEEENS7_INS1_17RealtimeShuntImplEEEES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEEC2B8fe180100IJRKNS_10shared_ptrINS1_15ExfiltratorImplEEERNS7_INS1_14SerializerImplEEEES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__13mapIyNS_7variantIJN12_GLOBAL__N_121QueryStageExfiltratedENS2_30QueryStageResolvedSuccessfullyENS2_32QueryStageResolvedUnsuccessfullyEEEENS_4lessIyEENS_9allocatorINS_4pairIKyS6_EEEEE2atERSB_
+ __ZNSt3__16__treeINS_12__value_typeIyNS_7variantIJN12_GLOBAL__N_121QueryStageExfiltratedENS3_30QueryStageResolvedSuccessfullyENS3_32QueryStageResolvedUnsuccessfullyEEEEEENS_19__map_value_compareIyS8_NS_4lessIyEELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__19to_stringEi
+ __ZTIN12_GLOBAL__N_120QueryIDGeneratorImplE
+ __ZTIN3acs16QueryIDGeneratorE
+ __ZTIN3acs16QueryMaintenanceE
+ __ZTIN3acs21ExclaveKitQueryClientE
+ __ZTIN3acs25ExclaveKitQueryClientImplE
+ __ZTINSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEEE
+ __ZTINSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEEE
+ __ZTSN12_GLOBAL__N_120QueryIDGeneratorImplE
+ __ZTSN3acs16QueryIDGeneratorE
+ __ZTSN3acs16QueryMaintenanceE
+ __ZTSN3acs21ExclaveKitQueryClientE
+ __ZTSN3acs25ExclaveKitQueryClientImplE
+ __ZTSNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEEE
+ __ZTVN12_GLOBAL__N_120QueryIDGeneratorImplE
+ __ZTVN3acs25ExclaveKitQueryClientImplE
+ __ZTVNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120QueryIDGeneratorImplENS_9allocatorIS2_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN3acs25ExclaveKitQueryClientImplENS_9allocatorIS2_EEEE
+ __ZThn16_N3acs14ControllerImpl15QueryPreferenceEN2ad16basic_string_refIcNSt3__111char_traitsIcEEEES6_
+ __ZThn16_N3acs14ControllerImpl23QueryPreferenceCompleteEyNS_6StatusENSt3__18optionalIiEE
+ __ZThn16_N3acs14ControllerImplD0Ev
+ __ZThn16_N3acs14ControllerImplD1Ev
+ __ZZN12_GLOBAL__N_120QueryIDGeneratorImpl24FetchNextQueryIdentifierEvE15queryIdentifier
+ ___ZN12_GLOBAL__N_113CreateHandlerENSt3__110shared_ptrIN3acs7LiaisonEEE_block_invoke.102
+ ___ZN12_GLOBAL__N_113CreateHandlerENSt3__110shared_ptrIN3acs7LiaisonEEE_block_invoke.106
+ ____ZNK3sec22SerializationProxyImpl32querypreferencemessage_unmarshalEPhmNSt3__18functionIFv43serializationtypes_querypreferencemessage_sEEE_block_invoke
+ ___copy_helper_block_e8_32c71_ZTSNSt3__18functionIFv43serializationtypes_querypreferencemessage_sEEE
+ ___destroy_helper_block_e8_32c71_ZTSNSt3__18functionIFv43serializationtypes_querypreferencemessage_sEEE
+ __block_descriptor_tmp.105
+ __block_descriptor_tmp.110
+ __block_descriptor_tmp.112
+ __block_descriptor_tmp.114
+ __block_descriptor_tmp.125
+ __block_descriptor_tmp.134
+ __block_descriptor_tmp.141
+ __block_descriptor_tmp.148
+ __block_descriptor_tmp.158
+ __block_descriptor_tmp.177
+ __block_descriptor_tmp.187
+ __block_descriptor_tmp.199
+ __block_descriptor_tmp.21
+ __block_descriptor_tmp.212
+ __block_descriptor_tmp.216
+ __block_descriptor_tmp.219
+ __block_descriptor_tmp.223
+ __block_descriptor_tmp.226
+ __block_descriptor_tmp.228
+ __block_descriptor_tmp.229
+ __block_descriptor_tmp.24
+ __block_descriptor_tmp.29
+ __block_descriptor_tmp.33
+ __block_descriptor_tmp.49
+ __block_descriptor_tmp.53
+ __block_descriptor_tmp.55
+ __block_descriptor_tmp.69
+ __block_descriptor_tmp.8
+ __block_descriptor_tmp.82
+ __block_descriptor_tmp.98
+ __captureaudiotypes_audiobuffer__v_encode_block_invoke.220
+ __decodeAudioCaptureServerNode2_block_invoke.101
+ __decodeAudioCaptureServerNode2_block_invoke.101.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.101.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.110
+ __decodeAudioCaptureServerNode2_block_invoke.110.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.110.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.121
+ __decodeAudioCaptureServerNode2_block_invoke.121.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.121.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.130
+ __decodeAudioCaptureServerNode2_block_invoke.130.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.130.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.137
+ __decodeAudioCaptureServerNode2_block_invoke.137.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.137.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.144
+ __decodeAudioCaptureServerNode2_block_invoke.144.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.155
+ __decodeAudioCaptureServerNode2_block_invoke.174
+ __decodeAudioCaptureServerNode2_block_invoke.183
+ __decodeAudioCaptureServerNode2_block_invoke.183.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.183.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.78
+ __decodeAudioCaptureServerNode2_block_invoke.78.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.78.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.87
+ __decodeAudioCaptureServerNode2_block_invoke.87.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.87.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.94
+ __decodeAudioCaptureServerNode2_block_invoke.94.cold.1
+ __decodeAudioCaptureServerNode2_block_invoke.94.cold.2
+ __decodeAudioCaptureServerNode2_block_invoke.cold.2
+ __f32__v_encode_block_invoke.227
+ __u8__v_encode_block_invoke.54
+ _audiocaptureserver_exclavekitclient_querypreference__result_init_failure
+ _audiocaptureserver_exclavekitclient_querypreference__result_init_success
+ _audiocaptureserver_userspaceclient_querypreferencecomplete__result_init_failure
+ _audiocaptureserver_userspaceclient_querypreferencecomplete__result_init_success
+ _serializationtypes_querypreferencemessage__marshal
+ _serializationtypes_querypreferencemessage__marshal_sizeof
+ _serializationtypes_querypreferencemessage__unmarshal
+ decodeAudioCaptureServerNode2.cold.48
+ decodeAudioCaptureServerNode2.cold.49
- GCC_except_table31
- GCC_except_table46
- GCC_except_table54
- GCC_except_table67
- GCC_except_table80
- _ZNSt3__112construct_atB8fe180100IN3acs20ExclaveKitClientImplEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEENS3_INS1_14SerializerImplEEENS3_IN3shm12SharedMemoryEEENS3_INS1_17RealtimeShuntImplEEEEPS2_EEPT_SH_DpOT0_.cold.1
- __Block_byref_object_copy_.23
- __Block_byref_object_dispose_.24
- __ZNSt3__112construct_atB8fe180100IN3acs20ExclaveKitClientImplEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEENS3_INS1_14SerializerImplEEENS3_IN3shm12SharedMemoryEEENS3_INS1_17RealtimeShuntImplEEEEPS2_EEPT_SH_DpOT0_
- __ZNSt3__115allocate_sharedB8fe180100IN3acs20ExclaveKitClientImplENS_9allocatorIS2_EEJRKNS_10shared_ptrINS1_15ExfiltratorImplEEENS5_INS1_14SerializerImplEEENS5_IN3shm12SharedMemoryEEENS5_INS1_17RealtimeShuntImplEEEEvEENS5_IT_EERKT0_DpOT1_
- __ZNSt3__120__shared_ptr_emplaceIN3acs20ExclaveKitClientImplENS_9allocatorIS2_EEEC2B8fe180100IJRKNS_10shared_ptrINS1_15ExfiltratorImplEEENS7_INS1_14SerializerImplEEENS7_IN3shm12SharedMemoryEEENS7_INS1_17RealtimeShuntImplEEEES4_Li0EEES4_DpOT_
- __block_descriptor_tmp.100
- __block_descriptor_tmp.102
- __block_descriptor_tmp.108
- __block_descriptor_tmp.119
- __block_descriptor_tmp.128
- __block_descriptor_tmp.135
- __block_descriptor_tmp.142
- __block_descriptor_tmp.152
- __block_descriptor_tmp.159
- __block_descriptor_tmp.16
- __block_descriptor_tmp.17
- __block_descriptor_tmp.192
- __block_descriptor_tmp.20
- __block_descriptor_tmp.206
- __block_descriptor_tmp.210
- __block_descriptor_tmp.213
- __block_descriptor_tmp.215
- __block_descriptor_tmp.218
- __block_descriptor_tmp.220
- __block_descriptor_tmp.221
- __block_descriptor_tmp.23
- __block_descriptor_tmp.28
- __block_descriptor_tmp.54
- __block_descriptor_tmp.57
- __block_descriptor_tmp.72
- __block_descriptor_tmp.85
- __block_descriptor_tmp.94
- __captureaudiotypes_audiobuffer__v_encode_block_invoke.214
- __decodeAudioCaptureServerNode2_block_invoke.104
- __decodeAudioCaptureServerNode2_block_invoke.104.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.115
- __decodeAudioCaptureServerNode2_block_invoke.115.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.124
- __decodeAudioCaptureServerNode2_block_invoke.124.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.131
- __decodeAudioCaptureServerNode2_block_invoke.131.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.138
- __decodeAudioCaptureServerNode2_block_invoke.138.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.149
- __decodeAudioCaptureServerNode2_block_invoke.156
- __decodeAudioCaptureServerNode2_block_invoke.81
- __decodeAudioCaptureServerNode2_block_invoke.81.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.90
- __decodeAudioCaptureServerNode2_block_invoke.90.cold.1
- __decodeAudioCaptureServerNode2_block_invoke.97
- __decodeAudioCaptureServerNode2_block_invoke.97.cold.1
- __f32__v_encode_block_invoke.219
- __u8__v_encode_block_invoke.55
CStrings:
+ "%!s(MISSING):%!d(MISSING) Begin completion function for query identifier %!l(MISSING)lu"
+ "%!s(MISSING):%!d(MISSING) Incoming Tightbeam call to complete preference query. { queryID=%!l(MISSING)lu, status=%!h(MISSING)hu, prefVal=%!s(MISSING) }"
+ "%!s(MISSING):%!d(MISSING) Maybe wake for query identifier %!l(MISSING)lu"
+ "%!s(MISSING):%!d(MISSING) Query resolved successfully. { id=%!l(MISSING)lu }"
+ "%!s(MISSING):%!d(MISSING) Query resolved unsucessfully. { id=%!l(MISSING)lu }"
+ "%!s(MISSING):%!d(MISSING) Unable to serialize client info for query identifier %!l(MISSING)lu."
+ "%!s(MISSING):%!d(MISSING) Unexpected Exfiltrated query stage received on roundtrip. { id=%!l(MISSING)lu }"
+ "%!s(MISSING):%!d(MISSING) Will%!{(MISSING)public}s wake for query identifier %!l(MISSING)lu."
+ "%!s(MISSING):%!d(MISSING) nextQueryIdentifier: %!l(MISSING)lu"
+ "(component->handler->querypreference != NULL) && \"implementation for queryPreference is not present\""
+ "(component->handler->querypreferencecomplete != NULL) && \"implementation for queryPreferenceComplete is not present\""
+ "(u8__v_decode(query, &preferenceDomain) == TB_ERROR_SUCCESS) && \"failed to decode type: UInt8\""
+ "(u8__v_decode(query, &preferenceKey) == TB_ERROR_SUCCESS) && \"failed to decode type: UInt8\""
+ "I104@?0^{audiocaptureservercomponent_audiocaptureservernode__context_s=^^v^^v}8{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}16{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}56@?<I@?{audiocaptureserver_exclavekitclient_querypreference__result_s=C(?=C{s32__opt_s=Bi})}>96"
+ "I10@?0{audiocaptureserver_userspaceclient_querypreferencecomplete__result_s=C(?=C)}8"
+ "I20@?0{audiocaptureserver_exclavekitclient_querypreference__result_s=C(?=C{s32__opt_s=Bi})}8"
+ "I44@?0^{audiocaptureservercomponent_audiocaptureservernode__context_s=^^v^^v}8Q16C24r^{s32__opt_s=Bi}28@?<I@?{audiocaptureserver_userspaceclient_querypreferencecomplete__result_s=C(?=C)}>36"
+ "POSTCONDITION FAILURE: [mExclaveKitQueryClient] is false"
+ "POSTCONDITION FAILURE: [mSynchronizedState.mQueries.empty()] is false"
+ "PRECONDITION FAILURE: [!domain.empty()] is false"
+ "PRECONDITION FAILURE: [!key.empty()] is false"
+ "PRECONDITION FAILURE: [exfiltrationCommand == sec::ExfiltrationCommand::QueryPreference] is false"
+ "RUNTIME FAILURE: [queryRegistry.contains(queryID)] is false"
+ "RUNTIME FAILURE: [std::holds_alternative<QueryStageExfiltrated>(queryRegistry.at(queryID))] is false"
+ "TB_FATAL: invalid error returned from clientInstanceCreationComplete (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from connectToExfiltrationService (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from exfiltrationServiceConnectionComplete (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getPreferenceState (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from preferenceStateChanged (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from processRealtimeMessages (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from queryPreference (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from queryPreferenceComplete (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from registerDataClient (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from registerPCMAudioClient (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from unregisterClient (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected bits, 0x%!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "acsExclaveKitQueryClient.cpp"
+ "none"
+ "v96@?0{serializationtypes_querypreferencemessage_s=Q{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8"
- "(audiocaptureserver_connectionstatus__decode(query, &status) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioCaptureServer.ConnectionStatus\""
- "(audiocaptureserver_datacreationinfo__decode(message, &val->values.DataInfo.field0) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioCaptureServer.DataCreationInfo\""
- "(audiocaptureserver_datacreationinfo__decode(query, &dataCreationInfo) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioCaptureServer.DataCreationInfo\""
- "(audiocaptureserver_preferencestate__decode(query, &preferenceState) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioCaptureServer.PreferenceState\""
- "(f32__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: Float32\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from clientInstanceCreationComplete\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from connectToExfiltrationService\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from exfiltrationServiceConnectionComplete\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getPreferenceState\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from preferenceStateChanged\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from processRealtimeMessages\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from registerDataClient\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from registerPCMAudioClient\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from unregisterClient\""
- "(u8__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: UInt8\""
- "(xnuupcalls_notificationerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: XnuUpcalls.NotificationError\""

```
