## MobileTimerUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/MobileTimerUI.framework/Versions/A/MobileTimerUI`

```diff

-2333.0.0.0.0
-  __TEXT.__text: 0xb5b8
+2333.2.3.0.0
+  __TEXT.__text: 0xb5e0
   __TEXT.__objc_methlist: 0x1370
-  __TEXT.__const: 0x1b8
+  __TEXT.__const: 0x1c0
   __TEXT.__cstring: 0x50b
+  __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x4b
   __TEXT.__unwind_info: 0x4e8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__got: 0x338
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x1d68
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 419
   Symbols:   1432
-  CStrings:  78
+  CStrings:  79
 
Symbols:
+ _objc_msgSend$mtui_lightTimeFont
- _objc_msgSend$mtui_thinTimeFont
Functions:
~ -[MTUIDateLabel _updateDateString] : 696 -> 736
~ +[UIFont(MTUIFonts) mtui_thinTimeFontOfSize:] : 36 -> 100
~ +[UIFont(MTUIFonts) mtui_thinTimeFont] : 76 -> 44
~ +[UIFont(MTUIFonts) mtui_lightTimeFont] : 76 -> 44
CStrings:
+ "\u2009"
```
