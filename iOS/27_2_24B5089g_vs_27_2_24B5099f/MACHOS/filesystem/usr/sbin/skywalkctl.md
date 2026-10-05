## skywalkctl

> `/usr/sbin/skywalkctl`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA.__data`

```diff

 170.0.0.0.0
-  __TEXT.__text: 0x1187c
+  __TEXT.__text: 0x11878
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__cstring: 0xc33d
+  __TEXT.__cstring: 0xc390
   __TEXT.__const: 0x60
   __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__const: 0x4398
+  __DATA_CONST.__const: 0x43a8
   __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   Functions: 193
   Symbols:   115
-  CStrings:  2094
+  CStrings:  2096
 
Functions:
~ sub_100004ac4 : 2876 -> 2872
CStrings:
+ "\t%llu dropped due to wrap flag not matching ring direction\n"
+ "FilterDropBadDirection"
```
