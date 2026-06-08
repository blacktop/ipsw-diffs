## languageassetd

> `/usr/libexec/languageassetd`

```diff

-64.3.3.0.0
-  __TEXT.__text: 0x4cac
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x250
-  __TEXT.__oslogstring: 0x548
+68.0.0.0.0
+  __TEXT.__text: 0x3b24
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x9c0
+  __TEXT.__objc_methlist: 0x208
+  __TEXT.__oslogstring: 0x48a
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x5a9
-  __TEXT.__objc_methname: 0xa93
+  __TEXT.__cstring: 0x40f
+  __TEXT.__objc_methname: 0x872
   __TEXT.__objc_classname: 0x2e
-  __TEXT.__objc_methtype: 0x14a
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x358
-  __DATA_CONST.__cfstring: 0x760
+  __TEXT.__objc_methtype: 0x150
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0xb8
   __DATA.__objc_const: 0x250
-  __DATA.__objc_selrefs: 0x348
+  __DATA.__objc_selrefs: 0x298
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__bss: 0x30
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices
-  - /System/Library/PrivateFrameworks/FontServices.framework/FontServices
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7BB1E1B-2992-3EB3-A3CB-DB4B8CA4A39C
-  Functions: 85
-  Symbols:   110
-  CStrings:  292
+  UUID: 1DC6EAB4-69E3-380B-B83A-2212B912955A
+  Functions: 75
+  Symbols:   107
+  CStrings:  239
 
Symbols:
+ _CTFontManagerDownloadFontsRequiredForLanguages
+ _objc_release_x24
+ _objc_release_x28
- _FSGetMaxSupportedFontAssetCompatibilityVersion
- _NSLog
- _OBJC_CLASS_$_ASAssetQuery
- _kFSFontAssetType
- _objc_release_x25
- _objc_release_x26
CStrings:
+ "configureDownloadFlagsForAssets:languageAssetInfo:assetType:languages:"
+ "handleCatalogDownloadResultForAssetType:languageAssetInfo:languages:"
+ "initiateActualDownload:languages:"
+ "processLanguageAssetInfo:languages:"
+ "purgeLocalAssetsWithType:"
+ "v16@?0^{__CFArray=}8"
+ "v48@0:8@16@24@32@40"
- "\t Error running language asset query: error %@."
- "/System/Library/PrivateFrameworks/FontServices.framework/FontAssetInfo.plist"
- "FontFamilyNameKey"
- "FontInfo4"
- "IdentifierContainerAttributeKey"
- "LanguageAndFontFamilyNamesMapping"
- "NotificationBaseKey"
- "PostScriptFontName"
- "V1 dictionary (%@) was installed and purged with error=%@"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "com.apple.MobileAsset.Font"
- "com.apple.MobileAsset.Font2"
- "com.apple.MobileAsset.Font3"
- "com.apple.MobileAsset.Font4"
- "com.apple.MobileAsset.Font5"
- "configureDownloadFlagsForAssets:languageAssetInfo:assetType:"
- "dictionaryWithContentsOfFile:"
- "filterIncompatibleFontAssets:"
- "fontAssetMatched:primaryLanguage:assetInfo:"
- "handleCatalogDownloadResultForAssetType:languageAssetInfo:"
- "initWithAssetType:"
- "initWithObjectsAndKeys:"
- "initiateActualDownload:"
- "intValue"
- "isEqualToNumber:"
- "notificationStringWithPrimaryLanguage:assetInfo:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "oldDictionaryAssetsWithLanguageAssetInfo:"
- "primaryLanguageIsInBlackList:assetType:assetInfo:"
- "processLanguageAssetInfo:"
- "purge:"
- "purgeAndReturnError:"
- "purgeLocalAssetsWithType: %{public}@, mobileAssetVersionV2: %{public}@"
- "purgeLocalAssetsWithType:mobileAssetVersionV2:"
- "purgeLocalFontAssets"
- "runQueryAndReturnError:"
- "setQueriesLocalAssetInformationOnly:"
- "setValue:forKey:"
- "startCatalogDownload purging local font assets assetType=[%{public}@]."
- "stringByAppendingString:"
- "unsignedIntValue"
- "v16@?0@\"NSError\"8"
- "v28@0:8@16B24"
- "zh-HK"

```
