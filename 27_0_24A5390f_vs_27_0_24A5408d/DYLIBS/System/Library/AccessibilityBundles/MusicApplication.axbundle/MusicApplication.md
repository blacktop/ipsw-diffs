## MusicApplication

> `/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x122a0
-  __TEXT.__objc_methlist: 0x2960
+3048.0.0.0.0
+  __TEXT.__text: 0x12598
+  __TEXT.__objc_methlist: 0x2980
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__cstring: 0x43ee
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b8
+  __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__got: 0x238
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x4f60
   __AUTH_CONST.__objc_const: 0x7270

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 761
-  Symbols:   2190
+  Functions: 764
+  Symbols:   2205
   CStrings:  684
 
Symbols:
+ -[PlayerTimeControlAccessibility accessibilityAttributedValue]
+ -[SongCellAccessibility _axLabelWithDurationString:]
+ -[SongCellAccessibility accessibilityAttributedLabel]
+ GCC_except_table519
+ GCC_except_table537
+ GCC_except_table665
+ _AXCompactDurationStringForDuration
+ _OBJC_CLASS_$_AXAttributedString
+ _UIAccessibilityTokenDurationTimeHHMMSS
+ _UIAccessibilityTokenDurationTimeMMSS
+ ___kCFBooleanTrue
+ _objc_msgSend$_axLabelWithDurationString:
+ _objc_msgSend$attributedString
+ _objc_msgSend$axAttributedStringWithString:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$localizedAttributedStringWithFormat:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$setAttribute:forKey:withRange:
- GCC_except_table516
- GCC_except_table534
- GCC_except_table662
```
