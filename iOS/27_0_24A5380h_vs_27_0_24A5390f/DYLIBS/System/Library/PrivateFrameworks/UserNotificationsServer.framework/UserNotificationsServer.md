## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-713.0.0.0.0
-  __TEXT.__text: 0x3b988
-  __TEXT.__objc_methlist: 0x2454
+717.0.0.0.0
+  __TEXT.__text: 0x3c354
+  __TEXT.__objc_methlist: 0x24d4
   __TEXT.__const: 0x4e4
-  __TEXT.__gcc_except_tab: 0x660
-  __TEXT.__cstring: 0x1628
+  __TEXT.__gcc_except_tab: 0x654
+  __TEXT.__cstring: 0x16b8
   __TEXT.__oslogstring: 0x6865
   __TEXT.__constg_swiftt: 0x278
   __TEXT.__swift5_typeref: 0x43c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__unwind_info: 0xdf8
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1210
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__const: 0x12b0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bb0
+  __DATA_CONST.__objc_selrefs: 0x2c08
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__got: 0x988
   __AUTH_CONST.__const: 0x778
   __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x5dd0
+  __AUTH_CONST.__objc_const: 0x5f28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xa30
-  __AUTH.__objc_data: 0x120
+  __AUTH.__objc_data: 0x170
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x228
+  __DATA.__objc_ivar: 0x23c
   __DATA.__data: 0xcd0
   __DATA.__bss: 0x1
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1119
-  Symbols:   3242
-  CStrings:  524
+  Functions: 1138
+  Symbols:   3288
+  CStrings:  527
 
Symbols:
+ -[UNSSettingsUpdateCoalescer .cxx_destruct]
+ -[UNSSettingsUpdateCoalescer _queue_ackRestoringOnFailure:]
+ -[UNSSettingsUpdateCoalescer _queue_drain]
+ -[UNSSettingsUpdateCoalescer connection]
+ -[UNSSettingsUpdateCoalescer enqueueSourceIdentifiers:]
+ -[UNSSettingsUpdateCoalescer enqueueSystemSettings:]
+ -[UNSSettingsUpdateCoalescer initWithConnection:]
+ -[UNSUserNotificationServerSettingsConnectionListener registerForSettingsUpdates]
+ GCC_except_table23
+ GCC_except_table24
+ _OBJC_CLASS_$_UNSSettingsUpdateCoalescer
+ _OBJC_IVAR_$_UNSSettingsUpdateCoalescer._connection
+ _OBJC_IVAR_$_UNSSettingsUpdateCoalescer._inFlight
+ _OBJC_IVAR_$_UNSSettingsUpdateCoalescer._pendingSourceIdentifiers
+ _OBJC_IVAR_$_UNSSettingsUpdateCoalescer._pendingSystemSettings
+ _OBJC_IVAR_$_UNSSettingsUpdateCoalescer._queue
+ _OBJC_IVAR_$_UNSUserNotificationServerSettingsConnectionListener._clients
+ _OBJC_METACLASS_$_UNSSettingsUpdateCoalescer
+ __OBJC_$_INSTANCE_METHODS_UNSSettingsUpdateCoalescer
+ __OBJC_$_INSTANCE_VARIABLES_UNSSettingsUpdateCoalescer
+ __OBJC_$_PROP_LIST_UNSSettingsUpdateCoalescer
+ __OBJC_CLASS_RO_$_UNSSettingsUpdateCoalescer
+ __OBJC_METACLASS_RO_$_UNSSettingsUpdateCoalescer
+ ___42-[UNSSettingsUpdateCoalescer _queue_drain]_block_invoke
+ ___42-[UNSSettingsUpdateCoalescer _queue_drain]_block_invoke_2
+ ___42-[UNSSettingsUpdateCoalescer _queue_drain]_block_invoke_3
+ ___42-[UNSSettingsUpdateCoalescer _queue_drain]_block_invoke_4
+ ___42-[UNSSettingsUpdateCoalescer _queue_drain]_block_invoke_5
+ ___42-[UNSSettingsUpdateCoalescer _queue_drain]_block_invoke_6
+ ___52-[UNSSettingsUpdateCoalescer enqueueSystemSettings:]_block_invoke
+ ___55-[UNSSettingsUpdateCoalescer enqueueSourceIdentifiers:]_block_invoke
+ ___59-[UNSSettingsUpdateCoalescer _queue_ackRestoringOnFailure:]_block_invoke
+ ___59-[UNSSettingsUpdateCoalescer _queue_ackRestoringOnFailure:]_block_invoke_2
+ ___90-[UNSUserNotificationServerSettingsConnectionListener _handleClientConnectionInvalidated:]_block_invoke
+ ___block_descriptor_40_e8_32s_e36_v16?0"UNSSettingsUpdateCoalescer"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_B32?0"UNSSettingsUpdateCoalescer"8Q16^B24ls32l8
+ ___block_descriptor_57_e8_32bs40r48w_e5_v8?0lr40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e8_v12?0B8ls32l8r48l8w56l8s40l8
+ _objc_msgSend$_queue_ackRestoringOnFailure:
+ _objc_msgSend$_queue_drain
+ _objc_msgSend$connection
+ _objc_msgSend$defaultSectionInfo
+ _objc_msgSend$enqueueSourceIdentifiers:
+ _objc_msgSend$enqueueSystemSettings:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithConnection:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$un_errorWithUNPrivateErrorCode:userInfo:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$updateNotificationSourcesWithBundleIdentifiers:reply:
+ _objc_msgSend$updateNotificationSystemSettings:reply:
- GCC_except_table20
- GCC_except_table22
- _OBJC_IVAR_$_UNSUserNotificationServerSettingsConnectionListener._connections
- _objc_msgSend$updateNotificationSourcesWithBundleIdentifiers:
- _objc_msgSend$updateNotificationSystemSettings:
CStrings:
+ "B32@?0@\"UNSSettingsUpdateCoalescer\"8Q16^B24"
+ "com.apple.usernotifications.UNSSettingsUpdateCoalescer"
+ "v16@?0@\"UNSSettingsUpdateCoalescer\"8"
```
