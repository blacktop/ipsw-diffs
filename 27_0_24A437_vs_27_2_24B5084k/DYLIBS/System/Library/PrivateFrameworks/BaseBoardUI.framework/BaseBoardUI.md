## BaseBoardUI

> `/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI`

```diff

-827.0.0.0.0
-  __TEXT.__text: 0x18650
+827.2.1.1.0
+  __TEXT.__text: 0x186f4
   __TEXT.__objc_methlist: 0x198c
-  __TEXT.__const: 0x3e0
-  __TEXT.__gcc_except_tab: 0x2e78
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0x2ea4
   __TEXT.__cstring: 0x11e9
-  __TEXT.__oslogstring: 0x778
+  __TEXT.__oslogstring: 0x7b0
   __TEXT.__unwind_info: 0xea8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 528
-  Symbols:   1820
-  CStrings:  183
+  Symbols:   1822
+  CStrings:  184
 
Symbols:
+ ___error
+ _strerror_r
Functions:
~ -[BSUIMappedImageCacheRegistry tmpPath] : 1012 -> 1176
CStrings:
+ "BSUIMappedImageCache failed to get relative tmpDir from dirhelper with errno=%i (%{public}s) for %@"
+ "BSUIMappedImageCache is falling back to NSTemporaryDirectory=%@ for %@"
- "BSUIMappedImageCache failed to get relative tmpDir from dirhelper for %@ : falling back to NSTemporaryDirectory=%@"
```
