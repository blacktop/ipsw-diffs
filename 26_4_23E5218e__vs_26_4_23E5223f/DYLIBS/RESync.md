## RESync

> `/System/Library/PrivateFrameworks/RESync.framework/RESync`

```diff

 403.100.11.0.0
-  __TEXT.__text: 0x7be70
-  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__text: 0x7bd44
+  __TEXT.__auth_stubs: 0xef0
   __TEXT.__objc_methlist: 0x2d4
   __TEXT.__const: 0x211f
-  __TEXT.__cstring: 0x7f67
+  __TEXT.__cstring: 0x722a
   __TEXT.__oslogstring: 0x4633
   __TEXT.__objc_classname: 0x6a
   __TEXT.__objc_methname: 0x8d8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0x3960
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x5e8

   - /usr/lib/libc++abi.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0C27C07-F92C-3B92-B0CA-5DEDE147FD08
+  UUID: E33BD6F4-513F-3B2E-BE29-9BC93CEB0208
   Functions: 2364
-  Symbols:   5962
-  CStrings:  1176
+  Symbols:   5961
+  CStrings:  1167
 
Symbols:
+ __ZNSt3__110__function12__value_funcIFbPKvPvEED2B9nqn210106Ev
+ __ZNSt3__110__function12__value_funcIFvPvEE4swapB9nqn210106ERS4_
+ __ZNSt3__110__function12__value_funcIFvPvEED2B9nqn210106Ev
+ __ZNSt3__110unique_ptrIN2re20SharedAppSyncManager9PeerStateENS1_11SyncDeleterIS3_EEE5resetB9nqn210106EPS3_
+ __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9nqn210106Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS7_EEENS3_ISB_EEED1B9nqn210106Ev
+ __ZNSt3__114__thread_proxyB9nqn210106INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS8_EEEEEPvSD_
+ __ZNSt3__125__throw_bad_function_callB9nqn210106Ev
+ __ZNSt3__127__insertion_sort_incompleteB9nqn210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEbT1_S9_T0_
+ __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZNSt3__110__function12__value_funcIFbPKvPvEED2B9fon210106Ev
- __ZNSt3__110__function12__value_funcIFvPvEE4swapB9fon210106ERS4_
- __ZNSt3__110__function12__value_funcIFvPvEED2B9fon210106Ev
- __ZNSt3__110unique_ptrIN2re20SharedAppSyncManager9PeerStateENS1_11SyncDeleterIS3_EEE5resetB9fon210106EPS3_
- __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9fon210106Ev
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS7_EEENS3_ISB_EEED1B9fon210106Ev
- __ZNSt3__114__thread_proxyB9fon210106INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS8_EEEEEPvSD_
- __ZNSt3__125__throw_bad_function_callB9fon210106Ev
- __ZNSt3__127__insertion_sort_incompleteB9fon210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEbT1_S9_T0_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZSt28__throw_bad_array_new_lengthB9fon210106v
Functions:
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerELb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb : 2592 -> 2292
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugDKeL9SyGgEs6qLrwq1KbcKfq4C7vdK1CI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"

```
