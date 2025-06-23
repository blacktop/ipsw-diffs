## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-270.59.4.11.2
-  __TEXT.__text: 0x2a50cc
-  __TEXT.__auth_stubs: 0x1fb0
+270.64.3.0.0
+  __TEXT.__text: 0x2a5ee0
+  __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x5c3c
-  __TEXT.__cstring: 0x4102e
+  __TEXT.__objc_methlist: 0x5ca4
+  __TEXT.__cstring: 0x4110c
   __TEXT.__const: 0x1b58
-  __TEXT.__gcc_except_tab: 0x2cd0
-  __TEXT.__oslogstring: 0x63be1
+  __TEXT.__gcc_except_tab: 0x2cf8
+  __TEXT.__oslogstring: 0x63ddd
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4ac8
-  __TEXT.__objc_classname: 0x763
-  __TEXT.__objc_methname: 0x150fc
-  __TEXT.__objc_methtype: 0x20f3
-  __TEXT.__objc_stubs: 0xcfa0
+  __TEXT.__unwind_info: 0x4b00
+  __TEXT.__objc_classname: 0x760
+  __TEXT.__objc_methname: 0x15293
+  __TEXT.__objc_methtype: 0x208e
+  __TEXT.__objc_stubs: 0xd1a0
   __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x65e8
+  __DATA_CONST.__const: 0x6640
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a28
+  __DATA_CONST.__objc_selrefs: 0x3aa0
   __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0xff0
-  __AUTH_CONST.__const: 0x3da0
-  __AUTH_CONST.__cfstring: 0x188c0
-  __AUTH_CONST.__objc_const: 0x8888
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x70
+  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH_CONST.__const: 0x3e00
+  __AUTH_CONST.__cfstring: 0x18b80
+  __AUTH_CONST.__objc_const: 0x8828
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa00
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x834
+  __DATA.__objc_ivar: 0x82c
   __DATA.__data: 0xfe0
-  __DATA.__bss: 0x1891
+  __DATA.__bss: 0x18a9
   __DATA.__common: 0x558
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x420

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34FA2FDC-D241-3E34-9A9C-8D57D922E367
-  Functions: 7368
-  Symbols:   23052
-  CStrings:  18272
+  UUID: 4A9B9F35-6A37-3934-A94A-B9C6C821CB3F
+  Functions: 7389
+  Symbols:   23131
+  CStrings:  18340
 
Symbols:
+ +[MXSystemController(InternalUse) sendPreferHeadphonesOverCarsAndSpeakersSettingsUpdateToAudioStatistics:]
+ +[MX_BannerManager getBannerCleanupDispatchQueue]
+ +[MX_BannerManager getBannerCleanupDispatchQueue].cold.1
+ +[MX_BannerManager getButtonType:]
+ +[MX_BannerManager getCacheKey:endpointType:]
+ +[MX_BannerManager getCacheKey:port:]
+ +[MX_BannerManager getRoutingTargetDeviceTypeString:]
+ -[MXBannerResponseInfoBase bannerResponse]
+ -[MXBannerResponseInfoBase dealloc]
+ -[MXBannerResponseInfoBase init]
+ -[MXBannerResponseInfoBase routeSemaphore]
+ -[MXBannerResponseInfoBase setBannerResponse:]
+ -[MXBannerResponseInfoBase setRouteSemaphore:]
+ -[MXBannerResponseInfoBase setTxid:]
+ -[MXBannerResponseInfoBase txid]
+ -[MXCoreSession copyCurrentActiveRoutes]
+ -[MXSessionManager phoneCallIsAboutToGoActiveOverCarPlay]
+ -[MXSessionManager setPhoneCallIsAboutToGoActiveOverCarPlay:]
+ -[MXSessionManager(Utilities) isPortHeadphoneAndInEar:]
+ -[MX_BannerManager cleanupBannerCache:]
+ -[MX_BannerManager cleanupBannerIfNeededForRoute:routeName:bannerType:]
+ -[MX_BannerManager cleanupBannerWithTxid:targetRouteUID:bannerType:]
+ -[MX_BannerManager cleanupBannersIfNeededForRoute:routeName:endpointManagerType:]
+ -[MX_BannerManager cleanupBanners]
+ -[MX_BannerManager newPortNeedsToShowBanner:previousPort:]
+ -[MX_BannerManager promptUserResponseForRoute:connectHandler:]
+ -[MX_BannerManager promptUserResponseForUndoRoute:undoHandler:]
+ -[MX_BannerManager sendBannerActionToAudioStatistics:bannerType:targetDeviceType:targetProductID:sourceDeviceType:]
+ -[MX_BannerManager updatePartnerPortsInUndoBannerResponseCacheForKey:forPort:]
+ _CMSMVAUtility_ChangeCarPlayPortFallbackRoutability
+ _CMSMVAUtility_ChangeCarPlayPortFallbackRoutabilityIfNecessary
+ _CMSMVAUtility_CopyBluetoothDeviceModelID
+ _CMSMVAUtility_CopyPartnerPorts
+ _CMSMVAUtility_IsPortOfTypeBuiltInSpeakerOrReceiver
+ _CMSMVAUtility_IsPortOfTypeCarPlay
+ _CMSMVAUtility_IsPortOfTypeCarPlayMainAudio
+ _CMSMVAUtility_LogPartnerPorts
+ _FigRouteDiscoveryManagerIsClientEligibleToReceiveUpdateNotifications
+ _FigRoutingManagerProcessCustomizedRouting
+ _MXEndpointDescriptorCacheDoesEndpointIDMatchDeviceID
+ _OBJC_CLASS_$_MXBannerResponseInfoBase
+ _OBJC_IVAR_$_MXBannerResponseInfoBase._bannerResponse
+ _OBJC_IVAR_$_MXBannerResponseInfoBase._routeSemaphore
+ _OBJC_IVAR_$_MXBannerResponseInfoBase._txid
+ _OBJC_IVAR_$_MXSessionManager._phoneCallIsAboutToGoActiveOverCarPlay
+ _OBJC_IVAR_$_MX_BannerManager.connectBannerResponseCache
+ _OBJC_IVAR_$_MX_BannerManager.undoBannerResponseCache
+ _OBJC_METACLASS_$_MXBannerResponseInfoBase
+ __OBJC_$_INSTANCE_METHODS_MXBannerResponseInfoBase
+ __OBJC_$_INSTANCE_VARIABLES_MXBannerResponseInfoBase
+ __OBJC_$_PROP_LIST_MXBannerResponseInfoBase
+ __OBJC_CLASS_RO_$_MXBannerResponseInfoBase
+ __OBJC_METACLASS_RO_$_MXBannerResponseInfoBase
+ ___34-[MX_BannerManager cleanupBanners]_block_invoke
+ ___49+[MX_BannerManager getBannerCleanupDispatchQueue]_block_invoke
+ ___62-[MX_BannerManager promptUserResponseForRoute:connectHandler:]_block_invoke
+ ___62-[MX_BannerManager promptUserResponseForRoute:connectHandler:]_block_invoke.100
+ ___63-[MX_BannerManager promptUserResponseForUndoRoute:undoHandler:]_block_invoke
+ ___63-[MX_BannerManager promptUserResponseForUndoRoute:undoHandler:]_block_invoke.110
+ ___81-[MX_BannerManager cleanupBannersIfNeededForRoute:routeName:endpointManagerType:]_block_invoke
+ ___83-[MXEndpointDescriptorCache _availableEndpointsDidChangeForEndpointManager:atDate:]_block_invoke.24
+ ___FigRoutingManagerProcessCustomizedRouting_block_invoke
+ ___FigRoutingManagerProcessCustomizedRouting_block_invoke.72
+ ___FigRoutingManagerProcessCustomizedRouting_block_invoke.74
+ ___FigRoutingManagerProcessCustomizedRouting_block_invoke_2
+ ___FigRoutingManagerProcessCustomizedRouting_block_invoke_2.73
+ ___FigRoutingManagerProcessCustomizedRouting_block_invoke_2.77
+ ___MXCoreSessionSetProperty_block_invoke.176
+ ___MXCoreSessionSetProperty_block_invoke.181
+ ___MXCoreSessionSetProperty_block_invoke.233
+ ___MXCoreSessionSetProperty_block_invoke.289
+ ___block_descriptor_112_e8_32o40o48o56b_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_120_e8_32o40o48o56o64b72r_e20_v20?0i8"NSError"12lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_140_e8_32o40o48o56o64b72r_e20_v20?0i8"NSError"12lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e20_v20?0i8"NSError"12l
+ ___block_descriptor_32_e36_v24?0^{__CFArray=}8^{__CFString=}16l
+ ___block_descriptor_37_e5_v8?0l
+ ___block_descriptor_41_e8_32o_e82_v40?0^{__CFArray=}8^{OpaqueFigEndpoint=}16^{OpaqueFigEndpoint=}24^{__CFString=}32ls32l8
+ ___block_descriptor_73_e8_32o_e5_v8?0ls32l8
+ ___block_literal_global.112
+ ___block_literal_global.114
+ ___block_literal_global.133
+ ___block_literal_global.158
+ ___block_literal_global.170
+ ___block_literal_global.178
+ ___block_literal_global.235
+ ___block_literal_global.400
+ ___block_literal_global.53
+ ___block_literal_global.55
+ ___block_literal_global.62
+ ___block_literal_global.66
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___block_literal_global.81
+ ___block_literal_global.90
+ ___block_literal_global.92
+ ___central_UpdateCarPlayFallbackRoutability_block_invoke
+ ___cmsSetIsActive_block_invoke.137
+ ___cmsSetIsPlaying_block_invoke.154
+ ___discoveryManager_updateDiscoveryModeForType_block_invoke.51
+ ___mx_runningBoardServices_initializeMonitoring_block_invoke.27
+ ___mx_runningBoardServices_initializeMonitoring_block_invoke.37
+ ___vaemUpdateSharedAudioRouteState_block_invoke.82
+ _dispatch_set_qos_class_floor
+ _dispatch_set_target_queue
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_scheduler_priority
+ _gDaemonCache
+ _gDaemonCacheLock
+ _gRouteTimestampPrefs
+ _getBannerCleanupDispatchQueue.onceToken
+ _kMXAirPodsInEarRoutingLog_BannerActionKey
+ _kMXAirPodsInEarRoutingLog_BannerShownTypeKey
+ _kMXAirPodsInEarRoutingLog_KeepAudioWithHeadphonesSettingKey
+ _kMXAirPodsInEarRoutingLog_SettingsUpdateKey
+ _kMXAirPodsInEarRoutingLog_SourceDeviceProductIDKey
+ _kMXAirPodsInEarRoutingLog_TargetDeviceProductIDKey
+ _kMXAirPodsInEarRoutingLog_TargetDeviceTypeKey
+ _mx_runningBoardServices_removePIDFromCaches
+ _objc_msgSend$bannerResponse
+ _objc_msgSend$cleanupBannerCache:
+ _objc_msgSend$cleanupBannerIfNeededForRoute:routeName:bannerType:
+ _objc_msgSend$cleanupBannerWithTxid:targetRouteUID:bannerType:
+ _objc_msgSend$cleanupBanners
+ _objc_msgSend$cleanupBannersIfNeededForRoute:routeName:endpointManagerType:
+ _objc_msgSend$copyCurrentActiveRoutes
+ _objc_msgSend$getBannerCleanupDispatchQueue
+ _objc_msgSend$getButtonType:
+ _objc_msgSend$getCacheKey:endpointType:
+ _objc_msgSend$getCacheKey:port:
+ _objc_msgSend$getRoutingTargetDeviceTypeString:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$isDaemon
+ _objc_msgSend$isPortHeadphoneAndInEar:
+ _objc_msgSend$newPortNeedsToShowBanner:previousPort:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$phoneCallIsAboutToGoActiveOverCarPlay
+ _objc_msgSend$promptForDisconnectedBanner:withIconType:callbackHandler:
+ _objc_msgSend$promptUserResponseForRoute:connectHandler:
+ _objc_msgSend$promptUserResponseForUndoRoute:undoHandler:
+ _objc_msgSend$sendBannerActionToAudioStatistics:bannerType:targetDeviceType:targetProductID:sourceDeviceType:
+ _objc_msgSend$sendPreferHeadphonesOverCarsAndSpeakersSettingsUpdateToAudioStatistics:
+ _objc_msgSend$setBannerResponse:
+ _objc_msgSend$setPhoneCallIsAboutToGoActiveOverCarPlay:
+ _objc_msgSend$updatePartnerPortsInUndoBannerResponseCacheForKey:forPort:
+ _sBannerCleanupDispatchQueue
+ _vaeCopyDeviceMacAddressFromVADPort
- +[MXEndpointDescriptorCache getConnectBannerResponseCache]
- +[MXEndpointDescriptorCache getConnectBannerResponseCache].cold.1
- -[MXConnectBannerResponseInfo connectBannerResponse]
- -[MXConnectBannerResponseInfo dealloc]
- -[MXConnectBannerResponseInfo init]
- -[MXConnectBannerResponseInfo routeSemaphore]
- -[MXConnectBannerResponseInfo setConnectBannerResponse:]
- -[MXConnectBannerResponseInfo setRouteSemaphore:]
- -[MXConnectBannerResponseInfo setTxid:]
- -[MXConnectBannerResponseInfo txid]
- -[MXUndoBannerResponseInfo routeSemaphore]
- -[MXUndoBannerResponseInfo setRouteSemaphore:]
- -[MXUndoBannerResponseInfo setTxid:]
- -[MXUndoBannerResponseInfo setUndoBannerResponse:]
- -[MXUndoBannerResponseInfo txid]
- -[MXUndoBannerResponseInfo undoBannerResponse]
- -[MX_BannerManager cleanupConnectBannerIfNeeded:routeName:]
- -[MX_BannerManager cleanupUndoBannerIfNeeded:routeName:]
- -[MX_BannerManager isAnyConnectBannerActive]
- -[MX_BannerManager newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:]
- -[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]
- -[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]
- GCC_except_table38
- _FigRouteDiscoveryManagerIsClientSuspendedOrTerminated
- _FigRoutingManagerCopyPartnerPorts
- _FigRoutingManagerIsRoutableConsideringBannerState
- _FigRoutingManagerProcessAirPodsInEarRouting
- _FigRoutingManagerUtilities_LogPartnerPorts
- _OBJC_CLASS_$_MXConnectBannerResponseInfo
- _OBJC_IVAR_$_MXConnectBannerResponseInfo._connectBannerResponse
- _OBJC_IVAR_$_MXConnectBannerResponseInfo._routeSemaphore
- _OBJC_IVAR_$_MXConnectBannerResponseInfo._txid
- _OBJC_IVAR_$_MXUndoBannerResponseInfo._routeSemaphore
- _OBJC_IVAR_$_MXUndoBannerResponseInfo._txid
- _OBJC_IVAR_$_MXUndoBannerResponseInfo._undoBannerResponse
- _OBJC_IVAR_$_MX_BannerManager._connectBannerResponseCache
- _OBJC_IVAR_$_MX_BannerManager._undoBannerResponseCache
- _OBJC_METACLASS_$_MXConnectBannerResponseInfo
- __OBJC_$_INSTANCE_METHODS_MXConnectBannerResponseInfo
- __OBJC_$_INSTANCE_VARIABLES_MXConnectBannerResponseInfo
- __OBJC_$_PROP_LIST_MXConnectBannerResponseInfo
- __OBJC_CLASS_RO_$_MXConnectBannerResponseInfo
- __OBJC_METACLASS_RO_$_MXConnectBannerResponseInfo
- ___138-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke
- ___138-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke_2
- ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke
- ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke.76
- ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke_2
- ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke_2.81
- ___58+[MXEndpointDescriptorCache getConnectBannerResponseCache]_block_invoke
- ___83-[MXEndpointDescriptorCache _availableEndpointsDidChangeForEndpointManager:atDate:]_block_invoke.27
- ___FigRoutingManagerProcessAirPodsInEarRouting_block_invoke
- ___FigRoutingManagerProcessAirPodsInEarRouting_block_invoke.50
- ___MXCoreSessionSetProperty_block_invoke.175
- ___MXCoreSessionSetProperty_block_invoke.180
- ___MXCoreSessionSetProperty_block_invoke.232
- ___MXCoreSessionSetProperty_block_invoke.288
- ___block_descriptor_112_e8_32o40o48b56r64r_e20_v20?0i8"NSError"12lr56l8s32l8s40l8s48l8r64l8
- ___block_descriptor_112_e8_32o40o48b56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_36_e82_v40?0^{__CFArray=}8^{OpaqueFigEndpoint=}16^{OpaqueFigEndpoint=}24^{__CFString=}32l
- ___block_descriptor_52_e51_v32?0^{__CFArray=}8^{__CFArray=}16^{__CFString=}24l
- ___block_descriptor_64_e8_32o40b_e5_v8?0ls40l8s32l8
- ___block_descriptor_80_e8_32b_e5_v8?0ls32l8
- ___block_descriptor_88_e8_32o40o48b56r64r_e20_v20?0i8"NSError"12lr56l8s32l8s40l8s48l8r64l8
- ___block_literal_global.101
- ___block_literal_global.144
- ___block_literal_global.157
- ___block_literal_global.169
- ___block_literal_global.182
- ___block_literal_global.2
- ___block_literal_global.234
- ___block_literal_global.25
- ___block_literal_global.399
- ___block_literal_global.40
- ___block_literal_global.59
- ___block_literal_global.60
- ___block_literal_global.63
- ___block_literal_global.82
- ___block_literal_global.85
- ___block_literal_global.89
- ___cmsSetIsActive_block_invoke.136
- ___cmsSetIsPlaying_block_invoke.153
- ___discoveryManager_updateDiscoveryModeForType_block_invoke_2
- ___discoveryManager_updateDiscoveryModeForType_block_invoke_3
- ___mx_runningBoardServices_initializeMonitoring_block_invoke.26
- ___mx_runningBoardServices_initializeMonitoring_block_invoke.36
- ___vaemUpdateSharedAudioRouteState_block_invoke.83
- _getConnectBannerResponseCache.connectBannerResponseDictionary
- _getConnectBannerResponseCache.onceTokenConnectBannerResponseDictionary
- _mx_runningBoardServices_removePIDFromApplicationStateCache
- _objc_msgSend$cleanupConnectBannerIfNeeded:routeName:
- _objc_msgSend$cleanupUndoBannerIfNeeded:routeName:
- _objc_msgSend$connectBannerResponse
- _objc_msgSend$isAnyConnectBannerActive
- _objc_msgSend$newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:
- _objc_msgSend$promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:
- _objc_msgSend$promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:
- _objc_msgSend$setConnectBannerResponse:
- _objc_msgSend$setUndoBannerResponse:
- _objc_msgSend$undoBannerResponse
CStrings:
+ "%@_%@"
+ "+[MX_BannerManager getCacheKey:endpointType:]"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData for %{public}s bud status failed with err = %d = %c%c%c%c for port = %u"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyInEarBluetoothStatus ) failed with err = %d = %{public}.4s for port = %u"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyInEarDetectSupported ) failed with err = %d = %{public}.4s for port = %u"
+ "-CMVAEndpoint- %s: Making port routable as fallback: %u"
+ "-CMVAEndptMgr- %s: Making device Routable: %{public}@"
+ "-CMVAEndptMgr- %s: Making device RoutableAsFallback: %{public}@"
+ "-CMVAEndptMgr- %s: Making device Unroutable: %{public}@"
+ "-CMVAEndptMgr- %s: category = '%{public}.4s'  mostRecentVADCategory = '%{public}.4s' mode = '%{public}.4s' mostRecentVADMode = '%{public}.4s' \n \t\t\t\t\t\t\t\t\t\t\tactivationContext: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\toverridePortsList: %{public}@ mostRecentOverridePortsList: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\troutablePorts:%{public}@ unroutablePorts:%{public}@ \t\t\t\t\t\n  \t\t\t\t\t\t\t\t\t\t\troutableAsFallback:%hhu \n \t\t\t\t\t\t\t\t\t\t\tportsToAggregate:%{public}@ portsToDeaggregate:%{public}@\t\t\t\t\n \t\t\t\t\t\t\t\t\t\t\tsubPortPreferences: %{public}@ mostRecentsubPortPreferences : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tsetScreenDarkMode = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tcreateSpeakerDevice = %{public}s \n \t\t\t\t\t\t\t\t\t\t\texcludedPortsList : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tignoreRingerSwitch = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tdecoupledInputOutput = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tallowedPortTypes = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\treporterIDs = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\tcameraParameters = %{public}@\n \t\t\t\t\t\t\t\t\t\t\tupdatePVMOnRedundantRouteConfiguration = %{public}s\n \t\t\t\t\t\t\t\t\t\t\tpersistentRoute = %{public}@ mostRecentPersistentRoute: %{public}@\n                                             userPreferredInputPort = %{public}@ \n"
+ "-CMVAEndptMgr- %s: portsToAdd count = %lu"
+ "-CMVAEndptMgr- %s: portsToAdd[%d]  = %{public}@, name = %{public}@"
+ "-CMVAEndptMgr- %s: portstoAdd does NOT contain a starkPort"
+ "-CMVAEndptUtl- %s: Adding partner port %u to result"
+ "-CMVAEndptUtl- %s: Setting CarPlay port routability = %u"
+ "-CMVAEndptUtl- %s: currentPort = %u : partnerPort = %{public}@"
+ "-CMVAEndptUtl- %s: isAnyBTVehicleConnected = %{BOOL}u due to port = %u"
+ "-CMVAEndptUtl- %s: port = %u, Endpoint name = %{public}@"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = %d for %@"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false for port %u due to portType equal to %d"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, A2DP port %u NOT jacking in as LineOut/USB/HDMI/DisplayPort/Thunderbolt/Stark/ContinuityScreenOutput is around."
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, BT audio route action is do not autoroute for port = %u"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, NOT jacking in because port %ld does not have ownership"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, NOT jacking in because port %ld does not support in-ear detection and does not have ownership"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, NOT jacking in because port %ld is not in-ear"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, new wireless port is Odeon however current route is BT that is inEar, do not make Odeon port routable."
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, port %u is out-of-ear, skip asking about the audio routing action"
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false, timeout occurred with requesting ownership - setting shouldAutoRoute to false for port = %u"
+ "-CMVAEndptUtl- %s: starkPort=%d, starkPortWasMadeRoutable=%s, gCMSM.doNotMakeStarkPortRoutable=%s, sessionToPlayOverStark=%@, routableType = %{private}u"
+ "-FigRouteDiscoverer- %s: Discoverer %p clientName %{public}@ is not eligible for notifications"
+ "-FigRouteDiscoveryManager- %s: Time taken to run notification handler %fms. Time taken to post %{public}@ to all discoverers: %fms. Average time: %fms. Cache misses this iteration %d."
+ "-FigRoutingManager_iOS- %s: BluetoothPortPairedToCarPlay = YES, ignoring routing to BT port %d/%{public}@"
+ "-FigRoutingManager_iOS- %s: Current output ports count= %ld"
+ "-FigRoutingManager_iOS- %s: FigRoutingManager_iOSAddEndpointToContext result = %u for endpoint = %{public}@, port = %d"
+ "-FigRoutingManager_iOS- %s: Reverse endpoints array = NULL, not performing undo routing"
+ "-FigRoutingManager_iOS- %s: Reversing endpointsToRoute = NULL"
+ "-FigRoutingManager_iOS- %s: Show undo transition banner"
+ "-FigRoutingManager_iOS- %s: currentOutputPort[%ld] = %{private}@, %{private}@"
+ "-FigRoutingManager_iOS- %s: endpointsToRoute[%ld] name = %{public}@, port = %d"
+ "-FigRoutingManager_iOS- %s: index = %ld, newPortNameAtIndex  = %{public}@, newPortSubTypeAtIndex = %{public}@, portDeviceIdentifierAtIndex = %{public}@, portMacAddressAtIndex = %{public}@, isPortOfTypeCarPlayAtIndex = %{BOOL}u, modelID = %{public}@"
+ "-FigRoutingManager_iOS- %s: newWirelessPorts count = %lu"
+ "-FigRoutingManager_iOS- %s: routingPreference - preferHeadphonesOverCarsAndSpeakersEnabled = %{BOOL}u"
+ "-MXCoreSession_Embedded- %s: Zero active ports for current category: %u and mode:%u "
+ "-MXCoreSession_Embedded- %s: returned routeTypes = %@,"
+ "-MXEndpointDescriptorCache- %s:  MXEndpointDescriptorCleanupBannersIfNeeded for routeuid = %{public}@, routeName = %{public}@, portNumber = %{public}@, headphone = %{public}@, headphoneBT = %{public}@, managerType = %{public}@"
+ "-MXEndpointDescriptorCache- %s: timeTaken to clean up banners: %llu ms."
+ "-MXSessionManagerUtilities- %s: port = %u is not in ear"
+ "-MXSessionManagerUtilities- %s: shouldAllowBluetoothAccessoryToRequestAudioRoute = YES due to isCurrentRouteHeadphonesAndInEar = NO"
+ "-MXSessionManagerUtilities- %s: shouldAllowBluetoothAccessoryToRequestAudioRoute = YES due to isPreferHeadphonesOverCarsAndSpeakersEnabled = NO"
+ "-MX_BannerManager- %s: Banner entry deleted before banner response for route %{public}@, route probably went away"
+ "-MX_BannerManager- %s: Cachekey NOT found, cacheKey = %{public}@, routeName = %{public}@"
+ "-MX_BannerManager- %s: Cachekey being REMOVED as device went away, target UID = %{public}@"
+ "-MX_BannerManager- %s: Cachekey being REMOVED as route went away, routeUID = %{public}@, dismissBannerResult = %{BOOL}u"
+ "-MX_BannerManager- %s: Caching partner port[%lu] = %{public}@"
+ "-MX_BannerManager- %s: Empty routeDescriptor, no op"
+ "-MX_BannerManager- %s: Headphones were on A2DP before transfer"
+ "-MX_BannerManager- %s: Headphones were on HFP before transfer"
+ "-MX_BannerManager- %s: Invalid endpoint type for cacheKey %{public}@"
+ "-MX_BannerManager- %s: Match found for newPortID = %{public}@ in connectedPorts for current category, newPortNeedsToShowBanner = YES"
+ "-MX_BannerManager- %s: Undo banner entry created for device = %{public}@, txid = %{public}@"
+ "-MX_BannerManager- %s: Undo banner entry deleted for device = %{public}@"
+ "-MX_BannerManager- %s: Undo banner response = %{public}@ for cacheKey = %{public}@"
+ "-MX_BannerManager- %s: UndoBannerResponse = connect BUT skipping due to isPortHeadphoneAndInEar = NO and not speaker/receiver route (if FF MediaExperience/CustomizedRoutingWithCarsAndSpeakers is enabled)"
+ "-MX_BannerManager- %s: bannerType = %{public}u, txid = %{public}@, targetRouteUID = %{public}@"
+ "-MX_BannerManager- %s: dismissBannerResult = %{BOOL}u"
+ "-MX_BannerManager- %s: isCarPlayPortRoutableFromCustomizedRoutingPerspective = %{BOOL}u"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = %u for newPortId = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Creating new banner entry for device = %{public}@, oldPortMacAddress = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES.  Connect banner request for port = %{public}d, id = %{public}@, cacheKey=%{public}@, route=%{public}@, cachedConnectBannerResponse = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner entry created (txid) for cacheKey = %{private}@, txid = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner entry deleted for cacheKey = %{private}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Connect banner response = %{public}@ for cacheKey = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Creating new banner object for device = %{public}@, oldPortMacAddress = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Object deleted before banner response, route %{public}@ went away before user banner action"
+ "-MX_BannerManager- %s: oldEndpoint NOT found for cacheKey = %{public}@, not performing Undo operation"
+ "-MX_BannerManager- %s: oldEndpoint[%ld] name = %{public}@, port = %d"
+ "-MX_BannerManager- %s: promptUserResponseForUndoRoute routingContextUUID = %{public}@, oldPort = %u, newPortID = %{public}@, cacheKey = %{public}@, modelID = %{public}@"
+ "-MX_BannerManager- %s: routeUID = %{public}@, cacheKey = %{public}@ "
+ "-MX_BannerManager- %s: routeUID = %{public}@, cacheKey = %{public}@, okToRoute = %{BOOL}u as user chose to ignore connect banner"
+ "-MX_BannerManager- %s: routeUID = %{public}@, cacheKey = %{public}@, okToRoute = %{BOOL}u as user clicked on undo banner"
+ "-MX_BannerManager- %s: routingContextUUID = %{public}@, oldPort = %u, newPortID = %{public}@"
+ "-MX_BannerManager- %s: txid = %{public}@, Cachekey being REMOVED, Route went away, routeUID = %{public}@, routeName = %{public}@"
+ "-MX_RunningBoardServices- %s: Process '%{public}@' is a daemon"
+ "-[MXCoreSession copyCurrentActiveRoutes]"
+ "-[MXSessionManager(Utilities) isPortHeadphoneAndInEar:]"
+ "-[MX_BannerManager cleanupBannerCache:]"
+ "-[MX_BannerManager cleanupBannerIfNeededForRoute:routeName:bannerType:]"
+ "-[MX_BannerManager cleanupBannerWithTxid:targetRouteUID:bannerType:]"
+ "-[MX_BannerManager cleanupBannersIfNeededForRoute:routeName:endpointManagerType:]"
+ "-[MX_BannerManager cleanupBanners]"
+ "-[MX_BannerManager newPortNeedsToShowBanner:previousPort:]"
+ "-[MX_BannerManager promptUserResponseForRoute:connectHandler:]"
+ "-[MX_BannerManager promptUserResponseForRoute:connectHandler:]_block_invoke"
+ "-[MX_BannerManager promptUserResponseForUndoRoute:undoHandler:]"
+ "-[MX_BannerManager promptUserResponseForUndoRoute:undoHandler:]_block_invoke"
+ "-[MX_BannerManager promptUserResponseForUndoRoute:undoHandler:]_block_invoke_2"
+ "-[MX_BannerManager updatePartnerPortsInUndoBannerResponseCacheForKey:forPort:]"
+ "-endpoint_central- %s: Make CarPlay %{public}@"
+ "00:10:36"
+ "10507"
+ "8218"
+ "@28@0:8@16I24"
+ "B28@0:8@16I24"
+ "BannerType"
+ "CMSMVAUtility_ChangeCarPlayPortFallbackRoutability"
+ "CMSMVAUtility_CopyPartnerPorts"
+ "CMSMVAUtility_IsAnyBluetoothVehicleConnected"
+ "CMSMVAUtility_LogPartnerPorts"
+ "FigRouteDiscoveryManagerIsClientEligibleToReceiveUpdateNotifications"
+ "FigRoutingManagerProcessCustomizedRouting"
+ "FigRoutingManagerProcessCustomizedRouting_block_invoke"
+ "FigRoutingManagerProcessCustomizedRouting_block_invoke_2"
+ "Jun 14 2025"
+ "KeepAudioWithHeadphonesSetting"
+ "KeepAudioWithHeadphonesSettingUpdate"
+ "MXBannerResponseInfoBase"
+ "MediaExperienceDiscovery WL"
+ "MostRecentCurrentlyActivatingEndpoint"
+ "OldPort"
+ "PortDeviceIdentifier"
+ "PortID"
+ "PortMacAddress"
+ "PortName"
+ "PortType"
+ "SourceDeviceProductID"
+ "TB,N,V_phoneCallIsAboutToGoActiveOverCarPlay"
+ "TC,N,V_bannerResponse"
+ "TargetDeviceProductID"
+ "TargetDeviceType"
+ "UnknownEndpointType"
+ "UserBannerAction"
+ "VideoPlayback"
+ "WirelessPorts"
+ "_bannerResponse"
+ "_phoneCallIsAboutToGoActiveOverCarPlay"
+ "bannerResponse"
+ "central_UpdateCarPlayFallbackRoutability"
+ "central_UpdateCarPlayFallbackRoutability_block_invoke"
+ "cleanupBannerCache:"
+ "cleanupBannerIfNeededForRoute:routeName:bannerType:"
+ "cleanupBannerWithTxid:targetRouteUID:bannerType:"
+ "cleanupBanners"
+ "cleanupBannersIfNeededForRoute:routeName:endpointManagerType:"
+ "com.apple.MediaExperience.BannerCleanupDispatchQueue"
+ "connectBannerResponseCache"
+ "copyCurrentActiveRoutes"
+ "fallback routable"
+ "getBannerCleanupDispatchQueue"
+ "getButtonType:"
+ "getCacheKey:endpointType:"
+ "getCacheKey:port:"
+ "getRoutingTargetDeviceTypeString:"
+ "initWithUnsignedLongLong:"
+ "isDaemon"
+ "isPortHeadphoneAndInEar:"
+ "mx_runningBoardServices_addPIDToCaches"
+ "mx_runningBoardServices_removePIDFromCaches"
+ "newPortNeedsToShowBanner:previousPort:"
+ "numberWithInteger:"
+ "phoneCallIsAboutToGoActiveOverCarPlay"
+ "promptForDisconnectedBanner:withIconType:callbackHandler:"
+ "promptUserResponseForRoute:connectHandler:"
+ "promptUserResponseForUndoRoute:undoHandler:"
+ "pvmUpdateMostRecentSynchronizedVolumeActivityTimestampPref"
+ "sendBannerActionToAudioStatistics:bannerType:targetDeviceType:targetProductID:sourceDeviceType:"
+ "sendPreferHeadphonesOverCarsAndSpeakersSettingsUpdateToAudioStatistics:"
+ "setBannerResponse:"
+ "setPhoneCallIsAboutToGoActiveOverCarPlay:"
+ "undoBannerResponseCache"
+ "updatePartnerPortsInUndoBannerResponseCacheForKey:forPort:"
+ "v24@?0^{__CFArray=}8^{__CFString=}16"
+ "v36@0:8@16^{__CFString=}24C32"
+ "v36@0:8^{__CFString=}16^{__CFString=}24C32"
+ "v40@0:8^{__CFString=}16^{__CFString=}24^{__CFString=}32"
+ "v56@0:8q16q24q32@40@48"
+ "vaemProcessCarPlayCustomizedRouting"
- "-CMVAEndpoint- %s: AudioObjectGetPropertyData for %{public}s bud status failed with err = %d = %c%c%c%c"
- "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyInEarBluetoothStatus ) failed with err = %d = %{public}.4s"
- "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyInEarDetectSupported ) failed with err = %d = %{public}.4s"
- "-CMVAEndpoint- %s: vaeMakePortRoutable, making fallback port routable"
- "-CMVAEndptMgr- %s: Making device %{public}sroutable: %{public}@"
- "-CMVAEndptMgr- %s: NOT a starkPort"
- "-CMVAEndptMgr- %s: category = '%{public}.4s'  mostRecentVADCategory = '%{public}.4s' mode = '%{public}.4s' mostRecentVADMode = '%{public}.4s' \n \t\t\t\t\t\t\t\t\t\t\tactivationContext: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\toverridePortsList: %{public}@ mostRecentOverridePortsList: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\troutablePorts:%{public}@ unroutablePorts:%{public}@ \t\t\t\t\t\n  \t\t\t\t\t\t\t\t\t\t\tportsToAggregate:%{public}@ portsToDeaggregate:%{public}@\t\t\t\t\n \t\t\t\t\t\t\t\t\t\t\tsubPortPreferences: %{public}@ mostRecentsubPortPreferences : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tsetScreenDarkMode = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tcreateSpeakerDevice = %{public}s \n \t\t\t\t\t\t\t\t\t\t\texcludedPortsList : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tignoreRingerSwitch = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tdecoupledInputOutput = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tallowedPortTypes = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\treporterIDs = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\tcameraParameters = %{public}@\n \t\t\t\t\t\t\t\t\t\t\tupdatePVMOnRedundantRouteConfiguration = %{public}s\n \t\t\t\t\t\t\t\t\t\t\tpersistentRoute = %{public}@ mostRecentPersistentRoute: %{public}@\n                                             userPreferredInputPort = %{public}@ \n"
- "-CMVAEndptMgr- %s: connectedOutputPorts[%ld] = %{public}@"
- "-CMVAEndptMgr- %s: currentPort endpointid = %{public}@"
- "-CMVAEndptMgr- %s: currentPort[%ld] = %{private}@"
- "-CMVAEndptMgr- %s: newWiredPorts count = %lu"
- "-CMVAEndptMgr- %s: newWirelessPorts count = %lu"
- "-CMVAEndptMgr- %s: portstoadd count = %lu"
- "-CMVAEndptMgr- %s: portstoadd[%d]  = %{public}@, name = %{public}@"
- "-CMVAEndptUtl- %s: BT audio route action is do not autoroute"
- "-CMVAEndptUtl- %s: NOT jacking in because port %ld does not have ownership"
- "-CMVAEndptUtl- %s: NOT jacking in because port %ld does not support in-ear detection and does not have ownership"
- "-CMVAEndptUtl- %s: NOT jacking in because port %ld is not in-ear"
- "-CMVAEndptUtl- %s: New wireless port is Odeon however current route is BT that is inEar, do not make Odeon port routable."
- "-CMVAEndptUtl- %s: Not really. A2DP not to be auto-jacked in if LineOut/USB/HDMI/DisplayPort/Thunderbolt/Stark/ContinuityScreenOutput is around."
- "-CMVAEndptUtl- %s: Port %u is out-of-ear, skip asking about the audio routing action"
- "-CMVAEndptUtl- %s: Timeout occurred with requesting ownership - setting shouldAutoRoute to false"
- "-CMVAEndptUtl- %s: shouldAutoRoute=%d for %@"
- "-CMVAEndptUtl- %s: starkPort=%d, starkPortWasMadeRoutable=%s, gCMSM.doNotMakeStarkPortRoutable=%s, sessionToPlayOverStark=%@"
- "-FigRouteDiscoverer- %s: Discoverer %p clientName %{public}@ is suspended or terminated"
- "-FigRouteDiscoveryManager- %s: Time taken to run notification handler %fms. Time taken to post %{public}@ to all discoverers: %fms. Average time: %fms. Cache misses this iteration %d. Time taken in RBS: %llu ms. Total calls to RBS: %d."
- "-FigRoutingManager-Utilities %s: currentPort = %u : partnerPort = %{public}@"
- "-FigRoutingManager-Utilities %s: port = %u, Endpoint name = %{public}@"
- "-FigRoutingManager_iOS- %s: Adding partner port %u to result"
- "-FigRoutingManager_iOS- %s: ConnectBanner is active, not allowing route picking now, returning false"
- "-FigRoutingManager_iOS- %s: Ignoring routing to BT port %{public}@/%{public}@ since BT port is paired to CarPlay"
- "-FigRoutingManager_iOS- %s: Picking routeName: %{public}@, routeUID : %{public}@, routeMacAddress : %{public}@"
- "-FigRoutingManager_iOS- %s: Returning true as routeDescriptor = NULL"
- "-FigRoutingManager_iOS- %s: Reverse endpoint name = %{public}@"
- "-FigRoutingManager_iOS- %s: Reverse endpoints array = NULL"
- "-FigRoutingManager_iOS- %s: Reversing from BT speaker"
- "-FigRoutingManager_iOS- %s: Reversing from CarPlay"
- "-FigRoutingManager_iOS- %s: _endpointsToRoute = NULL"
- "-FigRoutingManager_iOS- %s: _routingContextUUID = %{public}@"
- "-FigRoutingManager_iOS- %s: isrouted = %hhu"
- "-FigRoutingManager_iOS- %s: mostRecentCurrentlyActivatingEndpoint = NULL"
- "-FigRoutingManager_iOS- %s: mostRecentCurrentlyActivatingEndpoint name = %{public}@"
- "-FigRoutingManager_iOS- %s: newPortName  = %{public}@, newPortSubType = %{public}@, portDeviceIdentifier = %{public}@, portMacAddress = %{public}@, mostRecentCurrentlyActivatingEndpoint name = %{public}@, routingType = %ld"
- "-FigRoutingManager_iOS- %s: parent, mostRecentCurrentlyActivatingEndpoint = NULL"
- "-FigRoutingManager_iOS- %s: parent, mostRecentCurrentlyActivatingEndpoint name = %{public}@"
- "-FigRoutingManager_iOS- %s: prevEndpoint[%ld] name = %{public}@"
- "-FigRoutingManager_iOS- %s: routingPreference, preferHeadphonesOverCarsAndSpeakersEnabled = %d"
- "-FigRoutingManager_iOS- %s: routingType == kMXCustomizedRoutingTypeBTSpeaker"
- "-FigRoutingManager_iOS- %s: routingType == kMXCustomizedRoutingTypeCarPlay"
- "-MXEndpointDescriptorCache- %s:  MXEndpointDescriptorCleanupBannersIfNeeded for routeuid = %{public}@, routeName = %{public}@"
- "-MXEndpointDescriptorCache- %s: Endpoint added: %{public}@, %{public}@"
- "-MXEndpointDescriptorCache- %s: Endpoint removed: %{public}@, %{public}@"
- "-MXSystemSounds- %s: Active client playing to same VAD; system sound cannot take volume"
- "-MX_BannerManager- %s: AirPods were on A2DP before transfer"
- "-MX_BannerManager- %s: AirPods were on HFP before transfer"
- "-MX_BannerManager- %s: Banner entry already deleted, no op"
- "-MX_BannerManager- %s: Banner entry deleted before banner response, route probably went away"
- "-MX_BannerManager- %s: Cache key NOT present, Route went away, uid = %{public}@, routeName = %{public}@"
- "-MX_BannerManager- %s: Cache key REMOVED, Route went away, uid = %{public}@, routeName = %{public}@, dismissBanner result = %{public}d, txid = %{public}@"
- "-MX_BannerManager- %s: Cache key REMOVED, Route went away, uid = %{public}@, routeName = %{public}@, dismissBannerResult = %hhu"
- "-MX_BannerManager- %s: Reverse banner entry deleted for newRouteMacAddress = %{private}@"
- "-MX_BannerManager- %s: Undo banner entry created for newRouteMacAddress = %{private}@, txid = %{public}@"
- "-MX_BannerManager- %s: Undo banner response = %{public}@ for newRouteMacAddress = %{public}@"
- "-MX_BannerManager- %s: Undo banner response = do not connect"
- "-MX_BannerManager- %s: isCarPlayPortRoutableFromCustomizedRoutingPerspective = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = %u for newPortId = %{public}@, prevPortIsHfp = %u, newPortIsHfp = %u, prevPortIsA2dp = %u, newPortIsA2dp = %u, isCarPlayMainAudioPortType = %u"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Creating new banner entry for device = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES.  Connect banner request for port = %{public}d, id = %{public}@, macAddress=%{public}@, route=%{public}@, cachedConnectBannerResponse = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner entry created (txid) for newRouteMacAddress = %{private}@, txid = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner entry deleted for newRouteMacAddress = %{private}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner object present for device = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Connect banner response = %{public}@ for newRouteMacAddress = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Creating new banner object for device = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Object deleted before banner response, route probably went away"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. connectBannerResponseSemaphore signalled and ConnectBannerResponse = do not connect, userResponse = %{public}@"
- "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. connectBannerResponseSemaphore signalled and userResponse = MXUIService_UserAction_Pressed"
- "-MX_BannerManager- %s: newPortPrefix = %{public}@, newPortSuffix = %{public}@"
- "-MX_BannerManager- %s: oldEndpoint NOT found for newRouteMacAddress = %{public}@, not performing Undo operation"
- "-MX_BannerManager- %s: oldEndpoint[%ld] name = %{public}@"
- "-MX_BannerManager- %s: promptUserResponseForRoute routingContextUUID = %{public}@, oldPort = %u, newPortID = %{public}@"
- "-MX_BannerManager- %s: promptUserResponseForUndoRoute routingContextUUID = %{public}@, oldPort = %u, newPortID = %{public}@"
- "-MX_BannerManager- %s: routeUID = %{public}@, portMacAddress = %{public}@ "
- "-MX_BannerManager- %s: txid = %{public}@"
- "-[MX_BannerManager cleanupConnectBannerIfNeeded:routeName:]"
- "-[MX_BannerManager cleanupUndoBannerIfNeeded:routeName:]"
- "-[MX_BannerManager newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:]"
- "-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]"
- "-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke"
- "-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke_2"
- "-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]"
- "-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke"
- "-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke_2"
- "22:43:52"
- "B40@0:8@16^{__CFString=}24I32I36"
- "B72@0:8^{__CFString=}16^{__CFString=}24^{__CFString=}32@40I48I52^{__CFString=}56@?64"
- "B88@0:8^{__CFString=}16^{__CFString=}24^{__CFString=}32@40I48^{__CFArray=}52I60^{OpaqueFigEndpoint=}64^{__CFString=}72@?80"
- "FigRouteDiscoveryManagerIsClientSuspendedOrTerminated"
- "FigRoutingManagerCopyPartnerPorts"
- "FigRoutingManagerIsRoutableConsideringBannerState"
- "FigRoutingManagerNewWirelessPortsAdded"
- "FigRoutingManagerProcessAirPodsInEarRouting"
- "FigRoutingManagerProcessAirPodsInEarRouting_block_invoke"
- "FigRoutingManagerUtilities_LogPartnerPorts"
- "MXConnectBannerResponseInfo"
- "May 28 2025"
- "TC,N,V_connectBannerResponse"
- "TC,N,V_undoBannerResponse"
- "UN"
- "_connectBannerResponse"
- "_connectBannerResponseCache"
- "_undoBannerResponse"
- "_undoBannerResponseCache"
- "cleanupConnectBannerIfNeeded:routeName:"
- "cleanupUndoBannerIfNeeded:routeName:"
- "connectBannerResponse"
- "discoveryManager_updateDiscoveryModeForType_block_invoke_3"
- "getConnectBannerResponseCache"
- "isAnyConnectBannerActive"
- "mx_runningBoardServices_addPIDToApplicationStateCache"
- "mx_runningBoardServices_removePIDFromApplicationStateCache"
- "newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:"
- "promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:"
- "promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:"
- "pvmSetMostRecentSynchronizedVolumeActivityTimestampPref"
- "setConnectBannerResponse:"
- "setUndoBannerResponse:"
- "undoBannerResponse"
- "v32@0:8^{__CFString=}16^{__CFString=}24"
- "v32@?0^{__CFArray=}8^{__CFArray=}16^{__CFString=}24"
- "vaemProcessCustomizedRouting"

```
