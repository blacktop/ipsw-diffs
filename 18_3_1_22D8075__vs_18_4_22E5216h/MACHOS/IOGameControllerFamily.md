## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-12.3.1.0.0
+12.4.10.0.0
   __TEXT.__cstring: 0x7e9
   __TEXT.__const: 0x38
   __TEXT.__os_log: 0x1085
-  __TEXT_EXEC.__text: 0x8ae4
+  __TEXT_EXEC.__text: 0x89f8
   __TEXT_EXEC.__auth_stubs: 0x290
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__kalloc_type: 0x480
-  Functions: 276
-  Symbols:   664
+  Functions: 294
+  Symbols:   705
   CStrings:  83
 
Symbols:
+ IOGCCircularControlQueueGetLastAppliedPosition.cold.1
+ IOGCCircularControlQueueGetNextApplyPosition.cold.1
+ IOGCCircularControlQueueInit.cold.1
+ IOGCCircularControlQueueInit.cold.2
+ IOGCCircularControlQueueInit.cold.3
+ IOGCCircularControlQueueReset.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _ZN12IOGCResource5startEP9IOService.cold.1
+ _ZN12IOGCResource5startEP9IOService.cold.2
+ _ZN13IOHIDGCDevice12openProviderEj.cold.1
+ _ZN13IOHIDGCDevice16_tryOpenProviderEjy.cold.1
+ _ZN13IOHIDGCDevice17handleInputReportEyjP18IOMemoryDescriptor.cold.1
+ _ZN13IOHIDGCDevice24openProviderInBackgroundEv.cold.1
+ _ZN13IOHIDGCDevice24openProviderInBackgroundEv.cold.2
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.1
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.2
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.3
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.4
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.5
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.6
+ _ZN13IOHIDGCDevice5startEP9IOService.cold.7
+ _ZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iE.cold.1
+ _ZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.1
+ _ZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.2
+ _ZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iE.cold.1
+ _ZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.1
+ _ZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.2
+ _ZN16IOGCCommandQueue10syncActionEPFiP8OSObjectPvES2_.cold.1
+ _ZN16IOGCCommandQueue10syncActionEPFiP8OSObjectPvES2_.cold.2
+ _ZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationE.cold.1
+ _ZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationE.cold.2
+ _ZN21IOGCCircularDataQueue15initWithEntriesEjj.cold.1
+ _ZN21IOGCCircularDataQueue15initWithEntriesEjj.cold.2
+ _ZN21IOGCCircularDataQueue7enqueueEPvj.cold.1
+ _ZN27IOGCCircularDataQueueCursor4readEPvPj.cold.1
+ _ZN27IOGCCircularDataQueueCursor6accessEPvS0_PFiS0_S0_S0_jE.cold.1

```
