## automountd

> `usr/libexec/automountd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-322.0.0.0.0
-  __TEXT.__text: 0x1454c
+322.0.0.700.2
+  __TEXT.__text: 0x14624
   __TEXT.__auth_stubs: 0xd00
   __TEXT.__const: 0x208
   __TEXT.__oslogstring: 0x347
-  __TEXT.__cstring: 0x3bf4
+  __TEXT.__cstring: 0x3c23
   __TEXT.__unwind_info: 0x288
   __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0xc8

   - /usr/lib/libutil.dylib
   Functions: 224
   Symbols:   235
-  CStrings:  579
+  CStrings:  583
 
Functions:
~ sub_1000086f4 : 2980 -> 3144
~ sub_100010a78 -> sub_100010b1c : 496 -> 548
CStrings:
+ ".."
+ "AUTOMOUNTD_NODEV="
+ "Invalid fstype [%s]"
+ "nodev"
```
