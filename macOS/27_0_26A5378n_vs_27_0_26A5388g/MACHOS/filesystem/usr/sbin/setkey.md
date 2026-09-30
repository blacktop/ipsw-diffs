## setkey

> `/usr/sbin/setkey`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

-1129.0.0.0.0
-  __TEXT.__text: 0x8a30
+1130.0.0.0.0
+  __TEXT.__text: 0x8ab0
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__cstring: 0xfe4
-  __TEXT.__const: 0x3136
+  __TEXT.__cstring: 0x1005
+  __TEXT.__const: 0x32da
   __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__const: 0x460
   __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__data: 0x14
+  __DATA.__data: 0x18
   __DATA.__bss: 0x9a0
   __DATA.__common: 0x898
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libipsec.A.dylib
   Functions: 135
   Symbols:   83
-  CStrings:  241
+  CStrings:  243
 
Functions:
~ sub_100000718 : 2068 -> 2108
~ sub_100000f3c -> sub_100000f64 : 1308 -> 1348
~ sub_100005954 -> sub_1000059a4 : 4528 -> 4488
~ sub_100006b04 -> sub_100006b2c : 332 -> 348
~ sub_100006c54 -> sub_100006c8c : 196 -> 216
~ sub_100007428 -> sub_100007474 : 216 -> 224
~ sub_100007500 -> sub_100007554 : 3744 -> 3772
~ sub_1000083a0 -> sub_100008410 : 384 -> 400
CStrings:
+ "direction: in  "
+ "direction: out  "
```
