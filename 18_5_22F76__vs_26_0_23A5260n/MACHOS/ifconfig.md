## ifconfig

> `/sbin/ifconfig`

```diff

-705.100.5.0.0
-  __TEXT.__text: 0xb5bc
+725.0.0.0.0
+  __TEXT.__text: 0xb870
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__init_offsets: 0x2c
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x387a
+  __TEXT.__cstring: 0x3976
   __TEXT.__unwind_info: 0x218
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x280
-  __DATA.__data: 0x2d40
+  __DATA.__data: 0x2de0
   __DATA.__common: 0x7c
   __DATA.__bss: 0x1260
   - /usr/lib/libSystem.B.dylib
-  UUID: CBA54078-74F5-3AF9-8A3C-802E5C5CEFED
-  Functions: 229
-  Symbols:   411
-  CStrings:  827
+  UUID: EDD5F4E5-8857-372A-A30D-DE4BF238C989
+  Functions: 232
+  Symbols:   414
+  CStrings:  836
 
Symbols:
+ _setinbandwakepacket
+ _setlowpowerwake
+ _setultraconstrained
CStrings:
+ "\tL4S: %s\n"
+ "-ultraconstrained"
+ "inband wake packet: %d\n"
+ "inbandwakepacket"
+ "ioctl SIOCSINBANDWAKEPKT"
+ "ioctl SIOCSLOWPOWERWAKE"
+ "low power wake: %d\n"
+ "lowpowerwake"
+ "ultraconstrained"

```
