## backboardd

> `/usr/libexec/backboardd`

```diff

 668.1.5.0.0
-  __TEXT.__text: 0x9f900
-  __TEXT.__auth_stubs: 0x1c50
-  __TEXT.__objc_stubs: 0xe9a0
-  __TEXT.__objc_methlist: 0x6774
+  __TEXT.__text: 0xa4014
+  __TEXT.__auth_stubs: 0x1c90
+  __TEXT.__objc_stubs: 0xeaa0
+  __TEXT.__objc_methlist: 0x68b8
   __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0x4f54
-  __TEXT.__objc_methname: 0x14a54
-  __TEXT.__cstring: 0x711e
-  __TEXT.__objc_classname: 0x1c70
-  __TEXT.__objc_methtype: 0x3fed
-  __TEXT.__oslogstring: 0x9e5c
+  __TEXT.__gcc_except_tab: 0x5154
+  __TEXT.__objc_methname: 0x14c5b
+  __TEXT.__cstring: 0x73d6
+  __TEXT.__objc_classname: 0x1d39
+  __TEXT.__objc_methtype: 0x402d
+  __TEXT.__oslogstring: 0xa256
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2980
-  __DATA_CONST.__auth_got: 0xe40
-  __DATA_CONST.__got: 0xa18
+  __TEXT.__unwind_info: 0x2a50
+  __DATA_CONST.__auth_got: 0xe60
+  __DATA_CONST.__got: 0xa28
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4ad8
-  __DATA_CONST.__cfstring: 0x7ce0
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__const: 0x4bd8
+  __DATA_CONST.__cfstring: 0x8160
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x14058
-  __DATA.__objc_selrefs: 0x44f8
-  __DATA.__objc_ivar: 0xf1c
-  __DATA.__objc_data: 0x3930
+  __DATA.__objc_const: 0x14708
+  __DATA.__objc_selrefs: 0x4548
+  __DATA.__objc_ivar: 0xf60
+  __DATA.__objc_data: 0x3ac0
   __DATA.__data: 0x1bb0
   __DATA.__bss: 0x418
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3119
-  Symbols:   784
-  CStrings:  6239
+  Functions: 3182
+  Symbols:   790
+  CStrings:  6319
 
Symbols:
+ _OBJC_CLASS_$_BKSHIDEventBaseAttributes
+ _kCFAllocatorSystemDefault
+ _IOHIDEventCreateTouchSensitiveButtonEvent
+ _NSStringFromBKSHIDTouchSensitiveButtonIdentifier
+ _IOHIDEventCreateVendorDefinedEvent
+ _IOHIDEventCreateForceStageEvent
CStrings:
+ "TouchSensitiveButton: got event for idle stage, bailing"
+ "_lock_activeCameraButtonScanningPIDs"
+ "setPrimaryPage:primaryUsage:"
+ "idle"
+ "%!{(MISSING)public}@: added destinations: %!{(MISSING)public}@"
+ "BKHIDTouchSensitiveButtonEventProcessor"
+ "in %!l(MISSING)lX %!{(MISSING)public}@"
+ "BKHIDVendorDefinedTouchSensitiveButtonEventProcessor.m"
+ "out %!l(MISSING)lX -> %!{(MISSING)public}@"
+ "processDidTerminate:"
+ "collectionLineBreakNoneStyle"
+ "bug: shouldn't have a record at idle stage"
+ "setScanningActive: unsupported touch button identifier: %!d(MISSING)"
+ "forceProgress"
+ "_BKHIDXXTouchSensitiveButtonSetScanMode"
+ "out %!{(MISSING)public}@ -> %!{(MISSING)public}@"
+ "enumerateIndexesWithOptions:usingBlock:"
+ "HalfPressThresholdModifier"
+ "_postCancelEventToDestinations:locals:dispatcher:"
+ "progress"
+ "clickDownPredicted"
+ "overlayStyle:block:"
+ "nextThreshold"
+ "_lock_services"
+ "click"
+ "BKHIDTouchSensitiveButtonScanningController"
+ "maybeIntermediate"
+ "BKHIDTouchSensitiveButtonEventProcessor.m"
+ "intermediate"
+ "releasedThreshold"
+ "_buttonScanningController"
+ "makeObjectsPerformSelector:withObject:"
+ "missing force stage event -- dropping event: %!{(MISSING)public}@"
+ "_lock_pidToProcessDeathWatcher"
+ "[TouchSensitiveButton %!{(MISSING)public}@]: did not see an enter transition for this button, ignoring exit event"
+ "%!l(MISSING)lX/Tostada"
+ "%!l(MISSING)lX/%!X(MISSING)/%!X(MISSING)"
+ "_stagesEntered"
+ "setScanningActive:%!{(MISSING)BOOL}u button:%!{(MISSING)public}@ posting to service %!{(MISSING)public}@"
+ "setScanningActive:%!{(MISSING)BOOL}u button:%!{(MISSING)public}@ pid:%!d(MISSING)"
+ "forceProgressVelocity"
+ "%!@(MISSING) (%!d(MISSING))"
+ "_BKTouchSensitiveButtonKey"
+ "v32@0:8B16q20i28"
+ "pressedThreshold"
+ "<not a TouchSensitiveButton event>"
+ "%!{(MISSING)public}@: removed destinations: %!{(MISSING)public}@"
+ "setScanningActive:buttonIdentifier:forPID:"
+ "positionY"
+ "<missing force subevent>"
+ "incoming %!{(MISSING)public}@"
+ "CameraButtonScanActive"
+ "fastSwipe"
+ "BKHIDTouchSensitiveButton disallowed persistent properties: %!{(MISSING)public}@"
+ "outgoing %!{(MISSING)public}@ -> %!{(MISSING)public}@"
+ "BKHIDVendorDefinedTouchSensitiveButtonEventProcessor"
+ "<invalid:%!X(MISSING)>"
+ "_BKTouchSensitiveButtonEventRecord"
+ "[TouchSensitiveButton %!{(MISSING)public}@]: did not see an enter transition to stage %!d(MISSING), ignoring exit event"
+ "engaged"
+ "not a ForceStage event"
+ "()"
+ "progressVelocity"
+ "\x15"
+ "lowSNRSwipe"
+ "data for TouchSensitiveButton event is corrupt"
+ "positionDelta"
+ "liftOffPredicted"
+ "setScanningActive:%!{(MISSING)BOOL}u button:%!{(MISSING)public}@-- no services (yet?), pending"
+ "positionDeltaY"
+ "transition"
+ "touchSensitiveButtonServicePersistentPropertyController"
+ "v16@?0@\"BKSMutableHIDEventSenderDescriptor\"8"
+ "[TouchSensitiveButton %!{(MISSING)public}@]: did not see an enter transition to stage %!{(MISSING)public}@, ignoring change event"
+ "_lock_eventRecords"
+ "@\"BKHIDTouchSensitiveButtonScanningController\""
+ "_postEnterEventToDestinations:locals:dispatcher:"

```
