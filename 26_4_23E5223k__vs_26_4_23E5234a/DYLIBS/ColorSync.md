## ColorSync

> `/System/Library/Frameworks/ColorSync.framework/ColorSync`

```diff

 3813.3.3.0.0
-  __TEXT.__text: 0x5a530
-  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__text: 0x5a408
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__const: 0x122578
   __TEXT.__gcc_except_tab: 0xf64
-  __TEXT.__cstring: 0x660d
+  __TEXT.__cstring: 0x63a6
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x11d0
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x1ab8
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__const: 0x6dd0
   __AUTH_CONST.__cfstring: 0x48e0
   __DATA.__data: 0x810

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7E4962CF-7FCC-32C5-9065-E3763F86661B
+  UUID: DB5D23F5-9919-3FC4-BB62-2591EFB1F042
   Functions: 1537
-  Symbols:   4589
-  CStrings:  1394
+  Symbols:   4588
+  CStrings:  1392
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt12out_of_rangeC1B9nqe210106EPKc
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__120__throw_out_of_rangeB9nqe210106EPKc
+ __ZNSt3__16vectorI10CMMTagInfo10TAllocatorIS1_EE16__destroy_vectorclB9nqe210106Ev
+ __ZNSt3__16vectorI10CMMTagInfo10TAllocatorIS1_EE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI10CMMTagInfo10TAllocatorIS1_EE20__throw_out_of_rangeB9nqe210106Ev
+ __ZNSt3__16vectorI14CMMProfileInfo10TAllocatorIS1_EE16__destroy_vectorclB9nqe210106Ev
+ __ZNSt3__16vectorI14CMMProfileInfo10TAllocatorIS1_EE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI14CMMProfileInfo10TAllocatorIS1_EE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt12out_of_rangeC1B9foe210106EPKc
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__120__throw_out_of_rangeB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI10CMMTagInfo10TAllocatorIS1_EE16__destroy_vectorclB9foe210106Ev
- __ZNSt3__16vectorI10CMMTagInfo10TAllocatorIS1_EE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI10CMMTagInfo10TAllocatorIS1_EE20__throw_out_of_rangeB9foe210106Ev
- __ZNSt3__16vectorI14CMMProfileInfo10TAllocatorIS1_EE16__destroy_vectorclB9foe210106Ev
- __ZNSt3__16vectorI14CMMProfileInfo10TAllocatorIS1_EE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI14CMMProfileInfo10TAllocatorIS1_EE20__throw_out_of_rangeB9foe210106Ev
Functions:
~ _AppleCMMInitializeTransform : 2792 -> 2616
~ _AppleCMMInitializeLinkProfile : 3388 -> 3268
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJk5ugBfxB71SybPiO_F8MbX__yH9CyDvmjzw5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugBfxB71SybPiO_F8MbX__yH9CyDvmjzw5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"

```
