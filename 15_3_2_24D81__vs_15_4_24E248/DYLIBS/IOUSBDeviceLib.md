## IOUSBDeviceLib

> `/System/Library/Extensions/IOUSBDeviceFamily.kext/Contents/PlugIns/IOUSBDeviceLib.plugin/Contents/MacOS/IOUSBDeviceLib`

```diff

-818.60.2.0.0
-  __TEXT.__text: 0x2c98
+818.100.6.0.0
+  __TEXT.__text: 0x2c5c
   __TEXT.__auth_stubs: 0x2a0
   __TEXT.__gcc_except_tab: 0x38
   __TEXT.__const: 0x32

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 478324D1-7DE6-32EC-96B7-881D61166054
+  UUID: A6E7F4CA-72E1-3D91-A6E8-39EDB969DB1D
   Functions: 107
   Symbols:   165
   CStrings:  6
Functions:
~ __ZN19IOUSBDeviceIUnknown13factoryAddRefEv : 160 -> 148
~ __ZN19IOUSBDeviceIUnknown14factoryReleaseEv : 172 -> 164
~ __ZN25IOUSBDeviceInterfaceClass5startEPK14__CFDictionaryj : 168 -> 156
~ __ZN25IOUSBDeviceInterfaceClass19scheduleWithRunLoopEP11__CFRunLoopPK10__CFString : 392 -> 388
~ __ZN25IOUSBDeviceInterfaceClass21unscheduleFromRunLoopEP11__CFRunLoopPK10__CFString : 196 -> 180
~ __ZN25IOUSBDeviceInterfaceClass24setClassCommandCallbacksEPFiPvS0_P22IOUSBDeviceSetupPacketPyPP17__IOUSBDeviceDataPiEPFvS0_S0_S2_iyS5_EPFiS0_S0_S2_iyS5_ES0_S0_P11__CFRunLoopPK10__CFString : 556 -> 552
~ __ZN25IOUSBDeviceInterfaceClass23registerForDemandLaunchEPK10__CFString : 348 -> 344

```
