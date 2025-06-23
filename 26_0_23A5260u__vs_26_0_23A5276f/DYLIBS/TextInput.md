## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3504.100.0.0.0
-  __TEXT.__text: 0x7ce98
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0xb1a8
+3508.0.0.0.0
+  __TEXT.__text: 0x7d740
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0xb210
   __TEXT.__dlopen_cstrs: 0x4b9
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x47285
+  __TEXT.__cstring: 0x472a7
   __TEXT.__ustring: 0xb05e8
   __TEXT.__oslogstring: 0x8c9
-  __TEXT.__unwind_info: 0x1e10
+  __TEXT.__unwind_info: 0x1e30
   __TEXT.__objc_classname: 0x1569
-  __TEXT.__objc_methname: 0x191fb
-  __TEXT.__objc_methtype: 0x3609
-  __TEXT.__objc_stubs: 0xce40
+  __TEXT.__objc_methname: 0x193d3
+  __TEXT.__objc_methtype: 0x362c
+  __TEXT.__objc_stubs: 0xcf60
   __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x22f8
+  __DATA_CONST.__const: 0x2320
   __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5460
+  __DATA_CONST.__objc_selrefs: 0x54c8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x3f8
-  __DATA_CONST.__objc_arraydata: 0xd5db8
-  __AUTH_CONST.__auth_got: 0x798
+  __DATA_CONST.__objc_arraydata: 0xd5de8
+  __AUTH_CONST.__auth_got: 0x7a8
   __AUTH_CONST.__const: 0xd40
-  __AUTH_CONST.__cfstring: 0x217a20
+  __AUTH_CONST.__cfstring: 0x217a60
   __AUTH_CONST.__objc_const: 0x116d8
-  __AUTH_CONST.__objc_arrayobj: 0x4080
+  __AUTH_CONST.__objc_arrayobj: 0x40c8
   __AUTH_CONST.__objc_dictobj: 0xc990
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_doubleobj: 0xc0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0BC3BB6D-88D8-3AA5-B836-75A2A7E7458F
-  Functions: 3883
-  Symbols:   12962
-  CStrings:  99756
+  UUID: 10154663-7D5E-3094-92AF-FCD42DA0EFCD
+  Functions: 3893
+  Symbols:   12994
+  CStrings:  99775
 
Symbols:
+ +[NSString(TIExtras) _stringFromCharacterSet:]
+ -[NSString(TIExtras) _isLowercaseStringWithLocale:]
+ -[TIAutocorrectionList listBySettingNewAlternateCorrections:]
+ -[TIAutocorrectionList listBySettingNewAutocorrection:]
+ -[TIAutocorrectionList listBySettingNewEmojiList:]
+ -[TIAutocorrectionList listBySettingNewPredictions:]
+ -[TIPreferencesController setValue:forManagedPreferenceKey:asyncWithCompletion:]
+ -[TIPreferencesController setValue:forPreferenceKey:asyncIfManaged:]
+ _InputAnalyticsLibraryCore.12532
+ _InputAnalyticsLibraryCore.frameworkLibrary.12539
+ _SecurityLibrary.12834
+ _SecurityLibraryCore.frameworkLibrary.12845
+ ___68-[TIPreferencesController setValue:forPreferenceKey:asyncIfManaged:]_block_invoke
+ ___68-[TIPreferencesController setValue:forPreferenceKey:asyncIfManaged:]_block_invoke_2
+ ___Block_byref_object_copy_.11524
+ ___Block_byref_object_copy_.13038
+ ___Block_byref_object_copy_.1973
+ ___Block_byref_object_copy_.254
+ ___Block_byref_object_copy_.3010
+ ___Block_byref_object_copy_.7130
+ ___Block_byref_object_copy_.959
+ ___Block_byref_object_dispose_.11525
+ ___Block_byref_object_dispose_.13039
+ ___Block_byref_object_dispose_.1974
+ ___Block_byref_object_dispose_.255
+ ___Block_byref_object_dispose_.3011
+ ___Block_byref_object_dispose_.7131
+ ___Block_byref_object_dispose_.960
+ ___InputAnalyticsLibraryCore_block_invoke.12540
+ ___SecurityLibraryCore_block_invoke.12846
+ ___block_descriptor_48_8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1063
+ ___block_literal_global.1127
+ ___block_literal_global.12203
+ ___block_literal_global.12481
+ ___block_literal_global.12544
+ ___block_literal_global.12787
+ ___block_literal_global.13334
+ ___block_literal_global.13797
+ ___block_literal_global.1993
+ ___block_literal_global.22.12828
+ ___block_literal_global.24.5067
+ ___block_literal_global.2467
+ ___block_literal_global.2665
+ ___block_literal_global.276
+ ___block_literal_global.314
+ ___block_literal_global.346
+ ___block_literal_global.392
+ ___block_literal_global.4.4977
+ ___block_literal_global.4.8667
+ ___block_literal_global.4155
+ ___block_literal_global.4443
+ ___block_literal_global.4975
+ ___block_literal_global.5069
+ ___block_literal_global.5581
+ ___block_literal_global.6059
+ ___block_literal_global.6884
+ ___block_literal_global.7.8670
+ ___block_literal_global.7.9056
+ ___block_literal_global.702
+ ___block_literal_global.7193
+ ___block_literal_global.75.1100
+ ___block_literal_global.7644
+ ___block_literal_global.7795
+ ___block_literal_global.8085
+ ___block_literal_global.813
+ ___block_literal_global.829
+ ___block_literal_global.838
+ ___block_literal_global.85.2453
+ ___block_literal_global.854
+ ___block_literal_global.8644
+ ___block_literal_global.8663
+ ___block_literal_global.889
+ ___block_literal_global.9024
+ ___block_literal_global.9052
+ ___block_literal_global.908
+ ___block_literal_global.9628
+ ___block_literal_global.9787
+ ___block_literal_global.9969
+ ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.12840
+ ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.12836
+ _audit_stringInputAnalytics.12542
+ _audit_stringSecurity.12848
+ _generateIdentifier.count.9881
+ _getSecTaskCopySigningIdentifierSymbolLoc.ptr.12839
+ _getSecTaskCreateFromSelfSymbolLoc.ptr.12835
+ _objc_msgSend$emojiList
+ _objc_msgSend$listWithCorrections:predictions:emojiList:inlineCompletionList:proactiveTriggers:
+ _objc_msgSend$setAutoCorrectionAllowed:completion:
+ _objc_msgSend$setContinuousPathKeyboardAllowed:completion:
+ _objc_msgSend$setPredictiveKeyboardAllowed:completion:
+ _objc_msgSend$setSmartPunctuationAllowed:completion:
+ _objc_msgSend$setSpellCheckAllowed:completion:
+ _objc_msgSend$setValue:forManagedPreferenceKey:asyncWithCompletion:
+ _objc_msgSend$setValue:forPreferenceKey:asyncIfManaged:
+ _sharedInstance.instance.13335
+ _sharedInstance.instance.8645
+ _sharedInstance.onceToken.13333
+ _sharedInstance.onceToken.7794
+ _sharedInstance.onceToken.8643
+ _sharedPreferencesController.once.769
+ _sharedPreferencesController.once.806
+ _sharedPreferencesController.sharedController.770
+ _sharedPreferencesController.sharedController.807
+ _uset_getItem
+ _uset_getItemCount
- _InputAnalyticsLibraryCore.12514
- _InputAnalyticsLibraryCore.frameworkLibrary.12521
- _SecurityLibrary.12816
- _SecurityLibraryCore.frameworkLibrary.12827
- ___Block_byref_object_copy_.11507
- ___Block_byref_object_copy_.13022
- ___Block_byref_object_copy_.1974
- ___Block_byref_object_copy_.257
- ___Block_byref_object_copy_.3009
- ___Block_byref_object_copy_.7110
- ___Block_byref_object_copy_.932
- ___Block_byref_object_dispose_.11508
- ___Block_byref_object_dispose_.13023
- ___Block_byref_object_dispose_.1975
- ___Block_byref_object_dispose_.258
- ___Block_byref_object_dispose_.3010
- ___Block_byref_object_dispose_.7111
- ___Block_byref_object_dispose_.933
- ___InputAnalyticsLibraryCore_block_invoke.12522
- ___SecurityLibraryCore_block_invoke.12828
- ___block_descriptor_48_8_32bs40w_e17_v16?0"NSError"8ls32l8w40l8
- ___block_literal_global.1045
- ___block_literal_global.1121
- ___block_literal_global.12185
- ___block_literal_global.12463
- ___block_literal_global.12526
- ___block_literal_global.12769
- ___block_literal_global.13318
- ___block_literal_global.13779
- ___block_literal_global.1992
- ___block_literal_global.22.12810
- ___block_literal_global.24.5054
- ___block_literal_global.2469
- ___block_literal_global.2666
- ___block_literal_global.279
- ___block_literal_global.311
- ___block_literal_global.343
- ___block_literal_global.389
- ___block_literal_global.4.4964
- ___block_literal_global.4.8646
- ___block_literal_global.4141
- ___block_literal_global.4433
- ___block_literal_global.4962
- ___block_literal_global.5056
- ___block_literal_global.5568
- ___block_literal_global.6045
- ___block_literal_global.682
- ___block_literal_global.6869
- ___block_literal_global.7.8649
- ___block_literal_global.7.9035
- ___block_literal_global.7173
- ___block_literal_global.75.1082
- ___block_literal_global.7626
- ___block_literal_global.7777
- ___block_literal_global.792
- ___block_literal_global.8065
- ___block_literal_global.814
- ___block_literal_global.823
- ___block_literal_global.839
- ___block_literal_global.85.2455
- ___block_literal_global.8623
- ___block_literal_global.8642
- ___block_literal_global.874
- ___block_literal_global.880
- ___block_literal_global.9003
- ___block_literal_global.9031
- ___block_literal_global.9609
- ___block_literal_global.9777
- ___block_literal_global.9959
- ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.12822
- ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.12818
- _audit_stringInputAnalytics.12524
- _audit_stringSecurity.12830
- _generateIdentifier.count.9871
- _getSecTaskCopySigningIdentifierSymbolLoc.ptr.12821
- _getSecTaskCreateFromSelfSymbolLoc.ptr.12817
- _sharedInstance.instance.13319
- _sharedInstance.instance.8624
- _sharedInstance.onceToken.13317
- _sharedInstance.onceToken.7776
- _sharedInstance.onceToken.8622
- _sharedPreferencesController.once.754
- _sharedPreferencesController.once.791
- _sharedPreferencesController.sharedController.755
- _sharedPreferencesController.sharedController.792
CStrings:
+ "@24@0:8^{USet=}16"
+ "QWERTY-Maori"
+ "Zhuyin-Grid-Extended"
+ "_isLowercaseStringWithLocale:"
+ "_stringFromCharacterSet:"
+ "listBySettingNewAlternateCorrections:"
+ "listBySettingNewAutocorrection:"
+ "listBySettingNewEmojiList:"
+ "listBySettingNewPredictions:"
+ "setAutoCorrectionAllowed:completion:"
+ "setContinuousPathKeyboardAllowed:completion:"
+ "setPredictiveKeyboardAllowed:completion:"
+ "setSmartPunctuationAllowed:completion:"
+ "setSpellCheckAllowed:completion:"
+ "setValue:forManagedPreferenceKey:asyncWithCompletion:"
+ "setValue:forPreferenceKey:asyncIfManaged:"
+ "v36@0:8@16@24B32"

```
