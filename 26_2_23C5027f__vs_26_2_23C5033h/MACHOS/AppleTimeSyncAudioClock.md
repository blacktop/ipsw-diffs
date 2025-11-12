## AppleTimeSyncAudioClock

> `/System/Library/Audio/Plug-Ins/HAL/AppleTimeSyncAudioClock.driver/AppleTimeSyncAudioClock`

```diff

-1420.1.0.0.0
-  __TEXT.__text: 0x5718
+1420.2.0.0.0
+  __TEXT.__text: 0x571c
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x940
   __TEXT.__objc_methlist: 0x2d4

   __TEXT.__cstring: 0x352
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0xce6
-  __TEXT.__objc_methtype: 0x40a
+  __TEXT.__objc_methtype: 0x410
   __TEXT.__dof_ATSACCADe: 0x6a1
   __TEXT.__unwind_info: 0x220
   __DATA_CONST.__auth_got: 0x290

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27F95922-4FBA-38AF-8372-B1635C3F8943
+  UUID: BDCF9009-AA04-395A-9BA1-E3AB65E51761
   Functions: 87
   Symbols:   127
   CStrings:  282
Functions:
~ sub_6118 : 76 -> 80
CStrings:
+ "{LocklessTimestamp=\"mNumberOfSlots\"Q\"mTimestamps\"{vector<LocklessTimestamp::Timestamp, std::allocator<LocklessTimestamp::Timestamp>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}\"mTimestampIndex\"{atomic<unsigned long>=\"__a_\"{__cxx_atomic_impl<unsigned long, std::__cxx_atomic_base_impl<unsigned long>>=\"__a_value\"AQ}}}"
- "{LocklessTimestamp=\"mNumberOfSlots\"Q\"mTimestamps\"{vector<LocklessTimestamp::Timestamp, std::allocator<LocklessTimestamp::Timestamp>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}\"mTimestampIndex\"{atomic<unsigned long>=\"__a_\"{__cxx_atomic_impl<unsigned long, std::__cxx_atomic_base_impl<unsigned long>>=\"__a_value\"AQ}}}"

```
