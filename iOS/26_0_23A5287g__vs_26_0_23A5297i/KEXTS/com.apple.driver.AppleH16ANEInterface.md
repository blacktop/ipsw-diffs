## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.11.3.0.0
+9.12.3.0.0
   __TEXT.__const: 0xab8
-  __TEXT.__cstring: 0xed21
-  __TEXT.__os_log: 0x34a3b
-  __TEXT_EXEC.__text: 0x1031ac
+  __TEXT.__cstring: 0xed50
+  __TEXT.__os_log: 0x34dc8
+  __TEXT_EXEC.__text: 0x103964
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a7c
   __DATA.__common: 0x658

   __DATA_CONST.__const: 0xc200
   __DATA_CONST.__kalloc_type: 0x3b40
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: 58521ED3-CC54-36C0-BC88-7B3CC8DA0054
-  Functions: 3274
+  UUID: F2FC6806-72F6-3B2F-A884-BE3C80E400C3
+  Functions: 3275
   Symbols:   0
-  CStrings:  4263
+  CStrings:  4282
 
CStrings:
+ "%s: %s: DartMap: DVA: 0x%llx, descrSize: %llu\n"
+ "%s: %s: ERROR: baseDVA: 0x%llx, DVA: 0x%llx, physOffset: 0x%llx, descriptorSize: 0x%lx\n"
+ "%s: %s: Enable RTBuddy endpoint %s \n"
+ "%s: %s: Failed to connect to ANE1Endpoint1, clean and reconnect to ANEEndpoint1n"
+ "%s: Buffer data sum=%d\n"
+ "%s: init_addr=%p init_size=%llu procedure_count=%zu kernel_segment=%p kernel_segment_Size=%llx"
+ "%s: missing mutable metadata buffer: %p"
+ "%s: missing mutable weight buffer: %p (n=%d)"
+ "%s: mutable kernel segment zero size"
+ "%s: mutable metadata buffer zero size"
+ "%s: mutable weight symbol missing (n=%d)"
+ "%s: mutable weight symbol too long (n=%d)"
+ "%s: mutable weight zero size (n=%d)"
+ "%s: no procedures"
+ "%s: symbol=%s weight_data=%p weight_data_size=%llx"
+ "ANE1Endpoint1"
+ "EnableRTBuddyEndpoints"
+ "ZinComputeProgramStatus ZinComputeProgramUpdatePrecheckWithSymbolicWeights(uint32_t, const ZinComputeProgramInitInfo *, const ANECMutableWeightFileData *, uint64_t, void *, uint64_t)"
+ "[ERROR] %s: %s: FW sideloading not supported in RTBuddy mode\n"
+ "[ERROR] %s: %s: Failed to Initialize RTBuddy endpoints"
+ "[ERROR] %s: %s: Failed to connected to RTBuddy endpoint"
+ "[ERROR] %s: %s: Failed to enable endpoint"
+ "[ERROR] %s: %s: Failed to get endpoint %s service"
+ "[ERROR] %s: %s: No async ref set! Skipping callback for programid=%d request_uuid=%llx asyncRef=0x%llx programResource=0x%llx\n"
- "%s: %s: DartMap: DVA: 0x%llx\n, descrSize: %llu\n"
- "%s: %s: ERROR: physOffset: 0x%llx, descriptorSize: 0x%lx\n"
- "ZinComputeProgramStatus ZinComputeProgramUpdatePrecheckWithSymbolicWeights(uint32_t, const ZinComputeProgramInitInfo *, const ANECMutableWeightFileData *, uint64_t, void *)"
- "[ERROR] %s: %s: Failed to get ANE endpoint service"
- "[ERROR] %s: %s: Failed to initialize endpoint"

```
