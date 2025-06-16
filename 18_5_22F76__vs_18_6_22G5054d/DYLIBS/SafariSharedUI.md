## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0xe4548
+621.3.6.10.1
+  __TEXT.__text: 0xe4640
   __TEXT.__auth_stubs: 0x11f0
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xbd68
+  __TEXT.__objc_methlist: 0xbd70
   __TEXT.__const: 0x2ae8
   __TEXT.__oslogstring: 0x8020
   __TEXT.__cstring: 0xf4cc
-  __TEXT.__gcc_except_tab: 0xe4a4
+  __TEXT.__gcc_except_tab: 0xe4b0
   __TEXT.__ustring: 0x2a30
   __TEXT.__dlopen_cstrs: 0x3b5
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x63e0
   __TEXT.__objc_classname: 0x1deb
-  __TEXT.__objc_methname: 0x2a52e
-  __TEXT.__objc_methtype: 0x5684
-  __TEXT.__objc_stubs: 0x19860
+  __TEXT.__objc_methname: 0x2a5bc
+  __TEXT.__objc_methtype: 0x569c
+  __TEXT.__objc_stubs: 0x198a0
   __DATA_CONST.__got: 0x1278
   __DATA_CONST.__const: 0x68e8
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8438
+  __DATA_CONST.__objc_selrefs: 0x8450
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x19f0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7BBDC450-2580-3F75-9D5D-6E694540E401
-  Functions: 5459
-  Symbols:   20570
-  CStrings:  11317
+  UUID: 1833EF30-C768-3ED9-8483-41BC8910B8C7
+  Functions: 5460
+  Symbols:   20574
+  CStrings:  11321
 
Symbols:
+ +[WKWebsiteDataStore(SafariSharedExtras) safari_defaultDataStoreWithSourceApplicationSecondaryIdentifier:]
+ -[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]
+ ___150-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke
+ ___150-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_2
+ ___150-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:]_block_invoke_3
+ ___59-[WBSTouchIconFetchOperation _downloadPendingTouchIconURLs]_block_invoke.73
+ ___74-[WBSTouchIconFetchOperation didFetchTouchIconURLs:andFaviconURLs:forURL:]_block_invoke.81
+ ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke.69
+ ___block_descriptor_112_ea8_32s40s48s56s64s72s80s88bs_e17_v16?0"UIImage"8ls88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_ea8_32s40s48s56s64s72bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8s48l8s72l8s56l8s64l8
+ _objc_msgSend$_downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:
+ _objc_msgSend$_setPrivacyProxyFailClosed:
+ _objc_msgSend$safari_defaultDataStoreWithSourceApplicationSecondaryIdentifier:
+ _objc_msgSend$setSourceApplicationSecondaryIdentifier:
- -[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:completionHandler:]
- ___142-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:completionHandler:]_block_invoke
- ___142-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:completionHandler:]_block_invoke_2
- ___142-[WBSImageFetchingURLSessionTaskManager _downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:completionHandler:]_block_invoke_3
- ___59-[WBSTouchIconFetchOperation _downloadPendingTouchIconURLs]_block_invoke.70
- ___74-[WBSTouchIconFetchOperation didFetchTouchIconURLs:andFaviconURLs:forURL:]_block_invoke.78
- ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke.66
- ___block_descriptor_104_ea8_32s40s48s56s64s72s80s88bs_e17_v16?0"UIImage"8ls88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_88_ea8_32s40s48s56s64s72bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8s48l8s72l8s56l8s64l8
- _objc_msgSend$_downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:completionHandler:
- _objc_msgSend$userVisibleQueryFromSearchURL:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugDlHb-wgX-iyhpmqkTmYPoyKTBVY_lvdvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "_downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:options:completionHandler:"
+ "_setPrivacyProxyFailClosed:"
+ "safari_defaultDataStoreWithSourceApplicationSecondaryIdentifier:"
+ "setSourceApplicationSecondaryIdentifier:"
+ "v56@0:8@16@24@32Q40@?48"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "_downloadFirstValidImageWithURLs:inURLSession:failedURLDownloadsToErrorsDictionary:completionHandler:"

```
