## AppleCVHWA

> `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`

```diff

-4.3.6.0.0
-  __TEXT.__text: 0xb45d8
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__const: 0x2eb8
-  __TEXT.__gcc_except_tab: 0x5958
+4.3.7.0.0
+  __TEXT.__text: 0xc4590
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__const: 0x2a58
+  __TEXT.__gcc_except_tab: 0x5730
   __TEXT.__oslogstring: 0x349
-  __TEXT.__cstring: 0x810a
+  __TEXT.__cstring: 0xbfd5
   __TEXT.__unwind_info: 0x16f0
-  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_methname: 0x25
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1498
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 729D15F9-C0BF-3A82-A602-A717696E4884
-  Functions: 1101
-  Symbols:   446
-  CStrings:  608
+  UUID: 3934EF5B-1019-3F21-8319-B1253E946634
+  Functions: 1114
+  Symbols:   443
+  CStrings:  640
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retain_x19
+ _objc_retain_x22
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
- _memset_pattern16
- _objc_release_x21
- _objc_retain
- _objc_retain_x1
- _objc_retain_x21
CStrings:
+ "/"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBTzzyDBm8V_T_bkPsieX2zBzKGC9Aqp5Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/Essentials/Apple/src/BundlePath.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/AppleUtil/src/CvPixelBufferPoolUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/AppleUtil/src/CvPixelBufferTransferSession.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/AppleUtil/src/CvPixelBufferUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/ComputerVisionTypes/include/VIO/ComputerVisionTypes/Image.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/FeatureDetection/include/VIO/FeatureDetection/DoGFeatureDetector_impl.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/FeatureDetection/src/KeyEngineUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwCvdAllConfigurationUtils.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwCvdAllConfigurationUtilsImpl.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwDesgenConfigurationUtilsImpl.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwDesgenUtils.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwIspDataHandler.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwPlatformInterface.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwPlatformUtils.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwProcessOutputUtilsImpl.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwColl.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCrete.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCreteUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCvdAllConfigurationUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDebugUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDesgen.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDesgenConfigurationUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDesgenUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwFeatureExtraction.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwFeatureExtractionInterface.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwGPWrapper.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwGeneralProcessingAPI.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwIspDataHandler.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwKeyConfigurationUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwKeyDoGFeatureDetector.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwKeyEngine.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwLaccUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwPlatformUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwTahiti.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwThera-V53.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetectionUtils/include/VIO/HWFeatureDetectionUtils/HwFeatureExtractionCommon.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/HWFeatureDetectionUtils/src/HwKeyHeaderParser.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/include/VIO/Hardware/KeyPointAndDescriptorGeneratorUtils.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/include/VIO/Hardware/KeyPointDescriptorStore.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/include_private/VIO/Hardware/KeyPointAndDescriptorMatcherUtils.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/CollKPValidatorAndRefiner.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/CollKeyPointAndDescriptorMatcher.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/CollKeyPointToDescriptor.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/DescriptorTidAssignment.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/GaussianPyramidGenerator.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/GaussianPyramidGeneratorUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KPAndDescriptorGeneratorInterface.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KPValidatorAndRefiner.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KPValidatorAndRefinerUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointAndDescriptorGenerator.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointAndDescriptorGeneratorUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointAndDescriptorMatcher.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointDescriptorStore.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointToDescriptor.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/Hardware/src/ResponseMapAndKPCGenerator.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/ImageProcessing/include/VIO/ImageProcessing/ConvolutionsFixedPoint.h"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/ImageProcessing/include/VIO/ImageProcessing/PyramidScaleSpace.hpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/library/VIO/VisionHWAccelerationServicesUtils/src/VisionHWAServicesXPCUtils.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/product/AppleCVHWA/AppleCVHWA/src/CVHWAFeatureExtraction.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/product/AppleCVHWA/AppleCVHWA/src/CVHWAFeatureExtractionConfig.cpp"
+ "/Library/Caches/com.apple.xbs/120316ED-46B4-4104-AC52-AED251A72B63/TemporaryDirectory.PcRMRJ/Sources/AppleCVHWA/product/AppleCVHWA/AppleCVHWA/src/CVHWAFeatureExtractionHwBufferInfo.cpp"
+ "Out.rslt"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/Essentials/Apple/src/BundlePath.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/AppleUtil/src/CvPixelBufferPoolUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/AppleUtil/src/CvPixelBufferTransferSession.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/AppleUtil/src/CvPixelBufferUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/ComputerVisionTypes/include/VIO/ComputerVisionTypes/Image.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/FeatureDetection/include/VIO/FeatureDetection/DoGFeatureDetector_impl.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/FeatureDetection/src/KeyEngineUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwCvdAllConfigurationUtils.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwCvdAllConfigurationUtilsImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwDesgenConfigurationUtilsImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwDesgenUtils.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwIspDataHandler.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwPlatformInterface.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwPlatformUtils.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwProcessOutputUtilsImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwColl.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCrete.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCreteUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCvdAllConfigurationUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDebugUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDesgen.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDesgenConfigurationUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwDesgenUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwFeatureExtraction.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwFeatureExtractionInterface.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwGPWrapper.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwGeneralProcessingAPI.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwIspDataHandler.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwKeyConfigurationUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwKeyDoGFeatureDetector.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwKeyEngine.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwLaccUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwPlatformUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwTahiti.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwThera-V53.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetectionUtils/include/VIO/HWFeatureDetectionUtils/HwFeatureExtractionCommon.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetectionUtils/src/HwKeyHeaderParser.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/include/VIO/Hardware/KeyPointAndDescriptorGeneratorUtils.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/include/VIO/Hardware/KeyPointDescriptorStore.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/include_private/VIO/Hardware/KeyPointAndDescriptorMatcherUtils.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/CollKPValidatorAndRefiner.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/CollKeyPointAndDescriptorMatcher.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/CollKeyPointToDescriptor.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/DescriptorTidAssignment.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/GaussianPyramidGenerator.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/GaussianPyramidGeneratorUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KPAndDescriptorGeneratorInterface.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KPValidatorAndRefiner.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KPValidatorAndRefinerUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointAndDescriptorGenerator.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointAndDescriptorGeneratorUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointAndDescriptorMatcher.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointDescriptorStore.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/KeyPointToDescriptor.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/Hardware/src/ResponseMapAndKPCGenerator.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/ImageProcessing/include/VIO/ImageProcessing/ConvolutionsFixedPoint.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/ImageProcessing/include/VIO/ImageProcessing/PyramidScaleSpace.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/VisionHWAccelerationServicesUtils/src/VisionHWAServicesXPCUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/product/AppleCVHWA/AppleCVHWA/src/CVHWAFeatureExtraction.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/product/AppleCVHWA/AppleCVHWA/src/CVHWAFeatureExtractionConfig.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/product/AppleCVHWA/AppleCVHWA/src/CVHWAFeatureExtractionHwBufferInfo.cpp"

```
