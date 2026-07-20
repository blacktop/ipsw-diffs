## BannerKit

> `/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`

```diff

-167.0.0.0.0
-  __TEXT.__text: 0x2d77c
-  __TEXT.__objc_methlist: 0x3d2c
+168.0.0.0.0
+  __TEXT.__text: 0x2d8c8
+  __TEXT.__objc_methlist: 0x3d44
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0x2546
   __TEXT.__oslogstring: 0x208b
   __TEXT.__gcc_except_tab: 0x1148
-  __TEXT.__unwind_info: 0xfb0
+  __TEXT.__unwind_info: 0xfb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f68
+  __DATA_CONST.__objc_selrefs: 0x1f90
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__got: 0x3e8

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xfa0
+  __AUTH.__objc_data: 0xf50
   __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0x1a50
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x8
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1140
-  Symbols:   3164
+  Functions: 1142
+  Symbols:   3174
   CStrings:  435
 
Symbols:
+ -[UIView(BannerKitAdditions) bn_frameIgnoringTransform]
+ -[UIView(BannerKitAdditions) bn_setFrameRespectingTransform:]
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _objc_msgSend$anchorPoint
+ _objc_msgSend$bn_frameIgnoringTransform
+ _objc_msgSend$bn_setFrameRespectingTransform:
+ _objc_msgSend$position
+ _objc_msgSend$setBounds:
+ _objc_msgSend$transform
```
