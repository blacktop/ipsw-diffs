## demod

> `/usr/libexec/demod`

```diff

-1611.40.25.0.0
-  __TEXT.__text: 0xe7d40
-  __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_stubs: 0x18c60
-  __TEXT.__objc_methlist: 0xc16c
-  __TEXT.__const: 0x27a
-  __TEXT.__gcc_except_tab: 0x49f8
-  __TEXT.__oslogstring: 0x192bc
-  __TEXT.__cstring: 0xf2ea
-  __TEXT.__objc_classname: 0x1619
-  __TEXT.__objc_methtype: 0x38fc
-  __TEXT.__objc_methname: 0x1d0a3
+1611.60.7.0.0
+  __TEXT.__text: 0xe9120
+  __TEXT.__auth_stubs: 0x1cd0
+  __TEXT.__objc_stubs: 0x18dc0
+  __TEXT.__objc_methlist: 0xc1b4
+  __TEXT.__const: 0x282
+  __TEXT.__gcc_except_tab: 0x4a44
+  __TEXT.__oslogstring: 0x1965c
+  __TEXT.__cstring: 0xf3ea
+  __TEXT.__objc_classname: 0x1625
+  __TEXT.__objc_methtype: 0x390d
+  __TEXT.__objc_methname: 0x1d18f
   __TEXT.__swift5_typeref: 0x63
   __TEXT.__swift5_capture: 0x48
   __TEXT.__constg_swiftt: 0x38

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__unwind_info: 0x33c0
   __TEXT.__eh_frame: 0x120
-  __DATA_CONST.__auth_got: 0xe28
-  __DATA_CONST.__got: 0xce8
+  __DATA_CONST.__auth_got: 0xe78
+  __DATA_CONST.__got: 0xcf0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2d38
-  __DATA_CONST.__cfstring: 0xd980
+  __DATA_CONST.__const: 0x2d40
+  __DATA_CONST.__cfstring: 0xd9a0
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x3c0
-  __DATA_CONST.__objc_intobj: 0x4e0
+  __DATA_CONST.__objc_intobj: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x890
   __DATA_CONST.__objc_arrayobj: 0x438
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA.__objc_const: 0x17038
-  __DATA.__objc_selrefs: 0x72d0
+  __DATA.__objc_selrefs: 0x7328
   __DATA.__objc_ivar: 0xa1c
   __DATA.__objc_data: 0x4200
   __DATA.__data: 0x2670

   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libcompression.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 687D6EDB-2D68-3977-9280-D85473DAD458
-  Functions: 5335
-  Symbols:   904
-  CStrings:  11661
+  UUID: BADF0651-A492-33AD-BD16-F4DD3BFE7A0D
+  Functions: 5349
+  Symbols:   915
+  CStrings:  11700
 
Symbols:
+ _CGImageRelease
+ _CGImageRetain
+ _OBJC_CLASS_$_UIColor
+ _UIGraphicsBeginImageContextWithOptions
+ _UIGraphicsEndImageContext
+ _UIGraphicsGetImageFromCurrentImageContext
+ _UIRectFill
+ _compression_encode_buffer
+ _compression_stream_destroy
+ _compression_stream_init
+ _compression_stream_process
CStrings:
+ "%s - %{public}@ - Failed to convert UI image to JPEG representation."
+ "%s - %{public}@ - Failed to normalize uiImage."
+ "%s - %{public}@ - Redrawing UI image."
+ "%s - %{public}@ - Successful JPEG conversion after UI after redraw."
+ "%s - %{public}@ - Successful JPEG conversion after UI normalization."
+ "%s - %{public}@ - Successful direct JPEG conversion."
+ "%s - Compressed size:   %lu"
+ "%s - Decompressed size: %lu"
+ "%s - Decompression error"
+ "%s - Failed to init compression stream"
+ "%s - Failed to malloc buffer of size: %lu"
+ "%s - MSDPeerProtocolVersionCurrent: %ld"
+ "%s - Size of archiveIconImageDict:           %ld bytes."
+ "%s - Size of compressedArchiveIconImageDict: %ld bytes."
+ "%s - Size of compressedIconImageArchiveData:   %ld bytes."
+ "%s - Size of decompressedIconImageArchiveData: %ld bytes."
+ "%s - Uncompressed size: %lu"
+ "%s - Unexpected decompression status: %d"
+ "%s - compression_encode_buffer failed."
+ "%s - protocolVersion: %ld"
+ "+[MSDAppIcon convertUIImageToJPEG:withQuality:forApp:]"
+ "-[MSDDemoPeerCommander getIconImagesOfVisibleAppsOnPeerOfID:height:width:scale:withCompletion:]_block_invoke"
+ "-[NSData(Compression) compress]"
+ "-[NSData(Compression) decompress]"
+ "16"
+ "@40@0:8@16d24@32"
+ "AppIconCompressedArchiveDict"
+ "Compression"
+ "Failed to configure iCloud account features: %{public}@"
+ "_configureiCloudAccountFeatures:withError:"
+ "_getRequestTimeoutForRequest:"
+ "compress"
+ "configureiCloudAccountFeatures:withError:"
+ "convertUIImageToJPEG:withQuality:forApp:"
+ "decompress"
+ "drawInRect:"
+ "imageWithCGImage:scale:orientation:"
+ "scale"
+ "setFill"
+ "size"
+ "whiteColor"
- "%s - Successfully archive iconImageDict."
- "15"
- "imageWithCGImage:"

```
