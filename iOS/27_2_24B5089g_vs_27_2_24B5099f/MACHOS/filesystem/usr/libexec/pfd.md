## pfd

> `/usr/libexec/pfd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-120.0.0.0.0
-  __TEXT.__text: 0x7338
+120.40.2.0.0
+  __TEXT.__text: 0x7370
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__const: 0x2190
-  __TEXT.__cstring: 0x1625
+  __TEXT.__cstring: 0x1634
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x148
   __DATA_CONST.__const: 0xe0

   - /usr/lib/libSystem.B.dylib
   Functions: 63
   Symbols:   133
-  CStrings:  307
+  CStrings:  308
 
Functions:
~ sub_100000f24 : 1072 -> 1128
CStrings:
+ "%s: %s: %m"
+ "%s: DIOCGETLIMIT index %d: %m"
- "%s: DIOCGETLIMIT index %d"
```
