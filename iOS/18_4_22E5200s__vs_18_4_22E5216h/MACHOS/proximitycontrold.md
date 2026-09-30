## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-228.40.38.0.0
-  __TEXT.__text: 0x23bcd4
-  __TEXT.__auth_stubs: 0x30e0
+228.40.45.0.0
+  __TEXT.__text: 0x245e04
+  __TEXT.__auth_stubs: 0x3100
   __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x2904
   __TEXT.__objc_classname: 0x48b
   __TEXT.__objc_methname: 0x69c4
   __TEXT.__objc_methtype: 0x2d00
-  __TEXT.__const: 0x26140
-  __TEXT.__cstring: 0x17384
-  __TEXT.__swift5_typeref: 0x1285a
-  __TEXT.__constg_swiftt: 0x1020c
-  __TEXT.__swift5_reflstr: 0x9f3a
-  __TEXT.__swift5_fieldmd: 0xaa60
+  __TEXT.__const: 0x260f0
+  __TEXT.__cstring: 0x16ee4
+  __TEXT.__swift5_typeref: 0x127c8
+  __TEXT.__constg_swiftt: 0x101e0
+  __TEXT.__swift5_reflstr: 0x9f7a
+  __TEXT.__swift5_fieldmd: 0xaa78
   __TEXT.__swift5_builtin: 0x5c8
   __TEXT.__swift5_assocty: 0xec0
-  __TEXT.__swift5_capture: 0x3938
-  __TEXT.__oslogstring: 0x828
-  __TEXT.__swift5_proto: 0x226c
+  __TEXT.__swift5_capture: 0x3838
+  __TEXT.__oslogstring: 0xff8
+  __TEXT.__swift5_proto: 0x2260
   __TEXT.__swift5_types: 0xa64
   __TEXT.__swift5_protos: 0x32c
   __TEXT.__swift5_mpenum: 0x170
   __TEXT.__swift_as_entry: 0xc8
   __TEXT.__swift_as_ret: 0xc8
-  __TEXT.__unwind_info: 0x7880
-  __TEXT.__eh_frame: 0x7694
-  __DATA_CONST.__auth_got: 0x1878
-  __DATA_CONST.__got: 0xde8
-  __DATA_CONST.__auth_ptr: 0x3458
-  __DATA_CONST.__const: 0x1af98
+  __TEXT.__unwind_info: 0x7888
+  __TEXT.__eh_frame: 0x77b4
+  __DATA_CONST.__auth_got: 0x1888
+  __DATA_CONST.__got: 0xdf0
+  __DATA_CONST.__auth_ptr: 0x2058
+  __DATA_CONST.__const: 0x1ae80
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x17be0
+  __DATA.__objc_const: 0x17b60
   __DATA.__objc_selrefs: 0x1c80
   __DATA.__objc_ivar: 0x54
-  __DATA.__objc_data: 0x3028
-  __DATA.__data: 0x185f8
+  __DATA.__objc_data: 0x2fd0
+  __DATA.__data: 0x18640
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x3a190
-  __DATA.__common: 0x7c0
+  __DATA.__bss: 0x3a180
+  __DATA.__common: 0x7a0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11638
-  Symbols:   1520
-  CStrings:  4121
+  Functions: 11652
+  Symbols:   1524
+  CStrings:  4152
 
Symbols:
+ _$s15Synchronization5MutexVMn
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_runtimeSupportsNoncopyableTypes
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "\nHandoff enabled: "
+ " Should not initiate token sync: peer advertises 'no guest handoff'"
+ "### Activate failed: %@"
+ "### Activation failed: %@"
+ "### CBDiscovery error: %@"
+ "### Deliver content for %s failed: %@"
+ "### Disabled. FF=%{bool}d communal=%{bool}d"
+ "### Dismiss %s failed: %@"
+ "### Failed to create PCLockscreenControlsDevice for %s"
+ "### Failed to stop suppressing %s: %@"
+ "### Failed to suppress %s: %@"
+ "### Reactivated: %@"
+ "%s New legacyEvent: %s"
+ "%s caching mediaRouteID: %s"
+ "%s for %s"
+ "%s: device=%s, needsAssets=%{bool}d"
+ "%s: error=%s"
+ "Activate"
+ "Activated"
+ "Activated: %ld existing devices"
+ "Active call app is local foreground! Returning call"
+ "Active call can't be transferred. Returning nil"
+ "Active media app is local foreground! Returning media"
+ "Adding %@"
+ "Bluetooth state updated: %s"
+ "CBDevices changed, count=%ld"
+ "Clearing cached handoffDirection, oldValue = %s"
+ "Delivered content for %s"
+ "Dismissed %s"
+ "FOUND %@"
+ "Handle %s"
+ "Invalidate"
+ "LOST %@"
+ "New model: %s"
+ "No device found for %s - caching the event"
+ "Reactivated"
+ "Reactivating..."
+ "Removing %@"
+ "Reporting LOST: %s, distance=%s"
+ "Reporting update to clients %@"
+ "Simulating FOUND event for %s"
+ "Stop suppressing v1 for %s"
+ "Successfully stop suppressing v1 for %s"
+ "Successfully suppressed v1 for %s"
+ "Suppressing v1 for %s"
+ "Threshold changed: %f -> %f"
+ "Tracking %s"
+ "UPDATE: %s, distance=%s"
+ "Untrack %s"
+ "Untracking %s"
+ "Updating %s with %s"
+ "Updating handoffDirection to %s"
+ "XPC Publisher added: %s"
+ "XPC Publisher removed: %s"
+ "_deviceCloseServiceDeactivateDelay"
+ "activated(with:)"
+ "deviceCloseServiceDeactivateDelay"
+ "missedEvent"
+ "stopSuppressingIfNeeded(_:)"
+ "suppressIfNeeded(_:)"
+ "uwbRangingAvailable changed: %{bool}d"
- " caching mediaRouteID: "
- " existing devices"
- "### CBDiscovery error: "
- "### Disabled. FF="
- "### Failed to create PCLockscreenControlsDevice for "
- "### Failed to stop suppressing "
- "### Failed to suppress "
- "Bluetooth state updated: "
- "CBDevices changed, count="
- "Candidate no longer nearby, stopping transaction"
- "Candidate now nearby, starting transaction"
- "Clearing cached handoffDirection, oldValue = "
- "Delivered content for "
- "Reporting LOST: "
- "Reporting update to clients "
- "Simulating FOUND event for "
- "Stop suppressing v1 for "
- "Successfully stop suppressing v1 for "
- "Successfully suppressed v1 for "
- "Suppressing v1 for "
- "Suppressing v1 handoff in favor of v2 for "
- "Threshold changed: "
- "Updating handoffDirection to nil"
- "XPC Publisher added: "
- "XPC Publisher removed: "
- "_lastEvent"
- "activated(with:): error="
- "stopSuppressingIfNeeded(_:): device="
- "suppressIfNeeded(_:): device="
- "uwbRangingAvailable changed: "

```
