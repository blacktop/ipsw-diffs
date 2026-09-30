## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.4.9.0.0
-  __TEXT.__text: 0x10a62c
+13.5.1.0.0
+  __TEXT.__text: 0x10a864
   __TEXT.__auth_stubs: 0x1bf0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xfa7c
   __TEXT.__const: 0x1c34
-  __TEXT.__gcc_except_tab: 0x58fc
+  __TEXT.__gcc_except_tab: 0x59a4
   __TEXT.__cstring: 0x9fe4
   __TEXT.__oslogstring: 0x97b8
   __TEXT.__dlopen_cstrs: 0xfd

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xc4
-  __TEXT.__unwind_info: 0x5550
+  __TEXT.__unwind_info: 0x5578
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0x4033
+  __TEXT.__objc_classname: 0x4023
   __TEXT.__objc_methname: 0x18f0c
   __TEXT.__objc_methtype: 0x763d
   __TEXT.__objc_stubs: 0xf560
   __DATA_CONST.__got: 0xb88
-  __DATA_CONST.__const: 0x2db8
+  __DATA_CONST.__const: 0x2d80
   __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x778

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 78D64C20-639A-3CF3-B5BD-00747B60FD6B
+  UUID: B6136B3C-3D51-3793-A79F-C18EA782BA4A
   Functions: 7394
-  Symbols:   27537
-  CStrings:  9695
+  Symbols:   27539
+  CStrings:  9693
 
Symbols:
+ ___block_descriptor_48_e8_32w_e27_v16?0"<_GCGamepadEvent>"8lw32l8
+ ___block_descriptor_56_e8_32s40s_e11_v20?0q8C16ls32l8s40l8
- ___block_descriptor_40_e28_v16?0"<_GCKeyboardEvent>"8lu32l8
- ___block_descriptor_48_e23_v16?0^{__IOHIDEvent=}8lu40l8
- ___block_descriptor_48_e27_v16?0"<_GCGamepadEvent>"8lu32l8
- ___block_descriptor_56_e8_32s_e11_v20?0q8C16lu40l8s32l8
Functions:
~ -[_GCNintendoJoyConDevice(Components) gamepadEventSource] : 528 -> 568
~ ___68-[_GCHapticServerManager acceptNewConnection:fromHapticsEnabledApp:]_block_invoke.15 : 316 -> 320
~ -[_GCDefaultPhysicalDevice(Gamepad) gamepadEventSource] : 628 -> 640
~ -[_GCGamepadEventGamepadHIDAdapter initWithSource:service:] : 316 -> 392
~ ___59-[_GCGamepadEventGamepadHIDAdapter initWithSource:service:]_block_invoke : 364 -> 392
~ -[_GCMotionEventHIDAdapter initWithSource:service:] : 316 -> 392
~ ___51-[_GCMotionEventHIDAdapter initWithSource:service:]_block_invoke : 888 -> 908
~ -[_GCGamepadEventFusion initWithConfiguration:sources:] : 540 -> 628
~ ___55-[_GCGamepadEventFusion initWithConfiguration:sources:]_block_invoke : 488 -> 524
~ ___55-[_GCGamepadEventFusion initWithConfiguration:sources:]_block_invoke_2 : 252 -> 324
~ -[_GCGamepadEventKeyboardEventAdapter initWithConfiguration:source:] : 256 -> 324
~ ___68-[_GCGamepadEventKeyboardEventAdapter initWithConfiguration:source:]_block_invoke : 504 -> 520
~ -[_GCSimulatorControllerManager _onqueue_addController:] : 1056 -> 1088
CStrings:
- " `"
- "`"

```
