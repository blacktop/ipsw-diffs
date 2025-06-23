## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-196.0.0.0.0
-  __TEXT.__text: 0x6f540
+198.0.0.0.0
+  __TEXT.__text: 0x6faa0
   __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x69e4
+  __TEXT.__objc_methlist: 0x6a2c
   __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x518c
+  __TEXT.__cstring: 0x520e
   __TEXT.__gcc_except_tab: 0x1da8
-  __TEXT.__oslogstring: 0x8566
+  __TEXT.__oslogstring: 0x84e0
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__unwind_info: 0x1a88
   __TEXT.__objc_classname: 0x88f
-  __TEXT.__objc_methname: 0xedc2
-  __TEXT.__objc_methtype: 0x235b
-  __TEXT.__objc_stubs: 0xbd00
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0x2020
+  __TEXT.__objc_methname: 0xee31
+  __TEXT.__objc_methtype: 0x234d
+  __TEXT.__objc_stubs: 0xbd20
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x2058
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3908
+  __DATA_CONST.__objc_selrefs: 0x3918
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0xc00
-  __AUTH_CONST.__cfstring: 0x4c20
-  __AUTH_CONST.__objc_const: 0x12830
+  __AUTH_CONST.__cfstring: 0x4c80
+  __AUTH_CONST.__objc_const: 0x12890
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x330
+  __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x5ac
+  __DATA.__objc_ivar: 0x5a8
   __DATA.__data: 0xa40
   __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x8c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB201520-68DD-3BA4-AA4E-B9779FE04427
-  Functions: 2711
-  Symbols:   9468
-  CStrings:  5087
+  UUID: 38944CD7-7B18-342D-956C-8DC584C880B1
+  Functions: 2718
+  Symbols:   9483
+  CStrings:  5093
 
Symbols:
+ -[DEDBugSession didFinishUploadingWithError:]
+ -[DEDIDSInbound upload_finished:service:account:fromID:context:]
+ -[DEDIDSInbound upload_finished:service:account:fromID:context:].cold.1
+ -[DEDIDSOutbound didFinishUploadingWithError:sessionID:]
+ -[DEDLocalTransport didFinishUploadingWithError:sessionID:]
+ -[DEDSharingOutbound didFinishUploadingWithError:sessionID:]
+ -[DEDXPCInbound xpc_didFinishUploadingWithError:sessionID:]
+ -[DEDXPCOutbound didFinishUploadingWithError:sessionID:]
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table121
+ GCC_except_table75
+ GCC_except_table86
+ GCC_except_table96
+ _DEDCapabilityUploadErrorHandling
+ ___45-[DEDBugSession didFinishUploadingWithError:]_block_invoke
+ ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke.112
+ ___56-[DEDBugSession ongoingCollectOperationsWithOperations:]_block_invoke.139
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.138
+ ___block_literal_global.143
+ ___block_literal_global.201
+ ___block_literal_global.282
+ ___block_literal_global.286
+ _objc_msgSend$bugSession:didFinishUploadingWithError:
+ _objc_msgSend$didFinishUploadingWithError:
+ _objc_msgSend$didFinishUploadingWithError:sessionID:
+ _objc_msgSend$xpc_didFinishUploadingWithError:sessionID:
- -[DEDCloudKitFinisher elsManager]
- -[DEDCloudKitFinisher setElsManager:]
- GCC_except_table104
- GCC_except_table113
- GCC_except_table114
- GCC_except_table119
- GCC_except_table193
- GCC_except_table73
- GCC_except_table77
- GCC_except_table83
- _ELSEventTypeSessionCleanup
- _OBJC_IVAR_$_DEDCloudKitFinisher._elsManager
- ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke.105
- ___56-[DEDBugSession ongoingCollectOperationsWithOperations:]_block_invoke.137
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.199
- ___block_literal_global.281
- ___block_literal_global.285
- _objc_msgSend$elsManager
- _objc_msgSend$finishWithFailure
- _objc_msgSend$setElsManager:
CStrings:
+ "LOAD_EXTENSION_TEXT_DATA"
+ "UPLOAD_FINISHED"
+ "bugSession:didFinishUploadingWithError:"
+ "com.apple.diagnosticextensionsd.DEDCloudKitFinisher"
+ "didFinishUploadingWithError:"
+ "didFinishUploadingWithError:sessionID:"
+ "upload-error-handling"
+ "upload_finished on session [%{public}@]"
+ "upload_finished:service:account:fromID:context:"
+ "xpc_didFinishUploadingWithError:sessionID:"
- "@\"ELSManager\""
- "T@\"ELSManager\",&,N,V_elsManager"
- "_elsManager"
- "elsManager"
- "finishWithFailure"
- "setElsManager:"
- "uploadDelegate is nil in session [%{public}@]. Cannot send update"
- "uploadDelegate is nil or doesn't respond to compressionProgress in session [%{public}@]. Cannot send update"

```
