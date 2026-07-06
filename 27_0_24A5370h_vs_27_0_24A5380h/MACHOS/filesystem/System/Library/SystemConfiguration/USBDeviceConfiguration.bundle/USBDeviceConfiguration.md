## USBDeviceConfiguration

> `/System/Library/SystemConfiguration/USBDeviceConfiguration.bundle/USBDeviceConfiguration`

```diff

-  __TEXT.__text: 0xc04
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__cstring: 0x256
+  __TEXT.__text: 0xbfc
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__cstring: 0x278
   __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x70
-  __DATA_CONST.__cfstring: 0x1e0
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x38
   __DATA.__data: 0x70
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   Functions: 14
-  Symbols:   70
-  CStrings:  31
+  Symbols:   67
+  CStrings:  33
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
Symbols:
- _IOMIGMachPortGetPort
- _mach_port_mod_refs
- _mach_task_self_
Functions:
~ _start : 516 -> 552
~ sub_c34 -> sub_c58 : 416 -> 372
CStrings:
+ "DevUSB: pthread_create failed: %d"

```
