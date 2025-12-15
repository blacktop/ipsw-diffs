## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-623.1.14.10.9
-  __TEXT.__text: 0x13ae10
-  __TEXT.__auth_stubs: 0x3180
-  __TEXT.__objc_methlist: 0xbd0c
+623.2.2.0.0
+  __TEXT.__text: 0x13c094
+  __TEXT.__auth_stubs: 0x3170
+  __TEXT.__objc_methlist: 0xbdb4
   __TEXT.__const: 0x33b0
-  __TEXT.__gcc_except_tab: 0x6ef8
-  __TEXT.__cstring: 0x136b5
+  __TEXT.__gcc_except_tab: 0x707c
+  __TEXT.__cstring: 0x139f5
   __TEXT.__ustring: 0x2810
   __TEXT.__oslogstring: 0xaaad
   __TEXT.__dlopen_cstrs: 0x157

   __TEXT.__swift_as_entry: 0xf8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x6780
+  __TEXT.__unwind_info: 0x6820
   __TEXT.__eh_frame: 0x35c0
   __TEXT.__objc_classname: 0x1a78
-  __TEXT.__objc_methname: 0x253cc
-  __TEXT.__objc_methtype: 0x4020
-  __TEXT.__objc_stubs: 0x12060
-  __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__const: 0x4fb0
+  __TEXT.__objc_methname: 0x2568b
+  __TEXT.__objc_methtype: 0x40a5
+  __TEXT.__objc_stubs: 0x120a0
+  __DATA_CONST.__got: 0xe78
+  __DATA_CONST.__const: 0x5150
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d00
+  __DATA_CONST.__objc_selrefs: 0x6d68
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x498
-  __DATA_CONST.__objc_arraydata: 0x2a10
-  __AUTH_CONST.__auth_got: 0x18d8
+  __DATA_CONST.__objc_arraydata: 0x2a20
+  __AUTH_CONST.__auth_got: 0x18d0
   __AUTH_CONST.__const: 0x6aa0
-  __AUTH_CONST.__cfstring: 0x193c0
-  __AUTH_CONST.__objc_const: 0x137b0
-  __AUTH_CONST.__objc_intobj: 0x840
+  __AUTH_CONST.__cfstring: 0x199a0
+  __AUTH_CONST.__objc_const: 0x137f0
+  __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH_CONST.__objc_arrayobj: 0x570
+  __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH.__objc_data: 0x2710
   __AUTH.__data: 0x618
   __DATA.__objc_ivar: 0xc40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0DB2735B-B91D-3C4D-8356-9FC85018F88F
-  Functions: 7818
-  Symbols:   20843
-  CStrings:  13121
+  UUID: 30738404-7112-3A7C-85F5-6922B4E13D88
+  Functions: 7837
+  Symbols:   20904
+  CStrings:  13233
 
Symbols:
+ +[WBSUniqueFilenameEnumerator writeUniqueFileAtURL:error:usingBlock:]
+ -[NSData(SafariCoreExtras) safari_writeToUniqueFileURL:error:]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_copyItemAtURL:toURLWithUniqueName:error:]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_createDirectoryWithUniqueNameAtURL:error:]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_moveItemAtURL:toURLWithUniqueName:error:]
+ -[NSURL(SafariCoreExtras) safari_fallbackFaviconURL]
+ -[NSURL(SafariCoreExtras) safari_fallbackPrecomposedTouchIconURL]
+ -[NSURL(SafariCoreExtras) safari_fallbackTouchIconURL]
+ -[NSURL(SafariCoreExtras) safari_isOnBootVolume]
+ -[NSURL(SafariCoreExtras) safari_volumeName]
+ -[WBSAnalyticsLogger _recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:]
+ -[WBSAnalyticsLogger didCompleteSiteIconFetchOfType:iconURL:iconSize:didSucceed:didUseOffScreenWebView:numberOfDownloadAttempts:]
+ -[WBSAnalyticsLogger didFailSiteIconDownloadForFetchType:iconURL:iconSize:didUseOffScreenWebView:response:error:]
+ -[WBSUniqueFilenameEnumerator writeUniqueFileInDirectoryAtURL:error:usingBlock:]
+ GCC_except_table449
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table452
+ GCC_except_table453
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table57
+ _NSURLVolumeIdentifierKey
+ _NSURLVolumeLocalizedNameKey
+ __OBJC_$_CLASS_METHODS_WBSUniqueFilenameEnumerator
+ __ZL18siteIconTypeForURLP5NSURL
+ __ZL20siteIconFormatForURLP5NSURL
+ ___112-[NSFileManager(SafariNSFileManagerExtras) safari_removeContentsOfDirectory:preservingContainerManagerMetadata:]_block_invoke.88
+ ___129-[WBSAnalyticsLogger didCompleteSiteIconFetchOfType:iconURL:iconSize:didSucceed:didUseOffScreenWebView:numberOfDownloadAttempts:]_block_invoke
+ ___162-[WBSAnalyticsLogger _recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:]_block_invoke
+ ___62-[NSData(SafariCoreExtras) safari_writeToUniqueFileURL:error:]_block_invoke
+ ___91-[NSFileManager(SafariNSFileManagerExtras) safari_copyItemAtURL:toURLWithUniqueName:error:]_block_invoke
+ ___91-[NSFileManager(SafariNSFileManagerExtras) safari_moveItemAtURL:toURLWithUniqueName:error:]_block_invoke
+ ___92-[NSFileManager(SafariNSFileManagerExtras) safari_createDirectoryWithUniqueNameAtURL:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_B24?0"NSURL"8^16ls32l8
+ ___block_descriptor_40_ea8_32s_e19_B24?0"NSURL"8^16ls32l8
+ ___block_descriptor_48_ea8_32s40s_e19_B24?0"NSURL"8^16ls32l8s40l8
+ ___block_descriptor_74_ea8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_97_ea8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_literal_global.1004
+ ___block_literal_global.1006
+ ___block_literal_global.1040
+ ___block_literal_global.1106
+ ___block_literal_global.1255
+ ___block_literal_global.1257
+ ___block_literal_global.1280
+ ___block_literal_global.1282
+ ___block_literal_global.1284
+ ___block_literal_global.1354
+ ___block_literal_global.1356
+ ___block_literal_global.1358
+ ___block_literal_global.638
+ ___block_literal_global.65
+ ___block_literal_global.774
+ ___block_literal_global.779
+ ___block_literal_global.794
+ ___block_literal_global.806
+ ___block_literal_global.815
+ ___block_literal_global.824
+ ___block_literal_global.849
+ ___block_literal_global.918
+ _defaultFaviconLocation
+ _defaultPrecomposedTouchIconLocation
+ _defaultTouchIconLocation
+ _objc_msgSend$_recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$writeUniqueFileAtURL:error:usingBlock:
+ _objc_msgSend$writeUniqueFileInDirectoryAtURL:error:usingBlock:
- -[NSFileManager(SafariNSFileManagerExtras) safari_pathWithUniqueFilenameForPath:]
- -[NSURL(SafariCoreExtras) safari_URLWithUniqueFilename]
- __ZL10fileExistsP5NSURL
- ___112-[NSFileManager(SafariNSFileManagerExtras) safari_removeContentsOfDirectory:preservingContainerManagerMetadata:]_block_invoke.87
- ___block_literal_global.1000
- ___block_literal_global.1034
- ___block_literal_global.1100
- ___block_literal_global.1249
- ___block_literal_global.1251
- ___block_literal_global.1256
- ___block_literal_global.1258
- ___block_literal_global.1260
- ___block_literal_global.1342
- ___block_literal_global.1344
- ___block_literal_global.1346
- ___block_literal_global.632
- ___block_literal_global.64
- ___block_literal_global.768
- ___block_literal_global.773
- ___block_literal_global.788
- ___block_literal_global.800
- ___block_literal_global.809
- ___block_literal_global.818
- ___block_literal_global.843
- ___block_literal_global.912
- ___block_literal_global.998
- _lstat
- _objc_msgSend$safari_URLWithUniqueFilename
- _objc_msgSend$safari_filenameByFixingIllegalCharacters
CStrings:
+ "/apple-touch-icon-precomposed.png"
+ "/apple-touch-icon.png"
+ "/favicon.ico"
+ "@40@0:8@16^@24@?32"
+ "B24@?0@\"NSURL\"8^@16"
+ "_recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:"
+ "add bookmark from page menu"
+ "add to bookmarks"
+ "add to favorites"
+ "add to quick note"
+ "add to reading list"
+ "add to reading list from page menu"
+ "avif"
+ "com.apple.Safari.SiteIcons.DownloadFailed"
+ "com.apple.Safari.SiteIcons.FetchCompleted"
+ "didCompleteSiteIconFetchOfType:iconURL:iconSize:didSucceed:didUseOffScreenWebView:numberOfDownloadAttempts:"
+ "didFailSiteIconDownloadForFetchType:iconURL:iconSize:didUseOffScreenWebView:response:error:"
+ "didSucceed"
+ "didUseOffScreenWebView"
+ "errorCode"
+ "errorDomain"
+ "failureUUID"
+ "favicon"
+ "fetchType"
+ "find"
+ "heic"
+ "heif"
+ "hide toolbar"
+ "httpStatusCode"
+ "iconFormat"
+ "iconHeight"
+ "iconType"
+ "iconWidth"
+ "moveItemAtURL:toURL:error:"
+ "numberOfDownloadAttempts"
+ "page format more menu"
+ "pin tab"
+ "private tab"
+ "read this"
+ "reader from page menu"
+ "reload with private relay"
+ "report web compatibility issue"
+ "safari_copyItemAtURL:toURLWithUniqueName:error:"
+ "safari_createDirectoryWithUniqueNameAtURL:error:"
+ "safari_fallbackFaviconURL"
+ "safari_fallbackPrecomposedTouchIconURL"
+ "safari_fallbackTouchIconURL"
+ "safari_isOnBootVolume"
+ "safari_moveItemAtURL:toURLWithUniqueName:error:"
+ "safari_volumeName"
+ "safari_writeToUniqueFileURL:error:"
+ "scribble"
+ "scribble + content blocker"
+ "toggle content blockers"
+ "toggle desktop site"
+ "touch-icon"
+ "touch-icon-precomposed"
+ "translate from page menu"
+ "v64@0:8q16@24{CGSize=dd}32B48B52Q56"
+ "v68@0:8q16@24{CGSize=dd}32B48@52@60"
+ "v84@0:8q16q24q32{CGSize=dd}40@56B64q68@76"
+ "view security information"
+ "voice search"
+ "writeUniqueFileAtURL:error:usingBlock:"
+ "writeUniqueFileInDirectoryAtURL:error:usingBlock:"
+ "zoom in"
+ "zoom out"
- "safari_URLWithUniqueFilename"
- "safari_pathWithUniqueFilenameForPath:"

```
