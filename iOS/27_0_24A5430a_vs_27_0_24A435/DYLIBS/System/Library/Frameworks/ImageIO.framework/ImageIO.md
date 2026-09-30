## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

 2851.0.0.0.0
-  __TEXT.__text: 0x5028a4
+  __TEXT.__text: 0x5035b4
   __TEXT.__objc_methlist: 0xd58
   __TEXT.__const: 0x49ed0
-  __TEXT.__gcc_except_tab: 0x2298c
-  __TEXT.__cstring: 0xa667d
+  __TEXT.__gcc_except_tab: 0x229c0
+  __TEXT.__cstring: 0xa6a6d
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x26a4
   __TEXT.__swift5_typeref: 0x3d88

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x13880
-  __TEXT.__eh_frame: 0x9214
+  __TEXT.__unwind_info: 0x13890
+  __TEXT.__eh_frame: 0x921c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__got: 0xaa8
   __AUTH_CONST.__const: 0x4f290
-  __AUTH_CONST.__cfstring: 0x35fe0
+  __AUTH_CONST.__cfstring: 0x36000
   __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20

   __DATA_DIRTY.__data: 0x3b0
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xbe8
-  __DATA_DIRTY.__common: 0xfb8
+  __DATA_DIRTY.__common: 0xff0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 23178
-  Symbols:   24716
-  CStrings:  18232
+  Functions: 23179
+  Symbols:   24725
+  CStrings:  18247
 
Symbols:
+ __ZL33IIOCopyDNGProvenanceFromContainerPK14__CFDictionaryPK10__CFString
+ __ZN14IIOImageSource25copyProvenanceDataAtIndexEmP21CGImageProvenanceType
+ _gFunc_CMPhotoDNGCopyProperties
+ _gIIO_kCMPhotoCustomMetadataTypeURN_Provenance_LowerBoundTimeStamp
+ _gIIO_kCMPhotoCustomMetadataTypeURN_Provenance_ProcessedImage
+ _gIIO_kCMPhotoCustomMetadataTypeURN_Provenance_UnprocessedImage
+ _gIIO_kCMPhotoCustomMetadataTypeURN_Provenance_UpperBoundTimeStamp
+ _gIIO_kCMPhoto_CGImagePropertyDNGProvenanceProcessedImage
+ _gIIO_kCMPhoto_CGImagePropertyDNGProvenanceUnprocessedImage
CStrings:
+ "*** CMPhotoCompressionSessionAddCustomMetadata (provenance) err = %s [%d]\n"
+ "CMPhotoDNGCopyProperties"
+ "kCMPhotoCustomMetadataTypeURN_Provenance_LowerBoundTimeStamp"
+ "kCMPhotoCustomMetadataTypeURN_Provenance_ProcessedImage"
+ "kCMPhotoCustomMetadataTypeURN_Provenance_UnprocessedImage"
+ "kCMPhotoCustomMetadataTypeURN_Provenance_UpperBoundTimeStamp"
+ "kCMPhoto_CGImagePropertyDNGProvenanceProcessedImage"
+ "kCMPhoto_CGImagePropertyDNGProvenanceUnprocessedImage"
+ "❌  failed to load 'CMPhotoDNGCopyProperties' [%s]\n"
+ "❌  failed to load 'kCMPhotoCustomMetadataTypeURN_Provenance_LowerBoundTimeStamp' [%s]\n"
+ "❌  failed to load 'kCMPhotoCustomMetadataTypeURN_Provenance_ProcessedImage' [%s]\n"
+ "❌  failed to load 'kCMPhotoCustomMetadataTypeURN_Provenance_UnprocessedImage' [%s]\n"
+ "❌  failed to load 'kCMPhotoCustomMetadataTypeURN_Provenance_UpperBoundTimeStamp' [%s]\n"
+ "❌  failed to load 'kCMPhoto_CGImagePropertyDNGProvenanceProcessedImage' [%s]\n"
+ "❌  failed to load 'kCMPhoto_CGImagePropertyDNGProvenanceUnprocessedImage' [%s]\n"
```
