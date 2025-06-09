## libARIServer.dylib

> `/usr/lib/libARIServer.dylib`

```diff

-1257.0.0.0.0
-  __TEXT.__text: 0x155f0
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x1386
-  __TEXT.__gcc_except_tab: 0x14c4
-  __TEXT.__cstring: 0x2e88
-  __TEXT.__unwind_info: 0x9f8
-  __DATA_CONST.__got: 0xa8
+1533.0.0.0.0
+  __TEXT.__text: 0x1f99c
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__init_offsets: 0xc
+  __TEXT.__const: 0x1406
+  __TEXT.__gcc_except_tab: 0x1dd0
+  __TEXT.__cstring: 0x2deb
+  __TEXT.__oslogstring: 0x2234
+  __TEXT.__unwind_info: 0xa58
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x380
-  __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0x10f0
+  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__const: 0x1140
   __AUTH_CONST.__cfstring: 0x20
-  __DATA_DIRTY.__common: 0x8330
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__common: 0x8338
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libARI.dylib

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 47069E83-CCC7-3C84-AFA0-E0BFC45014BA
-  Functions: 467
-  Symbols:   1354
-  CStrings:  321
+  UUID: 1A2A4645-2CCF-3DE2-89E4-9243D8FB98D1
+  Functions: 489
+  Symbols:   1396
+  CStrings:  474
 
Symbols:
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table156
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table180
+ GCC_except_table189
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table232
+ GCC_except_table251
+ GCC_except_table270
+ GCC_except_table288
+ GCC_except_table306
+ GCC_except_table316
+ GCC_except_table32
+ GCC_except_table326
+ GCC_except_table33
+ GCC_except_table335
+ GCC_except_table353
+ GCC_except_table41
+ GCC_except_table71
+ GCC_except_table88
+ _.str.12
+ _AriHostRtInit
+ _AriHostRtShutdown
+ __ZGVN3ctu9SingletonI16AriAdaptiveTimerS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN12capabilities3pci16supportsRxIOPoolEv
+ __ZN16AriAdaptiveTimer10initializeEv
+ __ZN16AriAdaptiveTimer15getTimerServiceEv
+ __ZN16AriAdaptiveTimer21create_default_globalEv
+ __ZN16AriAdaptiveTimerC1Ev
+ __ZN16AriAdaptiveTimerC2Ev
+ __ZN16AriAdaptiveTimerD1Ev
+ __ZN16AriAdaptiveTimerD2Ev
+ __ZN3ctu20AdaptiveTimerService13getScaledTimeENSt3__16chrono8durationIxNS1_5ratioILl1ELl1000000EEEEE
+ __ZN3ctu20AdaptiveTimerService6createEONSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEONS1_6vectorINS1_10shared_ptrINS_20TimerScalingScenarioEEENS5_ISC_EEEE
+ __ZN3ctu20FirstBootAfterUpdate6createEhNSt3__16chrono8durationIxNS1_5ratioILl1ELl1EEEEE
+ __ZN3ctu23PthreadMutexGuardPolicyI16AriAdaptiveTimerED1Ev
+ __ZN3ctu23PthreadMutexGuardPolicyI16AriAdaptiveTimerED2Ev
+ __ZN3ctu9SingletonI16AriAdaptiveTimerS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN6AriOsa10IpcFreeBufEPNS_13IpcDescriptorEPhm
+ __ZN6AriOsa24LogToDefaultStringLoggerEjPKcz
+ __ZN6AriOsa8GetOsLogEv
+ __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne200100Ev
+ __ZNKSt9type_infoeqB8ne200100ERKS_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110__function12__value_funcIFbPvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFiiRNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS6_EEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvN9AriHostRt20ARI_CLIENT_ERROR_EVTENS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEijEEC2B8ne200100ERKSB_
+ __ZNSt3__110__function12__value_funcIFvN9AriHostRt20ARI_CLIENT_ERROR_EVTENS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEijEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN3Ari22AriXpcServerConnectionEEEEEC2B8ne200100ERKS7_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN3Ari22AriXpcServerConnectionEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvRNS_10shared_ptrIN3Ari14AriClientProxyEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFviRNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS6_EEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvijRNS_10shared_ptrIN3Ari14AriClientProxyEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvijRNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS6_EEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvvEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvvEED2B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIiNS_4pairIjNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS8_EEEEEEEEPvEENS_22__hash_node_destructorINS9_ISF_EEEEED1B8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__115allocate_sharedB8ne200100IN9AriHostRt23ClientTransitionTrackerENS_9allocatorIS2_EEJRNS_8functionIFvvEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__throw_bad_weak_ptrB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_10shared_ptrIN3Ari22AriXpcServerConnectionEEEPvEEEEEclB8ne200100EPS8_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIiNS_10shared_ptrIN9AriHostRt13RtTransactionEEEEEPvEEEEEclB8ne200100EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIiNS_4pairIjNS_10shared_ptrIN3Ari14AriClientProxyEEEEEEEPvEEEEEclB8ne200100EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyNS_10shared_ptrIN3Ari14AriClientProxyEEEEEPvEEEEEclB8ne200100EPSA_
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN3ctu20TimerScalingScenarioEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTINSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI16AriAdaptiveTimerNS_9allocatorIS1_EEEE
+ __ZnwmSt19__type_descriptor_t
+ ____ZN3Ari22AriXpcServerConnection19handleClientMessageEPv_block_invoke.74
+ ____ZN9AriHostRt21CancelAllTransactionsEv_block_invoke.110
+ ____ZN9AriHostRt9SetOPModeENS_11ARI_OP_MODEEP16dispatch_group_sj_block_invoke.136
+ ____ZN9AriHostRt9SetOPModeENS_11ARI_OP_MODEEP16dispatch_group_sj_block_invoke.139
+ ____ZN9AriHostRt9SetOPModeENS_11ARI_OP_MODEEP16dispatch_group_sj_block_invoke_2.148
+ ____ZN9AriHostRt9commitLPMEj_block_invoke.126
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.137
+ ___block_descriptor_tmp.14
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.156
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.158
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.40
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.46
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.85
+ ___block_descriptor_tmp.91
+ ___cxx_global_var_init
+ ___cxx_global_var_init.180
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_impl
+ _os_log_type_enabled
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
- GCC_except_table100
- GCC_except_table14
- GCC_except_table15
- GCC_except_table152
- GCC_except_table176
- GCC_except_table18
- GCC_except_table185
- GCC_except_table201
- GCC_except_table203
- GCC_except_table211
- GCC_except_table216
- GCC_except_table218
- GCC_except_table221
- GCC_except_table228
- GCC_except_table24
- GCC_except_table247
- GCC_except_table266
- GCC_except_table284
- GCC_except_table302
- GCC_except_table308
- GCC_except_table322
- GCC_except_table331
- GCC_except_table349
- GCC_except_table60
- GCC_except_table87
- _.str.15
- _.str.16
- _.str.2
- _.str.50
- _.str.57
- _.str.59
- __ZN11AriDispatch5Timer3setEyU13block_pointerFvvE
- __ZN11AriDispatch5Timer6CreateEP16dispatch_queue_s
- __ZN11AriDispatch5Timer6cancelEv
- __ZN12capabilities5radio19ARITransportTimeoutEv
- __ZN3Ari3LogEjPKcz
- __ZN6AriOsa10IpcFreeBufEPhm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne190102IS4_EENS_12basic_stringIcS2_T_EERKS8_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt9type_infoeqB8ne190102ERKS_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110__function12__value_funcIFbPvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFiiRNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS6_EEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvN9AriHostRt20ARI_CLIENT_ERROR_EVTENS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEijEEC2B8ne190102ERKSB_
- __ZNSt3__110__function12__value_funcIFvN9AriHostRt20ARI_CLIENT_ERROR_EVTENS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEijEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN3Ari22AriXpcServerConnectionEEEEEC2B8ne190102ERKS7_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN3Ari22AriXpcServerConnectionEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvRNS_10shared_ptrIN3Ari14AriClientProxyEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFviRNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS6_EEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvijRNS_10shared_ptrIN3Ari14AriClientProxyEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvijRNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS6_EEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvvEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFvvEED2B8ne190102Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIiNS_4pairIjNS_4listINS_10shared_ptrIN3Ari14AriClientProxyEEENS_9allocatorIS8_EEEEEEEEPvEENS_22__hash_node_destructorINS9_ISF_EEEEE5resetB8ne190102EPSF_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__115allocate_sharedB8ne190102IN9AriHostRt23ClientTransitionTrackerENS_9allocatorIS2_EEJRNS_8functionIFvvEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__120__throw_bad_weak_ptrB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_10shared_ptrIN3Ari22AriXpcServerConnectionEEEPvEEEEEclB8ne190102EPS8_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIiNS_10shared_ptrIN9AriHostRt13RtTransactionEEEEEPvEEEEEclB8ne190102EPSA_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIiNS_4pairIjNS_10shared_ptrIN3Ari14AriClientProxyEEEEEEEPvEEEEEclB8ne190102EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyNS_10shared_ptrIN3Ari14AriClientProxyEEEEEPvEEEEEclB8ne190102EPSA_
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB8ne190102Ev
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___FUNCTION__._ZN6AriOsa8IpcWriteEPNS_13IpcDescriptorEPKhmPKNS_10IpcOptionsE
- ___FUNCTION__._ZN9AriHostRt13RegIndicationEjj
- ___FUNCTION__._ZN9AriHostRt17RegAllIndicationsEj
- ___FUNCTION__._ZNK3Ari12AriXpcServer9dumpStateEv
- ____ZN3Ari22AriXpcServerConnection19handleClientMessageEPv_block_invoke.73
- ____ZN9AriHostRt21CancelAllTransactionsEv_block_invoke.108
- ____ZN9AriHostRt9SetOPModeENS_11ARI_OP_MODEEP16dispatch_group_sj_block_invoke_2.144
- ____ZN9AriHostRt9SetOPModeENS_11ARI_OP_MODEEP16dispatch_group_sj_block_invoke_3
- ____ZN9AriHostRt9SetOPModeENS_11ARI_OP_MODEEP16dispatch_group_sj_block_invoke_4
- ____ZN9AriHostRt9commitLPMEj_block_invoke.124
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.13
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.170
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.24
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.38
- ___block_descriptor_tmp.41
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.47
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.55
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.64
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.84
- ___block_descriptor_tmp.87
- _dispatch_time
CStrings:
+ "%s: (%s:%d) #%03d Client(%s-%d) ts(%u)"
+ "%s: (%s:%d) %s"
+ "%s: (%s:%d) %zu registered clients on connection %s"
+ "%s: (%s:%d) ** FAILED TO INIT ARI FRAMER / TRANSPORT **"
+ "%s: (%s:%d) ACK received for AriHostRt internal message(%d-0x%03X) with status(%s(%d))"
+ "%s: (%s:%d) All transitions are complete.  Executing post-transition action"
+ "%s: (%s:%d) AriHostRt in state(%s) unsuitable for DeregisterClient on cid %u"
+ "%s: (%s:%d) AriHostRt in state(%s) unsuitable for InboundMsgCB"
+ "%s: (%s:%d) AriHostRt in state(%s) unsuitable for RegisterSniffer"
+ "%s: (%s:%d) AriHostRt in state(%s) unsuitable for sendRawInternal(%s)"
+ "%s: (%s:%d) AriHostRt msgTimeoutMultiplier: prev(%d) new(%d)"
+ "%s: (%s:%d) Associated cids: %s"
+ "%s: (%s:%d) Attempt to de-reg an non-existant CID(%x)"
+ "%s: (%s:%d) Attempt to de-register cid 0x%x"
+ "%s: (%s:%d) BOTTOM newDataSizeRemains(%zu) newDataSizeConsumed(%zu) cachedSize(%zu)"
+ "%s: (%s:%d) Cache unfinished message @ index(%zu) and sz(%zu)"
+ "%s: (%s:%d) Canceling transaction 0x%04x gmid 0x%x reason(%s)"
+ "%s: (%s:%d) Client ID: 0x%x ( %s )"
+ "%s: (%s:%d) Client Resources:"
+ "%s: (%s:%d) Committing LPM to BB before AP sleep"
+ "%s: (%s:%d) Completed %s LPM"
+ "%s: (%s:%d) Connection error: %s"
+ "%s: (%s:%d) Could not send AriMsgAttribReq %s %s on msg(%d-0x%03x) val(0x%x-%s)..."
+ "%s: (%s:%d) Could not send boot state request"
+ "%s: (%s:%d) Data is NULL, but IpcRead also fails for size (%zu)"
+ "%s: (%s:%d) Deregistered cid 0x%x"
+ "%s: (%s:%d) Dispatched supervisory Started callback"
+ "%s: (%s:%d) Done"
+ "%s: (%s:%d) Entitlement check failed for client; ignoring xpc command 0x%x"
+ "%s: (%s:%d) Entitlement check; Client: %s Entitled: %s"
+ "%s: (%s:%d) Error getting expected internal message AriMsgAttribResp"
+ "%s: (%s:%d) Error handling indication for CID 0x%x registered for gmid(%d-0x%x)"
+ "%s: (%s:%d) Error registering ARI client %s"
+ "%s: (%s:%d) Fail to complete the transaction(%s), cancelling"
+ "%s: (%s:%d) Failed to deregister cid 0x%x"
+ "%s: (%s:%d) Failed to register indications"
+ "%s: (%s:%d) Failed to send AriGrpMsgsAttribReq"
+ "%s: (%s:%d) Failed to send the sensitive logging info"
+ "%s: (%s:%d) Failed write to framer with (%s) AP.SEQ(%d) not advanced"
+ "%s: (%s:%d) GetBufCtx Invalid CTX"
+ "%s: (%s:%d) Got message @ index(%zu) and sz(%zu)"
+ "%s: (%s:%d) Host RT framer success"
+ "%s: (%s:%d) Host RT invalid msgTimeoutMultiplier param: must be > 0"
+ "%s: (%s:%d) Host RT msgTimeoutMultiplier: (%d)"
+ "%s: (%s:%d) Host RT state init success"
+ "%s: (%s:%d) IPC write failure on buffer(%p) sz(%zu)"
+ "%s: (%s:%d) Illegal message len(%zu), resetting cachedSize(%zu)"
+ "%s: (%s:%d) Inbound Msg sz%zu ctx(0x%08X) for sniffer (%s) "
+ "%s: (%s:%d) Indication ID: (%d-0x%x), Client ID or Actor ID: 0x%x ( %s )"
+ "%s: (%s:%d) Indication Resources:"
+ "%s: (%s:%d) Indication(0x%08x) for client(%s) Type(GCD) size(%zu) dispq(%s:%p)"
+ "%s: (%s:%d) Indication(0x%08x) for client(%s) Type(XPC) size(%zu) conn(%s)"
+ "%s: (%s:%d) Init complete"
+ "%s: (%s:%d) Invalid msgTimeoutMultiplier param: must be > 0"
+ "%s: (%s:%d) Missing expected BB.SEQ(0x%03x), got BB.SEQ(0x%03x)"
+ "%s: (%s:%d) Msg for client(%s) Type(%s) cid(0x%x) size(%zu) ctx(0x%08x)"
+ "%s: (%s:%d) Msg for client(%s) Type(GCD) size(%zu) %s ctx(0x%08X)"
+ "%s: (%s:%d) NACK received for AriHostRt internal message(%d-0x%03X) likely due to pending shutdown (%s(%d))"
+ "%s: (%s:%d) NACK received for AriHostRt internal message(%d-0x%03X) with status(%s(%d))"
+ "%s: (%s:%d) NOT waiting for trx(%s) due to long timeout of %llums"
+ "%s: (%s:%d) New xpc connection: %s"
+ "%s: (%s:%d) No handler is registered for indication gmid(%d-0x%x)"
+ "%s: (%s:%d) No indications were pushed by cid 0x%x"
+ "%s: (%s:%d) No registered cid 0x%04X"
+ "%s: (%s:%d) No unfinished data, resetting cache"
+ "%s: (%s:%d) Non-registered cid 0x%04X from buffer ctx 0x%08X"
+ "%s: (%s:%d) Not able to handle ARI_RT_IPC_DATA"
+ "%s: (%s:%d) Not able to process ARI message due to internal error"
+ "%s: (%s:%d) Notifying ARI event for cid 0x%x event %s"
+ "%s: (%s:%d) Outbound Msg sz%d ctx(0x%08X) for sniffer (%s) "
+ "%s: (%s:%d) Owner(%p) data(%p) size(%zu)"
+ "%s: (%s:%d) PCITransportStatusError Async read error 0x%08x sz(%u)"
+ "%s: (%s:%d) PCITransportStatusError reported from PCITransport library (%p, %p)"
+ "%s: (%s:%d) PCITransportStatusNotReady reported from PCITransport library (%p, %p)"
+ "%s: (%s:%d) Pending transition for cid 0x%x token %llu client %s"
+ "%s: (%s:%d) Received All-ready via indication"
+ "%s: (%s:%d) Received All-ready via response"
+ "%s: (%s:%d) Received boot state, but %s"
+ "%s: (%s:%d) Received checkin from client %s"
+ "%s: (%s:%d) Received invalid check-in name in client registration request"
+ "%s: (%s:%d) Received invalid message from XPC client id(%u) size(%lu), msg(%p)\n"
+ "%s: (%s:%d) Received notify ACK from cid 0x%x for event %s token %llu"
+ "%s: (%s:%d) RegIndication: ARI_INVALID_CID for indication(%d-0x%x)"
+ "%s: (%s:%d) RegIndication: Add client(%s:0x%x) as listening for indication(%d-0x%x)"
+ "%s: (%s:%d) RegIndication: Duplicated handler from client(%s) for indication(%d-0x%x), no-op"
+ "%s: (%s:%d) RegIndication: No registered cid 0x%04X for indication(%d-0x%x)"
+ "%s: (%s:%d) RegIndication: client(%s:0x%x) first to register indication(%d-0x%x)"
+ "%s: (%s:%d) Registering all indications triggered by cid 0x%x"
+ "%s: (%s:%d) Registering indication gmid 0x%x triggered by cid 0x%x"
+ "%s: (%s:%d) Removing active transition tracking for cid 0x%x token %llu"
+ "%s: (%s:%d) Removing connection %s"
+ "%s: (%s:%d) ResMgr(%p) dump total entries: %zu"
+ "%s: (%s:%d) Sending AriGrpMsgsAttribReq with %u gmids"
+ "%s: (%s:%d) Sending XPC ARI registration reply with cid 0x%04x"
+ "%s: (%s:%d) Setting unknown mode"
+ "%s: (%s:%d) Skipping event due to termination imminent: %s"
+ "%s: (%s:%d) Skipping request-draining due to imminent LPM timeout in %dms"
+ "%s: (%s:%d) SocketTransport unavailable on this build"
+ "%s: (%s:%d) Some clients did not dump state"
+ "%s: (%s:%d) TOP newDataSizeRemains(%zu) newDataSizeConsumed(%zu) cachedSize(%zu) newDataToConsume(%zu)"
+ "%s: (%s:%d) Terminating conn(%s)"
+ "%s: (%s:%d) Transaction ID: 0x%x, GMID: (%d-0x%x), Client ID: 0x%x ( %s )"
+ "%s: (%s:%d) Transaction In-Flight:"
+ "%s: (%s:%d) Transaction(%s) timeout after %llu msec (%llu msec actual)"
+ "%s: (%s:%d) Unable to create payload.  Out of memory?"
+ "%s: (%s:%d) Unable to pack AriGrpMsgsAttribReq"
+ "%s: (%s:%d) Unable to re-register indications using invalid cid 0x%x"
+ "%s: (%s:%d) Unexpected AriHostRt internal message(%d-0x%03X)"
+ "%s: (%s:%d) Unknown xpc event: %s"
+ "%s: (%s:%d) Unrecognized status reported by PCITransport library: status=0x%08x (%p, %p)"
+ "%s: (%s:%d) Updating RT with all indications pushed by cid 0x%x"
+ "%s: (%s:%d) Updating sensitive logging gmid: 0x%x"
+ "%s: (%s:%d) Using transport device %s"
+ "%s: (%s:%d) Write(size=%u) completed with status %u"
+ "%s: (%s:%d) XPC Listener: setting up connection"
+ "%s: (%s:%d) XPC Server has %zu active connections:"
+ "%s: (%s:%d) XPC resources:"
+ "%s: (%s:%d) Zero gmids provided"
+ "%s: (%s:%d) attempt to drain lpm-critical request based on %u outstanding requests with %dms timeout"
+ "%s: (%s:%d) attempted ack of stale token %llu for cid 0x%x"
+ "%s: (%s:%d) canceling %u outstanding requests"
+ "%s: (%s:%d) cid 0x%x requested group registration, but no indications are registered"
+ "%s: (%s:%d) cid 0x%x requested group registration, registered %u indications"
+ "%s: (%s:%d) client(%s:0x%x) no longer listening for msgid(%d-0x%x)"
+ "%s: (%s:%d) clientAriMsgCB is NULL"
+ "%s: (%s:%d) entering with cachedSize(%zu) data(%p)"
+ "%s: (%s:%d) exiting with cachedSize(%zu)"
+ "%s: (%s:%d) id(%08d-0x%08x) ts:%d"
+ "%s: (%s:%d) id(%08d-0x%08x) ts:%u"
+ "%s: (%s:%d) indication msgid(%d-0x%x) is not registered with any cid (cid 0x%x attempted deregister)"
+ "%s: (%s:%d) lpm-critical transaction draining complete"
+ "%s: (%s:%d) lpmDrainSet.size(): %zu"
+ "%s: (%s:%d) message received for ctx 0x%08x to(%d)"
+ "%s: (%s:%d) mismatched cid, expected 0x%x, received ack for cid 0x%x with token %llu"
+ "%s: (%s:%d) no longer tracking client 0x%x with token %llu"
+ "%s: (%s:%d) notifying for all clients of end of cancellation"
+ "%s: (%s:%d) notifying for all clients to DumpState"
+ "%s: (%s:%d) notifying for all clients to enter LPM"
+ "%s: (%s:%d) notifying for all clients to exit LPM"
+ "%s: (%s:%d) notifying for all clients to stall (LPM enter)"
+ "%s: (%s:%d) notifying for all clients to stall (crash)"
+ "%s: (%s:%d) received notify ack from cid 0x%x for event %s"
+ "%s: (%s:%d) received unknown xpc command 0x%llx"
+ "%s: (%s:%d) sending RT AriMsgAttribReq %s %s on msg(%d-0x%03x) val(0x%x-%s)..."
+ "%s: (%s:%d) sending RT boot state request..."
+ "%s: (%s:%d) stall complete"
+ "%s: (%s:%d) timeout waiting %dms to drain lpm-critical transactions"
+ "%s: (%s:%d) timeout waiting for client to %s LPM"
+ "%s: (%s:%d) timeout waiting for client to stall"
+ "%s: (%s:%d) timeout waiting for clients to ack end of cancellation"
+ "%s: (%s:%d) timeout waiting for clients to stall"
+ "%s: (%s:%d) tracking client 0x%x with token %llu for transition: %s"
+ "%s: (%s:%d) trx(%s) is lpm-critical"
+ "%s: (%s:%d) trx(%s) not drained before lpm"
+ "ari"
+ "ari_rt_tx"
- "0 <= capabilities::radio::ARITransportTimeout().count()"
- "ari_osa_ios_libtu_ipc.cpp"
- "capabilities::radio::ARITransportTimeout().count() <= std::numeric_limits<UInt32>::max()"

```
