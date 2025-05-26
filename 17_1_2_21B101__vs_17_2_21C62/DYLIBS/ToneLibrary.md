## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-596.0.0.0.0
-  __TEXT.__text: 0x44fbc
+601.0.0.0.0
+  __TEXT.__text: 0x44ffc
   __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_methlist: 0x261c
-  __TEXT.__const: 0x110
+  __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x1098
-  __TEXT.__cstring: 0x5297
+  __TEXT.__cstring: 0x52e2
   __TEXT.__oslogstring: 0xc3b9
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x480

   __DATA_CONST.__objc_const: 0x3880
   __DATA_CONST.__objc_selrefs: 0x1d48
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0x4f80
+  __AUTH_CONST.__cfstring: 0x4fc0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 1373
   Symbols:   4820
-  CStrings:  2802
+  CStrings:  2804
 
Symbols:
+ ___32-[TLToneManager _removeAllTones]_block_invoke.253
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.728
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.728.cold.1
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.730
+ ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.243
+ ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.243.cold.1
+ ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.310
+ ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.310.cold.1
+ ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.312
+ ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.312.cold.1
+ ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.858
+ ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.731
+ ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.731.cold.1
+ ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.240
+ ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.240.cold.1
+ ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.314
+ ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.314.cold.1
+ ___block_literal_global.756
+ ___block_literal_global.767
+ ___block_literal_global.816
+ ___block_literal_global.860
+ __unnamed_array_storage.657
+ __unnamed_array_storage.769
- ___32-[TLToneManager _removeAllTones]_block_invoke.250
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.725
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.725.cold.1
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.727
- ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.240
- ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.240.cold.1
- ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.307
- ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.307.cold.1
- ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.309
- ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.309.cold.1
- ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.855
- ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.728
- ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.728.cold.1
- ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.237
- ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.237.cold.1
- ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.311
- ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.311.cold.1
- ___block_literal_global.753
- ___block_literal_global.764
- ___block_literal_global.813
- ___block_literal_global.857
- __unnamed_array_storage.654
- __unnamed_array_storage.766
CStrings:
+ "SystemAppNotificationVibrationIdentifier"
+ "app-notification-sound-identifier"

```
