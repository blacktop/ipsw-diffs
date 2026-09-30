## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 1870.6.1.0.0
-  __TEXT.__text: 0x165ca0
-  __TEXT.__auth_stubs: 0x2460
+  __TEXT.__text: 0x169364
+  __TEXT.__auth_stubs: 0x2450
   __TEXT.__objc_stubs: 0x1efe0
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x10884
-  __TEXT.__gcc_except_tab: 0x54b0
-  __TEXT.__const: 0x18cf0
-  __TEXT.__cstring: 0x502c4
+  __TEXT.__gcc_except_tab: 0x54ac
+  __TEXT.__const: 0x18d00
+  __TEXT.__cstring: 0x4f2c6
   __TEXT.__objc_classname: 0x10da
   __TEXT.__objc_methname: 0x30733
   __TEXT.__objc_methtype: 0x7a90
   __TEXT.__dlopen_cstrs: 0x3ca
   __TEXT.__oslogstring: 0x90
   __TEXT.__unwind_info: 0x4b28
-  __DATA_CONST.__auth_got: 0x1248
+  __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x4e90
-  __DATA_CONST.__cfstring: 0x2dd00
+  __DATA_CONST.__cfstring: 0x2ddc0
   __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x518
-  __DATA_CONST.__objc_intobj: 0x3558
-  __DATA_CONST.__objc_arraydata: 0x12870
-  __DATA_CONST.__objc_arrayobj: 0x80d0
+  __DATA_CONST.__objc_intobj: 0x3570
+  __DATA_CONST.__objc_arraydata: 0x12930
+  __DATA_CONST.__objc_arrayobj: 0x81c0
   __DATA_CONST.__objc_dictobj: 0x7a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x1ae58

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D28E1F4C-27D6-3228-9A6B-68E8A13C830E
-  Functions: 7210
-  Symbols:   812
-  CStrings:  21509
+  UUID: 7022850B-049F-3EDA-A6D8-1A31D794CF5F
+  Functions: 7212
+  Symbols:   811
+  CStrings:  21510
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "CoEx-Table-AntBlockPwrLmt-Coex027a"
+ "CoEx-Table-AntBlockPwrLmt-Coex058"
+ "CoEx-Table-AntBlockPwrLmt-Coex059"
+ "CoEx-Table-CellCoex027a_V7WiFiEnh"
+ "CoEx-Table-CellCoex058_V8WiFiEnh"
+ "CoEx-Table-CellCoex059_V8WiFiEnh"
+ "sAntHybridiOS"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJl0ugCTzrAGMIKpGNJw5FIwaz19iaU1XuC8HO4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"

```
