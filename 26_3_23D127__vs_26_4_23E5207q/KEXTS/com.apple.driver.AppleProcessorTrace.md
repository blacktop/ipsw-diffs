## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-78.80.3.0.0
-  __TEXT.__os_log: 0x1596
-  __TEXT.__cstring: 0x4a69
-  __TEXT.__const: 0x418
-  __TEXT_EXEC.__text: 0x28278
+78.100.33.0.0
+  __TEXT.__os_log: 0x195e
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x506e
+  __TEXT_EXEC.__text: 0x2d480
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
-  __DATA.__common: 0x3f8
-  __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0xa0
+  __DATA.__common: 0x6c0
+  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__mod_init_func: 0xc8
   __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x93c8
+  __DATA_CONST.__const: 0x9570
   __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 91D04ACB-CE55-3F7F-A433-B290D1C640DD
-  Functions: 1045
+  UUID: E4AC5201-5D27-3802-A65D-51849D21BA94
+  Functions: 1101
   Symbols:   0
-  CStrings:  435
+  CStrings:  485
 
CStrings:
+ "!(config.read_port || config.task_filtering) && config.prod"
+ "!_activeSession"
+ "\"'arm-io' EDT node not found.\" @%s:%d"
+ "\"CIO_Infinite is not supported\" @%s:%d"
+ "\"EDT-provided PA of SoCPhys is null.\" @%s:%d"
+ "\"failed to find the PMGR block offset in EDT. Looked up under 'pmgr' and 'cpmgr'.\" @%s:%d"
+ "%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x"
+ "%s: apt-carveout-size-mb property has invalid size (expected %zu, got %u)\n"
+ "%s: apt-carveout-size-mb property not found\n"
+ "%s: failed to allocate NVRAM key symbol\n"
+ "%s: failed to allocate OSNumber for size=%llu\n"
+ "%s: failed to create IODTNVRAM matching dictionary\n"
+ "%s: failed to find /chosen node\n"
+ "%s: failed to find IODTNVRAM service\n"
+ "%s: failed to set property to size=%llu\n"
+ "%s: found apt-carveout-size-mb=%u MB from DT\n"
+ "%s: property not found or invalid type\n"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211"
+ "1212211112112122222222222221122111212112111"
+ "AppleProcessorTrace::addTaskGated(read_port=%u)\n"
+ "AppleProcessorTrace::prepareForPanicTrace\n"
+ "AppleProcessorTrace::reset\n"
+ "AppleProcessorTrace::startPanicTrace\n"
+ "AppleProcessorTrace::validateConfig(panic_trace=%u)\n"
+ "AppleProcessorTrace::validateConfig(read_port=%u, task_filtering=%u)\n"
+ "AppleProcessorTraceSession::enableTracingForTask()\n"
+ "AppleProcessorTraceUserClient::externalMethodAddTask\n"
+ "IOReturn AppleProcessorTrace::addTaskGated(OSSharedPtr<AppleProcessorTraceSession>, MethodAddTaskArgs)"
+ "IOReturn AppleProcessorTrace::reset(OSSharedPtr<AppleProcessorTraceSession>)"
+ "IOReturn getOrSetCarveoutSizeInMBProperty(uint64_t, uint64_t *)"
+ "IOVector.hpp"
+ "SessionUUID"
+ "apt-carveout-size-mb"
+ "apt_panic_trace"
+ "arm-io"
+ "bool AppleProcessorTrace::prepareForPanicTrace()"
+ "bool AppleProcessorTrace::startPanicTrace()"
+ "bool AppleProcessorTraceSession::enableTracingForTask(mach_port_name_t)"
+ "chosen"
+ "config.ld_st_trace && !caps.LdStTrace"
+ "config.ld_st_trace && config.prod"
+ "config.nrg_trace && !caps.EnergyTrace"
+ "config.nrg_trace && config.nrg_trace_trigger_lvl_pow2 < apple_processor_trace::NRGMinimumTriggerPow2"
+ "config.trace_mode == TraceMode::CIO_Infinite && !caps.CIO"
+ "cpmgr"
+ "data"
+ "data && size < capacity"
+ "getCarveoutSizeFromDeviceTree"
+ "getOrSetCarveoutSizeInMBProperty"
+ "name"
+ "newCapacity > capacity"
+ "newData"
+ "pmgr"
+ "ranges"
+ "reg"
+ "static IOReturn AppleProcessorTraceUserClient::externalMethodAddTask(OSObject *, void *, IOExternalMethodArguments *)"
+ "uint32_t getCarveoutSizeFromDeviceTree()"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT6040::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8132::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8140::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8142::getChunkForCluster(unsigned int, uint64_t)"
+ "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8150::getChunkForCluster(unsigned int, uint64_t)"
+ "void IOVector<task_apt_token *>::push_back(const T &) [T = task_apt_token *]"
+ "void IOVector<task_apt_token *>::resize() [T = task_apt_token *]"
- "!config.read_port && config.prod"
- "121111121222121211111112112211211211211211211211211211211211211211211211211211211"
- "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211"
- "121221111211212222222222221111212112111"
- "AppleProcessorTrace::configureGated: failed to enable trace for task: %d\n"
- "AppleProcessorTrace::validateConfig(read_port=%u)\n"
- "AppleProcessorTrace::validateConfig: driver only supports ld/st trace on dev-fused silicon\n"
- "AppleProcessorTrace::validateConfig: missing HW support for ld/st trace\n"
- "_activeSession == nullptr"
- "_traceableTaskToken == nullptr"
- "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT6040::getChunkForCluster(unsigned int)"
- "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8132::getChunkForCluster(unsigned int)"
- "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8140::getChunkForCluster(unsigned int)"
- "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8142::getChunkForCluster(unsigned int)"
- "virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8150::getChunkForCluster(unsigned int)"

```
