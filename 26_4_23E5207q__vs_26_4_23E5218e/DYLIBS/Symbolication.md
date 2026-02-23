## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64575.66.1.0.0
-  __TEXT.__text: 0xb97a4
+64575.69.1.0.0
+  __TEXT.__text: 0xb9bf8
   __TEXT.__auth_stubs: 0x20b0
-  __TEXT.__objc_methlist: 0x6858
+  __TEXT.__objc_methlist: 0x6860
   __TEXT.__const: 0x2f6
-  __TEXT.__gcc_except_tab: 0x51bc
-  __TEXT.__cstring: 0x11850
+  __TEXT.__gcc_except_tab: 0x526c
+  __TEXT.__cstring: 0x11860
   __TEXT.__oslogstring: 0x187c
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2cb0
+  __TEXT.__unwind_info: 0x2cb8
   __TEXT.__objc_classname: 0x910
-  __TEXT.__objc_methname: 0x105ba
+  __TEXT.__objc_methname: 0x1060a
   __TEXT.__objc_methtype: 0x6971
-  __TEXT.__objc_stubs: 0xa620
-  __DATA_CONST.__got: 0x498
+  __TEXT.__objc_stubs: 0xa640
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x3b60
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3908
+  __DATA_CONST.__objc_selrefs: 0x3918
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0x1070
   __AUTH_CONST.__const: 0x11f8
-  __AUTH_CONST.__cfstring: 0xe060
+  __AUTH_CONST.__cfstring: 0xe080
   __AUTH_CONST.__objc_const: 0xc540
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: ED1CAC9C-0D75-34C2-A7CF-4B8427768693
-  Functions: 3280
-  Symbols:   11064
-  CStrings:  8068
+  UUID: 1E7CB4FF-55C5-347C-84AE-2B7FA5F901AF
+  Functions: 3281
+  Symbols:   11069
+  CStrings:  8072
 
Symbols:
+ +[VMUProcessDescription buildBinaryImagePathToUUIDDictFromBinaryImagesDescription:]
+ GCC_except_table60
+ _OBJC_CLASS_$_NSUUID
+ ___Block_byref_object_copy_.27
+ ___Block_byref_object_copy_.75
+ ___Block_byref_object_dispose_.28
+ ___Block_byref_object_dispose_.76
+ ___block_literal_global.127
+ ___block_literal_global.148
+ _objc_msgSend$initWithUUIDString:
- GCC_except_table26
- ___Block_byref_object_copy_.17
- ___Block_byref_object_copy_.65
- ___Block_byref_object_dispose_.18
- ___Block_byref_object_dispose_.66
- ___block_literal_global.117
- ___block_literal_global.138
Functions:
~ +[VMUProcessDescription parseBinaryImagesDescription:] : 504 -> 1104
+ +[VMUProcessDescription buildBinaryImagePathToUUIDDictFromBinaryImagesDescription:]
CStrings:
+ "%@-%@-%@-%@-%@"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugA032YpM6eRMQiBUieUp7zWtypcG5HqZBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "buildBinaryImagePathToUUIDDictFromBinaryImagesDescription:"
+ "initWithUUIDString:"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH-dugBVf_-8Ky_CSeZQPE7RREbkBjgPgle75bQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"

```
