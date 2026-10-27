## CoreDAV

> `/System/Library/PrivateFrameworks/CoreDAV.framework/Versions/A/CoreDAV`

```diff

-1248.0.0.0.0
-  __TEXT.__text: 0x56f0c
+1248.2.1.0.0
+  __TEXT.__text: 0x56f10
   __TEXT.__objc_methlist: 0x57c0
   __TEXT.__cstring: 0x3d45
   __TEXT.__const: 0xf0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27f0
+  __DATA_CONST.__objc_selrefs: 0x27f8
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x498

   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__objc_ivar: 0x7a4
-  __DATA.__data: 0x978
-  __DATA.__bss: 0x60
+  __DATA.__data: 0x60
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x2300
-  __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__data: 0x920
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
   Functions: 1764
-  Symbols:   4693
+  Symbols:   4694
   CStrings:  1010
 
Symbols:
+ -[CoreDAVMultiGetWithFallbackTaskGroup _fatalMultiGetError]
+ _objc_msgSend$_fatalMultiGetError
- -[CoreDAVMultiGetWithFallbackTaskGroup error]
Functions:
~ ___53-[CoreDAVMultiGetWithFallbackTaskGroup _fetchOneItem]_block_invoke : 584 -> 600
~ ___54-[CoreDAVMultiGetWithFallbackTaskGroup startTaskGroup]_block_invoke : 324 -> 312
```
