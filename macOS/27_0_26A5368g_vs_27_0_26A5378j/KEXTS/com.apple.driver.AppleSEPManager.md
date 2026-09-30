## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-  __TEXT.__cstring: 0xd088
+  __TEXT.__cstring: 0xd178
   __TEXT.__const: 0x56c
-  __TEXT_EXEC.__text: 0x2dcac
+  __TEXT_EXEC.__text: 0x2dfe4
   __TEXT_EXEC.__auth_stubs: 0x900
   __DATA.__data: 0x168
   __DATA.__common: 0xb08
   __DATA.__bss: 0x49
   __DATA_CONST.__mod_init_func: 0xa8
   __DATA_CONST.__mod_term_func: 0xa8
-  __DATA_CONST.__const: 0xa9f8
+  __DATA_CONST.__const: 0xaa78
   __DATA_CONST.__kalloc_type: 0xc00
   __DATA_CONST.__kalloc_var: 0x50
   __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1743
-  Symbols:   2607
-  CStrings:  1145
+  Functions: 1747
+  Symbols:   2614
+  CStrings:  1148
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _ZN18AppleSEPUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor
+ _ZN18AppleSEPUserClient27DispatchGetTraceRecordStateEPS_PvP25IOExternalMethodArguments
+ __ZN15AppleSEPTesting17stop_trace_recordEv
+ __ZN15AppleSEPTesting18start_trace_recordEv
+ __ZN15AppleSEPTesting22get_trace_record_stateEP18trace_record_state
+ __ZN15AppleSEPTesting28get_trace_record_decode_infoEN7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEEE
+ __ZN18AppleSEPUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor
+ __ZN18AppleSEPUserClient23DispatchStopTraceRecordEPS_PvP25IOExternalMethodArguments
+ __ZN18AppleSEPUserClient24DispatchStartTraceRecordEPS_PvP25IOExternalMethodArguments
+ __ZN18AppleSEPUserClient27DispatchGetTraceRecordStateEPS_PvP25IOExternalMethodArguments
+ ____ZN15AppleSEPTesting17stop_trace_recordEv_block_invoke
+ ____ZN15AppleSEPTesting18start_trace_recordEv_block_invoke
+ ____ZN15AppleSEPTesting22get_trace_record_stateEP18trace_record_state_block_invoke
+ ____ZN15AppleSEPTesting28get_trace_record_decode_infoEN7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEEE_block_invoke
- _ZN15AppleSEPControl29cmsgCPU_TRACE_GET_STREAM_FILLEPj
- __ZN12IOUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor
- __ZN15AppleSEPControl19cmsgCPU_TRACE_RESETEv
- __ZN15AppleSEPControl24cmsgCPU_TRACE_START_STOPEb
- __ZN15AppleSEPControl28cmsgCPU_TRACE_SET_WRAPAROUNDEb
- __ZN15AppleSEPControl29cmsgCPU_TRACE_GET_STREAM_FILLEPj
- __ZN18AppleSEPUserClient19DispatchCpuTraceGetEPS_PvP25IOExternalMethodArguments
- __ZN18AppleSEPUserClient21DispatchCpuTraceResetEPS_PvP25IOExternalMethodArguments
- __ZN18AppleSEPUserClient24DispatchCpuTraceDumpInfoEPS_PvP25IOExternalMethodArguments
- __ZN18AppleSEPUserClient25DispatchCpuTraceStartStopEPS_PvP25IOExternalMethodArguments
- __ZN18AppleSEPUserClient33DispatchCpuTraceSetWrapAroundModeEPS_PvP25IOExternalMethodArguments
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AllocMPM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPBooter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDebug.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDebugArgs.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDiscovery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPEndpoint.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPFirmware.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPManagerARM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPPairing.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPTesting.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPTraceBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/FIFO.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/SEPApNonce.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/SEPEpoch.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/AppleSEPXART.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/DisableLog.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/gigalocker/gigalocker.cpp"
+ "12111112122212121111111111111"
+ "PE_i_can_has_debugger(NULL)"
+ "decode_info != nullptr"
+ "static IOReturn AppleSEPUserClient::DispatchGetTraceRecordState(AppleSEPUserClient *, void *, IOExternalMethodArguments *)"
+ "target->_asep->cpu_trace_memory != nullptr"
+ "virtual IOReturn AppleSEPUserClient::clientMemoryForType(uint32_t, IOOptionBits *, IOMemoryDescriptor **)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AllocMPM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPBooter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPCommand.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPDebug.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPDebugArgs.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPDiscovery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPEndpoint.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPFirmware.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPLogger.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPManagerARM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPPairing.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPTesting.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPTraceBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/AppleSEPUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/FIFO.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/SEPApNonce.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/SEPEpoch.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/xART/AppleSEPXART.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/xART/DisableLog.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mhbN5l/Sources/AppleSEPManager/xART/gigalocker/gigalocker.cpp"
- "1211111212221212111111111111"
- "IOReturn AppleSEPControl::cmsgCPU_TRACE_GET_STREAM_FILL(uint32_t *)"
- "nullptr != fill"

```
