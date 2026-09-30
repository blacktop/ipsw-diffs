## MTLAssetUpgraderD

> `/usr/libexec/MTLAssetUpgraderD`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-382.5.0.0.0
-  __TEXT.__text: 0x18464
+382.5.3.0.0
+  __TEXT.__text: 0x1867c
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x740
-  __TEXT.__gcc_except_tab: 0xf48
+  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__gcc_except_tab: 0xf84
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0xaaf
-  __TEXT.__cstring: 0x8d4
-  __TEXT.__objc_methname: 0x4af
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__oslogstring: 0xadc
+  __TEXT.__cstring: 0x8ea
+  __TEXT.__objc_methname: 0x4e3
+  __TEXT.__unwind_info: 0x5b8
   __DATA_CONST.__const: 0x238
-  __DATA_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 347
-  Symbols:   606
-  CStrings:  197
+  Functions: 349
+  Symbols:   614
+  CStrings:  203
 
Symbols:
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table51
+ _NSCocoaErrorDomain
+ _ZN17MTLAssetUpgraderD24cleanupCompilerArtifactsEv
+ __ZN17MTLAssetUpgraderD24cleanupCompilerArtifactsEv
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$removeItemAtURL:error:
- GCC_except_table43
- GCC_except_table50
CStrings:
+ "Failed to remove compiler artifacts '%@': %@"
+ "code"
+ "com.apple.gpuarchiver"
+ "domain"
+ "isEqualToString:"
+ "removeItemAtURL:error:"
```
