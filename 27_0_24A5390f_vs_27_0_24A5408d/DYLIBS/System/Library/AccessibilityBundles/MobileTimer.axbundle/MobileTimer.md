## MobileTimer

> `/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x8d28
-  __TEXT.__objc_methlist: 0xfa8
+3048.0.0.0.0
+  __TEXT.__text: 0x8eb0
+  __TEXT.__objc_methlist: 0xfb8
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__cstring: 0x17ae
+  __TEXT.__cstring: 0x17d9
   __TEXT.__unwind_info: 0x3f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2520
+  __AUTH_CONST.__cfstring: 0x2580
   __AUTH_CONST.__objc_const: 0x2c00
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 304
-  Symbols:   1043
-  CStrings:  321
+  Functions: 305
+  Symbols:   1047
+  CStrings:  324
 
Symbols:
+ -[MTATimerButtonsControllerAccessibility _axUpdateCancelButtonState]
+ -[MTATimerButtonsControllerAccessibility _axUpdateStartStopButtonState]
+ GCC_except_table174
+ GCC_except_table218
+ GCC_except_table246
+ ___block_descriptor_48_e8_32s40w_e15_"NSString"8?0lw40l8s32l8
+ _objc_msgSend$_axUpdateCancelButtonState
+ _objc_msgSend$_axUpdateStartStopButtonState
+ _objc_msgSend$reuseIdentifier
+ _objc_msgSend$textLabel
- -[MTATimerButtonsControllerAccessibility _updateCancelButtonState]
- GCC_except_table173
- GCC_except_table217
- GCC_except_table245
- ___block_descriptor_48_e8_32s40w_e15_"NSString"8?0ls32l8w40l8
- _objc_msgSend$_updateCancelButtonState
CStrings:
+ "MTDTVC"
+ "_startStopButton"
+ "sunriseSunsetLabel"
+ "timer.cancel"
+ "timer.start"
- "sunriseLabel"
- "sunsetLabel"
```
