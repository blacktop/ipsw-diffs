## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64570.53.1.0.0
-  __TEXT.__text: 0xa9d20
-  __TEXT.__auth_stubs: 0x1f70
-  __TEXT.__objc_methlist: 0x6398
+64570.56.1.0.0
+  __TEXT.__text: 0xaaeac
+  __TEXT.__auth_stubs: 0x2190
+  __TEXT.__objc_methlist: 0x6408
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xf5be
-  __TEXT.__gcc_except_tab: 0x4f1c
+  __TEXT.__cstring: 0xfa20
+  __TEXT.__gcc_except_tab: 0x4f28
   __TEXT.__oslogstring: 0x1614
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x27c8
+  __TEXT.__unwind_info: 0x2800
   __TEXT.__objc_classname: 0x81d
-  __TEXT.__objc_methname: 0xf011
-  __TEXT.__objc_methtype: 0x8597
-  __TEXT.__objc_stubs: 0x9680
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x3588
+  __TEXT.__objc_methname: 0xf160
+  __TEXT.__objc_methtype: 0x85e5
+  __TEXT.__objc_stubs: 0x9720
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x3638
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3440
+  __DATA_CONST.__objc_selrefs: 0x3478
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0x700
-  __AUTH_CONST.__auth_got: 0xfd0
+  __DATA_CONST.__objc_arraydata: 0x870
+  __AUTH_CONST.__auth_got: 0x10e0
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0xaa8
-  __AUTH_CONST.__cfstring: 0xcc80
-  __AUTH_CONST.__objc_const: 0xb9b0
+  __AUTH_CONST.__const: 0xb88
+  __AUTH_CONST.__cfstring: 0xd3e0
+  __AUTH_CONST.__objc_const: 0xb9e0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x2d0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc54
+  __DATA.__objc_ivar: 0xc58
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x520
-  __DATA.__common: 0xd9
+  __DATA.__bss: 0x550
+  __DATA.__common: 0xf1
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__bss: 0xd8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2961
-  Symbols:   3895
-  CStrings:  5852
+  Functions: 2982
+  Symbols:   3953
+  CStrings:  5933
 
Symbols:
+ _OBJC_CLASS_$_NSXPCInterface
+ __xpc_error_connection_invalid
+ __xpc_type_connection
+ _class_getInstanceSize
+ _dispatch_activate
+ _dispatch_data_create
+ _dispatch_group_create
+ _dispatch_mach_create
+ _dispatch_mach_msg_create
+ _mapped_memory_pointer_to_local_mapping_updated_with_extra_bits
+ _nw_array_create
+ _nw_frame_create
+ _objc_allocateProtocol
+ _os_transaction_create
+ _xpc_array_create
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create
+ _xpc_connection_create_from_endpoint
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_connection_set_event_handler
+ _xpc_data_create
+ _xpc_date_create
+ _xpc_dictionary_create
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_send_reply
+ _xpc_dictionary_set_string
+ _xpc_double_create
+ _xpc_endpoint_create
+ _xpc_fd_create
+ _xpc_get_type
+ _xpc_int64_create
+ _xpc_pointer_create
+ _xpc_string_create
+ _xpc_uint64_create
+ _xpc_uuid_create
CStrings:
+ " for ACTIVE TRANSACTION with"
+ "*** Symbolication:  malloc zone address %#llx is invalid\n"
+ "Bootstrap Dictionary"
+ "OS_dispatch_"
+ "OS_dispatch_data"
+ "OS_dispatch_group"
+ "OS_dispatch_mach_msg"
+ "OS_dispatch_semaphore"
+ "OS_dispatch_source"
+ "OS_nw_array"
+ "OS_nw_frame"
+ "OS_object"
+ "OS_os_log"
+ "OS_xpc_"
+ "OS_xpc_activity"
+ "OS_xpc_array"
+ "OS_xpc_data"
+ "OS_xpc_date"
+ "OS_xpc_dictionary"
+ "OS_xpc_double"
+ "OS_xpc_endpoint"
+ "OS_xpc_fd"
+ "OS_xpc_int64"
+ "OS_xpc_pipe"
+ "OS_xpc_pointer"
+ "OS_xpc_serializer"
+ "OS_xpc_session"
+ "OS_xpc_string"
+ "OS_xpc_uint64"
+ "OS_xpc_uuid"
+ "Protocol"
+ "Reply Message"
+ "Request Message"
+ "VMUScanOverlay.m"
+ "^{_VMUBlockNode=Qb3b2b36b23}24@0:8r^v16"
+ "__IncompleteProtocol"
+ "_arr"
+ "_buff"
+ "_identifyXPCDictionaryStorageReferencedByBlock:"
+ "_protocol"
+ "_setSuperclassOffset:"
+ "_table[%u]"
+ "_untypedMallocBlockNodeReferencedFromAddress:"
+ "_xpcDictionaryStorageClassInfoIndex"
+ "classInfo.instanceSize >= tableOffset + tableSize"
+ "determineOSClassInstanceSize"
+ "dispatch_data_t"
+ "dispatch_group_t"
+ "dispatch_mach_msg_t"
+ "dispatch_mach_t"
+ "dispatch_semaphore_t"
+ "dispatch_source_t"
+ "identifier"
+ "invalid zone pointer"
+ "key: \"%@\""
+ "labelForCStructureWithMemory:length:remoteAddress:classInfo:"
+ "labelForOSXPCDictionaryStorageNode:length:remoteAddress:"
+ "labelForOSXPCString:length:remoteAddress:"
+ "launchTime"
+ "setSuperclassOffset:"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@8"
+ "v20@?0I8@\"NSString\"12"
+ "v24@0:8^{_VMUBlockNode=Qb3b2b36b23}16"
+ "v28@?0Q8@\"NSObject<OS_dispatch_mach_msg>\"16i24"
+ "xpc_activity_t"
+ "xpc_array_t"
+ "xpc_connection_t"
+ "xpc_data_t"
+ "xpc_date_t"
+ "xpc_dictionary_t"
+ "xpc_double_t"
+ "xpc_endpoint_t"
+ "xpc_fd_t"
+ "xpc_int64_t"
+ "xpc_pipe_t"
+ "xpc_pointer_t"
+ "xpc_serializer_t"
+ "xpc_session_t"
+ "xpc_string_t"
+ "xpc_uint64_t"
+ "xpc_uuid_t"
- "Request/Reply message for active transaction with "
- "protocol"

```
