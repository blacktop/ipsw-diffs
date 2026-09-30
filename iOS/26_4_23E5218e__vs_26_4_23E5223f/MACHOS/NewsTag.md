## NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

-5864.0.0.0.0
-  __TEXT.__text: 0xa0f2c
-  __TEXT.__auth_stubs: 0x3090
+5867.0.0.0.0
+  __TEXT.__text: 0xa0a18
+  __TEXT.__auth_stubs: 0x3080
   __TEXT.__objc_stubs: 0x4e20
   __TEXT.__objc_methlist: 0x2318
   __TEXT.__const: 0x6ac4
   __TEXT.__gcc_except_tab: 0x1f8
-  __TEXT.__cstring: 0x6177
+  __TEXT.__cstring: 0x5307
   __TEXT.__oslogstring: 0xeca
   __TEXT.__objc_methname: 0x7a05
   __TEXT.__objc_classname: 0xd16

   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2050
+  __TEXT.__unwind_info: 0x2058
   __TEXT.__eh_frame: 0x1ad4
-  __DATA_CONST.__auth_got: 0x1860
+  __DATA_CONST.__auth_got: 0x1858
   __DATA_CONST.__got: 0xc40
   __DATA_CONST.__auth_ptr: 0xaf0
   __DATA_CONST.__const: 0x3bf8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 23916CDD-3507-3A8B-940E-B3ACEC727870
+  UUID: 5E63FBB5-4073-31A8-A487-8A10C3FBD8F6
   Functions: 2879
-  Symbols:   593
-  CStrings:  2038
+  Symbols:   592
+  CStrings:  2028
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ __ZN13ImageAnalyzer17QuantizeColorMapsEv : 764 -> 732
~ __ZN13ImageAnalyzer19PickBackgroundColorEv : 656 -> 460
~ __ZN13ImageAnalyzer14PickTextColorsEv : 1424 -> 1268
~ __ZN13ImageAnalyzer26AddQuantizeColorEntryToSetER22sortQuantizeColorEntryRNSt3__16vectorIS0_NS2_9allocatorIS0_EEEE : 288 -> 240
~ __ZN13ImageAnalyzer14DominantColorsEv : 464 -> 424
~ __ZN13ImageAnalyzer26AddDominantColorEntryToSetER14sortColorEntryRNSt3__16vectorIS0_NS2_9allocatorIS0_EEEE : 524 -> 492
~ sub_100006118 -> sub_100005f20 : 340 -> 260
~ sub_10000626c -> sub_100006024 : 716 -> 564
~ sub_100006538 -> sub_100006258 : 704 -> 536
~ sub_1000087dc -> sub_100008454 : 340 -> 264
~ sub_100008930 -> sub_10000855c : 728 -> 568
~ sub_100008c08 -> sub_100008794 : 704 -> 544
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
