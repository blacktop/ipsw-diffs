## RenderBox

> `/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox`

```diff

-7.4.19.0.0
-  __TEXT.__text: 0x155174
+7.4.23.0.0
+  __TEXT.__text: 0x1552e8
   __TEXT.__auth_stubs: 0x2930
   __TEXT.__objc_methlist: 0x2c9c
   __TEXT.__const: 0x5d48
   __TEXT.__gcc_except_tab: 0x7a8c
   __TEXT.__cstring: 0x7c0e
   __TEXT.__oslogstring: 0x10d5
-  __TEXT.__unwind_info: 0x6548
+  __TEXT.__unwind_info: 0x6550
   __TEXT.__objc_classname: 0x496
   __TEXT.__objc_methname: 0x657b
   __TEXT.__objc_methtype: 0x364c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7A9D012-789B-3B49-BD94-1B7F1E03B0C2
-  Functions: 7051
-  Symbols:   18638
+  UUID: 5A8D949A-07E1-3EBB-A9ED-BD0A5F93B757
+  Functions: 7054
+  Symbols:   18644
   CStrings:  3729
 
Symbols:
+ GCC_except_table106
+ GCC_except_table134
+ GCC_except_table78
+ GCC_except_table95
+ __ZN2RB6Device14alloc_frame_idEv
+ __ZN2RB6Device15purge_resourcesEv
+ __ZN2RB6Device19RenderPipelineEntry6Loader13load_pipelineEv
- GCC_except_table105
- GCC_except_table108
- GCC_except_table120
- GCC_except_table76
- GCC_except_table84
- GCC_except_table99
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:360: libc++ Hardening assertion __idx < size() failed: span<T, N>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:538: libc++ Hardening assertion !empty() failed: span<T>::front() on empty span\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:543: libc++ Hardening assertion !empty() failed: span<T>::back() on empty span\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIqugDeqUD29RRvRy4l2HaYBmm9gzaYHD8Y5yc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "7.4.23"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:360: libc++ Hardening assertion __idx < size() failed: span<T, N>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:538: libc++ Hardening assertion !empty() failed: span<T>::front() on empty span\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:543: libc++ Hardening assertion !empty() failed: span<T>::back() on empty span\n"
- "/AppleInternal/Library/BuildRoots/4~CH9bugDrOempma3ftkk8e3ThhUomfcNqURH5wXE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "7.4.19"

```
