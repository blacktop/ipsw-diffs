## libAXSpeechManager.dylib

> `/usr/lib/libAXSpeechManager.dylib`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x24 sha256:4c09ff9eb27967ad451adb3c3829b24da706589e0b9cd572db51fe591494cb56
-  __TEXT.__auth_stubs: 0x40 sha256:3dd6bfdf2c67434483c091d56945465ad61e93a1ed261d8ff5db4cd15cfe2857
-  __TEXT.__unwind_info: 0x58 sha256:a9cb2d760c47a42e33f969b8a66d1908b1fbbdf9d54f480eff79d9b22f968ef0
-  __TEXT.__objc_classname: 0x11 sha256:c2b0bbddfb29c21bed6416e3989d68a83c219ac73d011957d7fa4bbd7a7bab04
-  __DATA_CONST.__objc_classlist: 0x8 sha256:9130cbc448c44c012efbfc2849582618c2d9d1d7fe328f6e299a05b3a7f0ee19
+3229.1.6.0.0
+  __TEXT.__text: 0x24 sha256:eab1ea9a29f0224c616b9890c4986b14e075da5feac6f0cadd9885a295768c19
+  __TEXT.__unwind_info: 0x58 sha256:c7a7990dcd232da94cb1c1398f51898f0f50a5c37d5f91b7dd5d9b90fe70b548
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __DATA_CONST.__objc_classlist: 0x8 sha256:115ac0b6a3a20a7222ae4ad79e1e0bf4993651ee00f891a683601248cfff1087
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __AUTH_CONST.__auth_got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
-  __AUTH_CONST.__objc_const: 0x90 sha256:fc2777d8b8782ad90cdf1aa726e608bf37daba5fbafe2c4978cde2410197f1a1
-  __DATA_DIRTY.__objc_data: 0x50 sha256:215c7db896bf37995fd0bf0824c219c016942c2f45e2eb5946ef8e8375b0ed64
+  __AUTH_CONST.__objc_const: 0x90 sha256:903f06ddc777fdb0083e500dd8391bab1570813e37a0bacc253222ef7882b779
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA_DIRTY.__objc_data: 0x50 sha256:4b55a19e4cf41b321a9180adc7d8624f51182698362e2eb6e88af8eba3e181a6
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
~ _isSpeakableEmojiString -> _AXSpeechLanguageCanonicalFormToGeneralLanguage : sha256 cd8d6b9db7e629c6a49eb03680269c6e811177df304739c9d3fae9e8d07f7dc2 -> b1e1d8af89b8c06ac8306663171e1e3f0a243210fdd79691f5074498dea316df
CStrings:
- "AXEmojiUtilities"

```
