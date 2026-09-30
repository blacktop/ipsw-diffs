## csplit

> `/usr/bin/csplit`

```diff

-190.0.1.0.0
-  __TEXT.__text: 0xdd8
-  __TEXT.__auth_stubs: 0x270
+195.0.0.0.0
+  __TEXT.__text: 0xdd4
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__const: 0x4a
-  __TEXT.__cstring: 0x1aa
+  __TEXT.__cstring: 0x1a8
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x28
   __DATA.__bss: 0xc60
   - /usr/lib/libSystem.B.dylib
-  UUID: 2FEFF61A-DBA7-3E84-8AC1-CD40201A39B8
+  UUID: 0B72694E-94AB-343E-AFD3-DBD07C249719
   Functions: 20
-  Symbols:   46
-  CStrings:  27
+  Symbols:   45
+  CStrings:  26
 
Symbols:
- _strcmp
Functions:
~ sub_100002d38 -> sub_100000588 : 1916 -> 1912
~ sub_100003914 -> sub_100001160 : 28 -> 48
~ sub_10000395c -> sub_1000011bc : 28 -> 60
~ sub_100003978 -> sub_1000011f8 : 56 -> 44
~ sub_1000039f8 -> sub_10000126c : 60 -> 56
~ sub_100003a34 -> sub_1000012a4 : 44 -> 28
~ sub_100003a60 -> sub_1000012c0 : 48 -> 28
CStrings:
- "-"

```
