## AutoFillCore

> `/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore`

```diff

-39.0.0.0.0
-  __TEXT.__text: 0xa364
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x4fc
+41.0.0.0.0
+  __TEXT.__text: 0x9c2c
+  __TEXT.__objc_methlist: 0x514
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x170f
-  __TEXT.__gcc_except_tab: 0x594
+  __TEXT.__cstring: 0x173d
+  __TEXT.__gcc_except_tab: 0x44c
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x34a
-  __TEXT.__unwind_info: 0x370
-  __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0x1bca
-  __TEXT.__objc_methtype: 0x3b4
-  __TEXT.__objc_stubs: 0x1560
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x318
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x1100
-  __AUTH_CONST.__objc_const: 0x828
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_const: 0x830
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xd0
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x158
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6853AA5-8F23-3190-BB5D-99A639F140DD
-  Functions: 227
-  Symbols:   1004
-  CStrings:  643
+  UUID: BD07CFC4-2D72-3B81-BF05-AB928C6989D4
+  Functions: 228
+  Symbols:   1003
+  CStrings:  339
 
Symbols:
+ -[AFCredentialManager oneTimeCodeProviderDeliveredCodesDidChange:]
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:]
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:].cold.1
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:].cold.2
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:completionHandler:]
+ ___162-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:]_block_invoke
+ ___162-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:]_block_invoke_2
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:
+ _objc_msgSend$authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:completionHandler:
+ _objc_msgSend$initWithExternalizedContext:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x9
- -[AFCredentialManager oneTimeCodeProviderReceivedCode:]
- -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:].cold.1
- -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:].cold.2
- GCC_except_table27
- GCC_except_table55
- GCC_except_table87
- GCC_except_table88
- GCC_except_table89
- GCC_except_table94
- GCC_except_table95
- GCC_except_table96
- _OUTLINED_FUNCTION_9
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFAppAutoFillOneTimeCodeProviderObserver
- ___125-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]_block_invoke
- ___125-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]_block_invoke_2
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:externalizedContext:callerAuditToken:completionHandler:]"
- "#16@0:8"
- "-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]"
- ".cxx_destruct"
- "@\"<_ICPredictionManaging>\""
- "@\"AFLocalizationManager\""
- "@\"LAContext\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SFAppAutoFillOneTimeCodeProvider\""
- "@\"SFAppAutoFillPasskeyProvider\""
- "@104@0:8@16@24@32@40@48^{CGImage=}56^{CGImage=}64@72@80@88Q96"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@48@0:8@16@24@32Q40"
- "@56@0:8@16@24@32@40Q48"
- "@64@0:8@16@24@32^{CGImage=}40^{CGImage=}48Q56"
- "@88@0:8@16@24@32^{CGImage=}40^{CGImage=}48@56@64@72Q80"
- "AFInsertionManager"
- "AFSuggestion"
- "AFSuggestionGenerationManager"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "NSObject"
- "Q16@0:8"
- "SFAppAutoFillOneTimeCodeProviderObserver"
- "T#,R"
- "T@\"AFLocalizationManager\",R,N,V_localizationManager"
- "T@\"LAContext\",&,N,V_laContext"
- "T@\"NSDictionary\",&,N,V_queuedCustomInfo"
- "T@\"NSDictionary\",&,N,V_queuedUnauthenticatedCustomInfo"
- "T@\"NSDictionary\",R,N,V_creditCardPayload"
- "T@\"NSDictionary\",R,N,V_oneTimeCodePayload"
- "T@\"NSDictionary\",R,N,V_usernameAndPasswordPayload"
- "T@\"NSString\",&,N,V_localeIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_altDSID"
- "T@\"NSString\",R,N,V_applicationBundleId"
- "T@\"NSString\",R,N,V_applicationKey"
- "T@\"NSString\",R,N,V_subTitle"
- "T@\"NSString\",R,N,V_title"
- "TQ,R"
- "TQ,R,N,V_customInfoType"
- "T^{CGImage=},R,N,V_leadingImage"
- "T^{CGImage=},R,N,V_trailingImage"
- "UUIDString"
- "Vv16@0:8"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_altDSID"
- "_applicationBundleId"
- "_applicationKey"
- "_autoFillPayloadForPasskey:customInfoType:"
- "_autoFillPayloadForPasswordCredential:customInfoType:"
- "_consumeOneTimeCodeAutoFillSuggestionIfNeeded:"
- "_creditCardPayload"
- "_customInfoType"
- "_deviceLanguage"
- "_inputContextPredictionManager"
- "_laContext"
- "_leadingImage"
- "_localeIdentifier"
- "_localizationManager"
- "_makeQueue"
- "_oneTimeCodePayload"
- "_oneTimeCodeProvider"
- "_passkeyProvider"
- "_queue"
- "_queuedCustomInfo"
- "_queuedUnauthenticatedCustomInfo"
- "_subTitle"
- "_suggestionForPasskey:autoFillPayload:customInfoType:"
- "_suggestionForPasswordCredential:autoFillPayload:customInfoType:"
- "_title"
- "_trailingImage"
- "_truncationSentinel"
- "_usernameAndPasswordPayload"
- "accessibilityLabelForAFTextContentType:"
- "accessibilityLabelsForSecureHeaders:secureContents:truncationSentinel:"
- "activeFPANCardsWithOptions:allowedCardTypes:completion:"
- "addObject:"
- "addObserver:"
- "altDSID"
- "altDSIDForAccount:"
- "appId"
- "applicationBundleId"
- "applicationKey"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "artwork"
- "associatedDomains"
- "auditToken"
- "authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:"
- "authenticateIfNecessaryForSuggestion:completionHandler:"
- "authenticateIfNecessaryForSuggestion:documentTraits:completionHandler:"
- "authenticateIfNecessaryForSuggestion:documentTraits:withCompletionHandler:"
- "autofillContext"
- "autofillSubMode"
- "autorelease"
- "bestDomainForAppID:completionHandler:"
- "boolValue"
- "bundleForClass:"
- "bundleId"
- "bundleIdentifier"
- "canEvaluatePolicy:error:"
- "canUse"
- "cardNickname"
- "cardholderName"
- "class"
- "conformsToProtocol:"
- "consumeOneTimeCode:"
- "containsObject:"
- "containsString:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creationDate"
- "credentialForFPANCard:authorization:options:merchantHost:completion:"
- "credentialType"
- "creditCardPayload"
- "currentConnection"
- "currentLocale"
- "currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:"
- "customInfoType"
- "date"
- "debugDescription"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "displayableLastFour"
- "domain"
- "effectiveBoolValueForSetting:"
- "enumerateObjectsUsingBlock:"
- "evaluatePolicy:options:reply:"
- "expirationDate"
- "externalizedContext"
- "firstObject"
- "flags"
- "generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:"
- "generateContactAutoFillSuggestionsWithTextPrefix:documentTraits:completionHandler:"
- "generateCreditCardAutoFillWithCompletionHandler:externalizedContext:"
- "generateHideMyEmailAutoFillWithRenderTraits:completionHandler:"
- "generateHideMyEmailSuggestionWithApplicationBundleId:applicationId:completionHandler:"
- "generateLoginAutoFillWithDocumentTraits:"
- "generateOneTimeCodeAutoFillSuggestionsWithDocumentTraits:completionHandler:"
- "generateSignupAutoFillWithAutoFillMode:documentTraits:completionHandler:"
- "generateSuggestionsForContactAutoFill:textPrefix:"
- "getApprovedSharedWebCredentialsEntriesForAppWithAppID:completionHandler:"
- "getAvailablePasskeysForApplicationIdentifier:completionHandler:"
- "getCredentialsForAppWithAppID:completionHandler:"
- "getCredentialsForAppWithAppID:externallyVerifiedAndApprovedSharedWebCredentialDomains:completionHandler:"
- "getCredentialsForAppWithAppID:websiteURL:completionHandler:"
- "getCredentialsWithApplicationIdentifier:documentTraits:withCompletionHandler:"
- "hasAutoFillContextEntitlementForConnection:"
- "hasPrefix:"
- "hash"
- "identifier"
- "init"
- "initForLocalizedStrings"
- "initPrivate"
- "initWithArray:"
- "initWithContext:inputContextHistory:contentType:"
- "initWithKey:altDSID:clientAppBundleId:"
- "initWithLocaleIdentifier:"
- "initWithTitle:applicationKey:applicationBundleId:altDSID:customInfoType:"
- "initWithTitle:subTitle:creditCardPayload:customInfoType:"
- "initWithTitle:subTitle:usernameAndPasswordPayload:creditCardPayload:oneTimeCodePayload:leadingImage:trailingImage:applicationKey:applicationBundleId:altDSID:customInfoType:"
- "initWithTitle:subTitle:usernameAndPasswordPayload:leadingImage:trailingImage:applicationKey:applicationBundleId:altDSID:customInfoType:"
- "initWithTitle:subTitle:usernameAndPasswordPayload:leadingImage:trailingImage:customInfoType:"
- "initWithTitle:subtitle:oneTimeCodePayload:customInfoType:"
- "initWithUUIDBytes:"
- "inputContextPredictionManager"
- "isEqual:"
- "isEqualToString:"
- "isExternal"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyboardType"
- "laContext"
- "label"
- "leadingImage"
- "length"
- "localeIdentifier"
- "localizationManager"
- "localizedDescription"
- "localizedStringForKey:"
- "localizedStringForKey:value:table:"
- "localizedStringForKey:value:table:localization:"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "localizedSubtitleForContext:"
- "localizedTitleForContext:"
- "lookupPrivateEmailWithContext:completion:"
- "mainBundle"
- "mutableCopy"
- "needContactAutofill:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "obtainApplicationIdentifierFromConnection:"
- "obtainBundleIdentifierFromConnection:"
- "oneTimeCodePayload"
- "oneTimeCodeProvider"
- "oneTimeCodeProvider:didUpdateOneTimeCode:"
- "oneTimeCodeProviderReceivedCode:"
- "operationData"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:"
- "predictionManager"
- "preferredInsertionOrder"
- "preferredLocalizations"
- "preferredLocalizationsFromArray:forPreferences:"
- "primaryAccountNumber"
- "primaryAuthKitAccount"
- "privateEmailAddress"
- "processId"
- "queuedCustomInfo"
- "queuedUnauthenticatedCustomInfo"
- "recipientId"
- "release"
- "relyingPartyIdentifier"
- "requestFeatureWithId:completion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "searchWithTriggers:application:recipient:localeIdentifier:isResponseDenyListed:shouldDisableAutoCaps:timeoutInMilliseconds:resultLimit:error:"
- "securityCode"
- "self"
- "setLaContext:"
- "setLocaleIdentifier:"
- "setObject:forKey:"
- "setQueuedCustomInfo:"
- "setQueuedUnauthenticatedCustomInfo:"
- "setWithArray:"
- "setWithObjects:"
- "sharedConnection"
- "sharedFeatureManager"
- "sharedInstance"
- "sharedProvider"
- "shouldAcceptAutoFill:withPayload:documentTraits:completionHandler:"
- "shouldAcceptSuggestion:completionHandler:"
- "shouldAggregate"
- "shouldAuthenticateToAcceptAutoFill"
- "shouldAutoFillPasswords"
- "site"
- "source"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithValidatedFormat:validFormatSpecifiers:error:"
- "subTitle"
- "subarrayWithRange:"
- "suggestedUsersOfType:completionHandler:"
- "superclass"
- "textContentType"
- "textInputTraits"
- "textSuggestionHeaderForExternalCredential:"
- "timeIntervalSinceNow"
- "title"
- "trailingImage"
- "user"
- "userSelectedPasskey:authenticatedLAContext:"
- "usernameAndPasswordPayload"
- "v16@0:8"
- "v24@0:8@\"SFAppAutoFillOneTimeCodeProvider\"16"
- "v24@0:8@16"
- "v32@0:8@\"SFAppAutoFillOneTimeCodeProvider\"16@\"SFAutoFillOneTimeCode\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@24"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@16@24@32@?40"
- "v56@0:8Q16@24@32@40@?48"
- "value"
- "zone"

```
