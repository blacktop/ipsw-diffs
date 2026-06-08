## ShortcutUIKit

> `/System/Library/PrivateFrameworks/ShortcutUIKit.framework/ShortcutUIKit`

```diff

-375.5.2.100.0
-  __TEXT.__text: 0xac8
-  __TEXT.__auth_stubs: 0x170
+387.0.0.0.0
+  __TEXT.__text: 0x9dc
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x14c
+  __TEXT.__cstring: 0x14e
   __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0x436
-  __TEXT.__objc_methtype: 0x45
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x218
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 756BFE72-D896-3C58-83A6-ADEF2E2C986C
+  UUID: C212AB8E-7DF8-310A-9E91-9D92B136671E
   Functions: 17
   Symbols:   152
-  CStrings:  127
+  CStrings:  69
 
Symbols:
+ -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:traitCollection:]
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$displayScale
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:]
- _OBJC_CLASS_$_UIScreen
- _objc_msgSend$mainScreen
- _objc_msgSend$scale
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ -[SCUIAssetProvider imageNamed:] : 212 -> 192
~ -[SCUIAssetProvider _assetManager] : 184 -> 168
~ _ShortcutUIKitBundle : 120 -> 108
~ +[SBSApplicationShortcutIcon(ShortcutUIKit) _scui_defaultImage] : 84 -> 68
~ ___63+[SBSApplicationShortcutIcon(ShortcutUIKit) _scui_defaultImage]_block_invoke : 152 -> 140
~ -[SBSApplicationShortcutIcon(ShortcutUIKit) scui_iconImageWithAssetProvider:] : 84 -> 76
~ -[SBSApplicationShortcutSystemIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 332 -> 300
~ -[SBSApplicationShortcutTemplateIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 148 -> 136
~ -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] -> -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:traitCollection:] : 264 -> 220
~ -[SBSApplicationShortcutCustomImageIcon(ShortcutUIKit) _scui_iconImageForCachedBitmapData:scale:] : 128 -> 124
~ -[SBSApplicationShortcutContactIcon(ShortcutUIKit) _scui_iconImageWithAssetProvider:] : 632 -> 576
~ -[SCUIAssetProvider initWithBundleURL:].cold.1 : 128 -> 124
CStrings:
- ".cxx_destruct"
- "@\"NSURL\""
- "@\"_UIAssetManager\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16d24"
- "SCUIAssetProvider"
- "ShortcutUIKit"
- "URLByAppendingPathComponent:"
- "_assetManager"
- "_bundleURL"
- "_scui_defaultImage"
- "_scui_iconImageForCachedBitmapData:scale:"
- "_scui_iconImageName"
- "_scui_iconImageWithAssetProvider:"
- "arrayWithObjects:count:"
- "bundleForClass:"
- "configurationWithPointSize:weight:scale:"
- "contactIdentifier"
- "currentDevice"
- "currentHandler"
- "dataType"
- "defaultFontForTextStyle:"
- "descriptorForRequiredKeysIncludingImage:"
- "firstName"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "imageData"
- "imageNamed:"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageNamed:withTrait:"
- "imageWithCGImage:scale:orientation:"
- "imageWithContentsOfFile:"
- "imageWithData:scale:"
- "imageWithRenderingMode:"
- "init"
- "initWithBundleURL:"
- "initWithStyle:diameter:"
- "initWithURL:idiom:error:"
- "isTemplate"
- "lastName"
- "mainScreen"
- "monogramForContact:"
- "monogramForPersonWithFirstName:lastName:"
- "path"
- "pointSize"
- "scale"
- "scui_iconImageWithAssetProvider:"
- "setFamilyName:"
- "setGivenName:"
- "setImageData:"
- "silhouetteMonogram"
- "systemImageName"
- "systemImageNamed:withConfiguration:"
- "templateImageName"
- "type"
- "unifiedContactWithIdentifier:keysToFetch:error:"
- "userInterfaceIdiom"
- "v16@0:8"

```
