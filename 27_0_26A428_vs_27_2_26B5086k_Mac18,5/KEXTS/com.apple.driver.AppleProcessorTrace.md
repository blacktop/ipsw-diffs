## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-130.0.0.0.0
-  __TEXT.__os_log: 0x19a2
+130.40.6.0.0
+  __TEXT.__os_log: 0x1993
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x5981
-  __TEXT_EXEC.__text: 0x3bc30
+  __TEXT.__cstring: 0x59a7
+  __TEXT_EXEC.__text: 0x3beb4
   __TEXT_EXEC.__auth_stubs: 0x760
   __DATA.__data: 0xc4
   __DATA.__common: 0x760
   __DATA_CONST.__mod_init_func: 0xe8
   __DATA_CONST.__mod_term_func: 0xe8
-  __DATA_CONST.__const: 0x115a8
+  __DATA_CONST.__const: 0x115e8
   __DATA_CONST.__weak_auth_got: 0xb0
   __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0x1e0
   __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0xb0
-  Functions: 1314
-  Symbols:   2058
-  CStrings:  519
+  __DATA_CONST.__got: 0xb8
+  Functions: 1317
+  Symbols:   2063
+  CStrings:  522
 
Symbols:
+ __ZN19AppleProcessorTrace10enterSleepEv
+ __ZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTarget
+ __ZN19AppleProcessorTrace28clearTraceChunksClusterGatedE16ChunkQueueTarget
+ __ZN19AppleProcessorTrace9enterWakeEv
+ __ZN37AppleProcessorTraceFracturedMemoryMap5bzeroEv
+ __ZTV8OSObject
+ __ZZN19AppleProcessorTrace10enterSleepEvE11_os_log_fmt
+ __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetE11_os_log_fmt
+ __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetEN3$_08__invokeEPZNS_26stopTracingOnClustersGatedES0_E12XCallPayload
+ __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetEN3$_18__invokeEPS_
+ __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetEN3$_28__invokeEPS_
+ __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetEN3$_38__invokeEPS_
+ __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetEN3$_48__invokeEPS_
+ __ZZN19AppleProcessorTrace27startTracingOnClustersGatedEN21apple_processor_trace11DriverStateEE11_os_log_fmt_5
+ __ZZN19AppleProcessorTrace9enterWakeEvE11_os_log_fmt
+ __ZZN23cpu_broadcast_xcallableIZN19AppleProcessorTrace26stopTracingOnClustersGatedE16ChunkQueueTargetE12XCallPayloadEclEvENUlPvE_8__invokeES4_
+ ____ZN37AppleProcessorTraceFracturedMemoryMap5bzeroEv_block_invoke
- __ZN19AppleProcessorTrace15hibernationWakeEv
- __ZN19AppleProcessorTrace16hibernationSleepEv
- __ZN19AppleProcessorTrace26stopTracingOnClustersGatedEv
- __ZN19AppleProcessorTrace28clearTraceChunksClusterGatedEv
- __ZZN19AppleProcessorTrace15hibernationWakeEvE11_os_log_fmt
- __ZZN19AppleProcessorTrace16hibernationSleepEvE11_os_log_fmt
- __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedEvE11_os_log_fmt
- __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedEvEN3$_08__invokeEPS_
- __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedEvEN3$_18__invokeEPS_
- __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedEvEN3$_28__invokeEPS_
- __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedEvEN3$_38__invokeEPS_
- __ZZN19AppleProcessorTrace26stopTracingOnClustersGatedEvEN3$_48__invokeEPS_
CStrings:
+ "%s: resume tracing"
+ "%s: state=%d"
+ "AppleProcessorTrace::enterSleep\n"
+ "AppleProcessorTrace::enterWake\n"
+ "expectState(DriverState::Sleeping)"
+ "setState"
+ "startTracingOnClustersGated"
+ "void AppleProcessorTrace::enterSleep()"
+ "void AppleProcessorTrace::enterWake()"
+ "void AppleProcessorTrace::stopTracingOnClustersGated(ChunkQueueTarget)"
- "AppleProcessorTrace::hibernationSleep\n"
- "AppleProcessorTrace::hibernationWake\n"
- "AppleProcessorTrace::setState(%d)\n"
- "expectState(DriverState::Hibernating)"
- "void AppleProcessorTrace::hibernationSleep()"
- "void AppleProcessorTrace::hibernationWake()"
- "void AppleProcessorTrace::stopTracingOnClustersGated()"
```
