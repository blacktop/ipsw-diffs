## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

-1104.120.3.0.0
-  __TEXT.__text: 0x9b298
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0x27f4
-  __TEXT.__cstring: 0x1f092
-  __TEXT.__const: 0x6416
+1104.120.3.0.1
+  __TEXT.__text: 0x9d4f4
+  __TEXT.__auth_stubs: 0x19f0
+  __TEXT.__objc_methlist: 0x2a64
+  __TEXT.__cstring: 0x1f980
+  __TEXT.__const: 0x6446
+  __TEXT.__gcc_except_tab: 0x3710
+  __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0x53c
-  __TEXT.__gcc_except_tab: 0x365c
-  __TEXT.__unwind_info: 0x2850
-  __TEXT.__objc_classname: 0x8a8
-  __TEXT.__objc_methname: 0x2923
-  __TEXT.__objc_methtype: 0x776
-  __TEXT.__objc_stubs: 0x23a0
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x2df0
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__unwind_info: 0x2910
+  __TEXT.__objc_classname: 0x8f6
+  __TEXT.__objc_methname: 0x2fb8
+  __TEXT.__objc_methtype: 0x952
+  __TEXT.__objc_stubs: 0x2900
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x2f48
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb68
+  __DATA_CONST.__objc_selrefs: 0xd70
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xca8
-  __AUTH_CONST.__const: 0x1498
-  __AUTH_CONST.__cfstring: 0xee80
-  __AUTH_CONST.__objc_const: 0x4c18
+  __AUTH_CONST.__auth_got: 0xd10
+  __AUTH_CONST.__const: 0x1578
+  __AUTH_CONST.__cfstring: 0xf400
+  __AUTH_CONST.__objc_const: 0x4fd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x1400
+  __AUTH.__objc_data: 0x1450
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0x328
-  __DATA.__data: 0x928
-  __DATA.__bss: 0xd88
+  __DATA.__objc_ivar: 0x34c
+  __DATA.__data: 0x9e8
+  __DATA.__bss: 0xdb0
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 701E9080-6C34-3329-B880-C7E21F22102C
-  Functions: 3556
-  Symbols:   10025
-  CStrings:  7306
+  UUID: 72AD0F86-7286-3EEA-BE5D-A0803E34013F
+  Functions: 3612
+  Symbols:   10249
+  CStrings:  7533
 
Symbols:
+ -[AMAuthInstallOSSsoAuthenticator .cxx_destruct]
+ -[AMAuthInstallOSSsoAuthenticator authenticate]
+ -[AMAuthInstallOSSsoAuthenticator authenticationController]
+ -[AMAuthInstallOSSsoAuthenticator authenticationURL]
+ -[AMAuthInstallOSSsoAuthenticator authorizationController:didCompleteWithAuthorization:]
+ -[AMAuthInstallOSSsoAuthenticator authorizationController:didCompleteWithError:]
+ -[AMAuthInstallOSSsoAuthenticator authorizationController:shouldRetryAfterError:]
+ -[AMAuthInstallOSSsoAuthenticator completionHandler]
+ -[AMAuthInstallOSSsoAuthenticator flags]
+ -[AMAuthInstallOSSsoAuthenticator queryItemsWithParameters:]
+ -[AMAuthInstallOSSsoAuthenticator service]
+ -[AMAuthInstallOSSsoAuthenticator setAuthenticationController:]
+ -[AMAuthInstallOSSsoAuthenticator setCompletionHandler:]
+ -[AMAuthInstallOSSsoAuthenticator setFlags:]
+ -[AMAuthInstallOSSsoAuthenticator setService:]
+ -[AMAuthInstallOSSsoAuthenticator setSsoEnv:]
+ -[AMAuthInstallOSSsoAuthenticator setSsoHost:]
+ -[AMAuthInstallOSSsoAuthenticator setSsoRealm:]
+ -[AMAuthInstallOSSsoAuthenticator setStealthMode:]
+ -[AMAuthInstallOSSsoAuthenticator setUseLegacyAuthURL:]
+ -[AMAuthInstallOSSsoAuthenticator ssoEnv]
+ -[AMAuthInstallOSSsoAuthenticator ssoHost]
+ -[AMAuthInstallOSSsoAuthenticator ssoRealm]
+ -[AMAuthInstallOSSsoAuthenticator stealthMode]
+ -[AMAuthInstallOSSsoAuthenticator useLegacyAuthURL]
+ GCC_except_table39
+ _AMAuthInstallSsoCreateToken
+ _AMAuthInstallSsoCreateToken.cold.1
+ _AMAuthInstallSsoCreateToken.cold.2
+ _AuthenticationServicesLibrary
+ _AuthenticationServicesLibrary.cold.1
+ _AuthenticationServicesLibraryCore.frameworkLibrary
+ _CFRunLoopAddSource
+ _CFRunLoopGetCurrent
+ _CFRunLoopRemoveSource
+ _CFRunLoopRun
+ _CFRunLoopSourceCreate
+ _CFRunLoopSourceInvalidate
+ _CFRunLoopSourceSignal
+ _CFRunLoopStop
+ _CFRunLoopWakeUp
+ _NSClassFromString
+ _OBJC_CLASS_$_AMAuthInstallOSSsoAuthenticator
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._authenticationController
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._completionHandler
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._flags
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._service
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._ssoEnv
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._ssoHost
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._ssoRealm
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._stealthMode
+ _OBJC_IVAR_$_AMAuthInstallOSSsoAuthenticator._useLegacyAuthURL
+ _OBJC_METACLASS_$_AMAuthInstallOSSsoAuthenticator
+ __AMAuthInstallSsoAuthSvcsCreateServiceTicketWithAppId
+ __OBJC_$_INSTANCE_METHODS_AMAuthInstallOSSsoAuthenticator
+ __OBJC_$_INSTANCE_VARIABLES_AMAuthInstallOSSsoAuthenticator
+ __OBJC_$_PROP_LIST_AMAuthInstallOSSsoAuthenticator
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ASAuthorizationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASAuthorizationControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_ASAuthorizationControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AMAuthInstallOSSsoAuthenticator
+ __OBJC_CLASS_RO_$_AMAuthInstallOSSsoAuthenticator
+ __OBJC_LABEL_PROTOCOL_$_ASAuthorizationControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_AMAuthInstallOSSsoAuthenticator
+ __OBJC_PROTOCOL_$_ASAuthorizationControllerDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ __StopRunLoopPerform
+ __StopRunLoopPerform.cold.1
+ ___60-[AMAuthInstallOSSsoAuthenticator queryItemsWithParameters:]_block_invoke
+ ___60-[AMAuthInstallOSSsoAuthenticator queryItemsWithParameters:]_block_invoke_2
+ ___AuthenticationServicesLibraryCore_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____AMAuthInstallSsoAuthSvcsCreateServiceTicketWithAppId_block_invoke
+ ____AMAuthInstallSsoAuthSvcsCreateServiceTicketWithAppId_block_invoke_2
+ ___block_descriptor_32_e50_v32?0"NSMutableArray"8"NSString"16"NSString"24l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e31_v32?0"NSURLQueryItem"8Q16^B24l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e35_v32?0"NSString"8"NSString"16^B24l
+ ___block_descriptor_80_e8_32r40r48r56r_e34_v24?0"NSDictionary"8"NSError"16l
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32r40r48r56r
+ ___copy_helper_block_e8_32s40b
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32r40r48r56r
+ ___getASAuthorizationControllerClass_block_invoke
+ ___getASAuthorizationControllerClass_block_invoke.cold.1
+ ___getASAuthorizationErrorDomainSymbolLoc_block_invoke
+ ___getASAuthorizationSingleSignOnCredentialClass_block_invoke
+ ___getASAuthorizationSingleSignOnCredentialClass_block_invoke.cold.1
+ ___getASAuthorizationSingleSignOnProviderClass_block_invoke
+ ___getASAuthorizationSingleSignOnProviderClass_block_invoke.cold.1
+ __kAMAuthInstallKnownSsoService1205
+ __kAMAuthInstallKnownSsoService171383
+ __kAMAuthInstallKnownSsoService172489
+ __kAMAuthInstallKnownSsoService20
+ __kAMAuthInstallKnownSsoService761
+ __kAMAuthInstallKnownSsoService901793
+ __sl_dlopen
+ _audit_stringAuthenticationServices
+ _getASAuthorizationControllerClass.softClass
+ _getASAuthorizationErrorDomain
+ _getASAuthorizationErrorDomain.cold.1
+ _getASAuthorizationErrorDomainSymbolLoc.ptr
+ _getASAuthorizationSingleSignOnCredentialClass.softClass
+ _getASAuthorizationSingleSignOnProviderClass.softClass
+ _kAMAuthInstallSsoTokenInfoPersonID
+ _kAMAuthInstallSsoTokenInfoUsername
+ _objc_getClass
+ _objc_msgSend$allHeaderFields
+ _objc_msgSend$authenticate
+ _objc_msgSend$authenticatedResponse
+ _objc_msgSend$authenticationController
+ _objc_msgSend$authenticationURL
+ _objc_msgSend$authorizationController:shouldRetryAfterError:
+ _objc_msgSend$authorizationProviderWithIdentityProviderURL:
+ _objc_msgSend$canPerformAuthorization
+ _objc_msgSend$completionHandler
+ _objc_msgSend$createRequest
+ _objc_msgSend$credential
+ _objc_msgSend$currentHandler
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$flags
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$initWithAuthorizationRequests:
+ _objc_msgSend$name
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$percentEncodedQuery
+ _objc_msgSend$performRequests
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$queryItems
+ _objc_msgSend$queryItemsWithParameters:
+ _objc_msgSend$service
+ _objc_msgSend$setAuthenticationController:
+ _objc_msgSend$setAuthorizationOptions:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setFlags:
+ _objc_msgSend$setQuery:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setService:
+ _objc_msgSend$setSsoHost:
+ _objc_msgSend$setSsoRealm:
+ _objc_msgSend$setStealthMode:
+ _objc_msgSend$setUseLegacyAuthURL:
+ _objc_msgSend$setUserInterfaceEnabled:
+ _objc_msgSend$ssoHost
+ _objc_msgSend$ssoRealm
+ _objc_msgSend$stealthMode
+ _objc_msgSend$useLegacyAuthURL
+ _objc_msgSend$value
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "#16@0:8"
+ "%s: AppleConnect not supported on this platform."
+ "%s: Failed to fetch SSO token"
+ "%s: Requested ANY type, but UseSpecifiedTypesOnly is set."
+ "%s: service is NULL"
+ "-[AMAuthInstallOSSsoAuthenticator authenticate]"
+ "-[AMAuthInstallOSSsoAuthenticator authorizationController:didCompleteWithAuthorization:]"
+ "-[AMAuthInstallOSSsoAuthenticator authorizationController:didCompleteWithError:]"
+ "0"
+ "14640371804122341"
+ "15439634935985085"
+ "16305813941943436"
+ "16435966288656694"
+ "27503691874361152"
+ "@\"ASAuthorizationController\""
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "@?"
+ "@?16@0:8"
+ "AMAuthInstallOSSsoAuthenticator"
+ "AMAuthInstallSsoAuthSvcs.m"
+ "AMAuthInstallSsoCreateToken"
+ "AMAuthInstallSsoCreateToken() ACM token requested, status=%d."
+ "AMAuthInstallSsoCreateToken() DAW token requested, status=%d."
+ "AMAuthInstallSsoCreateToken() OIDC token requested, status=%d."
+ "APPLECONNECT.APPLE.COM"
+ "ASAuthorizationController"
+ "ASAuthorizationControllerDelegate"
+ "ASAuthorizationErrorDomain"
+ "ASAuthorizationSingleSignOnCredential"
+ "ASAuthorizationSingleSignOnProvider"
+ "AuthInstallSSOHost"
+ "AuthInstallSSORealm"
+ "Authentication completed: %@"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "Class getASAuthorizationControllerClass(void)_block_invoke"
+ "Class getASAuthorizationSingleSignOnCredentialClass(void)_block_invoke"
+ "Class getASAuthorizationSingleSignOnProviderClass(void)_block_invoke"
+ "DAWRequest"
+ "ERROR: Authentication completed with error: %@."
+ "ERROR: Can't authenticate with provider URL: %@."
+ "INFO: Authentication did complete with result: %@."
+ "NSErrorDomain getASAuthorizationErrorDomain(void)"
+ "NSObject"
+ "No type selected"
+ "PersonID"
+ "Provider cannot perform authorization"
+ "Response is nil"
+ "Retrying with Legacy URL..."
+ "SSOHost"
+ "SSORealm"
+ "T#,R"
+ "T@\"ASAuthorizationController\",&,N,V_authenticationController"
+ "T@\"NSString\",&,N,V_ssoEnv"
+ "T@\"NSString\",&,N,V_ssoHost"
+ "T@\"NSString\",&,N,V_ssoRealm"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@?,C,N,V_completionHandler"
+ "TB,N,V_stealthMode"
+ "TB,N,V_useLegacyAuthURL"
+ "TQ,N,V_flags"
+ "TQ,R"
+ "Tr^{?=IIQQ^{__CFString}^{__CFString}},N,V_service"
+ "Unable to find class %s"
+ "VinylRestore-146~951"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_AMAuthInstallSsoAuthSvcsCreateServiceTicketWithAppId"
+ "_AMAuthInstallSsoAuthSvcsCreateServiceTicketWithAppId_block_invoke"
+ "_StopRunLoopPerform"
+ "_authenticationController"
+ "_completionHandler"
+ "_flags"
+ "_service"
+ "_ssoEnv"
+ "_ssoHost"
+ "_ssoRealm"
+ "_stealthMode"
+ "_useLegacyAuthURL"
+ "allHeaderFields"
+ "applicationIdentifier"
+ "authenticate"
+ "authenticatedResponse"
+ "authenticationController"
+ "authenticationURL"
+ "authorizationController:didCompleteWithAuthorization:"
+ "authorizationController:didCompleteWithCustomMethod:"
+ "authorizationController:didCompleteWithError:"
+ "authorizationController:shouldRetryAfterError:"
+ "authorizationProviderWithIdentityProviderURL:"
+ "autorelease"
+ "canPerformAuthorization"
+ "class"
+ "completionHandler"
+ "conformsToProtocol:"
+ "credential"
+ "currentHandler"
+ "debugDescription"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumerateObjectsUsingBlock:"
+ "environmentIdentifier"
+ "flags"
+ "g54xhr7fct39kf7ahbkys1sjhoymlz"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "https://idmsac.apple.com/IDMSNativeAuth/authenticate"
+ "https://sso.corp.apple.com/authenticate"
+ "id_token"
+ "initWithAuthorizationRequests:"
+ "interactivity"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "jthopfdpkkcaukplnxjfmjn9kvdqof"
+ "libauthinstall_device-1104.120.3.0.1"
+ "name"
+ "numberFromString:"
+ "oauth-pkce"
+ "oauthClientID"
+ "oauthGrantType"
+ "oauthScope"
+ "openid,dsid"
+ "otherInfo"
+ "otherParameters"
+ "percentEncodedQuery"
+ "performRequests"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "personId"
+ "queryItemWithName:value:"
+ "queryItems"
+ "queryItemsWithParameters:"
+ "r^{?=IIQQ^{__CFString}^{__CFString}}"
+ "r^{?=IIQQ^{__CFString}^{__CFString}}16@0:8"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "runLoop == CFRunLoopGetCurrent()"
+ "self"
+ "setAuthenticationController:"
+ "setAuthorizationOptions:"
+ "setCompletionHandler:"
+ "setDelegate:"
+ "setFlags:"
+ "setQuery:"
+ "setQueryItems:"
+ "setService:"
+ "setSsoEnv:"
+ "setSsoHost:"
+ "setSsoRealm:"
+ "setStealthMode:"
+ "setUseLegacyAuthURL:"
+ "setUserInterfaceEnabled:"
+ "softlink:r:path:/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices"
+ "ssoEnv"
+ "ssoHost"
+ "ssoRealm"
+ "superclass"
+ "token"
+ "useLegacyAuthURL"
+ "username"
+ "v24@0:8@?16"
+ "v24@0:8r^{?=IIQQ^{__CFString}^{__CFString}}16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v2moajdtswxekdtyqnenkxna8yxvhv"
+ "v32@0:8@\"ASAuthorizationController\"16@\"ASAuthorization\"24"
+ "v32@0:8@\"ASAuthorizationController\"16@\"NSError\"24"
+ "v32@0:8@\"ASAuthorizationController\"16@\"NSString\"24"
+ "v32@?0@\"NSMutableArray\"8@\"NSString\"16@\"NSString\"24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v32@?0@\"NSURLQueryItem\"8Q16^B24"
+ "value"
+ "void *AuthenticationServicesLibrary(void)"
+ "ypilkyibsrqvlyazp6iuq6tu4i2ume"
+ "znkudjqthe3mekdby1z33rifsdmsop"
+ "zone"
- "VinylRestore-146~868"
- "libauthinstall_device-1104.120.3"

```
