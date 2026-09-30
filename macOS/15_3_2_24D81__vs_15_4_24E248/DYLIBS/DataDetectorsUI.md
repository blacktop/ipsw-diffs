## DataDetectorsUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/DataDetectorsUI.framework/Versions/A/DataDetectorsUI`

```diff

-551.20.0.0.0
-  __TEXT.__text: 0x31d3c
-  __TEXT.__auth_stubs: 0xc30
+551.26.0.0.0
+  __TEXT.__text: 0x322b0
+  __TEXT.__auth_stubs: 0xc50
   __TEXT.__delay_helper: 0x41c
-  __TEXT.__objc_methlist: 0x2bb8
+  __TEXT.__objc_methlist: 0x2f28
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x378b
-  __TEXT.__gcc_except_tab: 0x8f4
+  __TEXT.__cstring: 0x38d1
+  __TEXT.__gcc_except_tab: 0x8fc
   __TEXT.__oslogstring: 0x1aa1
-  __TEXT.__ustring: 0x354
-  __TEXT.__unwind_info: 0xd18
+  __TEXT.__ustring: 0x3a2
+  __TEXT.__unwind_info: 0xd40
   __TEXT.__objc_classname: 0x702
-  __TEXT.__objc_methname: 0x8078
+  __TEXT.__objc_methname: 0x7f8d
   __TEXT.__objc_methtype: 0x1dde
-  __TEXT.__objc_stubs: 0x7d40
+  __TEXT.__objc_stubs: 0x7c20
   __DATA_CONST.__got: 0x7d8
   __DATA_CONST.__const: 0x940
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2448
+  __DATA_CONST.__objc_selrefs: 0x24f8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0x2a8
-  __AUTH_CONST.__auth_got: 0x628
+  __DATA_CONST.__objc_arraydata: 0x2b0
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x4980
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x4278
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x11d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CEF73C91-10C7-38E3-B092-28E7479AF478
-  Functions: 1188
-  Symbols:   3485
+  UUID: 8A3088D7-95DE-36A3-92EC-56717F3BB4F1
+  Functions: 1207
+  Symbols:   3500
   CStrings:  2775
 
Symbols:
+ +[DDDetectionController sharedController].cold.1
+ +[DDRemoteActionViewController controllerIsAvailable].cold.1
+ +[DDRevealBridge _lookupTextForText:].cold.1
+ -[DDActionController _presentCurrentViewControllerOurselves].cold.1
+ -[DDActionGroup cleanup].cold.1
+ -[DDDetectionController _doURLification:].cold.8
+ -[DDDetectionController _newOperationForContainer:].cold.1
+ -[DDDetectionController _resultForIdentifier:forContainer:context:].cold.4
+ -[DDDetectionController(TextKitBackEnd) urlifyTextView:withExternalResults:context:].cold.1
+ -[DDDetectionController(WebKitBackEnd) resetResultsForFrame:].cold.1
+ -[DDOpenMapsAction defaultAppRecord]
+ -[DDOpenURLAction appLink].cold.1
+ -[DDOperation dealloc].cold.2
+ -[DDOperation dealloc].cold.3
+ -[DDTextMessageAction localizedShowInMessages]
+ -[NSURL dd_isAppleApps]
+ -[NSURL dd_isAppleBooks]
+ -[NSURL dd_isAppleMusic]
+ -[NSURL dd_isApplePodcasts]
+ -[NSURL dd_isAppleStore]
+ -[NSURL dd_isAppleTV]
+ DDMapsGetBestAddressForResults.cold.1
+ DDPerformWebSearchFromQuery.cold.1
+ DDTrackEventCreationInHostApplication.cold.1
+ GCC_except_table26
+ GCC_except_table71
+ _OBJC_CLASS_$_GEOMapURLBuilder
+ ___block_descriptor_106_e8_32s40s48s56s64s72r80r_e31_v32?0"TUCallProvider"8Q16^B24ls32l8s40l8s48l8s56l8r72l8s64l8r80l8
+ ___block_descriptor_108_e8_32s40s48s56s64s72r80r_e32_v32?0"TUSenderIdentity"8q16q24ls32l8s40l8s48l8s56l8r72l8s64l8r80l8
+ __block_literal_global.406
+ _gotLoadHelper_x8$_OBJC_CLASS_$_GEOMapURLBuilder
+ _objc_msgSend$buildForDefaultNavigation
+ _objc_msgSend$defaultAppRecord
+ _objc_msgSend$initForAddress:label:
+ _objc_msgSend$initForDirectionsTo:
+ _objc_msgSend$name
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x10
+ actionSheetTitleForResult.cold.1
+ actionSheetTitleForResult.cold.2
+ actionSheetTitleForURL.cold.1
+ dd_hostApplicationCanListCallProviders.cold.1
+ dd_isInternalInstall.cold.1
+ dd_phoneNumberResultCanBeRdarLink.cold.1
+ dd_transientAttributesSet.cold.1
- -[DDTelephoneNumberAction contactsMatchingPhoneNumber:inContactStore:].cold.1
- -[NSURL(dd_private) dd_AppleOtherSchemes]
- -[NSURL(dd_private) dd_AppleiTunesSchemes]
- -[NSURL(dd_private) dd_isAppleApps]
- -[NSURL(dd_private) dd_isAppleBooks]
- -[NSURL(dd_private) dd_isAppleMusic]
- -[NSURL(dd_private) dd_isApplePodcasts]
- -[NSURL(dd_private) dd_isAppleStore]
- -[NSURL(dd_private) dd_isAppleTV]
- -[NSURL(dd_private) dd_isAppleiTunesStore]
- -[NSURL(dd_private) dd_isCloudLink]
- -[NSURL(dd_private) dd_productIdentifierFromAppleStoreScheme]
- GCC_except_table24
- GCC_except_table73
- _OBJC_CLASS_$__GEOMapURLBuilder
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- ___block_descriptor_98_e8_32s40s48s56s64s72r_e31_v32?0"TUCallProvider"8Q16^B24ls32l8s40l8s48l8s56l8r72l8s64l8
- ___block_descriptor_99_e8_32s40s48s56s64s72r_e26_v16?0"TUSenderIdentity"8ls32l8s40l8s48l8s56l8r72l8s64l8
- __block_literal_global.415
- _gotLoadHelper_x8$_OBJC_CLASS_$__GEOMapURLBuilder
- _objc_msgSend$URLForAddress:
- _objc_msgSend$URLForDirectionsFromHereTo:
- _objc_msgSend$dd_AppleOtherSchemes
- _objc_msgSend$dd_AppleiTunesSchemes
- _objc_msgSend$dd_isAppleApps
- _objc_msgSend$dd_isAppleBooks
- _objc_msgSend$dd_isAppleMusic
- _objc_msgSend$dd_isApplePodcasts
- _objc_msgSend$dd_isAppleStore
- _objc_msgSend$dd_isAppleTV
- _objc_msgSend$iCloudSharingURL_noFragment
- _objc_msgSend$intValue
- _objc_msgSend$numberWithInt:
- _objc_msgSend$pathComponents
CStrings:
+ "&destination="
+ "-prompt"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDAction.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDActionController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDAddressActions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDCallAction.m"
+ "?destination="
+ "Context Menu action title to open an item (link, address, etc...) in the default app for this item"
+ "Notification title to show a place in the default navigation app"
+ "Notification title to show a place in the default navigation app when the default is unknown"
+ "Notification title to show gps coordinates in the default navigation app"
+ "Notification title to show gps coordinates in the default navigation app when the default is unknown"
+ "Show on Map"
+ "buildForDefaultNavigation"
+ "defaultAppRecord"
+ "geo-navigation"
+ "initForAddress:label:"
+ "initForDirectionsTo:"
+ "name"
+ "recipient"
+ "replay.music.apple.com"
+ "v32@?0@\"TUSenderIdentity\"8q16q24"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDAction.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDActionController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDAddressActions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI_iosmac/Actions/DDCallAction.m"
- "Context Menu action on web url to open that url in the default web browser"
- "Notification title to show a place in Maps"
- "Notification title to show gps coordinates in Maps"
- "Open in Maps"
- "URLForAddress:"
- "URLForDirectionsFromHereTo:"
- "^(id)?[0-9]+?$"
- "dd_AppleOtherSchemes"
- "dd_AppleiTunesSchemes"
- "dd_isAppleApps"
- "dd_isAppleBooks"
- "dd_isAppleMusic"
- "dd_isApplePodcasts"
- "dd_isAppleStore"
- "dd_isAppleTV"
- "dd_isAppleiTunesStore"
- "dd_isCloudLink"
- "dd_productIdentifierFromAppleStoreScheme"
- "iCloudSharingURL_noFragment"
- "id"
- "intValue"
- "itunes"
- "numberWithInt:"
- "pathComponents"
- "v16@?0@\"TUSenderIdentity\"8"

```
