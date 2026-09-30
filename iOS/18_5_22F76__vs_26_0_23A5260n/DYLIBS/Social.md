## Social

> `/System/Library/Frameworks/Social.framework/Social`

```diff

-765.0.0.0.0
-  __TEXT.__text: 0x3d928
+772.0.0.0.0
+  __TEXT.__text: 0x3d570
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x546c
+  __TEXT.__objc_methlist: 0x5464
   __TEXT.__const: 0xe00
-  __TEXT.__cstring: 0x9b6e
-  __TEXT.__gcc_except_tab: 0x544
+  __TEXT.__cstring: 0x9b31
+  __TEXT.__gcc_except_tab: 0x548
   __TEXT.__ustring: 0x59c
   __TEXT.__oslogstring: 0x73
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__unwind_info: 0x10b0
   __TEXT.__objc_classname: 0xe1b
-  __TEXT.__objc_methname: 0xda6d
-  __TEXT.__objc_methtype: 0x37ea
-  __TEXT.__objc_stubs: 0x9280
-  __DATA_CONST.__got: 0x788
-  __DATA_CONST.__const: 0x10f8
+  __TEXT.__objc_methname: 0xda03
+  __TEXT.__objc_methtype: 0x383e
+  __TEXT.__objc_stubs: 0x9180
+  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3540
+  __DATA_CONST.__objc_selrefs: 0x3510
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0x830
   __AUTH_CONST.__cfstring: 0x7100
-  __AUTH_CONST.__objc_const: 0xff40
+  __AUTH_CONST.__objc_const: 0xff58
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x1e00
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x62c
+  __DATA.__objc_ivar: 0x628
   __DATA.__data: 0xe68
   __DATA.__bss: 0x458
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
-  - /System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WebKit.framework/WebKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D23B6957-09A8-39A4-A221-6663677E721E
-  Functions: 1599
-  Symbols:   6506
-  CStrings:  4645
+  UUID: 2AC7401F-004F-3EB5-A754-7AEE12E3B883
+  Functions: 1594
+  Symbols:   6480
+  CStrings:  4637
 
Symbols:
+ ___82-[SLWebAuthController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke_2.106
+ ___block_literal_global.230
+ _objc_msgSend$setAccountProperty:forKey:
- -[SLComposeViewController _urlForUntypedAsset:]
- -[SLSheetPreviewImageSource _fetchPreviewImageForAssetURL:resultBlock:]
- -[SLSheetPreviewImageSource assetsLibrary]
- _ALAssetPropertyDuration
- _ALErrorInvalidProperty
- _OBJC_CLASS_$_ALAsset
- _OBJC_CLASS_$_ALAssetsLibrary
- _OBJC_IVAR_$_SLSheetPreviewImageSource._assetsLibrary
- __OBJC_$_PROP_LIST_SLSheetPreviewImageSource
- ___71-[SLSheetPreviewImageSource _fetchPreviewImageForAssetURL:resultBlock:]_block_invoke
- ___71-[SLSheetPreviewImageSource _fetchPreviewImageForAssetURL:resultBlock:]_block_invoke_2
- ___82-[SLWebAuthController _extensionRequestDidCompleteWithTokens:extensionCompletion:]_block_invoke_2.103
- ___block_descriptor_40_e8_32bs_e17_v16?0"ALAsset"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_literal_global.231
- _objc_msgSend$_fetchPreviewImageForAssetURL:resultBlock:
- _objc_msgSend$_urlForUntypedAsset:
- _objc_msgSend$aspectRatioThumbnail
- _objc_msgSend$assetForURL:resultBlock:failureBlock:
- _objc_msgSend$assetsLibrary
- _objc_msgSend$defaultRepresentation
- _objc_msgSend$initWithCGImage:
- _objc_msgSend$url
- _objc_msgSend$valueForProperty:
CStrings:
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "ACUISaysNotToSaveThis"
+ "ALAsset attachment support is deprecated"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "SLAttachment media assets must be URLs - returning nil attachment"
+ "Unsupported asset type %@"
+ "setAccountProperty:forKey:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
- "@\"ALAssetsLibrary\""
- "Failed to fetch asset URL %@ with error %{public}@"
- "Fetched asset for asset URL, fetching preview"
- "SLAttachment media assets must be URLs or ALAssets - returning nil attachment"
- "T@\"ALAssetsLibrary\",R"
- "Unsupported asset type"
- "_assetsLibrary"
- "_fetchPreviewImageForAssetURL:resultBlock:"
- "_urlForUntypedAsset:"
- "aspectRatioThumbnail"
- "assetForURL:resultBlock:failureBlock:"
- "assetsLibrary"
- "defaultRepresentation"
- "initWithCGImage:"
- "v16@?0@\"ALAsset\"8"
- "valueForProperty:"

```
