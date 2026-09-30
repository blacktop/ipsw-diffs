## SIMToolkitUI

> `/System/Library/PrivateFrameworks/SIMToolkitUI.framework/SIMToolkitUI`

```diff

-86.0.0.0.0
-  __TEXT.__text: 0x12578
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x1554
+87.0.0.0.0
+  __TEXT.__text: 0x13aa8
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_methlist: 0x158c
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xe2f
-  __TEXT.__oslogstring: 0x17b3
-  __TEXT.__gcc_except_tab: 0x284
-  __TEXT.__unwind_info: 0x608
-  __TEXT.__objc_classname: 0x5f2
-  __TEXT.__objc_methname: 0x3327
-  __TEXT.__objc_methtype: 0xc00
-  __TEXT.__objc_stubs: 0x2380
+  __TEXT.__cstring: 0xe51
+  __TEXT.__oslogstring: 0x1a05
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__unwind_info: 0x680
+  __TEXT.__objc_classname: 0x5f3
+  __TEXT.__objc_methname: 0x331d
+  __TEXT.__objc_methtype: 0xc0f
+  __TEXT.__objc_stubs: 0x23a0
   __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x690
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__objc_const: 0x6ec0
+  __AUTH_CONST.__cfstring: 0xce0
+  __AUTH_CONST.__objc_const: 0x6fa0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x21c
+  __DATA.__objc_ivar: 0x230
   __DATA.__data: 0x600
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x5a0

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62C800A8-2595-347F-AAAA-55BB6E952236
-  Functions: 490
-  Symbols:   2257
-  CStrings:  1136
+  UUID: 76FB1DAD-6C06-3630-9CC5-D64766B63F4D
+  Functions: 505
+  Symbols:   2301
+  CStrings:  1153
 
Symbols:
+ -[STKUSSDAlertSessionManager _removeNotification]
+ -[STKUSSDAlertSessionManager _showAfterDeviceUnlock:]
+ -[STKUSSDAlertSessionManager _showNotification]
+ -[STKUSSDAlertSessionManager _showNotification].cold.1
+ -[STKUSSDAlertSessionManager checkLockScreenPolicy:timeoutSec:]
+ -[STKUSSDAlertSessionManager deviceLockStateChanged:]
+ GCC_except_table17
+ _OBJC_IVAR_$_STKUSSDAlertSessionManager._deviceLockMonitor
+ _OBJC_IVAR_$_STKUSSDAlertSessionManager._lock
+ _OBJC_IVAR_$_STKUSSDAlertSessionManager._lock_deviceLocked
+ _OBJC_IVAR_$_STKUSSDAlertSessionManager._notificationGroup
+ _OBJC_IVAR_$_STKUSSDAlertSessionManager._userNotificationCenter
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ ___47-[STKUSSDAlertSessionManager _showNotification]_block_invoke
+ ___47-[STKUSSDAlertSessionManager _showNotification]_block_invoke.cold.1
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.69
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.71
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.75
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.76
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.79
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.82
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.83
+ ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.84
+ ___84-[STKSIMToolkitAlertSessionManager _queue_handleSIMToolkitEvent:responder:userInfo:]_block_invoke.98
+ ___block_literal_global.73
+ ___block_literal_global.78
+ ___block_literal_global.81
+ ___block_literal_global.86
+ _kAllowSTKAlertInLockScreen
+ _kKeyImportantCarrierMsg
+ _kKeyUnlockIPhoneViewMsg
+ _kSIMToolkitUIFrameworkBundle
+ _kSIMToolkitUIFrameworkBundleTable
+ _kSTKAlertLockScreenNotificationTimeoutSeconds
+ _objc_msgSend$checkLockScreenPolicy:timeoutSec:
+ _objc_retainAutoreleasedReturnValue
- -[STKSIMToolkitAlertSessionManager remoteAlertDescriptorForSession:].cold.2
- -[STKSIMToolkitAlertSessionManager remoteAlertDescriptorForSession:].cold.3
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.34
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.36
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.40
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.41
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.44
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.47
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.48
- ___72-[STKUSSDAlertSessionManager _queue_handleUSSDEvent:responder:userInfo:]_block_invoke.49
- ___84-[STKSIMToolkitAlertSessionManager _queue_handleSIMToolkitEvent:responder:userInfo:]_block_invoke.110
- ___block_literal_global.38
- ___block_literal_global.43
- ___block_literal_global.46
- ___block_literal_global.51
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "%s USSD alert; %s"
+ "B32@0:8@16^Q24"
+ "Device lock state changed: %s"
+ "Device unlocked, signaling notification group"
+ "LOCKED"
+ "Remove USSD notifications with Identifier='%@'"
+ "Session <%p> - USSD Begin alert blocked due to lock screen timeout"
+ "Session <%p> - USSD alert blocked due to lock screen timeout"
+ "Show STK alert; device already unlocked"
+ "Show USSD alert; device already unlocked"
+ "Show USSD alerts notification with timeout = %ld secs (using STK carrier bundle key)"
+ "Show USSD notification asking user to unlock device (identifier: %@)"
+ "UNLOCKED"
+ "USSD_Notification"
+ "Unable to add USSD notification request %@"
+ "Waiting up to %ld seconds for device unlock..."
+ "checkLockScreenPolicy:timeoutSec:"
- "smsMessageTestMessageReceived:body:address:"

```
