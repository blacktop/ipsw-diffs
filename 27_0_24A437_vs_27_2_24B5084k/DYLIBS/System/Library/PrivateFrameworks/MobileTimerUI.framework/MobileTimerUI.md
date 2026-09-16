## MobileTimerUI

> `/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI`

```diff

-2333.0.0.0.0
-  __TEXT.__text: 0xbf8c
+2333.2.3.0.0
+  __TEXT.__text: 0xbfb4
   __TEXT.__objc_methlist: 0x1850
-  __TEXT.__const: 0x1b8
+  __TEXT.__const: 0x1c0
   __TEXT.__cstring: 0x585
+  __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x124
   __TEXT.__unwind_info: 0x540
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__got: 0x338
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__objc_const: 0x2620
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 459
   Symbols:   1527
-  CStrings:  93
+  CStrings:  94
 
Symbols:
+ _objc_msgSend$mtui_lightTimeFont
- _objc_msgSend$mtui_thinTimeFont
Functions:
~ +[UIFont(MTUIFonts) mtui_thinTimeFont] : 76 -> 44
~ +[UIFont(MTUIFonts) mtui_thinTimeFontOfSize:] : 36 -> 100
~ -[MTUIDateLabel _updateDateString] : 696 -> 736
~ +[UIFont(MTUIFonts) mtui_lightTimeFont] : 76 -> 44
CStrings:
+ "\u2009"
```
