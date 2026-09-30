## com.apple.driver.AppleOLYHAL

> `com.apple.driver.AppleOLYHAL`

```diff

-531.5.0.0.0
-  __TEXT.__const: 0x1ef0
-  __TEXT.__cstring: 0x4a9c
-  __TEXT_EXEC.__text: 0x1df1c
+531.7.0.0.0
+  __TEXT.__const: 0x1f88
+  __TEXT.__cstring: 0x50bb
+  __TEXT_EXEC.__text: 0x1e774
   __TEXT_EXEC.__auth_stubs: 0x7a0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170
   __DATA.__bss: 0xc
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x2048
+  __DATA_CONST.__const: 0x20b8
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0xf8
-  Functions: 578
-  Symbols:   1030
-  CStrings:  524
+  Functions: 589
+  Symbols:   1041
+  CStrings:  543
 
Symbols:
+ _ZN11AppleOLYHAL37reportInitFailureWithChipResetDK_ImplEP8OSStringb
+ __ZN11AppleOLYHAL28initFailureChipResetCompleteEv
+ __ZN11AppleOLYHAL29initFailureResetActionHandlerEjPv
+ __ZN11AppleOLYHAL30reportInitFailureWithChipResetEP8OSStringb
+ __ZN11AppleOLYHAL31requestDextInitFailureChipResetEv
+ __ZN11AppleOLYHAL37reportInitFailureWithChipResetDK_CallEP8OSStringb
+ __ZN11AppleOLYHAL37reportInitFailureWithChipResetDK_ImplEP8OSStringb
+ __ZN11AppleOLYHAL39reportInitFailureWithChipResetDK_InvokeE5IORPCPFiP8OSStringbE
+ __ZN28AppleOLYHALPortInterfacePCIe29setInitFailureRecoveryPendingEb
+ __ZN32AppleOLYHALPortInterfacePCIeAMFM29setInitFailureRecoveryPendingEb
+ __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_699
+ __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_716
+ __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_731
+ __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_744
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_523
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_529
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1426
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_558
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_560
+ ____ZN11AppleOLYHAL28initFailureChipResetCompleteEv_block_invoke
+ ____ZN11AppleOLYHAL31requestDextInitFailureChipResetEv_block_invoke
+ ____ZN32AppleOLYHALPortInterfacePCIeAMFM29setInitFailureRecoveryPendingEb_block_invoke
- __ZN11AppleOLYHAL7mapbar0Ev
- __ZN11AppleOLYHAL9unmapbar0Ev
- __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_698
- __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_715
- __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_730
- __ZZN11AppleOLYHAL15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_743
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_522
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_528
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1414
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_557
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_559
CStrings:
+ "%s::%s: OLYHAL-port(AMFM) enableGated is_enabled=%d pActionType=%d first=%d fResetProgress=%d\n"
+ "%s::%s: setPowerEnable is_enabled=%d\n"
+ "1211111212221212111111112212112111221121112212221111111"
+ "AppleOLYHAL::reportInitFailure: str=%s\n"
+ "AppleOLYHAL::reportInitFailureWithChipReset: str=%s requiresChipResetAndRegisterService=%d\n"
+ "BCMWLAN Init-failure chip reset limit reached"
+ "Init-failure chip reset (attempt %u/%u); AMFM-coordinated power-cycle + respawn\n"
+ "Init-failure chip reset limit (%u) reached; leaving WiFi down\n"
+ "Init-failure chip reset requested during shutdown; ignoring reset\n"
+ "Init-failure chip reset unsupported on non-AMFM-managed port; leaving WiFi down\n"
+ "Manually triggering IOPCIDevice powerOn\n"
+ "OLYHAL initFailureChipResetComplete -> restoreDeviceState()\n"
+ "OLYHAL initFailureChipResetComplete: reset finished (attempt %u)\n"
+ "OLYHAL requestDextInitFailureChipReset gate: shutdown=%d fPCIePort=%p amfmManaged=%d count=%u/%u\n"
+ "OLYHAL reset -> fPCIePort->requestChipReset attempt=%u\n"
+ "OLYHAL reset -> registerActionHandler + resetPortActionHandler status=0x%x\n"
+ "OLYHAL reset -> requestChipReset returned 0x%x\n"
+ "OLYHAL reset -> saveDeviceState() (captured cfg pre power-cycle)\n"
+ "OLYHAL-port kAMFMChipIsUp -> init failure recovery reset complete, notifying OLYHAL\n"
+ "OLYHAL-port requestChipReset -> fManager NULL (offline, no reset)\n"
+ "OLYHAL-port requestChipReset powerPreserve=%d fManager=%p fResetProgress=%d fResetIsInternal=%d\n"
+ "OLYHAL-port setInitFailureRecoveryPending pending=%d\n"
+ "Retriggering wifi dext matching\n"
+ "initFailureChipResetComplete: dext already published. nothing to respawn\n"
+ "initFailureChipResetComplete: fWlanPCIDevice missing. dext will spawn automatically when it appears\n"
+ "reportInitFailureWithChipResetDK_Impl"
- "%s::%s: %u\n"
- "%s::%s: PCIe device is gone.\n"
- "121111121222121211111111221211211122111121112212221111111"
- "APB0_S"
- "APB1_S"
- "OLYHAL panic: %s[%x] = 0x%08x\n"
- "mapbar0"
```
