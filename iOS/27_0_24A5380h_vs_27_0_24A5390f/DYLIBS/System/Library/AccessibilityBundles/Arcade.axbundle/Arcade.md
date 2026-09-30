## Arcade

> `/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0xa864
+3045.0.0.0.0
+  __TEXT.__text: 0xa89c
   __TEXT.__objc_methlist: 0x2784
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x36a5
+  __TEXT.__cstring: 0x36db
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x5b8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x77d0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x4290

   - /usr/lib/libobjc.A.dylib
   Functions: 663
   Symbols:   1982
-  CStrings:  494
+  CStrings:  496
 
Functions:
~ +[StoryCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 300 -> 332
~ -[StoryCardCollectionViewCellAccessibility accessibilityElements] : 416 -> 440
CStrings:
+ "Arcade.EditorialVideoView"
+ "Arcade.TodayCardEditorialVideoView"
+ "EditorialVideoView"
+ "Optional<VideoView>"
+ "TodayCardEditorialVideoView"
+ "editorialVideoView"
- "Arcade.RevealingVideoView"
- "Optional<TodayCardVideoView>"
- "RevealingVideoView"
- "revealingVideoView"
```
