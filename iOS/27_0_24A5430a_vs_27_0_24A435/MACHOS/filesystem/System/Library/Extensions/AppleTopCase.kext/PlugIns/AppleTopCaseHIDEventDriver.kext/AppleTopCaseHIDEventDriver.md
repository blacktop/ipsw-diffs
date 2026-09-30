## AppleTopCaseHIDEventDriver

> `/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleTopCaseHIDEventDriver.kext/AppleTopCaseHIDEventDriver`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

   __TEXT.__cstring: 0xa24
   __TEXT.__os_log: 0x1168
   __TEXT.__const: 0x7b
-  __TEXT_EXEC.__text: 0x856c
+  __TEXT_EXEC.__text: 0x870c
   __TEXT_EXEC.__auth_stubs: 0x2a0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0
Functions:
~ __ZN36AppleDeviceManagementHIDEventService9MetaClassC1Ev : 72 -> 76
~ __ZN36AppleDeviceManagementHIDEventServiceC2EPK11OSMetaClass : 100 -> 104
~ __ZN36AppleDeviceManagementHIDEventServiceD2Ev : 760 -> 764
~ __ZN36AppleDeviceManagementHIDEventServiceD1Ev : 760 -> 764
~ __ZN36AppleDeviceManagementHIDEventServiceD0Ev : 68 -> 72
~ __ZN36AppleDeviceManagementHIDEventService9MetaClassC2Ev : 72 -> 76
~ __ZNK36AppleDeviceManagementHIDEventService9MetaClass5allocEv : 52 -> 56
~ __ZN36AppleDeviceManagementHIDEventServiceC2Ev : 136 -> 140
~ __ZN36AppleDeviceManagementHIDEventService4initEP12OSDictionary : 240 -> 244
~ __ZN36AppleDeviceManagementHIDEventService26resumeFromSleepThreadEnterEP8OSObject : 400 -> 404
~ __ZN36AppleDeviceManagementHIDEventService4freeEv : 96 -> 100
~ __ZN36AppleDeviceManagementHIDEventService5startEP9IOService : 480 -> 484
~ __ZN36AppleDeviceManagementHIDEventService4stopEP9IOService : 508 -> 512
~ __ZN36AppleDeviceManagementHIDEventService12didTerminateEP9IOServicejPb : 200 -> 204
~ __ZN36AppleDeviceManagementHIDEventService11handleStartEP9IOService : 3788 -> 3792
~ __Z16OSDynamicPtrCastI8OSString8OSObjectE11OSSharedPtrIT_ERKS2_IT0_E : 92 -> 96
~ __Z16OSDynamicPtrCastI8OSNumber8OSObjectE11OSSharedPtrIT_ERKS2_IT0_E : 92 -> 96
~ __ZN36AppleDeviceManagementHIDEventService21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypejPv : 788 -> 792
~ __ZN36AppleDeviceManagementHIDEventService15getBatteryStateEv : 376 -> 380
~ __ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb : 336 -> 340
~ __ZN36AppleDeviceManagementHIDEventService16getBluetoothInfoEv : 920 -> 924
~ __ZN36AppleDeviceManagementHIDEventService19getFirmwareVersionsEv : 848 -> 852
~ __ZN36AppleDeviceManagementHIDEventService20getSTFirmwareVersionEv : 516 -> 520
~ __ZN36AppleDeviceManagementHIDEventService13getHardwareIdEv : 508 -> 512
~ __ZN36AppleDeviceManagementHIDEventService20handleDeviceInitDoneEv : 116 -> 120
~ __ZN36AppleDeviceManagementHIDEventService16getCriticalErrorEv : 364 -> 368
~ __ZN36AppleDeviceManagementHIDEventService20processCriticalErrorEPhy : 236 -> 240
~ __ZN36AppleDeviceManagementHIDEventService13getWakeReasonEv : 432 -> 436
~ __ZN36AppleDeviceManagementHIDEventService17processWakeReasonEPhy : 600 -> 604
~ __ZN36AppleDeviceManagementHIDEventService13setWakeReasonEh : 172 -> 176
~ __ZN36AppleDeviceManagementHIDEventService19getDevicePowerStateEv : 392 -> 396
~ __ZN36AppleDeviceManagementHIDEventService15getSerialNumberEv : 808 -> 812
~ __ZN7libkern20intrusive_shared_ptrI8OSString27intrusive_osobject_retainerE5resetEPS1_NS_8retain_tE : 116 -> 120
~ __ZN36AppleDeviceManagementHIDEventService12getProductIDEv : 292 -> 296
~ __ZN36AppleDeviceManagementHIDEventService15simpleGetReportEhPhPj15IOHIDReportType : 492 -> 496
~ __ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm : 60 -> 64
~ __ZN36AppleDeviceManagementHIDEventService15simpleSetReportEhPhj : 464 -> 468
~ __ZN36AppleDeviceManagementHIDEventService24systemPowerChangeHandlerEPvjP9IOServiceS0_m : 132 -> 136
~ __ZN36AppleDeviceManagementHIDEventService23scheduleResumeFromSleepEv : 308 -> 312
~ __ZN36AppleDeviceManagementHIDEventService21_resumeFromSleepGatedEv : 564 -> 568
~ __ZN36AppleDeviceManagementHIDEventService22powerStateWillChangeToEmmP9IOService : 156 -> 160
~ __ZN36AppleDeviceManagementHIDEventService20setUSBSleepOnSuspendEb : 172 -> 176
~ _GLOBAL__sub_I_AppleDeviceManagementHIDEventService.cpp : 80 -> 84
~ __atc_parseSimpleMouseV2Packet : 392 -> 396
~ __atc_extractButtonStateFromBinaryV4Header : 156 -> 160
~ __atc_parseSimpleMouseV3Packet : 232 -> 236
~ _MTCompactV7HeaderUnpack : 260 -> 264
~ _MTBinaryV4HeaderUnpack : 132 -> 136
~ __ZN34AppleMultitouchInputHIDEventDriver9MetaClassC1Ev : 72 -> 76
~ __ZN34AppleMultitouchInputHIDEventDriverC2EPK11OSMetaClass : 68 -> 72
~ __ZN34AppleMultitouchInputHIDEventDriverC1EPK11OSMetaClass : 68 -> 72
~ __ZN34AppleMultitouchInputHIDEventDriverD2Ev : 280 -> 284
~ __ZN34AppleMultitouchInputHIDEventDriverD1Ev : 280 -> 284
~ __ZN34AppleMultitouchInputHIDEventDriverD0Ev : 68 -> 72
~ __ZN34AppleMultitouchInputHIDEventDriver9MetaClassC2Ev : 72 -> 76
~ __ZNK34AppleMultitouchInputHIDEventDriver9MetaClass5allocEv : 52 -> 56
~ __ZN34AppleMultitouchInputHIDEventDriverC2Ev : 104 -> 108
~ __ZN34AppleMultitouchInputHIDEventDriver4initEP12OSDictionary : 856 -> 860
~ __ZN34AppleMultitouchInputHIDEventDriver4freeEv : 144 -> 148
~ __ZN34AppleMultitouchInputHIDEventDriver11handleStartEP9IOService : 1992 -> 1996
~ __ZN34AppleMultitouchInputHIDEventDriver27handleInterfaceNotificationEP8OSNumber : 308 -> 312
~ __ZN34AppleMultitouchInputHIDEventDriver4stopEP9IOService : 160 -> 164
~ __ZN34AppleMultitouchInputHIDEventDriver13setPropertiesEP8OSObject : 584 -> 588
~ __ZN34AppleMultitouchInputHIDEventDriver24multitouchDeviceDidStartEv : 348 -> 352
~ __ZN34AppleMultitouchInputHIDEventDriver24setMultitouchPreferencesEP12OSDictionary : 272 -> 276
~ __ZN34AppleMultitouchInputHIDEventDriver22enableMultitouchEventsEb : 300 -> 304
~ __ZN34AppleMultitouchInputHIDEventDriver27enableMultitouchEventsGatedEb : 408 -> 412
~ __ZN34AppleMultitouchInputHIDEventDriver15scheduleUnleashEv : 348 -> 352
~ __ZN34AppleMultitouchInputHIDEventDriver18unleashThreadEnterEv : 304 -> 308
~ __ZN34AppleMultitouchInputHIDEventDriver18unleashDeviceGatedEv : 476 -> 480
~ __ZN34AppleMultitouchInputHIDEventDriver26clearButtonStateForUnleashEv : 276 -> 280
~ _GLOBAL__sub_I_AppleMultitouchInputHIDEventDriver.cpp : 80 -> 84
~ __ZN37AppleMultitouchTrackpadHIDEventDriver9MetaClassC1Ev : 72 -> 76
~ __ZN37AppleMultitouchTrackpadHIDEventDriverC2EPK11OSMetaClass : 52 -> 56
~ __ZN37AppleMultitouchTrackpadHIDEventDriverC1EPK11OSMetaClass : 52 -> 56
~ __ZN37AppleMultitouchTrackpadHIDEventDriverD0Ev : 68 -> 72
~ __ZN37AppleMultitouchTrackpadHIDEventDriver9MetaClassC2Ev : 72 -> 76
~ __ZNK37AppleMultitouchTrackpadHIDEventDriver9MetaClass5allocEv : 104 -> 108
~ __ZN37AppleMultitouchTrackpadHIDEventDriverC1Ev : 88 -> 92
~ __ZN37AppleMultitouchTrackpadHIDEventDriverC2Ev : 88 -> 92
~ __ZN37AppleMultitouchTrackpadHIDEventDriver4initEP12OSDictionary : 148 -> 152
~ __ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej : 1264 -> 1268
~ _GLOBAL__sub_I_AppleMultitouchTrackpadHIDEventDriver.cpp : 80 -> 84
~ __ZN34AppleMultitouchMouseHIDEventDriver9MetaClassC1Ev : 72 -> 76
~ __ZN34AppleMultitouchMouseHIDEventDriverC2EPK11OSMetaClass : 52 -> 56
~ __ZN34AppleMultitouchMouseHIDEventDriverC1EPK11OSMetaClass : 52 -> 56
~ __ZN34AppleMultitouchMouseHIDEventDriverD0Ev : 68 -> 72
~ __ZN34AppleMultitouchMouseHIDEventDriver9MetaClassC2Ev : 72 -> 76
~ __ZNK34AppleMultitouchMouseHIDEventDriver9MetaClass5allocEv : 104 -> 108
~ __ZN34AppleMultitouchMouseHIDEventDriverC1Ev : 88 -> 92
~ __ZN34AppleMultitouchMouseHIDEventDriverC2Ev : 88 -> 92
~ __ZN34AppleMultitouchMouseHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej : 1152 -> 1156
~ _GLOBAL__sub_I_AppleMultitouchMouseHIDEventDriver.cpp : 80 -> 84
~ __ZN36AppleDeviceManagementHIDEventService14getDeviceColorEv : 1012 -> 1016
~ __ZN9os_detail21panic_trapping_policy4trapEPKc : 48 -> 52
~ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.1 : 24 -> 28
~ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.2 : 16 -> 20
~ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.4 : 16 -> 20
~ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.5 : 16 -> 20
~ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.1 : 24 -> 28
~ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.2 : 24 -> 28
~ _atc_parseSimpleMouseV2Packet.cold.4 : 16 -> 20
~ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.1 : 24 -> 28
~ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.5 : 24 -> 28
```
