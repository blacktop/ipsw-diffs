## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-603.0.0.0.0
+605.0.0.0.0
   __TEXT.__text: 0x44ffc
   __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_methlist: 0x261c

   __TEXT.__dlopen_cstrs: 0x480
   __TEXT.__unwind_info: 0x10ec
   __TEXT.__objc_classname: 0x4fa
-  __TEXT.__objc_methname: 0x98bc
+  __TEXT.__objc_methname: 0x98d2
   __TEXT.__objc_methtype: 0xfd1
   __TEXT.__objc_stubs: 0x65a0
   __DATA_CONST.__got: 0x178

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3880
   __DATA_CONST.__objc_selrefs: 0x1d48
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__cfstring: 0x4fc0
   __AUTH_CONST.__const: 0x80

   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x4a0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x280
-  __DATA.__objc_superrefs: 0xf0
   __DATA.__objc_ivar: 0x3a8
   __DATA.__data: 0x4e0
   __DATA.__common: 0x4
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x100
   __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0xfb0
   __DATA_DIRTY.__objc_data: 0xbe0
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   Functions: 1373
   Symbols:   4820
-  CStrings:  2804
+  CStrings:  2805
 
Symbols:
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.729
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.729.cold.1
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.731
+ ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.311
+ ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.311.cold.1
+ ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.313
+ ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.313.cold.1
+ ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.859
+ ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.732
+ ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.732.cold.1
+ ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.315
+ ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.315.cold.1
+ ___block_literal_global.757
+ ___block_literal_global.768
+ ___block_literal_global.817
+ ___block_literal_global.861
+ __unnamed_array_storage.770
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.728
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.728.cold.1
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.730
- ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.310
- ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.310.cold.1
- ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.312
- ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.312.cold.1
- ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.858
- ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.731
- ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.731.cold.1
- ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.314
- ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.314.cold.1
- ___block_literal_global.756
- ___block_literal_global.767
- ___block_literal_global.816
- ___block_literal_global.860
- __unnamed_array_storage.769
CStrings:
+ "T@\"NSString\",?,R,C"

```
