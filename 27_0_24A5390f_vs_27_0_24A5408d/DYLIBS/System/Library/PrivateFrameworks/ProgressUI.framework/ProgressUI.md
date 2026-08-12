## ProgressUI

> `/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI`

```diff

-2854.0.0.0.0
-  __TEXT.__text: 0x322c
+2858.0.0.0.0
+  __TEXT.__text: 0x325c
   __TEXT.__objc_methlist: 0x41c
   __TEXT.__const: 0x248
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x978
+  __TEXT.__cstring: 0x99e
   __TEXT.__unwind_info: 0x148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0xb30
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x88

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore

   - /usr/lib/libobjc.A.dylib
   Functions: 58
   Symbols:   369
-  CStrings:  87
+  CStrings:  88
 
Functions:
~ -[PUIProgressWindow _initWithOptions:contextLevel:appearance:environment:] : 652 -> 700
CStrings:
+ "PUIProgressWindow got product type %@"
```
