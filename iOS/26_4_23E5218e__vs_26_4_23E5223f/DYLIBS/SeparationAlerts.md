## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-107.0.12.0.3
-  __TEXT.__text: 0x36cf8
-  __TEXT.__auth_stubs: 0x5f0
+107.0.12.0.4
+  __TEXT.__text: 0x36ca4
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x3aa4
   __TEXT.__const: 0x118
-  __TEXT.__oslogstring: 0x7d16
-  __TEXT.__cstring: 0x1958
+  __TEXT.__oslogstring: 0x7d2f
+  __TEXT.__cstring: 0x16e7
   __TEXT.__gcc_except_tab: 0x23c
   __TEXT.__unwind_info: 0xb98
   __TEXT.__objc_classname: 0x5fd

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2070
   __DATA_CONST.__objc_superrefs: 0xf0
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x22e0
   __AUTH_CONST.__objc_const: 0x56e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 575E3456-33A6-3A90-A098-7A3E78005A07
-  Functions: 1079
-  Symbols:   4003
-  CStrings:  2670
+  UUID: DC8D0EF0-7A25-3239-99C3-766BAB653202
+  Functions: 1078
+  Symbols:   4000
+  CStrings:  2668
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__117__floyd_sift_downB9nqe210106INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE9push_backB9nqe210106ERU8__strongKS2_
+ __ZNSt3__19__sift_upB9nqe210106INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__117__floyd_sift_downB9foe210106INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB9foe210106Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE8pop_backB9foe210106Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE9push_backB9foe210106ERU8__strongKS2_
- __ZNSt3__19__sift_upB9foe210106INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ -[SATime earliestAlarm] : 128 -> 96
~ +[SABeaconGroupVerifier verifyBeaconGroupsWithBeaconGroups:deviceUUIDtoDeviceMap:deviceToSafeLocationMap:] : 3280 -> 3312
~ +[SABeaconGroupVerifier beaconGroupSizeForDevice:] : 164 -> 180
~ __ZNSt3__114priority_queueIU8__strongP11SAAlarmTaskNS_6vectorIS3_NS_9allocatorIS3_EEEE19SAAlarmClassCompareE3popEv : 212 -> 220
~ -[SATime getEarliestAlarmDate] : 132 -> 100
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE8pop_backB9foe210106Ev
CStrings:
+ "{\"msg%{public}.0s\":\"#sa #beaconMonitoring incorrect beacon group size\", \"groupIdentifier\":\"%{private}@\", \"beaconIdentifier\":\"%{private}@\", \"deviceType\":\"%{public}@\", \"expectedBeaconGroupSize\":%{public}lu, \"beaconGroup.count\":%{public}lu, \"productID\":%{public}lu}"
- "/AppleInternal/Library/BuildRoots/4~CI8UugAg4-jYL0rTEhDyrIzIZLhFpS7g2gdlLTY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI8UugAg4-jYL0rTEhDyrIzIZLhFpS7g2gdlLTY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "{\"msg%{public}.0s\":\"#sa #beaconMonitoring incorrect beacon group size\", \"groupIdentifier\":\"%{private}@\", \"beaconIdentifier\":\"%{private}@\", \"deviceType\":\"%{public}@\", \"expectedBeaconGroupSize\":%{public}lu, \"beaconGroup.count\":%{public}lu}"

```
