## accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

-1338.0.37.0.0
-  __TEXT.__text: 0x51bf8
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_stubs: 0x73c0
-  __TEXT.__objc_methlist: 0x3c0c
+1338.0.46.502.1
+  __TEXT.__text: 0x52e60
+  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__objc_stubs: 0x7420
+  __TEXT.__objc_methlist: 0x3c24
   __TEXT.__const: 0x400
-  __TEXT.__objc_methname: 0x9259
-  __TEXT.__cstring: 0x8474
+  __TEXT.__objc_methname: 0x927c
+  __TEXT.__cstring: 0x8537
   __TEXT.__objc_classname: 0x69e
   __TEXT.__objc_methtype: 0x1b3a
-  __TEXT.__oslogstring: 0x66d8
+  __TEXT.__oslogstring: 0x6a29
   __TEXT.__gcc_except_tab: 0x57c
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x12b0
-  __DATA_CONST.__auth_got: 0x880
-  __DATA_CONST.__got: 0x3c8
+  __TEXT.__unwind_info: 0x12c0
+  __DATA_CONST.__auth_got: 0x8d8
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x17a0
-  __DATA_CONST.__cfstring: 0x5820
+  __DATA_CONST.__cfstring: 0x5880
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x9428
-  __DATA.__objc_selrefs: 0x2380
-  __DATA.__objc_ivar: 0x554
+  __DATA.__objc_const: 0x9448
+  __DATA.__objc_selrefs: 0x2390
+  __DATA.__objc_ivar: 0x558
   __DATA.__objc_data: 0xf00
   __DATA.__data: 0xb45
   __DATA.__bss: 0x1230

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBEF9196-D913-3173-A0EA-22324ED93600
-  Functions: 2113
-  Symbols:   403
-  CStrings:  4341
+  UUID: 50516CF1-B085-3B9D-AA20-BFE049390254
+  Functions: 2135
+  Symbols:   418
+  CStrings:  4378
 
Symbols:
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_type_connection
+ __xpc_type_dictionary
+ _addObjectToXpcDictionary
+ _clientHasEntitlement
+ _sendReplyMessageToExternalClient
+ _xpc_connection_create_mach_service
+ _xpc_connection_resume
+ _xpc_connection_set_context
+ _xpc_connection_set_event_handler
+ _xpc_connection_set_target_queue
+ _xpc_copy_description
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_audit_token
CStrings:
+ "Cannot handle API event with NULL client identifier"
+ "Cannot handle NULL XPC message"
+ "Cannot process NULL XPC Event"
+ "Client connection lost"
+ "ClientIdentifier"
+ "ClientRegistrationName"
+ "Command"
+ "Current plugin list is: %@"
+ "Empty Partner Serial Numbers for accessory %{public}@"
+ "Error: %@ has invalid options dictionary for eventType = %llu, pluginName = %@"
+ "Error: %@ has invalid options key %@"
+ "Error: %@ has invalid value for key %@"
+ "Error: Client is not entitled"
+ "Event received %s"
+ "Failed to create earlyInstance"
+ "Failed to create fud xpc listener"
+ "FilterIdentifier"
+ "Fud got an API event"
+ "Handle event: %@, eventType = %llu, pluginName = %@, options = %@"
+ "Ignoring unexpected xpc msg type"
+ "Invalid XPC options type"
+ "Invalid object type, expecting a XPC connection"
+ "Kicking off FUDGenericKextUpdater Plugin earlyboot path"
+ "New API Event"
+ "New external client event"
+ "PluginsList"
+ "Response"
+ "Sending query response."
+ "Unsupported command type %llu"
+ "XPC message received"
+ "com.apple.MobileAccessoryUpdater.FUDGenericKextUpdater"
+ "com.apple.mobileaccessoryupdater.externalclientaccess"
+ "handleXPCAPIEvent:"
+ "processAPIDict:"
- "+"

```
