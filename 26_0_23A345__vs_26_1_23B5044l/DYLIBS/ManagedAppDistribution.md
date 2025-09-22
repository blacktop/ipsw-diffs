## ManagedAppDistribution

> `/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution`

```diff

-3.0.52.0.0
-  __TEXT.__text: 0x7e5e4
-  __TEXT.__auth_stubs: 0x1280
+3.1.3.0.0
+  __TEXT.__text: 0x7db00
+  __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_methlist: 0x30c
-  __TEXT.__const: 0xdeb4
+  __TEXT.__const: 0xdee4
   __TEXT.__cstring: 0x1266
   __TEXT.__swift5_typeref: 0x244f
-  __TEXT.__constg_swiftt: 0x24ac
+  __TEXT.__constg_swiftt: 0x2494
   __TEXT.__swift5_proto: 0xdf4
   __TEXT.__swift5_types: 0x400
   __TEXT.__swift_as_entry: 0x114
   __TEXT.__swift_as_ret: 0x160
-  __TEXT.__oslogstring: 0x57d
-  __TEXT.__unwind_info: 0x2c78
-  __TEXT.__eh_frame: 0x4830
+  __TEXT.__oslogstring: 0x5dd
+  __TEXT.__unwind_info: 0x2c28
+  __TEXT.__eh_frame: 0x4788
   __TEXT.__objc_methname: 0x96a
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x940
-  __AUTH_CONST.__const: 0x8460
-  __AUTH_CONST.__objc_const: 0x6e8
+  __AUTH_CONST.__auth_got: 0x918
+  __AUTH_CONST.__const: 0x84e0
+  __AUTH_CONST.__objc_const: 0x6c8
   __AUTH.__objc_data: 0x108
   __AUTH.__data: 0x828
   __DATA.__data: 0x2200
   __DATA.__bss: 0x18b00
-  __DATA_DIRTY.__objc_data: 0x160
-  __DATA_DIRTY.__data: 0xd70
+  __DATA_DIRTY.__objc_data: 0x150
+  __DATA_DIRTY.__data: 0xcb0
   __DATA_DIRTY.__bss: 0x3380
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6389927E-DE3F-38E4-94C7-2A5D39143773
-  Functions: 4148
-  Symbols:   1566
+  UUID: A530A5E8-020D-3C4D-84E0-944AF7E3EADB
+  Functions: 4134
+  Symbols:   1563
   CStrings:  304
 
Symbols:
+ _block_copy_helper.29
+ _block_copy_helper.36
+ _block_copy_helper.43
+ _block_descriptor.31
+ _block_descriptor.38
+ _block_descriptor.45
+ _block_destroy_helper.30
+ _block_destroy_helper.37
+ _block_destroy_helper.44
+ _objc_release_x27
+ _objectdestroy.21Tm
+ _type_layout_string 22ManagedAppDistribution9XPCClientC24MessageRegistrationStateV
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_ManagedAppDistribution
- _block_copy_helper.31
- _block_copy_helper.38
- _block_descriptor.33
- _block_descriptor.40
- _block_destroy_helper.32
- _block_destroy_helper.39
- _objc_retain_x26
- _objc_retain_x27
- _objectdestroy.23Tm
- _swift_updateClassMetadata2
CStrings:
+ "Adding new #listener for managed app catalog"
+ "Client-deliverable error registering #listener for message: %{public}s: %{public}s"
+ "Error registering #listener for message: %{public}s: %{public}s"
+ "Re-registering #listener for messages; interrupted the first time"
+ "Registering %s#listener for messages: %{public}s"
+ "Sending cached app catalog results to #listener"
- "Client-deliverable error registering for message: %{public}s: %{public}s"
- "Error registering for message: %{public}s: %{public}s"
- "Re-registering for messages; interrupted the first time"
- "Registering for messages: %{public}s"
- "Sending cached app catalog results to listener"
- "id"

```
