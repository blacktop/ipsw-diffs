## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-625.1.29.10.29
-  __TEXT.__text: 0x178960
-  __TEXT.__objc_methlist: 0x1bd4c
-  __TEXT.__const: 0x2eb4
-  __TEXT.__cstring: 0xd470
-  __TEXT.__gcc_except_tab: 0xfc84
+625.2.4.1.0
+  __TEXT.__text: 0x17a3d0
+  __TEXT.__objc_methlist: 0x1bdbc
+  __TEXT.__const: 0x2ec4
+  __TEXT.__cstring: 0xd640
+  __TEXT.__gcc_except_tab: 0xfe5c
   __TEXT.__dlopen_cstrs: 0xb7f
-  __TEXT.__oslogstring: 0x81d7
+  __TEXT.__oslogstring: 0x83a7
   __TEXT.__ustring: 0x3774
-  __TEXT.__swift5_typeref: 0x6ac
-  __TEXT.__swift5_capture: 0x47c
+  __TEXT.__swift5_typeref: 0x6b0
+  __TEXT.__swift5_capture: 0x49c
   __TEXT.__constg_swiftt: 0x218
   __TEXT.__swift5_reflstr: 0x108
   __TEXT.__swift5_fieldmd: 0x148

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x7c
   __TEXT.__swift_as_cont: 0xfc
-  __TEXT.__unwind_info: 0xa5c0
+  __TEXT.__unwind_info: 0xa628
   __TEXT.__eh_frame: 0x1208
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x7818
   __DATA_CONST.__objc_classlist: 0xa50
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x8e8
+  __DATA_CONST.__objc_protolist: 0x8e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12328
+  __DATA_CONST.__objc_selrefs: 0x12390
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x858
-  __DATA_CONST.__objc_arraydata: 0x588
-  __DATA_CONST.__got: 0x2710
-  __AUTH_CONST.__const: 0x2220
-  __AUTH_CONST.__cfstring: 0xc3e0
-  __AUTH_CONST.__objc_const: 0x2c6a8
+  __DATA_CONST.__objc_arraydata: 0x5a8
+  __DATA_CONST.__got: 0x2728
+  __AUTH_CONST.__const: 0x2270
+  __AUTH_CONST.__cfstring: 0xc640
+  __AUTH_CONST.__objc_const: 0x2c700
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x1488
+  __AUTH_CONST.__auth_got: 0x14a8
   __AUTH.__objc_data: 0x5e98
   __AUTH.__data: 0x2e0
-  __DATA.__objc_ivar: 0x1f24
-  __DATA.__data: 0x69b0
+  __DATA.__objc_ivar: 0x1f34
+  __DATA.__data: 0x6950
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9284
-  Symbols:   24487
-  CStrings:  2549
+  Functions: 9308
+  Symbols:   24523
+  CStrings:  2573
 
Symbols:
+ -[SFWebViewController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:watchdogTimeout:completionHandler:]
+ -[_SFBrowserContentViewController _automaticPasswordChangeInitialLoadDidFailWithError:]
+ -[_SFBrowserContentViewController _logAutomaticPasswordChangeNavigationMilestone:navigation:error:]
+ -[_SFBrowserContentViewController _updateOverlayStateForDigitalHealthTracking:]
+ -[_SFDynamicBarAnimator synchronizedValueForHiddenValue:shownValue:]
+ -[_SFFormAutoFillController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:watchdogTimeout:completionHandler:]
+ -[_SFWebAppServiceViewController _guidedBrowsingReportingTabForViewController:]
+ -[_SFWebAppServiceViewController _reportBlockedGuidedBrowsingNavigationAction:isMainFrameNavigation:inViewController:]
+ -[_SFWebAppServiceViewController _reportGuidedBrowsingCurrentURLForViewController:]
+ -[_SFWebAppServiceViewController _reportGuidedBrowsingNavigationEventWithURL:httpMethod:statusCode:wasBlocked:forTab:]
+ -[_SFWebAppServiceViewController _reportGuidedBrowsingSameDocumentNavigationForViewController:]
+ -[_SFWebAppServiceViewController webViewController:decidePolicyForNavigationResponse:decisionHandler:]
+ -[_SFWebAppServiceViewController webViewController:didCommitNavigation:]
+ -[_SFWebAppServiceViewController webViewController:didSameDocumentNavigation:ofType:]
+ -[_SFWebAppTab pendingHTTPMethod]
+ -[_SFWebAppTab pendingStatusCode]
+ -[_SFWebAppTab setPendingHTTPMethod:]
+ -[_SFWebAppTab setPendingStatusCode:]
+ GCC_except_table583
+ GCC_except_table587
+ GCC_except_table590
+ GCC_except_table596
+ GCC_except_table598
+ GCC_except_table601
+ GCC_except_table606
+ GCC_except_table613
+ GCC_except_table619
+ GCC_except_table622
+ GCC_except_table624
+ GCC_except_table629
+ GCC_except_table631
+ GCC_except_table633
+ GCC_except_table638
+ GCC_except_table641
+ GCC_except_table645
+ GCC_except_table647
+ GCC_except_table650
+ GCC_except_table657
+ GCC_except_table662
+ GCC_except_table664
+ GCC_except_table671
+ GCC_except_table672
+ GCC_except_table673
+ _OBJC_CLASS_$_SFStrongPasswordGenerator
+ _OBJC_CLASS_$_WBSUsageRetentionDonationManager
+ _OBJC_IVAR_$__SFBrowserContentViewController._currentAutomaticPasswordChangeNavigationDidRenderVisibleContent
+ _OBJC_IVAR_$__SFBrowserContentViewController._hasCompletedAutomaticPasswordChangeNavigation
+ _OBJC_IVAR_$__SFFormAutoFillController._pageLevelAutoFillStaleOneTimeCodeThresholdDate
+ _OBJC_IVAR_$__SFWebAppTab._pendingHTTPMethod
+ _OBJC_IVAR_$__SFWebAppTab._pendingStatusCode
+ _WBSEnableGraphicIconsInCompletionListKey
+ _WBSEnableRecentSearchesStartPageModuleAtTopOfStartPageKey
+ ___189-[_SFFormAutoFillController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:watchdogTimeout:completionHandler:]_block_invoke
+ ___189-[_SFFormAutoFillController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:watchdogTimeout:completionHandler:]_block_invoke_2
+ ___79-[_SFBrowserContentViewController _updateOverlayStateForDigitalHealthTracking:]_block_invoke
+ ___79-[_SFBrowserContentViewController _updateOverlayStateForDigitalHealthTracking:]_block_invoke_2
+ ___block_descriptor_72_ea8_32s40s48s56bs_e28_v20?0"WBSFormMetadata"8B16ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_automaticPasswordChangeInitialLoadDidFailWithError:
+ _objc_msgSend$_guidedBrowsingReportingTabForViewController:
+ _objc_msgSend$_logAutomaticPasswordChangeNavigationMilestone:navigation:error:
+ _objc_msgSend$_reportBlockedGuidedBrowsingNavigationAction:isMainFrameNavigation:inViewController:
+ _objc_msgSend$_reportGuidedBrowsingCurrentURLForViewController:
+ _objc_msgSend$_reportGuidedBrowsingNavigationEventWithURL:httpMethod:statusCode:wasBlocked:forTab:
+ _objc_msgSend$_reportGuidedBrowsingSameDocumentNavigationForViewController:
+ _objc_msgSend$_updateOverlayStateForDigitalHealthTracking:
+ _objc_msgSend$autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:
+ _objc_msgSend$currentURLChanged:inTabWithUUID:
+ _objc_msgSend$donateAutoFillForFormType:fieldCount:
+ _objc_msgSend$donateAutoFillWithCategory:fieldCount:
+ _objc_msgSend$donateDistractionControlOpenedWebsite
+ _objc_msgSend$donateExtensionUsedWithType:
+ _objc_msgSend$initForStrongPasswordGenerator:passwordRules:overrideApplicationIdentifier:
+ _objc_msgSend$pendingHTTPMethod
+ _objc_msgSend$pendingStatusCode
+ _objc_msgSend$performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:watchdogTimeout:completionHandler:
+ _objc_msgSend$reportNavigationEventWithURL:httpMethod:statusCode:wasBlocked:forTabWithUUID:
+ _objc_msgSend$setPendingHTTPMethod:
+ _objc_msgSend$setPendingStatusCode:
+ _objc_msgSend$staleOneTimeCodeThresholdDate
+ _objc_msgSend$statusCode
+ _swift_isEscapingClosureAtFileLocation
+ _swift_retain_x22
+ _symbolic Ig_
- -[SFWebViewController _webView:requestPresentingViewControllerWithCompletionHandler:]
- -[SFWebViewController _webViewDidExitElementFullscreen:]
- -[SFWebViewController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:watchdogTimeout:completionHandler:]
- -[_SFFormAutoFillController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:watchdogTimeout:completionHandler:]
- GCC_except_table116
- GCC_except_table584
- GCC_except_table588
- GCC_except_table595
- GCC_except_table597
- GCC_except_table600
- GCC_except_table602
- GCC_except_table612
- GCC_except_table618
- GCC_except_table621
- GCC_except_table623
- GCC_except_table627
- GCC_except_table630
- GCC_except_table632
- GCC_except_table635
- GCC_except_table639
- GCC_except_table642
- GCC_except_table646
- GCC_except_table648
- GCC_except_table654
- GCC_except_table658
- GCC_except_table665
- GCC_except_table667
- _OBJC_CLASS_$_SFAutoFillHelperProxy
- _OBJC_IVAR_$__SFBrowserContentViewController._hasStartedAutomaticPasswordChange
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKFullscreenDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__WKFullscreenDelegate
- __OBJC_$_PROTOCOL_REFS__WKFullscreenDelegate
- __OBJC_LABEL_PROTOCOL_$__WKFullscreenDelegate
- __OBJC_PROTOCOL_$__WKFullscreenDelegate
- ___159-[_SFFormAutoFillController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:watchdogTimeout:completionHandler:]_block_invoke
- ___159-[_SFFormAutoFillController performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:watchdogTimeout:completionHandler:]_block_invoke_2
- ___63-[_SFBrowserContentViewController _updateDigitalHealthTracking]_block_invoke_2
- ___63-[_SFBrowserContentViewController _updateDigitalHealthTracking]_block_invoke_3
- ___block_descriptor_56_ea8_32s40s48bs_e28_v20?0"WBSFormMetadata"8B16ls32l8s40l8s48l8
- _objc_msgSend$_setFullscreenDelegate:
- _objc_msgSend$autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:
- _objc_msgSend$didFinishLoad
- _objc_msgSend$initForAutoFillHelper:passwordRules:overrideApplicationIdentifier:
- _objc_msgSend$performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:watchdogTimeout:completionHandler:
- _objc_msgSend$setItemsUseContentSafeAreaLayoutMargins:
- _objc_msgSend$webViewController:requestPresentingViewControllerWithCompletionHandler:
- _objc_msgSend$webViewControllerDidExitElementFullscreen:
CStrings:
+ "&appid=aaplw_r"
+ "&enriched=1"
+ "<nil>"
+ "<none>"
+ "Failed to load change password page: %@"
+ "Initial page load did not finish within %.0f seconds, but the page rendered visible content; starting password change anyways"
+ "Initial page load failed after %.2f seconds: %{public}@"
+ "Navigating: %{public}@ at %.2fs (navigation %p, URL <%{private}@>, error %{public}@)"
+ "Navigating: decidePolicyForNavigationResponse for main frame (HTTP status %{public}ld, MIME type %{public}@, URL <%{private}@>)"
+ "Navigating: willPerformClientRedirect to <%{private}@> after %.2fs delay"
+ "com.bing.www"
+ "com.yahoo.www"
+ "didCancelClientRedirect"
+ "didCommitNavigation"
+ "didFailNavigation"
+ "didFailProvisionalNavigation"
+ "didFinishDocumentLoad"
+ "didFinishNavigation"
+ "didFirstVisuallyNonEmptyLayout"
+ "didReceiveServerRedirectForProvisionalNavigation"
+ "didStartProvisionalNavigation"
+ "loadRequest (not deferred)"
+ "loadRequest (resolved to fallback URL)"
+ "loadRequest (resolved, unchanged)"
```
