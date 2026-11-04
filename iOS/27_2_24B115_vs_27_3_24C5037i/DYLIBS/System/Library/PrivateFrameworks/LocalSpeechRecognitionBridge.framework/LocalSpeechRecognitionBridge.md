## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

```diff

-3605.32.1.0.0
-  __TEXT.__text: 0x1da44
-  __TEXT.__objc_methlist: 0x25a4
+3610.11.1.0.0
+  __TEXT.__text: 0x1ee24
+  __TEXT.__objc_methlist: 0x2684
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x4c65
-  __TEXT.__oslogstring: 0x2eb9
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__cstring: 0x4ec4
+  __TEXT.__oslogstring: 0x3162
+  __TEXT.__unwind_info: 0x988
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x870
-  __DATA_CONST.__objc_classlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__const: 0x968
+  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13b0
-  __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x1e8
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x3e28
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x1be0
+  __AUTH_CONST.__objc_const: 0x3fc8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x2dc
-  __DATA.__data: 0x8b0
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x2e8
+  __DATA.__data: 0x970
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 754
-  Symbols:   1499
-  CStrings:  626
+  Functions: 780
+  Symbols:   1553
+  CStrings:  650
 
Symbols:
+ -[LBRequestMutexClient .cxx_destruct]
+ -[LBRequestMutexClient _connection]
+ -[LBRequestMutexClient _dropConnection]
+ -[LBRequestMutexClient _invalidate]
+ -[LBRequestMutexClient _serviceWithErrorHandler:]
+ -[LBRequestMutexClient _tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]
+ -[LBRequestMutexClient dealloc]
+ -[LBRequestMutexClient init]
+ -[LBRequestMutexClient invalidate]
+ -[LBRequestMutexClient releaseCSRequestMutex:requestId:resourceType:]
+ -[LBRequestMutexClient requestMutexOwnershipChanged:]
+ -[LBRequestMutexClient setDelegate:]
+ -[LBRequestMutexClient tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]
+ GCC_except_table759
+ GCC_except_table768
+ _LBRequestMutexServiceDelegateGetXPCInterface
+ _LBRequestMutexServiceGetXPCInterface
+ _LBRequestMutexServiceName
+ _OBJC_CLASS_$_LBRequestMutexClient
+ _OBJC_IVAR_$_LBRequestMutexClient._delegate
+ _OBJC_IVAR_$_LBRequestMutexClient._queue
+ _OBJC_IVAR_$_LBRequestMutexClient._xpcConnection
+ _OBJC_METACLASS_$_LBRequestMutexClient
+ __OBJC_$_INSTANCE_METHODS_LBRequestMutexClient
+ __OBJC_$_INSTANCE_VARIABLES_LBRequestMutexClient
+ __OBJC_$_PROP_LIST_LBRequestMutexClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBRequestMutexService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBRequestMutexServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBRequestMutexService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBRequestMutexServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_LBRequestMutexService
+ __OBJC_$_PROTOCOL_REFS_LBRequestMutexServiceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_LBRequestMutexClient
+ __OBJC_CLASS_RO_$_LBRequestMutexClient
+ __OBJC_LABEL_PROTOCOL_$_LBRequestMutexService
+ __OBJC_LABEL_PROTOCOL_$_LBRequestMutexServiceDelegate
+ __OBJC_METACLASS_RO_$_LBRequestMutexClient
+ __OBJC_PROTOCOL_$_LBRequestMutexService
+ __OBJC_PROTOCOL_$_LBRequestMutexServiceDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_LBRequestMutexService
+ __OBJC_PROTOCOL_REFERENCE_$_LBRequestMutexServiceDelegate
+ ___100-[LBRequestMutexClient tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]_block_invoke
+ ___101-[LBRequestMutexClient _tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]_block_invoke
+ ___101-[LBRequestMutexClient _tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]_block_invoke_2
+ ___34-[LBRequestMutexClient invalidate]_block_invoke
+ ___35-[LBRequestMutexClient _connection]_block_invoke
+ ___36-[LBRequestMutexClient setDelegate:]_block_invoke
+ ___69-[LBRequestMutexClient releaseCSRequestMutex:requestId:resourceType:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e20_v20?0B8"NSError"12ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_73_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
CStrings:
+ "!"
+ "%s #mutex XPC error releasing ownership : %{public}@"
+ "%s #mutex XPC error reserving ownership : %{public}@"
+ "%s #mutex creating new xpc connection..."
+ "%s #mutex invalidating connection"
+ "%s #mutex listening for ownership changes"
+ "%s #mutex ownership changed to %lu"
+ "%s #mutex releasing ownership is a no-op, no connection"
+ "%s #mutex releasing ownership, isCompanionRequest : %d, requestId : %@"
+ "%s #mutex reservation success : %d, error : %{public}@"
+ "%s #mutex reserving ownership, isCompanionRequest : %d, requestId : %@, holdTimeInMillis : %ld"
+ "%s #mutex stopped listening for ownership changes"
+ "%s #mutex xpc connection %{public}@ interrupted"
+ "%s #mutex xpc connection %{public}@ invalidated"
+ "-[LBRequestMutexClient _connection]"
+ "-[LBRequestMutexClient _connection]_block_invoke"
+ "-[LBRequestMutexClient _invalidate]"
+ "-[LBRequestMutexClient _tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]"
+ "-[LBRequestMutexClient _tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]_block_invoke_2"
+ "-[LBRequestMutexClient releaseCSRequestMutex:requestId:resourceType:]_block_invoke"
+ "-[LBRequestMutexClient requestMutexOwnershipChanged:]"
+ "-[LBRequestMutexClient setDelegate:]_block_invoke"
+ "LBRequestMutexClient Queue"
+ "com.apple.siri.request.ownership.mutex.service.xpc"
```
