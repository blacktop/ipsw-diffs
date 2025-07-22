## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-490.2.0.0.0
-  __TEXT.__text: 0xa49dc
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x7bcc
+492.1.0.0.0
+  __TEXT.__text: 0xa6054
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_methlist: 0x7c74
   __TEXT.__const: 0x3da
-  __TEXT.__gcc_except_tab: 0x3084
-  __TEXT.__cstring: 0xe25b
-  __TEXT.__oslogstring: 0x3544
+  __TEXT.__gcc_except_tab: 0x3178
+  __TEXT.__cstring: 0xe4ab
+  __TEXT.__oslogstring: 0x35fd
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2540
+  __TEXT.__unwind_info: 0x2590
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x83f
-  __TEXT.__objc_methname: 0x13c86
+  __TEXT.__objc_classname: 0x840
+  __TEXT.__objc_methname: 0x13ee6
   __TEXT.__objc_methtype: 0x2183
-  __TEXT.__objc_stubs: 0xeb00
+  __TEXT.__objc_stubs: 0xebe0
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x33c0
+  __DATA_CONST.__const: 0x33f0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4880
+  __DATA_CONST.__objc_selrefs: 0x48e0
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
-  __AUTH_CONST.__auth_got: 0x890
-  __AUTH_CONST.__const: 0xd58
-  __AUTH_CONST.__cfstring: 0x8d00
-  __AUTH_CONST.__objc_const: 0xa3b8
-  __AUTH_CONST.__objc_intobj: 0xa98
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__const: 0xd98
+  __AUTH_CONST.__cfstring: 0x8da0
+  __AUTH_CONST.__objc_const: 0xa4c8
+  __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_doubleobj: 0xed0
   __AUTH.__objc_data: 0xfa8
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x8cc
+  __DATA.__objc_ivar: 0x8e4
   __DATA.__data: 0xc20
   __DATA.__bss: 0x3e8
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2C01250-AC3A-3F5F-8228-5DB80811C6E1
-  Functions: 3480
-  Symbols:   11244
-  CStrings:  6765
+  UUID: 1D453466-031C-3D3F-8174-EBC3088605EA
+  Functions: 3507
+  Symbols:   11320
+  CStrings:  6802
 
Symbols:
+ -[HUAccessoryManager resetAADeviceManager]
+ -[HUAccessoryManager setupAADeviceManager]
+ -[HUHeadphoneLevelController _startReceivingADAMAudioSample:]
+ -[HUNearbyController _sanitizedDictionaryForLoggingWithMessage:]
+ -[HUNearbyHearingAidController clientRemoved:]
+ -[HUNearbyHearingAidController processesHighMessagePriority]
+ -[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]
+ -[HUNearbyHearingAidController sendMessagesPriorityHighForClient:]
+ -[HUNearbyHearingAidController setProcessesHighMessagePriority:]
+ -[HUNearbyLiveListenControllerWatch _sendStartObservingMessageToDevices:]
+ -[HUNearbyLiveListenControllerWatch isObservingNearbyStatus]
+ -[HUNearbyLiveListenControllerWatch setIsObservingNearbyStatus:]
+ -[HUNearbyLiveListenControllerWatch setShouldBeObservingNearbyStatus:]
+ -[HUNearbyLiveListenControllerWatch shouldBeObservingNearbyStatus]
+ -[HUNearbyLiveListenControlleriOS _sendStartObservingMessageToDevices:]
+ -[HUNearbyLiveListenControlleriOS isObservingNearbyStatus]
+ -[HUNearbyLiveListenControlleriOS setIsObservingNearbyStatus:]
+ -[HUNearbyLiveListenControlleriOS setShouldBeObservingNearbyStatus:]
+ -[HUNearbyLiveListenControlleriOS shouldBeObservingNearbyStatus]
+ -[HUNoiseController contextualVolumeBuffer]
+ -[HUNoiseController setContextualVolumeBuffer:]
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table158
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table170
+ GCC_except_table29
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table83
+ _AXLogTemp
+ _HUHearingRoutesChangedNotification
+ _OBJC_IVAR_$_HUAccessoryManager._audioAccessoryDaemonStartedToken
+ _OBJC_IVAR_$_HUNearbyHearingAidController._processesHighMessagePriority
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._isObservingNearbyStatus
+ _OBJC_IVAR_$_HUNearbyLiveListenControllerWatch._shouldBeObservingNearbyStatus
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._isObservingNearbyStatus
+ _OBJC_IVAR_$_HUNearbyLiveListenControlleriOS._shouldBeObservingNearbyStatus
+ _OBJC_IVAR_$_HUNoiseController._contextualVolumeBuffer
+ ___103-[HUNearbyLiveListenControlleriOS _isListeningChanged:audioLevel:isPlayingBack:orTranscriptionChanged:]_block_invoke_2
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.533
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.546
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.554
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.563
+ ___25-[HUNoiseController init]_block_invoke.322
+ ___26-[HUAccessoryManager init]_block_invoke_2
+ ___37-[HUNearbyHearingAidController start]_block_invoke.102
+ ___37-[HUNearbyHearingAidController start]_block_invoke.116
+ ___37-[HUNearbyHearingAidController start]_block_invoke.121
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.117
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.122
+ ___37-[HUNearbyHearingAidController start]_block_invoke_3.124
+ ___37-[HUNearbyHearingAidController start]_block_invoke_4.125
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.411
+ ___41-[AXHeardController handleNewConnection:]_block_invoke.288
+ ___41-[AXHeardController handleNewConnection:]_block_invoke_2.289
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_2
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_2.cold.1
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_3
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_4
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_5
+ ___42-[HUAccessoryManager setupAADeviceManager]_block_invoke_6
+ ___46-[HUNearbyHearingAidController clientRemoved:]_block_invoke
+ ___49-[HUNearbyLiveListenControlleriOS _nearbyDevices]_block_invoke.68
+ ___49-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke.46
+ ___51-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke.16
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.636
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.437
+ ___56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.90
+ ___57-[HUNearbyHearingAidController requestConnectionForMedia]_block_invoke.44
+ ___58-[HUNearbyLiveListenControllerWatch _nearbyDevicesChanged]_block_invoke_3
+ ___61-[HUNearbyLiveListenControlleriOS stopObservingRemoteSession]_block_invoke
+ ___62-[HUNearbyLiveListenControlleriOS startObservingRemoteSession]_block_invoke
+ ___62-[HUNoiseController registerForEnvironmentalDosimetryUpdates:]_block_invoke
+ ___63-[HUAccessoryManager getPairedDeviceSupportsHearingProtection:]_block_invoke.74
+ ___63-[HUNearbyLiveListenControllerWatch stopObservingRemoteSession]_block_invoke
+ ___64-[HUNearbyLiveListenControllerWatch startObservingRemoteSession]_block_invoke
+ ___66-[HUNearbyHearingAidController sendMessagesPriorityHighForClient:]_block_invoke
+ ___66-[HUNearbyHearingAidController sendMessagesPriorityHighForClient:]_block_invoke.cold.1
+ ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke.88
+ ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.220
+ ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke
+ ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke.174
+ ___69-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke.174.cold.1
+ ___76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.54
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.477
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.497
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.25
+ ___block_literal_global.294
+ ___block_literal_global.304
+ ___block_literal_global.311
+ ___block_literal_global.401
+ ___block_literal_global.548
+ ___block_literal_global.556
+ ___block_literal_global.565
+ ___block_literal_global.59
+ ___block_literal_global.593
+ ___block_literal_global.603
+ ___block_literal_global.682
+ ___block_literal_global.85
+ ___block_literal_global.90
+ ___block_literal_global.92
+ _objc_msgSend$_sanitizedDictionaryForLoggingWithMessage:
+ _objc_msgSend$_sendStartObservingMessageToDevices:
+ _objc_msgSend$_startReceivingADAMAudioSample:
+ _objc_msgSend$contextualVolumeBuffer
+ _objc_msgSend$isObservingNearbyStatus
+ _objc_msgSend$processesHighMessagePriority
+ _objc_msgSend$resetAADeviceManager
+ _objc_msgSend$sendMessagesPriorityDefaultForClient:
+ _objc_msgSend$sendMessagesPriorityHighForClient:
+ _objc_msgSend$setIsObservingNearbyStatus:
+ _objc_msgSend$setShouldBeObservingNearbyStatus:
+ _objc_msgSend$setupAADeviceManager
+ _objc_msgSend$shouldBeObservingNearbyStatus
- -[HUHeadphoneLevelController _startRecevingADAMAudioSample:]
- -[HUNearbyHearingAidController sendMessagesPriorityDefault]
- -[HUNearbyHearingAidController sendMessagesPriorityHigh]
- -[HUNearbyLiveListenControllerWatch _sendStartObservingMessage]
- -[HUNearbyLiveListenControllerWatch startObserving].cold.1
- -[HUNearbyLiveListenControllerWatch stopObserving].cold.1
- -[HUNearbyLiveListenControlleriOS _sendMessageToRequestInitialState]
- -[HUNearbyLiveListenControlleriOS _sendStartObservingMessage]
- -[HUNoiseController latestNoiseSampleWasBuffered]
- -[HUNoiseController setLatestNoiseSampleWasBuffered:]
- GCC_except_table110
- GCC_except_table114
- GCC_except_table116
- GCC_except_table117
- GCC_except_table121
- GCC_except_table135
- GCC_except_table140
- GCC_except_table146
- GCC_except_table155
- GCC_except_table159
- GCC_except_table165
- GCC_except_table167
- GCC_except_table56
- GCC_except_table64
- GCC_except_table68
- _OBJC_IVAR_$_HUNoiseController._latestNoiseSampleWasBuffered
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.536
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.549
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.557
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.566
- ___25-[HUNoiseController init]_block_invoke.325
- ___37-[HUNearbyHearingAidController start]_block_invoke.101
- ___37-[HUNearbyHearingAidController start]_block_invoke.115
- ___37-[HUNearbyHearingAidController start]_block_invoke.120
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.116
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.121
- ___37-[HUNearbyHearingAidController start]_block_invoke_3.123
- ___37-[HUNearbyHearingAidController start]_block_invoke_4.124
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.414
- ___41-[AXHeardController handleNewConnection:]_block_invoke.287
- ___41-[AXHeardController handleNewConnection:]_block_invoke_2.288
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_11
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_12
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_12.cold.1
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_13
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_14
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_15
- ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_16
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.639
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.440
- ___56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.89
- ___56-[HUNearbyHearingAidController sendMessagesPriorityHigh]_block_invoke
- ___57-[HUNearbyHearingAidController requestConnectionForMedia]_block_invoke.43
- ___59-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke
- ___59-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke.173
- ___63-[HUAccessoryManager getPairedDeviceSupportsHearingProtection:]_block_invoke.72
- ___68-[HUNearbyLiveListenControlleriOS _handleRemoteControlSettingChange]_block_invoke.80
- ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.219
- ___76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.53
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.480
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.500
- ___block_literal_global.297
- ___block_literal_global.303
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.404
- ___block_literal_global.551
- ___block_literal_global.559
- ___block_literal_global.568
- ___block_literal_global.596
- ___block_literal_global.606
- ___block_literal_global.685
- ___block_literal_global.75
- ___block_literal_global.77
- ___block_literal_global.82
- ___block_literal_global.91
- _objc_msgSend$_sendStartObservingMessage
- _objc_msgSend$_startRecevingADAMAudioSample:
- _objc_msgSend$latestNoiseSampleWasBuffered
- _objc_msgSend$sendMessagesPriorityDefault
- _objc_msgSend$sendMessagesPriorityHigh
- _objc_msgSend$setLatestNoiseSampleWasBuffered:
CStrings:
+ "-[HUNearbyHearingAidController sendMessagesPriorityDefaultForClient:]_block_invoke"
+ "-[HUNearbyHearingAidController sendMessagesPriorityHighForClient:]_block_invoke"
+ "-[HUNearbyLiveListenControllerWatch _handleStateChangedMessage:]"
+ "-[HUNearbyLiveListenControllerWatch _sendStartObservingMessageToDevices:]"
+ "-[HUNearbyLiveListenControllerWatch startObserving]"
+ "-[HUNearbyLiveListenControllerWatch startObserving]_block_invoke"
+ "-[HUNearbyLiveListenControllerWatch stopObserving]"
+ "-[HUNearbyLiveListenControlleriOS _sendStartObservingMessageToDevices:]"
+ "-[HUNearbyLiveListenControlleriOS startObserving]_block_invoke"
+ "Added High priority client: %d, set: %@"
+ "Already not listening, no need to send empty state to unauthorized device %@"
+ "Checking High priority clients: %@"
+ "IDS Sending(%@) %@ to %@ with %@, priority: %@"
+ "Invalid high priority client: %d, %@"
+ "Multi-device settings change. Updated available controllers"
+ "Not listening, no need to send status"
+ "Removed High priority client: %d, clients: %@"
+ "Resetting aa device manager"
+ "Shouldn't be observing nearby status but got state changed message, broadcasting stop observing"
+ "T@\"NSMutableArray\",&,N,V_contextualVolumeBuffer"
+ "T@\"NSMutableSet\",&,N,V_processesHighMessagePriority"
+ "TB,N,V_isObservingNearbyStatus"
+ "TB,N,V_shouldBeObservingNearbyStatus"
+ "XPC error, client removed: %d, clients: %@"
+ "XPC received MessagesPriority isHigh: %d for client: %d"
+ "_audioAccessoryDaemonStartedToken"
+ "_contextualVolumeBuffer"
+ "_isObservingNearbyStatus"
+ "_processesHighMessagePriority"
+ "_sanitizedDictionaryForLoggingWithMessage:"
+ "_sendStartObservingMessageToDevices:"
+ "_shouldBeObservingNearbyStatus"
+ "_startReceivingADAMAudioSample:"
+ "com.apple.AudioAccessory.daemonStarted"
+ "com.apple.accessibility.hearing.routes.changed"
+ "contextualVolumeBuffer"
+ "isObservingNearbyStatus"
+ "multiDeviceSettingsEnabled"
+ "processesHighMessagePriority"
+ "resetAADeviceManager"
+ "sendMessagesPriorityDefaultForClient:"
+ "sendMessagesPriorityHighForClient:"
+ "setContextualVolumeBuffer:"
+ "setIsObservingNearbyStatus:"
+ "setProcessesHighMessagePriority:"
+ "setShouldBeObservingNearbyStatus:"
+ "setupAADeviceManager"
+ "shouldBeObservingNearbyStatus"
- "-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke"
- "-[HUNearbyHearingAidController sendMessagesPriorityHigh]_block_invoke"
- "-[HUNearbyLiveListenControllerWatch _sendStartObservingMessage]"
- "-[HUNearbyLiveListenControlleriOS _sendMessageToRequestInitialState]"
- "-[HUNearbyLiveListenControlleriOS _sendStartObservingMessage]"
- "IDS Sending(%@) %@ to %{sensitive}@ with %@, priority: %@"
- "Multidevice settings change. Updated available controllers"
- "TB,N,V_latestNoiseSampleWasBuffered"
- "XPC received MessagesPriority isHigh: %d"
- "_latestNoiseSampleWasBuffered"
- "_sendStartObservingMessage"
- "_startRecevingADAMAudioSample:"
- "latestNoiseSampleWasBuffered"
- "setLatestNoiseSampleWasBuffered:"

```
