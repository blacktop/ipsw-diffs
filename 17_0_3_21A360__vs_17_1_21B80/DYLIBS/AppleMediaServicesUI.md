## AppleMediaServicesUI

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`

```diff

-5.0.72.3.0
-  __TEXT.__text: 0x1163d0
-  __TEXT.__auth_stubs: 0x2300
-  __TEXT.__objc_methlist: 0xc370
+5.1.8.2.2
+  __TEXT.__text: 0x1180b8
+  __TEXT.__auth_stubs: 0x2310
+  __TEXT.__objc_methlist: 0xc450
   __TEXT.__const: 0x3d04
-  __TEXT.__cstring: 0x9204
-  __TEXT.__oslogstring: 0x86de
-  __TEXT.__gcc_except_tab: 0x10d8
+  __TEXT.__cstring: 0x9414
+  __TEXT.__oslogstring: 0x888c
+  __TEXT.__gcc_except_tab: 0x10f4
   __TEXT.__dlopen_cstrs: 0xbb6
   __TEXT.__swift5_typeref: 0x3cc2
   __TEXT.__swift5_reflstr: 0x10a8

   __TEXT.__constg_swiftt: 0x1dfc
   __TEXT.__swift5_fieldmd: 0xf58
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_capture: 0x688
+  __TEXT.__swift5_capture: 0x66c
   __TEXT.__swift5_proto: 0x1d0
   __TEXT.__swift5_types: 0x15c
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4f24
+  __TEXT.__unwind_info: 0x4f34
   __TEXT.__eh_frame: 0x1138
-  __TEXT.__objc_classname: 0x2154
-  __TEXT.__objc_methname: 0x20cc2
-  __TEXT.__objc_methtype: 0x6b43
-  __TEXT.__objc_stubs: 0x17e00
-  __DATA_CONST.__got: 0x830
-  __DATA_CONST.__const: 0x3450
+  __TEXT.__objc_classname: 0x2149
+  __TEXT.__objc_methname: 0x21224
+  __TEXT.__objc_methtype: 0x6b7d
+  __TEXT.__objc_stubs: 0x18120
+  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__const: 0x3478
   __DATA_CONST.__objc_classlist: 0x818
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x182e0
-  __DATA_CONST.__objc_selrefs: 0x7288
+  __DATA_CONST.__objc_const: 0x18378
+  __DATA_CONST.__objc_selrefs: 0x7380
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__objc_const: 0x54b0
-  __AUTH_CONST.__cfstring: 0x9960
-  __AUTH_CONST.__const: 0x4e28
+  __AUTH_CONST.__objc_const: 0x54f8
+  __AUTH_CONST.__cfstring: 0x9be0
+  __AUTH_CONST.__const: 0x4d88
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH_CONST.__auth_got: 0x1198
   __AUTH.__objc_data: 0x47c8
   __AUTH.__data: 0x2b00
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0xde8
+  __DATA.__objc_classrefs: 0xe00
   __DATA.__objc_superrefs: 0x630
-  __DATA.__objc_ivar: 0xec4
+  __DATA.__objc_ivar: 0xed0
   __DATA.__objc_data: 0x20
   __DATA.__data: 0x3098
   __DATA.__objc_stublist: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 23670C25-87BC-3468-9C61-ABF952192B0C
-  Functions: 8651
-  Symbols:   18545
-  CStrings:  9730
+  UUID: 182EF989-2C1F-3446-B2ED-9D463CE105F1
+  Functions: 8659
+  Symbols:   18610
+  CStrings:  9819
 
Symbols:
+ +[AMSUIAppearance _defaultButtonBackgroundColorForStyle:withTraitCollection:]
+ +[AMSUIParentalVerificationApplePayTask _biometricsRequestWithAccount:]
+ +[AMSUIParentalVerificationApplePayTask _contextIconWithBundle:accountParameters:]
+ +[AMSUIParentalVerificationApplePayTask _contextTitleWithBag:bundle:accountParameters:]
+ +[AMSUIParentalVerificationApplePayTask _messageWithBag:bundle:]
+ +[AMSUIParentalVerificationApplePayTask _paymentRequestMetadataWithBag:bundle:accountParameters:]
+ +[AMSUIParentalVerificationApplePayTask _sheetTitleWithBag:bundle:]
+ +[AMSUIParentalVerificationApplePayTask _titleIconWithBundle:]
+ +[AMSUIParentalVerificationApplePayTask paymentRequestFromPaymentSession:currencyCode:countryCode:networks:bag:accountParameters:bundle:biometricsRequest:]
+ +[AMSUIWebAppearance systemClearColor]
+ +[PPMUtilities PPMConfirmedValueWithValue:newValue:]
+ +[PPMUtilities PPMScaledValueUsingValue:]
+ -[AMSUIBaseMessageViewController _preferredContentSizeCategoryDidChange:]
+ -[AMSUIBubbleTipViewController _preferredContentSizeCategoryDidChange:]
+ -[AMSUIEngagementRemoteViewController internalPreferredContentSizeOverride]
+ -[AMSUIEngagementRemoteViewController preferredContentSizeOverride]
+ -[AMSUIEngagementRemoteViewController setInternalPreferredContentSizeOverride:]
+ -[AMSUIEngagementRemoteViewController setPreferredContentSizeOverride:]
+ -[AMSUIParentalVerificationApplePayTask _promiseToRequestWalletDataUsingSession:bag:accountParameters:bundle:]
+ -[AMSUIParentalVerificationApplePayTask biometricsRequest]
+ -[AMSUIParentalVerificationApplePayTask setBiometricsRequest:]
+ -[AMSUIWebAction presentingSceneBundleIdentifierPromise]
+ -[AMSUIWebAction presentingSceneBundleIdentifier]
+ -[AMSUIWebAction presentingSceneIdentifierPromise]
+ -[AMSUIWebAction presentingSceneIdentifier]
+ GCC_except_table25
+ _AMSPaymentSheetPaymentRequest
+ _AMSPaymentSheetPaymentRequestLayout
+ _AMSPaymentSheetPaymentRequestMetadata
+ _OBJC_CLASS_$_AMSBiometricsSignatureRequest
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_PPMUtilities
+ _OBJC_IVAR_$_AMSUIEngagementRemoteViewController._internalPreferredContentSizeOverride
+ _OBJC_IVAR_$_AMSUIEngagementRemoteViewController._preferredContentSizeOverride
+ _OBJC_IVAR_$_AMSUIParentalVerificationApplePayTask._biometricsRequest
+ _OBJC_METACLASS_$_PPMUtilities
+ __OBJC_$_CLASS_METHODS_PPMUtilities
+ __OBJC_CLASS_RO_$_PPMUtilities
+ __OBJC_METACLASS_RO_$_PPMUtilities
+ ___34-[AMSUIWebBuyAction _runLegacyBuy]_block_invoke.100
+ ___35-[AMSUIWebDelegateAction runAction]_block_invoke.51
+ ___44-[AMSUIWebBuyAction _runBuyWithContentType:]_block_invoke.91
+ ___48-[AMSUIWebViewController _loadRequest:bagValue:]_block_invoke.184
+ ___50-[AMSUIWebAction presentingSceneIdentifierPromise]_block_invoke
+ ___54-[AMSUIWebAuthorizeApplePayEnrollmentAction runAction]_block_invoke_2.39
+ ___54-[AMSUIWebAuthorizeApplePayEnrollmentAction runAction]_block_invoke_3
+ ___56-[AMSUIWebAction presentingSceneBundleIdentifierPromise]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_v16?0"PKPayment"8ls32l8
+ ___block_descriptor_40_e8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e29_"AMSPromise"16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.71
+ _objc_msgSend$_biometricsRequestWithAccount:
+ _objc_msgSend$_contextIconWithBundle:accountParameters:
+ _objc_msgSend$_contextTitleWithBag:bundle:accountParameters:
+ _objc_msgSend$_defaultButtonBackgroundColorForStyle:withTraitCollection:
+ _objc_msgSend$_messageWithBag:bundle:
+ _objc_msgSend$_paymentRequestMetadataWithBag:bundle:accountParameters:
+ _objc_msgSend$_preferredContentSizeCategoryDidChange:
+ _objc_msgSend$_promiseToRequestWalletDataUsingSession:bag:accountParameters:bundle:
+ _objc_msgSend$_sheetTitleWithBag:bundle:
+ _objc_msgSend$_titleIconWithBundle:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$biometricsRequest
+ _objc_msgSend$externalizedContext
+ _objc_msgSend$initWithAccount:clientInfo:challenge:localAuthContext:options:error:
+ _objc_msgSend$localAuthAccessControlRef
+ _objc_msgSend$localAuthContext
+ _objc_msgSend$paymentRequestFromPaymentSession:currencyCode:countryCode:networks:bag:accountParameters:bundle:biometricsRequest:
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:
+ _objc_msgSend$presentingSceneBundleIdentifier
+ _objc_msgSend$presentingSceneBundleIdentifierPromise
+ _objc_msgSend$presentingSceneIdentifier
+ _objc_msgSend$presentingSceneIdentifierPromise
+ _objc_msgSend$setAccesssControlRef:
+ _objc_msgSend$setBiometricsRequest:
+ _objc_msgSend$setClientViewSourceIdentifier:
+ _objc_msgSend$setClientViewSourceParameter:
+ _objc_msgSend$setDisablePasscodeFallback:
+ _objc_msgSend$setExternalizedContext:
+ _objc_msgSend$setLocalizedAuthorizingTitle:
+ _objc_msgSend$setPresentationSceneBundleIdentifier:
+ _objc_msgSend$setPresentationSceneIdentifier:
+ _objc_msgSend$sharedPurchaseConfig
+ _objc_msgSend$updateTraitsIfNeeded
- +[AMSUIParentalVerificationApplePayTask paymentRequestFromPaymentSession:currencyCode:countryCode:networks:]
- -[AMSUIBubbleTipViewController traitCollectionDidChange:]
- -[AMSUIParentalVerificationApplePayTask _promiseToRequestWalletDataUsingSession:]
- -[AMSUIWebBuyAction _presentingSceneBundleIdentifierPromise]
- -[AMSUIWebBuyAction _presentingSceneBundleIdentifier]
- -[AMSUIWebBuyAction _presentingSceneIdentifierPromise]
- -[AMSUIWebBuyAction _presentingSceneIdentifier]
- GCC_except_table24
- GCC_except_table31
- _AMSMaybeUpperCaseNormalisedStringFoundInList
- _OBJC_CLASS_$_AMSUIPaymentSessionTask
- _OBJC_METACLASS_$_AMSUIPaymentSessionTask
- __OBJC_CLASS_RO_$_AMSUIPaymentSessionTask
- __OBJC_METACLASS_RO_$_AMSUIPaymentSessionTask
- ___34-[AMSUIWebBuyAction _runLegacyBuy]_block_invoke.102
- ___35-[AMSUIWebDelegateAction runAction]_block_invoke.48
- ___44-[AMSUIWebBuyAction _runBuyWithContentType:]_block_invoke.99
- ___48-[AMSUIWebViewController _loadRequest:bagValue:]_block_invoke.190
- ___54-[AMSUIWebBuyAction _presentingSceneIdentifierPromise]_block_invoke
- ___60-[AMSUIWebBuyAction _presentingSceneBundleIdentifierPromise]_block_invoke
- ___block_descriptor_40_e8_32s_e31_v24?0"PKPayment"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16ls32l8
- ___block_literal_global.79
- _block_copy_helper.20
- _block_copy_helper.26
- _block_descriptor.22
- _block_descriptor.28
- _block_destroy_helper.21
- _block_destroy_helper.27
- _objc_msgSend$ISOCountryCodes
- _objc_msgSend$_presentingSceneBundleIdentifier
- _objc_msgSend$_presentingSceneBundleIdentifierPromise
- _objc_msgSend$_presentingSceneIdentifier
- _objc_msgSend$_presentingSceneIdentifierPromise
- _objc_msgSend$_promiseToRequestWalletDataUsingSession:
- _objc_msgSend$paymentRequestFromPaymentSession:currencyCode:countryCode:networks:
- _objc_msgSend$uppercaseString
CStrings:
+ "%@: %@ "
+ "%@: [%@] %@ "
+ "%{public}@ returning bundle identifier %{public}@"
+ "%{public}@ returning scene identifier %{public}@"
+ "%{public}@: [%{public}@] Failed to create biometrics request with error: %{public}@"
+ "%{public}@: [%{public}@] Failed to serialise payment request with error: %{public}@"
+ "%{public}@Calling into delegate: %{public}@"
+ "%{public}@Delegate does not implement %{public}@. delegate: %{public}@"
+ "%{public}@Delegate is nil"
+ "%{public}@Falling back to superclass"
+ "%{public}@Superclass returned scene identifier %{public}@"
+ "%{public}@begin"
+ "@\"AMSBiometricsSignatureRequest\""
+ "@\"NSValue\""
+ "AMSPaymentSheetPaymentRequestLayoutValuePVK"
+ "AMSUIPaymentSheetViewProvider"
+ "FS54x54"
+ "Failed to load cached content with no fallback"
+ "Loading asset from remote"
+ "No biometrics for payment request"
+ "PARENTAL_VERIFICATION_APPLE_PAY_CLASSIC_CONTEXT_NAME"
+ "PARENTAL_VERIFICATION_APPLE_PAY_CLASSIC_MESSAGE"
+ "PARENTAL_VERIFICATION_APPLE_PAY_CLASSIC_SHEET_AUTH_TITLE"
+ "PARENTAL_VERIFICATION_APPLE_PAY_CLASSIC_WALLET"
+ "PPMConfirmedValueWithValue:newValue:"
+ "PPMScaledValueUsingValue:"
+ "PPMUtilities"
+ "PVKAPCBiometricsChallenge"
+ "PVKApplePayClassicContextIcon"
+ "PVKApplePayClassicContextTitle"
+ "T@\"AMSBiometricsSignatureRequest\",&,N,V_biometricsRequest"
+ "T@\"NSValue\",&,N,V_internalPreferredContentSizeOverride"
+ "T{CGSize=dd},N,V_preferredContentSizeOverride"
+ "Unable to create Wallet biometrics request"
+ "Wallet20x20"
+ "_biometricsRequest"
+ "_biometricsRequestWithAccount:"
+ "_contextIconWithBundle:accountParameters:"
+ "_contextTitleWithBag:bundle:accountParameters:"
+ "_defaultButtonBackgroundColorForStyle:withTraitCollection:"
+ "_internalPreferredContentSizeOverride"
+ "_messageWithBag:bundle:"
+ "_paymentRequestMetadataWithBag:bundle:accountParameters:"
+ "_preferredContentSizeCategoryDidChange:"
+ "_preferredContentSizeOverride"
+ "_promiseToRequestWalletDataUsingSession:bag:accountParameters:bundle:"
+ "_sheetTitleWithBag:bundle:"
+ "_titleIconWithBundle:"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "biometricsRequest"
+ "contextIcon"
+ "contextTitle"
+ "d32@0:8d16d24"
+ "externalizedContext"
+ "initWithAccount:clientInfo:challenge:localAuthContext:options:error:"
+ "internalPreferredContentSizeOverride"
+ "localAuthAccessControlRef"
+ "localAuthContext"
+ "paymentRequestFromPaymentSession:currencyCode:countryCode:networks:bag:accountParameters:bundle:biometricsRequest:"
+ "preferredContentSizeOverride"
+ "preferredFontDescriptorWithTextStyle:"
+ "presentingSceneBundleIdentifierPromise"
+ "presentingSceneIdentifierPromise"
+ "screenScale"
+ "setADPState:"
+ "setAccesssControlRef:"
+ "setBiometricsRequest:"
+ "setClientViewSourceIdentifier:"
+ "setClientViewSourceParameter:"
+ "setDisablePasscodeFallback:"
+ "setExternalizedContext:"
+ "setInternalPreferredContentSizeOverride:"
+ "setLocalizedAuthorizingTitle:"
+ "setPreferredContentSizeOverride:"
+ "setPresentationSceneBundleIdentifier:"
+ "setPresentationSceneIdentifier:"
+ "sharedPurchaseConfig"
+ "sheetTitle"
+ "systemClearColor"
+ "titleIcon"
+ "updateTraitsIfNeeded"
+ "v16@?0@\"PKPayment\"8"
- "\f"
- "AMSNormalisedCountryCodeForPaymentRequest: [%{public}@] invalid country code: %{public}@"
- "AMSUIPaymentSessionTask"
- "Failed to load cached content"
- "ISOCountryCodes"
- "Loading Image from remote"
- "_presentingSceneBundleIdentifier"
- "_presentingSceneBundleIdentifierPromise"
- "_presentingSceneIdentifier"
- "_presentingSceneIdentifierPromise"
- "_promiseToRequestWalletDataUsingSession:"
- "paymentRequestFromPaymentSession:currencyCode:countryCode:networks:"
- "uppercaseString"
- "v24@?0@\"PKPayment\"8@\"NSError\"16"

```
