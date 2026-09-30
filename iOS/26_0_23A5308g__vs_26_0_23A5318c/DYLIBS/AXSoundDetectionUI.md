## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-494.0.0.0.0
-  __TEXT.__text: 0x54eb4
-  __TEXT.__auth_stubs: 0x1240
+495.0.0.0.0
+  __TEXT.__text: 0x55910
+  __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_methlist: 0x274c
   __TEXT.__const: 0x990
   __TEXT.__gcc_except_tab: 0x408
-  __TEXT.__oslogstring: 0x6004
-  __TEXT.__cstring: 0x1cf7
+  __TEXT.__oslogstring: 0x6174
+  __TEXT.__cstring: 0x1d67
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x79a
   __TEXT.__swift5_capture: 0x2ec
   __TEXT.__constg_swiftt: 0x82c
-  __TEXT.__swift5_reflstr: 0x2e1
-  __TEXT.__swift5_fieldmd: 0x330
+  __TEXT.__swift5_reflstr: 0x311
+  __TEXT.__swift5_fieldmd: 0x348
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x12c8
+  __TEXT.__unwind_info: 0x12e0
   __TEXT.__eh_frame: 0x908
   __TEXT.__objc_classname: 0x482
-  __TEXT.__objc_methname: 0x52dd
+  __TEXT.__objc_methname: 0x52e2
   __TEXT.__objc_methtype: 0xe36
   __TEXT.__objc_stubs: 0x4900
-  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__got: 0x698
   __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1720
+  __DATA_CONST.__objc_selrefs: 0x1728
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x930
-  __AUTH_CONST.__const: 0x10f8
-  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__const: 0x1118
+  __AUTH_CONST.__cfstring: 0x1160
   __AUTH_CONST.__objc_const: 0x3918
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0x15b8
   __AUTH.__data: 0x300
   __DATA.__objc_ivar: 0x1c8
-  __DATA.__data: 0xad8
+  __DATA.__data: 0xaf8
   __DATA.__bss: 0x930
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8ED867DB-6AED-3ACC-ADCD-8183204B313A
-  Functions: 1759
-  Symbols:   3767
-  CStrings:  1935
+  UUID: FE6924F6-6D58-3E3C-B677-3B5540DC3A7A
+  Functions: 1770
+  Symbols:   3778
+  CStrings:  1942
 
Symbols:
+ _AXDeviceSupportsNameRecognition
+ _AXLogTemp
+ _AXSDSettingsURL
+ _AXSDSoundDetectionSendKShotModelFailedWithEmptySoundEmbeddingsNotification
+ _AXSDSoundDetectionSendKShotModelFailedWithEmptySoundEmbeddingsNotification.cold.1
+ ___AXSDSoundDetectionSendKShotModelFailedWithEmptySoundEmbeddingsNotification_block_invoke
+ ___AXSDSoundDetectionSendKShotModelFailedWithEmptySoundEmbeddingsNotification_block_invoke.cold.1
+ ____SoundDetectionSendNotification_block_invoke.188
+ ____SoundDetectionSendNotification_block_invoke.188.cold.1
+ ___block_literal_global.133
+ ___block_literal_global.39
+ ___block_literal_global.44
+ ___block_literal_global.49
- ____SoundDetectionSendNotification_block_invoke.180
- ____SoundDetectionSendNotification_block_invoke.180.cold.1
- ___block_literal_global.128
- ___block_literal_global.34
- ___block_literal_global.45
- ___block_literal_global.50
CStrings:
+ "ModelFailedDueToEmptyEmbeddings"
+ "Requesting send notification for failed training of detector: %@ with reason: empty sound embeddings."
+ "Requesting send notification for failed training of detector: %@ with reason: unknown error."
+ "[%s]: empty training sound embeddings in detector: %@ - error: %s"
+ "[%s]: handle ML error with detector: %@ with reason: %@."
+ "[%s]: handle ML result with detector: %@ - model URL: %s - error: %s"
+ "[%s]: marking detector as failed. recorded sounds are too different from one another to produce a valid model."
+ "code"
+ "settings-navigation://com.apple.Settings.Accessibility/SOUND_AND_NAME_RECOGNITION_TITLE/SOUND_RECOGNITION/Sounds"
+ "settings-navigation://com.apple.Settings.Accessibility/SOUND_RECOGNITION_TITLE/Sounds"
- "Requesting send notification for detector: %@"
- "[%s]: handle ML error with detector: %@."
- "[%s]: handle ML result with detector: %@ - model URL: %s"
- "com.apple.accessibility.kshot.model.complete"
- "prefs:root=ACCESSIBILITY&path=SOUND_RECOGNITION_TITLE/Sounds/"

```
