## Moments

> `/System/Library/AccessibilityBundles/Moments.axbundle/Moments`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`

```diff

 3005.31.0.0.0
-  __TEXT.__text: 0x1324
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x450
-  __TEXT.__cstring: 0x665
+  __TEXT.__text: 0x1b34
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_methlist: 0x494
+  __TEXT.__cstring: 0x70d
   __TEXT.__ustring: 0x8
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0x120
   __TEXT.__objc_classname: 0x4ab
-  __TEXT.__objc_methname: 0x3cb
+  __TEXT.__objc_methname: 0x48a
   __TEXT.__objc_methtype: 0x3e
-  __TEXT.__objc_stubs: 0x340
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xa8
+  __TEXT.__objc_stubs: 0x440
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xe8
+  __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0xe10
   __AUTH.__objc_data: 0x7d0
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 76
-  Symbols:   282
-  CStrings:  109
+  Functions: 84
+  Symbols:   310
+  CStrings:  127
 
Symbols:
+ -[MOSuggestionCollectionViewCellAccessibility accessibilityCustomActions]
+ -[MOSuggestionCollectionViewCellAccessibility accessibilityHint]
+ -[MOSuggestionCollectionViewCellAccessibility accessibilityLabel]
+ -[MOSuggestionCollectionViewSingleAssetCellAccessibility accessibilityLabel]
+ -[MapImageViewAccessibility accessibilityLabel]
+ -[ReflectionPromptViewAccessibility accessibilityCustomActions]
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UIAccessibilityCustomAction
+ _OBJC_CLASS_$_UIButton
+ ___73-[MOSuggestionCollectionViewCellAccessibility accessibilityCustomActions]_block_invoke
+ ___block_descriptor_40_e8_32s_e37_B16?0"UIAccessibilityCustomAction"8ls32l8
+ _accessibilityJurassicLocalizedString
+ _accessibilityJurassicLocalizedString.axBundle
+ _objc_alloc
+ _objc_msgSend$addObject:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$count
+ _objc_msgSend$initWithName:actionHandler:
+ _objc_msgSend$initWithName:target:selector:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$sendActionsForControlEvents:
+ _objc_msgSend$stringWithFormat:
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x8
+ _objc_retain_x22
CStrings:
+ ""
+ "%lu"
+ "Accessibility-Jurassic"
+ "B16@?0@\"UIAccessibilityCustomAction\"8"
+ "accessibilityHint"
+ "addObject:"
+ "bundleForClass:"
+ "count"
+ "initWithName:actionHandler:"
+ "initWithName:target:selector:"
+ "localizedStringForKey:value:table:"
+ "map"
+ "sendActionsForControlEvents:"
+ "shuffle.reflection"
+ "stringWithFormat:"
+ "suggestion.cell.collapsed.hint"
+ "suggestion.elements"
+ "suggestion.write.about.this"
```
