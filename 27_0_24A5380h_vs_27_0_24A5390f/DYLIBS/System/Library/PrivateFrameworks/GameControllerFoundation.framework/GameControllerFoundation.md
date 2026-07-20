## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

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
-  __TEXT.__text: 0x6fc24
-  __TEXT.__objc_methlist: 0x6b84
+14.0.21.0.0
+  __TEXT.__text: 0x7010c
+  __TEXT.__objc_methlist: 0x6ba4
   __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x33a0
-  __TEXT.__cstring: 0x71ba
+  __TEXT.__cstring: 0x71d9
   __TEXT.__oslogstring: 0x32f7
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x2110
+  __TEXT.__unwind_info: 0x2120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e30
+  __DATA_CONST.__objc_selrefs: 0x1e48
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x520
   __AUTH_CONST.__const: 0x568
-  __AUTH_CONST.__cfstring: 0x6f80
+  __AUTH_CONST.__cfstring: 0x6fa0
   __AUTH_CONST.__objc_const: 0x149b8
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xa58
-  __AUTH.__objc_data: 0x2940
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH.__objc_data: 0x27b0
   __AUTH.__data: 0x1170
   __DATA.__objc_ivar: 0x880
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x130
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2957
-  Symbols:   6035
-  CStrings:  1336
+  Functions: 2962
+  Symbols:   6041
+  CStrings:  1337
 
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
