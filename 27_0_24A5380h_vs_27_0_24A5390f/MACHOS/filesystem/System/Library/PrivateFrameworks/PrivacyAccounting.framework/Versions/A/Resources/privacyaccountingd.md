## privacyaccountingd

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-148.0.0.0.0
-  __TEXT.__text: 0xc2b0
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x2280
+149.0.0.0.0
+  __TEXT.__text: 0xc59c
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0xc0c
-  __TEXT.__const: 0xe0
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x324
-  __TEXT.__cstring: 0xfc7
-  __TEXT.__oslogstring: 0x1106
-  __TEXT.__objc_methname: 0x2c23
+  __TEXT.__cstring: 0xfcf
+  __TEXT.__oslogstring: 0x1176
+  __TEXT.__objc_methname: 0x2c64
   __TEXT.__objc_classname: 0x1e1
   __TEXT.__objc_methtype: 0x852
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x468
-  __DATA_CONST.__const: 0x670
+  __TEXT.__unwind_info: 0x478
+  __DATA_CONST.__const: 0x698
   __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x260
   __DATA.__objc_const: 0x18b0
-  __DATA.__objc_selrefs: 0xb30
+  __DATA.__objc_selrefs: 0xb40
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x430

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 318
-  Symbols:   210
-  CStrings:  803
+  Functions: 322
+  Symbols:   217
+  CStrings:  807
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ __CFXPCCreateXPCObjectFromCFObject
+ __xpc_type_data
+ _xpc_copy
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ _xpc_dictionary_set_value
CStrings:
+ "Could not deserialize user info for XPC event: %{public}s error: %{public}@"
+ "No UserInfo data found in XPC event"
+ "com.apple.distnoted.matching.trusted"
+ "dataWithBytes:length:"
+ "propertyListWithData:options:format:error:"
- "com.apple.distnoted.matching"
```
