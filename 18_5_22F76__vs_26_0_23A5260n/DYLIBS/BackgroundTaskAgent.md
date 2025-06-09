## BackgroundTaskAgent

> `/System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x8ec
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x40b
-  __TEXT.__oslogstring: 0x21d
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xd8
+63.0.0.0.0
+  __TEXT.__text: 0x504
+  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__cstring: 0x39d
+  __TEXT.__oslogstring: 0x13f
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0x68
   __AUTH_CONST.__const: 0x20
   __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 20FF05F3-3EFB-3B64-BAEC-274686B2CD79
-  Functions: 23
-  Symbols:   100
-  CStrings:  40
+  UUID: 5859C923-7BB2-3B6D-ADD7-5C26277953EA
+  Functions: 19
+  Symbols:   72
+  CStrings:  33
 
Symbols:
- __NSConcreteStackBlock
- ___BackgroundTaskAgentInit_block_invoke
- ___BackgroundTaskAgentInit_block_invoke.cold.1
- ___BackgroundTaskAgentInit_block_invoke.cold.2
- ___BackgroundTaskAgentInit_block_invoke.cold.3
- ___block_descriptor_40_e8_32b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___stack_chk_fail
- ___stack_chk_guard
- __xpc_error_key_description
- __xpc_event_key_name
- __xpc_type_error
- __xpc_type_string
- _free
- _malloc_type_malloc
- _strcpy
- _strlen
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_int64
- _xpc_dictionary_get_string
- _xpc_dictionary_get_value
- _xpc_dictionary_set_value
- _xpc_retain
- _xpc_set_event_stream_handler
- _xpc_string_get_string_ptr
CStrings:
+ "BackgroundTaskAgent no longer supported"
- "BackgroundTaskAgent XPC Event Handler - Error: %s"
- "BackgroundTaskAgent XPC Event Handler - Event Type = XPC_TYPE_DICTIONARY, Not a BACKGROUND_TASK_AGENT_MESSAGE"
- "BackgroundTaskAgent XPC Event Handler: Unknown Event Type"
- "BackgroundTaskAgentInit"
- "BackgroundTaskAgentInit: clientName is NULL"
- "BackgroundTaskAgentMessage"
- "clientName != ((void*)0)"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"

```
