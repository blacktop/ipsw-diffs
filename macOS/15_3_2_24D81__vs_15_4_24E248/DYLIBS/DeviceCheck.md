## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/Versions/A/DeviceCheck`

```diff

-88.3.0.0.0
-  __TEXT.__text: 0x2af8
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_methlist: 0x160
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1ae
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__oslogstring: 0xce
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x700
-  __TEXT.__objc_methtype: 0x2b5
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x48
-  __DATA_CONST.__objc_classlist: 0x20
+108.2.0.0.0
+  __TEXT.__text: 0xa800
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0x65c
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0xa0e
+  __TEXT.__gcc_except_tab: 0x480
+  __TEXT.__oslogstring: 0x9bc
+  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__objc_classname: 0xf8
+  __TEXT.__objc_methname: 0xfce
+  __TEXT.__objc_methtype: 0x52e
+  __TEXT.__objc_stubs: 0xc20
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x158
-  __AUTH_CONST.__const: 0x270
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x728
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__const: 0x5a0
+  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__objc_const: 0xa58
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
+  - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97B4AFBD-74CA-30A8-9CF7-F74C869BB033
-  Functions: 71
-  Symbols:   267
-  CStrings:  173
+  UUID: 9EAEC5FB-9862-384C-A033-833147471D60
+  Functions: 191
+  Symbols:   591
+  CStrings:  410
 
Symbols:
+ +[DCAnalytics shared]
+ +[DCAnalytics shared].cold.1
+ +[DCAppAttestDeviceService sharedService]
+ +[DCAppAttestDeviceService sharedService].cold.1
+ +[DCAppAttestService sharedService].cold.1
+ +[DCAppAttestServicePriv sharedService]
+ +[DCAppAttestServicePriv sharedService].cold.1
+ +[DCAppAttestWebAuthService sharedService]
+ +[DCAppAttestWebAuthService sharedService].cold.1
+ +[DCDevice currentDevice].cold.1
+ -[DCAnalytics .cxx_destruct]
+ -[DCAnalytics convertCategory:]
+ -[DCAnalytics dealloc]
+ -[DCAnalytics init]
+ -[DCAnalytics isNetworkReachable]
+ -[DCAnalytics networkReachabilityChanged:]
+ -[DCAnalytics perfIdMap]
+ -[DCAnalytics perfLog]
+ -[DCAnalytics sendPayload:forEvent:withError:]
+ -[DCAnalytics sendPayload:forEvent:withError:].cold.1
+ -[DCAnalytics sendPerformanceForCategory:eventType:]
+ -[DCAnalytics sendPerformanceForCategory:eventType:].cold.1
+ -[DCAnalytics sendPerformanceForCategory:eventType:].cold.2
+ -[DCAnalytics sendPerformanceForCategory:eventType:].cold.3
+ -[DCAnalytics setIsNetworkReachable:]
+ -[DCAnalytics setPerfIdMap:]
+ -[DCAnalytics setPerfLog:]
+ -[DCAppAttestController .cxx_destruct]
+ -[DCAppAttestController appAttestType]
+ -[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]
+ -[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:].cold.1
+ -[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:].cold.2
+ -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]
+ -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:].cold.1
+ -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:].cold.2
+ -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:].cold.3
+ -[DCAppAttestController dispatchCompletionHandler:ontoQueue:]
+ -[DCAppAttestController dispatchCompletionHandler:ontoQueue:].cold.1
+ -[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]
+ -[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:].cold.1
+ -[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:].cold.2
+ -[DCAppAttestController generateKeyWithTeamIdentifier:completion:]
+ -[DCAppAttestController initWithType:]
+ -[DCAppAttestController isSupportedWithError:]
+ -[DCAppAttestController isSupported]
+ -[DCAppAttestController isSupported].cold.1
+ -[DCAppAttestController legacyUserDefaults]
+ -[DCAppAttestController loadAppUUID]
+ -[DCAppAttestController rewrapAsDCError:]
+ -[DCAppAttestController rewrapAsDCError:].cold.1
+ -[DCAppAttestController saveAppUUID:]
+ -[DCAppAttestController setAppAttestType:]
+ -[DCAppAttestController setLegacyUserDefaults:]
+ -[DCAppAttestController setUserDefaults:]
+ -[DCAppAttestController sign:withKey:completionHandler:]
+ -[DCAppAttestController sign:withKey:completionHandler:].cold.1
+ -[DCAppAttestController userDefaults]
+ -[DCAppAttestDeviceService .cxx_destruct]
+ -[DCAppAttestDeviceService appAttestController]
+ -[DCAppAttestDeviceService attestKey:clientDataHash:options:completionHandler:]
+ -[DCAppAttestDeviceService attestKey:clientDataHash:options:completionHandler:].cold.1
+ -[DCAppAttestDeviceService attestKey:clientDataHash:options:completionHandler:].cold.2
+ -[DCAppAttestDeviceService hasEntitlement]
+ -[DCAppAttestDeviceService hasEntitlement].cold.1
+ -[DCAppAttestDeviceService isSupported]
+ -[DCAppAttestDeviceService isSupported].cold.1
+ -[DCAppAttestDeviceService setAppAttestController:]
+ -[DCAppAttestService .cxx_destruct]
+ -[DCAppAttestService appAttestController]
+ -[DCAppAttestService setAppAttestController:]
+ -[DCAppAttestServicePriv .cxx_destruct]
+ -[DCAppAttestServicePriv appAttestController]
+ -[DCAppAttestServicePriv attestKey:teamIdentifier:clientDataHash:completionHandler:]
+ -[DCAppAttestServicePriv generateAssertion:teamIdentifier:clientDataHash:completionHandler:]
+ -[DCAppAttestServicePriv generateKeyWithTeamIdentifier:completion:]
+ -[DCAppAttestServicePriv isSupported]
+ -[DCAppAttestServicePriv setAppAttestController:]
+ -[DCAppAttestServicePriv sign:withKey:completionHandler:]
+ -[DCAppAttestWebAuthService .cxx_destruct]
+ -[DCAppAttestWebAuthService appAttestController]
+ -[DCAppAttestWebAuthService attestKey:clientDataHash:authData:completionHandler:]
+ -[DCAppAttestWebAuthService attestKey:clientDataHash:authData:completionHandler:].cold.1
+ -[DCAppAttestWebAuthService attestKey:clientDataHash:authData:completionHandler:].cold.2
+ -[DCAppAttestWebAuthService hasEntitlement]
+ -[DCAppAttestWebAuthService hasEntitlement].cold.1
+ -[DCAppAttestWebAuthService isSupported]
+ -[DCAppAttestWebAuthService isSupported].cold.1
+ -[DCAppAttestWebAuthService setAppAttestController:]
+ -[DCDeviceMetadataDaemonConnection connLock]
+ -[DCDeviceMetadataDaemonConnection conn]
+ -[DCDeviceMetadataDaemonConnection connection].cold.1
+ -[DCDeviceMetadataDaemonConnection setConn:]
+ -[DCDeviceMetadataDaemonConnection setConnLock:]
+ DCLogSystem.log
+ DCLogSystem.onceToken
+ GCC_except_table19
+ GCC_except_table28
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table5
+ GCC_except_table53
+ OBJC_IVAR_$_DCAnalytics._isNetworkReachable
+ OBJC_IVAR_$_DCAnalytics._perfIdMap
+ OBJC_IVAR_$_DCAnalytics._perfLog
+ OBJC_IVAR_$_DCAppAttestController._appAttestType
+ OBJC_IVAR_$_DCAppAttestController._legacyUserDefaults
+ OBJC_IVAR_$_DCAppAttestController._userDefaults
+ OBJC_IVAR_$_DCAppAttestDeviceService._appAttestController
+ OBJC_IVAR_$_DCAppAttestService._appAttestController
+ OBJC_IVAR_$_DCAppAttestServicePriv._appAttestController
+ OBJC_IVAR_$_DCAppAttestWebAuthService._appAttestController
+ _AnalyticsSendEventLazy
+ _CFErrorCopyDescription
+ _OBJC_CLASS_$_CPNetworkObserver
+ _OBJC_CLASS_$_DCAnalytics
+ _OBJC_CLASS_$_DCAppAttestController
+ _OBJC_CLASS_$_DCAppAttestDeviceService
+ _OBJC_CLASS_$_DCAppAttestServicePriv
+ _OBJC_CLASS_$_DCAppAttestWebAuthService
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_DCAnalytics
+ _OBJC_METACLASS_$_DCAppAttestController
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
+ __39-[DCDevice _isSupportedReturningError:]_block_invoke.24
+ __46-[DCAppAttestController isSupportedWithError:]_block_invoke.92
+ __46-[DCAppAttestController isSupportedWithError:]_block_invoke.97
+ __46-[DCAppAttestController isSupportedWithError:]_block_invoke.cold.1
+ __46-[DCDeviceMetadataDaemonConnection connection]_block_invoke.7
+ __47-[DCDevice generateTokenWithCompletionHandler:]_block_invoke.21
+ __56-[DCAppAttestController sign:withKey:completionHandler:]_block_invoke.91
+ __66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke.24
+ __66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke.38
+ __83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.42
+ __83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.50
+ __91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.90
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.59
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.59.cold.1
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.60
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.69
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.69.cold.1
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.69.cold.2
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.73
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.73.cold.1
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.76
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.70
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.70.cold.1
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.cold.1
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.cold.2
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.cold.3
+ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_3.cold.1
+ __OBJC_$_CLASS_METHODS_DCAnalytics
+ __OBJC_$_CLASS_METHODS_DCAppAttestDeviceService
+ __OBJC_$_CLASS_METHODS_DCAppAttestServicePriv
+ __OBJC_$_CLASS_METHODS_DCAppAttestWebAuthService
+ __OBJC_$_CLASS_PROP_LIST_DCAppAttestDeviceService
+ __OBJC_$_CLASS_PROP_LIST_DCAppAttestServicePriv
+ __OBJC_$_CLASS_PROP_LIST_DCAppAttestWebAuthService
+ __OBJC_$_INSTANCE_METHODS_DCAnalytics
+ __OBJC_$_INSTANCE_METHODS_DCAppAttestController
+ __OBJC_$_INSTANCE_METHODS_DCAppAttestDeviceService
+ __OBJC_$_INSTANCE_METHODS_DCAppAttestServicePriv
+ __OBJC_$_INSTANCE_METHODS_DCAppAttestWebAuthService
+ __OBJC_$_INSTANCE_VARIABLES_DCAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_DCAppAttestController
+ __OBJC_$_INSTANCE_VARIABLES_DCAppAttestDeviceService
+ __OBJC_$_INSTANCE_VARIABLES_DCAppAttestService
+ __OBJC_$_INSTANCE_VARIABLES_DCAppAttestServicePriv
+ __OBJC_$_INSTANCE_VARIABLES_DCAppAttestWebAuthService
+ __OBJC_$_PROP_LIST_DCAnalytics
+ __OBJC_$_PROP_LIST_DCAppAttestController
+ __OBJC_$_PROP_LIST_DCAppAttestDeviceService
+ __OBJC_$_PROP_LIST_DCAppAttestServicePriv
+ __OBJC_$_PROP_LIST_DCAppAttestWebAuthService
+ __OBJC_$_PROP_LIST_DCDeviceMetadataDaemonConnection
+ __OBJC_CLASS_RO_$_DCAnalytics
+ __OBJC_CLASS_RO_$_DCAppAttestController
+ __OBJC_CLASS_RO_$_DCAppAttestDeviceService
+ __OBJC_CLASS_RO_$_DCAppAttestServicePriv
+ __OBJC_CLASS_RO_$_DCAppAttestWebAuthService
+ __OBJC_METACLASS_RO_$_DCAnalytics
+ __OBJC_METACLASS_RO_$_DCAppAttestController
+ __OBJC_METACLASS_RO_$_DCAppAttestDeviceService
+ __OBJC_METACLASS_RO_$_DCAppAttestServicePriv
+ __OBJC_METACLASS_RO_$_DCAppAttestWebAuthService
+ ___21+[DCAnalytics shared]_block_invoke
+ ___39+[DCAppAttestServicePriv sharedService]_block_invoke
+ ___41+[DCAppAttestDeviceService sharedService]_block_invoke
+ ___42+[DCAppAttestWebAuthService sharedService]_block_invoke
+ ___42-[DCAppAttestDeviceService hasEntitlement]_block_invoke
+ ___42-[DCAppAttestDeviceService hasEntitlement]_block_invoke_2
+ ___42-[DCAppAttestDeviceService hasEntitlement]_block_invoke_3
+ ___43-[DCAppAttestWebAuthService hasEntitlement]_block_invoke
+ ___43-[DCAppAttestWebAuthService hasEntitlement]_block_invoke_2
+ ___43-[DCAppAttestWebAuthService hasEntitlement]_block_invoke_3
+ ___46-[DCAnalytics sendPayload:forEvent:withError:]_block_invoke
+ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke
+ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke_2
+ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke_3
+ ___56-[DCAppAttestController sign:withKey:completionHandler:]_block_invoke
+ ___61-[DCAppAttestController dispatchCompletionHandler:ontoQueue:]_block_invoke
+ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke
+ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke_2
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke_2
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke_2
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke_3
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_3
+ ___DCLogSystem_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_41_e8_32s_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e5_v8?0l
+ ___block_descriptor_49_e8_32s40s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs48r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0i8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48s56s_e19_"NSDictionary"8?0l
+ ___block_descriptor_65_e8_32s40s48s56bs_e20_v20?0i8"NSError"12l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88r_e5_v8?0l
+ ___copy_helper_block_e8_32s
+ ___copy_helper_block_e8_32s40b48r
+ ___copy_helper_block_e8_32s40s
+ ___copy_helper_block_e8_32s40s48s56b
+ ___copy_helper_block_e8_32s40s48s56s
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b88r
+ ___destroy_helper_block_e8_32s40s
+ ___destroy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r
+ ___kCFBooleanTrue
+ __block_literal_global.27
+ __block_literal_global.39
+ __block_literal_global.81
+ __os_signpost_emit_with_name_impl
+ _copy_keychain_data
+ _delete_keychain_item
+ _delete_keychain_item_for_system_keychain
+ _kCFAllocatorDefault
+ _kDeviceAttestKeychainAccessGroup
+ _kDeviceAttestKeychainCertSuffix
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
+ _kSecUseSystemKeychainAlways
+ _kSecValueRef
+ _kWebAttestKeychainAccessGroup
+ _kWebAttestKeychainCertSuffix
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$addNetworkReachableObserver:selector:
+ _objc_msgSend$appAttestController
+ _objc_msgSend$appAttestType
+ _objc_msgSend$appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:
+ _objc_msgSend$appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:
+ _objc_msgSend$appAttestationCreateKeyWithTeamIdentifier:appUUID:completion:
+ _objc_msgSend$appAttestationDeviceAttestKey:useSystemKeychain:clientDataHash:options:completion:
+ _objc_msgSend$appAttestationDeviceIsSupportedWithCompletion:
+ _objc_msgSend$appAttestationPrivIsSupportedWithCompletion:
+ _objc_msgSend$appAttestationSign:appUUID:keyId:completion:
+ _objc_msgSend$appAttestationWebAttestKey:clientDataHash:authData:completion:
+ _objc_msgSend$appAttestationWebIsSupportedWithCompletion:
+ _objc_msgSend$attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:
+ _objc_msgSend$attestKey:teamIdentifier:clientDataHash:completionHandler:
+ _objc_msgSend$convertCategory:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$generateAssertion:teamIdentifier:clientDataHash:completionHandler:
+ _objc_msgSend$generateKeyWithTeamIdentifier:completion:
+ _objc_msgSend$hasEntitlement
+ _objc_msgSend$initWithType:
+ _objc_msgSend$isNetworkReachable
+ _objc_msgSend$isSupported
+ _objc_msgSend$isSupportedWithError:
+ _objc_msgSend$legacyUserDefaults
+ _objc_msgSend$loadAppUUID
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$perfIdMap
+ _objc_msgSend$perfLog
+ _objc_msgSend$removeNetworkReachableObserver:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$rewrapAsDCError:
+ _objc_msgSend$saveAppUUID:
+ _objc_msgSend$sendPayload:forEvent:withError:
+ _objc_msgSend$sendPerformanceForCategory:eventType:
+ _objc_msgSend$setAppAttestType:
+ _objc_msgSend$setIsNetworkReachable:
+ _objc_msgSend$shared
+ _objc_msgSend$sharedNetworkObserver
+ _objc_msgSend$sign:withKey:completionHandler:
+ _objc_msgSend$stringWithFormat:
+ _objc_retainBlock
+ _objc_terminate
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _store_keychain_item
+ shared.onceToken
+ shared.shared
- -[DCAppAttestService _isSupportedReturningError:]
- -[DCAppAttestService _loadAppUUID]
- -[DCAppAttestService _rewrapAsDCError:]
- -[DCAppAttestService _rewrapAsDCError:].cold.1
- -[DCAppAttestService _saveAppUUID:]
- -[DCAppAttestService dispatchCompletionHandler:ontoQueue:]
- -[DCAppAttestService isSupported].cold.1
- GCC_except_table15
- GCC_except_table25
- GCC_except_table31
- _DCLogSystem.log
- _DCLogSystem.onceToken
- __39-[DCDevice _isSupportedReturningError:]_block_invoke.6
- __46-[DCDeviceMetadataDaemonConnection connection]_block_invoke.3
- __47-[DCDevice generateTokenWithCompletionHandler:]_block_invoke.4
- __49-[DCAppAttestService _isSupportedReturningError:]_block_invoke.3
- __49-[DCAppAttestService _isSupportedReturningError:]_block_invoke.cold.1
- __55-[DCAppAttestService generateKeyWithCompletionHandler:]_block_invoke.9
- __DCLogSystem
- ___49-[DCAppAttestService _isSupportedReturningError:]_block_invoke
- ___55-[DCAppAttestService generateKeyWithCompletionHandler:]_block_invoke
- ___55-[DCAppAttestService generateKeyWithCompletionHandler:]_block_invoke_2
- ___58-[DCAppAttestService dispatchCompletionHandler:ontoQueue:]_block_invoke
- ___65-[DCAppAttestService attestKey:clientDataHash:completionHandler:]_block_invoke
- ___65-[DCAppAttestService attestKey:clientDataHash:completionHandler:]_block_invoke_2
- ___65-[DCAppAttestService attestKey:clientDataHash:completionHandler:]_block_invoke_3
- ___73-[DCAppAttestService generateAssertion:clientDataHash:completionHandler:]_block_invoke
- ___73-[DCAppAttestService generateAssertion:clientDataHash:completionHandler:]_block_invoke_2
- ___73-[DCAppAttestService generateAssertion:clientDataHash:completionHandler:]_block_invoke_3
- ____DCLogSystem_block_invoke
- ___block_descriptor_64_e8_32s40s48bs56r_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0l
- __os_log_debug_impl
- __os_log_error_impl
- _objc_msgSend$_loadAppUUID
- _objc_msgSend$_rewrapAsDCError:
- _objc_msgSend$_saveAppUUID:
CStrings:
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
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypeDefault."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypeDevice."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypePriv."
+ "%25s:%-5d Invalid usage, cannot use this method for AppAttestTypeWeb."
+ "%25s:%-5d Performance analytics disabled. { category=%@ }"
+ "%25s:%-5d Re-mapped error. { mapped=%@, internal=%@ }"
+ "%25s:%-5d Updated AUID for client connection. { auid=%d }"
+ "%@:%@:%d"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Core/DCAnalytics.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Core/DCAppAttestController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Core/DCDeviceMetadataDaemonConnection.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestDeviceService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestWebAuthService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheck/Source/Interfaces/Public/DCDevice.m"
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
+ "com.apple.tokengenerationinference.ajaxinferenceprovider"
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
+ "objectForKeyedSubscript:"
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
+ "v48@0:8^{__SecKey=}16@24@32@?40"
+ "v52@0:8@\"NSString\"16B24@\"NSData\"28@\"NSDictionary\"36@?<v@?i@\"NSError\">44"
+ "v52@0:8@16B24@28@36@?44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "v64@0:8@16@24@32@40@48@?56"
+ "web"
- "Dispatching completion handler onto calling queue. { queueLabel=%s }"
- "Remap to DCError (%@) <- (%@)\n"
- "Updated AUID for client connection. { auid=%d }"
- "XPCConnection failed with error: %@"
- "_loadAppUUID"
- "_rewrapAsDCError:"
- "_saveAppUUID:"
- "core"
- "isSupported error: %@"

```
