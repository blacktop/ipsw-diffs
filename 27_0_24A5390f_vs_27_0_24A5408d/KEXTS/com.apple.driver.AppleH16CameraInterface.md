## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-6.14.1.0.0
+6.18.0.0.0
   __TEXT.__const: 0xa1b0
-  __TEXT.__cstring: 0x19947
-  __TEXT.__os_log: 0x15914
-  __TEXT_EXEC.__text: 0x9b0ac
-  __TEXT_EXEC.__auth_stubs: 0x10d0
+  __TEXT.__cstring: 0x19f97
+  __TEXT.__os_log: 0x15bb4
+  __TEXT_EXEC.__text: 0x9cd20
+  __TEXT_EXEC.__auth_stubs: 0x10e0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x4f0
   __DATA.__bss: 0x1f8
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x19770
+  __DATA_CONST.__const: 0x197d0
   __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0xa50
-  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__auth_got: 0x870
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 1818
+  Functions: 1822
   Symbols:   0
-  CStrings:  2338
+  CStrings:  2398
 
CStrings:
+ "            ... ISP only crashlogs when it panics.\n"
+ "\"AppleH16CamIn::%s - CISP_CMDCH_ERROR_NOTIFICAITON_ERROR_SOURCE_ASYNCH_ERROR, L2C_ERR_STS(0x%x), L2C_ERR_ADR(0x%x), L2C_ERR_INF(0x%x), \t\t\t\t  MMU_ERR_STS(0x%x), LSU_ERR_STS(0x%x), LSU_ERR_CTL(0x%x), FED_ERR_STS(0x%x), FED_ERR_CTL(0x%x)\\n\" @%s:%d"
+ "AppleCameraDirtyShutdownHistory"
+ "AppleCameraDirtyShutdownStats"
+ "AppleCameraLastDirtyShutdown"
+ "AppleH16CamIn:%s - DirtyShutdown captured: type=%u cmdId=0x%x pc=0x%llx igp0=0x%x igp6=0x%x reason='%s' total=%u\n"
+ "AppleH16CamIn:%s - DirtyShutdown context: clocks=%u init=%u priorTimeout=%u(type=%u,cmd=0x%x) pwrState=%u pwrEvent=%u kclient=%u clients=%u\n"
+ "AppleH16CamIn:%s - ISP command not permitted\n"
+ "AppleH16CamIn:%s - Power-off completed (fPowerEvent=%d), proceeding with power-on\n"
+ "AppleH16CamIn:%s - Power-off did not complete within 1s (fPowerEvent=%d). Return busy\n"
+ "AppleH16CamIn:%s - couldn't allocate kernel command buffer\n"
+ "AppleH16CamIn:%s - fPowerEvent=%d (PowerOffPending), waiting for power-off to complete before power-on\n"
+ "AppleH16CamIn:%s - fPowerEvent=%d, fw timeout=%d. Return busy (firmware timeout)\n"
+ "CAT register force-idle failed"
+ "CISP_CMD_CH_ERROR_NOTIFICATION"
+ "CISP_CMD_POWER_DOWN failed"
+ "CISP_CMD_STOP failed"
+ "CISP_CMD_SUSPEND failed"
+ "CaptureDirtyShutdown"
+ "CispCmdPowerDownFailed"
+ "CispCmdStopFailed"
+ "CispCmdSuspendFailed"
+ "CmdChErrorNotification"
+ "FW cmd timeout during ISP_Init"
+ "ForceIdleFailed"
+ "FwCmdTimeoutDuringInit"
+ "FwCmdTimeout_Legacy"
+ "FwCmdTimeout_Rtbuddy"
+ "ISP CED error"
+ "ISP Firmware panic (recovered)"
+ "ISPCoredump:%s - synthesized PC from UTTDBG_PCSAMPLE: 0x%llx\n"
+ "IspCedError"
+ "IspFirmwarePanic"
+ "L2C/MMU/LSU/FED async error"
+ "L2cAsyncError"
+ "Note: ISP did not crashlog; emitting minimal dump.\n"
+ "RTKit magic key not written"
+ "RtkitMagicKeyMissing"
+ "activeClientCount"
+ "clocksAndPowerOn"
+ "cmdId"
+ "currentPowerState"
+ "driverInterface"
+ "enableFwCore"
+ "firstSeen_abs"
+ "haltedCpuPC"
+ "hasActiveKernelClient"
+ "inRamdisk"
+ "initInProgress"
+ "ispIgp0rr"
+ "ispIgp6rr"
+ "lastSeen_abs"
+ "perType"
+ "powerEvent"
+ "priorTimeoutCmdId"
+ "priorTimeoutPending"
+ "priorTimeoutType"
+ "reason"
+ "restoreMode"
+ "ringHead"
+ "sCoredumpSaveThreadState"
+ "timestamp_abs"
+ "total"
+ "type"
- "            ... ISP only coredumps when it panics.\n"
- "\"AppleH16CamIn::%s - CISP_CMDCH_ERROR_NOTIFICAITON_ERROR_SOURCE_ASYNCH_ERROR, L2C_ERR_STS(0x%x), L2C_ERR_ADR(0x%x), L2C_ERR_INF(0x%x), \t\t\t  MMU_ERR_STS(0x%x), LSU_ERR_STS(0x%x), LSU_ERR_CTL(0x%x), FED_ERR_STS(0x%x), FED_ERR_CTL(0x%x)\\n\" @%s:%d"
- "AppleCamera:%s - ISP command not permitted\n"
- "AppleH16CamIn:%s - fPowerEvent=%d, fw timeout=%d. Return busy\n"
```
