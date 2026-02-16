## ActivitySharingUI

> `/System/Library/AccessibilityBundles/ActivitySharingUI.axbundle/ActivitySharingUI`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0xf20
-  __TEXT.__auth_stubs: 0x1f0
+1001.12.0.0.0
+  __TEXT.__text: 0xff8
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__objc_classname: 0x1e7

   __TEXT.__objc_methname: 0x4fc
   __TEXT.__objc_methtype: 0x84
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x4a0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5FAB8E83-0419-3AB7-9AF9-C9E72C00D7A6
+  UUID: A60A0319-CCF1-331B-B91D-77029088447F
   Functions: 37
-  Symbols:   191
+  Symbols:   190
   CStrings:  153
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
Functions:
~ +[ASCompetitionGraphViewAccessibility _accessibilityPerformValidations:] : 284 -> 292
~ -[ASCompetitionGraphViewAccessibility _axAnnotateGraphElements] : 1180 -> 1260
~ +[ASCompetitionScoreViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[ASCompetitionScoreViewAccessibility accessibilityLabel] : 248 -> 276
~ -[ASCompetitionMessageBubbleViewAccessibility accessibilityFrame] : 224 -> 232
~ +[ASCompetitionParticipantScoreViewAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[ASCompetitionParticipantScoreViewAccessibility accessibilityLabel] : 84 -> 92
~ -[ASCompetitionParticipantScoreViewAccessibility accessibilityValue] : 156 -> 172
~ -[ASCompetitionParticipantScoreViewAccessibility _accessibilityPointsLabel] : 356 -> 384
~ ___56+[AXActivitySharingUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___56+[AXActivitySharingUIGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___56+[AXActivitySharingUIGlue accessibilityInitializeBundle]_block_invoke_4 : 152 -> 160
~ _accessibilityLocalizedString : 160 -> 168

```
