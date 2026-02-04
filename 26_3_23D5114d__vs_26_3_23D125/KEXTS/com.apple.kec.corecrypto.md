## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-1922.80.3.0.0
-  __TEXT.__cstring: 0x4d71
+1922.80.7.0.0
+  __TEXT.__cstring: 0x4db6
   __TEXT.__const: 0x19770
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x6b31c
+  __TEXT_EXEC.__text: 0x6b69c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9340
   __DATA.__bss: 0x29e0

   __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x178
-  __DATA_CONST.__const: 0x3f98
-  UUID: D65A6954-C749-3280-9B23-06E8D30D2764
+  __DATA_CONST.__const: 0x3fc8
+  UUID: 112BB0BC-E757-3D1E-947C-F3F9C842760A
   Functions: 1829
   Symbols:   0
-  CStrings:  465
+  CStrings:  469
 
Functions:
~ _fipspost_post_indicator : 6328 -> 7232
~ sub_fffffe000b10a6d8 -> sub_fffffe000b04f020 : 24 -> 32
~ sub_fffffe000b125404 -> sub_fffffe000b069d54 : 124 -> 108
CStrings:
+ "cccmac_one_shot_generate"
+ "cccmac_one_shot_verify"
+ "ccrng"
+ "ccrng_generate"

```
