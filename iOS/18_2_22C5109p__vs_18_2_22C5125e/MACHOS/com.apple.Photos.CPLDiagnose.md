## com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x1c9cc
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_stubs: 0x3e40
-  __TEXT.__objc_methlist: 0x1934
-  __TEXT.__const: 0xf8
+720.4.101.0.0
+  __TEXT.__text: 0x1d0cc
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_stubs: 0x3f00
+  __TEXT.__objc_methlist: 0x196c
+  __TEXT.__const: 0xa0
   __TEXT.__objc_classname: 0x2ad
-  __TEXT.__objc_methname: 0x4a25
-  __TEXT.__objc_methtype: 0xb16
+  __TEXT.__objc_methname: 0x4b11
+  __TEXT.__objc_methtype: 0xaad
   __TEXT.__oslogstring: 0x635
-  __TEXT.__cstring: 0x61e1
-  __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__unwind_info: 0x698
-  __DATA_CONST.__auth_got: 0x778
+  __TEXT.__cstring: 0x6377
+  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__unwind_info: 0x6a8
+  __DATA_CONST.__auth_got: 0x780
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xbd0
-  __DATA_CONST.__cfstring: 0x5a20
+  __DATA_CONST.__cfstring: 0x5ba0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__objc_arraydata: 0x188
+  __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_const: 0x33b0
-  __DATA.__objc_selrefs: 0x1230
-  __DATA.__objc_ivar: 0x1f8
+  __DATA.__objc_const: 0x33f0
+  __DATA.__objc_selrefs: 0x1260
+  __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x558
   __DATA.__bss: 0xe0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 655
-  Symbols:   381
-  CStrings:  1939
+  Functions: 661
+  Symbols:   380
+  CStrings:  1959
 
Symbols:
+ _CPLContainerIdentifierForLibraryIdentifier
+ _objc_retain_x28
+ _realpath$DARWIN_EXTSN
- _CPLBundleIdentifierForLibraryIdentifier
- _com_apple_Photos_CPLDiagnoseVersionNumber
- _com_apple_Photos_CPLDiagnoseVersionString
- _objc_retain_x27
CStrings:
+ "  specified library path is the Syndication library"
+ "  specified library path is the System Library"
+ "-a photosDonationTimestamp -a photosSceneAnalysisVersion -a photosFaceAnalysisVersion -a photosMediaAnalysisImageVersion -a photosMediaAnalysisVersion -a photosCharacterRecognitionAnalysisVersion -a photosPrivateEncryptedComputeAnalysisVersion -a photosLocationPrivateEncryptedComputeAnalysisVersion -a photosImageEmbeddingVersion -a photosVideoEmbeddingVersion -a kMDItemPhotosResultType -a photosEmbeddingCount"
+ "-b"
+ "-b <bundleid>"
+ "-l cannot be used with -b"
+ "-l or -b are required if -n is specified"
+ "-n"
+ "/var/mobile/Library/Photos/Libraries/Syndication.photoslibrary"
+ "/var/mobile/Media"
+ "DiagnosticBundleID"
+ "ExcludeSPLAndSyndication"
+ "IncludeDatabases"
+ "IncludeSysdiagnose"
+ "LibraryURL"
+ "_determineLibraryPathFromDiagnoseBundleIdentifier:"
+ "_noAutoIncludeSPLAndSyndication"
+ "_syndicationLibraryPath"
+ "_targetLibraryIsSPL"
+ "_targetLibraryIsSyndication"
+ "caseInsensitiveCompare:"
+ "choose the library path using the bundle ID that matches a library container identifier"
+ "collectLOFetchRecordings"
+ "determineLibraryPaths"
+ "do not automatically include System Photo Library and Syndication library"
+ "includeSPL"
+ "includeSyndication"
+ "jujubectl photos analysisSummary --oneline --photo-library "
+ "o:l:tdDa:f:LcsSOmPir:nb:"
+ "runDiagnoseWithLibraryURL:bundleID:outputDirectoryURL:includeDatabases:includeSysdiagnose:excludeSPLAndSyndication:replyHandler:"
+ "runDiagnoseWithOptions:replyHandler:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSURL\"@\"NSError\">24"
+ "v60@0:8@16@24@32B40B44B48@?52"
- "- Could not determine location of client plist and CPL db"
- "-a photosDonationTimestamp -a photosSceneAnalysisVersion -a photosFaceAnalysisVersion -a photosMediaAnalysisImageVersion -a photosMediaAnalysisVersion -a photosCharacterRecognitionAnalysisVersion -a photosPrivateEncryptedComputeAnalysisVersion -a photosLocationPrivateEncryptedComputeAnalysisVersion -a kMDItemPhotosResultType -a photosEmbeddingCount"
- "Photos/Libraries/Messages.photoslibrary"
- "SyndicationLibrary"
- "collectFetchRecordingsFromSPL"
- "jujubectl photos analysisSummary --oneline --photo-library /var/mobile/Library/Photos/Libraries/Syndication.photoslibrary"
- "o:l:tdDa:f:LcsSOmPir:"
- "runDiagnoseIncludeDatabases:includeSysdiagnose:replyHandler:"
- "runDiagnoseWithLibraryURL:outputDirectoryURL:includeDatabases:includeSysdiagnose:replyHandler:"
- "v32@0:8B16B20@?24"
- "v32@0:8B16B20@?<v@?B@\"NSURL\"@\"NSError\">24"
- "v48@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSSecurityScopedURLWrapper\"24B32B36@?<v@?B@\"NSURL\"@\"NSError\">40"
- "v48@0:8@16@24B32B36@?40"

```
