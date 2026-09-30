## BaseBoardUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/BaseBoardUI.framework/Versions/A/BaseBoardUI`

```diff

-827.0.0.0.0
-  __TEXT.__text: 0x17c28
+827.2.1.0.0
+  __TEXT.__text: 0x17ccc
   __TEXT.__objc_methlist: 0x18bc
-  __TEXT.__const: 0x3e0
-  __TEXT.__gcc_except_tab: 0x2cc0
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0x2cec
   __TEXT.__cstring: 0x11ae
-  __TEXT.__oslogstring: 0x778
+  __TEXT.__oslogstring: 0x7b0
   __TEXT.__unwind_info: 0xe10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

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
~ -[BSUIMappedImageCacheRegistry tmpPath] : 1012 -> 1176
CStrings:
+ "BSUIMappedImageCache failed to get relative tmpDir from dirhelper with errno=%i (%{public}s) for %@"
+ "BSUIMappedImageCache is falling back to NSTemporaryDirectory=%@ for %@"
- "BSUIMappedImageCache failed to get relative tmpDir from dirhelper for %@ : falling back to NSTemporaryDirectory=%@"
```
