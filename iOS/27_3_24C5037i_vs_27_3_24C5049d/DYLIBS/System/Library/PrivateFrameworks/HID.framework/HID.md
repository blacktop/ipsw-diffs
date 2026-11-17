## HID

> `/System/Library/PrivateFrameworks/HID.framework/HID`

```diff

 2360.60.6.0.0
-  __TEXT.__text: 0x12e60
+  __TEXT.__text: 0x12da8
   __TEXT.__objc_methlist: 0x24ec
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x226f
   __TEXT.__gcc_except_tab: 0x2e8
   __TEXT.__oslogstring: 0x6cd
   __TEXT.__dof_iohidfami: 0x28d
-  __TEXT.__unwind_info: 0xba8
+  __TEXT.__unwind_info: 0xba0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 986
-  Symbols:   1595
+  Functions: 983
+  Symbols:   1592
   CStrings:  455
 
Symbols:
+ _os_unfair_recursive_lock_lock
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[IOHIDDeviceClass valueAvailableCallback:] : 620 -> 604
~ -[IOHIDDeviceClass setReport:reportID:report:reportLength:timeout:callback:context:options:] : 548 -> 552
- _OUTLINED_FUNCTION_11
~ -[HIDServiceClient(HIDFramework) setRemovalHandler:] : 148 -> 144
- _OUTLINED_FUNCTION_12
~ __asyncCallback : 732 -> 728
~ -[HIDManager setInputElementHandler:] : 136 -> 132
~ -[HIDManager setDeviceNotificationHandler:] : 164 -> 160
~ -[HIDManager setInputReportHandler:] : 136 -> 132
~ -[HIDManager setCancelHandler:] : 112 -> 108
~ -[HIDManager activate] : 160 -> 156
~ -[HIDDevice(HIDFramework) commitElements:direction:error:timeout:callback:] : 232 -> 228
~ _batchInputValueCallback : 268 -> 264
~ -[HIDDevice(HIDFramework) activate] : 364 -> 360
~ -[HIDDevice(HIDFramework) handlePropertyChange] : 908 -> 900
~ -[HIDEventSystemClient setCancelHandler:] : 112 -> 108
~ -[HIDEventSystemClient setEventHandler:] : 140 -> 136
~ -[HIDEventSystemClient setResetHandler:] : 140 -> 136
~ -[HIDEventSystemClient setEventFilterHandler:] : 140 -> 136
~ -[HIDEventSystemClient setServiceNotificationHandler:] : 140 -> 136
~ -[HIDEventSystemClient setPropertyChangedHandler:matching:] : 516 -> 512
~ -[HIDEventSystemClient activate] : 160 -> 156
~ -[IOHIDDeviceClass initConnect] : 212 -> 204
~ -[IOHIDDeviceClass start:service:] : 120 -> 116
~ -[IOHIDDeviceClass getProperty:property:] : 576 -> 568
~ -[IOHIDDeviceClass getAsyncEventSource:] : 120 -> 116
~ -[IOHIDDeviceClass copyMatchingElements:elements:options:] : 412 -> 408
~ -[IOHIDDeviceClass getValue:value:timeout:callback:context:options:] : 764 -> 760
~ -[IOHIDDeviceClass setInputReportCallback:reportLength:callback:context:options:] : 268 -> 256
~ __asyncCallback : 288 -> 284
~ -[IOHIDDeviceClass setInputReportWithTimeStampCallback:reportLength:callback:context:options:] : 232 -> 224
- _OUTLINED_FUNCTION_13
~ -[IOHIDTransactionClass commit:timeout:callback:options:] : 2552 -> 2544
~ -[IOHIDDeviceClass initElements] : 540 -> 548
~ -[IOHIDDeviceClass initPort] : 208 -> 220
~ -[IOHIDDeviceClass initQueue] : 492 -> 488
~ -[IOHIDDeviceClass open:] : 416 -> 412
~ -[IOHIDDeviceClass close:] : 244 -> 248
~ -[IOHIDDeviceClass setProperty:property:] : 388 -> 384
~ -[IOHIDDeviceClass setValue:value:timeout:callback:context:options:] : 588 -> 600
~ -[IOHIDDeviceClass getReport:reportID:report:reportLength:timeout:callback:context:options:] : 600 -> 604
```
