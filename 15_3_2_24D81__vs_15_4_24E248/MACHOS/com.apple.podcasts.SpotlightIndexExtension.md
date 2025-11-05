## com.apple.podcasts.SpotlightIndexExtension

> `/System/Applications/Podcasts.app/Contents/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/Contents/MacOS/com.apple.podcasts.SpotlightIndexExtension`

```diff

-4024.400.4.0.0
-  __TEXT.__text: 0x9554
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x26a0
-  __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__const: 0xd2
-  __TEXT.__gcc_except_tab: 0xfc
-  __TEXT.__objc_methname: 0x2695
-  __TEXT.__cstring: 0x4c3
+4024.540.4.0.0
+  __TEXT.__text: 0x8d6c
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0x97c
+  __TEXT.__const: 0x132
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__objc_methname: 0x2542
+  __TEXT.__cstring: 0x4b3
   __TEXT.__oslogstring: 0x588
   __TEXT.__objc_classname: 0x12a
-  __TEXT.__objc_methtype: 0x458
+  __TEXT.__objc_methtype: 0x4b9
   __TEXT.__swift5_typeref: 0x66
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x310
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x250
+  __TEXT.__unwind_info: 0x2e0
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__const: 0x860
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x12c8
-  __DATA.__objc_selrefs: 0xb78
+  __DATA.__objc_const: 0xff8
+  __DATA.__objc_selrefs: 0xbd0
   __DATA.__objc_ivar: 0x74
-  __DATA.__objc_data: 0x310
+  __DATA.__objc_data: 0x2f0
   __DATA.__data: 0x1d8
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
   - /System/Library/PrivateFrameworks/PodcastsFoundation.framework/Versions/A/PodcastsFoundation
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit

   - /System/iOSSupport/System/Library/PrivateFrameworks/PodcastsUI.framework/Versions/A/PodcastsUI
   - /System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore
   - /System/iOSSupport/usr/lib/swift/libswiftMapKit.dylib
-  - /System/iOSSupport/usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 69767D33-26AB-31B8-B7D1-822E1DB05D65
-  Functions: 234
-  Symbols:   211
-  CStrings:  628
+  UUID: 2FFF614B-D129-3A37-83AE-B8CFDD4E5B3B
+  Functions: 230
+  Symbols:   210
+  CStrings:  619
 
Symbols:
+ _OBJC_CLASS_$_PFObjCCachingImageContentProviderBridge
+ _UTTypeAudiovisualContent
+ _com_apple_podcasts_SpotlightIndexExtensionVersionNumber
+ _com_apple_podcasts_SpotlightIndexExtensionVersionString
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
- _OBJC_CLASS_$_MTImageStore
- _OBJC_CLASS_$_MTPodcastEpisodeFilter
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftWebKit
- _kEpisodeSeasonNumber
- _kMTLibraryDefaultImageKey
- _kUTTypeAudiovisualContent
CStrings:
+ "artworkBridge"
+ "configureArtworkForSearchableItemAttributeSet:withPodcast:completion:"
+ "dateByAddingTimeInterval:"
+ "extensionBridge"
+ "initWithContentType:"
+ "now"
+ "promptAccountAuthenticationWithDebugReason:forced:"
+ "searchableItemsDidUpdate:"
+ "searchableItemsForIdentifiers:searchableItemsHandler:"
+ "v24@0:8@\"NSArray\"16"
+ "v28@0:8@\"NSString\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
- "_fetchRequestForDistinctSeasons"
- "asyncImageURLForKey:squareDimension:cacheKeyModifier:completionHandler:"
- "configureArtworkForSearchableItemAttributeSet:withPodcastUuid:completion:"
- "defaultStore"
- "initWithItemContentType:"
- "latestSeasonNumber"
- "newestEpisodeWithFilter:"
- "objectsInEntity:predicate:sortDescriptors:returnsObjectsAsFaults:limit:"
- "podcastUuid"
- "predicateForEpisodeType:"
- "predicateForPodcast:"
- "predicateForSeasonNumberWithNoEpisodeNumber:"
- "seasonTrailerInSeason:"
- "setExcludeUnentitled:"
- "setPropertiesToFetch:"
- "setResultType:"
- "setReturnsDistinctResults:"
- "smartPlayEpisode"
- "sortDescriptorsForPubDateAscending:"
- "subscribed"
- "v24@?0@\"NSURL\"8@\"NSString\"16"
- "valueForKey:"

```
