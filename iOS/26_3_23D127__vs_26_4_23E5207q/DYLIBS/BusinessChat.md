## BusinessChat

> `/System/Library/Frameworks/BusinessChat.framework/BusinessChat`

```diff

-30114.32.10.7.1
-  __TEXT.__text: 0x12564
-  __TEXT.__auth_stubs: 0x4c0
+30114.34.9.10.5
+  __TEXT.__text: 0x13a4c
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x1184
   __TEXT.__const: 0x698
   __TEXT.__cstring: 0xf84
   __TEXT.__oslogstring: 0x14b2
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_classname: 0x3c1
-  __TEXT.__objc_methname: 0x2e78
+  __TEXT.__objc_methname: 0x2eae
   __TEXT.__objc_methtype: 0xa1f
-  __TEXT.__objc_stubs: 0x2960
+  __TEXT.__objc_stubs: 0x29a0
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd90
+  __DATA_CONST.__objc_selrefs: 0xda0
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1780
   __AUTH_CONST.__objc_const: 0x2eb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FA92DD1-7713-3151-9146-445D363163A5
+  UUID: C80E770E-E79B-323E-A129-2EADD44C905F
   Functions: 316
-  Symbols:   1594
-  CStrings:  1203
+  Symbols:   1588
+  CStrings:  1205
 
Symbols:
+ _objc_msgSend$defaultWebpagePreferences
+ _objc_msgSend$setSecurityRestrictionMode:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- _objc_retain_x9
Functions:
~ -[BCAuthenticationLabels initWithDictionary:] : 568 -> 600
~ -[BCAuthenticationLabels initWithTitle:subtitle:action:] : 332 -> 328
~ -[BCAuthenticationLabels encodeWithCoder:] : 128 -> 136
~ -[BCAuthenticationLabels initWithCoder:] : 236 -> 248
~ -[BCInternalAuthenticationResponse initWithDictionary:] : 1104 -> 1160
~ -[BCInternalAuthenticationResponse initWithBusinessIdentifier:groupIdentifier:credentials:error:] : 452 -> 464
~ -[BCInternalAuthenticationResponse responseMessageFor:message:] : 944 -> 1040
~ -[BCInternalAuthenticationResponse dictionaryValue] : 460 -> 472
~ -[BCInternalAuthenticationResponse error] : 76 -> 84
~ -[BCNetworkProvider init] : 144 -> 152
~ -[BCNetworkProvider performDataTaskWithRequest:completionHandler:] : 72 -> 76
~ -[BCMessageInfo initWithTitle:subtitle:style:alternateTitle:imageIdentifier:imageDescription:] : 248 -> 232
~ -[BCMessageInfo initWithDictionary:] : 756 -> 828
~ -[BCMessageInfo initWithDictionary:imageDictionary:] : 212 -> 232
~ -[BCMessageInfo style] : 8 -> 56
~ -[BCMessageInfo succinctDescription] : 76 -> 84
~ -[BCMessageInfo succinctDescriptionBuilder] : 184 -> 196
~ -[BCMessageInfo descriptionWithMultilinePrefix:] : 76 -> 84
~ -[BCMessageInfo descriptionBuilderWithMultilinePrefix:] : 276 -> 296
~ -[BCMessageInfo setTitle:] : 12 -> 64
~ -[BCMessageInfo setSubtitle:] : 12 -> 64
~ -[BCMessageInfo setAlternateTitle:] : 12 -> 64
~ -[BCMessageInfo setImageIdentifier:] : 12 -> 64
~ -[BCMessageInfo setImageDescription:] : 12 -> 64
~ -[BCMessageInfo setImage:] : 12 -> 64
~ ___66-[BCLogger mt_log_icloud_messages_apps_businessframework:version:]_block_invoke : 188 -> 196
~ +[BCLogger logEventWithName:businessURI:callToActionText:bizItemReturnedAfterAction:latency:] : 244 -> 236
~ ___93+[BCLogger logEventWithName:businessURI:callToActionText:bizItemReturnedAfterAction:latency:]_block_invoke : 284 -> 300
~ +[BCLogger logEventWithName:version:authDomain:status:] : 200 -> 188
~ ___55+[BCLogger logEventWithName:version:authDomain:status:]_block_invoke : 212 -> 220
~ -[BCWebViewController initWithCallbackURI:] : 280 -> 312
~ -[BCWebViewController loadURL:] : 192 -> 196
~ -[BCWebViewController reload] : 316 -> 332
~ -[BCWebViewController updateNavigationBar] : 104 -> 108
~ -[BCWebViewController viewDidLoad] : 844 -> 920
~ -[BCWebViewController setupSubviews] : 236 -> 260
~ -[BCWebViewController setupConstraints] : 648 -> 736
~ -[BCWebViewController presentCertificatErrorForHost:] : 744 -> 824
~ -[BCWebViewController observeValueForKeyPath:ofObject:change:context:] : 504 -> 508
~ -[BCWebViewController webView:decidePolicyForNavigationAction:decisionHandler:] : 552 -> 580
~ -[BCWebViewController webView:didFailProvisionalNavigation:withError:] : 1128 -> 1232
~ -[BCWebViewController webView:didStartProvisionalNavigation:] : 136 -> 140
~ -[BCWebViewController setWebkitView:] : 20 -> 80
~ -[BCWebViewController setCallbackURI:] : 20 -> 80
~ -[BCNativeOAuth2Response initWithToken:error:] : 380 -> 392
~ -[BCNativeOAuth2Response dictionaryValue] : 512 -> 516
~ -[BCServerSideOAuth2Response initWithRedirectURI:] : 1040 -> 1104
~ -[BCServerSideOAuth2Response _initWithDictionary:] : 504 -> 536
~ -[BCServerSideOAuth2Response dictionaryValue] : 216 -> 236
~ -[BCServerSideOAuth2Response setError:] : 12 -> 64
~ +[BCOAuth2ResponseFactory makeResponseObjectWithDictionary:version:] : 876 -> 908
~ _NativeAuthStatusFromNSString : 100 -> 104
~ _ServerSideAuthStatusFromNSString : 128 -> 132
~ -[BCBrandedHeaderViewController viewDidLoad] : 4032 -> 4508
~ -[BCBrandedHeaderViewController _fetchLogo] : 572 -> 588
~ ___43-[BCBrandedHeaderViewController _fetchLogo]_block_invoke.26 : 524 -> 556
~ -[BCBrandedHeaderViewController setLogoImageView:] : 20 -> 80
~ -[BCMessageData initWithUrl:data:] : 672 -> 692
~ -[BCMessageData decodeData:dictionaryKey:] : 560 -> 568
~ -[BCMessageData combinedDictionary] : 212 -> 232
~ -[BCMessageData imagesArray] : 84 -> 92
~ -[BCInternalAuthenticationRequest initWithDictionary:] : 1344 -> 1432
~ -[BCInternalAuthenticationRequest encodeWithCoder:] : 168 -> 176
~ -[BCInternalAuthenticationRequest initWithCoder:] : 456 -> 480
~ -[BCInternalAuthenticationRequest dictionaryValue] : 476 -> 484
~ -[BCImageStore initWithData:] : 412 -> 432
~ -[BCImageStore generateImageDictionaryFromArray:] : 804 -> 832
~ -[BCImageStore initWithArray:] : 320 -> 328
~ -[BCImageStore initWithImages:] : 472 -> 480
~ -[BCImageStore setRawArray:] : 12 -> 64
~ -[BCImageStore setDictionary:] : 12 -> 64
~ -[BCMessage initWithData:url:messageGUID:isFromMe:] : 1828 -> 1840
~ -[BCMessage updateTitles] : 672 -> 736
~ -[BCMessage initFromOriginalMessage:rootKey:rootObject:receivedMessage:replyMessage:] : 336 -> 332
~ -[BCMessage dictionaryValue] : 564 -> 624
~ -[BCMessage url] : 464 -> 500
~ -[BCMessage encodedStringForDictionary:] : 348 -> 360
~ -[BCMessage data] : 100 -> 108
~ -[BCMessage style] : 292 -> 308
~ -[BCMessage type] : 472 -> 508
~ -[BCMessage image] : 108 -> 120
~ -[BCMessage rootKey] : 900 -> 1020
~ -[BCMessage isAnyUnknownRootKey] : 356 -> 368
~ -[BCMessage makeRootObjectWithMessageData:dictionary:imageDictionary:version:] : 440 -> 476
~ ___32-[BCMessage isAnyUnknownRootKey]_block_invoke : 360 -> 364
~ +[BCMessage defaultBubbleTitleFor:] : 816 -> 888
~ -[BCMessage setTitle:] : 12 -> 64
~ -[BCMessage setSubtitle:] : 12 -> 64
~ -[BCMessage setSummaryText:] : 12 -> 64
~ -[BCMessage setSubcaption:] : 12 -> 64
~ -[BCMessage setAccessibilityLabel:] : 12 -> 64
~ -[BCImageManager init] : 136 -> 128
~ -[BCImageManager _fetchBrandIconDataForMapItem:desiredSize:allowSmaller:completion:] : 408 -> 412
~ -[BCImageManager _fetchNavBarBrandIconDataForMapItem:desiredSize:allowSmaller:completion:] : 408 -> 412
~ _LogCategory_Daemon : 84 -> 100
~ +[BCConstants allowedAppleURNs] : 84 -> 100
~ ___31+[BCConstants allowedAppleURNs]_block_invoke : 268 -> 276
~ -[NSString normalizedBase64Encoded] : 136 -> 144
~ -[NSURL fragments] : 444 -> 464
~ +[BCServerSideOAuth2URLProvider URLProviderWithDictionary:] : 1912 -> 2124
~ -[BCServerSideOAuth2URLProvider _initWithAuthorizationURL:clientIdentifier:redirectURI:scope:state:responseType:additionalParameters:] : 332 -> 304
~ -[BCServerSideOAuth2URLProvider encodeWithCoder:] : 208 -> 216
~ -[BCServerSideOAuth2URLProvider initWithCoder:] : 476 -> 508
~ -[BCServerSideOAuth2URLProvider authenticationSessionURL] : 732 -> 756
~ -[BCServerSideOAuth2URLProvider shouldHandleRedirectURI:] : 88 -> 96
~ -[BCServerSideOAuth2URLProvider debugDescription] : 148 -> 160
~ -[BCServerSideOAuth2URLProvider setRedirectURI:] : 12 -> 64
~ +[BCChatAction openTranscript:intentParameters:] : 624 -> 640
~ ___48+[BCChatAction openTranscript:intentParameters:]_block_invoke : 304 -> 316
~ -[BCOAuth2Request _initWithDictionary:URLProvider:] : 348 -> 356
~ -[BCOAuth2Request debugDescription] : 224 -> 244
~ -[BCOAuth2Request setBusinessIdentifier:] : 12 -> 64
~ -[BCOAuth2Request setOauth2:] : 12 -> 64
~ -[BCNativeOAuth2Request _initWithDictionary:] : 412 -> 436
~ -[BCServerSideOAuth2Request _initWithDictionary:] : 412 -> 436
~ +[BCCryptor encryptData:key:completion:] : 1044 -> 1052
~ ___40+[BCCryptor encryptData:key:completion:]_block_invoke : 808 -> 836
~ -[BCServerErrorView init] : 1780 -> 1944
~ -[BCChatButton setup] : 952 -> 1008
~ -[BCChatButton encodeWithCoder:] : 120 -> 124
~ -[BCChatButton updateAppearanceForState:] : 468 -> 492
~ -[BCChatButton calculateButtonLayout] : 856 -> 880
~ -[BCChatButton hitTest:withEvent:] : 96 -> 100
~ -[BCChatButton viewForFirstBaselineLayout] : 20 -> 76
~ -[BCChatButton viewForLastBaselineLayout] : 20 -> 76
~ -[BCInvalidCertificatView initWithHost:] : 3276 -> 3584
~ -[BCImage initWithImageData:identifier:description:] : 188 -> 172
~ -[BCInternalAuthenticationManager initWithAuthenticationRequest:] : 236 -> 220
~ -[BCInternalAuthenticationManager fetchCredentials:] : 248 -> 252
~ ___52-[BCInternalAuthenticationManager fetchCredentials:]_block_invoke : 1524 -> 1580
~ -[BCInternalAuthenticationManager isUserSignedIn] : 60 -> 64
~ -[BCInternalAuthenticationManager title] : 372 -> 420
~ -[BCInternalAuthenticationManager labelCategory] : 92 -> 112
~ -[BCInternalAuthenticationManager subtitle] : 420 -> 472
~ -[BCInternalAuthenticationManager action] : 328 -> 368
~ -[BCAuthenticationManager initWithAuthenticationRequest:] : 116 -> 108
~ -[BCAuthenticationManager fetchTokenWithRequest:completion:] : 1616 -> 1676
~ -[BCAuthenticationManager processQueryItems:completion:] : 552 -> 556
~ -[BCAuthenticationManager exchangeCode:completion:] : 608 -> 640
~ ___51-[BCAuthenticationManager exchangeCode:completion:]_block_invoke : 1164 -> 1200
~ -[BCAuthenticationManager URLSession:didReceiveChallenge:completionHandler:] : 180 -> 188
~ -[BCAuthenticationManager setAuthenticationRequest:] : 12 -> 64
~ -[BCProgressIndicatorView init] : 176 -> 184
~ -[BCError initWithCode:domain:message:] : 168 -> 160
~ -[BCError initWithDictionary:] : 640 -> 688
~ -[BCError encodeWithCoder:] : 128 -> 136
~ -[BCError initWithCoder:] : 236 -> 248
~ -[BCError setCode:] : 12 -> 64
~ -[BCError setDomain:] : 12 -> 64
~ -[BCError setMessage:] : 12 -> 64
~ +[BCNativeOAuth2URLProvider URLProviderWithDictionary:] : 1844 -> 1968
~ -[BCNativeOAuth2URLProvider _initWithAuthorizationURL:accessTokenURL:clientSecret:clientIdentifier:responseEncryptionKey:scope:state:responseType:] : 368 -> 340
~ -[BCNativeOAuth2URLProvider encodeWithCoder:] : 248 -> 256
~ -[BCNativeOAuth2URLProvider initWithCoder:] : 540 -> 576
~ -[BCNativeOAuth2URLProvider authenticationSessionURL] : 624 -> 640
~ -[BCNativeOAuth2URLProvider shouldHandleRedirectURI:] : 88 -> 96
~ -[BCNativeOAuth2URLProvider tokenExchangeBodyWithCode:] : 536 -> 556
CStrings:
+ "defaultWebpagePreferences"
+ "setSecurityRestrictionMode:"

```
