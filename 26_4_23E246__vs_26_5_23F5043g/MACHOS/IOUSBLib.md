## IOUSBLib

> `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBLib.bundle/IOUSBLib`

```diff

-1504.100.61.0.0
-  __TEXT.__text: 0x80f4
+1504.120.3.0.0
+  __TEXT.__text: 0x80e4
   __TEXT.__auth_stubs: 0x370
   __TEXT.__cstring: 0x218
   __TEXT.__const: 0x74

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 1D8E59F2-37DE-3DBA-A6CA-94AF850FACDE
+  UUID: C44C1D43-68FC-30D4-9C2C-F57895D01679
   Functions: 279
   Symbols:   359
   CStrings:  54
Functions:
~ __ZN16IOUSBDeviceClass13DeviceRequestEP17IOUSBDevRequestTO : 376 -> 360
~ __ZN16IOUSBDeviceClass18DeviceRequestAsyncEP17IOUSBDevRequestTOPFvPviS2_ES2_ : 356 -> 364
~ __ZN19IOUSBInterfaceClass14ControlRequestEhP17IOUSBDevRequestTO : 384 -> 368
~ __ZN19IOUSBInterfaceClass19ControlRequestAsyncEhP17IOUSBDevRequestTOPFvPviS2_ES2_ : 360 -> 368
~ __ZN19IOUSBInterfaceClass8ReadPipeEhPvPjjj : 260 -> 256
~ __ZN19IOUSBInterfaceClass13ReadPipeAsyncEhPvjjjPFvS0_iS0_ES0_ : 284 -> 304
~ __ZN19IOUSBInterfaceClass9WritePipeEhPvjjj : 232 -> 220
~ __ZN19IOUSBInterfaceClass17ReadStreamsPipeTOEhjPvPjjj : 260 -> 252
~ __ZN19IOUSBInterfaceClass18WriteStreamsPipeTOEhjPvjjj : 228 -> 216
~ __ZN19IOUSBInterfaceClass22ReadStreamsPipeAsyncTOEhjPvjjjPFvS0_iS0_ES0_ : 276 -> 292

```
