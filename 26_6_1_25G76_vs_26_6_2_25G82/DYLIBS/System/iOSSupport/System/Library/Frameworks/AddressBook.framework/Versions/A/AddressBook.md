## AddressBook

> `/System/iOSSupport/System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

 12671.700.11.0.0
-  __TEXT.__text: 0x1cd44
+  __TEXT.__text: 0x1d044
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_methlist: 0x18ac
-  __TEXT.__const: 0xdc
+  __TEXT.__const: 0xe4
   __TEXT.__cstring: 0x1edc
   __TEXT.__ustring: 0x1d6
-  __TEXT.__oslogstring: 0x3db
+  __TEXT.__oslogstring: 0x55b
   __TEXT.__gcc_except_tab: 0x174
   __TEXT.__unwind_info: 0x760
   __TEXT.__objc_classname: 0x1e9

   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/Versions/A/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 703
-  Symbols:   1984
-  CStrings:  1061
+  Functions: 710
+  Symbols:   1985
+  CStrings:  1065
 
Symbols:
+ ABImageUtilsCreateImageFromImageWithCropRect
CStrings:
+ "Could not create bitmap context. Error: bytesPerPixel × width × height overflows (w=%f h=%f)"
+ "Could not create bitmap context. Error: size is non-finite, negative, or exceeds SIZE_MAX (w=%f h=%f)"
+ "Could not scale image data. Error: bytesPerPixel × width × height overflows (w=%f h=%f)"
+ "Could not scale image data. Error: size is non-finite, negative, or exceeds SIZE_MAX (w=%f h=%f)"
```
