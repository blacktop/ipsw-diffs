## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-9150.2.0.0.0
-  __TEXT.__text: 0xc106c
+9170.34.1.0.0
+  __TEXT.__text: 0xd08ec
   __TEXT.__auth_stubs: 0x1930
-  __TEXT.__objc_stubs: 0x6260
-  __TEXT.__init_offsets: 0x1280
-  __TEXT.__objc_methlist: 0x4a78
-  __TEXT.__const: 0x3dde
-  __TEXT.__gcc_except_tab: 0xd810
-  __TEXT.__cstring: 0xae25
-  __TEXT.__oslogstring: 0x37eb
-  __TEXT.__objc_methname: 0x6f19
-  __TEXT.__objc_classname: 0xb9a
-  __TEXT.__objc_methtype: 0x59a6
-  __TEXT.__unwind_info: 0x4430
-  __DATA_CONST.__auth_got: 0xca8
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x1b70
-  __DATA_CONST.__cfstring: 0x6e40
-  __DATA_CONST.__objc_classlist: 0x388
+  __TEXT.__objc_stubs: 0x7ac0
+  __TEXT.__init_offsets: 0x150c
+  __TEXT.__objc_methlist: 0x5548
+  __TEXT.__const: 0x3e2e
+  __TEXT.__gcc_except_tab: 0xe954
+  __TEXT.__cstring: 0xdc47
+  __TEXT.__oslogstring: 0x49d9
+  __TEXT.__objc_methname: 0x9067
+  __TEXT.__objc_classname: 0xbb0
+  __TEXT.__objc_methtype: 0x58b1
+  __TEXT.__unwind_info: 0x48e0
+  __DATA_CONST.__const: 0x1c78
+  __DATA_CONST.__cfstring: 0x7540
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_intobj: 0x618
+  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_intobj: 0x6a8
   __DATA_CONST.__objc_doubleobj: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x518
-  __DATA_CONST.__objc_arrayobj: 0x150
+  __DATA_CONST.__objc_arraydata: 0x508
+  __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA.__objc_const: 0x8a38
-  __DATA.__objc_selrefs: 0x1d88
-  __DATA.__objc_ivar: 0x5cc
-  __DATA.__objc_data: 0x2350
+  __DATA_CONST.__auth_got: 0xca8
+  __DATA_CONST.__got: 0x280
+  __DATA.__objc_const: 0x9e90
+  __DATA.__objc_selrefs: 0x2428
+  __DATA.__objc_ivar: 0x72c
+  __DATA.__objc_data: 0x25d0
   __DATA.__data: 0x1610
   __DATA.__bss: 0xc0
   __DATA.__common: 0x890

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9830F1B6-9B6D-35CC-B626-9995C402E9EB
-  Functions: 4763
-  Symbols:   26511
-  CStrings:  4513
+  UUID: 50D47DD8-A55A-34C8-9573-D6B8E94F778C
+  Functions: 5272
+  Symbols:   29491
+  CStrings:  5170
 
Symbols:
+ +[ActuationPlaylistManager playlistFromPlist:forRevision:]
+ +[ActuationPlaylistManager playlistFromPlist:forRevision:].cold.1
+ +[ActuationPlaylistManager playlistFromPlist:forRevision:].cold.2
+ +[ActuationPlaylistManager playlistFromV2OrV3Plist:forRevision:withPlistVersion:]
+ +[ActuationPlaylistManager playlistFromV2OrV3Plist:forRevision:withPlistVersion:].cold.1
+ +[ActuationPlaylistManager plistV3FromPlaylist:]
+ +[ActuatorDevice actuatorRevisionForService:]
+ +[ActuatorDevice deviceIDForService:]
+ +[ActuatorDevice serviceSupportsActuationLimits:]
+ +[HSTCombinedTouchModeEvent hsClassName]
+ +[HSTFrameParser parsePathCollectionPacketV2:frame:surfaceCoordinates:]
+ +[HSTFrameParser parsePathCollectionPacketV2:frame:surfaceCoordinates:].cold.1
+ +[HSTFrameParser parsePathCollectionPacketV2:frame:surfaceCoordinates:].cold.2
+ +[HSTFrameParser parsePathCollectionPacketV2:frame:surfaceCoordinates:].cold.3
+ +[HSTFrameParser parseSAPreciseContact:toContact:surfaceCoordinates:]
+ +[HSTHelpers findAncestorHIDDeviceForService:]
+ +[HSTHelpers findAncestorHIDDeviceForService:].cold.1
+ +[HSTHelpers registryPropertyForKey:fromService:]
+ +[HSTHelpers registryPropertyForKey:fromService:expectedClass:defaultValue:]
+ +[TrackpadActuatorStage serviceSupportsActuations:]
+ -[ActuationPlaylistManager .cxx_destruct]
+ -[ActuationPlaylistManager actuatorRevision]
+ -[ActuationPlaylistManager debug]
+ -[ActuationPlaylistManager initWithRevision:fwDefinedPlaylist:]
+ -[ActuationPlaylistManager overridePlaylistPlist]
+ -[ActuationPlaylistManager overridePlaylist]
+ -[ActuationPlaylistManager parameterizedWaveformForDictionary:strength:timeDilation:actuatorLimits:options:]
+ -[ActuationPlaylistManager parameterizedWaveformForID:strength:timeDilation:actuatorLimits:options:]
+ -[ActuationPlaylistManager productionPlaylistPlist]
+ -[ActuationPlaylistManager productionPlaylist]
+ -[ActuationPlaylistManager productionPlist]
+ -[ActuationPlaylistManager productionPlist].cold.1
+ -[ActuationPlaylistManager productionPlist].cold.2
+ -[ActuationPlaylistManager setActuatorRevision:]
+ -[ActuationPlaylistManager setOverridePlaylist:]
+ -[ActuationPlaylistManager setOverridePlaylistPlist:]
+ -[ActuationPlaylistManager setProductionPlaylist:]
+ -[ActuatorDevice .cxx_destruct]
+ -[ActuatorDevice actServiceMatcher]
+ -[ActuatorDevice actuateForDictionary:]
+ -[ActuatorDevice actuateForID:strength:timeDilation:]
+ -[ActuatorDevice actuatorService]
+ -[ActuatorDevice createUserClientForService:]
+ -[ActuatorDevice dataPort]
+ -[ActuatorDevice dealloc]
+ -[ActuatorDevice debug]
+ -[ActuatorDevice destoryUserClient]
+ -[ActuatorDevice deviceID]
+ -[ActuatorDevice fetchLimits]
+ -[ActuatorDevice fetchLimits].cold.1
+ -[ActuatorDevice fetchLimits].cold.2
+ -[ActuatorDevice fwDefinedPlaylist]
+ -[ActuatorDevice handedOffHostClickControl]
+ -[ActuatorDevice hidDevice]
+ -[ActuatorDevice initWithService:queue:]
+ -[ActuatorDevice limits]
+ -[ActuatorDevice openActuatorForService:]
+ -[ActuatorDevice options]
+ -[ActuatorDevice playlistManager]
+ -[ActuatorDevice queue]
+ -[ActuatorDevice revision]
+ -[ActuatorDevice setActServiceMatcher:]
+ -[ActuatorDevice setActuatorService:]
+ -[ActuatorDevice setDataPort:]
+ -[ActuatorDevice setDeviceID:]
+ -[ActuatorDevice setFwDefinedPlaylist:]
+ -[ActuatorDevice setHandedOffHostClickControl:]
+ -[ActuatorDevice setHidDevice:actuatorService:]
+ -[ActuatorDevice setHostClickControl:]
+ -[ActuatorDevice setHostClickControl:].cold.1
+ -[ActuatorDevice setLimits:]
+ -[ActuatorDevice setOptions:]
+ -[ActuatorDevice setPlaylistManager:]
+ -[ActuatorDevice setQueue:]
+ -[ActuatorDevice setRevision:]
+ -[ActuatorDevice setSupportsActuationLimits:]
+ -[ActuatorDevice setWaveform:waveform:]
+ -[ActuatorDevice setWaveform:waveform:].cold.1
+ -[ActuatorDevice setWaveform:waveform:].cold.2
+ -[ActuatorDevice supportsActuationLimits]
+ -[ActuatorDevice updateFirmwareClicks]
+ -[DeviceInfoManager .cxx_destruct]
+ -[DeviceInfoManager colorID]
+ -[DeviceInfoManager dictionary]
+ -[DeviceInfoManager fetchDeviceInfo]
+ -[DeviceInfoManager hardwareID]
+ -[DeviceInfoManager hidElementMatchingUsagePage:usage:]
+ -[DeviceInfoManager initWithService:]
+ -[DeviceInfoManager locationID]
+ -[DeviceInfoManager manufacturer]
+ -[DeviceInfoManager mtfwVersion]
+ -[DeviceInfoManager populateDeviceInfoFrom:]
+ -[DeviceInfoManager productID]
+ -[DeviceInfoManager product]
+ -[DeviceInfoManager registryNumberPropertyForKey:]
+ -[DeviceInfoManager registryPropertyForKey:]
+ -[DeviceInfoManager registryStringPropertyForKey:]
+ -[DeviceInfoManager serialNumber]
+ -[DeviceInfoManager setColorID:]
+ -[DeviceInfoManager setHardwareID:]
+ -[DeviceInfoManager setLocationID:]
+ -[DeviceInfoManager setManufacturer:]
+ -[DeviceInfoManager setMtfwVersion:]
+ -[DeviceInfoManager setProduct:]
+ -[DeviceInfoManager setProductID:]
+ -[DeviceInfoManager setSerialNumber:]
+ -[DeviceInfoManager setTransport:]
+ -[DeviceInfoManager setVendorID:]
+ -[DeviceInfoManager transport]
+ -[DeviceInfoManager vendorID]
+ -[EmbeddedTrackpadFirmwareManager _handleHostStateEvent:].cold.1
+ -[EmbeddedTrackpadFirmwareManager handleActivateEvent:]
+ -[HSRecordingStage _startRecording].cold.4
+ -[HSRecordingStage _stopRecording].cold.2
+ -[HSTBackboardBridge _handleCombinedHostState:]
+ -[HSTBackboardBridge _handleCombinedHostState:].cold.1
+ -[HSTBackboardBridge _handleCombinedHostState:].cold.2
+ -[HSTBackboardBridge _handleCombinedHostState:].cold.3
+ -[HSTBackboardBridge _handleHostState:]
+ -[HSTBackboardBridge _handleSingleHostState:]
+ -[HSTBackboardBridge initWithQueue:deviceService:log:]
+ -[HSTBackboardBridge initWithQueue:deviceService:log:].cold.1
+ -[HSTBackboardBridge initWithQueue:deviceService:log:].cold.2
+ -[HSTCombinedTouchModeEvent .cxx_destruct]
+ -[HSTCombinedTouchModeEvent initWithTouchModeMap:]
+ -[HSTCombinedTouchModeEvent setTouchModeMap:]
+ -[HSTCombinedTouchModeEvent touchModeMap]
+ -[HSTContactStabilizer initWithConfig:log:]
+ -[HSTCoreAnalyticsStage .cxx_destruct]
+ -[HSTCoreAnalyticsStage initWithLog:]
+ -[HSTFirmwareManager _handleCombinedTouchModeEvent:]
+ -[HSTFirmwareManager _handleCombinedTouchModeEvent:].cold.1
+ -[HSTFirmwareManager _handleCombinedTouchModeEvent:].cold.2
+ -[HSTFirmwareManager _handleGetDebugEvent:].cold.2
+ -[HSTFirmwareManager _setEnabledInputsReport].cold.2
+ -[HSTFirmwareManager initWithDevice:hidDeviceRouter:log:]
+ -[HSTFrameParser .cxx_destruct]
+ -[HSTFrameParser initWithConfig:log:]
+ -[HSTFrameParser parseContactFrame75:].cold.6
+ -[HSTFrameParser parseExtraPayload75:frame:]
+ -[HSTFrameParser parseExtraPayload75:frame:].cold.1
+ -[HSTFrameParser parseExtraPayload75:frame:].cold.2
+ -[HSTFrameParser parseExtraPayload75:frame:].cold.3
+ -[HSTFrameParser parseSABinary:]
+ -[HSTHIDDeviceRouter .cxx_destruct]
+ -[HSTHIDDeviceRouter _cleanup]
+ -[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:]
+ -[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:].cold.1
+ -[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:].cold.2
+ -[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:].cold.3
+ -[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:].cold.4
+ -[HSTHIDDeviceRouter _findRoutingOverrideConfigForDevice:]
+ -[HSTHIDDeviceRouter _findRoutingOverrideConfigForDevice:].cold.1
+ -[HSTHIDDeviceRouter dealloc]
+ -[HSTHIDDeviceRouter defaultHIDDevice]
+ -[HSTHIDDeviceRouter hidDeviceForReportID:]
+ -[HSTHIDDeviceRouter initWithDevice:hidDevice:queue:log:inputReportHandler:]
+ -[HSTHIDEventGenerator initWithConfig:log:]
+ -[HSTPencilVirtualService .cxx_construct]
+ -[HSTPencilVirtualService _handleSetPropertyEvent:]
+ -[HSTPencilVirtualService _handleSetPropertyEvent:].cold.1
+ -[HSTPencilVirtualService dispatchPencilEvents:]
+ -[HSTPencilVirtualService initWithConfig:withQueue:log:]
+ -[HSTPencilVirtualService initWithConfig:withQueue:log:].cold.1
+ -[HSTPencilVirtualService isVirtualServiceEnumerated]
+ -[HSTPencilVirtualService notification:withProperty:forService:].cold.1
+ -[HSTPencilVirtualService queue]
+ -[HSTPencilVirtualService setIsVirtualServiceEnumerated:]
+ -[HSTPencilVirtualService setQueue:]
+ -[HSTPencilVirtualService setShouldRecreateVirtualService:]
+ -[HSTPencilVirtualService setShouldTerminateVirtualService:]
+ -[HSTPencilVirtualService shouldRecreateVirtualService]
+ -[HSTPencilVirtualService shouldTerminateVirtualService]
+ -[HSTPhoneFirmwareManager _handleCombinedTouchModeEvent:]
+ -[HSTPhoneFirmwareManager _setAODLogging].cold.2
+ -[HSTPhoneFirmwareManager initWithDevice:hidDeviceRouter:log:]
+ -[HSTRecordingManager .cxx_destruct]
+ -[HSTRecordingManager initWithPlaybackQueue:log:]
+ -[HSTSensingAlgs _bootloaderForService:]
+ -[HSTSensingAlgs _bootloaderForService:].cold.1
+ -[HSTSensingAlgs _bootloaderForService:].cold.2
+ -[HSTSensingAlgs _bootloaderForService:].cold.3
+ -[HSTSensingAlgs _calibrationDataForKey:]
+ -[HSTSensingAlgs _calibrationDataForKey:].cold.1
+ -[HSTSensingAlgs _calibrationDataForKey:].cold.2
+ -[HSTSensingAlgs _handleConfigurationRequest:needsConfirmation:]
+ -[HSTSensingAlgs _handleConfigurationRequest:needsConfirmation:].cold.1
+ -[HSTSensingAlgs _handleDataRequest:]
+ -[HSTSensingAlgs _handleDataRequest:].cold.1
+ -[HSTSensingAlgs _handleStream:].cold.1
+ -[HSTSensingAlgs algsClass]
+ -[HSTSensingAlgs createUserDevice:platformId:]
+ -[HSTSensingAlgs createUserDevice:platformId:].cold.1
+ -[HSTSensingAlgs initWithConfig:queue:log:]
+ -[HSTSensingAlgs initWithConfig:queue:log:].cold.1
+ -[HSTSensingAlgs initWithConfig:queue:log:].cold.2
+ -[HSTSensingAlgs initWithConfig:queue:log:].cold.3
+ -[HSTSensingAlgs log]
+ -[HSTSensingAlgs saFrameworkHandle]
+ -[HSTSensingAlgs setAlgsClass:]
+ -[HSTSensingAlgs setLog:]
+ -[HSTSensingAlgs setSaFrameworkHandle:]
+ -[HSTSensingAlgs setUserDevice:]
+ -[HSTSensingAlgs userDevice]
+ -[HSTSensingAlgsConfig .cxx_destruct]
+ -[HSTSensingAlgsConfig debug]
+ -[HSTSensingAlgsConfig description]
+ -[HSTSensingAlgsConfig device]
+ -[HSTSensingAlgsConfig frameworkBundle]
+ -[HSTSensingAlgsConfig frameworkString]
+ -[HSTSensingAlgsConfig ignoredDescriptionProperties]
+ -[HSTSensingAlgsConfig interfaceClassName]
+ -[HSTSensingAlgsConfig maxPacketSize]
+ -[HSTSensingAlgsConfig personalityId]
+ -[HSTSensingAlgsConfig platformId]
+ -[HSTSensingAlgsConfig setDevice:]
+ -[HSTSensingAlgsConfig setFrameworkBundle:]
+ -[HSTSensingAlgsConfig setFrameworkString:]
+ -[HSTSensingAlgsConfig setInterfaceClassName:]
+ -[HSTSensingAlgsConfig setMaxPacketSize:]
+ -[HSTSensingAlgsConfig setPersonalityId:]
+ -[HSTSensingAlgsConfig setPlatformId:]
+ -[HSTServerStage initWithName:description:queue:log:]
+ -[HSTServerStage initWithName:description:queue:log:].cold.1
+ -[HSTServerStage initWithName:description:queue:log:].cold.2
+ -[HSTServerStage initWithName:description:queue:log:].cold.3
+ -[HSTSetPropertyEvent initWithKey:value:]
+ -[HSTSetReportEvent .cxx_construct]
+ -[HSTSetReportEvent initWithData:]
+ -[HSTSetReportEvent result]
+ -[HSTSetReportEvent setResult:]
+ -[HSTTelemetryAnalyticsStage initWithQueue:log:]
+ -[HSTTipOffsetFilter .cxx_destruct]
+ -[HSTTipOffsetFilter initWithConfig:log:]
+ -[HSTWatchFirmwareManager _handleGetWaterStateEvent:].cold.2
+ -[HSTWatchFirmwareManager _handleSetPropertyEvent:].cold.2
+ -[HSTouchHIDService _handleDisplayServiceMatched:]
+ -[HSTouchHIDService _handleWorkIntervalEvent:].cold.1
+ -[HSTouchHIDService _handleWorkIntervalEvent:].cold.2
+ -[HSTouchHIDService _handleWorkIntervalEvent:].cold.3
+ -[HSTouchHIDService _handleWorkIntervalEvent:].cold.4
+ -[HSTouchHIDService _matchDisplayServiceFrom:]
+ -[HSTouchHIDService _matchDisplayServiceFrom:].cold.1
+ -[HSTouchHIDService _matchDisplayServiceFrom:].cold.2
+ -[HSTouchHIDService _matchDisplayServiceFrom:].cold.3
+ -[HSTouchHIDService _queueHIDPencilEventsToDispatch:]
+ -[HSTouchHIDService activate].cold.13
+ -[HSTouchHIDService activate].cold.14
+ -[HSTouchHIDService activate].cold.15
+ -[HSTouchHIDService hidDeviceKeys]
+ -[HSTouchHIDService initWithService:].cold.3
+ -[MTTrackpadUberAlg algButtonStateManager]
+ -[MTTrackpadUberAlg blockingDeviceClicks]
+ -[MTTrackpadUberAlg cacheAndUpdateDeviceButtonState:currentDeviceTimestampSec:isTouching:rawButtonState:]
+ -[MTTrackpadUberAlg canDelayClicks]
+ -[MTTrackpadUberAlg debug]
+ -[MTTrackpadUberAlg dragReleaseDelayNumberOfFrames]
+ -[MTTrackpadUberAlg dragReleaseMaxDebouncedUpFrames]
+ -[MTTrackpadUberAlg setAlgButtonStateManager:]
+ -[MTTrackpadUberAlg setDragReleaseDelayNumberOfFrames:]
+ -[MTTrackpadUberAlg setDragReleaseMaxDebouncedUpFrames:]
+ -[MTTrackpadUberAlg setGesturesBlockDeviceButtonClicks:]
+ -[MTTrackpadUberAlg shouldBlockClicks]
+ -[MTTrackpadUberAlg updateClickDelayState:]
+ -[MacOSTrackpadHIDEventProcessor initWithDeviceType:]
+ -[MacTrackpadBridge initWithService:hidDevice:]
+ -[MouseBridge initWithService:hidDevice:]
+ -[PointerBridge cachedProperties]
+ -[PointerBridge cachedPropertyKeys]
+ -[PointerBridge deviceType]
+ -[PointerBridge hidDevice]
+ -[PointerBridge initWithService:hidDevice:deviceType:settings:]
+ -[PointerBridge setCachedProperties:]
+ -[PointerBridge setCachedPropertyKeys:]
+ -[PointerBridge setHidDevice:]
+ -[PointerHIDEventProcessor initWithDeviceType:]
+ -[PointerHIDEventProcessor updateMomentumStartForEvent:forSubtype:]
+ -[ServiceMatcher .cxx_destruct]
+ -[ServiceMatcher cancelMatching]
+ -[ServiceMatcher dealloc]
+ -[ServiceMatcher initWithQueue:matchingCallback:]
+ -[ServiceMatcher matchingCallback]
+ -[ServiceMatcher queue]
+ -[ServiceMatcher serviceIterator]
+ -[ServiceMatcher serviceMatchingNotificationPort]
+ -[ServiceMatcher setMatchingCallback:]
+ -[ServiceMatcher setQueue:]
+ -[ServiceMatcher setServiceIterator:]
+ -[ServiceMatcher setServiceMatchingNotificationPort:]
+ -[ServiceMatcher startMatchingWithDictionary:]
+ -[TrackpadActuatorStage actuationRequestHistory]
+ -[TrackpadActuatorStage actuatorDevice]
+ -[TrackpadActuatorStage displayState]
+ -[TrackpadActuatorStage initWithService:]
+ -[TrackpadActuatorStage service]
+ -[TrackpadActuatorStage setActuationRequestHistory:]
+ -[TrackpadActuatorStage setActuatorDevice:]
+ -[TrackpadActuatorStage setDisplayState:]
+ -[TrackpadActuatorStage setService:]
+ -[TrackpadActuatorStage setSystemActuations:]
+ -[TrackpadActuatorStage systemActuations]
+ -[TrackpadAlgButtonStateManager cacheDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:isTouching:shouldDelayDragRelease:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:hasPointerTranslation:]
+ -[TrackpadAlgButtonStateManager cachedDeviceButtonState]
+ -[TrackpadAlgButtonStateManager clearState]
+ -[TrackpadAlgButtonStateManager consecutiveButtonUpFramesDuringDrag]
+ -[TrackpadAlgButtonStateManager consecutiveDebouncedUpFramesDuringDrag]
+ -[TrackpadAlgButtonStateManager currentlyDelayingClick]
+ -[TrackpadAlgButtonStateManager currentlyDelayingDragRelease]
+ -[TrackpadAlgButtonStateManager debug]
+ -[TrackpadAlgButtonStateManager delayDownClick:until:]
+ -[TrackpadAlgButtonStateManager delayedButtonState]
+ -[TrackpadAlgButtonStateManager delayedDownClickIsQueued]
+ -[TrackpadAlgButtonStateManager delayedDownClickTimestampSec]
+ -[TrackpadAlgButtonStateManager delayedDragReleaseButtonState]
+ -[TrackpadAlgButtonStateManager downClickDelaySec]
+ -[TrackpadAlgButtonStateManager fwDeviceButtonState]
+ -[TrackpadAlgButtonStateManager handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:]
+ -[TrackpadAlgButtonStateManager handleDragReleaseDelay:currentDeviceButtonState:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:]
+ -[TrackpadAlgButtonStateManager init]
+ -[TrackpadAlgButtonStateManager manageDragReleaseDelay:currentDeviceButtonState:rawButtonState:shouldDelayDragRelease:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:]
+ -[TrackpadAlgButtonStateManager newClickBlockedDueToExistingDelay]
+ -[TrackpadAlgButtonStateManager resetDragReleaseDelayState:]
+ -[TrackpadAlgButtonStateManager setCachedDeviceButtonState:]
+ -[TrackpadAlgButtonStateManager setConsecutiveButtonUpFramesDuringDrag:]
+ -[TrackpadAlgButtonStateManager setConsecutiveDebouncedUpFramesDuringDrag:]
+ -[TrackpadAlgButtonStateManager setCurrentlyDelayingClick:]
+ -[TrackpadAlgButtonStateManager setCurrentlyDelayingDragRelease:]
+ -[TrackpadAlgButtonStateManager setDelayedButtonState:]
+ -[TrackpadAlgButtonStateManager setDelayedDownClickTimestampSec:]
+ -[TrackpadAlgButtonStateManager setDelayedDragReleaseButtonState:]
+ -[TrackpadAlgButtonStateManager setFwDeviceButtonState:]
+ -[TrackpadAlgButtonStateManager setNewClickBlockedDueToExistingDelay:]
+ -[TrackpadAlgButtonStateManager setTranslationOccurredDuringClick:]
+ -[TrackpadAlgButtonStateManager setUpClickOccuredDuringDelay:]
+ -[TrackpadAlgButtonStateManager translationOccurredDuringClick]
+ -[TrackpadAlgButtonStateManager upClickOccuredDuringDelay]
+ -[TrackpadAlgButtonStateManager updateCachedButtonState:currentDeviceTimestampSec:isTouching:]
+ -[TrackpadAlgButtonStateManager updateFwButtonStateTo:]
+ -[TrackpadAlgButtonStateManager updateTranslationTracking:hasPointerTranslation:]
+ -[TrackpadAlgStage gesturesBlockDeviceButtonClicks]
+ -[TrackpadAlgStage hostClickEnabled]
+ -[TrackpadAlgStage rawDeviceButtonState]
+ -[TrackpadAlgStage sanitizedDeviceButtonState]
+ -[TrackpadAlgStage setGesturesBlockDeviceButtonClicks:]
+ -[TrackpadAlgStage setHostClickEnabled:]
+ -[TrackpadAlgStage setRawDeviceButtonState:]
+ -[TrackpadAlgStage setSanitizedDeviceButtonState:]
+ -[TrackpadBridge initWithService:hidDevice:]
+ -[TrackpadDeadzoneManager .cxx_destruct]
+ -[TrackpadDeadzoneManager active]
+ -[TrackpadDeadzoneManager debug]
+ -[TrackpadDeadzoneManager handleConsume:]
+ -[TrackpadDeadzoneManager handleContactFrame:]
+ -[TrackpadDeadzoneManager handleGetDebugEvent:]
+ -[TrackpadDeadzoneManager handleResetEvent:]
+ -[TrackpadDeadzoneManager handleSetPropertyEvent:]
+ -[TrackpadDeadzoneManager initWithConfig:]
+ -[TrackpadDeadzoneManager isContactInDeadzone:]
+ -[TrackpadDeadzoneManager setDeadzoneContacts:]
+ -[TrackpadDeadzoneManager setEnabled:]
+ -[TrackpadDeadzoneManager updateArtificialSurfaceSize]
+ -[TrackpadFirmwareManager _setReportIntervalUs:].cold.1
+ -[TrackpadFirmwareManager criticalErrors].cold.1
+ -[TrackpadFirmwareManager deviceInfoManager]
+ -[TrackpadFirmwareManager handleCancelEvent:]
+ -[TrackpadFirmwareManager handleGetPropertyEvent:]
+ -[TrackpadFirmwareManager hidDevice]
+ -[TrackpadFirmwareManager initWithService:hidDevice:]
+ -[TrackpadFirmwareManager mtfwScanRate].cold.1
+ -[TrackpadFirmwareManager queue]
+ -[TrackpadFirmwareManager service]
+ -[TrackpadFirmwareManager setDeviceInfoManager:]
+ -[TrackpadFirmwareManager setMouseButtonMode:buttonDivision:].cold.1
+ -[TrackpadFirmwareManager setQueue:]
+ -[TrackpadHIDEventProcessor handleSetPropertyEvent:]
+ -[TrackpadHIDEventProcessor initWithDeviceType:]
+ -[TrackpadHIDEventProcessor setDeviceID:]
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Contact.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTBackboardBridge.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCREventGenerator.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCircularBuffer.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTContactStabilizer.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCoreAnalytics.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTEvent.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame+Python.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrameParser.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventGenerator.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventStatistics.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEvents.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHelpers.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPencilVirtualService.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPipeline_vers.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTRecordingManager.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTSensingAlgs.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTServerStage.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTTipOffsetFilter.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Types.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTActionEvent_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCyclingTrackpad_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCycling_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordGestureSet_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordIntegrating_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordTable_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerEllipseTip_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerToPathMap_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceBehavior_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceConfig.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceFilter_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceManagement_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceThresholding_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTGestureConfig_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHIDEventAppend.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandMotion_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandStatistics_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPListGestureConfig_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParameterFactory_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParserPath_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPathStates_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTRestZoneIntegrator_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSlideGesture_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSurfaceDimensions_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTapDragManager_.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTrackpadUberAlg.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(TrackpadAlgButtonStateManager.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(USBKey.o)
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTPipeline.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationMultipliers.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationPlaylistManager.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationTone.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationWaveform.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorDevice.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorLimits.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/DeviceInfoManager.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadFirmwareManager.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSMousePipelineCreation.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTFirmwareManager.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTHIDDeviceRouter.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTPipelineCreation.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTSAPipelineCreation.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTTelemetryAnalyticsStage.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService_vers.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadDefs.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadPipelineCreation.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTGestureConfigGenerator.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPluginLogging.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPreferences.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacOSTrackpadHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacTrackpadBridge.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MomentumCurve.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MouseBridge.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PeppyHIDService.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerBridge.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerSettings.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ServiceMatcher.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadActuatorStage.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadAlgStage.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadBridge.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadDeadzoneManager.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadFirmwareManager.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadMomentumGeneratorStage.o
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/HIDSensingTouch/HSTPipeline/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/HIDSensingTouch/HSTPipeline/Helpers/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/TrackpadActuatorStage/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/FirmwareManagers/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/Plugin/
+ /Library/Caches/com.apple.xbs/1893992F-722F-46C7-BDD1-8CA0A27C45FB/TemporaryDirectory.8ZYaRe/Sources/Multitouch/Plugin/Parser/
+ ActuationPlaylistManager.mm
+ ActuatorDevice.mm
+ DeviceInfoManager.mm
+ GCC_except_table103
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table126
+ GCC_except_table141
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table197
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table229
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table291
+ GCC_except_table301
+ GCC_except_table315
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table336
+ GCC_except_table341
+ GCC_except_table356
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table366
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table380
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table395
+ GCC_except_table400
+ GCC_except_table412
+ GCC_except_table83
+ GCC_except_table96
+ HSTHIDDeviceRouter.mm
+ HSTHelpers.mm
+ OBJC_IVAR_$_ActuationPlaylistManager._actuatorRevision
+ OBJC_IVAR_$_ActuationPlaylistManager._overridePlaylist
+ OBJC_IVAR_$_ActuationPlaylistManager._productionPlaylist
+ OBJC_IVAR_$_ActuatorDevice._actServiceMatcher
+ OBJC_IVAR_$_ActuatorDevice._actuatorService
+ OBJC_IVAR_$_ActuatorDevice._dataPort
+ OBJC_IVAR_$_ActuatorDevice._deviceID
+ OBJC_IVAR_$_ActuatorDevice._fwDefinedPlaylist
+ OBJC_IVAR_$_ActuatorDevice._handedOffHostClickControl
+ OBJC_IVAR_$_ActuatorDevice._hidDevice
+ OBJC_IVAR_$_ActuatorDevice._limits
+ OBJC_IVAR_$_ActuatorDevice._options
+ OBJC_IVAR_$_ActuatorDevice._playlistManager
+ OBJC_IVAR_$_ActuatorDevice._queue
+ OBJC_IVAR_$_ActuatorDevice._revision
+ OBJC_IVAR_$_ActuatorDevice._supportsActuationLimits
+ OBJC_IVAR_$_DeviceInfoManager._colorID
+ OBJC_IVAR_$_DeviceInfoManager._hardwareID
+ OBJC_IVAR_$_DeviceInfoManager._locationID
+ OBJC_IVAR_$_DeviceInfoManager._manufacturer
+ OBJC_IVAR_$_DeviceInfoManager._mtfwVersion
+ OBJC_IVAR_$_DeviceInfoManager._product
+ OBJC_IVAR_$_DeviceInfoManager._productID
+ OBJC_IVAR_$_DeviceInfoManager._serialNumber
+ OBJC_IVAR_$_DeviceInfoManager._service
+ OBJC_IVAR_$_DeviceInfoManager._transport
+ OBJC_IVAR_$_DeviceInfoManager._vendorID
+ OBJC_IVAR_$_HSTBackboardBridge._digitizerID
+ OBJC_IVAR_$_HSTBackboardBridge._disableTTW
+ OBJC_IVAR_$_HSTBackboardBridge._hostStateFormatVersion
+ OBJC_IVAR_$_HSTBackboardBridge._log
+ OBJC_IVAR_$_HSTCombinedTouchModeEvent._touchModeMap
+ OBJC_IVAR_$_HSTContactStabilizer._log
+ OBJC_IVAR_$_HSTCoreAnalyticsStage._log
+ OBJC_IVAR_$_HSTFirmwareManager._hidDevice
+ OBJC_IVAR_$_HSTFirmwareManager._hidDeviceRouter
+ OBJC_IVAR_$_HSTFirmwareManager._log
+ OBJC_IVAR_$_HSTFirmwareManager._reportIDDenyList
+ OBJC_IVAR_$_HSTFrameParser._log
+ OBJC_IVAR_$_HSTHIDDeviceRouter._defaultHIDDevice
+ OBJC_IVAR_$_HSTHIDDeviceRouter._hidManager
+ OBJC_IVAR_$_HSTHIDDeviceRouter._inputReportHandler
+ OBJC_IVAR_$_HSTHIDDeviceRouter._log
+ OBJC_IVAR_$_HSTHIDDeviceRouter._overrideReportIDs
+ OBJC_IVAR_$_HSTHIDDeviceRouter._proxyDevice
+ OBJC_IVAR_$_HSTHIDEventGenerator._log
+ OBJC_IVAR_$_HSTPencilVirtualService._isVirtualServiceEnumerated
+ OBJC_IVAR_$_HSTPencilVirtualService._log
+ OBJC_IVAR_$_HSTPencilVirtualService._queue
+ OBJC_IVAR_$_HSTPencilVirtualService._shouldRecreateVirtualService
+ OBJC_IVAR_$_HSTPencilVirtualService._shouldTerminateVirtualService
+ OBJC_IVAR_$_HSTRecordingManager._log
+ OBJC_IVAR_$_HSTSensingAlgs._algsClass
+ OBJC_IVAR_$_HSTSensingAlgs._log
+ OBJC_IVAR_$_HSTSensingAlgs._saFrameworkHandle
+ OBJC_IVAR_$_HSTSensingAlgs._userDevice
+ OBJC_IVAR_$_HSTSensingAlgsConfig._device
+ OBJC_IVAR_$_HSTSensingAlgsConfig._frameworkBundle
+ OBJC_IVAR_$_HSTSensingAlgsConfig._frameworkString
+ OBJC_IVAR_$_HSTSensingAlgsConfig._interfaceClassName
+ OBJC_IVAR_$_HSTSensingAlgsConfig._maxPacketSize
+ OBJC_IVAR_$_HSTSensingAlgsConfig._personalityId
+ OBJC_IVAR_$_HSTSensingAlgsConfig._platformId
+ OBJC_IVAR_$_HSTServerStage._log
+ OBJC_IVAR_$_HSTSetReportEvent._result
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._log
+ OBJC_IVAR_$_HSTTipOffsetFilter._log
+ OBJC_IVAR_$_HSTouchHIDService._displayServiceCondition
+ OBJC_IVAR_$_MTTrackpadUberAlg._algButtonStateManager
+ OBJC_IVAR_$_MTTrackpadUberAlg._blockingDeviceClicks
+ OBJC_IVAR_$_MTTrackpadUberAlg._dragReleaseDelayNumberOfFrames
+ OBJC_IVAR_$_MTTrackpadUberAlg._dragReleaseMaxDebouncedUpFrames
+ OBJC_IVAR_$_MTTrackpadUberAlg._gesturesBlockDeviceButtonClicks
+ OBJC_IVAR_$_MTTrackpadUberAlg._hasPointerTranslationThisFrame
+ OBJC_IVAR_$_MTTrackpadUberAlg._shouldDelayClick
+ OBJC_IVAR_$_PointerBridge._cachedProperties
+ OBJC_IVAR_$_PointerBridge._cachedPropertyKeys
+ OBJC_IVAR_$_PointerBridge._deviceType
+ OBJC_IVAR_$_PointerBridge._hidDevice
+ OBJC_IVAR_$_ServiceMatcher._matchingCallback
+ OBJC_IVAR_$_ServiceMatcher._queue
+ OBJC_IVAR_$_ServiceMatcher._serviceIterator
+ OBJC_IVAR_$_ServiceMatcher._serviceMatchingNotificationPort
+ OBJC_IVAR_$_TrackpadActuatorStage._actuatorDevice
+ OBJC_IVAR_$_TrackpadActuatorStage._service
+ OBJC_IVAR_$_TrackpadActuatorStage._systemActuations
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._cachedDeviceButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._consecutiveButtonUpFramesDuringDrag
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._consecutiveDebouncedUpFramesDuringDrag
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._currentlyDelayingClick
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._currentlyDelayingDragRelease
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._delayedButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._delayedDownClickTimestampSec
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._delayedDragReleaseButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._downClickDelaySec
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._fwDeviceButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._newClickBlockedDueToExistingDelay
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._translationOccurredDuringClick
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._upClickOccuredDuringDelay
+ OBJC_IVAR_$_TrackpadAlgStage._gesturesBlockDeviceButtonClicks
+ OBJC_IVAR_$_TrackpadAlgStage._rawDeviceButtonState
+ OBJC_IVAR_$_TrackpadAlgStage._sanitizedDeviceButtonState
+ OBJC_IVAR_$_TrackpadDeadzoneManager._actualConfig
+ OBJC_IVAR_$_TrackpadDeadzoneManager._artificialSurfaceSize
+ OBJC_IVAR_$_TrackpadDeadzoneManager._bottomDeadzonePercentage
+ OBJC_IVAR_$_TrackpadDeadzoneManager._builtIn
+ OBJC_IVAR_$_TrackpadDeadzoneManager._deadzoneContacts
+ OBJC_IVAR_$_TrackpadDeadzoneManager._enabled
+ OBJC_IVAR_$_TrackpadDeadzoneManager._leftDeadzonePercentage
+ OBJC_IVAR_$_TrackpadDeadzoneManager._rightDeadzonePercentage
+ OBJC_IVAR_$_TrackpadDeadzoneManager._topDeadzonePercentage
+ OBJC_IVAR_$_TrackpadFirmwareManager._deviceInfoManager
+ OBJC_IVAR_$_TrackpadFirmwareManager._hidDevice
+ OBJC_IVAR_$_TrackpadFirmwareManager._queue
+ OBJC_IVAR_$_TrackpadFirmwareManager._service
+ ServiceMatcher.mm
+ TrackpadAlgButtonStateManager.mm
+ TrackpadDeadzoneManager.mm
+ _IOConnectCallScalarMethod
+ _IOObjectConformsTo
+ _IOObjectRetain
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryFromPath
+ _IORegistryEntryGetProperty
+ _IOServiceOpen
+ _IOServiceWaitQuiet
+ _MGGetSInt32Answer
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_ActuationPlaylistManager
+ _OBJC_CLASS_$_ActuatorDevice
+ _OBJC_CLASS_$_DeviceInfoManager
+ _OBJC_CLASS_$_HIDDevice
+ _OBJC_CLASS_$_HIDEventService
+ _OBJC_CLASS_$_HIDUserDevice
+ _OBJC_CLASS_$_HSTCombinedTouchModeEvent
+ _OBJC_CLASS_$_HSTHIDDeviceRouter
+ _OBJC_CLASS_$_HSTHelpers
+ _OBJC_CLASS_$_HSTSensingAlgsConfig
+ _OBJC_CLASS_$_MTAHTSupport
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_ServiceMatcher
+ _OBJC_CLASS_$_TrackpadAlgButtonStateManager
+ _OBJC_CLASS_$_TrackpadDeadzoneManager
+ _OBJC_METACLASS_$_ActuationPlaylistManager
+ _OBJC_METACLASS_$_ActuatorDevice
+ _OBJC_METACLASS_$_DeviceInfoManager
+ _OBJC_METACLASS_$_HSTCombinedTouchModeEvent
+ _OBJC_METACLASS_$_HSTHIDDeviceRouter
+ _OBJC_METACLASS_$_HSTHelpers
+ _OBJC_METACLASS_$_HSTSensingAlgsConfig
+ _OBJC_METACLASS_$_ServiceMatcher
+ _OBJC_METACLASS_$_TrackpadAlgButtonStateManager
+ _OBJC_METACLASS_$_TrackpadDeadzoneManager
+ _ZL17setReportWithDataP18HSTHIDDeviceRouterP6NSDataP5NSSet.cold.1
+ _ZL34touchModeFromHostStateNotificationP12NSDictionaryb.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport13EnabledInputs5AwakeEEvP9HIDDeviceRKT_P5NSSet.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport13EnabledInputs5AwakeEEvP9HIDDeviceRKT_P5NSSet.cold.2
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17FaceDetectionModeEEvP9HIDDeviceRKT_P5NSSet.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17FaceDetectionModeEEvP9HIDDeviceRKT_P5NSSet.cold.2
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17HostInterruptModeEEvP9HIDDeviceRKT_P5NSSet.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17HostInterruptModeEEvP9HIDDeviceRKT_P5NSSet.cold.2
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport23HostNotificationControlEEvP9HIDDeviceRKT_P5NSSet.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport23HostNotificationControlEEvP9HIDDeviceRKT_P5NSSet.cold.2
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport8DataModeEEvP9HIDDeviceRKT_P5NSSet.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport8DataModeEEvP9HIDDeviceRKT_P5NSSet.cold.2
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport9HostEventEEvP9HIDDeviceRKT_P5NSSet.cold.1
+ _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport9HostEventEEvP9HIDDeviceRKT_P5NSSet.cold.2
+ _ZN11HSTPipeline12FirmwareUtilL13GetReportDataEP9HIDDevicehP13NSMutableData.cold.1
+ _ZN11HSTPipeline12FirmwareUtilL13SetReportDataEP9HIDDeviceP6NSData.cold.1
+ _ZN11HSTPipeline12FirmwareUtilL13SetReportDataEP9HIDDeviceP6NSData.cold.2
+ _ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.1
+ _ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.2
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.1
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.2
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.3
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.4
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.5
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.6
+ _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem.cold.7
+ _ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.1
+ _ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.2
+ _ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.3
+ _ZN11HSTPipeline22CreateTrackpadPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.1
+ _ZN11HSTPipeline22CreateTrackpadPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage.cold.2
+ _ZN11HSTPipelineL19loadFrameworkBundleEP8NSString.cold.1
+ _ZN11HSTPipelineL19loadFrameworkBundleEP8NSString.cold.2
+ _ZN11HSTPipelineL26createConfigFromDictionaryEP12NSDictionaryP10__MTDevicem.cold.1
+ _ZN11HSTPipelineL26createConfigFromDictionaryEP12NSDictionaryP10__MTDevicem.cold.2
+ _ZN17InstabilityFilter6updateExRKN11HSTPipeline7ContactEb.cold.1
+ _ZNK17InstabilityFilter12_timeInRangeEv.cold.2
+ _ZNK17InstabilityFilter19_timeSinceLastFrameEv.cold.1
+ _ZNK17InstabilityFilter19_timeSinceLastFrameEv.cold.2
+ __36-[DeviceInfoManager fetchDeviceInfo]_block_invoke.39
+ __53-[HSTServerStage initWithName:description:queue:log:]_block_invoke.cold.1
+ __53-[HSTServerStage initWithName:description:queue:log:]_block_invoke.cold.2
+ __54-[HSTBackboardBridge initWithQueue:deviceService:log:]_block_invoke.38
+ __54-[HSTBackboardBridge initWithQueue:deviceService:log:]_block_invoke.40
+ __54-[HSTBackboardBridge initWithQueue:deviceService:log:]_block_invoke.42
+ __63-[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:]_block_invoke.cold.1
+ __Block_byref_object_copy_.470
+ __Block_byref_object_dispose_.471
+ __OBJC_$_CLASS_METHODS_ActuationPlaylistManager
+ __OBJC_$_CLASS_METHODS_ActuatorDevice
+ __OBJC_$_CLASS_METHODS_HSTCombinedTouchModeEvent
+ __OBJC_$_CLASS_METHODS_HSTFrameParser
+ __OBJC_$_CLASS_METHODS_HSTHelpers
+ __OBJC_$_CLASS_METHODS_TrackpadActuatorStage
+ __OBJC_$_INSTANCE_METHODS_ActuationPlaylistManager
+ __OBJC_$_INSTANCE_METHODS_ActuatorDevice
+ __OBJC_$_INSTANCE_METHODS_DeviceInfoManager
+ __OBJC_$_INSTANCE_METHODS_HSTCombinedTouchModeEvent
+ __OBJC_$_INSTANCE_METHODS_HSTHIDDeviceRouter
+ __OBJC_$_INSTANCE_METHODS_HSTSensingAlgsConfig
+ __OBJC_$_INSTANCE_METHODS_ServiceMatcher
+ __OBJC_$_INSTANCE_METHODS_TrackpadAlgButtonStateManager
+ __OBJC_$_INSTANCE_METHODS_TrackpadDeadzoneManager
+ __OBJC_$_INSTANCE_VARIABLES_ActuationPlaylistManager
+ __OBJC_$_INSTANCE_VARIABLES_ActuatorDevice
+ __OBJC_$_INSTANCE_VARIABLES_DeviceInfoManager
+ __OBJC_$_INSTANCE_VARIABLES_HSTCombinedTouchModeEvent
+ __OBJC_$_INSTANCE_VARIABLES_HSTCoreAnalyticsStage
+ __OBJC_$_INSTANCE_VARIABLES_HSTHIDDeviceRouter
+ __OBJC_$_INSTANCE_VARIABLES_HSTSensingAlgsConfig
+ __OBJC_$_INSTANCE_VARIABLES_ServiceMatcher
+ __OBJC_$_INSTANCE_VARIABLES_TrackpadAlgButtonStateManager
+ __OBJC_$_INSTANCE_VARIABLES_TrackpadDeadzoneManager
+ __OBJC_$_PROP_LIST_ActuationPlaylistManager
+ __OBJC_$_PROP_LIST_ActuatorDevice
+ __OBJC_$_PROP_LIST_DeviceInfoManager
+ __OBJC_$_PROP_LIST_HSTCombinedTouchModeEvent
+ __OBJC_$_PROP_LIST_HSTHIDDeviceRouter
+ __OBJC_$_PROP_LIST_HSTSensingAlgsConfig
+ __OBJC_$_PROP_LIST_ServiceMatcher
+ __OBJC_$_PROP_LIST_TrackpadAlgButtonStateManager
+ __OBJC_CLASS_RO_$_ActuationPlaylistManager
+ __OBJC_CLASS_RO_$_ActuatorDevice
+ __OBJC_CLASS_RO_$_DeviceInfoManager
+ __OBJC_CLASS_RO_$_HSTCombinedTouchModeEvent
+ __OBJC_CLASS_RO_$_HSTHIDDeviceRouter
+ __OBJC_CLASS_RO_$_HSTHelpers
+ __OBJC_CLASS_RO_$_HSTSensingAlgsConfig
+ __OBJC_CLASS_RO_$_ServiceMatcher
+ __OBJC_CLASS_RO_$_TrackpadAlgButtonStateManager
+ __OBJC_CLASS_RO_$_TrackpadDeadzoneManager
+ __OBJC_METACLASS_RO_$_ActuationPlaylistManager
+ __OBJC_METACLASS_RO_$_ActuatorDevice
+ __OBJC_METACLASS_RO_$_DeviceInfoManager
+ __OBJC_METACLASS_RO_$_HSTCombinedTouchModeEvent
+ __OBJC_METACLASS_RO_$_HSTHIDDeviceRouter
+ __OBJC_METACLASS_RO_$_HSTHelpers
+ __OBJC_METACLASS_RO_$_HSTSensingAlgsConfig
+ __OBJC_METACLASS_RO_$_ServiceMatcher
+ __OBJC_METACLASS_RO_$_TrackpadAlgButtonStateManager
+ __OBJC_METACLASS_RO_$_TrackpadDeadzoneManager
+ __ZGVN6HSUtil8CoderKey7LiteralIJLc72ELc83ELc84ELc67ELc111ELc109ELc98ELc105ELc110ELc101ELc100ELc84ELc111ELc117ELc99ELc104ELc77ELc111ELc100ELc101ELc69ELc118ELc101ELc110ELc116EEE3KeyE
+ __ZL12allowsReporthP5NSSet
+ __ZL14staticCallbackPvj
+ __ZL17setReportWithDataP18HSTHIDDeviceRouterP6NSDataP5NSSet
+ __ZL25createEnabledInputsReportjN11HSTPipeline17ScreenOrientationE
+ __ZL30_displayServiceMatchedCallbackPvj
+ __ZL34touchModeFromHostStateNotificationP12NSDictionaryb
+ __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport13EnabledInputs5AwakeEEvP9HIDDeviceRKT_P5NSSet
+ __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17FaceDetectionModeEEvP9HIDDeviceRKT_P5NSSet
+ __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17HostInterruptModeEEvP9HIDDeviceRKT_P5NSSet
+ __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport23HostNotificationControlEEvP9HIDDeviceRKT_P5NSSet
+ __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport8DataModeEEvP9HIDDeviceRKT_P5NSSet
+ __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport9HostEventEEvP9HIDDeviceRKT_P5NSSet
+ __ZN10HSPipeline9FindStageI23HSTPencilVirtualServiceEEPT_P7HSStage
+ __ZN11HSTPipeline10SensorSize11fromServiceEj
+ __ZN11HSTPipeline11SurfaceSize11fromServiceEj
+ __ZN11HSTPipeline12FirmwareUtilL13GetReportDataEP9HIDDevicehP13NSMutableData
+ __ZN11HSTPipeline12FirmwareUtilL13SetReportDataEP9HIDDeviceP6NSData
+ __ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage
+ __ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem
+ __ZN11HSTPipeline18SurfaceCoordinates11fromServiceEj
+ __ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage
+ __ZN11HSTPipeline22CreateTrackpadPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectjP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage
+ __ZN11HSTPipelineL19loadFrameworkBundleEP8NSString
+ __ZN11HSTPipelineL26createConfigFromDictionaryEP12NSDictionaryP10__MTDevicem
+ __ZN13MTHandMotion_C1ERK20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptions14MTHandIdentityPKc
+ __ZN13MTHandMotion_C2ERK20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptions14MTHandIdentityPKc
+ __ZN13MTParserPath_C1EN11HSTPipeline10DeviceTypeE
+ __ZN13MTParserPath_C2EN11HSTPipeline10DeviceTypeE
+ __ZN13MTPathStates_34setRestingThumbFromPalmRestingHandEi
+ __ZN13MTPathStates_C1ERK20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptionsbj
+ __ZN13MTPathStates_C2ERK20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptionsbj
+ __ZN14SABinaryParser13parseRunFrameEPFbPvRK19_SABinaryInjExtDataEPFbS0_RK21_SABinaryInjExtPacketPKhESC_
+ __ZN14SABinaryParser15parseInjExtDataEPFbPvRK21_SABinaryInjExtPacketPKhES7_PFbS0_RK20_SABinaryInjExtPointE
+ __ZN15MTChordCycling_C1E14MTHandIdentityPcR24MTDragManagerEventQueue_bN11HSTPipeline10DeviceTypeE
+ __ZN15MTChordCycling_C2E14MTHandIdentityPcR24MTDragManagerEventQueue_bN11HSTPipeline10DeviceTypeE
+ __ZN16MTForceBehavior_26isThresholdLadderMonotonicERKNSt3__16vectorIfNS0_9allocatorIfEEEE
+ __ZN16MTGestureConfig_C2EN11HSTPipeline10DeviceTypeEbR24MTDragManagerEventQueue_
+ __ZN17MTHandStatistics_C1E14MTHandIdentityPcN11HSTPipeline10DeviceTypeE15MTParserOptions
+ __ZN18MTForceManagement_22constructThresholdInfoEiiRK13MTPathStates_13MTForceEvent_
+ __ZN18MTForceManagement_25setBehaviorOnThresholdersERK16MTForceBehavior_ii
+ __ZN18MTForceManagement_26setClickStrengthPreferenceE15MTClickStrength
+ __ZN18MTForceManagement_36setBehaviorOnOtherFingerThresholdersERK16MTForceBehavior_i
+ __ZN18MTForceManagement_C1EU13block_pointerFviffE
+ __ZN18MTForceManagement_C2EU13block_pointerFviffE
+ __ZN19MTParameterFactory_19initTouchZoneParamsER22MTTouchZoneParameters_N11HSTPipeline10DeviceTypeEb
+ __ZN19MTParameterFactory_20initPathFilterParamsER23MTPathFilterParameters_N11HSTPipeline10DeviceTypeE15MTParserOptionsbRK20MTSurfaceDimensions_j
+ __ZN19MTParameterFactory_21initForceFilterParamsER24MTForceFilterParameters_
+ __ZN19MTParameterFactory_22initChordCyclingParamsER25MTChordCyclingParameters_N11HSTPipeline10DeviceTypeE
+ __ZN19MTParameterFactory_25initFingerTipOffsetParamsER30MTHMFingerTipOffsetParameters_N11HSTPipeline10DeviceTypeE15MTParserOptionsb
+ __ZN19MTParameterFactory_26initMotionExtractionParamsER29MTMotionExtractionParameters_
+ __ZN21MTPListGestureConfig_C1EN11HSTPipeline10DeviceTypeEbR24MTDragManagerEventQueue_
+ __ZN21MTRestZoneIntegrator_C1ERK20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptions
+ __ZN21MTRestZoneIntegrator_C2ERK20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptions
+ __ZN23MTChordCyclingTrackpad_C1E14MTHandIdentityPcR24MTDragManagerEventQueue_bN11HSTPipeline10DeviceTypeE
+ __ZN6HSUtil11DynamicCastI29HSTWirelessChargingStateEventEEPT_P11objc_object
+ __ZN6HSUtil7Encoder20_encodeKeyTableStartEv
+ __ZN6HSUtil8CoderKey7LiteralIJLc72ELc83ELc84ELc67ELc111ELc109ELc98ELc105ELc110ELc101ELc100ELc84ELc111ELc117ELc99ELc104ELc77ELc111ELc100ELc101ELc69ELc118ELc101ELc110ELc116EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc72ELc83ELc84ELc67ELc111ELc109ELc98ELc105ELc110ELc101ELc100ELc84ELc111ELc117ELc99ELc104ELc77ELc111ELc100ELc101ELc69ELc118ELc101ELc110ELc116EEE4_StrE
+ __ZNK17InstabilityFilter19_timeSinceLastFrameEv
+ __ZNKSt3__111__copy_implclB9foe220100IPNS_6vectorIiNS_9allocatorIiEEEES6_S6_Li0EEENS_4pairIT_T1_EES8_T0_S9_
+ __ZNKSt3__111__copy_implclB9foe220100IPU8__strongP8HIDEventS5_S5_Li0EEENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9fqe220100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqe220100EPKvm
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI15MTSlideGesture_EEPS2_EclB9foe220100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI16MTForceBehavior_EEPS2_EclB9foe220100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18MTChordGestureSet_EEPS2_EclB9foe220100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIiNS1_IiEEEEEEPS4_EclB9foe220100Ev
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9fqe220100ERKS6_S9_
+ __ZNKSt3__18equal_toIU6__weakPU26objcproto15HSPreferencable7HSStageEclB9fqe220100ERU6__weakKS3_S7_
+ __ZNKSt3__18equal_toIU6__weakPU26objcproto15HSStageObserver11objc_objectEclB9fqe220100ERU6__weakKS2_S6_
+ __ZNKSt9type_infoeqB9fqe220100ERKS_
+ __ZNSt12length_errorC1B9foe220100EPKc
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12out_of_rangeC1B9foe220100EPKc
+ __ZNSt19bad_optional_accessD1Ev
+ __ZNSt3__110__function12__value_funcIFN6HSUtil6BufferENS_10shared_ptrINS2_10ConnectionEEEOS3_EE4swapB9fqe220100ERS9_
+ __ZNSt3__110__function12__value_funcIFN6HSUtil6BufferENS_10shared_ptrINS2_10ConnectionEEEOS3_EEC2B9fqe220100ERKS9_
+ __ZNSt3__110__function12__value_funcIFN6HSUtil6BufferENS_10shared_ptrINS2_10ConnectionEEEOS3_EED2B9fqe220100Ev
+ __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEE4swapB9fqe220100ERSB_
+ __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEEC2B9fqe220100ERKSB_
+ __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEED2B9fqe220100Ev
+ __ZNSt3__110__function12__value_funcIFbRN6HSUtil7EncoderEP11objc_objectEE4swapB9fqe220100ERS8_
+ __ZNSt3__110__function12__value_funcIFbRN6HSUtil7EncoderEP11objc_objectEEC2B9fqe220100ERKS8_
+ __ZNSt3__110__function12__value_funcIFbRN6HSUtil7EncoderEP11objc_objectEED2B9fqe220100Ev
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI8HSMapperEEEE4swapB9fqe220100ERS6_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI8HSMapperEEEEC2B9fqe220100ERKS6_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI8HSMapperEEEED2B9fqe220100Ev
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN6HSUtil10ConnectionEEEEE4swapB9fqe220100ERS7_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN6HSUtil10ConnectionEEEEEC2B9fqe220100ERKS7_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN6HSUtil10ConnectionEEEEED2B9fqe220100Ev
+ __ZNSt3__110shared_ptrI8HSMapperEC2B9fqe220100IS1_Li0EEEPT_
+ __ZNSt3__110shared_ptrIN6HSUtil10ConnectionEEC2B9fqe220100IS2_Li0EEEPT_
+ __ZNSt3__110unique_ptrI8HSMapperNS_14default_deleteIS1_EEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrIN6HSUtil10ConnectionENS_14default_deleteIS2_EEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS2_EEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrIN6HSUtil7Decoder9CallbacksENS_14default_deleteIS3_EEE5resetB9foe220100EPS3_
+ __ZNSt3__110unique_ptrIN6HSUtil7Decoder9CallbacksENS_14default_deleteIS3_EEE5resetB9fqe220100EPS3_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP11objc_objectyEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP11objc_objectEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP7HSProxyEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeIU6__weakPU26objcproto15HSPreferencable7HSStagePvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeIU6__weakPU26objcproto15HSStageObserver11objc_objectPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeIU8__strongP7HSStagePvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9fqe220100Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN6HSUtil10Connection5startEvEUlvE_EEENS3_IS9_EEED1B9fqe220100Ev
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ER26MTPointVelocityGreaterThanP7MTPointEEvT2_OT1_NS_15iterator_traitsIS6_E15difference_typeESB_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_7greaterIfEEPfEEvT2_OT1_NS_15iterator_traitsIS6_E15difference_typeESB_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_7greaterIiEEPiEEvT2_OT1_NS_15iterator_traitsIS6_E15difference_typeESB_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb1ERNS_7greaterIfEEPfEEvT2_OT1_NS_15iterator_traitsIS6_E15difference_typeESB_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb1ERNS_7greaterIiEEPiEEvT2_OT1_NS_15iterator_traitsIS6_E15difference_typeESB_
+ __ZNSt3__111unique_lockINS_5mutexEE4lockB9fqe220100Ev
+ __ZNSt3__111unique_lockINS_5mutexEE6unlockB9fqe220100Ev
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorI14MTActionEvent_NS5_ISA_EEEEEEEEvPT_
+ __ZNSt3__112__destroy_atB9fqe220100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEEEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEE21__construct_node_hashIJRKNS_21piecewise_construct_tENS_5tupleIJRSE_EEENST_IJEEEEEENS_10unique_ptrINS_11__hash_nodeISB_PvEENS_22__hash_node_destructorINS5_IS10_EEEEEEmDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeISB_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualEEENS_21__unordered_map_equalIS3_SC_SE_SD_EENS_9allocatorISC_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualEEENS_21__unordered_map_equalIS3_SC_SE_SD_EENS_9allocatorISC_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualEEENS_21__unordered_map_equalIS3_SC_SE_SD_EENS_9allocatorISC_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualEEENS_21__unordered_map_equalIS3_SC_SE_SD_EENS_9allocatorISC_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_S9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_S9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_S9_SD_SB_EENS_9allocatorIS9_EEE4findIS4_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_S9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_S9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEEEENS_21__unordered_map_equalIhS6_SA_S8_EENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEEEENS_21__unordered_map_equalIhS6_SA_S8_EENS_9allocatorIS6_EEE4findIhEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEEEENS_21__unordered_map_equalIhS6_SA_S8_EENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEEEENS_21__unordered_map_equalIhS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSPreferencable7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS4_EENS_9allocatorIS4_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE16__copy_constructB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE16__copy_constructB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEESH_m
+ __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEEC2ERKSA_
+ __ZNSt3__112__hash_tableIU8__strongP7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9foe220100Em
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe220100ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ __ZNSt3__113__tree_removeB9fqe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferI15MTSlideGesture_RNS_9allocatorIS1_EEE17__destruct_at_endB9foe220100EPS1_
+ __ZNSt3__114__split_bufferI16MTForceBehavior_RNS_9allocatorIS1_EEE17__destruct_at_endB9foe220100EPS1_
+ __ZNSt3__114__split_bufferI18MTChordGestureSet_RNS_9allocatorIS1_EEE17__destruct_at_endB9foe220100EPS1_
+ __ZNSt3__114__split_bufferINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEERNS_9allocatorIS5_EEE17__destruct_at_endB9fqe220100EPS5_
+ __ZNSt3__114__split_bufferINS_6vectorIiNS_9allocatorIiEEEERNS2_IS4_EEE17__destruct_at_endB9foe220100EPS4_
+ __ZNSt3__114__thread_proxyB9fqe220100INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN6HSUtil10Connection5startEvEUlvE_EEEEEPvSB_
+ __ZNSt3__115allocate_sharedB9foe220100I13MTHandMotion_NS_9allocatorIS1_EEJR20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptions14MTHandIdentityRA6_KcELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I13MTPathStates_NS_9allocatorIS1_EEJR20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptionsRbiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I17MTHandStatistics_NS_9allocatorIS1_EEJ14MTHandIdentityPcN11HSTPipeline10DeviceTypeE15MTParserOptionsELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I18MTForceManagement_NS_9allocatorIS1_EEJRU8__strongU13block_pointerFviffEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I20MTSurfaceDimensions_NS_9allocatorIS1_EEJR6MTRect6MTSizeELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I21MTPListGestureConfig_NS_9allocatorIS1_EEJN11HSTPipeline10DeviceTypeERbR24MTDragManagerEventQueue_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100INS_6vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS7_EEEENS8_ISA_EEJRmELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9fqe220100I6ClientNS_9allocatorIS1_EEJS1_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9fqe220100IN6HSUtil12ReceiveRightENS_9allocatorIS2_EEJS2_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9fqe220100IN6HSUtil6BufferENS_9allocatorIS2_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9fqe220100IN6HSUtil6BufferENS_9allocatorIS2_EEJRKNS2_11InvalidTypeEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9fqe220100IN6HSUtil6BufferENS_9allocatorIS2_EEJRKNS2_8CopyTypeERU8__strongP6NSDataELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9fqe220100IN6HSUtil6BufferENS_9allocatorIS2_EEJRKNS2_9FixedTypeERmELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9fqe220100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9fqe220100Ej
+ __ZNSt3__116__insertion_sortB9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_S6_T0_
+ __ZNSt3__116__pad_and_outputB9fqe220100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116allocator_traitsINS_9allocatorI16MTForceBehavior_EEE7destroyB9foe220100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI18MTChordGestureSet_EEE7destroyB9foe220100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__117__floyd_sift_downB9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEET1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
+ __ZNSt3__118__bitset_partitionB9foe220100INS_17_ClassicAlgPolicyEPfRNS_7greaterIfEEEENS_4pairIT0_bEES7_S7_T1_
+ __ZNSt3__118__bitset_partitionB9foe220100INS_17_ClassicAlgPolicyEPiRNS_7greaterIiEEEENS_4pairIT0_bEES7_S7_T1_
+ __ZNSt3__118condition_variable8wait_forB9fqe220100IxNS_5ratioILl1ELl1000000EEEEENS_9cv_statusERNS_11unique_lockINS_5mutexEEERKNS_6chrono8durationIT_T0_EE
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI11StatContactEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI13MTParserPath_EENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI14MTActionEvent_EENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI15MTSlideGesture_EENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI16MTForceBehavior_EENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI17ContactStabilizerEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI18MTChordGestureSet_EENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI20MTForceThresholding_EENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI7MTPointEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIN11HSTPipeline7ContactEEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIN6HSUtil7Encoder15ContainerRecordEEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIN6HSUtil7Encoder8KeyStateEEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorINS_6atomicIPKN6HSUtil8CoderKeyEEEEENS_16allocator_traitsIS8_EEEENS_19__allocation_resultINT0_7pointerENSC_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorINS_6vectorI16MTForceBehavior_NS1_IS3_EEEEEENS_16allocator_traitsIS6_EEEENS_19__allocation_resultINT0_7pointerENSA_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorINS_6vectorIiNS1_IiEEEEEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIPKN6HSUtil8CoderKeyEEENS_16allocator_traitsIS6_EEEENS_19__allocation_resultINT0_7pointerENSA_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIU8__strongP8HIDEventEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIfEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIiEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIN16HSRecordingTypes9PlayFrameEEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS3_EEEEEENS_16allocator_traitsIS7_EEEENS_19__allocation_resultINT0_7pointerENSB_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS4_EEEEEENS_16allocator_traitsIS8_EEEENS_19__allocation_resultINT0_7pointerENSC_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIU8__strongP11objc_objectEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__partial_sort_implB9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointS5_EET1_S6_S6_T2_OT0_
+ __ZNSt3__119__partial_sort_implB9foe220100INS_17_ClassicAlgPolicyERNS_7greaterIfEEPfS5_EET1_S6_S6_T2_OT0_
+ __ZNSt3__119__partial_sort_implB9foe220100INS_17_ClassicAlgPolicyERNS_7greaterIiEEPiS5_EET1_S6_S6_T2_OT0_
+ __ZNSt3__119__shared_weak_count16__release_sharedB9foe220100Ev
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqe220100Ev
+ __ZNSt3__120__shared_ptr_emplaceI13MTHandMotion_NS_9allocatorIS1_EEEC2B9foe220100IJR20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptions14MTHandIdentityRA6_KcES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI13MTPathStates_NS_9allocatorIS1_EEEC2B9foe220100IJR20MTSurfaceDimensions_N11HSTPipeline10DeviceTypeE15MTParserOptionsRbiES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI17MTHandStatistics_NS_9allocatorIS1_EEEC2B9foe220100IJ14MTHandIdentityPcN11HSTPipeline10DeviceTypeE15MTParserOptionsES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI18MTForceManagement_NS_9allocatorIS1_EEEC2B9foe220100IJRU8__strongU13block_pointerFviffEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI20MTSurfaceDimensions_NS_9allocatorIS1_EEEC2B9foe220100IJR6MTRect6MTSizeES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21MTPListGestureConfig_NS_9allocatorIS1_EEEC2B9foe220100IJN11HSTPipeline10DeviceTypeERbR24MTDragManagerEventQueue_ES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI6ClientNS_9allocatorIS1_EEE21__on_zero_shared_implB9fqe220100IS3_Li0EEEvv
+ __ZNSt3__120__shared_ptr_emplaceI6ClientNS_9allocatorIS1_EEEC2B9fqe220100IJS1_ES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN6HSUtil12ReceiveRightENS_9allocatorIS2_EEEC2B9fqe220100IJS2_ES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9fqe220100IJES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9fqe220100IJRKNS2_11InvalidTypeEES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9fqe220100IJRKNS2_8CopyTypeERU8__strongP6NSDataES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9fqe220100IJRKNS2_9FixedTypeERmES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceINS_6vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS7_EEEENS8_ISA_EEEC2B9foe220100IJRmESB_Li0EEESB_DpOT_
+ __ZNSt3__120__throw_length_errorB9foe220100EPKc
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__120__throw_out_of_rangeB9foe220100EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9fqe220100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9fqe220100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9fqe220100EPKcm
+ __ZNSt3__124__put_character_sequenceB9fqe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB9fqe220100Ev
+ __ZNSt3__126__insertion_sort_unguardedB9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_S6_T0_
+ __ZNSt3__126__insertion_sort_unguardedB9foe220100INS_17_ClassicAlgPolicyERNS_7greaterIfEEPfEEvT1_S6_T0_
+ __ZNSt3__126__insertion_sort_unguardedB9foe220100INS_17_ClassicAlgPolicyERNS_7greaterIiEEPiEEvT1_S6_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEbT1_S6_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_7greaterIfEEPfEEbT1_S6_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_7greaterIiEEPiEEbT1_S6_T0_
+ __ZNSt3__127__throw_bad_optional_accessB9foe220100Ev
+ __ZNSt3__127__tree_balance_after_insertB9fqe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI15MTSlideGesture_EEPS3_EEED2B9foe220100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI16MTForceBehavior_EEPS3_EEED2B9foe220100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18MTChordGestureSet_EEPS3_EEED2B9foe220100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIiNS2_IiEEEEEEPS5_EEED2B9foe220100Ev
+ __ZNSt3__131__partition_with_equals_on_leftB9foe220100INS_17_ClassicAlgPolicyEP7MTPointR26MTPointVelocityGreaterThanEET0_S6_S6_T1_
+ __ZNSt3__131__partition_with_equals_on_leftB9foe220100INS_17_ClassicAlgPolicyEPfRNS_7greaterIfEEEET0_S6_S6_T1_
+ __ZNSt3__131__partition_with_equals_on_leftB9foe220100INS_17_ClassicAlgPolicyEPiRNS_7greaterIiEEEET0_S6_S6_T1_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__132__partition_with_equals_on_rightB9foe220100INS_17_ClassicAlgPolicyEP7MTPointR26MTPointVelocityGreaterThanEENS_4pairIT0_bEES7_S7_T1_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI13MTParserPath_EEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI15MTSlideGesture_EEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI16MTForceBehavior_EEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI18MTChordGestureSet_EEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe220100INS_9allocatorI15MTSlideGesture_EEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe220100INS_9allocatorINS_6vectorIiNS1_IiEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__13mapIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectN6HSUtil10ObjectLessIS1_EENS_9allocatorINS_4pairIU8__strongKS2_S6_EEEEE6insertB9fqe220100EOSD_
+ __ZNSt3__13mapIiNS_10shared_ptrI6ClientEENS_4lessIiEENS_9allocatorINS_4pairIKiS3_EEEEE6insertB9fqe220100EOS9_
+ __ZNSt3__13setINS_10shared_ptrI8HSMapperEENS_4lessIS3_EENS_9allocatorIS3_EEE6insertB9fqe220100ERKS3_
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEC2B9fqe220100ERKSB_
+ __ZNSt3__16__treeINS_10shared_ptrI8HSMapperEENS_4lessIS3_EENS_9allocatorIS3_EEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIS3_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE21MTGestureMotionParamsEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE21MTGestureMotionParamsEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE7destroyEPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorI14MTActionEvent_NS5_IS9_EEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SB_EENS_4lessIS7_EEEENS5_ISG_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeISC_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorI14MTActionEvent_NS5_IS9_EEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SB_EENS_4lessIS7_EEEENS5_ISG_EEE7destroyEPNS_11__tree_nodeISC_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EEEENS_9allocatorISC_EEE12__find_equalB9fqe220100IS4_EENSA_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSP_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EEEENS_9allocatorISC_EEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EEEENS_9allocatorISC_EEE16__construct_nodeIJSC_EEENS_10unique_ptrINS_11__tree_nodeIS8_PvEENS_22__tree_node_destructorINSH_ISO_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EEEENS_9allocatorISC_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSO_SO_
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EEEENS_9allocatorISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEEEENS_9allocatorIS9_EEE14__erase_uniqueIiEEmRKT_
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEEEENS_9allocatorIS9_EEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEEEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEEEENS_9allocatorIS9_EEE21__remove_node_pointerEPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEEEENS_9allocatorIS9_EEE5eraseENS_21__tree_const_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEEEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16threadC2B9fqe220100IZN6HSUtil10Connection5startEvEUlvE_JELi0EEEOT_DpOT0_
+ __ZNSt3__16vectorI11StatContactNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI11StatContactNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI11StatContactNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKN11HSTPipeline10DeviceTypeEEEEPS1_DpOT_
+ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE16__init_with_sizeB9foe220100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE22__base_destruct_at_endB9foe220100EPS1_
+ __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE9push_backB9foe220100ERKS1_
+ __ZNSt3__16vectorI17ContactStabilizerNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI17ContactStabilizerNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE22__base_destruct_at_endB9foe220100EPS1_
+ __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEEC2B9foe220100EmRKS1_
+ __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE16__init_with_sizeB9foe220100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS2_S8_EEvT0_T1_l
+ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN16HSRecordingTypes9PlayFrameENS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN16HSRecordingTypes9PlayFrameENS_9allocatorIS2_EEE9push_backB9fqe220100ERKS2_
+ __ZNSt3__16vectorIN6HSUtil7Encoder15ContainerRecordENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN6HSUtil7Encoder15ContainerRecordENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN6HSUtil7Encoder8KeyStateENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEEC2B9foe220100Em
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE16__init_with_sizeB9foe220100IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS3_S8_EEvT0_T1_l
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE9push_backB9foe220100EOS3_
+ __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE5clearB9fqe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEEC2B9foe220100Em
+ __ZNSt3__16vectorIPKN6HSUtil8CoderKeyENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPKN6HSUtil8CoderKeyENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE9push_backB9fqe220100ERU8__strongKS2_
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS3_S9_EEvT0_T1_l
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE9push_backB9foe220100ERU8__strongKS2_
+ __ZNSt3__16vectorIZ34-[HSRecordingStage _stopRecording]E6RegionNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9foe220100IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPfS6_EEvT0_T1_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE24__emplace_back_slow_pathIJRKfEEEPfDpOT_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9foe220100IPiS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPiS6_EEvT0_T1_l
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE24__emplace_back_slow_pathIJRKiEEEPiDpOT_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE24__emplace_back_slow_pathIJiEEEPiDpOT_
+ __ZNSt3__17__sort4B9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointLi0EEEvT1_S6_S6_S6_T0_
+ __ZNSt3__18__invokeB9fqe220100IJRZN8HSMapper23_createConnectionConfigENS_8weak_ptrIS1_EEPU28objcproto17OS_dispatch_queue8NSObjectbEUlNS_10shared_ptrIN6HSUtil10ConnectionEEEE_SA_EEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSE_
+ __ZNSt3__18__invokeB9fqe220100IJRZN8HSMapper23_createConnectionConfigENS_8weak_ptrIS1_EEPU28objcproto17OS_dispatch_queue8NSObjectbEUlNS_10shared_ptrIN6HSUtil10ConnectionEEEONS8_6BufferEE_SA_SB_EEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSG_
+ __ZNSt3__19__sift_upB9foe220100INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
+ __ZNSt3__1eqB9foe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEEbRKNS_12basic_stringIT_T0_T1_EEPKS6_
+ __ZSt28__throw_bad_array_new_lengthB9foe220100v
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTISt19bad_optional_access
+ __ZTVSt19bad_optional_access
+ __ZZ170-[TrackpadAlgButtonStateManager handleDragReleaseDelay:currentDeviceButtonState:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:]E12frameCounter
+ __ZZ32-[HSTFrameParser parseSABinary:]EN3$_08__invokeEPvRK19_SABinaryInjExtData
+ __ZZ32-[HSTFrameParser parseSABinary:]EN3$_18__invokeEPvRK21_SABinaryInjExtPacketPKh
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SF_SJ_SH_EENS5_ISF_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRSE_EEENST_IJEEEEEENSD_INS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEEbEEDpOT_ENKUlSU_SS_OSV_OSW_E_clESU_SS_S17_S18_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualEEENS_21__unordered_map_equalIS3_SC_SE_SD_EENS_9allocatorISC_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRSB_EEENSP_IJEEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEEDpOT_ENKUlSQ_SO_OSR_OSS_E_clESQ_SO_S13_S14_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_S9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqe220100IJRS4_RyEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlRS8_SL_SM_E_clESX_SL_SM_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEEEENS_21__unordered_map_equalIhS6_SA_S8_EENS_9allocatorIS6_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEEDpOT_ENKUlSM_SK_OSN_OSO_E_clESM_SK_SZ_S10_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqe220100IJRyRS4_EEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlRS8_SL_SM_E_clESX_SL_SM_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlSP_SN_OSQ_OSR_E_clESP_SN_S12_S13_
+ __ZZNSt3__112__hash_tableIU6__weakPU26objcproto15HSPreferencable7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS4_EENS_9allocatorIS4_EEE16__emplace_uniqueB9fqe220100IJS4_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEEDpOT_ENKUlRU6__weakKS3_OS4_E_clESP_SQ_
+ __ZZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE16__emplace_uniqueB9fqe220100IJRU6__weakKS2_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSD_SD_E_clESD_SD_
+ __ZZNSt3__112__hash_tableIU8__strongP7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE16__emplace_uniqueB9fqe220100IJRU8__strongKS2_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSD_SD_E_clESD_SD_
+ __ZZNSt3__16vectorIZ34-[HSRecordingStage _stopRecording]E6RegionNS_9allocatorIS1_EEE12emplace_backIJS1_EEERS1_DpOT_ENKUlvE0_clEv
+ ___36-[DeviceInfoManager fetchDeviceInfo]_block_invoke
+ ___40-[ActuatorDevice initWithService:queue:]_block_invoke
+ ___41-[ActuatorDevice openActuatorForService:]_block_invoke
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_2
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_3
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_4
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_5
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_6
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_7
+ ___43-[HSTSensingAlgs initWithConfig:queue:log:]_block_invoke_8
+ ___44-[DeviceInfoManager populateDeviceInfoFrom:]_block_invoke
+ ___46-[HSTSensingAlgs createUserDevice:platformId:]_block_invoke
+ ___47-[HSTBackboardBridge _handleCombinedHostState:]_block_invoke
+ ___53-[HSTServerStage initWithName:description:queue:log:]_block_invoke
+ ___54-[HSTBackboardBridge initWithQueue:deviceService:log:]_block_invoke
+ ___63-[HSTHIDDeviceRouter _configureProxyHIDDeviceWithConfig:queue:]_block_invoke
+ ____ZN10HSPipeline9FindStageI23HSTPencilVirtualServiceEEPT_P7HSStage_block_invoke
+ ____ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStage_block_invoke
+ ____ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP9HIDDevicePU19objcproto9OS_os_logS2_P7HSStagem_block_invoke
+ ___block_descriptor_40_ea8_32s_e18_v16?0"HSTFrame"8ls32l8
+ ___block_descriptor_40_ea8_32s_e20_B16?0^{__SecTask=}8ls32l8
+ ___block_descriptor_40_ea8_32s_e35_v32?0"NSString"8"NSObject"16^B24ls32l8
+ ___block_descriptor_40_ea8_32w_e14_v20?0i8f12f16lw32l8
+ ___block_descriptor_40_ea8_32w_e19_B20?0"NSData"8B16lw32l8
+ ___block_descriptor_40_ea8_32w_e19_i40?0q8q16r^v24q32lw32l8
+ ___block_descriptor_40_ea8_32w_e26_"NSData"16?0"NSString"8lw32l8
+ ___block_descriptor_40_ea8_32w_e39_v48?0"HIDDevice"8Q16q24q32"NSData"40lw32l8
+ ___block_descriptor_40_ea8_32w_e8_v12?0I8lw32l8
+ ___block_descriptor_48_ea8_32s40s_e29_v32?08"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e37_v32?0"NSString"8"HIDElement"16^B24ls32l8s40l8s48l8
+ __block_literal_global.113
+ __cxx_global_var_init.103
+ __cxx_global_var_init.106
+ __cxx_global_var_init.107
+ __cxx_global_var_init.108
+ __cxx_global_var_init.117
+ __cxx_global_var_init.118
+ __cxx_global_var_init.124
+ __cxx_global_var_init.141
+ __cxx_global_var_init.153
+ __cxx_global_var_init.158
+ __cxx_global_var_init.159
+ __cxx_global_var_init.160
+ __cxx_global_var_init.181
+ __cxx_global_var_init.198
+ __cxx_global_var_init.202
+ __cxx_global_var_init.204
+ __cxx_global_var_init.252
+ __cxx_global_var_init.283
+ __cxx_global_var_init.289
+ __cxx_global_var_init.295
+ __cxx_global_var_init.301
+ __cxx_global_var_init.307
+ __cxx_global_var_init.319
+ __cxx_global_var_init.327
+ __cxx_global_var_init.328
+ __cxx_global_var_init.329
+ __cxx_global_var_init.337
+ __cxx_global_var_init.338
+ __cxx_global_var_init.347
+ __cxx_global_var_init.353
+ __cxx_global_var_init.366
+ __cxx_global_var_init.371
+ __cxx_global_var_init.376
+ __cxx_global_var_init.552
+ __cxx_global_var_init.553
+ __cxx_global_var_init.554
+ __cxx_global_var_init.555
+ __cxx_global_var_init.57
+ __cxx_global_var_init.67
+ __cxx_global_var_init.81
+ __cxx_global_var_init.96
+ __cxx_global_var_init.97
+ __os_log_fault_impl
+ _class_copyPropertyList
+ _dlopen
+ _mach_get_times
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_bootloaderForService:
+ _objc_msgSend$_calibrationDataForKey:
+ _objc_msgSend$_cleanup
+ _objc_msgSend$_configureProxyHIDDeviceWithConfig:queue:
+ _objc_msgSend$_findRoutingOverrideConfigForDevice:
+ _objc_msgSend$_handleCombinedHostState:
+ _objc_msgSend$_handleCombinedTouchModeEvent:
+ _objc_msgSend$_handleConfigurationRequest:needsConfirmation:
+ _objc_msgSend$_handleDataRequest:
+ _objc_msgSend$_handleDisplayServiceMatched:
+ _objc_msgSend$_handleHostState:
+ _objc_msgSend$_handleSingleHostState:
+ _objc_msgSend$_matchDisplayServiceFrom:
+ _objc_msgSend$_queueHIDPencilEventsToDispatch:
+ _objc_msgSend$active
+ _objc_msgSend$actuateForDictionary:
+ _objc_msgSend$actuateForID:strength:timeDilation:
+ _objc_msgSend$actuationRequestHistory
+ _objc_msgSend$actuatorDevice
+ _objc_msgSend$actuatorRevisionForService:
+ _objc_msgSend$actuatorService
+ _objc_msgSend$algButtonStateManager
+ _objc_msgSend$bundleURL
+ _objc_msgSend$cacheAndUpdateDeviceButtonState:currentDeviceTimestampSec:isTouching:rawButtonState:
+ _objc_msgSend$cacheDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:isTouching:shouldDelayDragRelease:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:hasPointerTranslation:
+ _objc_msgSend$cachedDeviceButtonState
+ _objc_msgSend$cachedProperties
+ _objc_msgSend$cachedPropertyKeys
+ _objc_msgSend$canDelayClicks
+ _objc_msgSend$cancelMatching
+ _objc_msgSend$code
+ _objc_msgSend$colorID
+ _objc_msgSend$commitElements:direction:error:
+ _objc_msgSend$consecutiveButtonUpFramesDuringDrag
+ _objc_msgSend$consecutiveDebouncedUpFramesDuringDrag
+ _objc_msgSend$contactCount
+ _objc_msgSend$createUserDevice:platformId:
+ _objc_msgSend$currentlyDelayingClick
+ _objc_msgSend$currentlyDelayingDragRelease
+ _objc_msgSend$dataPort
+ _objc_msgSend$dataValue
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$defaultHIDDevice
+ _objc_msgSend$delayDownClick:until:
+ _objc_msgSend$delayedButtonState
+ _objc_msgSend$delayedDownClickIsQueued
+ _objc_msgSend$delayedDownClickTimestampSec
+ _objc_msgSend$delayedDragReleaseButtonState
+ _objc_msgSend$description
+ _objc_msgSend$destoryUserClient
+ _objc_msgSend$device
+ _objc_msgSend$deviceIDForService:
+ _objc_msgSend$deviceInfoManager
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dispatchPencilEvents:
+ _objc_msgSend$displayState
+ _objc_msgSend$downClickDelaySec
+ _objc_msgSend$dragReleaseDelayNumberOfFrames
+ _objc_msgSend$dragReleaseMaxDebouncedUpFrames
+ _objc_msgSend$elementsMatching:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$fetchDeviceInfo
+ _objc_msgSend$fetchLimits
+ _objc_msgSend$findAncestorHIDDeviceForService:
+ _objc_msgSend$firstObject
+ _objc_msgSend$frameworkBundle
+ _objc_msgSend$frameworkString
+ _objc_msgSend$fwDefinedPlaylist
+ _objc_msgSend$fwDeviceButtonState
+ _objc_msgSend$gesturesBlockDeviceButtonClicks
+ _objc_msgSend$getBootLoader
+ _objc_msgSend$getDeviceInServiceTree:
+ _objc_msgSend$getInterfaceInServiceTree:
+ _objc_msgSend$getProperty:property:options:error:
+ _objc_msgSend$getReport:reportLength:withIdentifier:forType:error:
+ _objc_msgSend$handedOffHostClickControl
+ _objc_msgSend$handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:
+ _objc_msgSend$handleDragReleaseDelay:currentDeviceButtonState:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:
+ _objc_msgSend$handleReport:error:
+ _objc_msgSend$handleResetEvent:
+ _objc_msgSend$hardwareID
+ _objc_msgSend$hidDevice
+ _objc_msgSend$hidDeviceForReportID:
+ _objc_msgSend$hidDeviceKeys
+ _objc_msgSend$hidElementMatchingUsagePage:usage:
+ _objc_msgSend$hostClickEnabled
+ _objc_msgSend$ignoredDescriptionProperties
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithConfig:log:
+ _objc_msgSend$initWithConfig:queue:log:
+ _objc_msgSend$initWithConfig:withQueue:log:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithDevice:hidDevice:queue:log:inputReportHandler:
+ _objc_msgSend$initWithDevice:hidDeviceRouter:log:
+ _objc_msgSend$initWithDeviceType:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithKey:value:
+ _objc_msgSend$initWithLog:
+ _objc_msgSend$initWithName:description:queue:log:
+ _objc_msgSend$initWithPlaybackQueue:log:
+ _objc_msgSend$initWithProperties:
+ _objc_msgSend$initWithQueue:deviceService:log:
+ _objc_msgSend$initWithQueue:log:
+ _objc_msgSend$initWithQueue:matchingCallback:
+ _objc_msgSend$initWithRevision:fwDefinedPlaylist:
+ _objc_msgSend$initWithService:hidDevice:
+ _objc_msgSend$initWithService:queue:
+ _objc_msgSend$initWithStreamSize:platformId:personalityId:streamCallback:
+ _objc_msgSend$initWithTouchModeMap:
+ _objc_msgSend$interfaceClassName
+ _objc_msgSend$isContactInDeadzone:
+ _objc_msgSend$isTouching
+ _objc_msgSend$lastObject
+ _objc_msgSend$limits
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$locationID
+ _objc_msgSend$manageDragReleaseDelay:currentDeviceButtonState:rawButtonState:shouldDelayDragRelease:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:
+ _objc_msgSend$manufacturer
+ _objc_msgSend$matchingCallback
+ _objc_msgSend$maxPacketSize
+ _objc_msgSend$metadata
+ _objc_msgSend$mtfwVersion
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$newClickBlockedDueToExistingDelay
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$open
+ _objc_msgSend$openActuatorForService:
+ _objc_msgSend$openWithOptions:error:
+ _objc_msgSend$parameterizedWaveformForDictionary:strength:timeDilation:actuatorLimits:options:
+ _objc_msgSend$parameterizedWaveformForID:strength:timeDilation:actuatorLimits:options:
+ _objc_msgSend$parseExtraPayload75:frame:
+ _objc_msgSend$parsePathCollectionPacketV2:frame:surfaceCoordinates:
+ _objc_msgSend$parseSABinary:
+ _objc_msgSend$parseSAPreciseContact:toContact:surfaceCoordinates:
+ _objc_msgSend$personalityId
+ _objc_msgSend$platformId
+ _objc_msgSend$playlistManager
+ _objc_msgSend$populateDeviceInfoFrom:
+ _objc_msgSend$product
+ _objc_msgSend$productID
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$rawDeviceButtonState
+ _objc_msgSend$registryPropertyForKey:fromService:
+ _objc_msgSend$registryPropertyForKey:fromService:expectedClass:defaultValue:
+ _objc_msgSend$resetDragReleaseDelayState:
+ _objc_msgSend$revision
+ _objc_msgSend$sanitizedDeviceButtonState
+ _objc_msgSend$serviceIterator
+ _objc_msgSend$serviceMatchingNotificationPort
+ _objc_msgSend$serviceSupportsActuationLimits:
+ _objc_msgSend$serviceSupportsActuations:
+ _objc_msgSend$setActuatorDevice:
+ _objc_msgSend$setActuatorService:
+ _objc_msgSend$setAlgButtonStateManager:
+ _objc_msgSend$setCachedDeviceButtonState:
+ _objc_msgSend$setColorID:
+ _objc_msgSend$setConfigurationCallback:
+ _objc_msgSend$setConsecutiveButtonUpFramesDuringDrag:
+ _objc_msgSend$setConsecutiveDebouncedUpFramesDuringDrag:
+ _objc_msgSend$setCurrentlyDelayingClick:
+ _objc_msgSend$setCurrentlyDelayingDragRelease:
+ _objc_msgSend$setDataPort:
+ _objc_msgSend$setDataRequestCallback:
+ _objc_msgSend$setDelayedButtonState:
+ _objc_msgSend$setDelayedDownClickTimestampSec:
+ _objc_msgSend$setDelayedDragReleaseButtonState:
+ _objc_msgSend$setDevice:
+ _objc_msgSend$setDeviceID:
+ _objc_msgSend$setDeviceInfoManager:
+ _objc_msgSend$setDisplayState:
+ _objc_msgSend$setFrameworkBundle:
+ _objc_msgSend$setFrameworkString:
+ _objc_msgSend$setFwDeviceButtonState:
+ _objc_msgSend$setGesturesBlockDeviceButtonClicks:
+ _objc_msgSend$setHandedOffHostClickControl:
+ _objc_msgSend$setHardwareID:
+ _objc_msgSend$setHidDevice:actuatorService:
+ _objc_msgSend$setInputReportHandler:
+ _objc_msgSend$setInterfaceClassName:
+ _objc_msgSend$setLimits:
+ _objc_msgSend$setLocationID:
+ _objc_msgSend$setManufacturer:
+ _objc_msgSend$setMaxPacketSize:
+ _objc_msgSend$setMtfwVersion:
+ _objc_msgSend$setNewClickBlockedDueToExistingDelay:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setPersonalityId:
+ _objc_msgSend$setPlatformId:
+ _objc_msgSend$setPlaylistManager:
+ _objc_msgSend$setProduct:
+ _objc_msgSend$setProductID:
+ _objc_msgSend$setRawDeviceButtonState:
+ _objc_msgSend$setRemovalHandler:
+ _objc_msgSend$setReport:reportLength:withIdentifier:forType:error:
+ _objc_msgSend$setRevision:
+ _objc_msgSend$setSanitizedDeviceButtonState:
+ _objc_msgSend$setServiceIterator:
+ _objc_msgSend$setServiceMatchingNotificationPort:
+ _objc_msgSend$setSetReportHandler:
+ _objc_msgSend$setSurfaceSize:
+ _objc_msgSend$setSystemActuations:
+ _objc_msgSend$setTranslationOccurredDuringClick:
+ _objc_msgSend$setTransport:
+ _objc_msgSend$setUpClickOccuredDuringDelay:
+ _objc_msgSend$setVendorID:
+ _objc_msgSend$setWaveform:waveform:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$shouldBlockClicks
+ _objc_msgSend$signal
+ _objc_msgSend$startMatchingWithDictionary:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$systemActuations
+ _objc_msgSend$touchModeMap
+ _objc_msgSend$translationOccurredDuringClick
+ _objc_msgSend$upClickOccuredDuringDelay
+ _objc_msgSend$updateArtificialSurfaceSize
+ _objc_msgSend$updateCachedButtonState:currentDeviceTimestampSec:isTouching:
+ _objc_msgSend$updateClickDelayState:
+ _objc_msgSend$updateFirmwareClicks
+ _objc_msgSend$updateFwButtonStateTo:
+ _objc_msgSend$updateMomentumStartForEvent:forSubtype:
+ _objc_msgSend$updateTranslationTracking:hasPointerTranslation:
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$vendorID
+ _objc_msgSend$virtualEventServiceWithDelegate:
+ _objc_msgSend$virtualServiceDispatchEvent:
+ _objc_msgSend$virtualServiceTerminate
+ _objc_msgSend$waitUntilDate:
+ _objc_msgSend$workIntervalUpdate:complexity:
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_setProperty_nonatomic_copy
+ _property_getName
+ _strerror
- +[ActuationManager playlistFromPlist:forRevision:]
- +[ActuationManager playlistFromPlist:forRevision:].cold.1
- +[ActuationManager playlistFromPlist:forRevision:].cold.2
- +[ActuationManager playlistFromV2OrV3Plist:forRevision:withPlistVersion:]
- +[ActuationManager playlistFromV2OrV3Plist:forRevision:withPlistVersion:].cold.1
- +[ActuationManager plistV3FromPlaylist:]
- -[ActuationManager .cxx_destruct]
- -[ActuationManager actuateForDictionary:strength:timeDilation:device:actuatorLimits:options:]
- -[ActuationManager actuateForID:strength:timeDilation:device:actuatorLimits:options:]
- -[ActuationManager actuateWaveform:strength:timeDilation:device:actuatorLimits:options:]
- -[ActuationManager actuatorRevision]
- -[ActuationManager debug]
- -[ActuationManager initWithService:]
- -[ActuationManager overridePlaylistPlist]
- -[ActuationManager overridePlaylist]
- -[ActuationManager productionPlaylistPlist]
- -[ActuationManager productionPlaylist]
- -[ActuationManager productionPlist]
- -[ActuationManager productionPlist].cold.1
- -[ActuationManager productionPlist].cold.2
- -[ActuationManager setActuatorRevision:]
- -[ActuationManager setOverridePlaylist:]
- -[ActuationManager setOverridePlaylistPlist:]
- -[ActuationManager setProductionPlaylist:]
- -[CoreAccessoryManager .cxx_destruct]
- -[CoreAccessoryManager accessoryConnectionInfoFromTransport:connection:transport:]
- -[CoreAccessoryManager coreAccessoryServiceInfoFromProperties:]
- -[CoreAccessoryManager dealloc]
- -[CoreAccessoryManager debug]
- -[CoreAccessoryManager deregisterForDeviceManagementMatching]
- -[CoreAccessoryManager driverFirmwareVersion]
- -[CoreAccessoryManager handleDeviceManagementMatching:]
- -[CoreAccessoryManager init]
- -[CoreAccessoryManager publishCoreAccessoryService:]
- -[CoreAccessoryManager queue]
- -[CoreAccessoryManager registerForDeviceManagementMatching]
- -[CoreAccessoryManager serialNumber]
- -[CoreAccessoryManager setDriverFirmwareVersion:]
- -[CoreAccessoryManager setQueue:]
- -[CoreAccessoryManager setSerialNumber:]
- -[CoreAccessoryManager unpublishCoreAccessoryService]
- -[EmbeddedTrackpadFirmwareManager _handleGetPropertyEvent:]
- -[HSTActuationEvent decodeFromMap:].cold.4
- -[HSTBackboardBridge initWithQueue:]
- -[HSTBackboardBridge initWithQueue:].cold.1
- -[HSTContactStabilizer initWithConfig:]
- -[HSTFirmwareManager initWithDevice:]
- -[HSTHIDEventGenerator initWithConfig:]
- -[HSTPencilVirtualService _dispatchHIDEvents:]
- -[HSTPencilVirtualService _dispatchHIDEventsAsync:]
- -[HSTPencilVirtualService _handleHIDEvents:]
- -[HSTPencilVirtualService _handleHIDPencilEvents:]
- -[HSTPencilVirtualService initWithConfig:withQueue:]
- -[HSTPencilVirtualService innie]
- -[HSTPencilVirtualService outie]
- -[HSTPencilVirtualService setInnie:]
- -[HSTPencilVirtualService setOutie:]
- -[HSTPhoneFirmwareManager initWithDevice:]
- -[HSTRecordingManager initWithPlaybackQueue:]
- -[HSTSensingAlgs .cxx_construct]
- -[HSTSensingAlgs initWithConfig:]
- -[HSTSensingAlgs initWithConfig:].cold.1
- -[HSTSensingAlgs initWithConfig:].cold.2
- -[HSTSensingAlgs initWithConfig:].cold.3
- -[HSTServerStage initWithName:description:queue:]
- -[HSTServerStage initWithName:description:queue:].cold.1
- -[HSTServerStage initWithName:description:queue:].cold.2
- -[HSTServerStage initWithName:description:queue:].cold.3
- -[HSTTelemetryAnalyticsStage initWithQueue:]
- -[HSTTipOffsetFilter initWithConfig:]
- -[MacOSTrackpadHIDEventProcessor initWithDeviceID:deviceType:]
- -[MacTrackpadBridge initWithService:]
- -[MouseBridge initWithService:]
- -[PointerBridge coreAccessoryManager]
- -[PointerBridge initWithService:settings:]
- -[PointerBridge setCoreAccessoryManager:]
- -[PointerHIDEventProcessor generateMomentumStartEventFrom:forSubtype:]
- -[PointerHIDEventProcessor initWithDeviceID:deviceType:]
- -[TrackpadActuatorStage _openActuatorDevice]
- -[TrackpadActuatorStage _openActuatorDevice].cold.1
- -[TrackpadActuatorStage actuationManager]
- -[TrackpadActuatorStage actuationOptions]
- -[TrackpadActuatorStage actuatorLimits]
- -[TrackpadActuatorStage fetchActuatorLimits]
- -[TrackpadActuatorStage handleActMatching:]
- -[TrackpadActuatorStage handleActMatching:].cold.1
- -[TrackpadActuatorStage initWithDevice:]
- -[TrackpadActuatorStage setActuationManager:]
- -[TrackpadActuatorStage setActuationOptions:]
- -[TrackpadActuatorStage setQueue:].cold.1
- -[TrackpadActuatorStage supportsActuationLimits]
- -[TrackpadAlgStage deviceButtonState]
- -[TrackpadAlgStage setDeviceButtonState:activePathCount:]
- -[TrackpadBridge initWithService:]
- -[TrackpadFirmwareManager initWithDevice:]
- -[TrackpadFirmwareManager mtDeviceRef]
- -[TrackpadFirmwareManager productId]
- -[TrackpadFirmwareManager setProductId:]
- -[TrackpadFirmwareManager setTransport:]
- -[TrackpadFirmwareManager transport]
- -[TrackpadHIDEventProcessor initWithDeviceID:deviceType:]
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Contact.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTBackboardBridge.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCREventGenerator.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCircularBuffer.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTContactStabilizer.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCoreAnalytics.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTEvent.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame+Python.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrameParser.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventGenerator.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventStatistics.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEvents.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPencilVirtualService.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPipeline_vers.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTRecordingManager.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTSensingAlgs.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTServerStage.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTTipOffsetFilter.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Types.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTActionEvent_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCyclingTrackpad_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCycling_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordGestureSet_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordIntegrating_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordTable_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerEllipseTip_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerToPathMap_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceBehavior_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceConfig.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceFilter_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceManagement_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceThresholding_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTGestureConfig_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHIDEventAppend.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandMotion_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandStatistics_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPListGestureConfig_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParameterFactory_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParserPath_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPathStates_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTRestZoneIntegrator_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSlideGesture_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSurfaceDimensions_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTapDragManager_.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTrackpadUberAlg.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(USBKey.o)
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTPipeline.build/DerivedSources/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/DerivedSources/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationManager.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationMultipliers.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationTone.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationWaveform.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorLimits.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/CoreAccessoryManager.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadFirmwareManager.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/FirmwareUtil.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSMousePipelineCreation.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTFirmwareManager.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTPipelineCreation.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTSAPipelineCreation.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTTelemetryAnalyticsStage.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService_vers.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadDefs.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadPipelineCreation.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTGestureConfigGenerator.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPluginLogging.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPreferences.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacOSTrackpadHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacTrackpadBridge.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MomentumCurve.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MouseBridge.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PeppyHIDService.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerBridge.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerSettings.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadActuatorStage.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadAlgStage.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadBridge.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadFirmwareManager.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadMomentumGeneratorStage.o
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/HIDSensingTouch/HSTPipeline/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/TrackpadActuatorStage/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/Managers/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/FirmwareManagers/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/Plugin/
- /Library/Caches/com.apple.xbs/007F0241-FFDA-42D3-A9CA-07605CCB9E0D/TemporaryDirectory.u6ZbBx/Sources/Multitouch/Plugin/Parser/
- ActuationManager.mm
- CoreAccessoryManager.mm
- FirmwareUtil.mm
- GCC_except_table104
- GCC_except_table108
- GCC_except_table113
- GCC_except_table119
- GCC_except_table120
- GCC_except_table123
- GCC_except_table125
- GCC_except_table133
- GCC_except_table142
- GCC_except_table157
- GCC_except_table166
- GCC_except_table167
- GCC_except_table173
- GCC_except_table179
- GCC_except_table180
- GCC_except_table181
- GCC_except_table186
- GCC_except_table187
- GCC_except_table188
- GCC_except_table189
- GCC_except_table190
- GCC_except_table191
- GCC_except_table192
- GCC_except_table198
- GCC_except_table204
- GCC_except_table209
- GCC_except_table210
- GCC_except_table231
- GCC_except_table232
- GCC_except_table233
- GCC_except_table234
- GCC_except_table235
- GCC_except_table236
- GCC_except_table237
- GCC_except_table242
- GCC_except_table243
- GCC_except_table248
- GCC_except_table280
- GCC_except_table281
- GCC_except_table288
- GCC_except_table298
- GCC_except_table312
- GCC_except_table325
- GCC_except_table326
- GCC_except_table328
- GCC_except_table337
- GCC_except_table350
- GCC_except_table351
- GCC_except_table352
- GCC_except_table353
- GCC_except_table361
- GCC_except_table362
- GCC_except_table367
- GCC_except_table368
- GCC_except_table370
- GCC_except_table376
- GCC_except_table382
- GCC_except_table384
- GCC_except_table391
- GCC_except_table408
- GCC_except_table90
- OBJC_IVAR_$_ActuationManager._actuatorRevision
- OBJC_IVAR_$_ActuationManager._overridePlaylist
- OBJC_IVAR_$_ActuationManager._productionPlaylist
- OBJC_IVAR_$_CoreAccessoryManager._connectionUUID
- OBJC_IVAR_$_CoreAccessoryManager._dmMatchedIterator
- OBJC_IVAR_$_CoreAccessoryManager._dmMatchedNotifierPortRef
- OBJC_IVAR_$_CoreAccessoryManager._driverFirmwareVersion
- OBJC_IVAR_$_CoreAccessoryManager._publishedAccessoryInfo
- OBJC_IVAR_$_CoreAccessoryManager._queue
- OBJC_IVAR_$_CoreAccessoryManager._serialNumber
- OBJC_IVAR_$_HSTActuationEvent.scale
- OBJC_IVAR_$_HSTPencilVirtualService._innie
- OBJC_IVAR_$_HSTPencilVirtualService._outie
- OBJC_IVAR_$_PointerBridge._coreAccessoryManager
- OBJC_IVAR_$_TrackpadActuatorStage._actDevice
- OBJC_IVAR_$_TrackpadActuatorStage._actuationManager
- OBJC_IVAR_$_TrackpadActuatorStage._actuationOptions
- OBJC_IVAR_$_TrackpadActuatorStage._actuationsEnabled
- OBJC_IVAR_$_TrackpadActuatorStage._actuatorEntryID
- OBJC_IVAR_$_TrackpadActuatorStage._actuatorLimits
- OBJC_IVAR_$_TrackpadActuatorStage._actuatorMatchedIterator
- OBJC_IVAR_$_TrackpadActuatorStage._actuatorMatchedNotifierPortRef
- OBJC_IVAR_$_TrackpadActuatorStage._mtDevice
- OBJC_IVAR_$_TrackpadAlgStage._deviceButtonState
- OBJC_IVAR_$_TrackpadFirmwareManager._mtDeviceRef
- OBJC_IVAR_$_TrackpadFirmwareManager._productId
- OBJC_IVAR_$_TrackpadFirmwareManager._transport
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CFNumberCreate
- _MTActuatorClose
- _MTActuatorGetReport
- _MTActuatorGetService
- _MTActuatorGetSystemActuationsEnabled
- _MTActuatorHandoffHostClickControl
- _MTActuatorIsOpen
- _MTActuatorOpen
- _MTActuatorReclaimHostClickControl
- _MTActuatorSetFirmwareClicks
- _MTActuatorSetReport
- _MTDeviceGetCriticalErrors
- _MTDeviceGetMTActuator
- _MTDeviceGetParserOptions
- _MTDeviceGetReport
- _MTDeviceSendExternalMessage
- _MTDeviceSetReport
- _MTDeviceSupportsActuation
- _OBJC_CLASS_$_ACCTransportClient
- _OBJC_CLASS_$_ActuationManager
- _OBJC_CLASS_$_CoreAccessoryManager
- _OBJC_CLASS_$_HIDVirtualEventService
- _OBJC_METACLASS_$_ActuationManager
- _OBJC_METACLASS_$_CoreAccessoryManager
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport13EnabledInputs5AwakeEEvP10__MTDeviceRKT_.cold.1
- _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17FaceDetectionModeEEvP10__MTDeviceRKT_.cold.1
- _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17HostInterruptModeEEvP10__MTDeviceRKT_.cold.1
- _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport23HostNotificationControlEEvP10__MTDeviceRKT_.cold.1
- _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport8DataModeEEvP10__MTDeviceRKT_.cold.1
- _ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport9HostEventEEvP10__MTDeviceRKT_.cold.1
- _ZN11HSTPipeline12FirmwareUtil17SetReportWithDataEP10__MTDeviceP6NSData.cold.1
- _ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.1
- _ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.2
- _ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStagem.cold.1
- _ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.1
- _ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.2
- _ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.3
- _ZN11HSTPipeline22CreateTrackpadPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.1
- _ZN11HSTPipeline22CreateTrackpadPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage.cold.2
- __36-[HSTBackboardBridge initWithQueue:]_block_invoke.38
- __36-[HSTBackboardBridge initWithQueue:]_block_invoke.40
- __36-[HSTBackboardBridge initWithQueue:]_block_invoke.42
- __49-[HSTServerStage initWithName:description:queue:]_block_invoke.cold.1
- __49-[HSTServerStage initWithName:description:queue:]_block_invoke.cold.2
- __52-[HSTPencilVirtualService initWithConfig:withQueue:]_block_invoke.30
- __52-[HSTPencilVirtualService initWithConfig:withQueue:]_block_invoke.cold.1
- __Block_byref_object_copy_.421
- __Block_byref_object_dispose_.422
- __OBJC_$_CLASS_METHODS_ActuationManager
- __OBJC_$_INSTANCE_METHODS_ActuationManager
- __OBJC_$_INSTANCE_METHODS_CoreAccessoryManager
- __OBJC_$_INSTANCE_VARIABLES_ActuationManager
- __OBJC_$_INSTANCE_VARIABLES_CoreAccessoryManager
- __OBJC_$_PROP_LIST_ActuationManager
- __OBJC_$_PROP_LIST_CoreAccessoryManager
- __OBJC_CLASS_RO_$_ActuationManager
- __OBJC_CLASS_RO_$_CoreAccessoryManager
- __OBJC_METACLASS_RO_$_ActuationManager
- __OBJC_METACLASS_RO_$_CoreAccessoryManager
- __Z18actMatchedCallbackPvj
- __ZGVN6HSUtil8CoderKey7LiteralIJLc115ELc99ELc97ELc108ELc101EEE3KeyE
- __ZL18_dmMatchedCallbackPvj
- __ZL25createEnabledInputsReporttN11HSTPipeline17ScreenOrientationE
- __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport13EnabledInputs5AwakeEEvP10__MTDeviceRKT_
- __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17FaceDetectionModeEEvP10__MTDeviceRKT_
- __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport17HostInterruptModeEEvP10__MTDeviceRKT_
- __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport23HostNotificationControlEEvP10__MTDeviceRKT_
- __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport8DataModeEEvP10__MTDeviceRKT_
- __ZL9setReportIN11HSTPipeline17FirmwareInterface13FeatureReport9HostEventEEvP10__MTDeviceRKT_
- __ZN11HSTPipeline12FirmwareUtil13GetReportDataEP10__MTDevicelPi
- __ZN11HSTPipeline12FirmwareUtil17SetReportWithDataEP10__MTDeviceP6NSData
- __ZN11HSTPipeline14CreatePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage
- __ZN11HSTPipeline16CreateSAPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStagem
- __ZN11HSTPipeline19CreateMousePipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage
- __ZN11HSTPipeline22CreateTrackpadPipelineEP8NSStringPU28objcproto17OS_dispatch_queue8NSObjectP10__MTDeviceP7HSStage
- __ZN11HSTPipelineL14getIntPropertyEjP8NSString
- __ZN13MTHandMotion_C1ERK20MTSurfaceDimensions_12MTParserType15MTParserOptions14MTHandIdentityPKc
- __ZN13MTHandMotion_C2ERK20MTSurfaceDimensions_12MTParserType15MTParserOptions14MTHandIdentityPKc
- __ZN13MTParserPath_C1E12MTParserType15MTParserOptions
- __ZN13MTParserPath_C2E12MTParserType15MTParserOptions
- __ZN13MTPathStates_C1ERK20MTSurfaceDimensions_12MTParserType15MTParserOptionsbj
- __ZN13MTPathStates_C2ERK20MTSurfaceDimensions_12MTParserType15MTParserOptionsbj
- __ZN15MTChordCycling_C1E14MTHandIdentityPcR24MTDragManagerEventQueue_b12MTParserType
- __ZN15MTChordCycling_C2E14MTHandIdentityPcR24MTDragManagerEventQueue_b12MTParserType
- __ZN16MTGestureConfig_C2E12MTParserType15MTParserOptionsbR24MTDragManagerEventQueue_
- __ZN17MTHandStatistics_C1E14MTHandIdentityPc12MTParserType15MTParserOptions
- __ZN18MTForceManagement_28setFirstStageClickPreferenceE15MTClickStrength
- __ZN18MTForceManagement_29setSecondStageClickPreferenceE15MTClickStrength
- __ZN18MTForceManagement_C1EU13block_pointerFvi15MTClickStrengthffE
- __ZN18MTForceManagement_C2EU13block_pointerFvi15MTClickStrengthffE
- __ZN19MTParameterFactory_19initTouchZoneParamsER22MTTouchZoneParameters_12MTParserType15MTParserOptionsbRK20MTSurfaceDimensions_
- __ZN19MTParameterFactory_20initPathFilterParamsER23MTPathFilterParameters_12MTParserType15MTParserOptionsbRK20MTSurfaceDimensions_j
- __ZN19MTParameterFactory_21initForceFilterParamsER24MTForceFilterParameters_12MTParserType15MTParserOptionsbRK20MTSurfaceDimensions_
- __ZN19MTParameterFactory_22initChordCyclingParamsER25MTChordCyclingParameters_12MTParserType
- __ZN19MTParameterFactory_25initFingerTipOffsetParamsER30MTHMFingerTipOffsetParameters_12MTParserType15MTParserOptionsb
- __ZN19MTParameterFactory_26initMotionExtractionParamsER29MTMotionExtractionParameters_12MTParserType15MTParserOptions
- __ZN21MTPListGestureConfig_C1E12MTParserType15MTParserOptionsbR24MTDragManagerEventQueue_
- __ZN21MTRestZoneIntegrator_C1ERK20MTSurfaceDimensions_12MTParserType15MTParserOptions
- __ZN21MTRestZoneIntegrator_C2ERK20MTSurfaceDimensions_12MTParserType15MTParserOptions
- __ZN23MTChordCyclingTrackpad_C1E14MTHandIdentityPcR24MTDragManagerEventQueue_b12MTParserType
- __ZN6HSUtil8CoderKey7LiteralIJLc115ELc99ELc97ELc108ELc101EEE3KeyE
- __ZN6HSUtil8CoderKey7LiteralIJLc115ELc99ELc97ELc108ELc101EEE4_StrE
- __ZNKSt3__111__copy_implclB9nqe210106IPNS_6vectorIiNS_9allocatorIiEEEES6_S6_EENS_4pairIT_T1_EES8_T0_S9_
- __ZNKSt3__111__copy_implclB9nqe210106IPU8__strongP8HIDEventS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9nqe210106ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe210106EPKvm
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI15MTSlideGesture_EEPS2_EclB9nqe210106Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI16MTForceBehavior_EEPS2_EclB9nqe210106Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18MTChordGestureSet_EEPS2_EclB9nqe210106Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIiNS1_IiEEEEEEPS4_EclB9nqe210106Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9nqe210106ERKS6_S9_
- __ZNKSt3__18equal_toIU6__weakPU26objcproto15HSPreferencable7HSStageEclB9nqe210106ERU6__weakKS3_S7_
- __ZNKSt3__18equal_toIU6__weakPU26objcproto15HSStageObserver11objc_objectEclB9nqe210106ERU6__weakKS2_S6_
- __ZNKSt9type_infoeqB9nqe210106ERKS_
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt12out_of_rangeC1B9nqe210106EPKc
- __ZNSt3__110__function12__value_funcIFN6HSUtil6BufferENS_10shared_ptrINS2_10ConnectionEEEOS3_EE4swapB9nqe210106ERS9_
- __ZNSt3__110__function12__value_funcIFN6HSUtil6BufferENS_10shared_ptrINS2_10ConnectionEEEOS3_EEC2B9nqe210106ERKS9_
- __ZNSt3__110__function12__value_funcIFN6HSUtil6BufferENS_10shared_ptrINS2_10ConnectionEEEOS3_EED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEE4swapB9nqe210106ERSB_
- __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEEC2B9nqe210106ERKSB_
- __ZNSt3__110__function12__value_funcIFP11objc_objectRN6HSUtil7DecoderERKNS4_8CoderKeyEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbRN6HSUtil7EncoderEP11objc_objectEE4swapB9nqe210106ERS8_
- __ZNSt3__110__function12__value_funcIFbRN6HSUtil7EncoderEP11objc_objectEEC2B9nqe210106ERKS8_
- __ZNSt3__110__function12__value_funcIFbRN6HSUtil7EncoderEP11objc_objectEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI8HSMapperEEEE4swapB9nqe210106ERS6_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI8HSMapperEEEEC2B9nqe210106ERKS6_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI8HSMapperEEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN6HSUtil10ConnectionEEEEE4swapB9nqe210106ERS7_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN6HSUtil10ConnectionEEEEEC2B9nqe210106ERKS7_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrIN6HSUtil10ConnectionEEEEED2B9nqe210106Ev
- __ZNSt3__110shared_ptrI8HSMapperEC2B9nqe210106IS1_Li0EEEPT_
- __ZNSt3__110shared_ptrIN6HSUtil10ConnectionEEC2B9nqe210106IS2_Li0EEEPT_
- __ZNSt3__110unique_ptrI8HSMapperNS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN6HSUtil10ConnectionENS_14default_deleteIS2_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS2_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN6HSUtil7Decoder9CallbacksENS_14default_deleteIS3_EEE5resetB9nqe210106EPS3_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP11objc_objectyEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP11objc_objectEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP7HSProxyEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeIU6__weakPU26objcproto15HSPreferencable7HSStagePvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeIU6__weakPU26objcproto15HSStageObserver11objc_objectPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeIU8__strongP7HSStagePvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN6HSUtil10Connection5startEvEUlvE_EEENS3_IS9_EEED1B9nqe210106Ev
- __ZNSt3__111__sift_downB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_OT0_NS_15iterator_traitsIS6_E15difference_typeES6_
- __ZNSt3__111__sift_downB9nqe210106INS_17_ClassicAlgPolicyERNS_7greaterIfEEPfEEvT1_OT0_NS_15iterator_traitsIS6_E15difference_typeES6_
- __ZNSt3__111__sift_downB9nqe210106INS_17_ClassicAlgPolicyERNS_7greaterIiEEPiEEvT1_OT0_NS_15iterator_traitsIS6_E15difference_typeES6_
- __ZNSt3__111unique_lockINS_5mutexEE4lockB9nqe210106Ev
- __ZNSt3__111unique_lockINS_5mutexEE6unlockB9nqe210106Ev
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorI14MTActionEvent_NS5_ISA_EEEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeISB_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRSE_EEENST_IJEEEEEENS_10unique_ptrINS_11__hash_nodeISB_PvEENS_22__hash_node_destructorINS5_IS10_EEEEEEmOT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRSE_EEENST_IJEEEEEENSD_INS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SA_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SF_SJ_SH_Lb1EEENS5_ISF_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualELb1EEENS_21__unordered_map_equalIS3_SC_SE_SD_Lb1EEENS_9allocatorISC_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualELb1EEENS_21__unordered_map_equalIS3_SC_SE_SD_Lb1EEENS_9allocatorISC_EEE25__emplace_unique_key_argsIS3_JRKNS_21piecewise_construct_tENS_5tupleIJRSB_EEENSP_IJEEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualELb1EEENS_21__unordered_map_equalIS3_SC_SE_SD_Lb1EEENS_9allocatorISC_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualELb1EEENS_21__unordered_map_equalIS3_SC_SE_SD_Lb1EEENS_9allocatorISC_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN6HSUtil8CoderKeyEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS5_13KeyStringHashENS5_14KeyStringEqualELb1EEENS_21__unordered_map_equalIS3_SC_SE_SD_Lb1EEENS_9allocatorISC_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIS4_JRS4_RyEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIS4_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP11objc_objectyEENS_22__unordered_map_hasherIS4_NS_4pairIU8__strongKS3_yEEN6HSUtil12ObjectHasherENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIhJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE4findIhEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIyJRyRS4_EEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP11objc_objectEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyU8__strongP7HSProxyEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSPreferencable7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS4_EENS_9allocatorIS4_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS4_PvEEEE
- __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSPreferencable7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS4_EENS_9allocatorIS4_EEE25__emplace_unique_key_argsIS4_JS4_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
- __ZNSt3__112__hash_tableIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS3_JRU6__weakKS2_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIU8__strongP7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
- __ZNSt3__112__hash_tableIU8__strongP7HSStageN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS3_JRU8__strongKS2_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__113__tree_removeB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113unordered_setIU6__weakPU26objcproto15HSStageObserver11objc_objectN6HSUtil12ObjectHasherENS_8equal_toIS3_EENS_9allocatorIS3_EEEC2ERKSA_
- __ZNSt3__114__split_bufferI15MTSlideGesture_RNS_9allocatorIS1_EEE17__destruct_at_endB9nqe210106EPS1_
- __ZNSt3__114__split_bufferI16MTForceBehavior_RNS_9allocatorIS1_EEE17__destruct_at_endB9nqe210106EPS1_
- __ZNSt3__114__split_bufferI18MTChordGestureSet_RNS_9allocatorIS1_EEE17__destruct_at_endB9nqe210106EPS1_
- __ZNSt3__114__split_bufferINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEERNS_9allocatorIS5_EEE17__destruct_at_endB9nqe210106EPS5_
- __ZNSt3__114__split_bufferINS_6vectorIiNS_9allocatorIiEEEERNS2_IS4_EEE17__destruct_at_endB9nqe210106EPS4_
- __ZNSt3__114__thread_proxyB9nqe210106INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN6HSUtil10Connection5startEvEUlvE_EEEEEPvSB_
- __ZNSt3__115allocate_sharedB9nqe210106I13MTHandMotion_NS_9allocatorIS1_EEJR20MTSurfaceDimensions_R12MTParserType15MTParserOptions14MTHandIdentityRA6_KcELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I13MTPathStates_NS_9allocatorIS1_EEJR20MTSurfaceDimensions_R12MTParserType15MTParserOptionsRbiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I17MTHandStatistics_NS_9allocatorIS1_EEJ14MTHandIdentityPcR12MTParserType15MTParserOptionsELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I18MTForceManagement_NS_9allocatorIS1_EEJRU8__strongU13block_pointerFvi15MTClickStrengthffEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I20MTSurfaceDimensions_NS_9allocatorIS1_EEJR6MTRect6MTSizeELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I21MTPListGestureConfig_NS_9allocatorIS1_EEJR12MTParserType15MTParserOptionsRbR24MTDragManagerEventQueue_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I6ClientNS_9allocatorIS1_EEJS1_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN6HSUtil12ReceiveRightENS_9allocatorIS2_EEJS2_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN6HSUtil6BufferENS_9allocatorIS2_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN6HSUtil6BufferENS_9allocatorIS2_EEJRKNS2_11InvalidTypeEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN6HSUtil6BufferENS_9allocatorIS2_EEJRKNS2_8CopyTypeERU8__strongP6NSDataELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN6HSUtil6BufferENS_9allocatorIS2_EEJRKNS2_9FixedTypeERmELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106INS_6vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS7_EEEENS8_ISA_EEJRmELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9nqe210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9nqe210106Ej
- __ZNSt3__116__insertion_sortB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_S6_T0_
- __ZNSt3__116__pad_and_outputB9nqe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__116allocator_traitsINS_9allocatorI16MTForceBehavior_EEE7destroyB9nqe210106IS2_Li0EEEvRS3_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorI18MTChordGestureSet_EEE7destroyB9nqe210106IS2_Li0EEEvRS3_PT_
- __ZNSt3__117__floyd_sift_downB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEET1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
- __ZNSt3__118__bitset_partitionB9nqe210106INS_17_ClassicAlgPolicyEPfRNS_7greaterIfEEEENS_4pairIT0_bEES7_S7_T1_
- __ZNSt3__118__bitset_partitionB9nqe210106INS_17_ClassicAlgPolicyEPiRNS_7greaterIiEEEENS_4pairIT0_bEES7_S7_T1_
- __ZNSt3__118condition_variable8wait_forB9nqe210106IxNS_5ratioILl1ELl1000000EEEEENS_9cv_statusERNS_11unique_lockINS_5mutexEEERKNS_6chrono8durationIT_T0_EE
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI11StatContactEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI13MTParserPath_EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI14MTActionEvent_EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI15MTSlideGesture_EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI16MTForceBehavior_EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI17ContactStabilizerEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI18MTChordGestureSet_EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI20MTForceThresholding_EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI7MTPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN11HSTPipeline7ContactEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN16HSRecordingTypes9PlayFrameEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN6HSUtil7Encoder15ContainerRecordEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN6HSUtil7Encoder8KeyStateEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorINS_6atomicIPKN6HSUtil8CoderKeyEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorINS_6vectorI16MTForceBehavior_NS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorINS_6vectorIiNS1_IiEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIPKN6HSUtil8CoderKeyEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIU8__strongP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIU8__strongP8HIDEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__partial_sort_implB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointS5_EET1_S6_S6_T2_OT0_
- __ZNSt3__119__partial_sort_implB9nqe210106INS_17_ClassicAlgPolicyERNS_7greaterIfEEPfS5_EET1_S6_S6_T2_OT0_
- __ZNSt3__119__partial_sort_implB9nqe210106INS_17_ClassicAlgPolicyERNS_7greaterIiEEPiS5_EET1_S6_S6_T2_OT0_
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
- __ZNSt3__120__shared_ptr_emplaceI13MTHandMotion_NS_9allocatorIS1_EEEC2B9nqe210106IJR20MTSurfaceDimensions_R12MTParserType15MTParserOptions14MTHandIdentityRA6_KcES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI13MTPathStates_NS_9allocatorIS1_EEEC2B9nqe210106IJR20MTSurfaceDimensions_R12MTParserType15MTParserOptionsRbiES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI17MTHandStatistics_NS_9allocatorIS1_EEEC2B9nqe210106IJ14MTHandIdentityPcR12MTParserType15MTParserOptionsES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI18MTForceManagement_NS_9allocatorIS1_EEEC2B9nqe210106IJRU8__strongU13block_pointerFvi15MTClickStrengthffEES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI20MTSurfaceDimensions_NS_9allocatorIS1_EEEC2B9nqe210106IJR6MTRect6MTSizeES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI21MTPListGestureConfig_NS_9allocatorIS1_EEEC2B9nqe210106IJR12MTParserType15MTParserOptionsRbR24MTDragManagerEventQueue_ES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI6ClientNS_9allocatorIS1_EEE21__on_zero_shared_implB9nqe210106IS3_Li0EEEvv
- __ZNSt3__120__shared_ptr_emplaceI6ClientNS_9allocatorIS1_EEEC2B9nqe210106IJS1_ES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN6HSUtil12ReceiveRightENS_9allocatorIS2_EEEC2B9nqe210106IJS2_ES4_Li0EEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9nqe210106IJES4_Li0EEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9nqe210106IJRKNS2_11InvalidTypeEES4_Li0EEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9nqe210106IJRKNS2_8CopyTypeERU8__strongP6NSDataES4_Li0EEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN6HSUtil6BufferENS_9allocatorIS2_EEEC2B9nqe210106IJRKNS2_9FixedTypeERmES4_Li0EEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS7_EEEENS8_ISA_EEEC2B9nqe210106IJRmESB_Li0EEESB_DpOT_
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__120__throw_out_of_rangeB9nqe210106EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9nqe210106EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9nqe210106EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9nqe210106EPKcm
- __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB9nqe210106Ev
- __ZNSt3__126__insertion_sort_unguardedB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_S6_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEbT1_S6_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_7greaterIfEEPfEEbT1_S6_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_7greaterIiEEPiEEbT1_S6_T0_
- __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI15MTSlideGesture_EEPS3_EEED2B9nqe210106Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI16MTForceBehavior_EEPS3_EEED2B9nqe210106Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18MTChordGestureSet_EEPS3_EEED2B9nqe210106Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIiNS2_IiEEEEEEPS5_EEED2B9nqe210106Ev
- __ZNSt3__131__partition_with_equals_on_leftB9nqe210106INS_17_ClassicAlgPolicyEP7MTPointR26MTPointVelocityGreaterThanEET0_S6_S6_T1_
- __ZNSt3__131__partition_with_equals_on_leftB9nqe210106INS_17_ClassicAlgPolicyEPfRNS_7greaterIfEEEET0_S6_S6_T1_
- __ZNSt3__131__partition_with_equals_on_leftB9nqe210106INS_17_ClassicAlgPolicyEPiRNS_7greaterIiEEEET0_S6_S6_T1_
- __ZNSt3__132__partition_with_equals_on_rightB9nqe210106INS_17_ClassicAlgPolicyEP7MTPointR26MTPointVelocityGreaterThanEENS_4pairIT0_bEES7_S7_T1_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI13MTParserPath_EEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI15MTSlideGesture_EEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI16MTForceBehavior_EEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI18MTChordGestureSet_EEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqe210106INS_9allocatorI15MTSlideGesture_EEPS2_S4_S4_EET2_RT_T0_T1_S5_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqe210106INS_9allocatorINS_6vectorIiNS1_IiEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEU8__strongP7HSStageEC2B9nqe210106ERKSB_
- __ZNSt3__16__treeINS_10shared_ptrI8HSMapperEENS_4lessIS3_EENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS3_JRKS3_EEENS_4pairINS_15__tree_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE21MTGestureMotionParamsEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE7destroyEPNS_11__tree_nodeIS9_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorI14MTActionEvent_NS5_IS9_EEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SB_EENS_4lessIS7_EELb1EEENS5_ISG_EEE7destroyEPNS_11__tree_nodeISC_PvEE
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EELb1EEENS_9allocatorISC_EEE12__find_equalIS4_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISO_EERKT_
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EELb1EEENS_9allocatorISC_EEE16__construct_nodeIJSC_EEENS_10unique_ptrINS_11__tree_nodeIS8_PvEENS_22__tree_node_destructorINSH_ISO_EEEEEEDpOT_
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EELb1EEENS_9allocatorISC_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSO_SO_
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EELb1EEENS_9allocatorISC_EEE25__emplace_unique_key_argsIS4_JSC_EEENSA_INS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EELb1EEENS_9allocatorISC_EEE4findIS4_EENS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEERKT_
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringU6__weakPU33objcproto22HSServiceDirectoryable11objc_objectEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EEN6HSUtil10ObjectLessIS2_EELb1EEENS_9allocatorISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
- __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEELb1EEENS_9allocatorIS9_EEE14__erase_uniqueIiEEmRKT_
- __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEELb1EEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
- __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEELb1EEENS_9allocatorIS9_EEE21__remove_node_pointerEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEELb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIiJS9_EEENS7_INS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEELb1EEENS_9allocatorIS9_EEE5eraseENS_21__tree_const_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEE
- __ZNSt3__16__treeINS_12__value_typeIiNS_10shared_ptrI6ClientEEEENS_19__map_value_compareIiNS_4pairIKiS4_EENS_4lessIiEELb1EEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16threadC2B9nqe210106IZN6HSUtil10Connection5startEvEUlvE_JELi0EEEOT_DpOT0_
- __ZNSt3__16vectorI11StatContactNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI13MTParserPath_NS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRK12MTParserTypeRK15MTParserOptionsEEEPS1_DpOT_
- __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE16__init_with_sizeB9nqe210106IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE18__assign_with_sizeB9nqe210106IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI14MTActionEvent_NS_9allocatorIS1_EEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE18__assign_with_sizeB9nqe210106IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI15MTSlideGesture_NS_9allocatorIS1_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE22__base_destruct_at_endB9nqe210106EPS1_
- __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorI16MTForceBehavior_NS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
- __ZNSt3__16vectorI17ContactStabilizerNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI18MTChordGestureSet_NS_9allocatorIS1_EEE22__base_destruct_at_endB9nqe210106EPS1_
- __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI20MTForceThresholding_NS_9allocatorIS1_EEEC2B9nqe210106EmRKS1_
- __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE16__init_with_sizeB9nqe210106IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE18__assign_with_sizeB9nqe210106IPS2_S7_EEvT_T0_l
- __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorIN16HSRecordingTypes9PlayFrameENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN16HSRecordingTypes9PlayFrameENS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIN6HSUtil7Encoder15ContainerRecordENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN6HSUtil7Encoder15ContainerRecordENS_9allocatorIS3_EEE9push_backB9nqe210106EOS3_
- __ZNSt3__16vectorIN6HSUtil7Encoder8KeyStateENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN6HSUtil7Encoder8KeyStateENS_9allocatorIS3_EEE8__appendEm
- __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS0_I16MTForceBehavior_NS_9allocatorIS1_EEEENS2_IS4_EEEC2B9nqe210106Em
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE16__init_with_sizeB9nqe210106IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE18__assign_with_sizeB9nqe210106IPS3_S7_EEvT_T0_l
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE9push_backB9nqe210106EOS3_
- __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI12EncoderStateNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE9push_backB9nqe210106EOS5_
- __ZNSt3__16vectorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrIN6HSUtil10EncoderBufENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_6atomicIPKN6HSUtil8CoderKeyEEENS_9allocatorIS6_EEEC2B9nqe210106Em
- __ZNSt3__16vectorIPKN6HSUtil8CoderKeyENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP11objc_objectNS_9allocatorIS3_EEE9push_backB9nqe210106ERU8__strongKS2_
- __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE18__assign_with_sizeB9nqe210106IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE9push_backB9nqe210106EOS3_
- __ZNSt3__16vectorIU8__strongP8HIDEventNS_9allocatorIS3_EEE9push_backB9nqe210106ERU8__strongKS2_
- __ZNSt3__16vectorIZ34-[HSRecordingStage _stopRecording]E6RegionNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9nqe210106IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB9nqe210106IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE8__appendEm
- __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB9nqe210106ERKf
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9nqe210106IPiS5_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB9nqe210106IPiS5_EEvT_T0_l
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE8__appendEm
- __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB9nqe210106EOi
- __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB9nqe210106ERKi
- __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointLi0EEEvT1_S6_S6_S6_T0_
- __ZNSt3__18__invokeB9nqe210106IJRZN8HSMapper23_createConnectionConfigENS_8weak_ptrIS1_EEPU28objcproto17OS_dispatch_queue8NSObjectbEUlNS_10shared_ptrIN6HSUtil10ConnectionEEEE_SA_EEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSE_
- __ZNSt3__18__invokeB9nqe210106IJRZN8HSMapper23_createConnectionConfigENS_8weak_ptrIS1_EEPU28objcproto17OS_dispatch_queue8NSObjectbEUlNS_10shared_ptrIN6HSUtil10ConnectionEEEONS8_6BufferEE_SA_SB_EEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSG_
- __ZNSt3__19__sift_upB9nqe210106INS_17_ClassicAlgPolicyER26MTPointVelocityGreaterThanP7MTPointEEvT1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
- __ZNSt3__1eqB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEEbRKNS_12basic_stringIT_T0_T1_EEPKS6_
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ___33-[HSTSensingAlgs initWithConfig:]_block_invoke
- ___33-[HSTSensingAlgs initWithConfig:]_block_invoke_2
- ___33-[HSTSensingAlgs initWithConfig:]_block_invoke_3
- ___33-[HSTSensingAlgs initWithConfig:]_block_invoke_4
- ___33-[HSTSensingAlgs initWithConfig:]_block_invoke_5
- ___36-[HSTBackboardBridge initWithQueue:]_block_invoke
- ___49-[HSTServerStage initWithName:description:queue:]_block_invoke
- ___51-[HSTPencilVirtualService _dispatchHIDEventsAsync:]_block_invoke
- ___52-[HSTPencilVirtualService initWithConfig:withQueue:]_block_invoke
- ___57-[HSTPencilVirtualService setProperty:forKey:forService:]_block_invoke
- ___57-[HSTPencilVirtualService setProperty:forKey:forService:]_block_invoke_2
- ___block_descriptor_32_e20_B16?0^{__SecTask=}8l
- ___block_descriptor_40_ea8_32w_e17_v24?0i8i12f16f20lw32l8
- ___block_descriptor_56_ea8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_56_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- __block_literal_global.112
- __block_literal_global.92
- __cxx_global_var_init.100
- __cxx_global_var_init.105
- __cxx_global_var_init.113
- __cxx_global_var_init.114
- __cxx_global_var_init.115
- __cxx_global_var_init.116
- __cxx_global_var_init.123
- __cxx_global_var_init.144
- __cxx_global_var_init.152
- __cxx_global_var_init.157
- __cxx_global_var_init.166
- __cxx_global_var_init.167
- __cxx_global_var_init.180
- __cxx_global_var_init.183
- __cxx_global_var_init.197
- __cxx_global_var_init.276
- __cxx_global_var_init.282
- __cxx_global_var_init.288
- __cxx_global_var_init.294
- __cxx_global_var_init.300
- __cxx_global_var_init.306
- __cxx_global_var_init.312
- __cxx_global_var_init.321
- __cxx_global_var_init.322
- __cxx_global_var_init.330
- __cxx_global_var_init.331
- __cxx_global_var_init.340
- __cxx_global_var_init.346
- __cxx_global_var_init.360
- __cxx_global_var_init.365
- __cxx_global_var_init.560
- __cxx_global_var_init.561
- __cxx_global_var_init.562
- __cxx_global_var_init.563
- __cxx_global_var_init.58
- __cxx_global_var_init.80
- __cxx_global_var_init.88
- __cxx_global_var_init.98
- __cxx_global_var_init.99
- _dispatch_set_qos_class_fallback
- _dispatch_workloop_create_inactive
- _dispatch_workloop_set_scheduler_priority
- _kACCInfo_FirmwareVersionActive
- _kACCInfo_HardwareVersion
- _kACCInfo_Manufacturer
- _kACCInfo_Model
- _kACCInfo_Name
- _kACCInfo_SerialNumber
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _objc_msgSend$_handleHIDPencilEvents:
- _objc_msgSend$_openActuatorDevice
- _objc_msgSend$accessoryConnectionInfoFromTransport:connection:transport:
- _objc_msgSend$actuateForDictionary:strength:timeDilation:device:actuatorLimits:options:
- _objc_msgSend$actuateForID:strength:timeDilation:device:actuatorLimits:options:
- _objc_msgSend$actuateWaveform:strength:timeDilation:device:actuatorLimits:options:
- _objc_msgSend$actuationManager
- _objc_msgSend$actuationOptions
- _objc_msgSend$actuatorLimits
- _objc_msgSend$appendString:
- _objc_msgSend$coreAccessoryManager
- _objc_msgSend$coreAccessoryServiceInfoFromProperties:
- _objc_msgSend$createConnectionWithType:andIdentifier:
- _objc_msgSend$createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:
- _objc_msgSend$deregisterForDeviceManagementMatching
- _objc_msgSend$destroyConnectionWithUUID:
- _objc_msgSend$driverFirmwareVersion
- _objc_msgSend$fetchActuatorLimits
- _objc_msgSend$generateMomentumStartEventFrom:forSubtype:
- _objc_msgSend$handleActMatching:
- _objc_msgSend$handleDeviceManagementMatching:
- _objc_msgSend$initWithConfig:withQueue:
- _objc_msgSend$initWithDevice:
- _objc_msgSend$initWithDeviceID:deviceType:
- _objc_msgSend$initWithInt:
- _objc_msgSend$initWithName:description:queue:
- _objc_msgSend$innie
- _objc_msgSend$mtDeviceRef
- _objc_msgSend$productId
- _objc_msgSend$publishConnectionWithUUID:
- _objc_msgSend$publishCoreAccessoryService:
- _objc_msgSend$registerForDeviceManagementMatching
- _objc_msgSend$setAccessoryInfo:forEndpointWithUUID:
- _objc_msgSend$setActuationOptions:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setDeviceButtonState:activePathCount:
- _objc_msgSend$setDriverFirmwareVersion:
- _objc_msgSend$sharedClient
- _objc_msgSend$stringWithCapacity:
- _objc_msgSend$unpublishCoreAccessoryService
- _objc_retain_x9
CStrings:
+ "\tDHML:  P%d Waiting for slide, ZInstability=%f, TimeInstability=%f (from dtstart=%lfs)"
+ "\"!"
+ "%!"
+ "%@/%@"
+ "%{public, signpost.description:begin_time}llu algs=%s"
+ "%{public, signpost.description:begin_time}llu, %{public, signpost.description:end_time}llu"
+ "%{public, signpost.description:begin_time}llu, Finish? %{BOOL}d"
+ "%{public, signpost.description:end_time}llu, Pencil? %{BOOL}d"
+ "+[HSTFrameParser parsePathCollectionPacketV2:frame:surfaceCoordinates:]"
+ "+[HSTHelpers findAncestorHIDDeviceForService:]"
+ ", Asleep 0x%04X 0x%04X"
+ "-%@"
+ "-[ActuatorDevice createUserClientForService:]"
+ "-[ActuatorDevice fetchLimits]"
+ "-[ActuatorDevice initWithService:queue:]"
+ "-[ActuatorDevice openActuatorForService:]"
+ "-[ActuatorDevice openActuatorForService:]_block_invoke"
+ "-[ActuatorDevice setHidDevice:actuatorService:]"
+ "-[ActuatorDevice updateFirmwareClicks]"
+ "-[DeviceInfoManager fetchDeviceInfo]"
+ "-[HSTBackboardBridge initWithQueue:deviceService:log:]"
+ "-[HSTFrameParser parseExtraPayload75:frame:]"
+ "-[HSTPencilVirtualService _handleSetPropertyEvent:]"
+ "-[HSTPencilVirtualService dispatchPencilEvents:]"
+ "-[HSTServerStage initWithName:description:queue:log:]"
+ "-[HSTServerStage initWithName:description:queue:log:]_block_invoke"
+ "-[TrackpadActuatorStage _handleActuationEvent:]"
+ "-[TrackpadActuatorStage _handleHostStateEvent:]"
+ "-[TrackpadActuatorStage _updateHostClickControl]"
+ "-[TrackpadAlgButtonStateManager handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:]"
+ "-[TrackpadAlgButtonStateManager handleDragReleaseDelay:currentDeviceButtonState:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:]"
+ "-[TrackpadAlgButtonStateManager manageDragReleaseDelay:currentDeviceButtonState:rawButtonState:shouldDelayDragRelease:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:]"
+ "-[TrackpadAlgButtonStateManager updateCachedButtonState:currentDeviceTimestampSec:isTouching:]"
+ "-[TrackpadAlgButtonStateManager updateTranslationTracking:hasPointerTranslation:]"
+ "-[TrackpadAlgStage setHostClickEnabled:]"
+ "-[TrackpadFirmwareManager _setReportIntervalUs:]"
+ "-[TrackpadFirmwareManager setMouseButtonMode:buttonDivision:]"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1146: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1156: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:418: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:441: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:445: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:494: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQ4uugB6aOF9KG1EWNL125vxbF9u8lkE1Gcji5I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1139: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Multitouch/HIDSensingTouch/HSTPipeline/Helpers/HSTHelpers.mm"
+ "1Q"
+ "9170.34.1"
+ "@\"ActuationPlaylistManager\""
+ "@\"ActuatorDevice\""
+ "@\"DeviceInfoManager\""
+ "@\"HIDDevice\""
+ "@\"HIDEventService\""
+ "@\"HIDUserDevice\""
+ "@\"HSTHIDDeviceRouter\""
+ "@\"HSTSensingAlgsConfig\""
+ "@\"NSBundle\""
+ "@\"NSCondition\""
+ "@\"NSData\"16@?0@\"NSString\"8"
+ "@\"NSSet\""
+ "@\"ServiceMatcher\""
+ "@\"TrackpadAlgButtonStateManager\""
+ "@20@0:8C16"
+ "@24@0:8I16I20"
+ "@32@0:8Q16@24"
+ "@32@0:8r^{Config={SurfaceCoordinates=iiii}{SensorSize=II}}16@24"
+ "@32@0:8r^{HSTContactStabilizerConfig={FloatRange=ff}{FloatRange=ff}{FloatRange=ff}{FloatRangeGain={FloatRange=ff}f}{FloatRangeGain={FloatRange=ff}f}fffii}16@24"
+ "@32@0:8r^{HSTHIDEventGeneratorConfig={SurfaceSize=ii}}16@24"
+ "@32@0:8r^{HSTTipOffsetFilterConfig={Position=ii}}16@24"
+ "@36@0:8@16I24@28"
+ "@40@0:8I16@20C28@32"
+ "@40@0:8^{__MTDevice=}16@24@32"
+ "@40@0:8i16f20f24@28I36"
+ "@40@0:8r^{HSTPencilVirtualServiceConfig=QQQQQQQBii@B}16@24@32"
+ "@44@0:8@16I24#28@36"
+ "@44@0:8@16f24f28@32I40"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8Q16Q24Q32@?40"
+ "@48@0:8Q16Q24Q32@?<v@?@\"NSData\">40"
+ "@48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@40"
+ "@56@0:8^{__MTDevice=}16@24@32@40@?48"
+ "@?<@\"NSData\"@?@\"NSString\">16@0:8"
+ "AAPL,phandle"
+ "AHTDevice doesn't have an AHTBootloader"
+ "AHTInterface doesn't have an AHTBootloader. Trying with AHTDevice"
+ "Accessibility"
+ "ActuationLimits"
+ "ActuationPlaylist"
+ "ActuationPlaylistManager"
+ "ActuationSupported"
+ "ActuatorDevice"
+ "AlgButtonStateManager"
+ "ArtificialSurfaceSize"
+ "B20@?0@\"NSData\"8B16"
+ "B28@0:8@16B24"
+ "B32@0:8@16Q24"
+ "B48@0:8r^{SAPreciseContact=CCCcffffffffffSS}16^{Contact=CCCcQ{Position=ii}B{Velocity=ii}iiiffff}24{SurfaceCoordinates=iiii}32"
+ "B48@0:8r^{_SABinaryInjExtData=SS[0C]}16@24{SurfaceCoordinates=iiii}32"
+ "B80@0:8{Contact=CCCcQ{Position=ii}B{Velocity=ii}iiiffff}16"
+ "BlockingClicks"
+ "C20@0:8I16"
+ "CachedDeviceButtonState"
+ "Cannot create HIDUserDevice"
+ "ColorID"
+ "Configuration request received"
+ "ConsecutiveButtonUpFramesDuringDrag"
+ "ConsecutiveDebouncedUpFramesDuringDrag"
+ "Could not create chained SA config from FW info: %@"
+ "Could not create chained SA config from legacy framework info: %@"
+ "Could not recreate HSTPencilVirtualService"
+ "Could not retrieve display UUID"
+ "CurrentlyDelayingClick"
+ "CurrentlyDelayingDragRelease"
+ "Custom report routing config missing usage page or usage"
+ "Data request received for %{public}@"
+ "DeadzoneActive"
+ "DeadzoneConfig"
+ "DeadzoneRequested"
+ "DelayedButtonState"
+ "DelayedDownClickTimestampSec"
+ "DelayedDragReleaseButtonState"
+ "DeviceClassNumber"
+ "DeviceID"
+ "DeviceInfo"
+ "DeviceInfoManager"
+ "Did not find display service on first search, will arm notification and wait"
+ "DownClickDelaySec"
+ "DragReleaseDelayNumberOfFrames"
+ "DragReleaseMaxDebouncedUpFrames"
+ "Expected only one proxy HID device, but found %lu instead"
+ "Failed to add matching notification. Results=%x"
+ "Failed to allocate HIDManager"
+ "Failed to copy host state dictionary"
+ "Failed to create HIDUserDevice"
+ "Failed to create HSTSensingAlgs stage!"
+ "Failed to create notification for display service"
+ "Failed to create notification port"
+ "Failed to create notification port for display service"
+ "Failed to fetch %@ from the bootloader: %@"
+ "Failed to find AHTBootLoader for MT device"
+ "Failed to find requested data for %{public}@"
+ "Failed to find service after waiting"
+ "Failed to match display service"
+ "Failed to open proxy HIDDevice with error: %@"
+ "Failed to read digitizerID"
+ "Failed to read touchMode for digitizerID: %@"
+ "FirmwareDeviceButtonState"
+ "FirmwareUtil::GetReport 0x%x failed: Response length(%ld) did not match the expected length(%ld)"
+ "FirmwareUtil::GetReportData 0x%hhx failed: %@"
+ "FirmwareUtil::SetReport 0x%x failed: %@"
+ "FirmwareUtil::SetReportData (0x%02X) failed: %{public}s"
+ "FirmwareUtil::SetReportData 0x%x failed: %@"
+ "FirmwareUtil::SetReportData failed: Empty buffer provided"
+ "Found custom report routing config"
+ "Found custom report routing usage pair"
+ "Found display UUID in display service: %@"
+ "GesturesBlockDeviceClicks"
+ "HID work interval notification enabled"
+ "HIDPointerAccelerationMultiplier"
+ "HIDRMHash"
+ "HSStage *HSTPipeline::CreateMousePipeline(NSString *__strong _Nonnull, __strong dispatch_queue_t _Nonnull, io_service_t, HIDDevice *__strong _Nonnull, __strong os_log_t, HSStage *__strong _Nonnull)"
+ "HSStage *HSTPipeline::CreatePipeline(NSString *__strong _Nonnull, __strong dispatch_queue_t, MTDeviceRef, HIDDevice *__strong _Nonnull, __strong os_log_t, HSStage *__strong _Nonnull)"
+ "HSStage *HSTPipeline::CreateSAPipeline(NSString *__strong, __strong dispatch_queue_t, MTDeviceRef, HIDDevice *__strong, __strong os_log_t, HSStage *__strong, NSUInteger)"
+ "HSStage *HSTPipeline::CreateTrackpadPipeline(NSString *__strong, __strong dispatch_queue_t, io_service_t, HIDDevice *__strong, __strong os_log_t, HSStage *__strong)"
+ "HSTCombinedTouchModeEvent"
+ "HSTHIDDeviceRouter"
+ "HSTHelpers"
+ "HSTPencilVirtualService: Finished initialization"
+ "HSTPencilVirtualService: Virtual service enumerated (serviceID: %@)"
+ "HSTPencilVirtualService: Virtual service terminated (serviceID: %@)"
+ "HSTSensingAlgs: Correctly loaded %@ from %{public}@"
+ "HSTSensingAlgs: Framework bundle not provided in config"
+ "HSTSensingAlgs: Provided InterfaceClass %@ does not conform to SASInterfaceProtocol"
+ "HSTSensingAlgsConfig"
+ "HandedOffHostClickControl"
+ "Handling proxy HID device input report"
+ "HasFWDefinedPlaylist"
+ "Host state count does not match"
+ "HostClickEnabled"
+ "HostStateFormatVersion"
+ "I36@0:8I16d20B28I32"
+ "I60@0:8I16B20B24d28B36B40I44I48I52B56"
+ "IODeviceTree:/product"
+ "IOHIDDevice"
+ "IOHIDFamily"
+ "IOMFBUUID"
+ "IOReturn HSTPipeline::FirmwareUtil::GetReportData(HIDDevice * _Nonnull __strong, UInt8, NSMutableData * _Nonnull __strong)"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::ContinuousRecordingEnableWatch]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::DataMode]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::AwakeAsleep]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::Awake]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::FaceDetectionMode]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostClickControl]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostEvent]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostInterruptMode]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostNotificationControl]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::MTScanRate]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::MouseButtonConfig]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(HIDDevice * _Nonnull __strong, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::OneByteReport]"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReportData(HIDDevice * _Nonnull __strong, NSData * _Nonnull __strong)"
+ "IOReturn getReport(HIDDevice *__strong, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::CriticalError]"
+ "IOReturn getReport(HIDDevice *__strong, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::WaterState]"
+ "Initializing with reportIDDenyList: %@"
+ "Invalid IOService"
+ "Invalid SAFrameworkName"
+ "Invalid combined host state dictionary"
+ "Invalid dictionary parameter"
+ "LocationID"
+ "MTDevice doesn't have an AHTDevice"
+ "MTDevice doesn't have an AHTInterface"
+ "Matched HID devices for custom routing"
+ "Matched proxy HID device: %@"
+ "MaxPacketSize"
+ "Message length (%ld) is larger than external message capacity (%d)"
+ "NSArray<HSTSensingAlgsConfig *> *HSTPipeline::getSensingAlgsConfig(MTDeviceRef, NSUInteger)"
+ "NewClickBlockedDueToExistingDelay"
+ "No custom report routing specified"
+ "No matching HID devices found for custom routing"
+ "No phandleData specified for display service"
+ "No report IDs specified for custom routing"
+ "Notified of matched display service"
+ "Opened proxy HID device successfully"
+ "PersonalityID"
+ "PlatformID"
+ "PlatformId"
+ "PlaylistManager"
+ "Q20@0:8I16"
+ "RawDeviceButtonState"
+ "Received Host State: %@"
+ "Report denied by configuration"
+ "ReportDescriptor"
+ "ReportIDDenyList"
+ "ReportIDs"
+ "ReportRoutingOverrides"
+ "RunAlgs"
+ "SAChainedAlgsConfig"
+ "SAFrameworkName"
+ "SASInterfaceClassName"
+ "SanitizedDeviceButtonState"
+ "SecondsF InstabilityFilter::_timeInRange() const"
+ "SecondsF InstabilityFilter::_timeSinceLastFrame() const"
+ "SensingAlgsConfig"
+ "Sensor Surface Height"
+ "Sensor Surface Width"
+ "SerialNumberLength"
+ "ServiceMatcher"
+ "Set display UUID on pencil virtual service: %@"
+ "ShouldDelayClick"
+ "Skipping touch mode update, no change (0x%x)"
+ "Standing up legacy pad firmware manager"
+ "Standing up legacy phone firmware manager"
+ "SupportPencilFSMStateMessage"
+ "SupportsPencilFSMStateMessageID"
+ "SystemActuations"
+ "T#,&,N,V_algsClass"
+ "T@\"ActuationPlaylistManager\",&,N,V_playlistManager"
+ "T@\"ActuatorDevice\",&,N,V_actuatorDevice"
+ "T@\"ActuatorLimits\",&,N,V_limits"
+ "T@\"DeviceInfoManager\",&,N,V_deviceInfoManager"
+ "T@\"HIDDevice\",&,N,V_hidDevice"
+ "T@\"HIDDevice\",R,N,V_defaultHIDDevice"
+ "T@\"HIDDevice\",R,N,V_hidDevice"
+ "T@\"HIDEventService\",&,N,V_virtualService"
+ "T@\"HIDUserDevice\",&,N,V_userDevice"
+ "T@\"HSTCircularBuffer\",&,N,V_actuationRequestHistory"
+ "T@\"HSTSensingAlgsConfig\",&,N,V_config"
+ "T@\"NSBundle\",&,N,V_frameworkBundle"
+ "T@\"NSDictionary\",&,N,V_cachedPropertyKeys"
+ "T@\"NSDictionary\",&,N,V_fwDefinedPlaylist"
+ "T@\"NSDictionary\",&,N,V_touchModeMap"
+ "T@\"NSMutableDictionary\",&,N,V_cachedProperties"
+ "T@\"NSNumber\",&,N,V_colorID"
+ "T@\"NSNumber\",&,N,V_hardwareID"
+ "T@\"NSNumber\",&,N,V_locationID"
+ "T@\"NSNumber\",&,N,V_mtfwVersion"
+ "T@\"NSNumber\",&,N,V_productID"
+ "T@\"NSNumber\",&,N,V_vendorID"
+ "T@\"NSObject<OS_os_log>\",&,N,V_log"
+ "T@\"NSString\",&,N,V_frameworkString"
+ "T@\"NSString\",&,N,V_interfaceClassName"
+ "T@\"NSString\",&,N,V_manufacturer"
+ "T@\"NSString\",&,N,V_product"
+ "T@\"ServiceMatcher\",&,N,V_actServiceMatcher"
+ "T@\"TrackpadAlgButtonStateManager\",&,N,V_algButtonStateManager"
+ "T@?,C,N,V_matchingCallback"
+ "TB,N,V_currentlyDelayingClick"
+ "TB,N,V_currentlyDelayingDragRelease"
+ "TB,N,V_gesturesBlockDeviceButtonClicks"
+ "TB,N,V_handedOffHostClickControl"
+ "TB,N,V_isVirtualServiceEnumerated"
+ "TB,N,V_newClickBlockedDueToExistingDelay"
+ "TB,N,V_shouldRecreateVirtualService"
+ "TB,N,V_shouldTerminateVirtualService"
+ "TB,N,V_supportsActuationLimits"
+ "TB,N,V_systemActuations"
+ "TB,N,V_translationOccurredDuringClick"
+ "TB,N,V_upClickOccuredDuringDelay"
+ "TC,N,V_displayState"
+ "TI,N,V_actuatorService"
+ "TI,N,V_cachedDeviceButtonState"
+ "TI,N,V_consecutiveButtonUpFramesDuringDrag"
+ "TI,N,V_consecutiveDebouncedUpFramesDuringDrag"
+ "TI,N,V_dataPort"
+ "TI,N,V_delayedButtonState"
+ "TI,N,V_delayedDragReleaseButtonState"
+ "TI,N,V_dragReleaseDelayNumberOfFrames"
+ "TI,N,V_dragReleaseMaxDebouncedUpFrames"
+ "TI,N,V_fwDeviceButtonState"
+ "TI,N,V_options"
+ "TI,N,V_rawDeviceButtonState"
+ "TI,N,V_sanitizedDeviceButtonState"
+ "TI,N,V_serviceIterator"
+ "TI,R,N,V_service"
+ "TQ,N,V_deviceID"
+ "TQ,N,V_maxPacketSize"
+ "TQ,N,V_personalityId"
+ "TQ,N,V_platformId"
+ "TQ,N,V_revision"
+ "T^v,N,V_saFrameworkHandle"
+ "T^{IONotificationPort=},N,V_serviceMatchingNotificationPort"
+ "T^{__MTDevice=},N,V_device"
+ "Td,N,V_delayedDownClickTimestampSec"
+ "Td,R,N,V_downClickDelaySec"
+ "Touch TTW mode overridden to Off mode"
+ "TrackpadAlgButtonStateManager"
+ "TrackpadDeadzoneManager"
+ "TrackpadInactiveRegionCustomization"
+ "TranslationOccurredDuringClick"
+ "T{HSTPencilVirtualServiceConfig=QQQQQQQBii@B},N,V_config"
+ "T{optional<int>=(?=ci)B},N,V_result"
+ "UberAlgsPropertyCache"
+ "Unsupported Pencil copyEvent match event: type=0x%x, usagePage=0x%x, usage=0x%x"
+ "Unsupported copyEvent match event: type=%x, usagePage=%x, usage=%x"
+ "UpClickOccuredDuringDelay"
+ "Usage"
+ "UsagePage"
+ "User device handle report failed: %{public}@"
+ "Using SA config: %@"
+ "Using default SA config: %@"
+ "WakeOnInteriorSwipeEnabled"
+ "WakeOnSwipeDownEnabled"
+ "WakeOnSwipeLeftEnabled"
+ "WakeOnSwipeRightEnabled"
+ "WakeOnSwipeUpEnabled"
+ "WorkIntervalStart failure: %{public}s"
+ "WorkIntervalTouchDeadline"
+ "WorkIntervalTouchSpan"
+ "WorkIntervalTouchUpdatedDeadline"
+ "[0x%08llx] Failed to open HID device: %@"
+ "[HID] [MT] %s%s%s Actuation(id=%d) failed to play with error 0x%08X"
+ "[HID] [MT] %s%s%s Actuation(id=%d) was requested"
+ "[HID] [MT] %s%s%s Actuations disabled - Dropping actuation event"
+ "[HID] [MT] %s%s%s Actuator disappeared!"
+ "[HID] [MT] %s%s%s Actuator service is still busy after %d seconods"
+ "[HID] [MT] %s%s%s Enabling NC gestures!"
+ "[HID] [MT] %s%s%s Failed start actuator service matching: %@"
+ "[HID] [MT] %s%s%s Failed to determine the device ID for service 0x%llx"
+ "[HID] [MT] %s%s%s Failed to fetch actuation limits from service: 0x%x"
+ "[HID] [MT] %s%s%s Failed to fetch device info: %{public}@"
+ "[HID] [MT] %s%s%s Failed to find the parent HID device for service"
+ "[HID] [MT] %s%s%s Failed to initialize actuator: Missing queue"
+ "[HID] [MT] %s%s%s Failed to initialize ancestor HID device for 0x%08llx"
+ "[HID] [MT] %s%s%s Failed to open HID device: %{public}@"
+ "[HID] [MT] %s%s%s Failed to open actuator HID device: %@"
+ "[HID] [MT] %s%s%s Failed to open user client: 0x%X"
+ "[HID] [MT] %s%s%s Failed to parse extra payload bytes"
+ "[HID] [MT] %s%s%s Failed to request host click control: 0x%x"
+ "[HID] [MT] %s%s%s Failed to request host click via the user client: 0x%X"
+ "[HID] [MT] %s%s%s Failed to update firmware down click waveform"
+ "[HID] [MT] %s%s%s Failed to update firmware up click waveform"
+ "[HID] [MT] %s%s%s Found matching actuator service 0x%08llx"
+ "[HID] [MT] %s%s%s Handing off host click control"
+ "[HID] [MT] %s%s%s Initialized actuator service 0x%08llx"
+ "[HID] [MT] %s%s%s Received nil host state event"
+ "[HID] [MT] %s%s%s Reclaiming host click control"
+ "[HID] [MT] %s%s%s Successfully changed the device report rate to %u"
+ "[HID] [MT] %s%s%s Successfully updated mouse button config: mode=%u division=%u"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Dispatching queued downclick (button mask = %d)"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Dispatching queued upclick (button mask = %d)"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Queued downclick (button mask = %d) until %.3f sec"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Queued upclick"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] All contacts lifted during delay - releasing button immediately"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Button states: debounced=%u, raw=%u, change=%d, delaying=%d"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Canceling drag release delay"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Debounced button pressed down during delay, canceling"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Delay complete after %u consecutive raw up frames (threshold=%u, debounced=0), releasing button"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Force release after %u consecutive debounced=0 frames (max threshold=%u), releasing button"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Pointer translation detected - drag confirmed"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Raw button down during delay, resetting counter. Had %u consecutive up frames"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Raw button up, consecutive frames: %u/%u, debounced=%u"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Started delay (raw=0, debounced=1), threshold=%u"
+ "[HID] [MT] %s%s%s [DragReleaseDelay] Touch break detected - releasing immediately"
+ "^v16@0:8"
+ "^{IONotificationPort=}16@0:8"
+ "_actServiceMatcher"
+ "_actualConfig"
+ "_actuatorDevice"
+ "_actuatorService"
+ "_algButtonStateManager"
+ "_algsClass"
+ "_artificialSurfaceSize"
+ "_blockingDeviceClicks"
+ "_bootloaderForService:"
+ "_bottomDeadzonePercentage"
+ "_cachedDeviceButtonState"
+ "_cachedProperties"
+ "_cachedPropertyKeys"
+ "_calibrationDataForKey:"
+ "_cleanup"
+ "_colorID"
+ "_configureProxyHIDDeviceWithConfig:queue:"
+ "_consecutiveButtonUpFramesDuringDrag"
+ "_consecutiveDebouncedUpFramesDuringDrag"
+ "_current"
+ "_currentlyDelayingClick"
+ "_currentlyDelayingDragRelease"
+ "_dataPort"
+ "_deadzoneContacts"
+ "_defaultHIDDevice"
+ "_delayedButtonState"
+ "_delayedDownClickTimestampSec"
+ "_delayedDragReleaseButtonState"
+ "_device"
+ "_deviceInfoManager"
+ "_digitizerID"
+ "_disableTTW"
+ "_displayServiceCondition"
+ "_downClickDelaySec"
+ "_dragReleaseDelayNumberOfFrames"
+ "_dragReleaseMaxDebouncedUpFrames"
+ "_enabled"
+ "_findRoutingOverrideConfigForDevice:"
+ "_frameworkBundle"
+ "_frameworkString"
+ "_fwDefinedPlaylist"
+ "_fwDeviceButtonState"
+ "_gesturesBlockDeviceButtonClicks"
+ "_handedOffHostClickControl"
+ "_handleCombinedHostState:"
+ "_handleCombinedTouchModeEvent:"
+ "_handleConfigurationRequest:needsConfirmation:"
+ "_handleDataRequest:"
+ "_handleDisplayServiceMatched:"
+ "_handleHostState:"
+ "_handleSingleHostState:"
+ "_hardwareID"
+ "_hasPointerTranslationThisFrame"
+ "_hidDevice"
+ "_hidDeviceRouter"
+ "_hostStateFormatVersion"
+ "_inputReportHandler"
+ "_interfaceClassName"
+ "_isVirtualServiceEnumerated"
+ "_leftDeadzonePercentage"
+ "_limits"
+ "_locationID"
+ "_manufacturer"
+ "_matchDisplayServiceFrom:"
+ "_matchingCallback"
+ "_maxPacketSize"
+ "_mtfwVersion"
+ "_newClickBlockedDueToExistingDelay"
+ "_options"
+ "_overrideReportIDs"
+ "_personalityId"
+ "_platformId"
+ "_playlistManager"
+ "_previous"
+ "_product"
+ "_productID"
+ "_proxyDevice"
+ "_queueHIDPencilEventsToDispatch:"
+ "_rawDeviceButtonState"
+ "_reportIDDenyList"
+ "_revision"
+ "_rightDeadzonePercentage"
+ "_saFrameworkHandle"
+ "_sanitizedDeviceButtonState"
+ "_serviceIterator"
+ "_serviceMatchingNotificationPort"
+ "_shouldDelayClick"
+ "_shouldRecreateVirtualService"
+ "_shouldTerminateVirtualService"
+ "_supportsActuationLimits"
+ "_systemActuations"
+ "_topDeadzonePercentage"
+ "_touchModeMap"
+ "_translationOccurredDuringClick"
+ "_upClickOccuredDuringDelay"
+ "_userDevice"
+ "_vendorID"
+ "actServiceMatcher"
+ "active"
+ "actualContactBufferSize >= requiredContactBufferSize"
+ "actuateForDictionary:"
+ "actuateForID:strength:timeDilation:"
+ "actuationRequestHistory"
+ "actuatorDevice"
+ "actuatorRevisionForService:"
+ "actuatorService"
+ "algButtonStateManager"
+ "algsClass"
+ "bundleURL"
+ "c"
+ "cacheAndUpdateDeviceButtonState:currentDeviceTimestampSec:isTouching:rawButtonState:"
+ "cacheDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:isTouching:shouldDelayDragRelease:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:hasPointerTranslation:"
+ "cachedDeviceButtonState"
+ "cachedProperties"
+ "cachedPropertyKeys"
+ "canDelayClicks"
+ "cancelMatching"
+ "code"
+ "colorID"
+ "com.apple.multitouch.displayServiceMatching"
+ "commitElements:direction:error:"
+ "consecutiveButtonUpFramesDuringDrag"
+ "consecutiveDebouncedUpFramesDuringDrag"
+ "createUserClientForService:"
+ "createUserDevice:platformId:"
+ "currentlyDelayingClick"
+ "currentlyDelayingDragRelease"
+ "dataPort"
+ "dataRequestCallback"
+ "dataValue"
+ "dataWithLength:"
+ "dateWithTimeIntervalSinceNow:"
+ "defaultHIDDevice"
+ "delayDownClick:until:"
+ "delayedButtonState"
+ "delayedDownClickIsQueued"
+ "delayedDownClickTimestampSec"
+ "delayedDragReleaseButtonState"
+ "destoryUserClient"
+ "deviceIDForService:"
+ "deviceInfoManager"
+ "deviceRouter"
+ "dictionaryWithCapacity:"
+ "digitizerID"
+ "dispatchPencilEvents:"
+ "displayState"
+ "displayUUID"
+ "downClickDelaySec"
+ "dragReleaseDelayNumberOfFrames"
+ "dragReleaseMaxDebouncedUpFrames"
+ "elementsMatching:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "extraPayloadOffset + extraPayloadLength == data.length"
+ "fetchDeviceInfo"
+ "fetchLimits"
+ "findAncestorHIDDeviceForService:"
+ "firstObject"
+ "frameworkBundle"
+ "frameworkString"
+ "fwDefinedPlaylist"
+ "fwDeviceButtonState"
+ "gesturesBlockDeviceButtonClicks"
+ "getBootLoader"
+ "getChainedAlgsConfig: Framework bundle has no Info.plist"
+ "getChainedAlgsConfig: config is not an array"
+ "getDeviceInServiceTree:"
+ "getInterfaceInServiceTree:"
+ "getProperty:property:options:error:"
+ "getReport:reportLength:withIdentifier:forType:error:"
+ "handedOffHostClickControl"
+ "handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:"
+ "handleDragReleaseDelay:currentDeviceButtonState:rawButtonState:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:"
+ "handleReport:error:"
+ "handleResetEvent:"
+ "hardwareID"
+ "header.num_contacts <= Contact::MaxContactCount"
+ "header.signature == ContactFrame75::ExtraPayload::Header::Signature"
+ "header.type != ContactFrame75::ExtraPayload::PayloadType::kPayloadTypeExtended"
+ "hid-workgroup-interval"
+ "hidDevice"
+ "hidDeviceForReportID:"
+ "hidDeviceKeys"
+ "hidElementMatchingUsagePage:usage:"
+ "i20@0:8B16"
+ "i28@0:8C16@20"
+ "i28@0:8i16f20f24"
+ "i40@?0q8q16r^v24q32"
+ "ignoredDescriptionProperties"
+ "infoDictionary"
+ "initWithBytes:length:"
+ "initWithConfig:log:"
+ "initWithConfig:queue:log:"
+ "initWithConfig:withQueue:log:"
+ "initWithData:"
+ "initWithData:encoding:"
+ "initWithDevice:hidDevice:queue:log:inputReportHandler:"
+ "initWithDevice:hidDeviceRouter:log:"
+ "initWithDeviceType:"
+ "initWithDomain:code:userInfo:"
+ "initWithKey:value:"
+ "initWithLog:"
+ "initWithName:description:queue:log:"
+ "initWithPlaybackQueue:log:"
+ "initWithProperties:"
+ "initWithQueue:deviceService:log:"
+ "initWithQueue:log:"
+ "initWithQueue:matchingCallback:"
+ "initWithRevision:fwDefinedPlaylist:"
+ "initWithService:hidDevice:"
+ "initWithService:hidDevice:deviceType:settings:"
+ "initWithService:queue:"
+ "initWithStreamSize:platformId:personalityId:streamCallback:"
+ "initWithTouchModeMap:"
+ "interfaceClassName"
+ "isContactInDeadzone:"
+ "isVirtualServiceEnumerated"
+ "lastObject"
+ "limits"
+ "loadFrameworkBundle: Failed to dlopen dylib at %{public}@"
+ "loadFrameworkBundle: Successfully dlopen'd dylib at %{public}@"
+ "loadFrameworkBundle: Unable to load SensingAlgs bundle from %{public}@"
+ "localizedDescription"
+ "locationID"
+ "log"
+ "manageDragReleaseDelay:currentDeviceButtonState:rawButtonState:shouldDelayDragRelease:dragReleaseDelayNumberOfFrames:dragReleaseMaxDebouncedUpFrames:isTouching:"
+ "manufacturer"
+ "matchingCallback"
+ "maxPacketSize"
+ "mtService != IO_OBJECT_NULL"
+ "mtfwVersion"
+ "mutableBytes"
+ "newClickBlockedDueToExistingDelay"
+ "numberFromString:"
+ "numberWithInteger:"
+ "open"
+ "openActuatorForService:"
+ "openWithOptions:error:"
+ "parameterizedWaveformForDictionary:strength:timeDilation:actuatorLimits:options:"
+ "parameterizedWaveformForID:strength:timeDilation:actuatorLimits:options:"
+ "parseExtraPayload75:frame:"
+ "parsePathCollectionPacketV2:frame:surfaceCoordinates:"
+ "parseSABinary:"
+ "parseSAPreciseContact:toContact:surfaceCoordinates:"
+ "parser-options"
+ "pathData.size >= sizeof(PathCollectionV2Packet)"
+ "payloadOffset + payloadLength <= data.length"
+ "personalityId"
+ "platformId"
+ "playlistManager"
+ "populateDeviceInfoFrom:"
+ "product"
+ "productID"
+ "propertyForKey:"
+ "rawDeviceButtonState"
+ "registryNumberPropertyForKey:"
+ "registryPropertyForKey:fromService:"
+ "registryPropertyForKey:fromService:expectedClass:defaultValue:"
+ "registryStringPropertyForKey:"
+ "resetDragReleaseDelayState:"
+ "ret == KERN_SUCCESS"
+ "revision"
+ "saFrameworkHandle"
+ "sanitizedDeviceButtonState"
+ "service != IO_OBJECT_NULL"
+ "service-display"
+ "serviceIterator"
+ "serviceMatchingNotificationPort"
+ "serviceSupportsActuationLimits:"
+ "serviceSupportsActuations:"
+ "setActServiceMatcher:"
+ "setActuationRequestHistory:"
+ "setActuatorDevice:"
+ "setActuatorService:"
+ "setAlgButtonStateManager:"
+ "setAlgsClass:"
+ "setCachedDeviceButtonState:"
+ "setCachedProperties:"
+ "setCachedPropertyKeys:"
+ "setColorID:"
+ "setConsecutiveButtonUpFramesDuringDrag:"
+ "setConsecutiveDebouncedUpFramesDuringDrag:"
+ "setCurrentlyDelayingClick:"
+ "setCurrentlyDelayingDragRelease:"
+ "setDataPort:"
+ "setDataRequestCallback:"
+ "setDelayedButtonState:"
+ "setDelayedDownClickTimestampSec:"
+ "setDelayedDragReleaseButtonState:"
+ "setDevice:"
+ "setDeviceID:"
+ "setDeviceInfoManager:"
+ "setDisplayState:"
+ "setDragReleaseDelayNumberOfFrames:"
+ "setDragReleaseMaxDebouncedUpFrames:"
+ "setFrameworkBundle:"
+ "setFrameworkString:"
+ "setFwDefinedPlaylist:"
+ "setFwDeviceButtonState:"
+ "setGesturesBlockDeviceButtonClicks:"
+ "setHandedOffHostClickControl:"
+ "setHardwareID:"
+ "setHidDevice:"
+ "setHidDevice:actuatorService:"
+ "setInputReportHandler:"
+ "setInterfaceClassName:"
+ "setIsVirtualServiceEnumerated:"
+ "setLimits:"
+ "setLocationID:"
+ "setLog:"
+ "setManufacturer:"
+ "setMatchingCallback:"
+ "setMaxPacketSize:"
+ "setMtfwVersion:"
+ "setNewClickBlockedDueToExistingDelay:"
+ "setOptions:"
+ "setPersonalityId:"
+ "setPlatformId:"
+ "setPlaylistManager:"
+ "setProduct:"
+ "setProductID:"
+ "setRawDeviceButtonState:"
+ "setRemovalHandler:"
+ "setReport:reportLength:withIdentifier:forType:error:"
+ "setRevision:"
+ "setSaFrameworkHandle:"
+ "setSanitizedDeviceButtonState:"
+ "setServiceIterator:"
+ "setServiceMatchingNotificationPort:"
+ "setSetReportHandler:"
+ "setShouldRecreateVirtualService:"
+ "setShouldTerminateVirtualService:"
+ "setSupportsActuationLimits:"
+ "setSystemActuations:"
+ "setTouchModeMap:"
+ "setTranslationOccurredDuringClick:"
+ "setUpClickOccuredDuringDelay:"
+ "setUserDevice:"
+ "setVendorID:"
+ "setWaveform:waveform:"
+ "setWithArray:"
+ "shouldBlockClicks"
+ "shouldRecreateVirtualService"
+ "shouldTerminateVirtualService"
+ "signal"
+ "startMatchingWithDictionary:"
+ "stringByDeletingPathExtension"
+ "stringWithString:"
+ "subdataWithRange:"
+ "systemActuations"
+ "touchModeMap"
+ "translationOccurredDuringClick"
+ "upClickOccuredDuringDelay"
+ "updateArtificialSurfaceSize"
+ "updateCachedButtonState:currentDeviceTimestampSec:isTouching:"
+ "updateClickDelayState:"
+ "updateFirmwareClicks"
+ "updateFwButtonStateTo:"
+ "updateMomentumStartForEvent:forSubtype:"
+ "updateTranslationTracking:hasPointerTranslation:"
+ "userDevice"
+ "v104@0:8{HSTPencilVirtualServiceConfig=QQQQQQQBii@B}16"
+ "v12@?0I8"
+ "v16@?0@\"HSTFrame\"8"
+ "v20@?0i8f12f16"
+ "v24@0:8#16"
+ "v24@0:8@?<@\"NSData\"@?@\"NSString\">16"
+ "v24@0:8I16B20"
+ "v24@0:8^{IONotificationPort=}16"
+ "v24@0:8^{__MTDevice=}16"
+ "v24@0:8d16"
+ "v24@0:8{optional<int>=(?=ci)B}16"
+ "v28@0:8@16I24"
+ "v28@0:8@16i24"
+ "v28@0:8I16d20"
+ "v32@0:8I16d20B28"
+ "v32@?0@\"NSString\"8@\"HIDElement\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSObject\"16^B24"
+ "v32@?0@8@\"NSDictionary\"16^B24"
+ "v40@0:8C16I20B24B28d32"
+ "v40@0:8C16I20I24I28I32B36"
+ "v44@0:8C16I20I24B28I32I36B40"
+ "v48@0:8^{__IOHIDEvent=}16r^{MTParserPath_=^^?C{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}{?=ddddddd}dIII{MTForceFilter_=^^?ffffffffff}f{MTPoint=ff}IBBBBf{MTPoint=ff}f{MTPoint=ff}f{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}ff{MTPoint=ff}f{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}f{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}ffffBBBBBBBfff}24I32Q36B44"
+ "v48@?0@\"HIDDevice\"8Q16q24q32@\"NSData\"40"
+ "valueForKey:"
+ "valueString"
+ "vendorID"
+ "virtualEventServiceWithDelegate:"
+ "virtualServiceDispatchEvent:"
+ "virtualServiceTerminate"
+ "void InstabilityFilter::update(HSTPipeline::Microseconds, const Contact &, bool)"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::ContinuousRecordingEnableWatch]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::DataMode]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::AwakeAsleep]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::Awake]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::FaceDetectionMode]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostEvent]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostInterruptMode]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostNotificationControl]"
+ "void setReport(HIDDevice *__strong, const T &, NSSet *__strong) [T = HSTPipeline::FirmwareInterface::FeatureReport::OneByteReport]"
+ "void setReportWithData(HSTHIDDeviceRouter *__strong, NSData *__strong, NSSet *__strong)"
+ "waitUntilDate:"
+ "workIntervalCancel failure: %{public}s"
+ "workIntervalFinish failure: %{public}s"
+ "workIntervalUpdate failure: %{public}s"
+ "workIntervalUpdate:complexity:"
+ "workgroup_interval_force_disable"
+ "workgroup_interval_force_enable"
+ "{?=\"hidEventService\"@\"HIDEventService\"\"hidDevice\"@\"HIDDevice\"\"service\"{SendRight=\"_vptr$PortRight\"^^?\"_mp\"I}\"queue\"@\"NSObject<OS_dispatch_queue>\"\"dispatcher\"@\"<HIDEventDispatcher>\"\"cancelHandler\"@?\"device\"@\"source\"@\"NSObject<OS_dispatch_source>\"\"pipeline\"@\"HSStage\"\"recording\"@\"HSTRecordingManager\"\"pencilVirtualService\"@\"HSTPencilVirtualService\"\"sysdiagnoseNotifyToken\"i\"formatter\"@\"NSDateFormatter\"\"requestedProperties\"@\"NSArray\"\"recordedProperties\"@\"NSMutableArray\"\"recordedPropertiesCount\"@\"NSMutableDictionary\"\"cachedSetProperties\"@\"NSMutableArray\"\"debugProperties\"@\"NSMutableDictionary\"\"deviceID\"Q\"builtIn\"B\"deviceType\"C\"widthMm\"i\"heightMm\"i\"hidEventsToSyncDispatch\"@\"NSMutableArray\"\"hidPencilEventsToSyncDispatch\"@\"NSMutableArray\"\"syncDispatch\"B\"dispatchCollection\"B\"enableHIDWorkInterval\"B\"hidWorkIntervalTouchTimeoutUs\"Q\"hidWorkIntervalStylusTimeoutUs\"Q\"workIntervalStartTime\"Q\"workIntervalStartTimeContinuous\"Q\"wasPencilPresent\"B\"didPencilAppear\"B\"displayServiceMatched\"B\"displayUUID\"@\"NSString\"}"
+ "{?=\"poweredWhenScreenOff\"B\"touchMode\"I\"prevTouchMode\"I\"screenOrientation\"C\"stockholmState\"C\"wirelessChargingState\"C\"usbChargingState\"C\"stuckTouchDetectorState\"C\"imagesEnabled\"B\"reportAlwaysEnabled\"B\"filteredClients\"B\"supportsEnabledInputsReport\"B}"
+ "{?=\"touchMode\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"screenOrientation\"{optional<HSTPipeline::ScreenOrientation>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"motionState\"{optional<HSTPipeline::MotionState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"touchHand\"{optional<HSTPipeline::TouchHand>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"wristState\"{optional<HSTPipeline::WristState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"stockholmState\"{optional<HSTPipeline::StockholmState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"wirelessChargingState\"{optional<HSTPipeline::WirelessChargingState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"usbChargingState\"{optional<HSTPipeline::USBChargingState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"stuckTouchDetectorState\"{optional<HSTPipeline::StuckTouchDetectorState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}}"
+ "{HSTContactFrameMetadata=\"surfaceSize\"{optional<HSTPipeline::SurfaceSize>=\"\"(?=\"__null_state_\"c\"__val_\"{SurfaceSize=\"width\"i\"height\"i})\"__engaged_\"B}\"image\"{optional<HSTContactFrameMetadata::Image>=\"\"(?=\"__null_state_\"c\"__val_\"{Image=\"sensorSize\"{SensorSize=\"width\"I\"height\"I}\"dataOffset\"Q})\"__engaged_\"B}\"tritium\"{optional<HSTContactFrameMetadata::Tritium3>=\"\"(?=\"__null_state_\"c\"__val_\"{Tritium3=\"version\"C\"gestureType\"i\"initialToCurrentFrameDeltaMs\"I})\"__engaged_\"B}\"buttonState\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"rawButtonState\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}}"
+ "{HSTPencilVirtualServiceConfig=\"vendorID\"Q\"productID\"Q\"ownerRegistryID\"Q\"minForce\"Q\"accurateMaxForce\"Q\"extendedMaxForce\"Q\"maxHoverHeight\"Q\"hoverDisabled\"B\"widthMm\"i\"heightMm\"i\"displayUUID\"@\"NSString\"\"supportsPencilFSMStateMessage\"B}"
+ "{HSTPencilVirtualServiceConfig=QQQQQQQBii@B}16@0:8"
+ "{optional<int>=\"\"(?=\"__null_state_\"c\"__val_\"i)\"__engaged_\"B}"
+ "{optional<int>=(?=ci)B}16@0:8"
+ "\x911"
+ "\xf0\xd1A"
- "\tDHML:  P%d Wating for slide, ZInstability=%f, TimeInstability=%f (from dtstart=%lfs)"
- "%04X"
- ", Alseep 0x%04X 0x%04X"
- "-[CoreAccessoryManager coreAccessoryServiceInfoFromProperties:]"
- "-[CoreAccessoryManager dealloc]"
- "-[CoreAccessoryManager deregisterForDeviceManagementMatching]"
- "-[CoreAccessoryManager handleDeviceManagementMatching:]"
- "-[CoreAccessoryManager publishCoreAccessoryService:]"
- "-[CoreAccessoryManager registerForDeviceManagementMatching]"
- "-[CoreAccessoryManager unpublishCoreAccessoryService]"
- "-[HSTBackboardBridge initWithQueue:]"
- "-[HSTPencilVirtualService _handleHIDPencilEvents:]"
- "-[HSTServerStage initWithName:description:queue:]"
- "-[HSTServerStage initWithName:description:queue:]_block_invoke"
- "9150.2"
- "@\"ActuationManager\""
- "@\"CoreAccessoryManager\""
- "@\"HIDVirtualEventService\""
- "@24@0:8^{__MTDevice={__CFRuntimeBase=QAQ}IIB^{__MTActuator}BBBBIIIIQIIIIIIII^{__CFString}{?=BB}BBBBBBIIBBBBBBBB*d^{__ALGLibraryState}IQCIqIIIISBii[20{MTSensorRegion=CCCCCC(?=CC)}]{MTSensorRegionThresholds=sss}{MTSensorSurfaceDescriptor=IIssss}I^{MTParsedMultitouchFrameRep_t}{__MTDeviceCallbacksStruct=[21{__MTDeviceCallbackRecord=(?=[4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?]^?[4^?])C[4^v]}]i[4S]f[4S]f[4{ImageCallbackFilter=II}][5f][5{MTStatisticParameters=ff}][5*]B{?=iII}}^{__CFMachPort}^{__CFString}^{__CFRunLoopSource}B^{__CFRunLoop}[3I]CiiBIBIB@i^{__CFData}QQQCBB[5I][5I]^vQB^vB{?=i*I{MTBinaryFrameHeader={MTBinaryHeader=CCCCI}{MTImagePathContentOptions=CCCC}SSCCsSsC}I[32{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}]I[32^{?}]{?=*IS}}[7C]CQ^{work_interval}IBC^{__CFDictionary}}16"
- "@24@0:8r^{HSTContactStabilizerConfig={FloatRange=ff}{FloatRange=ff}{FloatRange=ff}{FloatRangeGain={FloatRange=ff}f}{FloatRangeGain={FloatRange=ff}f}fffii}16"
- "@24@0:8r^{HSTHIDEventGeneratorConfig={SurfaceSize=ii}}16"
- "@24@0:8r^{HSTSensingAlgsConfig=QQ@^{__MTDevice}}16"
- "@24@0:8r^{HSTTipOffsetFilterConfig={Position=ii}}16"
- "@28@0:8@16i24"
- "@28@0:8Q16C24"
- "@32@0:8r^{HSTPencilVirtualServiceConfig=QQQQQQQBii}16@24"
- "AID"
- "Actuation(id=%d) failed to play with error 0x%08X (deviceID 0x%llX)"
- "Actuation(id=%d) was requested (deviceID 0x%llX)"
- "ActuationManager"
- "Actuations disabled - Dropping actuation event (deviceID 0x%llX)"
- "Actuator matched - 0x%08llx, actuations enabled : %s"
- "AlgHostClickMode"
- "Apple Inc."
- "AppleDeviceManagementHIDEventService"
- "B20@0:8S16"
- "Bluetooth"
- "BluetoothLowEnergy"
- "ConnectionUUID"
- "CoreAccessoryManager"
- "CoreAccessoryManager.mm"
- "Error 0x%08X sending external message"
- "Failed to add actuator matching notification"
- "Failed to fetch device published actuation limits with error 0x%08X (deviceID 0x%llX)"
- "Failed to open actuator - 0x%08x"
- "Failed to update host click control displayState=%hhu status=0x%08X (deviceID 0x%llX)"
- "FirmwareHostClickMode"
- "FirmwareUtil.mm"
- "FirmwareUtil::SetReport 0x%x failed: 0x%x"
- "HSStage *HSTPipeline::CreateMousePipeline(NSString *__strong, __strong dispatch_queue_t, MTDeviceRef, HSStage *__strong)"
- "HSStage *HSTPipeline::CreatePipeline(NSString *__strong, __strong dispatch_queue_t, MTDeviceRef, HSStage *__strong)"
- "HSStage *HSTPipeline::CreateSAPipeline(NSString *__strong, __strong dispatch_queue_t, MTDeviceRef, HSStage *__strong, NSUInteger)"
- "HSStage *HSTPipeline::CreateTrackpadPipeline(NSString *__strong, __strong dispatch_queue_t, MTDeviceRef, HSStage *__strong)"
- "HSTPencilVirtualService: Calling cancel handler"
- "HSTSensingAlgs: Correctly loaded %{public}@"
- "HSTSensingAlgs: Provided InterfaceClass does not conform to SASInterfaceProtocol"
- "HSTSensingAlgs: Unable to load SensingAlgsService from %{public}@"
- "Handing off host click control (deviceID 0x%llX)"
- "IONameMatch"
- "IOReturn HSTPipeline::FirmwareUtil::GetReport(MTDeviceRef _Nonnull, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::CriticalError]"
- "IOReturn HSTPipeline::FirmwareUtil::GetReport(MTDeviceRef _Nonnull, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::MTScanRate]"
- "IOReturn HSTPipeline::FirmwareUtil::GetReport(MTDeviceRef _Nonnull, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::WaterState]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::ContinuousRecordingEnableWatch]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::DataMode]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::AwakeAsleep]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::Awake]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::FaceDetectionMode]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostEvent]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostInterruptMode]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostNotificationControl]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::MTScanRate]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::MouseButtonConfig]"
- "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::OneByteReport]"
- "IOReturn getReport(MTDeviceRef, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::CriticalError]"
- "IOReturn getReport(MTDeviceRef, T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::WaterState]"
- "MultitouchDriverFirmwareVersion"
- "NSData * _Nullable HSTPipeline::FirmwareUtil::GetReportData(MTDeviceRef _Nonnull, NSInteger, IOReturn * _Nullable)"
- "PowerFW Version"
- "Properties"
- "PublishedAccessoryInfo"
- "RadioFW Version"
- "Received nil host state event (deviceID 0x%llX)"
- "Reclaiming host click control (deviceID 0x%llX)"
- "STFW Version"
- "Skip actuator setup - 0x%08llx"
- "Successfully changed the device report rate to %u (deviceID 0x%llX)"
- "Successfully updated mouse button config: mode=%u division=%u (deviceID 0x%llX)"
- "T@\"ActuationManager\",&,N,V_actuationManager"
- "T@\"ActuatorLimits\",R,N,V_actuatorLimits"
- "T@\"CoreAccessoryManager\",&,N,V_coreAccessoryManager"
- "T@\"HIDVirtualEventService\",&,N,V_virtualService"
- "T@\"NSNumber\",&,N,V_productId"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_innie"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_outie"
- "T@\"NSString\",&,N,V_driverFirmwareVersion"
- "TI,N,V_actuationOptions"
- "TI,R,N,V_deviceButtonState"
- "TQ,R,N,V_deviceID"
- "T^{__MTDevice=},R,N,V_mtDeviceRef"
- "T{HSTPencilVirtualServiceConfig=QQQQQQQBii},N,V_config"
- "T{HSTSensingAlgsConfig=QQ@^{__MTDevice}},N,V_config"
- "Unsuported Pencil copyEvent match event: type=0x%x, usagePage=0x%x, usage=0x%x"
- "Unsuported copyEvent match event: type=%x, usagePage=%x, usage=%x"
- "WorkIntervalCancel"
- "WorkIntervalFinish"
- "WorkIntervalStart"
- "[HID] [MT] %s%s%s Enablng NC gestures!"
- "[HID] [MT] %s%s%s [%{public}@] Could not create CoreAccessory connection"
- "[HID] [MT] %s%s%s [%{public}@] Could not create CoreAccessory endpoint"
- "[HID] [MT] %s%s%s [%{public}@] Existing device has already been published - Unpublishing previous device first"
- "[HID] [MT] %s%s%s [%{public}@] Failed to create notification port for device"
- "[HID] [MT] %s%s%s [%{public}@] Failed to create notification port: 0x%08x (deviceIterator: 0x%08jx)"
- "[HID] [MT] %s%s%s [%{public}@] Failed to determine MTFW version"
- "[HID] [MT] %s%s%s [%{public}@] Failed to retrieve the properties from device management service"
- "[HID] [MT] %s%s%s [%{public}@] Found multiple device management services expected only one"
- "[HID] [MT] %s%s%s [%{public}@] Published device %{public}@ with connection UUID %{public}@"
- "[HID] [MT] %s%s%s [%{public}@] Registering for device mangement matching notifications"
- "[HID] [MT] %s%s%s [%{public}@] Successfully registered for device mangement matching notifications"
- "[HID] [MT] %s%s%s [%{public}@] Unpublishing device with connection UUID %{public}@"
- "[HID] [MT] %s%s%s [%{public}@] enter"
- "[HID] [MT] %s%s%s ~%@"
- "^{__MTActuator={__CFRuntimeBase=QAQ}III^{__MTDevice}^{__CFDictionary}BQiI}"
- "^{__MTDevice={__CFRuntimeBase=QAQ}IIB^{__MTActuator}BBBBIIIIQIIIIIIII^{__CFString}{?=BB}BBBBBBIIBBBBBBBB*d^{__ALGLibraryState}IQCIqIIIISBii[20{MTSensorRegion=CCCCCC(?=CC)}]{MTSensorRegionThresholds=sss}{MTSensorSurfaceDescriptor=IIssss}I^{MTParsedMultitouchFrameRep_t}{__MTDeviceCallbacksStruct=[21{__MTDeviceCallbackRecord=(?=[4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?]^?[4^?])C[4^v]}]i[4S]f[4S]f[4{ImageCallbackFilter=II}][5f][5{MTStatisticParameters=ff}][5*]B{?=iII}}^{__CFMachPort}^{__CFString}^{__CFRunLoopSource}B^{__CFRunLoop}[3I]CiiBIBIB@i^{__CFData}QQQCBB[5I][5I]^vQB^vB{?=i*I{MTBinaryFrameHeader={MTBinaryHeader=CCCCI}{MTImagePathContentOptions=CCCC}SSCCsSsC}I[32{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}]I[32^{?}]{?=*IS}}[7C]CQ^{work_interval}IBC^{__CFDictionary}}"
- "_actDevice"
- "_actuationManager"
- "_actuationOptions"
- "_actuationsEnabled"
- "_actuatorEntryID"
- "_actuatorLimits"
- "_actuatorMatchedIterator"
- "_actuatorMatchedNotifierPortRef"
- "_connectionUUID"
- "_coreAccessoryManager"
- "_dmMatchedIterator"
- "_dmMatchedNotifierPortRef"
- "_driverFirmwareVersion"
- "_handleHIDPencilEvents:"
- "_innie"
- "_mtDevice"
- "_mtDeviceRef"
- "_openActuatorDevice"
- "_outie"
- "_productId"
- "_publishedAccessoryInfo"
- "_timeInRange"
- "accessoryConnectionInfoFromTransport:connection:transport:"
- "actuateForDictionary:strength:timeDilation:device:actuatorLimits:options:"
- "actuateForID:strength:timeDilation:device:actuatorLimits:options:"
- "actuateWaveform:strength:timeDilation:device:actuatorLimits:options:"
- "actuationManager"
- "actuationOptions"
- "actuatorLimits"
- "appendString:"
- "b"
- "com.apple.hid.PencilVirtualEventService"
- "coreAccessoryManager"
- "coreAccessoryServiceInfoFromProperties:"
- "createConnectionWithType:andIdentifier:"
- "createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:"
- "deregisterForDeviceManagementMatching"
- "destroyConnectionWithUUID:"
- "driverFirmwareVersion"
- "fetchActuatorLimits"
- "generateMomentumStartEventFrom:forSubtype:"
- "handleActMatching:"
- "handleDeviceManagementMatching:"
- "i48@0:8i16f20f24^{__MTActuator=}28@36I44"
- "i52@0:8@16f24f28^{__MTActuator=}32@40I48"
- "initWithConfig:withQueue:"
- "initWithDevice:"
- "initWithDeviceID:deviceType:"
- "initWithInt:"
- "initWithService:settings:"
- "innie"
- "mtDeviceRef"
- "outie"
- "prefsDomain"
- "productId"
- "publishConnectionWithUUID:"
- "publishCoreAccessoryService:"
- "registerForDeviceManagementMatching"
- "scale"
- "setAccessoryInfo:forEndpointWithUUID:"
- "setActuationManager:"
- "setActuationOptions:"
- "setCoreAccessoryManager:"
- "setDelegate:"
- "setDeviceButtonState:activePathCount:"
- "setDriverFirmwareVersion:"
- "setInnie:"
- "setOutie:"
- "setProductId:"
- "sharedClient"
- "start: %llu"
- "stringWithCapacity:"
- "unpublishCoreAccessoryService"
- "v24@0:8I16I20"
- "v24@?0i8i12f16f20"
- "v40@0:8@16^i24^i32"
- "v48@0:8^{__IOHIDEvent=}16r^{MTParserPath_=^^?ii{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}{?=ddddddd}dIII{MTForceFilter_=^^?ffffffffff}f{MTPoint=ff}IBBBBf{MTPoint=ff}f{MTPoint=ff}f{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}ff{MTPoint=ff}f{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}f{MTPoint=ff}{MTPoint=ff}{MTPoint=ff}ffffBBBBBBBfff}24I32Q36B44"
- "v48@0:8{HSTSensingAlgsConfig=QQ@^{__MTDevice}}16"
- "v88@0:8{HSTPencilVirtualServiceConfig=QQQQQQQBii}16"
- "void HSTPipeline::FirmwareUtil::SetReportWithData(MTDeviceRef _Nonnull, NSData * _Nonnull __strong)"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::ContinuousRecordingEnableWatch]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::DataMode]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::AwakeAsleep]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::EnabledInputs::Awake]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::FaceDetectionMode]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostEvent]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostInterruptMode]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::HostNotificationControl]"
- "void setReport(MTDeviceRef, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::OneByteReport]"
- "{?=\"hidEventService\"@\"HIDEventService\"\"service\"{SendRight=\"_vptr$PortRight\"^^?\"_mp\"I}\"queue\"@\"NSObject<OS_dispatch_queue>\"\"dispatcher\"@\"<HIDEventDispatcher>\"\"cancelHandler\"@?\"device\"@\"source\"@\"NSObject<OS_dispatch_source>\"\"pipeline\"@\"HSStage\"\"recording\"@\"HSTRecordingManager\"\"sysdiagnoseNotifyToken\"i\"formatter\"@\"NSDateFormatter\"\"requestedProperties\"@\"NSArray\"\"recordedProperties\"@\"NSMutableArray\"\"recordedPropertiesCount\"@\"NSMutableDictionary\"\"cachedSetProperties\"@\"NSMutableArray\"\"debugProperties\"@\"NSMutableDictionary\"\"deviceID\"Q\"builtIn\"B\"deviceType\"C\"widthMm\"i\"heightMm\"i\"hidEventsToSyncDispatch\"@\"NSMutableArray\"\"syncDispatch\"B\"dispatchCollection\"B\"enableHIDWorkInterval\"B\"hidWorkIntervalTouchTimeoutUs\"Q\"hidWorkIntervalStylusTimeoutUs\"Q\"workIntervalStartTime\"Q}"
- "{?=\"poweredWhenScreenOff\"B\"touchMode\"S\"prevTouchMode\"S\"screenOrientation\"C\"stockholmState\"C\"wirelessChargingState\"C\"usbChargingState\"C\"stuckTouchDetectorState\"C\"imagesEnabled\"B\"reportAlwaysEnabled\"B\"filteredClients\"B}"
- "{?=\"touchMode\"{optional<unsigned short>=\"\"(?=\"__null_state_\"c\"__val_\"S)\"__engaged_\"B}\"screenOrientation\"{optional<HSTPipeline::ScreenOrientation>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"motionState\"{optional<HSTPipeline::MotionState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"touchHand\"{optional<HSTPipeline::TouchHand>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"wristState\"{optional<HSTPipeline::WristState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"stockholmState\"{optional<HSTPipeline::StockholmState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"wirelessChargingState\"{optional<HSTPipeline::WirelessChargingState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"usbChargingState\"{optional<HSTPipeline::USBChargingState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}\"stuckTouchDetectorState\"{optional<HSTPipeline::StuckTouchDetectorState>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}}"
- "{HSTContactFrameMetadata=\"surfaceSize\"{optional<HSTPipeline::SurfaceSize>=\"\"(?=\"__null_state_\"c\"__val_\"{SurfaceSize=\"width\"i\"height\"i})\"__engaged_\"B}\"image\"{optional<HSTContactFrameMetadata::Image>=\"\"(?=\"__null_state_\"c\"__val_\"{Image=\"sensorSize\"{SensorSize=\"width\"I\"height\"I}\"dataOffset\"Q})\"__engaged_\"B}\"tritium\"{optional<HSTContactFrameMetadata::Tritium3>=\"\"(?=\"__null_state_\"c\"__val_\"{Tritium3=\"version\"C\"gestureType\"i\"initialToCurrentFrameDeltaMs\"I})\"__engaged_\"B}\"buttonState\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}}"
- "{HSTPencilVirtualServiceConfig=\"vendorID\"Q\"productID\"Q\"ownerRegistryID\"Q\"minForce\"Q\"accurateMaxForce\"Q\"extendedMaxForce\"Q\"maxHoverHeight\"Q\"hoverDisabled\"B\"widthMm\"i\"heightMm\"i}"
- "{HSTPencilVirtualServiceConfig=QQQQQQQBii}16@0:8"
- "{HSTSensingAlgsConfig=\"maxPacketSize\"Q\"familyID\"Q\"frameworkString\"@\"NSString\"\"device\"^{__MTDevice}}"
- "{HSTSensingAlgsConfig=QQ@^{__MTDevice}}16@0:8"
- "\xc1"
- "\xf0\xd1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe2"

```
