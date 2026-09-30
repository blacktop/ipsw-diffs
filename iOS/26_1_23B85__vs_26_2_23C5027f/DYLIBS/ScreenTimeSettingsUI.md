## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-605.1.19.101.0
-  __TEXT.__text: 0x11df74
-  __TEXT.__auth_stubs: 0x2dd0
-  __TEXT.__objc_methlist: 0xbccc
+605.2.3.0.0
+  __TEXT.__text: 0x11f2c4
+  __TEXT.__auth_stubs: 0x2e50
+  __TEXT.__objc_methlist: 0xbd94
   __TEXT.__const: 0x3b34
-  __TEXT.__cstring: 0xe1d9
-  __TEXT.__oslogstring: 0x53f3
-  __TEXT.__gcc_except_tab: 0x10ac
+  __TEXT.__cstring: 0xe249
+  __TEXT.__oslogstring: 0x5493
+  __TEXT.__gcc_except_tab: 0x10e0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x3cee
+  __TEXT.__swift5_typeref: 0x3cf4
   __TEXT.__constg_swiftt: 0x14d8
   __TEXT.__swift5_reflstr: 0xa00
   __TEXT.__swift5_fieldmd: 0xbc8
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x2d8
-  __TEXT.__swift5_capture: 0xc3c
+  __TEXT.__swift5_capture: 0xc8c
   __TEXT.__swift5_proto: 0xec
   __TEXT.__swift5_types: 0x100
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0x90
-  __TEXT.__unwind_info: 0x3a08
-  __TEXT.__eh_frame: 0x2060
-  __TEXT.__objc_classname: 0x1d3c
-  __TEXT.__objc_methname: 0x2160c
-  __TEXT.__objc_methtype: 0x3972
-  __TEXT.__objc_stubs: 0x149c0
-  __DATA_CONST.__got: 0x13f0
-  __DATA_CONST.__const: 0x23d0
-  __DATA_CONST.__objc_classlist: 0x740
+  __TEXT.__unwind_info: 0x3a58
+  __TEXT.__eh_frame: 0x20a8
+  __TEXT.__objc_classname: 0x1d5f
+  __TEXT.__objc_methname: 0x21a03
+  __TEXT.__objc_methtype: 0x39bc
+  __TEXT.__objc_stubs: 0x14c60
+  __DATA_CONST.__got: 0x13f8
+  __DATA_CONST.__const: 0x23d8
+  __DATA_CONST.__objc_classlist: 0x748
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69a8
+  __DATA_CONST.__objc_selrefs: 0x6a40
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x16f8
-  __AUTH_CONST.__const: 0x30b8
-  __AUTH_CONST.__cfstring: 0xa940
-  __AUTH_CONST.__objc_const: 0x24070
+  __AUTH_CONST.__auth_got: 0x1738
+  __AUTH_CONST.__const: 0x3158
+  __AUTH_CONST.__cfstring: 0xa980
+  __AUTH_CONST.__objc_const: 0x24200
   __AUTH_CONST.__objc_intobj: 0x840
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH.__objc_data: 0x4c38
+  __AUTH.__objc_data: 0x4c88
   __AUTH.__data: 0xa00
-  __DATA.__objc_ivar: 0xc74
+  __DATA.__objc_ivar: 0xc88
   __DATA.__data: 0x2498
   __DATA.__bss: 0x1e08
   __DATA.__common: 0xa0

   - /System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift
   - /System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI
   - /System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore
+  - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BC44FDEE-9028-3C5F-90F9-409261FBC51B
-  Functions: 6004
-  Symbols:   15823
-  CStrings:  8980
+  UUID: 67F75814-0EBC-3157-A3CB-74BF29CD831A
+  Functions: 6034
+  Symbols:   15901
+  CStrings:  9019
 
Symbols:
+ -[STCommunicationSafetyListController _shouldForceCommunicationSafetyEnabled]
+ -[STCommunicationSafetyViewModel setShouldForceCommunicationSafetyEnabled:]
+ -[STCommunicationSafetyViewModel shouldForceCommunicationSafetyEnabled]
+ -[STCommunicationSafetyViewModelCoordinator _shouldForceCommunicationSafetyEnabled]
+ -[STCommunicationSafetyViewModelCoordinator _shouldForceCommunicationSafetyEnabled].cold.1
+ -[STContentPrivacyMediaRestrictionsDetailController _shouldForceWebFilterToLimitAdultWebsites]
+ -[STContentPrivacyViewModel isWebContentFilterForcedToLimitAdultWebsites]
+ -[STContentPrivacyViewModel setIsWebContentFilterForcedToLimitAdultWebsites:]
+ -[STContentPrivacyViewModelCoordinator _isWebContentFilterForced]
+ -[STContentPrivacyViewModelCoordinator _isWebContentFilterForced].cold.1
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]
+ -[STContentPrivacyViewModelCoordinator regulatoryManager]
+ -[STRootViewController handleURLResourceDictionaryDidChange:]
+ -[STRootViewController setUrlCoordinator:]
+ -[STRootViewController urlCoordinator]
+ -[STRootViewControllerURLCoordinator .cxx_destruct]
+ -[STRootViewControllerURLCoordinator setUrlResourceDictionary:]
+ -[STRootViewControllerURLCoordinator urlResourceDictionary]
+ -[STWebFilterDetailController _shouldForceWebFilterToLimitAdultWebsites]
+ GCC_except_table102
+ GCC_except_table15
+ _OBJC_CLASS_$_STRegulatoryManager
+ _OBJC_CLASS_$_STRootViewControllerURLCoordinator
+ _OBJC_IVAR_$_STCommunicationSafetyViewModel._shouldForceCommunicationSafetyEnabled
+ _OBJC_IVAR_$_STContentPrivacyViewModel._isWebContentFilterForcedToLimitAdultWebsites
+ _OBJC_IVAR_$_STContentPrivacyViewModelCoordinator._regulatoryManager
+ _OBJC_IVAR_$_STRootViewController._urlCoordinator
+ _OBJC_IVAR_$_STRootViewControllerURLCoordinator._urlResourceDictionary
+ _OBJC_METACLASS_$_STRootViewControllerURLCoordinator
+ _STRootViewControllerURLCoordinatorSpecifierKey
+ __OBJC_$_INSTANCE_METHODS_STRootViewControllerURLCoordinator
+ __OBJC_$_INSTANCE_METHODS_UIViewController(SettingsPop|ScreenTimeSettingsUI)
+ __OBJC_$_INSTANCE_VARIABLES_STRootViewControllerURLCoordinator
+ __OBJC_$_PROP_LIST_STCommunicationSafetyViewModelCoordinator.180
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.987
+ __OBJC_$_PROP_LIST_STRootViewControllerURLCoordinator
+ __OBJC_CLASS_RO_$_STRootViewControllerURLCoordinator
+ __OBJC_METACLASS_RO_$_STRootViewControllerURLCoordinator
+ ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.59
+ ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.60
+ ___143-[STCommunicationSafetyViewModelCoordinator saveCommunicationSafetyReceivingRestricted:communicationSafetySendingRestricted:completionHandler:]_block_invoke.62
+ ___189-[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]_block_invoke
+ ___59-[STCommunicationSafetyViewModelCoordinator _loadViewModel]_block_invoke.56
+ ___61-[STRootViewController handleURLResourceDictionaryDidChange:]_block_invoke
+ ___61-[STRootViewController handleURLResourceDictionaryDidChange:]_block_invoke_2
+ ___61-[STRootViewController handleURLResourceDictionaryDidChange:]_block_invoke_3
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.798
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.798.cold.1
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.800
+ ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.809
+ ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.808
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.820
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_53_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_86_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_95_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.990
+ _objc_msgSend$_isWebContentFilterForced
+ _objc_msgSend$_shouldForceCommunicationSafetyEnabled
+ _objc_msgSend$_shouldForceWebFilterToLimitAdultWebsites
+ _objc_msgSend$colorWithAlphaComponent:
+ _objc_msgSend$create
+ _objc_msgSend$handleURL:withCompletion:
+ _objc_msgSend$handleURLResourceDictionaryDidChange:
+ _objc_msgSend$initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:
+ _objc_msgSend$isCommunicationSafetyForcedToEnabledAndReturnError:
+ _objc_msgSend$isWebContentFilterForcedToLimitAdultWebsites
+ _objc_msgSend$isWebContentFilterForcedToLimitAdultWebsitesAndReturnError:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$popToRootOfScreenTimeSettingsIfPossibleWithCompletion:
+ _objc_msgSend$prepareHandlingURLForSpecifierID:resourceDictionary:animatePush:withCompletion:
+ _objc_msgSend$regulatoryManager
+ _objc_msgSend$setIsWebContentFilterForcedToLimitAdultWebsites:
+ _objc_msgSend$setShouldForceCommunicationSafetyEnabled:
+ _objc_msgSend$setUrlCoordinator:
+ _objc_msgSend$setUrlResourceDictionary:
+ _objc_msgSend$shouldForceCommunicationSafetyEnabled
+ _objc_msgSend$urlCoordinator
+ _objc_msgSend$urlResourceDictionary
+ _symbolic ytSg
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]
- GCC_except_table100
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIViewController_$_SettingsPop
- __OBJC_$_PROP_LIST_STCommunicationSafetyViewModelCoordinator.172
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.976
- ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.54
- ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.55
- ___143-[STCommunicationSafetyViewModelCoordinator saveCommunicationSafetyReceivingRestricted:communicationSafetySendingRestricted:completionHandler:]_block_invoke.57
- ___171-[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]_block_invoke
- ___59-[STCommunicationSafetyViewModelCoordinator _loadViewModel]_block_invoke.51
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.794
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.794.cold.1
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.796
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke_2
- ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.804
- ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.803
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.815
- ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_85_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_85_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_94_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.979
- _objc_msgSend$initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:
CStrings:
+ "@\"<STRegulatoryManagerProtocol>\""
+ "@\"STRootViewControllerURLCoordinator\""
+ "@68@0:8@16@24@32@40@48B56@?60"
+ "Error checking if web content filter is forced: %{public}@ ; assuming forced"
+ "Failed to determine if Communication Safety is forced: %{public}@ ; assuming forced"
+ "RootViewControllerURLCoordinatorSpecifierKey"
+ "STRootViewControllerURLCoordinator"
+ "ScreenTimeSettingsUI"
+ "T@\"<STRegulatoryManagerProtocol>\",R,N,V_regulatoryManager"
+ "T@\"NSDictionary\",C,N,V_urlResourceDictionary"
+ "T@\"STRootViewControllerURLCoordinator\",&,N,V_urlCoordinator"
+ "TB,N,V_isWebContentFilterForcedToLimitAdultWebsites"
+ "TB,N,V_shouldForceCommunicationSafetyEnabled"
+ "_isWebContentFilterForced"
+ "_isWebContentFilterForcedToLimitAdultWebsites"
+ "_regulatoryManager"
+ "_shouldForceCommunicationSafetyEnabled"
+ "_shouldForceWebFilterToLimitAdultWebsites"
+ "_urlCoordinator"
+ "_urlResourceDictionary"
+ "aa_uk_restrictions"
+ "colorWithAlphaComponent:"
+ "create"
+ "handleURLResourceDictionaryDidChange:"
+ "initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:"
+ "isCommunicationSafetyForcedToEnabledAndReturnError:"
+ "isWebContentFilterForcedToLimitAdultWebsites"
+ "isWebContentFilterForcedToLimitAdultWebsitesAndReturnError:"
+ "pathComponents"
+ "popToRootOfScreenTimeSettingsIfPossibleWithCompletion:"
+ "regulatoryManager"
+ "setIsWebContentFilterForcedToLimitAdultWebsites:"
+ "setShouldForceCommunicationSafetyEnabled:"
+ "setUrlCoordinator:"
+ "setUrlResourceDictionary:"
+ "shouldForceCommunicationSafetyEnabled"
+ "urlCoordinator"
+ "urlResourceDictionary"
- "@60@0:8@16@24@32@40B48@?52"
- "initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:loadCompletionHandler:"

```
