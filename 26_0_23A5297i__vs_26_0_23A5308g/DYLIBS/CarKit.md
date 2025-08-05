## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-743.0.0.0.0
-  __TEXT.__text: 0x547dc
+745.1.2.0.0
+  __TEXT.__text: 0x54d1c
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x5abc
+  __TEXT.__objc_methlist: 0x5ae4
   __TEXT.__const: 0x42a
-  __TEXT.__cstring: 0x52d1
-  __TEXT.__oslogstring: 0x5ea0
-  __TEXT.__gcc_except_tab: 0xa44
+  __TEXT.__cstring: 0x52f1
+  __TEXT.__oslogstring: 0x5eb7
+  __TEXT.__gcc_except_tab: 0xa54
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__swift5_typeref: 0x3e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1800
+  __TEXT.__unwind_info: 0x17f8
   __TEXT.__objc_classname: 0xacc
-  __TEXT.__objc_methname: 0xfd85
+  __TEXT.__objc_methname: 0xffa1
   __TEXT.__objc_methtype: 0x2302
-  __TEXT.__objc_stubs: 0x9060
+  __TEXT.__objc_stubs: 0x9080
   __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x1e70
+  __DATA_CONST.__const: 0x1e90
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f8
+  __DATA_CONST.__objc_selrefs: 0x3310
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__const: 0x1740
+  __AUTH_CONST.__const: 0x1760
   __AUTH_CONST.__cfstring: 0x5620
-  __AUTH_CONST.__objc_const: 0xea38
+  __AUTH_CONST.__objc_const: 0xea48
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9B9905EF-AE9E-381C-A2E9-44B6A28C067F
-  Functions: 2623
-  Symbols:   8821
-  CStrings:  4832
+  UUID: 8AE53FC2-D525-3442-955F-3005E66D2C36
+  Functions: 2628
+  Symbols:   8834
+  CStrings:  4837
 
Symbols:
+ -[CARDisplayInfo hasVideoStreamWithIdentifier:]
+ -[CARDisplayInfo videoStreamIdentifiers]
+ -[CARDisplayInfo videoStreamWithIdentifier:]
+ -[CARSession _sessionUpdatesQueue_fetchFallbackIsNightWithToken:]
+ -[CARSession _sessionUpdatesQueue_fetchFallbackIsNightWithToken:].cold.1
+ -[CARSession _sessionUpdatesQueue_fetchFallbackIsNightWithToken:].cold.2
+ -[CARSession _sessionUpdatesQueue_handleAppearanceModeUpdateWithParameters:]
+ -[CARSession _sessionUpdatesQueue_handleAppearanceModeUpdateWithParameters:].cold.1
+ -[CARSession _sessionUpdatesQueue_handleAppearanceModeUpdateWithParameters:].cold.2
+ -[CARSession _sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:]
+ -[CARSession _sessionUpdatesQueue_handleEndpointDescriptionChanged]
+ -[CARSession _sessionUpdatesQueue_handleIsPlayingVideoFromApp:]
+ -[CARSession _sessionUpdatesQueue_handleMapAppearanceModeUpdateWithParameters:]
+ -[CARSession _sessionUpdatesQueue_handleMapAppearanceModeUpdateWithParameters:].cold.1
+ -[CARSession _sessionUpdatesQueue_handleNightModeChange]
+ -[CARSession _sessionUpdatesQueue_handleOpenURL:]
+ -[CARSession _sessionUpdatesQueue_handleShowUIWithParameters:]
+ -[CARSession _sessionUpdatesQueue_handleSiriRequestEvent:withPayload:]
+ -[CARSession _sessionUpdatesQueue_handleStopUIWithParameters:]
+ -[CARSession _sessionUpdatesQueue_handleViewAreaChangeWithPayload:]
+ -[CARSession _sessionUpdatesQueue_handleViewAreaChangeWithPayload:].cold.1
+ -[CARSession _sessionUpdatesQueue_handleViewAreaChangeWithPayload:].cold.2
+ -[CARSession _sessionUpdatesQueue_updateConfiguration]
+ -[CARSession _sessionUpdatesQueue_updateScreenInfo:currentViewAreaToViewArea:duration:transitionControlType:]
+ -[CARSessionStatus _sessionUpdatesQueue_handleConnectingTimeout]
+ -[CARSessionStatus _sessionUpdatesQueue_notifyCancelledConnectionAttemptOnTransport:]
+ -[CARSessionStatus _sessionUpdatesQueue_notifyDidConnectSession:]
+ -[CARSessionStatus _sessionUpdatesQueue_notifyDidDisconnectSession:]
+ -[CARSessionStatus _sessionUpdatesQueue_notifyDidUpdateSession:]
+ -[CARSessionStatus _sessionUpdatesQueue_notifyStartedConnectionAttemptOnTransport:]
+ -[CARSessionStatus _sessionUpdatesQueue_startConnectingTimer]
+ -[CARSessionStatus _sessionUpdatesQueue_stopConnectingTimer]
+ -[CARSessionStatus _sessionUpdatesQueue_updateSession]
+ ___40-[CARDisplayInfo videoStreamIdentifiers]_block_invoke
+ ___44-[CARDisplayInfo videoStreamWithIdentifier:]_block_invoke
+ ___54-[CARSession _sessionUpdatesQueue_updateConfiguration]_block_invoke
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.356
+ ___62-[CARSession _sessionUpdatesQueue_handleShowUIWithParameters:]_block_invoke
+ ___62-[CARSession _sessionUpdatesQueue_handleStopUIWithParameters:]_block_invoke
+ ___76-[CARSession _sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:]_block_invoke
+ ___76-[CARSession _sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:]_block_invoke_2
+ ___76-[CARSession _sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:]_block_invoke_3
+ ___76-[CARSession _sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:]_block_invoke_4
+ ___CARHandleSuggestUI_block_invoke.415
+ ___block_descriptor_32_e23_16?0"CARStreamInfo"8l
+ ___block_literal_global.414
+ ___block_literal_global.97
+ ___sessionUpdatesQueue_endpointNotificationCallback_block_invoke
+ _notificationsFromEndpoint
+ _objc_msgSend$_sessionUpdatesQueue_fetchFallbackIsNightWithToken:
+ _objc_msgSend$_sessionUpdatesQueue_handleAppearanceModeUpdateWithParameters:
+ _objc_msgSend$_sessionUpdatesQueue_handleConnectingTimeout
+ _objc_msgSend$_sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:
+ _objc_msgSend$_sessionUpdatesQueue_handleEndpointDescriptionChanged
+ _objc_msgSend$_sessionUpdatesQueue_handleIsPlayingVideoFromApp:
+ _objc_msgSend$_sessionUpdatesQueue_handleMapAppearanceModeUpdateWithParameters:
+ _objc_msgSend$_sessionUpdatesQueue_handleNightModeChange
+ _objc_msgSend$_sessionUpdatesQueue_handleOpenURL:
+ _objc_msgSend$_sessionUpdatesQueue_handleShowUIWithParameters:
+ _objc_msgSend$_sessionUpdatesQueue_handleSiriRequestEvent:withPayload:
+ _objc_msgSend$_sessionUpdatesQueue_handleStopUIWithParameters:
+ _objc_msgSend$_sessionUpdatesQueue_handleViewAreaChangeWithPayload:
+ _objc_msgSend$_sessionUpdatesQueue_notifyCancelledConnectionAttemptOnTransport:
+ _objc_msgSend$_sessionUpdatesQueue_notifyDidConnectSession:
+ _objc_msgSend$_sessionUpdatesQueue_notifyDidDisconnectSession:
+ _objc_msgSend$_sessionUpdatesQueue_notifyDidUpdateSession:
+ _objc_msgSend$_sessionUpdatesQueue_notifyStartedConnectionAttemptOnTransport:
+ _objc_msgSend$_sessionUpdatesQueue_startConnectingTimer
+ _objc_msgSend$_sessionUpdatesQueue_stopConnectingTimer
+ _objc_msgSend$_sessionUpdatesQueue_updateConfiguration
+ _objc_msgSend$_sessionUpdatesQueue_updateScreenInfo:currentViewAreaToViewArea:duration:transitionControlType:
+ _objc_msgSend$_sessionUpdatesQueue_updateSession
+ _objc_msgSend$videoStreamWithIdentifier:
+ _sessionUpdatesQueue_endpointNotificationCallback
+ _sessionUpdatesQueue_endpointNotificationCallback.cold.1
+ _sessionUpdatesQueue_endpointNotificationCallback.cold.2
+ _sessionUpdatesQueue_endpointNotificationCallback.cold.3
+ _sessionUpdatesQueue_endpointNotificationCallback.cold.4
+ _sessionUpdatesQueue_endpointNotificationCallback.cold.5
+ _sessionUpdatesQueue_endpointNotificationCallback.cold.6
+ _sessionUpdatesQueue_endpointNotificationCallback.createFigToAVFNotificationMappingOnce
+ _sessionUpdatesQueue_endpointNotificationCallback.figToCARSessionNotificationMapping
- -[CARSession _fetchFallbackIsNightWithToken:]
- -[CARSession _fetchFallbackIsNightWithToken:].cold.1
- -[CARSession _fetchFallbackIsNightWithToken:].cold.2
- -[CARSession _handleAppearanceModeUpdateWithParameters:]
- -[CARSession _handleAppearanceModeUpdateWithParameters:].cold.1
- -[CARSession _handleAppearanceModeUpdateWithParameters:].cold.2
- -[CARSession _handleDisplayPluginsUpdateWithParameters:]
- -[CARSession _handleEndpointDescriptionChanged]
- -[CARSession _handleIsPlayingVideoFromApp:]
- -[CARSession _handleMapAppearanceModeUpdateWithParameters:]
- -[CARSession _handleMapAppearanceModeUpdateWithParameters:].cold.1
- -[CARSession _handleNightModeChange]
- -[CARSession _handleOpenURL:]
- -[CARSession _handleShowUIWithParameters:]
- -[CARSession _handleSiriRequestEvent:withPayload:]
- -[CARSession _handleStopUIWithParameters:]
- -[CARSession _handleViewAreaChangeWithPayload:]
- -[CARSession _handleViewAreaChangeWithPayload:].cold.1
- -[CARSession _handleViewAreaChangeWithPayload:].cold.2
- -[CARSession _updateConfiguration]
- -[CARSession _updateScreenInfo:currentViewAreaToViewArea:duration:transitionControlType:]
- -[CARSessionStatus _handleConnectingTimeout]
- -[CARSessionStatus _notifyCancelledConnectionAttemptOnTransport:]
- -[CARSessionStatus _notifyDidConnectSession:]
- -[CARSessionStatus _notifyDidDisconnectSession:]
- -[CARSessionStatus _notifyDidUpdateSession:]
- -[CARSessionStatus _notifyStartedConnectionAttemptOnTransport:]
- -[CARSessionStatus _startConnectingTimer]
- -[CARSessionStatus _stopConnectingTimer]
- -[CARSessionStatus _updateSession]
- ___34-[CARSession _updateConfiguration]_block_invoke
- ___42-[CARSession _handleShowUIWithParameters:]_block_invoke
- ___42-[CARSession _handleStopUIWithParameters:]_block_invoke
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.355
- ___56-[CARSession _handleDisplayPluginsUpdateWithParameters:]_block_invoke
- ___56-[CARSession _handleDisplayPluginsUpdateWithParameters:]_block_invoke_2
- ___56-[CARSession _handleDisplayPluginsUpdateWithParameters:]_block_invoke_3
- ___56-[CARSession _handleDisplayPluginsUpdateWithParameters:]_block_invoke_4
- ___CARHandleSuggestUI_block_invoke.414
- ___figEndpointNotificationCallback_block_invoke
- _externalDeviceNotificationsFromEndpoint
- _figEndpointNotificationCallback
- _figEndpointNotificationCallback.cold.1
- _figEndpointNotificationCallback.cold.2
- _figEndpointNotificationCallback.cold.3
- _figEndpointNotificationCallback.cold.4
- _figEndpointNotificationCallback.cold.5
- _figEndpointNotificationCallback.cold.6
- _figEndpointNotificationCallback.createFigToAVFNotificationMappingOnce
- _figEndpointNotificationCallback.figToCARSessionNotificationMapping
- _objc_msgSend$_fetchFallbackIsNightWithToken:
- _objc_msgSend$_handleAppearanceModeUpdateWithParameters:
- _objc_msgSend$_handleConnectingTimeout
- _objc_msgSend$_handleDisplayPluginsUpdateWithParameters:
- _objc_msgSend$_handleEndpointDescriptionChanged
- _objc_msgSend$_handleIsPlayingVideoFromApp:
- _objc_msgSend$_handleMapAppearanceModeUpdateWithParameters:
- _objc_msgSend$_handleNightModeChange
- _objc_msgSend$_handleOpenURL:
- _objc_msgSend$_handleShowUIWithParameters:
- _objc_msgSend$_handleSiriRequestEvent:withPayload:
- _objc_msgSend$_handleStopUIWithParameters:
- _objc_msgSend$_handleViewAreaChangeWithPayload:
- _objc_msgSend$_notifyCancelledConnectionAttemptOnTransport:
- _objc_msgSend$_notifyDidConnectSession:
- _objc_msgSend$_notifyDidDisconnectSession:
- _objc_msgSend$_notifyDidUpdateSession:
- _objc_msgSend$_notifyStartedConnectionAttemptOnTransport:
- _objc_msgSend$_startConnectingTimer
- _objc_msgSend$_stopConnectingTimer
- _objc_msgSend$_updateConfiguration
- _objc_msgSend$_updateScreenInfo:currentViewAreaToViewArea:duration:transitionControlType:
- _objc_msgSend$_updateSession
CStrings:
+ "@16@?0@\"CARStreamInfo\"8"
+ "Physical size is zero or more than 500x500mm, applying default size Result(%{public}@) = PointSize(%{public}@)/CROptimalPointsPerMM(%{public}@)"
+ "_sessionUpdatesQueue_fetchFallbackIsNightWithToken:"
+ "_sessionUpdatesQueue_handleAppearanceModeUpdateWithParameters:"
+ "_sessionUpdatesQueue_handleConnectingTimeout"
+ "_sessionUpdatesQueue_handleDisplayPluginsUpdateWithParameters:"
+ "_sessionUpdatesQueue_handleEndpointDescriptionChanged"
+ "_sessionUpdatesQueue_handleIsPlayingVideoFromApp:"
+ "_sessionUpdatesQueue_handleMapAppearanceModeUpdateWithParameters:"
+ "_sessionUpdatesQueue_handleNightModeChange"
+ "_sessionUpdatesQueue_handleOpenURL:"
+ "_sessionUpdatesQueue_handleShowUIWithParameters:"
+ "_sessionUpdatesQueue_handleSiriRequestEvent:withPayload:"
+ "_sessionUpdatesQueue_handleStopUIWithParameters:"
+ "_sessionUpdatesQueue_handleViewAreaChangeWithPayload:"
+ "_sessionUpdatesQueue_notifyCancelledConnectionAttemptOnTransport:"
+ "_sessionUpdatesQueue_notifyDidConnectSession:"
+ "_sessionUpdatesQueue_notifyDidDisconnectSession:"
+ "_sessionUpdatesQueue_notifyDidUpdateSession:"
+ "_sessionUpdatesQueue_notifyStartedConnectionAttemptOnTransport:"
+ "_sessionUpdatesQueue_startConnectingTimer"
+ "_sessionUpdatesQueue_stopConnectingTimer"
+ "_sessionUpdatesQueue_updateConfiguration"
+ "_sessionUpdatesQueue_updateScreenInfo:currentViewAreaToViewArea:duration:transitionControlType:"
+ "_sessionUpdatesQueue_updateSession"
+ "hasVideoStreamWithIdentifier:"
+ "videoStreamIdentifiers"
+ "videoStreamWithIdentifier:"
- "Physical size is zero, applying default size Result(%{public}@) = PointSize(%{public}@)/CROptimalPointsPerMM(%{public}@)"
- "_fetchFallbackIsNightWithToken:"
- "_handleAppearanceModeUpdateWithParameters:"
- "_handleConnectingTimeout"
- "_handleDisplayPluginsUpdateWithParameters:"
- "_handleEndpointDescriptionChanged"
- "_handleIsPlayingVideoFromApp:"
- "_handleMapAppearanceModeUpdateWithParameters:"
- "_handleNightModeChange"
- "_handleOpenURL:"
- "_handleShowUIWithParameters:"
- "_handleSiriRequestEvent:withPayload:"
- "_handleStopUIWithParameters:"
- "_handleViewAreaChangeWithPayload:"
- "_notifyCancelledConnectionAttemptOnTransport:"
- "_notifyDidConnectSession:"
- "_notifyDidDisconnectSession:"
- "_notifyDidUpdateSession:"
- "_notifyStartedConnectionAttemptOnTransport:"
- "_startConnectingTimer"
- "_stopConnectingTimer"
- "_updateConfiguration"
- "_updateScreenInfo:currentViewAreaToViewArea:duration:transitionControlType:"
- "_updateSession"

```
