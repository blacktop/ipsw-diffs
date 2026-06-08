## MobileActivation

> `/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation`

```diff

-1076.120.12.0.0
-  __TEXT.__text: 0xf384
-  __TEXT.__auth_stubs: 0x2a0
+1137.0.0.0.0
+  __TEXT.__text: 0xeff4
   __TEXT.__objc_methlist: 0x4cc
-  __TEXT.__cstring: 0x2137
+  __TEXT.__cstring: 0x21e5
   __TEXT.__const: 0x8a
-  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x418
-  __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x1055
-  __TEXT.__objc_methtype: 0x3df
-  __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__unwind_info: 0x448
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e0
+  __DATA_CONST.__objc_selrefs: 0x4f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x4d8
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__objc_arraydata: 0x588
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2f0
-  __AUTH_CONST.__cfstring: 0x26c0
+  __AUTH_CONST.__cfstring: 0x2840
   __AUTH_CONST.__objc_const: 0x3b0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xe4
   __DATA.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF151E12-7278-3F71-B616-AEF6AAEE5CCC
-  Functions: 252
-  Symbols:   828
-  CStrings:  883
+  UUID: F6CA47F9-DFE8-329C-A511-21886BBB64CF
+  Functions: 255
+  Symbols:   840
+  CStrings:  701
 
Symbols:
+ _X509ExtensionParseKeyTransparencyLeaf
+ _copyMobileGestaltAnswer
+ _copyMobileGestaltAnswerDarwin
+ _gMobileGestaltInterface
+ _mobileactivationErrorHasDomainAndAnyErrorCode
+ _objc_msgSend$containsObject:
+ _objc_msgSend$numberWithInteger:
+ _objc_retainAutoreleaseReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _X509ExtensionParseMFIAuthv3Leaf
CStrings:
+ "EnergyKitService"
+ "Home Services Demo"
+ "HomeEnergyWidgetsExtension"
+ "NFReportingService"
+ "NanoHome"
+ "NanoHomeWidgetsExtension"
+ "Polaris"
+ "assetsd"
+ "cameracaptured"
+ "deferredmediad"
+ "enhancedloggingd"
+ "iOS Device Activator (MobileActivation-1137)"
+ "inboxupaterd"
+ "merchantd"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{__CFString=}16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8^{__CFString=}16"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "GestaltHlprMobileActivation"
- "MadGate"
- "MobileActivationProtocol"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",R,N,V_connection"
- "TQ,R"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__SecIdentity=}24@0:8^@16"
- "_connection"
- "addAGestaltKey:toDictionary:required:errors:"
- "addCharactersInString:"
- "addObject:"
- "allKeys"
- "alphanumericCharacterSet"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bytes"
- "class"
- "code"
- "compare:options:"
- "conformsToProtocol:"
- "connection"
- "containsString:"
- "copy"
- "copyActivationRecord:"
- "copyActivationRecordWithCompletionBlock:"
- "copyAnswer:"
- "copyAttestationDictionaryWithCompletionBlock:options:completion:"
- "copyAutomaticTimeEnabledWithCompletion:"
- "copyDCRT:withError:"
- "copyDCRTWithCompletionBlock:withCompletion:"
- "copyDeviceIDInfo:"
- "copyDeviceInfo:"
- "copyLegacyDeviceIdentity:"
- "copyLegacyDeviceIdentityWithCompletionBlock:"
- "copyMonotonicClockWithCompletionBlock:"
- "copyPCRTToken:"
- "copyPCRTTokenWithCompletionBlock:"
- "copyRTCResetCountWithCompletionBlock:"
- "copyRegulatoryImagesInfo:"
- "copyUCRTVersionInfo:"
- "copyUCRTVersionInfoWithCompletionBlock:"
- "copyUCRTWithCompletionBlock:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createActivationInfo:"
- "createActivationInfoWithCompletionBlock:"
- "createTunnel1ActivationInfo:options:error:"
- "createTunnel1ActivationInfo:options:withCompletionBlock:"
- "createTunnel1SessionInfo:"
- "createTunnel1SessionInfoWithCompletionBlock:"
- "dataUsingEncoding:allowLossyConversion:"
- "dataWithPropertyList:format:options:error:"
- "deactivateDevice:"
- "deactivateDeviceWithCompletionBlock:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "deleteLegacyDeviceIdentity:"
- "deleteLegacyDeviceIdentityWithCompletionBlock:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "getActivationBuild:"
- "getActivationBuildWithCompletionBlock:"
- "getActivationState:"
- "getActivationStateWithCompletionBlock:"
- "getBoolAnswer:"
- "getDCRTState:withError:"
- "getDCRTStateWithCompletionBlock:withCompletion:"
- "getSharedInstance"
- "getUCRTActivationLockState:"
- "getUCRTSalvageState:"
- "getUCRTSalvageStateWithCompletionBlock:"
- "handleActivationInfo:withCompletionBlock:"
- "handleActivationInfo:withError:"
- "handleActivationInfoWithSession:activationSignature:completionBlock:"
- "handleActivationInfoWithSession:activationSignature:error:"
- "hasSuffix:"
- "hash"
- "iOS Device Activator (MobileActivation-1076.120.12)"
- "init"
- "initWithBase64EncodedString:options:"
- "initWithBytes:length:"
- "initWithContentsOfFile:"
- "initWithData:encoding:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithMachServiceName:options:"
- "initWithURL:cachePolicy:timeoutInterval:"
- "interfaceWithProtocol:"
- "invalidate"
- "isDeviceABrick:"
- "isDeviceBrickedWithCompletionBlock:"
- "isEqual:"
- "isEqualToString:"
- "isInFieldCollected:"
- "isInFieldCollectedWithCompletionBlock:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isUCRTAvailable:"
- "issueClientCertificateLegacy:WithCompletionBlock:"
- "issueClientCertificateLegacy:error:"
- "issueClientCertificateWithReferenceKey:options:completion:"
- "issueCollection:withCompletion:"
- "issueCollection:withCompletionBlock:"
- "issueDCRT:withCompletion:"
- "issueDCRT:withCompletionBlock:"
- "issueUCRT:withCompletionBlock:"
- "issueUCRT:withError:"
- "length"
- "mutableCopy"
- "numberWithBool:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForCaseInsensitiveKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performMigrationWithCompletion:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertyListWithData:options:format:error:"
- "reactivateDevice:"
- "recertifyDeviceWithCompletionBlock:"
- "recertifyDeviceWithError:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "requestDeviceReactivationWithCompletionBlock:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setCachePolicy:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setTimeoutInterval:"
- "setURL:"
- "setValue:forHTTPHeaderField:"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingPathComponent:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "ucrtUpgradeRequired:"
- "ucrtUpgradeRequiredWithCompletionBlock:"
- "unbrickDevice:"
- "unbrickDeviceWithCompletionBlock:"
- "updateBasebandTicket:baaCert:baaIntermediateCert:options:withCompletion:"
- "updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:"
- "updateRecertInfo:errors:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@16^@24"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v44@0:8^{__CFString=}16@24B32@36"
- "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSDictionary\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16^{__SecCertificate=}24^{__SecCertificate=}32@40@?48"
- "xRyzf9zFE/ycr/wJPweZvQ"
- "zone"

```
