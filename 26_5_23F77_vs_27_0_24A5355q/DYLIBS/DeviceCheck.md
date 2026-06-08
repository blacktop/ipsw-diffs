## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`

```diff

-132.2.0.0.0
-  __TEXT.__text: 0xae8c
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x67c
+151.0.0.0.0
+  __TEXT.__text: 0xa470
+  __TEXT.__objc_methlist: 0x674
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x92b
-  __TEXT.__gcc_except_tab: 0x56c
-  __TEXT.__oslogstring: 0xc8e
-  __TEXT.__unwind_info: 0x2e8
-  __TEXT.__objc_classname: 0xf8
-  __TEXT.__objc_methname: 0x105b
-  __TEXT.__objc_methtype: 0x5b9
-  __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x558
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__cstring: 0x9c0
+  __TEXT.__gcc_except_tab: 0x468
+  __TEXT.__oslogstring: 0xcbc
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x180
+  __DATA_CONST.__got: 0x158
+  __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0xa60
+  __AUTH_CONST.__objc_const: 0xae0
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12573A37-1D4A-3987-B989-E40720D34456
-  Functions: 183
-  Symbols:   844
-  CStrings:  416
+  UUID: 5FAEE341-7E72-3FF7-9C1A-E02F74413645
+  Functions: 186
+  Symbols:   860
+  CStrings:  180
 
Symbols:
+ +[DCXPCUtil sharedSerialProcessingQueue]
+ +[DCXPCUtil sharedSerialProcessingQueue].cold.1
+ _OBJC_CLASS_$_DCXPCUtil
+ _OBJC_METACLASS_$_DCXPCUtil
+ __OBJC_$_CLASS_METHODS_DCXPCUtil
+ __OBJC_CLASS_RO_$_DCXPCUtil
+ __OBJC_METACLASS_RO_$_DCXPCUtil
+ ___40+[DCXPCUtil sharedSerialProcessingQueue]_block_invoke
+ ___40+[DCXPCUtil sharedSerialProcessingQueue]_block_invoke.cold.1
+ ___40+[DCXPCUtil sharedSerialProcessingQueue]_block_invoke.cold.2
+ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke.87
+ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke.22
+ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.82
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.84
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.84.cold.1
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.84.cold.2
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.84.cold.3
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.84.cold.4
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.43
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.74
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.51
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.57.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.58
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.67
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.67.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.67.cold.2
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.69.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.70
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.68
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.68.cold.1
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0ls48l8s32l8s40l8r56l8
+ ___block_literal_global.26
+ ___block_literal_global.5
+ ___block_literal_global.80
+ _dyld_get_program_sdk_version_token
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$appAttestationAssert:keyId:clientDataHash:clientSDKVersionToken:completion:
+ _objc_msgSend$appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:clientSDKVersionToken:completion:
+ _objc_msgSend$appAttestationAttestKey:keyId:clientDataHash:clientSDKVersionToken:completion:
+ _objc_msgSend$appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:clientSDKVersionToken:completion:
+ _objc_msgSend$sharedSerialProcessingQueue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _sharedSerialProcessingQueue.queue
+ _sharedSerialProcessingQueue.queueCreationGuard
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DCDeviceMetadataProtocol
- ___46-[DCAppAttestController isSupportedWithError:]_block_invoke.86
- ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke.21
- ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.80
- ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.82
- ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.1
- ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.2
- ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.3
- ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.4
- ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.41
- ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.73
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.50
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.56
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.56.cold.1
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.66
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.66.cold.1
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.66.cold.2
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.68
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.68.cold.1
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.67
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.67.cold.1
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8r80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r88l8
- ___block_literal_global.156
- ___block_literal_global.27
- ___block_literal_global.81
- ___clientProcessingQueue_block_invoke
- ___clientProcessingQueue_block_invoke.cold.1
- _clientProcessingQueue
- _clientProcessingQueue.cold.1
- _clientProcessingQueue.queue
- _clientProcessingQueue.queueCreationGuard
- _objc_msgSend$appAttestationAssert:keyId:clientDataHash:completion:
- _objc_msgSend$appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:
- _objc_msgSend$appAttestationAttestKey:keyId:clientDataHash:completion:
- _objc_msgSend$appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "%25s:%-5d Created XPC processing queue. { queueName=%s }"
+ "%25s:%-5d Failed to create XPC processing queue."
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/devicecheckd/Source/Core/DCXPCUtil.m"
+ "com.apple.devicecheck.xpc.processing"
- "#16@0:8"
- "%25s:%-5d Created client processing queue. { queueName=%s }"
- ".cxx_destruct"
- "@\"DCAppAttestController\""
- "@\"NSLock\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "DCAnalytics"
- "DCAppAttestController"
- "DCAppAttestDeviceService"
- "DCAppAttestService"
- "DCAppAttestServicePriv"
- "DCAppAttestWebAuthService"
- "DCDevice"
- "DCDeviceMetadataDaemonConnection"
- "DCDeviceMetadataInterface"
- "DCDeviceMetadataProtocol"
- "DeviceCheck"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"DCAppAttestController\",&,N,V_appAttestController"
- "T@\"DCAppAttestDeviceService\",R"
- "T@\"DCAppAttestService\",R"
- "T@\"DCAppAttestServicePriv\",R"
- "T@\"DCAppAttestWebAuthService\",R"
- "T@\"DCDevice\",R"
- "T@\"NSLock\",&,N,V_connLock"
- "T@\"NSMutableDictionary\",&,N,V_perfIdMap"
- "T@\"NSObject<OS_os_log>\",&,N,V_perfLog"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUserDefaults\",&,N,V_legacyUserDefaults"
- "T@\"NSUserDefaults\",&,N,V_userDefaults"
- "T@\"NSXPCConnection\",&,N,V_conn"
- "TB,N,V_isNetworkReachable"
- "TB,R,GisSupported"
- "TQ,N,V_appAttestType"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "XPCInterface"
- "^{_NSZone=}16@0:8"
- "_appAttestController"
- "_appAttestType"
- "_conn"
- "_connLock"
- "_isNetworkReachable"
- "_isSupportedReturningError:"
- "_legacyUserDefaults"
- "_perfIdMap"
- "_perfLog"
- "_userDefaults"
- "addNetworkReachableObserver:selector:"
- "addObject:"
- "appAttestController"
- "appAttestType"
- "appAttestationAssert:keyId:clientDataHash:completion:"
- "appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
- "appAttestationAttestKey:keyId:clientDataHash:completion:"
- "appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
- "appAttestationCreateKey:completion:"
- "appAttestationCreateKeyWithTeamIdentifier:appUUID:completion:"
- "appAttestationDeviceAttestKey:useSystemKeychain:clientDataHash:options:completion:"
- "appAttestationDeviceIsSupportedWithCompletion:"
- "appAttestationIsSupportedWithCompletion:"
- "appAttestationPrivIsSupportedWithCompletion:"
- "appAttestationSign:appUUID:keyId:teamId:completion:"
- "appAttestationWebAttestKey:clientDataHash:authData:completion:"
- "appAttestationWebIsSupportedWithCompletion:"
- "attestKey:clientDataHash:authData:completionHandler:"
- "attestKey:clientDataHash:completionHandler:"
- "attestKey:clientDataHash:options:completionHandler:"
- "attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:"
- "attestKey:teamIdentifier:clientDataHash:completionHandler:"
- "autorelease"
- "baaSignatureForData:completion:"
- "baaSignaturesForData:completion:"
- "boolForKey:"
- "class"
- "code"
- "com.apple.devicecheck.client.processing"
- "conformsToProtocol:"
- "conn"
- "connLock"
- "connection"
- "containsObject:"
- "convertCategory:"
- "createKeyFromEndpoint:error:"
- "currentConnection"
- "currentDevice"
- "dc_errorWithCode:"
- "dc_errorWithCode:userInfo:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchCompletionHandler:ontoQueue:"
- "domain"
- "doubleValue"
- "errorWithDomain:code:userInfo:"
- "fetchOpaqueBlobWithCompletion:"
- "generateAssertion:clientDataHash:completionHandler:"
- "generateAssertion:teamIdentifier:clientDataHash:completionHandler:"
- "generateKeyWithCompletionHandler:"
- "generateKeyWithTeamIdentifier:completion:"
- "generateTokenWithCompletionHandler:"
- "getKeyProxyEndpoint:keyId:teamIdentifier:completion:"
- "getPropertiesForKeyId:teamIdentifier:completionHandler:"
- "hasEntitlement"
- "hash"
- "init"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "initWithSuiteName:"
- "initWithType:"
- "initWithUUIDString:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNetworkReachable"
- "isProxy"
- "isSupportedDeviceWithCompletion:"
- "isSupportedWithError:"
- "legacyUserDefaults"
- "loadAppUUID"
- "localizedDescription"
- "lock"
- "mutableCopy"
- "networkReachabilityChanged:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "perfIdMap"
- "perfLog"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "release"
- "remoteObjectProxy:"
- "remoteObjectProxyWithErrorHandler:"
- "removeNetworkReachableObserver:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "rewrapAsDCError:"
- "saveAppUUID:"
- "self"
- "sendPayload:forEvent:withError:"
- "sendPerformanceForCategory:eventType:"
- "setAppAttestController:"
- "setAppAttestType:"
- "setConn:"
- "setConnLock:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsNetworkReachable:"
- "setLegacyUserDefaults:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPerfIdMap:"
- "setPerfLog:"
- "setRemoteObjectInterface:"
- "setUserDefaults:"
- "shared"
- "sharedNetworkObserver"
- "sharedService"
- "sign:withKey:completionHandler:"
- "sign:withKey:teamIdentifier:completionHandler:"
- "standardUserDefaults"
- "stringForKey:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supported"
- "synchronousRemoteObjectProxy:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unlock"
- "userDefaults"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@24"
- "v32@0:8Q16Q24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@?<v@?i@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24@32@?40"
- "v52@0:8@\"NSString\"16B24@\"NSData\"28@\"NSDictionary\"36@?<v@?i@\"NSError\">44"
- "v52@0:8@16B24@28@36@?44"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSData\"@\"NSError\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@16@24@32@40@48@?56"
- "zone"

```
