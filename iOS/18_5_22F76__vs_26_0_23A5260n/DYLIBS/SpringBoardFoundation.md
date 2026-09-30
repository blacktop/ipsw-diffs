## SpringBoardFoundation

> `/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`

```diff

-4503.5.9.0.0
-  __TEXT.__text: 0xab3f4
-  __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_methlist: 0x7e8c
-  __TEXT.__const: 0x2170
-  __TEXT.__cstring: 0xd21d
-  __TEXT.__gcc_except_tab: 0x760
+4552.106.0.0.0
+  __TEXT.__text: 0xae618
+  __TEXT.__auth_stubs: 0x1940
+  __TEXT.__objc_methlist: 0x7ff4
+  __TEXT.__const: 0x2258
+  __TEXT.__cstring: 0xda4e
+  __TEXT.__gcc_except_tab: 0x7d8
   __TEXT.__dlopen_cstrs: 0x4d2
-  __TEXT.__oslogstring: 0x2f36
+  __TEXT.__oslogstring: 0x2ecd
   __TEXT.__ustring: 0x2e4
-  __TEXT.__unwind_info: 0x2130
+  __TEXT.__unwind_info: 0x2160
   __TEXT.__objc_classname: 0x1a10
-  __TEXT.__objc_methname: 0x18e67
-  __TEXT.__objc_methtype: 0x333d
-  __TEXT.__objc_stubs: 0xe000
-  __DATA_CONST.__got: 0xc00
-  __DATA_CONST.__const: 0x1960
+  __TEXT.__objc_methname: 0x195cf
+  __TEXT.__objc_methtype: 0x335c
+  __TEXT.__objc_stubs: 0xe300
+  __DATA_CONST.__got: 0xc18
+  __DATA_CONST.__const: 0x1968
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e80
+  __DATA_CONST.__objc_selrefs: 0x4fb0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x508
-  __AUTH_CONST.__auth_got: 0xc38
-  __AUTH_CONST.__const: 0xce0
-  __AUTH_CONST.__cfstring: 0xb060
-  __AUTH_CONST.__objc_const: 0x19658
-  __AUTH_CONST.__objc_intobj: 0x570
+  __AUTH_CONST.__auth_got: 0xcb0
+  __AUTH_CONST.__const: 0xd00
+  __AUTH_CONST.__cfstring: 0xb220
+  __AUTH_CONST.__objc_const: 0x19968
+  __AUTH_CONST.__objc_intobj: 0x588
   __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH_CONST.__objc_doubleobj: 0x4f0
+  __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH.__objc_data: 0x37a0
-  __DATA.__objc_ivar: 0x9b0
+  __DATA.__objc_ivar: 0x9d8
   __DATA.__data: 0x14ca
-  __DATA.__bss: 0x838
-  __DATA.__common: 0x8
+  __DATA.__bss: 0x840
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CCED53A-F8D7-35FD-A187-9DBDF59906B6
-  Functions: 3564
-  Symbols:   12444
-  CStrings:  8329
+  UUID: 6A9BDF03-6FD4-36C3-A4E5-1893031A455D
+  Functions: 3657
+  Symbols:   12643
+  CStrings:  8481
 
Symbols:
+ +[SBDisplayModePredicate forDisplaysSimilarToDisplay:]
+ +[SBDisplayScaleMapping withDisplay:]
+ +[SBDisplayScaleMapping withDisplay:].cold.1
+ +[SBDisplayScaleMapping withDisplay:].cold.2
+ -[SBAppSwitcherDefaults _shouldMedusaMultitaskingEnabledByDefault]
+ -[SBFDateTimeController hasDateOverride]
+ -[SBFDateTimeController overrideDateWithAutoupdatingSeconds]
+ -[SBFDateTimeController setOverrideDateWithAutoupdatingSeconds:]
+ -[SBFLockScreenDateView _updatePreferredContentSizeCategoryForEnvironment:previousTraitCollection:]
+ -[SBFLockScreenDateView dealloc]
+ -[SBFLockScreenDateView maximumAdaptiveTimeTextHeight]
+ -[SBFLockScreenDateView posterHasComplications]
+ -[SBFLockScreenDateView setMaximumAdaptiveTimeTextHeight:]
+ -[SBFLockScreenDateView setPosterHasComplications:]
+ -[SBFLockScreenDateView setTimeSupportsStretch:]
+ -[SBFLockScreenDateView timeSupportsStretch]
+ -[SBFLockScreenDateView timeView]
+ -[SBFLockScreenDateViewController _backlightLuminanceChangedForEnvironment:previousTraitCollection:]
+ -[SBFLockScreenDateViewController _timeAnimationIntervalToUse]
+ -[SBFLockScreenDateViewController _updateCompactTime]
+ -[SBFLockScreenDateViewController adaptiveTextHeight]
+ -[SBFLockScreenDateViewController hasSidebarContents]
+ -[SBFLockScreenDateViewController setHasSidebarContents:]
+ -[SBFLockScreenDateViewController setShowCompactTime:]
+ -[SBFLockScreenDateViewController setShowCompactTime:animated:]
+ -[SBFLockScreenDateViewController setTimeSupportsStretch:]
+ -[SBFLockScreenDateViewController showCompactTime]
+ -[SBFOverridableDateProvider additionalOffset]
+ -[SBFOverridableDateProvider setAdditionalOffset:]
+ -[SBFSceneWorkspaceDefaultDelegate sceneDidDeactivate:withContext:]
+ -[SBHomeScreenDefaults .cxx_destruct]
+ -[SBHomeScreenDefaults iconUserInterfaceStyle]
+ -[SBHomeScreenDefaults setIconUserInterfaceStyle:]
+ -[_SBDisplaysWithSizePredicate initWithDisplay:]
+ -[_SBDisplaysWithSizePredicate initWithDisplay:].cold.1
+ GCC_except_table41
+ GCC_except_table57
+ GCC_except_table63
+ _ACMContextCopyData
+ _ACMContextCreateWithFlags
+ _ACMDecryptData
+ _ACMDecryptDataEx
+ _ACMEncryptData
+ _ACMEncryptDataEx
+ _CoverSheetKitLibrary
+ _CoverSheetKitLibrary.cold.1
+ _DefaultParallaxMotionEffectDefaultValueFunction
+ _FlexibleWindowingUIDefaultValueFunction
+ _LibCall_ACMContextContainsCredentialTypeEx
+ _LibCall_ACMContextCopyData
+ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
+ _LibSer_ACMDeserializeEnvironmentVariableType
+ _LibSer_ACMDeserializeSEPControlCode
+ _LibSer_GetSerializedContainsCredential_GetSize
+ _LibSer_GetSerializedContainsCredential_Serialize
+ _LightSourceMotionEffectsDefaultValueFunction
+ _MGGetSInt64Answer
+ _MotionEffectsDefaultValueFunction
+ _OBJC_CLASS_$_UITraitBacklightLuminance
+ _OBJC_CLASS_$_UITraitLegibilityWeight
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ _OBJC_IVAR_$_SBFDateTimeController._overrideDateWithAutoupdatingSeconds
+ _OBJC_IVAR_$_SBFLockScreenDateView._contentSizeCategoryTraitChangeRegistration
+ _OBJC_IVAR_$_SBFLockScreenDateView._maximumAdaptiveTimeTextHeight
+ _OBJC_IVAR_$_SBFLockScreenDateView._posterHasComplications
+ _OBJC_IVAR_$_SBFLockScreenDateView._timeSupportsStretch
+ _OBJC_IVAR_$_SBFLockScreenDateViewController._luminanceTraitChangeRegistration
+ _OBJC_IVAR_$_SBFLockScreenDateViewController._miscellaneousDefaults
+ _OBJC_IVAR_$_SBFLockScreenDateViewController._miscellaneousDefaultsObserver
+ _OBJC_IVAR_$_SBFLockScreenDateViewController._showCompactTime
+ _OBJC_IVAR_$_SBHomeScreenDefaults._iconUserInterfaceStyle
+ _SBFAreLightSourceMotionEffectsAvailable
+ _SBFAreMotionEffectsAvailable
+ _SBFIsDefaultParallaxMotionEffectAvailable
+ _SBFIsFlexibleWindowingUIAvailable
+ _SBFIsSwitcherForegroundAppsAvailable
+ _SBFIsWindowFlatteningAvailable
+ _SBFTestWithDefaultParallaxMotionEffect
+ _SBFTestWithFlexibleWindowingUI
+ _SBFTestWithLightSourceMotionEffects
+ _SBFTestWithMotionEffects
+ _SBFTestWithSwitcherForegroundApps
+ _SBFTestWithWindowFlattening
+ _SBLogSensitiveUI
+ _SBLogSensitiveUI.__logObj
+ _SBLogSensitiveUI.cold.1
+ _SBLogSensitiveUI.onceToken
+ _SwitcherForegroundAppsDefaultValueFunction
+ _SwitcherForegroundAppsDefaultValueFunction.cold.1
+ _WindowFlatteningDefaultValueFunction
+ __OBJC_$_INSTANCE_VARIABLES_SBHomeScreenDefaults
+ __OBJC_$_PROP_LIST_SBFDateProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBFDateProviding
+ __UISolariumEnabled
+ ___37+[SBDisplayScaleMapping withDisplay:]_block_invoke
+ ___37+[SBDisplayScaleMapping withDisplay:]_block_invoke.84
+ ___51-[SBMiscellaneousDefaults _bindAndRegisterDefaults]_block_invoke
+ ___58-[SBFLockScreenDateViewController initWithNibName:bundle:]_block_invoke_2
+ ___99-[SBFLockScreenDateView _updatePreferredContentSizeCategoryForEnvironment:previousTraitCollection:]_block_invoke
+ ___DefaultParallaxMotionEffectStorage
+ ___FlexibleWindowingUIStorage
+ ___LightSourceMotionEffectsStorage
+ ___MotionEffectsStorage
+ ___SBLogSensitiveUI_block_invoke
+ ___SwitcherForegroundAppsStorage
+ ___WindowFlatteningStorage
+ ___block_descriptor_56_e8_32s40s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8
+ ___block_literal_global.31
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___getCSProminentDisplayViewClass_block_invoke
+ ___getCSProminentDisplayViewClass_block_invoke.cold.1
+ __bindAndRegisterDefaults.onceToken
+ _acm_mem_alloc_typed
+ _cc_clear
+ _cc_cmp_safe
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccgcm_context_size
+ _ccgcm_finalize
+ _ccgcm_init
+ _ccgcm_set_iv
+ _ccgcm_update
+ _cchkdf
+ _ccrng
+ _ccsha256_di
+ _checkCCError
+ _crypto_decryptText
+ _crypto_decryptText_version1
+ _crypto_decryptText_version2
+ _crypto_deriveKeyAndDecryptData
+ _crypto_deriveKeyAndEncryptData
+ _crypto_encryptText
+ _crypto_encryptText_version1
+ _crypto_encryptText_version2
+ _crypto_encryptedTextLength
+ _crypto_generateKey
+ _crypto_generateKeyFromSharedInfo
+ _crypto_generateRandomSaltLazily
+ _crypto_plainTextLength
+ _generateRandom
+ _getCSProminentDisplayViewClass.softClass
+ _getRequirementDataSizeForVersion
+ _getRequirementDataSizeForVersion.cold.1
+ _getRequirementDataSizeForVersion.cold.2
+ _objc_msgSend$_shouldMedusaMultitaskingEnabledByDefault
+ _objc_msgSend$_timeAnimationIntervalToUse
+ _objc_msgSend$_updateCompactTime
+ _objc_msgSend$adaptiveTimeTextHeight
+ _objc_msgSend$additionalOffset
+ _objc_msgSend$animatesTimeChanges
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateByAddingUnit:value:toDate:options:
+ _objc_msgSend$forDisplaysSimilarToDisplay:
+ _objc_msgSend$hasSidebarContents
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$maximumAdaptiveTimeTextHeight
+ _objc_msgSend$prominentDisplayViewController
+ _objc_msgSend$registerForTraitChanges:withAction:
+ _objc_msgSend$registerForTraitChanges:withTarget:action:
+ _objc_msgSend$sensitiveUIEnabled
+ _objc_msgSend$setAdaptiveTimeTextHeight:
+ _objc_msgSend$setAdaptsTimeTextHeight:
+ _objc_msgSend$setAdditionalOffset:
+ _objc_msgSend$setAnimatesTimeChanges:
+ _objc_msgSend$setHasSidebarContents:
+ _objc_msgSend$setShowsCompactTime:
+ _objc_msgSend$setShowsCompactTime:animated:
+ _objc_msgSend$setTimeSupportsStretch:
+ _objc_msgSend$timeChangeAnimationDuration
+ _objc_msgSend$timeView
+ _objc_msgSend$unregisterForTraitChanges:
+ _objc_msgSend$withDisplay:
+ _platform_rng.state
+ _strlen
- +[SBDisplayModePredicate forDisplaysSimilarToDisplay:useNativeSize:]
- +[SBDisplayScaleMapping withDisplay:useNativeSize:]
- +[SBDisplayScaleMapping withDisplay:useNativeSize:].cold.1
- +[SBDisplayScaleMapping withDisplay:useNativeSize:].cold.2
- -[SBFLockScreenDateView traitCollectionDidChange:]
- -[SBFSceneWorkspaceDefaultDelegate sceneDidDeactivate:withError:]
- -[_SBDisplaysWithSizePredicate initWithDisplay:useNativeSize:]
- -[_SBDisplaysWithSizePredicate initWithDisplay:useNativeSize:].cold.1
- GCC_except_table52
- GCC_except_table54
- GCC_except_table7
- _MoreForegroundAppsDefaultValueFunction
- _MoreForegroundAppsDefaultValueFunction.cold.1
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- _SBFIsMoreForegroundAppsAvailable
- _SBFTestWithMoreForegroundApps
- ___50-[SBFLockScreenDateView traitCollectionDidChange:]_block_invoke
- ___51+[SBDisplayScaleMapping withDisplay:useNativeSize:]_block_invoke
- ___51+[SBDisplayScaleMapping withDisplay:useNativeSize:]_block_invoke.84
- ___MoreForegroundAppsStorage
- ___block_descriptor_72_e8_32s40s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8
- ___block_literal_global.38
- ___block_literal_global.40
- ___getCSProminentLayoutControllerClass_block_invoke.cold.2
- _acm_mem_alloc
- _gAllocatedBytes
- _objc_msgSend$chamois_97748869
- _objc_msgSend$forDisplaysSimilarToDisplay:useNativeSize:
- _objc_msgSend$initWithDisplay:useNativeSize:
- _objc_msgSend$withDisplay:useNativeSize:
CStrings:
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "%{public}@ %{public}@ highBandwidth: %{BOOL}u refreshRate: %.2g virtual: %{BOOL}u"
+ "%{public}@ CADisplay returned referencePixelSize of %{public}@ while the nativeSize is %{public}@"
+ "%{public}@ about to calculate available logicalScales. dumping display mode info:"
+ "%{public}@ currentMode: %{public}@ highBandwidth: %{BOOL}u refreshRate: %.2g virtual: %{BOOL}u"
+ "%{public}@ logicalScale bounds: {%.3f, %.3f}"
+ "%{public}@ logicalScale is out of the supported PPI range, so filtering out: %.2f; ppi: %.2f"
+ "%{public}@ nativeSize: %{public}@"
+ "%{public}@ not supported because we couldn't derive any usable resolutions"
+ "%{public}@ physicalSize: %{public}@"
+ "%{public}@ preferredMode: %{public}@ highBandwidth: %{BOOL}u refreshRate: %.2g virtual: %{BOOL}u"
+ "%{public}@ referenceSize (from preferred): %{public}@"
+ "%{public}@ scaling using: %{public}@; logicalScales before filtering on PPI: %{public}@"
+ "%{public}@ whoops -- we filtered out every logicalScale. stuff the best one back in: %.2f"
+ "-[SBMiscellaneousDefaults _bindAndRegisterDefaults]"
+ "@\"<UITraitChangeRegistration>\""
+ "ACMContextCopyData"
+ "ACMContextCreateWithFlags"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "CSProminentDisplayView"
+ "Class getCSProminentDisplayViewClass(void)_block_invoke"
+ "DeviceMemorySize"
+ "FlexibleWindowing"
+ "InspectorGadget"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "Migrating sensitive UI epoch from %@ to %d. SBSensitiveUIEnabled was %@"
+ "No sensitive UI epoch migration required"
+ "NorthByNorthwest"
+ "Notification"
+ "SBBackgroundNethermostWindows"
+ "SBCoverSheetDisableDeviceMotionEffectPerformanceOptimizations"
+ "SBCoverSheetProportionalAdaptiveTime"
+ "SBDefaultParallaxMotionEffect"
+ "SBFlexibleWindowingAutomaticStageCreationEnabledExternal"
+ "SBFlexibleWindowingManualStageCreationShouldRestorePreviousOpenWindows"
+ "SBFlexibleWindowingPreviouslyEnabledAutomaticStageCreation"
+ "SBFlexibleWindowingUI"
+ "SBLightSourceMotionEffects"
+ "SBMainDisplayDarkeningPercentage"
+ "SBMenuBarDemoMode"
+ "SBMotionEffects"
+ "SBNotificationVisibleIdleTimer"
+ "SBSensitiveUIEpoch"
+ "SBShouldInsertDownloadFileStackIconToFloatingDock"
+ "SBSwitcherForegroundApps"
+ "SBWantsManyForegroundWindows"
+ "SBWindowFlattening"
+ "Salvador"
+ "SensitiveUI"
+ "SwitcherForegroundApps"
+ "T@\"NSDate\",C,N,V_overrideDateWithAutoupdatingSeconds"
+ "T@\"NSString\",C,N,V_iconUserInterfaceStyle"
+ "T@\"UIView\",R,N"
+ "TB,N,V_posterHasComplications"
+ "TB,N,V_showCompactTime"
+ "TB,N,V_timeSupportsStretch"
+ "Td,?,N"
+ "Td,N,V_maximumAdaptiveTimeTextHeight"
+ "TinyTim"
+ "Vertigo"
+ "VertigoParallax"
+ "WindowFlattening"
+ "[SBValidateLogicalScale()] we're dropping logicalScale of %g because it's outside of logicalScaleLimits %{public}@; caDisplay: (%p) %{public}@"
+ "[SBValidateLogicalScale()] we're dropping logicalScale of %g because scaledDisplaySize %{public}@ [%{public}@] is over our hard-coded display pipeline limit of %{public}@. logicalScaleLimits: %{public}@; caDisplay: (%p) %{public}@"
+ "_backlightLuminanceChangedForEnvironment:previousTraitCollection:"
+ "_contentSizeCategoryTraitChangeRegistration"
+ "_iconUserInterfaceStyle"
+ "_luminanceTraitChangeRegistration"
+ "_maximumAdaptiveTimeTextHeight"
+ "_miscellaneousDefaults"
+ "_miscellaneousDefaultsObserver"
+ "_overrideDateWithAutoupdatingSeconds"
+ "_posterHasComplications"
+ "_shouldMedusaMultitaskingEnabledByDefault"
+ "_showCompactTime"
+ "_timeAnimationIntervalToUse"
+ "_timeSupportsStretch"
+ "_updateCompactTime"
+ "_updatePreferredContentSizeCategoryForEnvironment:previousTraitCollection:"
+ "acm_transport"
+ "adaptiveTextHeight"
+ "adaptiveTimeTextHeight"
+ "additionalOffset"
+ "animatesTimeChanges"
+ "areDeviceMotionEffectPerformanceOptimizationsDisabled"
+ "backgroundNethermostWindows"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
+ "crypto_decryptText"
+ "crypto_decryptText_version1"
+ "crypto_decryptText_version2"
+ "crypto_deriveKeyAndDecryptData"
+ "crypto_deriveKeyAndEncryptData"
+ "crypto_encryptText"
+ "crypto_encryptText_version1"
+ "crypto_encryptText_version2"
+ "crypto_generateKey"
+ "crypto_generateKeyFromSharedInfo"
+ "crypto_generateKeyFromSharedInfo_version1"
+ "crypto_generateKeyFromSharedInfo_version2"
+ "crypto_generateRandomSaltLazily"
+ "currentCalendar"
+ "dateByAddingUnit:value:toDate:options:"
+ "false"
+ "flexibleWindowingAutomaticStageCreationEnabledExternal"
+ "flexibleWindowingManualStageCreationShouldRestorePreviousOpenWindows"
+ "flexibleWindowingPreviouslyEnabledAutomaticStageCreation"
+ "forDisplaysSimilarToDisplay:"
+ "generateRandom"
+ "getRequirementDataSizeForVersion"
+ "hasDateOverride"
+ "hasSidebarContents"
+ "integerForKey:"
+ "mainDisplayDarkeningPercentage"
+ "maximumAdaptiveTimeTextHeight"
+ "menuBarDemoMode"
+ "notificationVisibleIdleTimer"
+ "overrideDateWithAutoupdatingSeconds"
+ "platform_rng"
+ "posterHasComplications"
+ "proportionalAdaptiveTime"
+ "registerForTraitChanges:withAction:"
+ "registerForTraitChanges:withTarget:action:"
+ "requirement"
+ "result: %{public}@"
+ "sensitiveUIEpoch"
+ "setAdaptiveTimeTextHeight:"
+ "setAdaptsTimeTextHeight:"
+ "setAdditionalOffset:"
+ "setAnimatesTimeChanges:"
+ "setHasSidebarContents:"
+ "setIconUserInterfaceStyle:"
+ "setMaximumAdaptiveTimeTextHeight:"
+ "setOverrideDateWithAutoupdatingSeconds:"
+ "setPosterHasComplications:"
+ "setShowCompactTime:"
+ "setShowCompactTime:animated:"
+ "setShowsCompactTime:"
+ "setShowsCompactTime:animated:"
+ "setTimeSupportsStretch:"
+ "shouldInsertDownloadFileStackIconToFloatingDock"
+ "showCompactTime"
+ "timeChangeAnimationDuration"
+ "timeSupportsStretch"
+ "timeView"
+ "unregisterForTraitChanges:"
+ "wantsManyForegroundWindows"
+ "withDisplay:"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] created.\n"
- "ACMContextCreate"
- "CHAMOIS_97748869"
- "DeviceSupportsSingleDisplayEnhancedMultitasking"
- "MoreForegroundApps"
- "SBChamoisWindowingEverEnabled"
- "SBMoreForegroundApps"
- "SBShowNonDefaultSystemApps"
- "[%{public}@] %{public}@ %{public}@ highBandwidth: %{BOOL}u refreshRate: %.2g virtual: %{BOOL}u"
- "[%{public}@] %{public}@ CADisplay returned referencePixelSize of %{public}@ while the nativeSize is %{public}@"
- "[%{public}@] %{public}@ about to calculate available logicalScales. dumping display mode info:"
- "[%{public}@] %{public}@ currentMode: %{public}@ highBandwidth: %{BOOL}u refreshRate: %.2g virtual: %{BOOL}u"
- "[%{public}@] %{public}@ logicalScale bounds: {%.3f, %.3f}"
- "[%{public}@] %{public}@ logicalScale is out of the supported PPI range, so filtering out: %.2f; ppi: %.2f"
- "[%{public}@] %{public}@ nativeSize: %{public}@"
- "[%{public}@] %{public}@ not supported because we couldn't derive any usable resolutions"
- "[%{public}@] %{public}@ physicalSize: %{public}@"
- "[%{public}@] %{public}@ preferredMode: %{public}@ highBandwidth: %{BOOL}u refreshRate: %.2g virtual: %{BOOL}u"
- "[%{public}@] %{public}@ referenceSize (from preferred): %{public}@"
- "[%{public}@] %{public}@ scaling using: %{public}@; logicalScales before filtering on PPI: %{public}@"
- "[%{public}@] %{public}@ whoops -- we filtered out every logicalScale. stuff the best one back in: %.2f"
- "[%{public}@] result: %{public}@"
- "[SBValidateLogicalScale()] [rdar://102453240] [rdar://102453504] we're dropping logicalScale of %g because it's outside of logicalScaleLimits %{public}@; caDisplay: (%p) %{public}@"
- "[SBValidateLogicalScale()] [rdar://102453240] [rdar://102453504] we're dropping logicalScale of %g because scaledDisplaySize %{public}@ [%{public}@] is over our hard-coded display pipeline limit of %{public}@. logicalScaleLimits: %{public}@; caDisplay: (%p) %{public}@"
- "chamoisEverEnabled"
- "chamois_97748869"
- "deleted"
- "destroyed"
- "forDisplaysSimilarToDisplay:useNativeSize:"
- "initWithDisplay:useNativeSize:"
- "shouldShowNonDefaultSystemApplications"
- "withDisplay:useNativeSize:"

```
