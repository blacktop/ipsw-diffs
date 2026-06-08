## distnoted

> `/usr/sbin/distnoted`

```diff

-5026.5.4.0.0
-  __TEXT.__text: 0x3b18
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x39c
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__objc_methname: 0x582
-  __TEXT.__cstring: 0x67e
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methtype: 0x284
-  __TEXT.__oslogstring: 0x176
-  __TEXT.__dof_distnoted: 0xb18
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x290
-  __DATA_CONST.__cfstring: 0x200
-  __DATA_CONST.__objc_classlist: 0x18
+5027.0.51.2.101
+  __TEXT.__text: 0x5268
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_stubs: 0x680
+  __TEXT.__objc_methlist: 0x464
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__objc_methname: 0x746
+  __TEXT.__cstring: 0x755
+  __TEXT.__objc_classname: 0x7b
+  __TEXT.__objc_methtype: 0x33d
+  __TEXT.__oslogstring: 0x5b1
+  __TEXT.__dof_distnoted: 0xc01
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__const: 0x2f8
+  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x7c8
-  __DATA.__objc_selrefs: 0x208
-  __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x118
-  __DATA.__bss: 0x38
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x970
+  __DATA.__objc_selrefs: 0x288
+  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x128
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACA4B2FE-7B33-344E-AACF-AB952AABD82F
-  Functions: 82
-  Symbols:   132
-  CStrings:  231
+  UUID: A08B69D4-C41D-3F71-9AC7-4C3B8FA1D683
+  Functions: 105
+  Symbols:   154
+  CStrings:  291
 
Symbols:
+ _CFBooleanGetValue
+ _CFStringGetCStringPtr
+ _CFXNotificationRegistrarIsEmpty
+ _OBJC_CLASS_$_NSMutableDictionary
+ ___error
+ __os_feature_enabled_impl
+ __os_log_fault_impl
+ __xpc_type_array
+ __xpc_type_data
+ __xpc_type_string
+ _abort
+ _csops_audittoken
+ _dispatch_queue_create_with_target$V2
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _objc_alloc_init
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_loadWeak
+ _xpc_connection_copy_entitlement_value
+ _xpc_copy
+ _xpc_dictionary_set_uint64
+ _xpc_event_publisher_activate
+ _xpc_event_publisher_create
+ _xpc_event_publisher_fire
+ _xpc_event_publisher_set_error_handler
+ _xpc_event_publisher_set_handler
+ _xpc_event_publisher_set_throttling
+ _xpc_strerror
- _CFGetTypeID
- _CFStringGetTypeID
- __CFXPCCreateXPCObjectFromCFObject
- _dispatch_queue_create
- _dispatch_set_target_queue
- _xpc_connection_send_message_with_reply_sync
- _xpc_dictionary_create_reply
- _xpc_dictionary_get_bool
- _xpc_dictionary_set_bool
CStrings:
+ "    Outgoing Queue: %{public}d"
+ "%{public}s (%{public}d) does not have required entitlement key '%{public}@'. Process will not receive posted notification (%{public}@)."
+ "%{public}s (%{public}d) is not trusted and does not have required entitlement key '%{public}@'. Process will not receive posted notification (%{public}@)."
+ "%{public}s (%{public}d) is not trusted. Process will not receive posted notification (%{public}@)."
+ "%{public}s (%{public}d) will not receive posted notification (name: %{public}@), outbound queue is too large (%{public}d)"
+ "@\"NSCountedSet\""
+ "@\"NSMutableDictionary\""
+ "@24@0:8^{__CFString=}16"
+ "@24@0:8^{distnoted_configuration=Q@@@@@@@@@@@@}16"
+ "@32@0:8@16@24"
+ "@32@0:8@16^{distnoted_configuration=Q@@@@@@@@@@@@}24"
+ "B24@0:8^{__CFString=}16"
+ "CFNotificationCenterRestoreState"
+ "CoreFoundation"
+ "EntitlementStringCache"
+ "Expected NSCountedSet to be available"
+ "I"
+ "NSCountedSet"
+ "Name"
+ "New connection from %{public}s (%{public}d)"
+ "Object"
+ "Posted notification cannot be delivered to trusted XPC audience. Process is configured as an XPC publisher but stream publisher does not exist."
+ "Received XPC event publisher error: %s (%d)"
+ "Unable to determine whether client is a platform binary (PID: %d). Error: %{darwin.errno}d"
+ "UserInfo"
+ "_NSDNXPCPublisher"
+ "_entitlementResults"
+ "_isTrustedProcess"
+ "_keyCache"
+ "_xpcOutboundCount"
+ "audience"
+ "clients"
+ "com.apple.distnoted.matching.trusted"
+ "entitlement_key"
+ "getCachedName:"
+ "getXPCOutboundCount"
+ "handlePostWithName:object:userInfo:msg:audience:entitlementKey:"
+ "handlePostWithName:xpcObject:xpcUserInfo:"
+ "hasEntitlementKey:"
+ "initWithCapacity:"
+ "initWithStreamName:queue:"
+ "kCFNotificationAnyObject"
+ "member:"
+ "objectForKey:"
+ "post_super"
+ "register name: %{public}@ object: %{public}@ token: %llx pid: (event)"
+ "registerRemoteToken:object:remoteToken:options:"
+ "registerSubscriber:name:object:"
+ "registrarIsEmpty"
+ "releaseCachedName:"
+ "removeAllObjects"
+ "removeObject:"
+ "restore"
+ "restore count: %zu pid: %d"
+ "retainCachedName:"
+ "setObject:forKey:"
+ "super_delivery_targets"
+ "unable to route notification to XPC publisher"
+ "unregister token: %llx pid: (event)"
+ "unregisterSubscriber:"
+ "v12@?0i8"
+ "v24@0:8Q16"
+ "v28@?0I8Q12@\"NSObject<OS_xpc_object>\"20"
+ "v40@0:8@16@24@32"
+ "v40@0:8Q16^{__CFString=}24^{__CFString=}32"
+ "v48@0:8r*16r*24Q32Q40"
+ "v60@0:8@16@24Q32Q40C48@52"
+ "v64@0:8@16@24@32@40Q48^{__CFString=}56"
- "@24@0:8^{distnoted_configuration=Q@@@@@@@@@@}16"
- "@32@0:8@16^{distnoted_configuration=Q@@@@@@@@@@}24"
- "com.apple.NSXPC.msg_needs_ack"
- "handlePost:userInfo:"
- "methodclients"
- "post_all"
- "sendMessage:waitForAck:"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v60@0:8^{__CFString=}16^{__CFString=}24Q32Q40C48@52"

```
