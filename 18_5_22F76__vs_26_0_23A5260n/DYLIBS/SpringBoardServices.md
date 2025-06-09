## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-4503.5.9.0.0
-  __TEXT.__text: 0x70b54
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x7a20
-  __TEXT.__cstring: 0xc829
-  __TEXT.__const: 0x5a8
-  __TEXT.__oslogstring: 0x40c9
-  __TEXT.__gcc_except_tab: 0xbf0
+4552.106.0.0.0
+  __TEXT.__text: 0x73b28
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x7d40
+  __TEXT.__cstring: 0xcb87
+  __TEXT.__const: 0x5d8
+  __TEXT.__oslogstring: 0x4286
+  __TEXT.__gcc_except_tab: 0xd04
   __TEXT.__dlopen_cstrs: 0x116
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x2548
-  __TEXT.__objc_classname: 0x28bc
-  __TEXT.__objc_methname: 0xf4bb
-  __TEXT.__objc_methtype: 0x2ada
-  __TEXT.__objc_stubs: 0x82a0
-  __DATA_CONST.__got: 0x818
-  __DATA_CONST.__const: 0x3280
-  __DATA_CONST.__objc_classlist: 0x638
+  __TEXT.__unwind_info: 0x2618
+  __TEXT.__objc_classname: 0x296a
+  __TEXT.__objc_methname: 0xf9d5
+  __TEXT.__objc_methtype: 0x2b7e
+  __TEXT.__objc_stubs: 0x8580
+  __DATA_CONST.__got: 0x838
+  __DATA_CONST.__const: 0x3320
+  __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e88
+  __DATA_CONST.__objc_selrefs: 0x2f88
   __DATA_CONST.__objc_protorefs: 0x1a8
-  __DATA_CONST.__objc_superrefs: 0x408
-  __AUTH_CONST.__auth_got: 0x7e0
-  __AUTH_CONST.__const: 0x2790
-  __AUTH_CONST.__cfstring: 0x9920
-  __AUTH_CONST.__objc_const: 0x221b0
-  __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x2990
-  __DATA.__objc_ivar: 0x778
+  __DATA_CONST.__objc_superrefs: 0x420
+  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__const: 0x27d0
+  __AUTH_CONST.__cfstring: 0x9be0
+  __AUTH_CONST.__objc_const: 0x22a08
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH.__objc_data: 0x2e90
+  __DATA.__objc_ivar: 0x7ac
   __DATA.__data: 0x1fc0
-  __DATA.__bss: 0x820
-  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA.__bss: 0x840
+  __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x258
+  __DATA_DIRTY.__bss: 0x250
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5AF3930-ED10-32DB-93ED-B03833FAFBDC
-  Functions: 3816
-  Symbols:   13040
-  CStrings:  5944
+  UUID: 0B837395-141E-38A9-8375-A42E2C2DAC26
+  Functions: 3905
+  Symbols:   13333
+  CStrings:  6061
 
Symbols:
+ +[FBSDisplayLayoutMonitorConfiguration(SBSExternalDisplayLayout) configurationForExternalDisplay:]
+ +[SBSAdaptiveTimeLayoutContext supportsSecureCoding]
+ +[SBSHomeScreenIconStyleConfiguration isSolariumAppIconsEnabled]
+ +[SBSPhysicalButtonTargetMonitorServiceSpecification identifier]
+ +[SBSPhysicalButtonTargetMonitorServiceSpecification interface]
+ +[SBSPhysicalButtonTargetMonitorServiceSpecification serviceQuality]
+ -[FBSDisplayLayoutElement(SBSDisplayLayoutElement) zOrderIndex]
+ -[SBSAdaptiveTimeLayoutContext copyWithZone:]
+ -[SBSAdaptiveTimeLayoutContext encodeWithBSXPCCoder:]
+ -[SBSAdaptiveTimeLayoutContext encodeWithCoder:]
+ -[SBSAdaptiveTimeLayoutContext encodeWithXPCDictionary:]
+ -[SBSAdaptiveTimeLayoutContext hasSidebarContents]
+ -[SBSAdaptiveTimeLayoutContext initWithBSXPCCoder:]
+ -[SBSAdaptiveTimeLayoutContext initWithCoder:]
+ -[SBSAdaptiveTimeLayoutContext initWithXPCDictionary:]
+ -[SBSAdaptiveTimeLayoutContext isEqual:]
+ -[SBSAdaptiveTimeLayoutContext orientation]
+ -[SBSAdaptiveTimeLayoutContext setHasSidebarContents:]
+ -[SBSAdaptiveTimeLayoutContext setOrientation:]
+ -[SBSAdaptiveTimeLayoutContext supportsBSXPCSecureCoding]
+ -[SBSBuddyMultitaskingFlow _isLowCapacityDevice]
+ -[SBSBuddyMultitaskingFlow currentMultitaskingOption]
+ -[SBSBuddyMultitaskingFlow needsToShow]
+ -[SBSBuddyMultitaskingFlow setCurrentMultitaskingOption:]
+ -[SBSDisplayLayoutElement setZOrderIndex:]
+ -[SBSDisplayLayoutElement setZOrderIndex:].cold.1
+ -[SBSDisplayLayoutElement zOrderIndex]
+ -[SBSHomeScreenIconStyleConfiguration iconServicesAppearanceUsingDarkInterfaceStyle:]
+ -[SBSHomeScreenIconStyleConfiguration iconServicesAppearanceVariantUsingDarkInterfaceStyle:]
+ -[SBSHomeScreenIconStyleConfiguration initWithConfigurationType:variant:tintColor:]
+ -[SBSHomeScreenIconStyleConfiguration updatedConfigurationType]
+ -[SBSHomeScreenIconStyleConfiguration variant]
+ -[SBSHomeScreenService addApplicationIconToHomeScreenWithBundleIdentifier:inPage:atPositionDescription:]
+ -[SBSHomeScreenService addApplicationIconToHomeScreenWithBundleIdentifier:inPage:atPositionDescription:].cold.1
+ -[SBSHomeScreenService addFileStackWithURL:]
+ -[SBSHomeScreenService addFileStackWithURL:].cold.1
+ -[SBSHomeScreenService addFileStackWithURL:].cold.2
+ -[SBSHomeScreenService addPageOfApplicationIconsWithBundleIdentifier:]
+ -[SBSHomeScreenService addPageOfApplicationIconsWithBundleIdentifier:].cold.1
+ -[SBSHomeScreenService changeDisplayedDateWithAutoupdatingSecondsOverride:]
+ -[SBSHomeScreenService changeDisplayedDateWithAutoupdatingSecondsOverride:].cold.1
+ -[SBSHomeScreenService precacheIconLayersOnFirstPageWithAppearanceDescriptions:]
+ -[SBSHomeScreenService precacheIconLayersOnFirstPageWithAppearanceDescriptions:].cold.1
+ -[SBSHomeScreenService removeFileStackWithURL:]
+ -[SBSHomeScreenService removeFileStackWithURL:].cold.1
+ -[SBSHomeScreenService removeFileStackWithURL:].cold.2
+ -[SBSHomeScreenService setHomeScreenIconStyleConfiguration:wallpaperDimmed:]
+ -[SBSHomeScreenService setHomeScreenIconStyleConfiguration:wallpaperDimmed:].cold.1
+ -[SBSPhysicalButtonTargetMonitor .cxx_destruct]
+ -[SBSPhysicalButtonTargetMonitor _addObserver:]
+ -[SBSPhysicalButtonTargetMonitor _notifyObserversOfPresenceOfPhysicalButtonTargets:]
+ -[SBSPhysicalButtonTargetMonitor _removeObserver:]
+ -[SBSPhysicalButtonTargetMonitor dealloc]
+ -[SBSPhysicalButtonTargetMonitor dealloc].cold.1
+ -[SBSPhysicalButtonTargetMonitor init]
+ -[SBSPhysicalButtonTargetMonitor startObservingPresenceOfPhysicalButtonTargets:]
+ -[SBSPhysicalButtonTargetMonitorClient .cxx_destruct]
+ -[SBSPhysicalButtonTargetMonitorClient init]
+ -[SBSPhysicalButtonTargetMonitorClient invalidate]
+ -[SBSPhysicalButtonTargetMonitorClient setPhysicalButtonTargets:]
+ -[SBSPhysicalButtonTargetMonitorClient startObservingPresenceOfPhysicalButtonTargets:]
+ -[SBSPhysicalButtonTargetMonitorClient startObservingPresenceOfPhysicalButtonTargets:].cold.1
+ -[SBSPhysicalButtonTargetMonitorClient startObservingPresenceOfPhysicalButtonTargets:].cold.2
+ -[SBSPhysicalButtonTargetMonitorServer .cxx_destruct]
+ -[SBSPhysicalButtonTargetMonitorServer connections]
+ -[SBSPhysicalButtonTargetMonitorServer dealloc]
+ -[SBSPhysicalButtonTargetMonitorServer init]
+ -[SBSPhysicalButtonTargetMonitorServer listener:didReceiveConnection:withContext:]
+ -[SBSPhysicalButtonTargetMonitorServer physicalButtonTargets]
+ -[SBSPhysicalButtonTargetMonitorServer setPhysicalButtonTargets:]
+ -[SBSPhysicalButtonTargetMonitorServer startServer]
+ -[SBSSystemServiceClient availableRecordableFlipBookElementIdentifiers]
+ -[SBSSystemServiceClient initiateSecureFlipBookRecordingsForElement:withCompletion:]
+ -[SBSTestAutomationService availableRecordableFlipBookElementIdentifiers]
+ -[SBSTestAutomationService initiateSecureFlipBookRecordingsForElement:withCompletion:]
+ -[SBSWallpaperClient fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:]
+ -[SBSWallpaperClient fetchAdaptiveTimeHeightLimitsForContext:completionHandler:]
+ -[SBSWallpaperClient fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]
+ -[SBSWallpaperService fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:]
+ -[SBSWallpaperService fetchAdaptiveTimeHeightLimitsForContext:completionHandler:]
+ -[SBSWallpaperService fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]
+ -[_SBSPhysicalButtonTargetMonitorObserver .cxx_destruct]
+ -[_SBSPhysicalButtonTargetMonitorObserver observationHandler]
+ -[_SBSPhysicalButtonTargetMonitorObserver setObservationHandler:]
+ GCC_except_table145
+ GCC_except_table25
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table49
+ GCC_except_table52
+ _BSDeserializeCGFloatFromXPCDictionaryWithKey
+ _BSSerializeCGFloatToXPCDictionaryWithKey
+ _MGGetSInt64Answer
+ _OBJC_CLASS_$_BSPlatform
+ _OBJC_CLASS_$_BSXPCCoder
+ _OBJC_CLASS_$_SBSAdaptiveTimeLayoutContext
+ _OBJC_CLASS_$_SBSBuddyMultitaskingFlow
+ _OBJC_CLASS_$_SBSPhysicalButtonTargetMonitor
+ _OBJC_CLASS_$_SBSPhysicalButtonTargetMonitorClient
+ _OBJC_CLASS_$_SBSPhysicalButtonTargetMonitorServer
+ _OBJC_CLASS_$_SBSPhysicalButtonTargetMonitorServiceSpecification
+ _OBJC_CLASS_$__SBSPhysicalButtonTargetMonitorObserver
+ _OBJC_IVAR_$_SBSAdaptiveTimeLayoutContext._hasSidebarContents
+ _OBJC_IVAR_$_SBSAdaptiveTimeLayoutContext._orientation
+ _OBJC_IVAR_$_SBSHomeScreenIconStyleConfiguration._variant
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitor._lock
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitor._lock_client
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitor._lock_observers
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitor._lock_targets
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorClient._lock
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorClient._lock_connection
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorClient._lock_observationBlock
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorServer._connectionListener
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorServer._lock
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorServer._lock_connections
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorServer._lock_physicalButtonTargets
+ _OBJC_IVAR_$_SBSPhysicalButtonTargetMonitorServer._windowSceneManager
+ _OBJC_IVAR_$__SBSPhysicalButtonTargetMonitorObserver._observationHandler
+ _OBJC_METACLASS_$_BSSimpleAssertion
+ _OBJC_METACLASS_$_SBSAdaptiveTimeLayoutContext
+ _OBJC_METACLASS_$_SBSBuddyMultitaskingFlow
+ _OBJC_METACLASS_$_SBSPhysicalButtonTargetMonitor
+ _OBJC_METACLASS_$_SBSPhysicalButtonTargetMonitorClient
+ _OBJC_METACLASS_$_SBSPhysicalButtonTargetMonitorServer
+ _OBJC_METACLASS_$_SBSPhysicalButtonTargetMonitorServiceSpecification
+ _OBJC_METACLASS_$__SBSPhysicalButtonTargetMonitorObserver
+ _SBLogDeviceMotionEffect
+ _SBLogDeviceMotionEffect.__logObj
+ _SBLogDeviceMotionEffect.cold.1
+ _SBLogDeviceMotionEffect.onceToken
+ _SBLogDockFileStack
+ _SBLogDockFileStack.__logObj
+ _SBLogDockFileStack.cold.1
+ _SBLogDockFileStack.onceToken
+ _SBLogDynamicLighting
+ _SBLogDynamicLighting.__logObj
+ _SBLogDynamicLighting.cold.1
+ _SBLogDynamicLighting.onceToken
+ _SBLogLayoutAttributes
+ _SBLogLayoutAttributes.__logObj
+ _SBLogLayoutAttributes.cold.1
+ _SBLogLayoutAttributes.onceToken
+ _SBLogPhoneUnlockWithVision
+ _SBLogPhoneUnlockWithVision.__logObj
+ _SBLogPhoneUnlockWithVision.cold.1
+ _SBLogPhoneUnlockWithVision.onceToken
+ _SBSDetailedBatteryUIDismissDuration
+ _SBSOpenApplicationOptionKeyWindowingArrangement
+ _SBSPhysicalButtonTargetMonitorEntitlement
+ _SBSStringForHomeScreenIconStyleConfigurationType
+ _SBSStringForHomeScreenIconStyleConfigurationVariant
+ __OBJC_$_CATEGORY_FBSDisplayLayoutMonitorConfiguration_$_SBSExternalDisplayLayout
+ __OBJC_$_CLASS_METHODS_FBSDisplayLayoutMonitorConfiguration(SBSExternalDisplayLayout|SBSContinuityDisplayLayout)
+ __OBJC_$_CLASS_METHODS_SBSAdaptiveTimeLayoutContext
+ __OBJC_$_CLASS_METHODS_SBSPhysicalButtonTargetMonitorServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_SBSAdaptiveTimeLayoutContext
+ __OBJC_$_CLASS_PROP_LIST_SBSPhysicalButtonTargetMonitorServiceSpecification
+ __OBJC_$_INSTANCE_METHODS_SBSAdaptiveTimeLayoutContext
+ __OBJC_$_INSTANCE_METHODS_SBSBuddyMultitaskingFlow
+ __OBJC_$_INSTANCE_METHODS_SBSPhysicalButtonTargetMonitor
+ __OBJC_$_INSTANCE_METHODS_SBSPhysicalButtonTargetMonitorClient
+ __OBJC_$_INSTANCE_METHODS_SBSPhysicalButtonTargetMonitorServer
+ __OBJC_$_INSTANCE_METHODS__SBSPhysicalButtonTargetMonitorObserver
+ __OBJC_$_INSTANCE_VARIABLES_SBSAdaptiveTimeLayoutContext
+ __OBJC_$_INSTANCE_VARIABLES_SBSPhysicalButtonTargetMonitor
+ __OBJC_$_INSTANCE_VARIABLES_SBSPhysicalButtonTargetMonitorClient
+ __OBJC_$_INSTANCE_VARIABLES_SBSPhysicalButtonTargetMonitorServer
+ __OBJC_$_INSTANCE_VARIABLES__SBSPhysicalButtonTargetMonitorObserver
+ __OBJC_$_PROP_LIST_SBSAdaptiveTimeLayoutContext
+ __OBJC_$_PROP_LIST_SBSBuddyMultitaskingFlow
+ __OBJC_$_PROP_LIST_SBSDisplayLayoutElement.185
+ __OBJC_$_PROP_LIST_SBSPhysicalButtonTargetMonitorClient
+ __OBJC_$_PROP_LIST_SBSPhysicalButtonTargetMonitorServer
+ __OBJC_$_PROP_LIST__SBSPhysicalButtonTargetMonitorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSPhysicalButtonTargetMonitorServiceClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSPhysicalButtonTargetMonitorServiceClient
+ __OBJC_$_PROTOCOL_REFS_SBSPhysicalButtonTargetMonitorServiceClient
+ __OBJC_$_PROTOCOL_REFS_SBSPhysicalButtonTargetMonitorServiceServer
+ __OBJC_CLASS_PROTOCOLS_$_SBSAdaptiveTimeLayoutContext
+ __OBJC_CLASS_PROTOCOLS_$_SBSPhysicalButtonTargetMonitorClient
+ __OBJC_CLASS_PROTOCOLS_$_SBSPhysicalButtonTargetMonitorServer
+ __OBJC_CLASS_RO_$_SBSAdaptiveTimeLayoutContext
+ __OBJC_CLASS_RO_$_SBSBuddyMultitaskingFlow
+ __OBJC_CLASS_RO_$_SBSPhysicalButtonTargetMonitor
+ __OBJC_CLASS_RO_$_SBSPhysicalButtonTargetMonitorClient
+ __OBJC_CLASS_RO_$_SBSPhysicalButtonTargetMonitorServer
+ __OBJC_CLASS_RO_$_SBSPhysicalButtonTargetMonitorServiceSpecification
+ __OBJC_CLASS_RO_$__SBSPhysicalButtonTargetMonitorObserver
+ __OBJC_LABEL_PROTOCOL_$_SBSPhysicalButtonTargetMonitorServiceClient
+ __OBJC_LABEL_PROTOCOL_$_SBSPhysicalButtonTargetMonitorServiceServer
+ __OBJC_METACLASS_RO_$_SBSAdaptiveTimeLayoutContext
+ __OBJC_METACLASS_RO_$_SBSBuddyMultitaskingFlow
+ __OBJC_METACLASS_RO_$_SBSPhysicalButtonTargetMonitor
+ __OBJC_METACLASS_RO_$_SBSPhysicalButtonTargetMonitorClient
+ __OBJC_METACLASS_RO_$_SBSPhysicalButtonTargetMonitorServer
+ __OBJC_METACLASS_RO_$_SBSPhysicalButtonTargetMonitorServiceSpecification
+ __OBJC_METACLASS_RO_$__SBSPhysicalButtonTargetMonitorObserver
+ __OBJC_PROTOCOL_$_SBSPhysicalButtonTargetMonitorServiceClient
+ __OBJC_PROTOCOL_$_SBSPhysicalButtonTargetMonitorServiceServer
+ __OBJC_PROTOCOL_REFERENCE_$_SBSPhysicalButtonTargetMonitorServiceClient
+ __OBJC_PROTOCOL_REFERENCE_$_SBSPhysicalButtonTargetMonitorServiceServer
+ ___47-[SBSPhysicalButtonTargetMonitor _addObserver:]_block_invoke
+ ___51-[SBSPhysicalButtonTargetMonitorServer startServer]_block_invoke
+ ___61-[_SBSPhysicalButtonTargetMonitorObserver observationHandler]_block_invoke
+ ___62-[SBSBackgroundActivityAssertionManager _reactivateAssertions]_block_invoke.137
+ ___62-[SBSBackgroundActivityAssertionManager unregisterCoordinator]_block_invoke.133
+ ___63+[SBSPhysicalButtonTargetMonitorServiceSpecification interface]_block_invoke
+ ___71-[SBSSystemServiceClient availableRecordableFlipBookElementIdentifiers]_block_invoke
+ ___74-[SBSBackgroundActivityAssertionManager statusBarTappedWithContext:reply:]_block_invoke.120
+ ___80+[SBSInCallPresentationRequest performPresentationWithConfiguration:completion:]_block_invoke.6.cold.1
+ ___80-[SBSPhysicalButtonTargetMonitor startObservingPresenceOfPhysicalButtonTargets:]_block_invoke
+ ___80-[SBSWallpaperClient fetchAdaptiveTimeHeightLimitsForContext:completionHandler:]_block_invoke
+ ___80-[SBSWallpaperClient fetchAdaptiveTimeHeightLimitsForContext:completionHandler:]_block_invoke_2
+ ___81-[SBSWallpaperService fetchAdaptiveTimeHeightLimitsForContext:completionHandler:]_block_invoke
+ ___81-[SBSWallpaperService fetchAdaptiveTimeHeightLimitsForContext:completionHandler:]_block_invoke_2
+ ___82-[SBSPhysicalButtonTargetMonitorServer listener:didReceiveConnection:withContext:]_block_invoke
+ ___82-[SBSPhysicalButtonTargetMonitorServer listener:didReceiveConnection:withContext:]_block_invoke.11
+ ___82-[SBSPhysicalButtonTargetMonitorServer listener:didReceiveConnection:withContext:]_block_invoke.12
+ ___82-[SBSPhysicalButtonTargetMonitorServer listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___84-[SBSSystemServiceClient initiateSecureFlipBookRecordingsForElement:withCompletion:]_block_invoke
+ ___84-[SBSSystemServiceClient initiateSecureFlipBookRecordingsForElement:withCompletion:]_block_invoke_2
+ ___85-[SBSWallpaperClient fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:]_block_invoke
+ ___85-[SBSWallpaperClient fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:]_block_invoke_2
+ ___86-[SBSPhysicalButtonTargetMonitorClient startObservingPresenceOfPhysicalButtonTargets:]_block_invoke
+ ___86-[SBSPhysicalButtonTargetMonitorClient startObservingPresenceOfPhysicalButtonTargets:]_block_invoke.100
+ ___86-[SBSPhysicalButtonTargetMonitorClient startObservingPresenceOfPhysicalButtonTargets:]_block_invoke_2
+ ___86-[SBSWallpaperService fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:]_block_invoke
+ ___86-[SBSWallpaperService fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:]_block_invoke_2
+ ___92-[SBSBackgroundActivityAssertionManager addBackgroundActivityAssertion:withHandler:onQueue:]_block_invoke.103
+ ___92-[SBSBackgroundActivityAssertionManager addBackgroundActivityAssertion:withHandler:onQueue:]_block_invoke.104
+ ___96-[SBSBackgroundActivityAssertionManager _registerBackgroundActivityCoordinatorAfterInterruption]_block_invoke.129
+ ___96-[SBSBackgroundActivityAssertionManager _registerBackgroundActivityCoordinatorAfterInterruption]_block_invoke_2.130
+ ___98-[SBSWallpaperService fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke
+ ___98-[SBSWallpaperService fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke_2
+ ___SBLogDeviceMotionEffect_block_invoke
+ ___SBLogDockFileStack_block_invoke
+ ___SBLogDynamicLighting_block_invoke
+ ___SBLogLayoutAttributes_block_invoke
+ ___SBLogPhoneUnlockWithVision_block_invoke
+ ___block_descriptor_32_e8_v16?0Q8l
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e11_v24?0d8d16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs_e5_v8?0ls32l8
+ ___block_literal_global.207
+ ___block_literal_global.210
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.219
+ ___block_literal_global.248
+ ___block_literal_global.251
+ ___block_literal_global.254
+ ___block_literal_global.257
+ ___block_literal_global.260
+ _kSBSTestAutomationServiceMessageKeyGetAvailableRecordableFlipBookElementIdentifiers
+ _kSBSTestAutomationServiceMessageKeySecureFlipBookElement
+ _kSBSTestAutomationServiceMessageKeySecureFlipBookErrorDescription
+ _kSBSTestAutomationServiceMessageKeySecureFlipBookRecordingDestinationURL
+ _kSBSWallpaperServiceClientMessageKeyAdaptiveTimeHeight
+ _kSBSWallpaperServiceClientMessageKeyAdaptiveTimeMaximumHeight
+ _kSBSWallpaperServiceClientMessageKeyAdaptiveTimeMinimumHeight
+ _kSBSWallpaperServiceClientMessageKeyLayoutContext
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_addObserver:
+ _objc_msgSend$_isLowCapacityDevice
+ _objc_msgSend$_notifyObserversOfPresenceOfPhysicalButtonTargets:
+ _objc_msgSend$_removeObserver:
+ _objc_msgSend$addApplicationIconToHomeScreenWithBundleIdentifier:inPage:atPositionDescription:
+ _objc_msgSend$addFileStackWithURL:
+ _objc_msgSend$addPageOfApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$availableRecordableFlipBookElementIdentifiers
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$changeDisplayedDateWithAutoupdatingSecondsOverride:
+ _objc_msgSend$coderWithMessage:
+ _objc_msgSend$currentMultitaskingOption
+ _objc_msgSend$deviceClass
+ _objc_msgSend$encodeWithBSXPCCoder:
+ _objc_msgSend$fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:
+ _objc_msgSend$fetchAdaptiveTimeHeightLimitsForContext:completionHandler:
+ _objc_msgSend$fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:
+ _objc_msgSend$initWithBSXPCCoder:
+ _objc_msgSend$initWithConfigurationType:variant:tintColor:
+ _objc_msgSend$initiateSecureFlipBookRecordingsForElement:withCompletion:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$isSolariumAppIconsEnabled
+ _objc_msgSend$observationHandler
+ _objc_msgSend$precacheIconLayersOnFirstPageWithAppearanceDescriptions:
+ _objc_msgSend$removeFileStackWithURL:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setHomeScreenIconStyleConfiguration:wallpaperDimmed:
+ _objc_msgSend$setObservationHandler:
+ _objc_msgSend$setPhysicalButtonTargets:
+ _objc_msgSend$startObservingPresenceOfPhysicalButtonTargets:
+ _objc_msgSend$startServer
+ _objc_msgSend$updatedConfigurationType
+ _objc_msgSend$variant
+ _objc_msgSend$zOrderIndex
- +[SBSAccessibilityWindowHostingSpecification identifier]
- +[SBSAccessibilityWindowHostingSpecification interface]
- +[SBSAccessibilityWindowHostingSpecification interface].cold.1
- +[SBSAccessibilityWindowHostingSpecification serviceQuality]
- +[SBSHomeScreenIconStyleConfiguration automaticStyleConfiguration].cold.1
- +[SBSHomeScreenIconStyleConfiguration darkStyleConfiguration].cold.1
- +[SBSHomeScreenIconStyleConfiguration lightStyleConfiguration].cold.1
- -[SBSAccessibilityWindowHostingController .cxx_destruct]
- -[SBSAccessibilityWindowHostingController _connectionQueue_connection]
- -[SBSAccessibilityWindowHostingController _connectionQueue_handleInterruption]
- -[SBSAccessibilityWindowHostingController init]
- -[SBSAccessibilityWindowHostingController invalidate]
- -[SBSAccessibilityWindowHostingController registerWindowWithContextID:atLevel:]
- -[SBSAccessibilityWindowHostingController unregisterWindowWithContextID:]
- -[SBSHomeScreenIconStyleConfiguration initWithConfigurationType:]
- -[SBSHomeScreenIconStyleConfiguration initWithConfigurationType:tintColor:]
- -[SBSHomeScreenService addIconTintColorObserver:]
- -[SBSHomeScreenService iconUserInterfaceStyle]
- -[SBSHomeScreenService reloadIcons]
- -[SBSHomeScreenService reloadIcons].cold.1
- -[SBSHomeScreenService setIconUserInterfaceStyle:]
- GCC_except_table29
- GCC_except_table32
- GCC_except_table35
- GCC_except_table45
- _OBJC_CLASS_$_SBSAccessibilityWindowHostingController
- _OBJC_CLASS_$_SBSAccessibilityWindowHostingSpecification
- _OBJC_IVAR_$_SBSAccessibilityWindowHostingController._connection
- _OBJC_IVAR_$_SBSAccessibilityWindowHostingController._connectionQueue
- _OBJC_IVAR_$_SBSAccessibilityWindowHostingController._registeredWindowContextIDsToLevel
- _OBJC_METACLASS_$_SBSAccessibilityWindowHostingController
- _OBJC_METACLASS_$_SBSAccessibilityWindowHostingSpecification
- __OBJC_$_CATEGORY_CLASS_METHODS_FBSDisplayLayoutMonitorConfiguration_$_SBSContinuityDisplayLayout
- __OBJC_$_CATEGORY_FBSDisplayLayoutMonitorConfiguration_$_SBSContinuityDisplayLayout
- __OBJC_$_CLASS_METHODS_SBSAccessibilityWindowHostingSpecification
- __OBJC_$_CLASS_PROP_LIST_SBSAccessibilityWindowHostingSpecification
- __OBJC_$_INSTANCE_METHODS_SBSAccessibilityWindowHostingController
- __OBJC_$_INSTANCE_VARIABLES_SBSAccessibilityWindowHostingController
- __OBJC_$_PROP_LIST_SBSAccessibilityWindowHostingController
- __OBJC_$_PROP_LIST_SBSDisplayLayoutElement.167
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSAccessibilityWindowHostingClientToServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBSAccessibilityWindowHostingClientToServerInterface
- __OBJC_$_PROTOCOL_REFS_SBSAccessibilityWindowHostingClientToServerInterface
- __OBJC_$_PROTOCOL_REFS_SBSAccessibilityWindowHostingServerToClientInterface
- __OBJC_CLASS_PROTOCOLS_$_SBSAccessibilityWindowHostingController
- __OBJC_CLASS_RO_$_SBSAccessibilityWindowHostingController
- __OBJC_CLASS_RO_$_SBSAccessibilityWindowHostingSpecification
- __OBJC_LABEL_PROTOCOL_$_SBSAccessibilityWindowHostingClientToServerInterface
- __OBJC_LABEL_PROTOCOL_$_SBSAccessibilityWindowHostingServerToClientInterface
- __OBJC_METACLASS_RO_$_SBSAccessibilityWindowHostingController
- __OBJC_METACLASS_RO_$_SBSAccessibilityWindowHostingSpecification
- __OBJC_PROTOCOL_$_SBSAccessibilityWindowHostingClientToServerInterface
- __OBJC_PROTOCOL_$_SBSAccessibilityWindowHostingServerToClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_SBSAccessibilityWindowHostingClientToServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_SBSAccessibilityWindowHostingServerToClientInterface
- ___53-[SBSAccessibilityWindowHostingController invalidate]_block_invoke
- ___55+[SBSAccessibilityWindowHostingSpecification interface]_block_invoke
- ___61+[SBSHomeScreenIconStyleConfiguration darkStyleConfiguration]_block_invoke
- ___62+[SBSHomeScreenIconStyleConfiguration lightStyleConfiguration]_block_invoke
- ___62-[SBSBackgroundActivityAssertionManager _reactivateAssertions]_block_invoke.136
- ___62-[SBSBackgroundActivityAssertionManager unregisterCoordinator]_block_invoke.132
- ___66+[SBSHomeScreenIconStyleConfiguration automaticStyleConfiguration]_block_invoke
- ___70-[SBSAccessibilityWindowHostingController _connectionQueue_connection]_block_invoke
- ___70-[SBSAccessibilityWindowHostingController _connectionQueue_connection]_block_invoke.7
- ___70-[SBSAccessibilityWindowHostingController _connectionQueue_connection]_block_invoke.8
- ___70-[SBSAccessibilityWindowHostingController _connectionQueue_connection]_block_invoke_2
- ___73-[SBSAccessibilityWindowHostingController unregisterWindowWithContextID:]_block_invoke
- ___74-[SBSBackgroundActivityAssertionManager statusBarTappedWithContext:reply:]_block_invoke.118
- ___78-[SBSAccessibilityWindowHostingController _connectionQueue_handleInterruption]_block_invoke
- ___79-[SBSAccessibilityWindowHostingController registerWindowWithContextID:atLevel:]_block_invoke
- ___92-[SBSBackgroundActivityAssertionManager addBackgroundActivityAssertion:withHandler:onQueue:]_block_invoke.101
- ___92-[SBSBackgroundActivityAssertionManager addBackgroundActivityAssertion:withHandler:onQueue:]_block_invoke.102
- ___96-[SBSBackgroundActivityAssertionManager _registerBackgroundActivityCoordinatorAfterInterruption]_block_invoke.128
- ___96-[SBSBackgroundActivityAssertionManager _registerBackgroundActivityCoordinatorAfterInterruption]_block_invoke_2.129
- ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_52_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.131
- ___block_literal_global.134
- ___block_literal_global.2
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.218
- ___block_literal_global.4
- ___stderrp
- __block_invoke.deviceSubtype
- _automaticStyleConfiguration.automaticStyleConfiguration
- _automaticStyleConfiguration.onceToken
- _darkStyleConfiguration.darkStyleConfiguration
- _darkStyleConfiguration.onceToken
- _fprintf
- _lightStyleConfiguration.lightStyleConfiguration
- _lightStyleConfiguration.onceToken
- _objc_msgSend$_connectionQueue_connection
- _objc_msgSend$_connectionQueue_handleInterruption
- _objc_msgSend$automaticStyleConfiguration
- _objc_msgSend$configurationType
- _objc_msgSend$darkStyleConfiguration
- _objc_msgSend$initWithConfigurationType:
- _objc_msgSend$initWithConfigurationType:tintColor:
- _objc_msgSend$lightStyleConfiguration
- _objc_msgSend$registerWindowWithContextID:atLevel:
- _objc_msgSend$reloadIcons
- _objc_msgSend$tintedStyleConfigurationWithTintColor:
- _objc_msgSend$unregisterWindowWithContextID:
CStrings:
+ "@\"SBSPhysicalButtonTargetMonitorClient\""
+ "@\"SBWindowSceneManager\""
+ "@40@0:8q16q24@32"
+ "Deallocated SBSPhysicalButtonTargetMonitor while observers were still attached."
+ "DeviceMemorySize"
+ "DeviceMotionEffect"
+ "DockFileStack"
+ "DynamicLighting"
+ "FlexibleWindowing"
+ "InitiateSecureFlipBookRecordingError"
+ "LayoutAttributes"
+ "PhoneUnlockWithVision"
+ "SBChamoisWindowingEnabled"
+ "SBMedusaMultitaskingEnabled"
+ "SBSAdaptiveTimeLayoutContext"
+ "SBSBuddyMultitaskingFlow"
+ "SBSDisplayLayoutElement.m"
+ "SBSExternalDisplayLayout"
+ "SBSHomeScreenService: failed %{public}@ request (no url specified)."
+ "SBSHomeScreenService: failed changeDisplayedDateWithAutoupdatingSecondsOverride request (no target)."
+ "SBSHomeScreenService: failed precacheIconLayersOnFirstPageWithAppearanceDescriptions request (no target)."
+ "SBSHomeScreenService: failed setHomeScreenIconStyleConfiguration:wallpaperDimmed: request (no target)."
+ "SBSPhysicalButtonTargetMonitor"
+ "SBSPhysicalButtonTargetMonitor.m"
+ "SBSPhysicalButtonTargetMonitorClient"
+ "SBSPhysicalButtonTargetMonitorServer"
+ "SBSPhysicalButtonTargetMonitorService interrupted connection %@"
+ "SBSPhysicalButtonTargetMonitorService invalidated connection %@"
+ "SBSPhysicalButtonTargetMonitorService.m"
+ "SBSPhysicalButtonTargetMonitorServiceClient"
+ "SBSPhysicalButtonTargetMonitorServiceServer"
+ "SBSPhysicalButtonTargetMonitorServiceSpecification"
+ "SBSSecureAppTypeContinuitySing"
+ "SBSSecureAppTypeTranslate"
+ "Solarium"
+ "Started observation for a client that was already observing!"
+ "Successfully unregistered from all overrides"
+ "SwiftUI"
+ "T@?,C,N,V_observationHandler"
+ "TB,N,V_hasSidebarContents"
+ "TQ,N,V_lock_physicalButtonTargets"
+ "Tq,N,V_orientation"
+ "Tq,R,N,V_variant"
+ "URLWithString:"
+ "_SBSPhysicalButtonTargetMonitorObserver"
+ "__Arrangement"
+ "_addObserver:"
+ "_hasSidebarContents"
+ "_isLowCapacityDevice"
+ "_lock_client"
+ "_lock_observationBlock"
+ "_lock_physicalButtonTargets"
+ "_lock_targets"
+ "_notifyObserversOfPresenceOfPhysicalButtonTargets:"
+ "_observationHandler"
+ "_orientation"
+ "_removeObserver:"
+ "_variant"
+ "_windowSceneManager"
+ "adaptiveTimeHeight"
+ "adaptiveTimeMaximumHeight"
+ "adaptiveTimeMinimumHeight"
+ "addApplicationIconToHomeScreenWithBundleIdentifier:inPage:atPositionDescription:"
+ "addFileStackWithURL:"
+ "addPageOfApplicationIconsWithBundleIdentifier:"
+ "availableRecordableFlipBookElementIdentifiers"
+ "availableRecordableSecureFlipBookElementIdentifiers"
+ "beyondQuaternary"
+ "boolForKey:"
+ "changeDisplayedDateWithAutoupdatingSecondsOverride:"
+ "clear"
+ "coderWithMessage:"
+ "com.apple.ContinuitySingShieldUI"
+ "com.apple.Translate"
+ "com.apple.springboard.physical-button-target-monitor-service"
+ "com.apple.springboard.private.physicalButtonTargetMonitor"
+ "configurationForExternalDisplay:"
+ "configurationVariant"
+ "currentMultitaskingOption"
+ "deviceClass"
+ "fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:"
+ "fetchAdaptiveTimeHeightLimitsForContext:completionHandler:"
+ "fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:"
+ "hasSidebarContents"
+ "iconServicesAppearanceUsingDarkInterfaceStyle:"
+ "iconServicesAppearanceVariantUsingDarkInterfaceStyle:"
+ "initWithConfigurationType:variant:tintColor:"
+ "initiateSecureFlipBookRecordingsForElement:withCompletion:"
+ "isSolariumAppIconsEnabled"
+ "layoutContext"
+ "needsToShow"
+ "observationBlock != ((void *)0)"
+ "observationHandler"
+ "physicalButtonTargets"
+ "precacheIconLayersOnFirstPageWithAppearanceDescriptions:"
+ "q20@0:8B16"
+ "removeFileStackWithURL:"
+ "secureFlipBookElement"
+ "secureFlipBookErrorDescription"
+ "secureFlipBookRecordingDestinationURL"
+ "setBool:forKey:"
+ "setCurrentMultitaskingOption:"
+ "setHasSidebarContents:"
+ "setHomeScreenIconStyleConfiguration:wallpaperDimmed:"
+ "setObservationHandler:"
+ "setOrientation:"
+ "setPhysicalButtonTargets:"
+ "setZOrderIndex:"
+ "startObservingPresenceOfPhysicalButtonTargets:"
+ "updatedConfigurationType"
+ "v16@?0Q8"
+ "v24@0:8@\"NSURL\"16"
+ "v24@?0d8d16"
+ "v32@0:8@\"SBSHomeScreenIconStyleConfiguration\"16@\"NSNumber\"24"
+ "v40@0:8@16d24@?32"
+ "zOrderIndex"
+ "zOrderIndex >= 0"
- "ArtworkDeviceSubType"
- "IsVirtualDevice"
- "SBSAccessibilityWindowHostingClientToServerInterface"
- "SBSAccessibilityWindowHostingController"
- "SBSAccessibilityWindowHostingServerToClientInterface"
- "SBSAccessibilityWindowHostingSpecification"
- "SBSHomeScreenService: failed reloadIcons request (no target)."
- "Sucessfully unregistered from all overrides"
- "T@\"BSColor\",C,N"
- "Unable to set icon style to %s\n"
- "_connectionQueue_connection"
- "_connectionQueue_handleInterruption"
- "_registeredWindowContextIDsToLevel"
- "addIconTintColorObserver:"
- "com.apple.SpringBoardServices.SBSAccessibilityWindowHostingController.connectionQueue"
- "com.apple.springboard.accessibility-window-hosting"
- "iconUserInterfaceStyle"
- "initWithConfigurationType:"
- "initWithConfigurationType:tintColor:"
- "oPeik/9e8lQWMszEjbPzng"
- "registerWindowWithContextID:atLevel:"
- "reloadIcons"
- "setIconUserInterfaceStyle:"
- "unregisterWindowWithContextID:"
- "v20@0:8I16"
- "v28@0:8I16d20"
- "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"

```
