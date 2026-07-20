## IntentsUI

> `/System/Library/Frameworks/IntentsUI.framework/Versions/A/IntentsUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-4016.0.43.5.0
-  __TEXT.__text: 0xc184
-  __TEXT.__objc_methlist: 0x1120
+4016.0.45.3.0
+  __TEXT.__text: 0xc588
+  __TEXT.__objc_methlist: 0x1128
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__cstring: 0xdf7
   __TEXT.__oslogstring: 0x6b8
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_selrefs: 0xdd0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x2b0
-  __AUTH_CONST.__const: 0x690
+  __DATA_CONST.__got: 0x2f0
+  __AUTH_CONST.__const: 0x6b0
   __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0x1cb0
   __AUTH_CONST.__objc_intobj: 0x18

   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x540
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 354
-  Symbols:   1174
+  Functions: 357
+  Symbols:   1193
   CStrings:  119
 
Symbols:
+ +[INUIPortableImageLoaderHelper _intents_downsampledBundleImage:]
+ GCC_except_table323
+ GCC_except_table343
+ _INUIImageSourceCreationOptions.onceToken
+ _INUIImageSourceCreationOptions.options
+ _NSZeroRect
+ _OBJC_CLASS_$_NSColorSpace
+ _UTTypeGIF
+ _UTTypeHEIC
+ _UTTypeHEIF
+ _UTTypeJPEG
+ _UTTypeTIFF
+ __INUIDownsampledBundleImageMac
+ ____INUIImageSourceCreationOptions_block_invoke
+ _kCGImageSourceAllowableTypes
+ _objc_msgSend$bitmapImageRepByConvertingToColorSpace:renderingIntent:
+ _objc_msgSend$drawInRect:fromRect:operation:fraction:
+ _objc_msgSend$initWithSize:
+ _objc_msgSend$lockFocus
+ _objc_msgSend$sRGBColorSpace
+ _objc_msgSend$unlockFocus
- GCC_except_table322
- GCC_except_table342
Functions:
~ +[INUIImageSizeProvider imageSizeForImage:] : 448 -> 536
~ +[INUIImageSizeProvider downscaledPNGImageForImage:size:error:] : 2560 -> 2640
+ ____INUIImageSourceCreationOptions_block_invoke
~ -[INUIPortableImageLoaderHelper loadImageDataFromBundle:withImageName:accessSpecifier:completion:] : 892 -> 1052
+ __INUIDownsampledBundleImageMac
+ +[INUIPortableImageLoaderHelper supportsSecureCoding]
```
