## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1349.0.0.0.0
-  __TEXT.__text: 0x4872c
+1355.0.0.0.0
+  __TEXT.__text: 0x48754
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_methlist: 0x3de4
   __TEXT.__gcc_except_tab: 0x1850
-  __TEXT.__const: 0x288
-  __TEXT.__cstring: 0x6386
+  __TEXT.__const: 0x290
+  __TEXT.__cstring: 0x63d4
   __TEXT.__oslogstring: 0x29e3
   __TEXT.__ustring: 0x22
   __TEXT.__unwind_info: 0x1988
   __TEXT.__objc_classname: 0x82d
-  __TEXT.__objc_methname: 0xbe4a
-  __TEXT.__objc_methtype: 0x1551
+  __TEXT.__objc_methname: 0xbe71
+  __TEXT.__objc_methtype: 0x155a
   __TEXT.__objc_stubs: 0x9040
   __DATA_CONST.__got: 0x690
   __DATA_CONST.__const: 0x1d48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9091A630-7256-3C0A-8853-F6999FEF394D
+  UUID: 65081651-5A8D-305D-9B10-E73E01852FBE
   Functions: 1900
-  Symbols:   6626
+  Symbols:   6627
   CStrings:  3472
 
Symbols:
+ +[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:]
+ +[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:].cold.1
+ -[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]
+ -[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:].cold.1
+ -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]
+ -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:].cold.1
+ ___122+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:]_block_invoke
+ ___122+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:]_block_invoke.cold.1
+ ___127-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]_block_invoke
+ ___127-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]_block_invoke.103
+ ___127-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]_block_invoke.cold.1
+ ___143-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]_block_invoke
+ ___143-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]_block_invoke.108
+ ___143-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]_block_invoke.cold.1
+ ___143-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]_block_invoke.cold.2
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e49_v40?0q8"AVURLAsset"16"NSString"24"NSString"32ls32l8s72l8s40l8s48l8s56l8s64l8
+ _kRCAssetWriterFragmentInterval
+ _objc_msgSend$_determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:
+ _objc_msgSend$_importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:
+ _objc_msgSend$_importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:
- +[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]
- +[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:].cold.1
- -[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]
- -[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:].cold.1
- -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]
- -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:].cold.1
- ___109+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]_block_invoke
- ___109+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]_block_invoke.cold.1
- ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke
- ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.103
- ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.cold.1
- ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke
- ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.108
- ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.cold.1
- ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.cold.2
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e49_v40?0q8"AVURLAsset"16"NSString"24"NSString"32ls32l8s72l8s40l8s48l8s56l8s64l8
- _objc_msgSend$_determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:
- _objc_msgSend$_importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:
- _objc_msgSend$_importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:
Functions:
~ +[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:] -> +[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:] : 628 -> 636
~ +[RCSavedRecordingsModel determineImportabilityOfRecordingWithAudioURL:completionHandler:] : 412 -> 416
~ -[RCSavedRecordingsModel importRecordingWithSourceAudioURL:name:date:xpcConnection:userInfo:completionHandler:] : 792 -> 816
~ -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:] -> -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:] : 1676 -> 1660
~ ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.103 -> ___127-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]_block_invoke.103 : 340 -> 348
~ -[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:] -> -[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:] : 1152 -> 1164
CStrings:
+ "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:]"
+ "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:]_block_invoke"
+ "-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]"
+ "-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:]_block_invoke"
+ "-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]"
+ "-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:]_block_invoke"
+ "_determineImportabilityOfRecordingWithAudioAsset:preferredFormat:forceRewrite:completionHandler:"
+ "_importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:forceRewrite:completionHandler:"
+ "_importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:forceRewrite:completionHandler:"
+ "v40@0:8@16I24B28@?32"
+ "v64@0:8@16@24@32@40I48B52@?56"
+ "v76@0:8@16@24@32@40@48@56B64@?68"
- "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]"
- "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]_block_invoke"
- "-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]"
- "-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke"
- "-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]"
- "-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke"
- "_determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:"
- "_importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:"
- "_importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:"
- "v36@0:8@16I24@?28"
- "v60@0:8@16@24@32@40I48@?52"
- "v72@0:8@16@24@32@40@48@56@?64"

```
