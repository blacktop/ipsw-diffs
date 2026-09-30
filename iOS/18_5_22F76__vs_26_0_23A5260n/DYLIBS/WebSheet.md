## WebSheet

> `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet`

```diff

-294.100.3.0.0
-  __TEXT.__text: 0x61ac
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0xb08
+308.0.0.0.2
+  __TEXT.__text: 0x6ddc
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0xbe0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1084
+  __TEXT.__cstring: 0x1337
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methname: 0x2d16
-  __TEXT.__objc_methtype: 0x102e
-  __TEXT.__objc_stubs: 0x2260
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x178
+  __TEXT.__unwind_info: 0x270
+  __TEXT.__objc_classname: 0x16a
+  __TEXT.__objc_methname: 0x327b
+  __TEXT.__objc_methtype: 0x12c1
+  __TEXT.__objc_stubs: 0x2540
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc80
+  __DATA_CONST.__objc_selrefs: 0xd90
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x1238
+  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x1328
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x360
+  __DATA.__objc_ivar: 0xd8
+  __DATA.__data: 0x3c0
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CertUI.framework/CertUI
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /System/Library/PrivateFrameworks/WebUI.framework/WebUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 087F676E-339D-3671-A3F2-60A5A2224EF4
-  Functions: 165
-  Symbols:   902
-  CStrings:  800
+  UUID: DB75950F-4B49-3E85-BD2C-D35F60148EF4
+  Functions: 176
+  Symbols:   971
+  CStrings:  874
 
Symbols:
+ -[WSWebSheetView _autoFillUserCredentialsUsingJavaScript]
+ -[WSWebSheetView _autoFocusDelayTimerFired:]
+ -[WSWebSheetView _fetchCaptivePortalCredentialsAndReturnNetworkName:deviceName:]
+ -[WSWebSheetView _populateTextSuggestionsWithCaptivePortalCredentials:networkName:deviceName:inputSession:]
+ -[WSWebSheetView _scrapeUserCredentialsUsingJavaScript]
+ -[WSWebSheetView _webView:decidePolicyForFocusedElement:]
+ -[WSWebSheetView webView:resourceLoad:didCompleteWithError:response:]
+ GCC_except_table104
+ _CWFCaptiveWebSheetJavaScriptAutoFocusFirstTextInput
+ _CWFCaptiveWebSheetJavaScriptScrapeCredentials
+ _CWFCaptiveWebSheetJavaScriptSetElementValueForSelectorNameFormat
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_UITextSuggestion
+ _OBJC_CLASS_$_WKContentWorld
+ _OBJC_IVAR_$_WSWebSheetView._autoFocusDelayTimer
+ _OBJC_IVAR_$_WSWebSheetView._corewifi
+ _OBJC_IVAR_$_WSWebSheetView._fetchedCredentials
+ _OBJC_IVAR_$_WSWebSheetView._scrapedUserCredentialsFromJavaScript
+ _WKErrorDomain
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKResourceLoadDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__WKResourceLoadDelegate
+ __OBJC_$_PROTOCOL_REFS__WKResourceLoadDelegate
+ __OBJC_LABEL_PROTOCOL_$__WKResourceLoadDelegate
+ __OBJC_PROTOCOL_$__WKResourceLoadDelegate
+ ___44-[WSWebSheetView _autoFocusDelayTimerFired:]_block_invoke
+ ___55-[WSWebSheetView _scrapeUserCredentialsUsingJavaScript]_block_invoke
+ ___57-[WSWebSheetView _autoFillUserCredentialsUsingJavaScript]_block_invoke
+ ___57-[WSWebSheetView _autoFillUserCredentialsUsingJavaScript]_block_invoke_2
+ ___block_descriptor_32_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_literal_global.120
+ ___block_literal_global.206
+ ___block_literal_global.211
+ ___block_literal_global.308
+ ___block_literal_global.346
+ ___block_literal_global.732
+ __os_feature_enabled_impl
+ _objc_msgSend$_autoFillUserCredentialsUsingJavaScript
+ _objc_msgSend$_fetchCaptivePortalCredentialsAndReturnNetworkName:deviceName:
+ _objc_msgSend$_populateTextSuggestionsWithCaptivePortalCredentials:networkName:deviceName:inputSession:
+ _objc_msgSend$_scrapeUserCredentialsUsingJavaScript
+ _objc_msgSend$_setResourceLoadDelegate:
+ _objc_msgSend$activate
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$callAsyncJavaScript:arguments:inFrame:inContentWorld:completionHandler:
+ _objc_msgSend$captivePortalCredentialsForKnownNetworkProfile:error:
+ _objc_msgSend$currentKnownNetworkProfile
+ _objc_msgSend$defaultClientWorld
+ _objc_msgSend$domain
+ _objc_msgSend$identifier
+ _objc_msgSend$inputText
+ _objc_msgSend$nearbyRecommendedNetworks
+ _objc_msgSend$networkName
+ _objc_msgSend$receivedFromDeviceName
+ _objc_msgSend$resignFirstResponder
+ _objc_msgSend$setCaptivePortalCredentials:knownNetworkProfile:error:
+ _objc_msgSend$setDisplayText:
+ _objc_msgSend$setHeaderText:
+ _objc_msgSend$setSuggestions:
+ _objc_msgSend$textSuggestionWithInputText:
+ _objc_retainAutorelease
- GCC_except_table96
- ___block_literal_global.116
- ___block_literal_global.199
- ___block_literal_global.204
- ___block_literal_global.662
CStrings:
+ "@\"CWFInterface\""
+ "@32@0:8^@16^@24"
+ "AutoFill"
+ "CoreWiFi"
+ "Could not get [CWFNetworkProfile receivedFromDeviceName] for the current known network"
+ "FAILED to auto-fill scraped captive portal value for selector, returned error (%@)"
+ "FAILED to scrape user-entered value, returned error (%@)"
+ "From %@"
+ "NearbyAutoJoinAssist"
+ "NearbyCaptiveAssist"
+ "[CWFInterface captivePortalCredentialsForKnownNetworkProfile:error:] failed, returned error (%@)"
+ "[CWFInterface currentKnownNetworkProfile] returned nil"
+ "[CWFInterface setCaptivePortalCredentials:knownNetworkProfile:error:] failed, returned error (%@)"
+ "[CWFNetworkProfile networkName] returned nil"
+ "_WKResourceLoadDelegate"
+ "_autoFillUserCredentialsUsingJavaScript"
+ "_autoFocusDelayTimer"
+ "_autoFocusDelayTimerFired:"
+ "_corewifi"
+ "_fetchCaptivePortalCredentialsAndReturnNetworkName:deviceName:"
+ "_fetchedCredentials"
+ "_populateTextSuggestionsWithCaptivePortalCredentials:networkName:deviceName:inputSession:"
+ "_scrapeUserCredentialsUsingJavaScript"
+ "_scrapedUserCredentialsFromJavaScript"
+ "_setResourceLoadDelegate:"
+ "_webView:focusRequiresStrongPasswordAssistance:completionHandler:"
+ "activate"
+ "addEntriesFromDictionary:"
+ "callAsyncJavaScript:arguments:inFrame:inContentWorld:completionHandler:"
+ "captivePortalCredentialsForKnownNetworkProfile:error:"
+ "currentKnownNetworkProfile"
+ "defaultClientWorld"
+ "dismissAutoFillInternalFeedbackActivityForFormAutoFillController:immediately:"
+ "domain"
+ "identifier"
+ "inputText"
+ "nearbyRecommendedNetworks"
+ "networkName"
+ "presentAutoFillInternalFeedbackToastForFormAutoFillController:diagnosticsDataWithoutPageContents:"
+ "receivedFromDeviceName"
+ "resetPendingAutoFillInternalFeedbackToastDismissalTimer"
+ "resignFirstResponder"
+ "setCaptivePortalCredentials:knownNetworkProfile:error:"
+ "setDisplayText:"
+ "setHeaderText:"
+ "setSuggestions:"
+ "textSuggestionWithInputText:"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v28@0:8@\"_SFFormAutoFillController\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"WKWebView\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"_SFFormAutoFillController\"16@\"WBSAutoFillInternalFeedbackDiagnosticsData\"24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v40@0:8@\"WKWebView\"16@\"<_WKFocusedElementInfo>\"24@?<v@?B>32"
+ "v40@0:8@\"WKWebView\"16@\"_WKResourceLoadInfo\"24@\"NSURLAuthenticationChallenge\"32"
+ "v40@0:8@\"WKWebView\"16@\"_WKResourceLoadInfo\"24@\"NSURLRequest\"32"
+ "v40@0:8@\"WKWebView\"16@\"_WKResourceLoadInfo\"24@\"NSURLResponse\"32"
+ "v48@0:8@\"WKWebView\"16@\"_WKResourceLoadInfo\"24@\"NSError\"32@\"NSURLResponse\"40"
+ "v48@0:8@\"WKWebView\"16@\"_WKResourceLoadInfo\"24@\"NSURLResponse\"32@\"NSURLRequest\"40"
+ "v48@0:8@16@24@32@40"
+ "webView:insertInputSuggestion:"
+ "webView:resourceLoad:didCompleteWithError:response:"
+ "webView:resourceLoad:didPerformHTTPRedirection:newRequest:"
+ "webView:resourceLoad:didReceiveChallenge:"
+ "webView:resourceLoad:didReceiveResponse:"
+ "webView:resourceLoad:didSendRequest:"
+ "\xf0\xf0q"
- "\xf0\xf0!"

```
