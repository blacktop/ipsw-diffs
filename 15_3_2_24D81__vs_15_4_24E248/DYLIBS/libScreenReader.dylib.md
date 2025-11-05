## libScreenReader.dylib

> `/usr/lib/libScreenReader.dylib`

```diff

-964.9.2.0.0
-  __TEXT.__text: 0x42a0
+964.12.7.1.0
+  __TEXT.__text: 0x4284
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x68
   __TEXT.__cstring: 0xe2e
   __TEXT.__dlopen_cstrs: 0x132
   __TEXT.__dof_ScreenRea: 0x22e
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x158
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x158
   __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x78

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7273815F-4FD1-35FC-A4D0-933819CB5664
+  UUID: 6E1E68C5-7CB8-3BBA-BD97-33D97256C393
   Functions: 79
   Symbols:   274
   CStrings:  246
Functions:
~ __ScreenReaderSetEnabledInPreferences : 652 -> 648
~ __ScreenReaderSendCommand : 132 -> 120
~ __ScreenReaderSendCommandWithServerPort : 348 -> 356
~ __ScreenReaderCopyInfo : 148 -> 144
~ __ScreenReaderCopyAudioIntroPath : 1084 -> 1088
~ __createTempFileURL : 176 -> 184
~ __createAndOpenAudioFile : 280 -> 268
~ __speechDoneCallback : 368 -> 372
~ __populateResultWithData : 764 -> 768
~ ___ScreenReaderGetEFIAudioFileData_block_invoke.75 : 464 -> 460
~ __setCommandList : 264 -> 260
~ __ScreenReaderCopyPerformedCommand : 364 -> 360
~ __ScreenReaderIsInRecoveryMode : 188 -> 176
~ _getAXFIsRunningAsRootOrInRootSessionSymbolLoc : 204 -> 200
~ _getUAVoiceOverSetEnabledSymbolLoc : 240 -> 236
~ __SCRSendCommand : 312 -> 308
~ __SCRCopyInfo : 652 -> 656
~ __SCRGetPerformedCommand : 652 -> 656
~ __SCRStartupSynchronous : 392 -> 396

```
