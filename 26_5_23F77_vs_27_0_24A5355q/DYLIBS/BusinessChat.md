## BusinessChat

> `/System/Library/Frameworks/BusinessChat.framework/BusinessChat`

```diff

-30114.35.3.19.1
-  __TEXT.__text: 0x13a4c
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x1184
+30122.30.5.19.1
+  __TEXT.__text: 0x124a4
+  __TEXT.__objc_methlist: 0x1190
   __TEXT.__const: 0x698
-  __TEXT.__cstring: 0xf84
+  __TEXT.__cstring: 0xf9e
   __TEXT.__oslogstring: 0x14b2
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x430
-  __TEXT.__objc_classname: 0x3c1
-  __TEXT.__objc_methname: 0x2eae
-  __TEXT.__objc_methtype: 0xa1f
-  __TEXT.__objc_stubs: 0x29a0
-  __DATA_CONST.__got: 0x2d0
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xda0
+  __DATA_CONST.__objc_selrefs: 0xda8
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x2d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1780
-  __AUTH_CONST.__objc_const: 0x2eb0
+  __AUTH_CONST.__objc_const: 0x2eb8
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x4e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F800949A-C067-3B61-8C4F-F04B95BE3946
+  UUID: 9F18B302-4283-3179-8774-06422B7AA0CF
   Functions: 316
-  Symbols:   1588
-  CStrings:  1205
+  Symbols:   1596
+  CStrings:  483
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
Functions:
~ -[BCAuthenticationLabels initWithDictionary:] : 600 -> 524
~ -[BCAuthenticationLabels initWithTitle:subtitle:action:] : 328 -> 288
~ -[BCAuthenticationLabels encodeWithCoder:] : 136 -> 128
~ -[BCAuthenticationLabels initWithCoder:] : 248 -> 236
~ -[BCInternalAuthenticationResponse initWithDictionary:] : 1160 -> 1108
~ -[BCInternalAuthenticationResponse initWithBusinessIdentifier:groupIdentifier:credentials:error:] : 464 -> 452
~ -[BCInternalAuthenticationResponse responseMessageFor:message:] : 1040 -> 944
~ -[BCInternalAuthenticationResponse dictionaryValue] : 472 -> 464
~ -[BCInternalAuthenticationResponse error] : 84 -> 76
~ -[BCNetworkProvider init] : 152 -> 144
~ -[BCNetworkProvider performDataTaskWithRequest:completionHandler:] : 76 -> 72
~ -[BCMessageInfo initWithTitle:subtitle:style:alternateTitle:imageIdentifier:imageDescription:] : 232 -> 248
~ -[BCMessageInfo initWithDictionary:] : 828 -> 756
~ -[BCMessageInfo initWithDictionary:imageDictionary:] : 232 -> 212
~ -[BCMessageInfo style] : 56 -> 8
~ -[BCMessageInfo succinctDescription] : 84 -> 76
~ -[BCMessageInfo succinctDescriptionBuilder] : 196 -> 184
~ -[BCMessageInfo descriptionWithMultilinePrefix:] : 84 -> 76
~ -[BCMessageInfo descriptionBuilderWithMultilinePrefix:] : 296 -> 276
~ -[BCMessageInfo setTitle:] : 64 -> 12
~ -[BCMessageInfo setSubtitle:] : 64 -> 12
~ -[BCMessageInfo setAlternateTitle:] : 64 -> 12
~ -[BCMessageInfo setImageIdentifier:] : 64 -> 12
~ -[BCMessageInfo setImageDescription:] : 64 -> 12
~ -[BCMessageInfo setImage:] : 64 -> 12
~ ___66-[BCLogger mt_log_icloud_messages_apps_businessframework:version:]_block_invoke : 196 -> 188
~ +[BCLogger logEventWithName:businessURI:callToActionText:bizItemReturnedAfterAction:latency:] : 236 -> 244
~ ___93+[BCLogger logEventWithName:businessURI:callToActionText:bizItemReturnedAfterAction:latency:]_block_invoke : 300 -> 284
~ +[BCLogger logEventWithName:version:authDomain:status:] : 188 -> 200
~ ___55+[BCLogger logEventWithName:version:authDomain:status:]_block_invoke : 220 -> 212
~ -[BCWebViewController reload] : 332 -> 340
~ -[BCWebViewController updateNavigationBar] : 108 -> 104
~ -[BCWebViewController viewDidLoad] : 920 -> 860
~ -[BCWebViewController setupSubviews] : 260 -> 240
~ -[BCWebViewController setupConstraints] : 736 -> 648
~ -[BCWebViewController presentCertificatErrorForHost:] : 824 -> 744
~ -[BCWebViewController observeValueForKeyPath:ofObject:change:context:] : 508 -> 516
~ ___70-[BCWebViewController observeValueForKeyPath:ofObject:change:context:]_block_invoke : 32 -> 36
~ -[BCWebViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 580 -> 512
~ -[BCWebViewController webView:didFailProvisionalNavigation:withError:] : 1232 -> 1136
~ -[BCWebViewController webkitView] : 16 -> 20
~ -[BCWebViewController setWebkitView:] : 80 -> 20
~ -[BCWebViewController callbackURI] : 16 -> 20
~ -[BCWebViewController setCallbackURI:] : 80 -> 20
~ -[BCNativeOAuth2Response initWithToken:error:] : 392 -> 380
~ -[BCServerSideOAuth2Response initWithRedirectURI:] : 1104 -> 1048
~ -[BCServerSideOAuth2Response _initWithDictionary:] : 536 -> 460
~ -[BCServerSideOAuth2Response dictionaryValue] : 236 -> 216
~ -[BCServerSideOAuth2Response setError:] : 64 -> 12
~ +[BCOAuth2ResponseFactory makeResponseObjectWithDictionary:version:] : 908 -> 880
~ _NativeAuthStatusFromNSString : 104 -> 100
~ _ServerSideAuthStatusFromNSString : 132 -> 128
~ -[BCBrandedHeaderViewController initWithBusinessItem:isCallMenu:] : 52 -> 56
~ -[BCBrandedHeaderViewController viewWillAppear:] : 100 -> 104
~ -[BCBrandedHeaderViewController viewDidLoad] : 4508 -> 4036
~ -[BCBrandedHeaderViewController _fetchLogo] : 588 -> 520
~ ___43-[BCBrandedHeaderViewController _fetchLogo]_block_invoke : 372 -> 328
~ ___43-[BCBrandedHeaderViewController _fetchLogo]_block_invoke.26 : 556 -> 480
~ -[BCBrandedHeaderViewController businessItem] : 16 -> 20
~ -[BCBrandedHeaderViewController logoImageView] : 16 -> 20
~ -[BCBrandedHeaderViewController setLogoImageView:] : 80 -> 20
~ -[BCBrandedHeaderViewController isCallMenu] : 16 -> 20
~ -[BCBrandedHeaderViewController setIsCallMenu:] : 16 -> 20
~ -[BCMessageData initWithUrl:data:] : 692 -> 672
~ -[BCMessageData decodeData:dictionaryKey:] : 568 -> 516
~ -[BCMessageData combinedDictionary] : 232 -> 212
~ -[BCMessageData imagesArray] : 92 -> 84
~ -[BCInternalAuthenticationRequest initWithDictionary:] : 1432 -> 1352
~ -[BCInternalAuthenticationRequest encodeWithCoder:] : 176 -> 168
~ -[BCInternalAuthenticationRequest initWithCoder:] : 480 -> 412
~ -[BCInternalAuthenticationRequest dictionaryValue] : 484 -> 480
~ -[BCImageStore initWithData:] : 432 -> 368
~ -[BCImageStore generateImageDictionaryFromArray:] : 832 -> 808
~ -[BCImageStore initWithArray:] : 328 -> 276
~ -[BCImageStore initWithImages:] : 480 -> 476
~ -[BCImageStore setRawArray:] : 64 -> 12
~ -[BCImageStore setDictionary:] : 64 -> 12
~ -[BCMessage initWithData:url:messageGUID:isFromMe:] : 1840 -> 1784
~ -[BCMessage updateTitles] : 736 -> 672
~ -[BCMessage initFromOriginalMessage:rootKey:rootObject:receivedMessage:replyMessage:] : 332 -> 336
~ -[BCMessage dictionaryValue] : 624 -> 564
~ -[BCMessage url] : 500 -> 464
~ -[BCMessage encodedStringForDictionary:] : 360 -> 304
~ -[BCMessage data] : 108 -> 100
~ -[BCMessage style] : 308 -> 248
~ -[BCMessage type] : 508 -> 472
~ -[BCMessage image] : 120 -> 108
~ -[BCMessage rootKey] : 1020 -> 900
~ -[BCMessage isAnyUnknownRootKey] : 368 -> 360
~ -[BCMessage makeRootObjectWithMessageData:dictionary:imageDictionary:version:] : 476 -> 440
~ ___32-[BCMessage isAnyUnknownRootKey]_block_invoke : 364 -> 360
~ +[BCMessage defaultBubbleTitleFor:] : 888 -> 816
~ -[BCMessage setTitle:] : 64 -> 12
~ -[BCMessage setSubtitle:] : 64 -> 12
~ -[BCMessage setSummaryText:] : 64 -> 12
~ -[BCMessage setSubcaption:] : 64 -> 12
~ -[BCMessage setAccessibilityLabel:] : 64 -> 12
~ -[BCImageManager init] : 128 -> 136
~ -[BCImageManager _fetchBrandIconDataForMapItem:desiredSize:allowSmaller:completion:] : 412 -> 364
~ ___84-[BCImageManager _fetchBrandIconDataForMapItem:desiredSize:allowSmaller:completion:]_block_invoke : 276 -> 232
~ -[BCImageManager _fetchNavBarBrandIconDataForMapItem:desiredSize:allowSmaller:completion:] : 412 -> 364
~ ___90-[BCImageManager _fetchNavBarBrandIconDataForMapItem:desiredSize:allowSmaller:completion:]_block_invoke : 276 -> 232
~ _LogCategory_Daemon : 100 -> 84
~ +[BCConstants allowedAppleURNs] : 100 -> 84
~ ___31+[BCConstants allowedAppleURNs]_block_invoke : 276 -> 268
~ -[NSString normalizedBase64Encoded] : 144 -> 136
~ -[NSURL fragments] : 464 -> 448
~ +[BCServerSideOAuth2URLProvider URLProviderWithDictionary:] : 2124 -> 1908
~ -[BCServerSideOAuth2URLProvider _initWithAuthorizationURL:clientIdentifier:redirectURI:scope:state:responseType:additionalParameters:] : 304 -> 332
~ -[BCServerSideOAuth2URLProvider encodeWithCoder:] : 216 -> 208
~ -[BCServerSideOAuth2URLProvider initWithCoder:] : 508 -> 476
~ -[BCServerSideOAuth2URLProvider authenticationSessionURL] : 756 -> 732
~ -[BCServerSideOAuth2URLProvider shouldHandleRedirectURI:] : 96 -> 88
~ -[BCServerSideOAuth2URLProvider debugDescription] : 160 -> 148
~ -[BCServerSideOAuth2URLProvider setRedirectURI:] : 64 -> 12
~ +[BCChatAction openTranscript:intentParameters:] : 640 -> 628
~ ___48+[BCChatAction openTranscript:intentParameters:]_block_invoke : 316 -> 260
~ -[BCOAuth2Request _initWithDictionary:URLProvider:] : 356 -> 348
~ -[BCOAuth2Request debugDescription] : 244 -> 224
~ -[BCOAuth2Request setBusinessIdentifier:] : 64 -> 12
~ -[BCOAuth2Request setOauth2:] : 64 -> 12
~ -[BCNativeOAuth2Request _initWithDictionary:] : 436 -> 412
~ -[BCServerSideOAuth2Request _initWithDictionary:] : 436 -> 412
~ +[BCCryptor encryptData:key:completion:] : 1052 -> 1044
~ ___40+[BCCryptor encryptData:key:completion:]_block_invoke : 836 -> 808
~ -[BCServerErrorView init] : 1944 -> 1884
~ -[BCChatButton initWithStyle:] : 116 -> 120
~ -[BCChatButton setup] : 1008 -> 1028
~ -[BCChatButton initWithCoder:] : 132 -> 136
~ -[BCChatButton updateAppearanceForState:] : 492 -> 520
~ -[BCChatButton calculateButtonLayout] : 880 -> 912
~ -[BCChatButton hitTest:withEvent:] : 100 -> 96
~ -[BCChatButton viewForFirstBaselineLayout] : 76 -> 24
~ -[BCChatButton viewForLastBaselineLayout] : 76 -> 24
~ -[BCInvalidCertificatView initWithHost:] : 3584 -> 3456
~ -[BCImage initWithImageData:identifier:description:] : 172 -> 188
~ -[BCInternalAuthenticationManager initWithAuthenticationRequest:] : 220 -> 236
~ -[BCInternalAuthenticationManager fetchCredentials:] : 252 -> 248
~ ___52-[BCInternalAuthenticationManager fetchCredentials:]_block_invoke : 1580 -> 1528
~ -[BCInternalAuthenticationManager isUserSignedIn] : 64 -> 60
~ -[BCInternalAuthenticationManager title] : 420 -> 372
~ -[BCInternalAuthenticationManager labelCategory] : 112 -> 92
~ -[BCInternalAuthenticationManager subtitle] : 472 -> 420
~ -[BCInternalAuthenticationManager action] : 368 -> 328
~ -[BCAuthenticationManager initWithAuthenticationRequest:] : 108 -> 116
~ -[BCAuthenticationManager fetchTokenWithRequest:completion:] : 1676 -> 1620
~ -[BCAuthenticationManager exchangeCode:completion:] : 640 -> 564
~ ___51-[BCAuthenticationManager exchangeCode:completion:]_block_invoke : 1200 -> 1164
~ -[BCAuthenticationManager URLSession:didReceiveChallenge:completionHandler:] : 188 -> 180
~ -[BCAuthenticationManager setAuthenticationRequest:] : 64 -> 12
~ -[BCProgressIndicatorView init] : 184 -> 176
~ -[BCError initWithCode:domain:message:] : 160 -> 168
~ -[BCError initWithDictionary:] : 688 -> 640
~ -[BCError encodeWithCoder:] : 136 -> 128
~ -[BCError initWithCoder:] : 248 -> 236
~ -[BCError setCode:] : 64 -> 12
~ -[BCError setDomain:] : 64 -> 12
~ -[BCError setMessage:] : 64 -> 12
~ +[BCNativeOAuth2URLProvider URLProviderWithDictionary:] : 1968 -> 1840
~ -[BCNativeOAuth2URLProvider _initWithAuthorizationURL:accessTokenURL:clientSecret:clientIdentifier:responseEncryptionKey:scope:state:responseType:] : 340 -> 368
~ -[BCNativeOAuth2URLProvider encodeWithCoder:] : 256 -> 248
~ -[BCNativeOAuth2URLProvider initWithCoder:] : 576 -> 540
~ -[BCNativeOAuth2URLProvider authenticationSessionURL] : 640 -> 624
~ -[BCNativeOAuth2URLProvider shouldHandleRedirectURI:] : 96 -> 88
~ -[BCNativeOAuth2URLProvider tokenExchangeBodyWithCode:] : 556 -> 536
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACAccountProtocol>\""
- "@\"<ACAccountStoreProtocol>\""
- "@\"<BCBaseOAuth2Protocol>\""
- "@\"<BCBaseOAuth2Protocol>\"16@0:8"
- "@\"<BCBrandedHeaderViewControllerDelegate>\""
- "@\"<BCDictionarySerializable>\""
- "@\"<BCNetworkProviderProtocol>\""
- "@\"<BCOAuth2RequestProtocol>\""
- "@\"<BCWebViewControllerDelegate>\""
- "@\"BCError\""
- "@\"BCError\"16@0:8"
- "@\"BCImageStore\""
- "@\"BCInternalAuthenticationRequest\""
- "@\"BCInvalidCertificatView\""
- "@\"BCMessageData\""
- "@\"BCMessageInfo\""
- "@\"BCProgressIndicatorView\""
- "@\"BCSBusinessItem\""
- "@\"BCServerErrorView\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"NSArray\""
- "@\"NSAttributedString\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSURLSession\""
- "@\"NSUUID\""
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIView\""
- "@\"WKWebView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8{CGPoint=dd}16@32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32q40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40@48@56"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSURL\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "BCAuthenticationLabels"
- "BCAuthenticationManager"
- "BCBaseOAuth2Protocol"
- "BCBrandedHeaderViewController"
- "BCChatAction"
- "BCChatButton"
- "BCConstants"
- "BCCryptor"
- "BCDictionarySerializable"
- "BCError"
- "BCFeatureFlag"
- "BCImage"
- "BCImageManager"
- "BCImageManagerProtocol"
- "BCImageStore"
- "BCInternalAuthenticationManager"
- "BCInternalAuthenticationRequest"
- "BCInternalAuthenticationResponse"
- "BCInvalidCertificatView"
- "BCLogger"
- "BCMessage"
- "BCMessageData"
- "BCMessageInfo"
- "BCNativeOAuth2Protocol"
- "BCNativeOAuth2Request"
- "BCNativeOAuth2Response"
- "BCNativeOAuth2URLProvider"
- "BCNetworkProvider"
- "BCNetworkProviderProtocol"
- "BCOAuth2Request"
- "BCOAuth2RequestFactory"
- "BCOAuth2RequestProtocol"
- "BCOAuth2ResponseFactory"
- "BCOAuth2ResponseProtocol"
- "BCProgressIndicatorView"
- "BCServerErrorView"
- "BCServerSideOAuth2Request"
- "BCServerSideOAuth2Response"
- "BCServerSideOAuth2URLProvider"
- "BCShared"
- "BCWebViewController"
- "BSDescriptionProviding"
- "BrandingUI"
- "CGColor"
- "HTTPBody"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSURLSessionDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<BCBaseOAuth2Protocol>\",&,N,V_oauth2"
- "T@\"<BCBaseOAuth2Protocol>\",R,N"
- "T@\"<BCBrandedHeaderViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<BCDictionarySerializable>\",R,N"
- "T@\"<BCOAuth2RequestProtocol>\",&,N,V_authenticationRequest"
- "T@\"<BCWebViewControllerDelegate>\",W,N,V_delegate"
- "T@\"BCError\",&,N,V_error"
- "T@\"BCError\",R,N"
- "T@\"BCImageStore\",R,N"
- "T@\"BCInternalAuthenticationRequest\",R,N"
- "T@\"BCMessageData\",R,N"
- "T@\"BCMessageInfo\",R,N"
- "T@\"BCSBusinessItem\",R,N,V_businessItem"
- "T@\"NSArray\",&,N,V_rawArray"
- "T@\"NSArray\",R,N"
- "T@\"NSAttributedString\",&,N,V_subtitle"
- "T@\"NSData\",R,N"
- "T@\"NSDictionary\",&,N,V_dictionary"
- "T@\"NSDictionary\",R,N"
- "T@\"NSNumber\",&,N,V_code"
- "T@\"NSString\",&,N,V_accessibilityLabel"
- "T@\"NSString\",&,N,V_alternateTitle"
- "T@\"NSString\",&,N,V_businessIdentifier"
- "T@\"NSString\",&,N,V_callbackURI"
- "T@\"NSString\",&,N,V_domain"
- "T@\"NSString\",&,N,V_imageDescription"
- "T@\"NSString\",&,N,V_imageIdentifier"
- "T@\"NSString\",&,N,V_message"
- "T@\"NSString\",&,N,V_subcaption"
- "T@\"NSString\",&,N,V_subtitle"
- "T@\"NSString\",&,N,V_summaryText"
- "T@\"NSString\",&,N,V_title"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",&,N,V_redirectURI"
- "T@\"NSURL\",R,N"
- "T@\"NSUUID\",R,N"
- "T@\"UIImage\",&,N,V_image"
- "T@\"UIImage\",R,N"
- "T@\"UIImageView\",&,N,V_logoImageView"
- "T@\"WKWebView\",&,N,V_webkitView"
- "TB,N,V_isCallMenu"
- "TB,R"
- "TB,R,N"
- "TQ,R"
- "Tq,N,V_status"
- "Tq,R,N"
- "URL"
- "URLProviderWithDictionary:"
- "URLQueryAllowedCharacterSet"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "Vv16@0:8"
- "WKNavigationDelegate"
- "^{_NSZone=}16@0:8"
- "__style"
- "_accessTokenURL"
- "_accessibilityLabel"
- "_account"
- "_accountStore"
- "_action"
- "_additionalParameters"
- "_alternateTitle"
- "_authenticationRequest"
- "_authorizationURL"
- "_bestBrandIconURLForSize:allowSmaller:"
- "_bestNavbarBrandIconURLForSize:allowSmaller:"
- "_businessIdentifier"
- "_businessItem"
- "_callbackURI"
- "_canShowWhileLocked"
- "_centeredView"
- "_clientIdentifier"
- "_clientSecret"
- "_code"
- "_contentView"
- "_credentials"
- "_data"
- "_delegate"
- "_dictionary"
- "_domain"
- "_error"
- "_errors"
- "_fetchBrandIconDataForMapItem:desiredSize:allowSmaller:completion:"
- "_fetchLogo"
- "_fetchNavBarBrandIconDataForMapItem:desiredSize:allowSmaller:completion:"
- "_groupIdentifier"
- "_host"
- "_iconImageView"
- "_identifier"
- "_image"
- "_imageData"
- "_imageDescription"
- "_imageIdentifier"
- "_imageStore"
- "_initWithDictionary:"
- "_initWithDictionary:URLProvider:"
- "_insecureIcon"
- "_internalRootKey"
- "_invalidCertificatView"
- "_isCallMenu"
- "_isFromMe"
- "_isInverted"
- "_jsonDictionary"
- "_label"
- "_labels"
- "_logoImageView"
- "_message"
- "_messageData"
- "_messageGUID"
- "_messageLabel"
- "_networkProvider"
- "_oauth2"
- "_originURL"
- "_populateArchivedSubviews:"
- "_progressIndicatorView"
- "_rawArray"
- "_receivedMessage"
- "_receivedMessageDictionary"
- "_redirectURI"
- "_replyMessage"
- "_replyMessageDictionary"
- "_requestIdentifier"
- "_responseEncryptionKey"
- "_responseType"
- "_retrieve"
- "_rootObject"
- "_scope"
- "_serverErrorView"
- "_session"
- "_sessionIdentifier"
- "_setContinuousCornerRadius:"
- "_smallLabel"
- "_state"
- "_status"
- "_style"
- "_subcaption"
- "_subtitle"
- "_summaryText"
- "_title"
- "_titleLabel"
- "_token"
- "_url"
- "_version"
- "_wasCallbackCaptured"
- "_webkitView"
- "_webkit_decodeHostName"
- "aa_firstName"
- "aa_lastName"
- "aa_middleName"
- "aa_personID"
- "aa_primaryAppleAccount"
- "absoluteString"
- "accessibilityLabel"
- "activateConstraints:"
- "addLayoutGuide:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forKeyPath:options:context:"
- "addSubview:"
- "aida_accountForiCloudAccount:"
- "aida_alternateDSID"
- "aida_tokenForService:"
- "ak_clientInfoHeader"
- "ak_deviceUDIDHeader"
- "allKeys"
- "allowedAppleURNs"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appleIDHeadersForRequest:completion:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "authenticationRequest"
- "authenticationSessionURL"
- "autorelease"
- "base64EncodedDataWithOptions:"
- "base64EncodedStringWithOptions:"
- "baseURL"
- "bizID"
- "boldSystemFontOfSize:"
- "boolForKey:"
- "bottomAnchor"
- "bounds"
- "brandedHeaderViewController:logoFetchingDidFinishForBusinessItem:success:"
- "brandedHeaderViewController:logoFetchingWillBeginForBusinessItem:"
- "build"
- "builderWithObject:"
- "bundleForClass:"
- "bundleIdentifier"
- "businessItem"
- "callbackURI"
- "centerXAnchor"
- "centerYAnchor"
- "class"
- "colorNamed:inBundle:compatibleWithTraitCollection:"
- "colorWithRed:green:blue:alpha:"
- "combinedDictionary"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "configurationWithFont:scale:"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToAnchor:constant:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultBubbleTitleFor:"
- "defaultSessionConfiguration"
- "defaultWebpagePreferences"
- "defaultWorkspace"
- "delegate"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "dictionary"
- "dictionaryValue"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeNavigationURL:"
- "didChangeSecureStatus:"
- "didReceiveCallbackRequest:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encryptData:key:completion:"
- "ephemeralSessionConfiguration"
- "fetchBrandIconDataForMapItem:desiredSize:allowSmaller:completion:"
- "fetchCredentials:"
- "fetchNavBarBrandIconDataForMapItem:desiredSize:allowSmaller:completion:"
- "fetchSquareIconDataForBusinessItem:completion:"
- "fetchTokenWithRequest:completion:"
- "firstBaselineAnchor"
- "firstName"
- "firstObject"
- "font"
- "fontDescriptor"
- "fontDescriptorByAddingAttributes:"
- "fontWithDescriptor:size:"
- "fragment"
- "frame"
- "hasPrefix:"
- "hash"
- "heightAnchor"
- "hitTest:withEvent:"
- "host"
- "image"
- "imageData"
- "imageNamed:inBundle:"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageStore"
- "imageWithData:"
- "imageWithRenderingMode:"
- "imagesArray"
- "init"
- "initFromOriginalMessage:rootKey:rootObject:receivedMessage:replyMessage:"
- "initWithArray:"
- "initWithAuthenticationRequest:"
- "initWithBase64EncodedString:options:"
- "initWithBusinessIdentifier:groupIdentifier:credentials:error:"
- "initWithBusinessItem:"
- "initWithBusinessItem:isCallMenu:"
- "initWithCallbackURI:"
- "initWithCode:domain:message:"
- "initWithCoder:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithData:url:messageGUID:isFromMe:"
- "initWithData:url:sessionIdentifier:isFromMe:"
- "initWithDictionary:"
- "initWithDictionary:imageDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithFrame:"
- "initWithFrame:configuration:"
- "initWithIdentifier:"
- "initWithImage:"
- "initWithImageData:identifier:description:"
- "initWithImages:"
- "initWithName:value:"
- "initWithNibName:bundle:"
- "initWithObjects:"
- "initWithRedirectURI:"
- "initWithString:"
- "initWithStyle:"
- "initWithTitle:subtitle:action:"
- "initWithTitle:subtitle:style:alternateTitle:imageIdentifier:imageDescription:"
- "initWithToken:error:"
- "initWithTrust:"
- "initWithURL:"
- "initWithURL:resolvingAgainstBaseURL:"
- "initWithUrl:data:"
- "integerValue"
- "intrinsicContentSize"
- "isCallMenu"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isFeatureEnabledForFeature:"
- "isFromMe"
- "isHighlighted"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunningInMac"
- "isRunningInMacCatalyst"
- "isUserSignedIn"
- "isVerified"
- "isVersionSupported"
- "jsonDictionary"
- "labelColor"
- "lastBaselineAnchor"
- "lastName"
- "layer"
- "layoutSubviews"
- "leadingAnchor"
- "leftAnchor"
- "length"
- "loadRequest:"
- "loadURL:"
- "loadView"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "logEventWithName:businessURI:callToActionText:bizItemReturnedAfterAction:latency:"
- "logEventWithName:version:authDomain:status:"
- "logoImageView"
- "lowercaseString"
- "mainBundle"
- "makeBrandedHeaderViewController"
- "makeBrandedHeaderViewControllerForCallMenu"
- "makeRequestObjectWithDictionary:version:"
- "makeResponseObjectWithDictionary:version:"
- "makeResponseObjectWithRedirectURI:"
- "makeRootObjectWithMessageData:dictionary:imageDictionary:version:"
- "messageData"
- "messageGUID"
- "messageSubtitle"
- "metricsForTextStyle:"
- "middleName"
- "mt_log_icloud_messages_apps_businessframework:version:"
- "mutableCopy"
- "name"
- "nonPersistentDataStore"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "openTranscript:intentParameters:"
- "openURL:configuration:completionHandler:"
- "performDataTaskWithRequest:completionHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointSize"
- "preferredFontForTextStyle:"
- "presentCertificatErrorForHost:"
- "progress"
- "protectionSpace"
- "q"
- "q16@0:8"
- "query"
- "queryItems"
- "rawArray"
- "receivedMessageDictionary"
- "release"
- "reload"
- "removeFromSuperview"
- "replyMessageDictionary"
- "request"
- "respondsToSelector:"
- "responseMessageFor:message:"
- "resume"
- "retain"
- "retainCount"
- "rightAnchor"
- "rootKey"
- "rootObject"
- "scaledFontForFont:"
- "scheme"
- "secondaryLabelColor"
- "self"
- "serverTrust"
- "sessionIdentifier"
- "sessionWithConfiguration:"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAccessibilityIgnoresInvertColors:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAdjustsFontForContentSizeCategory:"
- "setAlpha:"
- "setAlternateTitle:"
- "setAuthenticationRequest:"
- "setBackgroundColor:"
- "setBorderColor:"
- "setBorderWidth:"
- "setBusinessIdentifier:"
- "setByAddingObjectsFromArray:"
- "setCallbackURI:"
- "setCode:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContentMode:"
- "setCornerRadius:"
- "setCustomUserAgent:"
- "setDelegate:"
- "setDictionary:"
- "setDomain:"
- "setEnabled:"
- "setError:"
- "setFamilyName:"
- "setFont:"
- "setFrame:"
- "setGivenName:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHidden:"
- "setHighlighted:"
- "setImage:"
- "setImageDescription:"
- "setImageIdentifier:"
- "setIsCallMenu:"
- "setLineBreakMode:"
- "setLogoImageView:"
- "setMasksToBounds:"
- "setMessage:"
- "setNavigationDelegate:"
- "setNumberOfLines:"
- "setOauth2:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPreferredContentSize:"
- "setPriority:"
- "setProgress:animated:"
- "setProgressTintColor:"
- "setQuery:"
- "setQueryItems:"
- "setRawArray:"
- "setRedirectURI:"
- "setSecurityRestrictionMode:"
- "setStatus:"
- "setStyle:"
- "setSubcaption:"
- "setSubtitle:"
- "setSummaryText:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTintColor:"
- "setTitle:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setValue:forHTTPHeaderField:"
- "setView:"
- "setWebkitView:"
- "setWebsiteDataStore:"
- "setWithObjects:"
- "setupConstraints"
- "setupSubviews"
- "shouldHandleRedirectURI:"
- "sizeToFit"
- "sizeWithAttributes:"
- "standardUserDefaults"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingString:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromPersonNameComponents:"
- "stringWithFormat:"
- "subcaption"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "summaryText"
- "superclass"
- "supportsSecureCoding"
- "systemFontOfSize:"
- "systemFontOfSize:weight:"
- "systemImageNamed:withConfiguration:"
- "text"
- "textColor"
- "tokenExchangeBodyWithCode:"
- "tokenExchangeURL"
- "topAnchor"
- "touchesBegan:withEvent:"
- "touchesEnded:withEvent:"
- "trailingAnchor"
- "type"
- "updateNavigationBar"
- "updateSize"
- "url"
- "userInfo"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@\"WKWebView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@\"NSURLRequest\"16@?<v@?@\"NSData\"@\"NSURLResponse\"@\"NSError\">24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"WKWebView\"16@\"WKNavigation\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
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
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16q24@32@40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@\"<BCMapItemProtocol>\"16{CGSize=dd}24B40@?<v@?@\"NSData\"@\"NSError\">44"
- "v52@0:8@16@24@32B40q44"
- "v52@0:8@16{CGSize=dd}24B40@?44"
- "value"
- "valueForHTTPHeaderField:"
- "valueForKeyPath:"
- "view"
- "viewDidLoad"
- "viewForFirstBaselineLayout"
- "viewForLastBaselineLayout"
- "viewWillAppear:"
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
- "webkitView"
- "widthAnchor"
- "zone"
- "{CGSize=dd}16@0:8"

```
