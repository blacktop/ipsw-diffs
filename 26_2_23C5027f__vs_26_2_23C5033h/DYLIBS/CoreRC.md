## CoreRC

> `/System/Library/PrivateFrameworks/CoreRC.framework/CoreRC`

```diff

 268.60.1.0.0
-  __TEXT.__text: 0x4ad20
+  __TEXT.__text: 0x4acdc
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_methlist: 0x4f1c
   __TEXT.__const: 0x3e8

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D254617-3379-32F8-8BFE-E859BDC1B7C8
+  UUID: 3B4C8357-CDD8-31A1-9172-5AD1542F1CF3
   Functions: 2348
   Symbols:   6965
   CStrings:  4016
Functions:
~ _OUTLINED_FUNCTION_2 : 20 -> 8
~ -[AppleIRDeviceProvider _dispatchAppleVendorEventPage:usage:timestamp:toDevice:].cold.1 : 100 -> 120
~ -[CoreIRBusProvider updateAllowHibernation].cold.1 : 160 -> 156
~ -[CoreIRBusProvider updateLearnedProtocols].cold.1 : 152 -> 148
~ -[CoreIRBusProvider _recreatePairedDeviceFromDefaults:key:].cold.2 : 136 -> 132
~ -[CoreIRBusProvider deleteDevicePrefsWithUUID:UUIDKey:].cold.3 : 140 -> 136
~ -[CoreIRBusProvider setPrefsPropertyForUUID:UUIDKey:object:key:].cold.3 : 140 -> 136
~ -[CoreCECBusProvider updateAllowHibernation].cold.1 : 160 -> 156
~ -[CoreIRDeviceProvider dispatchButtonEventWithCommand:pressed:timestamp:toDevice:].cold.1 : 100 -> 120
~ -[CoreCECDeviceProvider didAddToBus:].cold.1 : 136 -> 132
~ -[CoreCECDeviceProvider handleFeatureAbortMessage:fromDevice:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterActiveSourceMessage:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterInactiveSourceMessage:toDevice:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterRoutingInformationMessage:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterSetOSDNameMessage:toDevice:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterDeviceVendorIDMessage:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterCECVersionMessage:toDevice:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterReportPhysicalAddressMessage:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterReportPowerStatusMessage:toDevice:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider filterDeckStatusMessage:toDevice:].cold.1 : 128 -> 124
~ -[CoreCECDeviceProvider handleReportAudioStatusMessage:fromDevice:].cold.1 : 120 -> 116
~ -[CoreCECDeviceProvider filterSetSystemAudioModeMessage:toDevice:].cold.2 : 128 -> 124
~ -[CoreCECDeviceProvider filterSystemAudioModeStatusMessage:toDevice:].cold.2 : 128 -> 124
~ -[IRCommand setSequence:withCount:] : 132 -> 128
~ -[CoreCECBusClient removeDeviceWithType:].cold.3 : 132 -> 128
~ -[CoreCECDeviceClient removeFromBus].cold.2 : 132 -> 128
~ -[CoreIRLearningSessionProvider _addMapping:] : 260 -> 256

```
