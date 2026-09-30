## AppleMIDINetworkDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDINetworkDriver.plugin/AppleMIDINetworkDriver`

```diff

 324.501.0.5.0
-  __TEXT.__text: 0x3a950
-  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__text: 0x39694
+  __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x3ae8
-  __TEXT.__const: 0x478
+  __TEXT.__gcc_except_tab: 0x3ab0
+  __TEXT.__const: 0x488
   __TEXT.__oslogstring: 0x1bd5
-  __TEXT.__cstring: 0x3e18
+  __TEXT.__cstring: 0x1358
   __TEXT.__objc_methname: 0x136
-  __TEXT.__unwind_info: 0x12d0
-  __DATA_CONST.__auth_got: 0x830
+  __TEXT.__unwind_info: 0x12a0
+  __DATA_CONST.__auth_got: 0x828
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0xe90
   __DATA_CONST.__cfstring: 0x640

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9634F83D-2B58-372D-B954-0AD6F351B8FC
-  Functions: 714
-  Symbols:   323
-  CStrings:  412
+  UUID: 3E4E4FE0-790C-3E40-BB64-E59D4BBB6FCE
+  Functions: 697
+  Symbols:   322
+  CStrings:  380
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/D6AD8D47-3404-47DA-BE62-AF905F39A037/TemporaryDirectory.RVu04Y/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventConversion.h: 656"
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/D6AD8D47-3404-47DA-BE62-AF905F39A037/TemporaryDirectory.RVu04Y/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventList.h: 76"
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/D6AD8D47-3404-47DA-BE62-AF905F39A037/TemporaryDirectory.RVu04Y/Sources/CoreMIDI_Drivers/Source/MIDI/Drivers/Network/RTP/MIDIRTPSession.cpp: 1738"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__iterator/counted_iterator.h:108: libc++ Hardening assertion __count_ > 0 failed: Iterator is equal to or past end.\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__ranges/view_interface.h:122: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.front()` called on an empty view.\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAK-o982NWb88PM0XM4GUp3tD8pOvlTUdM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/54C8C434-25BC-485F-830F-BF215F31C383/TemporaryDirectory.coHjfK/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventConversion.h: 656"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/54C8C434-25BC-485F-830F-BF215F31C383/TemporaryDirectory.coHjfK/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventList.h: 76"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/54C8C434-25BC-485F-830F-BF215F31C383/TemporaryDirectory.coHjfK/Sources/CoreMIDI_Drivers/Source/MIDI/Drivers/Network/RTP/MIDIRTPSession.cpp: 1738"

```
