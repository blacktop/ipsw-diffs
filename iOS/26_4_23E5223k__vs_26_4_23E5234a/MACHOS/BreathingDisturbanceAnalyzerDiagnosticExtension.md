## BreathingDisturbanceAnalyzerDiagnosticExtension

> `/System/Library/PrivateFrameworks/BreathingAlgorithms.framework/PlugIns/BreathingDisturbanceAnalyzerDiagnosticExtension.appex/BreathingDisturbanceAnalyzerDiagnosticExtension`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0xc944
-  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__text: 0xc18c
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0xaae
-  __TEXT.__gcc_except_tab: 0xc54
-  __TEXT.__cstring: 0x18bd
+  __TEXT.__const: 0xab6
+  __TEXT.__gcc_except_tab: 0xc4c
+  __TEXT.__cstring: 0xa71
   __TEXT.__oslogstring: 0x774
   __TEXT.__objc_classname: 0x79
   __TEXT.__objc_methname: 0x56f
   __TEXT.__objc_methtype: 0x8c
-  __TEXT.__unwind_info: 0x4e0
-  __DATA_CONST.__auth_got: 0x388
+  __TEXT.__unwind_info: 0x4c8
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__cfstring: 0x2e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0CFE37B-FA64-3D24-A76F-346EAECFF241
-  Functions: 267
-  Symbols:   195
-  CStrings:  291
+  UUID: C4A74378-966B-3ECB-8611-43142C7268E2
+  Functions: 262
+  Symbols:   194
+  CStrings:  280
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlcugDxZF8frNH0nNyxCUlERFB4PklurIcQlaA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"

```
