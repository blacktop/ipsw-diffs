## USBHost

> `/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`

```diff

-1139.40.1.0.0
-  __TEXT.__text: 0x1b84c
+1139.40.6.0.0
+  __TEXT.__text: 0x1ba5c
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x11ec
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x2d7d
+  __TEXT.__oslogstring: 0x2da4
   __TEXT.__cstring: 0x1984
   __TEXT.__gcc_except_tab: 0x5a4
   __TEXT.__unwind_info: 0x4f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28524383-DE38-3F40-95C4-078E3625CBCD
-  Functions: 562
-  Symbols:   2512
-  CStrings:  1394
+  UUID: BC981E0D-2571-3FD6-BC0B-3939351E385C
+  Functions: 563
+  Symbols:   2518
+  CStrings:  1395
 
Symbols:
+ _ReadCompletion.cold.12
+ _ReadCompletion.cold.13
+ _ReadCompletion.cold.14
Functions:
~ _ReadCompletion : 1536 -> 1952
+ -[AccessoryIAPInterface writeData:].cold.6
CStrings:
+ "Unable to clear USB pipe stall! (%08x)"

```
