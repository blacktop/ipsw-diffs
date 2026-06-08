## TransparencyDetailsView

> `/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView`

```diff

-637.5.1.0.0
-  __TEXT.__text: 0x91bc
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x8ac
+638.0.7.0.0
+  __TEXT.__text: 0x8634
+  __TEXT.__objc_methlist: 0x8b8
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xbef
+  __TEXT.__cstring: 0xbfa
   __TEXT.__ustring: 0x88
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x23a4
-  __TEXT.__objc_methtype: 0x559
-  __TEXT.__objc_stubs: 0x1e40
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x990
+  __DATA_CONST.__objc_selrefs: 0x998
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x1d0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x9e0
-  __AUTH_CONST.__objc_const: 0x19f8
+  __AUTH_CONST.__objc_const: 0x1a40
   __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0xac
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B12F7470-F220-35F9-B4F2-98732EFF4464
+  UUID: 35380876-E3EC-3D1A-BDAD-F7C2D6010093
   Functions: 161
   Symbols:   809
-  CStrings:  589
+  CStrings:  162
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x28
Functions:
~ -[UserTransparencyViewController _currentTextSizeValue] : 120 -> 100
~ -[UserTransparencyViewController _commonInit] : 340 -> 336
~ ___45-[UserTransparencyViewController _commonInit]_block_invoke : 188 -> 184
~ -[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:] : 416 -> 404
~ ___86-[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:]_block_invoke : 220 -> 216
~ ___86-[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:]_block_invoke_2 : 500 -> 468
~ ___86-[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:]_block_invoke_3 : 688 -> 636
~ -[UserTransparencyViewController presentViewDelegate] : 144 -> 136
~ -[UserTransparencyViewController errorDelegate] : 212 -> 200
~ -[UserTransparencyViewController _showErrorMessage:] : 876 -> 796
~ -[UserTransparencyViewController webView:didFinishNavigation:] : 88 -> 92
~ -[UserTransparencyViewController webView:didFailNavigation:withError:] : 80 -> 76
~ -[UserTransparencyViewController webView:didFailProvisionalNavigation:withError:] : 80 -> 76
~ -[UserTransparencyViewController _hideErrorMessage] : 128 -> 120
~ -[UserTransparencyViewController _closeViewController:] : 164 -> 160
~ ___55-[UserTransparencyViewController _closeViewController:]_block_invoke : 160 -> 152
~ -[UserTransparencyViewController immediatelyLoadViewControllerBeforeNetworkRequest] : 2868 -> 2584
~ -[UserTransparencyViewController loadWebView] : 404 -> 376
~ -[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 1252 -> 1168
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke : 160 -> 152
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_2 : 160 -> 152
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_3 : 128 -> 124
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_4 : 160 -> 152
~ -[UserTransparencyViewController _reportUserTransparencyViewControllerEventWithType:withCompletionHandler:] : 204 -> 212
~ ___107-[UserTransparencyViewController _reportUserTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke : 900 -> 864
~ ___107-[UserTransparencyViewController _reportUserTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke_2 : 336 -> 328
~ -[UserTransparencyViewController normalizeChineseLanguage:] : 240 -> 232
~ -[UserTransparencyViewController delegate] : 16 -> 20
~ -[UserTransparencyViewController setDelegate:] : 80 -> 20
~ -[UserTransparencyViewController userTransparencyDetails] : 16 -> 20
~ -[UserTransparencyViewController userTransparencyResponseData] : 16 -> 20
~ -[UserTransparencyViewController setUserTransparencyResponseData:] : 80 -> 20
~ -[UserTransparencyViewController userTransparencyDetailsUnavailableMessage] : 16 -> 20
~ -[UserTransparencyViewController setUserTransparencyDetailsUnavailableMessage:] : 80 -> 20
~ -[UserTransparencyViewController userTransparencyRendererPayload] : 16 -> 20
~ -[UserTransparencyViewController setUserTransparencyRendererPayload:] : 80 -> 20
~ -[UserTransparencyViewController userTransparencyRendererURL] : 16 -> 20
~ -[UserTransparencyViewController setUserTransparencyRendererURL:] : 80 -> 20
~ -[UserTransparencyViewController renderingStatusForPAPermission] : 16 -> 20
~ -[UserTransparencyViewController errorLabel] : 16 -> 20
~ -[UserTransparencyViewController setErrorLabel:] : 80 -> 20
~ -[UserTransparencyViewController transparencyNavBar] : 16 -> 20
~ -[UserTransparencyViewController setTransparencyNavBar:] : 80 -> 20
~ -[UserTransparencyViewController myUserPrivacyWebView] : 16 -> 20
~ -[UserTransparencyViewController setMyUserPrivacyWebView:] : 80 -> 20
~ -[UserTransparencyViewController isiPad] : 16 -> 20
~ -[UserTransparencyViewController setIsiPad:] : 16 -> 20
~ -[NewsTransparencyViewController initWithNewsTransparencyDetailsDictionary:] : 412 -> 396
~ ___76-[NewsTransparencyViewController initWithNewsTransparencyDetailsDictionary:]_block_invoke_2 : 212 -> 208
~ ___76-[NewsTransparencyViewController initWithNewsTransparencyDetailsDictionary:]_block_invoke_3 : 160 -> 152
~ -[NewsTransparencyViewController _currentTextSizeValue] : 120 -> 100
~ -[NewsTransparencyViewController viewDidLoad] : 448 -> 416
~ -[NewsTransparencyViewController _commonInit] : 1592 -> 1496
~ -[NewsTransparencyViewController loadWebView] : 1720 -> 1540
~ -[NewsTransparencyViewController _showErrorMessage:] : 836 -> 760
~ -[NewsTransparencyViewController webView:didFinishNavigation:] : 184 -> 180
~ -[NewsTransparencyViewController webView:didFailNavigation:withError:] : 80 -> 76
~ -[NewsTransparencyViewController webView:didFailProvisionalNavigation:withError:] : 80 -> 76
~ -[NewsTransparencyViewController _hideErrorMessage] : 128 -> 120
~ -[NewsTransparencyViewController _closeViewController:] : 76 -> 72
~ -[NewsTransparencyViewController presentViewDelegate] : 156 -> 148
~ -[NewsTransparencyViewController errorDelegate] : 212 -> 200
~ -[NewsTransparencyViewController viewDidAppear:] : 328 -> 324
~ -[NewsTransparencyViewController viewDidDisappear:] : 220 -> 204
~ -[NewsTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 1892 -> 1924
~ ___90-[NewsTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke : 160 -> 152
~ ___90-[NewsTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_2 : 128 -> 124
~ -[NewsTransparencyViewController displayDebugButtonWaitingIndicator] : 208 -> 200
~ -[NewsTransparencyViewController debugDetailsViewControllerReady:] : 176 -> 180
~ -[NewsTransparencyViewController _openDebugView:] : 136 -> 140
~ -[NewsTransparencyViewController delegate] : 16 -> 20
~ -[NewsTransparencyViewController setDelegate:] : 80 -> 20
~ -[NewsTransparencyViewController transparencyDetailsUnavailableMessage] : 16 -> 20
~ -[NewsTransparencyViewController transparencyRendererPayload] : 16 -> 20
~ -[NewsTransparencyViewController transparencyRendererURL] : 16 -> 20
~ -[NewsTransparencyViewController renderingStatusForLocationPermission] : 16 -> 20
~ -[NewsTransparencyViewController renderingStatusForPAPermission] : 16 -> 20
~ -[NewsTransparencyViewController transparencyDetailsDictionary] : 16 -> 20
~ -[NewsTransparencyViewController setTransparencyDetailsDictionary:] : 80 -> 20
~ -[NewsTransparencyViewController errorLabel] : 16 -> 20
~ -[NewsTransparencyViewController setErrorLabel:] : 80 -> 20
~ -[NewsTransparencyViewController myNewsPrivacyWebView] : 16 -> 20
~ -[NewsTransparencyViewController setMyNewsPrivacyWebView:] : 80 -> 20
~ -[NewsTransparencyViewController isiPad] : 16 -> 20
~ -[NewsTransparencyViewController setIsiPad:] : 16 -> 20
~ -[NewsTransparencyViewController isClientTodayWidget] : 16 -> 20
~ -[NewsTransparencyViewController setIsClientTodayWidget:] : 16 -> 20
~ -[NewsTransparencyViewController notificationObserver] : 16 -> 20
~ -[NewsTransparencyViewController setNotificationObserver:] : 80 -> 20
~ -[TDVHomeButtonHandler startConsumingHardwarePresses:] : 176 -> 164
~ -[TDVHomeButtonHandler stopConsumingHardwarePresses] : 80 -> 76
~ -[TDVHomeButtonHandler setHomeButtonAssertion:] : 64 -> 12
~ -[ADTransparencyViewController _currentTextSizeValue] : 120 -> 100
~ -[ADTransparencyViewController viewDidAppear:] : 328 -> 324
~ -[ADTransparencyViewController viewDidDisappear:] : 156 -> 148
~ -[ADTransparencyViewController requestViewWithTransparencyDetails:] : 424 -> 416
~ -[ADTransparencyViewController preferredInterfaceOrientationForPresentation] : 68 -> 64
~ -[ADTransparencyViewController _commonInit] : 1700 -> 1544
~ -[ADTransparencyViewController configureWebView] : 1616 -> 1460
~ -[ADTransparencyViewController renderWebView] : 832 -> 756
~ -[ADTransparencyViewController presentViewDelegate] : 144 -> 136
~ -[ADTransparencyViewController errorDelegate] : 212 -> 200
~ -[ADTransparencyViewController _closeViewController:] : 164 -> 160
~ ___53-[ADTransparencyViewController _closeViewController:]_block_invoke : 160 -> 152
~ -[ADTransparencyViewController _showErrorMessage:] : 1008 -> 912
~ -[ADTransparencyViewController webView:didFinishNavigation:] : 96 -> 100
~ -[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 1956 -> 1892
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke : 160 -> 152
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_2 : 160 -> 152
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_3 : 128 -> 124
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_4 : 160 -> 152
~ -[ADTransparencyViewController webView:didFailNavigation:withError:] : 80 -> 76
~ -[ADTransparencyViewController webView:didFailProvisionalNavigation:withError:] : 80 -> 76
~ -[ADTransparencyViewController _hideErrorMessage] : 128 -> 120
~ -[ADTransparencyViewController _reportTransparencyViewControllerEventWithType:withCompletionHandler:] : 204 -> 212
~ ___101-[ADTransparencyViewController _reportTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke : 900 -> 864
~ ___101-[ADTransparencyViewController _reportTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke_2 : 336 -> 328
~ -[ADTransparencyViewController _postDismissedNotification] : 152 -> 144
~ -[ADTransparencyViewController delegate] : 16 -> 20
~ -[ADTransparencyViewController setDelegate:] : 80 -> 20
~ -[ADTransparencyViewController transparencyDetailsUnavailableMessage] : 16 -> 20
~ -[ADTransparencyViewController transparencyRendererPayload] : 16 -> 20
~ -[ADTransparencyViewController transparencyRendererURL] : 16 -> 20
~ -[ADTransparencyViewController renderingStatusForLocationPermission] : 16 -> 20
~ -[ADTransparencyViewController renderingStatusForPAPermission] : 16 -> 20
~ -[ADTransparencyViewController transparencyDetails] : 16 -> 20
~ -[ADTransparencyViewController transparencyDetailsData] : 16 -> 20
~ -[ADTransparencyViewController setTransparencyDetailsData:] : 80 -> 20
~ -[ADTransparencyViewController errorLabel] : 16 -> 20
~ -[ADTransparencyViewController setErrorLabel:] : 80 -> 20
~ -[ADTransparencyViewController myWebView] : 16 -> 20
~ -[ADTransparencyViewController setMyWebView:] : 80 -> 20
~ -[ADTransparencyViewController transparencyNavBar] : 16 -> 20
~ -[ADTransparencyViewController setTransparencyNavBar:] : 80 -> 20
~ -[ADTransparencyViewController isiPad] : 16 -> 20
~ -[ADTransparencyViewController setIsiPad:] : 16 -> 20
~ -[ADTransparencyViewController notificationObserver] : 16 -> 20
~ -[ADTransparencyViewController setNotificationObserver:] : 80 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<ADTransparencyViewControllerDelegate>\""
- "@\"<BSInvalidatable>\""
- "@\"<NewsTransparencyViewControllerDelegate>\""
- "@\"<UserTransparencyViewControllerDelegate>\""
- "@\"ADUserTransparencyResponse\""
- "@\"NSDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"UIActivityIndicatorView\""
- "@\"UIBarButtonItem\""
- "@\"UILabel\""
- "@\"UINavigationBar\""
- "@\"UIViewController\""
- "@\"WKWebView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "ADTransparencyViewController"
- "AD_jsonString"
- "AD_toServerTime"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DSID"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "NewsTransparencyViewController"
- "Q16@0:8"
- "SBSHardwareButtonEventConsuming"
- "T#,R"
- "T@\"<ADTransparencyViewControllerDelegate>\",&,N,V_delegate"
- "T@\"<BSInvalidatable>\",&,N,V_homeButtonAssertion"
- "T@\"<NewsTransparencyViewControllerDelegate>\",&,N,V_delegate"
- "T@\"<UserTransparencyViewControllerDelegate>\",&,N,V_delegate"
- "T@\"ADUserTransparencyResponse\",&,N,V_userTransparencyResponseData"
- "T@\"NSDictionary\",&,N,V_transparencyDetailsData"
- "T@\"NSDictionary\",&,N,V_transparencyDetailsDictionary"
- "T@\"NSString\",&,N,V_userTransparencyDetailsUnavailableMessage"
- "T@\"NSString\",&,N,V_userTransparencyRendererPayload"
- "T@\"NSString\",&,N,V_userTransparencyRendererURL"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_transparencyDetails"
- "T@\"NSString\",C,N,V_userTransparencyDetails"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_transparencyDetailsUnavailableMessage"
- "T@\"NSString\",R,N,V_transparencyRendererPayload"
- "T@\"NSString\",R,N,V_transparencyRendererURL"
- "T@\"UILabel\",&,N,V_errorLabel"
- "T@\"UINavigationBar\",&,N,V_transparencyNavBar"
- "T@\"WKWebView\",&,N,V_myNewsPrivacyWebView"
- "T@\"WKWebView\",&,N,V_myUserPrivacyWebView"
- "T@\"WKWebView\",&,N,V_myWebView"
- "T@,&,N,V_notificationObserver"
- "T@?,C,N,V_homeButtonHandlerCallback"
- "TB,N,V_isClientTodayWidget"
- "TB,N,V_isiPad"
- "TB,R,N,V_renderingStatusForLocationPermission"
- "TB,R,N,V_renderingStatusForPAPermission"
- "TDVHomeButtonHandler"
- "TQ,R"
- "URL"
- "URLWithString:"
- "UserTransparencyViewController"
- "Vv16@0:8"
- "WKNavigationDelegate"
- "^{_NSZone=}16@0:8"
- "_closeViewController:"
- "_commonInit"
- "_currentTextSizeValue"
- "_delegate"
- "_errorLabel"
- "_hideErrorMessage"
- "_homeButtonAssertion"
- "_homeButtonHandlerCallback"
- "_isClientTodayWidget"
- "_isiPad"
- "_myNewsPrivacyWebView"
- "_myUserPrivacyWebView"
- "_myWebView"
- "_notificationObserver"
- "_openDebugView:"
- "_postDismissedNotification"
- "_renderingStatusForLocationPermission"
- "_renderingStatusForPAPermission"
- "_reportTransparencyViewControllerEventWithType:withCompletionHandler:"
- "_reportUserTransparencyViewControllerEventWithType:withCompletionHandler:"
- "_showErrorMessage:"
- "_transparencyDetails"
- "_transparencyDetailsData"
- "_transparencyDetailsDictionary"
- "_transparencyDetailsUnavailableMessage"
- "_transparencyNavBar"
- "_transparencyRendererPayload"
- "_transparencyRendererURL"
- "_userTransparencyDetails"
- "_userTransparencyDetailsUnavailableMessage"
- "_userTransparencyRendererPayload"
- "_userTransparencyRendererURL"
- "_userTransparencyResponseData"
- "absoluteString"
- "activateConstraints:"
- "activeDSIDRecord"
- "activityIndicator"
- "adTransparencyViewController:didFailWithError:"
- "adTransparencyViewControllerDidDismiss:"
- "adTransparencyViewControllerDidLoad:"
- "addConstraints:"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "addOperationWithBlock:"
- "addSubview:"
- "addUserScript:"
- "array"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "authorizationStatus"
- "autorelease"
- "beginConsumingPressesForButtonKind:eventConsumer:priority:"
- "boolValue"
- "bottomAnchor"
- "bundleForClass:"
- "bundleIdentifier"
- "class"
- "code"
- "componentsWithString:"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "configureWebView"
- "configureWithOpaqueBackground"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "consumeAnyPressEventForButtonKind:"
- "consumeDoublePressDownForButtonKind:"
- "consumeDoublePressUpForButtonKind:"
- "consumeLongPressForButtonKind:"
- "consumeSinglePressDownForButtonKind:"
- "consumeSinglePressUpForButtonKind:"
- "consumeStateChange:forButtonKind:"
- "consumeTriplePressUpForButtonKind:"
- "containsString:"
- "countByEnumeratingWithState:objects:count:"
- "currentTraitCollection"
- "dataUsingEncoding:"
- "date"
- "debugDescription"
- "debugDetailsViewControllerReady:"
- "debugViewController"
- "defaultCenter"
- "defaultServerURL"
- "defaultWorkspace"
- "delegate"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "dismissViewControllerAnimated:completion:"
- "displayDebugButtonWaitingIndicator"
- "encryptedIDForClientType:"
- "errorDelegate"
- "errorWithDomain:code:userInfo:"
- "frame"
- "handleRequest:serverURL:responseHandler:"
- "handlerWithCompletion:"
- "hasPrefix:"
- "hash"
- "homeButtonAssertion"
- "homeButtonHandlerCallback"
- "iTunesStorefront"
- "immediatelyLoadViewControllerBeforeNetworkRequest"
- "init"
- "initWithActivityIndicatorStyle:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBase64EncodedString:options:"
- "initWithCompletion:"
- "initWithCustomView:"
- "initWithData:"
- "initWithFrame:"
- "initWithFrame:configuration:"
- "initWithNewsTransparencyDetailsDictionary:"
- "initWithNibName:bundle:"
- "initWithSource:injectionTime:forMainFrameOnly:"
- "initWithTitle:"
- "initWithTitle:style:target:action:"
- "initWithTransparencyDetails:"
- "initWithURL:"
- "initWithUserTransparencyDetails:"
- "invalidate"
- "isClientTodayWidget"
- "isDeviceLocked"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPersonalizedAdsEnabled"
- "isProxy"
- "isiPad"
- "labelColor"
- "lastPathComponent"
- "leftAnchor"
- "leftButton"
- "loadIDs"
- "loadRequest:"
- "loadWebView"
- "localeIdentifier"
- "localeWithLocaleIdentifier:"
- "localizedStringForKey:value:table:"
- "localizedStringForKey:value:table:localization:"
- "mainBundle"
- "myNewsPrivacyWebView"
- "myUserPrivacyWebView"
- "myWebView"
- "name"
- "navigationBar"
- "navigationController"
- "navigationItem"
- "navigationType"
- "newsTransparencyViewController:didFailWithError:"
- "newsTransparencyViewControllerDidDismiss:"
- "newsTransparencyViewControllerDidLinkOut:"
- "newsTransparencyViewControllerDidLoad:"
- "newsTransparencyViewControllerDidRenderView:"
- "normalizeChineseLanguage:"
- "notificationObserver"
- "numberWithBool:"
- "objectForKey:"
- "openSensitiveURL:withOptions:"
- "openURL:options:completionHandler:"
- "osIdentifier"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personalizedAds"
- "popoverPresentationController"
- "postNotificationName:object:"
- "preferredContentSizeCategory"
- "preferredFontForTextStyle:"
- "preferredInterfaceOrientationForPresentation"
- "prepareRenderingPayload"
- "presentInNavigationStack:"
- "presentViewController:animated:completion:"
- "presentViewDelegate"
- "presenterForPrivacySplashWithIdentifier:"
- "presentingViewController"
- "q16@0:8"
- "queryItemWithName:value:"
- "queryItems"
- "rangeOfString:options:"
- "regionCode"
- "release"
- "reloadStorefront:"
- "removeFromSuperview"
- "removeObserver:"
- "renderWebView"
- "renderingStatusForLocationPermission"
- "renderingStatusForPAPermission"
- "request"
- "requestUserPassCodeUnlockUIWithBlock:"
- "requestUserTransparencyDetailsWithCompletionHandler:"
- "requestViewWithTransparencyDetails:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rightAnchor"
- "scrollView"
- "self"
- "setAccessibilityLabel:"
- "setAdjustsFontForContentSizeCategory:"
- "setAllowsLinkPreview:"
- "setAutoresizesSubviews:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBarButtonItem:"
- "setBounces:"
- "setBundleID:"
- "setCenter:"
- "setColor:"
- "setContentInsetAdjustmentBehavior:"
- "setContentiAdID:"
- "setDPID:"
- "setDelegate:"
- "setEdgesForExtendedLayout:"
- "setErrorLabel:"
- "setEvent:"
- "setEvents:"
- "setFont:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHidden:"
- "setHomeButtonAssertion:"
- "setHomeButtonHandlerCallback:"
- "setIAdID:"
- "setITunesStore:"
- "setIsClientTodayWidget:"
- "setIsSignedInToiTunes:"
- "setIsiPad:"
- "setItems:"
- "setLeftBarButtonItem:"
- "setLimitAdTracking:"
- "setLocaleIdentifier:"
- "setModalPresentationStyle:"
- "setModalTransitionStyle:"
- "setMyNewsPrivacyWebView:"
- "setMyUserPrivacyWebView:"
- "setMyWebView:"
- "setNavigationDelegate:"
- "setNotificationObserver:"
- "setNumberOfLines:"
- "setOpaque:"
- "setPresentingViewController:"
- "setQueryItems:"
- "setScrollEdgeAppearance:"
- "setScrollEnabled:"
- "setStandardAppearance:"
- "setStyle:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTimestamp:"
- "setTintColor:"
- "setTitle:"
- "setTitleTextAttributes:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setTranslucent:"
- "setTransparencyDetails:"
- "setTransparencyDetailsData:"
- "setTransparencyDetailsDictionary:"
- "setTransparencyNavBar:"
- "setUserContentController:"
- "setUserTransparencyDetails:"
- "setUserTransparencyDetailsUnavailableMessage:"
- "setUserTransparencyRendererPayload:"
- "setUserTransparencyRendererURL:"
- "setUserTransparencyResponseData:"
- "setValue:forKey:"
- "sharedApplication"
- "sharedInstance"
- "shortBuildVersion"
- "shortModelType"
- "sizeToFit"
- "startAnimating"
- "startConsumingHardwarePresses:"
- "statusBarOrientation"
- "stopAnimating"
- "stopConsumingHardwarePresses"
- "storefrontLocalizationLanguage"
- "stringWithFormat:"
- "superclass"
- "systemBackgroundColor"
- "systemBlueColor"
- "systemFontOfSize:"
- "systemGrayColor"
- "topAnchor"
- "transparencyDetails"
- "transparencyDetailsData"
- "transparencyDetailsDictionary"
- "transparencyNavBar"
- "userInterfaceStyle"
- "userTransparencyDetails"
- "userTransparencyDetailsUnavailableMessage"
- "userTransparencyRendererPayload"
- "userTransparencyRendererURL"
- "userTransparencyResponseData"
- "userTransparencyViewController:didFailWithError:"
- "userTransparencyViewControllerDidDismiss:"
- "userTransparencyViewControllerDidLoad:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"WKWebView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@\"WKWebView\"16@\"WKNavigation\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16q24"
- "v40@0:8@\"WKWebView\"16@\"NSURLAuthenticationChallenge\"24@?<v@?B>32"
- "v40@0:8@\"WKWebView\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigation\"24@\"NSError\"32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@\"WKDownload\"32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@?<v@?q>32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationResponse\"24@\"WKDownload\"32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationResponse\"24@?<v@?q>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@\"WKWebpagePreferences\"32@?<v@?q@\"WKWebpagePreferences\">40"
- "v48@0:8@16@24@32@?40"
- "value"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "webView:authenticationChallenge:shouldAllowDeprecatedTLS:"
- "webView:decidePolicyForNavigationAction:decisionHandler:"
- "webView:decidePolicyForNavigationAction:preferences:decisionHandler:"
- "webView:decidePolicyForNavigationResponse:decisionHandler:"
- "webView:didCommitNavigation:"
- "webView:didFailNavigation:withError:"
- "webView:didFailProvisionalNavigation:withError:"
- "webView:didFinishNavigation:"
- "webView:didReceiveAuthenticationChallenge:completionHandler:"
- "webView:didReceiveServerRedirectForProvisionalNavigation:"
- "webView:didStartProvisionalNavigation:"
- "webView:navigationAction:didBecomeDownload:"
- "webView:navigationResponse:didBecomeDownload:"
- "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "webViewWebContentProcessDidTerminate:"
- "whiteColor"
- "workQueue"
- "zone"

```
