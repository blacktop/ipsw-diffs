## icloudMCCKit

> `/System/Library/PrivateFrameworks/icloudMCCKit.framework/Versions/A/icloudMCCKit`

```diff

-2024.3.10.1.0
-  __TEXT.__text: 0xb314
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x8c8
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x761
-  __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__oslogstring: 0x1094
+2024.5.19.0.0
+  __TEXT.__text: 0x15678
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_methlist: 0xaf4
+  __TEXT.__const: 0x28a
+  __TEXT.__cstring: 0x79f
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__oslogstring: 0x103c
+  __TEXT.__constg_swiftt: 0xac
+  __TEXT.__swift5_typeref: 0xa2
+  __TEXT.__swift5_fieldmd: 0x3c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x23
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x18
+  __TEXT.__swift5_types: 0xc
   __TEXT.__unwind_info: 0x390
-  __TEXT.__objc_classname: 0x175
-  __TEXT.__objc_methname: 0x176d
-  __TEXT.__objc_methtype: 0x6d2
-  __TEXT.__objc_stubs: 0xc00
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x130
+  __TEXT.__objc_classname: 0x15c
+  __TEXT.__objc_methname: 0x1763
+  __TEXT.__objc_methtype: 0x6d7
+  __TEXT.__objc_stubs: 0xbe0
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x550
+  __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x150
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x20c0
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x20
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__const: 0x408
+  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__objc_const: 0x18f0
+  __AUTH.__objc_data: 0x3d0
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__data: 0x320
+  __DATA.__bss: 0x330
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/Email.framework/Versions/A/Email
   - /System/Library/PrivateFrameworks/EmailAddressing.framework/Versions/A/EmailAddressing

   - /System/Library/PrivateFrameworks/EmailFoundation.framework/Versions/A/EmailFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A0C3FF9-C590-3B90-A7C9-B4795329B7A6
-  Functions: 332
-  Symbols:   821
-  CStrings:  590
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: ACAE86BA-73E4-3E32-851C-096E135BB74B
+  Functions: 339
+  Symbols:   880
+  CStrings:  562
 
Symbols:
+ +[MCCSecretAgentInterface XPCInterface].cold.1
+ -[MCCCategoryRulesController _checkConnection]
+ -[MCCCategoryRulesController _checkConnection].cold.1
+ -[MCCCategoryRulesController _checkConnection].cold.2
+ -[MCCCategoryRulesController dealloc].cold.1
+ -[MCCCategoryRulesController newOldCategoryTimestampsChanged:]
+ -[MCCCategoryRulesController notifyFullSyncCategoryOverrides:]
+ -[MCCCategoryRulesController notifyNewOldCategoryChange:timestamp:]
+ -[MCCCategoryRulesController setupReconnectTimer]
+ -[MCCCategoryRulesController syncAllCategoryOverrides:]
+ -[MCCSecretAgentController getPKCategoryForDomain:completion:]
+ -[MCCSecretAgentController isCategorizationSupportedForLocale:completion:]
+ -[MCCSecretAgentController notifyFullSyncCategoryOverrides:]
+ -[MCCSecretAgentController notifyNewOldCategoryChange:timestamp:]
+ -[MCCSecretAgentController notifyWebRule:]
+ -[MCCSecretAgentController syncNewOldCategoryTimestamps:]
+ -[RCOverrideRule initWithEmailAddress:displayName:overrideIdentifier:category:categoryUpdateTime:]
+ -[RCOverrideRule initWithEmailAddress:overrideIdentifier:category:categoryUpdateTime:]
+ -[RCOverrideRule initWithMessageIdHeader:appleRequestHeader:overrideIdentifier:category:categoryUpdateTime:]
+ -[RCOverrideRule overrideIdentifier]
+ -[RCOverrideRule setOverrideIdentifier:]
+ GCC_except_table0
+ GCC_except_table14
+ GCC_except_table18
+ GCC_except_table83
+ GCC_except_table88
+ GCC_except_table92
+ OBJC_IVAR_$_MCCCategoryRulesController.reconnectTimerQueue
+ OBJC_IVAR_$_RCOverrideRule._overrideIdentifier
+ _MCCLogSystem.cold.1
+ _NLLanguageAmharic
+ _NLLanguageArabic
+ _NLLanguageArmenian
+ _NLLanguageBulgarian
+ _NLLanguageBurmese
+ _NLLanguageCatalan
+ _NLLanguageCherokee
+ _NLLanguageCroatian
+ _NLLanguageCzech
+ _NLLanguageDanish
+ _NLLanguageDutch
+ _NLLanguageEnglish
+ _NLLanguageFinnish
+ _NLLanguageFrench
+ _NLLanguageGeorgian
+ _NLLanguageGerman
+ _NLLanguageGreek
+ _NLLanguageGujarati
+ _NLLanguageHebrew
+ _NLLanguageHindi
+ _NLLanguageHungarian
+ _NLLanguageIcelandic
+ _NLLanguageIndonesian
+ _NLLanguageItalian
+ _NLLanguageJapanese
+ _NLLanguageKannada
+ _NLLanguageKazakh
+ _NLLanguageKhmer
+ _NLLanguageKorean
+ _NLLanguageLao
+ _NLLanguageMalay
+ _NLLanguageMalayalam
+ _NLLanguageMarathi
+ _NLLanguageMongolian
+ _NLLanguageNorwegian
+ _NLLanguagePersian
+ _NLLanguagePolish
+ _NLLanguagePortuguese
+ _NLLanguagePunjabi
+ _NLLanguageRomanian
+ _NLLanguageRussian
+ _NLLanguageSimplifiedChinese
+ _NLLanguageSinhalese
+ _NLLanguageSlovak
+ _NLLanguageSpanish
+ _NLLanguageSwedish
+ _NLLanguageTamil
+ _NLLanguageTelugu
+ _NLLanguageThai
+ _NLLanguageTibetan
+ _NLLanguageTraditionalChinese
+ _NLLanguageTurkish
+ _NLLanguageUkrainian
+ _NLLanguageUndetermined
+ _NLLanguageUrdu
+ _NLLanguageVietnamese
+ _OBJC_CLASS_$__TtC12icloudMCCKit23LanguageDetectionHelper
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtC12icloudMCCKit23LanguageDetectionHelper
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __39-[MCCSecretAgentConnection _connection]_block_invoke.13
+ __42-[MCCSecretAgentController notifyWebRule:]_block_invoke.cold.1
+ __47-[MCCSecretAgentController pingWithcompletion:]_block_invoke.62
+ __49-[MCCCategoryRulesController setupReconnectTimer]_block_invoke.92
+ __49-[MCCCategoryRulesController setupReconnectTimer]_block_invoke.92.cold.1
+ __55-[MCCSecretAgentController isModelReadyWithCompletion:]_block_invoke.49
+ __56-[MCCSecretAgentController isPersonalDomain:completion:]_block_invoke.59
+ __57-[MCCSecretAgentController syncNewOldCategoryTimestamps:]_block_invoke.cold.1
+ __59-[MCCSecretAgentController listCertificatesWithCompletion:]_block_invoke.16
+ __59-[MCCSecretAgentController listCertificatesWithCompletion:]_block_invoke.16.cold.1
+ __59-[MCCSecretAgentController listCertificatesWithCompletion:]_block_invoke.17
+ __60-[MCCSecretAgentController notifyFullSyncCategoryOverrides:]_block_invoke.cold.1
+ __62-[MCCSecretAgentController getPKCategoryForDomain:completion:]_block_invoke.58
+ __62-[MCCSecretAgentController getPKCategoryForDomain:completion:]_block_invoke.58.cold.1
+ __62-[MCCSecretAgentController getPKCategoryForDomain:completion:]_block_invoke_2.cold.1
+ __62-[MCCSecretAgentController invokeModelDownloadWithCompletion:]_block_invoke.50
+ __63-[MCCSecretAgentController getBlackPearlVersionWithCompletion:]_block_invoke.60
+ __63-[MCCSecretAgentController getBlackPearlVersionWithCompletion:]_block_invoke.60.cold.1
+ __64-[MCCSecretAgentController listCertificatesForEmail:completion:]_block_invoke.20
+ __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.91
+ __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.91.cold.1
+ __65-[MCCSecretAgentController notifyNewOldCategoryChange:timestamp:]_block_invoke.cold.1
+ __65-[MCCSecretAgentController syncRecategorizationRules:completion:]_block_invoke.48
+ __65-[MCCSecretAgentController syncRecategorizationRules:completion:]_block_invoke.48.cold.1
+ __70-[MCCSecretAgentController generateCertificateWithContext:completion:]_block_invoke.11
+ __70-[MCCSecretAgentController generateCertificateWithContext:completion:]_block_invoke.11.cold.1
+ __70-[MCCSecretAgentController generateCertificateWithContext:completion:]_block_invoke.12
+ __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.43
+ __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.43.cold.1
+ __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.44
+ __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.44.cold.1
+ __72-[MCCSecretAgentController setSignIsEnabled:forEmailAddress:completion:]_block_invoke.36
+ __72-[MCCSecretAgentController setSignIsEnabled:forEmailAddress:completion:]_block_invoke.36.cold.1
+ __74-[MCCSecretAgentController clearAllUserOverridesWithTimestamp:completion:]_block_invoke.63
+ __74-[MCCSecretAgentController clearAllUserOverridesWithTimestamp:completion:]_block_invoke.63.cold.1
+ __75-[MCCSecretAgentController setEncryptIsEnabled:forEmailAddress:completion:]_block_invoke.35
+ __75-[MCCSecretAgentController setEncryptIsEnabled:forEmailAddress:completion:]_block_invoke.35.cold.1
+ __76-[MCCSecretAgentController refreshCertificateWithContext:certId:completion:]_block_invoke.39
+ __76-[MCCSecretAgentController refreshCertificateWithContext:certId:completion:]_block_invoke.39.cold.1
+ __77-[MCCSecretAgentController registerCategoryRulesCallbackListener:completion:]_block_invoke.47
+ __77-[MCCSecretAgentController registerCategoryRulesCallbackListener:completion:]_block_invoke.47.cold.1
+ __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.24
+ __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.24.cold.1
+ __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.25
+ __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.25.cold.1
+ __86-[MCCSecretAgentController setSigningAndEncrytingStatusTo:forEmailAddress:completion:]_block_invoke.37
+ __86-[MCCSecretAgentController setSigningAndEncrytingStatusTo:forEmailAddress:completion:]_block_invoke.37.cold.1
+ __89-[MCCSecretAgentController updateCertificateDefaultsForEmailAddress:certInfo:completion:]_block_invoke.38
+ __89-[MCCSecretAgentController updateCertificateDefaultsForEmailAddress:certInfo:completion:]_block_invoke.38.cold.1
+ __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.31
+ __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.31.cold.1
+ __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.32
+ __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.32.cold.1
+ __CLASS_METHODS__TtC12icloudMCCKit23LanguageDetectionHelper
+ __DATA__TtC12icloudMCCKit12LocaleHelper
+ __DATA__TtC12icloudMCCKit23LanguageDetectionHelper
+ __INSTANCE_METHODS__TtC12icloudMCCKit23LanguageDetectionHelper
+ __METACLASS_DATA__TtC12icloudMCCKit12LocaleHelper
+ __METACLASS_DATA__TtC12icloudMCCKit23LanguageDetectionHelper
+ ___42-[MCCSecretAgentController notifyWebRule:]_block_invoke
+ ___49-[MCCCategoryRulesController setupReconnectTimer]_block_invoke
+ ___57-[MCCSecretAgentController syncNewOldCategoryTimestamps:]_block_invoke
+ ___60-[MCCSecretAgentController notifyFullSyncCategoryOverrides:]_block_invoke
+ ___62-[MCCSecretAgentController getPKCategoryForDomain:completion:]_block_invoke
+ ___62-[MCCSecretAgentController getPKCategoryForDomain:completion:]_block_invoke_2
+ ___65-[MCCSecretAgentController notifyNewOldCategoryChange:timestamp:]_block_invoke
+ ___chkstk_darwin
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __block_literal_global.65
+ __block_literal_global.67
+ __block_literal_global.69
+ __block_literal_global.71
+ __lock
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_icloudMCCKit
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_icloudMCCKit
+ _associated conformance So10NLLanguageaSHSCSQ
+ _associated conformance So10NLLanguageas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So10NLLanguageas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_allocWithZone
+ _objc_msgSend$_checkConnection
+ _objc_msgSend$categoryRulesController:didReceiveNewOldTimestamps:
+ _objc_msgSend$categoryRulesController:didReceiveSyncAllOverrideRules:
+ _objc_msgSend$getPKCategoryForDomain:completion:
+ _objc_msgSend$initWithEmailAddress:overrideIdentifier:category:categoryUpdateTime:
+ _objc_msgSend$isCategorizationSupportedFor:
+ _objc_msgSend$isValid
+ _objc_msgSend$notifyFullSyncCategoryOverrides:
+ _objc_msgSend$notifyNewOldCategoryChange:timestamp:
+ _objc_msgSend$notifyWebRule:
+ _objc_msgSend$setOverrideIdentifier:
+ _objc_msgSend$setupReconnectTimer
+ _objc_msgSend$syncNewOldCategoryTimestamps:
+ _objc_opt_self
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_getForeignTypeMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_lookUpClassMethod
+ _swift_once
+ _symbolic $sSY
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS
+ _symbolic So8NSObjectC
+ _symbolic So8NSStringC
+ _symbolic _____ 12icloudMCCKit12LocaleHelperC
+ _symbolic _____ 12icloudMCCKit23LanguageDetectionHelperC
+ _symbolic _____ So10NLLanguagea
+ _symbolic _____Sg 10Foundation6LocaleV12LanguageCodeV
+ _symbolic _____Sg 10Foundation6LocaleV6ScriptV
+ _symbolic _____Sg_ABt 10Foundation6LocaleV12LanguageCodeV
+ _symbolic _____Sg_ABt 10Foundation6LocaleV6ScriptV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So10NLLanguagea
- +[RCNativeRule supportsSecureCoding]
- +[RCWebRule supportsSecureCoding]
- -[MCCCategoryRulesController _checkConnectionWith:]
- -[MCCCategoryRulesController _checkConnectionWith:].cold.1
- -[MCCCategoryRulesController _checkConnectionWith:].cold.2
- -[MCCCategoryRulesController createRuleWithSender:category:lastModified:type:]
- -[MCCCategoryRulesController createRuleWithSender:category:lastModified:type:].cold.1
- -[MCCCategoryRulesController rulesChanged:]
- -[MCCCategoryRulesController sendPendingRules:]
- -[MCCSecretAgentController createWebRule:completion:]
- -[MCCSecretAgentController createWebRule:completion:].cold.1
- -[MCCSecretAgentController notifyWebRule:completion:]
- -[MCCSecretAgentController sendPendingRulesWithType:completion:]
- -[MCCSecretAgentController syncToWeb:]
- -[RCNativeRule .cxx_destruct]
- -[RCNativeRule category]
- -[RCNativeRule copyWithZone:]
- -[RCNativeRule encodeWithCoder:]
- -[RCNativeRule initWithCoder:]
- -[RCNativeRule messageRef]
- -[RCNativeRule setCategory:]
- -[RCNativeRule setMessageRef:]
- -[RCOverrideRule initWithEmailAddress:category:categoryUpdateTime:]
- -[RCOverrideRule initWithEmailAddress:displayName:category:categoryUpdateTime:]
- -[RCOverrideRule initWithMessageIdHeader:appleRequestHeader:category:categoryUpdateTime:]
- -[RCWebRule .cxx_destruct]
- -[RCWebRule category]
- -[RCWebRule copyWithZone:]
- -[RCWebRule description]
- -[RCWebRule encodeWithCoder:]
- -[RCWebRule initWithCoder:]
- -[RCWebRule initWithSender:category:lastModified:]
- -[RCWebRule lastModifiedDate]
- -[RCWebRule sender]
- -[RCWebRule setCategory:]
- -[RCWebRule setLastModifiedDate:]
- -[RCWebRule setSender:]
- GCC_except_table10
- GCC_except_table101
- GCC_except_table12
- GCC_except_table85
- GCC_except_table89
- GCC_except_table93
- GCC_except_table97
- OBJC_IVAR_$_RCNativeRule._category
- OBJC_IVAR_$_RCNativeRule._messageRef
- OBJC_IVAR_$_RCWebRule._category
- OBJC_IVAR_$_RCWebRule._lastModifiedDate
- OBJC_IVAR_$_RCWebRule._sender
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_RCNativeRule
- _OBJC_CLASS_$_RCWebRule
- _OBJC_METACLASS_$_RCNativeRule
- _OBJC_METACLASS_$_RCWebRule
- _OUTLINED_FUNCTION_3
- __38-[MCCSecretAgentController syncToWeb:]_block_invoke.cold.1
- __39-[MCCSecretAgentConnection _connection]_block_invoke.3
- __47-[MCCCategoryRulesController sendPendingRules:]_block_invoke.cold.1
- __47-[MCCSecretAgentController pingWithcompletion:]_block_invoke.60
- __53-[MCCSecretAgentController createWebRule:completion:]_block_invoke.43
- __53-[MCCSecretAgentController createWebRule:completion:]_block_invoke.43.cold.1
- __53-[MCCSecretAgentController createWebRule:completion:]_block_invoke.44
- __53-[MCCSecretAgentController createWebRule:completion:]_block_invoke.44.cold.1
- __53-[MCCSecretAgentController notifyWebRule:completion:]_block_invoke.45
- __53-[MCCSecretAgentController notifyWebRule:completion:]_block_invoke.45.cold.1
- __53-[MCCSecretAgentController notifyWebRule:completion:]_block_invoke_2.cold.1
- __55-[MCCSecretAgentController isModelReadyWithCompletion:]_block_invoke.47
- __56-[MCCSecretAgentController isPersonalDomain:completion:]_block_invoke.58
- __59-[MCCSecretAgentController listCertificatesWithCompletion:]_block_invoke.6
- __59-[MCCSecretAgentController listCertificatesWithCompletion:]_block_invoke.6.cold.1
- __59-[MCCSecretAgentController listCertificatesWithCompletion:]_block_invoke.7
- __62-[MCCSecretAgentController invokeModelDownloadWithCompletion:]_block_invoke.48
- __63-[MCCSecretAgentController getBlackPearlVersionWithCompletion:]_block_invoke.59
- __63-[MCCSecretAgentController getBlackPearlVersionWithCompletion:]_block_invoke.59.cold.1
- __64-[MCCSecretAgentController listCertificatesForEmail:completion:]_block_invoke.10
- __64-[MCCSecretAgentController sendPendingRulesWithType:completion:]_block_invoke.46
- __64-[MCCSecretAgentController sendPendingRulesWithType:completion:]_block_invoke.46.cold.1
- __64-[MCCSecretAgentController sendPendingRulesWithType:completion:]_block_invoke_2.cold.1
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.74
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.74.cold.1
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.74.cold.2
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.75
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.75.cold.1
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.75.cold.2
- __65-[MCCCategoryRulesController listener:shouldAcceptNewConnection:]_block_invoke.75.cold.3
- __65-[MCCSecretAgentController syncRecategorizationRules:completion:]_block_invoke.38
- __65-[MCCSecretAgentController syncRecategorizationRules:completion:]_block_invoke.38.cold.1
- __70-[MCCSecretAgentController generateCertificateWithContext:completion:]_block_invoke.1
- __70-[MCCSecretAgentController generateCertificateWithContext:completion:]_block_invoke.1.cold.1
- __70-[MCCSecretAgentController generateCertificateWithContext:completion:]_block_invoke.2
- __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.33
- __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.33.cold.1
- __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.34
- __71-[MCCSecretAgentController predictCommerceEmailWithContext:completion:]_block_invoke.34.cold.1
- __72-[MCCSecretAgentController setSignIsEnabled:forEmailAddress:completion:]_block_invoke.26
- __72-[MCCSecretAgentController setSignIsEnabled:forEmailAddress:completion:]_block_invoke.26.cold.1
- __74-[MCCSecretAgentController clearAllUserOverridesWithTimestamp:completion:]_block_invoke.61
- __74-[MCCSecretAgentController clearAllUserOverridesWithTimestamp:completion:]_block_invoke.61.cold.1
- __75-[MCCSecretAgentController setEncryptIsEnabled:forEmailAddress:completion:]_block_invoke.25
- __75-[MCCSecretAgentController setEncryptIsEnabled:forEmailAddress:completion:]_block_invoke.25.cold.1
- __76-[MCCCategoryRulesController notifyWebRuleWithSender:category:lastModified:]_block_invoke.cold.1
- __76-[MCCSecretAgentController refreshCertificateWithContext:certId:completion:]_block_invoke.29
- __76-[MCCSecretAgentController refreshCertificateWithContext:certId:completion:]_block_invoke.29.cold.1
- __77-[MCCSecretAgentController registerCategoryRulesCallbackListener:completion:]_block_invoke.37
- __77-[MCCSecretAgentController registerCategoryRulesCallbackListener:completion:]_block_invoke.37.cold.1
- __78-[MCCCategoryRulesController createRuleWithSender:category:lastModified:type:]_block_invoke.cold.1
- __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.14
- __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.14.cold.1
- __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.15
- __86-[MCCSecretAgentController fetchSigningAndEncryptingStatusForEmailAddress:completion:]_block_invoke.15.cold.1
- __86-[MCCSecretAgentController setSigningAndEncrytingStatusTo:forEmailAddress:completion:]_block_invoke.27
- __86-[MCCSecretAgentController setSigningAndEncrytingStatusTo:forEmailAddress:completion:]_block_invoke.27.cold.1
- __89-[MCCSecretAgentController updateCertificateDefaultsForEmailAddress:certInfo:completion:]_block_invoke.28
- __89-[MCCSecretAgentController updateCertificateDefaultsForEmailAddress:certInfo:completion:]_block_invoke.28.cold.1
- __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.21
- __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.21.cold.1
- __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.22
- __93-[MCCSecretAgentController fetchSigningAndEncrytionMessagesStatusForEmailAddress:completion:]_block_invoke.22.cold.1
- __OBJC_$_CLASS_METHODS_RCNativeRule
- __OBJC_$_CLASS_METHODS_RCWebRule
- __OBJC_$_CLASS_PROP_LIST_RCNativeRule
- __OBJC_$_CLASS_PROP_LIST_RCWebRule
- __OBJC_$_INSTANCE_METHODS_RCNativeRule
- __OBJC_$_INSTANCE_METHODS_RCWebRule
- __OBJC_$_INSTANCE_VARIABLES_RCNativeRule
- __OBJC_$_INSTANCE_VARIABLES_RCWebRule
- __OBJC_$_PROP_LIST_RCNativeRule
- __OBJC_$_PROP_LIST_RCWebRule
- __OBJC_CLASS_PROTOCOLS_$_RCNativeRule
- __OBJC_CLASS_PROTOCOLS_$_RCWebRule
- __OBJC_CLASS_RO_$_RCNativeRule
- __OBJC_CLASS_RO_$_RCWebRule
- __OBJC_METACLASS_RO_$_RCNativeRule
- __OBJC_METACLASS_RO_$_RCWebRule
- ___38-[MCCSecretAgentController syncToWeb:]_block_invoke
- ___47-[MCCCategoryRulesController sendPendingRules:]_block_invoke
- ___53-[MCCSecretAgentController createWebRule:completion:]_block_invoke
- ___53-[MCCSecretAgentController notifyWebRule:completion:]_block_invoke
- ___53-[MCCSecretAgentController notifyWebRule:completion:]_block_invoke_2
- ___64-[MCCSecretAgentController sendPendingRulesWithType:completion:]_block_invoke
- ___64-[MCCSecretAgentController sendPendingRulesWithType:completion:]_block_invoke_2
- ___76-[MCCCategoryRulesController notifyWebRuleWithSender:category:lastModified:]_block_invoke
- ___78-[MCCCategoryRulesController createRuleWithSender:category:lastModified:type:]_block_invoke
- ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12l
- ___block_descriptor_40_e8_32s_e20_v16?0"MCCBgTimer"8l
- ___copy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r
- __block_literal_global.50
- _objc_msgSend$_checkConnectionWith:
- _objc_msgSend$addressWith:
- _objc_msgSend$categoryRulesController:didReceiveRules:
- _objc_msgSend$containsObject:
- _objc_msgSend$createWebRule:completion:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$initWithEmailAddress:category:categoryUpdateTime:
- _objc_msgSend$initWithSender:category:lastModified:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$lowercaseString
- _objc_msgSend$notifyWebRule:completion:
- _objc_msgSend$sendPendingRulesWithType:completion:
- _objc_msgSend$syncToWeb:
- _objc_opt_isKindOfClass
CStrings:
+ ""
+ "@56@0:8@16@24@32@40d48"
+ "B32@0:8@16d24"
+ "Failed to notify full sync with error: %{public}@"
+ "Failed to notify new/old category change with error: %{public}@"
+ "Failed to syncNewOldCategoryTimestamps with error: %{public}@"
+ "Get IAB category domain: Initiation of remote secret agent service getPKCategoryForDomain returned an error: %{public}@"
+ "Remote secret agent get PK category call with error: %{public}@"
+ "T@\"NSString\",C,N,V_overrideIdentifier"
+ "[%@ email:%@<%@> uuid:%@ msgId:%@ cat:%@ lastmod:%@ iungoID:%@]"
+ "[rules] Cancelling previous timer"
+ "[rules] Self does exist, firing timer"
+ "[rules] Self is deallocated, timer won't work"
+ "[rules] deallocated"
+ "_TtC12icloudMCCKit12LocaleHelper"
+ "_TtC12icloudMCCKit23LanguageDetectionHelper"
+ "_checkConnection"
+ "_overrideIdentifier"
+ "a"
+ "categoryRulesController:didReceiveNewOldTimestamps:"
+ "categoryRulesController:didReceiveSyncAllOverrideRules:"
+ "com.apple.icloudmcckit.reconnect.timer.queue"
+ "getPKCategoryForDomain:completion:"
+ "initWithEmailAddress:displayName:overrideIdentifier:category:categoryUpdateTime:"
+ "initWithEmailAddress:overrideIdentifier:category:categoryUpdateTime:"
+ "initWithMessageIdHeader:appleRequestHeader:overrideIdentifier:category:categoryUpdateTime:"
+ "isCategorizationSupportedFor:"
+ "isCategorizationSupportedForLocale: %d"
+ "isCategorizationSupportedForLocale:completion:"
+ "newOldCategoryTimestampsChanged:"
+ "notifyFullSyncCategoryOverrides:"
+ "notifyNewOldCategoryChange:timestamp:"
+ "notifyWebRule:"
+ "overrideIdentifier"
+ "reconnectTimerQueue"
+ "setOverrideIdentifier:"
+ "setupReconnectTimer"
+ "syncAllCategoryOverrides:"
+ "syncNewOldCategoryTimestamps:"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@\"RCOverrideRule\"16"
+ "v32@0:8@\"NSString\"16d24"
+ "v32@0:8@16d24"
- "@40@0:8@16@24d32"
- "B48@0:8@16@24d32@40"
- "Failed to add web rule with error: %{public}@"
- "Failed to send pending rules with error: %{public}@"
- "Incorrect class presented to rule-create"
- "Initiation of remote secret agent service to sync recategorization rules returned an error: %{public}@"
- "RCNativeRule"
- "RCWebRule"
- "Remote add web rule with error: %{public}@"
- "Remote notify web rule with error: %{public}@"
- "Remote send pending rules error: %{public}@"
- "Remote send pending rules failed with error: %{public}@"
- "T@\"NSDictionary\",C,N,V_messageRef"
- "T@\"NSDictionary\",C,N,V_sender"
- "T@\"NSNumber\",&,N,V_lastModifiedDate"
- "WebRule:{%@,%@}"
- "[%@ email:%@<%@> uuid:%@ msgId:%@ cat:%@ lastmod:%@]"
- "[rules] '%@' is not in standard form"
- "[rules] Cancelling reconnect timer"
- "[rules] Remote create-web-rule failed with error: %{public}@"
- "[rules] Remote notify-web-rule failed with error: %{public}@"
- "_checkConnectionWith:"
- "_lastModifiedDate"
- "_messageRef"
- "_sender"
- "categoryRulesController:didReceiveRules:"
- "containsObject:"
- "createRuleWithSender:category:lastModified:type:"
- "createWebRule:completion:"
- "dictionaryWithObjects:forKeys:count:"
- "email"
- "errorWithDomain:code:userInfo:"
- "initWithEmailAddress:category:categoryUpdateTime:"
- "initWithEmailAddress:displayName:category:categoryUpdateTime:"
- "initWithMessageIdHeader:appleRequestHeader:category:categoryUpdateTime:"
- "initWithSender:category:lastModified:"
- "isEqualToString:"
- "lastModifiedDate"
- "lowercaseString"
- "messageRef"
- "news"
- "notifyWebRule:completion:"
- "others"
- "personal"
- "promotions"
- "rules"
- "rulesChanged:"
- "sendPendingRules:"
- "sendPendingRulesWithType:completion:"
- "sender"
- "setLastModifiedDate:"
- "setMessageRef:"
- "setSender:"
- "social"
- "syncToWeb:"
- "transactions"
- "v16@?0@\"MCCBgTimer\"8"
- "v32@0:8@\"<NSObject>\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"RCWebRule\"16@?<v@?B@\"NSError\">24"

```
