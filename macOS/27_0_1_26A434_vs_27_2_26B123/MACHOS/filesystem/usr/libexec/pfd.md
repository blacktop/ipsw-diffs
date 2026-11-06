## pfd

> `/usr/libexec/pfd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-118.0.0.0.0
-  __TEXT.__text: 0x75ec
+120.40.2.0.0
+  __TEXT.__text: 0x7624
   __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0x2190
-  __TEXT.__cstring: 0x1753
+  __TEXT.__cstring: 0x1762
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x150
   __DATA_CONST.__const: 0x120

   - /usr/lib/libSystem.B.dylib
   Functions: 64
   Symbols:   142
-  CStrings:  320
+  CStrings:  321
 
Functions:
~ sub_100000f44 : 1072 -> 1128
CStrings:
+ "%s: %s: %m"
+ "%s: DIOCGETLIMIT index %d: %m"
- "%s: DIOCGETLIMIT index %d"
```
