## WirelessCoexManager

> `/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager`

```diff

-1740.5.1.0.0
-  __TEXT.__text: 0x9584
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x640
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__cstring: 0x1aa4
-  __TEXT.__unwind_info: 0x2b0
+1828.0.0.0.0
+  __TEXT.__text: 0xa51c
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x668
+  __TEXT.__const: 0xb8
+  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__cstring: 0x188f
+  __TEXT.__oslogstring: 0x434
+  __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x1192
-  __TEXT.__objc_methtype: 0x25d
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x6d8
+  __TEXT.__objc_methname: 0x1211
+  __TEXT.__objc_methtype: 0x26c
+  __TEXT.__objc_stubs: 0xa20
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f0
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0xd48
+  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__cfstring: 0xcc0
+  __AUTH_CONST.__objc_const: 0xd88
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0xec
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x30
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70122166-BE73-3B74-859D-C3E19428C260
-  Functions: 186
-  Symbols:   708
-  CStrings:  619
+  UUID: 3A1386E1-F7BF-3FF6-9600-B01552D4C82B
+  Functions: 198
+  Symbols:   743
+  CStrings:  622
 
Symbols:
+ -[WRM_UCMInterface checkConnection:].cold.1
+ -[WRM_UCMInterface checkConnection:].cold.2
+ -[WRM_UCMInterface checkConnection:].cold.3
+ -[WRM_iRATInterface getVoiceLqmValue:completionHandler:]
+ -[WRM_iRATInterface processVoiceLqmNotification:]
+ -[WRM_iRATInterface subscribeVoiceLqmNotification:]
+ GCC_except_table20
+ GCC_except_table28
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table49
+ GCC_except_table54
+ _OBJC_IVAR_$_WRM_iRATInterface.mVoiceLqmCb
+ _OBJC_IVAR_$_WRM_iRATInterface.mVoiceLqmCbEnabled
+ _OUTLINED_FUNCTION_0
+ ___29-[WRM_UCMInterface stopTimer]_block_invoke.85
+ ___31-[WRM_UCMInterface startTimer:]_block_invoke.88
+ ___34-[WRM_UCMInterface getInstantLoad]_block_invoke.82
+ ___41-[WRM_UCMInterface registerClient:queue:]_block_invoke_2.cold.1
+ ___49-[WRM_iRATInterface processVoiceLqmNotification:]_block_invoke
+ ___51-[WRM_iRATInterface subscribeVoiceLqmNotification:]_block_invoke
+ ___56-[WRM_iRATInterface getVoiceLqmValue:completionHandler:]_block_invoke
+ ___56-[WRM_iRATInterface getVoiceLqmValue:completionHandler:]_block_invoke_2
+ ___58-[WRM_UCMInterface getWirelessFrequencyBandUpdatesForMIC:]_block_invoke.98
+ ___block_descriptor_48_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ __os_log_default
+ __os_log_error_impl
+ __os_log_impl
+ _objc_msgSend$processVoiceLqmNotification:
+ _objc_msgSend$subscribeVoiceLqmNotification:
+ _os_log_type_enabled
- GCC_except_table18
- GCC_except_table36
- GCC_except_table39
- GCC_except_table42
- GCC_except_table47
- ___29-[WRM_UCMInterface stopTimer]_block_invoke_2
- ___31-[WRM_UCMInterface startTimer:]_block_invoke_2
- ___34-[WRM_UCMInterface getInstantLoad]_block_invoke_2
- ___58-[WRM_UCMInterface getWirelessFrequencyBandUpdatesForMIC:]_block_invoke_2
CStrings:
+ "Inovoke mVoiceLqmCb slotId=%lu, vLqm=%d"
+ "Invoking reConnect %@"
+ "No voiceLQM callback registered"
+ "Received getVoiceLqmValue from %s, simSlot=%ld"
+ "Received subscribeVoiceLqmNotification from %s"
+ "XPC message sent: subscribeVoiceLqmNotification"
+ "getVoiceLqmValue error: Invalid XPC Connection"
+ "getVoiceLqmValue invalid completionHandler"
+ "getVoiceLqmValue invalid response, return UnKnown LQM"
+ "getVoiceLqmValue response : simSlot=%ld, vLQM=%d"
+ "getVoiceLqmValue:completionHandler:"
+ "kWRMVoiceLqmValue"
+ "kWRMVoiceLqm_SlotId"
+ "mVoiceLqmCb"
+ "mVoiceLqmCbEnabled"
+ "processVoiceLqmNotification:"
+ "subscribeVoiceLqmNotification error: Invalid XPC Connection"
+ "subscribeVoiceLqmNotification:"
+ "v32@0:8q16@?24"
- "Received unknown message:%@"

```
