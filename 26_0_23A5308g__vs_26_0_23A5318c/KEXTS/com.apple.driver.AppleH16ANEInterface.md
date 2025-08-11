## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.12.3.0.0
+9.15.0.0.0
   __TEXT.__const: 0xab8
-  __TEXT.__cstring: 0xed50
-  __TEXT.__os_log: 0x34dc8
-  __TEXT_EXEC.__text: 0x103964
+  __TEXT.__cstring: 0xedd3
+  __TEXT.__os_log: 0x355af
+  __TEXT_EXEC.__text: 0x1051f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a7c
   __DATA.__common: 0x658

   __DATA_CONST.__got: 0x148
   __DATA_CONST.__mod_init_func: 0x248
   __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0xc200
+  __DATA_CONST.__const: 0xc278
   __DATA_CONST.__kalloc_type: 0x3b40
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: F2FC6806-72F6-3B2F-A884-BE3C80E400C3
-  Functions: 3275
+  UUID: 1D89ECCD-B25E-30BE-AC79-E7B323615553
+  Functions: 3286
   Symbols:   0
-  CStrings:  4282
+  CStrings:  4300
 
CStrings:
+ "\"ANEHWDevice::Failed to validate ANE register offset %#x with expected value: %#x, read register value %#x\\n\" @%s:%d"
+ "%s: %s:      %18s %12s %10s %16s %16s %12s %10s\n"
+ "%s: %s: %3u: %#18llx %12llu %#10x %#16llx %#16llx %#12x %#10x\n"
+ "%s: %s: ANEHWDevice::Failed to validate ANE register offset %#x with expected value: %#x, read register value %#x\n"
+ "%s: %s: ANEScheduler: Releasing ANE resource. programHandle: 0x%llx surfaceId: %u resourceId: 0x%llx usageType: %u size: %llu bufferIndex: %u\n"
+ "%s: %s: ANEScheduler: unwireResourceQueue is empty\n"
+ "%s: %s: All resources are already cached\n"
+ "%s: %s: Move resource with id %llx to unwire queue in case of fFirmwareTimeout/fSystemInitiatedSleep \n"
+ "%s: %s: RTBuddy endpoint panic handler, IsApPanicked %d\n"
+ "%s: %s: RTBuddy endpoint panic handler, No action, AP panicked"
+ "%s: %s: fUnwireResourceQueue->isEmpty() %d\n"
+ "%s: %s: i:%d, windowIndex: %u, usageType: 0x%x, score: %u, windowScore[%u]: %u\n"
+ "%s: %s: numCachedResources: %u cachedWiredMemorySize: 0x%x\n"
+ "%s: %s: process bufferCache freeCount: %u programHandle: 0x%llx\n"
+ "%s: %s: programId: %u, processId: %u, iopDMACommand: %p, dva: 0x%llx usageType: 0x%x pVisibleMemory %p\n"
+ "%s: %s: trying to freeup dart Space for size: %zu for usageType: 0x%x\n"
+ "%s: %s: trying to freeup dart Space for usageType: 0x%x, size: %lluK, with requested size: %zuK, programHandle: 0x%llx, numWindowsNeeded: %u, retries: %u\n"
+ "%s: %s: usageType: 0x%x, pendingRequestsWithFirmware: %u, score: %d\n"
+ "%s: %s: usageType: 0x%x, programResource: %p, programId: %u, programHandle: 0x%llx, pendingUpdate: %d pendingRequestsWithFirmware: %u, score: %d\n"
+ "%s: %s: usageType: 0x%x, programResource: %p, programId: %u, programHandle: 0x%llx, pendingUpdate: %d, pendingRequestsWithFirmware: %u, score: %d\n"
+ "%s: %s: usageType: 0x%x, programResource: %p, programId: %u, programHandle: 0x%llx, pendingUpdate: %d, same as requested programResource, buffer:programHandle: 0x%llx, clientBufferType: %d, score: %d\n"
+ "%s: %s: usageType: 0x%x, programResource: %p, programId: %u, programHandle: 0x%llx, pendingUpdate: %d, score: %d, same as requested programResource\n"
+ "%s: %s: usageType: 0x%x, same as requested intermediateUnion, buffer:programHandle: 0x%llx\n"
+ "%s: %s: usageType: 0x%x, score: %d\n"
+ "%s: %s: usageType: 0x%x, score: %d, refCount: %lu\n"
+ "[ERROR] %s: %s: Failed syncWithUnwireThread. result: 0x%x ResourceID: 0x%llx programHandle: 0x%llx usageType: %u surfaceId: %u symbolIdx: %u bufferIndex: %u\n"
+ "[ERROR] %s: %s: Failed to unwire ANE resource. programHandle: 0x%llx surfaceId: %u resourceId: 0x%llx usageType: %u size: %llu bufferIndex: %u\n"
+ "[ERROR] %s: %s: Invalid input symbol index: %u. Total inputs for model: %u\n"
+ "[ERROR] %s: %s: Invalid output symbol index: %u. Total outputs for model: %u\n"
+ "[ERROR] %s: %s: Process invalid after disable dynamic power gating programHande: 0x%llx. programId: %d, processId: %d\n"
+ "[ERROR] %s: %s: ResourceId: 0x%llx still in flight for unwiring\n"
+ "[ERROR] %s: %s: Timed out waiting for resource to be unwired programHandle: 0x%llx surfaceId: %u resourceId: 0x%llx usageType: %u size: %llu bufferIndex: %u\n"
+ "[ERROR] %s: %s: aotProgramHandle: 0x%llx not found\n"
+ "[ERROR] %s: %s: syncWithUnwireThread failed as ANE is off. result: 0x%x\n"
+ "aProgramHandle"
+ "bProgramHandle"
+ "syncWithUnwireThread"
+ "unwireThreadFunction"
+ "updateLastActivityTime"
- "\"ANEHWDevice::Failed to validate ANE register offset %x with value: %x\\n\" @%s:%d"
- "%s: %s:      %18s %12s %10s %10s %10s\n"
- "%s: %s: %3u: %#18llx %12llu %#10x %#10x %#10x\n"
- "%s: %s: ANEHWDevice::Failed to validate ANE register offset %x with value: %x\n"
- "%s: %s: RTBuddy endpoint panic handler\n"
- "%s: %s: clientBufferType:  0x%x\n"
- "%s: %s: i:%d, windowIndex: %u, score: %u, windowScore[%u]: %u, for programHandle: 0x%llx\n"
- "%s: %s: numCachedResources: %u\n"
- "%s: %s: programId: %u, processId: %u, iopDMACommand: %p, dva: 0x%llx pVisibleMemory %p\n"
- "%s: %s: trying to freeup dart Space for size: %zu for usageType: %d\n"
- "%s: %s: trying to freeup dart Space for usageType: %d, size: %lluK, with requested size: %zuK, programHandle: 0x%llx, numWindowsNeeded: %u, retries: %u\n"
- "%s: %s: usageType: %d\n"
- "%s: %s: usageType: %d, pendingRequestsWithFirmware: %u, score: %d\n"
- "%s: %s: usageType: %d, programResource: %p, programId: %u, programHandle: 0x%llx, pendingUpdate: %d\n"
- "%s: %s: usageType: %d, same as requested intermediateUnion, buffer:programHandle: 0x%llx\n"
- "%s: %s: usageType: %d, same as requested programResource, buffer:programHandle: 0x%llx\n"
- "%s: %s: usageType: %d, same as requested programResource, buffer:programHandle: 0x%llx, clientBufferType: %d\n"
- "%s: %s: usageType: %d, score: %d, refCount: %lu\n"
- "ANEHWDevice: Releasing ANE resource. programHandle: 0x%llx surfaceId: %u resourceId: 0x%llx usageType: %u size: %llu bufferIndex: %u\n"
- "ANEHWDevice: unwireResourceQueue is empty\n"
- "[ERROR] %s: %s: LiveinParam map() failed. result: 0x%x\n"

```
