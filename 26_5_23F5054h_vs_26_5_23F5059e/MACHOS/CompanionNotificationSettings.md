## CompanionNotificationSettings

> `/System/Library/NanoPreferenceBundles/General/CompanionNotificationSettings.bundle/CompanionNotificationSettings`

```diff

-1114.4.44.0.0
-  __TEXT.__text: 0x7e18
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0xea
+1114.4.50.0.0
+  __TEXT.__text: 0xa6f8
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x1460
+  __TEXT.__objc_methlist: 0x60c
+  __TEXT.__const: 0x112
   __TEXT.__cstring: 0xbf5
-  __TEXT.__objc_methname: 0x15c2
+  __TEXT.__objc_methname: 0x15d2
   __TEXT.__objc_classname: 0x202
   __TEXT.__objc_methtype: 0x1e1
-  __TEXT.__oslogstring: 0x209
+  __TEXT.__oslogstring: 0x34d
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__swift5_typeref: 0x39
+  __TEXT.__swift5_typeref: 0x7e
+  __TEXT.__swift5_capture: 0x38
   __TEXT.__constg_swiftt: 0x5c
   __TEXT.__swift5_reflstr: 0xa
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x288
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__eh_frame: 0x1d8
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__const: 0x300
   __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0xa68
-  __DATA.__objc_selrefs: 0x720
+  __DATA.__objc_selrefs: 0x728
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x390
-  __DATA.__data: 0x1d0
+  __DATA.__data: 0x1d8
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C7FE31D-D8B9-3E49-8086-FC712CDB38BC
-  Functions: 149
-  Symbols:   246
-  CStrings:  554
+  UUID: 06D8C570-57F9-3DAE-9ED7-FC5F2232B9F5
+  Functions: 170
+  Symbols:   252
+  CStrings:  560
 
Symbols:
+ _swift_deallocObject
+ _swift_retain
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
CStrings:
+ "Failed to save forwardAll to enabled transition: %{public}@"
+ "Notification forwarding is forwardAll for pairingID: %{public}s"
+ "Saved transition to enabled: %{bool,public}d"
+ "Transitioning from forwardAll to enabled, disabling app: %{public}s"
+ "Unknown forwarding decision for pairingID: %{public}s"
+ "_state"
+ "transitionFromForwardAllToEnabledDisablingApp:"
- "_forwardingState"

```
