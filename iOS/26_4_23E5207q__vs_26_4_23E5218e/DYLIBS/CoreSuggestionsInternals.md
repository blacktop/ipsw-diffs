## CoreSuggestionsInternals

> `/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals`

```diff

-1311.4.1.0.0
-  __TEXT.__text: 0x2a2c40
+1311.5.0.1.0
+  __TEXT.__text: 0x2a2e90
   __TEXT.__auth_stubs: 0x33d0
   __TEXT.__objc_methlist: 0x15b14
   __TEXT.__const: 0x79ba

   __TEXT.__swift_as_ret: 0x40
   __TEXT.__gcc_except_tab: 0xaeb0
   __TEXT.__ustring: 0xc4
-  __TEXT.__unwind_info: 0x8918
-  __TEXT.__eh_frame: 0xbb8
+  __TEXT.__unwind_info: 0x8920
+  __TEXT.__eh_frame: 0xc30
   __TEXT.__objc_classname: 0x2b14
   __TEXT.__objc_methname: 0x3d8a9
   __TEXT.__objc_methtype: 0x7306
   __TEXT.__objc_stubs: 0x2bc20
   __DATA_CONST.__got: 0x24f0
-  __DATA_CONST.__const: 0xb640
+  __DATA_CONST.__const: 0xb638
   __DATA_CONST.__objc_classlist: 0xb58
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x208

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 59F93944-7C51-39A1-9674-8F3F6479E628
-  Functions: 10614
+  UUID: B852665F-5DFB-36DA-BD36-393303B8A317
+  Functions: 10619
   Symbols:   35089
   CStrings:  23277
 
Symbols:
+ ___42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.335
+ ___42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.336
+ ___42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.337
+ ___Block_byref_object_copy_.42578
+ ___Block_byref_object_dispose_.42579
+ ___block_literal_global.42539
+ ___block_literal_global.42740
+ ___block_literal_global.43216
- ___42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.296
- ___42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.297
- ___42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.298
- ___Block_byref_object_copy_.42582
- ___Block_byref_object_dispose_.42583
- ___block_literal_global.42540
- ___block_literal_global.42744
- ___block_literal_global.43220
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_CoreSuggestionsInternals
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI8xugBsT_cHQaBuTq24iDMEe2JolaTOHR0pnJw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI8xugBsT_cHQaBuTq24iDMEe2JolaTOHR0pnJw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI8xugBsT_cHQaBuTq24iDMEe2JolaTOHR0pnJw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI8xugBsT_cHQaBuTq24iDMEe2JolaTOHR0pnJw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI8xugBsT_cHQaBuTq24iDMEe2JolaTOHR0pnJw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/11682005-0243-4D9D-AE95-F5BDF8C63CE1/TemporaryDirectory.gOqAHK/Sources/Suggestions/re2/re2/re2_nfa.cc"
+ "/Library/Caches/com.apple.xbs/11682005-0243-4D9D-AE95-F5BDF8C63CE1/TemporaryDirectory.gOqAHK/Sources/Suggestions/re2/re2/re2_prefilter.h"
+ "/Library/Caches/com.apple.xbs/11682005-0243-4D9D-AE95-F5BDF8C63CE1/TemporaryDirectory.gOqAHK/Sources/Suggestions/re2/re2/re2_regexp.h"
- "/AppleInternal/Library/BuildRoots/4~CIA_ugA6HjqP4EsS82-SxJU0BuFhf1a_9vjazgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIA_ugA6HjqP4EsS82-SxJU0BuFhf1a_9vjazgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIA_ugA6HjqP4EsS82-SxJU0BuFhf1a_9vjazgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CIA_ugA6HjqP4EsS82-SxJU0BuFhf1a_9vjazgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CIA_ugA6HjqP4EsS82-SxJU0BuFhf1a_9vjazgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/Library/Caches/com.apple.xbs/38294F2A-79F7-4E7E-9F10-874062AAFA0D/TemporaryDirectory.REgJM9/Sources/Suggestions/re2/re2/re2_nfa.cc"
- "/Library/Caches/com.apple.xbs/38294F2A-79F7-4E7E-9F10-874062AAFA0D/TemporaryDirectory.REgJM9/Sources/Suggestions/re2/re2/re2_prefilter.h"
- "/Library/Caches/com.apple.xbs/38294F2A-79F7-4E7E-9F10-874062AAFA0D/TemporaryDirectory.REgJM9/Sources/Suggestions/re2/re2/re2_regexp.h"

```
