## AppleMesaLib

> `/System/Library/Extensions/AppleBiometricSensor.kext/PlugIns/AppleMesaLib.plugin/AppleMesaLib`

```diff

-259.100.1.0.0
-  __TEXT.__text: 0x2f0c
+271.0.0.0.0
+  __TEXT.__text: 0x30c0
   __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__const: 0x18
+  __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__oslogstring: 0x51
-  __TEXT.__cstring: 0x1aa
+  __TEXT.__oslogstring: 0x75
+  __TEXT.__cstring: 0x1c7
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x38
-  __DATA.__data: 0x108
+  __DATA.__data: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 341DB7CE-02E8-3ACA-AD5E-80E133A3E48F
-  Functions: 72
-  Symbols:   110
-  CStrings:  40
+  UUID: 5E9A2612-292F-3469-9B9A-05AA74EFBE8C
+  Functions: 74
+  Symbols:   112
+  CStrings:  42
 
Symbols:
+ _CFAllocatorAllocateTyped
+ __ZN10MesaPlugIn28GetModuleSerialNumberDynamicEPhPm
+ __ZN10MesaPlugIn28GetModuleSerialNumberDynamicEPvPhPm
- _CFAllocatorAllocate
Functions:
+ __ZN10MesaPlugIn20SetInterruptCallbackEPvPFvmPhmEm
~ _AppleMesaFactory : 496 -> 512
+ __ZN10MesaPlugIn28GetModuleSerialNumberDynamicEPhPm
CStrings:
+ "%s: %s: %s size=%zu\n"
+ "%s: %s: %s size=%zu serialLen:%zu\n"
+ "GetModuleSerialNumberDynamic"
- "%s: %s: %s size=%x\n"

```
