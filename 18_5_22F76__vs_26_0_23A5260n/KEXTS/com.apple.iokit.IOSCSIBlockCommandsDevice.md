## com.apple.iokit.IOSCSIBlockCommandsDevice

> `com.apple.iokit.IOSCSIBlockCommandsDevice`

```diff

-500.120.2.0.0
-  __TEXT.__cstring: 0x69e
-  __TEXT_EXEC.__text: 0xbaa8
+529.0.0.0.2
+  __TEXT.__cstring: 0xef8
+  __TEXT_EXEC.__text: 0xdbc8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2a8
+  __DATA.__data: 0x2a9
   __DATA.__common: 0x98
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__kalloc_type: 0x3c0
-  UUID: E1915E26-A2CF-3A52-A4F7-28A7D8AA1A66
-  Functions: 281
+  UUID: C34C81F0-D1E9-3622-AE9C-81766F4080D3
+  Functions: 288
   Symbols:   0
-  CStrings:  71
+  CStrings:  121
 
CStrings:
+ "1222222122"
+ ">"
+ "ClearNotReadyStatus"
+ "CumUnmapLatency"
+ "HWError"
+ "HandlePowerChange"
+ "IOMinimumSaturationByteCount"
+ "IOPMResetPowerStateOnWake"
+ "LastRdError"
+ "LastWrError"
+ "LinkRetrain"
+ "MaxPowCNRSLatency"
+ "MaxPowerIOWaitLatency"
+ "MaxPowerOffLatency"
+ "MaxPowerOnLatency"
+ "MaxPowerVMPLatency"
+ "MaxUnmapBlkDescCount"
+ "MaxUnmapLBACount"
+ "MediaOfflineTS"
+ "MediaOnlineTS"
+ "MediumError"
+ "PowerEventError"
+ "PowerEventLatencyLog"
+ "PowerEventLog"
+ "PowerEventTS"
+ "RdWrErrors"
+ "RdWrXferMismatch"
+ "SCSIBusyTaskStatus"
+ "UnmapCount"
+ "UnmapDescCount"
+ "UnmapLBACount"
+ "VerifyMediumPresence"
+ "[%s:%s] [%s]: ClearNotReadyStatus error\n"
+ "[%s:%s] [%s]: ClearNotReadyStatus failed or took long; result %d, duration %llu sec, status 0x%llx\n"
+ "[%s:%s] [%s]: ClearNotReadyStatus in progress for %llu sec, service response 0x%x, task status 0x%x, valid Sense %d; sense data 0x%02X/0x%02X/0x%02X ...\n"
+ "[%s:%s] [%s]: ClearPowerOnReset error\n"
+ "[%s:%s] [%s]: Could not send TEST_UNIT_READY to device; service response 0x%X, task status 0x%X; exiting ClearNotReadyStatus.\n"
+ "[%s:%s] [%s]: Done; CurrentPowerState %d ProposedPowerState %d isPMAborted %d isInactive %d\n"
+ "[%s:%s] [%s]: START_STOP_UNIT [1] error! serviceResponse 0x%x TaskStatus 0x%x\n"
+ "[%s:%s] [%s]: Scheduling PM abort thread\n"
+ "[%s:%s] [%s]: Stop verify media presense check; PM abort %d isInactive %d\n"
+ "[%s:%s] [%s]: Verify Medium in progress for %llu sec, service response 0x%x, task status 0x%x, valid Sense %d; sense data 0x%02X/0x%02X/0x%02X ...\n"
+ "[%s:%s] [%s]: Verify Medium took long or failed; Verify Medium status 0x%llx\n"
+ "[%s:%s] [%s]: [ %ld => %ld ] : waiting for commands to complete: %llu, %llu\n"
+ "[%s:%s] [%s]: [ %ld => %ld ] Wait time exceeded for outstanding commands, PM aborted %d Exiting ...\n"
+ "[%s:%s] [%s]: drive READY, media present, sense data 0x%02X/0x%02X/0x%02X\n"
+ "[%s:%s] [%s]: drive READY, sense data 0x%02X/0x%02X/0x%02X\n"
+ "[%s:%s] [%s]: serviceResponse 0x%x taskStatus 0x%x START_STOP_UNIT [0] error!"
+ "[%s:%s] [%s]: serviceResponse 0x%x taskStatus 0x%x START_STOP_UNIT [1] error!"
+ "[%s:%s] [%s]: stop medium capacity checks; PM abort %d isInactive %d\n"
+ "[%s::AbortPMTransition] [%s] Ack power event\n"
+ "[%s::AbortPMTransition] [%s] Could not complete power transition %u to %u...terminating\n"
+ "[%s::AbortPMTransition] [%s] HandlePowerChange ack-ed power event\n"
+ "[%s::AbortPMTransition] [%s] Terminate \n"
+ "[%s]: I/O error [0x%x] dir 0x%x lba 0x%llx count 0x%llx, retry %d ...\n"
+ "force-smart"
+ "scsi-smart"
- "12222221"
- "CNRS failed for %d iterations. Invalid Sense.\n"
- "CNRS failed for %d iterations. SenseKey = %u, ASC = %u, ASCQ = %u\n"
- "HandlePowerChange-Error"
- "SBC Transition took too long, terminating.\n"
- "SBC: CNRS failed\n"
- "SBC: CPOR failed\n"

```
