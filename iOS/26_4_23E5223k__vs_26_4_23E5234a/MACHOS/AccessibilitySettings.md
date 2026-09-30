## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1817.16.0.0.0
-  __TEXT.__text: 0x1aad64
+1817.19.0.0.0
+  __TEXT.__text: 0x1aaff8
   __TEXT.__auth_stubs: 0x4e40
   __TEXT.__objc_stubs: 0x25460
-  __TEXT.__objc_methlist: 0x15854
+  __TEXT.__objc_methlist: 0x1586c
   __TEXT.__const: 0x34c4
-  __TEXT.__gcc_except_tab: 0x402c
+  __TEXT.__gcc_except_tab: 0x4088
   __TEXT.__objc_methname: 0x3567d
-  __TEXT.__cstring: 0x1876e
-  __TEXT.__oslogstring: 0x3d4f
+  __TEXT.__cstring: 0x1875e
+  __TEXT.__oslogstring: 0x3d7f
   __TEXT.__objc_classname: 0x4915
   __TEXT.__objc_methtype: 0x61ba
   __TEXT.__dlopen_cstrs: 0x28e

   __DATA_CONST.__got: 0x24b0
   __DATA_CONST.__auth_ptr: 0x7a0
   __DATA_CONST.__const: 0x5ae8
-  __DATA_CONST.__cfstring: 0x1cea0
+  __DATA_CONST.__cfstring: 0x1ce60
   __DATA_CONST.__objc_classlist: 0xeb0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x2a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6E6388DE-95EF-322F-9E62-1D25866300F1
-  Functions: 8842
-  Symbols:   19999
-  CStrings:  17113
+  UUID: CF2C0A28-A8B2-34C6-A43F-8ED0D4EF0186
+  Functions: 8844
+  Symbols:   20001
+  CStrings:  17112
 
Symbols:
+ -[AXDisplayController reduceHighlightingEffectsEnabled:]
+ -[AXDisplayController setReduceHighlightingEffectsEnabled:specifier:]
Functions:
~ -[VoiceOverBrailleController setSoundCurtainEnabled:specifier:] : 712 -> 884
~ ___63-[VoiceOverBrailleController setSoundCurtainEnabled:specifier:]_block_invoke_2 : 132 -> 100
~ -[VoiceOverBrailleController setTouchCurtainEnabled:specifier:] : 712 -> 884
~ ___63-[VoiceOverBrailleController setTouchCurtainEnabled:specifier:]_block_invoke_2 : 132 -> 100
~ -[AXDisplayController specifiers] : 2492 -> 2724
+ -[AXDisplayController reduceHighlightingEffectsEnabled:]
+ -[AXDisplayController setDimFlashingLights:specifier:]
~ -[AXDisplayTextMotionSpecifiersHelper displayTextSpecifiersIncludingSmartInvert:isPerApp:] : 5232 -> 5272
CStrings:
+ "REDUCE_HIGHLIGHTING_EFFECTS_FOOTER"
+ "Set sound curtain: %@"
+ "Set touch curtain: %@"
- "VOTSoundCurtainConfirmed"
- "VOTTouchCurtainConfirmed"

```
