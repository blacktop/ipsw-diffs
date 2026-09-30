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
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-259.0.0.0.0
-  __TEXT.__text: 0x6052c
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_stubs: 0x9960
+260.0.0.0.0
+  __TEXT.__text: 0x607c4
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_stubs: 0x9980
   __TEXT.__objc_methlist: 0x6724
   __TEXT.__const: 0x150
   __TEXT.__objc_classname: 0x1b16
-  __TEXT.__objc_methname: 0xc381
+  __TEXT.__objc_methname: 0xc3aa
   __TEXT.__objc_methtype: 0x16be
-  __TEXT.__cstring: 0x43b7
-  __TEXT.__oslogstring: 0x6bd8
+  __TEXT.__cstring: 0x43dc
+  __TEXT.__oslogstring: 0x6c4a
   __TEXT.__gcc_except_tab: 0xc04
   __TEXT.__ustring: 0x498
-  __TEXT.__unwind_info: 0x1a18
-  __DATA_CONST.__const: 0x1878
-  __DATA_CONST.__cfstring: 0x4800
+  __TEXT.__unwind_info: 0x1a20
+  __DATA_CONST.__const: 0x1880
+  __DATA_CONST.__cfstring: 0x4820
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0xf8

   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__auth_got: 0x4e0
   __DATA_CONST.__got: 0xf90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1ab28
-  __DATA.__objc_selrefs: 0x2c18
+  __DATA.__objc_selrefs: 0x2c20
   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x3e30
   __DATA.__data: 0xba8

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2414
-  Symbols:   699
-  CStrings:  3234
+  Functions: 2416
+  Symbols:   700
+  CStrings:  3237
 
Symbols:
+ _xpc_dictionary_get_data
CStrings:
+ "Received xpc stream event (trusted distributed notification matching) with name: %{public}@ user info: %{public}@"
+ "com.apple.distnoted.matching.trusted"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
```
