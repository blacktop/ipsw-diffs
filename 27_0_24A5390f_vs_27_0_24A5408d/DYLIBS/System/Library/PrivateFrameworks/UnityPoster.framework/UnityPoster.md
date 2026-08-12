## UnityPoster

> `/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster`

```diff

-50.4.1.0.0
-  __TEXT.__text: 0x4640
+51.0.0.0.0
+  __TEXT.__text: 0x4828
   __TEXT.__objc_methlist: 0x5f0
-  __TEXT.__const: 0x3d0
-  __TEXT.__cstring: 0x9d
+  __TEXT.__const: 0x3d8
+  __TEXT.__cstring: 0xcc
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__oslogstring: 0x85
+  __TEXT.__unwind_info: 0x1c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x530
+  __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x98
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x80
+  __DATA_CONST.__got: 0xa0
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x1018
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xf0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 171
-  Symbols:   470
-  CStrings:  11
+  Functions: 173
+  Symbols:   479
+  CStrings:  14
 
Symbols:
+ _OBJC_CLASS_$_NSFileManager
+ __os_log_error_impl
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$URLsForDirectory:inDomains:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$defaultManager
+ _os_log_create
+ _os_log_type_enabled
+ _setupLayerForIdentifier:.log
Functions:
~ ___42-[UPQuiltViewPad setupLayerForIdentifier:]_block_invoke : 72 -> 68
~ ___42-[UPQuiltViewPad setupLayerForIdentifier:]_block_invoke_2 : 116 -> 308
+ ___42-[UPQuiltViewPad setupLayerForIdentifier:]_block_invoke.10
~ _OUTLINED_FUNCTION_0 : 28 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 28
~ _OUTLINED_FUNCTION_4 : 16 -> 12
~ _OUTLINED_FUNCTION_5 : 12 -> 16
~ -[UPQuiltViewPad setupLayerForIdentifier:] : 376 -> 484
+ ___42-[UPQuiltViewPad setupLayerForIdentifier:]_block_invoke_2.cold.1
CStrings:
+ "BSUIMappedImageCache unavailable (caches dir not writable: %{public}@); falling back to non-mapped UIImage decode for poster assets."
+ "MappedImageCache"
+ "com.apple.Posters.UnityPoster"
```
