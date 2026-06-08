## IOUSBLib

> `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBLib.bundle/IOUSBLib`

```diff

-1504.120.4.0.0
-  __TEXT.__text: 0x80e4
+1616.0.0.0.0
+  __TEXT.__text: 0x8104
   __TEXT.__auth_stubs: 0x370
   __TEXT.__cstring: 0x218
   __TEXT.__const: 0x74
-  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__gcc_except_tab: 0x80
   __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x30
   __DATA.__data: 0x490
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 1588ACA0-F85A-34EA-8EB9-06EF701EC155
+  UUID: 2A6DF32C-14A0-337E-B7BD-2FA08F75EB57
   Functions: 279
   Symbols:   359
   CStrings:  54
Functions:
~ __ZN13IOUSBIUnknown24_versionNumberFromStringEPK10__CFString : 548 -> 544
~ __ZN16IOUSBDeviceClassD2Ev : 232 -> 236
~ __ZN16IOUSBDeviceClass21CacheConfigDescriptorEv : 388 -> 392
~ __ZN16IOUSBDeviceClass30GetBandwidthAvailableForDeviceEPj : 80 -> 84
~ __ZN19IOUSBInterfaceClassD2Ev : 256 -> 260
~ __ZN19IOUSBInterfaceClass21GetBandwidthAvailableEPj : 80 -> 84
~ __ZN19IOUSBInterfaceClass21CacheConfigDescriptorEv : 460 -> 468
~ __ZN19IOUSBInterfaceClass18FindNextDescriptorEPKvh : 272 -> 280

```
