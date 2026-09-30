## ibv_uc_pingpong

> `/usr/bin/ibv_uc_pingpong`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-100.0.0.0.0
-  __TEXT.__text: 0x1a2c
-  __TEXT.__auth_stubs: 0x3f0
+105.0.0.0.0
+  __TEXT.__text: 0x1b0c
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x8ed
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x20
   __DATA.__data: 0x180
   __DATA.__bss: 0x8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/librdma.dylib
   Functions: 15
-  Symbols:   69
+  Symbols:   70
   CStrings:  82
 
Symbols:
+ _kdebug_trace
Functions:
~ sub_100000610 : 3288 -> 3352
~ sub_100001424 -> sub_100001464 : 176 -> 252
~ sub_100001bb4 -> sub_100001c40 : 144 -> 228
```
