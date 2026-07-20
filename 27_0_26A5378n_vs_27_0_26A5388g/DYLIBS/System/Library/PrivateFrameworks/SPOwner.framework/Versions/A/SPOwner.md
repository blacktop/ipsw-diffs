## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
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
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-449.20.6.14.6
-  __TEXT.__text: 0x7cfbc
-  __TEXT.__objc_methlist: 0xbd3c
+449.20.6.14.15
+  __TEXT.__text: 0x7d8f0
+  __TEXT.__objc_methlist: 0xbd54
   __TEXT.__const: 0x5e8
-  __TEXT.__gcc_except_tab: 0x14f0
+  __TEXT.__gcc_except_tab: 0x1514
   __TEXT.__cstring: 0x69c9
-  __TEXT.__oslogstring: 0x8298
+  __TEXT.__oslogstring: 0x8378
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x24d0
+  __TEXT.__unwind_info: 0x24e0
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x890
+  __DATA_CONST.__const: 0x878
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e38
+  __DATA_CONST.__objc_selrefs: 0x3e40
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x2228
+  __AUTH_CONST.__const: 0x21d8
   __AUTH_CONST.__cfstring: 0x6000
-  __AUTH_CONST.__objc_const: 0x14738
+  __AUTH_CONST.__objc_const: 0x14740
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH.__objc_data: 0x1308
+  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH.__objc_data: 0x138
   __DATA.__objc_ivar: 0xf54
   __DATA.__data: 0x15f8
   __DATA.__bss: 0x660
-  __DATA_DIRTY.__objc_data: 0x1878
+  __DATA_DIRTY.__objc_data: 0x2a48
   __DATA_DIRTY.__data: 0x1d0
   __DATA_DIRTY.__bss: 0x4c0
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4405
-  Symbols:   8935
-  CStrings:  1584
+  Functions: 4407
+  Symbols:   8937
+  CStrings:  1586
 
Symbols:
+ -[SPIntentSession redonateItemEntitiesWithCompletion:]
+ ___block_descriptor_64_e8_32s40s48bs56w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16l
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _kBeaconUpdateQueueKey
+ _objc_msgSend$redonateItemEntitiesWithCompletion:
- ___block_descriptor_32_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_e8_32bs40w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16l
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12l
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
