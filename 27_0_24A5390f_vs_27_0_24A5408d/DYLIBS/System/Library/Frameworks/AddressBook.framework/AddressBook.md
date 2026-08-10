## AddressBook

> `/System/Library/Frameworks/AddressBook.framework/AddressBook`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 12679.100.1.0.0
-  __TEXT.__text: 0x1a698
+  __TEXT.__text: 0x1a940
   __TEXT.__objc_methlist: 0x17d4
-  __TEXT.__const: 0xd4
+  __TEXT.__const: 0xdc
   __TEXT.__cstring: 0x1ef5
   __TEXT.__ustring: 0x1d6
-  __TEXT.__oslogstring: 0x3db
+  __TEXT.__oslogstring: 0x55b
   __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__unwind_info: 0x718
   __TEXT.__objc_stubs: 0x0

   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 682
+  Functions: 688
   Symbols:   1933
-  CStrings:  268
+  CStrings:  272
 
CStrings:
+ "Could not create bitmap context. Error: bytesPerPixel × width × height overflows (w=%f h=%f)"
+ "Could not create bitmap context. Error: size is non-finite, negative, or exceeds SIZE_MAX (w=%f h=%f)"
+ "Could not scale image data. Error: bytesPerPixel × width × height overflows (w=%f h=%f)"
+ "Could not scale image data. Error: size is non-finite, negative, or exceeds SIZE_MAX (w=%f h=%f)"
```
