## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-560.4.11.0.0
-  __TEXT.__text: 0x4e2a0
+578.0.1.0.0
+  __TEXT.__text: 0x461e0
   __TEXT.__auth_stubs: 0x1460
   __TEXT.__objc_methlist: 0x1b68
-  __TEXT.__const: 0x13fc
+  __TEXT.__const: 0x13ec
   __TEXT.__cstring: 0x2937
-  __TEXT.__oslogstring: 0x476b
+  __TEXT.__oslogstring: 0x47eb
   __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__constg_swiftt: 0x988
   __TEXT.__swift5_typeref: 0x60b
+  __TEXT.__swift5_capture: 0x7c
+  __TEXT.__constg_swiftt: 0x988
   __TEXT.__swift5_reflstr: 0x2e3
   __TEXT.__swift5_fieldmd: 0x47c
   __TEXT.__swift5_proto: 0xfc
   __TEXT.__swift5_types: 0x78
-  __TEXT.__swift5_capture: 0x7c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf20
-  __TEXT.__eh_frame: 0x16d0
+  __TEXT.__unwind_info: 0xf18
+  __TEXT.__eh_frame: 0x16e0
   __TEXT.__objc_classname: 0x370
-  __TEXT.__objc_methname: 0x5940
+  __TEXT.__objc_methname: 0x5948
   __TEXT.__objc_methtype: 0x87b
-  __TEXT.__objc_stubs: 0x2e40
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x678
+  __TEXT.__objc_stubs: 0x2e80
+  __DATA_CONST.__got: 0x580
+  __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1368
+  __DATA_CONST.__objc_selrefs: 0x1370
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0xa40
-  __AUTH_CONST.__const: 0xb28
+  __AUTH_CONST.__const: 0xb50
   __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x2e48
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x720
+  __AUTH.__objc_data: 0x770
   __AUTH.__data: 0xaa0
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x6a0
   __DATA.__bss: 0x20c0
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 3598E343-9876-3217-BEB4-4A756F9BCE8B
-  Functions: 1345
-  Symbols:   2987
-  CStrings:  1844
+  UUID: 30EA6486-6409-3021-8D73-05F85D00D5F8
+  Functions: 1343
+  Symbols:   2968
+  CStrings:  1847
 
Symbols:
+ -[RMManagedDevice getPropertyForKey:scope:].cold.1
+ -[RMManagedDevice setProperty:forKey:scope:].cold.1
+ _OBJC_CLASS_$_MDMConfigurationBase
+ ___block_descriptor_48_e8_32s40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_RemoteManagement
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_RemoteManagement
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_RemoteManagement
+ _objc_msgSend$getPropertyForKey:error:
+ _objc_msgSend$managedDevice
+ _objc_msgSend$managingProfileIdentifier
+ _objc_msgSend$setPropertyForKey:value:error:
+ _objc_msgSend$sharedConfigurationForChannel:
- ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_RemoteManagement
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_RemoteManagement
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_RemoteManagement
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_RemoteManagement
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_RemoteManagement
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_RemoteManagement
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_RemoteManagement
- _objc_msgSend$getPropertyForKey:channelType:
- _objc_msgSend$memberQueueManagingProfileIdentifier
- _objc_msgSend$setPropertyForKey:value:channelType:
- _swift_unknownObjectRelease_n
CStrings:
+ "Failed to get property for key %{public}@ with error %{public}@"
+ "Failed to set property for key %{public}@ with error %{public}@"
+ "getPropertyForKey:error:"
+ "managingProfileIdentifier"
+ "setPropertyForKey:value:error:"
+ "sharedConfigurationForChannel:"
- "getPropertyForKey:channelType:"
- "memberQueueManagingProfileIdentifier"
- "setPropertyForKey:value:channelType:"

```
