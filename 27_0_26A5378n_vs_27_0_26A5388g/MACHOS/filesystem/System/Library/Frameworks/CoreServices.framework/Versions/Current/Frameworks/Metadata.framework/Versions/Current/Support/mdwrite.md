## mdwrite

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/Current/Support/mdwrite`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2451.1.401.0.0
-  __TEXT.__text: 0x1335c
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_stubs: 0x1760
-  __TEXT.__objc_methlist: 0x5f4
-  __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x2d0
+2454.100.0.0.0
+  __TEXT.__text: 0x13550
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_stubs: 0x1780
+  __TEXT.__objc_methlist: 0x5fc
+  __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x165a
-  __TEXT.__oslogstring: 0x6c6
-  __TEXT.__objc_methname: 0x143a
+  __TEXT.__oslogstring: 0x6f6
+  __TEXT.__gcc_except_tab: 0x2d0
+  __TEXT.__objc_methname: 0x1453
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methtype: 0x579
-  __TEXT.__unwind_info: 0x530
-  __DATA_CONST.__const: 0xf28
+  __TEXT.__objc_methtype: 0x589
+  __TEXT.__unwind_info: 0x538
+  __DATA_CONST.__const: 0xf48
   __DATA_CONST.__cfstring: 0xb80
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x9d8
+  __DATA_CONST.__auth_got: 0x9d0
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x968
-  __DATA.__objc_selrefs: 0x640
+  __DATA.__objc_selrefs: 0x648
   __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x148
+  __DATA.__data: 0x14c
   __DATA.__bss: 0x1a0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /System/Library/PrivateFrameworks/SpotlightServerKit.framework/Versions/A/SpotlightServerKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 443
-  Symbols:   438
-  CStrings:  531
+  Functions: 446
+  Symbols:   437
+  CStrings:  534
 
Symbols:
- _setxattr
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jIESVu/Sources/Spotlight/spotlight/mdwrite/MDLabelServices.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jIESVu/Sources/Spotlight/spotlight/mdwrite/MDPlistBytesCryptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jIESVu/Sources/Spotlight/spotlight/mdwrite/mdwrite.m"
+ "fsetxattr error: %d path: %s"
+ "i32@0:8r*16r*24"
+ "sandboxCheckedOpen: open('%s') failed errno:%d"
+ "sandboxCheckedOpen:path:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.J0kiAA/Sources/Spotlight/spotlight/mdwrite/MDLabelServices.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.J0kiAA/Sources/Spotlight/spotlight/mdwrite/MDPlistBytesCryptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.J0kiAA/Sources/Spotlight/spotlight/mdwrite/mdwrite.m"
- "setxattr error: %d path: %s"
```
