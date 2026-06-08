## vm_stat

> `/usr/bin/vm_stat`

```diff

-1042.120.1.0.0
-  __TEXT.__text: 0xc04
-  __TEXT.__auth_stubs: 0x110
-  __TEXT.__const: 0x48
+1066.0.0.0.0
+  __TEXT.__text: 0xbe0
+  __TEXT.__auth_stubs: 0x120
+  __TEXT.__const: 0x40
   __TEXT.__cstring: 0x55a
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__got: 0x30
-  __DATA.__common: 0x208
+  __DATA.__common: 0x358
   __DATA.__bss: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 03D6C235-7164-39BE-BD39-DB5FAFAFB51D
+  UUID: 1C64ACD4-3CA7-3EBB-B46D-CC50B5790CA9
   Functions: 8
-  Symbols:   25
+  Symbols:   26
   CStrings:  81
 
Symbols:
+ _memcpy
Functions:
~ sub_100000aec : 728 -> 676
~ sub_100000e08 -> sub_100000dd4 : 508 -> 524

```
