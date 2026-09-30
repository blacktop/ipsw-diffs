## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0x1bfe8
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x26e0
-  __TEXT.__objc_methlist: 0xa8c
+1170.0.7.0.0
+  __TEXT.__text: 0x1bda4
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_stubs: 0x27a0
+  __TEXT.__objc_methlist: 0xaa4
   __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__objc_methname: 0x3525
+  __TEXT.__objc_methname: 0x35d0
   __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0xb1f
-  __TEXT.__cstring: 0x171a
+  __TEXT.__objc_methtype: 0xb29
+  __TEXT.__cstring: 0x171b
   __TEXT.__oslogstring: 0x1037
   __TEXT.__const: 0xb0
-  __TEXT.__unwind_info: 0x738
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x730
+  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x718
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x26c0
-  __DATA.__objc_selrefs: 0xba0
-  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_const: 0x26f0
+  __DATA.__objc_selrefs: 0xbd0
+  __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x315
   __DATA.__bss: 0x1180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 717
-  Symbols:   520
-  CStrings:  929
+  Functions: 715
+  Symbols:   516
+  CStrings:  938
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _uarpPlatformAssetSuperBinaryPullProposedPayloadHeader
- _dispatch_assert_queue$V2
- _uarpPlatformAssetSuperBinaryPullPayloadHeader
- _uarpSendAssetAvailableNotificationAck
- _uarpSendAssetProcessingNotificationAck
- _uarpSendDynamicAssetPreProcessingStatusAck
- _uarpSendNoFirmwareUpdateAvailable
CStrings:
+ "\x03\x11I"
+ "-[UARPUpdaterServiceHID qProcessStandaloneDynamicAssetSolicitation:modelNumbers:notifyService:]"
+ "@\"NSDate\""
+ "T@\"NSDate\",&,V_lastReportedStagingTime"
+ "_lastReportedStagingTime"
+ "compare:"
+ "dateByAddingTimeInterval:"
+ "distantPast"
+ "lastReportedStagingTime"
+ "now"
+ "qHoldPowerAssertionForAccessory:"
+ "qPostStagingStatusNotificationForAccessory:status:"
+ "qProcessStandaloneDynamicAssetSolicitation:modelNumbers:notifyService:"
+ "qReleasePowerAssertionForAccessory:"
+ "setLastReportedStagingTime:"
- "\x03\x11H"
- "-[UARPUpdaterServiceHID processStandaloneDynamicAssetSolicitation:modelNumbers:notifyService:]"
- "holdPowerAssertionForAccessory:"
- "postStagingStatusNotificationForAccessory:status:"
- "processStandaloneDynamicAssetSolicitation:modelNumbers:notifyService:"
- "releasePowerAssertionForAccessory:"

```
