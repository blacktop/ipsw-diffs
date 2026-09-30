## dmd

> `/usr/libexec/dmd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-259.0.0.0.0
-  __TEXT.__text: 0x812dc
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0xe960
+260.0.0.0.0
+  __TEXT.__text: 0x81558
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_stubs: 0xe980
   __TEXT.__objc_methlist: 0x7fdc
   __TEXT.__const: 0x168
   __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x11846
+  __TEXT.__objc_methname: 0x1186f
   __TEXT.__objc_methtype: 0x1d98
-  __TEXT.__cstring: 0x5489
-  __TEXT.__oslogstring: 0xb22e
+  __TEXT.__cstring: 0x54ae
+  __TEXT.__oslogstring: 0xb2a0
   __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x2210
-  __DATA_CONST.__const: 0x2740
-  __DATA_CONST.__cfstring: 0x57e0
+  __TEXT.__unwind_info: 0x2218
+  __DATA_CONST.__const: 0x2748
+  __DATA_CONST.__cfstring: 0x5800
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__auth_got: 0x790
   __DATA_CONST.__got: 0x13e0
   __DATA.__objc_const: 0x1d6e8
-  __DATA.__objc_selrefs: 0x4198
+  __DATA.__objc_selrefs: 0x41a0
   __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 3218
-  Symbols:   918
-  CStrings:  4519
+  Functions: 3220
+  Symbols:   919
+  CStrings:  4522
 
Symbols:
+ _xpc_dictionary_get_data
CStrings:
+ "Received xpc stream event (trusted distributed notification matching) with name: %{public}@ user info: %{public}@"
+ "com.apple.distnoted.matching.trusted"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
```
