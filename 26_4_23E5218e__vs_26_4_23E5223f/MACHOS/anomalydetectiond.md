## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-150.0.6.0.0
-  __TEXT.__text: 0x3553c8
-  __TEXT.__auth_stubs: 0x16b0
+150.0.7.0.0
+  __TEXT.__text: 0x34fb68
+  __TEXT.__auth_stubs: 0x16a0
   __TEXT.__objc_stubs: 0x9480
   __TEXT.__objc_methlist: 0x8d98
-  __TEXT.__gcc_except_tab: 0x11f08
-  __TEXT.__const: 0x441be
-  __TEXT.__cstring: 0x1d338
+  __TEXT.__gcc_except_tab: 0x11e80
+  __TEXT.__const: 0x441ce
+  __TEXT.__cstring: 0x1afb6
   __TEXT.__oslogstring: 0x1113b
   __TEXT.__objc_classname: 0x10ce
   __TEXT.__objc_methtype: 0x5f66
   __TEXT.__objc_methname: 0xc218
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc3d8
+  __TEXT.__unwind_info: 0xc3c8
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb70
+  __DATA_CONST.__auth_got: 0xb68
   __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x25558
-  __DATA_CONST.__cfstring: 0x6aa0
+  __DATA_CONST.__cfstring: 0x6a20
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 326C0F9D-682F-330A-BB21-696D4F48B951
-  Functions: 16396
-  Symbols:   573
-  CStrings:  9984
+  UUID: D192BD81-89FC-3461-8A9E-FE8E14D57A62
+  Functions: 16385
+  Symbols:   572
+  CStrings:  9950
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1530: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRsugA_sp4qh-PsoMHjtzEV54qbWShVw7kKWl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "alertTriggerProbability"
- "envMovementTriggerProbability"
- "metadataHarvestTriggerProbability"
- "motionTriggerProbability"

```
