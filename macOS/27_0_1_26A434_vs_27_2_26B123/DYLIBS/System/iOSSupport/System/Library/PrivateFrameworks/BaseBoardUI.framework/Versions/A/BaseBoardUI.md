## BaseBoardUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/BaseBoardUI.framework/Versions/A/BaseBoardUI`

```diff

-827.0.0.0.0
-  __TEXT.__text: 0x184a4
+827.2.3.0.0
+  __TEXT.__text: 0x18548
   __TEXT.__objc_methlist: 0x18bc
-  __TEXT.__const: 0x3e0
-  __TEXT.__gcc_except_tab: 0x2cc0
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0x2cec
   __TEXT.__cstring: 0x11ae
-  __TEXT.__oslogstring: 0x778
+  __TEXT.__oslogstring: 0x7b0
   __TEXT.__unwind_info: 0xda0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x398
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x480
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0x618
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 518
-  Symbols:   1784
-  CStrings:  181
+  Symbols:   1786
+  CStrings:  182
 
Symbols:
+ ___error
+ _strerror_r
Functions:
~ -[BSUIMappedImageCacheRegistry tmpPath] : 1024 -> 1188
CStrings:
+ "BSUIMappedImageCache failed to get relative tmpDir from dirhelper with errno=%i (%{public}s) for %@"
+ "BSUIMappedImageCache is falling back to NSTemporaryDirectory=%@ for %@"
- "BSUIMappedImageCache failed to get relative tmpDir from dirhelper for %@ : falling back to NSTemporaryDirectory=%@"
```
