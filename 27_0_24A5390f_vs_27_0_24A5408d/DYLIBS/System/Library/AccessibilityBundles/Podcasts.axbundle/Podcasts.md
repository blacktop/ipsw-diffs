## Podcasts

> `/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x7c64
-  __TEXT.__objc_methlist: 0x12cc
+3048.0.0.0.0
+  __TEXT.__text: 0x7d0c
+  __TEXT.__objc_methlist: 0x12dc
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x1b0
   __TEXT.__cstring: 0x1cf2
-  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__unwind_info: 0x400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x530
+  __DATA_CONST.__objc_selrefs: 0x548
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__got: 0xf0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x2500
   __AUTH_CONST.__objc_const: 0x3878

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 306
-  Symbols:   1028
+  Functions: 308
+  Symbols:   1035
   CStrings:  322
 
Symbols:
+ -[EpisodeInfoViewAccessibility accessibilityTraits]
+ -[PlayControlsStackViewAccessibility accessibilityActivate]
+ GCC_except_table114
+ GCC_except_table141
+ GCC_except_table162
+ GCC_except_table186
+ GCC_except_table213
+ GCC_except_table271
+ GCC_except_table299
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table74
+ GCC_except_table78
+ _AXCompactDurationStringForDuration
+ _UIAccessibilityTraitStaticText
+ _objc_msgSend$attributedString
+ _objc_msgSend$setAccessibilityAttributedLabel:
+ _objc_msgSend$string
- GCC_except_table112
- GCC_except_table139
- GCC_except_table160
- GCC_except_table184
- GCC_except_table211
- GCC_except_table269
- GCC_except_table297
- GCC_except_table59
- GCC_except_table62
- GCC_except_table73
- GCC_except_table77
Functions:
+ -[PlayControlsStackViewAccessibility accessibilityActivate]
+ -[EpisodeInfoViewAccessibility accessibilityTraits]
~ -[MTAVPlayerTOCViewControllerAccessibility configureCell:withObject:atIndexPath:] : 212 -> 308
```
