## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x58
+1394.62.1.0.0
+  __TEXT.__text: 0x39f0
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x46c
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x3c2
+  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__oslogstring: 0x39
+  __TEXT.__constg_swiftt: 0x88
+  __TEXT.__swift5_typeref: 0x62
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__unwind_info: 0x1fc
+  __TEXT.__objc_classname: 0x10f
+  __TEXT.__objc_methname: 0xe6e
+  __TEXT.__objc_methtype: 0x46b
+  __TEXT.__objc_stubs: 0x880
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_catlist: 0x0
+  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_const: 0x15c8
+  __DATA_CONST.__objc_selrefs: 0x3f0
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__const: 0x130
+  __AUTH_CONST.__auth_got: 0x370
+  __AUTH.__objc_data: 0x470
+  __AUTH.__data: 0xc0
+  __DATA.__objc_classrefs: 0xb0
+  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_ivar: 0x40
+  __DATA.__data: 0x1f8
+  __DATA.__bss: 0x50
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 5C459814-5F46-38C9-8210-4CB3BB50919D
-  Functions: 0
-  Symbols:   2
-  CStrings:  0
+  - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: E4F1EFB7-B61C-3618-8D7D-2240F17F5FE5
+  Functions: 127
+  Symbols:   704
+  CStrings:  314
 
Symbols:
+ +[LACBackgroundTaskErrorBuilder _errorWithCode:userInfo:]
+ +[LACBackgroundTaskErrorBuilder errorWithCode:]
+ +[LACBackgroundTaskErrorBuilder errorWithCode:debugDescription:]
+ +[LACDarwinNotificationCenter sharedInstance]
+ +[LACError _errorWithCode:userInfo:]
+ +[LACError error:hasCode:]
+ +[LACError error:hasCode:subcode:]
+ +[LACError errorWithCode:]
+ +[LACError errorWithCode:debugDescription:]
+ +[LACLocalizationUtils decodeLocalizationKeyFromString:]
+ +[LACLocalizationUtils encodeLocalizationKey:]
+ +[LACLocalizationUtils isLocalizationKey:]
+ +[LACMobileGestalt _deviceClass]
+ +[LACMobileGestalt currentDeviceScreenSize]
+ +[LACMobileGestalt isIdiomPad]
+ +[LACMobileGestalt isIdiomPhone]
+ +[LACMobileGestalt isVirtualMachine]
+ +[LACMobileGestalt serialNumber]
+ +[LACUNManagerPool sharedInstance]
+ -[LACBackgroundTask .cxx_destruct]
+ -[LACBackgroundTask _completeTaskWithResult:]
+ -[LACBackgroundTask _invalidateRequestWatchdog]
+ -[LACBackgroundTask _setupRequestWatchdogWithTimeout:queue:]
+ -[LACBackgroundTask _startWorkerIfNeeded]
+ -[LACBackgroundTask delegate]
+ -[LACBackgroundTask initWithWorker:]
+ -[LACBackgroundTask runWithTimeout:completion:]
+ -[LACBackgroundTask runWithTimeout:queue:completion:]
+ -[LACBackgroundTask setDelegate:]
+ -[LACBackgroundTaskResult .cxx_destruct]
+ -[LACBackgroundTaskResult description]
+ -[LACBackgroundTaskResult error]
+ -[LACBackgroundTaskResult initWithError:]
+ -[LACBackgroundTaskResult initWithValue:]
+ -[LACBackgroundTaskResult initWithValue:error:]
+ -[LACBackgroundTaskResult isEqual:]
+ -[LACBackgroundTaskResult value]
+ -[LACDarwinNotificationCenter .cxx_destruct]
+ -[LACDarwinNotificationCenter _addSubscriptionToNotification:]
+ -[LACDarwinNotificationCenter _hasSubscriptionToNotification:]
+ -[LACDarwinNotificationCenter _notifyObserversAboutNotification:]
+ -[LACDarwinNotificationCenter _postNotification:]
+ -[LACDarwinNotificationCenter _startObservingNotification:]
+ -[LACDarwinNotificationCenter _stopObservingAllNotifications]
+ -[LACDarwinNotificationCenter addObserver:]
+ -[LACDarwinNotificationCenter addObserver:notification:]
+ -[LACDarwinNotificationCenter hasObserver:]
+ -[LACDarwinNotificationCenter init]
+ -[LACDarwinNotificationCenter listenToLaunchNotifications]
+ -[LACDarwinNotificationCenter observerCount]
+ -[LACDarwinNotificationCenter postNotification:]
+ -[LACDarwinNotificationCenter removeAllObservers]
+ -[LACDarwinNotificationCenter removeObserver:]
+ -[LACDarwinNotificationCenter stopListeningToAllNotifications]
+ -[LACServiceLocator .cxx_destruct]
+ -[LACServiceLocator init]
+ -[LACServiceLocator registerService:identifier:]
+ -[LACServiceLocator serviceWithIdentifier:]
+ -[LACTimer .cxx_destruct]
+ -[LACTimer _dispatchAfter:inQueue:repeat:block:]
+ -[LACTimer cancel]
+ -[LACTimer dispatchAfter:inQueue:block:]
+ -[LACTimer dispatchAfter:inQueue:repeat:block:]
+ -[LACTimer isRunning]
+ -[LACUNManager .cxx_destruct]
+ -[LACUNManager initWithBundleIdentifier:]
+ -[LACUNManager initWithBundleIdentifier:categoryIdentifier:]
+ -[LACUNManager notificationCenter]
+ -[LACUNManagerPool .cxx_destruct]
+ -[LACUNManagerPool init]
+ -[LACUNManagerPool setSharedInstances:]
+ -[LACUNManagerPool sharedInstanceWithBundleIdentifier:]
+ -[LACUNManagerPool sharedInstanceWithBundleIdentifier:categoryIdentifier:]
+ -[LACUNManagerPool sharedInstances]
+ -[LACXPCClientInfo auditToken]
+ -[LACXPCClientInfo initWithConnection:]
+ -[LACXPCClientInfo processId]
+ -[LACXPCClientInfo setAuditToken:]
+ -[LACXPCClientInfo setProcessId:]
+ <redacted>
+ GCC_except_table2
+ GCC_except_table3
+ GCC_except_table6
+ _$s10Foundation22_convertErrorToNSErrorySo0E0Cs0C0_pF
+ _$s10Foundation3URLV19_bridgeToObjectiveCSo5NSURLCyF
+ _$s10Foundation3URLV36_unconditionallyBridgeFromObjectiveCyACSo5NSURLCSgFZ
+ _$s10Foundation3URLVMa
+ _$s10Foundation3URLVMn
+ _$s10Foundation3URLVSgMD
+ _$s10Foundation3URLVSgWOh
+ _$s10Foundation4UUIDV10uuidStringSSvg
+ _$s10Foundation4UUIDVACycfC
+ _$s10Foundation4UUIDVMa
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCACycfC
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCACycfc
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCACycfcTo
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCMF
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCMa
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCMf
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCMn
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCMo
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCN
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCfD
+ _$s23LocalAuthenticationCoreMXM
+ _$s2os32getNullTerminatedUTF8PointerImpl_21storingStringOwnersInSVSS_SpyypGSgztF
+ _$s2os6LoggerV23LocalAuthenticationCoreE13notificationsACvgZ
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerVMa
+ _$s2os6LoggerVyACSo03OS_A4_logCcfC
+ _$sBOWV
+ _$sBoWV
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSSN
+ _$sSa10FoundationE19_bridgeToObjectiveCSo7NSArrayCyF
+ _$sSa10FoundationE36_unconditionallyBridgeFromObjectiveCySayxGSo7NSArrayCSgFZ
+ _$sSa11descriptionSSvg
+ _$sSo12LACUNManagerC23LocalAuthenticationCoreE16makeNotification33_AD50F919EBABD1A30556CF15258AB3F4LL4withSo09UNMutableF7ContentCSo30LACUNNotificationConfiguration_p_tFTf4nd_n
+ _$sSo12LACUNManagerC23LocalAuthenticationCoreE16postNotification33_AD50F919EBABD1A30556CF15258AB3F4LL4with7content5delay6center10completionySSSg_So21UNNotificationContentCSdSo06UNUserF6CenterCys5Error_pSgcSgtFTf4nnnnnd_n
+ _$sSo12LACUNManagerC23LocalAuthenticationCoreE16postNotification4with5delay10completionySo30LACUNNotificationConfiguration_p_Sdys5Error_pSgcSgtF
+ _$sSo12LACUNManagerC23LocalAuthenticationCoreE16postNotification4with5delay10completionySo30LACUNNotificationConfiguration_p_Sdys5Error_pSgcSgtFTo
+ _$sSo12LACUNManagerC23LocalAuthenticationCoreE19cancelNotifications15withIdentifiers10completionySaySSG_ys5Error_pSgcSgtF
+ _$sSo12LACUNManagerC23LocalAuthenticationCoreE19cancelNotifications15withIdentifiers10completionySaySSG_ys5Error_pSgcSgtFTo
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$sSo7NSErrorCSgIeyBy_s5Error_pSgIegg_TR
+ _$sSo7NSErrorCSgIeyBy_s5Error_pSgIegg_TRTA
+ _$sSo7NSErrorCSgIeyBy_s5Error_pSgIegg_TRTA.4
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCMF
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCMXX
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCMa
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCMf
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCMm
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCMn
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCN
+ _$sSo8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLCfD
+ _$sSo8NSBundleC23LocalAuthenticationCoreEMXE
+ _$sSo8NSObjectCSgMD
+ _$ss11_StringGutsV16_deconstructUTF87scratchyXlSg5owner_xSi6lengthSb11usesScratchSb15allocatedMemorytSwSg_ts8_PointerRzlFSV_Tgq5
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyF
+ _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsVN
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs5UInt8V_Tgq5
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tgq5Tf4nnd_n
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMD
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSS8UTF8ViewV_Tgq5
+ _$ss5Error_pSgIegg_SgWOe
+ _$ss5Error_pSgIegg_So7NSErrorCSgIeyBy_TR
+ _$ss5UInt8VMn
+ _$sypN
+ _$sypWOc
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _CFNotificationCenterRemoveEveryObserver
+ _CFNotificationCenterRemoveObserver
+ _LACBackgroundTaskErrorDomain
+ _LACDarwinNotificationCenterCallBack
+ _LACEntitlementSPI
+ _LACErrorCodeAuthenticationFailed
+ _LACErrorCodeBiometryNotEnrolled
+ _LACErrorCodeInternal
+ _LACErrorCodeNoAuthenticationRequired
+ _LACErrorCodeNotSupported
+ _LACErrorCodeParameter
+ _LACErrorCodePasscodeNotSet
+ _LACErrorCodeUserCancel
+ _LACErrorDomain
+ _LACErrorSubcodeKey
+ _LACErrorSubcodeNone
+ _LACErrorSubcodeUnsatisfiable
+ _LACLogNotifications
+ _LACLogNotifications.__logObj
+ _LACLogNotifications.onceToken
+ _LACLogTests
+ _LACLogTests.__logObj
+ _LACLogTests.onceToken
+ _LACPolicyDeviceOwnerAuthentication
+ _LACPolicyOptionAuthenticationReason
+ _LACPolicyOptionBiometryLockoutRecovery
+ _LACPolicyOptionBiometryLockoutRecoveryRetries
+ _LACPolicyOptionFallbackVisible
+ _LACPolicyOptionMaxBiometryFailures
+ _LACPolicyOptionNoFailureUI
+ _LACPolicyOptionNotInteractive
+ _LACPolicyOptionPasscodeTitle
+ _MGCopyAnswer
+ _MGGetBoolAnswer
+ _MGGetSInt32Answer
+ _NSDebugDescriptionErrorKey
+ _NSStringFromLACPolicy
+ _OBJC_CLASS_$_LACBackgroundTask
+ _OBJC_CLASS_$_LACBackgroundTaskErrorBuilder
+ _OBJC_CLASS_$_LACBackgroundTaskResult
+ _OBJC_CLASS_$_LACDarwinNotificationCenter
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACLocalizationUtils
+ _OBJC_CLASS_$_LACMobileGestalt
+ _OBJC_CLASS_$_LACServiceLocator
+ _OBJC_CLASS_$_LACTimer
+ _OBJC_CLASS_$_LACUNManager
+ _OBJC_CLASS_$_LACUNManagerPool
+ _OBJC_CLASS_$_LACXPCClientInfo
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationCategory
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNTimeIntervalNotificationTrigger
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_CLASS_$__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_LACBackgroundTask._currentHandler
+ _OBJC_IVAR_$_LACBackgroundTask._delegate
+ _OBJC_IVAR_$_LACBackgroundTask._isWorkerRunning
+ _OBJC_IVAR_$_LACBackgroundTask._watchdog
+ _OBJC_IVAR_$_LACBackgroundTask._worker
+ _OBJC_IVAR_$_LACBackgroundTaskResult._error
+ _OBJC_IVAR_$_LACBackgroundTaskResult._value
+ _OBJC_IVAR_$_LACDarwinNotificationCenter._observers
+ _OBJC_IVAR_$_LACDarwinNotificationCenter._subscriptions
+ _OBJC_IVAR_$_LACServiceLocator._services
+ _OBJC_IVAR_$_LACTimer._isRunning
+ _OBJC_IVAR_$_LACTimer._timer
+ _OBJC_IVAR_$_LACUNManager._notificationCenter
+ _OBJC_IVAR_$_LACUNManagerPool._sharedInstances
+ _OBJC_IVAR_$_LACXPCClientInfo._auditToken
+ _OBJC_IVAR_$_LACXPCClientInfo._processId
+ _OBJC_METACLASS_$_LACBackgroundTask
+ _OBJC_METACLASS_$_LACBackgroundTaskErrorBuilder
+ _OBJC_METACLASS_$_LACBackgroundTaskResult
+ _OBJC_METACLASS_$_LACDarwinNotificationCenter
+ _OBJC_METACLASS_$_LACError
+ _OBJC_METACLASS_$_LACLocalizationUtils
+ _OBJC_METACLASS_$_LACMobileGestalt
+ _OBJC_METACLASS_$_LACServiceLocator
+ _OBJC_METACLASS_$_LACTimer
+ _OBJC_METACLASS_$_LACUNManager
+ _OBJC_METACLASS_$_LACUNManagerPool
+ _OBJC_METACLASS_$_LACXPCClientInfo
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __DATA__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ __DATA__TtCE23LocalAuthenticationCoreCSo8NSBundleP33_06C5009961CF12380B02F6187ECF79568Sentinel
+ __METACLASS_DATA__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ __METACLASS_DATA__TtCE23LocalAuthenticationCoreCSo8NSBundleP33_06C5009961CF12380B02F6187ECF79568Sentinel
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_LACBackgroundTaskErrorBuilder
+ __OBJC_$_CLASS_METHODS_LACDarwinNotificationCenter
+ __OBJC_$_CLASS_METHODS_LACError
+ __OBJC_$_CLASS_METHODS_LACLocalizationUtils
+ __OBJC_$_CLASS_METHODS_LACMobileGestalt
+ __OBJC_$_CLASS_METHODS_LACUNManagerPool
+ __OBJC_$_CLASS_PROP_LIST_LACDarwinNotificationCenter
+ __OBJC_$_INSTANCE_METHODS_LACBackgroundTask
+ __OBJC_$_INSTANCE_METHODS_LACBackgroundTaskResult
+ __OBJC_$_INSTANCE_METHODS_LACDarwinNotificationCenter
+ __OBJC_$_INSTANCE_METHODS_LACServiceLocator
+ __OBJC_$_INSTANCE_METHODS_LACTimer
+ __OBJC_$_INSTANCE_METHODS_LACUNManager(Base)
+ __OBJC_$_INSTANCE_METHODS_LACUNManagerPool
+ __OBJC_$_INSTANCE_METHODS_LACXPCClientInfo
+ __OBJC_$_INSTANCE_METHODS__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ __OBJC_$_INSTANCE_VARIABLES_LACBackgroundTask
+ __OBJC_$_INSTANCE_VARIABLES_LACBackgroundTaskResult
+ __OBJC_$_INSTANCE_VARIABLES_LACDarwinNotificationCenter
+ __OBJC_$_INSTANCE_VARIABLES_LACServiceLocator
+ __OBJC_$_INSTANCE_VARIABLES_LACTimer
+ __OBJC_$_INSTANCE_VARIABLES_LACUNManager
+ __OBJC_$_INSTANCE_VARIABLES_LACUNManagerPool
+ __OBJC_$_INSTANCE_VARIABLES_LACXPCClientInfo
+ __OBJC_$_PROP_LIST_LACBackgroundTask
+ __OBJC_$_PROP_LIST_LACBackgroundTaskResult
+ __OBJC_$_PROP_LIST_LACDarwinNotificationCenter
+ __OBJC_$_PROP_LIST_LACServiceLocator
+ __OBJC_$_PROP_LIST_LACTimer
+ __OBJC_$_PROP_LIST_LACUNManager
+ __OBJC_$_PROP_LIST_LACUNManagerPool
+ __OBJC_$_PROP_LIST_LACXPCClientInfo
+ __OBJC_$_PROP_LIST_LACXPCClientInfo.62
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDarwinNotificationCenter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACServiceLocator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACXPCClientInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UNUserNotificationCenterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDarwinNotificationCenter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACServiceLocator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACXPCClientInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UNUserNotificationCenterDelegate
+ __OBJC_$_PROTOCOL_REFS_LACDarwinNotificationCenter
+ __OBJC_$_PROTOCOL_REFS_LACServiceLocator
+ __OBJC_$_PROTOCOL_REFS_LACXPCClientInfo
+ __OBJC_$_PROTOCOL_REFS_UNUserNotificationCenterDelegate
+ __OBJC_CLASS_PROTOCOLS_$_LACDarwinNotificationCenter
+ __OBJC_CLASS_PROTOCOLS_$_LACServiceLocator
+ __OBJC_CLASS_PROTOCOLS_$_LACUNManager
+ __OBJC_CLASS_PROTOCOLS_$_LACXPCClientInfo
+ __OBJC_CLASS_RO_$_LACBackgroundTask
+ __OBJC_CLASS_RO_$_LACBackgroundTaskErrorBuilder
+ __OBJC_CLASS_RO_$_LACBackgroundTaskResult
+ __OBJC_CLASS_RO_$_LACDarwinNotificationCenter
+ __OBJC_CLASS_RO_$_LACError
+ __OBJC_CLASS_RO_$_LACLocalizationUtils
+ __OBJC_CLASS_RO_$_LACMobileGestalt
+ __OBJC_CLASS_RO_$_LACServiceLocator
+ __OBJC_CLASS_RO_$_LACTimer
+ __OBJC_CLASS_RO_$_LACUNManager
+ __OBJC_CLASS_RO_$_LACUNManagerPool
+ __OBJC_CLASS_RO_$_LACXPCClientInfo
+ __OBJC_LABEL_PROTOCOL_$_LACDarwinNotificationCenter
+ __OBJC_LABEL_PROTOCOL_$_LACServiceLocator
+ __OBJC_LABEL_PROTOCOL_$_LACXPCClientInfo
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_UNUserNotificationCenterDelegate
+ __OBJC_METACLASS_RO_$_LACBackgroundTask
+ __OBJC_METACLASS_RO_$_LACBackgroundTaskErrorBuilder
+ __OBJC_METACLASS_RO_$_LACBackgroundTaskResult
+ __OBJC_METACLASS_RO_$_LACDarwinNotificationCenter
+ __OBJC_METACLASS_RO_$_LACError
+ __OBJC_METACLASS_RO_$_LACLocalizationUtils
+ __OBJC_METACLASS_RO_$_LACMobileGestalt
+ __OBJC_METACLASS_RO_$_LACServiceLocator
+ __OBJC_METACLASS_RO_$_LACTimer
+ __OBJC_METACLASS_RO_$_LACUNManager
+ __OBJC_METACLASS_RO_$_LACUNManagerPool
+ __OBJC_METACLASS_RO_$_LACXPCClientInfo
+ __OBJC_PROTOCOL_$_LACDarwinNotificationCenter
+ __OBJC_PROTOCOL_$_LACServiceLocator
+ __OBJC_PROTOCOL_$_LACXPCClientInfo
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_UNUserNotificationCenterDelegate
+ __Unwind_Resume
+ ___32+[LACMobileGestalt _deviceClass]_block_invoke
+ ___34+[LACUNManagerPool sharedInstance]_block_invoke
+ ___40-[LACTimer dispatchAfter:inQueue:block:]_block_invoke
+ ___41-[LACBackgroundTask _startWorkerIfNeeded]_block_invoke
+ ___45+[LACDarwinNotificationCenter sharedInstance]_block_invoke
+ ___58-[LACDarwinNotificationCenter listenToLaunchNotifications]_block_invoke
+ ___60-[LACBackgroundTask _setupRequestWatchdogWithTimeout:queue:]_block_invoke
+ ___60-[LACUNManager initWithBundleIdentifier:categoryIdentifier:]_block_invoke
+ ___CFConstantStringClassReference
+ ___LACLogNotifications_block_invoke
+ ___LACLogTests_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32w_e33_v16?0"LACBackgroundTaskResult"8lw32l8
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e31_"UNUserNotificationCenter"8?0ls32l8s40l8s48l8
+ ___block_literal_global
+ ___block_literal_global.4
+ ___chkstk_darwin
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __deviceClass.deviceClass
+ __deviceClass.onceToken
+ __dispatch_main_q
+ __dispatch_source_type_timer
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreGraphics_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_LocalAuthenticationCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_LocalAuthenticationCore
+ __swift_stdlib_malloc_size
+ __xpc_event_key_name
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _dispatch_activate
+ _dispatch_once
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_source_testcancel
+ _dispatch_time
+ _getpid
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_alloc
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend
+ _objc_msgSend$_addSubscriptionToNotification:
+ _objc_msgSend$_completeTaskWithResult:
+ _objc_msgSend$_deviceClass
+ _objc_msgSend$_dispatchAfter:inQueue:repeat:block:
+ _objc_msgSend$_errorWithCode:userInfo:
+ _objc_msgSend$_hasSubscriptionToNotification:
+ _objc_msgSend$_invalidateRequestWatchdog
+ _objc_msgSend$_notifyObserversAboutNotification:
+ _objc_msgSend$_postNotification:
+ _objc_msgSend$_setupRequestWatchdogWithTimeout:queue:
+ _objc_msgSend$_startObservingNotification:
+ _objc_msgSend$_startWorkerIfNeeded
+ _objc_msgSend$_stopObservingAllNotifications
+ _objc_msgSend$addObject:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$auditToken
+ _objc_msgSend$backgroundTask:didCompleteTaskWithResult:
+ _objc_msgSend$cancel
+ _objc_msgSend$categoryWithIdentifier:actions:intentIdentifiers:options:
+ _objc_msgSend$code
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$delegate
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dispatchAfter:inQueue:block:
+ _objc_msgSend$domain
+ _objc_msgSend$error
+ _objc_msgSend$error:hasCode:subcode:
+ _objc_msgSend$errorWithCode:
+ _objc_msgSend$errorWithCode:debugDescription:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithBundleIdentifier:categoryIdentifier:
+ _objc_msgSend$initWithError:
+ _objc_msgSend$initWithValue:error:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isLocalizationKey:
+ _objc_msgSend$isRunning
+ _objc_msgSend$length
+ _objc_msgSend$notificationCenter:didReceiveNotification:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$runWithTimeout:queue:completion:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setNotificationCategories:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setSharedInstances:
+ _objc_msgSend$setWantsNotificationResponsesDelivered
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$sharedInstanceWithBundleIdentifier:categoryIdentifier:
+ _objc_msgSend$sharedInstances
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$strongToWeakObjectsMapTable
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$userInfo
+ _objc_msgSend$value
+ _objc_msgSend$weakObjectsHashTable
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_new
+ _objc_opt_self
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeStrong
+ _objc_storeWeak
+ _os_log_create
+ _os_log_type_enabled
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_getObjCClassFromMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSBundleC
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 23LocalAuthenticationCore19LACLocalizedStringsC
+ _symbolic _____ So8NSBundleC23LocalAuthenticationCoreE8Sentinel33_06C5009961CF12380B02F6187ECF7956LLC
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
CStrings:
+ "\x01"
+ "\x02"
+ "\x03"
+ "#16@0:8"
+ "%@%@"
+ "%@-%@"
+ ".cxx_destruct"
+ "; "
+ "<%@ %p; %@>"
+ "<UNKNOWN>"
+ "@"
+ "@\"<LACBackgroundTaskDelegate>\""
+ "@\"LACTimer\""
+ "@\"NSError\""
+ "@\"NSHashTable\""
+ "@\"NSMapTable\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableSet\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSString\"16@0:8"
+ "@\"UNUserNotificationCenter\""
+ "@\"UNUserNotificationCenter\"8@?0"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSString\"16"
+ "@24@0:8@16"
+ "@24@0:8@?16"
+ "@24@0:8q16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@32@0:8q16@24"
+ "@40@0:8:16@24@32"
+ "@?"
+ "A"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"<LACDarwinNotificationCenterObserver>\"16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@0:8^{__CFString=}16"
+ "B32@0:8@16q24"
+ "B40@0:8@16q24q32"
+ "Base"
+ "Cancelling notifications with identifiers: %s"
+ "DeviceClassNumber"
+ "Did receive notification %{public}@"
+ "Invalid worker"
+ "IsVirtualDevice"
+ "LACBackgroundTask"
+ "LACBackgroundTaskErrorBuilder"
+ "LACBackgroundTaskErrorDomain"
+ "LACBackgroundTaskResult"
+ "LACDarwinNotificationCenter"
+ "LACError"
+ "LACLocalizationUtils"
+ "LACMobileGestalt"
+ "LACPolicyDeviceOwnerAuthentication"
+ "LACServiceLocator"
+ "LACTimer"
+ "LACUNManager"
+ "LACUNManagerPool"
+ "LACXPCClientInfo"
+ "NSObject"
+ "Notifications"
+ "Posted notification with content: %@ identifier: %s"
+ "Q16@0:8"
+ "Request timed out"
+ "SerialNumber"
+ "Setting category identifier for notification: %s"
+ "Subcode"
+ "T#,R"
+ "T@\"<LACBackgroundTaskDelegate>\",W,N,V_delegate"
+ "T@\"LACDarwinNotificationCenter\",R,N"
+ "T@\"NSError\",R,N,V_error"
+ "T@\"NSMutableDictionary\",&,N,V_sharedInstances"
+ "T@\"NSString\",R,C"
+ "T@,R,N,V_value"
+ "TB,R,N"
+ "TQ,R"
+ "Tests"
+ "Ti,N,V_processId"
+ "Ti,R,N"
+ "Tq,R,N"
+ "T{?=[8I]},N,V_auditToken"
+ "T{?=[8I]},R,N"
+ "UNUserNotificationCenter instance is nil"
+ "UNUserNotificationCenterDelegate"
+ "Vv16@0:8"
+ "Will post %{public}@"
+ "^{_NSZone=}16@0:8"
+ "_TtC23LocalAuthenticationCore19LACLocalizedStrings"
+ "_TtCE23LocalAuthenticationCoreCSo8NSBundleP33_06C5009961CF12380B02F6187ECF79568Sentinel"
+ "__LAC_LOCALIZATION_KEY__"
+ "_addSubscriptionToNotification:"
+ "_auditToken"
+ "_completeTaskWithResult:"
+ "_currentHandler"
+ "_delegate"
+ "_deviceClass"
+ "_dispatchAfter:inQueue:repeat:block:"
+ "_error"
+ "_errorWithCode:userInfo:"
+ "_hasSubscriptionToNotification:"
+ "_invalidateRequestWatchdog"
+ "_isRunning"
+ "_isWorkerRunning"
+ "_notificationCenter"
+ "_notifyObserversAboutNotification:"
+ "_observers"
+ "_postNotification:"
+ "_processId"
+ "_services"
+ "_setupRequestWatchdogWithTimeout:queue:"
+ "_sharedInstances"
+ "_startObservingNotification:"
+ "_startWorkerIfNeeded"
+ "_stopObservingAllNotifications"
+ "_subscriptions"
+ "_timer"
+ "_value"
+ "_watchdog"
+ "_worker"
+ "addNotificationRequest:withCompletionHandler:"
+ "addObject:"
+ "addObserver:"
+ "addObserver:notification:"
+ "arrayWithObjects:count:"
+ "auditToken"
+ "autorelease"
+ "backgroundTask:didCompleteTaskWithResult:"
+ "body"
+ "cancel"
+ "cancelNotificationsWithIdentifiers:completion:"
+ "categoryIdentifier"
+ "categoryWithIdentifier:actions:intentIdentifiers:options:"
+ "class"
+ "code"
+ "com.apple.LocalAuthentication"
+ "com.apple.notifyd.matching"
+ "com.apple.private.CoreAuthentication.SPI"
+ "componentsJoinedByString:"
+ "conformsToProtocol:"
+ "containsObject:"
+ "copy"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "currentDeviceScreenSize"
+ "dealloc"
+ "debugDescription"
+ "decodeLocalizationKeyFromString:"
+ "default"
+ "defaultActionURL"
+ "delegate"
+ "description"
+ "dictionaryWithObjects:forKeys:count:"
+ "dispatchAfter:inQueue:block:"
+ "dispatchAfter:inQueue:repeat:block:"
+ "domain"
+ "encodeLocalizationKey:"
+ "error"
+ "error: %@"
+ "error:hasCode:"
+ "error:hasCode:subcode:"
+ "errorWithCode:"
+ "errorWithCode:debugDescription:"
+ "errorWithDomain:code:userInfo:"
+ "hasObserver:"
+ "hasPrefix:"
+ "hash"
+ "i"
+ "i16@0:8"
+ "iconForSystemImageNamed:"
+ "identifier"
+ "init"
+ "initWithBundleIdentifier:"
+ "initWithBundleIdentifier:categoryIdentifier:"
+ "initWithConnection:"
+ "initWithError:"
+ "initWithValue:"
+ "initWithValue:error:"
+ "initWithWorker:"
+ "integerValue"
+ "isEqual:"
+ "isEqualToString:"
+ "isIdiomPad"
+ "isIdiomPhone"
+ "isKindOfClass:"
+ "isLocalizationKey:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isRunning"
+ "isTimeSensitive"
+ "isVirtualMachine"
+ "length"
+ "listenToLaunchNotifications"
+ "main-screen-class"
+ "notificationCenter"
+ "notificationCenter:didReceiveNotification:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "observerCount"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "postNotification:"
+ "postNotificationWithConfiguration:delay:completion:"
+ "processId"
+ "processIdentifier"
+ "q16@0:8"
+ "registerService:identifier:"
+ "release"
+ "removeAllObjects"
+ "removeAllObservers"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "removeObject:"
+ "removeObserver:"
+ "removePendingNotificationRequestsWithIdentifiers:"
+ "requestWithIdentifier:content:trigger:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "runWithTimeout:completion:"
+ "runWithTimeout:queue:completion:"
+ "self"
+ "serialNumber"
+ "serviceWithIdentifier:"
+ "setAuditToken:"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setDefaultActionURL:"
+ "setDelegate:"
+ "setHasDefaultAction:"
+ "setIcon:"
+ "setInterruptionLevel:"
+ "setNotificationCategories:"
+ "setObject:forKey:"
+ "setObject:forKeyedSubscript:"
+ "setProcessId:"
+ "setSharedInstances:"
+ "setShouldBackgroundDefaultAction:"
+ "setShouldIgnoreDoNotDisturb:"
+ "setTitle:"
+ "setWantsNotificationResponsesDelivered"
+ "setWithObject:"
+ "sharedInstance"
+ "sharedInstanceWithBundleIdentifier:"
+ "sharedInstanceWithBundleIdentifier:categoryIdentifier:"
+ "sharedInstances"
+ "stopListeningToAllNotifications"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "strongToWeakObjectsMapTable"
+ "substringFromIndex:"
+ "superclass"
+ "systemIconName"
+ "title"
+ "triggerWithTimeInterval:repeats:"
+ "userInfo"
+ "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
+ "userNotificationCenter:openSettingsForNotification:"
+ "userNotificationCenter:willPresentNotification:withCompletionHandler:"
+ "v16@0:8"
+ "v16@?0@\"LACBackgroundTaskResult\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v20@0:8i16"
+ "v24@0:8@\"<LACDarwinNotificationCenterObserver>\"16"
+ "v24@0:8@16"
+ "v24@0:8^{__CFString=}16"
+ "v32@0:8@\"<LACDarwinNotificationCenterObserver>\"16^{__CFString=}24"
+ "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
+ "v32@0:8@16@\"NSString\"24"
+ "v32@0:8@16@24"
+ "v32@0:8@16@?24"
+ "v32@0:8@16^{__CFString=}24"
+ "v32@0:8d16@24"
+ "v32@0:8d16@?24"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@16d24@?32"
+ "v40@0:8d16@24@?32"
+ "v44@0:8d16@24B32@?36"
+ "v48@0:8{?=[8I]}16"
+ "v8@?0"
+ "value"
+ "value: %@"
+ "weakObjectsHashTable"
+ "zone"
+ "{?=\"val\"[8I]}"
+ "{?=[8I]}16@0:8"

```
