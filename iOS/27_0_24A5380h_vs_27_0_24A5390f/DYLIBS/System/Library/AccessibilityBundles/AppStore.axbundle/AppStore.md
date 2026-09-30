## AppStore

> `/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore`

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
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0xbe18
+3045.0.0.0.0
+  __TEXT.__text: 0xbe50
   __TEXT.__objc_methlist: 0x282c
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x3972
+  __TEXT.__cstring: 0x39aa
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x6c8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x3aa0
+  __AUTH_CONST.__cfstring: 0x3ac0
   __AUTH_CONST.__objc_const: 0x7a10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0

   - /usr/lib/libobjc.A.dylib
   Functions: 674
   Symbols:   2015
-  CStrings:  516
+  CStrings:  518
 
Functions:
~ +[StoryCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 300 -> 332
~ -[StoryCardCollectionViewCellAccessibility accessibilityElements] : 416 -> 440
CStrings:
+ "AppStore.EditorialVideoView"
+ "AppStore.TodayCardEditorialVideoView"
+ "EditorialVideoView"
+ "Optional<VideoView>"
+ "TodayCardEditorialVideoView"
+ "editorialVideoView"
- "AppStore.RevealingVideoView"
- "Optional<TodayCardVideoView>"
- "RevealingVideoView"
- "revealingVideoView"
```
