## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.50.5.0.0
-  __TEXT.__text: 0x461b4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x5a1c
-  __TEXT.__const: 0x230
-  __TEXT.__gcc_except_tab: 0xc04
-  __TEXT.__cstring: 0x3013
-  __TEXT.__oslogstring: 0x6afc
-  __TEXT.__unwind_info: 0x14e8
-  __TEXT.__objc_classname: 0x828
-  __TEXT.__objc_methname: 0xc880
-  __TEXT.__objc_methtype: 0x209c
-  __TEXT.__objc_stubs: 0x7f20
+548.50.7.0.0
+  __TEXT.__text: 0x49848
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x5d1c
+  __TEXT.__const: 0x2b0
+  __TEXT.__gcc_except_tab: 0xd68
+  __TEXT.__cstring: 0x332e
+  __TEXT.__oslogstring: 0x6b1e
+  __TEXT.__unwind_info: 0x1608
+  __TEXT.__objc_classname: 0x890
+  __TEXT.__objc_methname: 0xcc6d
+  __TEXT.__objc_methtype: 0x21c2
+  __TEXT.__objc_stubs: 0x8160
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0x1570
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e68
+  __DATA_CONST.__objc_selrefs: 0x2f08
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x3ee0
-  __AUTH_CONST.__objc_const: 0x88e8
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x4440
+  __AUTH_CONST.__objc_const: 0x8f38
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x5b4
-  __DATA.__data: 0x9d0
-  __DATA.__bss: 0xf8
+  __AUTH.__objc_data: 0x14f0
+  __DATA.__objc_ivar: 0x604
+  __DATA.__data: 0xa30
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D378BA4-BA9D-3433-A5AE-5C97740186BA
-  Functions: 1873
-  Symbols:   6412
-  CStrings:  4155
+  UUID: 10D69E08-0950-3AA6-92B9-AB9C5ECF5602
+  Functions: 1974
+  Symbols:   6763
+  CStrings:  4324
 
Symbols:
+ +[TVRCFeatures isTVRemoteInputEventsEnabled]
+ -[TVRCHIDSession .cxx_destruct]
+ -[TVRCHIDSession _commandForButtonEvent:]
+ -[TVRCHIDSession _stateForButtonEvent:]
+ -[TVRCHIDSession activateWithCompletion:]
+ -[TVRCHIDSession hidCommand:buttonState:completion:]
+ -[TVRCHIDSession init]
+ -[TVRCHIDSession invalidate]
+ -[TVRCHIDSession messenger]
+ -[TVRCHIDSession sendButtonEvent:completion:]
+ -[TVRCHIDSession setMessenger:]
+ -[TVRCHIDTouchEvent finger]
+ -[TVRCHIDTouchEvent initWithTVRCTouchEvent:]
+ -[TVRCHIDTouchEvent location]
+ -[TVRCHIDTouchEvent phase]
+ -[TVRCHIDTouchEvent setFinger:]
+ -[TVRCHIDTouchEvent setLocation:]
+ -[TVRCHIDTouchEvent setPhase:]
+ -[TVRCHIDTouchEvent setTimestampSeconds:]
+ -[TVRCHIDTouchEvent timestampSeconds]
+ -[TVRCHIDTouchSession .cxx_destruct]
+ -[TVRCHIDTouchSession _activateWithCompletion:]
+ -[TVRCHIDTouchSession _activateWithCompletion:].cold.1
+ -[TVRCHIDTouchSession _invalidateWithCompletion:]
+ -[TVRCHIDTouchSession activateWithCompletion:]
+ -[TVRCHIDTouchSession flags]
+ -[TVRCHIDTouchSession init]
+ -[TVRCHIDTouchSession invalidateWithCompletion:]
+ -[TVRCHIDTouchSession invalidate]
+ -[TVRCHIDTouchSession messenger]
+ -[TVRCHIDTouchSession screenSize]
+ -[TVRCHIDTouchSession sendTouchEvent:completion:]
+ -[TVRCHIDTouchSession sendTouchEvent:completion:].cold.1
+ -[TVRCHIDTouchSession setFlags:]
+ -[TVRCHIDTouchSession setMessenger:]
+ -[TVRCHIDTouchSession setScreenSize:]
+ -[TVRCInputSessionManager .cxx_destruct]
+ -[TVRCInputSessionManager activateWithCompletionHandler:]
+ -[TVRCInputSessionManager activateWithCompletionHandler:].cold.1
+ -[TVRCInputSessionManager activated]
+ -[TVRCInputSessionManager companionClient]
+ -[TVRCInputSessionManager hidSession]
+ -[TVRCInputSessionManager hidTouchSession]
+ -[TVRCInputSessionManager initWithCompanionLinkClient:]
+ -[TVRCInputSessionManager invalidateWithCompletion:]
+ -[TVRCInputSessionManager rtiSessionHandler]
+ -[TVRCInputSessionManager sendButtonEvent:completion:]
+ -[TVRCInputSessionManager sendTouchEvent:completion:]
+ -[TVRCInputSessionManager setActivated:]
+ -[TVRCInputSessionManager setCompanionClient:]
+ -[TVRCInputSessionManager setHidSession:]
+ -[TVRCInputSessionManager setHidTouchSession:]
+ -[TVRCInputSessionManager setRtiSessionHandler:]
+ -[TVRCInputSessionManager setTextInputSession:]
+ -[TVRCInputSessionManager textInputSession]
+ -[TVRCRPCompanionLinkClientWrapper _sendSessionStartWithCompletion:]
+ -[TVRCRPCompanionLinkClientWrapper _setupInputSessionManagerIfNeeded]
+ -[TVRCRPCompanionLinkClientWrapper _setupInputSessionManagerIfNeeded].cold.1
+ -[TVRCRPCompanionLinkClientWrapper inputSessionActivated]
+ -[TVRCRPCompanionLinkClientWrapper inputSessionManager]
+ -[TVRCRPCompanionLinkClientWrapper setInputSessionActivated:]
+ -[TVRCRPCompanionLinkClientWrapper setInputSessionManager:]
+ -[TVRCRapportRemoteTextInputKeyboardImpl rtiSessionProvider]
+ -[TVRCRapportRemoteTextInputKeyboardImpl setRtiSessionProvider:]
+ -[TVRCTextInputSession _activateWithCompletion:].cold.1
+ GCC_except_table101
+ GCC_except_table114
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table131
+ GCC_except_table136
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ _NSDictionaryGetNSNumber
+ _OBJC_CLASS_$_TVRCHIDSession
+ _OBJC_CLASS_$_TVRCHIDTouchEvent
+ _OBJC_CLASS_$_TVRCHIDTouchSession
+ _OBJC_CLASS_$_TVRCInputSessionManager
+ _OBJC_IVAR_$_TVRCHIDSession._dispatchQueue
+ _OBJC_IVAR_$_TVRCHIDSession._messenger
+ _OBJC_IVAR_$_TVRCHIDTouchEvent._finger
+ _OBJC_IVAR_$_TVRCHIDTouchEvent._location
+ _OBJC_IVAR_$_TVRCHIDTouchEvent._phase
+ _OBJC_IVAR_$_TVRCHIDTouchEvent._timestampSeconds
+ _OBJC_IVAR_$_TVRCHIDTouchSession._dispatchQueue
+ _OBJC_IVAR_$_TVRCHIDTouchSession._flags
+ _OBJC_IVAR_$_TVRCHIDTouchSession._messenger
+ _OBJC_IVAR_$_TVRCHIDTouchSession._screenSize
+ _OBJC_IVAR_$_TVRCHIDTouchSession._touchSessionID
+ _OBJC_IVAR_$_TVRCInputSessionManager._activated
+ _OBJC_IVAR_$_TVRCInputSessionManager._companionClient
+ _OBJC_IVAR_$_TVRCInputSessionManager._hidSession
+ _OBJC_IVAR_$_TVRCInputSessionManager._hidTouchSession
+ _OBJC_IVAR_$_TVRCInputSessionManager._rtiSessionHandler
+ _OBJC_IVAR_$_TVRCInputSessionManager._textInputSession
+ _OBJC_IVAR_$_TVRCRPCompanionLinkClientWrapper._inputSessionActivated
+ _OBJC_IVAR_$_TVRCRPCompanionLinkClientWrapper._inputSessionManager
+ _OBJC_IVAR_$_TVRCRapportRemoteTextInputKeyboardImpl._rtiSessionProvider
+ _OBJC_METACLASS_$_TVRCHIDSession
+ _OBJC_METACLASS_$_TVRCHIDTouchEvent
+ _OBJC_METACLASS_$_TVRCHIDTouchSession
+ _OBJC_METACLASS_$_TVRCInputSessionManager
+ _OUTLINED_FUNCTION_13
+ _TVRCEventIDHIDGameController
+ _TVRCEventIDHIDTouch
+ _TVRCEventIDTextInputChanged
+ _TVRCEventIDTextInputStarted
+ _TVRCEventIDTextInputStopped
+ _TVRCLuckierFAlignedVersion
+ _TVRCMessageGCButtonA
+ _TVRCMessageGCButtonB
+ _TVRCMessageGCButtonHome
+ _TVRCMessageGCButtonMenu
+ _TVRCMessageGCButtonOptions
+ _TVRCMessageGCButtonX
+ _TVRCMessageGCButtonY
+ _TVRCMessageGCDpadDown
+ _TVRCMessageGCDpadLeft
+ _TVRCMessageGCDpadRight
+ _TVRCMessageGCDpadUp
+ _TVRCMessageGCLeftThumbstickButton
+ _TVRCMessageGCLeftThumbstickX
+ _TVRCMessageGCLeftThumbstickY
+ _TVRCMessageGCRightThumbstickButton
+ _TVRCMessageGCRightThumbstickX
+ _TVRCMessageGCRightThumbstickY
+ _TVRCMessageGCShoulderButtonL1
+ _TVRCMessageGCShoulderButtonL2
+ _TVRCMessageGCShoulderButtonR1
+ _TVRCMessageGCShoulderButtonR2
+ _TVRCMessageKeyCoordinateX
+ _TVRCMessageKeyCoordinateY
+ _TVRCMessageKeyHIDButtonState
+ _TVRCMessageKeyHIDCommand
+ _TVRCMessageKeyHeight
+ _TVRCMessageKeyIdentifier
+ _TVRCMessageKeyNanoseconds
+ _TVRCMessageKeyTextInputData
+ _TVRCMessageKeyTextInputVersion
+ _TVRCMessageKeyTouchFinger
+ _TVRCMessageKeyTouchFlags
+ _TVRCMessageKeyTouchPhase
+ _TVRCMessageKeyWidth
+ _TVRCRequestIDHIDCommand
+ _TVRCRequestIDHIDGameControllerStart
+ _TVRCRequestIDHIDGameControllerStop
+ _TVRCRequestIDHIDTouchStart
+ _TVRCRequestIDHIDTouchStop
+ _TVRCRequestIDTextInputStart
+ _TVRCRequestIDTextInputStop
+ __OBJC_$_INSTANCE_METHODS_TVRCHIDSession
+ __OBJC_$_INSTANCE_METHODS_TVRCHIDTouchEvent
+ __OBJC_$_INSTANCE_METHODS_TVRCHIDTouchSession
+ __OBJC_$_INSTANCE_METHODS_TVRCInputSessionManager
+ __OBJC_$_INSTANCE_VARIABLES_TVRCHIDSession
+ __OBJC_$_INSTANCE_VARIABLES_TVRCHIDTouchEvent
+ __OBJC_$_INSTANCE_VARIABLES_TVRCHIDTouchSession
+ __OBJC_$_INSTANCE_VARIABLES_TVRCInputSessionManager
+ __OBJC_$_PROP_LIST_TVRCHIDSession
+ __OBJC_$_PROP_LIST_TVRCHIDTouchEvent
+ __OBJC_$_PROP_LIST_TVRCHIDTouchSession
+ __OBJC_$_PROP_LIST_TVRCInputSessionManager
+ __OBJC_$_PROP_LIST_TVRCRTISessionProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRCRTISessionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TVRCRTISessionProviding
+ __OBJC_CLASS_PROTOCOLS_$_TVRCInputSessionManager
+ __OBJC_CLASS_RO_$_TVRCHIDSession
+ __OBJC_CLASS_RO_$_TVRCHIDTouchEvent
+ __OBJC_CLASS_RO_$_TVRCHIDTouchSession
+ __OBJC_CLASS_RO_$_TVRCInputSessionManager
+ __OBJC_LABEL_PROTOCOL_$_TVRCRTISessionProviding
+ __OBJC_METACLASS_RO_$_TVRCHIDSession
+ __OBJC_METACLASS_RO_$_TVRCHIDTouchEvent
+ __OBJC_METACLASS_RO_$_TVRCHIDTouchSession
+ __OBJC_METACLASS_RO_$_TVRCInputSessionManager
+ __OBJC_PROTOCOL_$_TVRCRTISessionProviding
+ __TVRCHIDEventLog
+ __TVRCHIDEventLog.cold.1
+ __TVRCHIDEventLog.log
+ __TVRCHIDEventLog.onceToken
+ ___28-[TVRCHIDSession invalidate]_block_invoke
+ ___33-[TVRCHIDTouchSession invalidate]_block_invoke
+ ___41-[TVRCHIDSession activateWithCompletion:]_block_invoke
+ ___41-[TVRCHIDSession activateWithCompletion:]_block_invoke.cold.1
+ ___46-[TVRCHIDTouchSession activateWithCompletion:]_block_invoke
+ ___47-[TVRCHIDTouchSession _activateWithCompletion:]_block_invoke
+ ___47-[TVRCHIDTouchSession _activateWithCompletion:]_block_invoke.cold.1
+ ___47-[TVRCHIDTouchSession _activateWithCompletion:]_block_invoke.cold.2
+ ___48-[TVRCHIDTouchSession invalidateWithCompletion:]_block_invoke
+ ___48-[TVRCInputSessionManager setRtiSessionHandler:]_block_invoke
+ ___48-[TVRCTextInputSession _activateWithCompletion:]_block_invoke_4.cold.1
+ ___48-[TVRCTextInputSession handleTextActionPayload:]_block_invoke.14
+ ___49-[TVRCHIDTouchSession _invalidateWithCompletion:]_block_invoke
+ ___49-[TVRCHIDTouchSession _invalidateWithCompletion:]_block_invoke.cold.1
+ ___51-[TVRCRPCompanionLinkClientWrapper sendTouchEvent:]_block_invoke.20
+ ___51-[TVRCRPCompanionLinkClientWrapper sendTouchEvent:]_block_invoke.20.cold.1
+ ___51-[TVRCRPCompanionLinkClientWrapper sendTouchEvent:]_block_invoke.20.cold.2
+ ___52-[TVRCHIDSession hidCommand:buttonState:completion:]_block_invoke
+ ___52-[TVRCInputSessionManager invalidateWithCompletion:]_block_invoke
+ ___52-[TVRCInputSessionManager invalidateWithCompletion:]_block_invoke.cold.1
+ ___52-[TVRCRPCompanionLinkClientWrapper sendButtonEvent:]_block_invoke.18
+ ___52-[TVRCRPCompanionLinkClientWrapper sendButtonEvent:]_block_invoke.18.cold.1
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke.12
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke.12.cold.1
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke.17
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke.6
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke.6.cold.1
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke.cold.1
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke_2
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke_2.13
+ ___57-[TVRCInputSessionManager activateWithCompletionHandler:]_block_invoke_2.7
+ ___57-[TVRCRPCompanionLinkClientWrapper _updateConnectedState]_block_invoke
+ ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.164
+ ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.164.cold.1
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.129
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.129.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.157
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.157.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.158
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.158.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.159
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.159.cold.1
+ ___64-[TVRCRapportRemoteTextInputKeyboardImpl setRtiSessionProvider:]_block_invoke
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.131
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.131.cold.1
+ ___68-[TVRCRPCompanionLinkClientWrapper _sendSessionStartWithCompletion:]_block_invoke
+ ___68-[TVRCRPCompanionLinkClientWrapper _sendSessionStartWithCompletion:]_block_invoke.cold.1
+ ___69-[TVRCRPCompanionLinkClientWrapper _setupInputSessionManagerIfNeeded]_block_invoke
+ ___69-[TVRCRPCompanionLinkClientWrapper _setupInputSessionManagerIfNeeded]_block_invoke.cold.1
+ ___75-[TVRCRPCompanionLinkClientWrapper sendEvent:options:shouldRetry:response:]_block_invoke.21
+ ___75-[TVRCRPCompanionLinkClientWrapper sendEvent:options:shouldRetry:response:]_block_invoke.21.cold.1
+ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.113.cold.1
+ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.114.cold.1
+ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.115
+ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.115.cold.1
+ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.116
+ ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.117
+ ____TVRCHIDEventLog_block_invoke
+ ___block_descriptor_48_e8_32bs40w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e17_v16?0"NSError"8lw56l8s32l8s40l8s48l8
+ ___block_literal_global.133
+ ___block_literal_global.149
+ ___block_literal_global.17
+ _dispatch_group_notify
+ _objc_msgSend$_invalidateWithCompletion:
+ _objc_msgSend$_sendSessionStartWithCompletion:
+ _objc_msgSend$_setupInputSessionManagerIfNeeded
+ _objc_msgSend$hidCommand:buttonState:completion:
+ _objc_msgSend$initWithCompanionLinkClient:
+ _objc_msgSend$initWithTVRCTouchEvent:
+ _objc_msgSend$inputSessionActivated
+ _objc_msgSend$inputSessionManager
+ _objc_msgSend$isTVRemoteInputEventsEnabled
+ _objc_msgSend$location
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$rtiSessionHandler
+ _objc_msgSend$sendButtonEvent:completion:
+ _objc_msgSend$setInputSessionActivated:
+ _objc_msgSend$setInputSessionManager:
+ _objc_msgSend$setRtiSessionProvider:
+ _objc_msgSend$timestampSeconds
- -[TVRCRPCompanionLinkClientWrapper _sendSessionStart]
- GCC_except_table104
- GCC_except_table115
- GCC_except_table125
- GCC_except_table130
- GCC_except_table33
- GCC_except_table37
- GCC_except_table40
- GCC_except_table41
- GCC_except_table74
- GCC_except_table76
- GCC_except_table78
- GCC_except_table80
- GCC_except_table82
- GCC_except_table90
- GCC_except_table96
- ___48-[TVRCTextInputSession handleTextActionPayload:]_block_invoke.35
- ___53-[TVRCRPCompanionLinkClientWrapper _sendSessionStart]_block_invoke
- ___53-[TVRCRPCompanionLinkClientWrapper _sendSessionStart]_block_invoke.cold.1
- ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.159
- ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.159.cold.1
- ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.126
- ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.126.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.152
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.152.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.153
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.153.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.154
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.154.cold.1
- ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.128
- ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.128.cold.1
- ___75-[TVRCRPCompanionLinkClientWrapper sendEvent:options:shouldRetry:response:]_block_invoke.19
- ___75-[TVRCRPCompanionLinkClientWrapper sendEvent:options:shouldRetry:response:]_block_invoke.19.cold.1
- ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.111
- ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.111.cold.1
- ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.112
- ___77-[TVRCRPCompanionLinkClientWrapper _invalidateAndResetWithCompletionHandler:]_block_invoke.112.cold.1
- ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
- ___block_literal_global.130
- ___block_literal_global.144
- ___block_literal_global.38
- _objc_msgSend$_sendSessionStart
CStrings:
+ "### Activate failed: %{public}@"
+ "### Drop touch event with no messenger"
+ "### TouchStart failed: %{public}@"
+ "### TouchStop failed: %{public}@"
+ "%s %@ %@"
+ "%s - Disconnecting %@ %@"
+ "%s - device: %@, %@"
+ "%s, error=%@ %@"
+ "&"
+ ", "
+ "-[TVRCInputSessionManager setRtiSessionHandler:]"
+ "1.2"
+ "@\"<TVRCRTISessionProviding>\""
+ "@\"TVRCHIDSession\""
+ "@\"TVRCHIDTouchSession\""
+ "@\"TVRCInputSessionManager\""
+ "@\"TVRCTextInputSession\""
+ "@?<v@?@\"RTIInputSystemSourceSession\">16@0:8"
+ "Activate"
+ "Activate: screen %f x %f"
+ "Active InputSessionManager already exists"
+ "Attempting to send button event %@ to Rapport device - %@"
+ "AuthCompletionHandler called on companionLinkClient for device %@. Error - %@"
+ "CoordinateX"
+ "CoordinateY"
+ "Could not create InputSessionManager for companionLinkClient %@. Error - %@"
+ "Could not create companionLinkClient for device %@. Error - %@ %@"
+ "Could not create hidSession for companionLinkClient %@. Error - %@"
+ "Could not create hidTouchSession for companionLinkClient %@. Error - %@"
+ "Could not create textInputSession for companionLinkClient %@. Error - %@"
+ "Could not find paired remote for device: %@"
+ "Could not send SessionStart for companionLinkClient %@. Error - %@"
+ "Could not send SessionStop for companionLinkClient %@. Error - %@"
+ "De-registering event %@ %@"
+ "Device name changed: old: %@, new: %@"
+ "Device was connected. Attempting to reconnect to new device: %@"
+ "Error activating Siri session for Rapport companionLinkClient %@. Error - %@"
+ "Error launching URL %@. Error - %@"
+ "Error launching application %@. Error - %@"
+ "Error prewarming Siri session for Rapport companionLinkClient %@. Error - %@"
+ "Error sending HID event to companionLinkClient %@. Error - %@"
+ "Error sending Touch event to Rapport companionLinkClient %@. Error - %@"
+ "Failed sessions: %@"
+ "Failed to reestablish connection for %@: %@"
+ "Failed to reestablish connection with client: %@"
+ "GCButtonA"
+ "GCButtonB"
+ "GCButtonHome"
+ "GCButtonMenu"
+ "GCButtonOptions"
+ "GCButtonX"
+ "GCButtonY"
+ "GCDpadDown"
+ "GCDpadLeft"
+ "GCDpadRight"
+ "GCDpadUp"
+ "GCLeftThumbstickButton"
+ "GCLeftThumbstickX"
+ "GCLeftThumbstickY"
+ "GCRightThumbstickButton"
+ "GCRightThumbstickX"
+ "GCRightThumbstickY"
+ "GCShoulderButtonL1"
+ "GCShoulderButtonL2"
+ "GCShoulderButtonR1"
+ "GCShoulderButtonR2"
+ "HIDButtonState"
+ "HIDCommand"
+ "HIDEvent"
+ "HIDGameController"
+ "HIDGameControllerStart"
+ "HIDGameControllerStop"
+ "HIDTouch"
+ "HIDTouchStart"
+ "HIDTouchStop"
+ "Heartbeat timer fired for remote: %@"
+ "Height"
+ "I16@0:8"
+ "InputEvents"
+ "InputSessionManager invalidation failed %@"
+ "Invalidate"
+ "Invalidated all sessions. Invalidating CompanionLinkClient: %@"
+ "Invalidating InputSessionManager"
+ "Nanoseconds"
+ "No touch device ID"
+ "PromptForPasswordHandler called on companionLinkClient for device %@"
+ "Received an error from settingsConnection - %@"
+ "Received event response: %@, options %@"
+ "Received request response with ID %@, response %@, error %@"
+ "Registering event with ID %@ %@"
+ "Remote info dict: %@"
+ "Resolved Feature Flags: %@"
+ "Sent touch event to companionLinkClient %@"
+ "Session started for companionLinkClient %@ \n currentVersion: %@ peerVersion: %@ negotiatedVersion: %@"
+ "Session stopped for companionLinkClient %@."
+ "Setting up InputSessionManager with nil companionClient"
+ "Siri Enabled on device %@ : %d"
+ "Siri is %@. Calling delegate to update supported buttons"
+ "Skipping. Timer already exists for remote: %@"
+ "Starting heartbeat timer for remote: %@"
+ "Stopping heartbeat timer for remote: %@ tv: %@"
+ "Successfully created InputSessionManager for companionLinkClient %@."
+ "Successfully created hidSession for companionLinkClient %@."
+ "Successfully created hidTouchSession for companionLinkClient %@."
+ "Successfully created textInputSession for companionLinkClient %@."
+ "Successfully invalidated InputSessionManager"
+ "Successfully registered %@"
+ "Successfully set up companionLinkClient %@. Letting clients know we connected successfully"
+ "T@\"<TVRCRTISessionProviding>\",&,N,V_rtiSessionProvider"
+ "T@\"TVRCHIDSession\",&,N,V_hidSession"
+ "T@\"TVRCHIDTouchSession\",&,N,V_hidTouchSession"
+ "T@\"TVRCInputSessionManager\",&,N,V_inputSessionManager"
+ "T@\"TVRCTextInputSession\",&,N,V_textInputSession"
+ "T@?,C,N"
+ "TB,N,V_inputSessionActivated"
+ "TI,N,V_flags"
+ "TV is in %@ state. Ignoring Siri invocation"
+ "TVRCHIDSession"
+ "TVRCHIDTouchEvent"
+ "TVRCHIDTouchSession"
+ "TVRCInputSessionManager"
+ "TVRCInputSessionManager is already active"
+ "TVRCInputSessionManager.errorQueue"
+ "TVRCRTISessionProviding"
+ "Td,N,V_timestampSeconds"
+ "TextInputChanged"
+ "TextInputData"
+ "TextInputStart"
+ "TextInputStarted"
+ "TextInputStop"
+ "TextInputStopped"
+ "TextInputVersion"
+ "Ti,N,V_finger"
+ "Ti,N,V_phase"
+ "TouchFinger"
+ "TouchFlags"
+ "TouchPhase"
+ "TouchStarted: ID %@"
+ "TouchStopped"
+ "T{CGPoint=dd},N,V_location"
+ "T{CGSize=dd},N,V_screenSize"
+ "Unable to register %@. CompanionLinkClient is not active! %@"
+ "Updated connected remote info: %@"
+ "Updated now playing info: %@"
+ "Using legacy input sessions"
+ "Width"
+ "[%@] attention state updated to %@ from %@"
+ "_flags"
+ "_inputSessionActivated"
+ "_inputSessionManager"
+ "_invalidateWithCompletion:"
+ "_location"
+ "_rtiSessionProvider"
+ "_screenSize"
+ "_sendSessionStartWithCompletion:"
+ "_setupInputSessionManagerIfNeeded"
+ "_timestampSeconds"
+ "_touchSessionID"
+ "companionLinkClient authCompletionHandler, diconnecting with error=%@"
+ "getAssistantIsEnabledForDeviceWithSiriInfo, enabled=%{bool}d, error=%@"
+ "hidCommand:buttonState:completion:"
+ "initWithCompanionLinkClient:"
+ "initWithTVRCTouchEvent:"
+ "inputSessionActivated"
+ "inputSessionManager"
+ "isTVRemoteInputEventsEnabled"
+ "location"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLongLong:"
+ "numberWithUnsignedShort:"
+ "rtiSessionProvider"
+ "screenSize"
+ "sendButtonEvent:completion:"
+ "setInputSessionActivated:"
+ "setInputSessionManager:"
+ "setRtiSessionProvider:"
+ "setScreenSize:"
+ "timestampSeconds"
+ "v20@0:8I16"
+ "v24@0:8@?<v@?@\"RTIInputSystemSourceSession\">16"
+ "v32@0:8i16i20@?24"
+ "v32@0:8{CGPoint=dd}16"
+ "v32@0:8{CGSize=dd}16"
+ "\x81"
- "%"
- "%s %@ %{public}@"
- "%s - Disconnecting %{public}@ %@"
- "%s - device: %{public}@, %{public}@"
- "%s, error=%{public}@ %@"
- "Attempting to send button event %@ to Rapport device - %{public}@"
- "AuthCompletionHandler called on companionLinkClient for device %{public}@. Error - %{public}@"
- "Could not create companionLinkClient for device %{public}@. Error - %{public}@ %@"
- "Could not create hidSession for companionLinkClient %{public}@. Error - %{public}@"
- "Could not create hidTouchSession for companionLinkClient %{public}@. Error - %{public}@"
- "Could not create textInputSession for companionLinkClient %{public}@. Error - %{public}@"
- "Could not find paired remote for device: %{public}@"
- "Could not send SessionStart for companionLinkClient %{public}@. Error - %{public}@"
- "Could not send SessionStop for companionLinkClient %{public}@. Error - %{public}@"
- "De-registering event %{public}@ %@"
- "Device name changed: old: %{public}@, new: %{public}@"
- "Device was connected. Attempting to reconnect to new device: %{public}@"
- "Error activating Siri session for Rapport companionLinkClient %{public}@. Error - %{public}@"
- "Error launching URL %@. Error - %{public}@"
- "Error launching application %@. Error - %{public}@"
- "Error prewarming Siri session for Rapport companionLinkClient %{public}@. Error - %{public}@"
- "Error sending HID event to Rapport companionLinkClient %{public}@. Error - %{public}@"
- "Error sending Touch event to Rapport companionLinkClient %{public}@. Error - %{public}@"
- "Failed to reestablish connection for %{public}@: %{public}@"
- "Failed to reestablish connection with client: %{public}@"
- "Heartbeat timer fired for remote: %{public}@"
- "Invalidated all sessions. Invalidating CompanionLinkClient: %{public}@"
- "PromptForPasswordHandler called on companionLinkClient for device %{public}@"
- "Received an error from settingsConnection - %{public}@"
- "Received event response: %{public}@, options %{public}@"
- "Received request response with ID %{public}@, response %{public}@, error %{public}@"
- "Registering event with ID %{public}@ %@"
- "Remote info dict: %{public}@"
- "Resolved Feature Flags: %{public}@"
- "Sent touch event to companionLinkClient %{public}@"
- "Session started for companionLinkClient %{public}@ \n currentVersion: %{public}@ peerVersion: %{public}@ negotiatedVersion: %{public}@"
- "Session stopped for companionLinkClient %{public}@."
- "Siri Enabled on device %{public}@ : %d"
- "Siri is %{public}@. Calling delegate to update supported buttons"
- "Skipping. Timer already exists for remote: %{public}@"
- "Starting heartbeat timer for remote: %{public}@"
- "Stopping heartbeat timer for remote: %{public}@ tv: %{public}@"
- "Successfully created hidSession for companionLinkClient %{public}@."
- "Successfully created hidTouchSession for companionLinkClient %{public}@."
- "Successfully created textInputSession for companionLinkClient %{public}@."
- "Successfully registered %{public}@"
- "Successfully set up companionLinkClient %{public}@. Letting clients know we connected successfully"
- "TV is in %{public}@ state. Ignoring Siri invocation"
- "Unable to register %{public}@. CompanionLinkClient is not active! %@"
- "Updated connected remote info: %{public}@"
- "Updated now playing info: %{public}@"
- "[%{public}@] attention state updated to %{public}@ from %{public}@"
- "_sendSessionStart"
- "_tiC"
- "_tiD"
- "_tiStart"
- "_tiStarted"
- "_tiStop"
- "_tiStopped"
- "_tiV"
- "companionLinkClient authCompletionHandler, diconnecting with error=%{public}@"
- "getAssistantIsEnabledForDeviceWithSiriInfo, enabled=%{bool}d, error=%{public}@"

```
