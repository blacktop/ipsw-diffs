## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-  __TEXT.__text: 0x1bbff8
-  __TEXT.__objc_methlist: 0x20c84
-  __TEXT.__const: 0x490
+  __TEXT.__text: 0x19c9ec
+  __TEXT.__objc_methlist: 0x1efec
+  __TEXT.__const: 0x3d0
   __TEXT.__dlopen_cstrs: 0x538
-  __TEXT.__gcc_except_tab: 0x2358
-  __TEXT.__cstring: 0x41423
-  __TEXT.__oslogstring: 0x12bed
+  __TEXT.__gcc_except_tab: 0x2108
+  __TEXT.__cstring: 0x3d09c
+  __TEXT.__oslogstring: 0xf297
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x8800
+  __TEXT.__unwind_info: 0x8018
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8ca8
-  __DATA_CONST.__objc_classlist: 0xfb0
+  __DATA_CONST.__const: 0x8548
+  __DATA_CONST.__objc_classlist: 0xef8
   __DATA_CONST.__objc_catlist: 0x2a8
-  __DATA_CONST.__objc_protolist: 0x618
+  __DATA_CONST.__objc_protolist: 0x5e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcf58
+  __DATA_CONST.__objc_selrefs: 0xc060
   __DATA_CONST.__objc_protorefs: 0x170
-  __DATA_CONST.__objc_superrefs: 0xfb8
-  __DATA_CONST.__objc_arraydata: 0x2428
-  __DATA_CONST.__got: 0x17f8
-  __AUTH_CONST.__const: 0x3f40
-  __AUTH_CONST.__cfstring: 0x29b20
-  __AUTH_CONST.__objc_const: 0x39640
-  __AUTH_CONST.__objc_intobj: 0x27f0
-  __AUTH_CONST.__objc_dictobj: 0xd70
+  __DATA_CONST.__objc_superrefs: 0xf10
+  __DATA_CONST.__objc_arraydata: 0x2330
+  __DATA_CONST.__got: 0x16c8
+  __AUTH_CONST.__const: 0x3c80
+  __AUTH_CONST.__cfstring: 0x28260
+  __AUTH_CONST.__objc_const: 0x362e0
+  __AUTH_CONST.__objc_intobj: 0x2628
+  __AUTH_CONST.__objc_dictobj: 0xcf8
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0xb28
-  __AUTH.__objc_data: 0x8bd8
-  __AUTH.__data: 0x280
-  __DATA.__objc_ivar: 0x28e4
-  __DATA.__data: 0x4a70
-  __DATA.__bss: 0x1480
+  __AUTH_CONST.__auth_got: 0xae8
+  __AUTH.__objc_data: 0x8610
+  __AUTH.__data: 0x248
+  __DATA.__objc_ivar: 0x2574
+  __DATA.__data: 0x4800
+  __DATA.__bss: 0x1390
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1108
+  __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12845
-  Symbols:   40834
-  CStrings:  14571
+  Functions: 12087
+  Symbols:   38415
+  CStrings:  13701
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isTTRUserVocabProfileAttachmentEnabled]
+ +[AFInvocationContext supportsSecureCoding]
+ +[AFWindowDescriptor supportsSecureCoding]
+ -[AFAuthKitManager protoAgeRange]
+ -[AFConnection clearContextWithInvocationContext:]
+ -[AFConnection resumeSessionWithId:invocationContext:]
+ -[AFInvocationContext .cxx_destruct]
+ -[AFInvocationContext copyWithZone:]
+ -[AFInvocationContext description]
+ -[AFInvocationContext encodeWithCoder:]
+ -[AFInvocationContext hash]
+ -[AFInvocationContext initWithCoder:]
+ -[AFInvocationContext invocationSource]
+ -[AFInvocationContext isEqual:]
+ -[AFInvocationContext setInvocationSource:]
+ -[AFInvocationContext setTargetWindow:]
+ -[AFInvocationContext targetWindow]
+ -[AFRequestInfo invocationContext]
+ -[AFRequestInfo setInvocationContext:]
+ -[AFSiriAvailability initWithStatus:restrictionReasons:isAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:]
+ -[AFSiriAvailability restrictionReasons]
+ -[AFSiriAvailability status]
+ -[AFSpeechRequestOptions blockAttending]
+ -[AFSpeechRequestOptions setBlockAttending:]
+ -[AFVoiceInfo expressivityPresetString]
+ -[AFVoiceInfo expressivityPreset]
+ -[AFVoiceInfo initWithLanguageCode:gender:isCustom:name:footprint:contentVersion:masteredVersion:pacePreset:expressivityPreset:]
+ -[AFVoiceInfo initWithLanguageCode:gender:name:footprint:isCustom:pacePreset:expressivityPreset:]
+ -[AFVoiceInfo pacePresetString]
+ -[AFVoiceInfo pacePreset]
+ -[AFWindowDescriptor .cxx_destruct]
+ -[AFWindowDescriptor bundleIdentifier]
+ -[AFWindowDescriptor copyWithZone:]
+ -[AFWindowDescriptor description]
+ -[AFWindowDescriptor encodeWithCoder:]
+ -[AFWindowDescriptor hash]
+ -[AFWindowDescriptor identifier]
+ -[AFWindowDescriptor initWithCoder:]
+ -[AFWindowDescriptor initWithIdentifier:bundleIdentifier:pid:pidVersion:]
+ -[AFWindowDescriptor isEqual:]
+ -[AFWindowDescriptor pidVersion]
+ -[AFWindowDescriptor pid]
+ -[AFWindowDescriptor setBundleIdentifier:]
+ -[AFWindowDescriptor setIdentifier:]
+ -[AFWindowDescriptor setPid:]
+ -[AFWindowDescriptor setPidVersion:]
+ GCC_except_table10121
+ GCC_except_table10161
+ GCC_except_table10192
+ GCC_except_table10197
+ GCC_except_table10198
+ GCC_except_table10202
+ GCC_except_table10391
+ GCC_except_table10562
+ GCC_except_table10591
+ GCC_except_table10688
+ GCC_except_table10696
+ GCC_except_table10725
+ GCC_except_table1102
+ GCC_except_table11077
+ GCC_except_table11079
+ GCC_except_table11082
+ GCC_except_table11152
+ GCC_except_table11173
+ GCC_except_table11198
+ GCC_except_table11204
+ GCC_except_table11348
+ GCC_except_table11352
+ GCC_except_table11354
+ GCC_except_table11357
+ GCC_except_table11363
+ GCC_except_table11367
+ GCC_except_table11373
+ GCC_except_table11577
+ GCC_except_table1168
+ GCC_except_table1174
+ GCC_except_table11901
+ GCC_except_table12035
+ GCC_except_table12038
+ GCC_except_table12040
+ GCC_except_table1467
+ GCC_except_table1480
+ GCC_except_table1484
+ GCC_except_table1496
+ GCC_except_table1500
+ GCC_except_table1605
+ GCC_except_table1607
+ GCC_except_table1679
+ GCC_except_table1723
+ GCC_except_table2085
+ GCC_except_table2092
+ GCC_except_table2096
+ GCC_except_table2098
+ GCC_except_table2143
+ GCC_except_table2145
+ GCC_except_table2151
+ GCC_except_table2157
+ GCC_except_table2161
+ GCC_except_table2165
+ GCC_except_table2168
+ GCC_except_table2170
+ GCC_except_table2175
+ GCC_except_table2177
+ GCC_except_table2182
+ GCC_except_table2194
+ GCC_except_table2197
+ GCC_except_table2211
+ GCC_except_table2213
+ GCC_except_table2215
+ GCC_except_table2217
+ GCC_except_table2219
+ GCC_except_table2221
+ GCC_except_table2223
+ GCC_except_table2266
+ GCC_except_table2292
+ GCC_except_table231
+ GCC_except_table2349
+ GCC_except_table237
+ GCC_except_table2382
+ GCC_except_table243
+ GCC_except_table257
+ GCC_except_table2755
+ GCC_except_table3043
+ GCC_except_table3240
+ GCC_except_table3248
+ GCC_except_table3306
+ GCC_except_table352
+ GCC_except_table3683
+ GCC_except_table3687
+ GCC_except_table370
+ GCC_except_table3732
+ GCC_except_table3738
+ GCC_except_table374
+ GCC_except_table3763
+ GCC_except_table3769
+ GCC_except_table3978
+ GCC_except_table4087
+ GCC_except_table4098
+ GCC_except_table4131
+ GCC_except_table4134
+ GCC_except_table4211
+ GCC_except_table4215
+ GCC_except_table4225
+ GCC_except_table4236
+ GCC_except_table4249
+ GCC_except_table4334
+ GCC_except_table4336
+ GCC_except_table4360
+ GCC_except_table4475
+ GCC_except_table4538
+ GCC_except_table4541
+ GCC_except_table4545
+ GCC_except_table4576
+ GCC_except_table4650
+ GCC_except_table4708
+ GCC_except_table4734
+ GCC_except_table5007
+ GCC_except_table5149
+ GCC_except_table5162
+ GCC_except_table5205
+ GCC_except_table5299
+ GCC_except_table5406
+ GCC_except_table5408
+ GCC_except_table5589
+ GCC_except_table5626
+ GCC_except_table5632
+ GCC_except_table5636
+ GCC_except_table5656
+ GCC_except_table5662
+ GCC_except_table5665
+ GCC_except_table575
+ GCC_except_table6031
+ GCC_except_table6145
+ GCC_except_table625
+ GCC_except_table6276
+ GCC_except_table6399
+ GCC_except_table6413
+ GCC_except_table6432
+ GCC_except_table6433
+ GCC_except_table6436
+ GCC_except_table6442
+ GCC_except_table6489
+ GCC_except_table6491
+ GCC_except_table6493
+ GCC_except_table6511
+ GCC_except_table6517
+ GCC_except_table6560
+ GCC_except_table6572
+ GCC_except_table6718
+ GCC_except_table6804
+ GCC_except_table6858
+ GCC_except_table7094
+ GCC_except_table7097
+ GCC_except_table7098
+ GCC_except_table7295
+ GCC_except_table7354
+ GCC_except_table7568
+ GCC_except_table7571
+ GCC_except_table7583
+ GCC_except_table7584
+ GCC_except_table7597
+ GCC_except_table7598
+ GCC_except_table7599
+ GCC_except_table7605
+ GCC_except_table7643
+ GCC_except_table7649
+ GCC_except_table7655
+ GCC_except_table7723
+ GCC_except_table7725
+ GCC_except_table7763
+ GCC_except_table7874
+ GCC_except_table7937
+ GCC_except_table7939
+ GCC_except_table7941
+ GCC_except_table7943
+ GCC_except_table7957
+ GCC_except_table7963
+ GCC_except_table8086
+ GCC_except_table8093
+ GCC_except_table826
+ GCC_except_table829
+ GCC_except_table836
+ GCC_except_table8462
+ GCC_except_table8477
+ GCC_except_table8484
+ GCC_except_table8500
+ GCC_except_table8567
+ GCC_except_table8576
+ GCC_except_table8606
+ GCC_except_table8661
+ GCC_except_table9045
+ GCC_except_table9050
+ GCC_except_table9053
+ GCC_except_table9056
+ GCC_except_table9059
+ GCC_except_table9062
+ GCC_except_table9065
+ GCC_except_table9068
+ GCC_except_table9239
+ GCC_except_table9242
+ GCC_except_table9303
+ GCC_except_table9311
+ GCC_except_table9316
+ GCC_except_table9329
+ GCC_except_table9489
+ GCC_except_table9589
+ GCC_except_table967
+ GCC_except_table9778
+ GCC_except_table9783
+ GCC_except_table9913
+ _AFDeviceSupportsAlwaysListeningHeySiri
+ _AFIsIPhone
+ _AFIsIPhone.isIPhone
+ _AFIsIPhone.onceToken
+ _AFSiriAvailabilityRestrictionReasonsKey
+ _AFSiriAvailabilityStatusKey
+ _AFSiriAvailabilityVisualIntelligenceCapabilitiesKey
+ _AFVoiceExpressivityPresetGetName
+ _AFVoicePacePresetGetName
+ _MCFeatureSiri3489Allowed
+ _NSStringFromAFSiriRestrictionReasons
+ _NSStringFromAFSiriStatus
+ _NSStringFromAFSiriVisualIntelligenceCapabilities
+ _OBJC_CLASS_$_AFInvocationContext
+ _OBJC_CLASS_$_AFWindowDescriptor
+ _OBJC_IVAR_$_AFInvocationContext._invocationSource
+ _OBJC_IVAR_$_AFInvocationContext._targetWindow
+ _OBJC_IVAR_$_AFRequestInfo._invocationContext
+ _OBJC_IVAR_$_AFSiriAvailability._restrictionReasons
+ _OBJC_IVAR_$_AFSiriAvailability._status
+ _OBJC_IVAR_$_AFSpeechRequestOptions._blockAttending
+ _OBJC_IVAR_$_AFVoiceInfo._expressivityPreset
+ _OBJC_IVAR_$_AFVoiceInfo._pacePreset
+ _OBJC_IVAR_$_AFWindowDescriptor._bundleIdentifier
+ _OBJC_IVAR_$_AFWindowDescriptor._identifier
+ _OBJC_IVAR_$_AFWindowDescriptor._pid
+ _OBJC_IVAR_$_AFWindowDescriptor._pidVersion
+ _OBJC_METACLASS_$_AFInvocationContext
+ _OBJC_METACLASS_$_AFWindowDescriptor
+ __OBJC_$_CATEGORY_AceObject_$_AssistantAdditions
+ __OBJC_$_CATEGORY_NSArray_$_AFCollectionUtilities
+ __OBJC_$_CATEGORY_NSDate_$_AssistantAdditions
+ __OBJC_$_CATEGORY_NSDictionary_$_AFCollectionUtilities
+ __OBJC_$_CATEGORY_NSNull_$_AFBundleResourceSupport
+ __OBJC_$_CATEGORY_NSString_$_AFPreferences
+ __OBJC_$_CATEGORY_NSURL_$_AFBundleResourceSupport
+ __OBJC_$_CLASS_METHODS_AFInvocationContext
+ __OBJC_$_CLASS_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions|VSAdditions)
+ __OBJC_$_CLASS_METHODS_AFWindowDescriptor
+ __OBJC_$_CLASS_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
+ __OBJC_$_CLASS_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
+ __OBJC_$_CLASS_PROP_LIST_AFInvocationContext
+ __OBJC_$_CLASS_PROP_LIST_AFWindowDescriptor
+ __OBJC_$_INSTANCE_METHODS_AFClockTimer(ClockItem|AFClockTimerMutability)
+ __OBJC_$_INSTANCE_METHODS_AFInvocationContext
+ __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions|VSAdditions)
+ __OBJC_$_INSTANCE_METHODS_AFWindowDescriptor
+ __OBJC_$_INSTANCE_METHODS_AceObject(AssistantAdditions|AFSecurityDigestibleChunksProvider|AnalyticsContextVending)
+ __OBJC_$_INSTANCE_METHODS_NSArray(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
+ __OBJC_$_INSTANCE_METHODS_NSDate(AssistantAdditions|AFSecurityDigestibleChunksProvider)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
+ __OBJC_$_INSTANCE_METHODS_NSNull(AFBundleResourceSupport|AFSecurityDigestibleChunksProvider)
+ __OBJC_$_INSTANCE_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
+ __OBJC_$_INSTANCE_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
+ __OBJC_$_INSTANCE_VARIABLES_AFInvocationContext
+ __OBJC_$_INSTANCE_VARIABLES_AFWindowDescriptor
+ __OBJC_$_PROP_LIST_AFInvocationContext
+ __OBJC_$_PROP_LIST_AFWindowDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_AFClockTimer(ClockItem|AFClockTimerMutability)
+ __OBJC_CLASS_PROTOCOLS_$_AFInvocationContext
+ __OBJC_CLASS_PROTOCOLS_$_AFWindowDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_AceObject(AssistantAdditions|AFSecurityDigestibleChunksProvider|AnalyticsContextVending)
+ __OBJC_CLASS_PROTOCOLS_$_NSArray(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
+ __OBJC_CLASS_PROTOCOLS_$_NSDate(AssistantAdditions|AFSecurityDigestibleChunksProvider)
+ __OBJC_CLASS_PROTOCOLS_$_NSDictionary(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
+ __OBJC_CLASS_PROTOCOLS_$_NSNull(AFBundleResourceSupport|AFSecurityDigestibleChunksProvider)
+ __OBJC_CLASS_PROTOCOLS_$_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
+ __OBJC_CLASS_PROTOCOLS_$_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
+ __OBJC_CLASS_RO_$_AFInvocationContext
+ __OBJC_CLASS_RO_$_AFWindowDescriptor
+ __OBJC_METACLASS_RO_$_AFInvocationContext
+ __OBJC_METACLASS_RO_$_AFWindowDescriptor
+ ___AFIsIPhone_block_invoke
+ _kAFAllowSiri3489Key
+ _objc_msgSend$clearContextWithInvocationContext:
+ _objc_msgSend$expressivityPreset
+ _objc_msgSend$expressivityPresetString
+ _objc_msgSend$initWithIdentifier:bundleIdentifier:pid:pidVersion:
+ _objc_msgSend$initWithLanguageCode:gender:isCustom:name:footprint:contentVersion:masteredVersion:pacePreset:expressivityPreset:
+ _objc_msgSend$initWithStatus:restrictionReasons:isAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:
+ _objc_msgSend$invocationSource
+ _objc_msgSend$pacePreset
+ _objc_msgSend$pacePresetString
+ _objc_msgSend$pidVersion
+ _objc_msgSend$protoAccount
+ _objc_msgSend$proto_ageRange
+ _objc_msgSend$restrictionReasons
+ _objc_msgSend$resumeSessionWithId:invocationContext:
+ _objc_msgSend$setBlockAttending:
+ _objc_msgSend$setInvocationContext:
+ _objc_msgSend$setTargetWindow:
+ _objc_msgSend$targetWindow
- +[AFMyriadAccessoryMessage acknowledgeRequestKey]
- +[AFMyriadAccessoryMessage audioDataKey]
- +[AFMyriadAccessoryMessage deviceInfoKey]
- +[AFMyriadAccessoryMessage electionDecisionKey]
- +[AFMyriadAccessoryMessage emergencyHandledKey]
- +[AFMyriadAccessoryMessage isMyriadRequestMessage:]
- +[AFMyriadAccessoryMessage messageKey]
- +[AFMyriadAccessoryMessage myriadRequestTypeAsString:]
- +[AFMyriadAccessoryMessage protocolName]
- +[AFMyriadAccessoryMessage requestTypeKey]
- +[AFMyriadAccessoryMessage sessionIdKey]
- +[AFMyriadAdvertisementContext newWithBuilder:]
- +[AFMyriadAdvertisementContext supportsSecureCoding]
- +[AFMyriadContext newWithBuilder:]
- +[AFMyriadContext supportsSecureCoding]
- +[AFMyriadCoordinator clearCurrentCoordinator]
- +[AFMyriadCoordinator currentCoordinator]
- +[AFMyriadCoordinator didChangeDefaults]
- +[AFMyriadGoodnessScoreOverrideState newWithBuilder:]
- +[AFMyriadGoodnessScoreOverrideState supportsSecureCoding]
- +[AFMyriadMetrics sharedInstance]
- +[AFMyriadMonitor sharedMonitor]
- +[AFMyriadPerceptualAudioHash newWithBuilder:]
- +[AFMyriadPerceptualAudioHash supportsSecureCoding]
- +[AFMyriadSession newWithBuilder:]
- +[AFMyriadSession supportsSecureCoding]
- -[AFMyriadAccessoryMessage .cxx_destruct]
- -[AFMyriadAccessoryMessage _copyRawBytesFromSource:toDest:length:]
- -[AFMyriadAccessoryMessage _initWithMessage:]
- -[AFMyriadAccessoryMessage _initializeMessageObj:]
- -[AFMyriadAccessoryMessage _initializeMessageObjFromDictionary:]
- -[AFMyriadAccessoryMessage accessoryId]
- -[AFMyriadAccessoryMessage audioHash]
- -[AFMyriadAccessoryMessage description]
- -[AFMyriadAccessoryMessage deviceClass]
- -[AFMyriadAccessoryMessage deviceGroup]
- -[AFMyriadAccessoryMessage electionWon]
- -[AFMyriadAccessoryMessage goodnessScore]
- -[AFMyriadAccessoryMessage initElectionDecisionMessageWithSessionId:decision:accessoryId:]
- -[AFMyriadAccessoryMessage initPreheatMessageWithSessionId:accessoryId:]
- -[AFMyriadAccessoryMessage initResetMessageWithSessionId:accessoryId:]
- -[AFMyriadAccessoryMessage initWithAccessoryMessage:accessoryId:]
- -[AFMyriadAccessoryMessage initWithAccessoryMessageAsDictionary:accessoryId:]
- -[AFMyriadAccessoryMessage initWithRequestType:session:voiceTriggerEndTime:audioHash:goodnessScore:userConfidenceScore:tieBreaker:deviceClass:deviceGroup:productType:electionDecision:emergencyHandled:ack:accessoryId:]
- -[AFMyriadAccessoryMessage isAcknowledgement]
- -[AFMyriadAccessoryMessage isEmergencyHandled]
- -[AFMyriadAccessoryMessage isSane]
- -[AFMyriadAccessoryMessage messageAsData]
- -[AFMyriadAccessoryMessage productType]
- -[AFMyriadAccessoryMessage requestType]
- -[AFMyriadAccessoryMessage session]
- -[AFMyriadAccessoryMessage tieBreaker]
- -[AFMyriadAccessoryMessage userConfidenceScore]
- -[AFMyriadAccessoryMessage usesSerializedProtocol]
- -[AFMyriadAccessoryMessage version]
- -[AFMyriadAccessoryMessage voiceTriggerEndTime]
- -[AFMyriadAccessoryMetricMessage _decodeMetricDataPayload:decodedPayload:]
- -[AFMyriadAccessoryMetricMessage _extractMetricDataFromDataPayload:]
- -[AFMyriadAccessoryMetricMessage advDelay]
- -[AFMyriadAccessoryMetricMessage advInterval]
- -[AFMyriadAccessoryMetricMessage coordinationAllowed]
- -[AFMyriadAccessoryMetricMessage decision]
- -[AFMyriadAccessoryMetricMessage deviceGroup]
- -[AFMyriadAccessoryMetricMessage electionParticipantCount]
- -[AFMyriadAccessoryMetricMessage electionParticipantDeviceType]
- -[AFMyriadAccessoryMetricMessage electionParticipantGoodnessScore]
- -[AFMyriadAccessoryMetricMessage electionParticipantProductType]
- -[AFMyriadAccessoryMetricMessage eventType]
- -[AFMyriadAccessoryMetricMessage homepodInvolved]
- -[AFMyriadAccessoryMetricMessage initWithDataPayload:]
- -[AFMyriadAccessoryMetricMessage initWithMetricData:]
- -[AFMyriadAccessoryMetricMessage lateToElection]
- -[AFMyriadAccessoryMetricMessage messageAsData]
- -[AFMyriadAccessoryMetricMessage messageAsStruct]
- -[AFMyriadAccessoryMetricMessage previousDecisionTime]
- -[AFMyriadAccessoryMetricMessage previousDecision]
- -[AFMyriadAccessoryMetricMessage requestType]
- -[AFMyriadAccessoryMetricMessage sessionId]
- -[AFMyriadAccessoryMetricMessage state]
- -[AFMyriadAccessoryMetricMessage version]
- -[AFMyriadAccessoryMetricMessage winnerDeviceClass]
- -[AFMyriadAccessoryMetricMessage winnerGoodnessScore]
- -[AFMyriadAccessoryMetricMessage winnerProductType]
- -[AFMyriadAdvertisementContext .cxx_destruct]
- -[AFMyriadAdvertisementContext _descriptionWithIndent:]
- -[AFMyriadAdvertisementContext contextData]
- -[AFMyriadAdvertisementContext contextFetchDelay]
- -[AFMyriadAdvertisementContext copyWithZone:]
- -[AFMyriadAdvertisementContext description]
- -[AFMyriadAdvertisementContext encodeWithCoder:]
- -[AFMyriadAdvertisementContext generation]
- -[AFMyriadAdvertisementContext hash]
- -[AFMyriadAdvertisementContext initWithBuilder:]
- -[AFMyriadAdvertisementContext initWithCoder:]
- -[AFMyriadAdvertisementContext initWithGeneration:contextData:contextFetchDelay:]
- -[AFMyriadAdvertisementContext init]
- -[AFMyriadAdvertisementContext isEqual:]
- -[AFMyriadAdvertisementContext(AFMyriadAdvertisementContextMutability) mutatedCopyWithMutator:]
- -[AFMyriadAdvertisementContextManager .cxx_destruct]
- -[AFMyriadAdvertisementContextManager _resetSettingsConnection]
- -[AFMyriadAdvertisementContextManager _settingsConnection]
- -[AFMyriadAdvertisementContextManager initWithQueue:]
- -[AFMyriadAdvertisementContextManager reset]
- -[AFMyriadAdvertisementContextManager triggerABCForType:subType:context:]
- -[AFMyriadAdvertisementContextRecord .cxx_destruct]
- -[AFMyriadAdvertisementContextRecord _advertisementPayloadSizeForVersion:]
- -[AFMyriadAdvertisementContextRecord _deviceIDFromBytes:]
- -[AFMyriadAdvertisementContextRecord _getAdvertisementRecordTypeForVersion:data:]
- -[AFMyriadAdvertisementContextRecord _getDeviceIdForVersion:data:]
- -[AFMyriadAdvertisementContextRecord _getMyriadAdvertisementDataForVersion:data:]
- -[AFMyriadAdvertisementContextRecord _getVoiceTriggerEndTimeForVersion:data:]
- -[AFMyriadAdvertisementContextRecord _initializeMyriadAdvertisementContextRecordFromData:]
- -[AFMyriadAdvertisementContextRecord advertisementContextVersion]
- -[AFMyriadAdvertisementContextRecord advertisementDispatchTime]
- -[AFMyriadAdvertisementContextRecord advertisementPayload]
- -[AFMyriadAdvertisementContextRecord advertisementRecordType]
- -[AFMyriadAdvertisementContextRecord compareAdvertisementPayload:]
- -[AFMyriadAdvertisementContextRecord description]
- -[AFMyriadAdvertisementContextRecord deviceID]
- -[AFMyriadAdvertisementContextRecord initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:]
- -[AFMyriadAdvertisementContextRecord initWithMyriadAdvertisementContextRecordData:]
- -[AFMyriadAdvertisementContextRecord isSaneForVoiceTriggerEndTime:endtimeDistanceThreshold:]
- -[AFMyriadAdvertisementContextRecord myriadAdvertisementContextAsData]
- -[AFMyriadAdvertisementContextRecord recordForDeviceId:]
- -[AFMyriadAdvertisementContextRecord setAdvertisementDispatchTime:]
- -[AFMyriadAdvertisementContextRecord voiceTriggerEndTime]
- -[AFMyriadContext .cxx_destruct]
- -[AFMyriadContext _descriptionWithIndent:]
- -[AFMyriadContext activationExpirationTime]
- -[AFMyriadContext activationSource]
- -[AFMyriadContext copyWithZone:]
- -[AFMyriadContext description]
- -[AFMyriadContext encodeWithCoder:]
- -[AFMyriadContext hash]
- -[AFMyriadContext initWithBuilder:]
- -[AFMyriadContext initWithCoder:]
- -[AFMyriadContext initWithTimestamp:perceptualAudioHash:overrideState:activationSource:activationExpirationTime:]
- -[AFMyriadContext init]
- -[AFMyriadContext isEqual:]
- -[AFMyriadContext overrideState]
- -[AFMyriadContext perceptualAudioHash]
- -[AFMyriadContext timestamp]
- -[AFMyriadContext(AFMyriadContextMutability) mutatedCopyWithMutator:]
- -[AFMyriadCoordinator .cxx_destruct]
- -[AFMyriadCoordinator _addElectionAdvertisementDataToMyriadSession:]
- -[AFMyriadCoordinator _adjustActionWindowsFromSlowdown:]
- -[AFMyriadCoordinator _advertise:afterDelay:maxInterval:andMoveTo:]
- -[AFMyriadCoordinator _advertise:andMoveTo:]
- -[AFMyriadCoordinator _advertiseIndefinite:]
- -[AFMyriadCoordinator _advertiseSlowdown]
- -[AFMyriadCoordinator _advertiseSuppressTriggerInOutput]
- -[AFMyriadCoordinator _advertiseTrigger]
- -[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]
- -[AFMyriadCoordinator _ageWedgeFilter]
- -[AFMyriadCoordinator _cancelOverallTimeout]
- -[AFMyriadCoordinator _cancelTimer]
- -[AFMyriadCoordinator _clearMyriadSession]
- -[AFMyriadCoordinator _clearWiProxReadinessTimer]
- -[AFMyriadCoordinator _contextFetchDelayForAdvertimentInterval:advertisementDelay:]
- -[AFMyriadCoordinator _createDispatchTimerFor:toExecute:]
- -[AFMyriadCoordinator _createDispatchTimerForEvent:toExecute:]
- -[AFMyriadCoordinator _createDispatchTimerWithTime:toExecute:]
- -[AFMyriadCoordinator _createMyriadSessionIfRequired]
- -[AFMyriadCoordinator _createWaitWiProxTimer:waitBlock:]
- -[AFMyriadCoordinator _deviceShouldContinue:]
- -[AFMyriadCoordinator _duringNextWindowEnterState:]
- -[AFMyriadCoordinator _duringNextWindowExecute:]
- -[AFMyriadCoordinator _endAdvertising:]
- -[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]
- -[AFMyriadCoordinator _endAdvertisingWithDeviceProhibitions:]
- -[AFMyriadCoordinator _enterBLEDiagnosticMode]
- -[AFMyriadCoordinator _enterState:]
- -[AFMyriadCoordinator _enteringIntoState:fromState:]
- -[AFMyriadCoordinator _forceLocalWinner:]
- -[AFMyriadCoordinator _handleStateMachineErrorIfNeeded]
- -[AFMyriadCoordinator _inTaskTriggerWasTooSoon]
- -[AFMyriadCoordinator _initDeviceClassAndAdjustments]
- -[AFMyriadCoordinator _initializeTimer]
- -[AFMyriadCoordinator _initializeWiProxReadinessTimer]
- -[AFMyriadCoordinator _isAPhone:]
- -[AFMyriadCoordinator _leaveBLEDiagnosticMode]
- -[AFMyriadCoordinator _loseElection]
- -[AFMyriadCoordinator _myriadSession]
- -[AFMyriadCoordinator _myriadStateForSelf:]
- -[AFMyriadCoordinator _nextElectionPublisherState]
- -[AFMyriadCoordinator _okayToSuppressOnOutput]
- -[AFMyriadCoordinator _phsSetupRecord]
- -[AFMyriadCoordinator _readDefaults]
- -[AFMyriadCoordinator _resetActionWindows]
- -[AFMyriadCoordinator _resetAdvertisementTimings]
- -[AFMyriadCoordinator _resetAudioData]
- -[AFMyriadCoordinator _resumeWiProxReadinessTimer]
- -[AFMyriadCoordinator _setMyriadContext:]
- -[AFMyriadCoordinator _setOverallTimeout]
- -[AFMyriadCoordinator _setupActionWindows]
- -[AFMyriadCoordinator _shouldContinueFor:]
- -[AFMyriadCoordinator _shouldHandleEmergency]
- -[AFMyriadCoordinator _shouldStopListeningBeforeAdvertising]
- -[AFMyriadCoordinator _shouldUseContextCollector]
- -[AFMyriadCoordinator _signalEmergencyCallHandled]
- -[AFMyriadCoordinator _sortedReplies:]
- -[AFMyriadCoordinator _sortedReplies]
- -[AFMyriadCoordinator _startAdvertising:afterDelay:maxInterval:]
- -[AFMyriadCoordinator _startAdvertisingFromInTaskVoiceTrigger]
- -[AFMyriadCoordinator _startAdvertisingFromVoiceTrigger]
- -[AFMyriadCoordinator _startListenTimer]
- -[AFMyriadCoordinator _startListening:]
- -[AFMyriadCoordinator _startListeningAfterWiProxIsReady:inState:completion:]
- -[AFMyriadCoordinator _startTimer:for:thenEnterState:]
- -[AFMyriadCoordinator _startTimer:for:thenExecute:]
- -[AFMyriadCoordinator _stateAsString:]
- -[AFMyriadCoordinator _stateAsString]
- -[AFMyriadCoordinator _stopAdvertising:]
- -[AFMyriadCoordinator _stopAdvertisingAndListening]
- -[AFMyriadCoordinator _stopListening:]
- -[AFMyriadCoordinator _suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:]
- -[AFMyriadCoordinator _suspendWiProxReadinessTimer]
- -[AFMyriadCoordinator _testAndFilterAdvertisementsFromContextCollector:voiceTriggerEndTime:advertisementDispatchTime:advertisement:]
- -[AFMyriadCoordinator _testAndUpdateWedgeFilter:]
- -[AFMyriadCoordinator _trackHeySiriStartedAdvertisingAt:]
- -[AFMyriadCoordinator _triggerABCForType:context:]
- -[AFMyriadCoordinator _unduck]
- -[AFMyriadCoordinator _updateRepliesWith:id:data:]
- -[AFMyriadCoordinator _updateVoiceTriggerTimeFromFile]
- -[AFMyriadCoordinator _waitWiProx:andExecute:]
- -[AFMyriadCoordinator _waitWiProxAndExecute:]
- -[AFMyriadCoordinator _winElection]
- -[AFMyriadCoordinator advertiseWith:]
- -[AFMyriadCoordinator advertiseWith:afterDelay:maxInterval:]
- -[AFMyriadCoordinator continuationRecord]
- -[AFMyriadCoordinator dealloc]
- -[AFMyriadCoordinator deviceClass]
- -[AFMyriadCoordinator deviceGroup]
- -[AFMyriadCoordinator deviceTrumpDelay]
- -[AFMyriadCoordinator directTriggerRecord]
- -[AFMyriadCoordinator emergencyHandledRecord]
- -[AFMyriadCoordinator emergencyRecord]
- -[AFMyriadCoordinator emptyRecord]
- -[AFMyriadCoordinator endAdvertising:]
- -[AFMyriadCoordinator endAdvertisingAfterDelay:]
- -[AFMyriadCoordinator endAdvertisingWithDeviceProhibitions:]
- -[AFMyriadCoordinator endTask]
- -[AFMyriadCoordinator enterState:]
- -[AFMyriadCoordinator faceDetectedBoostWithMyriadContext:]
- -[AFMyriadCoordinator heySiri:failedToStartAdvertisingWithError:]
- -[AFMyriadCoordinator heySiri:failedToStartScanningWithError:]
- -[AFMyriadCoordinator heySiri:foundDevice:withInfo:]
- -[AFMyriadCoordinator heySiriAdvertisingPending:]
- -[AFMyriadCoordinator heySiriDidUpdateState:]
- -[AFMyriadCoordinator heySiriStartedAdvertising:]
- -[AFMyriadCoordinator heySiriStartedAdvertisingAt:timeStamp:]
- -[AFMyriadCoordinator heySiriStartedScanning:]
- -[AFMyriadCoordinator heySiriStoppedAdvertising:]
- -[AFMyriadCoordinator heySiriStoppedScanning:]
- -[AFMyriadCoordinator inTask]
- -[AFMyriadCoordinator initWithDelegate:]
- -[AFMyriadCoordinator injectAdvertisementForTesting:forDevice:]
- -[AFMyriadCoordinator instrumentationUpdateBoost:value:]
- -[AFMyriadCoordinator lateSuppressionRecord]
- -[AFMyriadCoordinator myriadSession:]
- -[AFMyriadCoordinator notifyCurrentDecisionResult]
- -[AFMyriadCoordinator notifyObserver:didReceiveNotificationWithToken:]
- -[AFMyriadCoordinator preheatWiProx]
- -[AFMyriadCoordinator readDefaults]
- -[AFMyriadCoordinator requestWillPresentUsefulUserResult]
- -[AFMyriadCoordinator resetMyriadCoordinator:]
- -[AFMyriadCoordinator resetReplies]
- -[AFMyriadCoordinator resetStateMachine]
- -[AFMyriadCoordinator responseObject:]
- -[AFMyriadCoordinator setCurrentRequestId:]
- -[AFMyriadCoordinator setInTask:]
- -[AFMyriadCoordinator setupActionWindows]
- -[AFMyriadCoordinator setupAdvIntervalsInDelay:interval:withSlowdown:]
- -[AFMyriadCoordinator setupEnabled:]
- -[AFMyriadCoordinator slowdownRecord:]
- -[AFMyriadCoordinator startAdvertising:afterDelay:maxInterval:]
- -[AFMyriadCoordinator startAdvertisingEmergencyHandled]
- -[AFMyriadCoordinator startAdvertisingEmergencySignal]
- -[AFMyriadCoordinator startAdvertisingEmergency]
- -[AFMyriadCoordinator startAdvertisingForPHSSetupAfterDelay:maxInterval:]
- -[AFMyriadCoordinator startAdvertisingFromAlertFiringVoiceTriggerWithContext:]
- -[AFMyriadCoordinator startAdvertisingFromAlertFiringVoiceTrigger]
- -[AFMyriadCoordinator startAdvertisingFromCarPlayTrigger]
- -[AFMyriadCoordinator startAdvertisingFromDirectTriggerWithContext:]
- -[AFMyriadCoordinator startAdvertisingFromDirectTrigger]
- -[AFMyriadCoordinator startAdvertisingFromInEarTrigger]
- -[AFMyriadCoordinator startAdvertisingFromInTaskTriggerWithContext:]
- -[AFMyriadCoordinator startAdvertisingFromInTaskVoiceTriggerWithContext:]
- -[AFMyriadCoordinator startAdvertisingFromInTaskVoiceTrigger]
- -[AFMyriadCoordinator startAdvertisingFromOutgoingTriggerWithContext:]
- -[AFMyriadCoordinator startAdvertisingFromOutgoingTrigger]
- -[AFMyriadCoordinator startAdvertisingFromVoiceTriggerAdjusted:]
- -[AFMyriadCoordinator startAdvertisingFromVoiceTriggerAdjusted:withContext:]
- -[AFMyriadCoordinator startAdvertisingFromVoiceTriggerWithContext:]
- -[AFMyriadCoordinator startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:]
- -[AFMyriadCoordinator startAdvertisingFromVoiceTrigger]
- -[AFMyriadCoordinator startAdvertisingSlowdown:]
- -[AFMyriadCoordinator startListening:]
- -[AFMyriadCoordinator startListeningToEmergencySignal]
- -[AFMyriadCoordinator startListening]
- -[AFMyriadCoordinator startResponseAdvertising:]
- -[AFMyriadCoordinator startWatchAdvertisingFromDirectTriggerWithContext:]
- -[AFMyriadCoordinator startWatchAdvertisingFromDirectTrigger]
- -[AFMyriadCoordinator startWatchAdvertisingFromVoiceTriggerWithContext:]
- -[AFMyriadCoordinator startWatchAdvertisingFromVoiceTrigger]
- -[AFMyriadCoordinator stateAsString:]
- -[AFMyriadCoordinator stopListening:]
- -[AFMyriadCoordinator stopListening]
- -[AFMyriadCoordinator updateRepliesWith:id:data:]
- -[AFMyriadCoordinator updateRequestId:]
- -[AFMyriadCoordinator voiceTriggerRecord]
- -[AFMyriadCoordinator waitWiProx:andExecute:]
- -[AFMyriadEmergencyCallPunchout .cxx_destruct]
- -[AFMyriadEmergencyCallPunchout init]
- -[AFMyriadEmergencyCallPunchout initiateEmergencyCallMyriad]
- -[AFMyriadGoodnessScoreContext .cxx_destruct]
- -[AFMyriadGoodnessScoreContext description]
- -[AFMyriadGoodnessScoreContext getOverridingContext]
- -[AFMyriadGoodnessScoreContext init]
- -[AFMyriadGoodnessScoreContext mediaPlaybackInterruptedTime]
- -[AFMyriadGoodnessScoreContext reasons]
- -[AFMyriadGoodnessScoreContext recentlyWonBySmallAmount]
- -[AFMyriadGoodnessScoreContext setMediaPlaybackInterruptedTime:]
- -[AFMyriadGoodnessScoreContext setOverridingContext:]
- -[AFMyriadGoodnessScoreContext setReasons:]
- -[AFMyriadGoodnessScoreContext setRecentlyWonBySmallAmount:]
- -[AFMyriadGoodnessScoreEvaluator .cxx_destruct]
- -[AFMyriadGoodnessScoreEvaluator _bumpGoodnessScore:lastActivationTime:mediaPlaybackInterruptedTime:ignoreAdjustedBoost:recentlyWonBySmallAmount:]
- -[AFMyriadGoodnessScoreEvaluator _createSettingsConnectionIfRequired]
- -[AFMyriadGoodnessScoreEvaluator _fetchDevicePlatformBiasIfRequired]
- -[AFMyriadGoodnessScoreEvaluator _findSidekickBoost:isSpeaker:model:]
- -[AFMyriadGoodnessScoreEvaluator _getRecentBump:ignoreAdjustedBoost:recentlyWonBySmallAmount:]
- -[AFMyriadGoodnessScoreEvaluator _readSidekickBoostsFile:]
- -[AFMyriadGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]
- -[AFMyriadGoodnessScoreEvaluator _setSidekickPlatformBiasForSpeaker:model:]
- -[AFMyriadGoodnessScoreEvaluator _settingsConnectionDidDisconnect]
- -[AFMyriadGoodnessScoreEvaluator _updateMediaPlaybackBoost:]
- -[AFMyriadGoodnessScoreEvaluator _updatePlatformBias:]
- -[AFMyriadGoodnessScoreEvaluator _updateRecentSiriBoostTrialEnabled:]
- -[AFMyriadGoodnessScoreEvaluator _updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:]
- -[AFMyriadGoodnessScoreEvaluator _updateSidekickBoosts:]
- -[AFMyriadGoodnessScoreEvaluator dealloc]
- -[AFMyriadGoodnessScoreEvaluator evaluateForAudioAccessory]
- -[AFMyriadGoodnessScoreEvaluator getMyriadAdjustedBoostForGoodnessScoreContext:]
- -[AFMyriadGoodnessScoreEvaluator getPlatformBias]
- -[AFMyriadGoodnessScoreEvaluator initWithDeviceInstanceContext:preferences:queue:]
- -[AFMyriadGoodnessScoreEvaluator initWithDeviceInstanceContext:preferences:queue:instrumentation:]
- -[AFMyriadGoodnessScoreEvaluator initWithDeviceInstanceContext:queue:]
- -[AFMyriadGoodnessScoreEvaluator lastActivationTime]
- -[AFMyriadGoodnessScoreEvaluator myriadTrialBoostsUpdated:]
- -[AFMyriadGoodnessScoreEvaluator preheat]
- -[AFMyriadGoodnessScoreEvaluator setLastActivationTime:]
- -[AFMyriadGoodnessScoreOverrideContext overriddenAdjustedScore]
- -[AFMyriadGoodnessScoreOverrideContext overrideContext]
- -[AFMyriadGoodnessScoreOverrideContext setOverriddenAdjustedScore:]
- -[AFMyriadGoodnessScoreOverrideContext setOverrideContext:]
- -[AFMyriadGoodnessScoreOverrideState .cxx_destruct]
- -[AFMyriadGoodnessScoreOverrideState _descriptionWithIndent:]
- -[AFMyriadGoodnessScoreOverrideState copyWithZone:]
- -[AFMyriadGoodnessScoreOverrideState description]
- -[AFMyriadGoodnessScoreOverrideState encodeWithCoder:]
- -[AFMyriadGoodnessScoreOverrideState hash]
- -[AFMyriadGoodnessScoreOverrideState initWithBuilder:]
- -[AFMyriadGoodnessScoreOverrideState initWithCoder:]
- -[AFMyriadGoodnessScoreOverrideState initWithOverrideOption:reason:]
- -[AFMyriadGoodnessScoreOverrideState init]
- -[AFMyriadGoodnessScoreOverrideState isEqual:]
- -[AFMyriadGoodnessScoreOverrideState overrideOption]
- -[AFMyriadGoodnessScoreOverrideState reason]
- -[AFMyriadGoodnessScoreOverrideState(AFMyriadGoodnessScoreOverrideStateMutability) mutatedCopyWithMutator:]
- -[AFMyriadInstrumentation .cxx_destruct]
- -[AFMyriadInstrumentation _boostTypeAsString:]
- -[AFMyriadInstrumentation _createSchemaClientEvent:]
- -[AFMyriadInstrumentation _logRequestLinkMessageRequestId:cdaId:]
- -[AFMyriadInstrumentation _sendAndLogClientEvent:stState:atTimestamp:]
- -[AFMyriadInstrumentation currentBoost]
- -[AFMyriadInstrumentation getPreviousBoostsWithCompletion:]
- -[AFMyriadInstrumentation init]
- -[AFMyriadInstrumentation logCDADeviceStateActivityEnded:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDADeviceStateActivityStartedOrChanged:withTrigger:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionAdvertisingEnded:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionAdvertisingEnding:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionAdvertisingStarted:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionAdvertisingStarting:withDelay:withInterval:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionDecisionMadeDebug:withCrossDeviceArbitrationAllowed:advertisementData:withDeviceGroup:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation logCDAElectionTimerEnded:withCdaId:withTimestamp:]
- -[AFMyriadInstrumentation resetCurrentBoost]
- -[AFMyriadInstrumentation updateBoost:value:]
- -[AFMyriadInstrumentation updateIsTrump:withReason:]
- -[AFMyriadMetrics _createEndAnalyticContexFromIntermediateContext:forVersion:sessionId:]
- -[AFMyriadMetrics _decisionMadeContext:additionalContext:instrumentation:completion:]
- -[AFMyriadMetrics _getCDASchemaCDATriggerType:]
- -[AFMyriadMetrics _getRequestType:]
- -[AFMyriadMetrics _submitMyriadMetrics:additionalContext:toStream:instrumentation:completion:]
- -[AFMyriadMetrics getCDASessionId:]
- -[AFMyriadMetrics getSessionId:]
- -[AFMyriadMetrics getVersion:]
- -[AFMyriadMetrics isMyriadMetricsMessage:]
- -[AFMyriadMetrics submitAccessoryMyriadMetricsToAnalyticsStream:payload:additionalContext:instrumentation:completion:]
- -[AFMyriadMetrics submitAccessoryMyriadMetricsToAnalyticsStream:payload:instrumentation:completion:]
- -[AFMyriadMetrics submitMyriadMetricsToAnalyticsStream:context:forEvent:contextNoCopy:]
- -[AFMyriadMetricsAdditionalContext description]
- -[AFMyriadMetricsAdditionalContext deviceClass]
- -[AFMyriadMetricsAdditionalContext deviceProductType]
- -[AFMyriadMetricsAdditionalContext goodnessScore]
- -[AFMyriadMetricsAdditionalContext initWithRawGoodnessScore:goodnessScore:deviceClass:deviceProductType:]
- -[AFMyriadMetricsAdditionalContext rawGoodnessScore]
- -[AFMyriadMonitor .cxx_destruct]
- -[AFMyriadMonitor _cancelRepostedMyriadDecisionTimer]
- -[AFMyriadMonitor _clear]
- -[AFMyriadMonitor _dequeueBlocksWithSignal:]
- -[AFMyriadMonitor _deregisterFromMyriadEventNotifications]
- -[AFMyriadMonitor _deregisterFromRepostedDecisionResultsObservers]
- -[AFMyriadMonitor _enqueueBlock:forReason:]
- -[AFMyriadMonitor _fetchCurrentMyriadDecisionWithWaitTime:]
- -[AFMyriadMonitor _flushCompletions:]
- -[AFMyriadMonitor _ignoreRepostMyriadNotification:]
- -[AFMyriadMonitor _myriadStateToString:]
- -[AFMyriadMonitor _registerForMyriadEvents]
- -[AFMyriadMonitor _resultSeenWithValue:]
- -[AFMyriadMonitor _setDecisionIsPending]
- -[AFMyriadMonitor dealloc]
- -[AFMyriadMonitor dequeueBlocksWaitingForMyriadDecision]
- -[AFMyriadMonitor didWin]
- -[AFMyriadMonitor ignoreMyriadEvents:]
- -[AFMyriadMonitor init]
- -[AFMyriadMonitor isMonitoring]
- -[AFMyriadMonitor notifyObserver:didChangeStateFrom:to:]
- -[AFMyriadMonitor notifyObserver:didReceiveNotificationWithToken:]
- -[AFMyriadMonitor startMonitoringWithTimeoutInterval:]
- -[AFMyriadMonitor startMonitoringWithTimeoutInterval:instanceContext:]
- -[AFMyriadMonitor stopMonitoring]
- -[AFMyriadMonitor waitForMyriadDecisionForReason:withCompletion:]
- -[AFMyriadMonitor waitForMyriadDecisionWithCompletion:]
- -[AFMyriadPerceptualAudioHash .cxx_destruct]
- -[AFMyriadPerceptualAudioHash _descriptionWithIndent:]
- -[AFMyriadPerceptualAudioHash copyWithZone:]
- -[AFMyriadPerceptualAudioHash data]
- -[AFMyriadPerceptualAudioHash description]
- -[AFMyriadPerceptualAudioHash encodeWithCoder:]
- -[AFMyriadPerceptualAudioHash hash]
- -[AFMyriadPerceptualAudioHash initWithBuilder:]
- -[AFMyriadPerceptualAudioHash initWithCoder:]
- -[AFMyriadPerceptualAudioHash initWithData:]
- -[AFMyriadPerceptualAudioHash init]
- -[AFMyriadPerceptualAudioHash isEqual:]
- -[AFMyriadPerceptualAudioHash(AFMyriadPerceptualAudioHashMutability) mutatedCopyWithMutator:]
- -[AFMyriadPreferences .cxx_destruct]
- -[AFMyriadPreferences BLEActivityEnabled]
- -[AFMyriadPreferences constantGoodnessScore]
- -[AFMyriadPreferences coordinationEnabledForAccessoryLogging]
- -[AFMyriadPreferences coordinationEnabled]
- -[AFMyriadPreferences deviceAdjust]
- -[AFMyriadPreferences deviceClass]
- -[AFMyriadPreferences deviceDelay]
- -[AFMyriadPreferences deviceGroup]
- -[AFMyriadPreferences deviceSlowDown]
- -[AFMyriadPreferences deviceTrumpDelay]
- -[AFMyriadPreferences enableCoordination:]
- -[AFMyriadPreferences ignoreAdjustedBoost]
- -[AFMyriadPreferences ignorePlatformBias]
- -[AFMyriadPreferences initWithDeviceInstanceContext:preferences:]
- -[AFMyriadPreferences maxNoOperationDelay]
- -[AFMyriadPreferences myriadServerHasProvisioned]
- -[AFMyriadPreferences setConstantGoodnessScore:]
- -[AFMyriadPreferences setDeviceAdjust:]
- -[AFMyriadPreferences setDeviceClass:]
- -[AFMyriadPreferences setDeviceDelay:]
- -[AFMyriadPreferences setDeviceGroup:completion:]
- -[AFMyriadPreferences setDeviceSlowDown:]
- -[AFMyriadPreferences setDeviceTrumpDelay:]
- -[AFMyriadPreferences setIgnoreAdjustedBoost:]
- -[AFMyriadPreferences setIgnorePlatformBias:]
- -[AFMyriadPreferences setMaxNoOperationDelay:]
- -[AFMyriadPreferences setTestDeviceDelay:]
- -[AFMyriadPreferences setVoiceTriggerEndtimeDelayThreshold:]
- -[AFMyriadPreferences testDeviceDelay]
- -[AFMyriadPreferences voiceTriggerEndtimeDelayThreshold]
- -[AFMyriadRecord .cxx_destruct]
- -[AFMyriadRecord adjustByMultiplier:adding:]
- -[AFMyriadRecord advertisementDataIsDirty]
- -[AFMyriadRecord advertisementData]
- -[AFMyriadRecord asAdvertisementData]
- -[AFMyriadRecord bump]
- -[AFMyriadRecord copyWithZone:]
- -[AFMyriadRecord description]
- -[AFMyriadRecord deviceClass]
- -[AFMyriadRecord deviceGroup]
- -[AFMyriadRecord deviceID]
- -[AFMyriadRecord generateRandomConfidence]
- -[AFMyriadRecord generateTiebreaker]
- -[AFMyriadRecord goodness]
- -[AFMyriadRecord hasEqualAdvertisementData:]
- -[AFMyriadRecord hasEqualAdvertismentData:]
- -[AFMyriadRecord hash]
- -[AFMyriadRecord initWithAudioData:]
- -[AFMyriadRecord initWithDeviceID:data:]
- -[AFMyriadRecord init]
- -[AFMyriadRecord isAContinuation]
- -[AFMyriadRecord isALateSupressionTrumpFor:]
- -[AFMyriadRecord isATrump]
- -[AFMyriadRecord isAnEmergencyHandled]
- -[AFMyriadRecord isAnEmergency]
- -[AFMyriadRecord isCarplayTrump]
- -[AFMyriadRecord isCollectedFromContextCollector]
- -[AFMyriadRecord isEqual:]
- -[AFMyriadRecord isInEarTrump]
- -[AFMyriadRecord isMe]
- -[AFMyriadRecord isSane]
- -[AFMyriadRecord isSlowdown]
- -[AFMyriadRecord pHash]
- -[AFMyriadRecord productType]
- -[AFMyriadRecord rawAudioGoodnessScore]
- -[AFMyriadRecord setAdvertisementData:]
- -[AFMyriadRecord setAdvertisementDataIsDirty:]
- -[AFMyriadRecord setBump:]
- -[AFMyriadRecord setDeviceClass:]
- -[AFMyriadRecord setDeviceGroup:]
- -[AFMyriadRecord setDeviceID:]
- -[AFMyriadRecord setGoodness:]
- -[AFMyriadRecord setIsCollectedFromContextCollector:]
- -[AFMyriadRecord setIsMe:]
- -[AFMyriadRecord setPHash:]
- -[AFMyriadRecord setProductType:]
- -[AFMyriadRecord setRawAudioGoodnessScore:]
- -[AFMyriadRecord setRawAudioGoodnessScore:withBump:]
- -[AFMyriadRecord setTieBreaker:]
- -[AFMyriadRecord setUserConfidence:]
- -[AFMyriadRecord slowdownDelay]
- -[AFMyriadRecord tieBreaker]
- -[AFMyriadRecord userConfidence]
- -[AFMyriadSession .cxx_destruct]
- -[AFMyriadSession _descriptionWithIndent:]
- -[AFMyriadSession copyWithZone:]
- -[AFMyriadSession currentElectionAdvertisementData]
- -[AFMyriadSession currentElectionAdvertisementId]
- -[AFMyriadSession description]
- -[AFMyriadSession electionAdvertisementDataByIds]
- -[AFMyriadSession encodeWithCoder:]
- -[AFMyriadSession generation]
- -[AFMyriadSession hash]
- -[AFMyriadSession initWithBuilder:]
- -[AFMyriadSession initWithCoder:]
- -[AFMyriadSession initWithGeneration:sessionId:currentElectionAdvertisementId:currentElectionAdvertisementData:electionAdvertisementDataByIds:]
- -[AFMyriadSession init]
- -[AFMyriadSession isEqual:]
- -[AFMyriadSession sessionId]
- -[AFMyriadSession(AFMyriadSessionMutability) mutatedCopyWithMutator:]
- -[AFSiriAvailability initWithIsAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:]
- -[AFSiriAvailability initWithIsAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:]
- -[AFSpeechRequestOptions myriadContext]
- -[AFSpeechRequestOptions setMyriadContext:]
- -[_AFMyriadAdvertisementContextMutation .cxx_destruct]
- -[_AFMyriadAdvertisementContextMutation getContextData]
- -[_AFMyriadAdvertisementContextMutation getContextFetchDelay]
- -[_AFMyriadAdvertisementContextMutation getGeneration]
- -[_AFMyriadAdvertisementContextMutation initWithBase:]
- -[_AFMyriadAdvertisementContextMutation isDirty]
- -[_AFMyriadAdvertisementContextMutation setContextData:]
- -[_AFMyriadAdvertisementContextMutation setContextFetchDelay:]
- -[_AFMyriadAdvertisementContextMutation setGeneration:]
- -[_AFMyriadContextMutation .cxx_destruct]
- -[_AFMyriadContextMutation getActivationExpirationTime]
- -[_AFMyriadContextMutation getActivationSource]
- -[_AFMyriadContextMutation getOverrideState]
- -[_AFMyriadContextMutation getPerceptualAudioHash]
- -[_AFMyriadContextMutation getTimestamp]
- -[_AFMyriadContextMutation initWithBase:]
- -[_AFMyriadContextMutation isDirty]
- -[_AFMyriadContextMutation setActivationExpirationTime:]
- -[_AFMyriadContextMutation setActivationSource:]
- -[_AFMyriadContextMutation setOverrideState:]
- -[_AFMyriadContextMutation setPerceptualAudioHash:]
- -[_AFMyriadContextMutation setTimestamp:]
- -[_AFMyriadGoodnessScoreOverrideStateMutation .cxx_destruct]
- -[_AFMyriadGoodnessScoreOverrideStateMutation getOverrideOption]
- -[_AFMyriadGoodnessScoreOverrideStateMutation getReason]
- -[_AFMyriadGoodnessScoreOverrideStateMutation initWithBase:]
- -[_AFMyriadGoodnessScoreOverrideStateMutation isDirty]
- -[_AFMyriadGoodnessScoreOverrideStateMutation setOverrideOption:]
- -[_AFMyriadGoodnessScoreOverrideStateMutation setReason:]
- -[_AFMyriadPerceptualAudioHashMutation .cxx_destruct]
- -[_AFMyriadPerceptualAudioHashMutation getData]
- -[_AFMyriadPerceptualAudioHashMutation initWithBase:]
- -[_AFMyriadPerceptualAudioHashMutation isDirty]
- -[_AFMyriadPerceptualAudioHashMutation setData:]
- -[_AFMyriadSessionMutation .cxx_destruct]
- -[_AFMyriadSessionMutation getCurrentElectionAdvertisementData]
- -[_AFMyriadSessionMutation getCurrentElectionAdvertisementId]
- -[_AFMyriadSessionMutation getElectionAdvertisementDataByIds]
- -[_AFMyriadSessionMutation getGeneration]
- -[_AFMyriadSessionMutation getSessionId]
- -[_AFMyriadSessionMutation initWithBase:]
- -[_AFMyriadSessionMutation isDirty]
- -[_AFMyriadSessionMutation setCurrentElectionAdvertisementData:]
- -[_AFMyriadSessionMutation setCurrentElectionAdvertisementId:]
- -[_AFMyriadSessionMutation setElectionAdvertisementDataByIds:]
- -[_AFMyriadSessionMutation setGeneration:]
- -[_AFMyriadSessionMutation setSessionId:]
- GCC_except_table10070
- GCC_except_table10075
- GCC_except_table10139
- GCC_except_table10254
- GCC_except_table10646
- GCC_except_table10733
- GCC_except_table10821
- GCC_except_table10861
- GCC_except_table10892
- GCC_except_table10897
- GCC_except_table10898
- GCC_except_table10902
- GCC_except_table1100
- GCC_except_table11262
- GCC_except_table11291
- GCC_except_table11388
- GCC_except_table11392
- GCC_except_table11396
- GCC_except_table11425
- GCC_except_table1166
- GCC_except_table1172
- GCC_except_table11813
- GCC_except_table11815
- GCC_except_table11818
- GCC_except_table11827
- GCC_except_table11887
- GCC_except_table11908
- GCC_except_table11933
- GCC_except_table11939
- GCC_except_table12080
- GCC_except_table12084
- GCC_except_table12086
- GCC_except_table12089
- GCC_except_table12095
- GCC_except_table12099
- GCC_except_table12105
- GCC_except_table12309
- GCC_except_table12657
- GCC_except_table12791
- GCC_except_table12794
- GCC_except_table12796
- GCC_except_table1298
- GCC_except_table1300
- GCC_except_table1514
- GCC_except_table1551
- GCC_except_table1557
- GCC_except_table1561
- GCC_except_table1581
- GCC_except_table1587
- GCC_except_table1590
- GCC_except_table1956
- GCC_except_table2091
- GCC_except_table2298
- GCC_except_table230
- GCC_except_table2311
- GCC_except_table2315
- GCC_except_table2327
- GCC_except_table2331
- GCC_except_table236
- GCC_except_table242
- GCC_except_table2436
- GCC_except_table2438
- GCC_except_table2510
- GCC_except_table2554
- GCC_except_table256
- GCC_except_table2916
- GCC_except_table2923
- GCC_except_table2927
- GCC_except_table2929
- GCC_except_table2974
- GCC_except_table2976
- GCC_except_table2982
- GCC_except_table2988
- GCC_except_table2992
- GCC_except_table2996
- GCC_except_table2999
- GCC_except_table3001
- GCC_except_table3006
- GCC_except_table3008
- GCC_except_table3013
- GCC_except_table3025
- GCC_except_table3028
- GCC_except_table3042
- GCC_except_table3044
- GCC_except_table3046
- GCC_except_table3048
- GCC_except_table3050
- GCC_except_table3052
- GCC_except_table3054
- GCC_except_table3097
- GCC_except_table3123
- GCC_except_table3180
- GCC_except_table3213
- GCC_except_table350
- GCC_except_table3586
- GCC_except_table368
- GCC_except_table372
- GCC_except_table3843
- GCC_except_table4040
- GCC_except_table4048
- GCC_except_table4106
- GCC_except_table4482
- GCC_except_table4486
- GCC_except_table4531
- GCC_except_table4537
- GCC_except_table4568
- GCC_except_table4776
- GCC_except_table4885
- GCC_except_table4896
- GCC_except_table4929
- GCC_except_table4932
- GCC_except_table5009
- GCC_except_table5013
- GCC_except_table5023
- GCC_except_table5034
- GCC_except_table5047
- GCC_except_table5132
- GCC_except_table5134
- GCC_except_table5158
- GCC_except_table5273
- GCC_except_table5336
- GCC_except_table5339
- GCC_except_table5343
- GCC_except_table5360
- GCC_except_table5374
- GCC_except_table5448
- GCC_except_table5506
- GCC_except_table5532
- GCC_except_table573
- GCC_except_table5803
- GCC_except_table5944
- GCC_except_table5957
- GCC_except_table6000
- GCC_except_table6094
- GCC_except_table623
- GCC_except_table6289
- GCC_except_table6426
- GCC_except_table6438
- GCC_except_table6445
- GCC_except_table6446
- GCC_except_table6449
- GCC_except_table6455
- GCC_except_table6543
- GCC_except_table6545
- GCC_except_table6547
- GCC_except_table6565
- GCC_except_table6571
- GCC_except_table6614
- GCC_except_table6626
- GCC_except_table6799
- GCC_except_table6885
- GCC_except_table6939
- GCC_except_table7202
- GCC_except_table7205
- GCC_except_table7206
- GCC_except_table7403
- GCC_except_table7462
- GCC_except_table7730
- GCC_except_table7733
- GCC_except_table7745
- GCC_except_table7746
- GCC_except_table7759
- GCC_except_table7761
- GCC_except_table7767
- GCC_except_table7805
- GCC_except_table7811
- GCC_except_table7817
- GCC_except_table7885
- GCC_except_table7887
- GCC_except_table7922
- GCC_except_table7925
- GCC_except_table8064
- GCC_except_table8160
- GCC_except_table8162
- GCC_except_table8164
- GCC_except_table8166
- GCC_except_table8180
- GCC_except_table8186
- GCC_except_table824
- GCC_except_table827
- GCC_except_table8309
- GCC_except_table8316
- GCC_except_table834
- GCC_except_table8700
- GCC_except_table8707
- GCC_except_table8723
- GCC_except_table8814
- GCC_except_table8823
- GCC_except_table8846
- GCC_except_table8876
- GCC_except_table8931
- GCC_except_table8955
- GCC_except_table9332
- GCC_except_table9337
- GCC_except_table9340
- GCC_except_table9343
- GCC_except_table9346
- GCC_except_table9349
- GCC_except_table9352
- GCC_except_table9355
- GCC_except_table9531
- GCC_except_table9534
- GCC_except_table9595
- GCC_except_table9603
- GCC_except_table9608
- GCC_except_table9621
- GCC_except_table965
- GCC_except_table9781
- GCC_except_table9881
- _AFElectionBeginNotifyStateObserver
- _AFElectionBeginNotifyStatePublisher
- _AFElectionDecisionRequestNotifyStateObserver
- _AFElectionLossNotifyStateObserver
- _AFElectionLossNotifyStatePublisher
- _AFElectionRepostWinDecisionNotifyStateObserver
- _AFElectionRepostWinDecisionNotifyStatePublisher
- _AFElectionWinNotifyStateObserver
- _AFElectionWinNotifyStatePublisher
- _AFGetOSEligibilitySiriMode.osEligibilitySiriMode
- _AFMyriadAdvertisementContextKey
- _AFMyriadAdvertisementRecordTypeGetFromName
- _AFMyriadAdvertisementRecordTypeGetFromName.map
- _AFMyriadAdvertisementRecordTypeGetFromName.onceToken
- _AFMyriadAdvertisementRecordTypeGetIsValid
- _AFMyriadAdvertisementRecordTypeGetIsValidAndSpecified
- _AFMyriadAdvertisementRecordTypeGetName
- _AFMyriadContextKey
- _AFMyriadDecisionGetWaitTime
- _AFMyriadDecisionWaitTime
- _AFMyriadForceNoActivityNotifyStateObserver
- _AFMyriadForceNoActivityNotifyStatePublisher
- _AFMyriadGoodnessComputeExponentialBoost
- _AFMyriadGoodnessScoreBumpReasonGetFromName
- _AFMyriadGoodnessScoreBumpReasonGetFromName.map
- _AFMyriadGoodnessScoreBumpReasonGetFromName.onceToken
- _AFMyriadGoodnessScoreBumpReasonGetIsValid
- _AFMyriadGoodnessScoreBumpReasonGetIsValidAndSpecified
- _AFMyriadGoodnessScoreBumpReasonGetName
- _AFMyriadGoodnessScoreOverrideOptionGetFromName
- _AFMyriadGoodnessScoreOverrideOptionGetFromName.map
- _AFMyriadGoodnessScoreOverrideOptionGetFromName.onceToken
- _AFMyriadGoodnessScoreOverrideOptionGetIsValid
- _AFMyriadGoodnessScoreOverrideOptionGetIsValidAndSpecified
- _AFMyriadGoodnessScoreOverrideOptionGetName
- _AFMyriadGoodnessScoreOverrideStateKey
- _AFMyriadMaxNoOperationAccessoryMessageCount
- _AFMyriadMaxNoOperationDelay
- _AFMyriadMaxNoOperationDelay.noopDelay
- _AFMyriadMaxNoOperationDelay.onceToken
- _AFMyriadMonitorDecisionGetWaitTime
- _AFMyriadPerceptualAudioHashKey
- _AFMyriadPreferencesChangedNotifyStateObserver
- _AFMyriadPreferencesChangedNotifyStatePublisher
- _AFMyriadPreheatGetWaitTime
- _AFMyriadReadDefaultsNotificationName
- _AFMyriadSessionKey
- _AF_MYRIAD_FORCE_NO_ACTIVITY_NOTIFICATION
- _MCFeatureSiriFeature1Spring2026Allowed
- _MGGetProductType
- _NSHomeDirectory
- _OBJC_CLASS_$_AFMyriadAccessoryMessage
- _OBJC_CLASS_$_AFMyriadAccessoryMetricMessage
- _OBJC_CLASS_$_AFMyriadAdvertisementContext
- _OBJC_CLASS_$_AFMyriadAdvertisementContextManager
- _OBJC_CLASS_$_AFMyriadAdvertisementContextRecord
- _OBJC_CLASS_$_AFMyriadContext
- _OBJC_CLASS_$_AFMyriadCoordinator
- _OBJC_CLASS_$_AFMyriadEmergencyCallPunchout
- _OBJC_CLASS_$_AFMyriadGoodnessScoreContext
- _OBJC_CLASS_$_AFMyriadGoodnessScoreEvaluator
- _OBJC_CLASS_$_AFMyriadGoodnessScoreOverrideContext
- _OBJC_CLASS_$_AFMyriadGoodnessScoreOverrideState
- _OBJC_CLASS_$_AFMyriadInstrumentation
- _OBJC_CLASS_$_AFMyriadMetrics
- _OBJC_CLASS_$_AFMyriadMetricsAdditionalContext
- _OBJC_CLASS_$_AFMyriadMonitor
- _OBJC_CLASS_$_AFMyriadPerceptualAudioHash
- _OBJC_CLASS_$_AFMyriadPreferences
- _OBJC_CLASS_$_AFMyriadRecord
- _OBJC_CLASS_$_AFMyriadSession
- _OBJC_CLASS_$_CDASchemaCDAAdvertisementData
- _OBJC_CLASS_$_CDASchemaCDAClientEvent
- _OBJC_CLASS_$_CDASchemaCDAClientEventMetadata
- _OBJC_CLASS_$_CDASchemaCDADebugElectionDecisionMade
- _OBJC_CLASS_$_CDASchemaCDADeviceAdvertisingEndContext
- _OBJC_CLASS_$_CDASchemaCDADeviceAdvertisingStartContext
- _OBJC_CLASS_$_CDASchemaCDADeviceStateActivityEnded
- _OBJC_CLASS_$_CDASchemaCDADeviceStateActivityStarted
- _OBJC_CLASS_$_CDASchemaCDADeviceStateContext
- _OBJC_CLASS_$_CDASchemaCDAElectionAdvertisingEndEnded
- _OBJC_CLASS_$_CDASchemaCDAElectionAdvertisingEndStarted
- _OBJC_CLASS_$_CDASchemaCDAElectionAdvertisingStartEnded
- _OBJC_CLASS_$_CDASchemaCDAElectionAdvertisingStartStarted
- _OBJC_CLASS_$_CDASchemaCDAElectionDecisionMade
- _OBJC_CLASS_$_CDASchemaCDAElectionTimerEnded
- _OBJC_CLASS_$_CDASchemaCDAParticipant
- _OBJC_CLASS_$_CDASchemaCDAScoreBoosters
- _OBJC_CLASS_$__AFMyriadAdvertisementContextMutation
- _OBJC_CLASS_$__AFMyriadContextMutation
- _OBJC_CLASS_$__AFMyriadGoodnessScoreOverrideStateMutation
- _OBJC_CLASS_$__AFMyriadPerceptualAudioHashMutation
- _OBJC_CLASS_$__AFMyriadSessionMutation
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._accessoryId
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._ack
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._audioHash
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._deviceClass
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._deviceGroup
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._electionDecision
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._emergencyHandled
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._goodnessScore
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._isSane
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._message
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._productType
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._requestType
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._serializedProtocol
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._session
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._tieBreaker
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._userConfidenceScore
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._version
- _OBJC_IVAR_$_AFMyriadAccessoryMessage._voiceTriggerEndTime
- _OBJC_IVAR_$_AFMyriadAccessoryMetricMessage._metric
- _OBJC_IVAR_$_AFMyriadAdvertisementContext._contextData
- _OBJC_IVAR_$_AFMyriadAdvertisementContext._contextFetchDelay
- _OBJC_IVAR_$_AFMyriadAdvertisementContext._generation
- _OBJC_IVAR_$_AFMyriadAdvertisementContextManager._queue
- _OBJC_IVAR_$_AFMyriadAdvertisementContextManager._settingsConnection
- _OBJC_IVAR_$_AFMyriadAdvertisementContextRecord._advertisementContextVersion
- _OBJC_IVAR_$_AFMyriadAdvertisementContextRecord._advertisementDispatchTime
- _OBJC_IVAR_$_AFMyriadAdvertisementContextRecord._advertisementPayload
- _OBJC_IVAR_$_AFMyriadAdvertisementContextRecord._advertisementRecordType
- _OBJC_IVAR_$_AFMyriadAdvertisementContextRecord._deviceID
- _OBJC_IVAR_$_AFMyriadAdvertisementContextRecord._voiceTriggerEndTime
- _OBJC_IVAR_$_AFMyriadContext._activationExpirationTime
- _OBJC_IVAR_$_AFMyriadContext._activationSource
- _OBJC_IVAR_$_AFMyriadContext._overrideState
- _OBJC_IVAR_$_AFMyriadContext._perceptualAudioHash
- _OBJC_IVAR_$_AFMyriadContext._timestamp
- _OBJC_IVAR_$_AFMyriadCoordinator._BLEActivityEnabled
- _OBJC_IVAR_$_AFMyriadCoordinator._BTLEReady
- _OBJC_IVAR_$_AFMyriadCoordinator._advContextManager
- _OBJC_IVAR_$_AFMyriadCoordinator._advTiming
- _OBJC_IVAR_$_AFMyriadCoordinator._advertInterval
- _OBJC_IVAR_$_AFMyriadCoordinator._callPunchout
- _OBJC_IVAR_$_AFMyriadCoordinator._center
- _OBJC_IVAR_$_AFMyriadCoordinator._clientDoneRespondingToSlowdown
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsDeciding
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsDirectActivating
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsInEarActivation
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsListeningAfterRecentWin
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsRespondingToSlowdown
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsWatchActivation
- _OBJC_IVAR_$_AFMyriadCoordinator._clientIsWatchTrumpPromote
- _OBJC_IVAR_$_AFMyriadCoordinator._clientLostDueToTrumping
- _OBJC_IVAR_$_AFMyriadCoordinator._clientRecentlyLostElection
- _OBJC_IVAR_$_AFMyriadCoordinator._clientRespondingToCarPlay
- _OBJC_IVAR_$_AFMyriadCoordinator._constantGoodness
- _OBJC_IVAR_$_AFMyriadCoordinator._contextRecord
- _OBJC_IVAR_$_AFMyriadCoordinator._coordinationEnabled
- _OBJC_IVAR_$_AFMyriadCoordinator._currentMyriadContext
- _OBJC_IVAR_$_AFMyriadCoordinator._currentRequestId
- _OBJC_IVAR_$_AFMyriadCoordinator._dateFormat
- _OBJC_IVAR_$_AFMyriadCoordinator._delayTarget
- _OBJC_IVAR_$_AFMyriadCoordinator._delegate
- _OBJC_IVAR_$_AFMyriadCoordinator._designatedSelfID
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceAdjust
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceClass
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceClassName
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceDelay
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceGroup
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceInEarDelay
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceInEarInterval
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceTrumpDelay
- _OBJC_IVAR_$_AFMyriadCoordinator._deviceVTEndtimeDistanceThreshold
- _OBJC_IVAR_$_AFMyriadCoordinator._ducking
- _OBJC_IVAR_$_AFMyriadCoordinator._electionBeginPublisher
- _OBJC_IVAR_$_AFMyriadCoordinator._electionLossPublisher
- _OBJC_IVAR_$_AFMyriadCoordinator._electionPublisherState
- _OBJC_IVAR_$_AFMyriadCoordinator._electionRepostWinDecisionPublisher
- _OBJC_IVAR_$_AFMyriadCoordinator._electionWinPublisher
- _OBJC_IVAR_$_AFMyriadCoordinator._eventToken
- _OBJC_IVAR_$_AFMyriadCoordinator._goodnessScoreEvaluator
- _OBJC_IVAR_$_AFMyriadCoordinator._heySiriBTLE
- _OBJC_IVAR_$_AFMyriadCoordinator._heySiriBTLEState
- _OBJC_IVAR_$_AFMyriadCoordinator._ignoreInTaskTimer
- _OBJC_IVAR_$_AFMyriadCoordinator._inSetupMode
- _OBJC_IVAR_$_AFMyriadCoordinator._inTask
- _OBJC_IVAR_$_AFMyriadCoordinator._incomingAdjustment
- _OBJC_IVAR_$_AFMyriadCoordinator._incomingTrumps
- _OBJC_IVAR_$_AFMyriadCoordinator._lastDecision
- _OBJC_IVAR_$_AFMyriadCoordinator._lastDecisionTime
- _OBJC_IVAR_$_AFMyriadCoordinator._lastEmergencyAttempt
- _OBJC_IVAR_$_AFMyriadCoordinator._lastPHash
- _OBJC_IVAR_$_AFMyriadCoordinator._lastWonBySmallAmountDate
- _OBJC_IVAR_$_AFMyriadCoordinator._latestRecordReceivedTime
- _OBJC_IVAR_$_AFMyriadCoordinator._listenTimerIsRunning
- _OBJC_IVAR_$_AFMyriadCoordinator._maxSlowdownRecord
- _OBJC_IVAR_$_AFMyriadCoordinator._multipleContinuations
- _OBJC_IVAR_$_AFMyriadCoordinator._myriadAdvertisementContextQueue
- _OBJC_IVAR_$_AFMyriadCoordinator._myriadInstrumentation
- _OBJC_IVAR_$_AFMyriadCoordinator._myriadSession
- _OBJC_IVAR_$_AFMyriadCoordinator._myriadState
- _OBJC_IVAR_$_AFMyriadCoordinator._myriadStateMachineForceNoActivityObserver
- _OBJC_IVAR_$_AFMyriadCoordinator._myriadWorkQueue
- _OBJC_IVAR_$_AFMyriadCoordinator._nDeltaTs
- _OBJC_IVAR_$_AFMyriadCoordinator._nTimesContinued
- _OBJC_IVAR_$_AFMyriadCoordinator._nTimesExtended
- _OBJC_IVAR_$_AFMyriadCoordinator._nextState
- _OBJC_IVAR_$_AFMyriadCoordinator._overallTimeout
- _OBJC_IVAR_$_AFMyriadCoordinator._overrideMyriadRecord
- _OBJC_IVAR_$_AFMyriadCoordinator._powerAssertionManager
- _OBJC_IVAR_$_AFMyriadCoordinator._preferences
- _OBJC_IVAR_$_AFMyriadCoordinator._preferencesChangedNotification
- _OBJC_IVAR_$_AFMyriadCoordinator._previousAdvertisedData
- _OBJC_IVAR_$_AFMyriadCoordinator._previousState
- _OBJC_IVAR_$_AFMyriadCoordinator._previousTrumps
- _OBJC_IVAR_$_AFMyriadCoordinator._productType
- _OBJC_IVAR_$_AFMyriadCoordinator._productTypeName
- _OBJC_IVAR_$_AFMyriadCoordinator._recordType
- _OBJC_IVAR_$_AFMyriadCoordinator._replies
- _OBJC_IVAR_$_AFMyriadCoordinator._repliesBeforeDecision
- _OBJC_IVAR_$_AFMyriadCoordinator._replyCounts
- _OBJC_IVAR_$_AFMyriadCoordinator._sfDiagnosticsTimer
- _OBJC_IVAR_$_AFMyriadCoordinator._sfdiagnostics
- _OBJC_IVAR_$_AFMyriadCoordinator._slowdownMsecs
- _OBJC_IVAR_$_AFMyriadCoordinator._stateMachineEncounteredError
- _OBJC_IVAR_$_AFMyriadCoordinator._suppressLateTrigger
- _OBJC_IVAR_$_AFMyriadCoordinator._testInducedSlowdownMsecs
- _OBJC_IVAR_$_AFMyriadCoordinator._timer
- _OBJC_IVAR_$_AFMyriadCoordinator._timerLabel
- _OBJC_IVAR_$_AFMyriadCoordinator._timerSource
- _OBJC_IVAR_$_AFMyriadCoordinator._triggerRecord
- _OBJC_IVAR_$_AFMyriadCoordinator._triggerTime
- _OBJC_IVAR_$_AFMyriadCoordinator._voiceTriggerTime
- _OBJC_IVAR_$_AFMyriadCoordinator._waitForWiproxReadinessToScan
- _OBJC_IVAR_$_AFMyriadCoordinator._wasEmergency
- _OBJC_IVAR_$_AFMyriadCoordinator._wiproxReadinessTimer
- _OBJC_IVAR_$_AFMyriadEmergencyCallPunchout._myriadEmergencyCallingQueue
- _OBJC_IVAR_$_AFMyriadGoodnessScoreContext._mediaPlaybackInterruptedTime
- _OBJC_IVAR_$_AFMyriadGoodnessScoreContext._overriddenContext
- _OBJC_IVAR_$_AFMyriadGoodnessScoreContext._reasons
- _OBJC_IVAR_$_AFMyriadGoodnessScoreContext._recentlyWonBySmallAmount
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._deviceInstanceContext
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._endpointModelName
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._evaluateForAudioAccessory
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._isExponentialBoostDefined
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._isRecentSiriBoostTrialEnabled
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._isSpeakerEndpoint
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._lastActivationTime
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._mediaPlaybackBoost
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._myriadInstrumentation
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._myriadPlatformBias
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._platformBiasAcquisitionState
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._pref
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._queue
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._recentSiriFirstDegreeCoefficient
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._recentSiriIntercept
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._recentSiriSecondDegreeCoefficient
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._scoreEvaluationLock
- _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._settingsConnection
- _OBJC_IVAR_$_AFMyriadGoodnessScoreOverrideContext._overriddenAdjustedScore
- _OBJC_IVAR_$_AFMyriadGoodnessScoreOverrideContext._overrideContext
- _OBJC_IVAR_$_AFMyriadGoodnessScoreOverrideState._overrideOption
- _OBJC_IVAR_$_AFMyriadGoodnessScoreOverrideState._reason
- _OBJC_IVAR_$_AFMyriadInstrumentation._currentBoost
- _OBJC_IVAR_$_AFMyriadInstrumentation._previousBoosts
- _OBJC_IVAR_$_AFMyriadInstrumentation._queue
- _OBJC_IVAR_$_AFMyriadMetricsAdditionalContext._deviceClass
- _OBJC_IVAR_$_AFMyriadMetricsAdditionalContext._deviceProductType
- _OBJC_IVAR_$_AFMyriadMetricsAdditionalContext._goodnessScore
- _OBJC_IVAR_$_AFMyriadMetricsAdditionalContext._rawGoodnessScore
- _OBJC_IVAR_$_AFMyriadMonitor._beginObserver
- _OBJC_IVAR_$_AFMyriadMonitor._completions
- _OBJC_IVAR_$_AFMyriadMonitor._fetchRepostedMyriadDecisionTimer
- _OBJC_IVAR_$_AFMyriadMonitor._ignoreMyriadEvents
- _OBJC_IVAR_$_AFMyriadMonitor._ignoreRepostMyriadNotification
- _OBJC_IVAR_$_AFMyriadMonitor._instanceContext
- _OBJC_IVAR_$_AFMyriadMonitor._isMonitoring
- _OBJC_IVAR_$_AFMyriadMonitor._isRegisteredForMyriadEventNotification
- _OBJC_IVAR_$_AFMyriadMonitor._lostObserver
- _OBJC_IVAR_$_AFMyriadMonitor._myriadEventMonitorTimeout
- _OBJC_IVAR_$_AFMyriadMonitor._myriadMonitorQueue
- _OBJC_IVAR_$_AFMyriadMonitor._repostedWonObserver
- _OBJC_IVAR_$_AFMyriadMonitor._state
- _OBJC_IVAR_$_AFMyriadMonitor._timer
- _OBJC_IVAR_$_AFMyriadMonitor._wonObserver
- _OBJC_IVAR_$_AFMyriadPerceptualAudioHash._data
- _OBJC_IVAR_$_AFMyriadPreferences._instanceContext
- _OBJC_IVAR_$_AFMyriadPreferences._pref
- _OBJC_IVAR_$_AFMyriadRecord._advertisementData
- _OBJC_IVAR_$_AFMyriadRecord._advertisementDataIsDirty
- _OBJC_IVAR_$_AFMyriadRecord._bump
- _OBJC_IVAR_$_AFMyriadRecord._deviceClass
- _OBJC_IVAR_$_AFMyriadRecord._deviceGroup
- _OBJC_IVAR_$_AFMyriadRecord._deviceID
- _OBJC_IVAR_$_AFMyriadRecord._goodness
- _OBJC_IVAR_$_AFMyriadRecord._isCollectedFromContextCollector
- _OBJC_IVAR_$_AFMyriadRecord._isMe
- _OBJC_IVAR_$_AFMyriadRecord._pHash
- _OBJC_IVAR_$_AFMyriadRecord._productType
- _OBJC_IVAR_$_AFMyriadRecord._rawAudioGoodnessScore
- _OBJC_IVAR_$_AFMyriadRecord._tieBreaker
- _OBJC_IVAR_$_AFMyriadRecord._userConfidence
- _OBJC_IVAR_$_AFMyriadSession._currentElectionAdvertisementData
- _OBJC_IVAR_$_AFMyriadSession._currentElectionAdvertisementId
- _OBJC_IVAR_$_AFMyriadSession._electionAdvertisementDataByIds
- _OBJC_IVAR_$_AFMyriadSession._generation
- _OBJC_IVAR_$_AFMyriadSession._sessionId
- _OBJC_IVAR_$_AFSpeechRequestOptions._myriadContext
- _OBJC_IVAR_$__AFMyriadAdvertisementContextMutation._base
- _OBJC_IVAR_$__AFMyriadAdvertisementContextMutation._contextData
- _OBJC_IVAR_$__AFMyriadAdvertisementContextMutation._contextFetchDelay
- _OBJC_IVAR_$__AFMyriadAdvertisementContextMutation._generation
- _OBJC_IVAR_$__AFMyriadAdvertisementContextMutation._mutationFlags
- _OBJC_IVAR_$__AFMyriadContextMutation._activationExpirationTime
- _OBJC_IVAR_$__AFMyriadContextMutation._activationSource
- _OBJC_IVAR_$__AFMyriadContextMutation._base
- _OBJC_IVAR_$__AFMyriadContextMutation._mutationFlags
- _OBJC_IVAR_$__AFMyriadContextMutation._overrideState
- _OBJC_IVAR_$__AFMyriadContextMutation._perceptualAudioHash
- _OBJC_IVAR_$__AFMyriadContextMutation._timestamp
- _OBJC_IVAR_$__AFMyriadGoodnessScoreOverrideStateMutation._base
- _OBJC_IVAR_$__AFMyriadGoodnessScoreOverrideStateMutation._mutationFlags
- _OBJC_IVAR_$__AFMyriadGoodnessScoreOverrideStateMutation._overrideOption
- _OBJC_IVAR_$__AFMyriadGoodnessScoreOverrideStateMutation._reason
- _OBJC_IVAR_$__AFMyriadPerceptualAudioHashMutation._base
- _OBJC_IVAR_$__AFMyriadPerceptualAudioHashMutation._data
- _OBJC_IVAR_$__AFMyriadPerceptualAudioHashMutation._mutationFlags
- _OBJC_IVAR_$__AFMyriadSessionMutation._base
- _OBJC_IVAR_$__AFMyriadSessionMutation._currentElectionAdvertisementData
- _OBJC_IVAR_$__AFMyriadSessionMutation._currentElectionAdvertisementId
- _OBJC_IVAR_$__AFMyriadSessionMutation._electionAdvertisementDataByIds
- _OBJC_IVAR_$__AFMyriadSessionMutation._generation
- _OBJC_IVAR_$__AFMyriadSessionMutation._mutationFlags
- _OBJC_IVAR_$__AFMyriadSessionMutation._sessionId
- _OBJC_METACLASS_$_AFMyriadAccessoryMessage
- _OBJC_METACLASS_$_AFMyriadAccessoryMetricMessage
- _OBJC_METACLASS_$_AFMyriadAdvertisementContext
- _OBJC_METACLASS_$_AFMyriadAdvertisementContextManager
- _OBJC_METACLASS_$_AFMyriadAdvertisementContextRecord
- _OBJC_METACLASS_$_AFMyriadContext
- _OBJC_METACLASS_$_AFMyriadCoordinator
- _OBJC_METACLASS_$_AFMyriadEmergencyCallPunchout
- _OBJC_METACLASS_$_AFMyriadGoodnessScoreContext
- _OBJC_METACLASS_$_AFMyriadGoodnessScoreEvaluator
- _OBJC_METACLASS_$_AFMyriadGoodnessScoreOverrideContext
- _OBJC_METACLASS_$_AFMyriadGoodnessScoreOverrideState
- _OBJC_METACLASS_$_AFMyriadInstrumentation
- _OBJC_METACLASS_$_AFMyriadMetrics
- _OBJC_METACLASS_$_AFMyriadMetricsAdditionalContext
- _OBJC_METACLASS_$_AFMyriadMonitor
- _OBJC_METACLASS_$_AFMyriadPerceptualAudioHash
- _OBJC_METACLASS_$_AFMyriadPreferences
- _OBJC_METACLASS_$_AFMyriadRecord
- _OBJC_METACLASS_$_AFMyriadSession
- _OBJC_METACLASS_$__AFMyriadAdvertisementContextMutation
- _OBJC_METACLASS_$__AFMyriadContextMutation
- _OBJC_METACLASS_$__AFMyriadGoodnessScoreOverrideStateMutation
- _OBJC_METACLASS_$__AFMyriadPerceptualAudioHashMutation
- _OBJC_METACLASS_$__AFMyriadSessionMutation
- _SFDiagnosticsFunction
- _SharingLibrary.frameworkLibrary
- _TUCallProviderManagerFunction
- _TUCallSourceIdentifierSpeakerRouteFunction
- _TUDialRequestFunction
- _TelephonyUtilitiesLibrary.sLib
- _TelephonyUtilitiesLibrary.sOnce
- _WPHeySiriAdvertisingDataFunction
- _WPHeySiriFunction
- _WPHeySiriKeyManufacturerDataFunction
- _WirelessProximityLibrary
- _WirelessProximityLibrary.frameworkLibrary
- __OBJC_$_CATEGORY_AceObject_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CATEGORY_NSArray_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CATEGORY_NSDate_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CATEGORY_NSDictionary_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CATEGORY_NSNull_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CATEGORY_NSString_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CATEGORY_NSURL_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_CLASS_METHODS_AFMyriadAccessoryMessage
- __OBJC_$_CLASS_METHODS_AFMyriadAdvertisementContext
- __OBJC_$_CLASS_METHODS_AFMyriadContext
- __OBJC_$_CLASS_METHODS_AFMyriadCoordinator
- __OBJC_$_CLASS_METHODS_AFMyriadGoodnessScoreOverrideState
- __OBJC_$_CLASS_METHODS_AFMyriadMetrics
- __OBJC_$_CLASS_METHODS_AFMyriadMonitor
- __OBJC_$_CLASS_METHODS_AFMyriadPerceptualAudioHash
- __OBJC_$_CLASS_METHODS_AFMyriadSession
- __OBJC_$_CLASS_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions|VSAdditions)
- __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
- __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
- __OBJC_$_CLASS_PROP_LIST_AFMyriadAdvertisementContext
- __OBJC_$_CLASS_PROP_LIST_AFMyriadContext
- __OBJC_$_CLASS_PROP_LIST_AFMyriadGoodnessScoreOverrideState
- __OBJC_$_CLASS_PROP_LIST_AFMyriadPerceptualAudioHash
- __OBJC_$_CLASS_PROP_LIST_AFMyriadSession
- __OBJC_$_INSTANCE_METHODS_AFClockTimer(AFClockTimerMutability|ClockItem)
- __OBJC_$_INSTANCE_METHODS_AFMyriadAccessoryMessage
- __OBJC_$_INSTANCE_METHODS_AFMyriadAccessoryMetricMessage
- __OBJC_$_INSTANCE_METHODS_AFMyriadAdvertisementContext(AFMyriadAdvertisementContextMutability)
- __OBJC_$_INSTANCE_METHODS_AFMyriadAdvertisementContextManager
- __OBJC_$_INSTANCE_METHODS_AFMyriadAdvertisementContextRecord
- __OBJC_$_INSTANCE_METHODS_AFMyriadContext(AFMyriadContextMutability)
- __OBJC_$_INSTANCE_METHODS_AFMyriadCoordinator
- __OBJC_$_INSTANCE_METHODS_AFMyriadEmergencyCallPunchout
- __OBJC_$_INSTANCE_METHODS_AFMyriadGoodnessScoreContext
- __OBJC_$_INSTANCE_METHODS_AFMyriadGoodnessScoreEvaluator
- __OBJC_$_INSTANCE_METHODS_AFMyriadGoodnessScoreOverrideContext
- __OBJC_$_INSTANCE_METHODS_AFMyriadGoodnessScoreOverrideState(AFMyriadGoodnessScoreOverrideStateMutability)
- __OBJC_$_INSTANCE_METHODS_AFMyriadInstrumentation
- __OBJC_$_INSTANCE_METHODS_AFMyriadMetrics
- __OBJC_$_INSTANCE_METHODS_AFMyriadMetricsAdditionalContext
- __OBJC_$_INSTANCE_METHODS_AFMyriadMonitor
- __OBJC_$_INSTANCE_METHODS_AFMyriadPerceptualAudioHash(AFMyriadPerceptualAudioHashMutability)
- __OBJC_$_INSTANCE_METHODS_AFMyriadPreferences
- __OBJC_$_INSTANCE_METHODS_AFMyriadRecord
- __OBJC_$_INSTANCE_METHODS_AFMyriadSession(AFMyriadSessionMutability)
- __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions|VSAdditions)
- __OBJC_$_INSTANCE_METHODS_AceObject(AFSecurityDigestibleChunksProvider|AssistantAdditions|AnalyticsContextVending)
- __OBJC_$_INSTANCE_METHODS_NSArray(AFSecurityDigestibleChunksProvider|AFCollectionUtilities)
- __OBJC_$_INSTANCE_METHODS_NSDate(AFSecurityDigestibleChunksProvider|AssistantAdditions)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(AFSecurityDigestibleChunksProvider|AFCollectionUtilities)
- __OBJC_$_INSTANCE_METHODS_NSNull(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport)
- __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
- __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
- __OBJC_$_INSTANCE_METHODS__AFMyriadAdvertisementContextMutation
- __OBJC_$_INSTANCE_METHODS__AFMyriadContextMutation
- __OBJC_$_INSTANCE_METHODS__AFMyriadGoodnessScoreOverrideStateMutation
- __OBJC_$_INSTANCE_METHODS__AFMyriadPerceptualAudioHashMutation
- __OBJC_$_INSTANCE_METHODS__AFMyriadSessionMutation
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadAccessoryMessage
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadAccessoryMetricMessage
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadAdvertisementContext
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadAdvertisementContextManager
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadAdvertisementContextRecord
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadContext
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadCoordinator
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadEmergencyCallPunchout
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadGoodnessScoreContext
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadGoodnessScoreEvaluator
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadGoodnessScoreOverrideContext
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadGoodnessScoreOverrideState
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadInstrumentation
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadMetricsAdditionalContext
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadMonitor
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadPerceptualAudioHash
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadPreferences
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadRecord
- __OBJC_$_INSTANCE_VARIABLES_AFMyriadSession
- __OBJC_$_INSTANCE_VARIABLES__AFMyriadAdvertisementContextMutation
- __OBJC_$_INSTANCE_VARIABLES__AFMyriadContextMutation
- __OBJC_$_INSTANCE_VARIABLES__AFMyriadGoodnessScoreOverrideStateMutation
- __OBJC_$_INSTANCE_VARIABLES__AFMyriadPerceptualAudioHashMutation
- __OBJC_$_INSTANCE_VARIABLES__AFMyriadSessionMutation
- __OBJC_$_PROP_LIST_AFMyriadAccessoryMessage
- __OBJC_$_PROP_LIST_AFMyriadAccessoryMetricMessage
- __OBJC_$_PROP_LIST_AFMyriadAdvertisementContext
- __OBJC_$_PROP_LIST_AFMyriadAdvertisementContextRecord
- __OBJC_$_PROP_LIST_AFMyriadContext
- __OBJC_$_PROP_LIST_AFMyriadCoordinator
- __OBJC_$_PROP_LIST_AFMyriadGoodnessScoreContext
- __OBJC_$_PROP_LIST_AFMyriadGoodnessScoreEvaluator
- __OBJC_$_PROP_LIST_AFMyriadGoodnessScoreOverrideContext
- __OBJC_$_PROP_LIST_AFMyriadGoodnessScoreOverrideState
- __OBJC_$_PROP_LIST_AFMyriadInstrumentation
- __OBJC_$_PROP_LIST_AFMyriadMetricsAdditionalContext
- __OBJC_$_PROP_LIST_AFMyriadMonitor
- __OBJC_$_PROP_LIST_AFMyriadPerceptualAudioHash
- __OBJC_$_PROP_LIST_AFMyriadRecord
- __OBJC_$_PROP_LIST_AFMyriadSession
- __OBJC_$_PROP_LIST_NSArray_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_PROP_LIST_NSDate_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_PROP_LIST_NSDictionary_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_PROP_LIST_NSString_$_AFSecurityDigestibleChunksProvider
- __OBJC_$_PROP_LIST__AFMyriadAdvertisementContextMutation
- __OBJC_$_PROP_LIST__AFMyriadContextMutation
- __OBJC_$_PROP_LIST__AFMyriadGoodnessScoreOverrideStateMutation
- __OBJC_$_PROP_LIST__AFMyriadPerceptualAudioHashMutation
- __OBJC_$_PROP_LIST__AFMyriadSessionMutation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFMyriadAdvertisementContextMutating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFMyriadContextMutating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFMyriadGoodnessScoreOverrideStateMutating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFMyriadPerceptualAudioHashMutating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFMyriadSessionMutating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WPHeySiriProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WPHeySiriProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFMyriadAdvertisementContextMutating
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFMyriadContextMutating
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFMyriadGoodnessScoreOverrideStateMutating
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFMyriadPerceptualAudioHashMutating
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFMyriadSessionMutating
- __OBJC_$_PROTOCOL_METHOD_TYPES_WPHeySiriProtocol
- __OBJC_$_PROTOCOL_REFS_AFMyriadAdvertisementContextMutating
- __OBJC_$_PROTOCOL_REFS_AFMyriadContextMutating
- __OBJC_$_PROTOCOL_REFS_AFMyriadGoodnessScoreOverrideStateMutating
- __OBJC_$_PROTOCOL_REFS_AFMyriadPerceptualAudioHashMutating
- __OBJC_$_PROTOCOL_REFS_AFMyriadSessionMutating
- __OBJC_$_PROTOCOL_REFS_WPHeySiriProtocol
- __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$_AFSecurityDigestibleChunksProvider
- __OBJC_CATEGORY_PROTOCOLS_$_NSDate_$_AFSecurityDigestibleChunksProvider
- __OBJC_CATEGORY_PROTOCOLS_$_NSDictionary_$_AFSecurityDigestibleChunksProvider
- __OBJC_CATEGORY_PROTOCOLS_$_NSString_$_AFSecurityDigestibleChunksProvider
- __OBJC_CLASS_PROTOCOLS_$_AFClockTimer(AFClockTimerMutability|ClockItem)
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadAdvertisementContext
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadContext
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadCoordinator
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadGoodnessScoreEvaluator
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadGoodnessScoreOverrideState
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadMonitor
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadPerceptualAudioHash
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadRecord
- __OBJC_CLASS_PROTOCOLS_$_AFMyriadSession
- __OBJC_CLASS_PROTOCOLS_$_AceObject(AFSecurityDigestibleChunksProvider|AssistantAdditions|AnalyticsContextVending)
- __OBJC_CLASS_PROTOCOLS_$_NSNull(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport)
- __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
- __OBJC_CLASS_PROTOCOLS_$__AFMyriadAdvertisementContextMutation
- __OBJC_CLASS_PROTOCOLS_$__AFMyriadContextMutation
- __OBJC_CLASS_PROTOCOLS_$__AFMyriadGoodnessScoreOverrideStateMutation
- __OBJC_CLASS_PROTOCOLS_$__AFMyriadPerceptualAudioHashMutation
- __OBJC_CLASS_PROTOCOLS_$__AFMyriadSessionMutation
- __OBJC_CLASS_RO_$_AFMyriadAccessoryMessage
- __OBJC_CLASS_RO_$_AFMyriadAccessoryMetricMessage
- __OBJC_CLASS_RO_$_AFMyriadAdvertisementContext
- __OBJC_CLASS_RO_$_AFMyriadAdvertisementContextManager
- __OBJC_CLASS_RO_$_AFMyriadAdvertisementContextRecord
- __OBJC_CLASS_RO_$_AFMyriadContext
- __OBJC_CLASS_RO_$_AFMyriadCoordinator
- __OBJC_CLASS_RO_$_AFMyriadEmergencyCallPunchout
- __OBJC_CLASS_RO_$_AFMyriadGoodnessScoreContext
- __OBJC_CLASS_RO_$_AFMyriadGoodnessScoreEvaluator
- __OBJC_CLASS_RO_$_AFMyriadGoodnessScoreOverrideContext
- __OBJC_CLASS_RO_$_AFMyriadGoodnessScoreOverrideState
- __OBJC_CLASS_RO_$_AFMyriadInstrumentation
- __OBJC_CLASS_RO_$_AFMyriadMetrics
- __OBJC_CLASS_RO_$_AFMyriadMetricsAdditionalContext
- __OBJC_CLASS_RO_$_AFMyriadMonitor
- __OBJC_CLASS_RO_$_AFMyriadPerceptualAudioHash
- __OBJC_CLASS_RO_$_AFMyriadPreferences
- __OBJC_CLASS_RO_$_AFMyriadRecord
- __OBJC_CLASS_RO_$_AFMyriadSession
- __OBJC_CLASS_RO_$__AFMyriadAdvertisementContextMutation
- __OBJC_CLASS_RO_$__AFMyriadContextMutation
- __OBJC_CLASS_RO_$__AFMyriadGoodnessScoreOverrideStateMutation
- __OBJC_CLASS_RO_$__AFMyriadPerceptualAudioHashMutation
- __OBJC_CLASS_RO_$__AFMyriadSessionMutation
- __OBJC_LABEL_PROTOCOL_$_AFMyriadAdvertisementContextMutating
- __OBJC_LABEL_PROTOCOL_$_AFMyriadContextMutating
- __OBJC_LABEL_PROTOCOL_$_AFMyriadGoodnessScoreOverrideStateMutating
- __OBJC_LABEL_PROTOCOL_$_AFMyriadPerceptualAudioHashMutating
- __OBJC_LABEL_PROTOCOL_$_AFMyriadSessionMutating
- __OBJC_LABEL_PROTOCOL_$_WPHeySiriProtocol
- __OBJC_METACLASS_RO_$_AFMyriadAccessoryMessage
- __OBJC_METACLASS_RO_$_AFMyriadAccessoryMetricMessage
- __OBJC_METACLASS_RO_$_AFMyriadAdvertisementContext
- __OBJC_METACLASS_RO_$_AFMyriadAdvertisementContextManager
- __OBJC_METACLASS_RO_$_AFMyriadAdvertisementContextRecord
- __OBJC_METACLASS_RO_$_AFMyriadContext
- __OBJC_METACLASS_RO_$_AFMyriadCoordinator
- __OBJC_METACLASS_RO_$_AFMyriadEmergencyCallPunchout
- __OBJC_METACLASS_RO_$_AFMyriadGoodnessScoreContext
- __OBJC_METACLASS_RO_$_AFMyriadGoodnessScoreEvaluator
- __OBJC_METACLASS_RO_$_AFMyriadGoodnessScoreOverrideContext
- __OBJC_METACLASS_RO_$_AFMyriadGoodnessScoreOverrideState
- __OBJC_METACLASS_RO_$_AFMyriadInstrumentation
- __OBJC_METACLASS_RO_$_AFMyriadMetrics
- __OBJC_METACLASS_RO_$_AFMyriadMetricsAdditionalContext
- __OBJC_METACLASS_RO_$_AFMyriadMonitor
- __OBJC_METACLASS_RO_$_AFMyriadPerceptualAudioHash
- __OBJC_METACLASS_RO_$_AFMyriadPreferences
- __OBJC_METACLASS_RO_$_AFMyriadRecord
- __OBJC_METACLASS_RO_$_AFMyriadSession
- __OBJC_METACLASS_RO_$__AFMyriadAdvertisementContextMutation
- __OBJC_METACLASS_RO_$__AFMyriadContextMutation
- __OBJC_METACLASS_RO_$__AFMyriadGoodnessScoreOverrideStateMutation
- __OBJC_METACLASS_RO_$__AFMyriadPerceptualAudioHashMutation
- __OBJC_METACLASS_RO_$__AFMyriadSessionMutation
- __OBJC_PROTOCOL_$_AFMyriadAdvertisementContextMutating
- __OBJC_PROTOCOL_$_AFMyriadContextMutating
- __OBJC_PROTOCOL_$_AFMyriadGoodnessScoreOverrideStateMutating
- __OBJC_PROTOCOL_$_AFMyriadPerceptualAudioHashMutating
- __OBJC_PROTOCOL_$_AFMyriadSessionMutating
- __OBJC_PROTOCOL_$_WPHeySiriProtocol
- ___105-[AFMyriadInstrumentation logCDADeviceStateActivityStartedOrChanged:withTrigger:withCdaId:withTimestamp:]_block_invoke
- ___108-[AFMyriadInstrumentation logCDAElectionAdvertisingStarting:withDelay:withInterval:withCdaId:withTimestamp:]_block_invoke
- ___113-[AFMyriadContext initWithTimestamp:perceptualAudioHash:overrideState:activationSource:activationExpirationTime:]_block_invoke
- ___132-[AFMyriadCoordinator _testAndFilterAdvertisementsFromContextCollector:voiceTriggerEndTime:advertisementDispatchTime:advertisement:]_block_invoke
- ___143-[AFMyriadSession initWithGeneration:sessionId:currentElectionAdvertisementId:currentElectionAdvertisementData:electionAdvertisementDataByIds:]_block_invoke
- ___151-[AFMyriadInstrumentation logCDAElectionDecisionMadeDebug:withCrossDeviceArbitrationAllowed:advertisementData:withDeviceGroup:withCdaId:withTimestamp:]_block_invoke
- ___228-[AFMyriadInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:]_block_invoke
- ___25-[AFMyriadMonitor didWin]_block_invoke
- ___29-[AFMyriadCoordinator inTask]_block_invoke
- ___30-[AFMyriadCoordinator endTask]_block_invoke
- ___31-[AFMyriadMonitor isMonitoring]_block_invoke
- ___32+[AFMyriadMonitor sharedMonitor]_block_invoke
- ___33+[AFMyriadMetrics sharedInstance]_block_invoke
- ___33-[AFMyriadCoordinator setInTask:]_block_invoke
- ___33-[AFMyriadMonitor stopMonitoring]_block_invoke
- ___34-[AFMyriadCoordinator enterState:]_block_invoke
- ___35-[AFMyriadCoordinator _enterState:]_block_invoke
- ___35-[AFMyriadCoordinator readDefaults]_block_invoke
- ___36-[AFMyriadCoordinator preheatWiProx]_block_invoke
- ___36-[AFMyriadCoordinator setupEnabled:]_block_invoke
- ___36-[AFMyriadCoordinator stopListening]_block_invoke
- ___37-[AFMyriadCoordinator advertiseWith:]_block_invoke
- ___37-[AFMyriadCoordinator startListening]_block_invoke
- ___37-[AFMyriadCoordinator stopListening:]_block_invoke
- ___38-[AFMyriadCoordinator _ageWedgeFilter]_block_invoke
- ___38-[AFMyriadCoordinator _sortedReplies:]_block_invoke
- ___38-[AFMyriadCoordinator _sortedReplies:]_block_invoke_2
- ___38-[AFMyriadCoordinator _stopListening:]_block_invoke
- ___38-[AFMyriadCoordinator endAdvertising:]_block_invoke
- ___38-[AFMyriadCoordinator startListening:]_block_invoke
- ___38-[AFMyriadMonitor ignoreMyriadEvents:]_block_invoke
- ___39-[AFMyriadCoordinator _initializeTimer]_block_invoke
- ___39-[AFMyriadCoordinator _startListening:]_block_invoke
- ___39-[AFMyriadCoordinator updateRequestId:]_block_invoke
- ___40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke
- ___40-[AFMyriadCoordinator _stopAdvertising:]_block_invoke
- ___40-[AFMyriadCoordinator initWithDelegate:]_block_invoke
- ___40-[AFMyriadMonitor _setDecisionIsPending]_block_invoke
- ___41-[AFMyriadCoordinator _advertiseSlowdown]_block_invoke
- ___41-[AFMyriadCoordinator _forceLocalWinner:]_block_invoke
- ___41-[AFMyriadCoordinator _setOverallTimeout]_block_invoke
- ___41-[AFMyriadGoodnessScoreEvaluator preheat]_block_invoke
- ___42-[AFMyriadCoordinator _clearMyriadSession]_block_invoke
- ___42-[AFMyriadCoordinator _shouldContinueFor:]_block_invoke
- ___43-[AFMyriadCoordinator setCurrentRequestId:]_block_invoke
- ___43-[AFMyriadMonitor _enqueueBlock:forReason:]_block_invoke
- ___44-[AFMyriadAdvertisementContextManager reset]_block_invoke
- ___44-[AFMyriadCoordinator _advertiseIndefinite:]_block_invoke
- ___44-[AFMyriadInstrumentation resetCurrentBoost]_block_invoke
- ___44-[AFMyriadPerceptualAudioHash initWithData:]_block_invoke
- ___45-[AFMyriadCoordinator _shouldHandleEmergency]_block_invoke
- ___45-[AFMyriadCoordinator heySiriDidUpdateState:]_block_invoke
- ___45-[AFMyriadCoordinator waitWiProx:andExecute:]_block_invoke
- ___45-[AFMyriadInstrumentation updateBoost:value:]_block_invoke
- ___46-[AFMyriadCoordinator _enterBLEDiagnosticMode]_block_invoke
- ___46-[AFMyriadCoordinator _waitWiProx:andExecute:]_block_invoke
- ___46-[AFMyriadCoordinator resetMyriadCoordinator:]_block_invoke
- ___48-[AFMyriadCoordinator endAdvertisingAfterDelay:]_block_invoke
- ___48-[AFMyriadCoordinator endAdvertisingAfterDelay:]_block_invoke_2
- ___48-[AFMyriadCoordinator startAdvertisingEmergency]_block_invoke
- ___48-[AFMyriadCoordinator startAdvertisingSlowdown:]_block_invoke
- ___48-[AFMyriadCoordinator startResponseAdvertising:]_block_invoke
- ___50-[AFMyriadCoordinator notifyCurrentDecisionResult]_block_invoke
- ___51-[AFMyriadCoordinator _duringNextWindowEnterState:]_block_invoke
- ___51-[AFMyriadCoordinator _startTimer:for:thenExecute:]_block_invoke
- ___51-[AFMyriadCoordinator _stopAdvertisingAndListening]_block_invoke
- ___51-[AFMyriadMonitor _ignoreRepostMyriadNotification:]_block_invoke
- ___52-[AFMyriadCoordinator heySiri:foundDevice:withInfo:]_block_invoke
- ___52-[AFMyriadInstrumentation updateIsTrump:withReason:]_block_invoke
- ___53-[AFMyriadCoordinator _createMyriadSessionIfRequired]_block_invoke
- ___54-[AFMyriadCoordinator _initializeWiProxReadinessTimer]_block_invoke
- ___54-[AFMyriadCoordinator _startTimer:for:thenEnterState:]_block_invoke
- ___55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke
- ___55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke_2
- ___55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke_3
- ___55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke_4
- ___55-[AFMyriadCoordinator startAdvertisingEmergencyHandled]_block_invoke
- ___55-[AFMyriadCoordinator startAdvertisingFromInEarTrigger]_block_invoke
- ___55-[AFMyriadMonitor waitForMyriadDecisionWithCompletion:]_block_invoke
- ___56-[AFMyriadCoordinator _advertiseSuppressTriggerInOutput]_block_invoke
- ___56-[AFMyriadCoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke
- ___56-[AFMyriadMonitor dequeueBlocksWaitingForMyriadDecision]_block_invoke
- ___57-[AFMyriadCoordinator startAdvertisingFromCarPlayTrigger]_block_invoke
- ___58-[AFMyriadCoordinator faceDetectedBoostWithMyriadContext:]_block_invoke
- ___59-[AFMyriadGoodnessScoreEvaluator myriadTrialBoostsUpdated:]_block_invoke
- ___59-[AFMyriadInstrumentation getPreviousBoostsWithCompletion:]_block_invoke
- ___59-[AFMyriadMonitor _fetchCurrentMyriadDecisionWithWaitTime:]_block_invoke
- ___60-[AFMyriadCoordinator advertiseWith:afterDelay:maxInterval:]_block_invoke
- ___60-[AFMyriadCoordinator advertiseWith:afterDelay:maxInterval:]_block_invoke_2
- ___60-[AFMyriadCoordinator advertiseWith:afterDelay:maxInterval:]_block_invoke_3
- ___60-[AFMyriadCoordinator endAdvertisingWithDeviceProhibitions:]_block_invoke
- ___60-[AFMyriadEmergencyCallPunchout initiateEmergencyCallMyriad]_block_invoke
- ___61-[AFMyriadCoordinator _endAdvertisingWithDeviceProhibitions:]_block_invoke
- ___62-[AFMyriadCoordinator _createDispatchTimerWithTime:toExecute:]_block_invoke
- ___63-[AFMyriadCoordinator startAdvertising:afterDelay:maxInterval:]_block_invoke
- ___65-[AFMyriadInstrumentation _logRequestLinkMessageRequestId:cdaId:]_block_invoke
- ___65-[AFMyriadMonitor waitForMyriadDecisionForReason:withCompletion:]_block_invoke
- ___66-[AFMyriadGoodnessScoreEvaluator _settingsConnectionDidDisconnect]_block_invoke
- ___67-[AFMyriadCoordinator _advertise:afterDelay:maxInterval:andMoveTo:]_block_invoke
- ___67-[AFMyriadCoordinator startAdvertisingFromVoiceTriggerWithContext:]_block_invoke
- ___67-[AFMyriadGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]_block_invoke
- ___68-[AFMyriadCoordinator _addElectionAdvertisementDataToMyriadSession:]_block_invoke
- ___68-[AFMyriadCoordinator startAdvertisingFromDirectTriggerWithContext:]_block_invoke
- ___68-[AFMyriadGoodnessScoreOverrideState initWithOverrideOption:reason:]_block_invoke
- ___70-[AFMyriadCoordinator startAdvertisingFromOutgoingTriggerWithContext:]_block_invoke
- ___70-[AFMyriadMonitor startMonitoringWithTimeoutInterval:instanceContext:]_block_invoke
- ___72-[AFMyriadCoordinator startWatchAdvertisingFromVoiceTriggerWithContext:]_block_invoke
- ___73-[AFMyriadAdvertisementContextManager triggerABCForType:subType:context:]_block_invoke
- ___73-[AFMyriadAdvertisementContextManager triggerABCForType:subType:context:]_block_invoke_2
- ___73-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke
- ___73-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke_2
- ___73-[AFMyriadCoordinator startAdvertisingFromInTaskVoiceTriggerWithContext:]_block_invoke
- ___73-[AFMyriadCoordinator startWatchAdvertisingFromDirectTriggerWithContext:]_block_invoke
- ___76-[AFMyriadCoordinator _startListeningAfterWiProxIsReady:inState:completion:]_block_invoke
- ___76-[AFMyriadInstrumentation logCDAElectionTimerEnded:withCdaId:withTimestamp:]_block_invoke
- ___78-[AFMyriadCoordinator startAdvertisingFromAlertFiringVoiceTriggerWithContext:]_block_invoke
- ___81-[AFMyriadAdvertisementContext initWithGeneration:contextData:contextFetchDelay:]_block_invoke
- ___82-[AFMyriadInstrumentation logCDADeviceStateActivityEnded:withCdaId:withTimestamp:]_block_invoke
- ___82-[AFMyriadInstrumentation logCDAElectionAdvertisingEnded:withCdaId:withTimestamp:]_block_invoke
- ___83-[AFMyriadInstrumentation logCDAElectionAdvertisingEnding:withCdaId:withTimestamp:]_block_invoke
- ___84-[AFMyriadInstrumentation logCDAElectionAdvertisingStarted:withCdaId:withTimestamp:]_block_invoke
- ___92-[AFMyriadCoordinator startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:]_block_invoke
- ___94-[AFMyriadMetrics _submitMyriadMetrics:additionalContext:toStream:instrumentation:completion:]_block_invoke
- ___95-[AFMyriadCoordinator _suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:]_block_invoke
- ___98-[AFMyriadGoodnessScoreEvaluator initWithDeviceInstanceContext:preferences:queue:instrumentation:]_block_invoke
- ___AFMyriadAdvertisementRecordTypeGetFromName_block_invoke
- ___AFMyriadGoodnessScoreBumpReasonGetFromName_block_invoke
- ___AFMyriadGoodnessScoreOverrideOptionGetFromName_block_invoke
- ___AFMyriadMaxNoOperationDelay_block_invoke
- ___TelephonyUtilitiesLibrary_block_invoke
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_32_e15_v32?08Q16^B24l
- ___block_descriptor_32_e31_v32?0"NSUUID"8"NSData"16^B24l
- ___block_descriptor_32_e35_v16?0"<AFMyriadSessionMutating>"8l
- ___block_descriptor_40_e8_32r_e15_v32?08Q16^B24lr32l8
- ___block_descriptor_40_e8_32s_e31_v32?0"AFMyriadRecord"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e47_v16?0"<AFMyriadPerceptualAudioHashMutating>"8ls32l8
- ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32r40w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw40l8r32l8
- ___block_descriptor_48_e8_32s40s_e31_v32?0"AFMyriadRecord"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s_e54_v16?0"<AFMyriadGoodnessScoreOverrideStateMutating>"8ls32l8
- ___block_descriptor_50_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e8_v16?0q8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e35_v16?0"<AFMyriadSessionMutating>"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e25_v24?0"NSData"8?<v?>16ls32l8s40l8
- ___block_descriptor_56_e8_32s_e48_v16?0"<AFMyriadAdvertisementContextMutating>"8ls32l8
- ___block_descriptor_60_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r_e22_v16?0"NSDictionary"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e59_v32?0"NSUUID"8"AFMyriadAdvertisementContextRecord"16^B24ls32l8s40l8s48l8
- ___block_descriptor_68_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s40l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s_e35_v16?0"<AFMyriadSessionMutating>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s_e35_v16?0"<AFMyriadContextMutating>"8ls32l8s40l8
- ___block_descriptor_72_e8_32s_e31_v32?08"AFMyriadRecord"16^B24ls32l8
- ___block_descriptor_73_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___initSFDiagnostics_block_invoke
- ___initTUCallProviderManager_block_invoke
- ___initTUCallSourceIdentifierSpeakerRoute_block_invoke
- ___initTUDialRequest_block_invoke
- ___initWPHeySiriAdvertisingData_block_invoke
- ___initWPHeySiriKeyManufacturerData_block_invoke
- ___initWPHeySiri_block_invoke
- __currentCoordinator
- __lastRandomConfidenceGenerated
- __lastRandomTieBreakerGenerated
- _bzero
- _carplayTriggerSeenCallback
- _classSFDiagnostics
- _classTUCallProviderManager
- _classTUDialRequest
- _classWPHeySiri
- _constantTUCallSourceIdentifierSpeakerRoute
- _constantWPHeySiriAdvertisingData
- _constantWPHeySiriKeyManufacturerData
- _currentMyrAccessoryVersion
- _emergencyCallback
- _exp
- _extractMyriadDataFromAudioContext
- _getEffectiveNotificationName
- _getSFDiagnosticsClass
- _getTUCallProviderManagerClass
- _getTUCallSourceIdentifierSpeakerRoute
- _getTUDialRequestClass
- _getWPHeySiriAdvertisingData
- _getWPHeySiriClass
- _getWPHeySiriKeyManufacturerData
- _hammingDistance
- _inEarTriggerSeenCallback
- _initSFDiagnostics
- _initSFDiagnostics.sOnce
- _initTUCallProviderManager
- _initTUCallProviderManager.sOnce
- _initTUCallSourceIdentifierSpeakerRoute
- _initTUCallSourceIdentifierSpeakerRoute.sOnce
- _initTUDialRequest
- _initTUDialRequest.sOnce
- _initWPHeySiri
- _initWPHeySiri.sOnce
- _initWPHeySiriAdvertisingData
- _initWPHeySiriAdvertisingData.sOnce
- _initWPHeySiriKeyManufacturerData
- _initWPHeySiriKeyManufacturerData.sOnce
- _kMyriadAdvertisementContextRecordVersion
- _kRequestIdForMyriadService
- _memcpy
- _myrAccessoryMetricsMessageKey
- _myriadDecisionRequestCallback
- _myriad_attention_queue_label
- _myriad_context_queue_label
- _myriad_readiness_queue_label
- _myriad_timer_mgmt_queue_label
- _myriad_work_queue_label
- _notificationCallback
- _objc_msgSend$BLEActivityEnabled
- _objc_msgSend$_addElectionAdvertisementDataToMyriadSession:
- _objc_msgSend$_adjustActionWindowsFromSlowdown:
- _objc_msgSend$_advertise:afterDelay:maxInterval:andMoveTo:
- _objc_msgSend$_advertise:andMoveTo:
- _objc_msgSend$_advertiseIndefinite:
- _objc_msgSend$_advertiseSlowdown
- _objc_msgSend$_advertiseSuppressTriggerInOutput
- _objc_msgSend$_advertiseTrigger
- _objc_msgSend$_advertiseWith:afterDelay:maxInterval:thenExecute:
- _objc_msgSend$_advertisementPayloadSizeForVersion:
- _objc_msgSend$_ageWedgeFilter
- _objc_msgSend$_boostTypeAsString:
- _objc_msgSend$_bumpGoodnessScore:lastActivationTime:mediaPlaybackInterruptedTime:ignoreAdjustedBoost:recentlyWonBySmallAmount:
- _objc_msgSend$_cancelOverallTimeout
- _objc_msgSend$_cancelRepostedMyriadDecisionTimer
- _objc_msgSend$_cancelTimer
- _objc_msgSend$_clear
- _objc_msgSend$_clearMyriadSession
- _objc_msgSend$_clearWiProxReadinessTimer
- _objc_msgSend$_copyRawBytesFromSource:toDest:length:
- _objc_msgSend$_createDispatchTimerFor:toExecute:
- _objc_msgSend$_createDispatchTimerForEvent:toExecute:
- _objc_msgSend$_createDispatchTimerWithTime:toExecute:
- _objc_msgSend$_createEndAnalyticContexFromIntermediateContext:forVersion:sessionId:
- _objc_msgSend$_createMyriadSessionIfRequired
- _objc_msgSend$_createSchemaClientEvent:
- _objc_msgSend$_createWaitWiProxTimer:waitBlock:
- _objc_msgSend$_decisionMadeContext:additionalContext:instrumentation:completion:
- _objc_msgSend$_decodeMetricDataPayload:decodedPayload:
- _objc_msgSend$_dequeueBlocksWithSignal:
- _objc_msgSend$_deregisterFromMyriadEventNotifications
- _objc_msgSend$_deregisterFromRepostedDecisionResultsObservers
- _objc_msgSend$_deviceIDFromBytes:
- _objc_msgSend$_deviceShouldContinue:
- _objc_msgSend$_duringNextWindowEnterState:
- _objc_msgSend$_duringNextWindowExecute:
- _objc_msgSend$_endAdvertising:
- _objc_msgSend$_endAdvertisingAnalyticsContext:
- _objc_msgSend$_endAdvertisingWithDeviceProhibitions:
- _objc_msgSend$_enqueueBlock:forReason:
- _objc_msgSend$_enterBLEDiagnosticMode
- _objc_msgSend$_enterState:
- _objc_msgSend$_enteringIntoState:fromState:
- _objc_msgSend$_extractMetricDataFromDataPayload:
- _objc_msgSend$_fetchCurrentMyriadDecisionWithWaitTime:
- _objc_msgSend$_fetchDevicePlatformBiasIfRequired
- _objc_msgSend$_flushCompletions:
- _objc_msgSend$_forceLocalWinner:
- _objc_msgSend$_getAdvertisementRecordTypeForVersion:data:
- _objc_msgSend$_getCDASchemaCDATriggerType:
- _objc_msgSend$_getDeviceIdForVersion:data:
- _objc_msgSend$_getMyriadAdvertisementDataForVersion:data:
- _objc_msgSend$_getRecentBump:ignoreAdjustedBoost:recentlyWonBySmallAmount:
- _objc_msgSend$_getRequestType:
- _objc_msgSend$_getVoiceTriggerEndTimeForVersion:data:
- _objc_msgSend$_handleStateMachineErrorIfNeeded
- _objc_msgSend$_inTaskTriggerWasTooSoon
- _objc_msgSend$_initDeviceClassAndAdjustments
- _objc_msgSend$_initWithMessage:
- _objc_msgSend$_initializeMessageObj:
- _objc_msgSend$_initializeMessageObjFromDictionary:
- _objc_msgSend$_initializeMyriadAdvertisementContextRecordFromData:
- _objc_msgSend$_initializeTimer
- _objc_msgSend$_initializeWiProxReadinessTimer
- _objc_msgSend$_isAPhone:
- _objc_msgSend$_leaveBLEDiagnosticMode
- _objc_msgSend$_logRequestLinkMessageRequestId:cdaId:
- _objc_msgSend$_loseElection
- _objc_msgSend$_myriadSession
- _objc_msgSend$_myriadStateForSelf:
- _objc_msgSend$_myriadStateToString:
- _objc_msgSend$_nextElectionPublisherState
- _objc_msgSend$_okayToSuppressOnOutput
- _objc_msgSend$_phsSetupRecord
- _objc_msgSend$_readDefaults
- _objc_msgSend$_registerForMyriadEvents
- _objc_msgSend$_reloadTrialConfiguredBoostValues
- _objc_msgSend$_resetActionWindows
- _objc_msgSend$_resetAdvertisementTimings
- _objc_msgSend$_resetAudioData
- _objc_msgSend$_resetSettingsConnection
- _objc_msgSend$_resultSeenWithValue:
- _objc_msgSend$_resumeWiProxReadinessTimer
- _objc_msgSend$_sendAndLogClientEvent:stState:atTimestamp:
- _objc_msgSend$_setDecisionIsPending
- _objc_msgSend$_setMyriadContext:
- _objc_msgSend$_setOverallTimeout
- _objc_msgSend$_setupActionWindows
- _objc_msgSend$_shouldContinueFor:
- _objc_msgSend$_shouldHandleEmergency
- _objc_msgSend$_shouldStopListeningBeforeAdvertising
- _objc_msgSend$_signalEmergencyCallHandled
- _objc_msgSend$_sortedReplies
- _objc_msgSend$_sortedReplies:
- _objc_msgSend$_startAdvertising:afterDelay:maxInterval:
- _objc_msgSend$_startAdvertisingFromInTaskVoiceTrigger
- _objc_msgSend$_startAdvertisingFromVoiceTrigger
- _objc_msgSend$_startListening:
- _objc_msgSend$_startListeningAfterWiProxIsReady:inState:completion:
- _objc_msgSend$_startTimer:for:thenEnterState:
- _objc_msgSend$_startTimer:for:thenExecute:
- _objc_msgSend$_stateAsString
- _objc_msgSend$_stateAsString:
- _objc_msgSend$_stopAdvertising:
- _objc_msgSend$_stopAdvertisingAndListening
- _objc_msgSend$_stopListening:
- _objc_msgSend$_submitMyriadMetrics:additionalContext:toStream:instrumentation:completion:
- _objc_msgSend$_suspendWiProxReadinessTimer
- _objc_msgSend$_testAndUpdateWedgeFilter:
- _objc_msgSend$_trackHeySiriStartedAdvertisingAt:
- _objc_msgSend$_triggerABCForType:context:
- _objc_msgSend$_unduck
- _objc_msgSend$_updateMediaPlaybackBoost:
- _objc_msgSend$_updatePlatformBias:
- _objc_msgSend$_updateRecentSiriBoostTrialEnabled:
- _objc_msgSend$_updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:
- _objc_msgSend$_updateRepliesWith:id:data:
- _objc_msgSend$_updateVoiceTriggerTimeFromFile
- _objc_msgSend$_waitWiProx:andExecute:
- _objc_msgSend$_waitWiProxAndExecute:
- _objc_msgSend$_winElection
- _objc_msgSend$acknowledgeRequestKey
- _objc_msgSend$activationExpirationTime
- _objc_msgSend$activationSource
- _objc_msgSend$adjustByMultiplier:adding:
- _objc_msgSend$advertiseWith:afterDelay:maxInterval:
- _objc_msgSend$advertisementPayload
- _objc_msgSend$advertisingDidBegin:
- _objc_msgSend$advertisingDidEnd:
- _objc_msgSend$advertisingWillBeginWithDelay:advertisingInterval:
- _objc_msgSend$asAdvertisementData
- _objc_msgSend$bump
- _objc_msgSend$compareAdvertisementPayload:
- _objc_msgSend$constantGoodnessScore
- _objc_msgSend$contextFetchDelay
- _objc_msgSend$continuationRecord
- _objc_msgSend$coordinationEnabled
- _objc_msgSend$currentElectionAdvertisementData
- _objc_msgSend$currentElectionAdvertisementId
- _objc_msgSend$dataWithCapacity:
- _objc_msgSend$debugDescription
- _objc_msgSend$dequeueAllObjects
- _objc_msgSend$deviceAdjust
- _objc_msgSend$deviceClass
- _objc_msgSend$deviceDelay
- _objc_msgSend$deviceGroup
- _objc_msgSend$deviceProductType
- _objc_msgSend$deviceSlowDown
- _objc_msgSend$deviceTrumpDelay
- _objc_msgSend$diagnosticBLEModeWithCompletion:
- _objc_msgSend$directTriggerRecord
- _objc_msgSend$disableMyriadBLEActivity
- _objc_msgSend$electionAdvertisementDataByIds
- _objc_msgSend$electionDecisionKey
- _objc_msgSend$emergencyHandledKey
- _objc_msgSend$emergencyHandledRecord
- _objc_msgSend$emergencyProvider
- _objc_msgSend$emergencyRecord
- _objc_msgSend$emitMessage:timestamp:
- _objc_msgSend$emptyRecord
- _objc_msgSend$enterState:
- _objc_msgSend$generateRandomConfidence
- _objc_msgSend$generateTiebreaker
- _objc_msgSend$getActivationExpirationTime
- _objc_msgSend$getActivationSource
- _objc_msgSend$getCDASessionId:
- _objc_msgSend$getContextData
- _objc_msgSend$getContextFetchDelay
- _objc_msgSend$getCurrentElectionAdvertisementData
- _objc_msgSend$getCurrentElectionAdvertisementId
- _objc_msgSend$getData
- _objc_msgSend$getElectionAdvertisementDataByIds
- _objc_msgSend$getMyriadAdjustedBoostForGoodnessScoreContext:
- _objc_msgSend$getOverrideOption
- _objc_msgSend$getOverrideState
- _objc_msgSend$getOverridingContext
- _objc_msgSend$getPerceptualAudioHash
- _objc_msgSend$getPlatformBias
- _objc_msgSend$getSessionId:
- _objc_msgSend$getVersion:
- _objc_msgSend$goodness
- _objc_msgSend$goodnessScore
- _objc_msgSend$goodnessScoreBoosts
- _objc_msgSend$hasEqualAdvertisementData:
- _objc_msgSend$heySiri:foundDevice:withInfo:
- _objc_msgSend$ignoreMyriadPlatformBias
- _objc_msgSend$initWithAudioData:
- _objc_msgSend$initWithDelegate:queue:
- _objc_msgSend$initWithDeviceID:data:
- _objc_msgSend$initWithDeviceInstanceContext:preferences:
- _objc_msgSend$initWithDeviceInstanceContext:preferences:queue:instrumentation:
- _objc_msgSend$initWithGeneration:contextData:contextFetchDelay:
- _objc_msgSend$initWithGeneration:sessionId:currentElectionAdvertisementId:currentElectionAdvertisementData:electionAdvertisementDataByIds:
- _objc_msgSend$initWithIdentifier:
- _objc_msgSend$initWithIsAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:
- _objc_msgSend$initWithIsAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:unavailabilityReasons:allCapabilities:linwoodEverAvailable:
- _objc_msgSend$initWithIsAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:
- _objc_msgSend$initWithMetricData:
- _objc_msgSend$initWithOverrideOption:reason:
- _objc_msgSend$initWithProvider:
- _objc_msgSend$initWithTimestamp:perceptualAudioHash:overrideState:activationSource:activationExpirationTime:
- _objc_msgSend$initiateEmergencyCallMyriad
- _objc_msgSend$isAContinuation
- _objc_msgSend$isALateSupressionTrumpFor:
- _objc_msgSend$isATrump
- _objc_msgSend$isAnEmergency
- _objc_msgSend$isAnEmergencyHandled
- _objc_msgSend$isCollectedFromContextCollector
- _objc_msgSend$isInEarTrump
- _objc_msgSend$isMyriadMetricsMessage:
- _objc_msgSend$isSCDATrialEnabled
- _objc_msgSend$isSane
- _objc_msgSend$isSaneForVoiceTriggerEndTime:endtimeDistanceThreshold:
- _objc_msgSend$isSlowdown
- _objc_msgSend$lateSuppressionRecord
- _objc_msgSend$launchAppForDialRequest:completion:
- _objc_msgSend$listeningDidBegin:
- _objc_msgSend$listeningDidEnd:
- _objc_msgSend$logCDADeviceStateActivityEnded:withCdaId:withTimestamp:
- _objc_msgSend$logCDADeviceStateActivityStartedOrChanged:withTrigger:withCdaId:withTimestamp:
- _objc_msgSend$logCDAElectionAdvertisingEnded:withCdaId:withTimestamp:
- _objc_msgSend$logCDAElectionAdvertisingEnding:withCdaId:withTimestamp:
- _objc_msgSend$logCDAElectionAdvertisingStarted:withCdaId:withTimestamp:
- _objc_msgSend$logCDAElectionAdvertisingStarting:withDelay:withInterval:withCdaId:withTimestamp:
- _objc_msgSend$logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:
- _objc_msgSend$logCDAElectionDecisionMadeDebug:withCrossDeviceArbitrationAllowed:advertisementData:withDeviceGroup:withCdaId:withTimestamp:
- _objc_msgSend$logCDAElectionTimerEnded:withCdaId:withTimestamp:
- _objc_msgSend$mediaPlaybackInterruptedTime
- _objc_msgSend$messageAsStruct
- _objc_msgSend$messageKey
- _objc_msgSend$myriadConstantGoodness
- _objc_msgSend$myriadCoordinationEnabled
- _objc_msgSend$myriadCoordinationEnabledForAccessoryLogging
- _objc_msgSend$myriadCoordinator:didAddAdvertisement:toSession:
- _objc_msgSend$myriadCoordinator:didEnterState:fromState:
- _objc_msgSend$myriadCoordinator:didReceiveAdvertisement:
- _objc_msgSend$myriadCoordinator:willStartAdvertisingUsingData:
- _objc_msgSend$myriadCoordinator:willStartAdvertisingWithSlowDownInterval:
- _objc_msgSend$myriadCoordinatorBTLEDidEndAdvertising:
- _objc_msgSend$myriadCoordinatorBTLEDidEndScanning:
- _objc_msgSend$myriadCoordinatorBTLEDidStartAdvertising:
- _objc_msgSend$myriadCoordinatorBTLEDidStartScanning:
- _objc_msgSend$myriadCoordinatorDidHandleEmergency:
- _objc_msgSend$myriadCoordinatorIsAdvertisingEmergency:
- _objc_msgSend$myriadCoordinatorOverallTimerCancelled:
- _objc_msgSend$myriadCoordinatorWillHandleEmergency:
- _objc_msgSend$myriadDeviceAdjust
- _objc_msgSend$myriadDeviceClass
- _objc_msgSend$myriadDeviceDelay
- _objc_msgSend$myriadDeviceGroup
- _objc_msgSend$myriadDeviceTrumpDelay
- _objc_msgSend$myriadDeviceVTEndTimeDistanceThreshold
- _objc_msgSend$myriadMaxNoOperationDelay
- _objc_msgSend$myriadRequestTypeAsString:
- _objc_msgSend$myriadServerHasProvisioned
- _objc_msgSend$myriadShouldIgnoreAdjustedBoost
- _objc_msgSend$myriadTestDeviceDelay
- _objc_msgSend$notifyCurrentDecisionResult
- _objc_msgSend$numberWithUnsignedChar:
- _objc_msgSend$overriddenAdjustedScore
- _objc_msgSend$overrideOption
- _objc_msgSend$overrideState
- _objc_msgSend$pHash
- _objc_msgSend$perceptualAudioHash
- _objc_msgSend$publishState:
- _objc_msgSend$rawAudioGoodnessScore
- _objc_msgSend$rawGoodnessScore
- _objc_msgSend$reasons
- _objc_msgSend$recentlyWonBySmallAmount
- _objc_msgSend$recordForDeviceId:
- _objc_msgSend$releaseAllPowerAssertions
- _objc_msgSend$requestTypeKey
- _objc_msgSend$resetReplies
- _objc_msgSend$responseObject:
- _objc_msgSend$sessionIdKey
- _objc_msgSend$setActivationExpirationTime:
- _objc_msgSend$setActivationSource:
- _objc_msgSend$setAdvertisementDatas:
- _objc_msgSend$setAdvertisementDelay:
- _objc_msgSend$setAdvertisementInterval:
- _objc_msgSend$setAudioHash:
- _objc_msgSend$setAudioSourceIdentifier:
- _objc_msgSend$setBump:
- _objc_msgSend$setCdaAdvertisingEndChanged:
- _objc_msgSend$setCdaAdvertisingStartChanged:
- _objc_msgSend$setCdaId:
- _objc_msgSend$setContextData:
- _objc_msgSend$setContextFetchDelay:
- _objc_msgSend$setCurrentElectionAdvertisementData:
- _objc_msgSend$setCurrentElectionAdvertisementId:
- _objc_msgSend$setDebugElectionDecisionMade:
- _objc_msgSend$setDecision:
- _objc_msgSend$setDeviceBoost:
- _objc_msgSend$setDeviceClass:
- _objc_msgSend$setDeviceElectionStateContext:
- _objc_msgSend$setDeviceGroup:
- _objc_msgSend$setDialType:
- _objc_msgSend$setDispatchQueue:
- _objc_msgSend$setElectionAdvertisementDataByIds:
- _objc_msgSend$setElectionDecisionMade:
- _objc_msgSend$setElectionTimerEnded:
- _objc_msgSend$setGoodness:
- _objc_msgSend$setGoodnessScore:
- _objc_msgSend$setGoodnessScoreBoosts:
- _objc_msgSend$setHeardParticipants:
- _objc_msgSend$setIgnoreMyriadAdjustedBoost:
- _objc_msgSend$setIgnoreMyriadPlatformBias:
- _objc_msgSend$setIsCollectedFromContextCollector:
- _objc_msgSend$setIsCrossDeviceArbitrationAllowed:
- _objc_msgSend$setIsFromContextCollector:
- _objc_msgSend$setIsMe:
- _objc_msgSend$setIsSelf:
- _objc_msgSend$setIsTrump:
- _objc_msgSend$setLastActivationTime:
- _objc_msgSend$setMyriadConstantGoodness:
- _objc_msgSend$setMyriadCoordinationEnabled:
- _objc_msgSend$setMyriadDeviceAdjust:
- _objc_msgSend$setMyriadDeviceClass:
- _objc_msgSend$setMyriadDeviceDelay:
- _objc_msgSend$setMyriadDeviceGroup:
- _objc_msgSend$setMyriadDeviceSlowdown:
- _objc_msgSend$setMyriadDeviceTrumpDelay:
- _objc_msgSend$setMyriadDeviceVTEndTimeDistanceThreshold:
- _objc_msgSend$setMyriadMaxNoOperationDelay:
- _objc_msgSend$setMyriadTestDeviceDelay:
- _objc_msgSend$setOverriddenAdjustedScore:
- _objc_msgSend$setOverrideContext:
- _objc_msgSend$setOverrideOption:
- _objc_msgSend$setOverrideState:
- _objc_msgSend$setOverridingContext:
- _objc_msgSend$setPHash:
- _objc_msgSend$setPerceptualAudioHash:
- _objc_msgSend$setPerformDialAssist:
- _objc_msgSend$setPreviousDecision:
- _objc_msgSend$setRawAudioGoodnessScore:
- _objc_msgSend$setRawAudioGoodnessScore:withBump:
- _objc_msgSend$setRawGoodnessScore:
- _objc_msgSend$setRecentAlarmBoost:
- _objc_msgSend$setRecentMotionBoost:
- _objc_msgSend$setRecentPlaybackBoost:
- _objc_msgSend$setRecentRaiseToWakeBoost:
- _objc_msgSend$setRecentSiriRequestBoost:
- _objc_msgSend$setRecentUnlockBoost:
- _objc_msgSend$setRecentlyWonBySmallAmount:
- _objc_msgSend$setThisDevice:
- _objc_msgSend$setTieBreaker:
- _objc_msgSend$setTimeSinceLastDecisionInMs:
- _objc_msgSend$setTrigger:
- _objc_msgSend$setTrumpReason:
- _objc_msgSend$setUserConfidence:
- _objc_msgSend$setWinningDevice:
- _objc_msgSend$setXPCConnectionManagementQueue:
- _objc_msgSend$setupAdvIntervalsInDelay:interval:withSlowdown:
- _objc_msgSend$shouldAbortAnotherDeviceBetter:
- _objc_msgSend$shouldContinue:
- _objc_msgSend$shouldLogForQA
- _objc_msgSend$shouldUnduck:
- _objc_msgSend$slowdownDelay
- _objc_msgSend$slowdownRecord:
- _objc_msgSend$startAdvertisingEmergency
- _objc_msgSend$startAdvertisingFromAlertFiringVoiceTriggerWithContext:
- _objc_msgSend$startAdvertisingFromCarPlayTrigger
- _objc_msgSend$startAdvertisingFromDirectTriggerWithContext:
- _objc_msgSend$startAdvertisingFromInEarTrigger
- _objc_msgSend$startAdvertisingFromInTaskVoiceTrigger
- _objc_msgSend$startAdvertisingFromInTaskVoiceTriggerWithContext:
- _objc_msgSend$startAdvertisingFromOutgoingTriggerWithContext:
- _objc_msgSend$startAdvertisingFromVoiceTrigger
- _objc_msgSend$startAdvertisingFromVoiceTriggerAdjusted:withContext:
- _objc_msgSend$startAdvertisingFromVoiceTriggerWithContext:
- _objc_msgSend$startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:
- _objc_msgSend$startAdvertisingSlowdown:
- _objc_msgSend$startMonitoringWithTimeoutInterval:instanceContext:
- _objc_msgSend$startScanning
- _objc_msgSend$startScanningAndAdvertisingWithData:
- _objc_msgSend$startWatchAdvertisingFromDirectTriggerWithContext:
- _objc_msgSend$startWatchAdvertisingFromVoiceTriggerWithContext:
- _objc_msgSend$stopAdvertising
- _objc_msgSend$stopScanning
- _objc_msgSend$stopScanningAndAdvertising
- _objc_msgSend$submitAccessoryMyriadMetricsToAnalyticsStream:payload:additionalContext:instrumentation:completion:
- _objc_msgSend$takePowerAssertionWithName:
- _objc_msgSend$testDeviceDelay
- _objc_msgSend$tieBreaker
- _objc_msgSend$triggerABCForType:subType:context:
- _objc_msgSend$trumpReason
- _objc_msgSend$updateBoost:value:
- _objc_msgSend$updateIsTrump:withReason:
- _objc_msgSend$userConfidence
- _objc_msgSend$voiceTriggerEndtimeDelayThreshold
- _objc_msgSend$voiceTriggerRecord
- _objc_msgSend$waitWiProx:andExecute:
- _objc_msgSend$willEndSession:
- _objc_msgSend$willStartWithSession:
- _observerWithNotificationName
- _outputTriggerSeenCallback
- _publisherWithNotificationName
- _safelyGetAudioData
- _sharedInstance.metrics
- _sharedMonitor.sharedMonitor
- _strcmp
- _uuid_is_null
- _uuid_unparse_upper
CStrings:
+ "%012llX"
+ "%@ languageCode: %@ name: %@ gender: %@ custom: %@ footprint: %@ contentVersion: %@ masteredVersion: %@ pacePreset: %@ expressivityPreset: %@"
+ "%s #SAEStatus #cacheUpdate Updating cache:\ndeviceSupportsSAE: %d (%d)\n       saeEnabled: %d (%d)\n     saeAvailable: %d (%d)\n      swaiEnabled: %d (%d)\n        viEnabled: %d (%d)\n        saeCapabilities: %{public}@\n        visualIntelligenceCapabilities: %{public}@\n        siriAvailability:\n        %{public}@\n        (%{public}@)"
+ "%s %p sessionId:%@ invocationContext=%@"
+ "%s %s activation=%{public}@"
+ "%s [AFAuthKitManager] No proto account - returning NotSignedIn"
+ "%s [AFAuthKitManager] Proto account age range: Adult"
+ "%s [AFAuthKitManager] Proto account age range: Child"
+ "%s [AFAuthKitManager] Proto account age range: Teen"
+ "%s [AFAuthKitManager] Proto account age range: Unknown"
+ "%s clearContext: called without invocationContext (legacy path)"
+ "%s resumeSessionWithId: called without invocationContext (legacy path), sessionId:%@"
+ "%s siri_signpost_begin `%s`"
+ "-[AFAuthKitManager protoAgeRange]"
+ "-[AFConnection clearContext]"
+ "-[AFConnection resumeSessionWithId:invocationContext:]"
+ "<%@: %p identifier=%@ bundleIdentifier=%@ pid=%d pidVersion=%d>"
+ "<%@: %p invocationSource=%ld targetWindow=%@>"
+ "AppleIntelligenceUseCaseAvailable"
+ "ChildAccountRestricted"
+ "Expressivity1"
+ "Expressivity2"
+ "Expressivity3"
+ "Expressivity4"
+ "Expressivity5"
+ "ExpressivityPreset"
+ "FormFactorSupported"
+ "GreymatterEligible"
+ "MDM"
+ "NotCameraRestricted"
+ "NotChildAccount"
+ "Pace1"
+ "Pace2"
+ "Pace3"
+ "Pace4"
+ "Pace5"
+ "PacePreset"
+ "Q!"
+ "Restricted"
+ "ScreenTimeOrParentalControl"
+ "_blockAttending"
+ "_expressivityPreset"
+ "_invocationContext"
+ "_pacePreset"
+ "allowSiri3489"
+ "invocationSource"
+ "pid"
+ "pidVersion"
+ "restrictionReasons"
+ "targetWindow"
+ "ttr_user_vocab_profile_attachment"
+ "uuid: %@, timestamp: %llu, requestId: %@, turnId: %@, options: %lu, notifyState: %@, text: %@, directAction: %@, handoffOriginDeviceName: %@, handOffData: %@, handoffURL: %@, handoffRequiresUserInteraction: %d, handoffNotification: %@, correctedSpeech: %@, startRequest: %@, activationEvent: %@, invocationSource: %ld, speechRequestOptions: %@, testRequestOptions: %@, requestCompletionOptions: %@, sharedUserID: %@, confidenceScore: %lu, nonspeakerConfidenceScores: %@, SuggestionRequestType: %@, intelligenceFlowActionDescriptor: %@, isAlwaysAllowedWhileDeviceLocked: %@, explicitRequestContext: %@, announcementContext: %@, resumeSessionId: %@, invocationContext: %@"
+ "visualIntelligenceCapabilities"
- "%02x"
- "%2llX"
- "%@ languageCode: %@ name: %@ gender: %@ custom: %@ footprint: %@ contentVersion: %@ masteredVersion: %@"
- "%@ {data = (%llu bytes)}"
- "%@ {generation = %llu, contextData = (%llu bytes), contextFetchDelay = %f}"
- "%@ {generation = %llu, sessionId = %@, currentElectionAdvertisementId = %@, currentElectionAdvertisementData = (%llu bytes), electionAdvertisementDataByIds = %@}"
- "%@ {overrideOption = %@, reason = %@}"
- "%@ {timestamp = %llu, perceptualAudioHash = %@, overrideState = %@, activationSource = %@, activationExpirationTime = %llu}"
- "%hhu"
- "%llu"
- "%llu (%@)"
- "%s #SAEStatus #cacheUpdate Updating cache:\ndeviceSupportsSAE: %d (%d)\n       saeEnabled: %d (%d)\n     saeAvailable: %d (%d)\n      swaiEnabled: %d (%d)\n        viEnabled: %d (%d)\n        siriAvailability:\n        %{public}@\n        (%{public}@)"
- "%s #myriad"
- "%s #myriad %@"
- "%s #myriad BTLE CarPlay trigger signal received"
- "%s #myriad BTLE WiProx readiness timer timed out, WiProx not called"
- "%s #myriad BTLE audio data signal received"
- "%s #myriad BTLE could not open audio data file"
- "%s #myriad BTLE could not read 12 bytes from audio data file"
- "%s #myriad BTLE could open audio data file, MYR_EXT_FINGERPRINT_LEN: %d"
- "%s #myriad BTLE device class: %@ (%@) detected, adjusting goodness by %d incomingAdjustment %d, rawAudioGoodnessScore: %d"
- "%s #myriad BTLE done waiting on WiProx to execute"
- "%s #myriad BTLE emergency signal received"
- "%s #myriad BTLE in ear trigger signal received"
- "%s #myriad BTLE in-task continious voice trigger heard. NOT ignoring."
- "%s #myriad BTLE in-task continuous voice trigger heard too soon. Ignoring."
- "%s #myriad BTLE myriad decision fetch signal received"
- "%s #myriad BTLE not ready, waiting to execute for up to %ld msecs (current HeySiri WPState %ld)"
- "%s #myriad BTLE opening audio file at path %{private}s"
- "%s #myriad BTLE overriding to constant goodness %d"
- "%s #myriad BTLE overriding to goodness %@"
- "%s #myriad BTLE self trigger signal received"
- "%s #myriad CarPlay override"
- "%s #myriad CarPlay override %@"
- "%s #myriad Clearing myriad session %@"
- "%s #myriad Context collector returned 0 AFMyriadAdvertisementContextRecords instances"
- "%s #myriad CurrentTime: %f TrigerTime: %f, ElectionAdvertisementTime: %f, triggerDelta: %f, electionAdvertisementRemainingTime: %f [isIntaskTooSoonForVoiceTriggerActivation = %d, isIntaskTooSoonForDirectActivation = %d, currentElectionAdvertisementIsSane = %d]"
- "%s #myriad Downgrading goodness as HS invocation too soon %f for score %d"
- "%s #myriad Election advertisement %@ -> %@"
- "%s #myriad Election advertisement %@ added to myriad session %@"
- "%s #myriad Error loading Trial factors: %@"
- "%s #myriad Error updating sidekick boosts: unsupported platform"
- "%s #myriad Event token: %@, current event token: %@"
- "%s #myriad Force stopping BTLE scan"
- "%s #myriad Goodness score override state %@"
- "%s #myriad Initialized myriad session %@ when myriad is in state %@"
- "%s #myriad Method called on unexpected thread (curr:%{private}s expected:%{private}s)"
- "%s #myriad Recent Siri Boost Trial Enable Not Loaded"
- "%s #myriad Recent Siri exponential factors not loaded: %@ %@ %@"
- "%s #myriad Suppressing the current device due to late trigger (voicetrigger endtime: %f, advertisement dispatch time: %f, advertisement delay: %f, myriad record count: %ld)"
- "%s #myriad Trial HomePod Boost not loaded: %@"
- "%s #myriad Trial Playback Boost not loaded: %@"
- "%s #myriad WiProx readiness timer initialized"
- "%s #myriad WiProx readiness timer suspended"
- "%s #myriad WiProx readiness timer wait block cleared"
- "%s #myriad Won by a small margin, storing state to mitigate recency boost"
- "%s #myriad _deviceAdjust=%d, adjustment= %d"
- "%s #myriad _voiceTriggerTime: %llu"
- "%s #myriad adjusted score: %ld"
- "%s #myriad alarm/timer bumping is no longer allowed"
- "%s #myriad attention is boosting goodness score, rawAudioGoodnessScore %u, goodness:%u bump: %u, tieBreaker:%u, _myriadState: %@"
- "%s #myriad bumping goodness score (reason: media playback active, adjusted score: %d)"
- "%s #myriad bumping goodness score (reason: media playback interrupted, last playback time: %f seconds ago, adjusted score: %d)"
- "%s #myriad bumping goodness score (reason: platform bias, adjusted bias: %d)"
- "%s #myriad bumptoGoodness secsAgo=%f yields %d = %f(act) + %f(siri)"
- "%s #myriad coordinationEnabled=%d, BLEActivityEnabled=%d "
- "%s #myriad device is unlocked, compute bump"
- "%s #myriad didRequestForBTLEAdvertisement: %s -> %s, didRequestForBTLEScan: %s -> %s"
- "%s #myriad endTime from a file is good, secondsSinceTrigger=%f"
- "%s #myriad endTime from a file is too old, secondsSinceTrigger=%f"
- "%s #myriad exponential bump %f"
- "%s #myriad force win on this device with context: %@, triggerRecord: %@"
- "%s #myriad got attention, ignoring too-soon time limit."
- "%s #myriad ignoring advert from other deviceGroup %d: %@ data=%@"
- "%s #myriad ignoring recent event bump"
- "%s #myriad newGoodness: %d"
- "%s #myriad not initializing myriad session, myriad is in state %@"
- "%s #myriad overrideContext: %@, _incomingAdjustment %d"
- "%s #myriad payload adjusted score: %ld"
- "%s #myriad platform bias acquisition state: %ld"
- "%s #myriad previous close win: canceling recency bump from secsAgo=%f yields %f = %f(act) + %f(siri)"
- "%s #myriad reading defaults"
- "%s #myriad reading defaults: BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, vt_endtime threshold %f"
- "%s #myriad reading server provisioned defaults"
- "%s #myriad removing negative iPad device boost (adding %d back) due to activationSource"
- "%s #myriad requestIdNotification: %@"
- "%s #myriad setupEnabled: %d, current state: %@"
- "%s #myriad trial exponential boost configured, replacing %f with %du"
- "%s #myriad triggerABCForSubType failed: %@"
- "%s #myriad unlock bump is ignored due to awareness being on"
- "%s #myriad updated Trial recent Siri exponential boost to %du %.12f %.12f %.12f"
- "%s #myriad updated _isRecentSiriBoostTrialEnabled to %@"
- "%s #myriad updated _mediaPlaybackBoost to %d"
- "%s #myriad updated platform bias to %d"
- "%s #myriad watch trumping due to score being 0"
- "%s #myriad watch trumping due to threshold for rawAudioGoodnessScore: %u >= %u"
- "%s #myriad-advertisementcontext: Received wedged Myriad advertisement context record %@"
- "%s AFMyriadRecord initfrom: %@ - %@"
- "%s AFMyriadRecord initfrom: <THISDEVICE> - %@"
- "%s AFMyriadRecord invalid data during init: %@"
- "%s AFMyriadRecord sanity: %d"
- "%s Activation source: %ld, Time since activation: %f, last election record received time: %llu, current time: %llu, activation expiration time: %llu"
- "%s Analytics data has a invalid version %d"
- "%s Attempt to initialize MyriadCoordinator when one already exists."
- "%s BTLE %@ timer fires"
- "%s BTLE Attempt to execute time windowed action when trigger time not initialized"
- "%s BTLE Coordinator altered state: %@ -> %@"
- "%s BTLE Coordinator cancelling overall timeout"
- "%s BTLE Coordinator hitting overall timeout, resetting to NoActivity and declaring loss"
- "%s BTLE Coordinator setting overall timeout"
- "%s BTLE Emergency Call: No device available to handle this call"
- "%s BTLE Emergency call: This device should NOT handle, another is better"
- "%s BTLE Emergency call: this device should handle"
- "%s BTLE EmergencyCallSummary %lu: %@"
- "%s BTLE Updating record table with a late supression ( %hhu -> %hhu), data= %@, for %@"
- "%s BTLE Updating record table, data= %@, for %@"
- "%s BTLE action window adjusted by slowdown signal %d msecs new time: %@"
- "%s BTLE action window trigger time: %@"
- "%s BTLE activation time %f"
- "%s BTLE added diagnostic mode timer for %f seconds %@"
- "%s BTLE advertising TEST INDUCED slowdown delay, 2nd pass seen"
- "%s BTLE advertising is being ignored"
- "%s BTLE advertising slowdown delay, 2nd pass seen"
- "%s BTLE advertising slowdown finished, advertising delayed trigger"
- "%s BTLE advertising slowdown: %d msecs"
- "%s BTLE audio hash base directory %{private}@"
- "%s BTLE audio hash file path %{private}@"
- "%s BTLE cancelling diagnostic mode timer for %f seconds %@"
- "%s BTLE checking if slowdown needed testmsecs=%d msecs=%d state=%@"
- "%s BTLE computed advertising delay: %f finished, interval: %f"
- "%s BTLE created slowdown record %@"
- "%s BTLE daemon advertising begins at: %lld"
- "%s BTLE daemon advertising ends at: %lld"
- "%s BTLE daemon advertising overridden and now pending"
- "%s BTLE daemon asked to start advertise at: %lld"
- "%s BTLE daemon failed to start advertising with error %@"
- "%s BTLE daemon failed to start scanning with error %@"
- "%s BTLE daemon scanning begins"
- "%s BTLE daemon scanning ends"
- "%s BTLE daemon state changed to: %ld"
- "%s BTLE daemon wiprox state signalling"
- "%s BTLE delay finished, advertising: %@"
- "%s BTLE delay monitor watchdog timeout %f context %@"
- "%s BTLE detected a slowdown signal for %d msecs, resetting election for later time"
- "%s BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, in_ear delay %f interval %f vt_endtime threshold %f"
- "%s BTLE deviceShouldContinue:%ld (coordinationDisabled:%ld, isDirectlyActivating:%ld, isInEarTrigger:%ld, suppressLateTrigger:%ld."
- "%s BTLE diagnostic mode timer fired"
- "%s BTLE editDist: %d > allowed, ignoring this advert "
- "%s BTLE emergency is being handled"
- "%s BTLE emergencyCallSummary: %@"
- "%s BTLE end advertising summary: %@"
- "%s BTLE ending advertising after %f secs delay"
- "%s BTLE ending slowdown advertising, 2nd pass not seen"
- "%s BTLE entering diagnostic mode"
- "%s BTLE error: attempting to readvertise %@"
- "%s BTLE failed to enter diagnostic mode %@"
- "%s BTLE handling emergency beacon"
- "%s BTLE heard a continuation: %@ data= %@"
- "%s BTLE heard a record waiting for a emergency handled notice: %@ "
- "%s BTLE heard advert from: %@ data= %@"
- "%s BTLE heard an emergency declaration was handled: %@ data= %@"
- "%s BTLE heard an emergency declaration: %@ data= %@"
- "%s BTLE heard another device sending continuation: %@ data= %@"
- "%s BTLE heard slowdown advert from: %@ data= %@, max delay is now %d msecs"
- "%s BTLE ignoring advert from other deviceGroup %d: %@ data= %@"
- "%s BTLE ignoring advert while in state %@: %@ data= %@"
- "%s BTLE ignoring as wedged suppress %@"
- "%s BTLE ignoring decision result callback (state = %@)"
- "%s BTLE ignoring in-task voice trigger and continuing with ongoing advertisement."
- "%s BTLE ignoring incoming event bad device class for Horseman %@"
- "%s BTLE ignoring this advert because one already exists, data= %@, for %@"
- "%s BTLE ignoring watch voice trigger and continuing with ongoing advertisement."
- "%s BTLE in-task voice trigger heard"
- "%s BTLE leaving diagnostic mode"
- "%s BTLE next action window: %@"
- "%s BTLE notify Myriad win due to state machine error"
- "%s BTLE notify myriad loss"
- "%s BTLE notify myriad won"
- "%s BTLE processing advert in state: %lu from: %@ data= %@"
- "%s BTLE record %@  isSane: %d"
- "%s BTLE reposting result win (state = %@)"
- "%s BTLE sending emergency beacon"
- "%s BTLE slowdown advertising delay: %f finished, interval: %f"
- "%s BTLE startFromVoiceTrigger inTask=%d, inSetupMode=%d, context=%@"
- "%s BTLE startFromVoiceTrigger inTask=%d, inSetupMode=%d, incomingAdjustment=%d,  context=%@, goodnessScoreContext=%@"
- "%s BTLE starting %@ timer for %f secs"
- "%s BTLE starting advert delay timer for %f secs"
- "%s BTLE stopping advertising HeySiri advertisements"
- "%s BTLE stopping advertising and scanning of HeySiri advertisements"
- "%s BTLE stopping to scan HeySiri advertisements"
- "%s BTLE summary %lu: %@"
- "%s BTLE suppressing straggler response to: %@ data= %@"
- "%s BTLE suppressing stragglers"
- "%s BTLE suppressing trigger in audio output"
- "%s BTLE task MYR_WAIT_EMERGENCY_HANDLED only stopping advertising, not listening"
- "%s BTLE task MYR_WAIT_EMERGENCY_OR_TASK only stopping advertising, not listening"
- "%s BTLE task continuation: %d"
- "%s BTLE timer %@ cancelled (%@)"
- "%s BTLE trumping"
- "%s BTLE trumping from in CarPlay trigger"
- "%s BTLE trumping from in ear voice trigger"
- "%s BTLE unable to cancel against: %@"
- "%s BTLE voice trigger during alert heard"
- "%s BTLE voice trigger while inTask with context: %@"
- "%s Bad data of unexpected length %@ : %@"
- "%s Clear pending for Myriad decision: %@."
- "%s Coordination disabled, continuing with the request)"
- "%s Dequeueing command for Myriad decision: %@ (reason = %@)."
- "%s Dequeuing after %f seconds for Myriad decision (reason = %@) and dequeue signal %zd."
- "%s Emergency beacon handling created dial request %@"
- "%s Emergency beacon initiated call created: %@"
- "%s Emergency beacon initiated call failed, error: %@"
- "%s Emitting Myriad RequestLinkEvent with requestId: %@, cdaId: %@"
- "%s Generated Myriad advertisement context data: %lu bytes"
- "%s Generated myriad hash: %hu"
- "%s Initialized MyriadCoordinator"
- "%s Initializing Myriad advertisement context (version: %d)"
- "%s Invalid Voicetrigger endtime: %f"
- "%s Invalid analytics data payload: %@"
- "%s Invalid analytics data received"
- "%s Invalid analytics stream."
- "%s Myriad Delay Monitor Begin (%@)"
- "%s Myriad Delay Monitor received reposted result: YES (%@)"
- "%s Myriad Delay Monitor result: NO (%@)"
- "%s Myriad Delay Monitor result: YES (%@)"
- "%s Myriad Delay Monitor: Deregistering from Myriad event notifications."
- "%s Myriad Delay Monitor: Deregistering from reposted Myriad event notification."
- "%s Myriad Delay Monitor: Fetching reposted Myriad event notification."
- "%s Myriad Delay Monitor: Ignoring Myriad repost notifications."
- "%s Myriad Delay Monitor: Registering for Myriad event notifications (beginObserver: %p, wonObserver: %p, lostObserver: %p, decisionRepostObserver: %p)."
- "%s Myriad Delay Monitor: Should ignoring Myriad events -> %d."
- "%s Myriad decision had %d block(s) waiting"
- "%s Myriad decision is already in pending state."
- "%s Myriad decision is based on 0 replies"
- "%s Myriad decision is pending."
- "%s Myriad decision seen: state is %@."
- "%s Myriad endpoint metrics context: %@"
- "%s Myriad monitor cancelling existing watch dog timer."
- "%s Myriad monitor initializing safety timer with timeout: %f seconds"
- "%s Myriad monitor times out, Myriad is probably unable to finish, clear pending blocks"
- "%s No longer used by this device."
- "%s Not yet supported on this device."
- "%s Notification received: %@ (%d)"
- "%s Preheat shows slowdown for this device as %d msecs"
- "%s Punching out to Phone app to make emergency call"
- "%s Queueing command waiting for Myriad decision: %@ (reason = %@)."
- "%s Received a payload %@ with session id %@ for accessory id: %@, Ignoring."
- "%s Skipped emitting RequestLinkEvent as requestId or cdaId is nil"
- "%s Trial Boosts Updated Notification"
- "%s Unable to find sidekick boosts plist at path %@."
- "%s Unable to initialize sidekick boosts from plist file at path %@ due to error %@"
- "%s Unable to read sidekick boosts plist file at path %@."
- "%s Unexpected type of initialized sidekick boosts plist %@."
- "%s Unknown request type %@ for accessory id: %@, Ignoring."
- "%s VoicetriggerEndtime isSane: %d (threshold: %f, me: %f, other: %f, abs-diff: %f adv: %@)"
- "%s Waiting for wiprox to be ready in state: %lu"
- "%s Wedged message received with version: %hhu and message length: %zu"
- "%s [(rawAudioGoodnessScore + bump) overflow] rawAudioGoodnessScore: %d, bump: %d. Overwriting goodness score to 0xff"
- "%s _readSidekickBoostsFile: called with empty filepath"
- "%s adjusted advInterval: %f (secs) adjusted delay: %f (secs), slowDown: %f (secs)"
- "%s adjusted advInterval: %f (secs) device delay: %f (secs), slowDown: %f (secs)"
- "%s boostType: %@, boostValue:%d"
- "%s cdaId: %@, state: %@"
- "%s cdaId: %@, state: %@, arbitrationAllowed: %d, deviceGroup: %d, advertisements: %@"
- "%s cdaId: %@, state: %@, trigger: %@"
- "%s cdaId: %@, state: %@, withDecision: %@, withPreviousDecision: %@, timeSincePreviousDecision: %llu, withWinningDevice: %@ (score: %d), withThisDevice: %@ (score: %d), withParticipants: %@, withRawScore:%u, withBoost:%@, withTrumpReason:%@"
- "%s currentTime=%llu timeSinceActivationInSeconds=%f"
- "%s data=%@, hash=%hu, good=%hu, conf=%hu, absTime=%llu, frac=%hu"
- "%s data=%@, voiceTriggerTimeRaw=%f"
- "%s data=%@, voiceTriggerTimeRaw=%llu, secondsSinceTrigger=%f"
- "%s endTime: %f targetTime: %f, advInterval: %f, slowDown: %d (ms)"
- "%s fromState: %@, myriadState: %@, is _clientIsDeciding: %d"
- "%s fromState: %@, myriadState: %@, is _clientIsDeciding: %d, _voiceTriggerTime: %llu, secondsSinceVoiceTrigger: %f"
- "%s inTask=%d"
- "%s notifyObserver %p didChangeStateFrom %ld -> %ld"
- "%s rawAudioGoodnessScore: %d, bump: %d goodness: %d"
- "%s starting to scan in state: %lu"
- "%s trump: %d, with Reason:%@"
- "%s version = %u analytics stream = %p additional = [%@]"
- "-[AFMyriadAccessoryMessage _initializeMessageObj:]"
- "-[AFMyriadAccessoryMessage _initializeMessageObjFromDictionary:]"
- "-[AFMyriadAccessoryMetricMessage _decodeMetricDataPayload:decodedPayload:]"
- "-[AFMyriadAdvertisementContextManager reset]"
- "-[AFMyriadAdvertisementContextManager triggerABCForType:subType:context:]_block_invoke_2"
- "-[AFMyriadAdvertisementContextRecord _initializeMyriadAdvertisementContextRecordFromData:]"
- "-[AFMyriadAdvertisementContextRecord isSaneForVoiceTriggerEndTime:endtimeDistanceThreshold:]"
- "-[AFMyriadAdvertisementContextRecord myriadAdvertisementContextAsData]"
- "-[AFMyriadCoordinator _addElectionAdvertisementDataToMyriadSession:]"
- "-[AFMyriadCoordinator _adjustActionWindowsFromSlowdown:]"
- "-[AFMyriadCoordinator _advertiseIndefinite:]_block_invoke"
- "-[AFMyriadCoordinator _advertiseSlowdown]"
- "-[AFMyriadCoordinator _advertiseSlowdown]_block_invoke"
- "-[AFMyriadCoordinator _advertiseSuppressTriggerInOutput]"
- "-[AFMyriadCoordinator _advertiseSuppressTriggerInOutput]_block_invoke"
- "-[AFMyriadCoordinator _advertiseTrigger]"
- "-[AFMyriadCoordinator _advertiseTrigger]_block_invoke"
- "-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]"
- "-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke"
- "-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke_2"
- "-[AFMyriadCoordinator _cancelOverallTimeout]"
- "-[AFMyriadCoordinator _cancelTimer]"
- "-[AFMyriadCoordinator _clearMyriadSession]"
- "-[AFMyriadCoordinator _clearMyriadSession]_block_invoke"
- "-[AFMyriadCoordinator _clearWiProxReadinessTimer]"
- "-[AFMyriadCoordinator _createDispatchTimerWithTime:toExecute:]_block_invoke"
- "-[AFMyriadCoordinator _createMyriadSessionIfRequired]"
- "-[AFMyriadCoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke"
- "-[AFMyriadCoordinator _deviceShouldContinue:]"
- "-[AFMyriadCoordinator _duringNextWindowExecute:]"
- "-[AFMyriadCoordinator _endAdvertising:]"
- "-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]"
- "-[AFMyriadCoordinator _endAdvertisingWithDeviceProhibitions:]"
- "-[AFMyriadCoordinator _enterBLEDiagnosticMode]"
- "-[AFMyriadCoordinator _enterBLEDiagnosticMode]_block_invoke"
- "-[AFMyriadCoordinator _enterState:]"
- "-[AFMyriadCoordinator _forceLocalWinner:]_block_invoke"
- "-[AFMyriadCoordinator _handleStateMachineErrorIfNeeded]"
- "-[AFMyriadCoordinator _inTaskTriggerWasTooSoon]"
- "-[AFMyriadCoordinator _initDeviceClassAndAdjustments]"
- "-[AFMyriadCoordinator _initializeTimer]"
- "-[AFMyriadCoordinator _initializeWiProxReadinessTimer]"
- "-[AFMyriadCoordinator _leaveBLEDiagnosticMode]"
- "-[AFMyriadCoordinator _loseElection]"
- "-[AFMyriadCoordinator _readDefaults]"
- "-[AFMyriadCoordinator _setOverallTimeout]"
- "-[AFMyriadCoordinator _setOverallTimeout]_block_invoke"
- "-[AFMyriadCoordinator _setupActionWindows]"
- "-[AFMyriadCoordinator _shouldContinueFor:]"
- "-[AFMyriadCoordinator _shouldContinueFor:]_block_invoke"
- "-[AFMyriadCoordinator _shouldHandleEmergency]"
- "-[AFMyriadCoordinator _shouldHandleEmergency]_block_invoke"
- "-[AFMyriadCoordinator _signalEmergencyCallHandled]"
- "-[AFMyriadCoordinator _startAdvertisingFromInTaskVoiceTrigger]"
- "-[AFMyriadCoordinator _startAdvertisingFromVoiceTrigger]"
- "-[AFMyriadCoordinator _startListening:]"
- "-[AFMyriadCoordinator _startListeningAfterWiProxIsReady:inState:completion:]"
- "-[AFMyriadCoordinator _startListeningAfterWiProxIsReady:inState:completion:]_block_invoke"
- "-[AFMyriadCoordinator _startTimer:for:thenExecute:]"
- "-[AFMyriadCoordinator _startTimer:for:thenExecute:]_block_invoke"
- "-[AFMyriadCoordinator _stopAdvertising:]"
- "-[AFMyriadCoordinator _stopAdvertising:]_block_invoke"
- "-[AFMyriadCoordinator _stopAdvertisingAndListening]_block_invoke"
- "-[AFMyriadCoordinator _stopListening:]"
- "-[AFMyriadCoordinator _stopListening:]_block_invoke"
- "-[AFMyriadCoordinator _suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:]_block_invoke"
- "-[AFMyriadCoordinator _suspendWiProxReadinessTimer]"
- "-[AFMyriadCoordinator _testAndFilterAdvertisementsFromContextCollector:voiceTriggerEndTime:advertisementDispatchTime:advertisement:]"
- "-[AFMyriadCoordinator _testAndFilterAdvertisementsFromContextCollector:voiceTriggerEndTime:advertisementDispatchTime:advertisement:]_block_invoke"
- "-[AFMyriadCoordinator _testAndUpdateWedgeFilter:]"
- "-[AFMyriadCoordinator _updateRepliesWith:id:data:]"
- "-[AFMyriadCoordinator _updateVoiceTriggerTimeFromFile]"
- "-[AFMyriadCoordinator _waitWiProx:andExecute:]"
- "-[AFMyriadCoordinator _waitWiProx:andExecute:]_block_invoke"
- "-[AFMyriadCoordinator _winElection]"
- "-[AFMyriadCoordinator endAdvertisingAfterDelay:]_block_invoke_2"
- "-[AFMyriadCoordinator endTask]_block_invoke"
- "-[AFMyriadCoordinator faceDetectedBoostWithMyriadContext:]_block_invoke"
- "-[AFMyriadCoordinator heySiri:failedToStartAdvertisingWithError:]"
- "-[AFMyriadCoordinator heySiri:failedToStartScanningWithError:]"
- "-[AFMyriadCoordinator heySiri:foundDevice:withInfo:]"
- "-[AFMyriadCoordinator heySiri:foundDevice:withInfo:]_block_invoke"
- "-[AFMyriadCoordinator heySiriAdvertisingPending:]"
- "-[AFMyriadCoordinator heySiriDidUpdateState:]"
- "-[AFMyriadCoordinator heySiriDidUpdateState:]_block_invoke"
- "-[AFMyriadCoordinator heySiriStartedAdvertising:]"
- "-[AFMyriadCoordinator heySiriStartedAdvertisingAt:timeStamp:]"
- "-[AFMyriadCoordinator heySiriStartedScanning:]"
- "-[AFMyriadCoordinator heySiriStoppedAdvertising:]"
- "-[AFMyriadCoordinator heySiriStoppedScanning:]"
- "-[AFMyriadCoordinator initWithDelegate:]"
- "-[AFMyriadCoordinator notifyCurrentDecisionResult]_block_invoke"
- "-[AFMyriadCoordinator notifyObserver:didReceiveNotificationWithToken:]"
- "-[AFMyriadCoordinator preheatWiProx]_block_invoke"
- "-[AFMyriadCoordinator setInTask:]_block_invoke"
- "-[AFMyriadCoordinator setupAdvIntervalsInDelay:interval:withSlowdown:]"
- "-[AFMyriadCoordinator setupEnabled:]_block_invoke"
- "-[AFMyriadCoordinator slowdownRecord:]"
- "-[AFMyriadCoordinator startAdvertisingEmergencyHandled]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingEmergency]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingForPHSSetupAfterDelay:maxInterval:]"
- "-[AFMyriadCoordinator startAdvertisingFromAlertFiringVoiceTriggerWithContext:]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingFromCarPlayTrigger]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingFromDirectTriggerWithContext:]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingFromInEarTrigger]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingFromInTaskVoiceTriggerWithContext:]"
- "-[AFMyriadCoordinator startAdvertisingFromOutgoingTriggerWithContext:]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingFromVoiceTriggerAdjusted:withContext:]"
- "-[AFMyriadCoordinator startAdvertisingFromVoiceTriggerWithContext:]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:]_block_invoke"
- "-[AFMyriadCoordinator startAdvertisingSlowdown:]_block_invoke"
- "-[AFMyriadCoordinator startResponseAdvertising:]_block_invoke"
- "-[AFMyriadCoordinator startWatchAdvertisingFromDirectTriggerWithContext:]_block_invoke"
- "-[AFMyriadCoordinator startWatchAdvertisingFromVoiceTriggerWithContext:]_block_invoke"
- "-[AFMyriadCoordinator updateRequestId:]_block_invoke"
- "-[AFMyriadEmergencyCallPunchout initiateEmergencyCallMyriad]_block_invoke"
- "-[AFMyriadGoodnessScoreEvaluator _bumpGoodnessScore:lastActivationTime:mediaPlaybackInterruptedTime:ignoreAdjustedBoost:recentlyWonBySmallAmount:]"
- "-[AFMyriadGoodnessScoreEvaluator _getRecentBump:ignoreAdjustedBoost:recentlyWonBySmallAmount:]"
- "-[AFMyriadGoodnessScoreEvaluator _readSidekickBoostsFile:]"
- "-[AFMyriadGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]_block_invoke"
- "-[AFMyriadGoodnessScoreEvaluator _settingsConnectionDidDisconnect]_block_invoke"
- "-[AFMyriadGoodnessScoreEvaluator _updateMediaPlaybackBoost:]"
- "-[AFMyriadGoodnessScoreEvaluator _updatePlatformBias:]"
- "-[AFMyriadGoodnessScoreEvaluator _updateRecentSiriBoostTrialEnabled:]"
- "-[AFMyriadGoodnessScoreEvaluator _updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:]"
- "-[AFMyriadGoodnessScoreEvaluator _updateSidekickBoosts:]"
- "-[AFMyriadGoodnessScoreEvaluator getMyriadAdjustedBoostForGoodnessScoreContext:]"
- "-[AFMyriadGoodnessScoreEvaluator getPlatformBias]"
- "-[AFMyriadGoodnessScoreEvaluator myriadTrialBoostsUpdated:]_block_invoke"
- "-[AFMyriadInstrumentation _logRequestLinkMessageRequestId:cdaId:]"
- "-[AFMyriadInstrumentation _logRequestLinkMessageRequestId:cdaId:]_block_invoke"
- "-[AFMyriadInstrumentation logCDADeviceStateActivityEnded:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDADeviceStateActivityStartedOrChanged:withTrigger:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionAdvertisingEnded:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionAdvertisingEnding:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionAdvertisingStarted:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionAdvertisingStarting:withDelay:withInterval:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionDecisionMade:withDecision:withPreviousDecision:timeSincePreviousDecision:withWinningDevice:withThisDevice:withParticipants:withRawScore:withBoost:withCdaId:currentRequestId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionDecisionMadeDebug:withCrossDeviceArbitrationAllowed:advertisementData:withDeviceGroup:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation logCDAElectionTimerEnded:withCdaId:withTimestamp:]_block_invoke"
- "-[AFMyriadInstrumentation updateBoost:value:]_block_invoke"
- "-[AFMyriadInstrumentation updateIsTrump:withReason:]_block_invoke"
- "-[AFMyriadMetrics _submitMyriadMetrics:additionalContext:toStream:instrumentation:completion:]"
- "-[AFMyriadMetrics submitAccessoryMyriadMetricsToAnalyticsStream:payload:additionalContext:instrumentation:completion:]"
- "-[AFMyriadMonitor _clear]"
- "-[AFMyriadMonitor _dequeueBlocksWithSignal:]"
- "-[AFMyriadMonitor _deregisterFromMyriadEventNotifications]"
- "-[AFMyriadMonitor _deregisterFromRepostedDecisionResultsObservers]"
- "-[AFMyriadMonitor _enqueueBlock:forReason:]"
- "-[AFMyriadMonitor _enqueueBlock:forReason:]_block_invoke"
- "-[AFMyriadMonitor _fetchCurrentMyriadDecisionWithWaitTime:]"
- "-[AFMyriadMonitor _fetchCurrentMyriadDecisionWithWaitTime:]_block_invoke"
- "-[AFMyriadMonitor _registerForMyriadEvents]"
- "-[AFMyriadMonitor _resultSeenWithValue:]"
- "-[AFMyriadMonitor _setDecisionIsPending]"
- "-[AFMyriadMonitor _setDecisionIsPending]_block_invoke"
- "-[AFMyriadMonitor dequeueBlocksWaitingForMyriadDecision]_block_invoke"
- "-[AFMyriadMonitor ignoreMyriadEvents:]_block_invoke"
- "-[AFMyriadMonitor notifyObserver:didChangeStateFrom:to:]"
- "-[AFMyriadMonitor notifyObserver:didReceiveNotificationWithToken:]"
- "-[AFMyriadMonitor startMonitoringWithTimeoutInterval:instanceContext:]_block_invoke"
- "-[AFMyriadRecord adjustByMultiplier:adding:]"
- "-[AFMyriadRecord initWithAudioData:]"
- "-[AFMyriadRecord initWithDeviceID:data:]"
- "-[AFMyriadRecord isSane]"
- "-[AFMyriadRecord setRawAudioGoodnessScore:withBump:]"
- "/System/Library/PrivateFrameworks/Sharing.framework/Sharing"
- "/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity"
- "00000000-0000-0000-0000-%012u"
- "1 (ACKNOWLEDGEMENT)"
- "<AFMYR_State_ERROR>"
- "ACK"
- "AFCDABoostTypeAlarmAndTimerFiring"
- "AFCDABoostTypeDevice"
- "AFCDABoostTypeRecentMotion"
- "AFCDABoostTypeRecentPlayback"
- "AFCDABoostTypeRecentRaiseToWake"
- "AFCDABoostTypeRecentRequest"
- "AFCDABoostTypeUnknown"
- "AFCDABoostTypeUnlock"
- "AFMyriadAdvertisementContext::contextData"
- "AFMyriadAdvertisementContext::contextFetchDelay"
- "AFMyriadAdvertisementContext::generation"
- "AFMyriadAdvertisementContextRecord: contextVersion=%ld vtEndTime=%f advRecordType=%ld advPayload=0x%@ deviceID=%@"
- "AFMyriadContext::activationExpirationTime"
- "AFMyriadContext::activationSource"
- "AFMyriadContext::overrideState"
- "AFMyriadContext::perceptualAudioHash"
- "AFMyriadContext::timestamp"
- "AFMyriadCoordinator.m"
- "AFMyriadCoordinatorAudioHashFileBaseDirectory"
- "AFMyriadCoordinatorAudioHashFilePath"
- "AFMyriadEmergencyCallPunchout.m"
- "AFMyriadGoodnessComputeExponentialBoost"
- "AFMyriadGoodnessScoreOverrideState::overrideOption"
- "AFMyriadGoodnessScoreOverrideState::reason"
- "AFMyriadPerceptualAudioHash::data"
- "AFMyriadSession::currentElectionAdvertisementData"
- "AFMyriadSession::currentElectionAdvertisementId"
- "AFMyriadSession::electionAdvertisementDataByIds"
- "AFMyriadSession::generation"
- "AFMyriadSession::sessionId"
- "AlertFiringVoiceTrigger"
- "AudioHash"
- "Bridge"
- "CDADECISION_LOSS"
- "CDADECISION_UNKNOWN"
- "CDADECISION_WIN"
- "CDASTATE_ADVERT_CONTINUATION"
- "CDASTATE_ADVERT_EMERGENCY"
- "CDASTATE_ADVERT_HANDLED"
- "CDASTATE_ADVERT_OUTPUT_TRIGGER"
- "CDASTATE_ADVERT_SLOWDOWN"
- "CDASTATE_ADVERT_SUPPRESS"
- "CDASTATE_ADVERT_SUPPRESS_LATE"
- "CDASTATE_ADVERT_TRAINING"
- "CDASTATE_ADVERT_TRIGGER"
- "CDASTATE_INIT_FILTERS"
- "CDASTATE_LISTEN_EMERGENCY"
- "CDASTATE_LISTEN_LATE"
- "CDASTATE_LISTEN_TASK"
- "CDASTATE_NO_ACTIVITY"
- "CDASTATE_PREHEAT"
- "CDASTATE_UNKNOWN"
- "CDASTATE_WAIT_EMERGENCY_HANDLED"
- "CDASTATE_WAIT_EMERGENCY_OR_TASK"
- "CDASTATE_WAIT_TASK"
- "CDATRIGGER_ALERT_FIRING_VOICE_TRIGGER"
- "CDATRIGGER_CARPLAY_TRIGGER"
- "CDATRIGGER_DIRECT_TRIGGER"
- "CDATRIGGER_EMERGENCY_TRIGGER"
- "CDATRIGGER_IN_EAR_TRIGGER"
- "CDATRIGGER_IN_TASK_VOICE_TRIGGER"
- "CDATRIGGER_OUTGOING_TRIGGER"
- "CDATRIGGER_UKNOWN"
- "CDATRIGGER_VOICE_TRIGGER"
- "CDATRUMPREASON_ALARM_FIRING"
- "CDATRUMPREASON_DIRECT_TRIGGER"
- "CDATRUMPREASON_FACE_DETECTED"
- "CDATRUMPREASON_IN_TASK_TRIGGER"
- "CDATRUMPREASON_OUTGOING_TRIGGER"
- "CDATRUMPREASON_PERSONALIZED_HEY_SIRI_SETUP"
- "CDATRUMPREASON_RAISE_TO_SPEAK"
- "CDATRUMPREASON_THRESHOLD_REACHED"
- "CDATRUMPREASON_UNKNOWN"
- "CarPlay request"
- "CarPlayTrigger"
- "DeviceClass"
- "DeviceGroup"
- "DirectTrigger"
- "ElectionDecision"
- "Emergency"
- "EmergencyHandled"
- "FALSE"
- "GoodnessScore"
- "HOMEPOD_BOOST"
- "InEarTrigger"
- "InTaskVoiceTrigger"
- "Library/VoiceTrigger"
- "Lost"
- "MYR_ADVERT_CONT"
- "MYR_ADVERT_EMERGENCY"
- "MYR_ADVERT_HANDLED"
- "MYR_ADVERT_OUTGOING_TRIGGER"
- "MYR_ADVERT_SLOWDOWN"
- "MYR_ADVERT_SUPPRESS"
- "MYR_ADVERT_SUPPRESS_LATE"
- "MYR_ADVERT_TRIGGER"
- "MYR_INIT_FILTERS"
- "MYR_LISTEN_EMERGENCY"
- "MYR_LISTEN_LATE"
- "MYR_LISTEN_TASK"
- "MYR_NOACTIVITY"
- "MYR_PREHEAT"
- "MYR_WAIT_EMERGENCY_HANDLED"
- "MYR_WAIT_EMERGENCY_OR_TASK"
- "MYR_WAIT_TASK"
- "MyriadRecord: hash=%#04x,good=%d,conf=%d,dc=%d,pt=%d,tb=%d,isMe=%@,g=%d,cc=%d"
- "OutgoingTrigger"
- "Pending"
- "RECENT_PLAYBACK_BOOST"
- "RECENT_SIRI_BOOST_FIRST_DEGREE_COEFF"
- "RECENT_SIRI_BOOST_INTERCEPT"
- "RECENT_SIRI_BOOST_SECOND_DEGREE_COEFF"
- "RECENT_SIRI_BOOST_TRIAL_ENABLE"
- "RequestType"
- "SFDiagnostics"
- "SharingLibrary"
- "TRUE"
- "TUCallProviderManager"
- "TUCallSourceIdentifierSpeakerRoute"
- "TUDialRequest"
- "TieBreaker"
- "UserConfidence"
- "VoiceTrigger endtime"
- "WPHeySiri"
- "WPHeySiriAdvertisingData"
- "WPHeySiriKeyManufacturerData"
- "WirelessProximityLibrary"
- "Won"
- "_generateRandomHash"
- "_myriadWorkQueue"
- "aData"
- "accessoryMetrics"
- "ack"
- "activationExpirationTime"
- "activationSource"
- "adv-delay"
- "adv-interval"
- "advert delay"
- "advertise"
- "advertisementDispatchTime"
- "alarmAndTimerFiring"
- "carplayTriggerSeenCallback"
- "classSFDiagnostics"
- "classWPHeySiri"
- "com.apple.assistant.myriad"
- "com.apple.assistant.myriad.delay_monitor"
- "com.apple.assistant.myriad.instrumentation"
- "com.apple.deviceArbitration"
- "com.apple.myriad_adv_context"
- "com.apple.myriad_attention"
- "com.apple.myriad_emergncy_call"
- "com.apple.myriad_readiness"
- "com.apple.myriad_timer_mgmt"
- "com.apple.myriad_work"
- "com.apple.siri.corespeech.selftrigger"
- "com.apple.siri.myriad.apayload"
- "com.apple.siri.myriad.decision.begin"
- "com.apple.siri.myriad.decision.lost"
- "com.apple.siri.myriad.decision.won"
- "com.apple.siri.myriad.falseemergency"
- "com.apple.siri.myriad.force.noactivity.state"
- "com.apple.siri.myriad.get.decision"
- "com.apple.siri.myriad.in.ear"
- "com.apple.siri.myriad.jarvis"
- "com.apple.siri.myriad.readdefaults"
- "com.apple.siri.myriad.repost.decision.won"
- "contextData"
- "contextFetchDelay"
- "continuation"
- "coordination_allowed"
- "counts"
- "currentElectionAdvertisementData"
- "currentElectionAdvertisementId"
- "dInfo"
- "dc"
- "decision"
- "delay"
- "device-group"
- "device_arbitration_delay"
- "device_count"
- "direct"
- "directTrigger"
- "eDecision"
- "election"
- "electionAdvertisementDataByIds"
- "emergency"
- "emergencyCallback"
- "emergencyHandled"
- "end advert delay"
- "extractMyriadDataFromAudioContext"
- "filter initialization timer"
- "goodness"
- "goodness_scores"
- "hash=%#04x"
- "hh:mm:ss.SSS"
- "hi-Latn"
- "homepod_involved"
- "iSane"
- "inEarTrigger"
- "inEarTriggerSeenCallback"
- "initSFDiagnostics_block_invoke"
- "initTUCallSourceIdentifierSpeakerRoute_block_invoke"
- "initWPHeySiriAdvertisingData_block_invoke"
- "initWPHeySiriKeyManufacturerData_block_invoke"
- "initWPHeySiri_block_invoke"
- "late_for_device_arbitration"
- "listen"
- "listen emergency handled"
- "listen late"
- "listen wait/emergency"
- "listening late"
- "max_slowdown"
- "mediaPlaybackStateInterrupted"
- "mediaPlaybackStatePlaying"
- "my_device_class"
- "my_goodness"
- "my_product_type"
- "myrRequestTypeAdvertiseEmergency"
- "myrRequestTypeContiniousVoiceTrigger"
- "myrRequestTypeDeviceFound"
- "myrRequestTypeDirectTrigger"
- "myrRequestTypeElectionDecision"
- "myrRequestTypeEmergencyHandledStatus"
- "myrRequestTypePreheat"
- "myrRequestTypeReset"
- "myrRequestTypeSelfTrigger"
- "myrRequestTypeUnknown"
- "myrRequestTypeVoiceTrigger"
- "myriadDecisionRequestCallback"
- "notificationCallback"
- "other"
- "outputTriggerSeenCallback"
- "overrideOption"
- "overrideState"
- "perceptualAudioHash"
- "preheat timer"
- "previous_decision"
- "previous_decision_time"
- "pt"
- "raw Goodness = %d, boosted goodness = %d  class = %d, product type = %d"
- "raw_goodness_score"
- "reasons: %@, playback interrupted time: %f"
- "reqType"
- "safelyGetAudioData"
- "session_id"
- "sid"
- "siriBC"
- "slowDown"
- "state_machine_error"
- "suppressLate"
- "trigger"
- "usesSerializedProtocol"
- "uuid: %@, timestamp: %llu, requestId: %@, turnId: %@, options: %lu, notifyState: %@, text: %@, directAction: %@, handoffOriginDeviceName: %@, handOffData: %@, handoffURL: %@, handoffRequiresUserInteraction: %d, handoffNotification: %@, correctedSpeech: %@, startRequest: %@, activationEvent: %@, invocationSource: %ld, speechRequestOptions: %@, testRequestOptions: %@, requestCompletionOptions: %@, sharedUserID: %@, confidenceScore: %lu, nonspeakerConfidenceScores: %@, SuggestionRequestType: %@, intelligenceFlowActionDescriptor: %@, isAlwaysAllowedWhileDeviceLocked: %@, explicitRequestContext: %@, announcementContext: %@, resumeSessionId: %@"
- "v16@?0@\"<AFMyriadAdvertisementContextMutating>\"8"
- "v16@?0@\"<AFMyriadContextMutating>\"8"
- "v16@?0@\"<AFMyriadGoodnessScoreOverrideStateMutating>\"8"
- "v16@?0@\"<AFMyriadPerceptualAudioHashMutating>\"8"
- "v16@?0@\"<AFMyriadSessionMutating>\"8"
- "v24@?0@\"NSData\"8@?<v@?>16"
- "v32@?0@\"AFMyriadRecord\"8Q16^B24"
- "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
- "v32@?0@\"NSUUID\"8@\"AFMyriadAdvertisementContextRecord\"16^B24"
- "v32@?0@\"NSUUID\"8@\"NSData\"16^B24"
- "v32@?0@8@\"AFMyriadRecord\"16^B24"
- "voiceTriggerEndTime"
- "wait until after suppress"
- "watch1,1"
- "watch1,2"
- "winner_device_class"
- "winner_goodness"
- "winner_product_type"
- "winner_sent_suppresssion"
- "\xa1"
- "\xb1"

```
