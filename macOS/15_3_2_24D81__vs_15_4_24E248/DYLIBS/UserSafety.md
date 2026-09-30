## UserSafety

> `/System/Library/PrivateFrameworks/UserSafety.framework/Versions/A/UserSafety`

```diff

-88.1.0.0.0
-  __TEXT.__text: 0x4074
+91.14.0.0.0
+  __TEXT.__text: 0x4058
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_methlist: 0x2d0
   __TEXT.__const: 0x78

   __TEXT.__cstring: 0x2a2
   __TEXT.__oslogstring: 0x229
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_classname: 0x80
   __TEXT.__objc_methname: 0xb0a
   __TEXT.__objc_methtype: 0x1c9

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2256B573-0DB4-3CD8-BD84-5BB66B744D82
-  Functions: 105
-  Symbols:   299
+  UUID: 6ADAAB03-6C4C-3A16-8538-ADF2C7B82DCA
+  Functions: 107
+  Symbols:   301
   CStrings:  167
 
Symbols:
+ +[USLog clientUI].cold.1
+ +[USLog client].cold.1
Functions:
~ -[USMediaAnalysisService init] : 260 -> 256
~ -[USMediaAnalysisService isSensitiveImage:completionHandler:] : 588 -> 584
~ -[USMediaAnalysisService isSensitiveCGImage:withOrientation:completionHandler:] : 576 -> 572
~ -[USMediaAnalysisService isSensitiveVideoFile:useBlastdoor:progressHandler:completionHandler:] : 768 -> 760
~ -[USMediaAnalysisService isSensitiveImageWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:] : 608 -> 604
~ -[USMediaAnalysisService isSensitiveVideoWithLocalIdentifier:fromPhotoLibraryWithURL:progressHandler:completionHandler:] : 760 -> 756
~ -[USMediaAnalysisService _newImageClassificationRequest] : 216 -> 212
~ -[USMediaAnalysisService _newVideoClassificationRequest] : 216 -> 212
~ +[USLog client] : 84 -> 68
~ +[USLog clientUI] : 84 -> 68
~ -[USMediaAnalysisService _processMADResults:requestID:error:request:].cold.1 : 152 -> 112
~ -[USMediaAnalysisService _processMADResults:requestID:error:request:].cold.3 : 112 -> 152
~ -[USMediaAnalysisService _processMADResults:requestID:error:videoRequest:].cold.1 : 152 -> 112
~ -[USMediaAnalysisService _processMADResults:requestID:error:videoRequest:].cold.3 : 112 -> 152

```
