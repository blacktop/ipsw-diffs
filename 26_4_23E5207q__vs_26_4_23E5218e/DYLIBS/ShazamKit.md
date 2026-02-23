## ShazamKit

> `/System/Library/Frameworks/ShazamKit.framework/ShazamKit`

```diff

-426.4.31.0.0
-  __TEXT.__text: 0x97368
-  __TEXT.__auth_stubs: 0x1cb0
+426.4.35.1.0
+  __TEXT.__text: 0x97728
+  __TEXT.__auth_stubs: 0x1dd0
   __TEXT.__objc_methlist: 0x5028
   __TEXT.__const: 0x21887
-  __TEXT.__cstring: 0x5dd4
+  __TEXT.__cstring: 0x5de4
   __TEXT.__gcc_except_tab: 0x3ba4
-  __TEXT.__oslogstring: 0x152b
+  __TEXT.__oslogstring: 0x155b
   __TEXT.__constg_swiftt: 0x5f0
   __TEXT.__swift5_typeref: 0xbd6
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x280
-  __TEXT.__unwind_info: 0x3330
-  __TEXT.__eh_frame: 0x1b48
+  __TEXT.__unwind_info: 0x3378
+  __TEXT.__eh_frame: 0x1bb8
   __TEXT.__objc_classname: 0xe06
   __TEXT.__objc_methname: 0xa893
   __TEXT.__objc_methtype: 0x207d
-  __TEXT.__objc_stubs: 0x7ca0
-  __DATA_CONST.__got: 0x720
+  __TEXT.__objc_stubs: 0x7c80
+  __DATA_CONST.__got: 0x728
   __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2478
+  __DATA_CONST.__objc_selrefs: 0x2470
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x240
-  __AUTH_CONST.__auth_got: 0xe70
+  __AUTH_CONST.__auth_got: 0xf00
   __AUTH_CONST.__const: 0x1c90
   __AUTH_CONST.__cfstring: 0x27a0
   __AUTH_CONST.__objc_const: 0x9ca0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x798
   __DATA.__objc_ivar: 0x4c0
   __DATA.__data: 0x1b24e0
-  __DATA.__bss: 0x1de8
+  __DATA.__bss: 0x1df8
   __DATA.__common: 0x1c8
   __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal
   - /System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E919F4EE-2B12-31C0-98B3-1B575719313D
-  Functions: 3383
-  Symbols:   9223
+  UUID: 74C16C5C-B0A9-3B77-9732-D44C37C62CEF
+  Functions: 3411
+  Symbols:   9220
   CStrings:  3105
 
Symbols:
+ -[SHSession isDurationValidForSignature:error:]
+ -[SHSession validateSignature:]
+ _objc_getAssociatedObject
+ _objc_msgSend$isDurationValidForSignature:error:
+ _objc_msgSend$validateSignature:
+ _objc_setAssociatedObject
+ _objc_sync_enter
+ _objc_sync_exit
+ _propertyCategoryMap
+ _swift_dynamicCastClass
+ _swift_isUniquelyReferenced_native
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_retain_n
+ _swift_unknownObjectRetain_n
+ _symbolic _____ySo11SHMediaItemCG 19CollectionsInternal10OrderedSetV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation4UUIDV
- -[SHSession _shouldAddSignatureForMatching:]
- -[SHSession validateSignature:error:]
- _URLProperties
- _booleanProperties
- _codableDictionaryProperties
- _dateProperties
- _locationCoordinateValueProperties
- _numberProperties
- _objc_msgSend$_shouldAddSignatureForMatching:
- _objc_msgSend$unionSet:
- _objc_msgSend$validateSignature:error:
- _rangeArrayProperties
- _signatureAlignmentArrayProperties
- _stringArrayProperties
- _stringProperties
- _symbolic ScTyyt_____GSg s5NeverO
- _symbolic _____Sg 10Foundation4DateV
- _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
- _uuidProperties
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugAVl5BFNS2pkqbjTw2jsvHijaUxmIlbD3U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "Signature(ID:%@, Duration:%f) is invalid and cannot be matched. Rejecting match request for %lu signature(s)"
+ "isDurationValidForSignature:error:"
+ "validateSignature:"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9SugCg_kgY2DAXn5027t4NmA6Bdi8H-Xg9Kpw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "No valid signatures to match after filtering %lu signatures"
- "_shouldAddSignatureForMatching:"
- "unionSet:"
- "validateSignature:error:"

```
