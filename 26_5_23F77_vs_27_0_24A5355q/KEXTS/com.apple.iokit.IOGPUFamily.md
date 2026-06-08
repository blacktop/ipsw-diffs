## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-130.14.0.0.0
-  __TEXT.__cstring: 0x5e27 sha256:70f3f5b950249cafd7e94b30eeb5816a3791e899685df27e9b5c27b6afe6dce2
-  __TEXT.__os_log: 0x4bbf sha256:f0116395b0a40a26f838039f2050d3291139ad1e04075c2e85260d65df46680f
-  __TEXT.__const: 0x7c sha256:96419aa1bd138c093f19968e246d0ea061d8653df52c210c4e8b2795d8752a05
-  __TEXT_EXEC.__text: 0x3f9b4 sha256:27c1ca672bc9f2b18eb3d7cec508f9a4d8885b4cf8658bf6e73358b5b39ab48f
+162.5.0.0.0
+  __TEXT.__cstring: 0x616e sha256:8b01e62bf7088de58d2461bbe7a4c97b2af7448380e4e77a4bac61f0228f28d2
+  __TEXT.__os_log: 0x521d sha256:8649be727783df18a2ea73cdf2056783cb209cf00f8876fd57f1b7094fbf3472
+  __TEXT.__const: 0x8c sha256:700087fbd09f1eb70adb9b94351edf4264a8b934295fa8264a54dcbfb15d644e
+  __TEXT_EXEC.__text: 0x41d4c sha256:59f6c7464119dcc476e313f0997e9a67e5602f683c02c9d32b52a343c32c4483
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x460 sha256:73a5cbc81e158195e6f42b7c5789659b0e8f6eebe46e0c0d59a7dc56f6ff3fa4
+  __DATA.__data: 0x460 sha256:e67c3fd3ef7185afa58978c9bbb6c38f03bb4e36bb100147ab69b6ef4584e340
   __DATA.__common: 0x898 sha256:2b63efc11f049529eb9b9876a5396ba3a5af8b73f813836efd844c114bb29834
   __DATA.__bss: 0x9 sha256:3e7077fd2f66d689e0cee6a7cf5b37bf2dca7c979af356d0a31cbc5c85605c7d
-  __DATA_CONST.__auth_got: 0x6c0 sha256:88180178b449523671ab46b3e715a2b75f0a4bc921e79b4a43df4ef210061a0a
-  __DATA_CONST.__got: 0x100 sha256:f590752dadbb777f59130dd5eba0a380f4c6e493f6ac239e82be1099c57766ea
-  __DATA_CONST.__auth_ptr: 0x8 sha256:bf6ec49501e3d3040672c70ea50ab65eaa2eef4728b3363a17ff6bb8037bd37e
-  __DATA_CONST.__mod_init_func: 0x100 sha256:0eef02e94f754be950c5f8c7734348ba088413c68d81f286a557714cf9d0e26d
-  __DATA_CONST.__mod_term_func: 0x100 sha256:3a10d3f338bdd160e0d639599971c17d309409cc36740da914b05acf45d8739b
-  __DATA_CONST.__const: 0x6f80 sha256:2a602584dc96479f1fc4f1aa407fa2854e5fc864f23ef31866d70938b9ab1e16
-  __DATA_CONST.__kalloc_type: 0x11c0 sha256:6d97b016f2f83a0c9a7bf6c52b7b9d05085424c34d00ac0e16407576296052db
-  __DATA_CONST.__kalloc_var: 0x1090 sha256:5c1bee4e841945fc474842f3fca35a7da9f8e904a932683632e25281c736eac3
-  __DATA_CONST.__assert: 0xa0 sha256:b7ce5e845e47a1afa883d12acae247218016de1ef3cf8d601818569dc9a56385
-  UUID: 77CCB658-4E6A-30BD-83E9-5EB437305A07
-  Functions: 1982
+  __DATA_CONST.__mod_init_func: 0x100 sha256:6dbd053436d5478464583710a06204180f26f0c327863e7bbfc168775216e034
+  __DATA_CONST.__mod_term_func: 0x100 sha256:d6bf5cb4f9b7adf12007363579f63cebd7b4430c003109481a5d8bec127c43b8
+  __DATA_CONST.__const: 0x6fd0 sha256:2c83c26c048dab745bc15e6bf10a4d04656496455e94993dffb1b8a223af6f14
+  __DATA_CONST.__kalloc_type: 0x11c0 sha256:1e45a1ccfac811d0ec4d9a85ec1108aef86088807a8b4b8b9f5d36620890fd14
+  __DATA_CONST.__kalloc_var: 0x1090 sha256:8527231d824773db7752a25dd055a081186826c1bde33ef7f81e5f9f1471530c
+  __DATA_CONST.__assert: 0x28 sha256:20541010a77670f2f3340924e9f8897c1607c751e4dd0fdcff31c514f61da542
+  __DATA_CONST.__auth_got: 0x6e0 sha256:24de6af7c06d7ce4807a696afc695e7d78e84dd4ad5e903637e62ca689c6b526
+  __DATA_CONST.__got: 0x100 sha256:7ab20a8a93f4f9fc169d873e402858e671482ccf429c5317afd62e447703cf40
+  __DATA_CONST.__auth_ptr: 0x8 sha256:69313162d1be749c70415fb133b7d6ddf4b4a06432cfd6e3427dc32e2fc6c519
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
