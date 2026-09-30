## PhotosUIPrivate

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate`

```diff

-842.0.102.0.0
-  __TEXT.__text: 0x5cd414
+850.0.100.0.0
+  __TEXT.__text: 0x5cd3e0
   __TEXT.__auth_stubs: 0xa020
   __TEXT.__objc_methlist: 0x55754
   __TEXT.__const: 0x17248

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D8110B8B-0CA4-31F3-83F1-3F4354249BA5
+  UUID: AB93D92B-CE2C-38AC-AE27-8C68EDC67EF5
   Functions: 41231
   Symbols:   105789
   CStrings:  52573
Symbols:
+ _objc_msgSend$createPurgeableOutboundSharingSubDirectoriesIfNeededWithPath:error:
+ _objc_msgSend$outboundSharingTmpURL
+ _objc_msgSend$tmpVideoTranscodeFilePathWithExtension:locateInPhotoLibraryBundle:
- _objc_msgSend$createDirectoryIfNeededAtPath:error:
- _objc_msgSend$privateDirectoryWithSubType:createIfNeeded:error:
- _objc_msgSend$tmpFileForVideoTranscodeToPhotoDataDirectory:withExtension:
Functions:
~ -[PUActivityItemSource _copyResourceAtURL:toURL:shouldMove:] : 892 -> 896
~ -[PUActivityItemSource _outboundResourcesDirectoryURL] : 184 -> 136
~ -[PUCleanupToolController _showFeedbackThumbs] : 104 -> 96
CStrings:
+ "createPurgeableOutboundSharingSubDirectoriesIfNeededWithPath:error:"
+ "outboundSharingTmpURL"
+ "tmpVideoTranscodeFilePathWithExtension:locateInPhotoLibraryBundle:"
- "createDirectoryIfNeededAtPath:error:"
- "privateDirectoryWithSubType:createIfNeeded:error:"
- "tmpFileForVideoTranscodeToPhotoDataDirectory:withExtension:"

```
