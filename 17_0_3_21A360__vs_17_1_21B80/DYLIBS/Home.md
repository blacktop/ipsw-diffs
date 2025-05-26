## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

-803.3.7.1.5
-  __TEXT.__text: 0x2ec614
-  __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_methlist: 0x26b3c
+825.2.8.1.1
+  __TEXT.__text: 0x2ee5d8
+  __TEXT.__auth_stubs: 0x20f0
+  __TEXT.__objc_methlist: 0x26c7c
   __TEXT.__const: 0x2238
-  __TEXT.__cstring: 0x347b2
+  __TEXT.__cstring: 0x347ce
   __TEXT.__swift5_typeref: 0x117c
   __TEXT.__swift5_reflstr: 0x53a
   __TEXT.__swift5_assocty: 0x210

   __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_capture: 0x3d4
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__oslogstring: 0x17fe4
-  __TEXT.__gcc_except_tab: 0x3da4
+  __TEXT.__oslogstring: 0x183db
+  __TEXT.__gcc_except_tab: 0x3ed0
   __TEXT.__ustring: 0x88
   __TEXT.__dlopen_cstrs: 0x4b
-  __TEXT.__unwind_info: 0xcdc8
-  __TEXT.__eh_frame: 0x1d88
+  __TEXT.__unwind_info: 0xce6c
+  __TEXT.__eh_frame: 0x1dd8
   __TEXT.__objc_classname: 0x68ac
-  __TEXT.__objc_methname: 0x54cce
-  __TEXT.__objc_methtype: 0x7531
-  __TEXT.__objc_stubs: 0x37420
+  __TEXT.__objc_methname: 0x552a8
+  __TEXT.__objc_methtype: 0x756e
+  __TEXT.__objc_stubs: 0x376a0
   __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x10408
+  __DATA_CONST.__const: 0x10450
   __DATA_CONST.__objc_classlist: 0x16c8
   __DATA_CONST.__objc_catlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x38e00
-  __DATA_CONST.__objc_selrefs: 0x113d8
+  __DATA_CONST.__objc_const: 0x38f58
+  __DATA_CONST.__objc_selrefs: 0x114b8
   __DATA_CONST.__objc_arraydata: 0x348
   __AUTH_CONST.__const: 0xcaf0
   __AUTH_CONST.__auth_ptr: 0xa0
-  __AUTH_CONST.__objc_const: 0x14260
+  __AUTH_CONST.__objc_const: 0x142a8
   __AUTH_CONST.__cfstring: 0x255a0
   __AUTH_CONST.__objc_intobj: 0x2070
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1080
+  __AUTH_CONST.__auth_got: 0x1088
   __AUTH.__objc_data: 0xa298
   __AUTH.__data: 0x4f8
   __DATA.__objc_protorefs: 0x320
   __DATA.__objc_classrefs: 0x1b58
   __DATA.__objc_superrefs: 0x12b0
-  __DATA.__objc_ivar: 0x1474
+  __DATA.__objc_ivar: 0x1480
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x74d8
+  __DATA.__data: 0x74c8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x20d8
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_ivar: 0xc24
+  __DATA_DIRTY.__objc_ivar: 0xc38
   __DATA_DIRTY.__objc_data: 0x4ee8
   __DATA_DIRTY.__data: 0x240
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18148
-  Symbols:   54520
-  CStrings:  22453
+  Functions: 18177
+  Symbols:   54606
+  CStrings:  22510
 
Symbols:
+ +[HFCameraPlaybackEngineEventCache isDisplayableEvent:]
+ +[HFCameraPlaybackEngineEventCache isTimelineEligibleEvent:]
+ +[HFCameraPlaybackEngineEventCache isValidEvent:]
+ +[HFMediaHelper isSiriEndpoint:]
+ +[HFSetupPairingControllerUtilities getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:setupError:]
+ +[HFSetupPairingControllerUtilities processFirstPartyAccessorySetupProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:]
+ +[HFSetupPairingControllerUtilities processSetupAccessoryProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:thirdParty:]
+ +[HFSetupPairingControllerUtilities processThirdPartyAccessorySetupProgressChange:currentPhase:context:discoveredAccessory:setupResult:callerClass:]
+ +[HFUtilities isAVisionPro]
+ +[HMEventTrigger(NaturalLanguage) hf_triggerValueNaturalLanguageDescriptionWithCharacteristics:triggerValue:visibleTriggerValues:]
+ -[HFAccessoryInfoDetailsItemProvider overrideSoftwareVersion]
+ -[HFAccessoryInfoDetailsItemProvider overrideWifiInfo]
+ -[HFAccessoryInfoDetailsItemProvider setOverrideSoftwareVersion:]
+ -[HFAccessoryInfoDetailsItemProvider setOverrideWifiInfo:]
+ -[HFAccessoryInfoItem initWithAccessory:infoType:overrideValue:]
+ -[HFAccessoryInfoItem overrideValue]
+ -[HFAccessoryNetworkInfoItem initWithAccessory:overrideSSIDName:]
+ -[HFAccessoryNetworkInfoItem overrideName]
+ -[HFAccessoryNetworkInfoItem setOverrideName:]
+ -[HFCameraPlaybackEngine _recordingEventManager:didUpdateRecordingEvents:]
+ -[HFCameraPlaybackEngine batchedRecordingEventsTimer]
+ -[HFCameraPlaybackEngine batchedRecordingEvents]
+ -[HFCameraPlaybackEngine setBatchedRecordingEvents:]
+ -[HFCameraPlaybackEngine setBatchedRecordingEventsTimer:]
+ -[HFCameraPlaybackEngine setShouldBatchRecordingEvents:]
+ -[HFCameraPlaybackEngine shouldBatchRecordingEvents]
+ -[HFDiscoveredAccessory rawSetupPayloadString]
+ -[HFDiscoveredAccessory setRawSetupPayloadString:]
+ -[HFPinCodeItem _userName]
+ -[HFPinCodeItem isUnknownGuest]
+ -[HFUserItem initWithHome:user:nameStyle:userDefaults:]
+ -[HFUserItem setUserDefaults:]
+ -[HFUserItem userDefaults]
+ GCC_except_table77
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._batchedRecordingEvents
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._batchedRecordingEventsTimer
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._shouldBatchRecordingEvents
+ _OBJC_IVAR_$_HFDiscoveredAccessory._rawSetupPayloadString
+ __OBJC_$_CLASS_METHODS_HFCameraPlaybackEngineEventCache
+ ___130+[HMEventTrigger(NaturalLanguage) hf_triggerValueNaturalLanguageDescriptionWithCharacteristics:triggerValue:visibleTriggerValues:]_block_invoke
+ ___46-[HFCameraPlaybackEngine updateConfiguration:]_block_invoke
+ ___46-[HFCameraPlaybackEngine updateConfiguration:]_block_invoke.104
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.137
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.139
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.138
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.140
+ ___49-[HFCharacteristicValueManager executeActionSet:]_block_invoke.126
+ ___58-[HFCameraPlaybackEngine fetchCameraEventsWithCompletion:]_block_invoke.91
+ ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.105
+ ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.99
+ ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.156
+ ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.114
+ ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.117
+ ___72-[HFUserItem setDismissWalletKeyExpressModeOnboarding:forWalletKeyUUID:]_block_invoke.75
+ ___74-[HFCameraPlaybackEngine _recordingEventManager:didUpdateRecordingEvents:]_block_invoke
+ ___74-[HFCameraPlaybackEngine _recordingEventManager:didUpdateRecordingEvents:]_block_invoke.134
+ ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.119
+ ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.120
+ ___block_descriptor_40_e8_32w_e29_v24?0"NSArray"8"NSError"16lw32l8
+ ___block_descriptor_41_e8_32w_e47_"NAFuture"16?0"HMAccessorySelectionSetting"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e28_v24?0"NSNull"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e31_q24?0"NSNumber"8"NSNumber"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e47_"NAFuture"16?0"HMAccessorySelectionSetting"8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48w_e47_"NAFuture"16?0"HMAccessorySelectionSetting"8ls32l8s40l8w48l8
+ ___block_literal_global.116
+ _objc_msgSend$_recordingEventManager:didUpdateRecordingEvents:
+ _objc_msgSend$_userName
+ _objc_msgSend$batchedRecordingEvents
+ _objc_msgSend$continuePairingForAccessoryWithUUID:setupCode:onboardingSetupPayloadString:completionHandler:
+ _objc_msgSend$getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:setupError:
+ _objc_msgSend$hf_triggerValueNaturalLanguageDescriptionWithCharacteristics:triggerValue:visibleTriggerValues:
+ _objc_msgSend$hmf_integerForKey:error:
+ _objc_msgSend$initWithAccessory:infoType:overrideValue:
+ _objc_msgSend$initWithAccessory:overrideSSIDName:
+ _objc_msgSend$initWithHome:user:nameStyle:userDefaults:
+ _objc_msgSend$isAVisionPro
+ _objc_msgSend$isDisplayableEvent:
+ _objc_msgSend$isSiriEndpoint:
+ _objc_msgSend$isTimelineEligibleEvent:
+ _objc_msgSend$isValidEvent:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$overrideName
+ _objc_msgSend$overrideSoftwareVersion
+ _objc_msgSend$overrideValue
+ _objc_msgSend$overrideWifiInfo
+ _objc_msgSend$performCloudPullWithCompletion:
+ _objc_msgSend$processFirstPartyAccessorySetupProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:
+ _objc_msgSend$processSetupAccessoryProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:thirdParty:
+ _objc_msgSend$rawSetupPayloadString
+ _objc_msgSend$setBatchedRecordingEventsTimer:
+ _objc_msgSend$setShouldBatchRecordingEvents:
+ _objc_msgSend$shouldBatchRecordingEvents
- +[HFSetupPairingControllerUtilities getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:]
- +[HFSetupPairingControllerUtilities processSetupAccessoryProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:]
- -[HFAccessoryInfoItem initWithAccessory:infoType:]
- -[HFAccessoryNetworkInfoItem initWithAccessory:]
- -[HFCameraPlaybackEngineEventCache isEventDisplayable:]
- -[HFPinCodeItem _userLabel]
- -[HFPinCodeItem setIsGuest:]
- GCC_except_table71
- _HFImageIconIdentifierServiceUnknown
- _HFImageIconIdentifierZones
- _OBJC_IVAR_$_HFAccessoryNetworkInfoItem._networkInfoType
- ___109+[HMEventTrigger(NaturalLanguage) hf_triggerValueNaturalLanguageDescriptionWithCharacteristics:triggerValue:]_block_invoke
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.136
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.138
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.137
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.139
- ___49-[HFCharacteristicValueManager executeActionSet:]_block_invoke.124
- ___58-[HFCameraPlaybackEngine fetchCameraEventsWithCompletion:]_block_invoke.89
- ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.103
- ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.98
- ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.152
- ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.113
- ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.116
- ___72-[HFUserItem setDismissWalletKeyExpressModeOnboarding:forWalletKeyUUID:]_block_invoke.70
- ___73-[HFCameraPlaybackEngine recordingEventManager:didUpdateRecordingEvents:]_block_invoke
- ___73-[HFCameraPlaybackEngine recordingEventManager:didUpdateRecordingEvents:]_block_invoke.129
- ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.114
- ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.115
- ___block_descriptor_33_e18_"NAFuture"16?08l
- ___block_descriptor_41_e8_32s_e47_"NAFuture"16?0"HMAccessorySelectionSetting"8ls32l8
- ___block_descriptor_48_e8_32s40s_e31_q24?0"NSNumber"8"NSNumber"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e47_"NAFuture"16?0"HMAccessorySelectionSetting"8ls32l8s40l8
- ___block_literal_global.134
- _objc_msgSend$_userLabel
- _objc_msgSend$continuePairingForAccessoryWithUUID:setupCode:completionHandler:
- _objc_msgSend$getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:
- _objc_msgSend$initWithAccessory:infoType:
- _objc_msgSend$isEventDisplayable:
- _objc_msgSend$processSetupAccessoryProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:
- _objc_msgSend$setIsGuest:
CStrings:
+ "\a\x11\x11"
+ "\t"
+ "\x12\x14"
+ "%@:%@ Siri endpoint media profile container: %@ has doorbell setting: %@, for common settings manager: %@"
+ "%@:%@ media profile container: %@ has doorbell setting: %@"
+ "%s locale's country code = %s for %s"
+ "26\x11!\x11\x14"
+ "Batch recording event throttling timer invalidated"
+ "Batch recording event throttling timer invoked; batched events: %@; batch in progress: %{BOOL}d"
+ "Batch recording events begin"
+ "Batch recording events end"
+ "Error getting country code: %s for %s. Using cachedHomeEnergyAvailable = %{bool}d"
+ "Failed to decode major OS version for when home hub migration banner was dismissed! Error: %@"
+ "Failed to decode minor OS version for when home hub migration banner was dismissed! Error: %@"
+ "HFUserHasDismissedHomeHubMigrationBannerForThisDevice"
+ "Ignoring previous user dismissal for home hub migration banner due to updated system software. Previous OS version: %ld.%ld | Current OS version: %ld.%ld"
+ "Q64@0:8q16Q24@32@40@48#56"
+ "Q76@0:8q16Q24@32@40@48@56#64B72"
+ "Reverse geocode succeeded. Country code = %s for %s"
+ "T@\"NSMutableSet\",&,N,V_batchedRecordingEvents"
+ "T@\"NSString\",&,N,V_overrideName"
+ "T@\"NSString\",&,N,V_overrideSoftwareVersion"
+ "T@\"NSString\",&,N,V_overrideWifiInfo"
+ "T@\"NSString\",&,N,V_rawSetupPayloadString"
+ "T@\"NSString\",R,N,V_overrideValue"
+ "T@\"NSTimer\",&,N,V_batchedRecordingEventsTimer"
+ "TB,N,V_shouldBatchRecordingEvents"
+ "User defaults for home hub migration banner dismissal with major/minor OS version does not exist!"
+ "User did previously dismiss home hub migration banner on OS version: %ld.%ld | Current OS version: %ld.%ld"
+ "[%@]: Skipping pin code that does not have a value %@"
+ "[DOCUMENTATION] Software update does not possess necessary documentation: %@, for accessory: %@"
+ "[STATUS] Skipping didReceiveUpdate for accessory: %@, with software update: %@, existingDocumentation: %@"
+ "_batchedRecordingEvents"
+ "_batchedRecordingEventsTimer"
+ "_overrideName"
+ "_overrideSoftwareVersion"
+ "_overrideValue"
+ "_overrideWifiInfo"
+ "_rawSetupPayloadString"
+ "_recordingEventManager:didUpdateRecordingEvents:"
+ "_shouldBatchRecordingEvents"
+ "_userName"
+ "batchedRecordingEvents"
+ "batchedRecordingEventsTimer"
+ "continuePairingForAccessoryWithUUID:setupCode:onboardingSetupPayloadString:completionHandler:"
+ "getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:setupError:"
+ "hf_triggerValueNaturalLanguageDescriptionWithCharacteristics:triggerValue:visibleTriggerValues:"
+ "hmf_integerForKey:error:"
+ "initWithAccessory:infoType:overrideValue:"
+ "initWithAccessory:overrideSSIDName:"
+ "initWithHome:user:nameStyle:userDefaults:"
+ "isAVisionPro"
+ "isDisplayableEvent:"
+ "isSiriEndpoint:"
+ "isTimelineEligibleEvent:"
+ "isUnknownGuest"
+ "isValidEvent:"
+ "operatingSystemVersion"
+ "overrideName"
+ "overrideSoftwareVersion"
+ "overrideValue"
+ "overrideWifiInfo"
+ "performCloudPullWithCompletion:"
+ "processFirstPartyAccessorySetupProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:"
+ "processSetupAccessoryProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:thirdParty:"
+ "processThirdPartyAccessorySetupProgressChange:currentPhase:context:discoveredAccessory:setupResult:callerClass:"
+ "rawSetupPayloadString"
+ "setBatchedRecordingEvents:"
+ "setBatchedRecordingEventsTimer:"
+ "setOverrideName:"
+ "setOverrideSoftwareVersion:"
+ "setOverrideWifiInfo:"
+ "setRawSetupPayloadString:"
+ "setShouldBatchRecordingEvents:"
+ "shouldBatchRecordingEvents"
+ "v80@0:8^@16^@24Q32@40@48@56@64@72"
- "\a\x11"
- "\x12\x13"
- "!\x12"
- "%s locale's country code = %s"
- "26\x11!\x11\x12"
- "Error getting country code: %s. Returning false"
- "HFImageIconIdentifierServiceUnknown"
- "HFImageIconIdentifierZones"
- "HFUserHasDismissedHomeHubMigrationBannerOnThisDevice"
- "Reverse geocode succeeded. Country code = %s"
- "TB,N,V_isGuest"
- "[DOCUMENTATION] Software update does not possess necessary documentation: %@"
- "[STATUS] Skipping didReceiveUpdate for accessory: %@, with software update: %@"
- "_isGuest"
- "continuePairingForAccessoryWithUUID:setupCode:completionHandler:"
- "getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:"
- "initWithAccessory:infoType:"
- "isEventDisplayable:"
- "processSetupAccessoryProgressChange:currentPhase:context:discoveredAccessory:setupResult:home:callerClass:"
- "setIsGuest:"
- "v72@0:8^@16^@24Q32@40@48@56@64"

```
