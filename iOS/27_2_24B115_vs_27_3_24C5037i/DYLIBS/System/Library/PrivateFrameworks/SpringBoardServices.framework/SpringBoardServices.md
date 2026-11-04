## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-4637.1.14.103.0
-  __TEXT.__text: 0x79170
-  __TEXT.__objc_methlist: 0x8eb0
-  __TEXT.__cstring: 0xe051
-  __TEXT.__const: 0x798
-  __TEXT.__oslogstring: 0x4bed
-  __TEXT.__gcc_except_tab: 0xcf8
+4637.2.11.104.0
+  __TEXT.__text: 0x7edf0
+  __TEXT.__objc_methlist: 0x9400
+  __TEXT.__cstring: 0xe8ab
+  __TEXT.__const: 0x808
+  __TEXT.__oslogstring: 0x52d7
+  __TEXT.__gcc_except_tab: 0xda4
   __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x3b80
+  __TEXT.__unwind_info: 0x3e20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3978
-  __DATA_CONST.__objc_classlist: 0x700
+  __DATA_CONST.__const: 0x3928
+  __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35e8
-  __DATA_CONST.__objc_protorefs: 0x1d0
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_selrefs: 0x37a8
+  __DATA_CONST.__objc_protorefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x8f0
-  __AUTH_CONST.__const: 0x2928
-  __AUTH_CONST.__cfstring: 0xaf60
-  __AUTH_CONST.__objc_const: 0x279f0
+  __DATA_CONST.__got: 0x938
+  __AUTH_CONST.__const: 0x2a90
+  __AUTH_CONST.__cfstring: 0xb6a0
+  __AUTH_CONST.__objc_const: 0x28eb0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x830
-  __AUTH.__objc_data: 0x39a8
-  __DATA.__objc_ivar: 0x898
-  __DATA.__data: 0x2390
+  __AUTH_CONST.__auth_got: 0x868
+  __AUTH.__objc_data: 0x3bd8
+  __DATA.__objc_ivar: 0x8d0
+  __DATA.__data: 0x23f0
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x278
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4367
-  Symbols:   8064
-  CStrings:  2143
+  Functions: 4551
+  Symbols:   8318
+  CStrings:  2238
 
Symbols:
+ +[SBSDeviceDeterminedConfiguration _classFromDevice:referenceBounds:idiom:homeButton:distinguishers:nativeScale:]
+ +[SBSDisplayToolServiceSpecification identifier]
+ +[SBSDisplayToolServiceSpecification interface]
+ +[SBSDisplayToolServiceSpecification serviceQuality]
+ +[SBSHomeScreenItemWebClip supportsBSXPCSecureCoding]
+ +[SBSHomeScreenServicePageState supportsSecureCoding]
+ +[SBSOrientationLockServiceSpecification identifier]
+ +[SBSOrientationLockServiceSpecification interface]
+ -[SBSDisplayConfigurationContext displaySurfaceType]
+ -[SBSDisplayConfigurationContext setDisplaySurfaceType:]
+ -[SBSDisplayToolService .cxx_destruct]
+ -[SBSDisplayToolService awaitSystemSpace:completionHandler:]
+ -[SBSDisplayToolService dealloc]
+ -[SBSDisplayToolService disableYoinkingFlipOverrideWithCompletion:]
+ -[SBSDisplayToolService enableYoinkingFlipOverrideForDuration:completion:]
+ -[SBSDisplayToolService init]
+ -[SBSDisplayToolService invalidate]
+ -[SBSDisplayToolService lockForTestingWithCompletion:]
+ -[SBSDisplayToolService replayHingeSamplesWithSettings:samplesPath:completionHandler:]
+ -[SBSDisplayToolService setBacklightState:displayUUID:completion:]
+ -[SBSDisplayToolService setDynamicMarkPersistence:completion:]
+ -[SBSDisplayToolService setPrimary:displayUUID:completion:]
+ -[SBSDisplayToolService swapDisplayWithSettings:completion:]
+ -[SBSDisplayToolService swapDisplayWithSettings:completionHandler:]
+ -[SBSDisplayToolService unlockForTestingWithCompletion:]
+ -[SBSDisplayToolServiceConnection .cxx_destruct]
+ -[SBSDisplayToolServiceConnection awaitSystemSpace:completionHandler:]
+ -[SBSDisplayToolServiceConnection dealloc]
+ -[SBSDisplayToolServiceConnection disableYoinkingFlipOverrideWithCompletion:]
+ -[SBSDisplayToolServiceConnection enableYoinkingFlipOverrideForDuration:completion:]
+ -[SBSDisplayToolServiceConnection init]
+ -[SBSDisplayToolServiceConnection lockForTestingWithCompletion:]
+ -[SBSDisplayToolServiceConnection replayHingeSamplesWithSettings:samplesPath:completionHandler:]
+ -[SBSDisplayToolServiceConnection setBacklightState:displayUUID:completion:]
+ -[SBSDisplayToolServiceConnection setDynamicMarkPersistence:completion:]
+ -[SBSDisplayToolServiceConnection setPrimary:displayUUID:completion:]
+ -[SBSDisplayToolServiceConnection swapDisplayWithSettings:completionHandler:]
+ -[SBSDisplayToolServiceConnection unlockForTestingWithCompletion:]
+ -[SBSFDIDeviceControlHostComponent setDisablesLiftToWake:]
+ -[SBSFDIDeviceControlHostComponent setDisablesTapToWake:]
+ -[SBSFDIDeviceControlHostComponent setRestrictsToConfigurationA:]
+ -[SBSHomeScreenItemWebClip .cxx_destruct]
+ -[SBSHomeScreenItemWebClip copyWithZone:]
+ -[SBSHomeScreenItemWebClip description]
+ -[SBSHomeScreenItemWebClip encodeWithBSXPCCoder:]
+ -[SBSHomeScreenItemWebClip hash]
+ -[SBSHomeScreenItemWebClip initWithBSXPCCoder:]
+ -[SBSHomeScreenItemWebClip initWithWebClipIdentifier:]
+ -[SBSHomeScreenItemWebClip isEqual:]
+ -[SBSHomeScreenItemWebClip kind]
+ -[SBSHomeScreenItemWebClip webClipIdentifier]
+ -[SBSHomeScreenService homeScreenPageState]
+ -[SBSHomeScreenService setDockEdge:animated:]
+ -[SBSHomeScreenService silhouetteLayoutForPageAtIndex:displaySize:]
+ -[SBSHomeScreenServicePageState copyWithZone:]
+ -[SBSHomeScreenServicePageState currentPageIndex]
+ -[SBSHomeScreenServicePageState currentPageType]
+ -[SBSHomeScreenServicePageState encodeWithCoder:]
+ -[SBSHomeScreenServicePageState initWithCoder:]
+ -[SBSHomeScreenServicePageState initWithCurrentPageIndex:currentPageType:pageCount:]
+ -[SBSHomeScreenServicePageState init]
+ -[SBSHomeScreenServicePageState pageCount]
+ -[SBSLockScreenService fetchDeviceDeterminedConfigurationsWithCompletionHandler:]
+ -[SBSLockScreenService fetchLockScreenContentCutoutReadouts:displayContext:orientation:completionHandler:]
+ -[SBSLockScreenServiceConnection _fetchLockScreenContentCutoutReadouts:displayContext:orientation:completionHandler:]
+ -[SBSLockScreenServiceConnection fetchDeviceDeterminedConfigurationsWithCompletionHandler:]
+ -[SBSLockScreenServiceConnection fetchLockScreenContentCutoutReadouts:displayContext:orientation:completionHandler:]
+ -[SBSOrientationLockService .cxx_destruct]
+ -[SBSOrientationLockService _connectionInterrupted:]
+ -[SBSOrientationLockService _connectionInvalidated:]
+ -[SBSOrientationLockService _noConnectionErrorForRequest:]
+ -[SBSOrientationLockService _remoteTarget]
+ -[SBSOrientationLockService dealloc]
+ -[SBSOrientationLockService init]
+ -[SBSOrientationLockService invalidate]
+ -[SBSOrientationLockService isOrientationLockedForTarget:completion:]
+ -[SBSOrientationLockService lockOrientationForTarget:completion:]
+ -[SBSOrientationLockService lockedOrientationForTarget:completion:]
+ -[SBSOrientationLockService supportedOrientationLockTargetsWithCompletion:]
+ -[SBSOrientationLockService unlockOrientationForTarget:completion:]
+ -[SBSSceneAccessoryDisplayLayoutElement displayIdentity]
+ -[SBSSceneAccessoryDisplayLayoutElement initWithIdentifier:displayIdentity:]
+ -[SBSSceneAccessoryDisplayLayoutElement succinctDescriptionBuilder]
+ -[SBSSystemServiceClient deviceOrientationForSystemSpaceOrientation:]
+ -[SBSSystemServiceClient getDevicePose]
+ -[SBSSystemServiceClient isButterflySplitViewStronglyPaired]
+ -[SBSSystemServiceClient setDevicePoseOverride:]
+ -[SBSSystemServiceClient systemSpaceOrientationForDeviceOrientation:]
+ -[SBSSystemServiceClient togglePictureInPictureProminence]
+ -[SBSTestAutomationService deviceOrientationForSystemSpaceOrientation:]
+ -[SBSTestAutomationService getDevicePose]
+ -[SBSTestAutomationService isButterflySplitViewStronglyPaired]
+ -[SBSTestAutomationService setDevicePoseOverride:]
+ -[SBSTestAutomationService systemSpaceOrientationForDeviceOrientation:]
+ -[SBSTestAutomationService togglePictureInPictureProminence]
+ -[SBSWallpaperClient .cxx_destruct]
+ -[SBSWallpaperClient _encodeDisplayContext:]
+ -[SBSWallpaperClient displayContext]
+ -[SBSWallpaperClient fetchAllLockScreenBoundsForType:orientation:completionHandler:]
+ -[SBSWallpaperClient fetchLockScreenBoundsForType:orientation:completionHandler:]
+ -[SBSWallpaperClient setDisplayContext:]
+ -[SBSWallpaperService _messageTypeForCutoutType:]
+ GCC_except_table127
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table160
+ GCC_except_table194
+ GCC_except_table28
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table47
+ _BSSerializeDataToXPCDictionaryWithKey
+ _CFPreferencesGetAppBooleanValue
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _OBJC_CLASS_$_SBSDisplayToolService
+ _OBJC_CLASS_$_SBSDisplayToolServiceConnection
+ _OBJC_CLASS_$_SBSDisplayToolServiceSpecification
+ _OBJC_CLASS_$_SBSHomeScreenItemWebClip
+ _OBJC_CLASS_$_SBSHomeScreenServicePageState
+ _OBJC_CLASS_$_SBSOrientationLockService
+ _OBJC_CLASS_$_SBSOrientationLockServiceSpecification
+ _OBJC_CLASS_$_SBSSceneAccessoryDisplayLayoutElement
+ _OBJC_IVAR_$_SBSDisplayConfigurationContext._displaySurfaceType
+ _OBJC_IVAR_$_SBSDisplayToolService._lock
+ _OBJC_IVAR_$_SBSDisplayToolService._lock_connection
+ _OBJC_IVAR_$_SBSDisplayToolServiceConnection._connection
+ _OBJC_IVAR_$_SBSFDIDeviceControlHostComponent.disablesLiftToWake
+ _OBJC_IVAR_$_SBSFDIDeviceControlHostComponent.disablesTapToWake
+ _OBJC_IVAR_$_SBSFDIDeviceControlHostComponent.restrictsToConfigurationA
+ _OBJC_IVAR_$_SBSHomeScreenItemWebClip._webClipIdentifier
+ _OBJC_IVAR_$_SBSHomeScreenServicePageState._currentPageIndex
+ _OBJC_IVAR_$_SBSHomeScreenServicePageState._currentPageType
+ _OBJC_IVAR_$_SBSHomeScreenServicePageState._pageCount
+ _OBJC_IVAR_$_SBSOrientationLockService._lock
+ _OBJC_IVAR_$_SBSOrientationLockService._lock_connection
+ _OBJC_IVAR_$_SBSOrientationLockService._lock_invalidated
+ _OBJC_IVAR_$_SBSWallpaperClient._displayContext
+ _OBJC_METACLASS_$_SBSDisplayToolService
+ _OBJC_METACLASS_$_SBSDisplayToolServiceConnection
+ _OBJC_METACLASS_$_SBSDisplayToolServiceSpecification
+ _OBJC_METACLASS_$_SBSHomeScreenItemWebClip
+ _OBJC_METACLASS_$_SBSHomeScreenServicePageState
+ _OBJC_METACLASS_$_SBSOrientationLockService
+ _OBJC_METACLASS_$_SBSOrientationLockServiceSpecification
+ _OBJC_METACLASS_$_SBSSceneAccessoryDisplayLayoutElement
+ _SBDisplayLayoutTransitionReasonHomeScreenEditing
+ _SBGetTopButtonFramesForDisplay
+ _SBLogDeviceOrientationUpdateDeferral
+ _SBLogDeviceOrientationUpdateDeferral.__logObj
+ _SBLogDeviceOrientationUpdateDeferral.onceToken
+ _SBLogDisplaySceneTracking
+ _SBLogDisplaySceneTracking.__logObj
+ _SBLogDisplaySceneTracking.onceToken
+ _SBLogLockScreenBiometricPocketSuppression
+ _SBLogLockScreenBiometricPocketSuppression.__logObj
+ _SBLogLockScreenBiometricPocketSuppression.onceToken
+ _SBLogSecureIndicator
+ _SBLogSecureIndicator.__logObj
+ _SBLogSecureIndicator.onceToken
+ _SBLogTouchRegions
+ _SBLogTouchRegions.__logObj
+ _SBLogTouchRegions.onceToken
+ _SBLogWallpaperHingeProgress
+ _SBLogWallpaperHingeProgress.__logObj
+ _SBLogWallpaperHingeProgress.onceToken
+ _SBSCurrentCoverDisplaySize
+ _SBSCurrentCoverDisplaySize.onceToken
+ _SBSCurrentCoverDisplaySize.sResolvedCoverSize
+ _SBSDisplayLayoutElementSceneAccessoryIdentifier
+ _SBSOrientationLockServiceEntitlement
+ _SBSTopButtonFramesForPostersForDisplayIdentifier
+ __OBJC_$_CLASS_METHODS_SBSDisplayToolServiceSpecification
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenItemWebClip
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenServicePageState
+ __OBJC_$_CLASS_METHODS_SBSOrientationLockServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_SBSDisplayToolServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_SBSHomeScreenServicePageState
+ __OBJC_$_CLASS_PROP_LIST_SBSOrientationLockServiceSpecification
+ __OBJC_$_INSTANCE_METHODS_SBSDisplayToolService
+ __OBJC_$_INSTANCE_METHODS_SBSDisplayToolServiceConnection
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenItemWebClip
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenServicePageState
+ __OBJC_$_INSTANCE_METHODS_SBSOrientationLockService
+ __OBJC_$_INSTANCE_METHODS_SBSSceneAccessoryDisplayLayoutElement
+ __OBJC_$_INSTANCE_VARIABLES_SBSDisplayToolService
+ __OBJC_$_INSTANCE_VARIABLES_SBSDisplayToolServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_SBSHomeScreenItemWebClip
+ __OBJC_$_INSTANCE_VARIABLES_SBSHomeScreenServicePageState
+ __OBJC_$_INSTANCE_VARIABLES_SBSOrientationLockService
+ __OBJC_$_INSTANCE_VARIABLES_SBSWallpaperClient
+ __OBJC_$_PROP_LIST_SBSDisplayToolService
+ __OBJC_$_PROP_LIST_SBSHomeScreenItemWebClip
+ __OBJC_$_PROP_LIST_SBSHomeScreenServicePageState
+ __OBJC_$_PROP_LIST_SBSOrientationLockService
+ __OBJC_$_PROP_LIST_SBSSceneAccessoryDisplayLayoutElement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSDisplayToolServiceServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSOrientationLockServiceServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSDisplayToolServiceServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSOrientationLockServiceServerInterface
+ __OBJC_$_PROTOCOL_REFS_SBSOrientationLockServiceServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_SBSDisplayToolService
+ __OBJC_CLASS_PROTOCOLS_$_SBSHomeScreenServicePageState
+ __OBJC_CLASS_PROTOCOLS_$_SBSOrientationLockService
+ __OBJC_CLASS_PROTOCOLS_$_SBSSceneAccessoryDisplayLayoutElement
+ __OBJC_CLASS_RO_$_SBSDisplayToolService
+ __OBJC_CLASS_RO_$_SBSDisplayToolServiceConnection
+ __OBJC_CLASS_RO_$_SBSDisplayToolServiceSpecification
+ __OBJC_CLASS_RO_$_SBSHomeScreenItemWebClip
+ __OBJC_CLASS_RO_$_SBSHomeScreenServicePageState
+ __OBJC_CLASS_RO_$_SBSOrientationLockService
+ __OBJC_CLASS_RO_$_SBSOrientationLockServiceSpecification
+ __OBJC_CLASS_RO_$_SBSSceneAccessoryDisplayLayoutElement
+ __OBJC_LABEL_PROTOCOL_$_SBSDisplayToolServiceServerInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSOrientationLockServiceServerInterface
+ __OBJC_METACLASS_RO_$_SBSDisplayToolService
+ __OBJC_METACLASS_RO_$_SBSDisplayToolServiceConnection
+ __OBJC_METACLASS_RO_$_SBSDisplayToolServiceSpecification
+ __OBJC_METACLASS_RO_$_SBSHomeScreenItemWebClip
+ __OBJC_METACLASS_RO_$_SBSHomeScreenServicePageState
+ __OBJC_METACLASS_RO_$_SBSOrientationLockService
+ __OBJC_METACLASS_RO_$_SBSOrientationLockServiceSpecification
+ __OBJC_METACLASS_RO_$_SBSSceneAccessoryDisplayLayoutElement
+ __OBJC_PROTOCOL_$_SBSDisplayToolServiceServerInterface
+ __OBJC_PROTOCOL_$_SBSOrientationLockServiceServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SBSDisplayToolServiceServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SBSOrientationLockServiceServerInterface
+ __SBMigGetTopButtonFramesForDisplay
+ __SBSGetTopButtonFramesForDisplay
+ __SBS_Private_BaseIsV68OrSimilarDevice
+ __XGetTopButtonFramesForDisplay
+ ___110-[SBSWallpaperService fetchLockScreenContentCutoutBoundsForType:orientation:displayContext:completionHandler:]_block_invoke
+ ___113+[SBSDeviceDeterminedConfiguration _classFromDevice:referenceBounds:idiom:homeButton:distinguishers:nativeScale:]_block_invoke
+ ___113+[SBSDeviceDeterminedConfiguration _classFromDevice:referenceBounds:idiom:homeButton:distinguishers:nativeScale:]_block_invoke_2
+ ___113-[SBSWallpaperService fetchAllLockScreenContentCutoutBoundsForType:orientation:displayContext:completionHandler:]_block_invoke_2
+ ___116-[SBSLockScreenServiceConnection fetchLockScreenContentCutoutReadouts:displayContext:orientation:completionHandler:]_block_invoke
+ ___33-[SBSOrientationLockService init]_block_invoke
+ ___33-[SBSOrientationLockService init]_block_invoke_2
+ ___36-[SBSHomeScreenItemWebClip isEqual:]_block_invoke
+ ___39-[SBSDisplayToolServiceConnection init]_block_invoke
+ ___39-[SBSDisplayToolServiceConnection init]_block_invoke_2
+ ___39-[SBSSystemServiceClient getDevicePose]_block_invoke
+ ___39-[SBSSystemServiceClient getDevicePose]_block_invoke_2
+ ___47+[SBSDisplayToolServiceSpecification interface]_block_invoke
+ ___48-[SBSSystemServiceClient setDevicePoseOverride:]_block_invoke
+ ___48-[SBSSystemServiceClient setDevicePoseOverride:]_block_invoke_2
+ ___51+[SBSOrientationLockServiceSpecification interface]_block_invoke
+ ___60-[SBSDisplayToolService swapDisplayWithSettings:completion:]_block_invoke
+ ___60-[SBSSystemServiceClient isButterflySplitViewStronglyPaired]_block_invoke
+ ___64-[SBSDisplayToolServiceConnection lockForTestingWithCompletion:]_block_invoke
+ ___65-[SBSOrientationLockService lockOrientationForTarget:completion:]_block_invoke
+ ___66-[SBSDisplayToolServiceConnection unlockForTestingWithCompletion:]_block_invoke
+ ___67-[SBSOrientationLockService lockedOrientationForTarget:completion:]_block_invoke
+ ___67-[SBSOrientationLockService unlockOrientationForTarget:completion:]_block_invoke
+ ___69-[SBSDisplayToolServiceConnection setPrimary:displayUUID:completion:]_block_invoke
+ ___69-[SBSOrientationLockService isOrientationLockedForTarget:completion:]_block_invoke
+ ___69-[SBSSystemServiceClient deviceOrientationForSystemSpaceOrientation:]_block_invoke
+ ___69-[SBSSystemServiceClient deviceOrientationForSystemSpaceOrientation:]_block_invoke_2
+ ___69-[SBSSystemServiceClient deviceOrientationForSystemSpaceOrientation:]_block_invoke_3
+ ___69-[SBSSystemServiceClient systemSpaceOrientationForDeviceOrientation:]_block_invoke
+ ___69-[SBSSystemServiceClient systemSpaceOrientationForDeviceOrientation:]_block_invoke_2
+ ___69-[SBSSystemServiceClient systemSpaceOrientationForDeviceOrientation:]_block_invoke_3
+ ___70-[SBSDisplayToolServiceConnection awaitSystemSpace:completionHandler:]_block_invoke
+ ___72-[SBSDisplayToolServiceConnection setDynamicMarkPersistence:completion:]_block_invoke
+ ___75-[SBSOrientationLockService supportedOrientationLockTargetsWithCompletion:]_block_invoke
+ ___76-[SBSDisplayToolServiceConnection setBacklightState:displayUUID:completion:]_block_invoke
+ ___77-[SBSDisplayToolServiceConnection disableYoinkingFlipOverrideWithCompletion:]_block_invoke
+ ___77-[SBSDisplayToolServiceConnection swapDisplayWithSettings:completionHandler:]_block_invoke
+ ___81-[SBSWallpaperClient fetchLockScreenBoundsForType:orientation:completionHandler:]_block_invoke
+ ___84-[SBSDisplayToolServiceConnection enableYoinkingFlipOverrideForDuration:completion:]_block_invoke
+ ___84-[SBSWallpaperClient fetchAllLockScreenBoundsForType:orientation:completionHandler:]_block_invoke
+ ___84-[SBSWallpaperClient fetchAllLockScreenBoundsForType:orientation:completionHandler:]_block_invoke_2
+ ___91-[SBSLockScreenServiceConnection fetchDeviceDeterminedConfigurationsWithCompletionHandler:]_block_invoke
+ ___96-[SBSDisplayToolServiceConnection replayHingeSamplesWithSettings:samplesPath:completionHandler:]_block_invoke
+ ___SBLogDeviceOrientationUpdateDeferral_block_invoke
+ ___SBLogDisplaySceneTracking_block_invoke
+ ___SBLogLockScreenBiometricPocketSuppression_block_invoke
+ ___SBLogSecureIndicator_block_invoke
+ ___SBLogTouchRegions_block_invoke
+ ___SBLogWallpaperHingeProgress_block_invoke
+ ___SBSCurrentCoverDisplaySize_block_invoke
+ ___block_descriptor_40_e28_{CGSize=dd}24?0{CGSize=dd}8l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e67_v24?0"NSArray<__SBSDeviceDeterminedConfiguration__>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e15_v32?0{?=qiii}8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v16?0q8lr32l8
+ ___block_descriptor_40_e8_32w_e42_v16?0"<BSServiceConnectionConfiguring>"8lw32l8
+ ___block_descriptor_44_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_48_e18_B24?0{CGSize=dd}8l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___strlcpy_chk
+ __xpc_type_array
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kSBSTestAutomationServiceMessageKeyButterflySplitViewStronglyPaired
+ _kSBSTestAutomationServiceMessageKeyDevicePoseOverride
+ _kSBSTestAutomationServiceMessageKeyInterfaceOrientation
+ _kSBSWallpaperServiceClientMessageKeyDisplayContext
+ _kSBSWallpaperServiceClientMessageKeyRects
+ _xpc_array_get_count
+ _xpc_array_get_value
- +[SBSDeviceDeterminedConfiguration _classFromDevice:referenceBounds:idiom:homeButton:nativeScale:]
- +[SBSFDIDeviceControlClientSettingsExtension protocol]
- -[SBSLockScreenService setBacklightState:displayUUID:completion:]
- -[SBSLockScreenService setPrimary:displayUUID:completion:]
- -[SBSLockScreenServiceConnection setBacklightState:displayUUID:completion:]
- -[SBSLockScreenServiceConnection setPrimary:displayUUID:completion:]
- -[SBSWallpaperClient _fetchLockScreenBoundsCheckOfType:orientation:completionHandler:]
- -[SBSWallpaperClient fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]
- -[SBSWallpaperClient fetchLimitedOcclusionBoundsForOrientation:completionHandler:]
- -[SBSWallpaperClient fetchLockScreenContentCutoutBoundsForOrientation:completionHandler:]
- -[SBSWallpaperClient fetchLockScreenTimeBoundsForOrientation:completionHandler:]
- -[SBSWallpaperClient fetchMaximalLockScreenContentCutoutBoundsForOrientation:completionHandler:]
- -[SBSWallpaperClient fetchObscurableBoundsForOrientation:completionHandler:]
- GCC_except_table133
- GCC_except_table137
- GCC_except_table140
- GCC_except_table177
- GCC_except_table32
- GCC_except_table35
- GCC_except_table36
- GCC_except_table38
- GCC_except_table39
- GCC_except_table41
- GCC_except_table48
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_SBSFDIDeviceControlClientSettingsExtension
- _OBJC_IVAR_$_SBSWallpaperService._displayContext
- _OBJC_METACLASS_$_FBSSettingsExtension
- _OBJC_METACLASS_$_SBSFDIDeviceControlClientSettingsExtension
- __OBJC_$_CLASS_METHODS_SBSFDIDeviceControlClientSettingsExtension
- __OBJC_$_PROP_LIST_SBSFDIDeviceControlClientSettings
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSFDIDeviceControlClientSettings
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBSFDIDeviceControlClientSettings
- __OBJC_$_PROTOCOL_REFS_SBSFDIDeviceControlClientSettings
- __OBJC_CLASS_RO_$_SBSFDIDeviceControlClientSettingsExtension
- __OBJC_LABEL_PROTOCOL_$_SBSFDIDeviceControlClientSettings
- __OBJC_METACLASS_RO_$_SBSFDIDeviceControlClientSettingsExtension
- __OBJC_PROTOCOL_$_SBSFDIDeviceControlClientSettings
- ___68-[SBSLockScreenServiceConnection setPrimary:displayUUID:completion:]_block_invoke
- ___75-[SBSLockScreenServiceConnection setBacklightState:displayUUID:completion:]_block_invoke
- ___77-[SBSWallpaperService fetchObscurableBoundsForOrientation:completionHandler:]_block_invoke
- ___77-[SBSWallpaperService fetchObscurableBoundsForOrientation:completionHandler:]_block_invoke_2
- ___81-[SBSWallpaperService fetchLockScreenTimeBoundsForOrientation:completionHandler:]_block_invoke
- ___81-[SBSWallpaperService fetchLockScreenTimeBoundsForOrientation:completionHandler:]_block_invoke_2
- ___83-[SBSWallpaperService fetchLimitedOcclusionBoundsForOrientation:completionHandler:]_block_invoke
- ___83-[SBSWallpaperService fetchLimitedOcclusionBoundsForOrientation:completionHandler:]_block_invoke_2
- ___86-[SBSWallpaperClient _fetchLockScreenBoundsCheckOfType:orientation:completionHandler:]_block_invoke
- ___86-[SBSWallpaperClient _fetchLockScreenBoundsCheckOfType:orientation:completionHandler:]_block_invoke_2
- ___90-[SBSWallpaperService fetchLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke
- ___90-[SBSWallpaperService fetchLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke_2
- ___97-[SBSWallpaperService fetchMaximalLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke
- ___97-[SBSWallpaperService fetchMaximalLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke_2
- ___98-[SBSWallpaperService fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke
- ___98-[SBSWallpaperService fetchExtendedLockScreenContentCutoutBoundsForOrientation:completionHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e39_v40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8
- _kSBSSystemApertureDisabled_block_invoke.deviceSubtype
CStrings:
+ "B24@?0{CGSize=dd}8"
+ "DeviceOrientationUpdateDeferral"
+ "DisplaySceneTracking"
+ "EdgeSwipeBandExpansionEnabled"
+ "FBSDisplayIdentity"
+ "Failed to synchronize cover display crop to global domain; clients will resolve a stale or absent value for %{public}@"
+ "PhoneRoundedBehind (V68 Inner)"
+ "PhoneRoundedCorner (V68 Cover)"
+ "PocketSuppression"
+ "Published cover display crop to global domain: %{public}@=%{BOOL}u synchronized=%{BOOL}u"
+ "Read published cover display crop from global domain: %{public}@=%{BOOL}u set=%{BOOL}u"
+ "Resolved cover display crop in SpringBoard: cropped=%{BOOL}u (EdgeSwipeBandExpansionEnabled=%{BOOL}u set=%{BOOL}u)"
+ "Resolved cover display size: {%g, %g} (cropped=%{BOOL}u inSpringBoard=%{BOOL}u)"
+ "SBCoverDisplayCropped"
+ "SBSDisplayToolService.m"
+ "SBSDisplayToolService: failed request for backlight state change (no remoteTarget)"
+ "SBSDisplayToolService: failed request for disableYoinkingFlipOverride (no remoteTarget)"
+ "SBSDisplayToolService: failed request for enableYoinkingFlipOverrideForDuration (no remoteTarget)"
+ "SBSDisplayToolService: failed request for hinge replay (no remoteTarget)"
+ "SBSDisplayToolService: failed request for lockForTesting (no remoteTarget)"
+ "SBSDisplayToolService: failed request for setDynamicMarkPersistence (no remoteTarget)"
+ "SBSDisplayToolService: failed request for setPrimary change (no remoteTarget)"
+ "SBSDisplayToolService: failed request for swap display (no remoteTarget)"
+ "SBSDisplayToolService: failed request for unlockForTesting (no remoteTarget)"
+ "SBSDisplayToolService: failed request to await a system space (no remoteTarget)"
+ "SBSDisplayToolService: invalidated remotely"
+ "SBSDisplayToolServiceErrorDomain"
+ "SBSHomeScreenService: failed homeScreenPageState request (no reply)."
+ "SBSHomeScreenService: failed homeScreenPageState request (no target)."
+ "SBSHomeScreenService: failed setDockEdge request (no target)."
+ "SBSHomeScreenService: failed silhouetteLayoutForPageAtIndex:displaySize: request (no target)."
+ "SBSLockScreenService: failed request for device determined configuration fetch (no remoteTarget)"
+ "SBSOrientationLockService.m"
+ "SBSOrientationLockService: connection interrupted, reactivating"
+ "SBSOrientationLockService: failed request for %{public}@ (no remoteTarget)"
+ "SBSOrientationLockService: unable to create endpoint"
+ "SBSOrientationLockServiceErrorDomain"
+ "SBSSceneAccessoryDisplayLayoutElement.m"
+ "SecureIndicator"
+ "TouchRegions"
+ "WallpaperHingeProgress"
+ "[_bs_assert_object isKindOfClass:FBSDisplayIdentityClass]"
+ "_SBXXGetTopButtonFramesForDisplay"
+ "band"
+ "butterflySplitViewStronglyPaired"
+ "called awaitSystemSpace:completionHandler: after invalidation"
+ "called disableYoinkingFlipOverrideWithCompletion: after invalidation"
+ "called enableYoinkingFlipOverrideForDuration:completion: after invalidation"
+ "called fetchDeviceDeterminedConfigurationsWithCompletionHandler after invalidation"
+ "called lockForTestingWithCompletion: after invalidation"
+ "called replayHingeSamplesWithSettings:samplesPath:completionHandler: after invalidation"
+ "called setDynamicMarkPersistence:completion: after invalidation"
+ "called swapDisplayWithSettings:completionHandler: after invalidation"
+ "called unlockForTestingWithCompletion: after invalidation"
+ "com.apple.SpringBoard.transitionReason.homescreenEditing"
+ "com.apple.backboardd"
+ "com.apple.springboard.orientation-lock-service"
+ "com.apple.springboard.sbdisplay"
+ "com.apple.springboard.sceneAccessory"
+ "currentPageIndex"
+ "currentPageType"
+ "devicePoseOverride"
+ "directionMode"
+ "displayContext"
+ "displaySurfaceType"
+ "duration"
+ "firstSweep"
+ "interLoopDelay"
+ "interSweepDelay"
+ "interfaceOrientation"
+ "isOrientationLocked"
+ "landingMaximumDegrees"
+ "landingMinimumDegrees"
+ "lockedOrientation"
+ "loopCount"
+ "loopIdentifier"
+ "maxDuration"
+ "mode"
+ "must invalidate SBSOrientationLockService before dealloc"
+ "no connection to SpringBoard's display tool service"
+ "no connection to SpringBoard's orientation lock service"
+ "pageCount"
+ "prewarmDuration"
+ "profileOverride"
+ "rects"
+ "seed"
+ "supported targets"
+ "targetHingePosition"
+ "targetMode"
+ "unlock"
+ "v16@?0@\"NSArray\"8"
+ "v24@?0@\"NSArray<__SBSDeviceDeterminedConfiguration__>\"8@\"NSError\"16"
+ "v32@?0{?=qiii}8"
+ "waitForCompletion"
+ "webClipIdentifier"
+ "windowDuration"
+ "{CGSize=dd}24@?0{CGSize=dd}8"
- "SBSLockScreenService: failed request for backlight state change (no remoteTarget)"
- "SBSLockScreenService: failed request for setPrimary change (no remoteTarget)"
```
