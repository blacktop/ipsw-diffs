## DataDetectorsUI

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI`

```diff

-551.20.0.0.0
-  __TEXT.__text: 0x4bb88
-  __TEXT.__auth_stubs: 0xd30
+551.25.0.0.0
+  __TEXT.__text: 0x4c778
+  __TEXT.__auth_stubs: 0xd40
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x123c
-  __TEXT.__objc_methlist: 0x4238
-  __TEXT.__const: 0x200
-  __TEXT.__oslogstring: 0x2090
-  __TEXT.__gcc_except_tab: 0xc10
-  __TEXT.__cstring: 0x53c6
-  __TEXT.__ustring: 0x45c
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__objc_methlist: 0x49dc
+  __TEXT.__const: 0x210
+  __TEXT.__oslogstring: 0x20cc
+  __TEXT.__gcc_except_tab: 0xc18
+  __TEXT.__cstring: 0x5537
+  __TEXT.__ustring: 0x4aa
+  __TEXT.__unwind_info: 0x1368
   __TEXT.__objc_classname: 0xbbc
-  __TEXT.__objc_methname: 0xb8c1
+  __TEXT.__objc_methname: 0xb8a3
   __TEXT.__objc_methtype: 0x2f41
-  __TEXT.__objc_stubs: 0xac20
-  __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0xcd0
+  __TEXT.__objc_stubs: 0xab40
+  __DATA_CONST.__got: 0xa60
+  __DATA_CONST.__const: 0xcf8
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30d0
+  __DATA_CONST.__objc_selrefs: 0x3270
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a8
-  __DATA_CONST.__objc_arraydata: 0x1608
-  __AUTH_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__objc_arraydata: 0x1610
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x6260
-  __AUTH_CONST.__objc_const: 0x7dc8
+  __AUTH_CONST.__cfstring: 0x6320
+  __AUTH_CONST.__objc_const: 0x6fb0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0xde0
   __AUTH_CONST.__objc_doubleobj: 0x2f0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x40c
+  __DATA.__objc_ivar: 0x41c
   __DATA.__data: 0xaf0
   __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x11d0

   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/EventKitUI.framework/EventKitUI
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LinkPresentation.framework/LinkPresentation
   - /System/Library/Frameworks/MessageUI.framework/MessageUI
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/WebKit.framework/WebKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1721
-  Symbols:   2368
-  CStrings:  3418
+  Functions: 1761
+  Symbols:   2421
+  CStrings:  3420
 
Symbols:
+ _OBJC_CLASS_$_GEOMapURLBuilder
+ _OBJC_CLASS_$_LPLinkView
+ _OBJC_CLASS_$_LPMetadataProvider
+ _OBJC_CLASS_$_LSBundleRecord
+ _objc_retain_x10
- _OBJC_CLASS_$_SKStoreProductViewController
- _OBJC_CLASS_$__GEOMapURLBuilder
- _SKStoreProductParameterITunesItemIdentifier
CStrings:
+ "\x02\x11\x11"
+ "&destination="
+ "-prompt"
+ "/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation"
+ "?destination="
+ "Context Menu action title to open an item (link, address, etc...) in the default app for this item"
+ "Couldn't get messages app record %@. Error: %@"
+ "Couldn't load link preview metadata. Error: %@"
+ "DDLinkPresentationAction"
+ "Notification title to show a place in the default navigation app"
+ "Notification title to show a place in the default navigation app when the default is unknown"
+ "Notification title to show gps coordinates in the default navigation app"
+ "Notification title to show gps coordinates in the default navigation app when the default is unknown"
+ "Show on Map"
+ "_defaultAppRecord"
+ "_defaultAppRecordFetched"
+ "_messagesAppRecord"
+ "_messagesAppRecordFetched"
+ "_setDisableAutoPlay:"
+ "_setDisablePlaybackControls:"
+ "buildForDefaultNavigation"
+ "bundleRecordWithApplicationIdentifier:error:"
+ "defaultAppRecord"
+ "geo-navigation"
+ "initForAddress:label:"
+ "initForDirectionsTo:"
+ "initWithMetadata:"
+ "intrinsicContentSize"
+ "replay.music.apple.com"
+ "sizeToFit"
+ "startFetchingMetadataForURL:completionHandler:"
+ "v24@?0@\"LPLinkMetadata\"8@\"NSError\"16"
+ "v32@?0@\"TUSenderIdentity\"8q16q24"
- "\x02\x11"
- "/System/Library/Frameworks/StoreKit.framework/StoreKit"
- "Context Menu action on web url to open that url in the default web browser"
- "DDAppleStorePreviewAction"
- "Error loading Apple Store content"
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
- "id"
- "intValue"
- "itunes"
- "loadProductWithParameters:completionBlock:"
- "numberWithInt:"
- "pathComponents"
- "rangeOfString:options:"
- "supportedInterfaceOrientations"
- "v16@?0@\"TUSenderIdentity\"8"

```
