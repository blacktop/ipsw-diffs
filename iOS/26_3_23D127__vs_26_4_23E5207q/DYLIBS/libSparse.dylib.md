## libSparse.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib`

```diff

 184.80.2.0.0
-  __TEXT.__text: 0x1651bc
+  __TEXT.__text: 0x187754
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__const: 0x760
-  __TEXT.__cstring: 0x4d1d
+  __TEXT.__const: 0x6d0
+  __TEXT.__cstring: 0x6229
   __TEXT.__oslogstring: 0x1c5d
-  __TEXT.__gcc_except_tab: 0xa4c
-  __TEXT.__unwind_info: 0x1768
-  __TEXT.__eh_frame: 0x8b0
+  __TEXT.__gcc_except_tab: 0xa98
+  __TEXT.__unwind_info: 0x1760
+  __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0xad0
   __AUTH_CONST.__auth_got: 0x628

   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B4007CC8-DD82-3559-B2BC-1FF9BBCB0513
-  Functions: 1944
+  UUID: AC05F3B0-763A-39CD-B8EB-C57F3C20D674
+  Functions: 1980
   Symbols:   676
-  CStrings:  694
+  CStrings:  709
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- ___udivti3
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDZ64AOggb3ExaQSQHtgzibpp3sMA0VMpI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/Library/Caches/com.apple.xbs/9A7C1740-7CF5-4511-8276-7B1B58078511/TemporaryDirectory.enqyYB/Sources/Sparse/MTMetis/metis/libmetis/kwayfm.c"
- "/Library/Caches/com.apple.xbs/Sources/Sparse/MTMetis/metis/libmetis/kwayfm.c"

```
