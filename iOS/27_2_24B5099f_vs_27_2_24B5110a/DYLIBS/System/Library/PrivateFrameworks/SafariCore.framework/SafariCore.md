## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-625.2.7.1.0
-  __TEXT.__text: 0x1e4e64
-  __TEXT.__objc_methlist: 0xd34c
+625.2.8.10.4
+  __TEXT.__text: 0x1e576c
+  __TEXT.__objc_methlist: 0xd354
   __TEXT.__const: 0x7d84
-  __TEXT.__gcc_except_tab: 0x7930
-  __TEXT.__cstring: 0x171c7
+  __TEXT.__gcc_except_tab: 0x7974
+  __TEXT.__cstring: 0x17237
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe721
+  __TEXT.__oslogstring: 0xe7f1
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__constg_swiftt: 0x2380
   __TEXT.__swift5_typeref: 0x2706

   __TEXT.__swift5_capture: 0x154c
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xbf18
-  __TEXT.__eh_frame: 0xa718
+  __TEXT.__unwind_info: 0xbf58
+  __TEXT.__eh_frame: 0xa778
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5b80
+  __DATA_CONST.__const: 0x5b88
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7710
+  __DATA_CONST.__objc_selrefs: 0x7718
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x2aa0
   __DATA_CONST.__got: 0x13c8
-  __AUTH_CONST.__const: 0xb3b8
-  __AUTH_CONST.__cfstring: 0x1af60
+  __AUTH_CONST.__const: 0xb3d8
+  __AUTH_CONST.__cfstring: 0x1afa0
   __AUTH_CONST.__objc_const: 0x165f0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
-  __AUTH_CONST.__auth_got: 0x21b8
+  __AUTH_CONST.__auth_got: 0x21c8
   __AUTH.__objc_data: 0x748
   __AUTH.__data: 0x2c8
   __DATA.__objc_ivar: 0xd34
-  __DATA.__data: 0x3680
+  __DATA.__data: 0x37c0
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x45e0
   __DATA_DIRTY.__data: 0x1bb8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11438
-  Symbols:   12119
-  CStrings:  5290
+  Functions: 11468
+  Symbols:   12127
+  CStrings:  5297
 
Symbols:
+ -[NSFileManager(SafariNSFileManagerExtras) safari_pebbleSafariContainer]
+ -[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:pageLoadSource:]
+ GCC_except_table54
+ GCC_except_table74
+ _WBSCloudBookmarkListRecordNamePinnedSuggestions
+ __ZZ72-[NSFileManager(SafariNSFileManagerExtras) safari_pebbleSafariContainer]E12containerURL
+ __ZZ72-[NSFileManager(SafariNSFileManagerExtras) safari_pebbleSafariContainer]E9onceToken
+ ___72-[NSFileManager(SafariNSFileManagerExtras) safari_pebbleSafariContainer]_block_invoke
+ ___94-[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:pageLoadSource:]_block_invoke
+ _container_get_path
+ _container_query_set_group_identifiers
- -[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:]
- GCC_except_table67
- ___79-[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:]_block_invoke
CStrings:
+ "Failed to consume sandbox extension for BrowserKit group container"
+ "Failed to get BrowserKit group container for primary persona: %{public}s"
+ "Failed to get Pebble Safari group container path, groupID = %{public}@"
+ "PebbleDataFetching"
+ "Pinned Suggestions"
+ "WebContentRestrictions"
+ "group.com.apple.safari.pebble"
+ "pageLoadSource"
- "wasUserLoggedIn"
```
