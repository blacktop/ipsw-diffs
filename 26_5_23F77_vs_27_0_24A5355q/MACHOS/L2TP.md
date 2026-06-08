## L2TP

> `/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/L2TP.ppp/L2TP`

```diff

 1027.0.0.0.0
-  __TEXT.__text: 0xec04
+  __TEXT.__text: 0xeca4
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__const: 0x120
   __TEXT.__cstring: 0x3a9d
   __TEXT.__unwind_info: 0x210
-  __DATA_CONST.__auth_got: 0x520
-  __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__cfstring: 0xfe0
+  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__got: 0x160
   __DATA.__data: 0x9e0
   __DATA.__common: 0xe98
   __DATA.__bss: 0x5f8

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libipsec.A.dylib
-  UUID: B754D2C7-FFB3-3D90-96C8-6D56849E1568
+  UUID: 2AF7A4F9-3E9E-3AB4-A2C7-2C11668716A6
   Functions: 148
   Symbols:   331
   CStrings:  695
Functions:
~ sub_e24 : 1860 -> 1864
~ sub_3da0 -> sub_3da4 : 6220 -> 6228
~ sub_6118 -> sub_6124 : 124 -> 148
~ _pfkey_send_getspi : 988 -> 996
~ sub_6824 -> sub_6850 : 1600 -> 1604
~ sub_6ecc -> sub_6efc : 768 -> 776
~ _pfkey_send_delete_all : 688 -> 696
~ _pfkey_send_register : 212 -> 240
~ sub_7a8c -> sub_7ae8 : 892 -> 896
~ _pfkey_align : 240 -> 244
~ _makepath : 312 -> 324
~ _get_src_address : 1108 -> 1120
~ _IPSecCreateCiscoDefaultConfiguration : 2880 -> 2884
~ sub_ebac -> sub_ec2c : 416 -> 436
~ sub_ed4c -> sub_ede0 : 324 -> 336

```
