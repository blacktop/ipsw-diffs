## com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x1d730
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x3fc0
-  __TEXT.__objc_methlist: 0x1eb8
+800.14.111.0.0
+  __TEXT.__text: 0x1dc48
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x4140
+  __TEXT.__objc_methlist: 0x1f28
   __TEXT.__const: 0xa0
   __TEXT.__objc_classname: 0x2ad
-  __TEXT.__objc_methname: 0x4b76
-  __TEXT.__objc_methtype: 0xaad
+  __TEXT.__objc_methname: 0x4cac
+  __TEXT.__objc_methtype: 0xab0
   __TEXT.__oslogstring: 0x635
-  __TEXT.__cstring: 0x6531
+  __TEXT.__cstring: 0x683f
   __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__unwind_info: 0x6f0
-  __DATA_CONST.__auth_got: 0x7a0
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__unwind_info: 0x700
+  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xbd0
-  __DATA_CONST.__cfstring: 0x5c20
+  __DATA_CONST.__cfstring: 0x5d20
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__objc_arraydata: 0x1a0
+  __DATA_CONST.__objc_arraydata: 0x1a8
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_const: 0x2a38
-  __DATA.__objc_selrefs: 0x1368
-  __DATA.__objc_ivar: 0x204
+  __DATA.__objc_const: 0x2ab8
+  __DATA.__objc_selrefs: 0x13c8
+  __DATA.__objc_ivar: 0x208
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x558
   __DATA.__bss: 0xe0

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary
+  - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 6E6B65A4-C894-3611-8FBD-DC5EFAA75ED2
-  Functions: 683
-  Symbols:   386
-  CStrings:  2688
+  UUID: F3CF5194-54F3-3486-AC9C-5ABD0D3A667F
+  Functions: 690
+  Symbols:   387
+  CStrings:  2726
 
Symbols:
+ _CPLIsCollectionShareFeatureEnabled
+ _OBJC_CLASS_$_PFAppleArchive
+ _PFAppleArchiveExtension
- __os_feature_enabled_impl
- _objc_retain_x27
CStrings:
+ "  Failed to open archive for writing: %@"
+ "  Failed to write archive: %@"
+ "%@\n"
+ "%@-%@-T%s%@"
+ "%@-T%s%@"
+ "/var/mobile/Media/MediaAnalysis/MediaAnalysis.sqlite"
+ "@36@0:8i16B20B24B28B32"
+ "COLORTERM"
+ "DSID: %@\n"
+ "ImagePlayground"
+ "MPS"
+ "MediaAnalysis.sqlite"
+ "MediaAnalysis/MediaAnalysis.sqlite"
+ "MediaAnalysisSystem.sqlite"
+ "No dataclasses enabled\n"
+ "PhotosDiagnosticsAppleArchive"
+ "SharedAlbum"
+ "TB,R,N,V_supports24BitColor"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=28"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=46"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=73"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=74"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=78"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=79"
+ "UPDATE ZRESULT SET ZRESULTS=null WHERE ZRESULTSTYPE=82"
+ "Unexpected nil destinationPath. libraryPath: %@, filepath: %@"
+ "_supports24BitColor"
+ "aa_personID"
+ "close:"
+ "diagnosticExtension"
+ "encodeContentOfDirectoryAtURL:entryPredicate:error:"
+ "initWithArchiveURL:"
+ "initWithFileDescriptor:isATTY:supportsEscapeSequences:usesColor:supports24BitColor:"
+ "mediaAnalysisSystemDatabasePath"
+ "openForWriting:"
+ "private/com.apple.mediaanalysisd/MediaAnalysis/MediaAnalysis.sqlite"
+ "setTransportShare:"
+ "supports24BitColor"
+ "transportShare"
+ "truecolor"
+ "update ZSHARE set ZSHAREURL = filterMomentShareURL(ZSHAREURL), ZPREVIEWDATA = null, ZTHUMBNAILIMAGEDATA = null, ZCKSHAREDATA = null"
+ "update ZSHARE set ZSHAREURL = null, ZPREVIEWDATA = null, ZTHUMBNAILIMAGEDATA = null, ZCKSHAREDATA = null"
+ "useAppleArchive"
+ "userLibraryDir"
- "%@-%@-T%s%@.tgz"
- "%@-T%s%@.tgz"
- "@32@0:8i16B20B24B28"
- "CPL "
- "Enabled accounts: "
- "ImagePlayground "
- "MPS "
- "MemoryCreation"
- "No accounts enabled\n"
- "SharedAlbum "
- "Unexpect nil libraryPath for UBF library. Filepath: %@"
- "initWithFileDescriptor:isATTY:supportsEscapeSequences:usesColor:"
- "update ZSHARE set ZSHAREURL = filterMomentShareURL(ZSHAREURL), ZPREVIEWDATA = null"
- "update ZSHARE set ZSHAREURL = null, ZPREVIEWDATA = null"

```
