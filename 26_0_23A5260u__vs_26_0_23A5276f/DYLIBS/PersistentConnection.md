## PersistentConnection

> `/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`

```diff

-556.100.1.0.0
-  __TEXT.__text: 0x23988
+557.100.1.0.0
+  __TEXT.__text: 0x23b1c
   __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0x1fa8
   __TEXT.__const: 0x250
-  __TEXT.__gcc_except_tab: 0xe60
+  __TEXT.__gcc_except_tab: 0xf10
   __TEXT.__cstring: 0x1b8e
-  __TEXT.__oslogstring: 0x4b5f
-  __TEXT.__unwind_info: 0xb90
+  __TEXT.__oslogstring: 0x4b89
+  __TEXT.__unwind_info: 0xbb0
   __TEXT.__objc_classname: 0x321
-  __TEXT.__objc_methname: 0x49ec
+  __TEXT.__objc_methname: 0x49fe
   __TEXT.__objc_methtype: 0x1071
-  __TEXT.__objc_stubs: 0x3200
+  __TEXT.__objc_stubs: 0x3220
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6a0
+  __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8EAFC94-5241-3ED1-B8FA-1DC0151E13E5
+  UUID: BBEC1475-91CE-326E-B33F-0DC8C63B9782
   Functions: 769
-  Symbols:   2999
-  CStrings:  1689
+  Symbols:   3005
+  CStrings:  1690
 
Symbols:
+ -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:]
+ -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:].cold.1
+ GCC_except_table34
+ GCC_except_table55
+ GCC_except_table94
+ GCC_except_table95
+ ___76-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:]_block_invoke
+ ___76-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:]_block_invoke_2
+ ___76-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:]_block_invoke_2.cold.1
+ ___block_descriptor_65_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ __saveWWANKeepAliveIntervalWithInfo:resetStateMachine:.pred
+ __saveWWANKeepAliveIntervalWithInfo:resetStateMachine:.queue
+ _objc_msgSend$_saveWWANKeepAliveIntervalWithInfo:resetStateMachine:
+ _objc_msgSend$resetKeepAliveStateMachineIfNecessary
- -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]
- -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:].cold.1
- ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke
- ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke_2
- ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke_2.cold.1
- __saveWWANKeepAliveIntervalWithInfo:.pred
- __saveWWANKeepAliveIntervalWithInfo:.queue
- _objc_msgSend$_saveWWANKeepAliveIntervalWithInfo:
Functions:
~ -[PCConnectionManager resumeManagerWithAction:forceGrow:] : 2400 -> 2412
~ -[PCConnectionManager resetKeepAliveStateMachineIfNecessary] : 352 -> 536
~ -[PCConnectionManager saveKeepAliveInterval:isInitialGrowth:] : 248 -> 252
~ -[PCConnectionManager setKeepAliveOverrideOnInterface:interval:timeout:] : 408 -> 440
~ -[PCConnectionManager _saveWWANKeepAliveInterval] : 96 -> 144
~ -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:] -> -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:] : 336 -> 428
~ ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke_2 -> ___76-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:resetStateMachine:]_block_invoke_2 : 428 -> 460
CStrings:
+ "Re-creating state machine %@ with info %@"
+ "_saveWWANKeepAliveIntervalWithInfo:resetStateMachine:"
- "_saveWWANKeepAliveIntervalWithInfo:"

```
