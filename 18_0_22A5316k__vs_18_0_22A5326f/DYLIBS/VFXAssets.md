## VFXAssets

> `/System/Library/PrivateFrameworks/VFXAssets.framework/VFXAssets`

```diff

   __TEXT.__eh_frame: 0x168
   __TEXT.__objc_methname: 0xb2
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
   __AUTH_CONST.__auth_got: 0x230

   - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 116
-  Symbols:   131
-  CStrings:  0
+  Symbols:   139
+  CStrings:  79
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "ACLASS_$_SXSubscriptionButtonComponent"
+ "_OBJC_CLASS_$_SXComponentScrollPosition"
+ "_OBJC_CLASS_$_SXFullscreenCanvasViewController"
+ "_OBJC_CLASS_$_WCComplicationManager"
+ "_OBJC_CLASS_$_WCContentIndex"
+ "_OBJC_CLASS_$_WCDProtoUserInfoTransfer"
+ "_OBJC_CLASS_$_WCDataMessageRecord"
+ "_OBJC_CLASS_$_WCDictionaryMessageRecord"
+ "_OBJC_CLASS_$_WCMessageRecord"
+ "_OBJC_CLASS_$_WCPrivateXPCManager"
+ "_OBJC_CLASS_$_WCSessionFile"
+ "_OBJC_CLASS_$_WCUserInfo"
+ "_OBJC_CLASS_$_WCXPCManager"
+ "_OBJC_METACLASS_$_SXWebContentComponent"
+ "_OBJC_METACLASS_$_WCComplicationManager"
+ "_OBJC_METACLASS_$_WCContentIndex"
+ "_OBJC_METACLASS_$_WCDProtoUserInfoTransfer"
+ "_OBJC_METACLASS_$_WCDataMessageRecord"
+ "_OBJC_METACLASS_$_WCDictionaryMessageRecord"
+ "_OBJC_METACLASS_$_WCMessage"
+ "_OBJC_METACLASS_$_WCMessageRecord"
+ "_OBJC_METACLASS_$_WCMessageRequest"
+ "_OBJC_METACLASS_$_WCMessageResponse"
+ "_OBJC_METACLASS_$_WCPrivateXPCManager"
+ "_OBJC_METACLASS_$_WCSessionFile"
+ "_OBJC_METACLASS_$_WCSessionFileTransfer"
+ "_OBJC_METACLASS_$_WCSessionState"
+ "_OBJC_METACLASS_$_WCSessionUserInfoTransfer"
+ "_OBJC_METACLASS_$_WCUserInfo"
+ "_OBJC_METACLASS_$_WCXPCManager"
+ "_SLHomographCopyTune"
+ "_SLHomographGetPOS"
+ "_SLHomographGetPhonemes"
+ "_SLHomographGetTags"
+ "_SLTokenCountHomographs"
+ "_SLTokenCreateTemp"
+ "_SLTokenGetClass"
+ "_SLTokenGetHomograph"
+ "_SLTokenGetInfo"
+ "_SLTokenGetText"
+ "_SLTokenGetTupleGroup"
+ "_SLTokenRelease"
+ "__Z15SLFirstPOSInSetj"
+ "__Z27SLGetSpeechDictionaryBundlev"
+ "__ZN10SLMMapHintD2Ev"
+ "__ZN11SLMMapCache3MapEPK7__CFURLP10SLMMapHint"
+ "__ZN11SLMMapCache5UnmapEPv"
+ "__ZN12SLDictLookup20CreatePhonemeSymbolsEPK10__CFLocale"
+ "__ZN12SLDictLookup6CreateEPK10__CFLocale"
+ "__ZN12SLDictionaryC2Ev"
+ "__ZN12SLDictionaryD2Ev"
+ "__ZN12SLPronouncer6CreateEPK10__CFLocalePK12SLDictLookup"
+ "__ZN12SLWordTagSet5eraseEt"
+ "__ZN13SLWordBuilderC1Ev"
+ "__ZN13SLWordBuilderD1Ev"
+ "__ZN14SLEncyclopedia6LookupEPKcmP13SLWordBuilderP12SLDictionary"
+ "__ZN14SLEncyclopedia6RemoveEP12SLDictionary"
+ "__ZN14SLEncyclopedia8PushBackEP12SLDictionary"
+ "__ZN14SLEncyclopediaD1Ev"
+ "__ZN16SLCFArrayBuilder11CreateArrayEv"
+ "__ZN16SLCFArrayBuilderD1Ev"
+ "__ZN16SLCFArrayBuilderD2Ev"
+ "__ZN20SLCFStringTextSource6RefillERPtS1_PKt"
+ "__ZN20SLCFStringTextSourceC1EPK10__CFString"
+ "__ZN20SLCFStringTextSourceC2EPK10__CFString"
+ "__ZN20SLCFStringTextSourceD1Ev"
+ "__ZN20SLCFStringTextSourceD2Ev"
+ "__ZN21SLCFDictionaryBuilder16CreateDictionaryEv"
+ "__ZN21SLCFDictionaryBuilder9push_backEPKvS1_"
+ "__ZN5SLTag4NameEt"
+ "__ZN7SLLexer6CreateEP12SLTextSourceP12SLDictLookupP12SLPronouncerPK10__CFLocalej"
+ "__ZN8SLBndEng4NameEh"
+ "__ZN8SLTagEng4NameEt"
+ "__ZN9SLPhonEng5sExt1E"
+ "__ZN9SLPhonEng5sExt2E"
+ "__ZNK12SLDictLookup6LookupEP12SLDictionaryPKcmP7SLTokenb"
+ "__ZNK12SLWordTagSet4findEt"
+ "__ZpLR12SLWordTagSetRKS_"
+ "serInfoTransfer"

```
