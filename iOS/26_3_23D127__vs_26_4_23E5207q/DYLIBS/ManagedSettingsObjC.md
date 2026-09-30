## ManagedSettingsObjC

> `/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC`

```diff

-266.80.2.0.0
-  __TEXT.__text: 0x2ac14
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x3e24
+267.100.11.0.0
+  __TEXT.__text: 0x2e100
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_methlist: 0x4104
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x570
-  __TEXT.__cstring: 0x1152
+  __TEXT.__gcc_except_tab: 0x578
+  __TEXT.__cstring: 0x1373
   __TEXT.__oslogstring: 0x1610
-  __TEXT.__unwind_info: 0xf88
+  __TEXT.__unwind_info: 0xf28
   __TEXT.__objc_classname: 0xd02
-  __TEXT.__objc_methname: 0x6ab2
-  __TEXT.__objc_methtype: 0x10ca
-  __TEXT.__objc_stubs: 0x2480
+  __TEXT.__objc_methname: 0x7258
+  __TEXT.__objc_methtype: 0x10cd
+  __TEXT.__objc_stubs: 0x24a0
   __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0xa30
+  __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17c0
+  __DATA_CONST.__objc_selrefs: 0x19b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1c80
-  __AUTH_CONST.__objc_const: 0x8650
+  __AUTH_CONST.__cfstring: 0x1f20
+  __AUTH_CONST.__objc_const: 0x8900
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0x658
+  __DATA.__bss: 0x798
   __DATA_DIRTY.__objc_data: 0x1ea0
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9147A080-AC11-3E72-86C3-85EF7B307D44
-  Functions: 1368
-  Symbols:   4793
-  CStrings:  1952
+  UUID: 371F44CE-D525-33B7-88CD-DC3D2665AAD7
+  Functions: 1457
+  Symbols:   5021
+  CStrings:  2059
 
Symbols:
+ +[MODeviceActivitySettingsGroup allowedDataClientsMetadata]
+ +[MOIntelligenceSettingsGroup allowedExternalIntelligenceWorkspaceIDsMetadata]
+ +[MOIntelligenceSettingsGroup denyAppleIntelligenceReportMetadata]
+ +[MOIntelligenceSettingsGroup denyExternalIntelligenceIntegrationsSignInMetadata]
+ +[MOIntelligenceSettingsGroup denyMailSmartRepliesMetadata]
+ +[MOIntelligenceSettingsGroup denyMailSummaryMetadata]
+ +[MOIntelligenceSettingsGroup denyNotesTranscriptionMetadata]
+ +[MOIntelligenceSettingsGroup denyNotesTranscriptionSummaryMetadata]
+ +[MOIntelligenceSettingsGroup denyPersonalizedHandwritingResultsMetadata]
+ +[MOIntelligenceSettingsGroup denySpotlightInternetResultsMetadata]
+ +[MOIntelligenceSettingsGroup denyVisualIntelligenceSummaryMetadata]
+ +[MOIntelligenceSettingsGroup forceOnDeviceOnlyDictationMetadata]
+ +[MOIntelligenceSettingsGroup forceOnDeviceOnlyTranslationMetadata]
+ +[MOKeyboardSettingsGroup denyAutoCorrectionMetadata]
+ +[MOKeyboardSettingsGroup denyContinuousPathKeyboardMetadata]
+ +[MOKeyboardSettingsGroup denyDefinitionLookupMetadata]
+ +[MOKeyboardSettingsGroup denyKeyboardShortcutsMetadata]
+ +[MOKeyboardSettingsGroup denyPredictiveKeyboardMetadata]
+ +[MOKeyboardSettingsGroup denySpellCheckMetadata]
+ +[MOSiriSettingsGroup denySiriWhileLockedMetadata]
+ -[MODeviceActivitySettingsGroup allowedDataClients]
+ -[MODeviceActivitySettingsGroup setAllowedDataClients:]
+ -[MOIntelligenceSettingsGroup allowedExternalIntelligenceWorkspaceIDs]
+ -[MOIntelligenceSettingsGroup denyAppleIntelligenceReport]
+ -[MOIntelligenceSettingsGroup denyExternalIntelligenceIntegrationsSignIn]
+ -[MOIntelligenceSettingsGroup denyMailSmartReplies]
+ -[MOIntelligenceSettingsGroup denyMailSummary]
+ -[MOIntelligenceSettingsGroup denyNotesTranscriptionSummary]
+ -[MOIntelligenceSettingsGroup denyNotesTranscription]
+ -[MOIntelligenceSettingsGroup denyPersonalizedHandwritingResults]
+ -[MOIntelligenceSettingsGroup denySpotlightInternetResults]
+ -[MOIntelligenceSettingsGroup denyVisualIntelligenceSummary]
+ -[MOIntelligenceSettingsGroup forceOnDeviceOnlyDictation]
+ -[MOIntelligenceSettingsGroup forceOnDeviceOnlyTranslation]
+ -[MOIntelligenceSettingsGroup setAllowedExternalIntelligenceWorkspaceIDs:]
+ -[MOIntelligenceSettingsGroup setDenyAppleIntelligenceReport:]
+ -[MOIntelligenceSettingsGroup setDenyExternalIntelligenceIntegrationsSignIn:]
+ -[MOIntelligenceSettingsGroup setDenyMailSmartReplies:]
+ -[MOIntelligenceSettingsGroup setDenyMailSummary:]
+ -[MOIntelligenceSettingsGroup setDenyNotesTranscription:]
+ -[MOIntelligenceSettingsGroup setDenyNotesTranscriptionSummary:]
+ -[MOIntelligenceSettingsGroup setDenyPersonalizedHandwritingResults:]
+ -[MOIntelligenceSettingsGroup setDenySpotlightInternetResults:]
+ -[MOIntelligenceSettingsGroup setDenyVisualIntelligenceSummary:]
+ -[MOIntelligenceSettingsGroup setForceOnDeviceOnlyDictation:]
+ -[MOIntelligenceSettingsGroup setForceOnDeviceOnlyTranslation:]
+ -[MOKeyboardSettingsGroup denyAutoCorrection]
+ -[MOKeyboardSettingsGroup denyContinuousPathKeyboard]
+ -[MOKeyboardSettingsGroup denyDefinitionLookup]
+ -[MOKeyboardSettingsGroup denyKeyboardShortcuts]
+ -[MOKeyboardSettingsGroup denyPredictiveKeyboard]
+ -[MOKeyboardSettingsGroup denySpellCheck]
+ -[MOKeyboardSettingsGroup setDenyAutoCorrection:]
+ -[MOKeyboardSettingsGroup setDenyContinuousPathKeyboard:]
+ -[MOKeyboardSettingsGroup setDenyDefinitionLookup:]
+ -[MOKeyboardSettingsGroup setDenyKeyboardShortcuts:]
+ -[MOKeyboardSettingsGroup setDenyPredictiveKeyboard:]
+ -[MOKeyboardSettingsGroup setDenySpellCheck:]
+ -[MOShieldConfiguration initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:secondaryButtonSubmenuItems:]
+ -[MOShieldConfiguration secondaryButtonSubmenuItems]
+ -[MOSiriSettingsGroup denySiriWhileLocked]
+ -[MOSiriSettingsGroup setDenySiriWhileLocked:]
+ _MOCodingKeySecondaryButtonSubmenuItems
+ _OBJC_IVAR_$_MOShieldConfiguration._secondaryButtonSubmenuItems
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_9
+ ___49+[MOKeyboardSettingsGroup denySpellCheckMetadata]_block_invoke
+ ___50+[MOSiriSettingsGroup denySiriWhileLockedMetadata]_block_invoke
+ ___53+[MOKeyboardSettingsGroup denyAutoCorrectionMetadata]_block_invoke
+ ___54+[MOIntelligenceSettingsGroup denyMailSummaryMetadata]_block_invoke
+ ___55+[MOKeyboardSettingsGroup denyDefinitionLookupMetadata]_block_invoke
+ ___56+[MOKeyboardSettingsGroup denyKeyboardShortcutsMetadata]_block_invoke
+ ___57+[MOKeyboardSettingsGroup denyPredictiveKeyboardMetadata]_block_invoke
+ ___59+[MODeviceActivitySettingsGroup allowedDataClientsMetadata]_block_invoke
+ ___59+[MOIntelligenceSettingsGroup denyMailSmartRepliesMetadata]_block_invoke
+ ___61+[MOIntelligenceSettingsGroup denyNotesTranscriptionMetadata]_block_invoke
+ ___61+[MOKeyboardSettingsGroup denyContinuousPathKeyboardMetadata]_block_invoke
+ ___65+[MOIntelligenceSettingsGroup forceOnDeviceOnlyDictationMetadata]_block_invoke
+ ___66+[MOIntelligenceSettingsGroup denyAppleIntelligenceReportMetadata]_block_invoke
+ ___67+[MOIntelligenceSettingsGroup denySpotlightInternetResultsMetadata]_block_invoke
+ ___67+[MOIntelligenceSettingsGroup forceOnDeviceOnlyTranslationMetadata]_block_invoke
+ ___68+[MOIntelligenceSettingsGroup denyNotesTranscriptionSummaryMetadata]_block_invoke
+ ___68+[MOIntelligenceSettingsGroup denyVisualIntelligenceSummaryMetadata]_block_invoke
+ ___73+[MOIntelligenceSettingsGroup denyPersonalizedHandwritingResultsMetadata]_block_invoke
+ ___78+[MOIntelligenceSettingsGroup allowedExternalIntelligenceWorkspaceIDsMetadata]_block_invoke
+ ___81+[MOIntelligenceSettingsGroup denyExternalIntelligenceIntegrationsSignInMetadata]_block_invoke
+ _allowedDataClientsMetadata.metadata
+ _allowedDataClientsMetadata.onceToken
+ _allowedExternalIntelligenceWorkspaceIDsMetadata.metadata
+ _allowedExternalIntelligenceWorkspaceIDsMetadata.onceToken
+ _denyAppleIntelligenceReportMetadata.metadata
+ _denyAppleIntelligenceReportMetadata.onceToken
+ _denyAutoCorrectionMetadata.metadata
+ _denyAutoCorrectionMetadata.onceToken
+ _denyContinuousPathKeyboardMetadata.metadata
+ _denyContinuousPathKeyboardMetadata.onceToken
+ _denyDefinitionLookupMetadata.metadata
+ _denyDefinitionLookupMetadata.onceToken
+ _denyExternalIntelligenceIntegrationsSignInMetadata.metadata
+ _denyExternalIntelligenceIntegrationsSignInMetadata.onceToken
+ _denyKeyboardShortcutsMetadata.metadata
+ _denyKeyboardShortcutsMetadata.onceToken
+ _denyMailSmartRepliesMetadata.metadata
+ _denyMailSmartRepliesMetadata.onceToken
+ _denyMailSummaryMetadata.metadata
+ _denyMailSummaryMetadata.onceToken
+ _denyNotesTranscriptionMetadata.metadata
+ _denyNotesTranscriptionMetadata.onceToken
+ _denyNotesTranscriptionSummaryMetadata.metadata
+ _denyNotesTranscriptionSummaryMetadata.onceToken
+ _denyPersonalizedHandwritingResultsMetadata.metadata
+ _denyPersonalizedHandwritingResultsMetadata.onceToken
+ _denyPredictiveKeyboardMetadata.metadata
+ _denyPredictiveKeyboardMetadata.onceToken
+ _denySiriWhileLockedMetadata.metadata
+ _denySiriWhileLockedMetadata.onceToken
+ _denySpellCheckMetadata.metadata
+ _denySpellCheckMetadata.onceToken
+ _denySpotlightInternetResultsMetadata.metadata
+ _denySpotlightInternetResultsMetadata.onceToken
+ _denyVisualIntelligenceSummaryMetadata.metadata
+ _denyVisualIntelligenceSummaryMetadata.onceToken
+ _forceOnDeviceOnlyDictationMetadata.metadata
+ _forceOnDeviceOnlyDictationMetadata.onceToken
+ _forceOnDeviceOnlyTranslationMetadata.metadata
+ _forceOnDeviceOnlyTranslationMetadata.onceToken
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:secondaryButtonSubmenuItems:
+ _objc_retainAutoreleasedReturnValue
- -[MOShieldConfiguration initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:]
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "\t"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "SecondaryButtonSubmenuItems"
+ "T@\"NSArray\",R,C,V_secondaryButtonSubmenuItems"
+ "_secondaryButtonSubmenuItems"
+ "allowedDataClients"
+ "allowedDataClientsMetadata"
+ "allowedExternalIntelligenceWorkspaceIDs"
+ "allowedExternalIntelligenceWorkspaceIDsMetadata"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "denyAppleIntelligenceReport"
+ "denyAppleIntelligenceReportMetadata"
+ "denyAutoCorrection"
+ "denyAutoCorrectionMetadata"
+ "denyContinuousPathKeyboard"
+ "denyContinuousPathKeyboardMetadata"
+ "denyDefinitionLookup"
+ "denyDefinitionLookupMetadata"
+ "denyExternalIntelligenceIntegrationsSignIn"
+ "denyExternalIntelligenceIntegrationsSignInMetadata"
+ "denyKeyboardShortcuts"
+ "denyKeyboardShortcutsMetadata"
+ "denyMailSmartReplies"
+ "denyMailSmartRepliesMetadata"
+ "denyMailSummary"
+ "denyMailSummaryMetadata"
+ "denyNotesTranscription"
+ "denyNotesTranscriptionMetadata"
+ "denyNotesTranscriptionSummary"
+ "denyNotesTranscriptionSummaryMetadata"
+ "denyPersonalizedHandwritingResults"
+ "denyPersonalizedHandwritingResultsMetadata"
+ "denyPredictiveKeyboard"
+ "denyPredictiveKeyboardMetadata"
+ "denySiriWhileLocked"
+ "denySiriWhileLockedMetadata"
+ "denySpellCheck"
+ "denySpellCheckMetadata"
+ "denySpotlightInternetResults"
+ "denySpotlightInternetResultsMetadata"
+ "denyVisualIntelligenceSummary"
+ "denyVisualIntelligenceSummaryMetadata"
+ "forceOnDeviceOnlyDictation"
+ "forceOnDeviceOnlyDictationMetadata"
+ "forceOnDeviceOnlyTranslation"
+ "forceOnDeviceOnlyTranslationMetadata"
+ "initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:secondaryButtonSubmenuItems:"
+ "secondaryButtonSubmenuItems"
+ "setAllowedDataClients:"
+ "setAllowedExternalIntelligenceWorkspaceIDs:"
+ "setDenyAppleIntelligenceReport:"
+ "setDenyAutoCorrection:"
+ "setDenyContinuousPathKeyboard:"
+ "setDenyDefinitionLookup:"
+ "setDenyExternalIntelligenceIntegrationsSignIn:"
+ "setDenyKeyboardShortcuts:"
+ "setDenyMailSmartReplies:"
+ "setDenyMailSummary:"
+ "setDenyNotesTranscription:"
+ "setDenyNotesTranscriptionSummary:"
+ "setDenyPersonalizedHandwritingResults:"
+ "setDenyPredictiveKeyboard:"
+ "setDenySiriWhileLocked:"
+ "setDenySpellCheck:"
+ "setDenySpotlightInternetResults:"
+ "setDenyVisualIntelligenceSummary:"
+ "setForceOnDeviceOnlyDictation:"
+ "setForceOnDeviceOnlyTranslation:"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:"

```
