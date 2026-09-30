## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-639.0.0.0.0
-  __TEXT.__text: 0x49074
+651.0.0.0.0
+  __TEXT.__text: 0x49590
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x2d40
+  __TEXT.__objc_methlist: 0x2d60
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x1698
-  __TEXT.__cstring: 0x5be6
+  __TEXT.__gcc_except_tab: 0x16e8
+  __TEXT.__cstring: 0x5c85
   __TEXT.__oslogstring: 0xd18a
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x534
   __TEXT.__unwind_info: 0x1240
   __TEXT.__objc_classname: 0x595
-  __TEXT.__objc_methname: 0xa8a4
+  __TEXT.__objc_methname: 0xa90d
   __TEXT.__objc_methtype: 0x10fc
-  __TEXT.__objc_stubs: 0x6ea0
+  __TEXT.__objc_stubs: 0x6ee0
   __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x18e0
+  __DATA_CONST.__const: 0x1910
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2058
+  __DATA_CONST.__objc_selrefs: 0x2070
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__objc_const: 0x4d40
+  __AUTH_CONST.__cfstring: 0x5aa0
+  __AUTH_CONST.__objc_const: 0x4d50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 749C8556-9839-3674-932E-A0F29C18EE49
-  Functions: 1388
-  Symbols:   5257
-  CStrings:  3765
+  UUID: 34C587C8-E995-3274-905E-072C8A98383A
+  Functions: 1392
+  Symbols:   5251
+  CStrings:  3781
 
Symbols:
+ -[TLCapabilitiesManager supportsReflectionRemixes]
+ -[TLToneManager _importTone:metadata:completionBlock:]
+ -[TLToneManager _systemEmbeddedEncoreRemixSoundDirectory]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table134
+ GCC_except_table140
+ GCC_except_table159
+ GCC_except_table173
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table76
+ _TLToneImportErrorDomain
+ ___121+[TLVibrationManager _handleVibrationPreferencesDidChangeNotificationForPreferencesKinds:atInitiativeOfVibrationManager:]_block_invoke.247
+ ___32-[TLToneManager _removeAllTones]_block_invoke.298
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.775
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.775.cold.1
+ ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.777
+ ___54-[TLToneManager _importTone:metadata:completionBlock:]_block_invoke
+ ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.288
+ ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.288.cold.1
+ ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.324
+ ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.324.cold.1
+ ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.326
+ ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.326.cold.1
+ ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.976
+ ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.977
+ ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.778
+ ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.778.cold.1
+ ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.285
+ ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.285.cold.1
+ ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.328
+ ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.328.cold.1
+ ___block_descriptor_40_e8_32bs_e42_v24?0"TLToneImportResponse"8"NSError"16ls32l8
+ ___block_literal_global.249
+ ___block_literal_global.866
+ ___block_literal_global.880
+ ___block_literal_global.934
+ _objc_msgSend$_importTone:metadata:completionBlock:
+ _objc_msgSend$supportsReflectionRemixes
- GCC_except_table104
- GCC_except_table106
- GCC_except_table109
- GCC_except_table112
- GCC_except_table116
- GCC_except_table118
- GCC_except_table131
- GCC_except_table137
- GCC_except_table156
- GCC_except_table170
- GCC_except_table176
- GCC_except_table180
- GCC_except_table59
- GCC_except_table70
- GCC_except_table99
- ___121+[TLVibrationManager _handleVibrationPreferencesDidChangeNotificationForPreferencesKinds:atInitiativeOfVibrationManager:]_block_invoke.244
- ___32-[TLToneManager _removeAllTones]_block_invoke.292
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.768
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.768.cold.1
- ___44-[TLToneManager _tonePreferencesFromService]_block_invoke.770
- ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.282
- ___60-[TLToneManager _removeToneWithIdentifier:orSyncIdentifier:]_block_invoke.282.cold.1
- ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.321
- ___73-[TLVibrationManager _retrieveUserGeneratedVibrationPatternsUsingService]_block_invoke.321.cold.1
- ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.323
- ___75-[TLVibrationManager _setUserGeneratedVibrationPatternsUsingService:error:]_block_invoke.323.cold.1
- ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.962
- ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.963
- ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.771
- ___78-[TLToneManager _setToneIdentifierUsingService:keyedByTopic:forPreferenceKey:]_block_invoke.771.cold.1
- ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.279
- ___82-[TLToneManager _addToneEntries:toManifestAtPath:mediaDirectory:shouldSkipReload:]_block_invoke.279.cold.1
- ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.325
- ___84-[TLVibrationManager _removeAllUserGeneratedVibrationPatternsUsingServiceWithError:]_block_invoke.325.cold.1
- ___block_literal_global.246
- ___block_literal_global.860
- ___block_literal_global.871
- ___block_literal_global.920
CStrings:
+ "-EncoreRemix"
+ "EncoreRemix"
+ "Solarium"
+ "SwiftUI"
+ "TL-EncoreRemix"
+ "TLToneImportErrorDomain"
+ "Unexpected failure to import tone."
+ "_importTone:metadata:completionBlock:"
+ "_systemEmbeddedEncoreRemixSoundDirectory"
+ "supportsReflectionRemixes"
+ "v24@?0@\"TLToneImportResponse\"8@\"NSError\"16"

```
