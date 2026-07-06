## com.apple.driver.AppleOLYHAL

> `com.apple.driver.AppleOLYHAL`

```diff

   __TEXT.__const: 0x1ef0
-  __TEXT.__cstring: 0x4973
-  __TEXT_EXEC.__text: 0x1d5d4
-  __TEXT_EXEC.__auth_stubs: 0x790
+  __TEXT.__cstring: 0x4a9c
+  __TEXT_EXEC.__text: 0x1df1c
+  __TEXT_EXEC.__auth_stubs: 0x7a0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170
   __DATA.__bss: 0xc
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__const: 0x2048
   __DATA_CONST.__kalloc_type: 0x600
-  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0xf8
-  Functions: 572
-  Symbols:   1094
-  CStrings:  516
+  Functions: 578
+  Symbols:   1102
+  CStrings:  524
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _OUTLINED_FUNCTION_5
+ __ZN11AppleOLYHAL7mapbar0Ev
+ __ZN11AppleOLYHAL9unmapbar0Ev
+ __ZN22IOInterruptEventSource20interruptEventSourceEP8OSObjectPFvS1_PS_iEP9IOServicei
+ __ZN32AppleOLYHALPortInterfacePCIeAMFM19resetProgressWakeupEP22IOInterruptEventSourcei
+ __ZN32AppleOLYHALPortInterfacePCIeAMFM19resetProgressWakeupEP22IOInterruptEventSourcei_vfpthunk_
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_522
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_528
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1414
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_557
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_559
+ ____ZN32AppleOLYHALPortInterfacePCIeAMFM19resetProgressWakeupEP22IOInterruptEventSourcei_block_invoke
- _ZN11AppleOLYHAL23dextRespawnTimerExpiredEP18IOTimerEventSource
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_471
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_477
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1352
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_506
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_508
CStrings:
+ "\"%s:%u:\" \"completionTimeoutRecoveryInProgress\" @%s:%d"
+ "%s::%s: Deferred dext recovery already pending; coalescing repeat crash\n"
+ "%s::%s: PCIe device is gone.\n"
+ "%s::%s: Spurious dext respawn timer expiration"
+ "%s::%s: WiFi dext launched in unallowable state\n"
+ "%s::%s: completion timeout recovery in progress: reset cannot finish until termination is complete\n"
+ "%s::%s: waiting for reset progress... current progress: %u\n"
+ "121111121222121211111111221211211122111121112212221111111"
+ "1211112211111222211112211112211"
+ "APB0_S"
+ "APB1_S"
+ "OLYHAL panic: %s[%x] = 0x%08x\n"
+ "mapbar0"
- "\"%s:%u:\" \"!fDextRecoveryPaused\" @%s:%d"
- "\"AppleBCMWLAN Dext didn't respawn within %u milliseconds\\n\" @%s:%d"
- "%s::%s: Still waiting for reset progress... current progress: %u\n"
- "1211111212221212111111112212112111221121112212221111111"
- "121111221111122221111221111221"

```
