## PlatterKit

> `/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit`

```diff

-374.101.0.0.0
-  __TEXT.__text: 0x25988
+375.2.1.0.0
+  __TEXT.__text: 0x25a98
   __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0x3928
   __TEXT.__const: 0x1f8

   __TEXT.__oslogstring: 0x512
   __TEXT.__unwind_info: 0xd28
   __TEXT.__objc_classname: 0x860
-  __TEXT.__objc_methname: 0xb132
+  __TEXT.__objc_methname: 0xb106
   __TEXT.__objc_methtype: 0x234d
   __TEXT.__objc_stubs: 0x7c40
   __DATA_CONST.__got: 0x4f8

   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15DCD495-D626-3A88-9BA4-BE81BDF0EF12
+  UUID: 8FCB5EFF-CD1B-3C8D-864E-677C885CD067
   Functions: 1139
   Symbols:   4578
-  CStrings:  2111
+  CStrings:  2110
 
Symbols:
+ -[PLPlatterActionButton customBackgroundView]
+ -[PLPlatterActionButton setCustomBackgroundView:]
+ -[PLPlatterActionButtonsView customBackgroundView]
+ -[PLPlatterActionButtonsView setCustomBackgroundView:]
+ _OBJC_IVAR_$_PLPlatterActionButton._customBackgroundView
+ _OBJC_IVAR_$_PLPlatterActionButtonsView._customBackgroundView
+ _objc_msgSend$buttonCustomBackgroundViewForSwipeInteraction:
+ _objc_msgSend$customBackgroundView
+ _objc_msgSend$setCustomBackgroundView:
- -[PLPlatterActionButton customBackgroundColor]
- -[PLPlatterActionButton setCustomBackgroundColor:]
- -[PLPlatterActionButtonsView customBackgroundColor]
- -[PLPlatterActionButtonsView setCustomBackgroundColor:]
- _OBJC_IVAR_$_PLPlatterActionButton._customBackgroundColor
- _OBJC_IVAR_$_PLPlatterActionButtonsView._customBackgroundColor
- _objc_msgSend$buttonCustomBackgroundColorForSwipeInteraction:
- _objc_msgSend$customBackgroundColor
- _objc_msgSend$setCustomBackgroundColor:
Functions:
~ -[PLPlatterActionButton _configureTitleLabelEffects] : 240 -> 400
~ -[PLPlatterActionButton _configureBackgroundViewIfNecessary] : 648 -> 656
~ -[PLPlatterActionButtonsView setCustomBackgroundColor:] -> -[PLPlatterActionButtonsView setCustomBackgroundView:] : 308 -> 348
~ -[PLPlatterActionButtonsView .cxx_destruct] : 184 -> 204
~ -[PLSwipeInteraction _handlePanGesture:] : 1220 -> 1264
CStrings:
+ "T@\"UIView\",C,N,V_customBackgroundView"
+ "_customBackgroundView"
+ "buttonCustomBackgroundViewForSwipeInteraction:"
+ "customBackgroundView"
+ "setCustomBackgroundView:"
- "T@\"UIColor\",&,N,V_customBackgroundColor"
- "T@\"UIColor\",N,V_customBackgroundColor"
- "_customBackgroundColor"
- "buttonCustomBackgroundColorForSwipeInteraction:"
- "customBackgroundColor"
- "setCustomBackgroundColor:"

```
