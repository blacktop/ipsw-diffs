## PeerPaymentMessagesExtension

> `/System/Library/AccessibilityBundles/PeerPaymentMessagesExtension.axbundle/PeerPaymentMessagesExtension`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xbec
-  __TEXT.__auth_stubs: 0x170
+3005.16.0.0.0
+  __TEXT.__text: 0xc58
+  __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__cstring: 0x32f
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABC0C646-8730-3968-B4CF-8E1AF1EEC134
+  UUID: 60DDEC14-9AD2-3656-893C-1C696E0F1C95
   Functions: 40
-  Symbols:   209
+  Symbols:   208
   CStrings:  133
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXPeerPaymentGlue accessibilityInitializeBundle] : 144 -> 148
~ ___50+[AXPeerPaymentGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___50+[AXPeerPaymentGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ _accessibilityPeerPaymentLocalizedString : 160 -> 168
~ -[PKPeerPaymentMessagesContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 172 -> 180
~ +[PKPeerPaymentMessagesNumberPadViewAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[PKPeerPaymentMessagesNumberPadViewAccessibility _handleActionButton:] : 280 -> 292
~ -[PKPeerPaymentNumberPadActionButtonAccessibility accessibilityLabel] : 148 -> 156
~ +[PKPeerPaymentMessagesAmountStepperViewAccessibility _accessibilityPerformValidations:] : 256 -> 264
~ -[PKPeerPaymentMessagesAmountStepperViewAccessibility accessibilityValue] : 84 -> 92
~ -[PKPeerPaymentMessagesAmountStepperViewAccessibility accessibilityHint] : 128 -> 136
~ -[PKPeerPaymentMessagesAmountStepperViewAccessibility handleNumberPadAction:] : 284 -> 296
~ ___77-[PKPeerPaymentMessagesAmountStepperViewAccessibility handleNumberPadAction:]_block_invoke : 164 -> 176

```
