## AppleTopCaseHIDEventDriver

> `/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleTopCaseHIDEventDriver.kext/AppleTopCaseHIDEventDriver`

```diff

   __TEXT.__cstring: 0xbcb
   __TEXT.__os_log: 0x11a4
   __TEXT.__const: 0x7b
-  __TEXT_EXEC.__text: 0xa8dc
+  __TEXT_EXEC.__text: 0xa8b8
   __TEXT_EXEC.__auth_stubs: 0x2b0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x20e0
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__kalloc_type: 0x100
-  Functions: 175
-  Symbols:   1391
+  Functions: 177
+  Symbols:   1477
   CStrings:  176
 
Symbols:
+ MTBinaryV4HeaderUnpack.cold.1
+ MTBinaryV4HeaderUnpack.cold.2
+ MTBinaryV4HeaderUnpack.cold.3
+ MTCompactV7HeaderUnpack.cold.1
+ MTCompactV7HeaderUnpack.cold.2
+ MTCompactV7HeaderUnpack.cold.3
+ MTCompactV7HeaderUnpack.cold.4
+ MTCompactV7HeaderUnpack.cold.5
+ MTCompactV7HeaderUnpack.cold.6
+ MTCompactV7HeaderUnpack.cold.7
+ MTCompactV7HeaderUnpack.cold.8
+ _OUTLINED_FUNCTION_0
+ _ZN34AppleMultitouchMouseHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.1
+ _ZN34AppleMultitouchMouseHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.2
+ _ZN34AppleMultitouchMouseHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.3
+ _ZN34AppleMultitouchMouseHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.4
+ _ZN36AppleDeviceManagementHIDEventService15simpleGetReportEhPhPj15IOHIDReportType.cold.1
+ _ZN36AppleDeviceManagementHIDEventService15simpleSetReportEhPhj.cold.1
+ _ZN36AppleDeviceManagementHIDEventService15simpleSetReportEhPhj.cold.2
+ _ZN36AppleDeviceManagementHIDEventService15simpleSetReportEhPhj.cold.3
+ _ZN36AppleDeviceManagementHIDEventService17processWakeReasonEPhy.cold.1
+ _ZN36AppleDeviceManagementHIDEventService17processWakeReasonEPhy.cold.2
+ _ZN36AppleDeviceManagementHIDEventService17processWakeReasonEPhy.cold.3
+ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.1
+ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.2
+ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.3
+ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.4
+ _ZN36AppleDeviceManagementHIDEventService19processBatteryStateEPhyb.cold.5
+ _ZN36AppleDeviceManagementHIDEventService20processCriticalErrorEPhy.cold.1
+ _ZN36AppleDeviceManagementHIDEventService20processCriticalErrorEPhy.cold.2
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.1
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.2
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.3
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.4
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.5
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.6
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.7
+ _ZN36AppleDeviceManagementHIDEventService27processBatteryStateExtendedEPhy.cold.8
+ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.1
+ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.2
+ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.3
+ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.4
+ _ZN37AppleMultitouchTrackpadHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej.cold.5
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.1
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.2
+ _ZNK7libkern17bounded_array_refIhN9os_detail21panic_trapping_policyEE5sliceEmm.cold.3
+ _atc_parseSimpleMouseV2Packet.cold.1
+ _atc_parseSimpleMouseV2Packet.cold.10
+ _atc_parseSimpleMouseV2Packet.cold.11
+ _atc_parseSimpleMouseV2Packet.cold.12
+ _atc_parseSimpleMouseV2Packet.cold.13
+ _atc_parseSimpleMouseV2Packet.cold.14
+ _atc_parseSimpleMouseV2Packet.cold.15
+ _atc_parseSimpleMouseV2Packet.cold.16
+ _atc_parseSimpleMouseV2Packet.cold.2
+ _atc_parseSimpleMouseV2Packet.cold.3
+ _atc_parseSimpleMouseV2Packet.cold.4
+ _atc_parseSimpleMouseV2Packet.cold.5
+ _atc_parseSimpleMouseV2Packet.cold.6
+ _atc_parseSimpleMouseV2Packet.cold.7
+ _atc_parseSimpleMouseV2Packet.cold.8
+ _atc_parseSimpleMouseV2Packet.cold.9
+ _atc_parseSimpleMouseV3Packet.cold.1
+ _atc_parseSimpleMouseV3Packet.cold.2
+ _atc_parseSimpleMouseV3Packet.cold.3
+ _atc_parseSimpleMouseV3Packet.cold.4
+ _atc_parseSimpleMouseV3Packet.cold.5
+ _atc_parseSimpleMouseV3Packet.cold.6
+ _atc_parseSimpleMouseV3Packet.cold.7
+ _atc_parseSimpleMouseV3Packet.cold.8

```
