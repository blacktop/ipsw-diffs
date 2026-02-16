## BackBoardHIDEventProcessors

> `/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors`

```diff

-735.1.10.0.0
-  __TEXT.__text: 0x21d8
-  __TEXT.__auth_stubs: 0x370
+735.4.6.0.0
+  __TEXT.__text: 0x243c
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x364
   __TEXT.__const: 0x80
   __TEXT.__oslogstring: 0x2b2
   __TEXT.__cstring: 0x15d
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__unwind_info: 0x128
   __TEXT.__objc_classname: 0x12d
   __TEXT.__objc_methname: 0x85f
   __TEXT.__objc_methtype: 0x304

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x250
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0xa20

   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC3361B3-6EA3-3B0A-B263-7A4C9C92923C
+  UUID: 3985A363-FCC4-3A96-946D-8E5A9C6DFC52
   Functions: 60
-  Symbols:   347
+  Symbols:   344
   CStrings:  191
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ _BKLogMotionEvents -> -[BKHIDVendorDefinedEventProcessor processEvent:sender:dispatcher:] : 84 -> 532
~ _BKLogHID -> _BKLogMotionEvents : 84 -> 100
~ -[BKHIDVendorDefinedEventProcessor processEvent:sender:dispatcher:] -> _BKLogHID : 524 -> 100
~ -[BKHIDGameControllerEventProcessor processEvent:sender:dispatcher:] : 448 -> 452
~ -[BKHIDGenericGestureEventProcessor setEventDispatcher:] : 12 -> 64
~ -[BKHIDGenericGestureEventProcessor setGenericGestureTypePerSenderID:] : 12 -> 64
~ -[BKHIDGenericGestureEventProcessor setPendingDestinationsPerSenderID:] : 12 -> 64
~ -[BKHIDGenericGestureEventProcessor _postEvent:toDestination:usingDispatcher:] : 280 -> 284
~ -[BKHIDGenericGestureEventProcessor serviceDidDisappear:] : 576 -> 596
~ -[BKHIDGenericGestureEventProcessor processEvent:sender:dispatcher:] : 1276 -> 1292
~ -[BKHIDPointerEventRecord setDestinations:] : 12 -> 64
~ -[BKHIDPointerEventRecord setSenderInfo:] : 12 -> 64
~ -[BKHIDPointerEventRecord succinctDescriptionBuilder] : 180 -> 184
~ -[BKHIDPointerEventRecord succinctDescription] : 76 -> 84
~ -[BKHIDPointerEventRecord descriptionWithMultilinePrefix:] : 76 -> 84
~ -[BKHIDPointerEventRecord descriptionBuilderWithMultilinePrefix:] : 204 -> 208
~ -[BKHIDPointerEventProcessor _dispatchEvent:sender:dispatcher:destinations:] : 348 -> 344
~ -[BKHIDPointerEventProcessor processEvent:sender:dispatcher:] : 1232 -> 1300
~ _BKLogBootUI : 84 -> 100
~ _BKLogButton : 84 -> 100
~ _BKLogDisplayAnnotations : 84 -> 100
~ _BKLogDisplayMonitor : 84 -> 100
~ _BKLogGenericGesture : 84 -> 100
~ _BKLogIdleTimer : 84 -> 100
~ _BKLogRenderOverlay : 84 -> 100
~ _BKLogHapticFeedback : 84 -> 100
~ _BKLogAccelerometer : 84 -> 100
~ _BKLogKeyPresses : 84 -> 100
~ _BKLogSendHIDEvent : 84 -> 100
~ -[BKHIDScrollEventProcessor _dispatchEvent:sender:dispatcher:destinations:] : 348 -> 344
~ -[BKHIDScrollEventProcessor processEvent:sender:dispatcher:] : 192 -> 196
~ -[BKHIDBiometricEventProcessor processEvent:sender:dispatcher:] : 476 -> 480

```
