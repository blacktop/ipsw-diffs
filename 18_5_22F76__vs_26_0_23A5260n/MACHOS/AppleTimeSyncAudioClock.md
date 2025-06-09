## AppleTimeSyncAudioClock

> `/System/Library/Audio/Plug-Ins/HAL/AppleTimeSyncAudioClock.driver/AppleTimeSyncAudioClock`

```diff

-1340.12.0.0.0
-  __TEXT.__text: 0x5710
+1400.53.0.0.0
+  __TEXT.__text: 0x5718
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x940
   __TEXT.__objc_methlist: 0x2d4

   __TEXT.__cstring: 0x352
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0xce6
-  __TEXT.__objc_methtype: 0x47a
+  __TEXT.__objc_methtype: 0x40a
   __TEXT.__dof_ATSACCADe: 0x6a1
   __TEXT.__unwind_info: 0x220
   __DATA_CONST.__auth_got: 0x290

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A48FD6AF-F5CB-3ACF-A44E-E4050BC1E75E
+  UUID: 6F0EB2B7-BF08-38EB-8EB3-3E1E4FB18C3E
   Functions: 87
   Symbols:   127
   CStrings:  282
Symbols:
+ __ZnwmSt19__type_descriptor_t
- __Znwm
Functions:
~ sub_6118 : 84 -> 76
~ sub_6184 -> sub_617c : 72 -> 88
CStrings:
+ "{LocklessTimestamp=\"mNumberOfSlots\"Q\"mTimestamps\"{vector<LocklessTimestamp::Timestamp, std::allocator<LocklessTimestamp::Timestamp>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}\"mTimestampIndex\"{atomic<unsigned long>=\"__a_\"{__cxx_atomic_impl<unsigned long, std::__cxx_atomic_base_impl<unsigned long>>=\"__a_value\"AQ}}}"
- "{LocklessTimestamp=\"mNumberOfSlots\"Q\"mTimestamps\"{vector<LocklessTimestamp::Timestamp, std::allocator<LocklessTimestamp::Timestamp>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<LocklessTimestamp::Timestamp *, std::allocator<LocklessTimestamp::Timestamp>>=\"__value_\"^{?}}}\"mTimestampIndex\"{atomic<unsigned long>=\"__a_\"{__cxx_atomic_impl<unsigned long, std::__cxx_atomic_base_impl<unsigned long>>=\"__a_value\"AQ}}}"

```
