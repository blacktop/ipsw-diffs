## UserActivity

> `/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_UA`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-626.0.0.0.0
-  __TEXT.__text: 0x411a4
+628.0.0.0.0
+  __TEXT.__text: 0x413f0
   __TEXT.__objc_methlist: 0x2b70
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x2869
-  __TEXT.__oslogstring: 0x4dea
+  __TEXT.__cstring: 0x2881
+  __TEXT.__oslogstring: 0x4e19
   __TEXT.__gcc_except_tab: 0x595c
   __TEXT.__dof_UA: 0x1c51
-  __TEXT.__unwind_info: 0x1790
+  __TEXT.__unwind_info: 0x1798
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d58
+  __DATA_CONST.__objc_selrefs: 0x1d80
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0x24a0
+  __AUTH_CONST.__cfstring: 0x24c0
   __AUTH_CONST.__objc_const: 0x7340
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x550
-  __AUTH.__data: 0x38
+  __AUTH.__objc_data: 0x5f0
+  __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x750
-  __DATA.__bss: 0x148
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA.__bss: 0x190
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__data: 0x70
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1294
-  Symbols:   3084
-  CStrings:  734
+  Symbols:   3089
+  CStrings:  736
 
Symbols:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$filePathURL
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$isFileReferenceURL
+ _objc_msgSend$stringByAppendingString:
Functions:
~ -[UASharedPasteboardTypeInfo description] : 572 -> 708
~ -[UAPBIRFileURLConverter convertPlatformDataToIR:] : 8 -> 460
CStrings:
+ ", fileContentType: %@"
+ "Updating referenceURL to filePathURL: %@ -> %@"
+ "info { %ld type: %@, uuid: %@%@%@%@}"
- "info { %ld type: %@, uuid: %@%@%@}"
```
