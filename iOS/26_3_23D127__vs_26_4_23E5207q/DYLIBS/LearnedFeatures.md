## LearnedFeatures

> `/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures`

```diff

-8.25.6.25.71
-  __TEXT.__text: 0x198bd4
-  __TEXT.__auth_stubs: 0x1310
-  __TEXT.__gcc_except_tab: 0x132d0
-  __TEXT.__cstring: 0x9eb3
-  __TEXT.__const: 0x16d17
-  __TEXT.__oslogstring: 0x34
-  __TEXT.__unwind_info: 0x6aa8
-  __TEXT.__eh_frame: 0xa0
-  __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x64
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0xd40
-  __DATA_CONST.__objc_classlist: 0x10
+8.25.12.16.0
+  __TEXT.__text: 0x224504
+  __TEXT.__auth_stubs: 0x14e0
+  __TEXT.__gcc_except_tab: 0x1447c
+  __TEXT.__cstring: 0xf041
+  __TEXT.__const: 0x17aef
+  __TEXT.__oslogstring: 0x87
+  __TEXT.__unwind_info: 0x7470
+  __TEXT.__eh_frame: 0x598
+  __TEXT.__objc_classname: 0xba
+  __TEXT.__objc_methname: 0x3d
+  __TEXT.__objc_stubs: 0xa0
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__const: 0x1060
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x998
-  __AUTH_CONST.__const: 0xe5f0
-  __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0x120
+  __DATA_CONST.__objc_selrefs: 0x28
+  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH_CONST.__const: 0xf1c8
+  __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__objc_const: 0x2d0
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x8
-  __DATA.__data: 0x7e0
+  __DATA.__data: 0x840
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x7d8
-  __DATA.__common: 0xd8
+  __DATA.__bss: 0x890
+  __DATA.__common: 0xb0
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D351B80-8D49-3E4B-A1B1-5BD7F33BE6BC
-  Functions: 4316
-  Symbols:   485
-  CStrings:  863
+  UUID: 2CBE2DB5-C378-3609-BA18-65A5BD645A6E
+  Functions: 5223
+  Symbols:   541
+  CStrings:  1023
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFBundleCopyBundleURL
+ _CFBundleCopyResourcesDirectoryURL
+ _CFNumberGetValue
+ _CFURLGetString
+ _LFV2DetectAndComputeFeaturesWithMaskAndRotateKeypoints
+ _LFV2KeypointsGetOrientationAt
+ _LFV2KeypointsGetScaleAt
+ _LFV2KeypointsGetScoreAt
+ _LFV2MatchDescriptors
+ _LFV2MatcherCopyLastError
+ _LFV2MatcherCopyLastErrorDescription
+ _LFV2MatcherHandleCreate
+ _LFV2MatcherHandleCreateWithOptions
+ _LFV2MatcherHandleRelease
+ _LFV2MatcherHandleSupported
+ _LFV2MatcherModelVersion
+ _LFV2MatchesAppend
+ _LFV2MatchesCreate
+ _LFV2MatchesGetQueryIndexAt
+ _LFV2MatchesGetReferenceIndexAt
+ _LFV2MatchesGetSize
+ _LFV2MatchesRelease
+ _LFV2MatchesRetain
+ _LFV2RetrievalAppend
+ _LFV2RetrievalCreate
+ _LFV2RetrievalGetDistanceAt
+ _LFV2RetrievalGetSize
+ _LFV2RetrievalIndexAt
+ _LFV2RetrievalRelease
+ _LFV2RetrievalRetain
+ _LFV2RetrievalTopK
+ __NSConcreteGlobalBlock
+ __ZNKSt3__14__fs10filesystem4path16__root_directoryEv
+ __ZNSt13runtime_errorC1ERKS_
+ __ZNSt3__117__assoc_sub_state12__make_readyEv
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ ___chkstk_darwin
+ ___cxa_get_exception_ptr
+ __get_cpu_capabilities
+ __os_log_default
+ __os_log_error_impl
+ _cblas_errprn
+ _cblas_scopy
+ _cblas_sdot
+ _cblas_sgemm
+ _cblas_sger
+ _cblas_sscal
+ _cblas_xerbla
+ _dispatch_once
+ _getenv
+ _malloc_type_aligned_alloc
+ _malloc_type_malloc
+ _malloc_type_valloc
+ _memset_pattern4
+ _objc_retainAutoreleasedReturnValue
+ _printf
+ _pthread_qos_max_parallelism
+ _qos_class_self
+ _strtol
+ _sysctlbyname
- _OBJC_CLASS_$_NSString
- _objc_autoreleaseReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x19
- _objc_release_x25
- _objc_release_x8
CStrings:
+ "  #"
+ " Unable to bind surface object to input port. Port name:"
+ " does not exist."
+ " for format with properties:\n"
+ " getting tensor shape for buffer for output port:"
+ " size "
+ "!mask.has_value()"
+ "'). "
+ "'. "
+ "': "
+ "*** ERROR *** CONTEXT ID is incorrect"
+ ", espresso_v2_initialized="
+ ", format OneComponent8: "
+ ", format="
+ ", height="
+ ", image "
+ ", model="
+ ". If using espresso.net model. Please try setting \"experimental.aot.enable_surface_desc\" : \"1\"  in model.espresso.net properties"
+ ". Valid combinations: (param+model+espresso_v2), (param only), or (none for defaults)"
+ ".disabled"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugAX-q_vGQg1c65nyzIpbUw9_dPKhKlspIw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Apple/src/BundleInfo.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Resource/src/Resource.mm"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp:56"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/BundleRef.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/Ptr.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/Ref.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/URLRef.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/include/Kit/IOSurface/View.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp:47"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/Image.h:1193"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/ImageStorage.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/Size.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ImageProcessing/src/NonMaximumSuppression.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/include/Kit/ML/DataView.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/DataView.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Execution.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Model.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoModelInstance.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoUtil.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2ModelInstance.mm"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2StreamPool.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/Kit/PixelFormat/include/Kit/PixelFormat/Properties.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/Common/src/FeaturesData.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/ATUDescriptorExtractor.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/ATUDescriptorModel.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/ATUDescriptorModelDefinition.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionCommonUtil.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionUtil.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorModelDefinition.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/IDescriptorModel.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/include_private/LearnedFeatures/EndToEndExtraction/Densefeat2.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/Densefeat2.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndExtractor.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndModel.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndUtils.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/FeatureExtraction/src/FeatureExtractor.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/FeatureExtractionApi/src/FeatureExtractionApiUtil.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointDetector.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointModel.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/include_private/LearnedFeatures/private/LearnedFeaturesConversion.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/src/LearnedFeaturesCommon.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/src/LearnedFeaturesInterface.mm"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/src/LearnedFeaturesMatcherInterface.mm"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/include/LearnedFeatures/PatchCropping/ImagePatches.h"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/src/PatchCropper.cpp"
+ "/Library/Caches/com.apple.xbs/4B4144E4-5ABF-4AEE-8647-E06AC58204F0/TemporaryDirectory.UwE4uT/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/src/SIMDCropper.cpp"
+ "; caused by:\n"
+ "APPLE_LAPACK_FILL_NAN"
+ "Binary not found for callable"
+ "Binary packed matching is not supported by this matcher"
+ "Binary packed matching method not implemented"
+ "Binary packed matching not supported by this matcher implementation"
+ "Bundle does not have a bundle identifier"
+ "CFErrorRef LFV2MatcherCopyLastError(LFV2MutableMatcherHandleRef)"
+ "CFStringRef LFV2MatcherCopyLastErrorDescription(LFV2MutableMatcherHandleRef)"
+ "Could not access bundle location from function pointer. Detail: "
+ "Could not access bundle location from obj-c class '"
+ "Densefeat2: Failed to create default mask image IOSurface with size "
+ "DepthDensefeat2ModelBundleIdentifier"
+ "EspressoV2"
+ "Failed to allocate buffer for FP32 output: "
+ "Failed to create "
+ "Failed to create HammingSecondNNMutualModel: "
+ "Failed to create HammingSecondNNMutualModel: Unknown error occurred"
+ "Failed to create ImageRetrievalTop15L2Model: "
+ "Failed to create ImageRetrievalTop15L2Model: Unknown error occurred"
+ "Failed to create buffer from surface: "
+ "Failed to create surface for buffer: "
+ "Failed to load bundle from "
+ "Failed to obtain executable path"
+ "Floating point matching method not implemented"
+ "Floating point matching not supported by this matcher implementation"
+ "HammingMutualMatcherModelBundleIdentifier"
+ "IOSurface"
+ "Image retrieval method not implemented"
+ "Image retrieval not supported by this matcher implementation"
+ "ImageRetrievalTop15L2Model only supports k=15, got k="
+ "ImageRetrievalTop15L2Model requires a mask to be provided"
+ "ImageRetrievalTop15L2ModelBundleIdentifier"
+ "Invalid argument combination: param="
+ "Invalid or unsupported matcher model type"
+ "IsValidInputImageResolution(mask.value().Size())"
+ "K cannot be less than zero 0, but has value %d."
+ "LFReturn LFV2DetectAndComputeFeaturesWithMaskAndRotateKeypoints(LFV2HandleRef, CVPixelBufferRef, CVPixelBufferRef, LFV2KeypointRotationArguments, LFV2FeaturesRef *)"
+ "LFReturn LFV2MatchDescriptors(LFV2MutableMatcherHandleRef, CVPixelBufferRef, CVPixelBufferRef, CVPixelBufferRef, LFV2MatchesRef *)"
+ "LFReturn LFV2MatcherHandleCreate(LFV2MutableMatcherHandleRef *, LFMatcherType, LFMatcherDeviceType)"
+ "LFReturn LFV2MatcherHandleCreateWithOptions(LFV2MutableMatcherHandleRef *, LFMatcherType, LFMatcherDeviceType, LFV2OptionsRef, CFErrorRef *)"
+ "LFReturn LFV2MatcherHandleRelease(LFV2MutableMatcherHandleRef)"
+ "LFReturn LFV2MatcherModelVersion(LFV2MutableMatcherHandleRef, LFMatcherVersion *)"
+ "LFReturn LFV2OptionsRelease(LFV2MutableOptionsRef)"
+ "LFReturn LFV2RetrievalTopK(LFV2MutableMatcherHandleRef, CVPixelBufferRef, CVPixelBufferRef, CVPixelBufferRef, LFV2RetrievalRef *)"
+ "M cannot be less than zero 0, but has value %d."
+ "ML model creation failed"
+ "ML model execution failed"
+ "ML model execution failed: "
+ "Mask is not supported for DetectAndComputeFeatures with no valid EndToEndExtractor."
+ "Mask must have {DATABASE_SIZE, 1} shape, got {"
+ "Mask support not yet implemented for DenseFeatModelBase"
+ "Mask support not yet implemented for GlobalFeatModel"
+ "Match indices must have {128, 1} shape, got {"
+ "Match validity must have {128, 1} shape, got {"
+ "Matcher model is not initialized"
+ "Model version is not available"
+ "Models/DepthDenseFeat/"
+ "Models/GloFeatMatch/"
+ "Models/LoFeatMatch/"
+ "N cannot be less than zero 0, but has value %d."
+ "No SecondNeirestNeighborRatio provided"
+ "No model loaded for HammingSecondNNMutualModel"
+ "No model loaded for ImageRetrievalTop15L2Model"
+ "Not EspressoV2 Compatible"
+ "Order must be %d or %d, but is set to %d."
+ "Properties are missing required arguments for surface creation. Required: width, height, format. Given: width="
+ "Query descriptors must have {128, 1} shape, got {"
+ "Query descriptors must have {64, 128} shape, got {"
+ "RearCameraOffsetFromDisplayCenter"
+ "Reference descriptors must have {128, DATABASE_SIZE} shape, got {"
+ "Reference descriptors must have {64, 128} shape, got {"
+ "Resource at "
+ "Return value != E5RT_ERROR_CODE_OK. "
+ "SecondNeirestNeighborRatio must have 1x1 shape, got "
+ "Top-K indices must have {15, 1} shape, got {"
+ "TransA must be %d, %d or %d, but is set to %d."
+ "TransB must be %d, %d or %d, but is set to %d."
+ "Unexpected exception when converting pixel buffer"
+ "VECLIB_MAXIMUM_THREADS"
+ "bundle_url"
+ "cblas_sgemm"
+ "cblas_sgemv"
+ "child_surface.Format() == Format(plane_index)"
+ "com.apple.cv3d"
+ "default_mask_df2"
+ "description"
+ "descriptor format is not supported"
+ "descriptor size is invalid"
+ "descriptors1"
+ "descriptors2"
+ "distances"
+ "e5def"
+ "enable_tensor_interface is set to true, but .net models do not support tensor interface (buffer objects). They require surface interface. Either use a .mil/.mlmodel model or set enable_tensor_interface to false."
+ "feature matching operation failed"
+ "file://"
+ "given "
+ "hw.cpufamily"
+ "hw.cpusubfamily"
+ "hw.perflevel0.cpusperl2"
+ "hw.perflevel0.l2cachesize"
+ "hw.perflevel0.physicalcpu_max"
+ "hw.perflevel1.cpusperl2"
+ "hw.perflevel1.l2cachesize"
+ "hw.perflevel1.physicalcpu_max"
+ "indices_fp16"
+ "lda must be >= MAX(K,1): lda=%d K=%d."
+ "lda must be >= MAX(M,1): lda=%d M=%d."
+ "ldb must be >= MAX(K,1): ldb=%d K=%d."
+ "ldb must be >= MAX(N,1): ldb=%d N=%d."
+ "ldc must be >= MAX(M,1): ldc=%d M=%d."
+ "ldc must be >= MAX(N,1): ldc=%d N=%d."
+ "lf-320x256"
+ "mask not supported with this feature type"
+ "mask_result"
+ "match_indices"
+ "matcher type is not supported"
+ "null"
+ "provided"
+ "pthread_qos_max_parallelism() returned error in LAPACK call to initHardwareInfo()\n"
+ "ptr_"
+ "resources_directory_url"
+ "second_nn_ratio"
+ "std::aligned_alloc failed to allocate "
+ "surface_factory"
+ "unexpected{"
+ "v8@?0"
+ "valid_matches"
+ "x"
- " (ENOMEM)"
- "' does not exist."
- ", used properties:\n"
- "/.disabled"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Apple/src/BundlePath.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/src/ArrayBuffer.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Resource/src/Resource.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp:56"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/BundleRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/Ptr.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/Ref.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/URLRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/include/Kit/IOSurface/View.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp:47"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/Image.h:1193"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/ImageStorage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/Size.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ImageProcessing/src/NonMaximumSuppression.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/include/Kit/ML/DataView.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/DataView.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Execution.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Model.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoModelInstance.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2ModelInstance.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2StreamPool.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/PixelFormat/include/Kit/PixelFormat/Properties.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/Common/src/FeaturesData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/ATUDescriptorExtractor.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/ATUDescriptorModel.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/ATUDescriptorModelDefinition.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionCommonUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorModelDefinition.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/IDescriptorModel.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/include_private/LearnedFeatures/EndToEndExtraction/Densefeat2.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/Densefeat2.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndExtractor.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndModel.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/FeatureExtraction/src/FeatureExtractor.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/FeatureExtractionApi/src/FeatureExtractionApiUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointDetector.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointModel.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/include_private/LearnedFeatures/private/LearnedFeaturesConversion.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/src/LearnedFeaturesInterface.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/include/LearnedFeatures/PatchCropping/ImagePatches.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/src/PatchCropper.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/src/SIMDCropper.cpp"
- ": error code "
- "Could not access bundle location"
- "Failed to create IOSurface for format "
- "Input "
- "LFReturn LFV2OptionsRelease(LFV2OptionsRef)"
- "Resource at '"
- "Unable to bind surface object to input port.Please set \"experimental.aot.enable_surface_desc\" : \"1\"  in model.espresso.net properties"
- "Unable to load program function: "
- "bundleWithPath:"
- "cf_current_bundle"
- "child_surface.Format() == surface.Format(plane_index)"
- "given IOSurface size "
- "mem_ret == E5RT_ERROR_CODE_OK"
- "posix_memalign failed to allocate "
- "resourcePath"
- "resources_path"
- "stringWithUTF8String:"
- "wrapper_path"

```
