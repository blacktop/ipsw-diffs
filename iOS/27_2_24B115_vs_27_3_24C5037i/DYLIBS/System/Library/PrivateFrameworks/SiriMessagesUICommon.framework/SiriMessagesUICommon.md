## SiriMessagesUICommon

> `/System/Library/PrivateFrameworks/SiriMessagesUICommon.framework/SiriMessagesUICommon`

```diff

-3605.21.1.11.2
-  __TEXT.__text: 0xa443c
-  __TEXT.__const: 0xbc94
-  __TEXT.__cstring: 0x3374
-  __TEXT.__swift5_typeref: 0x2274
-  __TEXT.__swift5_reflstr: 0x215e
-  __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__constg_swiftt: 0x2290
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0x2ed4
-  __TEXT.__oslogstring: 0x225a
-  __TEXT.__swift5_proto: 0xae4
-  __TEXT.__swift5_types: 0x31c
-  __TEXT.__swift_as_entry: 0xf4
-  __TEXT.__swift_as_ret: 0x128
+3610.11.1.0.0
+  __TEXT.__text: 0xa8160
+  __TEXT.__const: 0xc094
+  __TEXT.__cstring: 0x33e4
+  __TEXT.__swift5_typeref: 0x231a
+  __TEXT.__swift5_reflstr: 0x21be
+  __TEXT.__swift5_assocty: 0x318
+  __TEXT.__constg_swiftt: 0x2334
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_fieldmd: 0x2f48
+  __TEXT.__oslogstring: 0x23fa
+  __TEXT.__swift5_proto: 0xb24
+  __TEXT.__swift5_types: 0x328
+  __TEXT.__swift_as_entry: 0xf8
+  __TEXT.__swift_as_ret: 0x12c
   __TEXT.__swift_as_cont: 0x1a4
   __TEXT.__swift5_capture: 0x4a8
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4b20
-  __TEXT.__eh_frame: 0x53a0
+  __TEXT.__unwind_info: 0x4c08
+  __TEXT.__eh_frame: 0x5450
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x4a8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x740
+  __DATA_CONST.__objc_selrefs: 0x750
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x75d0
+  __AUTH_CONST.__const: 0x75c0
   __AUTH_CONST.__objc_const: 0xbd8
-  __AUTH_CONST.__auth_got: 0x11b0
+  __AUTH_CONST.__auth_got: 0x1238
   __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x990
-  __DATA.__data: 0x1738
+  __AUTH.__data: 0xab8
+  __DATA.__data: 0x1828
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x1c0
   __DATA_DIRTY.__data: 0x1ce0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6191
-  Symbols:   1552
-  CStrings:  518
+  Functions: 6281
+  Symbols:   1582
+  CStrings:  529
 
Symbols:
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithData
+ _CGImageDestinationFinalize
+ _CGImageSourceCreateThumbnailAtIndex
+ _CGImageSourceCreateWithURL
+ _NSFileType
+ _NSFileTypeSymbolicLink
+ _NSURLFileResourceIdentifierKey
+ _OBJC_CLASS_$_NSMutableData
+ _OUTLINED_FUNCTION_211
+ ___swift_memcpy18_8
+ _associated conformance So11CFStringRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So11CFStringRefaSHSCSQ
+ _associated conformance So16NSURLResourceKeyaSHSCSQ
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So19NSFileAttributeTypeaSHSCSQ
+ _associated conformance So19NSFileAttributeTypeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So19NSFileAttributeTypeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _kCGImageDestinationLossyCompressionQuality
+ _kCGImageSourceCreateThumbnailFromImageAlways
+ _kCGImageSourceCreateThumbnailWithTransform
+ _kCGImageSourceShouldCache
+ _kCGImageSourceShouldCacheImmediately
+ _kCGImageSourceThumbnailMaxPixelSize
+ _symbolic _____ So16NSURLResourceKeya
+ _symbolic _____ So19NSFileAttributeTypea
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____y_____G s11_SetStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16NSURLResourceKeya
+ _symbolic _____y______SbtG s23_ContiguousArrayStorageC So11CFStringRefa
+ _symbolic _____y______SdtG s23_ContiguousArrayStorageC So11CFStringRefa
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So11CFStringRefa
+ _type_layout_string So30PHAssetExportRequestFileURLKeya
- ___swift_memcpy112_8
- _type_layout_string 20SiriMessagesUICommon13CarPlayHeaderV
- _type_layout_string 20SiriMessagesUICommon25TapbackPromptSnippetModelV
- _type_layout_string So18NSFileAttributeKeya
CStrings:
+ "#PhotoAssetManager could not create JPEG destination for %s"
+ "#PhotoAssetManager could not create thumbnail for %s"
+ "#PhotoAssetManager could not encode thumbnail for %s"
+ "#PhotoAssetManager could not open image source for %s"
+ "#TemporaryFileManager '%s' is already in the temp dir, not copying"
+ "#TemporaryFileManager rejected filename '%s' at an existing symlink"
+ "#TemporaryFileManager rejected invalid filename '%s'"
+ "SCHEDULED_DATE_CLEARED"
+ "SCHEDULED_DATE_TAPPED"
+ "SendMessage#MessageScheduled"
+ "UnsendSentMessage"
+ "isScheduledToSendLater"
+ "payload"
+ "serviceType"
- "#PhotoAssetManager error loading thumbnail from %s: %@"
- "EditLastMessageSentWithSiri"
- "UnsendLastMessageSentWithSiri"
```
