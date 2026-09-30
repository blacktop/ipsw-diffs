## configd

> `usr/libexec/configd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1405.160.3.0.0
-  __TEXT.__text: 0x6d124
+1405.160.3.701.3
+  __TEXT.__text: 0x6d0e0
   __TEXT.__auth_stubs: 0x2460
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0xb64
-  __TEXT.__const: 0x228
+  __TEXT.__const: 0x248
   __TEXT.__cstring: 0x3249
-  __TEXT.__oslogstring: 0x5938
+  __TEXT.__oslogstring: 0x5972
   __TEXT.__objc_methname: 0x1c8d
   __TEXT.__objc_classname: 0x7c
   __TEXT.__objc_methtype: 0x672

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 995
+  Functions: 994
   Symbols:   821
   CStrings:  1772
 
Functions:
~ sub_100008c9c : 668 -> 744
- sub_10006d5cc
CStrings:
+ "%s : %5u : %s : %{private}@"
+ "%s : %5u : %{private}@"
+ "%s%s : %5u : %{private}@"
+ "*copy   : %5u : %{private}@"
+ "add  %s : %5u : %{private}@"
+ "list    : %5u : %s : %{private}@"
+ "open    : %5u : pid=%d"
- "%s : %5u : %@"
- "%s : %5u : %s : %@"
- "%s%s : %5u : %@"
- "*copy   : %5u : %@"
- "add  %s : %5u : %@"
- "list    : %5u : %s : %@"
- "open    : %5u : %@"
```
