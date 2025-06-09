## IdleTimerServices

> `/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices`

```diff

-37.4.1.0.0
-  __TEXT.__text: 0x3fa8
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x69c
+39.0.0.0.0
+  __TEXT.__text: 0x4d9c
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x714
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x337
+  __TEXT.__cstring: 0x33b
   __TEXT.__oslogstring: 0x57a
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_classname: 0x1bf
-  __TEXT.__objc_methname: 0x1041
-  __TEXT.__objc_methtype: 0x5c0
-  __TEXT.__objc_stubs: 0xd00
+  __TEXT.__objc_methname: 0x12cb
+  __TEXT.__objc_methtype: 0x6ea
+  __TEXT.__objc_stubs: 0xe20
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1e8
+  __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x1960
+  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__objc_const: 0x1998
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x3c8
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C38A47FA-679A-34CB-A720-682AD25EC82E
-  Functions: 118
-  Symbols:   623
-  CStrings:  340
+  UUID: F8555A74-918E-3F9F-86D1-54C6044B369C
+  Functions: 132
+  Symbols:   670
+  CStrings:  360
 
Symbols:
+ -[ITIdleTimerState newAssertionToDisableIdleTimerOnBehalfOfSceneWithPID:forReason:error:]
+ -[ITIdleTimerState newAssertionToDisableIdleTimerOnBehalfOfSceneWithPID:forReason:error:].cold.1
+ -[ITIdleTimerState newAssertionToDisableIdleTimerOnBehalfOfSceneWithPID:forReason:error:].cold.2
+ -[ITIdleTimerState newAssertionToDisableIdleTimerOnBehalfOfSceneWithPID:forReason:error:].cold.3
+ -[ITIdleTimerStateClient _access_addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:]
+ -[ITIdleTimerStateClient _access_addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:].cold.1
+ -[ITIdleTimerStateClient addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:]
+ -[ITIdleTimerStateModel _access_newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:]
+ -[ITIdleTimerStateModel _access_newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:].cold.1
+ -[ITIdleTimerStateModel newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:]
+ -[ITIdleTimerStateModel newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:].cold.1
+ -[ITIdleTimerStateServer addIdleTimerServiceOnBehalfOfSceneWithPID:withConfiguration:forReason:error:]
+ -[ITIdleTimerStateService addIdleTimerOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:]
+ GCC_except_table10
+ GCC_except_table11
+ ___111-[ITIdleTimerStateModel _access_newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:]_block_invoke
+ ___43-[ITIdleTimerStateClient initWithDelegate:]_block_invoke.59
+ ___43-[ITIdleTimerStateClient initWithDelegate:]_block_invoke.59.cold.1
+ ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.65
+ ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.65.cold.1
+ ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.67
+ ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.67.cold.1
+ _objc_msgSend$_access_addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:
+ _objc_msgSend$_access_newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:
+ _objc_msgSend$acquireIdleTimerAssertionOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:
+ _objc_msgSend$addIdleTimerOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:
+ _objc_msgSend$addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:
+ _objc_msgSend$addIdleTimerServiceOnBehalfOfSceneWithPID:withConfiguration:forReason:error:
+ _objc_msgSend$intValue
+ _objc_msgSend$newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:
+ _objc_msgSend$numberWithInt:
+ _objc_opt_respondsToSelector
+ _objc_retain_x4
- GCC_except_table7
- GCC_except_table9
- ___43-[ITIdleTimerStateClient initWithDelegate:]_block_invoke.56
- ___43-[ITIdleTimerStateClient initWithDelegate:]_block_invoke.56.cold.1
- ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.62
- ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.62.cold.1
- ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.64
- ___68-[ITIdleTimerStateServer listener:didReceiveConnection:withContext:]_block_invoke.64.cold.1
CStrings:
+ "@36@0:8i16@20^@28"
+ "@44@0:8i16@20@28^@36"
+ "B44@0:8i16@\"BSProcessHandle\"20@\"ITIdleTimerConfiguration\"28@\"NSString\"36"
+ "B44@0:8i16@20@28@36"
+ "_access_addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
+ "_access_newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
+ "acquireIdleTimerAssertionOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:"
+ "addIdleTimerOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:"
+ "addIdleTimerOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
+ "addIdleTimerServiceOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
+ "intValue"
+ "newAssertionToDisableIdleTimerOnBehalfOfSceneWithPID:forReason:error:"
+ "newIdleTimerAssertionOnBehalfOfSceneWithPID:withConfiguration:forReason:error:"
+ "numberWithInt:"
+ "v44@0:8i16@\"ITIdleTimerConfiguration\"20@\"NSString\"28^@36"
+ "v44@0:8i16@20@28^@36"
+ "v48@0:8@\"NSNumber\"16@\"ITIdleTimerConfiguration\"24@\"NSString\"32^@40"
+ "v48@0:8@16@24@32^@40"

```
