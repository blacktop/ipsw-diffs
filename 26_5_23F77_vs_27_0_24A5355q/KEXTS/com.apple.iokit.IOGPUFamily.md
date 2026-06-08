## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-130.14.0.0.0
-  __TEXT.__cstring: 0x5e27
-  __TEXT.__os_log: 0x4bbf
-  __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x3f9b4
+162.5.0.0.0
+  __TEXT.__cstring: 0x616e
+  __TEXT.__os_log: 0x521d
+  __TEXT.__const: 0x8c
+  __TEXT_EXEC.__text: 0x41d4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x898
   __DATA.__bss: 0x9
-  __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x6f80
+  __DATA_CONST.__const: 0x6fd0
   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0x1090
-  __DATA_CONST.__assert: 0xa0
-  UUID: 77CCB658-4E6A-30BD-83E9-5EB437305A07
-  Functions: 1982
+  __DATA_CONST.__assert: 0x28
+  __DATA_CONST.__auth_got: 0x6e0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x8
+  UUID: 508851A8-19FE-34DC-A92D-845C688DAD1E
+  Functions: 1997
   Symbols:   0
-  CStrings:  878
+  CStrings:  916
 
CStrings:
+ "\"%s: 0x%X mapping is not valid for wireRange, cannot unwire PTEs\" @%s:%d"
+ "\"%s: 0x%X mapping is not valid for wireRange, cannot wire PTEs\" @%s:%d"
+ "\"Memory object must be Resident\" @%s:%d"
+ "\"Memory object not found in fMemoryCountedSet or fPendingMemorySet\" @%s:%d"
+ "\"Timeout MTLEvent: waiting for signal (%llu) for event (%u) to be scheduled\" @%s:%d"
+ "\"Timeout SharedEvent: %s: Shared event wait timed out for value : %llx\" @%s:%d"
+ "\"Timeout SharedEvent: Cmd queue %p sleep port_name %d value: %08llx timed out waiting for prior signals!\" @%s:%d"
+ "\"Timeout SharedEvent: Cmd queue %p sleep port_name %d value: %08llx timed out!\" @%s:%d"
+ "\"Unable to remove just added resource after addMemoryFromResources failure\" @%s:%d"
+ "\"Unexpected pending memory objects\" @%s:%d"
+ "%s <%s> (%p) : required > max : requiredBytes = <%llu> preparedBytes : <%llu> maxWired = <%llu> maxWiredInternal = <%llu> currentWired = <%llu>\n"
+ "%s <%s> FAILED To Free, should return error: <0x%X> total accelerator = 0x%llX max = 0x%llX\n"
+ "%s <%s>: preparedBytes != requiredBytes : preparedBytes = <%llu> requiredBytes = <%llu> maxWired = <%llu> preWiring = <%llu> currentWired = <%llu> wiring delta = <%llu>\n\n"
+ "%s <%s>: requiredBytes = <%llu> maxWired = <%llu> preparedBytes : <%llu> remainingBytes : <%lld> remainingPages = <%lld>\n\n"
+ "%s fMaxSingleSysMemoryPercent = %u fMaxSysMemoryWiredSize[API] = %llu fMaxSingleSysMemory = %llu\n"
+ "%s maxSingleSysMemoryPercent override = %u\n"
+ "%s maxSysMemoryWiredSizeAPI override = %llu\n"
+ "%s null device\n"
+ "%s null queue\n"
+ "%s waitForEventTimeoutSeconds = %u\n"
+ "%s: Failed to set purgeable state 0x%x\n"
+ "%s: GARTReclaimInterval set to non default value (%u) milisec\n"
+ "%s: GARTReclaimTimeout set to non default value (%u) milisec\n"
+ "%s: failed to create rw Lock\n"
+ "%s: failed to create sleep lock\n"
+ "%s: failed to map memory for CPU wire mapping\n"
+ "%s: failed to prepare memory status = 0x%X\n"
+ "12111111212112222222222111122211122222111112111222222111122212222122222221"
+ "12111111222122222222222212200000"
+ "121111121222121212111111121211121222221111112112211122111112122222222222222222222222222122212"
+ "121112211122"
+ "1211212112111122222222222222222222122222"
+ "121121211211112222222222222222222212222211121120"
+ "12122222212111222112121112221"
+ "12122222222222222222221112222121222222"
+ "12122222222222222222222"
+ "122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222211111112222222222222222212111222222211222222222"
+ "2222222211112"
+ "MTLEvent: timed out but sleep started after deadline <%llu>. This is a real timeout\n"
+ "MTLEvent: timed out while waiting, GPU is not up yet\n"
+ "MTLEvent: timed out while waiting, GPU is up now, extending deadline by <%llu>\n"
+ "MTLEvent: timed out while waiting. Sleep/wake occurred while waiting. Extend deadline by <%llu>\n"
+ "MTLEvent: while waiting, sleep occurred, but woken up from an unknown event <%d>\n"
+ "OSPtr<IOMemoryMap> IOGPUSysMemory::retainCPUWireMapping(IOOptionBits)"
+ "Timeout MTLEvent: waiting for signal (%llu) for event (%u) to be scheduled\n"
+ "aborted"
+ "iogpu_disable_restart_limit"
+ "iogpu_event_timeout_secs"
+ "iogpu_gart_interval_ms"
+ "iogpu_gart_timeout_ms"
+ "iogpu_no_abort"
+ "iogpu_no_check_descriptor_size"
+ "iogpu_no_prepare_avoid_throttling"
+ "iogpu_no_throttled_multi_kick"
+ "iogpu_panic_on_event_timeout"
+ "iogpu_single_sysmem_pct"
+ "iogpu_sysmem_mb"
+ "virtual void IOGPUSysMemory::unwire()"
+ "void IOGPU::terminateQueues()"
+ "void IOGPUResource::setPurgeable(IOOptionBits, IOOptionBits)"
- "\"Memory object unexpectedly not found in fMemoryCountedSet\" @%s:%d"
- "\"Memory object unexpectedly not found in fPendingMemorySet\" @%s:%d"
- "%s: This command buffer is nopped\n"
- "%s: failed to prepare memory\n"
- "(numMemoryHashResourcesAdded + numPendingHashResourcesAdded) <= countOfObjectsToAdd"
- "1211111121211222222222211112221112222211111211122222211112221222212222"
- "12111111222122202222222221200000"
- "121111121222121212111111121211121222221111112112211122111112212222222222222222222222221222122"
- "1211122211122"
- "121121121"
- "12112121121111222222222222222222221222"
- "121121211211112222222222222222222212221112112"
- "121222222121112221121211122"
- "1212222222222222222222"
- "121222222222222222222211122221221222222"
- "12222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222111111122222222222222222121112222222211"
- "2222222211211"
- "i == (numMemoryHashResourcesAdded + numPendingHashResourcesAdded)"
- "iogpu_boost_cpu_priority"
- "removedResource == addedResources[i]"
- "result != kIOReturnSuccess"
- "result == kIOReturnSuccess"

```
