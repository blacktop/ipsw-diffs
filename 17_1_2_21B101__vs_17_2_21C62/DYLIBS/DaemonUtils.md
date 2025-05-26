## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0xb1a0
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0xe9c
+1394.62.1.0.0
+  __TEXT.__text: 0xb424
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0xeec
   __TEXT.__const: 0xe0
   __TEXT.__cstring: 0xca8
   __TEXT.__oslogstring: 0xa0e
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methname: 0x29d8
-  __TEXT.__objc_methtype: 0x590
-  __TEXT.__objc_stubs: 0x2180
+  __TEXT.__unwind_info: 0x44c
+  __TEXT.__objc_classname: 0x234
+  __TEXT.__objc_methname: 0x2ae6
+  __TEXT.__objc_methtype: 0x5bc
+  __TEXT.__objc_stubs: 0x21e0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ad0
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_const: 0x1ef8
+  __DATA_CONST.__objc_selrefs: 0xb28
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__cfstring: 0xcc0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__objc_const: 0x8f8
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH.__objc_data: 0x190
   __DATA.__objc_classrefs: 0x150
   __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x13c
-  __DATA.__data: 0x120
+  __DATA.__objc_ivar: 0x144
+  __DATA.__data: 0x180
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x128

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 380
-  Symbols:   1537
-  CStrings:  850
+  Functions: 387
+  Symbols:   1569
+  CStrings:  866
 
Symbols:
+ +[DaemonUtils callerIdWithPid:auditToken:]
+ -[Caller processId]
+ -[EvaluationRequest evaluationUserId]
+ -[EvaluationRequest performAsyncUpdatesWithCompletion:]
+ -[Request performAsyncUpdatesWithCompletion:]
+ -[Request serviceLocator]
+ -[Request setServiceLocator:]
+ _OBJC_IVAR_$_EvaluationRequest._evaluationUserId
+ _OBJC_IVAR_$_Request._serviceLocator
+ __OBJC_$_PROP_LIST_LACXPCClientInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACXPCClientInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACXPCClientInfo
+ __OBJC_$_PROTOCOL_REFS_LACXPCClientInfo
+ __OBJC_CLASS_PROTOCOLS_$_Caller
+ __OBJC_LABEL_PROTOCOL_$_LACXPCClientInfo
+ __OBJC_PROTOCOL_$_LACXPCClientInfo
+ ___block_literal_global.21
+ ___block_literal_global.26
+ ___block_literal_global.31
+ ___block_literal_global.36
+ ___block_literal_global.41
+ ___block_literal_global.82
+ ___block_literal_global.84
+ _dispatch_assert_queue$V2
+ _objc_msgSend$binaryNameForPid:
+ _objc_msgSend$callerDisplayNameWithPid:auditToken:bundleId:
+ _objc_msgSend$isClarityBoardRunning
+ _objc_unsafeClaimAutoreleasedReturnValue
- ___block_literal_global.20
- ___block_literal_global.25
- ___block_literal_global.30
- ___block_literal_global.35
- ___block_literal_global.78
- ___block_literal_global.80
CStrings:
+ "\x02\x14"
+ "@\"<LACServiceLocator>\""
+ "@52@0:8i16{?=[8I]}20"
+ "LACXPCClientInfo"
+ "T@\"<LACServiceLocator>\",&,N,V_serviceLocator"
+ "TI,R,N,V_evaluationUserId"
+ "Ti,R,N"
+ "T{?=[8I]},R,N"
+ "_evaluationUserId"
+ "_serviceLocator"
+ "callerIdWithPid:auditToken:"
+ "evaluationUserId"
+ "isClarityBoardRunning"
+ "performAsyncUpdatesWithCompletion:"
+ "processId"
+ "serviceLocator"
+ "setServiceLocator:"
- "\x02\x13"

```
