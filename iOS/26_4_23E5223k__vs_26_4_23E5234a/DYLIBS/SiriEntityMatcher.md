## SiriEntityMatcher

> `/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher`

```diff

 3520.56.2.0.0
-  __TEXT.__text: 0x602bc
-  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__text: 0x5f750
+  __TEXT.__auth_stubs: 0x1650
   __TEXT.__objc_methlist: 0x400c
   __TEXT.__const: 0x13b2c
   __TEXT.__dlopen_cstrs: 0x78
   __TEXT.__oslogstring: 0x678f
-  __TEXT.__cstring: 0x8686
+  __TEXT.__cstring: 0x704e
   __TEXT.__swift5_typeref: 0x2a
   __TEXT.__gcc_except_tab: 0x3af4
   __TEXT.__ustring: 0x9e78
-  __TEXT.__unwind_info: 0x1c50
+  __TEXT.__unwind_info: 0x1c48
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0xa02
   __TEXT.__objc_methname: 0x848f

   __DATA_CONST.__objc_selrefs: 0x2070
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
-  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__auth_got: 0xb40
   __AUTH_CONST.__const: 0x16a0
   __AUTH_CONST.__cfstring: 0x3720
   __AUTH_CONST.__objc_const: 0x75a8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FBABD8E4-86A3-3B17-8707-3FBA9C00A253
+  UUID: AC64F9AB-E558-36DA-B294-A3463E9DD66C
   Functions: 1635
-  Symbols:   547
-  CStrings:  3579
+  Symbols:   545
+  CStrings:  3563
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
- _objc_retain_x5
Functions:
~ sub_2705cfa8c -> sub_27054fa8c : 1956 -> 1784
~ sub_2705d0e28 -> sub_270550d7c : 3356 -> 3292
~ sub_2705d26f8 -> sub_27055260c : 868 -> 840
~ sub_2705d97a4 -> sub_27055969c : 1108 -> 828
~ sub_2705d9e14 -> sub_270559bf4 : 3996 -> 3932
~ sub_2705dc280 -> sub_27055c020 : 160 -> 136
~ sub_2705dc334 -> sub_27055c0bc : 184 -> 112
~ sub_2705dc508 -> sub_27055c248 : 184 -> 112
~ sub_2705dc6a4 -> sub_27055c39c : 184 -> 112
~ sub_2705dd24c -> sub_27055cefc : 4544 -> 4264
~ sub_2705e12d0 -> sub_270560e68 : 1388 -> 1364
~ sub_2705e183c -> sub_2705613bc : 1424 -> 1264
~ sub_2705e1e04 -> sub_2705618e4 : 2516 -> 1504
~ sub_2705e3a90 -> sub_27056317c : 7232 -> 6736
~ sub_2705e838c -> sub_270567888 : 892 -> 872
~ sub_270613b8c -> sub_270593074 : 1944 -> 1860
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJmSugDzkHRN3Ug87DTFr3Fq-Lg650254XDlrfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"

```
