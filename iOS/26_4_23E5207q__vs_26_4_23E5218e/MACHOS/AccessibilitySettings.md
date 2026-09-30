## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1817.13.0.0.0
-  __TEXT.__text: 0x1aa01c
-  __TEXT.__auth_stubs: 0x4e00
-  __TEXT.__objc_stubs: 0x25380
-  __TEXT.__objc_methlist: 0x157f4
+1817.15.0.0.0
+  __TEXT.__text: 0x1aa9a8
+  __TEXT.__auth_stubs: 0x4e40
+  __TEXT.__objc_stubs: 0x25400
+  __TEXT.__objc_methlist: 0x15824
   __TEXT.__const: 0x34c4
-  __TEXT.__gcc_except_tab: 0x3fcc
-  __TEXT.__objc_methname: 0x35537
-  __TEXT.__cstring: 0x186de
+  __TEXT.__gcc_except_tab: 0x4000
+  __TEXT.__objc_methname: 0x3562d
+  __TEXT.__cstring: 0x1876e
   __TEXT.__oslogstring: 0x3d4f
   __TEXT.__objc_classname: 0x4915
   __TEXT.__objc_methtype: 0x61ba

   __TEXT.__swift5_types: 0x124
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x6718
+  __TEXT.__unwind_info: 0x6730
   __TEXT.__eh_frame: 0xc04
-  __DATA_CONST.__auth_got: 0x2710
+  __DATA_CONST.__auth_got: 0x2730
   __DATA_CONST.__got: 0x24b0
   __DATA_CONST.__auth_ptr: 0x7a0
   __DATA_CONST.__const: 0x5ae8
-  __DATA_CONST.__cfstring: 0x1cdc0
+  __DATA_CONST.__cfstring: 0x1cea0
   __DATA_CONST.__objc_classlist: 0xeb0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x2a0

   __DATA_CONST.__objc_dictobj: 0xaa0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x1e258
-  __DATA.__objc_selrefs: 0xcda0
+  __DATA.__objc_selrefs: 0xcde0
   __DATA.__objc_ivar: 0xdf8
   __DATA.__objc_data: 0x9f28
   __DATA.__data: 0x3e90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D9C10F4-ABDD-329B-8BFB-0D29EF00D5BE
-  Functions: 8826
-  Symbols:   19971
-  CStrings:  17089
+  UUID: 05B25826-C3F7-3037-AAD4-1F0AA17670BD
+  Functions: 8835
+  Symbols:   19989
+  CStrings:  17110
 
Symbols:
+ -[AXDisplayController dimFlashingLights:]
+ -[AXDisplayController setDimFlashingLights:specifier:]
+ -[AXDisplayTextMotionSpecifiersHelper reduceHighlightingEffectsEnabled:]
+ -[AXDisplayTextMotionSpecifiersHelper setReduceHighlightingEffectsEnabled:specifier:]
+ -[VoiceOverBrailleController setTouchCurtainEnabled:specifier:]
+ -[VoiceOverBrailleController touchCurtainEnabled:]
+ __146-[ClarityUIController _checkExistenceOfSettingsForAppSpecifier:identifier:bundleIdentifiersCheckingExistenceOfSettings:specifiersRequiringReload:]_block_invoke.618
+ __AXSReduceHighlightingEffectsEnabledApp
+ __AXSReduceHighlightingEffectsEnabledGlobal
+ __AXSSetReduceHighlightingEffectsEnabled
+ __AXSSetReduceHighlightingEffectsEnabledApp
+ ___63-[VoiceOverBrailleController setTouchCurtainEnabled:specifier:]_block_invoke
+ ___63-[VoiceOverBrailleController setTouchCurtainEnabled:specifier:]_block_invoke_2
+ ___68-[AXDisplayTextMotionSpecifiersHelper setBoldTextEnabled:specifier:]_block_invoke
+ ___90-[AXDisplayTextMotionSpecifiersHelper displayTextSpecifiersIncludingSmartInvert:isPerApp:]_block_invoke_19
+ ___90-[AXDisplayTextMotionSpecifiersHelper displayTextSpecifiersIncludingSmartInvert:isPerApp:]_block_invoke_20
+ _objc_msgSend$reduceHighlightingEffectsEnabled:
+ _objc_msgSend$setReduceHighlightingEffectsEnabled:specifier:
+ _objc_msgSend$setVoiceOverTouchCurtain:
+ _objc_msgSend$voiceOverTouchCurtain
- -[AXDisplayTextMotionSpecifiersHelper preferenceValue:]
- -[AXDisplayTextMotionSpecifiersHelper setPreferenceValue:specifier:]
- GCC_except_table29
- __146-[ClarityUIController _checkExistenceOfSettingsForAppSpecifier:identifier:bundleIdentifiersCheckingExistenceOfSettings:specifiersRequiringReload:]_block_invoke.614
CStrings:
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/ASTCustomizeCell.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXCallAudioRoutingController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXKeyRepeatController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXListItemController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXNamedItemsListController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXPronunciationEntryViewController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXPronunciationSuggestionsViewController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXReorderableCheckmarkListController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXSensitivitySliderCell.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AXSettingsLocalization.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/AccessibilitySettingsUtilities.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/ButtonClickController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/CustomGestureController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATAlertCoordinator.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATCustomizeDeviceMenuController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATCustomizeMenuBaseController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATCustomizeTopLevelMenuController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATLaunchRecipeController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATMIDISwitchChannelViewController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATMIDISwitchKeyViewController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATRecipeEditController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATRecipeLongPressController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATRecipeSwitchesController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/SCATSwitchDetailsViewController.m"
+ "/Library/Caches/com.apple.xbs/F2618726-D4DC-4935-9EF2-EE9A539BD6B6/TemporaryDirectory.B6DD4P/Sources/AccessibilitySettings/Source/VoiceOverGestureHelpView.m"
+ "CONFIRM_TOUCH_CURTAIN_MESSAGE"
+ "REDUCE_HIGHLIGHTING_EFFECTS"
+ "TOUCH_CURTAIN"
+ "VOTSoundCurtainConfirmed"
+ "VOTTouchCurtainConfirmed"
+ "VO_TOUCH_CURTAIN_FOOTER"
+ "dimFlashingLights:"
+ "reduceHighlightingEffectsEnabled:"
+ "setDimFlashingLights:specifier:"
+ "setReduceHighlightingEffectsEnabled:specifier:"
+ "setTouchCurtainEnabled:specifier:"
+ "setVoiceOverTouchCurtain:"
+ "touchCurtainEnabled:"
+ "voiceOverTouchCurtain"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/ASTCustomizeCell.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXCallAudioRoutingController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXKeyRepeatController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXListItemController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXNamedItemsListController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXPronunciationEntryViewController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXPronunciationSuggestionsViewController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXReorderableCheckmarkListController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXSensitivitySliderCell.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AXSettingsLocalization.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/AccessibilitySettingsUtilities.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/ButtonClickController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/CustomGestureController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATAlertCoordinator.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATCustomizeDeviceMenuController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATCustomizeMenuBaseController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATCustomizeTopLevelMenuController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATLaunchRecipeController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATMIDISwitchChannelViewController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATMIDISwitchKeyViewController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATRecipeEditController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATRecipeLongPressController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATRecipeSwitchesController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/SCATSwitchDetailsViewController.m"
- "/Library/Caches/com.apple.xbs/F243BF64-9921-4660-A179-2C6582476DDA/TemporaryDirectory.GAhMDu/Sources/AccessibilitySettings/Source/VoiceOverGestureHelpView.m"

```
