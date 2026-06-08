## CertUI

> `/System/Library/PrivateFrameworks/CertUI.framework/CertUI`

```diff

-2052.100.2.0.0
-  __TEXT.__text: 0x46b4
-  __TEXT.__auth_stubs: 0x490
+2054.0.0.0.0
+  __TEXT.__text: 0x4200
   __TEXT.__objc_methlist: 0x378
   __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x4ed
-  __TEXT.__cstring: 0x49f
+  __TEXT.__cstring: 0x4a8
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0xa41
-  __TEXT.__objc_methtype: 0x2b9
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0x178
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x338
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x3f8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x28
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29E7F245-66C0-38EA-B448-F79EEEE28AFF
+  UUID: 9A5F3804-5C58-341C-A805-FC6D796AE5BF
   Functions: 86
-  Symbols:   457
-  CStrings:  317
+  Symbols:   461
+  CStrings:  158
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain_x25
Functions:
~ +[CertUIUtilities bundleIDFromAuditToken:] : 464 -> 420
~ +[CertUIUtilities localizedAppTitleForBundleID:] : 608 -> 536
~ +[CertUIUtilities _certUIBundle] : 176 -> 160
~ ___32+[CertUIUtilities _certUIBundle]_block_invoke : 76 -> 72
~ +[CertUIConnectionDelegate defaultServiceForProtocol:] : 312 -> 308
~ -[CertUIConnectionDelegate connection:canAuthenticateAgainstProtectionSpace:] : 356 -> 312
~ -[CertUIConnectionDelegate _continueConnectionWithResponse:challenge:service:] : 600 -> 528
~ -[CertUIConnectionDelegate connection:didReceiveAuthenticationChallenge:] : 960 -> 864
~ +[CertUITrustManager defaultTrustManager] : 84 -> 68
~ -[CertUITrustManager _actionForTrust:exceptions:] : 520 -> 476
~ -[CertUITrustManager _getExceptionsForSSLTrust:hostname:service:] : 428 -> 388
~ __CopyExceptionsForMutableQuery : 620 -> 592
~ -[CertUITrustManager actionForSSLTrust:hostname:service:] : 356 -> 312
~ -[CertUITrustManager rawTrustResultForSSLTrust:hostname:service:] : 356 -> 312
~ -[CertUITrustManager actionForSMIMETrust:sender:] : 376 -> 332
~ -[CertUITrustManager addSSLTrust:hostname:service:] : 388 -> 348
~ __SaveExceptionsForMutableQuery : 752 -> 724
~ -[CertUITrustManager addSMIMETrust:sender:] : 364 -> 312
~ -[CertUITrustManager removeSSLTrust:hostname:service:] : 348 -> 308
~ __DeleteExceptionsForQuery : 484 -> 452
~ -[CertUITrustManager removeSMIMETrust:sender:] : 324 -> 280
~ -[CertUITrustManager(SMIMEExtensions) _hasExceptionsForSMIMETrust:sender:] : 816 -> 796
~ __CopyKeychainAccountForPrefixParticularDigest : 400 -> 408
~ +[CertUIPrompt(Private) stringForResponse:] : 192 -> 200
~ -[CertUIPrompt description] : 136 -> 128
~ -[CertUIPrompt connectionDisplayName] : 188 -> 176
~ +[CertUIPrompt promptQueue] : 84 -> 68
~ -[CertUIPrompt _sendablePropertyFromProperty:] : 368 -> 340
~ -[CertUIPrompt _sendablePropertiesFromProperties:] : 348 -> 340
~ -[CertUIPrompt _sendablePropertiesFromTrust:] : 344 -> 340
~ -[CertUIPrompt _propertyNamed:ofType:inProperties:] : 472 -> 460
~ -[CertUIPrompt _purposeFromTrustProperties:] : 224 -> 208
~ -[CertUIPrompt _newUserInfoWithHostname:trust:options:] : 920 -> 876
~ -[CertUIPrompt _responseFromReplyDict:] : 344 -> 288
~ -[CertUIPrompt _sendRemoteMessageWithPromptOptions:] : 312 -> 264
~ -[CertUIPrompt showPromptWithOptions:responseBlock:] : 212 -> 220
~ -[CertUIPrompt showAndWaitForResponse] : 228 -> 224
~ -[CertUIPrompt setHost:] : 64 -> 12
~ -[CertUIPrompt setService:] : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@"
- "@\"CertUITrustManager\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{?=[8I]}16"
- "@24@0:8^{__SecTrust=}16"
- "@40@0:8@16@24@32"
- "@40@0:8@16^{__SecTrust=}24@32"
- "@40@0:8^{__SecTrust=}16@24@32"
- "@?"
- "B24@0:8:16"
- "B24@0:8^{__SecTrust=}16"
- "B32@0:8@16@24"
- "B32@0:8^{__SecTrust=}16@24"
- "CertUIConnectionDelegate"
- "CertUIPrompt"
- "CertUITrustManager"
- "CertUIUtilities"
- "Deprecated"
- "I32@0:8^{__SecTrust=}16@24"
- "I40@0:8^{__SecTrust=}16@24@32"
- "Private"
- "SMIMEExtensions"
- "T@\"NSString\",&,N,V_host"
- "T@\"NSString\",&,N,V_service"
- "T@\"NSString\",C,N,V_connectionDisplayName"
- "T@,W,N,V_forwardingDelegate"
- "^{__SecTrust=}"
- "^{__SecTrust=}16@0:8"
- "_access"
- "_actionForTrust:exceptions:"
- "_certUIBundle"
- "_connectionDisplayName"
- "_continueConnectionWithResponse:challenge:service:"
- "_copyPropertiesFromTrust:"
- "_delegateRespondsTo"
- "_digestFromTrust:"
- "_expirationFromTrust:"
- "_forwardingDelegate"
- "_getExceptionsForSSLTrust:hostname:service:"
- "_hasExceptionsForSMIMETrust:sender:"
- "_host"
- "_informConsumerOfResponse:"
- "_isRootCertificateFromTrust:"
- "_issuerFromTrust:"
- "_messagingCenter"
- "_newUserInfoWithHostname:trust:options:"
- "_propertyNamed:ofType:inProperties:"
- "_purposeFromTrustProperties:"
- "_rawTrustResultForTrust:exceptions:"
- "_responseBlock"
- "_responseFromReplyDict:"
- "_sendRemoteMessage"
- "_sendRemoteMessageWithPromptOptions:"
- "_sendablePropertiesFromProperties:"
- "_sendablePropertiesFromTrust:"
- "_sendablePropertyFromProperty:"
- "_service"
- "_subtitleFromTrust:"
- "_titleFromTrust:"
- "_trust"
- "_trustManager"
- "absoluteString"
- "actionForSMIMETrust:sender:"
- "actionForSSLTrust:hostname:service:"
- "actionForTrust:forHost:andService:"
- "addObject:"
- "addSMIMETrust:sender:"
- "addSSLTrust:hostname:service:"
- "allowTrust:forHost:service:"
- "applicationProxyForIdentifier:"
- "arrayWithCapacity:"
- "authenticationMethod"
- "boolValue"
- "bundleForClass:"
- "bundleIDFromAuditToken:"
- "bytes"
- "cancelAuthenticationChallenge:"
- "centerNamed:"
- "clearSavedTrustSettingsForTrust:host:service:"
- "connection:canAuthenticateAgainstProtectionSpace:"
- "connection:didReceiveAuthenticationChallenge:"
- "connectionDisplayName"
- "continueWithoutCredentialForAuthenticationChallenge:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultServiceForProtocol:"
- "defaultTrustManager"
- "description"
- "dictionaryWithDictionary:"
- "forwardingDelegate"
- "forwardingTargetForSelector:"
- "hasPrefix:"
- "host"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8^{__SecTrust=}16@24"
- "i40@0:8^{__SecTrust=}16@24@32"
- "init"
- "initWithAccessGroup:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithCapacity:"
- "initWithObjectsAndKeys:"
- "initWithTrust:"
- "intValue"
- "isEqualToString:"
- "length"
- "localizedAppTitleForBundleID:"
- "localizedName"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "numberWithBool:"
- "objectAtIndex:"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "processInfo"
- "processName"
- "promptQueue"
- "protectionSpace"
- "protocol"
- "rawTrustResultForSSLTrust:hostname:service:"
- "removeAllTrusts"
- "removeSMIMETrust:sender:"
- "removeSSLTrust:hostname:service:"
- "respondsToSelector:"
- "sendMessageAndReceiveReplyName:userInfo:error:"
- "sender"
- "serverTrust"
- "service"
- "setConnectionDisplayName:"
- "setForwardingDelegate:"
- "setHost:"
- "setObject:forKey:"
- "setService:"
- "setTrust:"
- "showAndWaitForResponse"
- "showPromptWithOptions:responseBlock:"
- "showPromptWithResponseBlock:"
- "stringByAppendingFormat:"
- "stringForResponse:"
- "trust"
- "useCredential:forAuthenticationChallenge:"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8^{__SecTrust=}16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8^{__SecTrust=}16@24"
- "v36@0:8i16@20@28"
- "v40@0:8^{__SecTrust=}16@24@32"
- "{?=\"canAuthenticateAgainstProtectionSpace\"b1\"didReceiveAuthenticationChallenge\"b1}"

```
