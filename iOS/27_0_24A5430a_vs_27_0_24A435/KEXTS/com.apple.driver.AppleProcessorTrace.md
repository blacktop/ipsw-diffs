## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

 130.0.0.0.0
   __TEXT.__os_log: 0x19a2
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x548e
-  __TEXT_EXEC.__text: 0x33bcc
+  __TEXT.__cstring: 0x5981
+  __TEXT_EXEC.__text: 0x3c314
   __TEXT_EXEC.__auth_stubs: 0x760
   __DATA.__data: 0xc4
-  __DATA.__common: 0x6e8
-  __DATA_CONST.__mod_init_func: 0xd0
-  __DATA_CONST.__mod_term_func: 0xd0
-  __DATA_CONST.__const: 0x9d90
+  __DATA.__common: 0x760
+  __DATA_CONST.__mod_init_func: 0xe8
+  __DATA_CONST.__mod_term_func: 0xe8
+  __DATA_CONST.__const: 0xb188
   __DATA_CONST.__weak_auth_got: 0xb0
-  __DATA_CONST.__kalloc_type: 0x680
+  __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0x1e0
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xb0
-  Functions: 1185
+  Functions: 1314
   Symbols:   0
-  CStrings:  500
+  CStrings:  519
 
CStrings:
+ "121111121222121211111112112211211211211211211211211211211211"
+ "AppleProcessorTraceT8152"
+ "AppleProcessorTraceT8160"
+ "AppleProcessorTraceT8320"
+ "site.AppleProcessorTraceT8152"
+ "site.AppleProcessorTraceT8160"
+ "site.AppleProcessorTraceT8320"
+ "uint64_t AppleProcessorTraceT8152::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)"
+ "uint64_t AppleProcessorTraceT8160::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)"
+ "uint64_t AppleProcessorTraceT8320::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8152::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8160::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8320::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual void AppleProcessorTraceT8152::defeatureCore(bool)"
+ "virtual void AppleProcessorTraceT8160::defeatureCore(bool)"
+ "virtual void AppleProcessorTraceT8320::defeatureCore(bool)"
+ "void AppleProcessorTraceT8152::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)"
+ "void AppleProcessorTraceT8160::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)"
+ "void AppleProcessorTraceT8320::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)"
```
