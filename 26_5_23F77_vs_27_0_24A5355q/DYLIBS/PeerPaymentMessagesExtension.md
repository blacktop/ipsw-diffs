## PeerPaymentMessagesExtension

> `/System/Library/AccessibilityBundles/PeerPaymentMessagesExtension.axbundle/PeerPaymentMessagesExtension`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xc58
-  __TEXT.__auth_stubs: 0x160
+3036.2.0.0.0
+  __TEXT.__text: 0xbf4
   __TEXT.__objc_methlist: 0x1ec
-  __TEXT.__cstring: 0x32f
   __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x32f
   __TEXT.__unwind_info: 0xc0
-  __TEXT.__objc_classname: 0x1c3
-  __TEXT.__objc_methname: 0x4bc
-  __TEXT.__objc_methtype: 0x49
-  __TEXT.__objc_stubs: 0x3c0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__bss: 0xa
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8C6ABD66-7DE9-3D55-8FF7-13301D04FF88
+  UUID: 295143D0-BC29-3FA8-B6F8-1F63D127A15D
   Functions: 40
-  Symbols:   208
-  CStrings:  133
+  Symbols:   209
+  CStrings:  70
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXPeerPaymentGlue accessibilityInitializeBundle] : 148 -> 144
~ ___50+[AXPeerPaymentGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___50+[AXPeerPaymentGlue accessibilityInitializeBundle]_block_invoke_3 : 140 -> 132
~ _accessibilityPeerPaymentLocalizedString : 168 -> 160
~ -[PKPeerPaymentMessagesContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 180 -> 172
~ +[PKPeerPaymentMessagesNumberPadViewAccessibility _accessibilityPerformValidations:] : 176 -> 168
~ -[PKPeerPaymentMessagesNumberPadViewAccessibility _handleActionButton:] : 292 -> 280
~ +[PKPeerPaymentMessagesAmountStepperViewAccessibility _accessibilityPerformValidations:] : 264 -> 256
~ -[PKPeerPaymentMessagesAmountStepperViewAccessibility accessibilityValue] : 92 -> 84
~ -[PKPeerPaymentMessagesAmountStepperViewAccessibility accessibilityHint] : 136 -> 128
~ -[PKPeerPaymentMessagesAmountStepperViewAccessibility handleNumberPadAction:] : 296 -> 284
~ ___77-[PKPeerPaymentMessagesAmountStepperViewAccessibility handleNumberPadAction:]_block_invoke : 176 -> 164
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXPeerPaymentGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__PKPeerPaymentMessagesAmountStepperViewAccessibility_super"
- "__PKPeerPaymentMessagesContentViewAccessibility_super"
- "__PKPeerPaymentMessagesNumberPadViewAccessibility_super"
- "__PKPeerPaymentNumberPadActionButtonAccessibility_super"
- "_accessibilityKeyboardKeyAllowsTouchTyping"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_axHasInvalidAmount"
- "_axSpeakAmountTimer"
- "_setAXHasInvalidAmount:"
- "_setAXSpeakAmountTimer:"
- "accessibilityBundles"
- "accessibilityDecrement"
- "accessibilityHint"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "afterDelay:processBlock:"
- "axAttributedStringWithString:"
- "boolValue"
- "bundleForClass:"
- "dealloc"
- "initWithTargetSerialQueue:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setAutomaticallyCancelPendingBlockUponSchedulingNewBlock:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
