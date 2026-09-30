## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-449.30.6.14.8
-  __TEXT.__text: 0x76bcc
-  __TEXT.__objc_methlist: 0xbb14
+449.30.6.14.15
+  __TEXT.__text: 0x77470
+  __TEXT.__objc_methlist: 0xbb2c
   __TEXT.__const: 0x5b8
-  __TEXT.__gcc_except_tab: 0x157c
+  __TEXT.__gcc_except_tab: 0x15a0
   __TEXT.__cstring: 0x6a49
-  __TEXT.__oslogstring: 0x7ed8
+  __TEXT.__oslogstring: 0x7fa8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_typeref: 0x133

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x21a8
+  __DATA_CONST.__const: 0x2168
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d90
+  __DATA_CONST.__objc_selrefs: 0x3d98
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x5f8
-  __AUTH_CONST.__const: 0xbf8
+  __AUTH_CONST.__const: 0xbd8
   __AUTH_CONST.__cfstring: 0x5e80
-  __AUTH_CONST.__objc_const: 0x14170
+  __AUTH_CONST.__objc_const: 0x14178
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH.__objc_data: 0x48
   __DATA.__objc_ivar: 0xefc
   __DATA.__data: 0x15c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4390
-  Symbols:   8711
-  CStrings:  1570
+  Functions: 4392
+  Symbols:   8713
+  CStrings:  1572
 
Symbols:
+ -[SPIntentSession redonateItemEntitiesWithCompletion:]
+ ___block_descriptor_56_e8_32s40bs48w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw56l8s32l8s48l8s40l8
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _kBeaconUpdateQueueKey
+ _objc_msgSend$redonateItemEntitiesWithCompletion:
- ___block_descriptor_32_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_e8_32bs40w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw48l8s40l8s32l8
- _objc_msgSend$beaconSession
CStrings:
+ "SPInternalSimpleBeacon: decoded nil for nonnull `identifier`; substituting all-zero UUID. Beacon will not match any client filter and is dropped downstream."
+ "SPInternalSimpleBeacon: decoded nil for nonnull `productUUID`; substituting all-zero UUID."
+ "[%{public}@] Error during update for %@: %@"
+ "[%{public}@] Error during update: %@"
+ "[%{public}@] Error stopping session. stopped=%i error: %@"
+ "[%{public}@] Failed to start session. subscribed=%i error: %@"
+ "[%{public}@] Session started"
+ "[%{public}@] self deallocated before update fired"
+ "com.apple.icloud.searchpartyd.simpleBeaconUpdate"
- "Error during update of device %@ error: %@"
- "Error during update of devices error: %@"
- "Error stopping fetch of device for %@. Stopped %i, error: %@"
- "Error stopping fetch of devices. Stopped %i, error: %@"
- "Starting fetch of device for %@. Subscribed %i, error: %@"
- "Starting fetch of devices. Subscribed %i, error: %@"
- "com.apple.icloud.seachpartyd.simpleBeaconUpdate"
```
