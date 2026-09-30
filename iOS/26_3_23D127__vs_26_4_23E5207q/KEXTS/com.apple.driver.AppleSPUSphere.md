## com.apple.driver.AppleSPUSphere

> `com.apple.driver.AppleSPUSphere`

```diff

-1046.60.2.0.0
-  __TEXT.__cstring: 0x220
-  __TEXT_EXEC.__text: 0x1a28
+1046.100.13.0.0
+  __TEXT.__cstring: 0x2aa
+  __TEXT.__os_log: 0x1b3
+  __TEXT_EXEC.__text: 0x1ae8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__const: 0x770
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 62B7AD06-B15D-3F61-AB54-C969F4F226C3
-  Functions: 57
+  UUID: 02CED20A-0CF0-3530-98FF-8A9B17708585
+  Functions: 59
   Symbols:   0
-  CStrings:  19
+  CStrings:  34
 
CStrings:
+ "AppleSPUSphereDriver setEnable(%d) for %s\n"
+ "UnkownSphereEndpoint"
+ "control: num_samples: %d latency: %d - %d\n"
+ "kSphereEndpointControl"
+ "kSphereEndpointCount"
+ "kSphereEndpointMotion"
+ "kSphereEndpointMotionFullRate"
+ "kSphereEndpointPearl"
+ "motion: num_samples: %d latency: %d - %d\n"
+ "motion_full_rate: num_samples: %d latency: %d - %d\n\n"
+ "motion_full_rate: num_samples: %d sample interval: %d - %d\n"
+ "motion_full_rate: session start ts: %llu, session end ts: %llu\n"
+ "motion_full_rate: session_latency_violations: %d\n"
+ "motion_full_rate: session_samples: %d\n"
+ "pearl: num_samples: %d latency: %d - %d\n"

```
