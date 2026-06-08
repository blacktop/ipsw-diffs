## IMTransferServices

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices`

```diff

-1121.600.1.0.0
-  __TEXT.__text: 0x4ff0
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x16c
+1132.100.1.0.0
+  __TEXT.__text: 0x4ff8
+  __TEXT.__objc_methlist: 0x178
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x6bc
-  __TEXT.__cstring: 0x4c4
+  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__cstring: 0x4cc
   __TEXT.__oslogstring: 0x83c
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x99c
-  __TEXT.__objc_methtype: 0x1f2
-  __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x1c0
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x148
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24EA1A47-A7E0-3FCB-8039-E4566EB99947
-  Functions: 56
-  Symbols:   82
-  CStrings:  199
+  UUID: A7748244-7B52-3B54-8864-D6CA2B6505B2
+  Functions: 57
+  Symbols:   80
+  CStrings:  122
 
Symbols:
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "senderExemptFromLDM"
- "@\"NSMutableDictionary\""
- "@16@0:8"
- "@?24@0:8@16"
- "IMTransferServicesCompressionController"
- "IMTransferServicesController"
- "Transcoding"
- "URLByDeletingLastPathComponent"
- "UTF8String"
- "_blockForCopier:"
- "_blockMap"
- "_mapCopier:toBlock:"
- "_randomTemporaryPathWithSuffix:"
- "_receiveFileTransfer:topic:path:requestURLString:ownerID:sourceAppID:signature:decryptionKey:retries:fileSize:progressBlock:completionBlock:"
- "_sendFilePath:topic:userInfo:transferID:sourceAppID:encryptFile:retries:progressBlock:completionBlock:"
- "_unmapCopier:"
- "cStringUsingEncoding:"
- "cancelSendTransferID:"
- "compressFileTransfer:completionBlock:"
- "copy"
- "copyItemAtPath:toPath:error:"
- "copyItemAtURL:toURL:error:"
- "count"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "defaultManager"
- "deleteAllPersonalNicknamesWithCompletion:"
- "didErrorOccur"
- "errorWithDomain:code:userInfo:"
- "fileCopierDidFinish:"
- "fileCopierDidStart:"
- "fileExistsAtPath:isDirectory:"
- "fileURLWithPath:"
- "getNicknameWithRecordID:decryptionKey:completionBlock:"
- "getNicknameWithRecordID:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:avatarRecipeDataTag:isKnownSender:shouldDecodeImageFields:completionBlock:"
- "getNicknameWithRecordID:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:completionBlock:"
- "getNicknameWithRecordID:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:isKnownSender:completionBlock:"
- "getNicknameWithRecordID:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:isKnownSender:shouldDecodeImageFields:completionBlock:"
- "identifier"
- "initWithInputURL:outputURL:identifier:operation:delegate:"
- "inputURL"
- "isEqualToString:"
- "objectForKey:"
- "outputURL"
- "pathExtension"
- "preWarmMMCSForOwnerID:"
- "receiveFileTransfer:topic:path:requestURLString:ownerID:signature:decryptionKey:fileSize:progressBlock:completionBlock:"
- "receiveFileTransfer:topic:path:requestURLString:ownerID:sourceAppID:signature:decryptionKey:fileSize:progressBlock:completionBlock:"
- "removeItemAtURL:error:"
- "removeObjectForKey:"
- "sendFilePath:topic:transferID:encryptFile:progressBlock:completionBlock:"
- "sendFilePath:topic:userInfo:transferID:encryptFile:progressBlock:completionBlock:"
- "sendFilePath:topic:userInfo:transferID:sourceAppID:encryptFile:progressBlock:completionBlock:"
- "setObject:forKey:"
- "setPersonalNickname:oldRecordID:completionBlock:"
- "setPersonalNickname:oldRecordID:completionBlockWithWallpaperAndRecipeDataTags:"
- "setPersonalNickname:oldRecordID:completionBlockWithWallpaperTags:"
- "sharedInstance"
- "start"
- "stringByAppendingPathExtension:"
- "stringByDeletingPathExtension"
- "stringGUID"
- "updateUltraConstrainedAttachments:"
- "v104@0:8@16@24@32@40@48@56@64@72Q80@?88@?96"
- "v108@0:8@16@24@32@40@48@56@64@72i80Q84@?92@?100"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v60@0:8@16@24@32B40@?44@?52"
- "v64@0:8@16@24@32@40@48@?56"
- "v68@0:8@16@24@32@40@48B56@?60"
- "v68@0:8@16@24@32@40B48@?52@?60"
- "v72@0:8@16@24@32@40@48B56B60@?64"
- "v76@0:8@16@24@32@40@48B56@?60@?68"
- "v80@0:8@16@24@32@40@48@56B64B68@?72"
- "v80@0:8@16@24@32@40@48B56i60@?64@?72"
- "v96@0:8@16@24@32@40@48@56@64Q72@?80@?88"

```
