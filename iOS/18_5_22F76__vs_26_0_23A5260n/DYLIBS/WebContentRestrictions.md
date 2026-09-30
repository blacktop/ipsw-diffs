## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-19.4.2.0.0
-  __TEXT.__text: 0x8d14
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x350
+37.0.0.0.0
+  __TEXT.__text: 0xc434
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x79c
   __TEXT.__const: 0x504
-  __TEXT.__cstring: 0xb06
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__oslogstring: 0x93
+  __TEXT.__cstring: 0x12e6
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__oslogstring: 0x183
   __TEXT.__swift5_typeref: 0x10c
   __TEXT.__constg_swiftt: 0x220
   __TEXT.__swift5_reflstr: 0x107

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__eh_frame: 0x528
-  __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0xcb2
-  __TEXT.__objc_methtype: 0x194
-  __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__objc_classname: 0xf2
+  __TEXT.__objc_methname: 0x1a98
+  __TEXT.__objc_methtype: 0x32c
+  __TEXT.__objc_stubs: 0x17a0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b0
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x520
-  __AUTH_CONST.__const: 0x350
-  __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x7a8
+  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x78
+  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__const: 0x390
+  __AUTH_CONST.__cfstring: 0x14c0
+  __AUTH_CONST.__objc_const: 0xcf0
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x2c0
+  __AUTH.__objc_data: 0x360
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0xd8
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x198
   __DATA.__bss: 0x690
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: EE3443DB-5F6E-36CB-922A-BF5206740596
-  Functions: 218
-  Symbols:   1040
-  CStrings:  351
+  UUID: 8A2AE842-6482-330C-BF58-9533118639DB
+  Functions: 312
+  Symbols:   1387
+  CStrings:  706
 
Symbols:
+ +[WCRBlockPage _allowedWebSitesHTML:]
+ +[WCRBlockPage _css:]
+ +[WCRBlockPage _fileContentWithName:inLanguage:extension:]
+ +[WCRBlockPage _javascript:]
+ +[WCRBlockPage _xssSafeStringFromString:]
+ +[WCRBlockPage blockPageForUser:inLanguage:withUserVisibleURLString:withFormPostToURLString:withFormRestrictedPageURLString:withFormRestrictedPageTitle:withAllowedWebsites:isAllowedWebsitesOnlyBlock:isNetworkAccount:allowsOverrides:]
+ +[WCRBlockPage createBlockPageFromTemplate:inLanguage:withUserVisibleURLString:isAllowedWebsitesOnlyBlock:withAllowedWebsites:withFormPostToURLString:withFormRestrictedPageURLString:withFormRestrictedPageTitle:]
+ +[WCRBrowserEngineClient _allowList:]
+ +[WCRBrowserEngineClient _allowedWebsitesOnly:]
+ +[WCRBrowserEngineClient _allowedWebsitesOnlyList:]
+ +[WCRBrowserEngineClient _blockPageForURL:forUser:inLanguage:isAllowedWebsitesOnlyBlock:withAllowedWebsites:withAllowButton:]
+ +[WCRBrowserEngineClient _defaultUserSettingsPath]
+ +[WCRBrowserEngineClient _denyList:]
+ +[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]
+ +[WCRBrowserEngineClient _mode:]
+ +[WCRBrowserEngineClient _preferredLanguageForUserName:]
+ +[WCRBrowserEngineClient _shouldEvaluateURLsForConfigurationAtPath:]
+ +[WCRBrowserEngineClient _shouldShowAllowButton:]
+ +[WCRBrowserEngineClient allowURLWithFamilyControls:withCompletion:]
+ +[WCRBrowserEngineClient base64StringFromString:]
+ +[WCRBrowserEngineClient generateMacOSExemptURLList]
+ +[WCRBrowserEngineClient isLegacyExemptURL:]
+ +[WCRBrowserEngineClient shouldEvaluateURLsForConfigurationAtPath:]
+ +[WCRBrowserEngineClient shouldEvaluateURLs]
+ +[WCRBrowserEngineClient urlToFormattedString:]
+ +[WCRRemotePINEntryViewController exportedInterface]
+ +[WCRRemotePINEntryViewController serviceViewControllerInterface]
+ -[WCRAutoAssetClient _createInterestInAsset]
+ -[WCRAutoAssetClient _lockLocalAsset:]
+ -[WCRAutoAssetClient createInterestInAsset]
+ -[WCRAutoAssetClient startUsingLocalAsset:]
+ -[WCRBloomFilter _loadFilterResourcesFromLocalFallback]
+ -[WCRBloomFilter _loadFilterResourcesFromMobileAsset:]
+ -[WCRBloomFilter _loadFilterResourcesFromMobileAsset]
+ -[WCRBloomFilter _loadFilterResourcesWithMobileAssetPath:]
+ -[WCRBrowserEngineClient .cxx_destruct]
+ -[WCRBrowserEngineClient _performLazyInitialization]
+ -[WCRBrowserEngineClient _reloadConfiguration]
+ -[WCRBrowserEngineClient allowList]
+ -[WCRBrowserEngineClient allowURL:withCompletion:]
+ -[WCRBrowserEngineClient allowURLCompletion]
+ -[WCRBrowserEngineClient allowedWebsitesOnlyList]
+ -[WCRBrowserEngineClient bloomFilter]
+ -[WCRBrowserEngineClient configurationPath]
+ -[WCRBrowserEngineClient denyList]
+ -[WCRBrowserEngineClient evaluateURL:withCompletion:]
+ -[WCRBrowserEngineClient evaluateURL:withCompletion:onCompletionQueue:]
+ -[WCRBrowserEngineClient evaluationQueue]
+ -[WCRBrowserEngineClient initWithConfigurationAtPath:]
+ -[WCRBrowserEngineClient init]
+ -[WCRBrowserEngineClient language]
+ -[WCRBrowserEngineClient macOSExemptURLList]
+ -[WCRBrowserEngineClient mode]
+ -[WCRBrowserEngineClient remoteViewController]
+ -[WCRBrowserEngineClient requestAllowListAuthenticationForURL:withCompletion:]
+ -[WCRBrowserEngineClient setAllowList:]
+ -[WCRBrowserEngineClient setAllowURLCompletion:]
+ -[WCRBrowserEngineClient setAllowedWebsitesOnlyList:]
+ -[WCRBrowserEngineClient setBloomFilter:]
+ -[WCRBrowserEngineClient setConfigurationPath:]
+ -[WCRBrowserEngineClient setDenyList:]
+ -[WCRBrowserEngineClient setEvaluationQueue:]
+ -[WCRBrowserEngineClient setLanguage:]
+ -[WCRBrowserEngineClient setMacOSExemptURLList:]
+ -[WCRBrowserEngineClient setMode:]
+ -[WCRBrowserEngineClient setRemoteViewController:]
+ -[WCRBrowserEngineClient setUserSettings:]
+ -[WCRBrowserEngineClient userDidCancel]
+ -[WCRBrowserEngineClient userEnteredCorrectPIN]
+ -[WCRBrowserEngineClient userSettings]
+ -[WCRRemotePINEntryViewController delegate]
+ -[WCRRemotePINEntryViewController getIsPINPresentWithCompletion:]
+ -[WCRRemotePINEntryViewController isNumericPIN]
+ -[WCRRemotePINEntryViewController permitURLWithCompletion:]
+ -[WCRRemotePINEntryViewController requiresKeyboard]
+ -[WCRRemotePINEntryViewController setDelegate:]
+ -[WCRRemotePINEntryViewController setPageTitle:]
+ -[WCRRemotePINEntryViewController setURL:]
+ -[WCRRemotePINEntryViewController shouldAutorotateToInterfaceOrientation:]
+ -[WCRRemotePINEntryViewController simplePIN]
+ -[WCRRemotePINEntryViewController supportedInterfaceOrientations]
+ -[WCRRemotePINEntryViewController userDidCancel]
+ -[WCRRemotePINEntryViewController userEnteredCorrectPIN]
+ -[WCRRemotePINEntryViewController viewDidLoad]
+ -[WCRURLList allowedURLStrings]
+ GCC_except_table29
+ _$s10Foundation4DataV06InlineB0V5countAESi_tcfCTf4nd_n
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufc8IteratorQz_SitSwXEfU1_AI_SitSryAEGXEfU_So6NSDataC_TG5
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufc8IteratorQz_SitSwXEfU1_AI_SitSryAEGXEfU_So6NSDataC_Tg5Tf4nn_g
+ _CFPreferencesCopyValue
+ _NSUserName
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_CLASS_$_WCRBlockPage
+ _OBJC_CLASS_$_WCRBrowserEngineClient
+ _OBJC_CLASS_$_WCRRemotePINEntryViewController
+ _OBJC_CLASS_$__UIRemoteViewController
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_WCRBrowserEngineClient._allowList
+ _OBJC_IVAR_$_WCRBrowserEngineClient._allowURLCompletion
+ _OBJC_IVAR_$_WCRBrowserEngineClient._allowedWebsitesOnlyList
+ _OBJC_IVAR_$_WCRBrowserEngineClient._bloomFilter
+ _OBJC_IVAR_$_WCRBrowserEngineClient._configurationPath
+ _OBJC_IVAR_$_WCRBrowserEngineClient._denyList
+ _OBJC_IVAR_$_WCRBrowserEngineClient._evaluationQueue
+ _OBJC_IVAR_$_WCRBrowserEngineClient._language
+ _OBJC_IVAR_$_WCRBrowserEngineClient._macOSExemptURLList
+ _OBJC_IVAR_$_WCRBrowserEngineClient._mode
+ _OBJC_IVAR_$_WCRBrowserEngineClient._remoteViewController
+ _OBJC_IVAR_$_WCRBrowserEngineClient._userSettings
+ _OBJC_IVAR_$_WCRRemotePINEntryViewController._delegate
+ _OBJC_METACLASS_$_WCRBlockPage
+ _OBJC_METACLASS_$_WCRBrowserEngineClient
+ _OBJC_METACLASS_$_WCRRemotePINEntryViewController
+ _OBJC_METACLASS_$__UIRemoteViewController
+ __OBJC_$_CLASS_METHODS_WCRBlockPage
+ __OBJC_$_CLASS_METHODS_WCRBrowserEngineClient
+ __OBJC_$_CLASS_METHODS_WCRRemotePINEntryViewController
+ __OBJC_$_INSTANCE_METHODS_WCRBrowserEngineClient
+ __OBJC_$_INSTANCE_METHODS_WCRRemotePINEntryViewController
+ __OBJC_$_INSTANCE_VARIABLES_WCRBrowserEngineClient
+ __OBJC_$_INSTANCE_VARIABLES_WCRRemotePINEntryViewController
+ __OBJC_$_PROP_LIST_WCRBrowserEngineClient
+ __OBJC_$_PROP_LIST_WCRRemotePINEntryViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WCRPINEntryViewControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WCRPINEntryViewControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WCRServicePINEntryControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRPINEntryViewControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRServicePINEntryControllerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_WCRBrowserEngineClient
+ __OBJC_CLASS_PROTOCOLS_$_WCRRemotePINEntryViewController
+ __OBJC_CLASS_RO_$_WCRBlockPage
+ __OBJC_CLASS_RO_$_WCRBrowserEngineClient
+ __OBJC_CLASS_RO_$_WCRRemotePINEntryViewController
+ __OBJC_LABEL_PROTOCOL_$_WCRPINEntryViewControllerProtocol
+ __OBJC_LABEL_PROTOCOL_$_WCRServicePINEntryControllerProtocol
+ __OBJC_METACLASS_RO_$_WCRBlockPage
+ __OBJC_METACLASS_RO_$_WCRBrowserEngineClient
+ __OBJC_METACLASS_RO_$_WCRRemotePINEntryViewController
+ __OBJC_PROTOCOL_$_WCRPINEntryViewControllerProtocol
+ __OBJC_PROTOCOL_$_WCRServicePINEntryControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WCRPINEntryViewControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WCRServicePINEntryControllerProtocol
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.56
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.57
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.58
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.59
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.60
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke_2
+ ___180+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke_3
+ ___38-[WCRAutoAssetClient _lockLocalAsset:]_block_invoke
+ ___39-[WCRBrowserEngineClient userDidCancel]_block_invoke
+ ___44-[WCRAutoAssetClient _createInterestInAsset]_block_invoke
+ ___47-[WCRBrowserEngineClient userEnteredCorrectPIN]_block_invoke
+ ___53-[WCRBloomFilter _loadFilterResourcesFromMobileAsset]_block_invoke
+ ___53-[WCRBloomFilter _loadFilterResourcesFromMobileAsset]_block_invoke_2
+ ___71-[WCRBrowserEngineClient evaluateURL:withCompletion:onCompletionQueue:]_block_invoke
+ ___78-[WCRBrowserEngineClient requestAllowListAuthenticationForURL:withCompletion:]_block_invoke
+ ___78-[WCRBrowserEngineClient requestAllowListAuthenticationForURL:withCompletion:]_block_invoke_2
+ ___78-[WCRBrowserEngineClient requestAllowListAuthenticationForURL:withCompletion:]_block_invoke_3
+ ___78-[WCRBrowserEngineClient requestAllowListAuthenticationForURL:withCompletion:]_block_invoke_4
+ ___WCRDefaultLog
+ ___WCRDefaultLog.cold.1
+ ___WCRDefaultLog.onceToken
+ ___WCRDefaultLog.osLogHandle
+ _____WCRDefaultLog_block_invoke
+ ___block_descriptor_32_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.123
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_WebContentRestrictions
+ _dispatch_async
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$URLForResource:withExtension:subdirectory:localization:
+ _objc_msgSend$_allowList:
+ _objc_msgSend$_allowedWebSitesHTML:
+ _objc_msgSend$_allowedWebsitesOnly:
+ _objc_msgSend$_allowedWebsitesOnlyList:
+ _objc_msgSend$_blockPageForURL:forUser:inLanguage:isAllowedWebsitesOnlyBlock:withAllowedWebsites:withAllowButton:
+ _objc_msgSend$_createInterestInAsset
+ _objc_msgSend$_css:
+ _objc_msgSend$_defaultUserSettingsPath
+ _objc_msgSend$_denyList:
+ _objc_msgSend$_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:
+ _objc_msgSend$_fileContentWithName:inLanguage:extension:
+ _objc_msgSend$_javascript:
+ _objc_msgSend$_loadFilterResourcesFromLocalFallback
+ _objc_msgSend$_loadFilterResourcesFromMobileAsset
+ _objc_msgSend$_loadFilterResourcesFromMobileAsset:
+ _objc_msgSend$_loadFilterResourcesWithMobileAssetPath:
+ _objc_msgSend$_lockLocalAsset:
+ _objc_msgSend$_lp_simplifiedDisplayString
+ _objc_msgSend$_mode:
+ _objc_msgSend$_performLazyInitialization
+ _objc_msgSend$_preferredLanguageForUserName:
+ _objc_msgSend$_reloadConfiguration
+ _objc_msgSend$_shouldEvaluateURLsForConfigurationAtPath:
+ _objc_msgSend$_shouldShowAllowButton:
+ _objc_msgSend$_xssSafeStringFromString:
+ _objc_msgSend$absoluteString
+ _objc_msgSend$addURLString:
+ _objc_msgSend$allowURLCompletion
+ _objc_msgSend$allowedWebsitesOnlyList
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$base64EncodedDataWithOptions:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$configurationPath
+ _objc_msgSend$containsURLString:
+ _objc_msgSend$createBlockPageFromTemplate:inLanguage:withUserVisibleURLString:isAllowedWebsitesOnlyBlock:withAllowedWebsites:withFormPostToURLString:withFormRestrictedPageURLString:withFormRestrictedPageTitle:
+ _objc_msgSend$createInterestInAsset
+ _objc_msgSend$currentDevice
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$denyList
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dismissViewControllerAnimated:completion:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$evaluationQueue
+ _objc_msgSend$firstObject
+ _objc_msgSend$getIsPINPresentWithCompletion:
+ _objc_msgSend$initWithConfigurationAtPath:
+ _objc_msgSend$interestInContent:completion:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isLegacyExemptURL:
+ _objc_msgSend$keyWindow
+ _objc_msgSend$language
+ _objc_msgSend$length
+ _objc_msgSend$localizations
+ _objc_msgSend$lockContent:withUsagePolicy:withTimeout:completion:
+ _objc_msgSend$macOSExemptURLList
+ _objc_msgSend$mode
+ _objc_msgSend$permitURLWithCompletion:
+ _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$remoteViewController
+ _objc_msgSend$requestAllowListAuthenticationForURL:withCompletion:
+ _objc_msgSend$requestViewController:fromServiceWithBundleIdentifier:connectionHandler:
+ _objc_msgSend$rootViewController
+ _objc_msgSend$serviceViewControllerProxy
+ _objc_msgSend$setAllowList:
+ _objc_msgSend$setAllowURLCompletion:
+ _objc_msgSend$setAllowedWebsitesOnlyList:
+ _objc_msgSend$setConfigurationPath:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDenyList:
+ _objc_msgSend$setLanguage:
+ _objc_msgSend$setModalPresentationStyle:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setPageTitle:
+ _objc_msgSend$setRemoteViewController:
+ _objc_msgSend$setURL:
+ _objc_msgSend$setUserSettings:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$shouldBlock:
+ _objc_msgSend$startUsingLocalAsset:
+ _objc_msgSend$string
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
+ _objc_msgSend$stringByReplacingPercentEscapesUsingEncoding:
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$urlToFormattedString:
+ _objc_msgSend$userDidCancel
+ _objc_msgSend$userEnteredCorrectPIN
+ _objc_msgSend$userInterfaceIdiom
+ _objc_msgSend$userSettings
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x28
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _swift_release_n
- +[WCRLogging log:withType:].cold.5
- -[WCRAutoAssetClient _createInterestInAssetType:withAssetSpecifier:withError:]
- -[WCRAutoAssetClient _lockLocalAsset]
- -[WCRAutoAssetClient _removeInterestInAssetType:withAssetSpecifier:withError:]
- -[WCRAutoAssetClient initWithError:]
- -[WCRAutoAssetClient startUsingLocalAsset]
- -[WCRBloomFilter _loadAssets]
- -[WCRBloomFilter _loadFallbackAssets]
- -[WCRBloomFilter _loadMobileAssets]
- _$s22WebContentRestrictions11BloomFilterC10CodingKeysO11stringValueSSvg
- _$s22WebContentRestrictions11BloomFilterC10CodingKeysO8rawValueSSvg
- _$s22WebContentRestrictions11BloomFilterC10CodingKeysO8rawValueSSvgTm
- _$s22WebContentRestrictions7FNVHashV4hashys6UInt32V10Foundation4DataVFZTf4nd_n
- _$sSTsE21_copySequenceContents12initializing8IteratorQz_SitSry7ElementQzG_tFSo6NSDataC_Tgq5
- _$sSYsSHRzSH8RawValueSYRpzrlE4hash4intoys6HasherVz_tF22WebContentRestrictions11BloomFilterC10CodingKeysO_Tg5
- ___22-[WCRBloomFilter init]_block_invoke_3
- ___27+[WCRLogging log:withType:]_block_invoke
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_literal_global.122
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_WebContentRestrictions
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_WebContentRestrictions
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_WebContentRestrictions
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_WebContentRestrictions
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_WebContentRestrictions
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_WebContentRestrictions
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_WebContentRestrictions
- _log:withType:.onceToken
- _objc_msgSend$_createInterestInAssetType:withAssetSpecifier:withError:
- _objc_msgSend$_loadAssets
- _objc_msgSend$_loadFallbackAssets
- _objc_msgSend$_loadMobileAssets
- _objc_msgSend$_lockLocalAsset
- _objc_msgSend$eliminateAllForSelectorSync:
- _objc_msgSend$initWithError:
- _objc_msgSend$interestInContentSync:
- _objc_msgSend$lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:
- _objc_msgSend$startUsingLocalAsset
- _osLogHandle
CStrings:
+ "\""
+ "%@-nooverride"
+ "%@..."
+ "%{private}@ -> %@"
+ "&"
+ "&amp;"
+ "&apos;"
+ "&gt;"
+ "&lt;"
+ "&quot;"
+ "'"
+ "-net"
+ "-wl"
+ ".apple.com"
+ ".icloud.com"
+ ".mac.com"
+ ".me.com"
+ "/Library/Managed Preferences/%@/com.apple.webcontentfilter.plist"
+ "<"
+ "<a href=\"%@\">%@</a><br>"
+ ">"
+ "@\"NSDictionary\""
+ "@\"NSObject<WCRPINEntryViewControllerProtocol>\""
+ "@\"WCRBloomFilter\""
+ "@\"WCRRemotePINEntryViewController\""
+ "@\"WCRURLList\""
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32B40@44B52"
+ "@76@0:8@16@24@32B40@44@52@60@68"
+ "@84@0:8@16@24@32@40@48@56@64B72B76B80"
+ "ALLOWED_LIST_OF_WEBSITES_NO_LOC"
+ "Allow list: %{private}@ -> Allowed"
+ "Allowed websites only: %{private}@ -> Allowed"
+ "Allowed websites only: %{private}@ -> Not Allowed"
+ "AppleLanguages"
+ "B24@0:8q16"
+ "Block page contents are nil!"
+ "BlockPageURL was nil"
+ "Caught exception: %@"
+ "Deny list: %{private}@ -> Not Allowed"
+ "Error finding file with name %@"
+ "Error getting address from websiteInfo"
+ "Error getting title from websiteInfo"
+ "Error loading block page: %@"
+ "Finished reloading configuration"
+ "Found preferred loc"
+ "INCLUDE_CSS_FILE_NO_LOC"
+ "INCLUDE_JAVASCRIPT_FILE_NO_LOC"
+ "Impossible to determine URL"
+ "Legacy: %{private}@ -> Allowed"
+ "Loaded Apple allow list at path %@"
+ "Loaded bloom filter at path %@"
+ "Loaded fallback Apple allow list at path %@"
+ "Loaded fallback filter at path %@"
+ "Loading bloom filter"
+ "Loading fallback Apple allow list %@"
+ "Loading fallback filter %@"
+ "Looking up preferred language"
+ "No available locs"
+ "No evaluation necessary"
+ "No framework bundle"
+ "No language prefs"
+ "No preferred locs"
+ "PAGE_TO_OVERRIDE_TITLE_NO_LOC"
+ "PAGE_TO_OVERRIDE_URL_NO_LOC"
+ "Provided userName was nil"
+ "Q"
+ "Q16@0:8"
+ "Q24@0:8@16"
+ "Running web content filter in mode %lu"
+ "SEND_FORM_TO_URL_NO_LOC"
+ "Started reloading configuration"
+ "T@\"MAAutoAssetSelector\",&,V_currentAssetSelector"
+ "T@\"NSDictionary\",&,V_userSettings"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_evaluationQueue"
+ "T@\"NSObject<WCRPINEntryViewControllerProtocol>\",N,V_delegate"
+ "T@\"NSString\",&,N,V_configurationPath"
+ "T@\"NSString\",&,V_language"
+ "T@\"WCRBloomFilter\",&,V_bloomFilter"
+ "T@\"WCRRemotePINEntryViewController\",&,N,V_remoteViewController"
+ "T@\"WCRURLList\",&,N,V_macOSExemptURLList"
+ "T@\"WCRURLList\",&,V_allowList"
+ "T@\"WCRURLList\",&,V_allowedWebsitesOnlyList"
+ "T@\"WCRURLList\",&,V_denyList"
+ "T@?,C,N,V_allowURLCompletion"
+ "TQ,V_mode"
+ "UNBLOCK_URL_NO_LOC"
+ "URLForResource:withExtension:subdirectory:localization:"
+ "USER_VISIBLE_RESTRICTED_URL_NO_LOC"
+ "WCRBlockPage"
+ "WCRBrowserEngineClient"
+ "WCRPINEntryErrorDomain"
+ "WCRPINEntryViewControllerProtocol"
+ "WCRRemotePINEntryViewController"
+ "WCRRemotePINEntryViewController created"
+ "WCRRemotePINEntryViewController is nil"
+ "WCRServicePINEntryControllerProtocol"
+ "WCRServicePINEntryNavigationController"
+ "_allowList:"
+ "_allowURLCompletion"
+ "_allowedWebSitesHTML:"
+ "_allowedWebsitesOnly:"
+ "_allowedWebsitesOnlyList"
+ "_allowedWebsitesOnlyList:"
+ "_blockPageForURL:forUser:inLanguage:isAllowedWebsitesOnlyBlock:withAllowedWebsites:withAllowButton:"
+ "_configurationPath"
+ "_createInterestInAsset"
+ "_css:"
+ "_defaultUserSettingsPath"
+ "_delegate"
+ "_denyList"
+ "_denyList:"
+ "_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:"
+ "_evaluationQueue"
+ "_fileContentWithName:inLanguage:extension:"
+ "_javascript:"
+ "_language"
+ "_loadFilterResourcesFromLocalFallback"
+ "_loadFilterResourcesFromMobileAsset"
+ "_loadFilterResourcesFromMobileAsset:"
+ "_loadFilterResourcesWithMobileAssetPath:"
+ "_lockLocalAsset:"
+ "_lp_simplifiedDisplayString"
+ "_macOSExemptURLList"
+ "_mode"
+ "_mode:"
+ "_performLazyInitialization"
+ "_preferredLanguageForUserName:"
+ "_reloadConfiguration"
+ "_remoteViewController"
+ "_shouldEvaluateURLsForConfigurationAtPath:"
+ "_shouldShowAllowButton:"
+ "_userSettings"
+ "_xssSafeStringFromString:"
+ "`"
+ "absoluteString"
+ "accounts.google.com"
+ "address"
+ "allowURL:withCompletion:"
+ "allowURLCompletion"
+ "allowURLWithFamilyControls:withCompletion:"
+ "allowedURLStrings"
+ "allowedWebsitesOnlyList"
+ "api.login.aol.com"
+ "appendFormat:"
+ "appendString:"
+ "apple.com"
+ "base64EncodedDataWithOptions:"
+ "base64StringFromString:"
+ "block page is nil"
+ "blockPageForUser:inLanguage:withUserVisibleURLString:withFormPostToURLString:withFormRestrictedPageURLString:withFormRestrictedPageTitle:withAllowedWebsites:isAllowedWebsitesOnlyBlock:isNetworkAccount:allowsOverrides:"
+ "blockpage"
+ "blockpage-macOS"
+ "blockpage-macOS-nooverride"
+ "blockpage_script"
+ "blockpage_style"
+ "blockpage_style-macOS"
+ "books.apple.com"
+ "boolValue"
+ "bundleForClass:"
+ "cancel"
+ "com.apple.WebContentFilter.remoteUI.WebContentAnalysisUI"
+ "com.apple.WebContentRestrictions.evaluationQueue"
+ "configurationPath"
+ "createBlockPageFromTemplate:inLanguage:withUserVisibleURLString:isAllowedWebsitesOnlyBlock:withAllowedWebsites:withFormPostToURLString:withFormRestrictedPageURLString:withFormRestrictedPageTitle:"
+ "createInterestInAsset"
+ "css"
+ "currentDevice"
+ "dataUsingEncoding:"
+ "delegate"
+ "denyList"
+ "dictionaryWithContentsOfFile:"
+ "dismissViewControllerAnimated:completion:"
+ "en"
+ "error loading file with name %@. Error: %@"
+ "errorWithDomain:code:userInfo:"
+ "evaluateURL:withCompletion:"
+ "evaluateURL:withCompletion:onCompletionQueue:"
+ "evaluationQueue"
+ "exportedInterface"
+ "filterBlacklist"
+ "filterWhitelist"
+ "firstObject"
+ "generateMacOSExemptURLList"
+ "getIsPINPresentWithCompletion:"
+ "gil.apple.com"
+ "help.apple.com"
+ "html"
+ "http://www.error.com"
+ "icloud.com"
+ "initWithConfigurationAtPath:"
+ "interestInContent:completion:"
+ "interfaceWithProtocol:"
+ "isLegacyExemptURL:"
+ "isNumericPIN"
+ "itunes.apple.com"
+ "js"
+ "keyWindow"
+ "language"
+ "length"
+ "localizations"
+ "lockContent:withUsagePolicy:withTimeout:completion:"
+ "login.aol.com"
+ "login.microsoftonline.com"
+ "login.yahoo.co.jp"
+ "login.yahoo.com"
+ "mac.com"
+ "macOSExemptURLList"
+ "me.com"
+ "mode"
+ "noOverridingAllowed"
+ "pageTitle"
+ "permitURLWithCompletion:"
+ "preferredLocalizationsFromArray:forPreferences:"
+ "presentViewController:animated:completion:"
+ "remoteViewController"
+ "requestAllowListAuthenticationForURL:withCompletion:"
+ "requestViewController:fromServiceWithBundleIdentifier:connectionHandler:"
+ "requiresKeyboard"
+ "restrictWeb"
+ "rootViewController"
+ "sb.music.apple.com"
+ "sb.tv.apple.com"
+ "serviceViewControllerInterface"
+ "serviceViewControllerProxy"
+ "setAllowURLCompletion:"
+ "setAllowedWebsitesOnlyList:"
+ "setConfigurationPath:"
+ "setDelegate:"
+ "setDenyList:"
+ "setEvaluationQueue:"
+ "setLanguage:"
+ "setMacOSExemptURLList:"
+ "setModalPresentationStyle:"
+ "setMode:"
+ "setPageTitle:"
+ "setRemoteViewController:"
+ "setURL:"
+ "setUserSettings:"
+ "setup.icloud.com"
+ "sharedApplication"
+ "shouldAutorotateToInterfaceOrientation:"
+ "shouldEvaluateURLs"
+ "shouldEvaluateURLsForConfigurationAtPath:"
+ "simplePIN"
+ "siteWhitelist"
+ "startUsingLocalAsset:"
+ "string"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
+ "stringByReplacingPercentEscapesUsingEncoding:"
+ "stringWithContentsOfURL:encoding:error:"
+ "stringWithString:"
+ "substringToIndex:"
+ "supportedInterfaceOrientations"
+ "urlToFormattedString:"
+ "useContentFilter"
+ "useContentFilterOverrides"
+ "userDidCancel"
+ "userEnteredCorrectPIN"
+ "userInterfaceIdiom"
+ "userSettings"
+ "v104@0:8@16Q24@32@40@48@56@64@72@80@?88@96"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSString\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"NSURL\"16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8Q16"
+ "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"
+ "v24@?0@\"_UIRemoteViewController\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v40@0:8@16@?24@32"
+ "v44@?0@\"MAAutoAssetSelector\"8B16@\"NSURL\"20@\"MAAutoAssetStatus\"28@\"NSError\"36"
+ "viewDidLoad"
+ "whitelistEnabled"
+ "www.google.com/accounts"
+ "www.googleapis.com/auth"
+ "x-apple-content-filter://unblock"
- "%@ -> %@"
- "@24@0:8^@16"
- "B40@0:8@16@24^@32"
- "Could not find a bloom filter from MobileAsset. Using local copy %@ instead"
- "Could not find an Apple allow list filter from MobileAsset. Using local copy %@ instead"
- "Error initializing WCRAutoAssetClient: %@"
- "Failed to eliminate asset: %@"
- "Initialized Apple allow list at path %@"
- "Initialized bloom filter at path %@"
- "T@\"MAAutoAssetSelector\",&,N,V_currentAssetSelector"
- "_createInterestInAssetType:withAssetSpecifier:withError:"
- "_loadAssets"
- "_loadFallbackAssets"
- "_loadMobileAssets"
- "_lockLocalAsset"
- "_removeInterestInAssetType:withAssetSpecifier:withError:"
- "eliminateAllForSelectorSync:"
- "initWithError:"
- "interestInContentSync:"
- "lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:"
- "startUsingLocalAsset"
- "v40@0:8@16@24^@32"

```
