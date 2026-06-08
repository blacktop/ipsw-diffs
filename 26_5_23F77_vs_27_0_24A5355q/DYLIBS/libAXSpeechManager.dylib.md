## libAXSpeechManager.dylib

> `/usr/lib/libAXSpeechManager.dylib`

```diff

-3191.35.0.0.0
+3229.1.6.0.0
   __TEXT.__text: 0x24
-  __TEXT.__auth_stubs: 0x40
   __TEXT.__unwind_info: 0x58
-  __TEXT.__objc_classname: 0x11
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x20
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EDC80B1F-AE46-3F93-9494-557BB491FF61
+  UUID: FDBA7285-8181-35F1-99C7-9B2C919E79FC
   Functions: 5
   Symbols:   17
-  CStrings:  1
+  CStrings:  0
 
Functions:
~ _AXSpeechTransformText -> _isSpeakableEmojiString : 12 -> 4
~ _AXSpeechTransformTextWithLanguageAndVoiceIdentifier -> _AXSpeechTransformText : 4 -> 12
~ _AXSpeechTransformTextWithLanguage -> _AXSpeechTransformTextWithLanguageAndVoiceIdentifier : 12 -> 4
~ _AXSpeechLanguageCanonicalFormToGeneralLanguage -> _AXSpeechTransformTextWithLanguage : 4 -> 12
CStrings:
- "AXEmojiUtilities"

```
