## ControlCenterUIKit

> `/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit`

```diff

-  __TEXT.__text: 0x5784
+  __TEXT.__text: 0x586c
   __TEXT.__objc_methlist: 0x82c
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__cstring: 0xecf
+  __TEXT.__cstring: 0xe8c
   __TEXT.__oslogstring: 0x8
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__got: 0xc8
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xf40
+  __DATA_CONST.__got: 0xd0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0xee0
   __AUTH_CONST.__objc_const: 0x1150
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x870
+  __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 185
-  Symbols:   768
-  CStrings:  270
+  Symbols:   770
+  CStrings:  263
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__objc_const : content changed
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_enumerationMutation
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_release_x25
- _objc_msgSend$_glyphViewForExpandedConnectivityModuleTapped
- _objc_msgSend$firstObject
- _objc_msgSend$gestureRecognizers
- _objc_retain_x23
Functions:
~ +[CCUIControlTemplateViewAccessibility _accessibilityPerformValidations:] : 428 -> 340
~ -[CCUIControlTemplateViewAccessibility accessibilityActivate] : 404 -> 652
~ ___61-[CCUIControlTemplateViewAccessibility accessibilityActivate]_block_invoke : 8 -> 80
CStrings:
+ "CCUIConnectivityModuleViewController"
+ "contentViewController"
+ "orderedButtonViewControllers"
- "CCUIAirDropModuleViewController"
- "NSMutableArray"
- "UIGestureRecognizer"
- "UIGestureRecognizerTarget"
- "_glyphViewForExpandedConnectivityModuleTapped"
- "_targets"
- "target"

```
