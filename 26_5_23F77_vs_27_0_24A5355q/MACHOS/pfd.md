## pfd

> `/usr/libexec/pfd`

```diff

-114.120.2.0.0
-  __TEXT.__text: 0x74b8
+118.0.0.0.0
+  __TEXT.__text: 0x7410
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__const: 0x2190
-  __TEXT.__cstring: 0x164c
+  __TEXT.__cstring: 0x1625
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x80
   __DATA.__data: 0x3c4
   __DATA.__common: 0x10
   __DATA.__bss: 0x8c

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter
   - /usr/lib/libSystem.B.dylib
-  UUID: D53F35FF-92B5-3EA7-90AD-8DC97E6F8C02
+  UUID: 75312761-CC20-3FF9-8AF2-6C97193BD197
   Functions: 63
   Symbols:   133
-  CStrings:  314
+  CStrings:  311
 
Functions:
~ sub_100000f30 : 1268 -> 1084
~ sub_1000033e4 -> sub_10000332c : 556 -> 560
~ sub_100003610 -> sub_10000355c : 288 -> 292
~ sub_100006a34 -> sub_100006984 : 372 -> 376
~ sub_100006ddc -> sub_100006d30 : 1100 -> 1104
CStrings:
- "%s: strlcpy"
- "__PFDSetInterfaceFlags"
- "lo0"

```
