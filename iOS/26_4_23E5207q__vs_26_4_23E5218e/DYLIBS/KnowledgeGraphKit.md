## KnowledgeGraphKit

> `/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit`

```diff

-840.1.220.0.0
-  __TEXT.__text: 0xf2e44
+840.1.250.0.0
+  __TEXT.__text: 0xf2e3c
   __TEXT.__auth_stubs: 0x2350
   __TEXT.__objc_methlist: 0x6c7c
   __TEXT.__const: 0x5cec

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 82A909D2-50D0-329C-AAE0-88AE943CD998
+  UUID: 43D0802A-9E1E-322F-97CD-BC543281B673
   Functions: 6133
   Symbols:   11290
   CStrings:  3335
Functions:
~ sub_25ecf82b8 -> sub_25f9292b8 : 656 -> 644
~ sub_25ed1cd60 -> sub_25f94dd54 : 1072 -> 1064
~ sub_25ed1d400 -> sub_25f94e3ec : 460 -> 448
~ sub_25ed1da80 -> sub_25f94ea60 : 552 -> 540
~ sub_25ed1de6c -> sub_25f94ee40 : 504 -> 492
~ sub_25ed21610 -> sub_25f9525d8 : 248 -> 260
~ sub_25ed21708 -> sub_25f9526dc : 316 -> 340
~ sub_25ed21844 -> sub_25f952830 : 248 -> 260
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJalugCzDJSf1bEUzXROVapF_gYy5HRHsZm_3tA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/Library/Caches/com.apple.xbs/9DAC3AF5-D2AD-4A54-9FB4-D3D1FF2661E8/TemporaryDirectory.a8Svlp/Sources/Photos/workspaces/photoanalysis/PhotosGraph/Modules/Matisse/Framework/Learning/Feature Extraction/MARelationFeatureExtractor.m"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIh6ugARERO5IA4ZNoSyIAfiLURhuI80q5dCA8k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/photoanalysis/PhotosGraph/Modules/Matisse/Framework/Learning/Feature Extraction/MARelationFeatureExtractor.m"

```
