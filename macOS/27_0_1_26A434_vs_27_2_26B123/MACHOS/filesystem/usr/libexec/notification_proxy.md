## notification_proxy

> `/usr/libexec/notification_proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x2150
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x1ec
+41.0.0.0.0
+  __TEXT.__text: 0x30a0
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__objc_methname: 0x3ac
-  __TEXT.__cstring: 0x176
-  __TEXT.__oslogstring: 0x4bf
+  __TEXT.__objc_methname: 0x3fd
+  __TEXT.__cstring: 0x1ea
+  __TEXT.__oslogstring: 0x85b
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methtype: 0x13e
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__cfstring: 0x100
+  __TEXT.__objc_methtype: 0x181
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x80
-  __DATA.__objc_const: 0x2a8
-  __DATA.__objc_selrefs: 0x1a0
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x90
+  __DATA.__objc_const: 0x2b0
+  __DATA.__objc_selrefs: 0x1c0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/Versions/A/RemoteXPC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 49
-  Symbols:   78
-  CStrings:  136
+  Functions: 57
+  Symbols:   92
+  CStrings:  167
 
Symbols:
+ __xpc_type_int64
+ __xpc_type_uint64
+ _notify_get_state
+ _notify_register_check
+ _notify_set_state
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _xpc_dictionary_apply
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_get_value
+ _xpc_dictionary_send_reply
+ _xpc_dictionary_set_value
CStrings:
+ "%@ - Failed to cancel the state token with status: %u"
+ "%@ - Failed to get notification state (%u)"
+ "%@ - Failed to register a state token for \"%@\" (%u)"
+ "%@ - Failed to set notification state (%u)"
+ "%@ - GET_NOTIFICATION_STATE is only supported over RemoteXPC"
+ "%@ - Got GET_NOTIFICATION_STATE command for notification: %@"
+ "%@ - Got SET_NOTIFICATION_STATE command for notification: %@"
+ "%@ - Holding state for %@"
+ "%@ - No name in get notification state command"
+ "%@ - No name in set notification state command"
+ "%@ - No state in set notification state command for \"%@\""
+ "%@ - no more state setters for \"%@\", releasing the state token"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "Failed to cancel the check token for \"%@\" (%u)"
+ "Failed to convert dictionary to XPC reply."
+ "Failed to read the state of \"%@\" to relay with it (%u)"
+ "Failed to register a check token for \"%@\" (%u)"
+ "GetNotificationState"
+ "Invalid input."
+ "No reply context for request, message: %@, connection: %@"
+ "RelayNotificationState"
+ "SetNotificationState"
+ "State"
+ "State is not a 64-bit integer, ignoring it."
+ "Status"
+ "longLongValue"
+ "numberWithLongLong:"
+ "numberWithUnsignedInt:"
+ "sendResponse:inReplyTo:"
+ "v32@0:8@\"NSDictionary\"16@\"NSObject<OS_xpc_object>\"24"
+ "v32@0:8@16@24"
```
