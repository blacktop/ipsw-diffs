## com.apple.CharacterPicker.FileService

> `/System/Library/PrivateFrameworks/CharacterPicker.framework/Versions/A/XPCServices/com.apple.CharacterPicker.FileService.xpc/Contents/MacOS/com.apple.CharacterPicker.FileService`

```diff

-249.228.200.0.0
-  __TEXT.__text: 0x5bb0
+249.308.200.0.0
+  __TEXT.__text: 0x5bc0
   __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x1340
-  __TEXT.__objc_methlist: 0x21c
+  __TEXT.__objc_methlist: 0x3e4
   __TEXT.__const: 0x39
-  __TEXT.__cstring: 0x852
+  __TEXT.__cstring: 0x84a
   __TEXT.__objc_methname: 0x1044
   __TEXT.__objc_classname: 0x4b
   __TEXT.__objc_methtype: 0x26c
-  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__unwind_info: 0x1f8
   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x10

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x710
-  __DATA.__objc_selrefs: 0x598
+  __DATA.__objc_const: 0x3c0
+  __DATA.__objc_selrefs: 0x648
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x140

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: FEE1A920-72B4-3063-BD61-A86361C92C33
-  Functions: 124
-  Symbols:   1120
-  CStrings:  516
+  UUID: 90151F61-D563-3668-9D07-39C21D56C8EB
+  Functions: 132
+  Symbols:   1156
+  CStrings:  514
 
Symbols:
+ +[CPCharacterDatabase sharedDatabase].cold.1
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPCharacterDatabase.o
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPFileService.o
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPKStandardCharacterEntity.o
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPUtilities.o
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmojiPicker/
+ /AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/EmojiPicker/FileService/
+ EmojiPickerSignpostLog.cold.1
+ IsWorkingInCharacterViewer.cold.1
+ IsWorkingInEmojiDFRIM.cold.1
+ LogCurrentTimeWithType.cold.1
+ SetGetKeyedGlobalParam.cold.1
+ SharedEmojiPreference.cold.1
+ ShouldDrawPreReleaseStamp.cold.1
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPCharacterDatabase.o
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPFileService.o
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPKStandardCharacterEntity.o
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/CPUtilities.o
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Binaries/EmojiPicker/install/TempContent/Objects/EmojiPicker.build/FileService.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmojiPicker/
- /AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/EmojiPicker/FileService/
Functions:
~ ___fileservice_event_handler_block_invoke : 1760 -> 1804
~ _SetGetKeyedGlobalParam : 396 -> 380
~ _SharedEmojiPreference : 120 -> 108
~ _SetGetDirtySharedEmojiPreference : 28 -> 24
~ _CharacterInfoFromEntityID : 872 -> 880
~ _StringFromUnicodeCodeString : 956 -> 960
~ _ImageForCouple : 1108 -> 1064
~ _FontForCharacterFittingInRect : 636 -> 620
~ _GetCategoryDataForLanguage : 228 -> 224
~ _IsWorkingInCharacterViewer : 68 -> 56
~ _IsWorkingInEmojiDFRIM : 68 -> 56
~ _LogCurrentTimeWithType : 444 -> 428
~ _ShouldDrawPreReleaseStamp : 156 -> 140
~ _DrawPreReleaseStampInRect : 628 -> 616
~ _EmojiPickerSignpostLog : 68 -> 56
~ -[CPKStandardCharacterEntity displayFont] : 88 -> 92
~ +[CPCharacterDatabase sharedDatabase] : 68 -> 56
~ -[CPCharacterDatabase createXPCArrayForSearchString:maxCount:] : 1808 -> 1788
~ -[CPCharacterDatabase createXPCArrayForRelatedCharacters:maxCount:] : 712 -> 716
CStrings:
- "add"
- "set"

```
