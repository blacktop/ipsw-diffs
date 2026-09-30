## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3532.4.3.0.0
-  __TEXT.__text: 0x85c38
+3532.4.5.0.0
+  __TEXT.__text: 0x86110
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0xb3e8
+  __TEXT.__objc_methlist: 0xb448
   __TEXT.__dlopen_cstrs: 0x4b9
   __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0x48099
+  __TEXT.__cstring: 0x480b8
   __TEXT.__ustring: 0xc7e48
   __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x2370
-  __TEXT.__objc_classname: 0x15a3
-  __TEXT.__objc_methname: 0x199fb
-  __TEXT.__objc_methtype: 0x372d
-  __TEXT.__objc_stubs: 0xd1c0
+  __TEXT.__unwind_info: 0x2390
+  __TEXT.__objc_classname: 0x15a5
+  __TEXT.__objc_methname: 0x19b8c
+  __TEXT.__objc_methtype: 0x37ae
+  __TEXT.__objc_stubs: 0xd200
   __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0x2408
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55c0
+  __DATA_CONST.__objc_selrefs: 0x55e8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xf60f8
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0xd60
-  __AUTH_CONST.__cfstring: 0x24d7c0
-  __AUTH_CONST.__objc_const: 0x11930
+  __AUTH_CONST.__cfstring: 0x24d7e0
+  __AUTH_CONST.__objc_const: 0x11970
   __AUTH_CONST.__objc_arrayobj: 0x43e0
   __AUTH_CONST.__objc_dictobj: 0xccb0
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH.__objc_data: 0x25d0
-  __DATA.__objc_ivar: 0xb70
+  __DATA.__objc_ivar: 0xb74
   __DATA.__data: 0xc30
-  __DATA.__bss: 0x768
+  __DATA.__bss: 0x770
   __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__bss: 0x2c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 13DE756C-7CBD-3192-9178-BD223E632A65
-  Functions: 3960
-  Symbols:   13185
-  CStrings:  107071
+  UUID: FC03F67A-FB65-31F0-AA23-2F57061F8E54
+  Functions: 3969
+  Symbols:   13207
+  CStrings:  107086
 
Symbols:
+ +[TICandidateRequestToken tokenForKeyboardState:preferredIdentifier:]
+ +[TIKeyboardTouchEvent touchEventWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:UUID:]
+ +[TIKeyboardTouchEvent touchEventWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:UUID:]
+ +[TIKeyboardTouchEvent touchEventWithStage:location:radius:timestamp:pathIndex:forcedKeyCode:UUID:]
+ -[TICandidateRequestToken identifier]
+ -[TICandidateRequestToken initForKeyboardState:preferredIdentifier:]
+ -[TIKeyboardTouchEvent .cxx_destruct]
+ -[TIKeyboardTouchEvent initWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:UUID:]
+ -[TIKeyboardTouchEvent touchUUID]
+ _InputAnalyticsLibraryCore.12646
+ _InputAnalyticsLibraryCore.frameworkLibrary.12653
+ _OBJC_IVAR_$_TIKeyboardTouchEvent._touchUUID
+ _SecurityLibrary.12953
+ _SecurityLibraryCore.frameworkLibrary.12964
+ ___Block_byref_object_copy_.11634
+ ___Block_byref_object_copy_.13156
+ ___Block_byref_object_copy_.2041
+ ___Block_byref_object_copy_.3030
+ ___Block_byref_object_copy_.7218
+ ___Block_byref_object_copy_.9095
+ ___Block_byref_object_copy_.999
+ ___Block_byref_object_dispose_.1000
+ ___Block_byref_object_dispose_.11635
+ ___Block_byref_object_dispose_.13157
+ ___Block_byref_object_dispose_.2042
+ ___Block_byref_object_dispose_.3031
+ ___Block_byref_object_dispose_.7219
+ ___Block_byref_object_dispose_.9096
+ ___InputAnalyticsLibraryCore_block_invoke.12654
+ ___SecurityLibraryCore_block_invoke.12965
+ ___block_literal_global.10085
+ ___block_literal_global.1093
+ ___block_literal_global.1160
+ ___block_literal_global.12318
+ ___block_literal_global.12595
+ ___block_literal_global.12658
+ ___block_literal_global.12906
+ ___block_literal_global.13450
+ ___block_literal_global.13911
+ ___block_literal_global.2057
+ ___block_literal_global.22.12947
+ ___block_literal_global.24.5087
+ ___block_literal_global.2486
+ ___block_literal_global.2681
+ ___block_literal_global.4.4997
+ ___block_literal_global.4.8795
+ ___block_literal_global.4165
+ ___block_literal_global.4172
+ ___block_literal_global.4461
+ ___block_literal_global.4995
+ ___block_literal_global.5089
+ ___block_literal_global.5134
+ ___block_literal_global.5609
+ ___block_literal_global.6090
+ ___block_literal_global.6958
+ ___block_literal_global.7.8798
+ ___block_literal_global.7.9189
+ ___block_literal_global.703
+ ___block_literal_global.7280
+ ___block_literal_global.75.1130
+ ___block_literal_global.7749
+ ___block_literal_global.7895
+ ___block_literal_global.818
+ ___block_literal_global.8199
+ ___block_literal_global.834
+ ___block_literal_global.843
+ ___block_literal_global.859
+ ___block_literal_global.8772
+ ___block_literal_global.8791
+ ___block_literal_global.895
+ ___block_literal_global.9161
+ ___block_literal_global.9185
+ ___block_literal_global.941
+ ___block_literal_global.9749
+ ___block_literal_global.9904
+ ___getMCFeatureEmojiKeyboardAllowedSymbolLoc_block_invoke
+ ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.12959
+ ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.12955
+ _audit_stringInputAnalytics.12656
+ _audit_stringSecurity.12967
+ _generateIdentifier.count.9996
+ _getMCFeatureEmojiKeyboardAllowed
+ _getMCFeatureEmojiKeyboardAllowedSymbolLoc.ptr
+ _getSecTaskCopySigningIdentifierSymbolLoc.ptr.12958
+ _getSecTaskCreateFromSelfSymbolLoc.ptr.12954
+ _objc_msgSend$initForKeyboardState:preferredIdentifier:
+ _objc_msgSend$initWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:UUID:
+ _objc_msgSend$touchEventWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:UUID:
+ _objc_msgSend$touchUUID
+ _sharedInstance.instance.13451
+ _sharedInstance.instance.8773
+ _sharedInstance.onceToken.13449
+ _sharedInstance.onceToken.7894
+ _sharedInstance.onceToken.8771
+ _sharedPreferencesController.once.774
+ _sharedPreferencesController.once.811
+ _sharedPreferencesController.sharedController.775
+ _sharedPreferencesController.sharedController.812
- -[TICandidateRequestToken initForKeyboardState:]
- -[TIKeyboardTouchEvent initWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:]
- _InputAnalyticsLibraryCore.12634
- _InputAnalyticsLibraryCore.frameworkLibrary.12641
- _SecurityLibrary.12941
- _SecurityLibraryCore.frameworkLibrary.12952
- ___Block_byref_object_copy_.11622
- ___Block_byref_object_copy_.13144
- ___Block_byref_object_copy_.2034
- ___Block_byref_object_copy_.3022
- ___Block_byref_object_copy_.7208
- ___Block_byref_object_copy_.9066
- ___Block_byref_object_copy_.993
- ___Block_byref_object_dispose_.11623
- ___Block_byref_object_dispose_.13145
- ___Block_byref_object_dispose_.2035
- ___Block_byref_object_dispose_.3023
- ___Block_byref_object_dispose_.7209
- ___Block_byref_object_dispose_.9067
- ___Block_byref_object_dispose_.994
- ___InputAnalyticsLibraryCore_block_invoke.12642
- ___SecurityLibraryCore_block_invoke.12953
- ___block_literal_global.10063
- ___block_literal_global.1087
- ___block_literal_global.1154
- ___block_literal_global.12306
- ___block_literal_global.12583
- ___block_literal_global.12646
- ___block_literal_global.12894
- ___block_literal_global.13438
- ___block_literal_global.13899
- ___block_literal_global.2050
- ___block_literal_global.22.12935
- ___block_literal_global.24.5078
- ___block_literal_global.2477
- ___block_literal_global.2672
- ___block_literal_global.4.4989
- ___block_literal_global.4.8765
- ___block_literal_global.4157
- ___block_literal_global.4164
- ___block_literal_global.4453
- ___block_literal_global.4987
- ___block_literal_global.5080
- ___block_literal_global.5125
- ___block_literal_global.5600
- ___block_literal_global.6081
- ___block_literal_global.6949
- ___block_literal_global.7.8768
- ___block_literal_global.7.9160
- ___block_literal_global.705
- ___block_literal_global.7270
- ___block_literal_global.75.1124
- ___block_literal_global.7740
- ___block_literal_global.7886
- ___block_literal_global.816
- ___block_literal_global.8190
- ___block_literal_global.837
- ___block_literal_global.846
- ___block_literal_global.862
- ___block_literal_global.8742
- ___block_literal_global.8761
- ___block_literal_global.897
- ___block_literal_global.9132
- ___block_literal_global.9156
- ___block_literal_global.935
- ___block_literal_global.9725
- ___block_literal_global.9883
- ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.12947
- ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.12943
- _audit_stringInputAnalytics.12644
- _audit_stringSecurity.12955
- _generateIdentifier.count.9975
- _getSecTaskCopySigningIdentifierSymbolLoc.ptr.12946
- _getSecTaskCreateFromSelfSymbolLoc.ptr.12942
- _objc_msgSend$initForKeyboardState:
- _objc_msgSend$initWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:
- _sharedInstance.instance.13439
- _sharedInstance.instance.8743
- _sharedInstance.onceToken.13437
- _sharedInstance.onceToken.7885
- _sharedInstance.onceToken.8741
- _sharedPreferencesController.once.777
- _sharedPreferencesController.once.814
- _sharedPreferencesController.sharedController.778
- _sharedPreferencesController.sharedController.815
CStrings:
+ "; UUID = %@"
+ "@76@0:8i16{CGPoint=dd}20d36d44q52q60@68"
+ "@80@0:8i16{CGPoint=dd}20d36d44q52i60q64@72"
+ "@84@0:8i16{CGPoint=dd}20d36d44q52i60q64i72@76"
+ "MCFeatureEmojiKeyboardAllowed"
+ "T@\"NSUUID\",R,C,N"
+ "T@\"NSUUID\",R,C,N,V_touchUUID"
+ "_touchUUID"
+ "initForKeyboardState:preferredIdentifier:"
+ "initWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:UUID:"
+ "tokenForKeyboardState:preferredIdentifier:"
+ "touchEventWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:UUID:"
+ "touchEventWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:UUID:"
+ "touchEventWithStage:location:radius:timestamp:pathIndex:forcedKeyCode:UUID:"
+ "touchUUID"
- "emojiKeyboardAllowed"
- "initForKeyboardState:"
- "initWithStage:location:radius:timestamp:pathIndex:fingerID:forcedKeyCode:continuousPathState:"

```
