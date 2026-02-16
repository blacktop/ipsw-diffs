## profiled

> `/usr/libexec/profiled`

```diff

-2432.80.10.0.0
-  __TEXT.__text: 0xc1424
-  __TEXT.__auth_stubs: 0x2870
-  __TEXT.__objc_stubs: 0x10620
-  __TEXT.__objc_methlist: 0x6084
-  __TEXT.__const: 0x1206
-  __TEXT.__gcc_except_tab: 0x1c38
-  __TEXT.__oslogstring: 0xfc10
-  __TEXT.__cstring: 0xa3da
-  __TEXT.__objc_methname: 0x1607f
-  __TEXT.__objc_classname: 0xbd5
-  __TEXT.__objc_methtype: 0x2315
-  __TEXT.__constg_swiftt: 0xd0c
+2438.100.15.502.1
+  __TEXT.__text: 0xd1a44
+  __TEXT.__auth_stubs: 0x2800
+  __TEXT.__objc_stubs: 0x130c0
+  __TEXT.__objc_methlist: 0x617c
+  __TEXT.__const: 0x12fe
+  __TEXT.__gcc_except_tab: 0x1afc
+  __TEXT.__oslogstring: 0x10130
+  __TEXT.__cstring: 0xa74a
+  __TEXT.__objc_methname: 0x16817
+  __TEXT.__objc_classname: 0xc1e
+  __TEXT.__objc_methtype: 0x2392
+  __TEXT.__constg_swiftt: 0xdc0
   __TEXT.__swift5_typeref: 0x7ba
-  __TEXT.__swift5_reflstr: 0x9e6
-  __TEXT.__swift5_fieldmd: 0x928
+  __TEXT.__swift5_reflstr: 0xcb6
+  __TEXT.__swift5_fieldmd: 0xa28
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x90
-  __TEXT.__swift5_types: 0xa8
+  __TEXT.__swift5_types: 0xac
   __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x1ab8
-  __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x1448
-  __DATA_CONST.__got: 0x1ff0
-  __DATA_CONST.__auth_ptr: 0x220
-  __DATA_CONST.__const: 0x2d60
-  __DATA_CONST.__cfstring: 0x86e0
+  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__eh_frame: 0x1c0
+  __DATA_CONST.__auth_got: 0x1410
+  __DATA_CONST.__got: 0x2048
+  __DATA_CONST.__auth_ptr: 0x2f0
+  __DATA_CONST.__const: 0x2ec0
+  __DATA_CONST.__cfstring: 0x86a0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6e98
-  __DATA.__objc_selrefs: 0x5200
+  __DATA.__objc_const: 0x6fd8
+  __DATA.__objc_selrefs: 0x53c8
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x8e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 510442C2-4437-3A48-9D5C-5EC2175F2D99
-  Functions: 2598
-  Symbols:   1763
-  CStrings:  6746
+  UUID: 1449FF3A-E036-3CA4-945D-15CB2B4F6BDD
+  Functions: 2695
+  Symbols:   1769
+  CStrings:  6832
 
Symbols:
+ _$ss5ErrorMp
+ _$ss5ErrorWS
+ _MCFeatureAppleIntelligenceReportAllowed
+ _MCFeatureEmojiKeyboardAllowed
+ _MCFeatureExternalIntelligenceSignInAllowed
+ _MCFeatureMailSmartRepliesAllowed
+ _MCFeatureMailSummaryAllowed
+ _MCFeatureNotesTranscriptionAllowed
+ _MCFeatureNotesTranscriptionSummaryAllowed
+ _MCFeatureOnDeviceOnlyDictationForced
+ _MCFeatureOnDeviceOnlyTranslationForced
+ _MCFeaturePersonalizedHandwritingResultsAllowed
+ _MCFeatureSpotlightInternetResultsAllowed
+ _MCFeatureVisualIntelligenceSummaryAllowed
+ _swift_bridgeObjectRelease_n
+ _swift_willThrowTypedImpl
- _MCCheckSystemGroupContainerFileReadability
- _OBJC_CLASS_$_MCDictionaryWriter
- _abort
- _kMCInternalAbortOnUnreadableFiles
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retain_x4
- _objc_retain_x9
- _swift_initStackObject
- _swift_setDeallocating
CStrings:
+ "/Library/Caches/com.apple.xbs/3E448326-2A03-4636-A770-8A097ABC0120/TemporaryDirectory.Fmty6G/Sources/ManagedConfigurationTools/Connection/MCInteractionClient.m"
+ "/Library/Caches/com.apple.xbs/3E448326-2A03-4636-A770-8A097ABC0120/TemporaryDirectory.Fmty6G/Sources/ManagedConfigurationTools/profiled/MCProfileServiceServer.m"
+ "4AA3FF3B-332F-481C-B7DE-7E80973B07BF"
+ "Applying allowedExternalIntelligenceWorkspaceIDs settings: %{public}s"
+ "Applying denyAppleIntelligenceReport settings: %{bool,public}d"
+ "Applying denyAutoCorrection settings: %{bool,public}d"
+ "Applying denyContinuousPathKeyboard settings: %{bool,public}d"
+ "Applying denyDefinitionLookup settings: %{bool,public}d"
+ "Applying denyExternalIntelligenceIntegrationsSignIn settings: %{bool,public}d"
+ "Applying denyKeyboardShortcuts settings: %{bool,public}d"
+ "Applying denyMailSmartReplies settings: %{bool,public}d"
+ "Applying denyMailSummary settings: %{bool,public}d"
+ "Applying denyNotesTranscription settings: %{bool,public}d"
+ "Applying denyNotesTranscriptionSummary settings: %{bool,public}d"
+ "Applying denyPersonalizedHandwritingResults settings: %{bool,public}d"
+ "Applying denyPredictiveKeyboard settings: %{bool,public}d"
+ "Applying denySiriWhileLocked settings: %{bool,public}d"
+ "Applying denySpellCheck settings: %{bool,public}d"
+ "Applying denySpotlightInternetResults settings: %{bool,public}d"
+ "Applying denyVisualIntelligenceSummary settings: %{bool,public}d"
+ "Applying forceOnDeviceOnlyDictation settings: %{bool,public}d"
+ "Applying forceOnDeviceOnlyTranslation settings: %{bool,public}d"
+ "MCCleanupMigrator: Cloud configuration from DEP is mandatory, but no MDM installation detected on device. Cleaning up Cloud Config to enable re-enrollment."
+ "System group container check found errors: %{public}@"
+ "_removeAllInstalledProfiles"
+ "allowedExternalIntelligenceWorkspaceIDs"
+ "allowedExternalIntelligenceWorkspaceIDsMetadata"
+ "appleIntelligenceReportAllowed"
+ "assistantWhileLockedAllowed"
+ "autoCorrectionAllowed"
+ "continuousPathKeyboardAllowed"
+ "definitionLookupAllowed"
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
+ "effectiveDenyAppleIntelligenceReport should never be nil"
+ "effectiveDenyAutoCorrection should never be nil"
+ "effectiveDenyContinuousPathKeyboard should never be nil"
+ "effectiveDenyDefinitionLookup should never be nil"
+ "effectiveDenyExternalIntelligenceIntegrationsSignIn should never be nil"
+ "effectiveDenyKeyboardShortcuts should never be nil"
+ "effectiveDenyMailSmartReplies should never be nil"
+ "effectiveDenyMailSummary should never be nil"
+ "effectiveDenyNotesTranscription should never be nil"
+ "effectiveDenyNotesTranscriptionSummary should never be nil"
+ "effectiveDenyPersonalizedHandwritingResults should never be nil"
+ "effectiveDenyPredictiveKeyboard should never be nil"
+ "effectiveDenySiriWhileLocked should never be nil"
+ "effectiveDenySpellCheck should never be nil"
+ "effectiveDenySpotlightInternetResults should never be nil"
+ "effectiveDenyVisualIntelligenceSummary should never be nil"
+ "effectiveForceOnDeviceOnlyDictation should never be nil"
+ "effectiveForceOnDeviceOnlyTranslation should never be nil"
+ "externalIntelligenceIntegrationsSignInAllowed"
+ "forceOnDeviceOnlyDictation"
+ "forceOnDeviceOnlyDictationMetadata"
+ "forceOnDeviceOnlyTranslation"
+ "forceOnDeviceOnlyTranslationMetadata"
+ "installWiFiProfileIfNeeded:completionHandler:"
+ "isMDMEnrollmentAllowed"
+ "keyboardShortcutsAllowed"
+ "mailSmartRepliesAllowed"
+ "mailSummaryAllowed"
+ "mc_atomicWriteToPath:error:"
+ "notesTranscriptionAllowed"
+ "notesTranscriptionSummaryAllowed"
+ "onDeviceOnlyDictationForced"
+ "onDeviceOnlyTranslationForced"
+ "personalizedHandwritingResultsAllowed"
+ "predictiveKeyboardAllowed"
+ "spellCheckAllowed"
+ "spotlightInternetResultsAllowed"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSString\"B@\"NSError\">24"
+ "visualIntelligenceSummaryAllowed"
- "/Library/Caches/com.apple.xbs/Sources/ManagedConfigurationTools/Connection/MCInteractionClient.m"
- "/Library/Caches/com.apple.xbs/Sources/ManagedConfigurationTools/profiled/MCProfileServiceServer.m"
- "4AA3FF3B-3224-42E6-995E-481F49AE9260"
- "B28@0:8@16B24"
- "Could not serialize data for %{public}@: %{public}@"
- "Could not write data to path %{public}@: %{public}@"
- "MCWriteToBinaryFile:atomically:"
- "System group container check complete!"
- "System group container check found %{public}@ errors!"
- "initWithDictionary:path:"
- "recoverable"
- "unrecoverable"
- "write"

```
