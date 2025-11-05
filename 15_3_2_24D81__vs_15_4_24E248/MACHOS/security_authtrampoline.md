## security_authtrampoline

> `/usr/libexec/security_authtrampoline`

```diff

   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x82
   __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xb8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x20

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E255FCAA-2411-33F8-8A45-54A128793A23
+  UUID: 2D834C9F-C1B3-3A3B-BF59-0417FA184207
   Functions: 7
   Symbols:   26
   CStrings:  12
Functions:
~ sub_100003c0c -> sub_100000a54 : 144 -> 68
~ sub_100003c9c -> sub_100000a98 : 68 -> 144

```
