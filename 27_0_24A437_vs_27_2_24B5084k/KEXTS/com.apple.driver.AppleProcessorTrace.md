## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-130.0.0.0.0
-  __TEXT.__os_log: 0x19a2
+130.40.6.0.0
+  __TEXT.__os_log: 0x1993
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x5981
-  __TEXT_EXEC.__text: 0x3ba2c
+  __TEXT.__cstring: 0x59a7
+  __TEXT_EXEC.__text: 0x3bcb0
   __TEXT_EXEC.__auth_stubs: 0x760
   __DATA.__data: 0xc4
   __DATA.__common: 0x760
   __DATA_CONST.__mod_init_func: 0xe8
   __DATA_CONST.__mod_term_func: 0xe8
-  __DATA_CONST.__const: 0xb188
+  __DATA_CONST.__const: 0xb1c8
   __DATA_CONST.__weak_auth_got: 0xb0
   __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0x1e0
   __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0xb0
-  Functions: 1314
+  __DATA_CONST.__got: 0xb8
+  Functions: 1317
   Symbols:   0
-  CStrings:  519
+  CStrings:  522
 
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
