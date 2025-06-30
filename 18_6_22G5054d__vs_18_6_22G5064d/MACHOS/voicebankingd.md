## voicebankingd

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd`

```diff

-641.1.19.0.0
-  __TEXT.__text: 0x1b5c0
-  __TEXT.__auth_stubs: 0xf50
+641.1.20.0.0
+  __TEXT.__text: 0x1cd68
+  __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_methlist: 0x3d8
-  __TEXT.__swift5_typeref: 0x564
-  __TEXT.__objc_methname: 0xa83
-  __TEXT.__oslogstring: 0x140f
-  __TEXT.__const: 0x540
-  __TEXT.__cstring: 0x13ff
+  __TEXT.__swift5_typeref: 0x596
+  __TEXT.__objc_methname: 0xafd
+  __TEXT.__oslogstring: 0x16df
+  __TEXT.__const: 0x560
+  __TEXT.__cstring: 0x14bf
   __TEXT.__constg_swiftt: 0x200
   __TEXT.__swift5_reflstr: 0x33f
   __TEXT.__swift5_fieldmd: 0x204
   __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_capture: 0x738
+  __TEXT.__swift5_capture: 0x790
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x24
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methtype: 0x1cc
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x518
-  __TEXT.__eh_frame: 0x328
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x2c8
+  __TEXT.__unwind_info: 0x570
+  __TEXT.__eh_frame: 0x3e8
+  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x270
-  __DATA_CONST.__const: 0x17b0
+  __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA.__objc_const: 0x7e0
-  __DATA.__objc_selrefs: 0x338
+  __DATA.__objc_selrefs: 0x360
   __DATA.__objc_data: 0x360
-  __DATA.__data: 0x680
+  __DATA.__data: 0x690
   __DATA.__bss: 0x408
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport
   - /usr/lib/libAccessibility.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1C79371F-BF75-356B-AB4B-AA6BC690E850
-  Functions: 567
-  Symbols:   429
-  CStrings:  351
+  UUID: 106483D7-EA1C-3BA5-B40A-7780289AC9CF
+  Functions: 594
+  Symbols:   433
+  CStrings:  367
 
Symbols:
+ _$s31TextToSpeechVoiceBankingSupport010TTSVBVoiceE7ManagerC39updateMissingCloudAudioFilesIfNecessary10completionyys6ResultOyAA13TTSVBResultOKOAA10TTSVBErrorVGYbc_tF
+ _$s31TextToSpeechVoiceBankingSupport010TTSVBVoiceE7ManagerC45synchronizeAudioFileBackedFuturesForAllVoices10completionyys6ResultOyAA13TTSVBResultOKOAA10TTSVBErrorVGYbc_tF
+ _$s31TextToSpeechVoiceBankingSupport8TTSVBLogV6common2os6LoggerVvgZ
+ _OBJC_CLASS_$_BGSystemTaskScheduler
CStrings:
+ "Error synchronizing audio file-backed sample futures: %s"
+ "Successfully finished synchronizing audio file-backed sample futures"
+ "Wake event received: [BGSystemTask] UpdateMissingCloudAudioFilesIfNecessary state=%s"
+ "com.apple.voicebanking.systemtask.ResolveCloudDatabaseAudioFileMismatch"
+ "com.apple.voicebanking.systemtask.UpdateMissingCloudAudioFilesIfNecessary"
+ "identifier"
+ "performUpdateMissingCloudAudioFilesIfNecessary: Did update missing cloud audio files if neccesary."
+ "performUpdateMissingCloudAudioFilesIfNecessary: Failed to update cloud audio files %@."
+ "performUpdateMissingCloudAudioFilesIfNecessary: Marking bg task complete. ID=%s"
+ "performUpdateMissingCloudAudioFilesIfNecessary: Will perform cloud audio file mismatch bg task. ID=%s"
+ "performUpdateMissingCloudAudioFilesIfNecessary: bg task expired. ID=%s"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setExpirationHandler:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "v16@?0@\"BGSystemTask\"8"

```
