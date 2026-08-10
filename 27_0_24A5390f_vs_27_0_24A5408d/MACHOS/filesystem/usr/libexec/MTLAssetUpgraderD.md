## MTLAssetUpgraderD

> `/usr/libexec/MTLAssetUpgraderD`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-382.5.0.0.0
-  __TEXT.__text: 0x18418
+382.5.3.0.0
+  __TEXT.__text: 0x18600
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__gcc_except_tab: 0xfb0
+  __TEXT.__objc_stubs: 0x840
+  __TEXT.__gcc_except_tab: 0xfe8
   __TEXT.__const: 0xe0
-  __TEXT.__oslogstring: 0xb14
-  __TEXT.__cstring: 0x92f
-  __TEXT.__objc_methname: 0x534
-  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__oslogstring: 0xb41
+  __TEXT.__cstring: 0x945
+  __TEXT.__objc_methname: 0x568
+  __TEXT.__unwind_info: 0x5c8
   __DATA_CONST.__const: 0x248
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x100
-  __DATA.__objc_selrefs: 0x1f0
+  __DATA_CONST.__got: 0x108
+  __DATA.__objc_selrefs: 0x210
   __DATA.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 348
-  Symbols:   633
-  CStrings:  206
+  Functions: 350
+  Symbols:   641
+  CStrings:  212
 
Symbols:
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table50
+ _NSCocoaErrorDomain
+ _ZN17MTLAssetUpgraderD24cleanupCompilerArtifactsEv
+ __ZN17MTLAssetUpgraderD24cleanupCompilerArtifactsEv
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$removeItemAtURL:error:
- GCC_except_table42
- GCC_except_table49
CStrings:
+ "Failed to remove compiler artifacts '%@': %@"
+ "code"
+ "com.apple.gpuarchiver"
+ "domain"
+ "isEqualToString:"
+ "removeItemAtURL:error:"
```
