## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

```diff

-296.10.0.0.0
-  __TEXT.__text: 0x113d44
+296.11.0.0.0
+  __TEXT.__text: 0x111250
   __TEXT.__auth_stubs: 0x1f00
-  __TEXT.__objc_methlist: 0x10c0c
-  __TEXT.__cstring: 0x8c41
-  __TEXT.__gcc_except_tab: 0x229e0
-  __TEXT.__const: 0x2324
+  __TEXT.__objc_methlist: 0x10794
+  __TEXT.__cstring: 0x8a01
+  __TEXT.__gcc_except_tab: 0x22380
+  __TEXT.__const: 0x22f4
   __TEXT.__ustring: 0x3d0
-  __TEXT.__oslogstring: 0x3bbb
+  __TEXT.__oslogstring: 0x3b8b
   __TEXT.__dlopen_cstrs: 0x9c7
   __TEXT.__swift5_typeref: 0xad8
   __TEXT.__constg_swiftt: 0x824

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__unwind_info: 0x86f8
+  __TEXT.__unwind_info: 0x8588
   __TEXT.__eh_frame: 0xc68
-  __TEXT.__objc_classname: 0x27b0
-  __TEXT.__objc_methname: 0x224a1
-  __TEXT.__objc_methtype: 0x4abd
-  __TEXT.__objc_stubs: 0x194c0
-  __DATA_CONST.__got: 0xe18
-  __DATA_CONST.__const: 0x2750
-  __DATA_CONST.__objc_classlist: 0x8e8
+  __TEXT.__objc_classname: 0x26d0
+  __TEXT.__objc_methname: 0x216ed
+  __TEXT.__objc_methtype: 0x435d
+  __TEXT.__objc_stubs: 0x18de0
+  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__const: 0x2730
+  __DATA_CONST.__objc_classlist: 0x8c8
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7828
+  __DATA_CONST.__objc_selrefs: 0x7560
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x680
+  __DATA_CONST.__objc_superrefs: 0x668
   __DATA_CONST.__objc_arraydata: 0x1608
   __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__const: 0x1f38
-  __AUTH_CONST.__cfstring: 0xddc0
-  __AUTH_CONST.__objc_const: 0x2e4b0
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__const: 0x1ef8
+  __AUTH_CONST.__cfstring: 0xda20
+  __AUTH_CONST.__objc_const: 0x2d598
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH.__objc_data: 0x30d0
+  __AUTH.__objc_data: 0x2f90
   __AUTH.__data: 0x4d8
-  __DATA.__objc_ivar: 0x1800
-  __DATA.__data: 0x1e18
+  __DATA.__objc_ivar: 0x17d0
+  __DATA.__data: 0x1c38
   __DATA.__bss: 0x1ae0
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x2968

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B4183A98-A7E6-32E1-AC83-4A91D3EF0C0E
-  Functions: 6718
-  Symbols:   23263
-  CStrings:  10507
+  UUID: 9CB96192-1D50-3EB2-A266-234BB59CD42E
+  Functions: 6671
+  Symbols:   23006
+  CStrings:  10300
 
Symbols:
+ ___55-[LPMetadataProvider _finishedPostProcessingWithError:]_block_invoke.141
+ ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.285
+ ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.288
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.148
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.151
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.152
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.150
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.153
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_3.154
+ ___Block_byref_object_copy_.139
+ ___Block_byref_object_dispose_.140
+ ___block_literal_global.256
- +[LPPresentationSpecializations isYouTubeEmbedURL:]
- +[LPPresentationSpecializations youTubeVideoComponentsForVideoURL:]
- -[LPMetadataProvider _propagateYouTubeTimestamps]
- -[LPYouTubePlayerScriptMessageHandler .cxx_destruct]
- -[LPYouTubePlayerScriptMessageHandler initWithPlayerView:]
- -[LPYouTubePlayerScriptMessageHandler userContentController:didReceiveScriptMessage:]
- -[LPYouTubePlayerView _evaluatePlayerCommand:]
- -[LPYouTubePlayerView _parameterScript]
- -[LPYouTubePlayerView _shouldUseElementFullScreen]
- -[LPYouTubePlayerView _webView:navigation:didFailProvisionalLoadInSubframe:withError:]
- -[LPYouTubePlayerView createVideoPlayerView]
- -[LPYouTubePlayerView dealloc]
- -[LPYouTubePlayerView didReceiveScriptMessage:]
- -[LPYouTubePlayerView dispatchErrorWithCode:]
- -[LPYouTubePlayerView layoutSubviews]
- -[LPYouTubePlayerView scrollViewDidScroll:]
- -[LPYouTubePlayerView webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:]
- -[LPYouTubePlayerView webView:decidePolicyForNavigationAction:preferences:decisionHandler:]
- -[LPYouTubePlayerView webView:didFailNavigation:withError:]
- -[LPYouTubePlayerView webView:didFailProvisionalNavigation:withError:]
- -[LPYouTubePlayerView webViewWebContentProcessDidTerminate:]
- -[LPYouTubePlayerView webViewWebContentProcessDidTerminate:].cold.1
- -[LPYouTubePlayerViewFullScreenDelegate _webViewDidExitElementFullscreen:]
- -[LPYouTubePlayerViewFullScreenDelegate _webViewWillExitElementFullscreen:]
- -[LPYouTubePlayerWebView allowFirstResponder]
- -[LPYouTubePlayerWebView becomeFirstResponder]
- -[LPYouTubePlayerWebView canBecomeFirstResponder]
- -[LPYouTubePlayerWebView setAllowFirstResponder:]
- -[LPYouTubeVideoView .cxx_destruct]
- -[LPYouTubeVideoView createVideoPlayerView]
- -[LPYouTubeVideoView enterCustomFullScreen]
- -[LPYouTubeVideoView initWithHost:video:style:posterFrame:posterFrameStyle:configuration:]
- -[LPYouTubeVideoView isMuted]
- -[LPYouTubeVideoView setAllowsUserInteractionWithVideoPlayer:]
- -[LPYouTubeVideoView setMuted:]
- -[LPYouTubeVideoView setPlaying:]
- -[LPYouTubeVideoView setVolume:]
- -[LPYouTubeVideoView shouldShowMuteButton]
- -[LPYouTubeVideoView usesCustomFullScreenImplementation]
- -[LPYouTubeVideoView usesSharedAudioSession]
- -[LPYouTubeVideoView volume]
- -[LPYouTubeVideoView youTubePlayer:didChangeToFullScreen:]
- -[LPYouTubeVideoView youTubePlayer:didChangeToState:]
- -[LPYouTubeVideoView youTubePlayer:didReceiveError:]
- _OBJC_CLASS_$_LPYouTubePlayerScriptMessageHandler
- _OBJC_CLASS_$_LPYouTubePlayerViewFullScreenDelegate
- _OBJC_CLASS_$_LPYouTubePlayerWebView
- _OBJC_CLASS_$_LPYouTubeVideoView
- _OBJC_CLASS_$_WKUserScript
- _OBJC_IVAR_$_LPVideo._youTubeURL
- _OBJC_IVAR_$_LPYouTubePlayerScriptMessageHandler._playerView
- _OBJC_IVAR_$_LPYouTubePlayerView._commandsPendingPlayerReadiness
- _OBJC_IVAR_$_LPYouTubePlayerView._fullScreenDelegate
- _OBJC_IVAR_$_LPYouTubePlayerView._ready
- _OBJC_IVAR_$_LPYouTubePlayerView._scriptMessageHandler
- _OBJC_IVAR_$_LPYouTubePlayerView._state
- _OBJC_IVAR_$_LPYouTubePlayerView._videoID
- _OBJC_IVAR_$_LPYouTubePlayerView._webView
- _OBJC_IVAR_$_LPYouTubePlayerWebView._allowFirstResponder
- _OBJC_IVAR_$_LPYouTubeVideoView._allowingInteractionUntilPlaybackResumes
- _OBJC_IVAR_$_LPYouTubeVideoView._platformYouTubeView
- _OBJC_METACLASS_$_LPYouTubePlayerScriptMessageHandler
- _OBJC_METACLASS_$_LPYouTubePlayerViewFullScreenDelegate
- _OBJC_METACLASS_$_LPYouTubePlayerWebView
- _OBJC_METACLASS_$_LPYouTubeVideoView
- _OBJC_METACLASS_$_WKWebView
- __OBJC_$_INSTANCE_METHODS_LPYouTubePlayerScriptMessageHandler
- __OBJC_$_INSTANCE_METHODS_LPYouTubePlayerViewFullScreenDelegate
- __OBJC_$_INSTANCE_METHODS_LPYouTubePlayerWebView
- __OBJC_$_INSTANCE_METHODS_LPYouTubeVideoView
- __OBJC_$_INSTANCE_VARIABLES_LPYouTubePlayerScriptMessageHandler
- __OBJC_$_INSTANCE_VARIABLES_LPYouTubePlayerWebView
- __OBJC_$_INSTANCE_VARIABLES_LPYouTubeVideoView
- __OBJC_$_PROP_LIST_LPYouTubePlayerScriptMessageHandler
- __OBJC_$_PROP_LIST_LPYouTubePlayerViewFullScreenDelegate
- __OBJC_$_PROP_LIST_LPYouTubePlayerWebView
- __OBJC_$_PROP_LIST_LPYouTubeVideoView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LPYouTubePlayerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WKUIDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKFullscreenDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WKScriptMessageHandler
- __OBJC_$_PROTOCOL_METHOD_TYPES_LPYouTubePlayerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WKScriptMessageHandler
- __OBJC_$_PROTOCOL_METHOD_TYPES_WKUIDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__WKFullscreenDelegate
- __OBJC_$_PROTOCOL_REFS_LPYouTubePlayerDelegate
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate
- __OBJC_$_PROTOCOL_REFS_WKScriptMessageHandler
- __OBJC_$_PROTOCOL_REFS_WKUIDelegate
- __OBJC_$_PROTOCOL_REFS__WKFullscreenDelegate
- __OBJC_CLASS_PROTOCOLS_$_LPYouTubePlayerScriptMessageHandler
- __OBJC_CLASS_PROTOCOLS_$_LPYouTubePlayerView
- __OBJC_CLASS_PROTOCOLS_$_LPYouTubePlayerViewFullScreenDelegate
- __OBJC_CLASS_PROTOCOLS_$_LPYouTubeVideoView
- __OBJC_CLASS_RO_$_LPYouTubePlayerScriptMessageHandler
- __OBJC_CLASS_RO_$_LPYouTubePlayerViewFullScreenDelegate
- __OBJC_CLASS_RO_$_LPYouTubePlayerWebView
- __OBJC_CLASS_RO_$_LPYouTubeVideoView
- __OBJC_LABEL_PROTOCOL_$_LPYouTubePlayerDelegate
- __OBJC_LABEL_PROTOCOL_$_UIScrollViewDelegate
- __OBJC_LABEL_PROTOCOL_$_WKScriptMessageHandler
- __OBJC_LABEL_PROTOCOL_$_WKUIDelegate
- __OBJC_LABEL_PROTOCOL_$__WKFullscreenDelegate
- __OBJC_METACLASS_RO_$_LPYouTubePlayerScriptMessageHandler
- __OBJC_METACLASS_RO_$_LPYouTubePlayerViewFullScreenDelegate
- __OBJC_METACLASS_RO_$_LPYouTubePlayerWebView
- __OBJC_METACLASS_RO_$_LPYouTubeVideoView
- __OBJC_PROTOCOL_$_LPYouTubePlayerDelegate
- __OBJC_PROTOCOL_$_UIScrollViewDelegate
- __OBJC_PROTOCOL_$_WKScriptMessageHandler
- __OBJC_PROTOCOL_$_WKUIDelegate
- __OBJC_PROTOCOL_$__WKFullscreenDelegate
- ___53-[LPYouTubeVideoView youTubePlayer:didChangeToState:]_block_invoke
- ___55-[LPMetadataProvider _finishedPostProcessingWithError:]_block_invoke.146
- ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.286
- ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.289
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.153
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.156
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.157
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.155
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.158
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_3.159
- ___91-[LPYouTubePlayerView webView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke
- ___97-[LPYouTubePlayerView webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:]_block_invoke
- ___Block_byref_object_copy_.144
- ___Block_byref_object_dispose_.145
- ___block_descriptor_32_e8_v12?0B8l
- ___block_literal_global.206
- ___block_literal_global.257
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$URLForResource:withExtension:
- _objc_msgSend$_clearOverrideLayoutParameters
- _objc_msgSend$_evaluatePlayerCommand:
- _objc_msgSend$_parameterScript
- _objc_msgSend$_propagateYouTubeTimestamps
- _objc_msgSend$_setCompositingBordersVisible:
- _objc_msgSend$_setFullscreenDelegate:
- _objc_msgSend$_setInlineMediaPlaybackRequiresPlaysInlineAttribute:
- _objc_msgSend$_setObject:forBundleParameter:
- _objc_msgSend$_shouldUseElementFullScreen
- _objc_msgSend$addScriptMessageHandler:name:
- _objc_msgSend$addUserScript:
- _objc_msgSend$becomeFirstResponder
- _objc_msgSend$builtInPlugInsURL
- _objc_msgSend$dataWithJSONObject:options:error:
- _objc_msgSend$didEncounterPlaybackError
- _objc_msgSend$didEncounterPossiblyTransientPlaybackError
- _objc_msgSend$didReceiveScriptMessage:
- _objc_msgSend$dispatchErrorWithCode:
- _objc_msgSend$evaluateJavaScript:completionHandler:
- _objc_msgSend$initWithPlayerView:
- _objc_msgSend$initWithSource:injectionTime:forMainFrameOnly:
- _objc_msgSend$initWithYouTubeURL:properties:
- _objc_msgSend$isMessagesOrMessagesViewService
- _objc_msgSend$isYouTubeEmbedURL:
- _objc_msgSend$loadVideoWithID:
- _objc_msgSend$navigationType
- _objc_msgSend$parseYouTubeTimeFormat:outTime:
- _objc_msgSend$processPool
- _objc_msgSend$removeScriptMessageHandlerForName:
- _objc_msgSend$resignFirstResponder
- _objc_msgSend$scrollView
- _objc_msgSend$setAllowFirstResponder:
- _objc_msgSend$setAllowsInlineMediaPlayback:
- _objc_msgSend$setAllowsPictureInPictureMediaPlayback:
- _objc_msgSend$setAllowsUserInteractionWithVideoPlayer:
- _objc_msgSend$setContentInsetAdjustmentBehavior:
- _objc_msgSend$setContentOffset:
- _objc_msgSend$setContentOffset:animated:
- _objc_msgSend$setDeviceManagementRestrictionsEnabled:
- _objc_msgSend$setElementFullscreenEnabled:
- _objc_msgSend$setFullScreen:
- _objc_msgSend$setInjectedBundleURL:
- _objc_msgSend$setMediaTypesRequiringUserActionForPlayback:
- _objc_msgSend$setShowsControls:
- _objc_msgSend$setUIDelegate:
- _objc_msgSend$stringWithContentsOfURL:encoding:error:
- _objc_msgSend$userContentController
- _objc_msgSend$youTubePlayer:didChangeToFullScreen:
- _objc_msgSend$youTubePlayer:didChangeToState:
- _objc_msgSend$youTubePlayer:didReceiveError:
- _objc_msgSend$youTubePlayerDidBecomeReady:
- _objc_msgSend$youTubeURL
- _objc_msgSend$youTubeVideoComponentsForVideoURL:
CStrings:
+ "T@\"NSURL\",R,&,N"
- "@\"LPYouTubePlayerScriptMessageHandler\""
- "@\"LPYouTubePlayerView\""
- "@\"LPYouTubePlayerViewFullScreenDelegate\""
- "@\"LPYouTubePlayerWebView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIViewController\"40@0:8@\"WKWebView\"16@\"WKPreviewElementInfo\"24@\"NSArray\"32"
- "@\"WKWebView\"48@0:8@\"WKWebView\"16@\"WKWebViewConfiguration\"24@\"WKNavigationAction\"32@\"WKWindowFeatures\"40"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"WKWebView\"16"
- "B32@0:8@\"WKWebView\"16@\"WKPreviewElementInfo\"24"
- "LPYouTubePlayerDelegate"
- "LPYouTubePlayerScriptMessageHandler"
- "LPYouTubePlayerView: Web Content process was terminated"
- "LPYouTubePlayerViewFullScreenDelegate"
- "LPYouTubePlayerWebView"
- "LPYouTubeVideoView"
- "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1"
- "T@\"NSURL\",R,&,N,V_youTubeURL"
- "TB,N,V_allowFirstResponder"
- "UIScrollViewDelegate"
- "URLByAppendingPathComponent:"
- "URLForResource:withExtension:"
- "WKScriptMessageHandler"
- "WKUIDelegate"
- "YouTubeContainer"
- "YouTubePlayer.wkbundle"
- "_WKFullscreenDelegate"
- "_allowFirstResponder"
- "_allowingInteractionUntilPlaybackResumes"
- "_clearOverrideLayoutParameters"
- "_commandsPendingPlayerReadiness"
- "_evaluatePlayerCommand:"
- "_fullScreenDelegate"
- "_parameterScript"
- "_platformYouTubeView"
- "_playerView"
- "_propagateYouTubeTimestamps"
- "_ready"
- "_scriptMessageHandler"
- "_setCompositingBordersVisible:"
- "_setFullscreenDelegate:"
- "_setInlineMediaPlaybackRequiresPlaysInlineAttribute:"
- "_setObject:forBundleParameter:"
- "_shouldUseElementFullScreen"
- "_webView:didFullscreenImageWithQuickLook:"
- "_webView:navigation:didFailProvisionalLoadInSubframe:withError:"
- "_webView:requestPresentingViewControllerWithCompletionHandler:"
- "_webViewDidEnterElementFullscreen:"
- "_webViewDidExitElementFullscreen:"
- "_webViewPreventDockingFromElementFullscreen:"
- "_webViewWillEnterElementFullscreen:"
- "_webViewWillExitElementFullscreen:"
- "_youTubeURL"
- "addScriptMessageHandler:name:"
- "addUserScript:"
- "allowFirstResponder"
- "becomeFirstResponder"
- "builtInPlugInsURL"
- "canBecomeFirstResponder"
- "controls"
- "dataWithJSONObject:options:error:"
- "didReceiveScriptMessage:"
- "dispatchErrorWithCode:"
- "enterElementFullScreen()"
- "enterVideoFullScreen()"
- "evaluateJavaScript:completionHandler:"
- "exitFullScreen()"
- "https://www.youtube.com/"
- "initWithPlayerView:"
- "initWithSource:injectionTime:forMainFrameOnly:"
- "isYouTubeEmbedURL:"
- "iv_load_policy"
- "mute()"
- "navigationType"
- "onError"
- "onPresentationModeChange"
- "onReady"
- "onStateChange"
- "pausePlaying()"
- "playerContainer"
- "playerVars"
- "processPool"
- "removeScriptMessageHandlerForName:"
- "resignFirstResponder"
- "scrollView"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "seekTo(%f)"
- "setAllowFirstResponder:"
- "setAllowsInlineMediaPlayback:"
- "setAllowsPictureInPictureMediaPlayback:"
- "setContentInsetAdjustmentBehavior:"
- "setContentOffset:"
- "setContentOffset:animated:"
- "setDeviceManagementRestrictionsEnabled:"
- "setElementFullscreenEnabled:"
- "setInjectedBundleURL:"
- "setMediaTypesRequiringUserActionForPlayback:"
- "setUIDelegate:"
- "showinfo"
- "startPlaying()"
- "startsPlayingMuted"
- "stringWithContentsOfURL:encoding:error:"
- "unMute()"
- "userContentController"
- "userContentController:didReceiveScriptMessage:"
- "v24@0:8@\"LPYouTubePlayerView\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v28@0:8@\"LPYouTubePlayerView\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v32@0:8@\"LPYouTubePlayerView\"16@\"NSError\"24"
- "v32@0:8@\"LPYouTubePlayerView\"16q24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"WKUserContentController\"16@\"WKScriptMessage\"24"
- "v32@0:8@\"WKWebView\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"WKWebView\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"WKWebView\"16@\"UIViewController\"24"
- "v32@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24"
- "v32@0:8@\"WKWebView\"16@?<v@?@\"UIViewController\"@\"NSError\">24"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"WKWebView\"16@\"NSString\"24@?<v@?q>32"
- "v40@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24@?<v@?@\"UIContextMenuConfiguration\">32"
- "v40@0:8@\"WKWebView\"16{CGSize=dd}24"
- "v40@0:8@16@24d32"
- "v40@0:8@16{CGSize=dd}24"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"WKWebView\"16@\"NSString\"24@\"WKFrameInfo\"32@?<v@?>40"
- "v48@0:8@\"WKWebView\"16@\"NSString\"24@\"WKFrameInfo\"32@?<v@?B>40"
- "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
- "v48@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32@?<v@?q>40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v56@0:8@\"WKWebView\"16@\"NSString\"24@\"NSString\"32@\"WKFrameInfo\"40@?<v@?@\"NSString\">48"
- "v56@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32q40@?<v@?q>48"
- "v56@0:8@16@24@32q40@?48"
- "videoId"
- "viewForZoomingInScrollView:"
- "webView:commitPreviewingViewController:"
- "webView:contextMenuConfigurationForElement:completionHandler:"
- "webView:contextMenuDidEndForElement:"
- "webView:contextMenuForElement:willCommitWithAnimator:"
- "webView:contextMenuWillPresentForElement:"
- "webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:"
- "webView:insertInputSuggestion:"
- "webView:previewingViewControllerForElement:defaultActions:"
- "webView:requestDeviceOrientationAndMotionPermissionForOrigin:initiatedByFrame:decisionHandler:"
- "webView:requestMediaCapturePermissionForOrigin:initiatedByFrame:type:decisionHandler:"
- "webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:"
- "webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:"
- "webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:completionHandler:"
- "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
- "webView:shouldPreviewElement:"
- "webView:showLockdownModeFirstUseMessage:completionHandler:"
- "webView:willDismissEditMenuWithAnimator:"
- "webView:willPresentEditMenuWithAnimator:"
- "webViewDidClose:"
- "window.parameters = %@;"
- "youTubePlayer:didChangeToFullScreen:"
- "youTubePlayer:didChangeToState:"
- "youTubePlayer:didReceiveError:"
- "youTubePlayerDidBecomeReady:"
- "youTubeVideoComponentsForVideoURL:"

```
