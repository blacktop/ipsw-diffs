## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3404.80.4.11.3
-  __TEXT.__text: 0x1ac3f8
+3405.21.2.0.0
+  __TEXT.__text: 0x1ac9b8
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x1dbfc
+  __TEXT.__objc_methlist: 0x1dc9c
   __TEXT.__const: 0x458
   __TEXT.__dlopen_cstrs: 0x484
   __TEXT.__gcc_except_tab: 0x2adc
-  __TEXT.__cstring: 0x3d2cb
-  __TEXT.__oslogstring: 0x10ea8
+  __TEXT.__cstring: 0x3d4ba
+  __TEXT.__oslogstring: 0x10f3b
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x7d10
+  __TEXT.__unwind_info: 0x7d40
   __TEXT.__objc_classname: 0x4f0c
-  __TEXT.__objc_methname: 0x3b165
-  __TEXT.__objc_methtype: 0xaaf0
-  __TEXT.__objc_stubs: 0x247e0
+  __TEXT.__objc_methname: 0x3b3d8
+  __TEXT.__objc_methtype: 0xab16
+  __TEXT.__objc_stubs: 0x248c0
   __DATA_CONST.__got: 0x1648
-  __DATA_CONST.__const: 0x8438
+  __DATA_CONST.__const: 0x8448
   __DATA_CONST.__objc_classlist: 0xdd8
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc328
+  __DATA_CONST.__objc_selrefs: 0xc380
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xdf0
   __DATA_CONST.__objc_arraydata: 0x2090
   __AUTH_CONST.__auth_got: 0xab8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3a60
-  __AUTH_CONST.__cfstring: 0x27080
-  __AUTH_CONST.__objc_const: 0x33638
+  __AUTH_CONST.__const: 0x3a80
+  __AUTH_CONST.__cfstring: 0x27180
+  __AUTH_CONST.__objc_const: 0x33750
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x7918
   __AUTH.__data: 0x2b0
-  __DATA.__objc_ivar: 0x255c
+  __DATA.__objc_ivar: 0x2574
   __DATA.__data: 0x4178
   __DATA.__bss: 0x1330
   __DATA.__common: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11758
-  Symbols:   14043
-  CStrings:  19242
+  Functions: 11772
+  Symbols:   14058
+  CStrings:  19275
 
Symbols:
+ _AFSystemAssistantExperienceAvailabilityDidChangeNotificationName
CStrings:
+ "%@ {spIdAudioProcessedDuration = %@, spIdUnknownUserScore = %@, spIdKnownUserScores = %@, spIdUserScoresVersion = %@, spIdScoreThresholdingType = %@, spIdAssetVersion = %@, userClassified = %@, userIdentityClassification = %@, lowScoreThreshold = %@, highScoreThreshold = %@, confidentScoreThreshold = %@, deltaScoreThreshold = %@, hasSufficientAudioProcessed = %@}"
+ "%s #posting AFSystemAssistantExperienceAvailabilityDidChangeNotificationName"
+ "%s Error in getLoggableIdentiferForUserWithSharedUserID:%@"
+ "%s idle timer speechRecognitionDidFinishWithError called with error %@"
+ "-[AFDictationConnectionServiceDelegate speechRecognitionDidFinishWithError:]"
+ "-[AFMultiUserConnection getLoggableIdentiferForUserWithSharedUserID:iCloudAltDSID:sessionID:completion:]"
+ "-[AFMultiUserConnection getLoggableIdentiferForUserWithSharedUserID:iCloudAltDSID:sessionID:completion:]_block_invoke_2"
+ "-[AFSystemAssistantExperienceStatusManager fetchGenerativeModelsAvailability]_block_invoke"
+ "@120@0:8@16@24@32@40@48@56@64q72@80@88@96@104q112"
+ "AFVoiceIdScoreCard::hasSufficientAudioProcessed"
+ "Has ATV in the home"
+ "Has HomePod(s) in the home"
+ "R\x11a\x19\x15\x11\x12\x14#"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_updateQueue"
+ "T@\"NSString\",C,N,V_userProfilePersonaId"
+ "TB,N,V_userProfileHeadphoneConnected"
+ "Tq,N,V_userProfileConfidence"
+ "Tq,R,N,V_hasSufficientAudioProcessed"
+ "_hasSufficientAudioProcessed"
+ "_updateQueue"
+ "_userProfileConfidence"
+ "_userProfileHeadphoneConnected"
+ "_userProfilePersonaId"
+ "com.apple.siri.availability.notification"
+ "com.apple.siri.systemAssistantExperienceStatusManagerQueue"
+ "deviceHasAtvInHome"
+ "deviceHasHomePodInHome"
+ "getHasSufficientAudioProcessed"
+ "getLoggableIdentiferForUserWithSharedUserID:iCloudAltDSID:sessionID:completion:"
+ "hasSufficientAudioProcessed"
+ "initWithSpIdAudioProcessedDuration:spIdUnknownUserScore:spIdKnownUserScores:spIdUserScoresVersion:spIdScoreThresholdingType:spIdAssetVersion:userClassified:userIdentityClassification:lowScoreThreshold:highScoreThreshold:confidentScoreThreshold:deltaScoreThreshold:hasSufficientAudioProcessed:"
+ "setHasSufficientAudioProcessed:"
+ "setUserProfileConfidence:"
+ "setUserProfileHeadphoneConnected:"
+ "setUserProfilePersonaId:"
+ "updateQueue"
+ "userProfileConfidence"
+ "userProfileHeadphoneConnected"
+ "userProfilePersonaId"
+ "{_mutationFlags=\"isDirty\"b1\"hasSpIdAudioProcessedDuration\"b1\"hasSpIdUnknownUserScore\"b1\"hasSpIdKnownUserScores\"b1\"hasSpIdUserScoresVersion\"b1\"hasSpIdScoreThresholdingType\"b1\"hasSpIdAssetVersion\"b1\"hasUserClassified\"b1\"hasUserIdentityClassification\"b1\"hasLowScoreThreshold\"b1\"hasHighScoreThreshold\"b1\"hasConfidentScoreThreshold\"b1\"hasDeltaScoreThreshold\"b1\"hasHasSufficientAudioProcessed\"b1}"
- "%@ {spIdAudioProcessedDuration = %@, spIdUnknownUserScore = %@, spIdKnownUserScores = %@, spIdUserScoresVersion = %@, spIdScoreThresholdingType = %@, spIdAssetVersion = %@, userClassified = %@, userIdentityClassification = %@, lowScoreThreshold = %@, highScoreThreshold = %@, confidentScoreThreshold = %@, deltaScoreThreshold = %@}"
- "%s Error in getLoggableIdentiferForUserWithiCloudAltDSID:%@"
- "-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]"
- "-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke_2"
- "@112@0:8@16@24@32@40@48@56@64q72@80@88@96@104"
- "R\x11a\x19\x15\x11\x12\x14\""
- "getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:"
- "hints"
- "initWithSpIdAudioProcessedDuration:spIdUnknownUserScore:spIdKnownUserScores:spIdUserScoresVersion:spIdScoreThresholdingType:spIdAssetVersion:userClassified:userIdentityClassification:lowScoreThreshold:highScoreThreshold:confidentScoreThreshold:deltaScoreThreshold:"
- "isHintsEnabled"
- "{_mutationFlags=\"isDirty\"b1\"hasSpIdAudioProcessedDuration\"b1\"hasSpIdUnknownUserScore\"b1\"hasSpIdKnownUserScores\"b1\"hasSpIdUserScoresVersion\"b1\"hasSpIdScoreThresholdingType\"b1\"hasSpIdAssetVersion\"b1\"hasUserClassified\"b1\"hasUserIdentityClassification\"b1\"hasLowScoreThreshold\"b1\"hasHighScoreThreshold\"b1\"hasConfidentScoreThreshold\"b1\"hasDeltaScoreThreshold\"b1}"

```
