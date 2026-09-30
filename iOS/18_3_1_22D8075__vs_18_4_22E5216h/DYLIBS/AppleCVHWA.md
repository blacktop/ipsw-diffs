## AppleCVHWA

> `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`

```diff

-3.6.9.0.0
-  __TEXT.__text: 0x8f414
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__const: 0x2c19
-  __TEXT.__gcc_except_tab: 0x36f8
-  __TEXT.__cstring: 0x7f89
-  __TEXT.__oslogstring: 0x15d3
-  __TEXT.__unwind_info: 0x18c8
-  __TEXT.__eh_frame: 0x80
+3.7.1.0.0
+  __TEXT.__text: 0xacd48
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__const: 0x2b49
+  __TEXT.__gcc_except_tab: 0x557c
+  __TEXT.__cstring: 0x7f59
+  __TEXT.__oslogstring: 0x1646
+  __TEXT.__unwind_info: 0x14d0
+  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_methname: 0x25
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xfd0
+  __AUTH_CONST.__const: 0x10c0
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__data: 0x94c0
+  __AUTH.__data: 0x20
+  __DATA.__data: 0x94ec
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x5e8
+  __DATA.__llvm_prf_cnts: 0x98
+  __DATA.__llvm_prf_data: 0x80
+  __DATA.__llvm_prf_names: 0x12b8
+  __DATA.__bss: 0x560
+  __DATA.__common: 0x20
+  __LLVM_COV.__llvm_covfun: 0xd6d6
+  __LLVM_COV.__llvm_covmap: 0x164
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
-  - /System/Library/Frameworks/ImageIO.framework/ImageIO
-  - /System/Library/Frameworks/Metal.framework/Metal
-  - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
-  - /System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1785
-  Symbols:   436
-  CStrings:  658
+  Functions: 991
+  Symbols:   437
+  CStrings:  676
 
Symbols:
+ _CFBundleCreate
+ _CFBundleGetValueForInfoDictionaryKey
+ _CFStringGetBytes
+ _CFStringGetLength
+ _CFURLCreateWithFileSystemPath
+ __NSGetExecutablePath
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNKSt3__14__fs10filesystem4path11__extensionEv
+ __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
+ __ZNKSt3__14__fs10filesystem4path9__compareENS_17basic_string_viewIcNS_11char_traitsIcEEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__14__fs10filesystem18__weakly_canonicalERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __ZnamSt11align_val_t
+ __os_log_pack_fill
+ __os_log_pack_size
+ __os_log_send_and_compose_impl
+ _dladdr
+ _kCFBundleIdentifierKey
+ _os_release
- _CFArrayGetCount
- _CFArrayGetTypeID
- _CFArrayGetValueAtIndex
- _CFDictionaryGetCount
- _CFDictionaryGetKeysAndValues
- _CFDictionaryGetTypeID
- _CFGetTypeID
- _CFStringGetTypeID
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt9exception4whatEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- _logf
- _strncpy
CStrings:
+ "%s"
+ "(expected_end <= start + kNumRegionOfInterestBlocks * block_size)"
+ "(start + block_size * kNumRegionOfInterestBlocks <= dimension)"
+ ".app"
+ ".bundle"
+ ".framework"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/Essentials/Apple/src/BundlePath.cpp"
+ "Abort: "
+ "AssignScaleBuckets_Thresholding() does not support spatial buckets."
+ "Buckets histogram is expected to be allocated on input."
+ "Each block has to be at least 4 pixels big"
+ "End should be smaller than size"
+ "Height of input data does not match expected height"
+ "Input dimension should be greater than 0"
+ "Input size mismatches the expected size"
+ "Invalid destination pointer"
+ "Only supporting binomial gaussian pyramid, with 2 scales per octave"
+ "Start should be greater than 0"
+ "User requested end of ROI should be in the HW ROI"
+ "Versions"
+ "Width of input data does not match expected width"
+ "block_size >= kMinBlockSize"
+ "buckets_hist.size() == bucket_num"
+ "cf_current_bundle"
+ "cf_path_str"
+ "cf_path_url"
+ "com.apple.cv3d"
+ "data.size() == levels().capacity()"
+ "dimension > 0"
+ "dst < dst_end"
+ "laplacian_pyr.num_scales_per_octave() == 2"
+ "num_buckets_x == 1 && num_buckets_y == 1"
+ "start >= 0"
+ "widthStep >= minimum_width_step"
+ "widthStep must be at least as big as minimum_width_step."
+ "x.height == height"
+ "x.width == width"
- "(bypassDesgen && bypassDesmatch) && \"ConfigureLacc currently expects that DG/DM is bypassed.\""
- "(expected_end <= start + kNumRegionOfInterestBlocks * block_size) && \"User requested end of ROI should be in the HW ROI\""
- "(start + block_size * kNumRegionOfInterestBlocks <= dimension) && \"End should be smaller than size\""
- "CVHWA"
- "ConsoleAppender"
- "ILayout"
- "PatternLayout"
- "__stop"
- "block_size >= kMinBlockSize && \"Each block has to be at least 4 pixels big\""
- "buckets_hist.size() == bucket_num && \"Buckets histogram is expected to be allocated on input.\""
- "curr idx"
- "data.size() == levels().capacity() && \"Input size mismatches the expected size\""
- "dst < dst_end && \"Invalid destination pointer\""
- "laplacian_pyr.num_scales_per_octave() == 2 && \"Only supporting binomial gaussian pyramid, with 2 scales per octave\""
- "num_buckets_x == 1 && num_buckets_y == 1 && \"AssignScaleBuckets_Thresholding() does not support spatial buckets.\""
- "num_octaves <= static_cast<int32_t>(requested_num_octave)"
- "num_stripes == 1"
- "prev idx"
- "ro"
- "start >= 0 && \"Start should be greater than 0\""
- "widthStep >= minimum_width_step && \"widthStep must be at least as big as minimum_width_step.\""
- "x.height == height && \"Height of input data does not match expected height\""
- "x.width == width && \"Width of input data does not match expected width\""

```
