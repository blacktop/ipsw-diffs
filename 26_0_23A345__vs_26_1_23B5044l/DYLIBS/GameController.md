## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.0.39.0.0
-  __TEXT.__text: 0x106090
-  __TEXT.__auth_stubs: 0x1c50
+13.1.4.0.0
+  __TEXT.__text: 0x107648
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xfe14
-  __TEXT.__const: 0x3c44
-  __TEXT.__cstring: 0xa119
-  __TEXT.__gcc_except_tab: 0x596c
-  __TEXT.__oslogstring: 0x9868
+  __TEXT.__objc_methlist: 0xfe34
+  __TEXT.__const: 0x3c74
+  __TEXT.__cstring: 0xa109
+  __TEXT.__gcc_except_tab: 0x5a40
+  __TEXT.__oslogstring: 0x9c78
   __TEXT.__dlopen_cstrs: 0xfd
   __TEXT.__swift5_typeref: 0x574
   __TEXT.__swift5_reflstr: 0x22f

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xc4
-  __TEXT.__unwind_info: 0x53c8
+  __TEXT.__unwind_info: 0x5448
   __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x41a6
-  __TEXT.__objc_methname: 0x190a9
-  __TEXT.__objc_methtype: 0x7ad6
+  __TEXT.__objc_classname: 0x41a8
+  __TEXT.__objc_methname: 0x190de
+  __TEXT.__objc_methtype: 0x7b31
   __TEXT.__objc_stubs: 0xf420
-  __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__const: 0x2d80
+  __DATA_CONST.__got: 0xba0
+  __DATA_CONST.__const: 0x2e08
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x7e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52e8
+  __DATA_CONST.__objc_selrefs: 0x52f0
   __DATA_CONST.__objc_protorefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x570
-  __AUTH_CONST.__auth_got: 0xe40
-  __AUTH_CONST.__const: 0x1f98
-  __AUTH_CONST.__cfstring: 0xb3e0
-  __AUTH_CONST.__objc_const: 0x48eb0
+  __AUTH_CONST.__auth_got: 0xe30
+  __AUTH_CONST.__const: 0x1f78
+  __AUTH_CONST.__cfstring: 0xb420
+  __AUTH_CONST.__objc_const: 0x48f28
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x4fc0
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x17a8
+  __DATA.__objc_ivar: 0x17ac
   __DATA.__data: 0x5e10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1f20
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0B68944B-9509-3E3D-9A4F-642D3BDF0B48
-  Functions: 7382
-  Symbols:   27404
-  CStrings:  9766
+  UUID: CF51D4C8-D8AC-3FB5-B8A5-139EF0EE3CA9
+  Functions: 7410
+  Symbols:   27474
+  CStrings:  9788
 
Symbols:
+ +[_GCSonyAccessControllerProfile logicalDevice:getSystemButtonName:sfSymbolName:needsMFiCompatibility:]
+ -[GCControllerAxisInput value].cold.1
+ -[GCControllerButtonInput isPressed].cold.1
+ -[GCControllerButtonInput isTouched].cold.1
+ -[GCControllerButtonInput value].cold.1
+ -[GCDeviceSessionConfiguration disableShareGestures]
+ -[GCDeviceSessionConfiguration setDisableShareGestures:]
+ -[GCMouseInput _handleButtonEventType:buttonMask:]
+ -[GCMouseInput handleMouseMovementEventWithDelta:]
+ -[GCMouseInput handleScrollEventWithDelta:]
+ -[_GCControllerManagerAppClient _onqueue_onHIDServiceAdded:]
+ -[_GCControllerManagerAppClient _onqueue_onHIDServiceRemoved:]
+ -[_GCDevicePhysicalInput popTransactionNotExceedingTimestamp:]
+ -[_GCDevicePhysicalInputFacade nextInputStateNotExceedingTimestamp:]
+ GCC_except_table127
+ GCC_except_table68
+ _OBJC_IVAR_$_GCController._spatial
+ _OBJC_IVAR_$_GCDeviceSessionConfiguration._disableShareGestures
+ __ZN18HapticSharedMemory11readCommandER13HapticCommand.cold.2
+ __ZN18HapticSharedMemory11readCommandER13HapticCommand.cold.3
+ __ZN18HapticSharedMemory5clearEv
+ __ZN18HapticSharedMemory5clearEv.cold.1
+ ___43-[GCControllerButtonInput _setValue:queue:]_block_invoke.89.cold.1
+ ___43-[GCControllerButtonInput _setValue:queue:]_block_invoke.90.cold.1
+ ___43-[GCControllerButtonInput _setValue:queue:]_block_invoke.cold.1
+ ___45-[GCControllerButtonInput _setTouched:queue:]_block_invoke.cold.1
+ ___48-[GCKeyboardInput(PubSub) _handleKeyboardEvent:]_block_invoke.cold.1
+ ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.136
+ ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.136.cold.1
+ ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.193
+ ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.193.cold.1
+ ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.193.cold.2
+ ___55-[GCControllerDirectionPad _fireValueChangedWithQueue:]_block_invoke.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.139
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.139.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.141
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.141.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.143
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.143.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.145
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.145.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.147
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.147.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.149
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.149.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.151
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.151.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.153
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.153.cold.1
+ ___58-[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]_block_invoke.286
+ ___58-[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]_block_invoke.cold.1
+ ___71-[_GCControllerManagerAppClient(ControllerService) publishControllers:]_block_invoke.442
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.201
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.201.cold.1
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.201.cold.2
+ ___ControllerAxisInputSetValue_block_invoke.cold.1
+ ___block_descriptor_40_e8_32w_e26_v16?0"<_GCButtonEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e26_v16?0"<_GCMotionEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e26_v16?0"<_GCScrollEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e27_v16?0"<_GCGamepadEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e27_v16?0"<_GCPointerEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e28_v16?0"<_GCKeyboardEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e29_v16?0"<_GCDigitizerEvent>"8lw32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"<_GCCollectionEvent>"8lw32l8
+ ___block_descriptor_68_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_69_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_70_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_73_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.434
+ ___block_literal_global.448
+ __gc_log_signpost
+ _objc_msgSend$disableShareGestures
+ _objc_msgSend$popTransactionNotExceedingTimestamp:
+ _objc_msgSend$setDisableShareGestures:
- -[GCMouseInput(PubSub) _handleButtonEventType:buttonMask:]
- -[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]
- -[GCMouseInput(PubSub) handleScrollEventWithDelta:]
- -[_GCControllerManagerAppClient controllersQueue]
- -[_GCControllerManagerAppClient onHIDServiceAdded:]
- -[_GCControllerManagerAppClient onHIDServiceRemoved:]
- -[_GCHapticServerManager readClientDataForStartTime:endTime:].cold.2
- -[_GCHapticServerManager readListCommand:client:renderTime:].cold.5
- GCC_except_table132
- GCC_except_table136
- _NSLog
- _OBJC_IVAR_$__GCControllerManagerAppClient._controllersQueue
- ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.137.cold.1
- ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.138
- ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke_3
- ___51-[_GCControllerManagerAppClient onHIDServiceAdded:]_block_invoke
- ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.194
- ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.194.cold.1
- ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.194.cold.2
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.140
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.140.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.142
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.142.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.144
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.144.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.146
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.146.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.148
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.148.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.150
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.150.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.152
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.152.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.154
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.154.cold.1
- ___58-[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]_block_invoke_2
- ___60-[_GCControllerManagerAppClient _onqueue_publishController:]_block_invoke
- ___62-[_GCControllerManagerAppClient _onqueue_unpublishController:]_block_invoke
- ___71-[_GCControllerManagerAppClient(ControllerService) publishControllers:]_block_invoke.447
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.203
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.203.cold.1
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.203.cold.2
- ___block_descriptor_40_e26_v16?0"<_GCButtonEvent>"8lu32l8
- ___block_descriptor_40_e26_v16?0"<_GCMotionEvent>"8lu32l8
- ___block_descriptor_40_e26_v16?0"<_GCScrollEvent>"8lu32l8
- ___block_descriptor_40_e27_v16?0"<_GCGamepadEvent>"8lu32l8
- ___block_descriptor_40_e27_v16?0"<_GCPointerEvent>"8lu32l8
- ___block_descriptor_40_e29_v16?0"<_GCDigitizerEvent>"8lu32l8
- ___block_descriptor_40_e30_v16?0"<_GCCollectionEvent>"8lu32l8
- ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_84_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_85_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
- ___block_descriptor_86_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_89_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
- ___block_literal_global.432
- ___block_literal_global.444
- ___block_literal_global.62
- ___getGCSignpostLogger_block_invoke
- __dispatch_queue_attr_concurrent
- _dispatch_barrier_async
- _dispatch_barrier_sync
- _gcSignpostLogger
- _getGCSignpostLogger
- _getGCSignpostLogger.cold.1
- _getGCSignpostLogger.onceToken
- _objc_msgSend$_handleButtonEventType:buttonMask:
- _objc_msgSend$handleMouseMovementEventWithDelta:
- _objc_msgSend$handleScrollEventWithDelta:
CStrings:
+ "@\"<GCDevicePhysicalInputState><GCDevicePhysicalInputStateDiff>\"24@0:8d16"
+ "@\"<GCDeviceSpatial>\""
+ "@24@0:8d16"
+ "BypassUIKit"
+ "DisableShareGestures"
+ "GCExtendedGamepad.handle.GamepadEvent"
+ "GCKeyboardInput.callback"
+ "GCKeyboardInput.handle.KeyboardEvent"
+ "GCMouseInput.callback"
+ "GCMouseInput.handle.ButtonEvent"
+ "GCMouseInput.handle.DigitizerEvent"
+ "GCMouseInput.handle.PointerEvent"
+ "GCMouseInput.handle.ScrollEvent"
+ "GCPhysicalInputProfile.Axis.value.callback"
+ "GCPhysicalInputProfile.Axis.value.read"
+ "GCPhysicalInputProfile.Axis.value.set"
+ "GCPhysicalInputProfile.Button.pressed.callback"
+ "GCPhysicalInputProfile.Button.pressed.read"
+ "GCPhysicalInputProfile.Button.touched.callback"
+ "GCPhysicalInputProfile.Button.touched.read"
+ "GCPhysicalInputProfile.Button.touched.set"
+ "GCPhysicalInputProfile.Button.value.callback"
+ "GCPhysicalInputProfile.Button.value.read"
+ "GCPhysicalInputProfile.Button.value.set"
+ "GCPhysicalInputProfile.DirectionPad.value.callback"
+ "IgnoresUIAlertAssertions"
+ "IsNonUI"
+ "MonitorControllerEventsInBackground"
+ "_disableShareGestures"
+ "_spatial"
+ "disableShareGestures"
+ "nextInputStateNotExceedingTimestamp:"
+ "popTransactionNotExceedingTimestamp:"
+ "setDisableShareGestures:"
+ "{device: \"%p\", eventTimestamp: %llu, lastEventTimestamp: %f}"
+ "{device: \"%p\", lastEventTimestamp: %f}"
+ "{device: \"%p\", primaryAlias: \"%{sensitive}@\", lastEventTimestamp: %f, value: %{sensitive}f}"
+ "{device: \"%p\", primaryAlias: \"%{sensitive}@\", lastEventTimestamp: %f, value: %{sensitive}u"
+ "{device: \"%p\", primaryAlias: \"%{sensitive}@\", lastEventTimestamp: %f, value: %{sensitive}u}"
+ "{device: \"%p\", primaryAlias: \"%{sensitive}@\", lastEventTimestamp: %f, value: {x: %{sensitive}f, y: %{sensitive}f}}"
+ "{device: \"%p\", primaryAlias: \"%{sensitive}@\", lastEventTimestamp: %f}"
+ "{handled: %u}"
+ "{}"
- "%@, receiveTimestamp=%f"
- "Axis Value Change Callback"
- "Axis Value Read"
- "Axis Value Updated"
- "Button Pressed Change Callback"
- "Button Touched Change"
- "Button Touched Change Callback"
- "Button Touched Updated"
- "Button Value Change Callback"
- "Button Value Read"
- "Button Value Updated"
- "DPad Value Change Callback"
- "DPad Value Updated"
- "Handle Extended Gamepad Event"
- "Resume Connection To Game Controller Daemon"
- "Signposts"
- "_handleButtonEventType:buttonMask:"
- "handleMouseMovementEventWithDelta:"
- "handleScrollEventWithDelta:"
- "timestamp=%llu"
- "timestamp=%llu, receiveTimestamp=%f"
- "v32@0:8Q16Q24"
- "\xf1"

```
