## ActivitySharingUI

> `/System/Library/AccessibilityBundles/ActivitySharingUI.axbundle/ActivitySharingUI`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0xff8
-  __TEXT.__auth_stubs: 0x1e0
+1029.0.0.0.0
+  __TEXT.__text: 0xf08
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__objc_classname: 0x1e7
   __TEXT.__cstring: 0x3be
   __TEXT.__objc_methname: 0x4fc
   __TEXT.__objc_methtype: 0x84
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x60
   __DATA.__objc_const: 0x630
   __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_data: 0x370

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2034CEE8-9447-36F4-AFD8-7EF397965C49
-  Functions: 37
+  UUID: 86F4458A-5AFD-39EE-9FEC-60DB23DDAB22
+  Functions: 36
   Symbols:   190
   CStrings:  153
 
Symbols:
+ __block_literal_global.352
+ __block_literal_global.354
+ __block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
- +[AXActivitySharingUIGlue accessibilityInitializeBundle].cold.1
- __block_literal_global.331
- __block_literal_global.333
- __block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
Functions:
~ +[ASCompetitionGraphViewAccessibility _accessibilityPerformValidations:] : 292 -> 284
~ -[ASCompetitionGraphViewAccessibility _axAnnotateGraphElements] : 1260 -> 1180
~ +[ASCompetitionScoreViewAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[ASCompetitionScoreViewAccessibility accessibilityLabel] : 276 -> 248
~ -[ASCompetitionMessageBubbleViewAccessibility accessibilityFrame] : 232 -> 224
~ +[ASCompetitionParticipantScoreViewAccessibility _accessibilityPerformValidations:] : 220 -> 212
~ -[ASCompetitionParticipantScoreViewAccessibility accessibilityLabel] : 92 -> 84
~ -[ASCompetitionParticipantScoreViewAccessibility accessibilityValue] : 172 -> 156
~ -[ASCompetitionParticipantScoreViewAccessibility _accessibilityPointsLabel] : 384 -> 356
~ +[AXActivitySharingUIGlue accessibilityInitializeBundle] : 44 -> 40
~ ___56+[AXActivitySharingUIGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___56+[AXActivitySharingUIGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___56+[AXActivitySharingUIGlue accessibilityInitializeBundle]_block_invoke_4 : 160 -> 152
~ _accessibilityLocalizedString : 168 -> 160

```
