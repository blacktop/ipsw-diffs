## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x76534
-  __TEXT.__objc_methlist: 0x6c14
+14.0.21.0.0
+  __TEXT.__text: 0x76a48
+  __TEXT.__objc_methlist: 0x6c34
   __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0x33bc
-  __TEXT.__cstring: 0x7243
+  __TEXT.__cstring: 0x7262
   __TEXT.__oslogstring: 0x33f5
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x21a8
+  __TEXT.__unwind_info: 0x21c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e70
+  __DATA_CONST.__objc_selrefs: 0x1e88
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x530
   __AUTH_CONST.__const: 0x1980
-  __AUTH_CONST.__cfstring: 0x6fc0
+  __AUTH_CONST.__cfstring: 0x6fe0
   __AUTH_CONST.__objc_const: 0x14b58
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x998
-  __AUTH.__objc_data: 0x2670
+  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH.__objc_data: 0x25d0
   __AUTH.__data: 0x1170
   __DATA.__objc_ivar: 0x89c
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3048
-  Symbols:   6186
-  CStrings:  1348
+  Functions: 3053
+  Symbols:   6192
+  CStrings:  1349
 
Symbols:
+ +[GCIOIterator iterate:handler:]
+ -[GCIOIterator nextObject:]
+ -[GCIORegistryEntry enumerateChildrenInPlane:handler:error:]
+ -[GCIORegistryEntry firstChildInPlane:objectClass:matching:error:]
+ _IORegistryEntryGetChildIterator
+ _objc_msgSend$nextObject:
CStrings:
+ "Error creating child iterator."
```
