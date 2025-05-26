## VisualLogger

> `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger`

```diff

-6.31.53.0.0
-  __TEXT.__text: 0x589070
-  __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__const: 0x52cf0
-  __TEXT.__gcc_except_tab: 0x4ec64
-  __TEXT.__cstring: 0x13a01
+6.58.55.0.0
+  __TEXT.__text: 0x6d29a0
+  __TEXT.__auth_stubs: 0x1a60
+  __TEXT.__const: 0x6209b
+  __TEXT.__gcc_except_tab: 0x5e458
+  __TEXT.__cstring: 0x141c8
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x152fc
+  __TEXT.__unwind_info: 0x190d4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_methname: 0x24
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x1328
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x1338
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__const: 0x968
+  __DATA_CONST.__objc_classrefs: 0x8
+  __AUTH_CONST.__const: 0x95c0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH_CONST.__auth_got: 0xd40
+  __AUTH.__data: 0x30
   __DATA.__got_weak: 0x8
-  __DATA.__objc_classrefs: 0x8
-  __DATA.__data: 0xbb20
+  __DATA.__data: 0xbef8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xff0
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__const: 0x240b8
+  __DATA.__bss: 0xf70
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__const: 0x23068
   __DATA_DIRTY.__data: 0x60
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14073
-  Symbols:   953
-  CStrings:  1900
+  Functions: 17022
+  Symbols:   1020
+  CStrings:  1982
 
Symbols:
+ _VZDataCreateWithImage
+ _VZDataGetCVPixelBufferView
+ _VZDataGetContainedCVPixelBuffer
+ _VZDataGetImage
+ _VZDataInfoGetAssociatedSpace
+ _VZDataInfoGetSpace
+ _VZDataInfoSetSpace
+ _VZFileImporterGetCurrentDataTypeID
+ _VZFileImporterGetCurrentFilePath
+ _VZFileImporterGetCurrentOffsetInFile
+ _VZFileImporterGetCurrentPackageID
+ _VZFileImporterGetCurrentSubloggerName
+ _VZImageCreateCopy
+ _VZImageCreateDefault
+ _VZImageCreateUninitialized
+ _VZImageCreateWithBytes
+ _VZImageCreateWithCVPixelBuffer
+ _VZImageEqual
+ _VZImageGetBaseAddress
+ _VZImageGetBaseAddressMutable
+ _VZImageGetByteSize
+ _VZImageGetBytesPerRow
+ _VZImageGetCVPixelBufferView
+ _VZImageGetContainedCVPixelBuffer
+ _VZImageGetFormat
+ _VZImageGetHeight
+ _VZImageGetTypeID
+ _VZImageGetWidth
+ _VZPixelFormatGetBytesPerPixel
+ _VZPixelFormatGetBytesPerValue
+ _VZPixelFormatGetChannels
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__14__fs10filesystem16_FilesystemClock3nowEv
+ __ZNSt3__16localeaSERKS0_
+ __ZnamSt11align_val_t
+ __os_log_pack_fill
+ __os_log_pack_size
+ _kVZPixelFormatAbgr16f
+ _kVZPixelFormatAbgr16u
+ _kVZPixelFormatAbgr32f
+ _kVZPixelFormatAbgr8u
+ _kVZPixelFormatArgb16f
+ _kVZPixelFormatArgb16u
+ _kVZPixelFormatArgb32f
+ _kVZPixelFormatArgb8u
+ _kVZPixelFormatBgr16f
+ _kVZPixelFormatBgr16u
+ _kVZPixelFormatBgr32f
+ _kVZPixelFormatBgr8u
+ _kVZPixelFormatBgra16f
+ _kVZPixelFormatBgra16u
+ _kVZPixelFormatBgra32f
+ _kVZPixelFormatBgra8u
+ _kVZPixelFormatFour16f
+ _kVZPixelFormatFour16u
+ _kVZPixelFormatFour32f
+ _kVZPixelFormatFour8u
+ _kVZPixelFormatGray16f
+ _kVZPixelFormatGray16u
+ _kVZPixelFormatGray32f
+ _kVZPixelFormatGray8u
+ _kVZPixelFormatInvalid
+ _kVZPixelFormatRgb16f
+ _kVZPixelFormatRgb16u
+ _kVZPixelFormatRgb32f
+ _kVZPixelFormatRgb8u
+ _kVZPixelFormatRgba16f
+ _kVZPixelFormatRgba16u
+ _kVZPixelFormatRgba32f
+ _kVZPixelFormatRgba8u
+ _kVZPixelFormatThree16f
+ _kVZPixelFormatThree16u
+ _kVZPixelFormatThree32f
+ _kVZPixelFormatThree8u
+ _kVZPixelFormatTwo16f
+ _kVZPixelFormatTwo16u
+ _kVZPixelFormatTwo32f
+ _kVZPixelFormatTwo8u
+ _os_log_pack_send
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC1EOS5_
- _strncpy
CStrings:
+ " .\\/:*?|<>\""
+ " and pixel format "
+ " for format list "
+ " is invalid for pixel format "
+ " is invalid for the given size "
+ "' for image creation with buffer type '"
+ "'. Must be one of `kVZPixelFormat`... "
+ "(bytes_per_row % bytes_per_pixel == 0)"
+ "(last == kSuccess)"
+ "(mesh.colors.size() == 0 || mesh.colors.size() == mesh.vertices.size())"
+ "(mesh.colors_type == TriMeshMetadataType::PerVertex || mesh.colors_type == TriMeshMetadataType::Unknown)"
+ "(mesh.normals_type == TriMeshMetadataType::PerVertex || mesh.normals_type == TriMeshMetadataType::Unknown)"
+ "(mesh.tex_faces.size() == 0)"
+ "(mesh.tex_faces.size() == mesh.faces.size())"
+ ") = "
+ ") x width ("
+ ")."
+ ". It must be a multiple of the pixel byte size ("
+ ". It must be aligned with the value type size ("
+ ". It must be at least: pixel byte size ("
+ ".tif"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Thread/src/DispatchQueue.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Thread/src/DispatchQueueTypeUtil.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/Format.h"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/src/ExternalBuffer.cpp"
+ "Abort: "
+ "Context may not be nullptr"
+ "ExportImageData requires data to be ImageData"
+ "ExportMeshData requires data to be MeshData"
+ "File"
+ "Format is not serializable. Must be a non-dynamic format."
+ "Function should contain valid target"
+ "Given data block is too big to be represented by uint32_t indexed ArrayView"
+ "IOSurfaceCVPixelBuffer"
+ "Image base address "
+ "Image row byte stride "
+ "Invalid runtime format "
+ "More than one error occurred"
+ "Number of keys must match number of values"
+ "OSLogAppender"
+ "VZDataCreateWithImage"
+ "VZDataGetCVPixelBufferView"
+ "VZDataGetContainedCVPixelBuffer"
+ "VZDataGetImage"
+ "VZDataInfoGetAssociatedSpace"
+ "VZDataInfoGetSpace"
+ "VZDataInfoSetSpace"
+ "VZFileImporterGetCurrentDataTypeID"
+ "VZFileImporterGetCurrentFilePath"
+ "VZFileImporterGetCurrentOffsetInFile"
+ "VZFileImporterGetCurrentPackageID"
+ "VZFileImporterGetCurrentSubloggerName"
+ "VZImageCreateCopy"
+ "VZImageCreateWithBytes"
+ "VZImageEqual"
+ "VZImageGetBaseAddress"
+ "VZImageGetBaseAddressMutable"
+ "VZImageGetByteSize"
+ "VZImageGetBytesPerRow"
+ "VZImageGetCVPixelBufferView"
+ "VZImageGetContainedCVPixelBuffer"
+ "VZImageGetFormat"
+ "VZImageGetHeight"
+ "VZImageGetWidth"
+ "VZPixelFormatGetBytesPerPixel"
+ "VZPixelFormatGetBytesPerValue"
+ "VZPixelFormatGetChannels"
+ "Wrong v fields for reading position"
+ "Wrong vn fields for reading position"
+ "Wrong vt fields for reading position"
+ "_f"
+ "bytes_per_row >= min_bytes_per_row"
+ "cannot return data as VZImage"
+ "context"
+ "context != nullptr"
+ "dispatch_group_wait failed"
+ "dynamic format properties only known at runtime"
+ "error == 0"
+ "for meshes with texture coords, mesh's #tex_faces must be equal to #faces"
+ "for meshes without texture coords, mesh's #tex_faces must be zero"
+ "format != img::Format::Dynamic"
+ "image does not contain a CVPixelBuffer"
+ "image of pixel format '"
+ "image_data_ptr"
+ "invalid VZBufferType value"
+ "invalid VZPixelFormat value '"
+ "invalid image format '"
+ "invalid value for `ImageInitialization`"
+ "keys.size() == values.size()"
+ "loader must specify the format to load as"
+ "maybe_format"
+ "mesh's #colors must be either zero or equal to #vertices"
+ "mesh_data_ptr"
+ "obj export requires per-vertex colors"
+ "obj export requires per-vertex normals"
+ "priv().initialized_root_appenders_ == current_root_appenders"
+ "read_count == 2"
+ "read_count == 3"
+ "read_count == 3 || read_count == 6"
+ "root appenders have been illegally modified between Initialize() and Enable() of APILogging"
+ "root appenders have been illegally modified between Initialize() and EnableInternal() of APILogging"
+ "scheduler must be valid"
+ "space"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 5U]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = VZImage]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::esn::arr::SizeT<2, cv3d::esn::arr::SizeType::Shape, void>]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::kio::ProtocolInfoSample]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::kio::Version]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vl::visual_logger::BufferType]"
+ "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = void (void *, const void *)]"
+ "stride must be multiple of pixel size"
+ "stride must not overlap internally"
+ "total_size < std::numeric_limits<uint32_t>::max()"
+ "unique_lock::lock: already locked"
+ "unique_lock::lock: references null mutex"
- "(bytes_per_row % bytes_per_pixel == 0) && \"stride must be multiple of pixel size\""
- "(last == kSuccess) && \"More than one error occurred\""
- "(mesh.colors.size() == 0 || mesh.colors.size() == mesh.vertices.size()) && \"mesh's #colors must be either zero or equal to #vertices\""
- "(mesh.colors_type == TriMeshMetadataType::PerVertex || mesh.colors_type == TriMeshMetadataType::Unknown) && \"obj export requires per-vertex colors\""
- "(mesh.normals_type == TriMeshMetadataType::PerVertex || mesh.normals_type == TriMeshMetadataType::Unknown) && \"obj export requires per-vertex normals\""
- "(mesh.tex_faces.size() == 0) && \"for meshes without texture coords, mesh's #tex_faces must be zero\""
- "(mesh.tex_faces.size() == mesh.faces.size()) && \"for meshes with texture coords, mesh's #tex_faces must be equal to #faces\""
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Thread/src/WorkQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Thread/src/WorkQueueTypeUtil.cpp"
- "NetworkOutputNodeAsync"
- "OSLogSurrogateAppender"
- "Production"
- "_f && \"Function should contain valid target\""
- "bytes_per_row >= min_bytes_per_row && \"stride must not overlap internally\""
- "const "
- "contained image data does not contain a CVPixelBuffer"
- "context != nullptr && \"Context may not be nullptr\""
- "context && \"Context may not be nullptr\""
- "error == 0 && \"dispatch_group_wait failed\""
- "format != img::Format::Dynamic && \"loader must specify the format to load as\""
- "image_data_ptr && \"ExportImageData requires data to be ImageData\""
- "impl_"
- "keys.size() == values.size() && \"Number of keys must match number of values\""
- "maybe_format && \"Format is not serializable. Must be a non-dynamic format.\""
- "mesh_data_ptr && \"ExportMeshData requires data to be MeshData\""
- "priv().initialized_root_appenders_ == current_root_appenders && \"root appenders have been illegally modified between Initialize() and \" \"Enable() of APILogging\""
- "priv().initialized_root_appenders_ == current_root_appenders && \"root appenders have been illegally modified between Initialize() and \" \"EnableInternal() of APILogging\""
- "read_count == 2 && \"Wrong vt fields for reading position\""
- "read_count == 3 && \"Wrong vn fields for reading position\""
- "read_count == 3 || read_count == 6 && \"Wrong v fields for reading position\""
- "scheduler_ && \"scheduler must be valid\""
- "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ProtocolInfoSample]"
- "static std::string cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::Version]"
- "total_size < std::numeric_limits<uint32_t>::max() && \"Given data block is too big to be represented by uint32_t indexed ArrayView\""

```
