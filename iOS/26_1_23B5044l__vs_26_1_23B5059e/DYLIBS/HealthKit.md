## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6200.2.7.2.1
-  __TEXT.__text: 0x348500
+6200.2.11.2.0
+  __TEXT.__text: 0x348744
   __TEXT.__auth_stubs: 0x3790
-  __TEXT.__objc_methlist: 0x3031c
+  __TEXT.__objc_methlist: 0x30324
   __TEXT.__cstring: 0x35d23
   __TEXT.__const: 0xac5c2
-  __TEXT.__oslogstring: 0xc703
-  __TEXT.__gcc_except_tab: 0x4218
+  __TEXT.__oslogstring: 0xc773
+  __TEXT.__gcc_except_tab: 0x422c
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x644
   __TEXT.__constg_swiftt: 0x3064

   __TEXT.__swift_as_ret: 0x174
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xfe10
+  __TEXT.__unwind_info: 0xfe18
   __TEXT.__eh_frame: 0x4628
   __TEXT.__objc_classname: 0x8a0d
-  __TEXT.__objc_methname: 0x5f5ed
+  __TEXT.__objc_methname: 0x5f607
   __TEXT.__objc_methtype: 0xc05d
   __TEXT.__objc_stubs: 0x2bfc0
   __DATA_CONST.__got: 0x1b68

   __AUTH_CONST.__auth_got: 0x1be0
   __AUTH_CONST.__const: 0xc6a0
   __AUTH_CONST.__cfstring: 0x32aa0
-  __AUTH_CONST.__objc_const: 0x50968
+  __AUTH_CONST.__objc_const: 0x509a8
   __AUTH_CONST.__objc_intobj: 0x4620
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x750
-  __AUTH.__objc_data: 0xece0
+  __AUTH.__objc_data: 0xecb8
   __AUTH.__data: 0x19a8
-  __DATA.__objc_ivar: 0x2e6c
+  __DATA.__objc_ivar: 0x2e74
   __DATA.__data: 0xd0c8
-  __DATA.__bss: 0x18c60
+  __DATA.__bss: 0x18c40
   __DATA.__common: 0x9c0
-  __DATA_DIRTY.__objc_data: 0x2480
+  __DATA_DIRTY.__objc_data: 0x24a8
   __DATA_DIRTY.__data: 0x130
-  __DATA_DIRTY.__bss: 0xca8
+  __DATA_DIRTY.__bss: 0xcb8
   __DATA_DIRTY.__common: 0xd8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B5C8056B-B05F-389C-8D3E-1E312724BCBF
-  Functions: 24353
-  Symbols:   61436
-  CStrings:  30235
+  UUID: F0A9E652-2E2C-3D50-8211-0FAC58A8A6E9
+  Functions: 24354
+  Symbols:   61441
+  CStrings:  30240
 
Symbols:
+ -[_HKWorkoutObserver description]
+ _HKWatchECGSampleAvailabilityDays
+ _OBJC_IVAR_$_HKUCUMUnitDisplayConverter._hkTableLock
+ _OBJC_IVAR_$_HKUCUMUnitDisplayConverter._synonymLock
+ ___34-[_HKWorkoutObserver setDelegate:]_block_invoke.18
- ___34-[_HKWorkoutObserver setDelegate:]_block_invoke_2
Functions:
~ -[_HKWorkoutObserver initWithHealthStore:reportInactiveSessions:] : 456 -> 612
~ -[_HKWorkoutObserver dealloc] : 76 -> 204
+ -[_HKWorkoutObserver description]
~ ___34-[_HKWorkoutObserver setDelegate:]_block_invoke : 200 -> 336
~ -[HKUCUMUnitDisplayConverter init] : 56 -> 64
~ -[HKUCUMUnitDisplayConverter synonymLookupTable] : 200 -> 204
~ -[HKUCUMUnitDisplayConverter hkUnitNameLookupTable] : 200 -> 204
CStrings:
+ "%{public}@: Registered for delegate updates"
+ "%{public}@: Workout Observer created"
+ "%{public}@: Workout Observer dealloc"
+ "_hkTableLock"
+ "_synonymLock"

```
