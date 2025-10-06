## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-1439.40.24.0.0
-  __TEXT.__text: 0x5b28
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x7e4
+1439.60.20.0.1
+  __TEXT.__text: 0x6070
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0x824
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__cstring: 0x550
-  __TEXT.__oslogstring: 0x7ec
-  __TEXT.__unwind_info: 0x184
-  __TEXT.__objc_classname: 0xec
-  __TEXT.__objc_methname: 0x1ab4
-  __TEXT.__objc_methtype: 0x242
-  __TEXT.__objc_stubs: 0x11c0
+  __TEXT.__oslogstring: 0x911
+  __TEXT.__unwind_info: 0x194
+  __TEXT.__objc_classname: 0xed
+  __TEXT.__objc_methname: 0x1bf6
+  __TEXT.__objc_methtype: 0x287
+  __TEXT.__objc_stubs: 0x1240
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x218
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xef0
-  __DATA_CONST.__objc_selrefs: 0x548
+  __DATA_CONST.__objc_const: 0xf50
+  __DATA_CONST.__objc_selrefs: 0x570
   __AUTH_CONST.__objc_const: 0x318
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__cfstring: 0x7e0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x2b8
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_classrefs: 0x60
   __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 189DC29C-09C8-31FC-ABB0-87F88E54FD8F
-  Functions: 209
-  Symbols:   818
-  CStrings:  521
+  UUID: 25A9B874-303F-3FE1-846D-78814526FE2F
+  Functions: 222
+  Symbols:   856
+  CStrings:  538
 
Symbols:
+ -[BGSystemTaskRequest networkEndpointPrimitive]
+ -[BGSystemTaskRequest networkParametersPrimitive]
+ -[BGSystemTaskRequest setNetworkEndpointPrimitive:]
+ -[BGSystemTaskRequest setNetworkParametersPrimitive:]
+ -[BGSystemTaskScheduler deregisterTaskWithIdentifier:]
+ GCC_except_table38
+ _OBJC_IVAR_$_BGSystemTaskRequest._networkEndpointPrimitive
+ _OBJC_IVAR_$_BGSystemTaskRequest._networkParametersPrimitive
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_9
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.cold.1
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.cold.2
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.cold.3
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.cold.4
+ _nw_endpoint_copy_dictionary
+ _nw_endpoint_create_from_dictionary
+ _nw_parameters_copy_dictionary
+ _nw_parameters_create_from_dictionary
+ _objc_msgSend$networkEndpointPrimitive
+ _objc_msgSend$networkParametersPrimitive
+ _objc_msgSend$setNetworkEndpointPrimitive:
+ _objc_msgSend$setNetworkParametersPrimitive:
+ _xpc_dictionary_set_value
CStrings:
+ "@\"NSObject<OS_nw_endpoint>\""
+ "@\"NSObject<OS_nw_parameters>\""
+ "AQ$2"
+ "B24@0:8@16"
+ "T@\"NSObject<OS_nw_endpoint>\",&,N,V_networkEndpointPrimitive"
+ "T@\"NSObject<OS_nw_parameters>\",&,N,V_networkParametersPrimitive"
+ "_networkEndpointPrimitive"
+ "_networkParametersPrimitive"
+ "deregisterTaskWithIdentifier:"
+ "deregisterTaskWithIdentifier: %{public}@"
+ "deregisterTaskWithIdentifier: Deregister is not supported for task %{public}@ since its already running"
+ "deregisterTaskWithIdentifier: Deregistering task %{public}@"
+ "deregisterTaskWithIdentifier: No registration found for task with identifier %{public}@"
+ "networkEndpointPrimitive"
+ "networkParametersPrimitive"
+ "setNetworkEndpointPrimitive:"
+ "setNetworkParametersPrimitive:"
- "AQ$"

```
