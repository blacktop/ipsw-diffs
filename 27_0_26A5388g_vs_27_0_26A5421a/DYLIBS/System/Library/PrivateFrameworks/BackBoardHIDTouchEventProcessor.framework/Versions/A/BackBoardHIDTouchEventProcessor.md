## BackBoardHIDTouchEventProcessor

> `/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/Versions/A/BackBoardHIDTouchEventProcessor`

```diff

-873.200.0.0.0
-  __TEXT.__text: 0x3ceac
+877.0.0.0.0
+  __TEXT.__text: 0x3cf30
   __TEXT.__objc_methlist: 0x27d0
   __TEXT.__const: 0x400
   __TEXT.__constg_swiftt: 0x124

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0x3ea8
-  __TEXT.__oslogstring: 0x2c3d
+  __TEXT.__oslogstring: 0x2c6b
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1328
+  __TEXT.__unwind_info: 0x1330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_const: 0x6f20
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x6c0
   __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x54c

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1121
-  Symbols:   3498
+  Symbols:   3500
   CStrings:  571
 
Symbols:
+ _BKLogEventDelivery
+ _objc_msgSend$setClientConnectionIdentifier:
Functions:
~ -[BKHIDDirectTouchEventProcessor initWithHitTestDispatcher:displayRenderSpace:deliveryManager:senderCache:serviceMatcherDataProvider:] -> -[BKHIDDirectTouchEventProcessor _initWithHitTestDispatcher:persistentPropertyController:deliveryManagerProvider:displayRenderSpace:orientationProvider:senderCache:touchServiceClientManager:touchPadManager:serviceMatcherDataProvider:] : 384 -> 2064
~ -[BKHIDDirectTouchEventProcessor _initWithHitTestDispatcher:persistentPropertyController:deliveryManagerProvider:displayRenderSpace:orientationProvider:senderCache:touchServiceClientManager:touchPadManager:serviceMatcherDataProvider:] -> -[BKHIDDirectTouchEventProcessor initWithHitTestDispatcher:displayRenderSpace:deliveryManager:senderCache:serviceMatcherDataProvider:] : 2064 -> 384
~ ___44-[BKDirectTouchState _postEventsFromPoster:]_block_invoke : 2664 -> 2708
~ -[BKHIDEventHitTestDispatcher sendEvent:forTargetID:toClientConnectionIdentifier:] : 180 -> 268
CStrings:
+ "can't dispatch event %{public}@ to target %{public}@: invalid client connection identifier / task name 0x%X"
- "can't dispatch pointer event to invalid client task name 0x%X"
```
