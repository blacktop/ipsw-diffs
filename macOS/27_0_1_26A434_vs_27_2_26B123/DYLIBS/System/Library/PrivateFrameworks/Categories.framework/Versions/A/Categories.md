## Categories

> `/System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories`

```diff

-58.0.1.0.0
-  __TEXT.__text: 0xc85c
-  __TEXT.__objc_methlist: 0x82c
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x428
-  __TEXT.__cstring: 0x2dbc
-  __TEXT.__oslogstring: 0x656
-  __TEXT.__unwind_info: 0x3e8
+58.1.7.1.0
+  __TEXT.__text: 0xc858
+  __TEXT.__objc_methlist: 0x89c
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x3f0
+  __TEXT.__cstring: 0x3297
+  __TEXT.__oslogstring: 0x6c7
+  __TEXT.__unwind_info: 0x400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x720
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0xab8
+  __DATA_CONST.__objc_arraydata: 0xc18
   __DATA_CONST.__got: 0xf0
-  __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0xca0
-  __AUTH_CONST.__objc_arrayobj: 0x990
+  __AUTH_CONST.__const: 0x820
+  __AUTH_CONST.__cfstring: 0x3b20
+  __AUTH_CONST.__objc_const: 0xcc8
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x9f0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x1e8
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/ContextKit.framework/Versions/A/ContextKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 250
-  Symbols:   698
-  CStrings:  501
+  Functions: 257
+  Symbols:   714
+  CStrings:  539
 
Symbols:
+ +[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:origin:withCompletionHandler:]
+ +[CTCategory _equivalentBundleIDForDestinationScheme:fromBundleID:sourceScheme:]
+ +[CTCategory _lookupAppStoreUsing:platform:origin:withCompletionHandler:]
+ +[CTCategory _shouldExcludeBundleIdentifierFromCategoryLookup:]
+ +[CTCategory bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:]
+ +[CTCategory categoryForBundleIdentifiers:platform:targetUserIsU13:origin:withCompletionHandler:]
+ +[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:origin:withCompletionHandler:]
+ +[CTCategory currentDeviceFamily]
+ +[CTCategory deviceFamilyForPlatform:]
+ +[CTCategory schemeStringForDeviceFamily:]
+ -[CTCategories bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:]
+ GCC_except_table122
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table93
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __103+[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:origin:withCompletionHandler:]_block_invoke
+ __105+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:origin:withCompletionHandler:]_block_invoke
+ __105+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:origin:withCompletionHandler:]_block_invoke_2
+ __73+[CTCategory _lookupAppStoreUsing:platform:origin:withCompletionHandler:]_block_invoke
+ ___103+[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:origin:withCompletionHandler:]_block_invoke
+ ___105+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:origin:withCompletionHandler:]_block_invoke
+ ___105+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:origin:withCompletionHandler:]_block_invoke_2
+ ___33+[CTCategory currentDeviceFamily]_block_invoke
+ ___73+[CTCategory _lookupAppStoreUsing:platform:origin:withCompletionHandler:]_block_invoke
+ ___73+[CTCategory _lookupAppStoreUsing:platform:origin:withCompletionHandler:]_block_invoke_2
+ ___80+[CTCategory _equivalentBundleIDForDestinationScheme:fromBundleID:sourceScheme:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48bs56r64r72r_e34_v24?0"NSDictionary"8"NSError"16l
+ _objc_msgSend$_bundleCategoriesLookupResultsForBundleIdentifiers:platform:origin:withCompletionHandler:
+ _objc_msgSend$_equivalentBundleIDForDestinationScheme:fromBundleID:sourceScheme:
+ _objc_msgSend$_lookupAppStoreUsing:platform:origin:withCompletionHandler:
+ _objc_msgSend$_shouldExcludeBundleIdentifierFromCategoryLookup:
+ _objc_msgSend$appStoreCategoriesForBundleIDs:platform:origin:replyHandler:
+ _objc_msgSend$bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:
+ _objc_msgSend$categoryForBundleIdentifiers:platform:targetUserIsU13:origin:withCompletionHandler:
+ _objc_msgSend$categoryForBundleIdentifiers:platform:version:targetUserIsU13:origin:withCompletionHandler:
+ _objc_msgSend$containsString:
+ _objc_msgSend$currentDeviceFamily
+ _objc_msgSend$deviceFamilyForPlatform:
+ _objc_msgSend$initWithIdentifier:webDomains:bundleIdentifier:
+ _objc_msgSend$integerValue
+ _objc_msgSend$schemeStringForDeviceFamily:
+ currentDeviceFamily.deviceFamily
+ currentDeviceFamily.onceToken
- +[CTCategories currentIOSDevice]
- +[CTCategory itemWith:platform:array:]
- +[CTCategory schemeStringForPlatform:]
- GCC_except_table100
- GCC_except_table117
- GCC_except_table26
- GCC_except_table29
- GCC_except_table31
- GCC_except_table35
- GCC_except_table40
- GCC_except_table44
- GCC_except_table48
- GCC_except_table50
- GCC_except_table62
- GCC_except_table68
- GCC_except_table85
- __38+[CTCategory itemWith:platform:array:]_block_invoke
- __66+[CTCategory _lookupAppStoreUsing:platform:withCompletionHandler:]_block_invoke
- __96+[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke
- __98+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]_block_invoke
- ___38+[CTCategory itemWith:platform:array:]_block_invoke
- ___38+[CTCategory itemWith:platform:array:]_block_invoke_2
- ___38+[CTCategory itemWith:platform:array:]_block_invoke_3
- ___38+[CTCategory itemWith:platform:array:]_block_invoke_4
- ___56+[CTCategory bundleIDForPlatform:fromBundleID:platform:]_block_invoke
- ___66+[CTCategory _lookupAppStoreUsing:platform:withCompletionHandler:]_block_invoke
- ___66+[CTCategory _lookupAppStoreUsing:platform:withCompletionHandler:]_block_invoke_2
- ___96+[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke
- ___98+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]_block_invoke
- ___98+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32r_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48bs56r64r72r_e34_v24?0"NSDictionary"8"NSError"16l
- _objc_msgSend$_bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:
- _objc_msgSend$_lookupAppStoreUsing:platform:withCompletionHandler:
- _objc_msgSend$appStoreCategoriesForBundleIDs:platform:replyHandler:
- _objc_msgSend$schemeStringForPlatform:
CStrings:
+ "%s: no scheme for device family (source %ld, destination %ld); one of them is outside CTDeviceFamily"
+ "+[CTCategory bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:]"
+ "SB"
+ "_lookupAppStoreUsing %@ origin: %ld"
+ "com.apple.EmojiPoster"
+ "com.apple.GradientPoster"
+ "com.apple.PridePoster"
+ "com.apple.control-center"
+ "com.apple.sharing."
+ "com.apple.springboard."
+ "homeaccessory"
+ "homeaccessory://com.apple.CalendarPebble"
+ "homeaccessory://com.apple.Home"
+ "homeaccessory://com.apple.MobileAddressBook"
+ "homeaccessory://com.apple.MobileSMS"
+ "homeaccessory://com.apple.Music"
+ "homeaccessory://com.apple.PebbleSettingsApp"
+ "homeaccessory://com.apple.facetime"
+ "homeaccessory://com.apple.findmy"
+ "homeaccessory://com.apple.iBooks"
+ "homeaccessory://com.apple.mobilesafari"
+ "homeaccessory://com.apple.mobiletimer"
+ "homeaccessory://com.apple.news"
+ "homeaccessory://com.apple.podcasts"
+ "homeaccessory://com.apple.reminders"
+ "homeaccessory://com.apple.stocks"
+ "homeaccessory://com.apple.tv"
+ "homeaccessory://com.apple.weather"
+ "ios://com.apple.TVRemoteApp"
+ "ios://com.apple.TapToRadar"
+ "ios://com.apple.Translate"
+ "ios://com.apple.compass"
+ "q"
+ "tvos://com.apple.Fitness"
+ "tvos://com.apple.TVAppStore"
+ "tvos://com.apple.TVMusic"
+ "tvos://com.apple.TVPhotos"
+ "tvos://com.apple.TVSettings"
+ "tvos://com.apple.TVWatchList"
+ "tvos://com.apple.facetime"
+ "tvos://com.apple.podcasts"
+ "watchos://com.apple.NanoCompass.watchkitapp"
+ "watchos://com.apple.NanoNotes"
+ "watchos://com.apple.NanoTapToRadar"
+ "watchos://com.apple.NanoTranslate"
+ "watchos://com.apple.findmy.watchapp"
- "_lookupAppStoreUsing %@"
- "ios://"
- "ios://com.apple.TVRemote"
- "iosmac://"
- "macos://"
- "tvos://"
- "visionos://"
- "watchos://"
```
