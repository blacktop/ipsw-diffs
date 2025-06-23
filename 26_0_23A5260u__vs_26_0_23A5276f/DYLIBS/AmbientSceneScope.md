## AmbientSceneScope

> `/System/Library/PrivateFrameworks/AmbientSceneScope.framework/AmbientSceneScope`

```diff

-1.2.0.0.0
-  __TEXT.__text: 0x1789c
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__cstring: 0x60b
-  __TEXT.__const: 0xb60
-  __TEXT.__gcc_except_tab: 0x14b4
+1.6.1.0.0
+  __TEXT.__text: 0x3d47f0
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__cstring: 0xa511
+  __TEXT.__const: 0x39f00
+  __TEXT.__gcc_except_tab: 0x34820
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x718
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x38
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x748
-  __DATA.__data: 0xc0
+  __TEXT.__unwind_info: 0xcb80
+  __TEXT.__eh_frame: 0xd8
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__const: 0x10c8
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH_CONST.__const: 0x15ae0
+  __AUTH_CONST.__cfstring: 0x80
+  __DATA.__data: 0x1880
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x260
-  __DATA.__common: 0x88
+  __DATA.__bss: 0x860
+  __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
+  - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D2BA37F2-5FB8-3E57-B20D-9E68F786B1AD
-  Functions: 247
-  Symbols:   151
-  CStrings:  56
+  - /usr/lib/libobjc.A.dylib
+  UUID: 75F99C4F-8820-3514-B85F-99747CE6A05E
+  Functions: 7384
+  Symbols:   364
+  CStrings:  1024
 
Symbols:
+ _AmbientSceneFrameBundleCreateWithSceneTypesAndConfidences
+ _AmbientSceneFrameBundleRelease
+ _AmbientSceneFusionResultCreateSceneTypesAndConfidencesArrays
+ _AmbientSceneFusionResultGetCount
+ _AmbientSceneFusionResultRelease
+ _AmbientSceneSessionConfigRelease
+ _AmbientSceneSessionCreateFusionResult
+ _CFArrayAppendValue
+ _CFArrayCreateMutable
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFBundleCopyExecutableURL
+ _CFBundleGetMainBundle
+ _CFBundleGetTypeID
+ _CFCopyDescription
+ _CFDataCreateWithBytesNoCopy
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFDictionaryAddValue
+ _CFDictionaryContainsKey
+ _CFDictionaryCreate
+ _CFDictionaryGetCount
+ _CFDictionaryGetKeysAndValues
+ _CFEqual
+ _CFNumberGetType
+ _CFNumberGetValue
+ _CFURLCopyFileSystemPath
+ _CFURLCopyScheme
+ _CFURLGetTypeID
+ _CGColorSpaceCreateDeviceCMYK
+ _CGColorSpaceCreateDeviceGray
+ _CGColorSpaceCreateDeviceRGB
+ _CGColorSpaceGetModel
+ _CGColorSpaceGetNumberOfComponents
+ _CGColorSpaceGetTypeID
+ _CGDataConsumerCreate
+ _CGDataConsumerGetTypeID
+ _CGDataProviderCopyData
+ _CGDataProviderCreateSequential
+ _CGDataProviderCreateWithCFData
+ _CGDataProviderGetTypeID
+ _CGImageCreate
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithDataConsumer
+ _CGImageDestinationFinalize
+ _CGImageDestinationGetTypeID
+ _CGImageGetAlphaInfo
+ _CGImageGetBitmapInfo
+ _CGImageGetBitsPerComponent
+ _CGImageGetBitsPerPixel
+ _CGImageGetByteOrderInfo
+ _CGImageGetBytesPerRow
+ _CGImageGetColorSpace
+ _CGImageGetDataProvider
+ _CGImageGetHeight
+ _CGImageGetPixelFormatInfo
+ _CGImageGetTypeID
+ _CGImageGetWidth
+ _CGImageSourceCreateImageAtIndex
+ _CGImageSourceCreateWithDataProvider
+ _CGImageSourceGetTypeID
+ _CVPixelBufferCreate
+ _CVPixelBufferGetBaseAddressOfPlane
+ _CVPixelBufferGetBytesPerRow
+ _CVPixelBufferGetHeight
+ _CVPixelBufferGetIOSurface
+ _CVPixelBufferGetPlaneCount
+ _CVPixelBufferGetTypeID
+ _CVPixelBufferGetWidth
+ _CVPixelBufferLockBaseAddress
+ _CVPixelBufferUnlockBaseAddress
+ _IOSurfaceGetBaseAddressOfPlane
+ _IOSurfaceGetPlaneCount
+ _IOSurfaceGetTypeID
+ __DefaultRuneLocale
+ __ZNKSt13runtime_error4whatEv
+ __ZNKSt3__114error_category10equivalentERKNS_10error_codeEi
+ __ZNKSt3__114error_category10equivalentEiRKNS_15error_conditionE
+ __ZNKSt3__114error_category23default_error_conditionEi
+ __ZNKSt8bad_cast4whatEv
+ __ZNKSt9exception4whatEv
+ __ZNSt11logic_errorC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt12domain_errorD1Ev
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt13runtime_errorC1ERKS_
+ __ZNSt13runtime_errorC2EPKc
+ __ZNSt13runtime_errorC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt13runtime_errorD2Ev
+ __ZNSt14overflow_errorD1Ev
+ __ZNSt3__111__call_onceERVmPvPFvS2_E
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE4peekEv
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE4readEPcl
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE5seekgExNS_8ios_base7seekdirE
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE5tellgEv
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED1Ev
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERd
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERf
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERi
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERj
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERs
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERt
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERx
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERy
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEPKv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEb
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEs
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEt
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEy
+ __ZNSt3__114error_categoryD2Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__117iostream_categoryEv
+ __ZNSt3__118condition_variableD1Ev
+ __ZNSt3__119__shared_mutex_base11lock_sharedEv
+ __ZNSt3__119__shared_mutex_base13unlock_sharedEv
+ __ZNSt3__119__shared_mutex_base4lockEv
+ __ZNSt3__119__shared_mutex_base6unlockEv
+ __ZNSt3__119__shared_mutex_baseC1Ev
+ __ZNSt3__119__shared_weak_count4lockEv
+ __ZNSt3__14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm
+ __ZNSt3__14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
+ __ZNSt3__18ios_base7failureD1Ev
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ __ZNSt3__19to_stringEd
+ __ZNSt3__19to_stringEf
+ __ZNSt3__19to_stringEj
+ __ZNSt3__19to_stringEl
+ __ZNSt3__19to_stringEx
+ __ZNSt3__19to_stringEy
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZNSt8bad_castC2Ev
+ __ZNSt8bad_castD2Ev
+ __ZNSt9bad_allocC1Ev
+ __ZNSt9bad_allocD1Ev
+ __ZTINSt3__114error_categoryE
+ __ZTINSt3__117bad_function_callE
+ __ZTINSt3__18ios_base7failureE
+ __ZTISt12bad_any_cast
+ __ZTISt12domain_error
+ __ZTISt13runtime_error
+ __ZTISt14overflow_error
+ __ZTISt8bad_cast
+ __ZTISt9bad_alloc
+ __ZTISt9exception
+ __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__113basic_istreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__113basic_ostreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__117bad_function_callE
+ __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVSt12bad_any_cast
+ __ZTVSt12domain_error
+ __ZTVSt14overflow_error
+ ___CFConstantStringClassReference
+ ___cxa_pure_virtual
+ ___dynamic_cast
+ ___error
+ ___exp10
+ ___maskrune
+ ___tolower
+ ___udivti3
+ ___umodti3
+ _atoi
+ _kCFAllocatorNull
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFTypeArrayCallBacks
+ _kCVPixelBufferBytesPerRowAlignmentKey
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPlaneAlignmentKey
+ _kCVPixelBufferWidthKey
+ _localeconv
+ _mach_continuous_time
+ _mach_task_self_
+ _mach_timebase_info
+ _malloc_type_malloc
+ _malloc_type_posix_memalign
+ _malloc_type_realloc
+ _snprintf
+ _strtod
+ _strtof
+ _strtol
+ _strtoll
+ _strtoull
+ _vm_allocate
+ _vm_deallocate
CStrings:
+ "\n}"
+ " "
+ "   ]"
+ " (ENOMEM)"
+ " and size "
+ " at line "
+ " but current sample version is "
+ " but file contains "
+ " but image is of color format "
+ " but must be 8-bit Gray or Rgb to save as pnm."
+ " but pnm file contains "
+ " but should be "
+ " but the image is of incompatible format "
+ " bytes with alignment "
+ " can't be saved with CoreGraphics."
+ " cannot be created with default arguments"
+ " data."
+ " does not allow the "
+ " error "
+ " for format "
+ " format, but file contains "
+ " formatting argument"
+ " from an "
+ " from stream with file format "
+ " incompatible with pnm."
+ " into Image of format "
+ " invalid. "
+ " is not a valid pnm format."
+ " not yet supported."
+ " to "
+ " was requested of `Number` containing "
+ " was requested of `Numbers` containing "
+ "\""
+ "\"\""
+ "\":"
+ "\": "
+ "\"bytes\": ["
+ "\"subtype\": "
+ "#"
+ "%.2X"
+ "'"
+ "' (="
+ "','"
+ "'."
+ "':'"
+ "'['"
+ "'[', '{', or a literal"
+ "']'"
+ "'{'"
+ "'}'"
+ "(bytes_per_row % bytes_per_pixel == 0)"
+ ")"
+ ",\n"
+ ", "
+ ", Size: "
+ ", bits_per_component="
+ ", bits_per_pixel="
+ ", but contains "
+ ", but is not supported by "
+ ", column "
+ ", cx,cy: "
+ ", dst: "
+ ", expected [Algebra|Affine][F|D]"
+ ", expected [Center|Corner][Pinhole|Heikkila][F|D]"
+ ", expected [u|i|f][{size}]"
+ ", expected one of "
+ ", float_components="
+ ", k1,..,k"
+ ", k1,k2,p1,p2,k3: "
+ ", transform:"
+ ", used attributes:\n"
+ ", values = {\n"
+ "- "
+ ". Minimum version required is "
+ ".denoising_parameters"
+ ".dynamic_parameters"
+ "/"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Essentials/Apple/src/Clock.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Container/src/Lines.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Container/src/Points.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreGraphics/src/ColorSpaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreGraphics/src/DataProviderRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreGraphics/src/ImageRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreVideo/src/CVImage.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreVideo/src/CVImage.cpp:56"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Foundation/FoundationIO/include/Kit/FoundationIO/DictionaryRefIO.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Foundation/src/BundleRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Foundation/src/DictionaryRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Foundation/src/Ref.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Foundation/src/URLRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/ImageView.h:1289"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/ImageView.h:1299"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/SharedImage.h:1236"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/src/ImageStorage.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Image/src/Size.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/ImageIO/include/Kit/ImageIO/ImageIO.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/ImageIO/src/Apple.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/ImageIO/src/ImageDestinationRef.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/ImageIO/src/ImageIO.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/ImageIO/src/Pnm.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/ImageIO/src/Serialization.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Memory/include/Kit/Memory/VMAllocator.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Mesh/include/Kit/Mesh/TriMeshAllocator.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Mesh/src/TriMesh.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Mesh/src/TriMeshAllocator.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Visualization/include/Kit/Visualization/DataIO.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Visualization/include/Kit/Visualization/IData.h"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Visualization/src/DataType.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Visualization/src/IData.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Visualization/src/NamedContext.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/Kit/Visualization/src/VisualLogger.cpp"
+ "0 == mach_timebase_info(&timebase)"
+ "01"
+ "01234567"
+ "0123456789"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "0x"
+ "128RGBAFloat"
+ "14Bayer_BGGR"
+ "14Bayer_GBRG"
+ "14Bayer_GRBG"
+ "14Bayer_RGGB"
+ "16BE555"
+ "16BE565"
+ "16Gray"
+ "16LE555"
+ "16LE5551"
+ "16LE565"
+ "16VersatileBayer"
+ "1IndexedGray_WhiteIsZero"
+ "1Monochrome"
+ "24BGR"
+ "24RGB"
+ "2Indexed"
+ "2IndexedGray_WhiteIsZero"
+ "30RGB"
+ "30RGBLEPackedWideGamut"
+ "32ABGR"
+ "32ARGB"
+ "32AlphaGray"
+ "32BGRA"
+ "32RGBA"
+ "40ARGBLEWideGamut"
+ "40ARGBLEWideGamutPremultiplied"
+ "420YpCbCr10BiPlanarFullRange"
+ "420YpCbCr10BiPlanarVideoRange"
+ "420YpCbCr8BiPlanarFullRange"
+ "420YpCbCr8BiPlanarVideoRange"
+ "420YpCbCr8Planar"
+ "420YpCbCr8PlanarFullRange"
+ "420YpCbCr8VideoRange_8A_TriPlanar"
+ "422YpCbCr10"
+ "422YpCbCr10BiPlanarFullRange"
+ "422YpCbCr10BiPlanarVideoRange"
+ "422YpCbCr16"
+ "422YpCbCr8"
+ "422YpCbCr8BiPlanarFullRange"
+ "422YpCbCr8BiPlanarVideoRange"
+ "422YpCbCr8FullRange"
+ "422YpCbCr8_yuvs"
+ "422YpCbCr_4A_8BiPlanar"
+ "4444AYpCbCr16"
+ "4444AYpCbCr8"
+ "4444YpCbCrA8"
+ "4444YpCbCrA8R"
+ "444YpCbCr10"
+ "444YpCbCr10BiPlanarFullRange"
+ "444YpCbCr10BiPlanarVideoRange"
+ "444YpCbCr8"
+ "444YpCbCr8BiPlanarFullRange"
+ "444YpCbCr8BiPlanarVideoRange"
+ "48RGB"
+ "4Indexed"
+ "4IndexedGray_WhiteIsZero"
+ "64ARGB"
+ "64RGBAHalf"
+ "64RGBALE"
+ "64RGBA_DownscaledProResRAW"
+ "8Indexed"
+ "8IndexedGray_WhiteIsZero"
+ ": "
+ ": 0x"
+ ": error code "
+ ";"
+ ";\n "
+ "; "
+ "; X/X"
+ "; expected "
+ "; last read: '"
+ "<"
+ "<U+%.4X>"
+ "<discarded>"
+ "<parse error>"
+ "<uninitialized>"
+ ">"
+ "ARGB2101010LEPacked"
+ "Abgr16f"
+ "Abgr16u"
+ "Abgr32f"
+ "Abgr8u"
+ "Access notification must only be done in debug."
+ "AffineD"
+ "AffineF"
+ "AlgebraD"
+ "AlgebraF"
+ "An argument index may not have a negative value"
+ "Argb16f"
+ "Argb16u"
+ "Argb32f"
+ "Argb8u"
+ "Array"
+ "Attempt to access an expired PixelBuffer. Note that an image buffer  created by an ImageView does not keep the buffer alive."
+ "Attempting to create an "
+ "Auto"
+ "Bgr16f"
+ "Bgr16u"
+ "Bgr32f"
+ "Bgr8u"
+ "Bgra16f"
+ "Bgra16u"
+ "Bgra32f"
+ "Bgra8u"
+ "Blob"
+ "Bool"
+ "Byte order and bits per component do not correspond to a supported format."
+ "Byte order is incompatible."
+ "Byte order is inverted."
+ "Byte order size for non-8 bits per component does not match bits per component."
+ "CF ref argument for `DictionaryValueSample` must be Number, String, Bool, Array or Dictionary, but is "
+ "CFDictionary cannot be used to create dict::Dictionary. It must only hold trivially serializable types: Boolean, Number, String, Array or Dictionary values"
+ "CMYK"
+ "Camera"
+ "Camera{Type: "
+ "CanSerialize(to_serialize.RuntimeFormat(), *op_format)"
+ "Cannot copy CGImage of format "
+ "Cannot set root context to inherit its enable-state"
+ "Center"
+ "CenterHeikkilaD"
+ "CenterHeikkilaF"
+ "CenterPinholeD"
+ "CenterPinholeF"
+ "Chronological"
+ "Color space model "
+ "Color values are premultiplied with alpha."
+ "ConstImageView"
+ "ConstSharedImage"
+ "Corner"
+ "CornerHeikkilaD"
+ "CornerHeikkilaF"
+ "CornerPinholeD"
+ "CornerPinholeF"
+ "D"
+ "DepthFloat16"
+ "DepthFloat32"
+ "Desired image format is "
+ "DeviceN"
+ "Dictionary"
+ "Dictionary cannot be serialized. It must only hold Boolean, Number, String, Array or Dictionary values, but contains "
+ "Dictionary to convert to json must only contain Number, String, Bool, Array or Dictionary, but has "
+ "DisparityFloat16"
+ "DisparityFloat32"
+ "Dynamic"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Endianness conversion not implemented for this format"
+ "F"
+ "F == format"
+ "Failed to create CVPixelBuffer: "
+ "Failed to load sample "
+ "Failed to save image to destination."
+ "Failure during "
+ "File"
+ "Fisheye4"
+ "Fisheye7"
+ "For channels="
+ "Format "
+ "Format is not serializable. Must be a non-dynamic format."
+ "Found file format of unsupported format signature byte '0x"
+ "Four16f"
+ "Four16u"
+ "Four32f"
+ "Four8u"
+ "Fusion result is empty"
+ "FusionResult argument is NULL"
+ "Given `camera` cannot be serialized. It does not contain a Kit_Camera camera"
+ "Given data block is too big to be represented by uint32_t indexed ArrayView"
+ "Gray16f"
+ "Gray16u"
+ "Gray32f"
+ "Gray8u"
+ "GroupD"
+ "GroupF"
+ "Heikkila"
+ "HighResolution"
+ "IOSurfaceName"
+ "Illegal or non-allocated address specified."
+ "Image"
+ "Image is of format "
+ "ImageDestinationRef does not (yet) support format "
+ "ImageIO"
+ "ImageView"
+ "Indexed"
+ "Input stream not in good state, in "
+ "Integral value outside the range of the char type"
+ "Invalid ArithmeticType value '"
+ "Invalid Format ("
+ "Invalid argument "
+ "Invalid image format. Format "
+ "Invalid mode"
+ "Invalid pnm file. Format magic number not recognized."
+ "Invalid pnm file. Unexpected end of file in header."
+ "Invalid serialization format type: "
+ "IsValid()"
+ "Jpeg"
+ "Lab"
+ "Lines2"
+ "Lines3"
+ "MachAbsolute"
+ "MachContinuous"
+ "MakePixelBuffer"
+ "Monochrome"
+ "Must choose format to save."
+ "No fusion result for the given timestamp"
+ "No known method to load file of "
+ "Not enough data to read"
+ "Not enough data to read binary blob"
+ "Not enough data to read span"
+ "Not enough data to read string"
+ "Not implemented"
+ "Number"
+ "Number of keys must match number of values"
+ "Numbers"
+ "OneComponent10"
+ "OneComponent12"
+ "OneComponent16"
+ "OneComponent16Half"
+ "OneComponent32Float"
+ "OneComponent8"
+ "P2\n"
+ "P3"
+ "P3\n"
+ "P5"
+ "P5\n"
+ "P6"
+ "P6\n"
+ "Pattern"
+ "Pgm"
+ "Pinhole"
+ "Pixel format is not kCGImagePixelFormatPacked."
+ "Png"
+ "Points2"
+ "Points3"
+ "Ppm"
+ "RGB"
+ "Raw"
+ "Received invalid format compatibility information"
+ "RefillBuffer"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "Requested format "
+ "Requested io-format "
+ "Requested to load "
+ "Requested to load format "
+ "Rgb16f"
+ "Rgb16u"
+ "Rgb32f"
+ "Rgb8u"
+ "Rgba16f"
+ "Rgba16u"
+ "Rgba32f"
+ "Rgba8u"
+ "Runtime format not in given Formats list"
+ "Should not happen"
+ "Skips first component."
+ "Skips last component."
+ "Span of value type "
+ "Steady"
+ "String"
+ "System"
+ "TextLog"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The buffer does not support the given format"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "Three16f"
+ "Three16u"
+ "Three32f"
+ "Three8u"
+ "Tiff"
+ "Transform3"
+ "Transform3{src: "
+ "TriMesh"
+ "TriMeshData{\n"
+ "Two16f"
+ "Two16u"
+ "Two32f"
+ "Two8u"
+ "TwoComponent16"
+ "TwoComponent16Half"
+ "TwoComponent32Float"
+ "TwoComponent8"
+ "Unequal scene_types and confidences counts"
+ "Unknown"
+ "Unknown pixel format '"
+ "Unsupported Format"
+ "Unsupported alpha info "
+ "Unsupported format"
+ "Unsupported pnm format. Loader does not support Rgb16u (.pbm) loading yet."
+ "Unsupported pnm format. Loader does not support intensity scaling. File specifies maximum intensity "
+ "Unsupported type"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "Value of type "
+ "XYZ"
+ "["
+ "[\n"
+ "[]"
+ "[json.exception."
+ "[row byte stride "
+ "\\\""
+ "\\'"
+ "\\;"
+ "\\\\"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u%04x"
+ "]"
+ "]\n"
+ "],\n"
+ "],\"subtype\":"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "affine3x4"
+ "algebra_r"
+ "algebra_t"
+ "alternate form"
+ "an integer"
+ "array"
+ "array size overflow"
+ "atto"
+ "auto_timestamp"
+ "bbox={"
+ "bin size overflow"
+ "binary"
+ "boolean"
+ "box"
+ "byte_size"
+ "bytes"
+ "bytes_per_row >= min_bytes_per_row"
+ "camera"
+ "camera_type"
+ "cannot compare iterators of different containers"
+ "cannot create object from initializer list"
+ "cannot get value"
+ "cannot use erase() with "
+ "cannot use key() for non-object iterators"
+ "cannot use operator[] with a numeric argument with "
+ "cannot use operator[] with a string argument with "
+ "cannot use push_back() with "
+ "centi"
+ "cg_image.IsValid()"
+ "clock_type"
+ "colors"
+ "colors={"
+ "colors_type"
+ "colors_type="
+ "compat.format.has_value()"
+ "confidences"
+ "confidences={"
+ "confidences_type"
+ "confidences_type="
+ "container size overflow"
+ "custom_timestamp"
+ "cv3d.ambient_scene_scope.spatio_temporal_agg"
+ "cv3d.viz"
+ "cv3d::kit::img::"
+ "d-slice #"
+ "data_"
+ "days"
+ "deca"
+ "decay_rate"
+ "deci"
+ "denoising_parameters"
+ "depth size overflow"
+ "detail"
+ "dictionary"
+ "discarded"
+ "distortion_coeff"
+ "dst"
+ "edges"
+ "edges={"
+ "end of input"
+ "exa"
+ "excessive array size: "
+ "excessive object size: "
+ "ext size overflow"
+ "f32"
+ "f64"
+ "faces"
+ "faces={"
+ "failed to load"
+ "failed to open file"
+ "false"
+ "false literal"
+ "femto"
+ "file contains different image format"
+ "file is of a different than specified format"
+ "file.good()"
+ "focal_length"
+ "format != img::Format::Dynamic"
+ "format not supported"
+ "giga"
+ "hecto"
+ "hours"
+ "i16"
+ "i32"
+ "i64"
+ "i8"
+ "idx < p_->GetCachedBaseAddress().size()"
+ "idx < static_cast<uint32_t>(DataType::End)"
+ "image format not supported by io format"
+ "image_data"
+ "image_dynamic.RuntimeFormat() == color_format"
+ "image_format"
+ "image_size"
+ "incomplete UTF-8 string; last byte: 0x"
+ "infnanINFNAN"
+ "info"
+ "instance_id"
+ "invalid BOM; must be 0xEF 0xBB 0xBF if given"
+ "invalid IOValueType string "
+ "invalid UTF-8 byte at index "
+ "invalid alpha"
+ "invalid arithmetic type string "
+ "invalid camera type"
+ "invalid camera type string "
+ "invalid clock_type "
+ "invalid comment; expecting '/' or '*' after '/'"
+ "invalid comment; missing closing '*/'"
+ "invalid image format type string "
+ "invalid literal"
+ "invalid number; expected '+', '-', or digit after exponent"
+ "invalid number; expected digit after '-'"
+ "invalid number; expected digit after '.'"
+ "invalid number; expected digit after exponent sign"
+ "invalid or unsupported file"
+ "invalid se3 type string "
+ "invalid serialization format type string "
+ "invalid string: '\\u' must be followed by 4 hex digits"
+ "invalid string: control character U+0000 (NUL) must be escaped to \\u0000"
+ "invalid string: control character U+0001 (SOH) must be escaped to \\u0001"
+ "invalid string: control character U+0002 (STX) must be escaped to \\u0002"
+ "invalid string: control character U+0003 (ETX) must be escaped to \\u0003"
+ "invalid string: control character U+0004 (EOT) must be escaped to \\u0004"
+ "invalid string: control character U+0005 (ENQ) must be escaped to \\u0005"
+ "invalid string: control character U+0006 (ACK) must be escaped to \\u0006"
+ "invalid string: control character U+0007 (BEL) must be escaped to \\u0007"
+ "invalid string: control character U+0008 (BS) must be escaped to \\u0008 or \\b"
+ "invalid string: control character U+0009 (HT) must be escaped to \\u0009 or \\t"
+ "invalid string: control character U+000A (LF) must be escaped to \\u000A or \\n"
+ "invalid string: control character U+000B (VT) must be escaped to \\u000B"
+ "invalid string: control character U+000C (FF) must be escaped to \\u000C or \\f"
+ "invalid string: control character U+000D (CR) must be escaped to \\u000D or \\r"
+ "invalid string: control character U+000E (SO) must be escaped to \\u000E"
+ "invalid string: control character U+000F (SI) must be escaped to \\u000F"
+ "invalid string: control character U+0010 (DLE) must be escaped to \\u0010"
+ "invalid string: control character U+0011 (DC1) must be escaped to \\u0011"
+ "invalid string: control character U+0012 (DC2) must be escaped to \\u0012"
+ "invalid string: control character U+0013 (DC3) must be escaped to \\u0013"
+ "invalid string: control character U+0014 (DC4) must be escaped to \\u0014"
+ "invalid string: control character U+0015 (NAK) must be escaped to \\u0015"
+ "invalid string: control character U+0016 (SYN) must be escaped to \\u0016"
+ "invalid string: control character U+0017 (ETB) must be escaped to \\u0017"
+ "invalid string: control character U+0018 (CAN) must be escaped to \\u0018"
+ "invalid string: control character U+0019 (EM) must be escaped to \\u0019"
+ "invalid string: control character U+001A (SUB) must be escaped to \\u001A"
+ "invalid string: control character U+001B (ESC) must be escaped to \\u001B"
+ "invalid string: control character U+001C (FS) must be escaped to \\u001C"
+ "invalid string: control character U+001D (GS) must be escaped to \\u001D"
+ "invalid string: control character U+001E (RS) must be escaped to \\u001E"
+ "invalid string: control character U+001F (US) must be escaped to \\u001F"
+ "invalid string: forbidden character after backslash"
+ "invalid string: ill-formed UTF-8 byte"
+ "invalid string: missing closing quote"
+ "invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF"
+ "invalid string: surrogate U+DC00..U+DFFF must follow U+D800..U+DBFF"
+ "invalid value type identifier"
+ "invalid_iterator"
+ "io_format"
+ "iterator does not fit current value"
+ "iterator out of range"
+ "kCGImageAlphaOnly"
+ "kCGImageAlphaPremultipliedFirst"
+ "kCVReturnAllocationFailed: The allocation for a buffer or buffer pool failed. Most likely because of lack of resources."
+ "kCVReturnDisplayLinkAlreadyRunning: The CVDisplayLink is already started and running."
+ "kCVReturnDisplayLinkCallbacksNotSet: The output callback is not set."
+ "kCVReturnDisplayLinkNotRunning: The CVDisplayLink has not been started."
+ "kCVReturnError: Function executed with unknown error."
+ "kCVReturnInvalidArgument: At least one of the arguments passed in is not valid. Either out of range or the wrong type."
+ "kCVReturnInvalidDisplay: A CVDisplayLink cannot be created for the given DisplayRef."
+ "kCVReturnInvalidPixelBufferAttributes: A CVBuffer cannot be created with the given attributes."
+ "kCVReturnInvalidPixelFormat: The requested pixelformat is not supported for the CVBuffer type."
+ "kCVReturnInvalidPoolAttributes: A CVBufferPool cannot be created with the given attributes."
+ "kCVReturnInvalidSize: The requested size (most likely too big) is not supported for the CVBuffer type."
+ "kCVReturnPixelBufferNotMetalCompatible: The Buffer cannot be used with Metal as either its size, pixelformat or attributes are not supported by Metal."
+ "kCVReturnPixelBufferNotOpenGLCompatible: The Buffer cannot be used with OpenGL as either its size, pixelformat or attributes are not supported by OpenGL."
+ "kCVReturnPoolAllocationFailed: The allocation for the buffer pool failed. Most likely because of lack of resources. Check if your parameters are in range."
+ "kCVReturnRetry: a scan hasn't completely traversed the CVBufferPool due to a concurrent operation. The client can retry the scan."
+ "kCVReturnSuccess: Function executed successfully without errors."
+ "kCVReturnUnsupported"
+ "kCVReturnWouldExceedAllocationThreshold: The allocation request failed because it would have exceeded a specified allocation threshold (see kCVPixelBufferPoolAllocationThresholdKey)."
+ "keys.size() == values.size()"
+ "kilo"
+ "lines2"
+ "lines3"
+ "load"
+ "loaded binary data size does not match given data blob size"
+ "loader must specify the format to load as"
+ "locale-specific form"
+ "location"
+ "map size overflow"
+ "materials"
+ "materials={"
+ "materials_type"
+ "materials_type="
+ "max"
+ "maybe_format"
+ "maybe_string"
+ "mega"
+ "micro"
+ "milli"
+ "min"
+ "min_version"
+ "minutes"
+ "months"
+ "name"
+ "nano"
+ "no error"
+ "normals"
+ "normals={"
+ "normals_type"
+ "normals_type="
+ "not implemented"
+ "ns"
+ "null"
+ "null literal"
+ "nullopt"
+ "nullptr"
+ "null}"
+ "number"
+ "number literal"
+ "number overflow parsing '"
+ "numbers"
+ "object"
+ "object key"
+ "object separator"
+ "out_of_range"
+ "p_"
+ "parse error"
+ "parse_error"
+ "per-face"
+ "per-vertex"
+ "peta"
+ "pico"
+ "points2"
+ "points3"
+ "posix_memalign failed to allocate "
+ "precision"
+ "principal_point"
+ "ptr != nullptr"
+ "public.jpeg"
+ "public.png"
+ "public.tiff"
+ "ratio<"
+ "references"
+ "save"
+ "scene_types or confidences argument is NULL"
+ "se3_type"
+ "seconds"
+ "semantics"
+ "semantics={"
+ "semantics_type"
+ "semantics_type="
+ "shape.size() == value_stride.size()"
+ "should not be reached"
+ "sign"
+ "size"
+ "size == image.Size()"
+ "space"
+ "src"
+ "src_to_dst"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 10U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 11U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 12U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 13U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 2U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 3U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 4U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 5U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 6U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 7U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 8U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 9U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::Number]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::Camera]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 4, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 4, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 7, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 7, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 4, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 4, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 7, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 7, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PixelOrigin::Center]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PixelOrigin::Corner]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::CameraSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cfio::DictionaryRefSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cfio::DictionaryValueSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::commonio::NumberSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Blob]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Lines<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Lines<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Numbers]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Points<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Points<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::BlobSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::LinesSample<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::LinesSample<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::NumbersSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::PointsSample<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::PointsSample<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Argb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Argb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Bgra8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgba16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgba32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::dict::Dictionary]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::dictio::DictionarySample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::DynamicBuffer]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Dynamic]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::imgio::ImageSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::imgio::ImageStructureSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::mesh::TriMeshBoundingBoxSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::mesh::TriMeshDataSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::timeio::TimestampSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::DataInfoSample<6>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ImageData]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::SE3Sample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::TextLog]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::Transform3Sample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::Transform3]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::TriMesh]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::Number>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::cam::Camera>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Blob>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Lines<2>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Lines<3>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Numbers>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Points<2>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Points<3>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::dict::Dictionary>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::img::SharedImage<cv3d::kit::img::Format::Dynamic, cv3d::kit::img::DynamicBuffer, cv3d::kit::img::Mutability::Const>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::TextLog>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::Transform3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::TriMesh>]"
+ "std::"
+ "std::__1::"
+ "str size overflow"
+ "stride must be multiple of pixel size"
+ "stride must not overlap internally"
+ "string"
+ "string literal"
+ "string_view::substr"
+ "structure"
+ "syntax error "
+ "tera"
+ "tex0='"
+ "tex_coords"
+ "tex_coords={"
+ "tex_faces"
+ "tex_faces={"
+ "textures"
+ "this->numbers.Size() % (N * 2) == 0"
+ "this->numbers.Size() % N == 0"
+ "total_size < std::numeric_limits<uint32_t>::max()"
+ "true"
+ "true literal"
+ "trying to cast camera"
+ "type must be array, but is "
+ "type must be boolean, but is "
+ "type must be number, but is "
+ "type must be string, but is "
+ "type_error"
+ "u16"
+ "u32"
+ "u64"
+ "u8"
+ "unexpected "
+ "unknown"
+ "unknown allocator mode"
+ "unknown arithmetic type"
+ "unknown error code"
+ "unknown token"
+ "unknown type id "
+ "unknown_package"
+ "value"
+ "value_type"
+ "version"
+ "vertices"
+ "vertices={"
+ "viz::Package"
+ "viz::PackageData"
+ "viz::SharedData"
+ "weeks"
+ "while parsing "
+ "window_expiry_duration_secs"
+ "world"
+ "x"
+ "years"
+ "zero-padding"
+ "{"
+ "{\n"
+ "{\"bytes\":["
+ "{:.{}}"
+ "{:<{}}"
+ "{:>{}}"
+ "{:{}}"
+ "{Model: "
+ "{fx,fy: "
+ "{unknown buffer type}"
+ "{}"
+ "}"
+ "}\n"
+ "�"
- "/Library/Caches/com.apple.xbs/Sources/AmbientSceneScope/library/AmbientSceneScope/FusionEngine/src/TemporalAggregator.cpp"
- "Invalid temporal aggregation strategy"

```
