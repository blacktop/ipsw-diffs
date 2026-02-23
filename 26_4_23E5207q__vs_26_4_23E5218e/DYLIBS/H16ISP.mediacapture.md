## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-5.401.2.0.0
-  __TEXT.__text: 0x1cf46c
+5.403.0.0.0
+  __TEXT.__text: 0x1cf4a8
   __TEXT.__auth_stubs: 0x32b0
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x2864f
+  __TEXT.__const: 0x2863f
   __TEXT.__oslogstring: 0x1dcf9
   __TEXT.__cstring: 0x1a8e0
   __TEXT.__gcc_except_tab: 0x72a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 40A20CEB-83BA-3CCF-AE35-064E6E485DE9
+  UUID: 5D5E1E46-710C-34BB-87A3-C282C2CDD18A
   Functions: 5936
   Symbols:   15309
   CStrings:  8046
Functions:
~ __ZN6H16ISP37H16ISPGraphExclaveObjectDetectionNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE : 716 -> 752
~ __ZL24inputCallbackForGrimaldiPvPjPK14AudioTimeStampjjP15AudioBufferList : 2720 -> 2724
~ __ZL32inputCallbackForGrimaldiHighFreqPvPjPK14AudioTimeStampjjP15AudioBufferList : 3048 -> 3052
~ __ZN6H16ISP12H16ISPDevice27CreateISPUnitInfoDictionaryEPP14__CFDictionaryb : 3724 -> 3740
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAcTjTQpd5FFYfSpPZg0lwalxHOzscKAxE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
