## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`

```diff

-88.3.0.0.0
-  __TEXT.__text: 0x231c
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x181
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0x9e
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x6e6
-  __TEXT.__objc_methtype: 0x2ad
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x20
+107.0.0.0.0
+  __TEXT.__text: 0x8dd8
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x654
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x79c
+  __TEXT.__gcc_except_tab: 0x440
+  __TEXT.__oslogstring: 0x9cd
+  __TEXT.__unwind_info: 0x280
+  __TEXT.__objc_classname: 0xf8
+  __TEXT.__objc_methname: 0xf9b
+  __TEXT.__objc_methtype: 0x552
+  __TEXT.__objc_stubs: 0xbe0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x728
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x8
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x640
+  __AUTH_CONST.__objc_const: 0xa58
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 54
-  Symbols:   141
-  CStrings:  154
+  Functions: 160
+  Symbols:   323
+  CStrings:  352
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFErrorCopyDescription
+ _CFPreferencesSynchronize
+ _CFRelease
+ _OBJC_CLASS_$_CPNetworkObserver
+ _OBJC_CLASS_$_DCAppAttestDeviceService
+ _OBJC_CLASS_$_DCAppAttestServicePriv
+ _OBJC_CLASS_$_DCAppAttestWebAuthService
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_DCAppAttestDeviceService
+ _OBJC_METACLASS_$_DCAppAttestServicePriv
+ _OBJC_METACLASS_$_DCAppAttestWebAuthService
+ _SecCertificateCreateWithData
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ _SecKeyCopyAttributes
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __CFPreferencesSetBackupDisabled
+ ___kCFBooleanTrue
+ __os_signpost_emit_with_name_impl
+ _kCFAllocatorDefault
+ _kCFBooleanTrue
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
+ _kSecAttrAccount
+ _kSecAttrGeneric
+ _kSecAttrLabel
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecClassKey
+ _kSecReturnData
+ _kSecUseDataProtectionKeychain
+ _kSecUseSystemKeychain
+ _kSecValueRef
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retainBlock
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_terminate
+ _os_signpost_enabled
+ _os_signpost_id_generate
- __os_log_debug_impl
- __os_log_error_impl
CStrings:
+ "\x01"
+ "\x12"
+ " enableTelemetry=YES com.apple.devicecheck.appattest.attestKey"
+ " enableTelemetry=YES com.apple.devicecheck.appattest.generateAssertion"
+ " enableTelemetry=YES com.apple.devicecheck.appattest.generateKey"
+ " enableTelemetry=YES com.apple.devicecheck.appattestdevice.attestKey"
+ " enableTelemetry=YES com.apple.devicecheck.appattestpriv.attestKey"
+ " enableTelemetry=YES com.apple.devicecheck.appattestpriv.generateAssertion"
+ " enableTelemetry=YES com.apple.devicecheck.appattestpriv.generateKey"
+ " enableTelemetry=YES com.apple.devicecheck.appattestweb.attestKey"
+ " enableTelemetry=YES com.apple.devicecheck.generateToken"
+ " enableTelemetry=YES com.apple.devicecheck.isSupported"
+ "%25s:%-5d Attempted to submit analytics event. { didSend=%d, event=%@, errorClass=%ld, networkReachable=%d }"
+ "%25s:%-5d Client is missing Device API entitlement."
+ "%25s:%-5d Client is missing WebAuth API entitlement."
+ "%25s:%-5d Client is not supported, cannot attest key."
+ "%25s:%-5d Client not supported, cannot attest key."
+ "%25s:%-5d Created cert. { label=%@ }"
+ "%25s:%-5d Dispatching completion handler onto calling queue. { queueLabel=%s }"
+ "%25s:%-5d Dropping signpost begin. { eventName=%@, eventId=%llu }"
+ "%25s:%-5d Dropping signpost end. { eventName=%@, eventId=%llu }"
+ "%25s:%-5d Failed to check if AppAttest is supported. { error=%@ }"
+ "%25s:%-5d Failed to check if client is supported. { error=%@ }"
+ "%25s:%-5d Failed to connect to daemon. { error=%@ }"
+ "%25s:%-5d Failed to copy certificate data. { error=%@, err=%d, label=%@ }"
+ "%25s:%-5d Failed to create cert. { label=%@ }"
+ "%25s:%-5d Failed to delete cert from keychain. { keyId=%@, error=%@ }"
+ "%25s:%-5d Failed to delete key from keychain. { keyId=%@, error=%@ }"
+ "%25s:%-5d Failed to fetch App UUID."
+ "%25s:%-5d Failed to fetch entitlement. { error=%@ }"
+ "%25s:%-5d Failed to save key to keychain. { error=%@ }"
+ "%25s:%-5d Failed to setup synchronous remote object proxy to daemon. { error=%@ }"
+ "%25s:%-5d Fetched UUID from legacy suite, transferring value to new suite."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypeDefault."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypeDevice."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypePriv."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypeWeb."
+ "%25s:%-5d Performance analytics disabled. { category=%@ }"
+ "%25s:%-5d Re-mapped error. { mapped=%@, internal=%@ }"
+ "%@:%@:%d"
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Core/DCAnalytics.m"
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Core/DCAppAttestController.m"
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestDeviceService.m"
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestWebAuthService.m"
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Interfaces/Public/DCDevice.m"
+ "2"
+ "@\"DCAppAttestController\""
+ "@\"NSDictionary\"8@?0"
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSUserDefaults\""
+ "@24@0:8Q16"
+ "B"
+ "DCAnalytics"
+ "DCAppAttestController"
+ "DCAppAttestDeviceService"
+ "DCAppAttestServicePriv"
+ "DCAppAttestWebAuthService"
+ "Failed to add %@ to keychain: %d"
+ "Failed to copy keychain item %@: %d"
+ "Failed to delete existing keychain item."
+ "Failed to remove existing keychain item %@: %d"
+ "Invalid input(s)."
+ "Invalid input."
+ "Q"
+ "T@\"DCAppAttestController\",&,N,V_appAttestController"
+ "T@\"DCAppAttestDeviceService\",R"
+ "T@\"DCAppAttestServicePriv\",R"
+ "T@\"DCAppAttestWebAuthService\",R"
+ "T@\"NSLock\",&,N,V_connLock"
+ "T@\"NSMutableDictionary\",&,N,V_perfIdMap"
+ "T@\"NSObject<OS_os_log>\",&,N,V_perfLog"
+ "T@\"NSUserDefaults\",&,N,V_legacyUserDefaults"
+ "T@\"NSUserDefaults\",&,N,V_userDefaults"
+ "T@\"NSXPCConnection\",&,N,V_conn"
+ "TB,N,V_isNetworkReachable"
+ "TQ,N,V_appAttestType"
+ "UUID"
+ "UUIDString"
+ "_appAttestController"
+ "_appAttestType"
+ "_isNetworkReachable"
+ "_legacyUserDefaults"
+ "_perfIdMap"
+ "_perfLog"
+ "_userDefaults"
+ "addNetworkReachableObserver:selector:"
+ "appAttestController"
+ "appAttestType"
+ "appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
+ "appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
+ "appAttestationCreateKeyWithTeamIdentifier:appUUID:completion:"
+ "appAttestationDeviceAttestKey:useSystemKeychain:clientDataHash:options:completion:"
+ "appAttestationDeviceIsSupportedWithCompletion:"
+ "appAttestationPrivIsSupportedWithCompletion:"
+ "appAttestationSign:appUUID:keyId:completion:"
+ "appAttestationWebAttestKey:clientDataHash:authData:completion:"
+ "appAttestationWebIsSupportedWithCompletion:"
+ "appUUIDLoaded"
+ "appattest-device"
+ "appattest-webauthn"
+ "attestKey"
+ "attestKey:clientDataHash:authData:completionHandler:"
+ "attestKey:clientDataHash:options:completionHandler:"
+ "attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:"
+ "attestKey:teamIdentifier:clientDataHash:completionHandler:"
+ "attestKeyDevice"
+ "attestKeyPriv"
+ "attestKeyWeb"
+ "attestedKey"
+ "cert"
+ "clientDataHashValid"
+ "com.apple.AppAttest.client"
+ "com.apple.devicecheck.appattest.attestKey"
+ "com.apple.devicecheck.appattest.generateAssertion"
+ "com.apple.devicecheck.appattest.generateKey"
+ "com.apple.devicecheck.appattest.isSupported"
+ "com.apple.devicecheck.appattestdevice.attestKey"
+ "com.apple.devicecheck.appattestpriv.attestKey"
+ "com.apple.devicecheck.appattestpriv.generateAssertion"
+ "com.apple.devicecheck.appattestweb.attestKey"
+ "com.apple.devicecheck.generateToken"
+ "com.apple.devicecheck.isSupported"
+ "com.apple.devicecheck.private.device"
+ "com.apple.devicecheck.private.webauth"
+ "conn"
+ "connLock"
+ "convertCategory:"
+ "copy_keychain_data"
+ "dc"
+ "dealloc"
+ "default"
+ "delete_keychain_item_for_system_keychain"
+ "device"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObjects:forKeys:count:"
+ "doubleValue"
+ "errorClass"
+ "generateAssertion"
+ "generateAssertion:teamIdentifier:clientDataHash:completionHandler:"
+ "generateAssertionPriv"
+ "generateKey"
+ "generateKeyPriv"
+ "generateKeyWithTeamIdentifier:completion:"
+ "generateToken"
+ "generatedAssertion"
+ "hasEntitlement"
+ "i"
+ "initWithType:"
+ "isNetworkReachable"
+ "isSupportedWithError:"
+ "keyIdValid"
+ "legacyUserDefaults"
+ "loadAppUUID"
+ "localizedDescription"
+ "mutableCopy"
+ "networkReachabilityChanged:"
+ "networkReachable"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "numberWithUnsignedLongLong:"
+ "objectForKey:"
+ "perf"
+ "perfIdMap"
+ "perfLog"
+ "priv"
+ "removeNetworkReachableObserver:"
+ "removeObjectForKey:"
+ "rewrapAsDCError:"
+ "saveAppUUID:"
+ "sendPayload:forEvent:withError:"
+ "sendPerformanceForCategory:eventType:"
+ "serviceType"
+ "setAppAttestController:"
+ "setAppAttestType:"
+ "setConn:"
+ "setConnLock:"
+ "setIsNetworkReachable:"
+ "setLegacyUserDefaults:"
+ "setPerfIdMap:"
+ "setPerfLog:"
+ "setUserDefaults:"
+ "shared"
+ "sharedNetworkObserver"
+ "sign:withKey:completionHandler:"
+ "store_keychain_item"
+ "stringWithFormat:"
+ "unknown"
+ "userDefaults"
+ "v20@0:8B16"
+ "v20@?0i8@\"NSError\"12"
+ "v24@0:8Q16"
+ "v32@0:8Q16Q24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@?<v@?i@\"NSError\">40"
+ "v48@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24@32@?40"
+ "v52@0:8@\"NSString\"16B24@\"NSData\"28@\"NSDictionary\"36@?<v@?i@\"NSError\">44"
+ "v52@0:8@16B24@28@36@?44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "v64@0:8@16@24@32@40@48@?56"
+ "web"
- "Dispatching completion handler onto calling queue. { queueLabel=%s }"
- "Remap to DCError (%@) <- (%@)\n"
- "XPCConnection failed with error: %@"
- "_loadAppUUID"
- "_rewrapAsDCError:"
- "_saveAppUUID:"
- "core"
- "isSupported error: %@"

```
