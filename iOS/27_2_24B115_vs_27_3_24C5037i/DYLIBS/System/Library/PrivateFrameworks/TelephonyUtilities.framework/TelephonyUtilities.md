## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`

```diff

-1626.200.91.2.3
-  __TEXT.__text: 0x1b3034
-  __TEXT.__objc_methlist: 0x1bbc0
-  __TEXT.__cstring: 0x147c6
-  __TEXT.__const: 0x4bac
-  __TEXT.__oslogstring: 0x14c0a
-  __TEXT.__gcc_except_tab: 0x183c
+1626.300.42.0.0
+  __TEXT.__text: 0x1b3e00
+  __TEXT.__objc_methlist: 0x1bd60
+  __TEXT.__cstring: 0x14b36
+  __TEXT.__const: 0x4bcc
+  __TEXT.__oslogstring: 0x14df4
+  __TEXT.__gcc_except_tab: 0x18d4
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8a5
-  __TEXT.__constg_swiftt: 0xec4
-  __TEXT.__swift5_typeref: 0x144b
+  __TEXT.__constg_swiftt: 0xebc
+  __TEXT.__swift5_typeref: 0x1427
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0xc89
-  __TEXT.__swift5_fieldmd: 0x1320
+  __TEXT.__swift5_fieldmd: 0x132c
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x3dc
   __TEXT.__swift5_types: 0x14c
-  __TEXT.__swift5_capture: 0x38c
-  __TEXT.__swift_as_entry: 0xec
-  __TEXT.__swift_as_ret: 0x104
-  __TEXT.__swift_as_cont: 0x1e4
+  __TEXT.__swift5_capture: 0x2fc
+  __TEXT.__swift_as_entry: 0xd8
+  __TEXT.__swift_as_ret: 0xf4
+  __TEXT.__swift_as_cont: 0x1cc
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x98a8
-  __TEXT.__eh_frame: 0x31e0
+  __TEXT.__unwind_info: 0x9960
+  __TEXT.__eh_frame: 0x2f98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3958
-  __DATA_CONST.__objc_classlist: 0x8a8
+  __DATA_CONST.__const: 0x3a48
+  __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x410
+  __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb940
+  __DATA_CONST.__objc_selrefs: 0xba48
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x6e8
-  __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x10a8
-  __AUTH_CONST.__const: 0x4ee0
-  __AUTH_CONST.__cfstring: 0x12960
-  __AUTH_CONST.__objc_const: 0x2b748
+  __DATA_CONST.__objc_superrefs: 0x6f0
+  __DATA_CONST.__objc_arraydata: 0xaf8
+  __DATA_CONST.__got: 0x10c8
+  __AUTH_CONST.__const: 0x4e90
+  __AUTH_CONST.__cfstring: 0x12be0
+  __AUTH_CONST.__objc_const: 0x2baa0
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__auth_got: 0x1688
-  __AUTH.__objc_data: 0x2b70
-  __AUTH.__data: 0xe00
-  __DATA.__objc_ivar: 0x1954
-  __DATA.__data: 0x3f50
+  __AUTH_CONST.__objc_arrayobj: 0x318
+  __AUTH_CONST.__auth_got: 0x1698
+  __AUTH.__objc_data: 0x2c60
+  __AUTH.__data: 0xde0
+  __DATA.__objc_ivar: 0x1964
+  __DATA.__data: 0x3fc0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x2da8
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12099
-  Symbols:   16292
-  CStrings:  4694
+  Functions: 12136
+  Symbols:   16395
+  CStrings:  4737
 
Symbols:
+ +[CSDMessagingHandle(Additions) handleForRelayWithTUHandle:]
+ +[TUFeatureFlags isLiveActivitiesQFAEnabled]
+ +[TUPlatformCapabilities isDualDisplayDevice]
+ +[TUVideoDeviceController _aspectRatioForAttributes:landscape:]
+ +[TUWalletBusinessCallerIDProvider sharedInstance]
+ -[TUAudioSystemController _pickedRouteIdentifier]
+ -[TUAudioSystemController _updateCachedDisabledRoutes:]
+ -[TUAudioSystemController currentlyActiveCategory]
+ -[TUBusinessServicesMetadataDataProvider fetchCachedBusinessServiceInformationForHandleValue:completion:]
+ -[TUCall isPrimaryVideoPaused]
+ -[TUCall setPrimaryVideoPaused:]
+ -[TUCallServicesInterface setPrimaryVideoPaused:forCallWithUniqueProxyIdentifier:]
+ -[TUDynamicCallDisplayContext _applyBusinessCallerItem:forCall:fromCache:]
+ -[TUDynamicCallDisplayContext updateDisplayContextWithCachedBusinessChatServiceInfoUsingCall:]
+ -[TUDynamicCallDisplayContext updateDisplayContextWithWalletBusinessInfoUsingCall:]
+ -[TUDynamicCallDisplayContext walletBusinessCallerIDProvider]
+ -[TUFeatureFlags globalReportUnknownEnabled]
+ -[TUProxyCall isPrimaryVideoPaused]
+ -[TUProxyCall setPrimaryVideoPaused:]
+ -[TURoute localizedDisabledReason]
+ -[TUVideoDeviceController setPreviewPresentationOrientation:]
+ -[TUVideoDeviceControllerProvider appendFriendModeCamerasToDevices:]
+ -[TUVideoDeviceControllerProvider setPreviewPresentationOrientation:]
+ -[TUWalletBusinessCallerIDProvider .cxx_destruct]
+ -[TUWalletBusinessCallerIDProvider digitsOnlyFromPhoneNumber:]
+ -[TUWalletBusinessCallerIDProvider escapedQueryStringLiteral:]
+ -[TUWalletBusinessCallerIDProvider fetchBusinessNameForNormalizedPhoneNumber:completion:]
+ -[TUWalletBusinessCallerIDProvider initWithSpotlightQuerying:]
+ -[TUWalletBusinessCallerIDProvider init]
+ -[TUWalletBusinessCallerIDProvider queryStringForDigitsOnlyPhoneNumber:]
+ -[TUWalletBusinessCallerIDProvider spotlightQuerying]
+ -[TUWalletCSSearchQueryRunner runQueryString:fetchAttributes:completion:]
+ GCC_except_table153
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table207
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table95
+ GCC_except_table96
+ _MGCopyAnswer
+ _MGIsDeviceOfType
+ _OBJC_CLASS_$_CSSearchQuery
+ _OBJC_CLASS_$_CSSearchQueryContext
+ _OBJC_CLASS_$_TUPlatformCapabilities
+ _OBJC_CLASS_$_TUWalletBusinessCallerIDProvider
+ _OBJC_CLASS_$_TUWalletCSSearchQueryRunner
+ _OBJC_IVAR_$_TUAudioSystemController._currentDisabledRoutes
+ _OBJC_IVAR_$_TUAudioSystemController._lastPickedRouteIdentifier
+ _OBJC_IVAR_$_TUProxyCall._primaryVideoPaused
+ _OBJC_IVAR_$_TUWalletBusinessCallerIDProvider._spotlightQuerying
+ _OBJC_METACLASS_$_TUPlatformCapabilities
+ _OBJC_METACLASS_$_TUWalletBusinessCallerIDProvider
+ _OBJC_METACLASS_$_TUWalletCSSearchQueryRunner
+ _TUCallAssistantThirdPartyAvailable
+ _TUCallPrimaryVideoPausedForVideoCaptureMode
+ _TUSimulatedModeEnabledDidChangeNotification
+ _TUVideoDeviceControllerSecondaryAttributesChangedLandscapeAspectRatioKey
+ _TUVideoDeviceControllerSecondaryAttributesChangedPortraitAspectRatioKey
+ __OBJC_$_CLASS_METHODS_TUPlatformCapabilities
+ __OBJC_$_CLASS_METHODS_TUWalletBusinessCallerIDProvider
+ __OBJC_$_CLASS_PROP_LIST_TUPlatformCapabilities
+ __OBJC_$_CLASS_PROP_LIST_TUWalletBusinessCallerIDProvider
+ __OBJC_$_INSTANCE_METHODS_TUWalletBusinessCallerIDProvider
+ __OBJC_$_INSTANCE_METHODS_TUWalletCSSearchQueryRunner
+ __OBJC_$_INSTANCE_VARIABLES_TUWalletBusinessCallerIDProvider
+ __OBJC_$_PROP_LIST_TUWalletBusinessCallerIDProvider
+ __OBJC_$_PROP_LIST_TUWalletCSSearchQueryRunner
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUWalletSpotlightQuerying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUWalletSpotlightQuerying
+ __OBJC_$_PROTOCOL_REFS_TUWalletSpotlightQuerying
+ __OBJC_CLASS_PROTOCOLS_$_TUWalletCSSearchQueryRunner
+ __OBJC_CLASS_RO_$_TUPlatformCapabilities
+ __OBJC_CLASS_RO_$_TUWalletBusinessCallerIDProvider
+ __OBJC_CLASS_RO_$_TUWalletCSSearchQueryRunner
+ __OBJC_LABEL_PROTOCOL_$_TUWalletSpotlightQuerying
+ __OBJC_METACLASS_RO_$_TUPlatformCapabilities
+ __OBJC_METACLASS_RO_$_TUWalletBusinessCallerIDProvider
+ __OBJC_METACLASS_RO_$_TUWalletCSSearchQueryRunner
+ __OBJC_PROTOCOL_$_TUWalletSpotlightQuerying
+ ___105-[TUBusinessServicesMetadataDataProvider fetchCachedBusinessServiceInformationForHandleValue:completion:]_block_invoke
+ ___37-[TUProxyCall setPrimaryVideoPaused:]_block_invoke
+ ___37-[TUProxyCall setPrimaryVideoPaused:]_block_invoke_2
+ ___44+[TUFeatureFlags isLiveActivitiesQFAEnabled]_block_invoke
+ ___45+[TUPlatformCapabilities isDualDisplayDevice]_block_invoke
+ ___50+[TUWalletBusinessCallerIDProvider sharedInstance]_block_invoke
+ ___68-[TUVideoDeviceControllerProvider appendFriendModeCamerasToDevices:]_block_invoke
+ ___68-[TUVideoDeviceControllerProvider appendFriendModeCamerasToDevices:]_block_invoke_2
+ ___68-[TUVideoDeviceControllerProvider appendFriendModeCamerasToDevices:]_block_invoke_3
+ ___70-[TUAudioSystemController _handlePickableRoutesDidChangeNotification:]_block_invoke_2
+ ___73-[TUWalletCSSearchQueryRunner runQueryString:fetchAttributes:completion:]_block_invoke
+ ___73-[TUWalletCSSearchQueryRunner runQueryString:fetchAttributes:completion:]_block_invoke_2
+ ___74-[TUDynamicCallDisplayContext _applyBusinessCallerItem:forCall:fromCache:]_block_invoke
+ ___83-[TUDynamicCallDisplayContext updateDisplayContextWithWalletBusinessInfoUsingCall:]_block_invoke
+ ___89-[TUWalletBusinessCallerIDProvider fetchBusinessNameForNormalizedPhoneNumber:completion:]_block_invoke
+ ___94-[TUDynamicCallDisplayContext updateDisplayContextWithCachedBusinessChatServiceInfoUsingCall:]_block_invoke
+ ___block_descriptor_32_e32_B32?0"AVCaptureDevice"8Q16^B24l
+ ___block_descriptor_35_e5_v8?0l
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e44_v24?0"<TUCachedBusinessItem>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48w_e18_v16?0"NSString"8lw48l8s32l8s40l8
+ ___getAVSystemController_CurrentlyActiveCategoryAttributeSymbolLoc_block_invoke
+ _appendFriendModeCamerasToDevices:._AVCaptureDeviceTypeBuiltInBostonUltraWideCamera
+ _appendFriendModeCamerasToDevices:._AVCaptureDeviceTypeBuiltInRenoUltraWideCamera
+ _appendFriendModeCamerasToDevices:._AVMediaTypeVideo
+ _appendFriendModeCamerasToDevices:._pred__AVCaptureDeviceTypeBuiltInBostonUltraWideCamera
+ _appendFriendModeCamerasToDevices:._pred__AVCaptureDeviceTypeBuiltInRenoUltraWideCamera
+ _appendFriendModeCamerasToDevices:._pred__AVMediaTypeVideo
+ _getAVSystemController_CurrentlyActiveCategoryAttributeSymbolLoc.ptr
+ _getAVSystemController_RouteDescriptionKey_AVAudioRouteName
+ _getAVSystemController_RouteDescriptionKey_RouteUID
+ _isDualDisplayDevice.isDualDisplayDevice
+ _isDualDisplayDevice.onceToken
+ _isLiveActivitiesQFAEnabled.onceToken
+ _isLiveActivitiesQFAEnabled.result
+ _sharedInstance.sProvider
- -[TUConfigurationProvider isSmartVoicemailActionsAvailable]
- -[TUConfigurationProvider isSmartVoicemailActionsEnabled]
- -[TUConfigurationProvider setSmartVoicemailActionsEnabled:]
- -[TUUserConfiguration isSmartVoicemailActionsEnabled]
- -[TUUserConfiguration setSmartVoicemailActionsEnabled:]
- GCC_except_table152
- GCC_except_table162
- GCC_except_table165
- GCC_except_table168
- GCC_except_table171
- GCC_except_table174
- GCC_except_table180
- GCC_except_table183
- GCC_except_table186
- GCC_except_table206
- GCC_except_table73
- GCC_except_table75
- GCC_except_table93
- _TUSmartVoicemailActionsEnabledKey
- _symbolic SbIeAgHr_
- _symbolic So8TUHandleC
- _symbolic _____ySb_G ScG8IteratorV
CStrings:
+ "(kMDItemContentType == \"%@\") && (%@ == 1) && (%@ == \"%@\")"
+ "AVCaptureDeviceTypeBuiltInBostonUltraWideCamera"
+ "AVCaptureDeviceTypeBuiltInRenoUltraWideCamera"
+ "AVLiveActivity"
+ "AVSystemController_CurrentlyActiveCategoryAttribute"
+ "Already have business information for call: %@, ignoring lower-priority cached result."
+ "Asked to set primaryVideoPaused from %d to %d for %@. Posting necessary notifications and updating daemon"
+ "B32@?0@\"AVCaptureDevice\"8Q16^B24"
+ "ControlCenter"
+ "Disabled routes changed from %@ to %@"
+ "Discarding _cachedInputDevices because %@ is disconnected"
+ "Got cached businessItem: %@ for destinationID: %@"
+ "Ignoring disconnected system-preferred camera: %@"
+ "LiveActivitiesQFA"
+ "Mac17,10"
+ "Mac17,11"
+ "Mac17,12"
+ "Mac17,13"
+ "MacQFA"
+ "MenuBar"
+ "NSString *getAVSystemController_CurrentlyActiveCategoryAttribute(void)"
+ "No Wallet business information found for '%@'"
+ "No primary session available for preview presentation orientation"
+ "Passbook_isPaymentPass"
+ "Passbook_normalizedPhoneNumbers"
+ "Posting TUAudioSystemAudioPickableRoutesChanged (didClearPickableRoutes: %d, didChangeDisabledRoutes: %d, didChangePickedRoute: %d)"
+ "ProductType"
+ "Proxying setPrimaryVideoPaused=%d for %@"
+ "Querying business service cache for destinationID: %@"
+ "ROUTE_DISABLED_ONLY_AVAILABLE_ON_FRONT_DISPLAY"
+ "Setting preview presentation orientation: %d"
+ "Sign in required"
+ "TUVideoDeviceControllerSecondaryAttributesChangedLandscapeAspectRatio"
+ "TUVideoDeviceControllerSecondaryAttributesChangedPortraitAspectRatio"
+ "TargetSubType"
+ "V68"
+ "Wallet business caller ID Spotlight query failed: %@"
+ "Wallet business caller ID Spotlight query string is invalid: %@"
+ "[TUInterpreterRequest] Sign in required for %s"
+ "\\"
+ "\\\""
+ "\\\\"
+ "com.apple.TelephonyUtilities.SimulatedModeEnabledDidChange"
+ "com.apple.pkpass"
+ "globalReportUnknown"
+ "kMDItemCreator"
+ "kMDItemDisplayName"
+ "setPreviewPresentationOrientation: not available on AVCPreviewCameraSession, requested orientation: %d"
+ "v16@?0@\"NSString\"8"
+ "v24@?0@\"<TUCachedBusinessItem>\"8@\"NSError\"16"
+ "\xf0\xd1"
+ "\xf0\xf0\xf0Q"
- "%@ setSmartVoicemailActionsEnabled called %d"
- "Clearing cached current pickable routes and posting TUAudioSystemAudioPickableRoutesChanged"
- "FaceTimeServiceAvailabilityHelper: All services returned unavailable"
- "FaceTimeServiceAvailabilityHelper: Querying availability of FaceTime services for handle %@ with timeout: %s"
- "FaceTimeServiceAvailabilityHelper: Received callback indicating FaceTime is available"
- "FaceTimeServiceAvailabilityHelper: Timeout reached querying availability of FaceTime, returning false"
- "SmartVoicemailActionsEnabled"
- "\xf0\xb1"
- "\xf0\xf0\xf0A"
```
