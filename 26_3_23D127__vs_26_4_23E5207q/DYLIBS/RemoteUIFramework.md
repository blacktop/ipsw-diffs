## RemoteUIFramework

> `/System/Library/AccessibilityBundles/RemoteUIFramework.axbundle/RemoteUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x188c
-  __TEXT.__auth_stubs: 0x250
+3005.16.0.0.0
+  __TEXT.__text: 0x197c
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__cstring: 0x318
   __TEXT.__const: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DD82382-2C47-32F2-8B11-FD6AB0838BD9
+  UUID: 03A6323D-D93D-338B-AEF0-999EFDE3A741
   Functions: 42
-  Symbols:   252
+  Symbols:   251
   CStrings:  167
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x8
Functions:
~ +[AXRemoteUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___47+[AXRemoteUIGlue accessibilityInitializeBundle]_block_invoke : 180 -> 184
~ ___47+[AXRemoteUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___47+[AXRemoteUIGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ _accessibilityLocalizedString : 160 -> 168
~ -[RUIPageAccessibility accessibilityPerformEscape] : 392 -> 420
~ +[RUIWebContainerViewAccessibility _accessibilityPerformValidations:] : 228 -> 240
~ -[RUIWebContainerViewAccessibility isAccessibilityElement] : 200 -> 212
~ -[RUIWebContainerViewAccessibility _axSubviewText] : 140 -> 156
~ -[RUIWebContainerViewAccessibility accessibilityActivationPoint] : 296 -> 316
~ -[RUIWebContainerViewAccessibility accessibilityLabel] : 112 -> 120
~ +[RemoteUITableViewCellAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[RemoteUITableViewCellAccessibility _accessoriesChanged] : 160 -> 168
~ -[RemoteUITableViewCellAccessibility setRemoteUIAccessoryView:] : 152 -> 156
~ -[RemoteUITableViewCellAccessibility accessibilityTraits] : 712 -> 732
~ ___57-[RemoteUITableViewCellAccessibility accessibilityTraits]_block_invoke : 116 -> 124
~ -[RemoteUITableViewCellAccessibility _privateAccessibilityCustomActions] : 348 -> 344
~ ___72-[RemoteUITableViewCellAccessibility _privateAccessibilityCustomActions]_block_invoke : 80 -> 84
~ -[RemoteUITableViewCellAccessibility accessibilityLabel] : 536 -> 564
~ ___56-[RemoteUITableViewCellAccessibility accessibilityLabel]_block_invoke : 80 -> 84
~ +[RUITableViewRowAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[RUITableViewRowAccessibility loadImage] : 864 -> 884
~ ___41-[RUITableViewRowAccessibility loadImage]_block_invoke : 96 -> 100
~ ___41-[RUITableViewRowAccessibility loadImage]_block_invoke_2 : 80 -> 84

```
