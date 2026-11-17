## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-10.203.200.0.0
-  __TEXT.__const: 0x1300
-  __TEXT.__cstring: 0x13e6c
-  __TEXT.__os_log: 0x4463a
-  __TEXT_EXEC.__text: 0x16e04c
-  __TEXT_EXEC.__auth_stubs: 0x12d0
+10.205.3.0.0
+  __TEXT.__const: 0x1340
+  __TEXT.__cstring: 0x141df
+  __TEXT.__os_log: 0x455cb
+  __TEXT_EXEC.__text: 0x1720e8
+  __TEXT_EXEC.__auth_stubs: 0x1300
   __DATA.__data: 0x54f4
   __DATA.__common: 0x558
   __DATA_CONST.__mod_init_func: 0x330
   __DATA_CONST.__mod_term_func: 0x140
-  __DATA_CONST.__const: 0x104e8
+  __DATA_CONST.__const: 0x10718
   __DATA_CONST.__kalloc_type: 0x7900
   __DATA_CONST.__kalloc_var: 0x9ab0
-  __DATA_CONST.__auth_got: 0x968
+  __DATA_CONST.__auth_got: 0x980
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 5260
+  Functions: 5337
   Symbols:   0
-  CStrings:  6038
+  CStrings:  6115
 
CStrings:
+ " Processes resident in firmware = %u (reserve %u)\n"
+ " Programs resident in firmware = %u (reserve %u)\n"
+ "%s: %s:  Processes resident in firmware = %u (reserve %u)\n"
+ "%s: %s:  Programs resident in firmware = %u (reserve %u)\n"
+ "%s: %s: ANE%u: Exclave mode already active, dropping the pending restore\n"
+ "%s: %s: ANE%u: ignoring firmware RTGraph support on H13\n"
+ "%s: %s: Deferring request (priority %u): lower-priority request (priority %u, UUID 0x%llx) has been executing for %u ms — starvation threshold exceeded. Further deferrals to this request are counted, not logged\n"
+ "%s: %s: Ended %u exclave perf work item(s) left outstanding at teardown\n"
+ "%s: %s: Ended %u started exclave perf work item(s) at ANE power-off\n"
+ "%s: %s: Exclave perf work upcall handlers registered\n"
+ "%s: %s: Exclave retry timer: not armed, stopping\n"
+ "%s: %s: Exclave retry timer: verdict=complete, all pending destroys resolved, stopping\n"
+ "%s: %s: Exclave retry timer: verdict=retry cacheHandle=0x%llx, re-arming\n"
+ "%s: %s: Firmware slot pressure on ANE%u: programs %u/%u, processes %u/%u free, no idle process to reclaim\n"
+ "%s: %s: No %s slot free on deviceId %u and none reclaimable; letting programHandle 0x%llx through to fail\n"
+ "%s: %s: No %s slot free on deviceId %u; holding programHandle 0x%llx pending until one is reclaimed\n"
+ "%s: %s: No firmware program slot free; leaving programHandle 0x%llx unprepared until first inference\n"
+ "%s: %s: No firmware slot free; leaving instance 0x%llx unprepared until first inference\n"
+ "%s: %s: Not escalating timed-out request uuid: 0x%llx - firmware timeout recovery unsupported on this product\n"
+ "%s: %s: Not escalating timed-out request uuid: 0x%llx - other requests are still executing on its ANEs\n"
+ "%s: %s: Reclaiming firmware slots on ANE%u from ResourceID: 0x%llx (idle longest)\n"
+ "%s: %s: WorkBegin upcall: request 0x%llx exclaveTs %llu slot %llu\n"
+ "%s: %s: WorkEnd (op %llu): request 0x%llx slot %llu started %d\n"
+ "%s: %s: WorkSubmit upcall: request 0x%llx tdCount %u priority %u qos 0x%x exclaveTs %llu slot %llu accepted %d\n"
+ "%s: %s: [%s] machoPath=\"%s\"\n"
+ "%s: %s: [%s] machoSize=%llu totalProgramSize=%llu isRTGraph=%d loaderPid=%d loaderStartTime=%llu signingId=%s..\n"
+ "%s: %s: [%s] programHandle=0x%llx ident=\"%s\" modelIdent=\"%s\"\n"
+ "%s: %s: [%s] uuid=0x%llx has no program resource - program identity unavailable\n"
+ "%s: %s: [%s] uuid=0x%llx submittedBy=\"%s\" pid=%d procedure=\"%s\" procedureId=%u priority=%u qos=%u timeoutMs=%u starvationDeferrals=%llu\n"
+ "%s: %s: enterShutdown: Exclave shutdown sweep complete after %u poll(s)\n"
+ "%s: %s: exitSimulatedShutdown: clearing shutdownInProgress\n"
+ "%s: %s: fFWSupportsRTGraph seeded to %s for cpu_subtype %d\n"
+ "%s: %s: notifyExclaveShutdownStarted: verdict=complete\n"
+ "%s: %s: notifyExclaveShutdownStarted: verdict=inProgress (timeoutMs=%u)\n"
+ "%s: %s: process slot release with no counted create; count already zero\n"
+ "%s: %s: program slot release with no counted load; count already zero\n"
+ "11122211222222111111222213332233322333223332222222222222222222222222222222222222222222222222222222122222111122222222222222222222222222222221111111111211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122222222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122222122212222222222222221122222222222222"
+ "121111222222222222222122222222222222212222222222222221222222222222222211110111101111122122112212212112111111211111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221221222212212212212212212212"
+ "222222222222222222211112121222222222222222222222222222222222222222122"
+ "<none>"
+ "<unknown>"
+ "ANEDriverECCmdHandleExclaveRetry"
+ "ANEDriverECCmdStartShutdown"
+ "B32@?0Q8Q16Q24"
+ "[ERROR] %s: %s: ANE%u: in-flight Exclave mode switch did not complete: 0x%x\n"
+ "[ERROR] %s: %s: Escalating timed-out request uuid: 0x%llx to firmware timeout recovery - nothing else is executing on residency 0x%x\n"
+ "[ERROR] %s: %s: Exclave perf work table full; request 0x%llx not reported to CLPC: 0x%x\n"
+ "[ERROR] %s: %s: Exclave perf work upcall registration failed: 0x%x\n"
+ "[ERROR] %s: %s: Exclave perf work upcall registration failed: submit 0x%x begin 0x%x end 0x%x\n"
+ "[ERROR] %s: %s: Exclave retry timer: DOWNCALL failed (0x%x), re-arming\n"
+ "[ERROR] %s: %s: Failed to allocate exclave perf work lock: 0x%x\n"
+ "[ERROR] %s: %s: Failed to prepare process - 0x%llx result: 0x%x\n"
+ "[ERROR] %s: %s: Failed to take power assertion to reclaim firmware slots. result: 0x%x\n"
+ "[ERROR] %s: %s: Failed to unprepare ResourceID: 0x%llx result: 0x%x\n"
+ "[ERROR] %s: %s: MachO carries an RTGraph section but firmware on this product does not support RTGraph - rejecting program create\n"
+ "[ERROR] %s: %s: No deviceInterface for ANE%u while escalating uuid: 0x%llx\n"
+ "[ERROR] %s: %s: Range already wired for SK refId=0x%llx offset=0x%llx size=0x%llx\n"
+ "[ERROR] %s: %s: Tile regions exceed surface: surfaceID=%u planeIdx=%u dataOffset=0x%x dataSize=0x%x metaOffset=0x%x metaSize=0x%x surfaceSize=0x%llx\n"
+ "[ERROR] %s: %s: Tile regions outside plane: surfaceID=%u planeIdx=%u planeOffset=0x%llx planeSize=0x%x headerOffset=0x%llx dataOffset=0x%llx\n"
+ "[ERROR] %s: %s: enterShutdown: Exclave shutdown sweep still pending after %u polls, proceeding\n"
+ "[ERROR] %s: %s: notifyExclaveShutdownStarted: startShutdown downcall failed (0x%x)\n"
+ "[ERROR] %s: %s: vnode_get failed (err=%d) for SK refId=0x%llx\n"
+ "[ERROR] %s: %s: vnode_ref failed (err=%d) for SK refId=0x%llx\n"
+ "aneExclaveRetryTimerFired_block_invoke"
+ "aneExclaveWorkBeginUpcall"
+ "aneExclaveWorkSubmitUpcall"
+ "aneProcessSlotReserve"
+ "aneProgramSlotReserve"
+ "dumpIdentity"
+ "dumpOwnerIdentity"
+ "endAllExclavePerfWork"
+ "endExclavePerfWorkForRequest"
+ "endStartedExclavePerfWork_gated"
+ "escalateTimedOutRequestToFirmwareRecovery"
+ "exclaveUnwireMemory"
+ "exclaveWireMemory"
+ "exitSimulatedShutdown"
+ "firmwareRecoveryEscalation"
+ "firmwareSlotsAvailableForProcess"
+ "pollExclaveShutdownUntilComplete"
+ "program and process"
+ "reclaimFirmwareSlotsOnDevice"
+ "registerExclavePerfWorkUpcalls"
+ "releaseProcessSlotCount"
+ "releaseProgramSlotCount"
+ "seedRTGraphSupport"
+ "starvationBlocker"
+ "v24@?0{aneexclave_aneexclaveretryverdict_s=Q(?={?=Q})}8"
+ "v24@?0{aneexclave_aneexclaveshutdownverdict_s=Q(?={?=I})}8"
- "%s: %s: Deferring request (priority %u): lower-priority request (priority %u, UUID 0x%llx) has been executing for %u ms — starvation threshold exceeded\n"
- "%s: %s: ERROR: ANEHWDevice: Exceeded max number of programs loaded on ANE - fANEMaxPrograms=%d \n"
- "%s: %s: enterShutdown: Exclave shutdown sweep did not converge within %ums, proceeding anyway (%u device(s) still pending)\n"
- "%s: %s: enterShutdown: no Exclave shutdown sweep pending on any device, skipping wait\n"
- "%s: %s: notifyExclaveShutdownStarted: startShutdown downcall not available on this SDK tbmodule\n"
- "1112221122222211111122221333223332233322333222222222222222222222222222222222222222222222222222222212222211112222222222222222222222222222222111111111121122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112221122211222112222222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212222212221222222222222221122222222222222"
- "1211112222222222222221222222222222222122222222222222212222222222222222111101111011111221221122122121121111112111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221221222212212212212212212212"
- "2222222222222222222111121212222222222222222222222222222222222222122"
- "[ERROR] %s: %s: Failed to prepare process - 0x%llx \n"
- "[ERROR] %s: %s: Max process count reached (%d) - Cannot create anymore\n"
- "[ERROR] %s: %s: enterShutdown: waitForExclaveShutdownSweepToConverge sleep failed (0x%x)\n"
- "waitForExclaveShutdownSweepToConverge"
```
