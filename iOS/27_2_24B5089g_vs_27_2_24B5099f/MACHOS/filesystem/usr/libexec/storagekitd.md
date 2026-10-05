## storagekitd

> `/usr/libexec/storagekitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1076.40.3.0.0
-  __TEXT.__text: 0x2c39c
+1076.40.4.0.0
+  __TEXT.__text: 0x2c420
   __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0x63e0
   __TEXT.__objc_methlist: 0x29a4
   __TEXT.__objc_classname: 0x4f1
   __TEXT.__objc_methname: 0x6637
   __TEXT.__objc_methtype: 0xfe6
-  __TEXT.__const: 0x90
+  __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0xb1c
   __TEXT.__cstring: 0x2ec6
-  __TEXT.__oslogstring: 0x2784
+  __TEXT.__oslogstring: 0x27c5
   __TEXT.__unwind_info: 0xca0
   __DATA_CONST.__const: 0xf60
   __DATA_CONST.__cfstring: 0x1ec0

   - /usr/lib/libutil.dylib
   Functions: 923
   Symbols:   376
-  CStrings:  2156
+  CStrings:  2157
 
Functions:
~ sub_100020c34 : 276 -> 408
CStrings:
+ "IO entry for %{public}@ does not conform to %{public}@, refusing"
```
