## RelativeMotion

> `/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion`

```diff

-300.0.2.0.0
-  __TEXT.__text: 0xa1a0
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x89c
+305.0.15.0.0
+  __TEXT.__text: 0x9ecc
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x824
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xd1d
+  __TEXT.__cstring: 0xd02
   __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0x17f4
-  __TEXT.__unwind_info: 0x428
-  __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x14a4
-  __TEXT.__objc_methtype: 0x675
-  __TEXT.__objc_stubs: 0xd00
-  __DATA_CONST.__got: 0x120
+  __TEXT.__oslogstring: 0x1811
+  __TEXT.__unwind_info: 0x418
+  __TEXT.__objc_classname: 0x1c6
+  __TEXT.__objc_methname: 0x13c5
+  __TEXT.__objc_methtype: 0x636
+  __TEXT.__objc_stubs: 0xca0
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x498
+  __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x1a50
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__cfstring: 0x4e0
+  __AUTH_CONST.__objc_const: 0x1890
+  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x108
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x3a0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD75B6BD-E4AD-340B-A8DD-EC1F95A0391E
-  Functions: 320
-  Symbols:   1333
-  CStrings:  555
+  UUID: E735F6CA-C9ED-3537-B581-8161E41F98C1
+  Functions: 311
+  Symbols:   1279
+  CStrings:  541
 
Symbols:
+ -[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:]
+ -[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]
+ -[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:]
+ -[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:].cold.1
+ -[RMRelativeMotionManager startReceivingAudioListenerPose]
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table20
+ ___105-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:]_block_invoke
+ ___113-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]_block_invoke
+ ___113-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]_block_invoke.29
+ ___113-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]_block_invoke.29.cold.1
+ ___113-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]_block_invoke.cold.1
+ ___113-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]_block_invoke.cold.2
+ ___113-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:]_block_invoke.cold.3
+ ___82-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:]_block_invoke
+ ___82-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:]_block_invoke_2
+ ___82-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:]_block_invoke_2.cold.1
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.32
+ ___block_literal_global.63
+ ___block_literal_global.67
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_msgSend$startReceivingAudioListenerPose
+ _objc_msgSend$startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:
- -[RMAudioListenerPoseManager setStatusCallback:]
- -[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:statusCallback:]
- -[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]
- -[RMAudioListenerPoseManager statusCallback]
- -[RMMediaSessionObserver .cxx_destruct]
- -[RMMediaSessionObserver manager]
- -[RMMediaSessionObserver setManager:]
- -[RMMediaSessionObserver startSessionStatusUpdatesForClientMode:toQueue:withHandler:]
- -[RMMediaSessionObserver stopSessionStatusUpdates]
- -[RMMediaSessionOptions init]
- -[RMMediaSessionStatus initWithInternal:]
- -[RMMediaSessionStatus shortDescription]
- -[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:]
- -[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:].cold.1
- -[RMRelativeMotionManager startReceivingAudioListenerPoseWithStatusCallback:]
- GCC_except_table12
- GCC_except_table21
- _OBJC_CLASS_$_RMMediaSessionObserver
- _OBJC_CLASS_$_RMMediaSessionStatus
- _OBJC_IVAR_$_RMAudioListenerPoseManager._statusCallback
- _OBJC_IVAR_$_RMMediaSessionObserver._manager
- _OBJC_IVAR_$_RMMediaSessionStatus._internal
- _OBJC_METACLASS_$_RMMediaSessionObserver
- _OBJC_METACLASS_$_RMMediaSessionStatus
- __OBJC_$_INSTANCE_METHODS_RMMediaSessionObserver
- __OBJC_$_INSTANCE_METHODS_RMMediaSessionStatus
- __OBJC_$_INSTANCE_VARIABLES_RMMediaSessionObserver
- __OBJC_$_INSTANCE_VARIABLES_RMMediaSessionStatus
- __OBJC_$_PROP_LIST_RMMediaSessionObserver
- __OBJC_$_PROP_LIST_RMMediaSessionStatus
- __OBJC_CLASS_RO_$_RMMediaSessionObserver
- __OBJC_CLASS_RO_$_RMMediaSessionStatus
- __OBJC_METACLASS_RO_$_RMMediaSessionObserver
- __OBJC_METACLASS_RO_$_RMMediaSessionStatus
- ___120-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:statusCallback:]_block_invoke
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.30
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.30.cold.1
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.1
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.2
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.3
- ___128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.4
- ___97-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:]_block_invoke
- ___97-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:]_block_invoke_2
- ___97-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:]_block_invoke_2.cold.1
- ___block_descriptor_57_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.33
- ___block_literal_global.65
- ___block_literal_global.69
- _kCMMediaSessionPredictionIntervalMicroseconds
- _objc_msgSend$initWithInternal:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$predictionIntervalMicroseconds
- _objc_msgSend$startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:
- _objc_msgSend$startReceivingAudioListenerPoseWithStatusCallback:
CStrings:
+ "-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:]"
+ "Connection still invalid, next reconnection attempt will be in %lu seconds"
+ "[RelativeMotionManager] receivingAudioListenerPose %{public}f, xpcLatency %{public}.2f ms"
+ "startReceivingAudioListenerPose"
+ "startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:"
+ "startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:"
+ "v28@0:8B16@?20"
- "-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:]"
- "@24@0:8r^{?=d}16"
- "Connection stil invalid, next reconnection attempt will be in %lu seconds"
- "RMMediaSessionObserver"
- "RMMediaSessionStatus"
- "State: %.0f"
- "[RelativeMotionManager] receivingAudioListenerPose %{public}f"
- "_internal"
- "_statusCallback"
- "initWithInternal:"
- "numberWithUnsignedLongLong:"
- "shortDescription"
- "startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallback:statusCallback:"
- "startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:"
- "startReceivingAudioListenerPoseWithStatusCallback:"
- "startSessionStatusUpdatesForClientMode:toQueue:withHandler:"
- "stopSessionStatusUpdates"
- "v36@0:8B16@?20@?28"
- "v40@0:8q16@24@?32"
- "{?=\"machAbsTimestamp\"d}"

```
