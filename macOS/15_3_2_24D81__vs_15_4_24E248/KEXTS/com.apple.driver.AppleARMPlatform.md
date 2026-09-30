## com.apple.driver.AppleARMPlatform

> `com.apple.driver.AppleARMPlatform`

```diff

-1066.60.6.0.0
-  __TEXT.__const: 0x1768
-  __TEXT.__os_log: 0x1416
-  __TEXT.__cstring: 0xcab2
-  __TEXT_EXEC.__text: 0x54984
+1066.100.11.0.0
+  __TEXT.__const: 0x1778
+  __TEXT.__os_log: 0x14f3
+  __TEXT.__cstring: 0xcb7b
+  __TEXT_EXEC.__text: 0x56020
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
   __DATA.__common: 0xca0
   __DATA.__bss: 0x69
-  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x128
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0x24008
+  __DATA_CONST.__const: 0x24000
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__kalloc_type: 0x1540
-  UUID: 8EA440EC-11DD-3D8A-9D13-21E22E62434B
-  Functions: 2122
-  Symbols:   3552
-  CStrings:  1684
+  UUID: 7E4C86DB-8979-3B59-9B1E-4D12030139DD
+  Functions: 2137
+  Symbols:   3581
+  CStrings:  1696
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _ZN16AppleARMNORNVRAM5startEP9IOService.cold.1
+ _ZN26AppleARMSPIFlashController10readBufferEPhyy.cold.1
+ _ZN26AppleARMSPIFlashController10readBufferEPhyy.cold.2
+ _ZN26AppleARMSPIFlashController10writeBytesEPKhyy.cold.1
+ _ZN26AppleARMSPIFlashController10writeBytesEPKhyy.cold.2
+ _ZN26AppleARMSPIFlashController10writeBytesEPKhyy.cold.3
+ _ZN26AppleARMSPIFlashController11_eraseBlockEj.cold.1
+ _ZN26AppleARMSPIFlashController11writeBufferEPKhyy.cold.1
+ _ZN26AppleARMSPIFlashController11writeBufferEPKhyy.cold.2
+ _ZN26AppleARMSPIFlashController11writeBufferEPKhyy.cold.3
+ _ZN26AppleARMSPIFlashController11writeBufferEPKhyy.cold.4
+ _ZN26AppleARMSPIFlashController12_eraseSectorEj.cold.1
+ _ZN26AppleARMSPIFlashController13_programBytesEPKhyy.cold.1
+ _ZN26AppleARMSPIFlashController15_readBufferQuadEPhyy.cold.1
+ _ZN26AppleARMSPIFlashController15_readBufferQuadEPhyy.cold.2
+ _ZN26AppleARMSPIFlashController16_programBytesSSTEPKhyy.cold.1
+ _ZN26AppleARMSPIFlashController17_programBytesQuadEPKhyy.cold.1
+ _ZN26AppleARMSPIFlashController9eraseAreaEyy.cold.1
+ _ZN26AppleARMSPIFlashController9eraseAreaEyy.cold.2
+ _ZN26AppleARMSPIFlashController9eraseAreaEyy.cold.3
+ _ZN9MCCommand6createEP18memcache_cmd_entryb.cold.1
+ __ZZN12MCDataStreamdlEPvmE20kalloc_type_view_248
+ __ZZN12MCDataStreamnwEmE20kalloc_type_view_248
+ __ZZN22AppleARMSPMIController17logNewSPMICommandEP19AppleARMSPMICommandE11_os_log_fmt
+ __ZZN22AppleARMSPMIController17logNewSPMICommandEP19AppleARMSPMICommandE11_os_log_fmt_0
+ __ZZN22AppleARMSPMIController20logFinishSPMICommandEP19AppleARMSPMICommandiE11_os_log_fmt
+ __ZZN22AppleARMSPMIController20logFinishSPMICommandEP19AppleARMSPMICommandiE11_os_log_fmt_0
+ __ZZN22AppleARMSPMIController20logFinishSPMICommandEP19AppleARMSPMICommandiE11_os_log_fmt_1
+ __ZZN22AppleARMSPMIController8copyLogsEPvPjS1_E11_os_log_fmt
+ _os_log_create
- _ZN16VictimUserClient8addFreqsEPjP20IOSACVictimFrequency.cold.1
- _ZN16VictimUserClient8addFreqsEPjP20IOSACVictimFrequency.cold.2
- _ZN17AppleARMBacklight5startEP9IOService.cold.1
- _ZN17AppleARMBacklight5startEP9IOService.cold.2
- _ZN20AppleARMPWMBacklight5startEP9IOService.cold.1
- _ZN20AppleARMPWMBacklight5startEP9IOService.cold.2
- _ZN29AppleARMPerformanceController31initVoltageAndPerformanceStatesEv.cold.3
- _ZN29AppleARMPerformanceController31initVoltageAndPerformanceStatesEv.cold.4
- __ZZN12MCDataStreamdlEPvmE20kalloc_type_view_236
- __ZZN12MCDataStreamnwEmE20kalloc_type_view_236
CStrings:
+ "%s: no mask supplied\n"
+ "%s: updated log mask to: %08x\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleARMPlatform/AppleARMSPMI.cpp"
+ "112122111111111111111111111111111111111111111111111111111111111111111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221"
+ "121111121222121211111222121111121"
+ "1211111212221212112121111111111111111111111211111111111111111111111111111111111111111111111111111111111111111111111111212112121"
+ "[%s]:%s:%d: %s"
+ "[%s]:%s:%d: CmdEnd[%d], %X - %s 0x%04x - #%x %uus\n"
+ "[%s]:%s:%d: CmdEnd[%d], %X - %s 0x%04x - #%x %uus, 0x%08x\n"
+ "[%s]:%s:%d: CmdStart[%d], %X - %s 0x%04x - #0x%x\n"
+ "[%s]:%s:%d: Copied %d entries\n"
+ "com.apple.spmi"
+ "copyLogs"
+ "logFinishSPMICommand"
+ "logNewSPMICommand"
+ "spmi.driver"
- "%s"
- "%s: CmdEnd[%d], %X - %s 0x%04x - #%x %uus\n"
- "%s: CmdEnd[%d], %X - %s 0x%04x - #%x %uus, 0x%08x\n"
- "%s: CmdStart[%d], %X - %s 0x%04x - #0x%x\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleARMPlatform/AppleARMSPMI.cpp"
- "112122111111111111111111111111111111111111111111111111111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221"
- "12111112122212121111122211211112"
- "1211111212221212112121111111111111111111111211111111111111111111111111111111111111111111111111111111111111212112121"
- "Copied %d entries\n"

```
