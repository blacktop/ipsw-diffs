## libKTLDynamic.dylib

> `/usr/lib/libKTLDynamic.dylib`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x21760
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x14d0
-  __TEXT.__cstring: 0x2f52
-  __TEXT.__unwind_info: 0xa78
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x160
-  __AUTH_CONST.__auth_got: 0xae0
-  __AUTH_CONST.__const: 0x10b8
-  __DATA.__data: 0x40
-  __DATA.__bss: 0x118
+1371.0.1.0.0
+  __TEXT.__text: 0x255b0
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__const: 0x158
+  __TEXT.__gcc_except_tab: 0x18b4
+  __TEXT.__cstring: 0x351d
+  __TEXT.__oslogstring: 0x41
+  __TEXT.__unwind_info: 0xbd8
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x180
+  __AUTH_CONST.__auth_got: 0xc68
+  __AUTH_CONST.__const: 0x1240
+  __DATA.__data: 0xa0
+  __DATA.__bss: 0x128
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libARI.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 79E2B692-1734-3792-AF01-85873FE09192
-  Functions: 400
-  Symbols:   1269
-  CStrings:  385
+  UUID: 8C195AC5-6154-3793-A71D-9448A794E473
+  Functions: 427
+  Symbols:   1412
+  CStrings:  421
 
Symbols:
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table87
+ GCC_except_table88
+ __Block_copy
+ __Block_release
+ __KTLDebugPrintBinaryOsLog
+ __KTLDebugPrintOsLog
+ __NSConcreteGlobalBlock
+ __ZN3Ari10MsgDefByIdEjj
+ __ZN3Ari11MsgNameByIdEj
+ __ZN3Ari12GetLogLevelsEv
+ __ZN3Bsp16BspCommandDriverD2Ev
+ __ZN3ktl13CommandDriver18registerIndicationEjN8dispatch5blockIU13block_pointerFiPhjEEE
+ __ZN3ktl13CommandDriver20deregisterIndicationEj
+ __ZN5eUICC18VinylCommandDriver12ResetSimCardEPN6AriSdk31ARI_IBIVinylSimCardResetReq_SDKEPPNS1_33ARI_IBIVinylSimCardResetRspCb_SDKE
+ __ZN5eUICC18VinylCommandDriver13ManagePairingEPN6AriSdk26ARI_IBIVinylPairingReq_SDKEPPNS1_28ARI_IBIVinylPairingRspCb_SDKE
+ __ZN5eUICC18VinylCommandDriver16GetHwIdSimConfigEPN6AriSdk32ARI_IBIVinylHwIdSimConfigReq_SDKEPPNS1_34ARI_IBIVinylHwIdSimConfigRspCb_SDKE
+ __ZN5trace16ARICommandDriver10TraceFlushEPN6AriSdk21ARI_TraceFlushReq_SDKEPPNS1_23ARI_TraceFlushRspCb_SDKE
+ __ZN5trace16ARICommandDriver18isARIResponseValidERKN6AriSdk7MsgBaseEj
+ __ZN6AriOsa24LogToDefaultStringLoggerEjPKcz
+ __ZN6AriOsa8GetOsLogEv
+ __ZN6AriSdk23ARI_TraceFlushRspCb_SDK6unpackEv
+ __ZN6AriSdk23ARI_TraceFlushRspCb_SDKC1EPKhj
+ __ZN6AriSdk28ARI_IBIVinylPairingRspCb_SDK6unpackEv
+ __ZN6AriSdk28ARI_IBIVinylPairingRspCb_SDKC1EPKhj
+ __ZN6AriSdk29ARI_TraceFlushCompleteInd_SDK6unpackEv
+ __ZN6AriSdk29ARI_TraceFlushCompleteInd_SDKC1EPKhj
+ __ZN6AriSdk29ARI_TraceFlushCompleteInd_SDKD1Ev
+ __ZN6AriSdk33ARI_IBIVinylSimCardResetRspCb_SDK6unpackEv
+ __ZN6AriSdk33ARI_IBIVinylSimCardResetRspCb_SDKC1EPKhj
+ __ZN6AriSdk34ARI_IBIVinylHwIdSimConfigRspCb_SDK6unpackEv
+ __ZN6AriSdk34ARI_IBIVinylHwIdSimConfigRspCb_SDKC1EPKhj
+ __ZN7AriHost13RegIndicationEjiU13block_pointerFiPhjE
+ __ZN7AriHost15DeregIndicationEji
+ __ZNK3ktl13CommandDriver12isIndicationEj
+ __ZNK6AriSdk23ARI_TraceFlushRspCb_SDK15hasDeclaredGmidEv
+ __ZNK6AriSdk28ARI_IBIVinylPairingRspCb_SDK15hasDeclaredGmidEv
+ __ZNK6AriSdk33ARI_IBIVinylSimCardResetRspCb_SDK15hasDeclaredGmidEv
+ __ZNK6AriSdk34ARI_IBIVinylHwIdSimConfigRspCb_SDK15hasDeclaredGmidEv
+ __ZNK6AriSdk7MsgBase7getGMIDEv
+ __ZNSt11logic_errorC2ERKS_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt13exception_ptr31__from_native_exception_pointerEPv
+ __ZNSt13exception_ptrC1ERKS_
+ __ZNSt13exception_ptrD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__110shared_ptrIKNS_6vectorIhNS_9allocatorIhEEEEED1B8ne200100Ev
+ __ZNSt3__110shared_ptrIN3ctu7GestaltEED1B8ne200100Ev
+ __ZNSt3__110shared_ptrIN3ctu7GestaltEEaSB8ne200100EOS3_
+ __ZNSt3__110shared_ptrIN3ktl13CommandDriverEED2B8ne200100Ev
+ __ZNSt3__110shared_ptrIN6AriSdk31ARI_CsiIceRFFilerWriteRspCb_SDKEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjN8dispatch5blockIU13block_pointerFiPhjEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEED1B8ne200100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjN8dispatch5blockIU13block_pointerFiPhjEEEEENS_22__unordered_map_hasherIjS8_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS8_SD_SB_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSO_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112future_errorC1ENS_10error_codeE
+ __ZNSt3__112future_errorD0Ev
+ __ZNSt3__112future_errorD1Ev
+ __ZNSt3__113__assoc_stateIbE16__on_zero_sharedEv
+ __ZNSt3__113__assoc_stateIbED0Ev
+ __ZNSt3__113__assoc_stateIbED1Ev
+ __ZNSt3__114__shared_countD2Ev
+ __ZNSt3__115future_categoryEv
+ __ZNSt3__117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
+ __ZNSt3__117__assoc_sub_state13set_exceptionESt13exception_ptr
+ __ZNSt3__117__assoc_sub_state9__executeEv
+ __ZNSt3__118condition_variable10notify_allEv
+ __ZNSt3__118condition_variable15__do_timed_waitERNS_11unique_lockINS_5mutexEEENS_6chrono10time_pointINS5_12system_clockENS5_8durationIxNS_5ratioILl1ELl1000000000EEEEEEE
+ __ZNSt3__118condition_variableD1Ev
+ __ZNSt3__119__shared_weak_count4lockEv
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__throw_future_errorB8ne200100ENS_11future_errcE
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ __ZNSt3__16chrono12steady_clock3nowEv
+ __ZNSt3__16chrono12system_clock3nowEv
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__17promiseIbED2Ev
+ __ZSt17rethrow_exceptionSt13exception_ptr
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTINSt3__112future_errorE
+ __ZTINSt3__113__assoc_stateIbEE
+ __ZTINSt3__117__assoc_sub_stateE
+ __ZTISt20bad_array_new_length
+ __ZTSNSt3__113__assoc_stateIbEE
+ __ZTVNSt3__112future_errorE
+ __ZTVNSt3__113__assoc_stateIbEE
+ __ZTVNSt3__117__assoc_sub_stateE
+ __ZZSt18make_exception_ptrB8ne200100INSt3__112future_errorEESt13exception_ptrT_ENUlPvE_8__invokeES4_
+ ___Block_byref_object_copy_.15
+ ___Block_byref_object_dispose_.16
+ ____KTLDebugGetOsLogObject_block_invoke
+ ____ZN3ktl13CommandDriver18registerIndicationEjN8dispatch5blockIU13block_pointerFiPhjEEE_block_invoke
+ ____ZN3ktl13CommandDriver7performIN6AriSdk23ARI_TraceFlushRspCb_SDKEEEbjNSt3__110shared_ptrIKNS4_6vectorIhNS4_9allocatorIhEEEEEEPPT__block_invoke
+ ____ZN3ktl13CommandDriver7performIN6AriSdk28ARI_IBIVinylPairingRspCb_SDKEEEbjNSt3__110shared_ptrIKNS4_6vectorIhNS4_9allocatorIhEEEEEEPPT__block_invoke
+ ____ZN3ktl13CommandDriver7performIN6AriSdk33ARI_IBIVinylSimCardResetRspCb_SDKEEEbjNSt3__110shared_ptrIKNS4_6vectorIhNS4_9allocatorIhEEEEEEPPT__block_invoke
+ ____ZN3ktl13CommandDriver7performIN6AriSdk34ARI_IBIVinylHwIdSimConfigRspCb_SDKEEEbjNSt3__110shared_ptrIKNS4_6vectorIhNS4_9allocatorIhEEEEEEPPT__block_invoke
+ ____ZN5trace16ARICommandDriver10TraceFlushEPN6AriSdk21ARI_TraceFlushReq_SDKEPPNS1_23ARI_TraceFlushRspCb_SDKE_block_invoke
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.53
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.59
+ ___block_literal_global
+ ___copy_helper_block_e8_32r48c44_ZTSNSt3__18weak_ptrIN3ktl13CommandDriverEEE
+ ___copy_helper_block_e8_40c44_ZTSNSt3__18weak_ptrIN3ktl13CommandDriverEEE
+ ___cxa_init_primary_exception
+ ___destroy_helper_block_e8_32r48c44_ZTSNSt3__18weak_ptrIN3ktl13CommandDriverEEE
+ ___destroy_helper_block_e8_40c44_ZTSNSt3__18weak_ptrIN3ktl13CommandDriverEEE
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_once
+ _os_log_create
+ _os_log_type_enabled
+ _vsnprintf
- GCC_except_table20
- _TelephonyUtilGetSystemTime
- _TelephonyUtilLogGetBufferSize
- __GLOBAL__sub_I_ice_filer.cpp
- __KTLDebugPrintBinaryStdout
- __KTLDebugPrintStdout
- __ZL15sKTLGetFileNamePKcS0_
- __ZL21ice_filer_lookup_head
- __ZL22ice_filer_lookup_mutex
- __ZL23CreateFilerWriteRequestPvjRNSt3__110shared_ptrIKNS0_6vectorIhNS0_9allocatorIhEEEEEE
- __ZN21ice_filer_lookup_nodeD1Ev
- __ZN3Ari3LogEjPKcz
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110shared_ptrIKNS_6vectorIhNS_9allocatorIhEEEEED1B8ne190102Ev
- __ZNSt3__110shared_ptrIN3ctu7GestaltEED1B8ne190102Ev
- __ZNSt3__110shared_ptrIN3ctu7GestaltEEaSB8ne190102EOS3_
- __ZNSt3__110shared_ptrIN6AriSdk31ARI_CsiIceRFFilerWriteRspCb_SDKEED1B8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- ___stderrp
- _fopen
- _sKTLDebugOutputFile
- _vfprintf
CStrings:
+ "%s"
+ "%s\n"
+ "%s indication received but no indication handler exists"
+ "%s indication received; calling indication handler"
+ "%s is not an indication, not deregistering it"
+ "%s is not an indication, not registering it"
+ "%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)"
+ "/AppleInternal/Library/BuildRoots/4~B2AGugDOa2l_yFhw3uGmjchactnzc7ObWLaiPV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "Command driver with ariId=%d deregistering for indication: %s (%u, 0x%x)"
+ "Command driver with ariId=%d failed to deregister indication: %s (%u, 0x%x)"
+ "Command driver with ariId=%d failed to register indication: %s (%u, 0x%x)"
+ "Command driver with ariId=%d registering for indication: %s (%u, 0x%x)"
+ "Command driver with ariId=%d successfully deregistered for indication: %s (%u, 0x%x)"
+ "Command driver with ariId=%d successfully registered for indication: %s (%u, 0x%x)"
+ "Error while receiving trace flush indication"
+ "Failed to flush trace"
+ "Flushing trace"
+ "GetHwIdSimConfig"
+ "Indication %s is not currently registered, no need to deregister it"
+ "ManagePairing"
+ "Perform trace flush"
+ "Received trace flush indication callback"
+ "Registering for trace flush complete indication"
+ "ResetSimCard"
+ "Successfully flushed trace"
+ "Timeout while waiting for trace flush indication"
+ "Trace flush indication received successfully"
+ "TraceFlush"
+ "TraceFlush_block_invoke"
+ "Unexpected status while waiting for trace flush indication"
+ "VinylCommandDriver GetHwIdSimConfig perform failure"
+ "VinylCommandDriver Manage pairing failure"
+ "VinylCommandDriver Reset Sim Card failure"
+ "[%s:%u] %s\n%s\n"
+ "[ind] Error while unpacking trace flush complete indication"
+ "[ind] Got unexpected message 0x%0x, expected trace flush complete indication (0x%0x)"
+ "[ind] Trace flush complete indication success"
+ "ari"
+ "com.apple.telephony.bb"
+ "deregisterIndication"
+ "ktl"
+ "registerIndication"
+ "registerIndication_block_invoke"
+ "v8@?0"
- "%u.%03u %s:"
- "%u.%03u [%s] %s\n%s"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/dev/null"
- "/private/var/wireless/Library/Logs/CrashReporter/Baseband/libKTL.log"
- "Warning: Failed to open %s for writing\n"
- "a"
- "w"

```
