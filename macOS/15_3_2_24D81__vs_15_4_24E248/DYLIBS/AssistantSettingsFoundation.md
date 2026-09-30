## AssistantSettingsFoundation

> `/System/Library/PrivateFrameworks/AssistantSettingsFoundation.framework/Versions/A/AssistantSettingsFoundation`

```diff

-3403.11.2.0.0
-  __TEXT.__text: 0x31b0
-  __TEXT.__auth_stubs: 0x1f0
+3404.71.4.0.0
+  __TEXT.__text: 0x3210
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_methlist: 0x2c8
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x55e

   __TEXT.__objc_methname: 0x864
   __TEXT.__objc_methtype: 0xf2
   __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0xf8
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x5e0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F19B1C8-C04F-3B09-B67D-6D3F1DD70926
+  UUID: A5218D87-B650-360B-8715-E01C1B7559FF
   Functions: 71
   Symbols:   242
   CStrings:  191
Functions:
~ -[ASFApplicationSupplier applicationForBundleId:] : 372 -> 388
~ -[ASFApplication initWithBundleId:localizedName:] : 268 -> 264
~ -[ASFApplication compareByName:] : 172 -> 188
~ -[ASFApplication isEqual:] : 492 -> 488
~ +[ASFAvailableSuggestionAppsController sharedController] : 436 -> 432
~ ___56+[ASFAvailableSuggestionAppsController sharedController]_block_invoke : 72 -> 80
~ -[ASFAvailableSuggestionAppsController init] : 140 -> 156
~ -[ASFAvailableSuggestionAppsController initWithApplicationSupplier:] : 220 -> 216
~ -[ASFAvailableSuggestionAppsController visibleApps] : 824 -> 848
~ -[ASFAvailableSuggestionAppsController __spotlightBundleIds] : 444 -> 468
~ ___60-[ASFAvailableSuggestionAppsController __spotlightBundleIds]_block_invoke : 172 -> 180
~ +[ASFController sharedController] : 436 -> 432
~ ___33+[ASFController sharedController]_block_invoke : 72 -> 80
~ -[ASFController init] : 248 -> 260
~ -[ASFController assistantIsEnabled] : 92 -> 96
~ -[ASFController setAssistantIsEnabled:] : 244 -> 240
~ -[ASFController hardwareButtonAssistantIsEnabled] : 52 -> 48
~ -[ASFController setHardwareButtonAssistant:] : 96 -> 84
~ -[ASFController typeToSiriIsEnabled] : 56 -> 52
~ -[ASFController setTypeToSiriEnabled:] : 72 -> 64
~ -[ASFController alwaysShowRecognizedSpeech] : 296 -> 300
~ -[ASFController setAlwaysShowRecognizedSpeech:] : 296 -> 300
~ -[ASFController siriResponseShouldAlwaysPrint] : 296 -> 300
~ -[ASFController setSiriResponseShouldAlwaysPrint:] : 296 -> 300
~ -[ASFController useDeviceSpeakerForTTS] : 292 -> 300
~ -[ASFController setUseDeviceSpeakerForTTS:] : 288 -> 296
~ -[ASFController setCallHangUpEnabled:] : 28 -> 24
~ -[ASFController setAnnounceNotificationEnabled:] : 28 -> 24
~ -[ASFController isSpokenNotificationSkipTriggerlessReplyConfirmationEnabled] : 296 -> 300
~ -[ASFController setSpokenNotificationSkipTriggerlessReplyConfirmationEnabled:] : 296 -> 300
~ -[ASFController setAnnounceNotificationEnabledForPlatform:annouceNotificationEnabled:] : 32 -> 28
~ -[ASFController getAllNotificationApps] : 324 -> 332
~ -[ASFController setAnnounceNotificationEnabledForApp:annouceNotificationEnabled:] : 96 -> 92
~ -[ASFController siriSuggestionClients] : 584 -> 568
~ -[ASFController isLearningEnabledForApp:] : 104 -> 100
~ _SGSiriCanLearnFromApp : 168 -> 172
~ -[ASFController setLearningForApp:enabled:] : 116 -> 108
~ _SGSetSiriCanLearnFromApp : 500 -> 512
~ -[ASFController isShowSuggestionsEnabledInApp:] : 104 -> 100
~ _SGAppCanShowSiriSuggestions : 92 -> 88
~ -[ASFController setShowSuggestionsInApp:enabled:] : 116 -> 108
~ _SGSetAppCanShowSiriSuggestions : 112 -> 104
~ _SGAppCanShowSiriSuggestions_iOSmacOS : 168 -> 172
~ _SGSetAppCanShowSiriSuggestions_iOSmacOS : 500 -> 512

```
