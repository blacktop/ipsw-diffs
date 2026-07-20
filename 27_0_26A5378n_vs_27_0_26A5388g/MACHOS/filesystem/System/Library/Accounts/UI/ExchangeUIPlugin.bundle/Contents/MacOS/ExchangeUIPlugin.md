## ExchangeUIPlugin

> `/System/Library/Accounts/UI/ExchangeUIPlugin.bundle/Contents/MacOS/ExchangeUIPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-842.0.0.0.0
-  __TEXT.__text: 0x8d94
+844.0.0.0.0
+  __TEXT.__text: 0x8c3c
   __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x724
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x12e9
+  __TEXT.__cstring: 0x1289
   __TEXT.__objc_methname: 0x209b
   __TEXT.__objc_classname: 0xb9
   __TEXT.__objc_methtype: 0x3ac

   __TEXT.__ustring: 0x9a
   __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__const: 0x340
-  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__got: 0x2e8
   __DATA.__objc_const: 0x998
   __DATA.__objc_selrefs: 0x9f0
   __DATA.__objc_ivar: 0x64

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 166
-  Symbols:   174
-  CStrings:  548
+  Symbols:   172
+  CStrings:  547
 
Symbols:
- _kSecAttrLabel
- _kSecMatchLimitOne
Functions:
~ sub_7324 : 896 -> 800
~ sub_77cc -> sub_776c : 796 -> 896
~ sub_7ae8 -> sub_7aec : 412 -> 352
~ sub_8fa4 -> sub_8f6c : 852 -> 564
CStrings:
+ "Excluding client identity with no displayable name from picker (no CN, no subject summary)"
- "Cert picker: %lu of %lu identities required keychain-label probe (slow path)"
- "Excluding client identity with no displayable name from picker (no CN, no subject summary, no keychain label)"
```
