## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-623.2.4.0.0
-  __TEXT.__text: 0x13c1a0
+623.2.7.0.0
+  __TEXT.__text: 0x13c5e8
   __TEXT.__auth_stubs: 0x3170
-  __TEXT.__objc_methlist: 0xbdbc
-  __TEXT.__const: 0x33b0
-  __TEXT.__gcc_except_tab: 0x707c
-  __TEXT.__cstring: 0x139f5
+  __TEXT.__objc_methlist: 0xbdd4
+  __TEXT.__const: 0x33d0
+  __TEXT.__gcc_except_tab: 0x7074
+  __TEXT.__cstring: 0x13a05
   __TEXT.__ustring: 0x2810
-  __TEXT.__oslogstring: 0xaaad
+  __TEXT.__oslogstring: 0xab2d
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__swift5_typeref: 0x100f
   __TEXT.__swift5_fieldmd: 0x964

   __TEXT.__swift_as_entry: 0xf8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x6828
+  __TEXT.__unwind_info: 0x6848
   __TEXT.__eh_frame: 0x35c0
   __TEXT.__objc_classname: 0x1a78
-  __TEXT.__objc_methname: 0x256c1
-  __TEXT.__objc_methtype: 0x40a5
+  __TEXT.__objc_methname: 0x2570a
+  __TEXT.__objc_methtype: 0x4098
   __TEXT.__objc_stubs: 0x120a0
   __DATA_CONST.__got: 0xe78
-  __DATA_CONST.__const: 0x5150
+  __DATA_CONST.__const: 0x5128
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d70
+  __DATA_CONST.__objc_selrefs: 0x6d80
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x2a20
   __AUTH_CONST.__auth_got: 0x18d0
-  __AUTH_CONST.__const: 0x6aa0
+  __AUTH_CONST.__const: 0x6a80
   __AUTH_CONST.__cfstring: 0x199a0
-  __AUTH_CONST.__objc_const: 0x137f0
+  __AUTH_CONST.__objc_const: 0x13800
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 21F1AA76-D9DE-33D5-B33D-133F4EE1EFE0
-  Functions: 7839
-  Symbols:   20908
-  CStrings:  13234
+  UUID: 830DF010-1BDE-3D19-8E59-56BC80D51A98
+  Functions: 7844
+  Symbols:   20916
+  CStrings:  13238
 
Symbols:
+ +[NSBundle(SafariCoreExtras) safari_isMobileSafariInstalledWithValueIfUnknown:]
+ +[NSBundle(SafariCoreExtras) safari_isMobileSafariInstalledWithValueIfUnknown:].cold.1
+ -[WBSAnalyticsLogger _recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:didDetermineSize:didUseOffScreenWebView:httpStatusCode:error:]
+ -[WBSKeychainSyncingMonitor isKeychainSyncEnabled].cold.1
+ -[WBSSavedAccount effectiveTitleForExporting]
+ GCC_except_table201
+ GCC_except_table456
+ __ZL31siteIconBinnedValueForDimensiond
+ ___158-[WBSAnalyticsLogger _recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:didDetermineSize:didUseOffScreenWebView:httpStatusCode:error:]_block_invoke
+ _objc_msgSend$_recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:didDetermineSize:didUseOffScreenWebView:httpStatusCode:error:
- -[WBSAnalyticsLogger _recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:]
- GCC_except_table113
- GCC_except_table117
- GCC_except_table453
- ___162-[WBSAnalyticsLogger _recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:]_block_invoke
- ___block_descriptor_97_ea8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
- ___block_literal_global.592
- ___block_literal_global.604
- _objc_msgSend$_recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:
CStrings:
+ "Initial keychain status fetch timed out"
+ "Unable to determine Safari installation status, returning %{public}s: %{public}@"
+ "_recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:didDetermineSize:didUseOffScreenWebView:httpStatusCode:error:"
+ "didDetermineSize"
+ "effectiveTitleForExporting"
+ "iconBinnedHeight"
+ "iconBinnedWidth"
+ "safari_isMobileSafariInstalledWithValueIfUnknown:"
+ "v64@0:8q16q24q32B40B44q48@56"
- "_recursivelyReportSiteIconDownloadFailureWithFetchType:iconType:iconFormat:iconSize:failureUUID:didUseOffScreenWebView:httpStatusCode:error:"
- "failureUUID"
- "iconHeight"
- "iconWidth"
- "v84@0:8q16q24q32{CGSize=dd}40@56B64q68@76"

```
