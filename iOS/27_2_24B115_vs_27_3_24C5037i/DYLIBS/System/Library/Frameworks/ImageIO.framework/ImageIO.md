## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2851.1.8.0.0
-  __TEXT.__text: 0x4fbfa0
+2851.2.2.0.0
+  __TEXT.__text: 0x4fc64c
   __TEXT.__objc_methlist: 0xd68
   __TEXT.__const: 0x4a070
-  __TEXT.__gcc_except_tab: 0x22bec
-  __TEXT.__cstring: 0xa777d
+  __TEXT.__gcc_except_tab: 0x22bf8
+  __TEXT.__cstring: 0xa7b1d
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x26a4
   __TEXT.__swift5_typeref: 0x3d88

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x18378
+  __TEXT.__unwind_info: 0x18380
   __TEXT.__eh_frame: 0x9324
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b890
+  __DATA_CONST.__const: 0x4b898
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__got: 0xb18
   __AUTH_CONST.__const: 0x4f498
-  __AUTH_CONST.__cfstring: 0x36100
+  __AUTH_CONST.__cfstring: 0x36120
   __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2fc0
+  __AUTH_CONST.__auth_got: 0x2fe0
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x15c8
   __AUTH.__thread_vars: 0x18

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/ASRKit.framework/ASRKit
   - /System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 23239
-  Symbols:   24492
-  CStrings:  18318
+  Functions: 23245
+  Symbols:   24506
+  CStrings:  18354
 
Symbols:
+ _IIO_GetClientAuditToken
+ __Z18IIOAsrAllowsParserPKc
+ __ZL17gClientAuditToken
+ __ZL20gHasClientAuditToken
+ __ZL21gClientAuditTokenLock
+ __ZN10IIO_Reader14isAllowedByAsrEv
+ __ZN10IIO_ReaderC2EPKPK10__CFStringPKcjS6_mm
+ __ZN13IIOReadPlugin14isAllowedByAsrEv
+ __ZN13IIOReadPluginC2EP11CGImagePlusjxjPKc
+ __ZN13IIOReadPluginC2EP18ReadPluginInitDatajPKc
+ __ZN14IIOImageSource13setHintReaderE13IIOSnifferRef
+ __ZN14JPEGReadPluginC2EP11CGImagePlusjmmbjPvjPKc
+ __ZN14JPEGReadPluginC2EP18ReadPluginInitDatajPKc
+ __ZN17IIO_ReaderHandler12lookupReaderEPK10__CFStringjb
+ __ZN17IIO_ReaderHandler14snifferForTypeEj
+ __ZN17IIO_ReaderHandler16snifferForUTTypeEPK10__CFString
+ __ZN17IIO_ReaderHandler23snifferForPathExtensionEPK10__CFString
+ __ZN20CommonASTCReadPluginC2EP11CGImagePlusjxjPKc
+ __ZN20CommonASTCReadPluginC2EP18ReadPluginInitDatajPKc
+ _asr_check_parser
+ _asr_check_parser_for_token
+ _kIIOPluginAsrId
+ _sandbox_get_container_expected
+ _xpc_connection_get_audit_token
- __ZN10IIO_ReaderC2EPKPK10__CFStringPKcjmm
- __ZN13IIOReadPluginC2EP11CGImagePlusjxj
- __ZN13IIOReadPluginC2EP18ReadPluginInitDataj
- __ZN14IIOImageSource13setHintReaderEP10IIO_Reader
- __ZN14JPEGReadPluginC2EP11CGImagePlusjmmbjPvj
- __ZN14JPEGReadPluginC2EP18ReadPluginInitDataj
- __ZN17IIO_ReaderHandler22readerForPathExtensionEPK10__CFString
- __ZN17IIO_ReaderHandler24readerForUTTypeAndOSTypeEPK10__CFStringj
- __ZN20CommonASTCReadPluginC2EP11CGImagePlusjxj
- __ZN20CommonASTCReadPluginC2EP18ReadPluginInitDataj
CStrings:
+ "*** ERROR: PHOTOMETRIC_PALETTE with samplesPerPixel %d at %d bpc is not supported\n"
+ "*** ERROR: no client audit token for ASR check of '%s' - denying\n"
+ "*** ImageIO OOP: container present (expected: %s), XPC look-up %s\n"
+ "ASRId"
+ "IIOAsrAllowsParser"
+ "allowed"
+ "com.apple.imageio.ai"
+ "com.apple.imageio.applejpeg"
+ "com.apple.imageio.astc"
+ "com.apple.imageio.atx"
+ "com.apple.imageio.bc"
+ "com.apple.imageio.bmp"
+ "com.apple.imageio.cmphoto"
+ "com.apple.imageio.cur"
+ "com.apple.imageio.etc"
+ "com.apple.imageio.gif"
+ "com.apple.imageio.icns"
+ "com.apple.imageio.ico"
+ "com.apple.imageio.jp2"
+ "com.apple.imageio.ktx"
+ "com.apple.imageio.ktx2"
+ "com.apple.imageio.libjpeg"
+ "com.apple.imageio.mpo"
+ "com.apple.imageio.openexr"
+ "com.apple.imageio.pbm"
+ "com.apple.imageio.pdf"
+ "com.apple.imageio.png"
+ "com.apple.imageio.psd"
+ "com.apple.imageio.pvrtc"
+ "com.apple.imageio.radiance"
+ "com.apple.imageio.rawcamera"
+ "com.apple.imageio.tga"
+ "com.apple.imageio.tiff"
+ "com.apple.imageio.webp"
+ "denied"
+ "isHighlySandboxedProcess"
```
