## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

 974.0.0.0.0
-  __TEXT.__text: 0xc8d1c
+  __TEXT.__text: 0xc8d2c
   __TEXT.__auth_stubs: 0x2c10
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0DD84830-1D2F-362B-B95D-B5E76CEF5CC1
-  Functions: 5351
+  UUID: 4A2DE413-0E7C-32AB-9888-935494ADDE9D
+  Functions: 5352
   Symbols:   16034
   CStrings:  12124
 
Functions:
+ sub_18e7b8ecc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7KugDHiLIzHE94n1UKorNts86baaSEBXxa7xE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/Bom/Common/BOMBufferManager.c"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/Bom/Common/BOMFile.c"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/Bom/Common/BOMStack.c"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/Bom/Storage/BOMStorage.c"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/Bom/Storage/BOMStream.c"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/Bom/Storage/BOMTree.c"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/CoreTheme/CUICatalog.m"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmap2Compression.m"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmapCompression.m"
+ "/Library/Caches/com.apple.xbs/5C6317AD-34D8-4154-9650-6A0E45BE296A/TemporaryDirectory.xY9zQL/Sources/CoreUI/CoreTheme/ImageUtils/CUIHEVCCompression.m"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugA5UveXzu-6i2LOMmHbUeSShQamy31vR5A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/Bom/Common/BOMBufferManager.c"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/Bom/Common/BOMFile.c"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/Bom/Common/BOMStack.c"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/Bom/Storage/BOMStorage.c"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/Bom/Storage/BOMStream.c"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/Bom/Storage/BOMTree.c"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/CoreTheme/CUICatalog.m"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmap2Compression.m"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmapCompression.m"
- "/Library/Caches/com.apple.xbs/3D1FF4F4-A534-4DD0-9845-E7FBCF02EA50/TemporaryDirectory.RY5WLH/Sources/CoreUI/CoreTheme/ImageUtils/CUIHEVCCompression.m"

```
