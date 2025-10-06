## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-191.3.0.0.0
-  __TEXT.__text: 0x13f450
-  __TEXT.__auth_stubs: 0x2c50
-  __TEXT.__objc_methlist: 0xb560
-  __TEXT.__const: 0x2da4
-  __TEXT.__cstring: 0xc3c1
-  __TEXT.__oslogstring: 0xa0d6
+191.6.0.0.0
+  __TEXT.__text: 0x140f90
+  __TEXT.__auth_stubs: 0x2c60
+  __TEXT.__objc_methlist: 0xb5f8
+  __TEXT.__const: 0x2dd4
+  __TEXT.__cstring: 0xc4c1
+  __TEXT.__oslogstring: 0xa3c6
   __TEXT.__gcc_except_tab: 0x1cbc
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x1cd4
-  __TEXT.__swift5_typeref: 0x3d90
+  __TEXT.__constg_swiftt: 0x1cf0
+  __TEXT.__swift5_typeref: 0x3d60
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0xac2
-  __TEXT.__swift5_fieldmd: 0xcec
+  __TEXT.__swift5_fieldmd: 0xcfc
   __TEXT.__swift5_assocty: 0x2a0
   __TEXT.__swift5_proto: 0x158
-  __TEXT.__swift5_types: 0x138
-  __TEXT.__swift5_capture: 0xcdc
+  __TEXT.__swift5_types: 0x13c
+  __TEXT.__swift5_capture: 0xcec
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4aa8
+  __TEXT.__unwind_info: 0x4b20
   __TEXT.__eh_frame: 0x1580
-  __TEXT.__objc_classname: 0x11c9
-  __TEXT.__objc_methname: 0x1d00a
+  __TEXT.__objc_classname: 0x11e1
+  __TEXT.__objc_methname: 0x1d10f
   __TEXT.__objc_methtype: 0x3dc8
-  __TEXT.__objc_stubs: 0x14c20
-  __DATA_CONST.__got: 0x11e8
-  __DATA_CONST.__const: 0x3fe0
-  __DATA_CONST.__objc_classlist: 0x530
+  __TEXT.__objc_stubs: 0x14d20
+  __DATA_CONST.__got: 0x11a8
+  __DATA_CONST.__const: 0x4010
+  __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7530
+  __DATA_CONST.__objc_selrefs: 0x7568
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4d0
-  __AUTH_CONST.__auth_got: 0x1638
-  __AUTH_CONST.__const: 0x46f8
-  __AUTH_CONST.__cfstring: 0x8e80
-  __AUTH_CONST.__objc_const: 0x1d4c0
-  __AUTH_CONST.__objc_intobj: 0x300
+  __AUTH_CONST.__auth_got: 0x1640
+  __AUTH_CONST.__const: 0x4740
+  __AUTH_CONST.__cfstring: 0x9040
+  __AUTH_CONST.__objc_const: 0x1d598
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x498
-  __AUTH.__objc_data: 0x4e08
+  __AUTH.__objc_data: 0x4e58
   __AUTH.__data: 0xd50
   __DATA.__objc_ivar: 0x700
   __DATA.__data: 0x2cb0
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x3028
+  __DATA.__bss: 0x3038
   __DATA.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 294EF9E6-43CD-3763-B56B-4603721DF879
-  Functions: 7285
-  Symbols:   15611
-  CStrings:  9353
+  UUID: 2522CEB9-11BB-3CE6-B44A-6133D545A836
+  Functions: 7319
+  Symbols:   15697
+  CStrings:  9406
 
Symbols:
+ +[FBKPresubmissionConsent entityName]
+ +[FBKPresubmissionConsent uniquingKey]
+ -[FBKBugForm hasPresubmissionConsent]
+ -[FBKBugForm presubmissionConsentID]
+ -[FBKBugForm presubmissionConsentText]
+ -[FBKData recordConsentResponseForConsent:completion:]
+ -[FBKPresubmissionConsent setPropertiesFromJSONObject:]
+ -[FBKPresubmissionConsent setPropertiesFromJSONObject:].cold.1
+ -[FBKSeedPortalAPI appleConnectAuthParamsURL]
+ -[FBKSeedPortalAPI getAppleConnectAuthParamsWithSuccess:error:]
+ -[FBKSeedPortalAPI respondToConsent:success:error:]
+ -[FBKUser addSignedConsentWithID:]
+ -[FBKUser hasSignedConsentWithID:]
+ -[FBKUser hasSignedConsentWithID:].cold.1
+ -[FBKUser userDefaultsKeyForConsentID:]
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table144
+ GCC_except_table149
+ GCC_except_table188
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table344
+ GCC_except_table388
+ GCC_except_table393
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table406
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table60
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table7
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table90
+ _FBKPerformAppleConnectAuthenticationWithClientID
+ _FBKPerformAppleConnectAuthenticationWithClientID.ACAuthenticationRequestClass
+ _FBKPerformAppleConnectAuthenticationWithClientID.ACAuthenticationResponseClass
+ _FBKPerformAppleConnectAuthenticationWithClientID.ACMobileAuthenticationContextClass
+ _FBKPerformAppleConnectAuthenticationWithClientID.cold.1
+ _FBKPerformAppleConnectAuthenticationWithClientID.cold.2
+ _FBKUnauthConsentKeyPrefix
+ _FBKValidateAuthParam
+ _FBKValidateAuthParam.cold.1
+ _FBKValidateAuthParam.cold.2
+ _FBKValidateAuthParam.cold.3
+ _OBJC_CLASS_$_FBKPresubmissionConsent
+ _OBJC_METACLASS_$_FBKPresubmissionConsent
+ __OBJC_$_CLASS_METHODS_FBKPresubmissionConsent
+ __OBJC_$_INSTANCE_METHODS_FBKPresubmissionConsent
+ __OBJC_$_PROP_LIST_FBKPresubmissionConsent
+ __OBJC_CLASS_RO_$_FBKPresubmissionConsent
+ __OBJC_METACLASS_RO_$_FBKPresubmissionConsent
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.255
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.255.cold.1
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.262
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.264
+ ___42-[FBKBugFormTableViewController legalText]_block_invoke.297
+ ___51-[FBKSeedPortalAPI respondToConsent:success:error:]_block_invoke
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke.308
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke_2
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke_3
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke_4
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke_5
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke_5.cold.1
+ ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.241
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.203
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.203.cold.1
+ ___63-[FBKSeedPortalAPI getAppleConnectAuthParamsWithSuccess:error:]_block_invoke
+ ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke.344
+ ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke_2.345
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.352
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.356
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.353
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.357
+ ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.253
+ ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.350
+ ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.350.cold.1
+ ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.271
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175.cold.1
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175.cold.2
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175.cold.3
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.178
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.314
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.316
+ ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.224
+ ___87-[FBKData beginSubmissionForFollowup:withResponses:didOptOut:withCollector:completion:]_block_invoke.359
+ ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.216
+ ___92-[FBKBugFormTableViewController checkPresubmissionLegalText:presentedDEConsent:andContinue:]_block_invoke_3
+ ___FBKLoginWithAppleConnect_block_invoke.45
+ ___FBKLoginWithAppleConnect_block_invoke.45.cold.1
+ ___FBKPerformAppleConnectAuthenticationWithClientID_block_invoke
+ ___FBKPerformAppleConnectAuthenticationWithClientID_block_invoke_2
+ ___FBKPerformAppleConnectAuthenticationWithClientID_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
+ ___block_literal_global.122
+ ___block_literal_global.258
+ ___block_literal_global.265
+ ___block_literal_global.284
+ ___block_literal_global.295
+ ___block_literal_global.299
+ ___block_literal_global.307
+ ___block_literal_global.318
+ ___block_literal_global.348
+ ___block_literal_global.372
+ ___block_literal_global.644
+ ___block_literal_global.95
+ _block_copy_helper.1
+ _block_copy_helper.15
+ _block_copy_helper.18
+ _block_descriptor.17
+ _block_descriptor.20
+ _block_descriptor.3
+ _block_destroy_helper.16
+ _block_destroy_helper.19
+ _block_destroy_helper.2
+ _legalText.onceToken.296
+ _objc_msgSend$addSignedConsentWithID:
+ _objc_msgSend$appleConnectAuthParamsURL
+ _objc_msgSend$getAppleConnectAuthParamsWithSuccess:error:
+ _objc_msgSend$hasPresubmissionConsent
+ _objc_msgSend$hasSignedConsentWithID:
+ _objc_msgSend$presubmissionConsent
+ _objc_msgSend$presubmissionConsentID
+ _objc_msgSend$presubmissionConsentText
+ _objc_msgSend$recordConsentResponseForConsent:completion:
+ _objc_msgSend$respondToConsent:success:error:
+ _objc_msgSend$setPresubmissionConsent:
+ _objc_msgSend$setSignedConsents:
+ _objc_msgSend$signedConsents
+ _objc_msgSend$userDefaultsKeyForConsentID:
+ _swift_release_n
+ _symbolic So13UIAlertActionCIegg_Sg
+ _symbolic _____ 12FeedbackCore26FBKDEConsentAlertPresenterV
- -[FBKSeedPortalAPI appleConnectEnvironment]
- GCC_except_table106
- GCC_except_table114
- GCC_except_table117
- GCC_except_table121
- GCC_except_table125
- GCC_except_table143
- GCC_except_table145
- GCC_except_table273
- GCC_except_table275
- GCC_except_table279
- GCC_except_table343
- GCC_except_table381
- GCC_except_table386
- GCC_except_table389
- GCC_except_table390
- GCC_except_table399
- GCC_except_table52
- GCC_except_table53
- GCC_except_table57
- GCC_except_table58
- GCC_except_table65
- GCC_except_table78
- GCC_except_table81
- _FBKLoginWithAppleConnect.ACAuthenticationRequestClass
- _FBKLoginWithAppleConnect.ACAuthenticationResponseClass
- _FBKLoginWithAppleConnect.ACMobileAuthenticationContextClass
- _FBKLoginWithAppleConnect.cold.1
- _FBKLoginWithAppleConnect.cold.2
- _NSHTTPCookieDiscard
- _NSHTTPCookieDomain
- _NSHTTPCookieExpires
- _NSHTTPCookieName
- _NSHTTPCookiePath
- _NSHTTPCookieSecure
- _NSHTTPCookieValue
- _OBJC_CLASS_$_NSHTTPCookie
- ___39-[FBKBugFormTableViewController submit]_block_invoke.265
- ___39-[FBKBugFormTableViewController submit]_block_invoke.265.cold.1
- ___39-[FBKBugFormTableViewController submit]_block_invoke.272
- ___39-[FBKBugFormTableViewController submit]_block_invoke.274
- ___42-[FBKBugFormTableViewController legalText]_block_invoke.307
- ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.245
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.207
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.207.cold.1
- ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke.343
- ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke_2.344
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.350
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.355
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.352
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.356
- ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.257
- ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.349
- ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.349.cold.1
- ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.275
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.180
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.180.cold.1
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.180.cold.2
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.180.cold.3
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.183
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.324
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.326
- ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.228
- ___87-[FBKData beginSubmissionForFollowup:withResponses:didOptOut:withCollector:completion:]_block_invoke.357
- ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.220
- ___FBKLoginWithAppleConnect_block_invoke_2
- ___FBKLoginWithAppleConnect_block_invoke_2.cold.1
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.252
- ___block_literal_global.255
- ___block_literal_global.274
- ___block_literal_global.304
- ___block_literal_global.305
- ___block_literal_global.309
- ___block_literal_global.328
- ___block_literal_global.347
- ___block_literal_global.371
- ___block_literal_global.642
- ___block_literal_global.90
- _block_copy_helper.16
- _block_copy_helper.23
- _block_descriptor.18
- _block_descriptor.25
- _block_destroy_helper.17
- _block_destroy_helper.24
- _legalText.onceToken.306
- _objc_msgSend$appleConnectEnvironment
- _objc_msgSend$arrayWithObjects:
- _objc_msgSend$cookieWithProperties:
- _objc_msgSend$requestHeaderFieldsWithCookies:
- _objc_msgSend$setAppID:
- _objc_msgSend$setAuthType:
- _symbolic So29FBKBugFormTableViewControllerC
- _symbolic So29FBKBugFormTableViewControllerCSgXwz_Xx
CStrings:
+ "%@%@-%@"
+ "(empty)"
+ "(null)"
+ "-%@"
+ "ACCEPT"
+ "Added Consent ID %@ to user's signed consents"
+ "Attempted to add nil Consent ID, ignoring"
+ "Authenticated Flow, check signed consent"
+ "Consent ID %@ already exists in signed consents, skipping"
+ "Consent ID was nil, returning NO"
+ "Consent status result for consent ID %@: %s"
+ "Empty %{public}@ in auth params"
+ "FBKPresubmissionConsent"
+ "FBKPresubmissionConsent setPropertiesFromJSONObject called with non-dictionary object of type: %{public}@"
+ "Failed to fetch auth params: [%{public}@]"
+ "GET"
+ "Missing or invalid %{public}@ in auth params"
+ "OAuth params - Client ID: [%{public}@], Scopes: [%{public}@], Audiences: [%{public}@], Resource: [%{public}@]"
+ "PresubmissionConsent"
+ "T@\"FBKBugForm\",W,D,N"
+ "T@\"FBKPresubmissionConsent\",&,D,N"
+ "UnauthConsent"
+ "Unauthenticated Flow, checking user defaults for consent using key: %@"
+ "Unauthenticated Flow, setting user defaults for consent using key: %@"
+ "User signed consent ID [%d]"
+ "addSignedConsentWithID:"
+ "appleConnectAuthParamsURL"
+ "authType"
+ "confidentiality_agreement"
+ "getAppleConnectAuthParamsWithSuccess:error:"
+ "hasPresubmissionConsent"
+ "hasSignedConsentWithID:"
+ "login/with_oidc/apple-connect"
+ "login/with_oidc/apple-connect/auth-params"
+ "nonce"
+ "not signed"
+ "oauthClientID"
+ "oauthGrantType"
+ "oauthScopes"
+ "oauth_audiences"
+ "oauth_client_id"
+ "oauth_resource"
+ "oauth_scopes"
+ "presubmissionConsent"
+ "presubmissionConsentID"
+ "presubmissionConsentText"
+ "presubmission_confidentiality_agreement"
+ "recordConsentResponseForConsent:completion:"
+ "respondToConsent:success:error:"
+ "setPresubmissionConsent:"
+ "setSignedConsents:"
+ "signed"
+ "signedConsents"
+ "userDefaultsKeyForConsentID:"
+ "v16@?0@\"NSDictionary\"8"
- ".apple.com"
- "AppleConnect headers: %@"
- "GO_BACK"
- "SUBMISSION_PII_MESSAGE"
- "TRUE"
- "acack"
- "acack-uat"
- "appleConnectEnvironment"
- "arrayWithObjects:"
- "cookieWithProperties:"
- "login/with_ac"
- "presentConsentTexts:presentedConsent:andContinue:"
- "requestHeaderFieldsWithCookies:"
- "setAppID:"
- "setAuthType:"

```
