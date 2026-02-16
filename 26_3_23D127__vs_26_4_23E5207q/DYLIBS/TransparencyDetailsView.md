## TransparencyDetailsView

> `/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView`

```diff

-637.2.3.0.0
-  __TEXT.__text: 0x83a0
+637.4.6.0.0
+  __TEXT.__text: 0x8ff8
   __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_methlist: 0x884
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0xb91
   __TEXT.__ustring: 0x88
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0xb9
   __TEXT.__objc_methname: 0x2371
   __TEXT.__objc_methtype: 0x559

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07BA487A-140B-3200-814D-13A8D4BE1ACC
+  UUID: 6A06980A-7342-37F1-8947-1322839C3D33
   Functions: 158
   Symbols:   800
   CStrings:  587
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x9
Functions:
~ -[UserTransparencyViewController _commonInit] : 328 -> 340
~ ___45-[UserTransparencyViewController _commonInit]_block_invoke : 184 -> 188
~ -[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:] : 404 -> 416
~ ___86-[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:]_block_invoke : 232 -> 220
~ ___86-[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:]_block_invoke_2 : 460 -> 500
~ ___86-[UserTransparencyViewController requestUserTransparencyDetailsWithCompletionHandler:]_block_invoke_3 : 636 -> 688
~ -[UserTransparencyViewController presentViewDelegate] : 136 -> 144
~ -[UserTransparencyViewController errorDelegate] : 200 -> 212
~ -[UserTransparencyViewController _showErrorMessage:] : 792 -> 876
~ -[UserTransparencyViewController webView:didFailNavigation:withError:] : 76 -> 80
~ -[UserTransparencyViewController webView:didFailProvisionalNavigation:withError:] : 76 -> 80
~ -[UserTransparencyViewController _hideErrorMessage] : 120 -> 128
~ -[UserTransparencyViewController _closeViewController:] : 160 -> 164
~ ___55-[UserTransparencyViewController _closeViewController:]_block_invoke : 152 -> 160
~ -[UserTransparencyViewController immediatelyLoadViewControllerBeforeNetworkRequest] : 2548 -> 2832
~ -[UserTransparencyViewController loadWebView] : 376 -> 404
~ -[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 1168 -> 1252
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke : 152 -> 160
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_2 : 152 -> 160
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_3 : 124 -> 128
~ ___90-[UserTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_4 : 152 -> 160
~ -[UserTransparencyViewController _reportUserTransparencyViewControllerEventWithType:withCompletionHandler:] : 212 -> 204
~ ___107-[UserTransparencyViewController _reportUserTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke : 864 -> 900
~ ___107-[UserTransparencyViewController _reportUserTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke_2 : 328 -> 336
~ -[UserTransparencyViewController normalizeChineseLanguage:] : 232 -> 240
~ -[UserTransparencyViewController setDelegate:] : 20 -> 80
~ -[UserTransparencyViewController setUserTransparencyResponseData:] : 20 -> 80
~ -[UserTransparencyViewController setUserTransparencyDetailsUnavailableMessage:] : 20 -> 80
~ -[UserTransparencyViewController setUserTransparencyRendererPayload:] : 20 -> 80
~ -[UserTransparencyViewController setUserTransparencyRendererURL:] : 20 -> 80
~ -[UserTransparencyViewController setErrorLabel:] : 20 -> 80
~ -[UserTransparencyViewController setTransparencyNavBar:] : 20 -> 80
~ -[UserTransparencyViewController setMyUserPrivacyWebView:] : 20 -> 80
~ -[NewsTransparencyViewController initWithNewsTransparencyDetailsDictionary:] : 396 -> 412
~ ___76-[NewsTransparencyViewController initWithNewsTransparencyDetailsDictionary:]_block_invoke_2 : 208 -> 212
~ ___76-[NewsTransparencyViewController initWithNewsTransparencyDetailsDictionary:]_block_invoke_3 : 152 -> 160
~ -[NewsTransparencyViewController viewDidLoad] : 416 -> 448
~ -[NewsTransparencyViewController _commonInit] : 1444 -> 1564
~ -[NewsTransparencyViewController loadWebView] : 1540 -> 1720
~ -[NewsTransparencyViewController _showErrorMessage:] : 756 -> 836
~ -[NewsTransparencyViewController webView:didFinishNavigation:] : 176 -> 184
~ -[NewsTransparencyViewController webView:didFailNavigation:withError:] : 76 -> 80
~ -[NewsTransparencyViewController webView:didFailProvisionalNavigation:withError:] : 76 -> 80
~ -[NewsTransparencyViewController _hideErrorMessage] : 120 -> 128
~ -[NewsTransparencyViewController _closeViewController:] : 72 -> 76
~ -[NewsTransparencyViewController presentViewDelegate] : 148 -> 156
~ -[NewsTransparencyViewController errorDelegate] : 200 -> 212
~ -[NewsTransparencyViewController viewDidAppear:] : 324 -> 328
~ -[NewsTransparencyViewController viewDidDisappear:] : 204 -> 220
~ -[NewsTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 1920 -> 1892
~ ___90-[NewsTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke : 152 -> 160
~ ___90-[NewsTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_2 : 124 -> 128
~ -[NewsTransparencyViewController displayDebugButtonWaitingIndicator] : 200 -> 208
~ -[NewsTransparencyViewController debugDetailsViewControllerReady:] : 172 -> 176
~ -[NewsTransparencyViewController _openDebugView:] : 132 -> 136
~ -[NewsTransparencyViewController setDelegate:] : 20 -> 80
~ -[NewsTransparencyViewController setTransparencyDetailsDictionary:] : 20 -> 80
~ -[NewsTransparencyViewController setErrorLabel:] : 20 -> 80
~ -[NewsTransparencyViewController setMyNewsPrivacyWebView:] : 20 -> 80
~ -[NewsTransparencyViewController setNotificationObserver:] : 20 -> 80
~ -[TDVHomeButtonHandler startConsumingHardwarePresses:] : 164 -> 176
~ -[TDVHomeButtonHandler stopConsumingHardwarePresses] : 76 -> 80
~ -[TDVHomeButtonHandler setHomeButtonAssertion:] : 12 -> 64
~ -[ADTransparencyViewController viewDidAppear:] : 324 -> 328
~ -[ADTransparencyViewController viewDidDisappear:] : 148 -> 156
~ -[ADTransparencyViewController requestViewWithTransparencyDetails:] : 412 -> 424
~ -[ADTransparencyViewController preferredInterfaceOrientationForPresentation] : 64 -> 68
~ -[ADTransparencyViewController _commonInit] : 1544 -> 1700
~ -[ADTransparencyViewController prepareRenderingPayload] : 428 -> 456
~ -[ADTransparencyViewController configureWebView] : 1432 -> 1588
~ -[ADTransparencyViewController renderWebView] : 756 -> 832
~ -[ADTransparencyViewController presentViewDelegate] : 136 -> 144
~ -[ADTransparencyViewController errorDelegate] : 200 -> 212
~ -[ADTransparencyViewController _closeViewController:] : 160 -> 164
~ ___53-[ADTransparencyViewController _closeViewController:]_block_invoke : 152 -> 160
~ -[ADTransparencyViewController _showErrorMessage:] : 908 -> 1008
~ -[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 1884 -> 1956
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke : 152 -> 160
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_2 : 152 -> 160
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_3 : 124 -> 128
~ ___88-[ADTransparencyViewController webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_4 : 152 -> 160
~ -[ADTransparencyViewController webView:didFailNavigation:withError:] : 76 -> 80
~ -[ADTransparencyViewController webView:didFailProvisionalNavigation:withError:] : 76 -> 80
~ -[ADTransparencyViewController _hideErrorMessage] : 120 -> 128
~ -[ADTransparencyViewController _reportTransparencyViewControllerEventWithType:withCompletionHandler:] : 212 -> 204
~ ___101-[ADTransparencyViewController _reportTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke : 864 -> 900
~ ___101-[ADTransparencyViewController _reportTransparencyViewControllerEventWithType:withCompletionHandler:]_block_invoke_2 : 328 -> 336
~ -[ADTransparencyViewController _postDismissedNotification] : 144 -> 152
~ -[ADTransparencyViewController setDelegate:] : 20 -> 80
~ -[ADTransparencyViewController setTransparencyDetailsData:] : 20 -> 80
~ -[ADTransparencyViewController setErrorLabel:] : 20 -> 80
~ -[ADTransparencyViewController setMyWebView:] : 20 -> 80
~ -[ADTransparencyViewController setTransparencyNavBar:] : 20 -> 80
~ -[ADTransparencyViewController setNotificationObserver:] : 20 -> 80

```
