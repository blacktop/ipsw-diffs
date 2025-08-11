## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

-95.0.0.0.1
-  __TEXT.__text: 0x10b58
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x1da0
+96.0.0.0.1
+  __TEXT.__text: 0x11744
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x3c20
+  __TEXT.__objc_methlist: 0x1e30
   __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0x5cf1
-  __TEXT.__oslogstring: 0x22d2
-  __TEXT.__cstring: 0x1e41
-  __TEXT.__objc_classname: 0x439
-  __TEXT.__objc_methtype: 0x20c9
+  __TEXT.__objc_methname: 0x5f56
+  __TEXT.__oslogstring: 0x2598
+  __TEXT.__cstring: 0x1fac
+  __TEXT.__objc_classname: 0x437
+  __TEXT.__objc_methtype: 0x20de
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x410
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x348
+  __TEXT.__unwind_info: 0x418
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x718
-  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__cfstring: 0xc40
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA.__objc_const: 0x3778
-  __DATA.__objc_selrefs: 0x1710
-  __DATA.__objc_ivar: 0x108
+  __DATA.__objc_const: 0x3808
+  __DATA.__objc_selrefs: 0x1790
+  __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x978
   __DATA.__bss: 0x78

   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit
   - /System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CE4235D-E9AB-364C-AD76-CAF701210B5C
-  Functions: 449
-  Symbols:   227
-  CStrings:  1621
+  UUID: 6A1B5900-D540-3740-B46B-0C6BC52669EA
+  Functions: 462
+  Symbols:   240
+  CStrings:  1671
 
Symbols:
+ _UIAccessibilitySpeechAttributeSpellOut
+ __AXSAssistiveTouchEnabled
+ __AXSAssistiveTouchScannerEnabled
+ __AXSAssistiveTouchScannerSetEnabled
+ __AXSAssistiveTouchSetEnabled
+ __AXSCommandAndControlEnabled
+ __AXSCommandAndControlSetEnabled
+ __AXSInvertColorsEnabled
+ __AXSInvertColorsSetEnabled
+ __AXSVoiceOverTouchEnabled
+ __AXSVoiceOverTouchSetEnabled
+ __AXSVoiceOverTouchSetUsageConfirmed
+ ___kCFBooleanTrue
CStrings:
+ "%{public}s: Accessibility settings already imported. Skipping..."
+ "%{public}s: Current VoiceOver state: %s. Toggling..."
+ "%{public}s: Enabling VoiceOver after first triple-press"
+ "%{public}s: First triple-press detected. Loading accessibility settings from daemon and enabling voiceover"
+ "%{public}s: Handling triple press action."
+ "%{public}s: Invalidated power button press count timer."
+ "%{public}s: Power button press count timer expired. Resetting count from %ld to 0."
+ "%{public}s: Power button press count: %ld"
+ "%{public}s: Reset power button press count."
+ "%{public}s: Started power button press count timer (1 second timeout)."
+ "%{public}s: Triple press detected! Performing action."
+ "%{public}s: VoiceOver toggled to: %s"
+ "-[Application _handleTriplePress]"
+ "-[Application _handleTriplePress]_block_invoke"
+ "-[Application _initializeAccessibilityFeatures]"
+ "-[Application _invalidatePowerButtonPressTimer]"
+ "-[Application _powerButtonPressCountTimerFired:]"
+ "-[Application _resetPowerButtonPressCount]"
+ "-[Application _startPowerButtonPressCountTimer]"
+ "AX_LANGUAGE_BUTTON"
+ "AX_QRCODE"
+ "T@\"NSTimer\",&,N,V_powerButtonPressTimer"
+ "TB,N,V_axSettingsImported"
+ "Tq,N,V_powerButtonPressCount"
+ "_axSettingsImported"
+ "_handleTriplePress"
+ "_initializeAccessibilityFeatures"
+ "_invalidatePowerButtonPressTimer"
+ "_powerButtonPressCount"
+ "_powerButtonPressCountTimerFired:"
+ "_powerButtonPressTimer"
+ "_resetPowerButtonPressCount"
+ "_startPowerButtonPressCountTimer"
+ "axSettingsImported"
+ "disabled"
+ "enabled"
+ "loadAccessibilitySettingsToDefaultsWithCompletion:"
+ "powerButtonPressCount"
+ "powerButtonPressTimer"
+ "q"
+ "q16@0:8"
+ "setAccessibilityAttributedLabel:"
+ "setAccessibilityLabel:"
+ "setAxSettingsImported:"
+ "setIsAccessibilityElement:"
+ "setPowerButtonPressCount:"
+ "setPowerButtonPressTimer:"
+ "v24@0:8q16"

```
