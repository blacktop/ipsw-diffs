## SplashBoard

> `/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard`

```diff

-302.2.3.0.0
-  __TEXT.__text: 0x28bfc
-  __TEXT.__auth_stubs: 0xc80
+306.0.0.0.0
+  __TEXT.__text: 0x295c0
+  __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x2588
   __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x25f5
+  __TEXT.__cstring: 0x269b
   __TEXT.__gcc_except_tab: 0xb58
-  __TEXT.__oslogstring: 0x2e1b
+  __TEXT.__oslogstring: 0x2fc6
   __TEXT.__ustring: 0x2a
-  __TEXT.__unwind_info: 0xc40
+  __TEXT.__unwind_info: 0xc60
   __TEXT.__objc_classname: 0x4e5
-  __TEXT.__objc_methname: 0x61d3
+  __TEXT.__objc_methname: 0x6208
   __TEXT.__objc_methtype: 0xe77
-  __TEXT.__objc_stubs: 0x4ce0
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0xde8
+  __TEXT.__objc_stubs: 0x4d20
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0xdc0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1710
+  __DATA_CONST.__objc_selrefs: 0x1718
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x2cc0
+  __AUTH_CONST.__cfstring: 0x2da0
   __AUTH_CONST.__objc_const: 0x6ae8
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x284
   __DATA.__data: 0x4e8

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5288649-708B-3C72-86CB-21E049062247
-  Functions: 1083
-  Symbols:   3945
-  CStrings:  2177
+  UUID: 978E3BDD-7A25-3959-A8A0-E5E62069A009
+  Functions: 1097
+  Symbols:   3988
+  CStrings:  2200
 
Symbols:
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.10
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.11
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.12
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.13
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.14
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.15
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.16
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.17
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.4
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.5
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.6
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.7
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.8
+ -[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:].cold.9
+ GCC_except_table183
+ GCC_except_table190
+ _CloseStreamCompressor
+ _CreateStreamCompressor
+ _CreateStreamCompressorQueueWithOptions
+ _FinishStreamCompressorQueue
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _VolumeSupportsCompression
+ _WriteToStreamCompressor
+ ___block_literal_global.310
+ ___block_literal_global.447
+ _kAFSCCompressionSystemRulesKey
+ _kAFSCCompressionTypes
+ _kAFSCForceAsynchronous
+ _kAFSCSynchronous
+ _kAFSCThrottledIO
+ _kCGImagePropertyASTCPreTwiddle
+ _objc_msgSend$fileFormat
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- GCC_except_table184
- GCC_except_table191
- ___76-[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:]_block_invoke
- ___76-[XBApplicationSnapshotManifestImpl _imageAccessQueue_saveData:forSnapshot:]_block_invoke.cold.1
- ___block_descriptor_56_e8_32s40s48s_e8_B12?0i8ls32l8s40l8s48l8
- ___block_literal_global.302
- ___block_literal_global.439
CStrings:
+ "%{public}@ Compressed write for %@ failed; falling back to uncompressed write"
+ "%{public}@ Failed to open fd for %@: (%s)"
+ "%{public}@ Failed to write to fd for %@: (%s)"
+ "CloseStreamCompressor() failed for %@: (%s)"
+ "CreateStreamCompressor() failed for %@: (%s)"
+ "CreateStreamCompressorQueueWithOptions() failed for %@: (%s)"
+ "FinishStreamCompressorQueue() failed for %@: (%s)"
+ "Volume for %@ does not support filesystem compression"
+ "WriteToStreamCompressor() failed for %@: (%s)"
+ "[data length] != 0"
+ "data != NULL"
+ "data != nil"
+ "fd >= 0"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "path != nil"
+ "size > 0"
+ "snapshot != nil"
+ "ssize_t AFSCCompressDataAndWriteToFile(int, NSString *__strong, const void *, size_t)"
- "%{public}@ Failed to write to %@: (%s)"
- "B12@?0i8"

```
