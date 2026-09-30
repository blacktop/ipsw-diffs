## IOStreamLib

> `/System/Library/Extensions/IOStreamFamily.kext/Contents/PlugIns/IOStreamLib.plugin/Contents/MacOS/IOStreamLib`

```diff

 120.0.0.0.0
-  __TEXT.__text: 0x18f0
+  __TEXT.__text: 0x1880
   __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__gcc_except_tab: 0x34
   __TEXT.__const: 0x2a
-  __TEXT.__gcc_except_tab: 0x40
   __TEXT.__cstring: 0x9
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x180

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 125F7776-6023-36CF-8935-49AB5361B7AE
+  UUID: B872F8A1-5C4A-3E0C-90D9-B462745148F8
   Functions: 80
   Symbols:   128
   CStrings:  1
Functions:
~ __ZN16IOStreamIUnknown13factoryAddRefEv : 172 -> 160
~ __ZN16IOStreamIUnknown14factoryReleaseEv : 184 -> 176
~ __ZN16IOStreamIUnknownD2Ev : 68 -> 72
~ __ZN16IOStreamIUnknownD1Ev -> sub_994 : 4 -> 20
~ __ZN16IOStreamIUnknown6addRefEv -> __ZN16IOStreamIUnknownD0Ev : 20 -> 4
~ __ZN16IOStreamIUnknown7releaseEv -> __ZN16IOStreamIUnknown6addRefEv : 92 -> 20
~ __ZN16IOStreamIUnknown21genericQueryInterfaceEPv11CFUUIDBytesPS0_ -> __ZN16IOStreamIUnknown7releaseEv : 40 -> 92
~ __ZN20IOStreamServiceClass8_getModeEPP22IOStreamInterface_v1_t -> __ZN20IOStreamServiceClass14_suspendStreamEPP22IOStreamInterface_v1_t : 48 -> 40
~ __ZN20IOStreamServiceClassC2Ev -> __ZN20IOStreamServiceClass8_setModeEPP22IOStreamInterface_v1_t12IOStreamMode : 104 -> 48
~ __ZN20IOStreamServiceClassD2Ev -> __ZN20IOStreamServiceClassC1Ev : 160 -> 104
~ sub_2d4c -> __ZN20IOStreamServiceClassD2Ev : 20 -> 140
~ __ZN20IOStreamServiceClassD0Ev : 108 -> 56
~ __ZN20IOStreamServiceClass4openEj : 452 -> 436
~ __ZN20IOStreamServiceClass13getBufferInfoEjPPvPyS1_S2_ : 196 -> 188

```
