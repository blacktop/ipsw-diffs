## AppleMediaServicesKitInternal

> `/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal`

```diff

-1.4.26.0.0
-  __TEXT.__text: 0x54b99c
+1.4.27.0.0
+  __TEXT.__text: 0x54b1cc
   __TEXT.__auth_stubs: 0x2570
   __TEXT.__objc_methlist: 0xf04
-  __TEXT.__const: 0x3d100
+  __TEXT.__const: 0x3d280
   __TEXT.__swift5_typeref: 0x1974
   __TEXT.__swift5_fieldmd: 0xf4c
   __TEXT.__constg_swiftt: 0x1104

   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x45c
   __TEXT.__swift5_types: 0x19c
-  __TEXT.__cstring: 0xc99b
+  __TEXT.__cstring: 0xbbb5
   __TEXT.__oslogstring: 0x9eb
   __TEXT.__swift_as_entry: 0x1f8
   __TEXT.__swift_as_ret: 0x1f0
   __TEXT.__swift5_capture: 0x198
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__gcc_except_tab: 0x218bc
-  __TEXT.__unwind_info: 0xb150
+  __TEXT.__gcc_except_tab: 0x21920
+  __TEXT.__unwind_info: 0xb160
   __TEXT.__eh_frame: 0x40ec
   __TEXT.__objc_classname: 0x61f
   __TEXT.__objc_methname: 0x233d

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 52CB73D0-0F91-3AD3-932C-9065E85D7831
-  Functions: 9024
+  UUID: 206DCF25-EF62-3FE5-890E-7ACE27D58248
+  Functions: 9021
   Symbols:   612
-  CStrings:  2496
+  CStrings:  2488
 
Symbols:
+ _os_transaction_create
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "1.4.27"
+ "AMSCoreBridge::FirstPartyDataProviderWrapper"
+ "AMSCoreBridge::FirstPartyHTTPCacheProviderWrapper"
+ "AMSCoreBridge::FirstPartyStructuredDataProviderWrapper"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:799: libc++ Hardening assertion this->__has_val() failed: expected::operator-> requires the expected to contain a value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:811: libc++ Hardening assertion this->__has_val() failed: expected::operator* requires the expected to contain a value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:873: libc++ Hardening assertion !this->__has_val() failed: expected::error requires the expected to contain an error\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJIfugDukb_Iv_WQ8uwNPhFoYNClSfyTG7yINOc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "1.4.26"

```
