## com.apple.driver.AppleSPMI

> `com.apple.driver.AppleSPMI`

```diff

-100.0.0.0.0
+104.0.0.0.1
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x21cb
-  __TEXT_EXEC.__text: 0xa2ec
+  __TEXT.__cstring: 0x23f0
+  __TEXT.__os_log: 0xc43
+  __TEXT_EXEC.__text: 0xb1f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x100

   __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x5530
+  __DATA_CONST.__const: 0x54d0
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0x230
-  UUID: C6D355D7-6A81-3900-B86D-94E0B87FB0D5
-  Functions: 192
-  Symbols:   626
-  CStrings:  241
+  UUID: 06566537-C759-3F08-AEC5-B3CECF6E8B49
+  Functions: 238
+  Symbols:   749
+  CStrings:  312
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandb.cold.1
+ _ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandb.cold.2
+ _ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandb.cold.3
+ _ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandb.cold.4
+ _ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandb.cold.5
+ _ZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandb.cold.1
+ _ZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandb.cold.2
+ _ZN19AppleSPMIController5startEP9IOService.cold.1
+ _ZN19AppleSPMIController5startEP9IOService.cold.10
+ _ZN19AppleSPMIController5startEP9IOService.cold.11
+ _ZN19AppleSPMIController5startEP9IOService.cold.12
+ _ZN19AppleSPMIController5startEP9IOService.cold.13
+ _ZN19AppleSPMIController5startEP9IOService.cold.14
+ _ZN19AppleSPMIController5startEP9IOService.cold.15
+ _ZN19AppleSPMIController5startEP9IOService.cold.16
+ _ZN19AppleSPMIController5startEP9IOService.cold.2
+ _ZN19AppleSPMIController5startEP9IOService.cold.3
+ _ZN19AppleSPMIController5startEP9IOService.cold.4
+ _ZN19AppleSPMIController5startEP9IOService.cold.5
+ _ZN19AppleSPMIController5startEP9IOService.cold.6
+ _ZN19AppleSPMIController5startEP9IOService.cold.7
+ _ZN19AppleSPMIController5startEP9IOService.cold.8
+ _ZN19AppleSPMIController5startEP9IOService.cold.9
+ __ZN19AppleSPMIController12panicCleanupEjjPKcj
+ __ZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandb
+ __ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandb
+ __ZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandb
+ __ZZN19AppleSPMIController10resetQueueEvE11_os_log_fmt
+ __ZZN19AppleSPMIController14copyFaultQueueEPvPjE11_os_log_fmt
+ __ZZN19AppleSPMIController14getHeaderMatchEjjiPKhyPjE11_os_log_fmt
+ __ZZN19AppleSPMIController15fifoQueuesEmptyEvE11_os_log_fmt
+ __ZZN19AppleSPMIController15waitForResponseEbyE11_os_log_fmt
+ __ZZN19AppleSPMIController15waitForResponseEbyE11_os_log_fmt_0
+ __ZZN19AppleSPMIController17dumpResponseQueueEvE11_os_log_fmt
+ __ZZN19AppleSPMIController18executeSPMICommandEP19AppleARMSPMICommandE11_os_log_fmt
+ __ZZN19AppleSPMIController18executeSPMICommandEP19AppleARMSPMICommandE11_os_log_fmt_0
+ __ZZN19AppleSPMIController18executeSPMICommandEP19AppleARMSPMICommandE11_os_log_fmt_1
+ __ZZN19AppleSPMIController18executeSPMICommandEP19AppleARMSPMICommandE11_os_log_fmt_2
+ __ZZN19AppleSPMIController20handleFaultInterruptEP22IOInterruptEventSourceiE11_os_log_fmt
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_0
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_1
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_2
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_3
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_4
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_5
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_6
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_7
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_8
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_9
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__10_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__11_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__12_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__13_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__14_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__15_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__16_
+ __ZZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt__17_
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_0
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_1
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_2
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_3
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_4
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_5
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_6
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_7
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_8
+ __ZZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommandbE11_os_log_fmt_9
+ __ZZN19AppleSPMIController25initializeFaultInterruptsEP9IOServiceE11_os_log_fmt
+ __ZZN19AppleSPMIController25initializeFaultInterruptsEP9IOServiceE20kalloc_type_view_344
+ __ZZN19AppleSPMIController25initializeFaultInterruptsEP9IOServiceE20kalloc_type_view_345
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_0
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_1
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_2
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_3
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_4
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_5
+ __ZZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommandbE11_os_log_fmt_6
+ __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1417
+ __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1438
+ __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1439
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_0
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_1
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_2
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_3
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_4
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_5
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_6
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_7
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_8
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt_9
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__10_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__11_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__12_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__13_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__14_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__15_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__16_
+ __ZZN19AppleSPMIController5startEP9IOServiceE11_os_log_fmt__17_
+ __ZZN19AppleSPMIController5startEP9IOServiceE20kalloc_type_view_164
+ __ZZN19AppleSPMIController9spmiPanicEPKczE21kalloc_type_view_1490
+ __ZZN23AppleGen0SPMIController16initRegisterFileEyyE11_os_log_fmt
+ __ZZN23AppleGen0SPMIController16initRegisterFileEyyE11_os_log_fmt_0
+ __ZZN23AppleGen0SPMIController16initRegisterFileEyyE11_os_log_fmt_1
+ __ZZN23AppleGen0SPMIController16initRegisterFileEyyE11_os_log_fmt_2
+ __ZZN23AppleGen1SPMIController16initRegisterFileEyyE11_os_log_fmt
+ __ZZN23AppleGen3SPMIController16initRegisterFileEyyE11_os_log_fmt
+ __ZZN23AppleGen4SPMIController16initRegisterFileEyyE11_os_log_fmt
+ __os_log_internal
- __ZN19AppleSPMIController12panicCleanupEjj
- __ZN19AppleSPMIController24executeLegacySPMICommandEP19AppleARMSPMICommand
- __ZN19AppleSPMIController24extendedReadWriteCommandEP19AppleARMSPMICommand
- __ZN19AppleSPMIController24registerReadWriteCommandEP19AppleARMSPMICommand
- __ZN19AppleSPMIController26executeSPMICommandMultipleEP19AppleARMSPMICommand
- __ZN19AppleSPMIController29performPayloadlessTransactionEP19AppleARMSPMICommand
- __ZZN19AppleSPMIController25initializeFaultInterruptsEP9IOServiceE20kalloc_type_view_354
- __ZZN19AppleSPMIController25initializeFaultInterruptsEP9IOServiceE20kalloc_type_view_355
- __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1513
- __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1534
- __ZZN19AppleSPMIController4freeEvE21kalloc_type_view_1535
- __ZZN19AppleSPMIController5startEP9IOServiceE20kalloc_type_view_174
- __ZZN19AppleSPMIController9spmiPanicEPKczE21kalloc_type_view_1586
- _printf
CStrings:
+ "%s:%u Timeout header:%x queueStatus:%x USE_INTERRUPTS:%x intMode:%x\n"
+ "12111112122212121111122212111112112221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222221121"
+ "1211111212221212111112221211111211222122222111212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112112222222112122222222222222212222122"
+ "12111112122212121111122212111112112221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222221121222222222222222122222122"
+ "121111121222121211111222121111121122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222221222221222222"
+ "12111112122212121111122212111112112221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222221121222222222222222122222222"
+ "[%s]:%s:%d: %s\n"
+ "[%s]:%s:%d: Copied %d entries\n"
+ "[%s]:%s:%d: Could not get virtual address of queue reset register."
+ "[%s]:%s:%d: Could not map fault counters."
+ "[%s]:%s:%d: Could not map main."
+ "[%s]:%s:%d: Could not map queue reset register."
+ "[%s]:%s:%d: NACK\n"
+ "[%s]:%s:%d: Process responses request_count:%u, timeout:%uus\n"
+ "[%s]:%s:%d: Start\n"
+ "[%s]:%s:%d: address 0x%X length:%u\n"
+ "[%s]:%s:%d: behaviorMap 0x%04x\n"
+ "[%s]:%s:%d: bytesQueued packetLen:%u\n"
+ "[%s]:%s:%d: cmd:%u opts: 0x%08X\n"
+ "[%s]:%s:%d: done\n"
+ "[%s]:%s:%d: entered polling mode!!!\n"
+ "[%s]:%s:%d: popQueue hdr 0x%08X\n"
+ "[%s]:%s:%d: popQueue pay 0x%08X\n"
+ "[%s]:%s:%d: pushQueue hdr 0x%08X intEn:%u\n"
+ "[%s]:%s:%d: pushQueue hdr 0x%08X interrupts:%u\n"
+ "[%s]:%s:%d: pushQueue pay 0x%08X\n"
+ "[%s]:%s:%d: reqs:%u popQueue hdr 0x%08X\n"
+ "[%s]:%s:%d: reset arbiter was successful!\n"
+ "[%s]:%s:%d: ret=0x%08x\n"
+ "[%s]:%s:%d: spmiCmdCount: %d\n"
+ "[%s]:%s:%d: waiting...\n"
+ "[%s]:%s:%d:[error] Entry %d: %X\n"
+ "[%s]:%s:%d:[error] Failed to initialize SPMI register file\n"
+ "[%s]:%s:%d:[error] IOReporters\n"
+ "[%s]:%s:%d:[error] Queues not empty at command end\n"
+ "[%s]:%s:%d:[error] Queues not empty at command start\n"
+ "[%s]:%s:%d:[error] Queues not empty at startup\n"
+ "[%s]:%s:%d:[error] Queues not empty reqEmpty: %s rspEmpty: %s\n"
+ "[%s]:%s:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X\n"
+ "[%s]:%s:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X irq status: %#X num tries: %d bad responses: %s\n"
+ "[%s]:%s:%d:[error] SPMI command timed out.\n"
+ "[%s]:%s:%d:[error] addEventSource(spmiFaultIES)\n"
+ "[%s]:%s:%d:[error] addEventSource(spmiIES)\n"
+ "[%s]:%s:%d:[error] batchHeaders\n"
+ "[%s]:%s:%d:[error] faultMemoryMap\n"
+ "[%s]:%s:%d:[error] getHeaderMatch failed, ret=%08x\n"
+ "[%s]:%s:%d:[error] interruptControllerName\n"
+ "[%s]:%s:%d:[error] interruptLock\n"
+ "[%s]:%s:%d:[error] interrupts\n"
+ "[%s]:%s:%d:[error] parity error\n"
+ "[%s]:%s:%d:[error] queue-depth\n"
+ "[%s]:%s:%d:[error] queuePop failed, ret=%08x\n"
+ "[%s]:%s:%d:[error] queuePopFailed, ret=%08x\n"
+ "[%s]:%s:%d:[error] runInterruptMode ret=%08x\n"
+ "[%s]:%s:%d:[error] runPolledMode ret=%08x\n"
+ "[%s]:%s:%d:[error] spmiFaultIES\n"
+ "[%s]:%s:%d:[error] spmiIES\n"
+ "[%s]:%s:%d:[error] spmiMemoryMap\n"
+ "[%s]:%s:%d:[error] vectors\n"
+ "[%s]:%s:%d:[error] waitForResponseFailed, ret=%08x\n"
+ "[%s]:%s:%d:[error] workoop\n"
+ "copyFaultQueue"
+ "dumpResponseQueue"
+ "executeSPMICommand"
+ "extendedReadWriteCommand"
+ "fifoQueuesEmpty"
+ "getHeaderMatch"
+ "handleFaultInterrupt"
+ "initRegisterFile"
+ "initializeFaultInterrupts"
+ "performPayloadlessTransaction"
+ "registerReadWriteCommand"
+ "resetQueue"
+ "start"
+ "waitForResponse"
- "%s.legs"
- "%s[%s]:%d: %s\n\n"
- "%s[%s]:%d: %s: Queues not empty at command end\n"
- "%s[%s]:%d: %s: Queues not empty at command start\n"
- "%s[%s]:%d: Could not get virtual address of queue reset register.\n"
- "%s[%s]:%d: Could not map fault counters.\n"
- "%s[%s]:%d: Could not map main.\n"
- "%s[%s]:%d: Could not map queue reset register.\n"
- "%s[%s]:%d: Process responses totalRequests:%u\n"
- "%s[%s]:%d: Queues not empty reqEmpty: %s rspEmpty: %s\n"
- "%s[%s]:%d: Rsp queue: %X\n"
- "%s[%s]:%d: SPMI command timed out.\n"
- "%s[%s]:%d: SPMI multiple command timed out.\n"
- "%s[%s]:%d: Start\n"
- "%s[%s]:%d: address 0x%X length:%llu\n"
- "%s[%s]:%d: bytesQueued packetLen:%u\n"
- "%s[%s]:%d: cmd:%u xfer 0x%08X\n"
- "%s[%s]:%d: done\n"
- "%s[%s]:%d: entered polling mode!!!\n"
- "%s[%s]:%d: popQueue hdr 0x%08X\n"
- "%s[%s]:%d: popQueue pay 0x%08X\n"
- "%s[%s]:%d: pushQueue hdr 0x%08X intEn:%u\n"
- "%s[%s]:%d: pushQueue pay 0x%08X\n"
- "%s[%s]:%d: reset arbiter was successful!\n\n"
- "%s[%s]:%d: ret=0x%08X\n"
- "%s[%s]:%d: spmiCmdCount: %d\n"
- "%s[%s]:%d: waiting...\n"
- "%s[%s]:%d:[error] Failed to initialize SPMI register file\n"
- "%s[%s]:%d:[error] IOReporters\n"
- "%s[%s]:%d:[error] Queues not empty at startup\n"
- "%s[%s]:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X\n"
- "%s[%s]:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X irq status: %#X num tries: %d bad responses: %s\n"
- "%s[%s]:%d:[error] addEventSource(spmiFaultIES)\n"
- "%s[%s]:%d:[error] addEventSource(spmiIES)\n"
- "%s[%s]:%d:[error] batchHeaders\n"
- "%s[%s]:%d:[error] faultMemoryMap\n"
- "%s[%s]:%d:[error] interruptControllerName\n"
- "%s[%s]:%d:[error] interruptLock\n"
- "%s[%s]:%d:[error] interrupts\n"
- "%s[%s]:%d:[error] queue-depth\n"
- "%s[%s]:%d:[error] spmiFaultIES\n"
- "%s[%s]:%d:[error] spmiIES\n"
- "%s[%s]:%d:[error] spmiMemoryMap\n"
- "%s[%s]:%d:[error] vectors\n"
- "%s[%s]:%d:[error] workoop\n"
- "12111112122212121111122211211112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212"
- "1211111212221212111112221121111212221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222221121222222222222222212222122"
- "12111112122212121111122211211112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222222122222122"
- "121111121222121211111222112111121222122222111212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112112222222112122222222222222221222221222222"
- "12111112122212121111122211211112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222222122222222"
- "AppleSPMI %s behaviorMap 0x%04x\n"
- "Copied %d entries\n"
- "SPMI read out-of-bounds single"
- "Timeout header:%x queueStatus:%x USE_INTERRUPTS:%x intMode:%x\n"
- "executeLegacySPMICommand"
- "executeSPMICommandMultiple"
- "executeSPMICommandMultiple: %u\n"
- "executeSPMICommandMultiple: ret %u\n"
- "use-legacy-spmi-command"

```
