## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-623.1.14.10.9
-  __TEXT.__text: 0x118798
+623.2.2.0.0
+  __TEXT.__text: 0x119280
   __TEXT.__auth_stubs: 0x23d0
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xc8d4
+  __TEXT.__objc_methlist: 0xc8fc
   __TEXT.__const: 0x6c330
-  __TEXT.__gcc_except_tab: 0xefd8
+  __TEXT.__gcc_except_tab: 0xf040
   __TEXT.__oslogstring: 0x9abd
-  __TEXT.__cstring: 0x11b26
+  __TEXT.__cstring: 0x11b36
   __TEXT.__ustring: 0x1fc2
   __TEXT.__dlopen_cstrs: 0x3b5
   __TEXT.__constg_swiftt: 0x304

   __TEXT.__swift5_capture: 0x38c
   __TEXT.__swift_as_entry: 0x80
   __TEXT.__swift_as_ret: 0xc0
-  __TEXT.__unwind_info: 0x72e8
+  __TEXT.__unwind_info: 0x7300
   __TEXT.__eh_frame: 0x1cf0
   __TEXT.__objc_classname: 0x1f34
-  __TEXT.__objc_methname: 0x2d49f
-  __TEXT.__objc_methtype: 0x5d69
-  __TEXT.__objc_stubs: 0x1a920
-  __DATA_CONST.__got: 0x15a8
-  __DATA_CONST.__const: 0x72b8
+  __TEXT.__objc_methname: 0x2d603
+  __TEXT.__objc_methtype: 0x5d94
+  __TEXT.__objc_stubs: 0x1aa40
+  __DATA_CONST.__got: 0x15b0
+  __DATA_CONST.__const: 0x7290
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c60
+  __DATA_CONST.__objc_selrefs: 0x8c98
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x19f8
   __AUTH_CONST.__auth_got: 0x1210
   __AUTH_CONST.__const: 0x23a0
   __AUTH_CONST.__cfstring: 0xfe20
-  __AUTH_CONST.__objc_const: 0x16520
+  __AUTH_CONST.__objc_const: 0x164f0
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x738
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x3f60
   __AUTH.__data: 0x4b0
-  __DATA.__objc_ivar: 0xf80
+  __DATA.__objc_ivar: 0xf7c
   __DATA.__data: 0x1f2c
   __DATA.__bss: 0xa60
   __DATA.__common: 0xa8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CEC4A7FD-F810-39D0-B1EF-6F88D78D4FBA
-  Functions: 6357
-  Symbols:   21735
-  CStrings:  12021
+  UUID: D92B6AA2-D7F8-39E5-869F-5BD1879CB9F3
+  Functions: 6361
+  Symbols:   21752
+  CStrings:  12029
 
Symbols:
+ +[WBSFaviconProviderUtilities maximumAvailableSizeFromFaviconInfo:]
+ +[WBSLPLinkMetadataFetchOperation reportFetchCompletionWithMetadata:error:didUseOffScreenWebView:]
+ +[WBSTouchIconFetchOperation reportFetchCompletionOfType:forIconURL:iconSize:didSucceed:didUseOffScreenWebView:response:error:]
+ +[WBSTouchIconFetchOperation reportFetchCompletionOfType:forIconURLs:responses:errors:lastFetchedURL:lastFetchedIcon:didUseOffScreenWebView:]
+ +[WBSTouchIconFetchOperationResult resultForFetchFailureWithHost:response:higherPriorityIconDownloadFailedDueToNetworkError:error:]
+ +[WBSTouchIconFetchOperationResult resultWithFavicon:iconData:iconURL:host:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:error:faviconInfoFromWebView:]
+ +[WBSTouchIconFetchOperationResult resultWithTouchIcon:host:isFavicon:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:error:]
+ -[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:]
+ -[WBSStartPageFallbackImageManager displayableImageForImage:withRequiredImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:]
+ -[WBSTouchIconFetchOperation _reportFetchFailureWithError:]
+ -[_WBSStartPageFallbackIconCacheIdentifier initWithConfiguration:imageSize:title:url:baseImage:]
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ __OBJC_$_CLASS_METHODS_WBSTouchIconFetchOperation
+ ___102-[WBSTouchIconCache _setUpAndReturnPreparedResponseForRequest:withImage:imageState:didReceiveNewData:]_block_invoke.35
+ ___116-[WBSTouchIconFetchOperation didFetchTouchIconURLs:fallbackTouchIconURLs:andFaviconURLs:fallbackFaviconURLs:forURL:]_block_invoke.87
+ ___176-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke
+ ___176-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_2
+ ___176-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_3
+ ___176-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_4
+ ___55-[WBSTouchIconCache _responseForRequest:withTouchIcon:]_block_invoke.52
+ ___59-[WBSTouchIconCache responseForRequest:willProvideUpdates:]_block_invoke.32
+ ___59-[WBSTouchIconCache responseForRequest:willProvideUpdates:]_block_invoke.33
+ ___59-[WBSTouchIconFetchOperation _downloadPendingTouchIconURLs]_block_invoke.78
+ ___68-[WBSLeadImageCache prepareResponseForRequest:allowDelayedResponse:]_block_invoke_5
+ ___78-[WBSFaviconProvider _linkPageURL:toIconWithInfo:isPrivate:completionHandler:]_block_invoke.48
+ ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke.73
+ ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke_2.75
+ ___block_descriptor_104_ea8_32s40s48s56s64s72bs80w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lw80l8s32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_112_ea8_32s40s48s56s64s72s80bs88w_e29_v24?0"UIImage"8"NSError"16lw88l8s32l8s40l8s80l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_40_e8_32s_e38_v28?0"NSURLResponse"8"NSError"16B24ls32l8
+ ___block_descriptor_40_ea8_32bs_e72_v48?0"UIImage"8"NSData"16"NSURL"24"NSDictionary"32"NSDictionary"40ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e72_v48?0"UIImage"8"NSData"16"NSURL"24"NSDictionary"32"NSDictionary"40ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48bs_e31_v28?0"NSData"8B16"NSError"20ls48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48w_e72_v48?0"UIImage"8"NSData"16"NSURL"24"NSDictionary"32"NSDictionary"40lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e8_v12?0B8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40r48r56r_e38_v32?0"UIImage"8"NSData"16"NSURL"24lr40l8r48l8r56l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e20_v24?0"UIImage"8q16lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_ea8_32s40s48bs56r64r72r_e5_v8?0ls48l8r56l8r64l8r72l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e47_v24?0"WBSFaviconInfoFromWebView"8"NSError"16ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8w80l8
+ ___block_descriptor_97_ea8_32s40s48s56bs64bs72w_e47_v24?0"WBSFaviconInfoFromWebView"8"NSError"16ls56l8w72l8s32l8s40l8s48l8s64l8
+ ___block_literal_global.33
+ ___block_literal_global.50
+ ___block_literal_global.54
+ _objc_msgSend$_downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:
+ _objc_msgSend$_reportFetchFailureWithError:
+ _objc_msgSend$didCompleteSiteIconFetchOfType:iconURL:iconSize:didSucceed:didUseOffScreenWebView:numberOfDownloadAttempts:
+ _objc_msgSend$didFailSiteIconDownloadForFetchType:iconURL:iconSize:didUseOffScreenWebView:response:error:
+ _objc_msgSend$displayableImageForImage:withRequiredImageSize:fallbackImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateGlyph:
+ _objc_msgSend$iconMetadata
+ _objc_msgSend$imageMetadata
+ _objc_msgSend$initWithConfiguration:imageSize:title:url:baseImage:
+ _objc_msgSend$maximumAvailableSizeFromFaviconInfo:
+ _objc_msgSend$reportFetchCompletionOfType:forIconURL:iconSize:didSucceed:didUseOffScreenWebView:response:error:
+ _objc_msgSend$reportFetchCompletionOfType:forIconURLs:responses:errors:lastFetchedURL:lastFetchedIcon:didUseOffScreenWebView:
+ _objc_msgSend$reportFetchCompletionWithMetadata:error:didUseOffScreenWebView:
+ _objc_msgSend$resultForFetchFailureWithHost:response:higherPriorityIconDownloadFailedDueToNetworkError:error:
+ _objc_msgSend$resultWithFavicon:iconData:iconURL:host:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:error:faviconInfoFromWebView:
+ _objc_msgSend$resultWithTouchIcon:host:isFavicon:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:error:
- +[WBSTouchIconFetchOperationResult resultForFetchFailureWithHost:pageRequestDidSucceed:response:error:]
- +[WBSTouchIconFetchOperationResult resultWithFavicon:iconData:iconURL:host:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:faviconInfoFromWebView:]
- +[WBSTouchIconFetchOperationResult resultWithTouchIcon:host:isFavicon:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:]
- -[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]
- -[WBSStartPageFallbackImageManager _displayableImageForImage:withRequiredImageSize:fallbackImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateGlyph:shouldGenerateThumbnail:]
- -[WBSStartPageFallbackImageManager displayableImageForImage:withRequiredImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateThumbnail:]
- -[_WBSStartPageFallbackIconCacheIdentifier initWithConfiguration:imageSize:title:url:baseImage:isThumbnail:]
- -[_WBSStartPageFallbackIconCacheIdentifier isThumbnail]
- _OBJC_IVAR_$__WBSStartPageFallbackIconCacheIdentifier._isThumbnail
- ___102-[WBSTouchIconCache _setUpAndReturnPreparedResponseForRequest:withImage:imageState:didReceiveNewData:]_block_invoke.33
- ___116-[WBSTouchIconFetchOperation didFetchTouchIconURLs:fallbackTouchIconURLs:andFaviconURLs:fallbackFaviconURLs:forURL:]_block_invoke.85
- ___150-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke
- ___150-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_2
- ___150-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_3
- ___231-[WBSStartPageFallbackImageManager _displayableImageForImage:withRequiredImageSize:fallbackImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateGlyph:shouldGenerateThumbnail:]_block_invoke
- ___55-[WBSTouchIconCache _responseForRequest:withTouchIcon:]_block_invoke.50
- ___59-[WBSTouchIconCache responseForRequest:willProvideUpdates:]_block_invoke.30
- ___59-[WBSTouchIconCache responseForRequest:willProvideUpdates:]_block_invoke.31
- ___59-[WBSTouchIconFetchOperation _downloadPendingTouchIconURLs]_block_invoke.76
- ___78-[WBSFaviconProvider _linkPageURL:toIconWithInfo:isPrivate:completionHandler:]_block_invoke.47
- ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke.71
- ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke_2.73
- ___block_descriptor_112_ea8_32s40s48s56s64s72s80s88bs_e17_v16?0"UIImage"8ls88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_40_e8_32s_e23_v16?0"NSURLResponse"8ls32l8
- ___block_descriptor_40_ea8_32bs_e73_v48?0"UIImage"8"NSData"16"NSURL"24"NSURLResponse"32"NSDictionary"40ls32l8
- ___block_descriptor_48_e8_32s40bs_e73_v48?0"UIImage"8"NSData"16"NSURL"24"NSURLResponse"32"NSDictionary"40ls32l8s40l8
- ___block_descriptor_48_ea8_32s40w_e73_v48?0"UIImage"8"NSData"16"NSURL"24"NSURLResponse"32"NSDictionary"40lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e8_v12?0B8ls32l8s40l8r48l8
- ___block_descriptor_56_ea8_32s40s48bs_e19_v20?0"NSData"8B16ls48l8s32l8s40l8
- ___block_descriptor_72_ea8_32s40r48r56r64r_e56_v40?0"UIImage"8"NSData"16"NSURL"24"NSURLResponse"32lr40l8r48l8r56l8r64l8s32l8
- ___block_descriptor_72_ea8_32s40s48s56s64bs_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_ea8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e35_v16?0"WBSFaviconInfoFromWebView"8ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e20_v24?0"UIImage"8q16ls32l8s40l8s48l8s56l8s64l8w72l8
- ___block_descriptor_80_ea8_32s40bs48r56r64r72r_e5_v8?0ls40l8r48l8r56l8r64l8r72l8s32l8
- ___block_descriptor_96_ea8_32s40s48s56s64s72bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8s48l8s72l8s56l8s64l8
- ___block_descriptor_97_ea8_32s40s48s56bs64bs72w_e35_v16?0"WBSFaviconInfoFromWebView"8ls56l8w72l8s32l8s40l8s48l8s64l8
- ___block_literal_global.48
- ___block_literal_global.52
- _objc_msgSend$_displayableImageForImage:withRequiredImageSize:fallbackImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateGlyph:shouldGenerateThumbnail:
- _objc_msgSend$_downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:
- _objc_msgSend$initWithConfiguration:imageSize:title:url:baseImage:isThumbnail:
- _objc_msgSend$resultForFetchFailureWithHost:pageRequestDidSucceed:response:error:
- _objc_msgSend$resultWithFavicon:iconData:iconURL:host:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:faviconInfoFromWebView:
- _objc_msgSend$resultWithTouchIcon:host:isFavicon:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CDzSugCyKAWUw8uUR6n2YjwH9G4LwHfkB_tMTSo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "@104@0:8@16{CGSize=dd}24d40q48q56d64@72d80@88@96"
+ "@60@0:8@16@24B32B36@40B48@52"
+ "@64@0:8@16{CGSize=dd}24@40@48@56"
+ "@80@0:8@16@24@32@40B48@52B60@64@72"
+ "_downloadFirstValidImageWithURLs:inURLSession:urlsToResponsesDictionary:failedURLDownloadsToErrorsDictionary:options:completionHandler:"
+ "_reportFetchFailureWithError:"
+ "didCompleteSiteIconFetchOfType:iconURL:iconSize:didSucceed:didUseOffScreenWebView:numberOfDownloadAttempts:"
+ "didFailSiteIconDownloadForFetchType:iconURL:iconSize:didUseOffScreenWebView:response:error:"
+ "displayableImageForImage:withRequiredImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:"
+ "iconMetadata"
+ "imageMetadata"
+ "initWithConfiguration:imageSize:title:url:baseImage:"
+ "maximumAvailableSizeFromFaviconInfo:"
+ "reportFetchCompletionOfType:forIconURL:iconSize:didSucceed:didUseOffScreenWebView:response:error:"
+ "reportFetchCompletionOfType:forIconURLs:responses:errors:lastFetchedURL:lastFetchedIcon:didUseOffScreenWebView:"
+ "reportFetchCompletionWithMetadata:error:didUseOffScreenWebView:"
+ "resultForFetchFailureWithHost:response:higherPriorityIconDownloadFailedDueToNetworkError:error:"
+ "resultWithFavicon:iconData:iconURL:host:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:error:faviconInfoFromWebView:"
+ "resultWithTouchIcon:host:isFavicon:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:error:"
+ "v24@?0@\"WBSFaviconInfoFromWebView\"8@\"NSError\"16"
+ "v28@?0@\"NSData\"8B16@\"NSError\"20"
+ "v28@?0@\"NSURLResponse\"8@\"NSError\"16B24"
+ "v32@?0@\"UIImage\"8@\"NSData\"16@\"NSURL\"24"
+ "v48@?0@\"UIImage\"8@\"NSData\"16@\"NSURL\"24@\"NSDictionary\"32@\"NSDictionary\"40"
+ "v64@0:8@16@24@32@40Q48@?56"
+ "v68@0:8q16@24@32@40@48@56B64"
+ "v72@0:8q16@24{CGSize=dd}32B48B52@56@64"
+ "{CGSize=dd}24@0:8@16"
- "/AppleInternal/Library/BuildRoots/4~CCm8ugDCp2v8e1bco3yfclNvZuUoRBFfJ2frZKA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "@108@0:8@16{CGSize=dd}24d40q48q56d64@72d80@88@96B104"
- "@128@0:8@16{CGSize=dd}24{CGSize=dd}40d56q64q72d80@88d96@104@112B120B124"
- "@52@0:8@16@24B32B36@40B48"
- "@68@0:8@16{CGSize=dd}24@40@48@56B64"
- "@72@0:8@16@24@32@40B48@52B60@64"
- "TB,R,N,V_isThumbnail"
- "_displayableImageForImage:withRequiredImageSize:fallbackImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateGlyph:shouldGenerateThumbnail:"
- "_downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:"
- "_isThumbnail"
- "displayableImageForImage:withRequiredImageSize:fontSize:fontWeight:fontDesign:baselineOffset:backgroundColor:cornerRadius:title:url:shouldGenerateThumbnail:"
- "initWithConfiguration:imageSize:title:url:baseImage:isThumbnail:"
- "isThumbnail"
- "resultForFetchFailureWithHost:pageRequestDidSucceed:response:error:"
- "resultWithFavicon:iconData:iconURL:host:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:faviconInfoFromWebView:"
- "resultWithTouchIcon:host:isFavicon:pageRequestDidSucceed:response:higherPriorityIconDownloadFailedDueToNetworkError:"
- "v16@?0@\"NSURLResponse\"8"
- "v16@?0@\"WBSFaviconInfoFromWebView\"8"
- "v20@?0@\"NSData\"8B16"
- "v40@?0@\"UIImage\"8@\"NSData\"16@\"NSURL\"24@\"NSURLResponse\"32"
- "v48@?0@\"UIImage\"8@\"NSData\"16@\"NSURL\"24@\"NSURLResponse\"32@\"NSDictionary\"40"

```
