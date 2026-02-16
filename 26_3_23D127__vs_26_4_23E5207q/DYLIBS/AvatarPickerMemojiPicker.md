## AvatarPickerMemojiPicker

> `/System/Library/AccessibilityBundles/AvatarPickerMemojiPicker.axbundle/AvatarPickerMemojiPicker`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x84c
-  __TEXT.__auth_stubs: 0x1e0
+3005.16.0.0.0
+  __TEXT.__text: 0x88c
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__auth_got: 0xe8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65F06D59-9F5A-3BE1-A0E2-D940EB47300B
+  UUID: 84E9F5D3-16B4-3EE0-AD59-6A269E0AC8BF
   Functions: 16
-  Symbols:   126
+  Symbols:   123
   CStrings:  70
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_release_x22
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ +[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility _accessibilityPerformValidations:] : 204 -> 216
~ -[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 420 -> 436
~ -[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility _axMarkupCell:atIndexPath:] : 288 -> 280
~ ___86-[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility _axMarkupCell:atIndexPath:]_block_invoke : 84 -> 88
~ -[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility _axLabelForIndexPath:] : 404 -> 420
~ ___81-[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility _axLabelForIndexPath:]_block_invoke : 80 -> 84
~ -[AVTUIAvatarPickerMemojiPickerViewControllerAccessibility collectionView:cellForItemAtIndexPath:] : 148 -> 152
~ +[AXAvatarPickerMemojiPickerGlue accessibilityInitializeBundle] : 148 -> 152
~ ___63+[AXAvatarPickerMemojiPickerGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
