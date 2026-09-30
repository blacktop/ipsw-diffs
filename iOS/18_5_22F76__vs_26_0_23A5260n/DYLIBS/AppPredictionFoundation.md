## AppPredictionFoundation

> `/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation`

```diff

-588.12.0.0.0
-  __TEXT.__text: 0xe3f0
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xb5c
-  __TEXT.__const: 0x258
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__cstring: 0x18b4
-  __TEXT.__oslogstring: 0x1281
-  __TEXT.__unwind_info: 0x450
-  __TEXT.__objc_classname: 0x1e1
-  __TEXT.__objc_methname: 0x2099
-  __TEXT.__objc_methtype: 0x506
-  __TEXT.__objc_stubs: 0x19e0
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x790
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x30
+610.0.11.0.0
+  __TEXT.__text: 0x19da8
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x18a4
+  __TEXT.__const: 0x418
+  __TEXT.__gcc_except_tab: 0x3dc
+  __TEXT.__cstring: 0x2048
+  __TEXT.__oslogstring: 0x1ad3
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__objc_classname: 0x47a
+  __TEXT.__objc_methname: 0x44ff
+  __TEXT.__objc_methtype: 0x894
+  __TEXT.__objc_stubs: 0x2f40
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0xaf8
+  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b0
+  __DATA_CONST.__objc_selrefs: 0x1100
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x12a0
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0x1fa0
+  __AUTH_CONST.__objc_const: 0x6f28
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x58
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x290
-  __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x58
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x158
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x2e8
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync
+  - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20DC2185-E168-3CC8-B324-6C8852F1C9BF
-  Functions: 478
-  Symbols:   1740
-  CStrings:  1031
+  UUID: FEA2EFF0-9A55-31EF-83DA-EF70E89CAD25
+  Functions: 825
+  Symbols:   3061
+  CStrings:  1562
 
Symbols:
+ +[ATXAppInFocusEvent supportsSecureCoding]
+ +[ATXAppInFocusEventSession supportsSecureCoding]
+ +[ATXAppInFocusStream currentAppInFocusStartEvent]
+ +[ATXAudioRouteStream atxAudioRouteTypeFromBMAudioRouteType:]
+ +[ATXBMBookmark _saveData:toFileURL:outError:]
+ +[ATXBMBookmark _saveData:toFileURL:outError:].cold.1
+ +[ATXBMBookmark _saveData:toFileURL:outError:].cold.2
+ +[ATXBMBookmark _saveData:toFileURL:outError:].cold.3
+ +[ATXBluetoothConnectedStream deviceTypeFromBiomeBluetoothDeviceType:]
+ +[ATXCarPlayConnectedEvent new]
+ +[ATXFeatureFlags controlCenterSuggestionsEnabled]
+ +[ATXFeatureFlags isSpotlightPlusEnabled]
+ +[ATXFeatureFlags isSpotlightPlusInternalToolKitInvocationsEnabled]
+ +[ATXFeatureFlags isSpotlightPlusModelDevelopmentEnabled]
+ +[ATXFeatureFlags widgetSuggestionsEnabled]
+ +[ATXGlobalStateForTesting sharedInstance]
+ +[ATXGlobalStateForTesting sharedInstance].cold.1
+ +[ATXPaths visualIntelligenceSessionLogFilePath]
+ +[ATXUtils logCurrentMemoryFootprint:]
+ +[ATXUtils logCurrentMemoryFootprint:].cold.1
+ +[ATXUtils shouldSkipExpensiveTask]
+ +[ATXUtils shuffle:]
+ +[NSError(ATXErrorSupport) atx_errorWithCode:]
+ +[NSError(ATXErrorSupport) atx_errorWithCode:debugDescription:]
+ +[NSError(ATXErrorSupport) atx_errorWithCode:debugDescription:underlyingError:]
+ +[NSError(ATXErrorSupport) atx_errorWithCode:debugDescription:underlyingErrors:]
+ +[NSError(ATXErrorSupport) atx_errorWithCode:userInfo:]
+ +[NSError(ATXErrorSupport) atx_errorWithCode:userInfoProvider:]
+ -[ATXAppClipUsageEvent .cxx_destruct]
+ -[ATXAppClipUsageEvent clipBundleID]
+ -[ATXAppClipUsageEvent fullURL]
+ -[ATXAppClipUsageEvent hash]
+ -[ATXAppClipUsageEvent initWithLaunchDate:urlHash:clipBundleID:parentAppBundleID:webAppBundleID:launchReason:fullURL:referrerURL:referrerBundleID:]
+ -[ATXAppClipUsageEvent init]
+ -[ATXAppClipUsageEvent isEqual:]
+ -[ATXAppClipUsageEvent isEqualToATXAppClipUsageEvent:]
+ -[ATXAppClipUsageEvent launchDate]
+ -[ATXAppClipUsageEvent launchReason]
+ -[ATXAppClipUsageEvent parentAppBundleID]
+ -[ATXAppClipUsageEvent referrerBundleID]
+ -[ATXAppClipUsageEvent referrerURL]
+ -[ATXAppClipUsageEvent urlHash]
+ -[ATXAppClipUsageEvent webAppBundleID]
+ -[ATXAppClipUsageStream _launchReasonFromString:]
+ -[ATXAppClipUsageStream _launchReasonFromString:].cold.1
+ -[ATXAppClipUsageStream _publisherWithStartDate:endDate:limit:shouldReverse:]
+ -[ATXAppClipUsageStream enumerateAppClipUsageEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXAppInFocusEvent .cxx_destruct]
+ -[ATXAppInFocusEvent absoluteTimestamp]
+ -[ATXAppInFocusEvent bundleID]
+ -[ATXAppInFocusEvent displayType]
+ -[ATXAppInFocusEvent encodeWithCoder:]
+ -[ATXAppInFocusEvent extensionHostID]
+ -[ATXAppInFocusEvent hash]
+ -[ATXAppInFocusEvent initWithBundleId:type:displayType:parentBundleID:extensionHostID:starting:absoluteTimestamp:launchReason:]
+ -[ATXAppInFocusEvent initWithBundleId:type:parentBundleID:extensionHostID:starting:absoluteTimestamp:launchReason:]
+ -[ATXAppInFocusEvent initWithCoder:]
+ -[ATXAppInFocusEvent isEqual:]
+ -[ATXAppInFocusEvent isEqualToATXAppInFocusEvent:]
+ -[ATXAppInFocusEvent launchReason]
+ -[ATXAppInFocusEvent parentBundleID]
+ -[ATXAppInFocusEvent starting]
+ -[ATXAppInFocusEvent type]
+ -[ATXAppInFocusEventSession .cxx_destruct]
+ -[ATXAppInFocusEventSession appSessionDuration]
+ -[ATXAppInFocusEventSession appSessionEndTime]
+ -[ATXAppInFocusEventSession appSessionStartTime]
+ -[ATXAppInFocusEventSession bundleID]
+ -[ATXAppInFocusEventSession displayType]
+ -[ATXAppInFocusEventSession encodeWithCoder:]
+ -[ATXAppInFocusEventSession extensionHostID]
+ -[ATXAppInFocusEventSession hash]
+ -[ATXAppInFocusEventSession initWithBundleId:type:displayType:parentBundleID:extensionHostID:appSessionStartTime:appSessionEndTime:launchReason:]
+ -[ATXAppInFocusEventSession initWithBundleId:type:parentBundleID:extensionHostID:appSessionStartTime:appSessionEndTime:launchReason:]
+ -[ATXAppInFocusEventSession initWithCoder:]
+ -[ATXAppInFocusEventSession isEqual:]
+ -[ATXAppInFocusEventSession isEqualToATXAppInFocusEventSession:]
+ -[ATXAppInFocusEventSession launchReason]
+ -[ATXAppInFocusEventSession parentBundleID]
+ -[ATXAppInFocusEventSession type]
+ -[ATXAppInFocusStream .cxx_destruct]
+ -[ATXAppInFocusStream _appLaunchPublisherWithStartDate:endDate:shouldReverse:]
+ -[ATXAppInFocusStream _atxAppInFocusDisplayTypeForBMAppInFocusDisplayType:]
+ -[ATXAppInFocusStream _atxAppInFocusDisplayTypeForBMAppInFocusDisplayType:].cold.1
+ -[ATXAppInFocusStream _atxAppInFocusEventTypeForBMAppInFocusType:]
+ -[ATXAppInFocusStream _atxAppInFocusEventTypeForBMAppInFocusType:].cold.1
+ -[ATXAppInFocusStream _createAppInFocusSessionFromEvent:startTime:endTime:]
+ -[ATXAppInFocusStream _enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]
+ -[ATXAppInFocusStream _enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:].cold.1
+ -[ATXAppInFocusStream _enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]
+ -[ATXAppInFocusStream _enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:].cold.1
+ -[ATXAppInFocusStream _fetchBMDeviceFromIDSIdentifier:]
+ -[ATXAppInFocusStream _fetchBMDeviceFromIDSIdentifier:].cold.1
+ -[ATXAppInFocusStream _fetchBMDeviceFromIDSIdentifier:].cold.2
+ -[ATXAppInFocusStream _getAppLaunchEventFromBMAppInFocus:]
+ -[ATXAppInFocusStream _getAppLaunchEventFromBMAppInFocus:].cold.1
+ -[ATXAppInFocusStream _getAppLaunchEventFromBMAppInFocus:].cold.2
+ -[ATXAppInFocusStream _shouldPairStartEvent:withEndEvent:]
+ -[ATXAppInFocusStream currentAppInFocusStartEventAtGivenTime:]
+ -[ATXAppInFocusStream enumerateAllAppLaunchSessionsFromStartDate:bundleIDFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:bundleIDFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:bundleIDsFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:bundleIDFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchEventsFromStartDate:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchEventsFromStartDate:bundleIDFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:bundleIDFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:bundleIDsFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:]
+ -[ATXAppInFocusStream enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:bundleIDFilter:block:]
+ -[ATXAppInFocusStream getFirstAppLaunchSessionBetweenStartDate:endDate:]
+ -[ATXAppInFocusStream getFirstAppLaunchStartEventBetweenStartDate:endDate:]
+ -[ATXAppInFocusStream getLastAppLaunchSessionBetweenStartDate:endDate:]
+ -[ATXAppInFocusStream getLastAppLaunchStartEventBetweenStartDate:endDate:]
+ -[ATXAppInFocusStream initWithRemoteIDSIdentifier:]
+ -[ATXAppInFocusStream numberOfAppLaunchEventsBetweenStartDate:endDate:]
+ -[ATXAppInFocusStream numberOfAppLaunchSessionsBetweenStartDate:endDate:forBundleID:]
+ -[ATXAudioRouteEvent .cxx_destruct]
+ -[ATXAudioRouteEvent connected]
+ -[ATXAudioRouteEvent endTime]
+ -[ATXAudioRouteEvent hash]
+ -[ATXAudioRouteEvent identifier]
+ -[ATXAudioRouteEvent initWithStartTime:endTime:connected:identifier:portType:portName:routeChangeReason:type:]
+ -[ATXAudioRouteEvent init]
+ -[ATXAudioRouteEvent isEqual:]
+ -[ATXAudioRouteEvent isEqualToATXAudioRouteEvent:]
+ -[ATXAudioRouteEvent portName]
+ -[ATXAudioRouteEvent portType]
+ -[ATXAudioRouteEvent routeChangeReason]
+ -[ATXAudioRouteEvent startTime]
+ -[ATXAudioRouteEvent type]
+ -[ATXAudioRouteStream _enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXAudioRouteStream _publisherWithStartDate:endDate:limit:shouldReverse:]
+ -[ATXAudioRouteStream enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXAudioRouteStream enumerateDisconnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXBluetoothConnectedEvent .cxx_destruct]
+ -[ATXBluetoothConnectedEvent connected]
+ -[ATXBluetoothConnectedEvent deviceAddress]
+ -[ATXBluetoothConnectedEvent deviceName]
+ -[ATXBluetoothConnectedEvent deviceType]
+ -[ATXBluetoothConnectedEvent endTime]
+ -[ATXBluetoothConnectedEvent hash]
+ -[ATXBluetoothConnectedEvent initWithStartTime:endTime:connected:deviceAddress:deviceName:deviceType:]
+ -[ATXBluetoothConnectedEvent init]
+ -[ATXBluetoothConnectedEvent isEqual:]
+ -[ATXBluetoothConnectedEvent isEqualToATXBluetoothConnectedEvent:]
+ -[ATXBluetoothConnectedEvent startTime]
+ -[ATXBluetoothConnectedStream _bluetoothPublisherWithStartDate:endDate:limit:shouldReverse:]
+ -[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXBluetoothConnectedStream enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXBluetoothConnectedStream enumerateDisconnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXCarPlayConnectedEvent .cxx_destruct]
+ -[ATXCarPlayConnectedEvent connected]
+ -[ATXCarPlayConnectedEvent endTime]
+ -[ATXCarPlayConnectedEvent hash]
+ -[ATXCarPlayConnectedEvent initWithStartTime:endTime:connected:]
+ -[ATXCarPlayConnectedEvent init]
+ -[ATXCarPlayConnectedEvent isEqual:]
+ -[ATXCarPlayConnectedEvent isEqualToATXCarPlayConnectedEvent:]
+ -[ATXCarPlayConnectedEvent startTime]
+ -[ATXCarPlayConnectedStream _carPlayPublisherWithStartDate:endDate:limit:shouldReverse:]
+ -[ATXCarPlayConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXCarPlayConnectedStream enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXCarPlayConnectedStream enumerateDisconnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXChargerPluggedInEvent .cxx_destruct]
+ -[ATXChargerPluggedInEvent adapterType]
+ -[ATXChargerPluggedInEvent connected]
+ -[ATXChargerPluggedInEvent endTime]
+ -[ATXChargerPluggedInEvent hash]
+ -[ATXChargerPluggedInEvent initWithStartTime:endTime:connected:adapterType:]
+ -[ATXChargerPluggedInEvent init]
+ -[ATXChargerPluggedInEvent isEqual:]
+ -[ATXChargerPluggedInEvent isEqualToATXChargerPluggedInEvent:]
+ -[ATXChargerPluggedInEvent startTime]
+ -[ATXChargerPluggedInStream _chargerPluggedInPublisherWithStartDate:endDate:]
+ -[ATXChargerPluggedInStream enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:]
+ -[ATXChargerPluggedInStream enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:].cold.1
+ -[ATXDeviceScreenLockStateEvent .cxx_destruct]
+ -[ATXDeviceScreenLockStateEvent endTime]
+ -[ATXDeviceScreenLockStateEvent hash]
+ -[ATXDeviceScreenLockStateEvent initWithStartTime:endTime:isLocked:]
+ -[ATXDeviceScreenLockStateEvent init]
+ -[ATXDeviceScreenLockStateEvent isEqual:]
+ -[ATXDeviceScreenLockStateEvent isEqualToATXDeviceScreenLockStateEvent:]
+ -[ATXDeviceScreenLockStateEvent isLocked]
+ -[ATXDeviceScreenLockStateEvent startTime]
+ -[ATXDeviceScreenLockStateStream _deviceScreenLockedPublisherWithStartDate:endDate:limit:shouldReverse:]
+ -[ATXDeviceScreenLockStateStream _enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXDeviceScreenLockStateStream enumerateDeviceScreenLockedStateEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXDeviceScreenLockStateStream enumerateDeviceScreenUnLockedStateEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXDisplayOnIntervalEvent .cxx_destruct]
+ -[ATXDisplayOnIntervalEvent hash]
+ -[ATXDisplayOnIntervalEvent initWithOnInterval:]
+ -[ATXDisplayOnIntervalEvent init]
+ -[ATXDisplayOnIntervalEvent isEqual:]
+ -[ATXDisplayOnIntervalEvent isEqualToATXDisplayOnIntervalEvent:]
+ -[ATXDisplayOnIntervalEvent onInterval]
+ -[ATXDisplayOnIntervalEvent prettyRepresentation]
+ -[ATXDisplayOnIntervalStream _displayBacklightPublisherWithStartDate:endDate:]
+ -[ATXDisplayOnIntervalStream displayStateAtTime:]
+ -[ATXDisplayOnIntervalStream enumerateDisplayOnIntervalsFromStartDate:endDate:block:]
+ -[ATXDisplayOnIntervalStream enumerateDisplayOnIntervalsFromStartDate:endDate:block:].cold.1
+ -[ATXDisplayOnIntervalStream enumerateDisplayStateEventsFromStartDate:endDate:block:]
+ -[ATXDisplayOnIntervalStream enumerateDisplayStateEventsFromStartDate:endDate:block:].cold.1
+ -[ATXDisplayStateEvent .cxx_destruct]
+ -[ATXDisplayStateEvent absoluteTimestamp]
+ -[ATXDisplayStateEvent displayState]
+ -[ATXDisplayStateEvent initWithDisplayState:absoluteTimestamp:]
+ -[ATXDisplayStateEvent init]
+ -[ATXDocumentInteractionEvent .cxx_destruct]
+ -[ATXDocumentInteractionEvent bookmarkData]
+ -[ATXDocumentInteractionEvent hash]
+ -[ATXDocumentInteractionEvent initWithBMAppDocumentInteraction:]
+ -[ATXDocumentInteractionEvent initWithBMAppDocumentInteraction:].cold.1
+ -[ATXDocumentInteractionEvent initWithBMAppDocumentInteraction:].cold.2
+ -[ATXDocumentInteractionEvent initWithBMAppDocumentInteraction:].cold.3
+ -[ATXDocumentInteractionEvent initWithBMAppDocumentInteraction:].cold.4
+ -[ATXDocumentInteractionEvent initWithBMAppDocumentInteraction:].cold.5
+ -[ATXDocumentInteractionEvent initWithInteractionType:originalFileURL:bookmarkData:isRemote:]
+ -[ATXDocumentInteractionEvent init]
+ -[ATXDocumentInteractionEvent isEqual:]
+ -[ATXDocumentInteractionEvent isEqualToATXDocumentInteractionEvent:]
+ -[ATXDocumentInteractionEvent isRemote]
+ -[ATXDocumentInteractionEvent originalFileURL]
+ -[ATXDocumentInteractionEvent type]
+ -[ATXDocumentInteractionStream _documentInteractionPublisherWithStartDate:endDate:limit:]
+ -[ATXDocumentInteractionStream enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:]
+ -[ATXDocumentInteractionStream enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:].cold.1
+ -[ATXDocumentInteractionStream getDocumentsOpenedInLastMonth]
+ -[ATXGlobalStateForTesting .cxx_destruct]
+ -[ATXGlobalStateForTesting clipBoardContentForTesting]
+ -[ATXGlobalStateForTesting clipboardContentForTesting]
+ -[ATXGlobalStateForTesting isTestModeEnabled]
+ -[ATXGlobalStateForTesting setClipBoardContentForTesting:]
+ -[ATXGlobalStateForTesting setClipboardContentForTesting:]
+ -[ATXGlobalStateForTesting setTestMode:]
+ -[ATXGlobalStateForTesting setTestModeEnabled:]
+ -[ATXGlobalStateForTesting testModeEnabled]
+ -[ATXMediaNowPlayingEvent .cxx_destruct]
+ -[ATXMediaNowPlayingEvent bundleID]
+ -[ATXMediaNowPlayingEvent debugDescription]
+ -[ATXMediaNowPlayingEvent endTime]
+ -[ATXMediaNowPlayingEvent eventDuration]
+ -[ATXMediaNowPlayingEvent hash]
+ -[ATXMediaNowPlayingEvent initWithStartTime:endTime:bundleID:title:playbackState:]
+ -[ATXMediaNowPlayingEvent init]
+ -[ATXMediaNowPlayingEvent isEqual:]
+ -[ATXMediaNowPlayingEvent isEqualToATXMediaNowPlayingEvent:]
+ -[ATXMediaNowPlayingEvent playbackState]
+ -[ATXMediaNowPlayingEvent startTime]
+ -[ATXMediaNowPlayingEvent title]
+ -[ATXMediaNowPlayingStream _publisherWithStartDate:endDate:shouldReverse:]
+ -[ATXMediaNowPlayingStream _shouldPairStartEvent:withEndEvent:]
+ -[ATXMediaNowPlayingStream atxPlaybackStateFromBMPlaybackState:]
+ -[ATXMediaNowPlayingStream enumerateEventsFromStartDate:endDate:filterBlock:ascending:block:]
+ -[ATXMediaNowPlayingStream enumerateEventsFromStartDate:endDate:filterBlock:ascending:block:].cold.1
+ -[ATXMediaNowPlayingStream getATXMediaNowPlayingEventFromBiomeEvent:]
+ GCC_except_table0
+ GCC_except_table13
+ GCC_except_table15
+ GCC_except_table2
+ GCC_except_table27
+ GCC_except_table3
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table9
+ _ATXBundleIdForRemoteBundleId
+ _ATXErrorDomain
+ _ATXIsRemoteAppBundleId
+ _ATXMemoryUsageInMBOfCurrentProcess
+ _ATXRemoteBundleIdForBundleId
+ _NSLocalizedDescriptionKey
+ _NSMultipleUnderlyingErrorsKey
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_ATXAppClipUsageEvent
+ _OBJC_CLASS_$_ATXAppClipUsageStream
+ _OBJC_CLASS_$_ATXAppInFocusEvent
+ _OBJC_CLASS_$_ATXAppInFocusEventSession
+ _OBJC_CLASS_$_ATXAppInFocusStream
+ _OBJC_CLASS_$_ATXAudioRouteEvent
+ _OBJC_CLASS_$_ATXAudioRouteStream
+ _OBJC_CLASS_$_ATXBluetoothConnectedEvent
+ _OBJC_CLASS_$_ATXBluetoothConnectedStream
+ _OBJC_CLASS_$_ATXCarPlayConnectedEvent
+ _OBJC_CLASS_$_ATXCarPlayConnectedStream
+ _OBJC_CLASS_$_ATXChargerPluggedInEvent
+ _OBJC_CLASS_$_ATXChargerPluggedInStream
+ _OBJC_CLASS_$_ATXDeviceScreenLockStateEvent
+ _OBJC_CLASS_$_ATXDeviceScreenLockStateStream
+ _OBJC_CLASS_$_ATXDisplayOnIntervalEvent
+ _OBJC_CLASS_$_ATXDisplayOnIntervalStream
+ _OBJC_CLASS_$_ATXDisplayStateEvent
+ _OBJC_CLASS_$_ATXDocumentInteractionEvent
+ _OBJC_CLASS_$_ATXDocumentInteractionStream
+ _OBJC_CLASS_$_ATXGlobalStateForTesting
+ _OBJC_CLASS_$_ATXMediaNowPlayingEvent
+ _OBJC_CLASS_$_ATXMediaNowPlayingStream
+ _OBJC_CLASS_$_ATXUtils
+ _OBJC_CLASS_$_BMPairedEventSession
+ _OBJC_CLASS_$_BMSyncService
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$__CDClientContext
+ _OBJC_CLASS_$__CDContextQueries
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._clipBundleID
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._fullURL
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._launchDate
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._launchReason
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._parentAppBundleID
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._referrerBundleID
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._referrerURL
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._urlHash
+ _OBJC_IVAR_$_ATXAppClipUsageEvent._webAppBundleID
+ _OBJC_IVAR_$_ATXAppInFocusEvent._absoluteTimestamp
+ _OBJC_IVAR_$_ATXAppInFocusEvent._bundleID
+ _OBJC_IVAR_$_ATXAppInFocusEvent._displayType
+ _OBJC_IVAR_$_ATXAppInFocusEvent._extensionHostID
+ _OBJC_IVAR_$_ATXAppInFocusEvent._launchReason
+ _OBJC_IVAR_$_ATXAppInFocusEvent._parentBundleID
+ _OBJC_IVAR_$_ATXAppInFocusEvent._starting
+ _OBJC_IVAR_$_ATXAppInFocusEvent._type
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._appSessionEndTime
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._appSessionStartTime
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._bundleID
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._displayType
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._extensionHostID
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._launchReason
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._parentBundleID
+ _OBJC_IVAR_$_ATXAppInFocusEventSession._type
+ _OBJC_IVAR_$_ATXAppInFocusStream._remoteIDSIdentifier
+ _OBJC_IVAR_$_ATXAudioRouteEvent._connected
+ _OBJC_IVAR_$_ATXAudioRouteEvent._endTime
+ _OBJC_IVAR_$_ATXAudioRouteEvent._identifier
+ _OBJC_IVAR_$_ATXAudioRouteEvent._portName
+ _OBJC_IVAR_$_ATXAudioRouteEvent._portType
+ _OBJC_IVAR_$_ATXAudioRouteEvent._routeChangeReason
+ _OBJC_IVAR_$_ATXAudioRouteEvent._startTime
+ _OBJC_IVAR_$_ATXAudioRouteEvent._type
+ _OBJC_IVAR_$_ATXBluetoothConnectedEvent._connected
+ _OBJC_IVAR_$_ATXBluetoothConnectedEvent._deviceAddress
+ _OBJC_IVAR_$_ATXBluetoothConnectedEvent._deviceName
+ _OBJC_IVAR_$_ATXBluetoothConnectedEvent._deviceType
+ _OBJC_IVAR_$_ATXBluetoothConnectedEvent._endTime
+ _OBJC_IVAR_$_ATXBluetoothConnectedEvent._startTime
+ _OBJC_IVAR_$_ATXCarPlayConnectedEvent._connected
+ _OBJC_IVAR_$_ATXCarPlayConnectedEvent._endTime
+ _OBJC_IVAR_$_ATXCarPlayConnectedEvent._startTime
+ _OBJC_IVAR_$_ATXChargerPluggedInEvent._adapterType
+ _OBJC_IVAR_$_ATXChargerPluggedInEvent._connected
+ _OBJC_IVAR_$_ATXChargerPluggedInEvent._endTime
+ _OBJC_IVAR_$_ATXChargerPluggedInEvent._startTime
+ _OBJC_IVAR_$_ATXDeviceScreenLockStateEvent._endTime
+ _OBJC_IVAR_$_ATXDeviceScreenLockStateEvent._isLocked
+ _OBJC_IVAR_$_ATXDeviceScreenLockStateEvent._startTime
+ _OBJC_IVAR_$_ATXDisplayOnIntervalEvent._onInterval
+ _OBJC_IVAR_$_ATXDisplayStateEvent._absoluteTimestamp
+ _OBJC_IVAR_$_ATXDisplayStateEvent._displayState
+ _OBJC_IVAR_$_ATXDocumentInteractionEvent._bookmarkData
+ _OBJC_IVAR_$_ATXDocumentInteractionEvent._isRemote
+ _OBJC_IVAR_$_ATXDocumentInteractionEvent._originalFileURL
+ _OBJC_IVAR_$_ATXDocumentInteractionEvent._type
+ _OBJC_IVAR_$_ATXGlobalStateForTesting._clipboardContentForTesting
+ _OBJC_IVAR_$_ATXGlobalStateForTesting._testModeEnabled
+ _OBJC_IVAR_$_ATXMediaNowPlayingEvent._bundleID
+ _OBJC_IVAR_$_ATXMediaNowPlayingEvent._endTime
+ _OBJC_IVAR_$_ATXMediaNowPlayingEvent._playbackState
+ _OBJC_IVAR_$_ATXMediaNowPlayingEvent._startTime
+ _OBJC_IVAR_$_ATXMediaNowPlayingEvent._title
+ _OBJC_METACLASS_$_ATXAppClipUsageEvent
+ _OBJC_METACLASS_$_ATXAppClipUsageStream
+ _OBJC_METACLASS_$_ATXAppInFocusEvent
+ _OBJC_METACLASS_$_ATXAppInFocusEventSession
+ _OBJC_METACLASS_$_ATXAppInFocusStream
+ _OBJC_METACLASS_$_ATXAudioRouteEvent
+ _OBJC_METACLASS_$_ATXAudioRouteStream
+ _OBJC_METACLASS_$_ATXBluetoothConnectedEvent
+ _OBJC_METACLASS_$_ATXBluetoothConnectedStream
+ _OBJC_METACLASS_$_ATXCarPlayConnectedEvent
+ _OBJC_METACLASS_$_ATXCarPlayConnectedStream
+ _OBJC_METACLASS_$_ATXChargerPluggedInEvent
+ _OBJC_METACLASS_$_ATXChargerPluggedInStream
+ _OBJC_METACLASS_$_ATXDeviceScreenLockStateEvent
+ _OBJC_METACLASS_$_ATXDeviceScreenLockStateStream
+ _OBJC_METACLASS_$_ATXDisplayOnIntervalEvent
+ _OBJC_METACLASS_$_ATXDisplayOnIntervalStream
+ _OBJC_METACLASS_$_ATXDisplayStateEvent
+ _OBJC_METACLASS_$_ATXDocumentInteractionEvent
+ _OBJC_METACLASS_$_ATXDocumentInteractionStream
+ _OBJC_METACLASS_$_ATXGlobalStateForTesting
+ _OBJC_METACLASS_$_ATXMediaNowPlayingEvent
+ _OBJC_METACLASS_$_ATXMediaNowPlayingStream
+ _OBJC_METACLASS_$_ATXUtils
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_ATXErrorSupport
+ __OBJC_$_CATEGORY_NSError_$_ATXErrorSupport
+ __OBJC_$_CLASS_METHODS_ATXAppInFocusEvent
+ __OBJC_$_CLASS_METHODS_ATXAppInFocusEventSession
+ __OBJC_$_CLASS_METHODS_ATXAppInFocusStream
+ __OBJC_$_CLASS_METHODS_ATXAudioRouteStream
+ __OBJC_$_CLASS_METHODS_ATXBluetoothConnectedStream
+ __OBJC_$_CLASS_METHODS_ATXCarPlayConnectedEvent
+ __OBJC_$_CLASS_METHODS_ATXGlobalStateForTesting
+ __OBJC_$_CLASS_METHODS_ATXUtils
+ __OBJC_$_CLASS_PROP_LIST_ATXAppInFocusEvent
+ __OBJC_$_CLASS_PROP_LIST_ATXAppInFocusEventSession
+ __OBJC_$_INSTANCE_METHODS_ATXAppClipUsageEvent
+ __OBJC_$_INSTANCE_METHODS_ATXAppClipUsageStream
+ __OBJC_$_INSTANCE_METHODS_ATXAppInFocusEvent
+ __OBJC_$_INSTANCE_METHODS_ATXAppInFocusEventSession
+ __OBJC_$_INSTANCE_METHODS_ATXAppInFocusStream
+ __OBJC_$_INSTANCE_METHODS_ATXAudioRouteEvent
+ __OBJC_$_INSTANCE_METHODS_ATXAudioRouteStream
+ __OBJC_$_INSTANCE_METHODS_ATXBluetoothConnectedEvent
+ __OBJC_$_INSTANCE_METHODS_ATXBluetoothConnectedStream
+ __OBJC_$_INSTANCE_METHODS_ATXCarPlayConnectedEvent
+ __OBJC_$_INSTANCE_METHODS_ATXCarPlayConnectedStream
+ __OBJC_$_INSTANCE_METHODS_ATXChargerPluggedInEvent
+ __OBJC_$_INSTANCE_METHODS_ATXChargerPluggedInStream
+ __OBJC_$_INSTANCE_METHODS_ATXDeviceScreenLockStateEvent
+ __OBJC_$_INSTANCE_METHODS_ATXDeviceScreenLockStateStream
+ __OBJC_$_INSTANCE_METHODS_ATXDisplayOnIntervalEvent
+ __OBJC_$_INSTANCE_METHODS_ATXDisplayOnIntervalStream
+ __OBJC_$_INSTANCE_METHODS_ATXDisplayStateEvent
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentInteractionEvent
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentInteractionStream
+ __OBJC_$_INSTANCE_METHODS_ATXGlobalStateForTesting
+ __OBJC_$_INSTANCE_METHODS_ATXMediaNowPlayingEvent
+ __OBJC_$_INSTANCE_METHODS_ATXMediaNowPlayingStream
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppClipUsageEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppInFocusEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppInFocusEventSession
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppInFocusStream
+ __OBJC_$_INSTANCE_VARIABLES_ATXAudioRouteEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXBluetoothConnectedEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXCarPlayConnectedEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXChargerPluggedInEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXDeviceScreenLockStateEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXDisplayOnIntervalEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXDisplayStateEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXDocumentInteractionEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXGlobalStateForTesting
+ __OBJC_$_INSTANCE_VARIABLES_ATXMediaNowPlayingEvent
+ __OBJC_$_PROP_LIST_ATXAppClipUsageEvent
+ __OBJC_$_PROP_LIST_ATXAppClipUsageStream
+ __OBJC_$_PROP_LIST_ATXAppInFocusEvent
+ __OBJC_$_PROP_LIST_ATXAppInFocusEventSession
+ __OBJC_$_PROP_LIST_ATXAppInFocusStream
+ __OBJC_$_PROP_LIST_ATXAudioRouteEvent
+ __OBJC_$_PROP_LIST_ATXAudioRouteStream
+ __OBJC_$_PROP_LIST_ATXBluetoothConnectedEvent
+ __OBJC_$_PROP_LIST_ATXBluetoothConnectedStream
+ __OBJC_$_PROP_LIST_ATXCarPlayConnectedEvent
+ __OBJC_$_PROP_LIST_ATXCarPlayConnectedStream
+ __OBJC_$_PROP_LIST_ATXChargerPluggedInEvent
+ __OBJC_$_PROP_LIST_ATXChargerPluggedInStream
+ __OBJC_$_PROP_LIST_ATXDeviceScreenLockStateEvent
+ __OBJC_$_PROP_LIST_ATXDeviceScreenLockStateStream
+ __OBJC_$_PROP_LIST_ATXDisplayOnIntervalEvent
+ __OBJC_$_PROP_LIST_ATXDisplayOnIntervalStream
+ __OBJC_$_PROP_LIST_ATXDisplayStateEvent
+ __OBJC_$_PROP_LIST_ATXDocumentInteractionEvent
+ __OBJC_$_PROP_LIST_ATXDocumentInteractionStream
+ __OBJC_$_PROP_LIST_ATXGlobalStateForTesting
+ __OBJC_$_PROP_LIST_ATXMediaNowPlayingEvent
+ __OBJC_$_PROP_LIST_ATXMediaNowPlayingStream
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_ATXGenericEventBase
+ __OBJC_$_PROTOCOL_REFS_ATXGenericEventStreamBase
+ __OBJC_CLASS_PROTOCOLS_$_ATXAppClipUsageEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXAppClipUsageStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXAppInFocusEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXAppInFocusEventSession
+ __OBJC_CLASS_PROTOCOLS_$_ATXAppInFocusStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXAudioRouteEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXAudioRouteStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXBluetoothConnectedEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXBluetoothConnectedStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXCarPlayConnectedEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXCarPlayConnectedStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXChargerPluggedInEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXChargerPluggedInStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXDeviceScreenLockStateEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXDeviceScreenLockStateStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXDisplayOnIntervalEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXDisplayOnIntervalStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXDisplayStateEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXDocumentInteractionEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXDocumentInteractionStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXMediaNowPlayingEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXMediaNowPlayingStream
+ __OBJC_CLASS_RO_$_ATXAppClipUsageEvent
+ __OBJC_CLASS_RO_$_ATXAppClipUsageStream
+ __OBJC_CLASS_RO_$_ATXAppInFocusEvent
+ __OBJC_CLASS_RO_$_ATXAppInFocusEventSession
+ __OBJC_CLASS_RO_$_ATXAppInFocusStream
+ __OBJC_CLASS_RO_$_ATXAudioRouteEvent
+ __OBJC_CLASS_RO_$_ATXAudioRouteStream
+ __OBJC_CLASS_RO_$_ATXBluetoothConnectedEvent
+ __OBJC_CLASS_RO_$_ATXBluetoothConnectedStream
+ __OBJC_CLASS_RO_$_ATXCarPlayConnectedEvent
+ __OBJC_CLASS_RO_$_ATXCarPlayConnectedStream
+ __OBJC_CLASS_RO_$_ATXChargerPluggedInEvent
+ __OBJC_CLASS_RO_$_ATXChargerPluggedInStream
+ __OBJC_CLASS_RO_$_ATXDeviceScreenLockStateEvent
+ __OBJC_CLASS_RO_$_ATXDeviceScreenLockStateStream
+ __OBJC_CLASS_RO_$_ATXDisplayOnIntervalEvent
+ __OBJC_CLASS_RO_$_ATXDisplayOnIntervalStream
+ __OBJC_CLASS_RO_$_ATXDisplayStateEvent
+ __OBJC_CLASS_RO_$_ATXDocumentInteractionEvent
+ __OBJC_CLASS_RO_$_ATXDocumentInteractionStream
+ __OBJC_CLASS_RO_$_ATXGlobalStateForTesting
+ __OBJC_CLASS_RO_$_ATXMediaNowPlayingEvent
+ __OBJC_CLASS_RO_$_ATXMediaNowPlayingStream
+ __OBJC_CLASS_RO_$_ATXUtils
+ __OBJC_LABEL_PROTOCOL_$_ATXGenericEventBase
+ __OBJC_LABEL_PROTOCOL_$_ATXGenericEventStreamBase
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_ATXAppClipUsageEvent
+ __OBJC_METACLASS_RO_$_ATXAppClipUsageStream
+ __OBJC_METACLASS_RO_$_ATXAppInFocusEvent
+ __OBJC_METACLASS_RO_$_ATXAppInFocusEventSession
+ __OBJC_METACLASS_RO_$_ATXAppInFocusStream
+ __OBJC_METACLASS_RO_$_ATXAudioRouteEvent
+ __OBJC_METACLASS_RO_$_ATXAudioRouteStream
+ __OBJC_METACLASS_RO_$_ATXBluetoothConnectedEvent
+ __OBJC_METACLASS_RO_$_ATXBluetoothConnectedStream
+ __OBJC_METACLASS_RO_$_ATXCarPlayConnectedEvent
+ __OBJC_METACLASS_RO_$_ATXCarPlayConnectedStream
+ __OBJC_METACLASS_RO_$_ATXChargerPluggedInEvent
+ __OBJC_METACLASS_RO_$_ATXChargerPluggedInStream
+ __OBJC_METACLASS_RO_$_ATXDeviceScreenLockStateEvent
+ __OBJC_METACLASS_RO_$_ATXDeviceScreenLockStateStream
+ __OBJC_METACLASS_RO_$_ATXDisplayOnIntervalEvent
+ __OBJC_METACLASS_RO_$_ATXDisplayOnIntervalStream
+ __OBJC_METACLASS_RO_$_ATXDisplayStateEvent
+ __OBJC_METACLASS_RO_$_ATXDocumentInteractionEvent
+ __OBJC_METACLASS_RO_$_ATXDocumentInteractionStream
+ __OBJC_METACLASS_RO_$_ATXGlobalStateForTesting
+ __OBJC_METACLASS_RO_$_ATXMediaNowPlayingEvent
+ __OBJC_METACLASS_RO_$_ATXMediaNowPlayingStream
+ __OBJC_METACLASS_RO_$_ATXUtils
+ __OBJC_PROTOCOL_$_ATXGenericEventBase
+ __OBJC_PROTOCOL_$_ATXGenericEventStreamBase
+ __OBJC_PROTOCOL_$_NSObject
+ ___107-[ATXCarPlayConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke
+ ___107-[ATXCarPlayConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.1
+ ___107-[ATXCarPlayConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.1.cold.1
+ ___107-[ATXCarPlayConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.cold.1
+ ___108-[ATXAppClipUsageStream enumerateAppClipUsageEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke
+ ___108-[ATXAppClipUsageStream enumerateAppClipUsageEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.11
+ ___108-[ATXAppClipUsageStream enumerateAppClipUsageEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.cold.1
+ ___109-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke
+ ___109-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.2
+ ___109-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.2.cold.1
+ ___109-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.2.cold.2
+ ___109-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.2.cold.3
+ ___109-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.cold.1
+ ___112-[ATXAudioRouteStream _enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke
+ ___112-[ATXAudioRouteStream _enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.2
+ ___112-[ATXAudioRouteStream _enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.2.cold.1
+ ___112-[ATXAudioRouteStream _enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.cold.1
+ ___112-[ATXDocumentInteractionStream enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke
+ ___112-[ATXDocumentInteractionStream enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke.23
+ ___112-[ATXDocumentInteractionStream enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke.cold.1
+ ___117-[ATXDeviceScreenLockStateStream _enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke
+ ___117-[ATXDeviceScreenLockStateStream _enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.11
+ ___117-[ATXDeviceScreenLockStateStream _enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.11.cold.1
+ ___117-[ATXDeviceScreenLockStateStream _enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.cold.1
+ ___126-[ATXAppInFocusStream _enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke
+ ___126-[ATXAppInFocusStream _enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke.26
+ ___126-[ATXAppInFocusStream _enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke.cold.1
+ ___128-[ATXAppInFocusStream _enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke
+ ___128-[ATXAppInFocusStream _enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke.31
+ ___128-[ATXAppInFocusStream _enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke.cold.1
+ ___131-[ATXAppInFocusStream enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke
+ ___133-[ATXAppInFocusStream enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:]_block_invoke
+ ___42+[ATXGlobalStateForTesting sharedInstance]_block_invoke
+ ___49-[ATXDisplayOnIntervalStream displayStateAtTime:]_block_invoke
+ ___49-[ATXDisplayOnIntervalStream displayStateAtTime:]_block_invoke.31
+ ___49-[ATXDisplayOnIntervalStream displayStateAtTime:]_block_invoke.cold.1
+ ___55-[ATXAppInFocusStream _fetchBMDeviceFromIDSIdentifier:]_block_invoke
+ ___61-[ATXDocumentInteractionStream getDocumentsOpenedInLastMonth]_block_invoke
+ ___61-[ATXDocumentInteractionStream getDocumentsOpenedInLastMonth]_block_invoke_2
+ ___61-[ATXDocumentInteractionStream getDocumentsOpenedInLastMonth]_block_invoke_3
+ ___62-[ATXAppInFocusStream currentAppInFocusStartEventAtGivenTime:]_block_invoke
+ ___62-[ATXAppInFocusStream currentAppInFocusStartEventAtGivenTime:]_block_invoke.15
+ ___62-[ATXAppInFocusStream currentAppInFocusStartEventAtGivenTime:]_block_invoke.cold.1
+ ___71-[ATXAppInFocusStream getLastAppLaunchSessionBetweenStartDate:endDate:]_block_invoke
+ ___71-[ATXAppInFocusStream numberOfAppLaunchEventsBetweenStartDate:endDate:]_block_invoke
+ ___72-[ATXAppInFocusStream getFirstAppLaunchSessionBetweenStartDate:endDate:]_block_invoke
+ ___74-[ATXAppInFocusStream getLastAppLaunchStartEventBetweenStartDate:endDate:]_block_invoke
+ ___75-[ATXAppInFocusStream getFirstAppLaunchStartEventBetweenStartDate:endDate:]_block_invoke
+ ___85-[ATXAppInFocusStream numberOfAppLaunchSessionsBetweenStartDate:endDate:forBundleID:]_block_invoke
+ ___85-[ATXDisplayOnIntervalStream enumerateDisplayOnIntervalsFromStartDate:endDate:block:]_block_invoke
+ ___85-[ATXDisplayOnIntervalStream enumerateDisplayOnIntervalsFromStartDate:endDate:block:]_block_invoke.17
+ ___85-[ATXDisplayOnIntervalStream enumerateDisplayOnIntervalsFromStartDate:endDate:block:]_block_invoke.cold.1
+ ___85-[ATXDisplayOnIntervalStream enumerateDisplayStateEventsFromStartDate:endDate:block:]_block_invoke
+ ___85-[ATXDisplayOnIntervalStream enumerateDisplayStateEventsFromStartDate:endDate:block:]_block_invoke.26
+ ___85-[ATXDisplayOnIntervalStream enumerateDisplayStateEventsFromStartDate:endDate:block:]_block_invoke.cold.1
+ ___93-[ATXMediaNowPlayingStream enumerateEventsFromStartDate:endDate:filterBlock:ascending:block:]_block_invoke
+ ___93-[ATXMediaNowPlayingStream enumerateEventsFromStartDate:endDate:filterBlock:ascending:block:]_block_invoke.18
+ ___93-[ATXMediaNowPlayingStream enumerateEventsFromStartDate:endDate:filterBlock:ascending:block:]_block_invoke.cold.1
+ ___99-[ATXChargerPluggedInStream enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke
+ ___99-[ATXChargerPluggedInStream enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke.21
+ ___99-[ATXChargerPluggedInStream enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke_2
+ ___99-[ATXChargerPluggedInStream enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:]_block_invoke_2.cold.1
+ ___NSArray0__struct
+ _____atxlog_handle_client_donations_block_invoke
+ _____atxlog_handle_document_predictor_block_invoke
+ _____atxlog_handle_menu_items_block_invoke
+ _____atxlog_handle_ml_inference_block_invoke
+ _____atxlog_handle_screen_entities_block_invoke
+ ___atxlog_handle_client_donations
+ ___atxlog_handle_client_donations.cold.1
+ ___atxlog_handle_client_donations.log
+ ___atxlog_handle_client_donations.onceToken
+ ___atxlog_handle_document_predictor
+ ___atxlog_handle_document_predictor.cold.1
+ ___atxlog_handle_document_predictor.log
+ ___atxlog_handle_document_predictor.onceToken
+ ___atxlog_handle_menu_items
+ ___atxlog_handle_menu_items.cold.1
+ ___atxlog_handle_menu_items.log
+ ___atxlog_handle_menu_items.onceToken
+ ___atxlog_handle_ml_inference
+ ___atxlog_handle_ml_inference.cold.1
+ ___atxlog_handle_ml_inference.log
+ ___atxlog_handle_ml_inference.onceToken
+ ___atxlog_handle_screen_entities
+ ___atxlog_handle_screen_entities.cold.1
+ ___atxlog_handle_screen_entities.log
+ ___atxlog_handle_screen_entities.onceToken
+ ___block_descriptor_32_e22_B16?0"BMStoreEvent"8l
+ ___block_descriptor_32_e37_B16?0"ATXDocumentInteractionEvent"8l
+ ___block_descriptor_40_e8_32bs_e22_B16?0"BMStoreEvent"8ls32l8
+ ___block_descriptor_40_e8_32r_e28_B16?0"ATXAppInFocusEvent"8lr32l8
+ ___block_descriptor_40_e8_32r_e35_B16?0"ATXAppInFocusEventSession"8lr32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"BMDevice"8ls32l8
+ ___block_descriptor_40_e8_32s_e30_v32?0"NSURL"8"NSData"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e37_v16?0"ATXDocumentInteractionEvent"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e22_v16?0"BMStoreEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40bs_e30_v16?0"BMPairedEventSession"8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40r_e22_B16?0"BMStoreEvent"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e22_v16?0"BMStoreEvent"8ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40r_e28_B16?0"ATXAppInFocusEvent"8lr40l8s32l8
+ ___block_descriptor_56_e8_32bs40r_e35_B16?0"ATXAppInFocusEventSession"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e22_B16?0"BMStoreEvent"8ls32l8r48l8s40l8
+ ___block_descriptor_58_e8_32bs40bs48r_e22_B16?0"BMStoreEvent"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40bs48bs56r_e22_B16?0"BMStoreEvent"8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48bs56bs_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56bs_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.137
+ ___block_literal_global.140
+ ___block_literal_global.25
+ ___block_literal_global.30
+ ___block_literal_global.31
+ _kATXCurrentMirroredPhoneIDSIdentifier
+ _mach_task_self_
+ _objc_msgSend$App
+ _objc_msgSend$Audio
+ _objc_msgSend$Backlight
+ _objc_msgSend$Bluetooth
+ _objc_msgSend$CarPlay
+ _objc_msgSend$Clip
+ _objc_msgSend$Connected
+ _objc_msgSend$Device
+ _objc_msgSend$Display
+ _objc_msgSend$InFocus
+ _objc_msgSend$Media
+ _objc_msgSend$NowPlaying
+ _objc_msgSend$PluggedIn
+ _objc_msgSend$Power
+ _objc_msgSend$Route
+ _objc_msgSend$ScreenLocked
+ _objc_msgSend$URLHash
+ _objc_msgSend$Wireless
+ _objc_msgSend$_appLaunchPublisherWithStartDate:endDate:shouldReverse:
+ _objc_msgSend$_atxAppInFocusDisplayTypeForBMAppInFocusDisplayType:
+ _objc_msgSend$_atxAppInFocusEventTypeForBMAppInFocusType:
+ _objc_msgSend$_bluetoothPublisherWithStartDate:endDate:limit:shouldReverse:
+ _objc_msgSend$_carPlayPublisherWithStartDate:endDate:limit:shouldReverse:
+ _objc_msgSend$_chargerPluggedInPublisherWithStartDate:endDate:
+ _objc_msgSend$_createAppInFocusSessionFromEvent:startTime:endTime:
+ _objc_msgSend$_deviceScreenLockedPublisherWithStartDate:endDate:limit:shouldReverse:
+ _objc_msgSend$_displayBacklightPublisherWithStartDate:endDate:
+ _objc_msgSend$_documentInteractionPublisherWithStartDate:endDate:limit:
+ _objc_msgSend$_enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:
+ _objc_msgSend$_enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:
+ _objc_msgSend$_enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:
+ _objc_msgSend$_enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:
+ _objc_msgSend$_enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:
+ _objc_msgSend$_fetchBMDeviceFromIDSIdentifier:
+ _objc_msgSend$_getAppLaunchEventFromBMAppInFocus:
+ _objc_msgSend$_launchReasonFromString:
+ _objc_msgSend$_pas_filteredArrayWithTest:
+ _objc_msgSend$_publisherWithStartDate:endDate:limit:shouldReverse:
+ _objc_msgSend$_publisherWithStartDate:endDate:shouldReverse:
+ _objc_msgSend$_saveData:toFileURL:outError:
+ _objc_msgSend$_setError
+ _objc_msgSend$_shouldPairStartEvent:withEndEvent:
+ _objc_msgSend$absoluteTimestamp
+ _objc_msgSend$adapterType
+ _objc_msgSend$address
+ _objc_msgSend$appBundleID
+ _objc_msgSend$appBundleIdKey
+ _objc_msgSend$appIdentity
+ _objc_msgSend$appSessionEndTime
+ _objc_msgSend$appSessionStartTime
+ _objc_msgSend$atxAudioRouteTypeFromBMAudioRouteType:
+ _objc_msgSend$atxPlaybackStateFromBMPlaybackState:
+ _objc_msgSend$atx_errorWithCode:userInfo:
+ _objc_msgSend$backlightLevel
+ _objc_msgSend$bookmarkData
+ _objc_msgSend$bundleID
+ _objc_msgSend$bundleURL
+ _objc_msgSend$clipBundleID
+ _objc_msgSend$connected
+ _objc_msgSend$currentAppInFocusStartEventAtGivenTime:
+ _objc_msgSend$currentLocale
+ _objc_msgSend$data
+ _objc_msgSend$dateFormatFromTemplate:options:locale:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$deviceAddress
+ _objc_msgSend$deviceName
+ _objc_msgSend$deviceType
+ _objc_msgSend$deviceTypeFromBiomeBluetoothDeviceType:
+ _objc_msgSend$displayType
+ _objc_msgSend$duration
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$endDate
+ _objc_msgSend$endEvent
+ _objc_msgSend$endTime
+ _objc_msgSend$enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:bundleIDFilter:block:
+ _objc_msgSend$enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:bundleIDsFilter:block:
+ _objc_msgSend$enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:
+ _objc_msgSend$enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:bundleIDFilter:block:
+ _objc_msgSend$enumerateAppLaunchEventsFromStartDate:bundleIDFilter:block:
+ _objc_msgSend$enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:bundleIDFilter:block:
+ _objc_msgSend$enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:bundleIDsFilter:block:
+ _objc_msgSend$enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:
+ _objc_msgSend$enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:bundleIDFilter:block:
+ _objc_msgSend$enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$exchangeObjectAtIndex:withObjectAtIndex:
+ _objc_msgSend$extensionHostID
+ _objc_msgSend$fileIdentity
+ _objc_msgSend$firstObject
+ _objc_msgSend$fullURL
+ _objc_msgSend$getATXMediaNowPlayingEventFromBiomeEvent:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initWithBMAppDocumentInteraction:
+ _objc_msgSend$initWithBundleId:type:displayType:parentBundleID:extensionHostID:appSessionStartTime:appSessionEndTime:launchReason:
+ _objc_msgSend$initWithBundleId:type:displayType:parentBundleID:extensionHostID:starting:absoluteTimestamp:launchReason:
+ _objc_msgSend$initWithDisplayState:absoluteTimestamp:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithInteractionType:originalFileURL:bookmarkData:isRemote:
+ _objc_msgSend$initWithLaunchDate:urlHash:clipBundleID:parentAppBundleID:webAppBundleID:launchReason:fullURL:referrerURL:referrerBundleID:
+ _objc_msgSend$initWithOnInterval:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$initWithStartTime:endTime:bundleID:title:playbackState:
+ _objc_msgSend$initWithStartTime:endTime:connected:
+ _objc_msgSend$initWithStartTime:endTime:connected:adapterType:
+ _objc_msgSend$initWithStartTime:endTime:connected:deviceAddress:deviceName:deviceType:
+ _objc_msgSend$initWithStartTime:endTime:connected:identifier:portType:portName:routeChangeReason:type:
+ _objc_msgSend$initWithStartTime:endTime:isLocked:
+ _objc_msgSend$isEqualToATXAppClipUsageEvent:
+ _objc_msgSend$isEqualToATXAppInFocusEvent:
+ _objc_msgSend$isEqualToATXAppInFocusEventSession:
+ _objc_msgSend$isEqualToATXAudioRouteEvent:
+ _objc_msgSend$isEqualToATXBluetoothConnectedEvent:
+ _objc_msgSend$isEqualToATXCarPlayConnectedEvent:
+ _objc_msgSend$isEqualToATXChargerPluggedInEvent:
+ _objc_msgSend$isEqualToATXDeviceScreenLockStateEvent:
+ _objc_msgSend$isEqualToATXDisplayOnIntervalEvent:
+ _objc_msgSend$isEqualToATXDocumentInteractionEvent:
+ _objc_msgSend$isEqualToATXMediaNowPlayingEvent:
+ _objc_msgSend$isLocked
+ _objc_msgSend$isRemote
+ _objc_msgSend$itemURL
+ _objc_msgSend$itemURLBookmarkData
+ _objc_msgSend$keyPathForAppDataDictionary
+ _objc_msgSend$launchDate
+ _objc_msgSend$launchReason
+ _objc_msgSend$name
+ _objc_msgSend$now
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$onInterval
+ _objc_msgSend$originalFileURL
+ _objc_msgSend$parentAppBundleID
+ _objc_msgSend$parentBundleID
+ _objc_msgSend$playbackState
+ _objc_msgSend$portName
+ _objc_msgSend$portType
+ _objc_msgSend$position
+ _objc_msgSend$publisherForDevice:withUseCase:options:
+ _objc_msgSend$referrerBundleID
+ _objc_msgSend$referrerURL
+ _objc_msgSend$remoteDevicesWithError:
+ _objc_msgSend$remoteUser
+ _objc_msgSend$routeChangeReason
+ _objc_msgSend$sessionPublisherWithStreamPublisher:startingBlock:sessionKeyBlock:options:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setTestModeEnabled:
+ _objc_msgSend$startDate
+ _objc_msgSend$startEvent
+ _objc_msgSend$startTime
+ _objc_msgSend$starting
+ _objc_msgSend$state
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$testModeEnabled
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$title
+ _objc_msgSend$type
+ _objc_msgSend$urlHash
+ _objc_msgSend$userContext
+ _objc_msgSend$webAppBundleID
+ _objc_release_x28
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x6
+ _sharedInstance._pasOnceToken7
+ _sharedInstance.sharedInstance
+ _task_info
- -[ATXBMBookmark saveBookmarkWithError:].cold.2
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _sharedInstance._pasOnceToken6
CStrings:
+ "#16@0:8"
+ "%"
+ "%@ - attempting to save data with directoryURL: %@"
+ "%@ - attempting to save data with fileURL: %@"
+ "%@ - could not write data file with error: %@"
+ "%@ start: %@, end: %@, bundleID: %@, title: %@, playbackState: %ld"
+ "%@ – Attempting to save data without a path is forbidden."
+ "%@ – _saveDatatoFileURL called without data"
+ "%f seconds: (%@, %@)"
+ "%s: Getting the current app in focus at time: %@"
+ "%s: Last event from BMAppInFocus stream at time %@ is %@. Is a starting event: %d"
+ "%s: error fetching latest App.Clip.InFocus event from biome %@"
+ "%s: error fetching latest Audio.Route event from biome %@"
+ "%s: error fetching latest CarPlay.Connected event from biome %@"
+ "%s: error fetching latest Device.ScreenLocked event from biome %@"
+ "%s: error fetching latest Device.Wireless.Bluetooth event from biome %@"
+ "+[ATXCarPlayConnectedEvent new]"
+ "-[ATXAppClipUsageStream enumerateAppClipUsageEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke"
+ "-[ATXAppInFocusStream currentAppInFocusStartEventAtGivenTime:]"
+ "-[ATXAppInFocusStream currentAppInFocusStartEventAtGivenTime:]_block_invoke"
+ "-[ATXAudioRouteStream _enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke"
+ "-[ATXBluetoothConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke"
+ "-[ATXCarPlayConnectedStream _enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke"
+ "-[ATXDeviceScreenLockStateStream _enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:]_block_invoke"
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@\"NSDateInterval\""
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@24@0:8q16"
+ "@28@0:8B16@20"
+ "@32@0:8:16@24"
+ "@32@0:8q16@24"
+ "@32@0:8q16@?24"
+ "@36@0:8@16@24B32"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24Q32"
+ "@40@0:8i16@20@28B36"
+ "@40@0:8q16@24@32"
+ "@44@0:8@16@24B32@36"
+ "@44@0:8@16@24Q32B40"
+ "@56@0:8@16@24@32@40q48"
+ "@60@0:8@16@24B32@36@44q52"
+ "@64@0:8@16i24@28@36B44@48@56"
+ "@68@0:8@16i24@28@36@44@52@60"
+ "@68@0:8@16i24i28@32@40B48@52@60"
+ "@72@0:8@16@24B32@36@44@52@60i68"
+ "@72@0:8@16i24i28@32@40@48@56@64"
+ "@84@0:8@16@24@32@40@48i56@60@68@76"
+ "ATXAppClipUsageEvent"
+ "ATXAppClipUsageStream"
+ "ATXAppInFocusEvent"
+ "ATXAppInFocusEventSession"
+ "ATXAppInFocusStream"
+ "ATXAppInFocusStream.m"
+ "ATXAppInFocusStream: Biome couldn't fetch remote devices with error: %@"
+ "ATXAppInFocusStream: Can't read App.InFocus stream with error: %@"
+ "ATXAppInFocusStream: Got %lu remote oneness devices from BMSyncService, expected 1"
+ "ATXAudioRouteEvent"
+ "ATXAudioRouteStream"
+ "ATXBluetoothConnectedEvent"
+ "ATXBluetoothConnectedStream"
+ "ATXCarPlayConnectedEvent"
+ "ATXCarPlayConnectedEvent.m"
+ "ATXCarPlayConnectedStream"
+ "ATXChargerPluggedInEvent"
+ "ATXChargerPluggedInStream"
+ "ATXChargerPluggedInStream.m"
+ "ATXChargerPluggedInStream: Error querying device plugged in stream: %@"
+ "ATXDeviceScreenLockStateEvent"
+ "ATXDeviceScreenLockStateStream"
+ "ATXDisplayOnIntervalEvent"
+ "ATXDisplayOnIntervalStream"
+ "ATXDisplayOnIntervalStream.m"
+ "ATXDisplayOnIntervalStream: Error querying Backlight stream: %@"
+ "ATXDisplayOnIntervalStream: displayStateAtTime Error querying Backlight stream: %@"
+ "ATXDisplayStateEvent"
+ "ATXDocumentInteractionEvent"
+ "ATXDocumentInteractionStream"
+ "ATXDocumentInteractionStream.m"
+ "ATXDocumentInteractionStream: Error querying document interaction stream: %@"
+ "ATXErrorSupport"
+ "ATXGenericEventBase"
+ "ATXGenericEventStreamBase"
+ "ATXGlobalStateForTesting"
+ "ATXMediaNowPlayingEvent"
+ "ATXMediaNowPlayingStream"
+ "ATXMediaNowPlayingStream.m"
+ "ATXMediaNowPlayingStream: Can't read Media.NowPlaying stream with error: %@"
+ "ATXUtils"
+ "App"
+ "Attempting to save data without a path is forbidden."
+ "Audio"
+ "B16@?0@\"ATXAppInFocusEvent\"8"
+ "B16@?0@\"ATXAppInFocusEventSession\"8"
+ "B16@?0@\"ATXDocumentInteractionEvent\"8"
+ "B16@?0@\"BMDevice\"8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B32@0:8@16@24"
+ "B40@0:8@16@24^@32"
+ "BMAppInFocusDisplayType: %lu not handled in switch statement. Returning ATXAppInFocusDisplayTypeUnknown"
+ "BMAppInFocusType: %lu not handled in switch statement. Returning ATXAppInFocusEventTypeUnknown"
+ "Backlight"
+ "Bluetooth"
+ "CarPlay"
+ "Clip"
+ "Connected"
+ "Could not obtain current App in Focus from Biome: %@"
+ "CurrentMirroredPhoneIDSIdentifier"
+ "Device"
+ "Display"
+ "Document"
+ "Document Interaction - %lu not handled in switch statement."
+ "Document Interaction - Empty appIdentity or missing bundle identifier/path"
+ "Document Interaction - Missing bookmark data; ignoring"
+ "Document Interaction - No original file URL."
+ "Document Interaction - No original file path."
+ "DocumentSpotlight"
+ "EMMMd HH:mm ss ZZZZ"
+ "Encountered an unknown launch reason for BMLibrary.App.Clip.InFocus: %@"
+ "InFocus"
+ "LocationBased"
+ "Mail"
+ "Maps"
+ "Media"
+ "Messages"
+ "NFC"
+ "NSObject"
+ "No bundleId found for BMAppInFocus event : %@"
+ "No eventBody found for BMStoreEvent : %@"
+ "NowPlaying"
+ "Other"
+ "PluggedIn"
+ "Power"
+ "Q32@0:8@16@24"
+ "Q40@0:8@16@24@32"
+ "QR"
+ "Route"
+ "Safari"
+ "ScreenLocked"
+ "Setting test mode: %{BOOL}d"
+ "Should hold off on expensive task"
+ "Skipping event as deviceType not supported: %@"
+ "Skipping event: %@ %@"
+ "Skipping event: %@ because address %@ or name %@ is nil"
+ "Some random text"
+ "Start date must be earlier than the end date %@ %@."
+ "Start date must be earlier than the end date."
+ "T#,R"
+ "T@\"NSData\",R,C,N,V_bookmarkData"
+ "T@\"NSDate\",R,N,V_absoluteTimestamp"
+ "T@\"NSDate\",R,N,V_appSessionEndTime"
+ "T@\"NSDate\",R,N,V_appSessionStartTime"
+ "T@\"NSDate\",R,N,V_endTime"
+ "T@\"NSDate\",R,N,V_launchDate"
+ "T@\"NSDate\",R,N,V_startTime"
+ "T@\"NSDateInterval\",R,N,V_onInterval"
+ "T@\"NSNumber\",R,N,V_adapterType"
+ "T@\"NSNumber\",R,N,V_routeChangeReason"
+ "T@\"NSString\",&,N,V_clipboardContentForTesting"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,N,V_bundleID"
+ "T@\"NSString\",R,N,V_clipBundleID"
+ "T@\"NSString\",R,N,V_deviceAddress"
+ "T@\"NSString\",R,N,V_deviceName"
+ "T@\"NSString\",R,N,V_extensionHostID"
+ "T@\"NSString\",R,N,V_fullURL"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@\"NSString\",R,N,V_launchReason"
+ "T@\"NSString\",R,N,V_parentAppBundleID"
+ "T@\"NSString\",R,N,V_parentBundleID"
+ "T@\"NSString\",R,N,V_portName"
+ "T@\"NSString\",R,N,V_portType"
+ "T@\"NSString\",R,N,V_referrerBundleID"
+ "T@\"NSString\",R,N,V_referrerURL"
+ "T@\"NSString\",R,N,V_title"
+ "T@\"NSString\",R,N,V_urlHash"
+ "T@\"NSString\",R,N,V_webAppBundleID"
+ "T@\"NSURL\",R,C,N,V_originalFileURL"
+ "TB,N,V_testModeEnabled"
+ "TB,R,N,V_connected"
+ "TB,R,N,V_displayState"
+ "TB,R,N,V_isLocked"
+ "TB,R,N,V_isRemote"
+ "TB,R,N,V_starting"
+ "TQ,R"
+ "Ti,R,N,V_displayType"
+ "Ti,R,N,V_launchReason"
+ "Ti,R,N,V_type"
+ "Tq,R,N,V_deviceType"
+ "Tq,R,N,V_playbackState"
+ "URLHash"
+ "VisualIntelligenceSessionLog"
+ "Vv16@0:8"
+ "WatchAppSettings"
+ "Wireless"
+ "[MemoryLogging] Physical memory footprint: %lf MB, context: %@"
+ "^{_NSZone=}16@0:8"
+ "_absoluteTimestamp"
+ "_adapterType"
+ "_appLaunchPublisherWithStartDate:endDate:shouldReverse:"
+ "_appSessionEndTime"
+ "_appSessionStartTime"
+ "_atxAppInFocusDisplayTypeForBMAppInFocusDisplayType:"
+ "_atxAppInFocusEventTypeForBMAppInFocusType:"
+ "_bluetoothPublisherWithStartDate:endDate:limit:shouldReverse:"
+ "_bookmarkData"
+ "_bundleID"
+ "_carPlayPublisherWithStartDate:endDate:limit:shouldReverse:"
+ "_chargerPluggedInPublisherWithStartDate:endDate:"
+ "_clipBundleID"
+ "_clipboardContentForTesting"
+ "_connected"
+ "_createAppInFocusSessionFromEvent:startTime:endTime:"
+ "_deviceAddress"
+ "_deviceName"
+ "_deviceScreenLockedPublisherWithStartDate:endDate:limit:shouldReverse:"
+ "_deviceType"
+ "_displayBacklightPublisherWithStartDate:endDate:"
+ "_displayState"
+ "_displayType"
+ "_documentInteractionPublisherWithStartDate:endDate:limit:"
+ "_endTime"
+ "_enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:"
+ "_enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:type:displayType:bundleIDsFilter:block:"
+ "_enumerateAudioOutputEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:"
+ "_enumerateEventsConnected:startDate:endDate:filterBlock:limit:ascending:block:"
+ "_enumerateEventsForLockedState:startDate:endDate:filterBlock:limit:ascending:block:"
+ "_extensionHostID"
+ "_fetchBMDeviceFromIDSIdentifier:"
+ "_fullURL"
+ "_getAppLaunchEventFromBMAppInFocus:"
+ "_identifier"
+ "_isLocked"
+ "_isRemote"
+ "_launchDate"
+ "_launchReason"
+ "_launchReasonFromString:"
+ "_onInterval"
+ "_originalFileURL"
+ "_parentAppBundleID"
+ "_parentBundleID"
+ "_pas_filteredArrayWithTest:"
+ "_playbackState"
+ "_portName"
+ "_portType"
+ "_publisherWithStartDate:endDate:limit:shouldReverse:"
+ "_publisherWithStartDate:endDate:shouldReverse:"
+ "_referrerBundleID"
+ "_referrerURL"
+ "_remoteIDSIdentifier"
+ "_routeChangeReason"
+ "_saveData:toFileURL:outError:"
+ "_saveDatatoFileURL called without data"
+ "_setError"
+ "_shouldPairStartEvent:withEndEvent:"
+ "_startTime"
+ "_testModeEnabled"
+ "_type"
+ "_urlHash"
+ "_webAppBundleID"
+ "absoluteTimestamp"
+ "adapterType"
+ "address"
+ "appBundleID"
+ "appBundleIdKey"
+ "appIdentity"
+ "appSessionDuration"
+ "appSessionEndTime"
+ "appSessionStartTime"
+ "atxAudioRouteTypeFromBMAudioRouteType:"
+ "atxPlaybackStateFromBMPlaybackState:"
+ "atx_errorWithCode:"
+ "atx_errorWithCode:debugDescription:"
+ "atx_errorWithCode:debugDescription:underlyingError:"
+ "atx_errorWithCode:debugDescription:underlyingErrors:"
+ "atx_errorWithCode:userInfo:"
+ "atx_errorWithCode:userInfoProvider:"
+ "autorelease"
+ "backlightLevel"
+ "bookmarkData"
+ "bundleID"
+ "bundleURL"
+ "class"
+ "client_donations"
+ "clipBoardContentForTesting"
+ "clipBundleID"
+ "clipboardContentForTesting"
+ "com.apple.camera"
+ "com.apple.proactive.app-prediction"
+ "conformsToProtocol:"
+ "connected"
+ "controlCenterSuggestionsEnabled"
+ "currentAppInFocusStartEvent"
+ "currentAppInFocusStartEventAtGivenTime:"
+ "currentLocale"
+ "dateFormatFromTemplate:options:locale:"
+ "dateWithTimeIntervalSinceNow:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "debugDescription"
+ "decodeBoolForKey:"
+ "decodeInt32ForKey:"
+ "decodeObjectOfClass:forKey:"
+ "deviceAddress"
+ "deviceName"
+ "deviceType"
+ "deviceTypeFromBiomeBluetoothDeviceType:"
+ "displayState"
+ "displayStateAtTime:"
+ "displayType"
+ "documentPredictor"
+ "duration"
+ "earlierDate:"
+ "encodeBool:forKey:"
+ "encodeInt32:forKey:"
+ "endDate"
+ "endEvent"
+ "endTime"
+ "enumerateAllAppLaunchSessionsFromStartDate:bundleIDFilter:block:"
+ "enumerateAppClipUsageEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:bundleIDFilter:block:"
+ "enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:bundleIDsFilter:block:"
+ "enumerateAppLaunchEventsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:"
+ "enumerateAppLaunchEventsBetweenStartDate:endDate:shouldReverse:bundleIDFilter:block:"
+ "enumerateAppLaunchEventsFromStartDate:block:"
+ "enumerateAppLaunchEventsFromStartDate:bundleIDFilter:block:"
+ "enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:bundleIDFilter:block:"
+ "enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:bundleIDsFilter:block:"
+ "enumerateAppLaunchSessionsBetweenStartDate:endDate:limit:shouldReverse:type:displayType:bundleIDsFilter:block:"
+ "enumerateAppLaunchSessionsBetweenStartDate:endDate:shouldReverse:bundleIDFilter:block:"
+ "enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateDeviceScreenLockedStateEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateDeviceScreenUnLockedStateEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateDisconnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateDisplayOnIntervalsFromStartDate:endDate:block:"
+ "enumerateDisplayStateEventsFromStartDate:endDate:block:"
+ "enumerateDocumentInteractionEventsFromStartDate:endDate:filterBlock:limit:block:"
+ "enumerateEventsFromStartDate:endDate:filterBlock:ascending:block:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumeratePluggedInEventsFromStartDate:endDate:filterBlock:limit:block:"
+ "eventDuration"
+ "exchangeObjectAtIndex:withObjectAtIndex:"
+ "extensionHostID"
+ "fileIdentity"
+ "firstObject"
+ "fullURL"
+ "getATXMediaNowPlayingEventFromBiomeEvent:"
+ "getBytes:range:"
+ "getDocumentsOpenedInLastMonth"
+ "getFirstAppLaunchSessionBetweenStartDate:endDate:"
+ "getFirstAppLaunchStartEventBetweenStartDate:endDate:"
+ "getLastAppLaunchSessionBetweenStartDate:endDate:"
+ "getLastAppLaunchStartEventBetweenStartDate:endDate:"
+ "hasError"
+ "i16@0:8"
+ "i20@0:8i16"
+ "i24@0:8@16"
+ "idsDeviceIdentifier"
+ "inference"
+ "initFileURLWithPath:"
+ "initWithBMAppDocumentInteraction:"
+ "initWithBundleId:type:displayType:parentBundleID:extensionHostID:appSessionStartTime:appSessionEndTime:launchReason:"
+ "initWithBundleId:type:displayType:parentBundleID:extensionHostID:starting:absoluteTimestamp:launchReason:"
+ "initWithBundleId:type:parentBundleID:extensionHostID:appSessionStartTime:appSessionEndTime:launchReason:"
+ "initWithBundleId:type:parentBundleID:extensionHostID:starting:absoluteTimestamp:launchReason:"
+ "initWithDisplayState:absoluteTimestamp:"
+ "initWithDomain:code:userInfo:"
+ "initWithInteractionType:originalFileURL:bookmarkData:isRemote:"
+ "initWithLaunchDate:urlHash:clipBundleID:parentAppBundleID:webAppBundleID:launchReason:fullURL:referrerURL:referrerBundleID:"
+ "initWithOnInterval:"
+ "initWithRemoteIDSIdentifier:"
+ "initWithStartDate:endDate:"
+ "initWithStartTime:endTime:bundleID:title:playbackState:"
+ "initWithStartTime:endTime:connected:"
+ "initWithStartTime:endTime:connected:adapterType:"
+ "initWithStartTime:endTime:connected:deviceAddress:deviceName:deviceType:"
+ "initWithStartTime:endTime:connected:identifier:portType:portName:routeChangeReason:type:"
+ "initWithStartTime:endTime:isLocked:"
+ "isEqualToATXAppClipUsageEvent:"
+ "isEqualToATXAppInFocusEvent:"
+ "isEqualToATXAppInFocusEventSession:"
+ "isEqualToATXAudioRouteEvent:"
+ "isEqualToATXBluetoothConnectedEvent:"
+ "isEqualToATXCarPlayConnectedEvent:"
+ "isEqualToATXChargerPluggedInEvent:"
+ "isEqualToATXDeviceScreenLockStateEvent:"
+ "isEqualToATXDisplayOnIntervalEvent:"
+ "isEqualToATXDocumentInteractionEvent:"
+ "isEqualToATXMediaNowPlayingEvent:"
+ "isKindOfClass:"
+ "isLocked"
+ "isProxy"
+ "isRemote"
+ "isSpotlightPlusEnabled"
+ "isSpotlightPlusInternalToolKitInvocationsEnabled"
+ "isSpotlightPlusModelDevelopmentEnabled"
+ "isTestModeEnabled"
+ "itemURL"
+ "itemURLBookmarkData"
+ "keyPathForAppDataDictionary"
+ "launchDate"
+ "launchReason"
+ "logCurrentMemoryFootprint:"
+ "menuItems"
+ "name"
+ "new"
+ "new called: %s"
+ "now"
+ "numberOfAppLaunchEventsBetweenStartDate:endDate:"
+ "numberOfAppLaunchSessionsBetweenStartDate:endDate:forBundleID:"
+ "numberWithInt:"
+ "numberWithLongLong:"
+ "onInterval"
+ "originalFileURL"
+ "parentAppBundleID"
+ "parentBundleID"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "playbackState"
+ "portName"
+ "portType"
+ "position"
+ "prettyRepresentation"
+ "proc_pid_rusage returned error: %s, context: %@"
+ "publisherForDevice:withUseCase:options:"
+ "q"
+ "q20@0:8i16"
+ "referrerBundleID"
+ "referrerURL"
+ "release"
+ "remote:"
+ "remoteDevicesWithError:"
+ "remoteUser"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "routeChangeReason"
+ "screenEntities"
+ "self"
+ "sessionPublisherWithStreamPublisher:startingBlock:sessionKeyBlock:options:"
+ "setClipBoardContentForTesting:"
+ "setClipboardContentForTesting:"
+ "setDateFormat:"
+ "setPosition:"
+ "setTestMode:"
+ "setTestModeEnabled:"
+ "shouldSkipExpensiveTask"
+ "shuffle:"
+ "startDate"
+ "startEvent"
+ "startTime"
+ "state"
+ "stringByAppendingString:"
+ "stringFromDate:"
+ "superclass"
+ "testModeEnabled"
+ "timeIntervalSinceDate:"
+ "timeIntervalSinceReferenceDate"
+ "title"
+ "type"
+ "urlHash"
+ "userContext"
+ "v16@?0@\"ATXDocumentInteractionEvent\"8"
+ "v16@?0@\"BMPairedEventSession\"8"
+ "v32@?0@\"NSURL\"8@\"NSData\"16^B24"
+ "v52@0:8@16@24@?32B40@?44"
+ "v52@0:8@16@24B32@36@?44"
+ "v56@0:8@16@24@?32Q40@?48"
+ "v60@0:8@16@24@?32Q40B48@?52"
+ "v60@0:8@16@24B32i36i40@44@?52"
+ "v60@0:8@16@24Q32B40@44@?52"
+ "v64@0:8B16@20@28@?36Q44B52@?56"
+ "v68@0:8@16@24Q32B40i44i48@52@?60"
+ "visualIntelligenceSessionLogFilePath"
+ "webAppBundleID"
+ "widgetSuggestionsEnabled"
+ "zone"
- "%@ - attempting to save bookmark with directoryURL: %@"
- "%@ - attempting to save bookmark with fileURL: %@"
- "%@ - could not write bookmark file with error: %@"

```
