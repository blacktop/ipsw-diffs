## com.apple.iokit.IOSCSIBlockCommandsDevice

> `com.apple.iokit.IOSCSIBlockCommandsDevice`

```diff

-535.0.0.0.0
-  __TEXT.__cstring: 0xef4
-  __TEXT_EXEC.__text: 0xdc24
+535.0.0.0.2
+  __TEXT.__cstring: 0xf50
+  __TEXT_EXEC.__text: 0xdcf8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a9
   __DATA.__common: 0x98
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__kalloc_type: 0x3c0
-  UUID: 14739090-AF8A-30B3-8373-387BC40F0041
+  UUID: D7B18E8A-1B2B-3283-B6F5-3A6E3441868E
   Functions: 288
   Symbols:   0
-  CStrings:  121
+  CStrings:  123
 
Functions:
~ sub_fffffff00a7f087c -> sub_fffffff00a806fac : 16 -> 12
~ sub_fffffff00a7f088c -> sub_fffffff00a806fb8 : 12 -> 16
~ sub_fffffff00a7f08a4 -> sub_fffffff00a806fd4 : 12 -> 24
~ sub_fffffff00a7f08b0 -> sub_fffffff00a806fec : 24 -> 12
~ sub_fffffff00a7f08e0 -> sub_fffffff00a807010 : 12 -> 20
~ sub_fffffff00a7f08f8 -> sub_fffffff00a807030 : 20 -> 12
~ sub_fffffff00a7f2e54 -> sub_fffffff00a809584 : 4252 -> 4268
~ sub_fffffff00a7f3ef0 -> sub_fffffff00a80a630 : 2120 -> 1128
~ sub_fffffff00a7f4738 -> sub_fffffff00a80aa98 : 932 -> 2120
CStrings:
+ "[%s:%s] [%s]: Abort PM transition ...\n"
+ "[%s::AbortPMTransition] [%s] Media has Changed\n"
+ "[%s::AbortPMTransition] [%s] Requesting Close\n"
- "[%s:%s] [%s]: Scheduling PM abort thread\n"

```
