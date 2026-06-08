## libSoftwareUpdateSSO.dylib

> `/usr/lib/libSoftwareUpdateSSO.dylib`

```diff

-1837.122.1.0.0
-  __TEXT.__text: 0x3164
-  __TEXT.__auth_stubs: 0x380
+2215.0.0.502.1
+  __TEXT.__text: 0x2de0
   __TEXT.__objc_methlist: 0x3b8
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2df
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x2fb
   __TEXT.__oslogstring: 0x7b9
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0xb17
-  __TEXT.__objc_methtype: 0x2e8
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x640
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25FB107A-6A89-3B00-A1A2-C71C4323062F
+  UUID: 4EFB0EA5-FFC4-3E9A-A4CE-FA49C442FFCF
   Functions: 62
-  Symbols:   358
-  CStrings:  312
+  Symbols:   363
+  CStrings:  129
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
Functions:
~ __MAClientLog : 180 -> 168
~ ____MAClientLog_block_invoke : 652 -> 688
~ -[SoftwareUpdateExtensibleSSOAuthenticator copyQueryItemsWithParameters:] : 208 -> 204
~ -[SoftwareUpdateExtensibleSSOAuthenticator authenticate] : 1468 -> 1368
~ -[SoftwareUpdateExtensibleSSOAuthenticator authenticationSupported] : 224 -> 212
~ -[SoftwareUpdateExtensibleSSOAuthenticator authorizationController:didCompleteWithAuthorization:] : 328 -> 304
~ -[SoftwareUpdateExtensibleSSOAuthenticator authorizationController:didCompleteWithError:] : 232 -> 180
~ -[SoftwareUpdateExtensibleSSOAuthenticator setAppIdentifier:] : 64 -> 12
~ -[SoftwareUpdateExtensibleSSOAuthenticator setEnvIdentifier:] : 64 -> 12
~ -[SoftwareUpdateExtensibleSSOAuthenticator setUsername:] : 64 -> 12
~ -[SoftwareUpdateExtensibleSSOAuthenticator setInteractivity:] : 64 -> 12
~ -[SoftwareUpdateExtensibleSSOAuthenticator setOtherParameters:] : 64 -> 12
~ -[SoftwareUpdateSSO initWithOptions:] : 804 -> 720
~ -[SoftwareUpdateSSO invalidate] : 84 -> 80
~ -[SoftwareUpdateSSO setupAuthenticator] : 232 -> 212
~ -[SoftwareUpdateSSO copyTokenFromAuthenticatorResponse:error:] : 1252 -> 1132
~ ___62-[SoftwareUpdateSSO copyTokenFromAuthenticatorResponse:error:]_block_invoke : 144 -> 132
~ -[SoftwareUpdateSSO callerHasRequiredEntitlements] : 260 -> 256
~ -[SoftwareUpdateSSO _completionDeadline] : 108 -> 104
~ ___33-[SoftwareUpdateSSO copyUserInfo]_block_invoke : 316 -> 300
~ -[SoftwareUpdateSSO getDawToken] : 160 -> 140
~ ___32-[SoftwareUpdateSSO getDawToken]_block_invoke : 496 -> 468
~ -[SoftwareUpdateSSO ssoIsSupported] : 188 -> 176
~ -[SoftwareUpdateSSO authenticator:didCompleteWithResult:] : 156 -> 152
~ -[SoftwareUpdateSSO authenticator:didCompleteWithError:] : 276 -> 220
~ _copyPersonID : 1236 -> 1200
~ _MSUSSOIsAvailable : 384 -> 376
~ _copyPersonalizationSSOToken : 924 -> 900
~ _copyDawTokenAndUsername : 844 -> 824
CStrings:
+ "AutoSet-CheckMetadata"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SoftwareUpdateExtensibleSSOAuthenticatorDelegate>\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SoftwareUpdateExtensibleSSOAuthenticator\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@36@0:8i16@20@28"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "ASAuthorizationControllerDelegate"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SoftwareUpdateExtensibleSSOAuthenticator"
- "SoftwareUpdateExtensibleSSOAuthenticatorDelegate"
- "SoftwareUpdateSSO"
- "SoftwareUpdateSSOCompletionSemaphore"
- "T#,R"
- "T@\"<SoftwareUpdateExtensibleSSOAuthenticatorDelegate>\",W,N,V_delegate"
- "T@\"NSDictionary\",&,N,V_otherParameters"
- "T@\"NSDictionary\",&,V_defaultAuthParameters"
- "T@\"NSString\",&,N,V_appIdentifier"
- "T@\"NSString\",&,N,V_envIdentifier"
- "T@\"NSString\",&,N,V_interactivity"
- "T@\"NSString\",&,N,V_username"
- "T@\"NSString\",&,V_appIdentifier"
- "T@\"NSString\",&,V_dawToken"
- "T@\"NSString\",&,V_envIdentifier"
- "T@\"NSString\",&,V_interactivityLevel"
- "T@\"NSString\",&,V_personID"
- "T@\"NSString\",&,V_userName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"SoftwareUpdateExtensibleSSOAuthenticator\",&,V_authenticator"
- "T@?,C,N,V_resultCallBack"
- "TQ,R"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_appIdentifier"
- "_authenticator"
- "_completionDeadline"
- "_dawToken"
- "_defaultAuthParameters"
- "_delegate"
- "_envIdentifier"
- "_interactivity"
- "_interactivityLevel"
- "_otherParameters"
- "_personID"
- "_resultCallBack"
- "_userName"
- "_username"
- "addObject:"
- "allHeaderFields"
- "appIdentifier"
- "appendBytes:length:"
- "array"
- "arrayWithObjects:count:"
- "authenticate"
- "authenticatedResponse"
- "authenticationSupported"
- "authenticator"
- "authenticator:didCompleteWithError:"
- "authenticator:didCompleteWithResult:"
- "authorizationController:didCompleteWithAuthorization:"
- "authorizationController:didCompleteWithCustomMethod:"
- "authorizationController:didCompleteWithError:"
- "authorizationProviderWithIdentityProviderURL:"
- "autorelease"
- "buildSSOError:underlying:description:"
- "callerHasRequiredEntitlements"
- "canPerformAuthorization"
- "cancel"
- "class"
- "conformsToProtocol:"
- "copy"
- "copyQueryItemsWithParameters:"
- "copyTokenFromAuthenticatorResponse:error:"
- "copyUserInfo"
- "createRequest"
- "credential"
- "debugDescription"
- "defaultAuthParameters"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "envIdentifier"
- "errorWithDomain:code:userInfo:"
- "getCString:maxLength:encoding:"
- "getDawToken"
- "hash"
- "init"
- "initWithAuthorizationRequests:"
- "initWithOptions:"
- "integerValue"
- "interactivityLevel"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "mutableBytes"
- "mutableCopy"
- "name"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performRequests"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personID"
- "query"
- "queryItemWithName:value:"
- "queryItems"
- "release"
- "respondsToSelector:"
- "resultCallBack"
- "retain"
- "retainCount"
- "self"
- "setAppIdentifier:"
- "setAuthenticator:"
- "setAuthorizationOptions:"
- "setDawToken:"
- "setDefaultAuthParameters:"
- "setDelegate:"
- "setEnvIdentifier:"
- "setInteractivity:"
- "setInteractivityLevel:"
- "setLength:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOtherParameters:"
- "setPersonID:"
- "setQuery:"
- "setQueryItems:"
- "setResultCallBack:"
- "setUserInterfaceEnabled:"
- "setUserName:"
- "setUsername:"
- "setupAuthenticator"
- "sharedCore"
- "ssoControllerQueue"
- "ssoIsSupported"
- "stringValue"
- "stringWithFormat:"
- "superclass"
- "url"
- "useDomain:"
- "userName"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"ASAuthorizationController\"16@\"ASAuthorization\"24"
- "v32@0:8@\"ASAuthorizationController\"16@\"NSError\"24"
- "v32@0:8@\"ASAuthorizationController\"16@\"NSString\"24"
- "v32@0:8@\"SoftwareUpdateExtensibleSSOAuthenticator\"16@\"NSDictionary\"24"
- "v32@0:8@\"SoftwareUpdateExtensibleSSOAuthenticator\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "value"
- "valueForKey:"
- "zone"

```
