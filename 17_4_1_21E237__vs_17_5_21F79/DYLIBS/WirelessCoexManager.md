## WirelessCoexManager

> `/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager`

```diff

-1630.4.8.0.0
-  __TEXT.__text: 0x7a54
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__const: 0x88
+1630.5.2.0.0
+  __TEXT.__text: 0x8380
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x604
+  __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x16e8
-  __TEXT.__unwind_info: 0x21c
+  __TEXT.__cstring: 0x1832
+  __TEXT.__unwind_info: 0x244
   __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x1021
-  __TEXT.__objc_methtype: 0x212
-  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methname: 0x10a7
+  __TEXT.__objc_methtype: 0x23a
+  __TEXT.__objc_stubs: 0x940
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x5c8
+  __DATA_CONST.__const: 0x640
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xaa8
-  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_const: 0xac8
+  __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_classrefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__cfstring: 0xc40
+  __AUTH_CONST.__cfstring: 0xd00
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x2a8
-  __DATA.__objc_ivar: 0xe0
+  __AUTH_CONST.__auth_got: 0x2e0
+  __DATA.__objc_ivar: 0xe4
   __DATA.__data: 0x30
   __DATA_DIRTY.__objc_const: 0x240
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 163
-  Symbols:   626
-  CStrings:  448
+  Functions: 173
+  Symbols:   661
+  CStrings:  468
 
Symbols:
+ -[WRM_UCMInterface getInstantLoad]
+ -[WRM_UCMInterface getWirelessRadioManagerReportLoad:loadDuration:callback:]
+ -[WRM_UCMInterface sendBtLoad:]
+ -[WRM_UCMInterface startTimer:]
+ -[WRM_UCMInterface stopTimer]
+ _OBJC_IVAR_$_WRM_UCMInterface.mHomeKitBTLoadFunctionPointer
+ __Block_object_dispose
+ ___29-[WRM_UCMInterface stopTimer]_block_invoke
+ ___31-[WRM_UCMInterface sendBtLoad:]_block_invoke
+ ___31-[WRM_UCMInterface startTimer:]_block_invoke
+ ___34-[WRM_UCMInterface getInstantLoad]_block_invoke
+ ___34-[WRM_UCMInterface getInstantLoad]_block_invoke_2
+ ___block_descriptor_48_e8_32s40r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_msgSend$getInstantLoad
+ _objc_msgSend$sendBtLoad:
+ _objc_msgSend$startTimer:
+ _objc_msgSend$stopTimer
+ _objc_retain_x9
+ _xpc_dictionary_set_double
CStrings:
+ "\x02!\x11"
+ "Duration is not Valid"
+ "I16@0:8"
+ "Received getWirelessRadioManagerReportLoad"
+ "WRMHomeKit"
+ "^?"
+ "getInstantLoad"
+ "getWirelessRadioManagerReportLoad Current BT Load: %u"
+ "getWirelessRadioManagerReportLoad Sending BtLoad: %u"
+ "getWirelessRadioManagerReportLoad Stop Timer"
+ "getWirelessRadioManagerReportLoad start Timer"
+ "getWirelessRadioManagerReportLoad:loadDuration:callback:"
+ "kWRMHomeKitBtLoad"
+ "kWRMHomeKitDuration"
+ "kWRMHomeKitEnable"
+ "mHomeKitBTLoadFunctionPointer"
+ "q36@0:8i16d20^?28"
+ "sendBtLoad:"
+ "startTimer:"
+ "stopTimer"
+ "v24@0:8d16"
- "\x02\x11\x11"

```
