## SPShared

> `/System/Library/PrivateFrameworks/SPShared.framework/SPShared`

```diff

-396.33.10.29.9
-  __TEXT.__text: 0x3f398
-  __TEXT.__auth_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0x215e
-  __TEXT.__cstring: 0x1692
-  __TEXT.__oslogstring: 0x5b4
-  __TEXT.__swift5_typeref: 0xccb
-  __TEXT.__swift5_reflstr: 0x9bd
+396.34.7.11.35
+  __TEXT.__text: 0x33ff8
+  __TEXT.__auth_stubs: 0x1940
+  __TEXT.__objc_methlist: 0x184
+  __TEXT.__const: 0x200e
+  __TEXT.__cstring: 0x1042
+  __TEXT.__oslogstring: 0x442
+  __TEXT.__swift5_typeref: 0xb1e
+  __TEXT.__swift5_reflstr: 0x8bd
   __TEXT.__swift5_assocty: 0x170
-  __TEXT.__constg_swiftt: 0x11e0
-  __TEXT.__swift5_fieldmd: 0xc24
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_proto: 0x14c
-  __TEXT.__swift5_types: 0xfc
-  __TEXT.__swift5_capture: 0xa40
+  __TEXT.__constg_swiftt: 0xfe8
+  __TEXT.__swift5_fieldmd: 0xab8
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_proto: 0x130
+  __TEXT.__swift5_types: 0xdc
+  __TEXT.__swift5_capture: 0x970
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x1050
-  __TEXT.__eh_frame: 0x1150
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__unwind_info: 0xd18
+  __TEXT.__eh_frame: 0xf40
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methname: 0x60b
   __TEXT.__objc_methtype: 0xe9
   __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e8
+  __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xd40
-  __AUTH_CONST.__auth_ptr: 0x420
-  __AUTH_CONST.__const: 0x2a58
-  __AUTH_CONST.__objc_const: 0x1920
+  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH_CONST.__auth_ptr: 0x3e8
+  __AUTH_CONST.__const: 0x2698
+  __AUTH_CONST.__objc_const: 0x12b0
   __AUTH.__objc_data: 0xe0
   __AUTH.__data: 0x878
-  __DATA.__data: 0x5b0
-  __DATA.__bss: 0x1f00
+  __DATA.__data: 0x580
+  __DATA.__bss: 0x1c00
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x148
-  __DATA_DIRTY.__data: 0x1118
-  __DATA_DIRTY.__bss: 0x800
-  __DATA_DIRTY.__common: 0x60
+  __DATA_DIRTY.__data: 0xcf8
+  __DATA_DIRTY.__bss: 0x780
+  __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1489
-  Symbols:   337
-  CStrings:  312
+  Functions: 1232
+  Symbols:   328
+  CStrings:  265
 
Symbols:
+ _OBJC_CLASS_$_NSXPCInterface
+ _objc_autorelease
+ _objc_release_x27
+ _objc_release_x28
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getExistentialTypeMetadata
+ _swift_getFunctionTypeMetadata0
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- __xpc_event_key_name
- _notify_cancel
- _notify_get_state
- _notify_register_check
- _notify_register_dispatch
- _notify_set_state
- _objc_release_x10
- _objc_retainAutorelease
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStackObject
- _swift_initStructMetadata
- _xpc_dictionary_get_string
- _xpc_set_event_stream_handler
CStrings:
- "DarwinNotificationHelper failed init. darwinCenter not available"
- "DarwinNotificationHelper initialized for posting. Not registered for %s"
- "DarwinNotificaton"
- "Division by zero"
- "Division results in an overflow"
- "Failed notify_register_check."
- "Insufficient space allocated to copy string contents"
- "Invoking callback, notification, %s"
- "Not enough bits to represent the passed value"
- "On XPC event stream, com.apple.notifyd.matching, notification: %{public}s)"
- "Posting %{public}s, rate-limiting: %{bool}d."
- "SPShared/DarwinNotificationHelper.swift"
- "Setting up darwin callback handler for %s"
- "Setup darwin callback handlers"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_TtC8SPShared24DarwinNotificationHelper"
- "_TtC8SPShared24DarwinNotificationPoster"
- "_TtC8SPShared25DarwinNotificationManager"
- "_TtC8SPShared26DarwinNotificationListener"
- "com.apple.SPShared.DarwinNotificationManager"
- "com.apple.icloud.SPShared.DarwinNotificationListener"
- "com.apple.icloud.SPShared.DarwinNotificationPoster"
- "com.apple.notifyd.matching"
- "darwinNotifications"
- "invalid Collection: less than 'count' elements in collection"
- "listener"
- "notificationHandlers"
- "poster"
- "publishers"
- "rateLimited"
- "tokens"
- "underTest"
- "v12@?0i8"
- "v16@?0@\"<OS_xpc_object>\"8"

```
