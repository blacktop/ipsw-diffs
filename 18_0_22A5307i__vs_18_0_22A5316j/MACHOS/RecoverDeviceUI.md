## RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

-2082.0.27.0.2
-  __TEXT.__text: 0xd13c
+2082.0.43.0.1
+  __TEXT.__text: 0xd8e4
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x2740
-  __TEXT.__objc_methlist: 0x70c
+  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_methlist: 0x73c
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xf1a
-  __TEXT.__objc_methname: 0x3c61
+  __TEXT.__cstring: 0xf29
+  __TEXT.__objc_methname: 0x3d49
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methtype: 0x15b6
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__oslogstring: 0xfe2
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_methtype: 0x15c1
+  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__oslogstring: 0x113e
+  __TEXT.__unwind_info: 0x258
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x2d8
-  __DATA_CONST.__cfstring: 0x13e0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__cfstring: 0x1400
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x22f8
-  __DATA.__objc_selrefs: 0xb08
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_const: 0x2328
+  __DATA.__objc_selrefs: 0xb58
+  __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 205
-  Symbols:   1716
-  CStrings:  1028
+  Functions: 213
+  Symbols:   1772
+  CStrings:  1050
 
Symbols:
+ -[RecoverDeviceUIExtensionRemoteViewController doneWaitingForServerResponse]
+ -[RecoverDeviceUIExtensionRemoteViewController doneWaitingForServerResponse]
+ -[RecoverDeviceUIExtensionRemoteViewController setSetupTimer:]
+ -[RecoverDeviceUIExtensionRemoteViewController setSetupTimer:]
+ -[RecoverDeviceUIExtensionRemoteViewController setupTimer]
+ -[RecoverDeviceUIExtensionRemoteViewController setupTimer]
+ -[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]
+ -[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._setupTimer
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.713
+ __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.713
+ __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.581
+ __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.581
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.655
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.655
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.657
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.657
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.717
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.717
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.718
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.718
+ __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.399
+ __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.399
+ __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.558
+ __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.558
+ __81-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:resultType:]_block_invoke.630
+ __81-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:resultType:]_block_invoke.630
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.637
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.637
+ ___69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke
+ ___69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke
+ ___76-[RecoverDeviceUIExtensionRemoteViewController doneWaitingForServerResponse]_block_invoke
+ ___76-[RecoverDeviceUIExtensionRemoteViewController doneWaitingForServerResponse]_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
+ __block_literal_global.715
+ __block_literal_global.715
+ _objc_msgSend$addTimer:forMode:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$doneWaitingForServerResponse
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$nearbyAuthTag
+ _objc_msgSend$setSetupTimer:
+ _objc_msgSend$setupTimer
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$timerWithTimeInterval:repeats:block:
+ _objc_msgSend$waitForServerResponse
- __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.710
- __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.710
- __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.578
- __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.578
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.652
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.652
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.654
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.654
- __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.395
- __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.395
- __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.555
- __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.555
- __81-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:resultType:]_block_invoke.627
- __81-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:resultType:]_block_invoke.627
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.634
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.634
- __block_literal_global.712
- __block_literal_global.712
CStrings:
+ "\x1f\x05\x12"
+ "@\"NSTimer\""
+ "ForceAuthTag"
+ "ForceAuthTag default is set to %!@(MISSING), but server have different auth tag %!@(MISSING), ignoring"
+ "ForceAuthTag default is set, and server have matching auth tag, continue"
+ "ForceAuthTag default is set, but server don't have auth tag, ignoring"
+ "OVERALL_RESULT_FAILURE_CONNECTED_TO_ANOTHER"
+ "RecoverDeviceUI ViewDidDissapear"
+ "T@\"NSTimer\",&,N,V_setupTimer"
+ "_setupTimer"
+ "addTimer:forMode:"
+ "dataUsingEncoding:"
+ "done waiting for server response"
+ "doneWaitingForServerResponse"
+ "mainRunLoop"
+ "nearbyAuthTag"
+ "setSetupTimer:"
+ "setupTimer"
+ "setupkitClient exist. Invalidating client"
+ "stringForKey:"
+ "timed out waiting for server response"
+ "timerWithTimeInterval:repeats:block:"
+ "v16@?0@\"NSTimer\"8"
+ "waitForServerResponse"
+ "will wait for server response"
- "\x1f\x05\x11"
- "OVERALL_RESULT_FAILURE_CONNECTED_TO_ANOTHER_DEVICE_TYPE_ATV"
- "RecoverDeviceUI ViewDidDissapear. Invalidating client"

```
