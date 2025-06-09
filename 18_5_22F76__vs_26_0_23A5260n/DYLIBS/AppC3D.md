## AppC3D

> `/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D`

```diff

-1.16.1.2.0
-  __TEXT.__text: 0x698f88
-  __TEXT.__auth_stubs: 0x2250
-  __TEXT.__cstring: 0x125b3
-  __TEXT.__const: 0x5f707
-  __TEXT.__gcc_except_tab: 0x4d798
+1.17.2.0.0
+  __TEXT.__text: 0x7a8d84
+  __TEXT.__auth_stubs: 0x23b0
+  __TEXT.__const: 0x60497
+  __TEXT.__cstring: 0x1309d
+  __TEXT.__gcc_except_tab: 0x47f7c
   __TEXT.__oslogstring: 0x36b
-  __TEXT.__unwind_info: 0x13520
-  __TEXT.__eh_frame: 0xc48
+  __TEXT.__unwind_info: 0x13bf8
+  __TEXT.__eh_frame: 0x1938
   __TEXT.__objc_methname: 0x4f
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x1bf0
+  __DATA_CONST.__const: 0x1be8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1138
-  __AUTH_CONST.__const: 0x204d0
+  __AUTH_CONST.__auth_got: 0x11e8
+  __AUTH_CONST.__const: 0x20d18
   __AUTH_CONST.__cfstring: 0x320
-  __AUTH.__data: 0x8
-  __DATA.__data: 0x5460
-  __DATA.__llvm_prf_cnts: 0x100
-  __DATA.__llvm_prf_data: 0x400
-  __DATA.__llvm_prf_names: 0x51d
-  __DATA.__crash_info: 0x40
+  __AUTH.__data: 0x38
+  __DATA.__data: 0x54e8
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x80
   __DATA.__common: 0x70
-  __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x2228
+  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__bss: 0x26e8
   __DATA_DIRTY.__common: 0x18
-  __LLVM_COV.__llvm_covfun: 0x2a98
-  __LLVM_COV.__llvm_covmap: 0x158
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 586DEDDF-F0F7-3A1D-8565-C9272CA38C62
-  Functions: 12567
-  Symbols:   714
-  CStrings:  1852
+  UUID: AB02E092-6020-394E-845F-FBFBDA06EF46
+  Functions: 13912
+  Symbols:   737
+  CStrings:  2006
 
Symbols:
+ _BLASStateRelease
+ _BLASStateRetain
+ _CFBundleGetTypeID
+ _CFDataGetTypeID
+ _CFErrorGetTypeID
+ _CFURLGetTypeID
+ _CGColorSpaceGetTypeID
+ _CGDataConsumerGetTypeID
+ _CGDataProviderGetTypeID
+ _CGImageDestinationGetTypeID
+ _CGImageGetTypeID
+ _CGImageSourceGetTypeID
+ _CVPixelBufferGetTypeID
+ _CVPixelBufferPoolGetTypeID
+ _IOSurfaceGetTypeID
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZnwmSt19__type_descriptor_t
+ _cblas_dcopy
+ _cblas_ddot
+ _cblas_dgemv
+ _cblas_dscal
+ _cblas_ssyrk$NEWLAPACK
+ _cblas_strmm$NEWLAPACK
+ _e5rt_buffer_object_create_from_iosurface
+ _e5rt_e5_compiler_options_set_compute_device_types_mask
+ _memset_pattern8
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x8
+ _powf
+ _vfprintf
+ _xerbla_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- ___toupper
- _dsysv$NEWLAPACK
- _sgesvd$NEWLAPACK
- _spotrf$NEWLAPACK
- _ssytrf$NEWLAPACK
- _ssytrs$NEWLAPACK
- _wmemchr
CStrings:
+ " != "
+ " ("
+ " to bind output buffer to output port "
+ " to create buffer for output port: "
+ "(stream_id == 0 || stream_id == 1)"
+ ") : "
+ ") does not match the expected compile time type ID "
+ "** On entry to %6s, parameter number %2i had an illegal value\n"
+ ", k1,..,k"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/AppCode/Decoder/src/Decoder.cpp:424"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/AppCode/Decoder/src/Decoder.cpp:434"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Resource/src/Resource.mm"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/CoreVideo/src/CVImage.cpp:56"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Foundation/src/Ptr.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/Image.h:1192"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/Image.h:1333"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/Image.h:1340"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/ImageView.h:1289"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/ImageView.h:1299"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/SharedImage.h:1236"
+ "1"
+ "2"
+ "A"
+ "Are you wrapping a CFTypeRef from an other type ?"
+ "Are you wrapping the same type from different static context ?"
+ "B"
+ "BR"
+ "BRD"
+ "C"
+ "Columnwise"
+ "DLASQ2"
+ "DSYCONV"
+ "DSYSV "
+ "DSYTF2"
+ "DSYTRF"
+ "DSYTRS"
+ "DSYTRS2"
+ "E"
+ "EBZ"
+ "EPS"
+ "EVC"
+ "Epsilon"
+ "Error "
+ "F"
+ "Fisheye4"
+ "Fisheye7"
+ "Forward"
+ "G"
+ "GB"
+ "GE"
+ "GG"
+ "GST"
+ "H"
+ "HD3"
+ "HE"
+ "HR"
+ "HRD"
+ "Incorrect stread id."
+ "Input/output port count mismatch: "
+ "IsNonBundleSupported(device)"
+ "L"
+ "LA"
+ "LAORH"
+ "LAQR"
+ "LDA must be >= MAX(K,1): LDA=%d K=%d."
+ "LDA must be >= MAX(M,1): LDA=%d M=%d."
+ "LDB must be >= MAX(K,1): LDB=%d K=%d."
+ "LDB must be >= MAX(N,1): LDB=%d N=%d."
+ "LDC must be >= MAX(M,1): LDC=%d M=%d."
+ "LDC must be >= MAX(N,1): LDC=%d N=%d."
+ "LQ"
+ "LQ "
+ "LQF"
+ "Left"
+ "Lower"
+ "M"
+ "N"
+ "No transpose"
+ "Non-unit"
+ "Not supported."
+ "O"
+ "OR"
+ "P"
+ "PB"
+ "PO"
+ "POTRF"
+ "Precision"
+ "Q"
+ "QL"
+ "QLF"
+ "QR"
+ "QR "
+ "QRF"
+ "R"
+ "RQ"
+ "RQF"
+ "Right"
+ "Rowwise"
+ "Runtime type ID "
+ "S"
+ "SBDSQR"
+ "SGEBD2"
+ "SGEBRD"
+ "SGELQ2"
+ "SGELQF"
+ "SGEQR2"
+ "SGEQRF"
+ "SGESVD"
+ "SLASCL"
+ "SLASQ1"
+ "SLASQ2"
+ "SLASR "
+ "SLASRT"
+ "SORG2R"
+ "SORGBR"
+ "SORGL2"
+ "SORGLQ"
+ "SORGQR"
+ "SORM2R"
+ "SORMBR"
+ "SORML2"
+ "SORMLQ"
+ "SORMQR"
+ "SPOTRF"
+ "SPOTRF2"
+ "SSYTF2"
+ "SSYTRF"
+ "SSYTRS"
+ "ST"
+ "SY"
+ "Safe minimum"
+ "T"
+ "TR"
+ "TRD"
+ "TRF"
+ "TRI"
+ "Transpose"
+ "U"
+ "UN"
+ "UUM"
+ "Unable to bind buffer object to input port."
+ "Unable to create buffer object from IOSurface"
+ "Unable to set compiler options: "
+ "Unit"
+ "Upper"
+ "V"
+ "Z"
+ "\\u%04x\\u%04x"
+ "\\ufffd"
+ "cblas_dcopy"
+ "cblas_dgemm"
+ "cblas_dgemv"
+ "cblas_dger"
+ "cblas_dscal_sequential"
+ "cblas_dswap"
+ "cblas_dsyr"
+ "cblas_dtrsm"
+ "cblas_scopy"
+ "cblas_sger"
+ "cblas_srot"
+ "cblas_sscal_sequential"
+ "cblas_sswap"
+ "cblas_ssyr"
+ "cblas_strmv"
+ "cfref == nullptr || IsOfCFType<T>(cfref)"
+ "child_surface.Format() == surface.Format(plane_index)"
+ "enable_tensor_interface"
+ "expected != found"
+ "pixel_buffer.IsValid()"
+ "plane_index < NumPlanes()"
+ "points_keypoint_id"
+ "points_patch_id"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 4, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 4, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 7, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 7, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 4, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 4, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 7, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 7, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::ml::SharedANE]"
+ "stream_id == 0"
+ "{nullptr}"
- " format."
- " option"
- "'). "
- "'. "
- "(camera_stream_id == 0 || camera_stream_id == 1)"
- ", image "
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/AppCode/Decoder/src/Decoder.cpp:422"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/AppCode/Decoder/src/Decoder.cpp:432"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Common/include/Essentials/Common/Span.h"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Resource/src/Resource.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/CoreVideo/src/CVImage.cpp:55"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/Image.h:1190"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/Image.h:1331"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/Image.h:1338"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/ImageView.h:1287"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/ImageView.h:1297"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Image/include/Kit/Image/SharedImage.h:1234"
- "0 "
- "ConfidenceScore"
- "Incorrect stread id"
- "Input/output port counts doesn't match."
- "IsNonBundleSupported()"
- "IsValid() && plane_index < NumPlanes()"
- "Not supported"
- "Unable to bind output buffer to output port "
- "Unable to create buffer for output port: "
- "] "
- "camera_stream_id == 0"
- "limiting_buffer_"
- "ptr != nullptr || size == 0"

```
