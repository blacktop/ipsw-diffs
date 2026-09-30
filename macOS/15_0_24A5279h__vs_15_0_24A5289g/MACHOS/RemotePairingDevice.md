## RemotePairingDevice

> `/System/Library/PrivateFrameworks/RemotePairingDevice.framework/Versions/A/RemotePairingDevice`

```diff

-194.0.0.501.1
-  __TEXT.__text: 0xd27d8
-  __TEXT.__auth_stubs: 0x27e0
+198.0.0.0.0
+  __TEXT.__text: 0xd341c
+  __TEXT.__auth_stubs: 0x28a0
   __TEXT.__objc_methlist: 0x348
-  __TEXT.__const: 0xb0c8
-  __TEXT.__oslogstring: 0x365c
-  __TEXT.__cstring: 0x62dc
-  __TEXT.__constg_swiftt: 0x37ec
-  __TEXT.__swift5_typeref: 0x3710
-  __TEXT.__swift5_reflstr: 0x2756
-  __TEXT.__swift5_fieldmd: 0x3270
+  __TEXT.__const: 0xb178
+  __TEXT.__oslogstring: 0x36dc
+  __TEXT.__cstring: 0x639c
+  __TEXT.__constg_swiftt: 0x3840
+  __TEXT.__swift5_typeref: 0x373a
+  __TEXT.__swift5_reflstr: 0x27b6
+  __TEXT.__swift5_fieldmd: 0x32a0
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_assocty: 0x240
   __TEXT.__swift5_proto: 0xab8
-  __TEXT.__swift5_types: 0x3dc
+  __TEXT.__swift5_types: 0x3e0
   __TEXT.__swift5_capture: 0x19f0
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x188
-  __TEXT.__unwind_info: 0x3f38
-  __TEXT.__eh_frame: 0x3628
-  __TEXT.__objc_classname: 0x12e
+  __TEXT.__unwind_info: 0x3f60
+  __TEXT.__eh_frame: 0x3658
+  __TEXT.__objc_classname: 0x13c
   __TEXT.__objc_methname: 0xa0a
   __TEXT.__objc_methtype: 0x127
   __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__const: 0x4e8
   __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x330
-  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x13f8
-  __AUTH_CONST.__auth_ptr: 0x8d0
-  __AUTH_CONST.__const: 0xaa50
+  __AUTH_CONST.__auth_got: 0x1458
+  __AUTH_CONST.__auth_ptr: 0x8e0
+  __AUTH_CONST.__const: 0xaad0
   __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x46a0
-  __AUTH.__objc_data: 0x7b0
-  __AUTH.__data: 0x2328
+  __AUTH_CONST.__objc_const: 0x4720
+  __AUTH.__objc_data: 0x800
+  __AUTH.__data: 0x2358
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x3120
+  __DATA.__data: 0x31a8
+  __DATA.__objc_clsrolist: 0x20
   __DATA.__bss: 0x14690
-  __DATA.__common: 0x5c
+  __DATA.__common: 0x68
   - /Library/Apple/System/Library/PrivateFrameworks/Mercury.framework/Versions/A/Mercury
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7349
-  Symbols:   3259
-  CStrings:  622
+  Functions: 7365
+  Symbols:   3284
+  CStrings:  626
 
Symbols:
+ _CFUUIDGetUUIDBytes
+ _NEVirtualInterfaceCopyNexusInstances
+ __OBJC_$_PROTOCOL_REFS_OS_nw_context
+ __OBJC_$_PROTOCOL_REFS_OS_nw_context
+ __OBJC_$_PROTOCOL_REFS_OS_nw_context
+ __OBJC_LABEL_PROTOCOL_$_OS_nw_context
+ __OBJC_PROTOCOL_$_OS_nw_context
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_RemotePairingDevice
+ _flat unique So13OS_nw_context_p
+ _generic_ro_datas
+ _generic_ro_datas
+ _nw_channel_create_with_attributes
+ _nw_context_activate
+ _nw_context_create
+ _nw_context_set_isolate_protocol_stack
+ _nw_context_set_scheduling_mode
+ _symbolic _____ 8Dispatch0A12TimeIntervalO
+ _symbolic _____Sg 8Dispatch0A8WorkItemC
+ _symbolic ______p So13OS_nw_contextP
+ block_copy_helper.20
+ block_copy_helper.38
+ block_copy_helper.51
+ block_descriptor.22
+ block_descriptor.40
+ block_descriptor.53
+ block_destroy_helper.21
+ block_destroy_helper.39
+ block_destroy_helper.52
+ objectdestroy.33Tm
- _NEVirtualInterfaceCreateChannel
- _nw_context_copy_implicit_context
- block_copy_helper.31
- block_copy_helper.47
- block_copy_helper.53
- block_descriptor.33
- block_descriptor.49
- block_descriptor.55
- block_destroy_helper.32
- block_destroy_helper.48
- block_destroy_helper.54
- objectdestroy.23Tm
CStrings:
+ "Unable to find nexus identifier associated with virtual interfaceref"
+ "_deferredCleanupFailsafeWorkItem"
+ "_networkContext"
+ "com.apple.remotepairing.SkywalkChannelVirtualInterface"
+ "deferredCleanupTimeoutInterval"
- "Failed to create skywalk channel for interface "

```
