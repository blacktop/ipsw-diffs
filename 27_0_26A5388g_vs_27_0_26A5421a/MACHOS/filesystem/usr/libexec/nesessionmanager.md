## nesessionmanager

> `/usr/libexec/nesessionmanager`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2331.0.0.0.1
-  __TEXT.__text: 0xbf2fc
+2340.1.2.0.0
+  __TEXT.__text: 0xbf3d4
   __TEXT.__auth_stubs: 0x1cd0
   __TEXT.__objc_stubs: 0x8920
   __TEXT.__objc_methlist: 0x3d84
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x2428
-  __TEXT.__objc_methname: 0x947b
-  __TEXT.__oslogstring: 0x10dc9
+  __TEXT.__gcc_except_tab: 0x241c
+  __TEXT.__objc_methname: 0x948d
+  __TEXT.__oslogstring: 0x10e05
   __TEXT.__cstring: 0x56d7
   __TEXT.__objc_classname: 0xb3b
   __TEXT.__objc_methtype: 0x1be5

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xe78
   __DATA_CONST.__got: 0x790
-  __DATA.__objc_const: 0x8280
+  __DATA.__objc_const: 0x82a0
   __DATA.__objc_selrefs: 0x2470
-  __DATA.__objc_ivar: 0x7bc
+  __DATA.__objc_ivar: 0x7c0
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0xeb8
   __DATA.__bss: 0x118

   - /usr/lib/libobjc.A.dylib
   Functions: 2007
   Symbols:   681
-  CStrings:  4153
+  CStrings:  4155
 
Functions:
~ sub_1000b01dc : 964 -> 1064
~ sub_1000b6e68 -> sub_1000b6ecc : 120 -> 164
~ sub_1000b8d5c -> sub_1000b8dec : 3928 -> 4000
CStrings:
+ "%@: %s - Filter not started, skipping reporting timer setup"
+ "_userEverLoggedIn"
```
