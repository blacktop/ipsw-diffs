## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-39.120.2.0.0
-  __TEXT.__text: 0xaed4
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x75c
-  __TEXT.__const: 0x560
-  __TEXT.__cstring: 0xf5c
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x1b3
-  __TEXT.__swift5_typeref: 0x10c
+63.0.0.0.0
+  __TEXT.__text: 0xeaf4
+  __TEXT.__objc_methlist: 0xf0c
+  __TEXT.__const: 0x590
+  __TEXT.__cstring: 0x152c
+  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__oslogstring: 0x773
+  __TEXT.__ustring: 0xf2
+  __TEXT.__swift5_typeref: 0x102
   __TEXT.__constg_swiftt: 0x220
   __TEXT.__swift5_reflstr: 0x107
   __TEXT.__swift5_fieldmd: 0x144

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__eh_frame: 0x378
-  __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x1860
-  __TEXT.__objc_methtype: 0x2d1
-  __TEXT.__objc_stubs: 0x1600
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x338
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__unwind_info: 0x468
+  __TEXT.__eh_frame: 0x2a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0xa18
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x389
-  __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0xc90
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__objc_const: 0x1cb8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x310
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0x190
+  __DATA.__objc_ivar: 0xe0
+  __DATA.__data: 0x488
   __DATA.__bss: 0x690
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DeviceConfiguration.framework/DeviceConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5837AAEA-890C-38A3-9105-E3166E112201
-  Functions: 296
-  Symbols:   1327
-  CStrings:  617
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: A7D9B61A-6A49-3907-A48D-51FC0D9AC83A
+  Functions: 417
+  Symbols:   1825
+  CStrings:  455
 
Symbols:
+ +[WCRBloomFilter _shouldBlock:withBloomFilter:limitAdultContent:limitWebProxies:cipherMLProvider:]
+ +[WCRBrowserEngineClient _allowTransitiveTrust:]
+ +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:]
+ +[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:overridePolicy:withCompletion:onCompletionQueue:]
+ +[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]
+ +[WCRBrowserEngineClient _getConfigurationFromDC]
+ +[WCRBrowserEngineClient _isMDMOrThirdParty:]
+ +[WCRBrowserEngineClient _limitWebProxies:]
+ +[WCRBrowserEngineClient _loadResource:withExtension:error:]
+ +[WCRBrowserEngineClient _localizedString:inLanguage:]
+ +[WCRBrowserEngineClient _overridePolicyFromConfiguration:]
+ +[WCRBrowserEngineClient _overridePolicyFromConfiguration:].cold.1
+ +[WCRBrowserEngineClient allowURLWithFamilyControls:referrerURL:withCompletion:]
+ +[WCRBrowserEngineClient isOverridePolicyForNewScreenTime:]
+ +[WCRBrowserEngineClient shieldStateForURL:referrerURL:]
+ +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:language:]
+ +[WCRRemoteAskToViewController exportedInterface]
+ +[WCRRemoteAskToViewController serviceViewControllerInterface]
+ +[WCRRemoteDeviceApprovalViewController exportedInterface]
+ +[WCRRemoteDeviceApprovalViewController serviceViewControllerInterface]
+ +[WCRURLList _doesList:containURLString:]
+ -[WCRAuthenticationSites .cxx_destruct]
+ -[WCRAuthenticationSites _loadFromFile:]
+ -[WCRAuthenticationSites _loadResourcesFromLocalFallback]
+ -[WCRAuthenticationSites _loadResourcesFromMobileAsset:]
+ -[WCRAuthenticationSites _loadResourcesFromMobileAsset]
+ -[WCRAuthenticationSites _loadResourcesWithMobileAssetPath:]
+ -[WCRAuthenticationSites allowList]
+ -[WCRAuthenticationSites autoAsset]
+ -[WCRAuthenticationSites containsURLString:]
+ -[WCRAuthenticationSites dealloc]
+ -[WCRAuthenticationSites init]
+ -[WCRAuthenticationSites reloadAssetQueue]
+ -[WCRAuthenticationSites setAllowList:]
+ -[WCRAuthenticationSites setAutoAsset:]
+ -[WCRAuthenticationSites setReloadAssetQueue:]
+ -[WCRAutoAssetClient currentAssetSetEntry]
+ -[WCRAutoAssetClient setCurrentAssetSetEntry:]
+ -[WCRBloomFilter cipherMLProvider]
+ -[WCRBloomFilter dealloc]
+ -[WCRBloomFilter initWithCipherMLProvider:]
+ -[WCRBloomFilter limitAdultContent]
+ -[WCRBloomFilter limitWebProxies]
+ -[WCRBloomFilter setCipherMLProvider:]
+ -[WCRBloomFilter setLimitAdultContent:]
+ -[WCRBloomFilter setLimitWebProxies:]
+ -[WCRBrowserEngineClient allowTransitiveTrust]
+ -[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]
+ -[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:].cold.1
+ -[WCRBrowserEngineClient askToBrowseURL:referrerURL:presentingView:withCompletion:]
+ -[WCRBrowserEngineClient askToBrowseURL:referrerURL:withCompletion:]
+ -[WCRBrowserEngineClient askToBrowseURLCompletion]
+ -[WCRBrowserEngineClient askToBrowseURL]
+ -[WCRBrowserEngineClient authenticationSites]
+ -[WCRBrowserEngineClient deviceApprovalCompleted:]
+ -[WCRBrowserEngineClient evaluateURL:mainDocumentURL:withCompletion:]
+ -[WCRBrowserEngineClient evaluateURL:mainDocumentURL:withCompletion:onCompletionQueue:]
+ -[WCRBrowserEngineClient isMDMRestricted]
+ -[WCRBrowserEngineClient overridePolicy]
+ -[WCRBrowserEngineClient popoverPresentationControllerDelegate]
+ -[WCRBrowserEngineClient remoteAskToViewController]
+ -[WCRBrowserEngineClient remoteDeviceApprovalViewController]
+ -[WCRBrowserEngineClient setAllowTransitiveTrust:]
+ -[WCRBrowserEngineClient setAskToBrowseURL:]
+ -[WCRBrowserEngineClient setAskToBrowseURLCompletion:]
+ -[WCRBrowserEngineClient setAuthenticationSites:]
+ -[WCRBrowserEngineClient setIsMDMRestricted:]
+ -[WCRBrowserEngineClient setOverridePolicy:]
+ -[WCRBrowserEngineClient setPopoverPresentationControllerDelegate:]
+ -[WCRBrowserEngineClient setRemoteAskToViewController:]
+ -[WCRBrowserEngineClient setRemoteDeviceApprovalViewController:]
+ -[WCRBrowserEngineClient userApprovedURL:error:]
+ -[WCRBrowserEngineClient userApprovedURL:error:].cold.1
+ -[WCRBrowserEngineClient userRequestedDeviceApproval]
+ -[WCRBrowserEngineClient userRequestedDeviceApproval].cold.1
+ -[WCRBrowserEngineClient userRequestedRemoteApproval]
+ -[WCRPopoverPresentationControllerDelegate adaptivePresentationStyleForPresentationController:]
+ -[WCRRemoteAskToViewController approveURL:withCompletion:]
+ -[WCRRemoteAskToViewController configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:overridePolicy:iframe:]
+ -[WCRRemoteAskToViewController delegate]
+ -[WCRRemoteAskToViewController isScreenTimeEnabledWithCompletion:]
+ -[WCRRemoteAskToViewController setDelegate:]
+ -[WCRRemoteAskToViewController userApprovedURL:error:]
+ -[WCRRemoteAskToViewController userRequestedDeviceApproval]
+ -[WCRRemoteAskToViewController userRequestedRemoteApproval]
+ -[WCRRemoteAskToViewController viewDidLoad]
+ -[WCRRemoteDeviceApprovalViewController delegate]
+ -[WCRRemoteDeviceApprovalViewController deviceApprovalCompleted:]
+ -[WCRRemoteDeviceApprovalViewController setDelegate:]
+ -[WCRRemoteDeviceApprovalViewController setURL:]
+ -[WCRRemoteDeviceApprovalViewController viewDidLoad]
+ -[WCRShieldButton .cxx_destruct]
+ -[WCRShieldButton id]
+ -[WCRShieldButton initWithTitle:url:id:isDefault:]
+ -[WCRShieldButton isDefault]
+ -[WCRShieldButton setId:]
+ -[WCRShieldButton setIsDefault:]
+ -[WCRShieldButton setTitle:]
+ -[WCRShieldButton setUrl:]
+ -[WCRShieldButton title]
+ -[WCRShieldButton url]
+ -[WCRShieldState .cxx_destruct]
+ -[WCRShieldState buttons]
+ -[WCRShieldState displayURL]
+ -[WCRShieldState iframe]
+ -[WCRShieldState initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:]
+ -[WCRShieldState overridePolicy]
+ -[WCRShieldState shieldType]
+ -[WCRShieldState showBadge]
+ -[WCRShieldState subtitle]
+ -[WCRShieldState symbol]
+ -[WCRShieldState title]
+ -[WCRURLList isEmpty]
+ GCC_except_table1
+ GCC_except_table40
+ GCC_except_table46
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ _$s10Foundation4DataV15_RepresentationOyAESWcfCTf4nd_n
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufcAC15_RepresentationOSWXEfU0_
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufcySwXEfU2_SS8UTF8ViewV_Tg5
+ _$s22WebContentRestrictions11MurmurHash3V4hash_4seeds6UInt32V10Foundation4DataV_AGtFZTf4nnd_n
+ _$s22WebContentRestrictions16MembershipFilter_pSgWOh
+ _$s22WebContentRestrictions7FNVHashV4hashys6UInt32V10Foundation4DataVFZTf4nd_n
+ _$ss5NeverON
+ _$ss5NeverOs5ErrorsWP
+ _CGRectGetMaxY
+ _CGRectGetWidth
+ _OBJC_CLASS_$_DCUserConsumer
+ _OBJC_CLASS_$_MAAutoAssetSet
+ _OBJC_CLASS_$_MAAutoAssetSetEntry
+ _OBJC_CLASS_$_MAAutoAssetSetNotifications
+ _OBJC_CLASS_$_MAAutoAssetSetPolicy
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_UIViewController
+ _OBJC_CLASS_$_WCRAuthenticationSites
+ _OBJC_CLASS_$_WCRPopoverPresentationControllerDelegate
+ _OBJC_CLASS_$_WCRRemoteAskToViewController
+ _OBJC_CLASS_$_WCRRemoteDeviceApprovalViewController
+ _OBJC_CLASS_$_WCRShieldButton
+ _OBJC_CLASS_$_WCRShieldState
+ _OBJC_IVAR_$_WCRAuthenticationSites._allowList
+ _OBJC_IVAR_$_WCRAuthenticationSites._autoAsset
+ _OBJC_IVAR_$_WCRAuthenticationSites._reloadAssetQueue
+ _OBJC_IVAR_$_WCRAutoAssetClient._currentAssetSetEntry
+ _OBJC_IVAR_$_WCRBloomFilter._cipherMLProvider
+ _OBJC_IVAR_$_WCRBloomFilter._limitAdultContent
+ _OBJC_IVAR_$_WCRBloomFilter._limitWebProxies
+ _OBJC_IVAR_$_WCRBrowserEngineClient._allowTransitiveTrust
+ _OBJC_IVAR_$_WCRBrowserEngineClient._askToBrowseURL
+ _OBJC_IVAR_$_WCRBrowserEngineClient._askToBrowseURLCompletion
+ _OBJC_IVAR_$_WCRBrowserEngineClient._authenticationSites
+ _OBJC_IVAR_$_WCRBrowserEngineClient._isMDMRestricted
+ _OBJC_IVAR_$_WCRBrowserEngineClient._overridePolicy
+ _OBJC_IVAR_$_WCRBrowserEngineClient._popoverPresentationControllerDelegate
+ _OBJC_IVAR_$_WCRBrowserEngineClient._remoteAskToViewController
+ _OBJC_IVAR_$_WCRBrowserEngineClient._remoteDeviceApprovalViewController
+ _OBJC_IVAR_$_WCRRemoteAskToViewController._delegate
+ _OBJC_IVAR_$_WCRRemoteDeviceApprovalViewController._delegate
+ _OBJC_IVAR_$_WCRShieldButton._id
+ _OBJC_IVAR_$_WCRShieldButton._isDefault
+ _OBJC_IVAR_$_WCRShieldButton._title
+ _OBJC_IVAR_$_WCRShieldButton._url
+ _OBJC_IVAR_$_WCRShieldState._buttons
+ _OBJC_IVAR_$_WCRShieldState._displayURL
+ _OBJC_IVAR_$_WCRShieldState._iframe
+ _OBJC_IVAR_$_WCRShieldState._overridePolicy
+ _OBJC_IVAR_$_WCRShieldState._shieldType
+ _OBJC_IVAR_$_WCRShieldState._showBadge
+ _OBJC_IVAR_$_WCRShieldState._subtitle
+ _OBJC_IVAR_$_WCRShieldState._symbol
+ _OBJC_IVAR_$_WCRShieldState._title
+ _OBJC_METACLASS_$_WCRAuthenticationSites
+ _OBJC_METACLASS_$_WCRPopoverPresentationControllerDelegate
+ _OBJC_METACLASS_$_WCRRemoteAskToViewController
+ _OBJC_METACLASS_$_WCRRemoteDeviceApprovalViewController
+ _OBJC_METACLASS_$_WCRShieldButton
+ _OBJC_METACLASS_$_WCRShieldState
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_WCRRemoteAskToViewController
+ __OBJC_$_CLASS_METHODS_WCRRemoteDeviceApprovalViewController
+ __OBJC_$_INSTANCE_METHODS_WCRAuthenticationSites
+ __OBJC_$_INSTANCE_METHODS_WCRPopoverPresentationControllerDelegate
+ __OBJC_$_INSTANCE_METHODS_WCRRemoteAskToViewController
+ __OBJC_$_INSTANCE_METHODS_WCRRemoteDeviceApprovalViewController
+ __OBJC_$_INSTANCE_METHODS_WCRShieldButton
+ __OBJC_$_INSTANCE_METHODS_WCRShieldState
+ __OBJC_$_INSTANCE_VARIABLES_WCRAuthenticationSites
+ __OBJC_$_INSTANCE_VARIABLES_WCRRemoteAskToViewController
+ __OBJC_$_INSTANCE_VARIABLES_WCRRemoteDeviceApprovalViewController
+ __OBJC_$_INSTANCE_VARIABLES_WCRShieldButton
+ __OBJC_$_INSTANCE_VARIABLES_WCRShieldState
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_WCRAuthenticationSites
+ __OBJC_$_PROP_LIST_WCRCipherMLClient
+ __OBJC_$_PROP_LIST_WCRPopoverPresentationControllerDelegate
+ __OBJC_$_PROP_LIST_WCRRemoteAskToViewController
+ __OBJC_$_PROP_LIST_WCRRemoteDeviceApprovalViewController
+ __OBJC_$_PROP_LIST_WCRShieldButton
+ __OBJC_$_PROP_LIST_WCRShieldState
+ __OBJC_$_PROTOCOL_CLASS_METHODS_WCRCipherMLProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIPopoverPresentationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WCRAskToViewControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WCRDeviceApprovalViewControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WCRAskToViewControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WCRDeviceApprovalViewControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WCRServiceAskToAlertControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WCRServiceDeviceApprovalControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIPopoverPresentationControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRAskToViewControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRCipherMLProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRDeviceApprovalViewControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRServiceAskToAlertControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WCRServiceDeviceApprovalControllerProtocol
+ __OBJC_$_PROTOCOL_REFS_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIPopoverPresentationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_WCRCipherMLProviding
+ __OBJC_CLASS_PROTOCOLS_$_WCRCipherMLClient
+ __OBJC_CLASS_PROTOCOLS_$_WCRPopoverPresentationControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WCRRemoteAskToViewController
+ __OBJC_CLASS_PROTOCOLS_$_WCRRemoteDeviceApprovalViewController
+ __OBJC_CLASS_RO_$_WCRAuthenticationSites
+ __OBJC_CLASS_RO_$_WCRPopoverPresentationControllerDelegate
+ __OBJC_CLASS_RO_$_WCRRemoteAskToViewController
+ __OBJC_CLASS_RO_$_WCRRemoteDeviceApprovalViewController
+ __OBJC_CLASS_RO_$_WCRShieldButton
+ __OBJC_CLASS_RO_$_WCRShieldState
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIPopoverPresentationControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_WCRAskToViewControllerProtocol
+ __OBJC_LABEL_PROTOCOL_$_WCRCipherMLProviding
+ __OBJC_LABEL_PROTOCOL_$_WCRDeviceApprovalViewControllerProtocol
+ __OBJC_LABEL_PROTOCOL_$_WCRServiceAskToAlertControllerProtocol
+ __OBJC_LABEL_PROTOCOL_$_WCRServiceDeviceApprovalControllerProtocol
+ __OBJC_METACLASS_RO_$_WCRAuthenticationSites
+ __OBJC_METACLASS_RO_$_WCRPopoverPresentationControllerDelegate
+ __OBJC_METACLASS_RO_$_WCRRemoteAskToViewController
+ __OBJC_METACLASS_RO_$_WCRRemoteDeviceApprovalViewController
+ __OBJC_METACLASS_RO_$_WCRShieldButton
+ __OBJC_METACLASS_RO_$_WCRShieldState
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
+ __OBJC_PROTOCOL_$_UIPopoverPresentationControllerDelegate
+ __OBJC_PROTOCOL_$_WCRAskToViewControllerProtocol
+ __OBJC_PROTOCOL_$_WCRCipherMLProviding
+ __OBJC_PROTOCOL_$_WCRDeviceApprovalViewControllerProtocol
+ __OBJC_PROTOCOL_$_WCRServiceAskToAlertControllerProtocol
+ __OBJC_PROTOCOL_$_WCRServiceDeviceApprovalControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WCRAskToViewControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WCRDeviceApprovalViewControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WCRServiceAskToAlertControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WCRServiceDeviceApprovalControllerProtocol
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke.85
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke.87
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke.88
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke.89
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke.90
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke.91
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke_2
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke_2.92
+ ___267+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:]_block_invoke_3
+ ___30-[WCRAuthenticationSites init]_block_invoke
+ ___30-[WCRAuthenticationSites init]_block_invoke_2
+ ___43-[WCRBloomFilter initWithCipherMLProvider:]_block_invoke
+ ___43-[WCRBloomFilter initWithCipherMLProvider:]_block_invoke_2
+ ___48-[WCRBrowserEngineClient userApprovedURL:error:]_block_invoke
+ ___53-[WCRBrowserEngineClient userRequestedDeviceApproval]_block_invoke
+ ___53-[WCRBrowserEngineClient userRequestedDeviceApproval]_block_invoke_2
+ ___53-[WCRBrowserEngineClient userRequestedDeviceApproval]_block_invoke_2.cold.1
+ ___55-[WCRAuthenticationSites _loadResourcesFromMobileAsset]_block_invoke
+ ___55-[WCRAuthenticationSites _loadResourcesFromMobileAsset]_block_invoke_2
+ ___83-[WCRBrowserEngineClient askToBrowseURL:referrerURL:presentingView:withCompletion:]_block_invoke
+ ___83-[WCRBrowserEngineClient askToBrowseURL:referrerURL:presentingView:withCompletion:]_block_invoke.360
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.384
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.388
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.cold.1
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.cold.2
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.cold.3
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.cold.4
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke.cold.5
+ ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke_2
+ ___86+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:language:]_block_invoke
+ ___87+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:]_block_invoke
+ ___87-[WCRBrowserEngineClient evaluateURL:mainDocumentURL:withCompletion:onCompletionQueue:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_32_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_40_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e31_v24?0"NSString"8"NSString"16lr32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e8_v12?0B8ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e8_v16?0Q8ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.125
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_WebContentRestrictions
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_WebContentRestrictions
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URLForResource:withExtension:subdirectory:
+ _objc_msgSend$_allowTransitiveTrust:
+ _objc_msgSend$_blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:
+ _objc_msgSend$_doesList:containURLString:
+ _objc_msgSend$_evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:withCompletion:onCompletionQueue:
+ _objc_msgSend$_getConfigurationFromDC
+ _objc_msgSend$_isMDMOrThirdParty:
+ _objc_msgSend$_limitWebProxies:
+ _objc_msgSend$_loadFromFile:
+ _objc_msgSend$_loadResource:withExtension:error:
+ _objc_msgSend$_loadResourcesFromLocalFallback
+ _objc_msgSend$_loadResourcesFromMobileAsset
+ _objc_msgSend$_loadResourcesFromMobileAsset:
+ _objc_msgSend$_loadResourcesWithMobileAssetPath:
+ _objc_msgSend$_localizedString:inLanguage:
+ _objc_msgSend$_overridePolicyFromConfiguration:
+ _objc_msgSend$_shouldBlock:withBloomFilter:limitAdultContent:limitWebProxies:cipherMLProvider:
+ _objc_msgSend$allowTransitiveTrust
+ _objc_msgSend$allowURL:withCompletion:
+ _objc_msgSend$approveURL:withCompletion:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$askToBrowseContextMenu:presentingView:state:withCompletion:
+ _objc_msgSend$askToBrowseURL
+ _objc_msgSend$askToBrowseURL:referrerURL:presentingView:withCompletion:
+ _objc_msgSend$askToBrowseURLCompletion
+ _objc_msgSend$authenticationSites
+ _objc_msgSend$bounds
+ _objc_msgSend$buttons
+ _objc_msgSend$cipherMLProvider
+ _objc_msgSend$configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:overridePolicy:iframe:
+ _objc_msgSend$deviceApprovalCompleted:
+ _objc_msgSend$displayURL
+ _objc_msgSend$endAtomicLocksSync:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:
+ _objc_msgSend$evaluateURL:mainDocumentURL:withCompletion:
+ _objc_msgSend$evaluateURL:mainDocumentURL:withCompletion:onCompletionQueue:
+ _objc_msgSend$getConfigurationSyncFor:error:
+ _objc_msgSend$id
+ _objc_msgSend$iframe
+ _objc_msgSend$initUsingClientDomain:forClientName:forAssetSetIdentifier:comprisedOfEntries:error:
+ _objc_msgSend$initWithCipherMLProvider:
+ _objc_msgSend$initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:
+ _objc_msgSend$initWithTitle:url:id:isDefault:
+ _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$isDefault
+ _objc_msgSend$isOverridePolicyForNewScreenTime:
+ _objc_msgSend$isScreenTimeEnabledWithCompletion:
+ _objc_msgSend$limitAdultContent
+ _objc_msgSend$limitWebProxies
+ _objc_msgSend$localContentURL
+ _objc_msgSend$localizedStringForKey:value:table:localization:
+ _objc_msgSend$lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:completion:
+ _objc_msgSend$name
+ _objc_msgSend$needForAtomic:completion:
+ _objc_msgSend$nextResponder
+ _objc_msgSend$notifyRegistrationName:forAssetSetIdentifier:
+ _objc_msgSend$overridePolicy
+ _objc_msgSend$popoverPresentationController
+ _objc_msgSend$popoverPresentationControllerDelegate
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$queryItems
+ _objc_msgSend$remoteAskToViewController
+ _objc_msgSend$remoteDeviceApprovalViewController
+ _objc_msgSend$setAllowTransitiveTrust:
+ _objc_msgSend$setAskToBrowseURL:
+ _objc_msgSend$setAskToBrowseURLCompletion:
+ _objc_msgSend$setAuthenticationSites:
+ _objc_msgSend$setCurrentAssetSetEntry:
+ _objc_msgSend$setLimitAdultContent:
+ _objc_msgSend$setLimitWebProxies:
+ _objc_msgSend$setOverridePolicy:
+ _objc_msgSend$setPermittedArrowDirections:
+ _objc_msgSend$setPopoverPresentationControllerDelegate:
+ _objc_msgSend$setRemoteAskToViewController:
+ _objc_msgSend$setRemoteDeviceApprovalViewController:
+ _objc_msgSend$setSourceRect:
+ _objc_msgSend$setSourceView:
+ _objc_msgSend$shieldStateForURL:referrerURL:
+ _objc_msgSend$shieldStateForURL:shieldType:overridePolicy:iframe:language:
+ _objc_msgSend$shieldType
+ _objc_msgSend$showBadge
+ _objc_msgSend$subtitle
+ _objc_msgSend$symbol
+ _objc_msgSend$title
+ _objc_msgSend$url
+ _objc_msgSend$userApprovedURL:error:
+ _objc_msgSend$userRequestedDeviceApproval
+ _objc_msgSend$userRequestedRemoteApproval
+ _objc_msgSend$value
+ _objc_msgSend$view
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x26
+ _swift_release_x28
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x27
+ _swift_willThrowTypedImpl
- +[WCRBloomFilter _shouldBlock:withBloomFilter:useCipherML:]
- +[WCRBrowserEngineClient _blockPageForURL:inLanguage:withAllowButton:]
- +[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]
- +[WCRBrowserEngineClient _shouldShowAllowButton:]
- +[WCRBrowserEngineClient allowURLWithFamilyControls:withCompletion:]
- -[WCRAutoAssetClient currentAssetSelector]
- -[WCRAutoAssetClient setCurrentAssetSelector:]
- GCC_except_table31
- _$s10Foundation13__DataStorageC22withUnsafeMutableBytes2in5applyxSnySiG_xSwKXEtKlFs16IndexingIteratorVySS8UTF8ViewVG_Sit_Tg5
- _$s10Foundation15ContiguousBytes_pSgMR
- _$s10Foundation15ContiguousBytes_pSgMd
- _$s10Foundation4DataV06InlineB0V5countAESi_tcfCTf4nd_n
- _$s10Foundation4DataV06InlineB0VyAESWcfCTf4nd_n
- _$s10Foundation4DataV10LargeSliceVyAESWcfCTf4nd_n
- _$s10Foundation4DataV11InlineSliceV21ensureUniqueReferenceyyF
- _$s10Foundation4DataV11InlineSliceV22withUnsafeMutableBytesyxxSwKXEKlFyt_Tg574$s22WebContentRestrictions11BloomFilterC6encode2toys7Encoder_p_tKFySwXEfU_So14CFBitVectorRefa0jK12Restrictions0mN0CTf1ncn_n
- _$s10Foundation4DataV11InlineSliceVyAESWcfCTf4nd_n
- _$s10Foundation4DataV15_RepresentationO22withUnsafeMutableBytesyxxSwKXEKlFs16IndexingIteratorVySS8UTF8ViewVG_Sit_Tg5
- _$s10Foundation4DataV15_RepresentationO22withUnsafeMutableBytesyxxSwKXEKlFyt_Tg574$s22WebContentRestrictions11BloomFilterC6encode2toys7Encoder_p_tKFySwXEfU_So14CFBitVectorRefa0iJ12Restrictions0lM0CTf1ncn_n
- _$s10Foundation4DataV15_RepresentationOSgWOe
- _$s10Foundation4DataV5countACSi_tcfCTf4nd_n
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufc8IteratorQz_SitSwXEfU1_SS8UTF8ViewV_TG5
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufc8IteratorQz_SitSwXEfU1_SS8UTF8ViewV_TG5TA
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufcAC15_RepresentationOSRyAEGXEfU0_
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufcAC15_RepresentationOSWXEfU_
- _$s22WebContentRestrictions16MembershipFilter_pSgWOhTm
- _OBJC_CLASS_$_MAAutoAsset
- _OBJC_CLASS_$_MAAutoAssetNotifications
- _OBJC_CLASS_$_MAAutoAssetPolicy
- _OBJC_CLASS_$_MAAutoAssetSelector
- _OBJC_IVAR_$_WCRAutoAssetClient._currentAssetSelector
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.56
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.57
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.58
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.59
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.60
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke.61
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke_2
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke_3
- ___22-[WCRBloomFilter init]_block_invoke
- ___22-[WCRBloomFilter init]_block_invoke_2
- ___71-[WCRBrowserEngineClient evaluateURL:withCompletion:onCompletionQueue:]_block_invoke
- ___block_descriptor_32_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_literal_global.123
- _objc_msgSend$URLForResource:withExtension:subdirectory:localization:
- _objc_msgSend$_blockPageForURL:inLanguage:withAllowButton:
- _objc_msgSend$_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:
- _objc_msgSend$_shouldBlock:withBloomFilter:useCipherML:
- _objc_msgSend$_shouldShowAllowButton:
- _objc_msgSend$currentAssetSelector
- _objc_msgSend$endAllPreviousLocksOfSelectorSync:forClientName:
- _objc_msgSend$initForClientName:selectingAsset:error:
- _objc_msgSend$interestInContent:completion:
- _objc_msgSend$lockContent:withUsagePolicy:withTimeout:completion:
- _objc_msgSend$notifyRegistrationName:forAssetType:forAssetSpecifier:
- _objc_msgSend$setCurrentAssetSelector:
- _objc_msgSend$setLanguage:
- _swift_release_n
- _symbolic ______pSg 10Foundation15ContiguousBytesP
CStrings:
+ " default"
+ " id=\"%@\""
+ "1"
+ "<a%@ href=\"%@\" class=\"button %@\">%@</a>"
+ "<div id=\"website\">%@ %@</div>"
+ "<img class=\"favicon\" src=\"https://%@/favicon.ico\" onerror=\"this.style.display='none';\" alt=\"Website Favicon\"/>"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "ALL_INSTANCES"
+ "ATOMIC_INSTANCE_DOWNLOADED"
+ "Add Website to Allow List"
+ "Ask Permission"
+ "Ask to Browse Website"
+ "Attempted to present AskToBrowse context menu when new ScreenTimeSettings is disabled. Falling back to old behavior."
+ "Authentication Sites"
+ "Authentication site allow list: %{sensitive}@ -> Allowed"
+ "Configuring popoverPresentationController with presentingView"
+ "Configuring popoverPresentationController with presentingViewController"
+ "Did not find overridePolicy in DC configuration. Setting the default"
+ "Ended atomic asset locks"
+ "Error creating WCRRemoteAskToViewController: %@"
+ "Error creating WCRRemoteDeviceApprovalViewController: %@"
+ "Error getting configuration from DC: %@"
+ "Failed to end atomic asset locks: %@"
+ "Failed to indicate need for content: %@"
+ "Falling back to keyWindow for the presenting view controller"
+ "Finding parent view controller"
+ "Got configuration from DC"
+ "INCLUDE_CSS_FILE"
+ "Loaded authentication sites at path %@"
+ "Loading authentication sites"
+ "Loading authentication sites from MobileAsset bundle: %@"
+ "Loading fallback authentication sites %@"
+ "Localizable"
+ "No popoverPresentationController found"
+ "Presenting Ask to Browse as page sheet (iframe context)"
+ "Requesting WCRServiceAskToAlertController"
+ "Sensitive Website"
+ "Shield symbol contents are nil! %@"
+ "Successfully indicated need for MobileAsset content"
+ "This Website is Blocked"
+ "Transitive trust: %{sensitive}@ -> Allowed"
+ "Transitive trust: %{sensitive}@ -> Not Allowed"
+ "USER_VISIBLE_BUTTONS"
+ "USER_VISIBLE_BUTTON_LINK"
+ "USER_VISIBLE_RESTRICTED_URL"
+ "USER_VISIBLE_SUBTITLE"
+ "USER_VISIBLE_SYMBOL"
+ "USER_VISIBLE_TITLE"
+ "Unable to create auto asset set instance: %@"
+ "Unable to lock any version of auto asset set content: %@"
+ "Unloading authentication sites"
+ "Unloading bloom filter"
+ "WCRAppleAllowList-2026-02-06.plist"
+ "WCRAuthenticationSites-2026-05-01.plist"
+ "WCRFilter-2026-02-06.plist"
+ "WCRServiceAskToAlertController"
+ "WCRServiceDeviceApprovalController"
+ "Website Not Allowed"
+ "You will need a parent or guardian’s permission to browse:"
+ "Your parent or guardian has blocked this website."
+ "add"
+ "ask"
+ "askForPermission"
+ "askToBrowse: user completed on-device approval: approved=%d"
+ "askToBrowse: user requested remote approval"
+ "askToBrowseURL called with presentingView and referrer: '%@'"
+ "askToBrowseURL called with referrer: '%@'"
+ "askToBrowseURL completed. result=%ld error: %@"
+ "askToBrowseURL legacy flow completed. didAllow=%d error: %@"
+ "blocked"
+ "blockiframe"
+ "checkmark.bubble.fill"
+ "com.apple.WebContentRestrictions"
+ "com.apple.WebContentRestrictions.WebContentRestrictionsFilterAssets"
+ "context"
+ "exclamationmark.shield.fill"
+ "href=\"%@&iframe=1\""
+ "iframe"
+ "limitWebProxies"
+ "localApprovalOnly"
+ "nosign"
+ "notAllowed"
+ "overridePolicy"
+ "overridePolicy from DC unrecognized: %s"
+ "overridePolicy from DC: askForPermission"
+ "overridePolicy from DC: localApprovalOnly"
+ "overridePolicy from DC: notAllowed"
+ "overridePolicy from DC: unverifiedAdultLegacyScreenTime. Using unset for now."
+ "overridePolicy from DC: unverifiedAdultScreenTime. Using unset for now."
+ "r"
+ "sensitive"
+ "shield"
+ "svg"
+ "unblock"
+ "unset"
+ "unverifiedAdultLegacyScreenTime"
+ "unverifiedAdultScreenTime"
+ "useTransitiveTrust"
+ "userApprovedURL"
+ "userRequestedDeviceApproval"
+ "v12@?0B8"
+ "v16@?0Q8"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSString\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"NSArray\"16@\"NSError\"24"
+ "x-apple-content-filter://unblock?context=%@&shield=%@"
+ "“USER_VISIBLE_RESTRICTED_URL_NO_LOC” is a restricted website."
- "%@-nooverride"
- ".cxx_destruct"
- "@\"MAAutoAssetSelector\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<WCRPINEntryViewControllerProtocol>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"WCRAppleAllowList\""
- "@\"WCRAutoAssetClient\""
- "@\"WCRBloomFilter\""
- "@\"WCRRemotePINEntryViewController\""
- "@\"WCRURLList\""
- "@\"_TtC22WebContentRestrictions15BloomFilterShim\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16B24B28"
- "@32@0:8@16^@24"
- "@36@0:8@16@24B32"
- "@?"
- "@?16@0:8"
- "ASSET_VERSION_DOWNLOADED"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8q16"
- "B36@0:8@16@24B32"
- "Ended local asset locks"
- "Failed to end asset locks: %@"
- "Failed to set interest in content: %@"
- "INCLUDE_CSS_FILE_NO_LOC"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Successfully set interest in MobileAsset content"
- "T@\"MAAutoAssetSelector\",&,V_currentAssetSelector"
- "T@\"NSDictionary\",&,V_userSettings"
- "T@\"NSMutableArray\",&,V_urlStringList"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_evaluationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_notifyQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_reloadAssetQueue"
- "T@\"NSObject<WCRPINEntryViewControllerProtocol>\",N,V_delegate"
- "T@\"NSSet\",&,V_allowList"
- "T@\"NSString\",&,N,V_configurationPath"
- "T@\"NSString\",&,N,V_localPath"
- "T@\"NSString\",&,V_language"
- "T@\"NSString\",R,N,V_localPath"
- "T@\"WCRAppleAllowList\",&,V_appleAllowList"
- "T@\"WCRAutoAssetClient\",&,N,V_autoAsset"
- "T@\"WCRBloomFilter\",&,V_bloomFilter"
- "T@\"WCRRemotePINEntryViewController\",&,N,V_remoteViewController"
- "T@\"WCRURLList\",&,N,V_macOSExemptURLList"
- "T@\"WCRURLList\",&,V_allowList"
- "T@\"WCRURLList\",&,V_allowedWebsitesOnlyList"
- "T@\"WCRURLList\",&,V_appleAllowList"
- "T@\"WCRURLList\",&,V_denyList"
- "T@\"_TtC22WebContentRestrictions15BloomFilterShim\",&,V_bloomFilter"
- "T@?,C,N,V_allowURLCompletion"
- "T@?,C,N,V_assetDidChangeHandler"
- "TB,V_useCipherML"
- "TQ,V_mode"
- "UNBLOCK_URL_NO_LOC"
- "URLForResource:withExtension:subdirectory:localization:"
- "URLWithString:"
- "UTF8String"
- "Unable to create auto-asset instance: %@"
- "Unable to lock any version of auto-asset content: %@"
- "WCRAppleAllowList"
- "WCRAppleAllowList-2025-09-29.plist"
- "WCRAutoAssetClient"
- "WCRBloomFilter"
- "WCRBrowserEngineClient"
- "WCRCipherMLClient"
- "WCRFilter-2025-09-29.plist"
- "WCRLogging"
- "WCRPINEntryViewControllerProtocol"
- "WCRRemotePINEntryViewController"
- "WCRServicePINEntryControllerProtocol"
- "WCRURLList"
- "_TtC22WebContentRestrictions11BloomFilter"
- "_TtC22WebContentRestrictions15BloomFilterShim"
- "_allowList"
- "_allowList:"
- "_allowURLCompletion"
- "_allowedWebsitesOnly:"
- "_allowedWebsitesOnlyList"
- "_allowedWebsitesOnlyList:"
- "_appleAllowList"
- "_appleAllowList:"
- "_assetDidChangeHandler"
- "_autoAsset"
- "_blockPageForURL:inLanguage:withAllowButton:"
- "_bloomFilter"
- "_configurationPath"
- "_createInterestInAsset"
- "_currentAssetSelector"
- "_defaultUserSettingsPath"
- "_delegate"
- "_denyList"
- "_denyList:"
- "_endLocalAssetLocks"
- "_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:"
- "_evaluationQueue"
- "_formattedStringFromURLString:fromBrowser:removePort:"
- "_handleAssetChangedNotification"
- "_language"
- "_loadFilterResourcesFromLocalFallback"
- "_loadFilterResourcesFromMobileAsset"
- "_loadFilterResourcesFromMobileAsset:"
- "_loadFilterResourcesWithMobileAssetPath:"
- "_localPath"
- "_lockLocalAsset:"
- "_lp_simplifiedDisplayString"
- "_macOSExemptURLList"
- "_matchingStringsForDomain:"
- "_matchingStringsForURL:"
- "_mode"
- "_mode:"
- "_nameOfNewestFile:"
- "_notifyQueue"
- "_performLazyInitialization"
- "_preferredLanguageForUserName:"
- "_registerForNotificationsForAssetType:andAssetSpecifier:"
- "_reloadAssetQueue"
- "_reloadConfiguration"
- "_remoteViewController"
- "_shouldBlock:withBloomFilter:useCipherML:"
- "_shouldEvaluateURLsForConfigurationAtPath:"
- "_shouldShowAllowButton:"
- "_urlStringList"
- "_useCipherML"
- "_userSettings"
- "absoluteString"
- "activateCipherML"
- "addObject:"
- "addObjectsFromArray:"
- "addURLString:"
- "allObjects"
- "allowList"
- "allowURL:withCompletion:"
- "allowURLCompletion"
- "allowURLWithFamilyControls:withCompletion:"
- "allowedURLStrings"
- "allowedWebsitesOnlyList"
- "appleAllowList"
- "assetDidChangeHandler"
- "autoAsset"
- "base64EncodedDataWithOptions:"
- "base64StringFromString:"
- "bitVector"
- "bloomFilter"
- "boolValue"
- "bundleForClass:"
- "bundleWithPath:"
- "cancel"
- "categoryForCategoryLetter:"
- "categoryForString:withError:"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configurationPath"
- "contains:"
- "containsString:"
- "containsURLString:"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createInterestInAsset"
- "currentAssetSelector"
- "currentDevice"
- "dataByStringKeyword:error:"
- "dataUsingEncoding:"
- "dealloc"
- "defaultManager"
- "delegate"
- "denyList"
- "description"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "dismissViewControllerAnimated:completion:"
- "en"
- "endAllPreviousLocksOfSelectorSync:forClientName:"
- "errorWithDomain:code:userInfo:"
- "evaluateURL:withCompletion:"
- "evaluateURL:withCompletion:onCompletionQueue:"
- "evaluationQueue"
- "exportedInterface"
- "fileExistsAtPath:"
- "filter"
- "firstObject"
- "fragment"
- "generateMacOSExemptURLList"
- "getIsPINPresentWithCompletion:"
- "hasPrefix:"
- "hasSuffix:"
- "host"
- "init"
- "initForAssetType:withAssetSpecifier:"
- "initForClientName:selectingAsset:error:"
- "initFromFile:"
- "initWithClientConfig:"
- "initWithConfigurationAtPath:"
- "initWithContentsOfFile:"
- "initWithData:encoding:"
- "initWithPath:"
- "initWithUseCase:"
- "integerValue"
- "interestInContent:completion:"
- "interfaceWithProtocol:"
- "isEqualToString:"
- "isLegacyExemptURL:"
- "isNumericPIN"
- "keyWindow"
- "language"
- "lastObject"
- "lastPathComponent"
- "localPath"
- "localizations"
- "lockContent:withUsagePolicy:withTimeout:completion:"
- "log:withType:"
- "lowercaseString"
- "macOSExemptURLList"
- "mode"
- "notifyQueue"
- "notifyRegistrationName:forAssetType:forAssetSpecifier:"
- "objectForKey:"
- "path"
- "pathComponents"
- "pathExtension"
- "pathForResource:ofType:"
- "permitURLWithCompletion:"
- "port"
- "preferredLocalizationsFromArray:forPreferences:"
- "presentViewController:animated:completion:"
- "query"
- "registerForAssetChangedNotificationsWithBlock:"
- "reloadAssetQueue"
- "remoteViewController"
- "reportAnalyticsBloomFilterBlocked"
- "reportAnalyticsBloomFilterVersion:withAppleAllowListVersion:"
- "requestAllowListAuthenticationForURL:withCompletion:"
- "requestStatusForClientConfig:options:completionHandler:"
- "requestViewController:fromServiceWithBundleIdentifier:connectionHandler:"
- "requiresKeyboard"
- "rootViewController"
- "scheme"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "setAllowList:"
- "setAllowURLCompletion:"
- "setAllowedWebsitesOnlyList:"
- "setAppleAllowList:"
- "setAssetDidChangeHandler:"
- "setAutoAsset:"
- "setBloomFilter:"
- "setConfigurationPath:"
- "setCurrentAssetSelector:"
- "setDelegate:"
- "setDenyList:"
- "setEvaluationQueue:"
- "setLanguage:"
- "setLocalPath:"
- "setMacOSExemptURLList:"
- "setModalPresentationStyle:"
- "setMode:"
- "setNotifyQueue:"
- "setPageTitle:"
- "setReloadAssetQueue:"
- "setRemoteViewController:"
- "setURL:"
- "setUrlStringList:"
- "setUseCipherML:"
- "setUserInitiated:"
- "setUserSettings:"
- "setWithArray:"
- "setWithCapacity:"
- "sharedApplication"
- "shouldAutorotateToInterfaceOrientation:"
- "shouldBlock:"
- "shouldEvaluateURLs"
- "shouldEvaluateURLsForConfigurationAtPath:"
- "simplePIN"
- "sortedArrayUsingComparator:"
- "startUsingLocalAsset:"
- "status"
- "stopUsingLocalAsset"
- "stringByAddingPercentEscapesUsingEncoding:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingPathExtension"
- "stringByRemovingPercentEncoding"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByReplacingPercentEscapesUsingEncoding:"
- "stringWithContentsOfURL:encoding:error:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "supportedInterfaceOrientations"
- "urlStringList"
- "urlToFormattedString:"
- "useCipherML"
- "userDidCancel"
- "userEnteredCorrectPIN"
- "userInterfaceIdiom"
- "userSettings"
- "v112@0:8@16Q24@32@40@48@56@64@72@80@88@?96@104"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v40@0:8@16@?24@32"
- "v44@?0@\"MAAutoAssetSelector\"8B16@\"NSURL\"20@\"MAAutoAssetStatus\"28@\"NSError\"36"
- "viewDidLoad"

```
