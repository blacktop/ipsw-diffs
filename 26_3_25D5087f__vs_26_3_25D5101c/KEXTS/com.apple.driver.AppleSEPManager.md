## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-880.80.5.0.0
+880.80.6.0.0
   __TEXT.__const: 0x5dc
-  __TEXT.__cstring: 0xc679
-  __TEXT_EXEC.__text: 0x30fc4
+  __TEXT.__cstring: 0xc980
+  __TEXT_EXEC.__text: 0x315f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xb08

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xa8
   __DATA_CONST.__mod_term_func: 0xa8
-  __DATA_CONST.__const: 0xa970
+  __DATA_CONST.__const: 0xa9c0
   __DATA_CONST.__kalloc_type: 0xc00
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: 540467DD-428F-37CB-96F3-75042B667A8C
-  Functions: 1660
-  Symbols:   2503
-  CStrings:  1105
+  UUID: 5A87C4EC-41E7-3380-AE56-C2E06055E3CF
+  Functions: 1668
+  Symbols:   2513
+  CStrings:  1121
 
Symbols:
+ _ZL23reseedXNUPRNGThreadCallPvS_.cold.1
+ _ZN15AppleSEPManager14_setPowerStateEPm.cold.8
+ __ZL23reseedXNUPRNGThreadCallPvS_
+ __ZN15AppleSEPManager14tryStartReseedEv
+ __ZN15AppleSEPManager9endReseedEv
+ ___ZN15AppleSEPManager9endReseedEv_block_invoke.cold.1
+ ____ZN15AppleSEPManager14tryStartReseedEv_block_invoke
+ ____ZN15AppleSEPManager9endReseedEv_block_invoke
+ __block_descriptor_tmp.190
+ __block_descriptor_tmp.193
+ __block_descriptor_tmp.198
+ __block_descriptor_tmp.308
+ __block_descriptor_tmp.314
- __block_descriptor_tmp.188
- __block_descriptor_tmp.295
- __block_descriptor_tmp.301
CStrings:
+ "!_fips_reseed_in_progress"
+ "\"Failed to reseed XNU PRNG after %d attempts during boot\" @%s:%d"
+ "\"Unreachable.\" @%s:%d"
+ "%s: FIPS reseed complete, waking up pending sleep operation\n"
+ "%s: FIPS reseed completed\n"
+ "%s: FIPS reseed rejected: SEP not ready (state: %u)\n"
+ "%s: FIPS reseed rejected: operation already in progress\n"
+ "%s: FIPS reseed rejected: system not in PM_STATE_ON (current: %u)\n"
+ "%s: FIPS reseed started\n"
+ "%s: Power state transition %u -> %u proceeding after FIPS reseeding completed\n"
+ "%s: Power state transition %u -> %u waiting for FIPS reseeding to complete\n"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AllocMPM.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPBooter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPControl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDebug.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDebugArgs.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDiscovery.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPEndpoint.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPFirmware.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPManagerARM.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPPairing.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPTesting.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPTraceBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/FIFO.h"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPApNonce.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPEpoch.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/AppleSEPXART.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/DisableLog.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC4xe4IecI0xYzzTztoMA8oZRtSxDNCn5I/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/gigalocker/gigalocker.cpp"
+ "121111121222121211121212221211111111112212221121111121222211111121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221211222222222222222222222222222222222221212"
+ "AppleSEP:WARNING: Unable to reseed XNU PRNG, attempt %d/%d\n"
+ "GET_ENTROPY_FOR_XNU_PRNG call to SEP returned unknown error"
+ "Unable to retrieve randomness out of SEP"
+ "_fips_reseed_in_progress"
+ "bool AppleSEPManager::reseedXNUPRNG()"
+ "bool AppleSEPManager::tryStartReseed()_block_invoke"
+ "void AppleSEPManager::endReseed()_block_invoke"
- "\"GET_ENTROPY_FOR_XNU_PRNG call to SEP returned unknown error\" @%s:%d"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AllocMPM.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPBooter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPCommand.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPControl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDebug.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDebugArgs.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDevice.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPDiscovery.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPEndpoint.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPFirmware.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPLogger.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPManagerARM.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPPairing.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPTesting.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPTraceBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/AppleSEPUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/FIFO.h"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPApNonce.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPEpoch.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/AppleSEPXART.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/DisableLog.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD23ugAm_oNttXBsG9UYPrWnk-C0n8V_k3LB6z0/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/xART/gigalocker/gigalocker.cpp"
- "12111112122212121112121222121111111111221222112111112122221111112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121122222222222222222222222222222222222121"
- "void AppleSEPManager::reseedXNUPRNG()"

```
