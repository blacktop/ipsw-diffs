## SpeakTypingServices

> `/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0xeb8
-  __TEXT.__auth_stubs: 0x1c0
+3191.19.0.0.0
+  __TEXT.__text: 0xf9c
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x29c
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0xc8

   __DATA_CONST.__objc_selrefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x260

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43D759D7-FFA0-3D10-996E-CA764EC38443
+  UUID: 562F38D0-4801-3F25-97CA-331F00A05899
   Functions: 27
-  Symbols:   150
+  Symbols:   146
   CStrings:  128
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x24
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ +[SpeakTypingServices sharedInstance] : 68 -> 84
~ -[SpeakTypingServices dealloc] : 92 -> 96
~ -[SpeakTypingServices speakTypingClient] : 68 -> 72
~ -[SpeakTypingServices clearLastSpokenString] : 120 -> 128
~ -[SpeakTypingServices setVoiceIdentifier:forLanguage:] : 228 -> 232
~ -[SpeakTypingServices lastUsedVoiceIdentifier] : 124 -> 136
~ -[SpeakTypingServices lastSpokenString] : 124 -> 136
~ -[SpeakTypingServices verifyTestingConnection] : 120 -> 132
~ -[SpeakTypingServices setWordFeedbackEnabled:] : 240 -> 256
~ -[SpeakTypingServices setPhoneticFeedbackEnabled:] : 240 -> 256
~ -[SpeakTypingServices setLetterFeedbackEnabled:] : 240 -> 256
~ -[SpeakTypingServices notifySpeakServicesToStopSpeaking] : 72 -> 76
~ -[SpeakTypingServices notifySpeakServicesToStopSpeakingAutocorrections] : 72 -> 76
~ -[SpeakTypingServices notifySpeakServicesForAttributedSpeechOutput:] : 240 -> 252
~ -[SpeakTypingServices notifySpeakServicesForSpeechOutput:volume:speakingRate:] : 324 -> 336
~ -[SpeakTypingServices notifySpeakServicesForSpeakAutoCorrections:forCurrentInputMode:] : 268 -> 264
~ -[SpeakTypingServices notifySpeakServicesToFeedbackQuickTypePrediction:forCurrentInputMode:] : 264 -> 268
~ -[SpeakTypingServices _clientIdentifier] : 152 -> 164
~ -[SpeakTypingServices initializeServerConnection] : 172 -> 176
~ ___81-[SpeakTypingServices connectionWithServiceWasInterruptedForUserInterfaceClient:]_block_invoke : 176 -> 184
~ -[SpeakTypingServices setSpeakTypingClient:] : 12 -> 64

```
