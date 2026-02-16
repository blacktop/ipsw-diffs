## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

```diff

-5.311.0.0.0
-  __TEXT.__const: 0xa238
-  __TEXT.__cstring: 0x19212
-  __TEXT.__os_log: 0x154d3
-  __TEXT_EXEC.__text: 0xa3698
+5.401.2.0.0
+  __TEXT.__const: 0xa1b0
+  __TEXT.__cstring: 0x1989e
+  __TEXT.__os_log: 0x1589c
+  __TEXT_EXEC.__text: 0x9a51c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x4f0
   __DATA.__bss: 0x1f8
-  __DATA_CONST.__auth_got: 0x840
+  __DATA_CONST.__auth_got: 0x858
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x196d0
+  __DATA_CONST.__const: 0x19770
   __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: F1D3161B-62E9-33DB-A227-3E10F5707FFE
-  Functions: 1785
+  UUID: 14792113-8062-3005-8A85-4D8907772B91
+  Functions: 1817
   Symbols:   0
-  CStrings:  3225
+  CStrings:  3255
 
CStrings:
+ "\"TB_FATAL: \" \"invalid result returned from endStrobeAck\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from exclaveIspHardwareIrq\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from forceCleanup\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from forceReset\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from ispEngineDirtyOff\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from ispEngineOff\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from ispEngineOn\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from notifyFirmwareTearDown\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from prepareToStrobeAck\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from queryChannelIndex\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from readNvmData\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from secureM3Isr\" @%s:%d"
+ "AppleH16CamIn:%s - Couldn't add isp strobe control upcall notify event source to exclave work loop\n"
+ "AppleH16CamIn:%s - Registering exclave isp upcall for strobe control notify failed\n"
+ "AppleH16CamIn:%s - Registering exclave isp upcall for strobe control with notification Id: %u\n"
+ "AppleH16CamIn:%s - Setting up exclave isp upcall for strobe control notify event source failed\n"
+ "AppleH16CamIn:%s - [Exclave] SendCmdEndStrobeAck returned 0x%x, result = 0x%x\n"
+ "AppleH16CamIn:%s - [Exclave] SendCmdPrepareStrobeAck returned 0x%x, result = 0x%x\n"
+ "ECAsyncNotifyRegister"
+ "ECEndStrobeAck"
+ "ECPrepareToStrobeAck"
+ "exclaveIspStrobeControlNotificationHandler"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_endstrobeack__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{exclavecoreispeng_ispengineexclavecore_preparetostrobeack__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"

```
