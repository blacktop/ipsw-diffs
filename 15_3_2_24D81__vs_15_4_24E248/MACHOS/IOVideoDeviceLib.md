## IOVideoDeviceLib

> `/System/Library/Extensions/IOVideoFamily.kext/Contents/PlugIns/IOVideoDeviceLib.plugin/Contents/MacOS/IOVideoDeviceLib`

```diff

-5590.80.3.0.0
-  __TEXT.__text: 0x1454
-  __TEXT.__auth_stubs: 0x2b0
+5590.100.8.0.0
+  __TEXT.__text: 0x1410
+  __TEXT.__auth_stubs: 0x2c0
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__const: 0x34
   __TEXT.__cstring: 0x49
   __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__cfstring: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 60EB7605-9B52-365E-AA09-BC40FF723607
+  UUID: 2D4F58C6-A608-3D96-BA0C-18944E2A4FCC
   Functions: 55
-  Symbols:   117
+  Symbols:   118
   CStrings:  7
 
Symbols:
+ _memcpy
Functions:
~ __ZN21IOVideoDeviceIUnknown13factoryAddRefEv : 172 -> 160
~ __ZN21IOVideoDeviceIUnknown14factoryReleaseEv : 184 -> 176
~ __ZN25IOVideoDeviceServiceClass21createStreamInterfaceEPK14__CFDictionaryjbPPP22IOStreamInterface_v1_t : 804 -> 784
~ __ZN25IOVideoDeviceServiceClass22releaseStreamInterfaceEbPPP22IOStreamInterface_v1_t : 140 -> 112

```
