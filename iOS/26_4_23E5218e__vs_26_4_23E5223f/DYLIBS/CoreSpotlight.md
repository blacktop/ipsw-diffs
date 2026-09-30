## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2418.4.10.1.0
-  __TEXT.__text: 0xe9550
-  __TEXT.__auth_stubs: 0x1d60
+2418.4.11.100.0
+  __TEXT.__text: 0xe9518
+  __TEXT.__auth_stubs: 0x1d50
   __TEXT.__objc_methlist: 0xd850
   __TEXT.__const: 0xd00
-  __TEXT.__cstring: 0x148f3
+  __TEXT.__cstring: 0x14682
   __TEXT.__gcc_except_tab: 0x2f94
   __TEXT.__oslogstring: 0x84be
   __TEXT.__dlopen_cstrs: 0x49b

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0xd90
-  __AUTH_CONST.__auth_got: 0xec8
+  __AUTH_CONST.__auth_got: 0xec0
   __AUTH_CONST.__const: 0x1a50
   __AUTH_CONST.__cfstring: 0x13e40
   __AUTH_CONST.__objc_const: 0x11fd8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7E1121EC-F294-3600-9F94-FF719A118C30
+  UUID: C552A9A7-559E-307B-92A2-53C94A15A009
   Functions: 5907
-  Symbols:   18687
-  CStrings:  12940
+  Symbols:   18686
+  CStrings:  12938
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__19__sift_upB9nqe210106INS_17_ClassicAlgPolicyERN12_GLOBAL__N_118WorkItemComparatorENS_11__wrap_iterIPNS2_8WorkItemEEEEEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__19__sift_upB9foe210106INS_17_ClassicAlgPolicyERN12_GLOBAL__N_118WorkItemComparatorENS_11__wrap_iterIPNS2_8WorkItemEEEEEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ -[CSRequestQueue processWorkItemsUpToRequestID:] : 524 -> 468
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIZugATEuOG37tyocnHKROXT_9XKJiQQrSEavg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIZugATEuOG37tyocnHKROXT_9XKJiQQrSEavg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"

```
