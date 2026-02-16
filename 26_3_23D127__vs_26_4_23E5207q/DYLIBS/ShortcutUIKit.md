## ShortcutUIKit

> `/System/Library/PrivateFrameworks/ShortcutUIKit.framework/ShortcutUIKit`

```diff

-375.2.2.0.0
-  __TEXT.__text: 0x9f4
-  __TEXT.__auth_stubs: 0x180
+375.4.1.0.0
+  __TEXT.__text: 0xac8
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x14c
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xa0
   __TEXT.__objc_classname: 0x22
   __TEXT.__objc_methname: 0x436
   __TEXT.__objc_methtype: 0x45

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x218

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7C4CF08-7ED8-3350-922D-810413428FBF
+  UUID: 255EE3AB-D7AB-3794-BCB3-DCB0B8C3A71E
   Functions: 17
-  Symbols:   153
+  Symbols:   152
   CStrings:  127
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
Functions:
~ -[SCUIAssetProvider imageNamed:] : 192 -> 212
~ -[SCUIAssetProvider _assetManager] : 168 -> 184
~ _ShortcutUIKitBundle : 108 -> 120
~ +[SBSApplicationShortcutIcon(ShortcutUIKit) _scui_defaultImage] : 68 -> 84
~ ___63+[SBSApplicationShortcutIcon(ShortcutUIKit) _scui_defaultImage]_block_invoke : 140 -> 152
~ -[SBSApplicationShortcutIcon(ShortcutUIKit) scui_iconImageWithAssetProvider:] : 76 -> 84
~ -[SBSApplicationShortcutSystemIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 300 -> 332
~ -[SBSApplicationShortcutTemplateIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 136 -> 148
~ -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 244 -> 264
~ -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageForCachedBitmapData:scale:] : 124 -> 128
~ -[SBSApplicationShortcutContactIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 576 -> 632
~ -[SCUIAssetProvider initWithBundleURL:].cold.1 : 124 -> 128

```
