## AskPermission

> `/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission`

```diff

-129.1.6.0.0
-  __TEXT.__text: 0xa464
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0xa9c
-  __TEXT.__const: 0xfa
+129.1.11.0.0
+  __TEXT.__text: 0x11208
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0xe3c
+  __TEXT.__const: 0x1b2
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__cstring: 0x7a8
-  __TEXT.__oslogstring: 0xc7d
-  __TEXT.__swift5_typeref: 0x94
-  __TEXT.__swift5_capture: 0x80
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x368
-  __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x1bb6
-  __TEXT.__objc_methtype: 0x6af
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0x118
+  __TEXT.__cstring: 0xad8
+  __TEXT.__oslogstring: 0xcb4
+  __TEXT.__swift5_typeref: 0x136
+  __TEXT.__swift5_capture: 0x1d0
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x4c
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0x830
+  __TEXT.__objc_classname: 0x18c
+  __TEXT.__objc_methname: 0x281c
+  __TEXT.__objc_methtype: 0x702
+  __TEXT.__objc_stubs: 0x16e0
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x470
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x748
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH_CONST.__const: 0x1a8
-  __AUTH_CONST.__cfstring: 0xba0
-  __AUTH_CONST.__objc_const: 0x10c0
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__const: 0x4c8
+  __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__objc_const: 0x1770
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x2d0
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0xd8
+  __DATA.__data: 0x2e8
   __DATA.__bss: 0x68
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E00E6B7-4E48-3D65-A272-92E2118F0001
-  Functions: 238
-  Symbols:   977
-  CStrings:  646
+  UUID: 7AF26A28-0EBC-3B94-B2AC-D3115D1E0370
+  Functions: 420
+  Symbols:   1248
+  CStrings:  862
 
Symbols:
+ +[APAskToAgeRestrictionMetadata supportsSecureCoding]
+ +[APRequestHandler addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:metadata:withCompletion:]
+ +[APRequestHandler localApproveExceptionWithUniqueIdentifier:completionHandler:]
+ -[APAskToAgeRestrictionMetadata .cxx_destruct]
+ -[APAskToAgeRestrictionMetadata accountID]
+ -[APAskToAgeRestrictionMetadata ageRatingString]
+ -[APAskToAgeRestrictionMetadata allowAccountPrompt]
+ -[APAskToAgeRestrictionMetadata appBundleID]
+ -[APAskToAgeRestrictionMetadata appItemID]
+ -[APAskToAgeRestrictionMetadata appName]
+ -[APAskToAgeRestrictionMetadata appShareURL]
+ -[APAskToAgeRestrictionMetadata appVersionID]
+ -[APAskToAgeRestrictionMetadata askerName]
+ -[APAskToAgeRestrictionMetadata authenticationContextData]
+ -[APAskToAgeRestrictionMetadata clientID]
+ -[APAskToAgeRestrictionMetadata compile]
+ -[APAskToAgeRestrictionMetadata copyWithZone:]
+ -[APAskToAgeRestrictionMetadata developerID]
+ -[APAskToAgeRestrictionMetadata developerName]
+ -[APAskToAgeRestrictionMetadata developerSupportURL]
+ -[APAskToAgeRestrictionMetadata distributorBundleID]
+ -[APAskToAgeRestrictionMetadata distributorDomain]
+ -[APAskToAgeRestrictionMetadata distributorID]
+ -[APAskToAgeRestrictionMetadata distributorIconURL]
+ -[APAskToAgeRestrictionMetadata distributorName]
+ -[APAskToAgeRestrictionMetadata distributorType]
+ -[APAskToAgeRestrictionMetadata encodeWithCoder:]
+ -[APAskToAgeRestrictionMetadata initWithCoder:]
+ -[APAskToAgeRestrictionMetadata initWithDictionary:]
+ -[APAskToAgeRestrictionMetadata installTypeRawValue]
+ -[APAskToAgeRestrictionMetadata installVerificationToken]
+ -[APAskToAgeRestrictionMetadata isDistributor]
+ -[APAskToAgeRestrictionMetadata isWebApp]
+ -[APAskToAgeRestrictionMetadata itemIDFromButtonConfiguration]
+ -[APAskToAgeRestrictionMetadata oAuthToken]
+ -[APAskToAgeRestrictionMetadata originallyRequestedVersionID]
+ -[APAskToAgeRestrictionMetadata referrer]
+ -[APAskToAgeRestrictionMetadata requestedAppIconURL]
+ -[APAskToAgeRestrictionMetadata setAccountID:]
+ -[APAskToAgeRestrictionMetadata setAgeRatingString:]
+ -[APAskToAgeRestrictionMetadata setAllowAccountPrompt:]
+ -[APAskToAgeRestrictionMetadata setAppBundleID:]
+ -[APAskToAgeRestrictionMetadata setAppItemID:]
+ -[APAskToAgeRestrictionMetadata setAppName:]
+ -[APAskToAgeRestrictionMetadata setAppShareURL:]
+ -[APAskToAgeRestrictionMetadata setAppVersionID:]
+ -[APAskToAgeRestrictionMetadata setAskerName:]
+ -[APAskToAgeRestrictionMetadata setAuthenticationContextData:]
+ -[APAskToAgeRestrictionMetadata setClientID:]
+ -[APAskToAgeRestrictionMetadata setDeveloperID:]
+ -[APAskToAgeRestrictionMetadata setDeveloperName:]
+ -[APAskToAgeRestrictionMetadata setDeveloperSupportURL:]
+ -[APAskToAgeRestrictionMetadata setDistributorBundleID:]
+ -[APAskToAgeRestrictionMetadata setDistributorDomain:]
+ -[APAskToAgeRestrictionMetadata setDistributorID:]
+ -[APAskToAgeRestrictionMetadata setDistributorIconURL:]
+ -[APAskToAgeRestrictionMetadata setDistributorName:]
+ -[APAskToAgeRestrictionMetadata setDistributorType:]
+ -[APAskToAgeRestrictionMetadata setInstallTypeRawValue:]
+ -[APAskToAgeRestrictionMetadata setInstallVerificationToken:]
+ -[APAskToAgeRestrictionMetadata setIsDistributor:]
+ -[APAskToAgeRestrictionMetadata setIsWebApp:]
+ -[APAskToAgeRestrictionMetadata setItemIDFromButtonConfiguration:]
+ -[APAskToAgeRestrictionMetadata setOAuthToken:]
+ -[APAskToAgeRestrictionMetadata setOriginallyRequestedVersionID:]
+ -[APAskToAgeRestrictionMetadata setReferrer:]
+ -[APAskToAgeRestrictionMetadata setRequestedAppIconURL:]
+ -[APAskToAgeRestrictionMetadata setUrl:]
+ -[APAskToAgeRestrictionMetadata setUserInitiatedOverride:]
+ -[APAskToAgeRestrictionMetadata url]
+ -[APAskToAgeRestrictionMetadata userInitiatedOverride]
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table26
+ _AMSSetLogKeyIfNeeded
+ _OBJC_CLASS_$_APAskToAgeRestrictionMetadata
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._accountID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._ageRatingString
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._allowAccountPrompt
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._appBundleID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._appItemID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._appName
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._appShareURL
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._appVersionID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._askerName
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._authenticationContextData
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._clientID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._developerID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._developerName
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._developerSupportURL
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._distributorBundleID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._distributorDomain
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._distributorID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._distributorIconURL
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._distributorName
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._distributorType
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._installTypeRawValue
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._installVerificationToken
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._isDistributor
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._isWebApp
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._itemIDFromButtonConfiguration
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._oAuthToken
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._originallyRequestedVersionID
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._referrer
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._requestedAppIconURL
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._url
+ _OBJC_IVAR_$_APAskToAgeRestrictionMetadata._userInitiatedOverride
+ _OBJC_METACLASS_$_APAskToAgeRestrictionMetadata
+ __CATEGORY_CLASS_METHODS_STExceptionApp_$_AskPermission
+ __OBJC_$_CLASS_METHODS_APAskToAgeRestrictionMetadata
+ __OBJC_$_CLASS_PROP_LIST_APAskToAgeRestrictionMetadata
+ __OBJC_$_INSTANCE_METHODS_APAskToAgeRestrictionMetadata
+ __OBJC_$_INSTANCE_VARIABLES_APAskToAgeRestrictionMetadata
+ __OBJC_$_PROP_LIST_APAskToAgeRestrictionMetadata
+ __OBJC_CLASS_PROTOCOLS_$_APAskToAgeRestrictionMetadata
+ __OBJC_CLASS_RO_$_APAskToAgeRestrictionMetadata
+ __OBJC_METACLASS_RO_$_APAskToAgeRestrictionMetadata
+ ___215+[APRequestHandler addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:metadata:withCompletion:]_block_invoke
+ ___44-[APConnectionNotifier _newRemoteConnection]_block_invoke.91
+ _block_copy_helper.102
+ _block_copy_helper.111
+ _block_copy_helper.116
+ _block_copy_helper.125
+ _block_copy_helper.135
+ _block_copy_helper.89
+ _block_copy_helper.97
+ _block_descriptor.104
+ _block_descriptor.113
+ _block_descriptor.118
+ _block_descriptor.127
+ _block_descriptor.137
+ _block_descriptor.91
+ _block_descriptor.99
+ _block_destroy_helper.103
+ _block_destroy_helper.112
+ _block_destroy_helper.117
+ _block_destroy_helper.126
+ _block_destroy_helper.136
+ _block_destroy_helper.90
+ _block_destroy_helper.98
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$absoluteString
+ _objc_msgSend$accountID
+ _objc_msgSend$addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:metadata:withCompletion:
+ _objc_msgSend$ageRatingString
+ _objc_msgSend$allowAccountPrompt
+ _objc_msgSend$appBundleID
+ _objc_msgSend$appItemID
+ _objc_msgSend$appName
+ _objc_msgSend$appShareURL
+ _objc_msgSend$appVersionID
+ _objc_msgSend$askerName
+ _objc_msgSend$authenticationContextData
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$clientID
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$developerID
+ _objc_msgSend$developerName
+ _objc_msgSend$developerSupportURL
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$distributorBundleID
+ _objc_msgSend$distributorDomain
+ _objc_msgSend$distributorID
+ _objc_msgSend$distributorIconURL
+ _objc_msgSend$distributorName
+ _objc_msgSend$distributorType
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$installTypeRawValue
+ _objc_msgSend$installVerificationToken
+ _objc_msgSend$isDistributor
+ _objc_msgSend$isWebApp
+ _objc_msgSend$itemIDFromButtonConfiguration
+ _objc_msgSend$localApproveExceptionWithUniqueIdentifier:completionHandler:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$oAuthToken
+ _objc_msgSend$originallyRequestedVersionID
+ _objc_msgSend$referrer
+ _objc_msgSend$requestedAppIconURL
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$url
+ _objc_msgSend$userInitiatedOverride
+ _objectdestroy.11Tm
+ _objectdestroy.87Tm
+ _objectdestroyTm
+ _symbolic SaySo14STExceptionAppCG
+ _symbolic ScCySaySo14STExceptionAppCG______pG s5ErrorP
+ _symbolic ScCySb______pG s5ErrorP
+ _symbolic So14STExceptionAppCXMT
+ _symbolic So14STExceptionAppCXMo
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
+ _symbolic So8NSNumberC
+ _symbolic _____ s6UInt64V
- +[APRequestHandler addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:]
- GCC_except_table18
- GCC_except_table20
- GCC_except_table22
- GCC_except_table25
- ___217+[APRequestHandler addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:]_block_invoke
- ___44-[APConnectionNotifier _newRemoteConnection]_block_invoke.89
- _block_copy_helper.4
- _block_descriptor.6
- _block_destroy_helper.5
- _objc_msgSend$addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:
- _objectdestroy.13Tm
- _symbolic ScCyyt______pG s5ErrorP
CStrings:
+ "%{public}@: Performing Local Approval for UniqueID: %@"
+ "@\"NSData\""
+ "@\"NSURL\""
+ "APAskToAgeRestrictionMetadata"
+ "Deleting exception: "
+ "Error deleting exceptions:"
+ "Error fetching exceptions:"
+ "Fetching exceptions for DSID: "
+ "T@\"NSData\",&,N,V_authenticationContextData"
+ "T@\"NSString\",&,N,V_accountID"
+ "T@\"NSString\",&,N,V_ageRatingString"
+ "T@\"NSString\",&,N,V_appBundleID"
+ "T@\"NSString\",&,N,V_appName"
+ "T@\"NSString\",&,N,V_askerName"
+ "T@\"NSString\",&,N,V_clientID"
+ "T@\"NSString\",&,N,V_developerID"
+ "T@\"NSString\",&,N,V_developerName"
+ "T@\"NSString\",&,N,V_distributorBundleID"
+ "T@\"NSString\",&,N,V_distributorDomain"
+ "T@\"NSString\",&,N,V_distributorID"
+ "T@\"NSString\",&,N,V_distributorName"
+ "T@\"NSString\",&,N,V_distributorType"
+ "T@\"NSString\",&,N,V_installTypeRawValue"
+ "T@\"NSString\",&,N,V_installVerificationToken"
+ "T@\"NSString\",&,N,V_oAuthToken"
+ "T@\"NSURL\",&,N,V_appShareURL"
+ "T@\"NSURL\",&,N,V_developerSupportURL"
+ "T@\"NSURL\",&,N,V_distributorIconURL"
+ "T@\"NSURL\",&,N,V_referrer"
+ "T@\"NSURL\",&,N,V_requestedAppIconURL"
+ "T@\"NSURL\",&,N,V_url"
+ "TB,N,V_allowAccountPrompt"
+ "TB,N,V_isDistributor"
+ "TB,N,V_isWebApp"
+ "TB,N,V_userInitiatedOverride"
+ "TQ,N,V_appItemID"
+ "TQ,N,V_appVersionID"
+ "TQ,N,V_itemIDFromButtonConfiguration"
+ "TQ,N,V_originallyRequestedVersionID"
+ "URLWithString:"
+ "_accountID"
+ "_ageRatingString"
+ "_allowAccountPrompt"
+ "_appBundleID"
+ "_appItemID"
+ "_appName"
+ "_appShareURL"
+ "_appVersionID"
+ "_askerName"
+ "_authenticationContextData"
+ "_clientID"
+ "_developerID"
+ "_developerName"
+ "_developerSupportURL"
+ "_distributorBundleID"
+ "_distributorDomain"
+ "_distributorID"
+ "_distributorIconURL"
+ "_distributorName"
+ "_distributorType"
+ "_installTypeRawValue"
+ "_installVerificationToken"
+ "_isDistributor"
+ "_isWebApp"
+ "_itemIDFromButtonConfiguration"
+ "_oAuthToken"
+ "_originallyRequestedVersionID"
+ "_referrer"
+ "_requestedAppIconURL"
+ "_url"
+ "_userInitiatedOverride"
+ "absoluteString"
+ "accountID"
+ "addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:metadata:withCompletion:"
+ "ageRatingString"
+ "allowAccountPrompt"
+ "appBundleID"
+ "appItemID"
+ "appName"
+ "appShareURL"
+ "appVersionID"
+ "askerName"
+ "authenticationContextData"
+ "base64EncodedStringWithOptions:"
+ "clientID"
+ "decodeBoolForKey:"
+ "decodeInt64ForKey:"
+ "decodeObjectOfClass:forKey:"
+ "deleteException(_:)"
+ "deleteException:completionHandler:"
+ "deleteExceptionFor:completionHandler:"
+ "developerID"
+ "developerName"
+ "developerSupportURL"
+ "dictionaryWithDictionary:"
+ "distributorBundleID"
+ "distributorDomain"
+ "distributorID"
+ "distributorIconURL"
+ "distributorName"
+ "distributorType"
+ "encodeBool:forKey:"
+ "encodeInt64:forKey:"
+ "encodeObject:forKey:"
+ "fetchAllAppExceptionsForRequesterDSID:completionHandler:"
+ "fetchExceptionsForRequesterDSID:adamID:completionHandler:"
+ "fetchExceptionsForRequesterDSID:completionHandler:"
+ "initWithBase64EncodedString:options:"
+ "installTypeRawValue"
+ "installVerificationToken"
+ "isDistributor"
+ "isWebApp"
+ "itemIDFromButtonConfiguration"
+ "localApproveExceptionWithUniqueIdentifier:completionHandler:"
+ "numberWithUnsignedLongLong:"
+ "oAuthToken"
+ "originallyRequestedVersionID"
+ "referrer"
+ "requestedAppIconURL"
+ "setAccountID:"
+ "setAgeRatingString:"
+ "setAllowAccountPrompt:"
+ "setAppBundleID:"
+ "setAppItemID:"
+ "setAppName:"
+ "setAppShareURL:"
+ "setAppVersionID:"
+ "setAskerName:"
+ "setAuthenticationContextData:"
+ "setClientID:"
+ "setDeveloperID:"
+ "setDeveloperName:"
+ "setDeveloperSupportURL:"
+ "setDistributorBundleID:"
+ "setDistributorDomain:"
+ "setDistributorID:"
+ "setDistributorIconURL:"
+ "setDistributorName:"
+ "setDistributorType:"
+ "setInstallTypeRawValue:"
+ "setInstallVerificationToken:"
+ "setIsDistributor:"
+ "setIsWebApp:"
+ "setItemIDFromButtonConfiguration:"
+ "setOAuthToken:"
+ "setOriginallyRequestedVersionID:"
+ "setReferrer:"
+ "setRequestedAppIconURL:"
+ "setUrl:"
+ "setUserInitiatedOverride:"
+ "unsignedLongLongValue"
+ "userInitiatedOverride"
+ "v136@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSNumber\"56@\"NSString\"64@\"NSNumber\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSString\"112@\"APAskToAgeRestrictionMetadata\"120@?<v@?B@\"NSError\">128"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"STExceptionApp\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSNumber\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:"
- "v136@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSNumber\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSString\"112@\"NSData\"120@?<v@?B@\"NSError\">128"

```
