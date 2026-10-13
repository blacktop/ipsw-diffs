## assistantd

> `System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3605.30.1.1.1
-  __TEXT.__text: 0x37bad4
-  __TEXT.__auth_stubs: 0x3930
-  __TEXT.__objc_stubs: 0x48ac0
-  __TEXT.__objc_methlist: 0x24460
+3605.31.1.11.2
+  __TEXT.__text: 0x37fbf4
+  __TEXT.__auth_stubs: 0x3940
+  __TEXT.__objc_stubs: 0x48e40
+  __TEXT.__objc_methlist: 0x24570
   __TEXT.__const: 0xede8
   __TEXT.__dlopen_cstrs: 0x9e9
-  __TEXT.__gcc_except_tab: 0x3e48
-  __TEXT.__cstring: 0x5572e
-  __TEXT.__oslogstring: 0x4b564
+  __TEXT.__gcc_except_tab: 0x3f08
+  __TEXT.__cstring: 0x55e98
+  __TEXT.__oslogstring: 0x4c023
   __TEXT.__objc_classname: 0x532c
-  __TEXT.__objc_methname: 0x6435e
-  __TEXT.__objc_methtype: 0x10465
+  __TEXT.__objc_methname: 0x648b3
+  __TEXT.__objc_methtype: 0x1047d
   __TEXT.__ustring: 0x98
-  __TEXT.__unwind_info: 0xd250
+  __TEXT.__unwind_info: 0xd2d8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x14a30
-  __DATA_CONST.__cfstring: 0x13040
+  __DATA_CONST.__const: 0x14b10
+  __DATA_CONST.__cfstring: 0x13260
   __DATA_CONST.__objc_classlist: 0xd70
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x758
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0xb38
-  __DATA_CONST.__objc_arraydata: 0x530
-  __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA_CONST.__objc_intobj: 0x8e8
+  __DATA_CONST.__objc_arraydata: 0x538
+  __DATA_CONST.__objc_arrayobj: 0x210
+  __DATA_CONST.__objc_intobj: 0x918
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1ca8
-  __DATA_CONST.__got: 0x3ec0
+  __DATA_CONST.__auth_got: 0x1cb0
+  __DATA_CONST.__got: 0x3ef0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x35e28
-  __DATA.__objc_selrefs: 0x15c98
-  __DATA.__objc_ivar: 0x27d8
+  __DATA.__objc_const: 0x35ee0
+  __DATA.__objc_selrefs: 0x15da0
+  __DATA.__objc_ivar: 0x27e4
   __DATA.__objc_data: 0x8660
-  __DATA.__data: 0x5fa0
+  __DATA.__data: 0x5fb0
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14975
-  Symbols:   3026
-  CStrings:  28727
+  Functions: 15015
+  Symbols:   3033
+  CStrings:  28845
 
Symbols:
+ _HMAccessoryCategoryTypeHomeAccessory
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_HMAccessoryNumberSetting
+ _OBJC_CLASS_$_TTSAsset
+ _OBJC_CLASS_$_TTSAssetTechnology
+ _OBJC_CLASS_$_TTSAssetType
+ _kVTPreferencesVTPhraseTypeDidChangeDarwinNotification
CStrings:
+ "%s #multi-user-atv Syncing %{private}@ to user profile companion."
+ "%s %@ setting does not exist on this Home device, no recovery needed"
+ "%s Accessory already in assistant access control, skipping update"
+ "%s Accessory not in assistant access control, skipping update"
+ "%s Adding companion IFP device capability (%{bool}d)"
+ "%s Adding companion Linwood device capability (%{bool}d)"
+ "%s Adding companion Siri availability (%{public}@)"
+ "%s Adding linwood capability"
+ "%s Adding voice '%@'"
+ "%s Cannot initialize Siri Phrase Options: currentHome is nil"
+ "%s Cannot sync VT state to HomeKit: currentHome is nil"
+ "%s Checking eligibility for additional voice subscription for '%@'"
+ "%s Companion IFP device capability record %{public}s (raw value %{public}@, resolved %{bool}d)"
+ "%s Companion Linwood device capability record %{public}s (raw value %{public}@, resolved %{bool}d)"
+ "%s Companion Siri availability is not serializable, so it cannot contribute to the identifiers anchor: %{public}@"
+ "%s Companion Siri availability record %{public}s (%{public}@)"
+ "%s Could not apply personal content setting with error %@"
+ "%s Deleting personal content setting record %@ from CloudKit"
+ "%s Failed to initialize Siri Phrase Options: %@"
+ "%s Failed to read VT phrase type: %@"
+ "%s Failed to read the always-recognized demo experience setting, error = %@"
+ "%s Failed to update Siri Phrase Options: %@"
+ "%s Failed to update personal content assistant access control with error %@"
+ "%s Found home for personal content update"
+ "%s Invalid type found for personal content record value"
+ "%s Invalid type found for the Linwood enablement setting"
+ "%s No accessories found for home with id %@"
+ "%s No companion Siri availability computed yet; leaving %{public}@ absent"
+ "%s No home unique identifier found in personal content record %@"
+ "%s No homes found"
+ "%s No personal content setting found in record %@"
+ "%s Not a secure demo device, error = %@"
+ "%s Object is not of the expected type HMAccessoryNumberSetting"
+ "%s Personal content record found: %@"
+ "%s Personal content setting delete operation completed with error %@"
+ "%s Posting Darwin notification that companion info changed for a shared user"
+ "%s Setting Me Linwood Enablement Status %@"
+ "%s Setting companion Linwood enablement (%{bool}d) and device capability (%{bool}d) on new deviceOwner"
+ "%s Siri Phrase Options is unset, initializing from local VT preference: %lu"
+ "%s Syncing Linwood enablement status of me device to cloud (%{private}d)"
+ "%s Syncing Siri Phrase Options to HomeKit: %ld"
+ "%s Unable to subscribe voice [%@], error: %@"
+ "%s Updated personal content assistant access control successfully"
+ "%s Updating companion IFP device capability (%{bool}d)"
+ "%s Updating companion Linwood device capability (%{bool}d)"
+ "%s Updating companion Siri availability (%{public}@)"
+ "%s Voices targeted for subscription '%@'"
+ "%s homeUniqueIdentifier: %{private}@, accessoryIdentifier: %{private}@, enabled: %d"
+ "-[ADCloudKitManager syncPersonalContentSetting:iCloudAltDSID:homeUniqueIdentifier:accessoryIdentifier:completion:]"
+ "-[ADCloudKitManager syncPersonalContentSetting:iCloudAltDSID:homeUniqueIdentifier:accessoryIdentifier:completion:]_block_invoke"
+ "-[ADCloudKitMultiUserSharedDataStore checkForMeLinwodSettingUpdate:]"
+ "-[ADCloudKitMultiUserSharedDataStore checkForPersonalContentSettingUpdate:]"
+ "-[ADCloudKitMultiUserSharedDataStore checkForPersonalContentSettingUpdate:]_block_invoke"
+ "-[ADHomeInfoManager isLinwoodEnabledOnAnyDeviceInHome:]"
+ "-[ADHomeInfoManager isLinwoodEnabledOnAnyHomeDevice:]"
+ "-[ADHomeInfoManager isLinwoodEnabledOnAnyHomeDevice:]_block_invoke"
+ "-[ADHomeInfoManager updateCurrentUserPersonalContentSettingForHome:accessoryIdentifier:enabled:completion:]"
+ "-[ADHomeInfoManager updateCurrentUserPersonalContentSettingForHome:accessoryIdentifier:enabled:completion:]_block_invoke"
+ "-[ADHomeInfoManager(VoiceActivation) syncVoiceTriggerStateToHomeKit]"
+ "-[ADHomeInfoManager(VoiceActivation) syncVoiceTriggerStateToHomeKit]_block_invoke"
+ "-[ADHomeInfoManager(VoiceActivation) updateVoiceTriggerPhrase:currentAccessoryInfo:]_block_invoke"
+ "-[ADMultiUserCloudKitSyncer capabilitiesDidChange]_block_invoke"
+ "/\n"
+ "/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit"
+ "14"
+ "?3"
+ "ADCompanionSiriAvailabilityAnchorValue"
+ "ADIsAlwaysRecognizedStoreDemo"
+ "DeviceSupportsInstructionFollowingPruningModels"
+ "Failed to get assistant access control for user"
+ "Failed to get mutable assistant access control"
+ "Invalid accessoryIdentifier UUID"
+ "MSDKDemoState"
+ "MSDKManagedDevice"
+ "MobileAssistantDaemons-3605.31.1.11.2"
+ "No accessory found matching accessoryIdentifier"
+ "PressDemoMode"
+ "T@\"NSDictionary\",C,N,V_companionSiriAvailability"
+ "TB,N,V_companionIFPCapableDevice"
+ "TB,N,V_companionLinwoodCapableDevice"
+ "_companionIFPCapableDevice"
+ "_companionLinwoodCapableDevice"
+ "_companionSiriAvailability"
+ "_setLinwoodEnabledMeDevice:"
+ "accessoryDidUpdateSupportsAppleTVSiriSettings:"
+ "accessoryDidUpdateSupportsTopCapPlusAndMinus:"
+ "accessoryDidUpdateSupportsTopCapTouchAndHold:"
+ "addAccessory:"
+ "capabilitiesDidChange"
+ "checkForMeLinwodSettingUpdate:"
+ "checkForPersonalContentSettingUpdate:"
+ "companionIFPCapableDevice"
+ "companionLinwoodCapableDevice"
+ "companionSiriAvailability"
+ "createDictionaryExcludingBootSession"
+ "gryphonVoice"
+ "homeDidSetHasOwnerAcknowledgedHomePodSiriOnboarding:"
+ "homeUniqueIdentifier"
+ "ifpCapableDevice"
+ "initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:siriAvailability:"
+ "isAlwaysRecognizedDemoExperience"
+ "isAlwaysRecognizedDemoExperience:"
+ "isLinwoodEnabledOnAnyDeviceInHome:"
+ "isLinwoodEnabledOnAnyHomeDevice:"
+ "isReplyToSiriPrompt"
+ "isSecureDemoModeEnabled:"
+ "linwoodCapableDevice"
+ "listAssetsOfTypes:matching:"
+ "meDeviceIsIFPCapableDevice"
+ "meDeviceIsLinwoodCapableDevice"
+ "meDeviceSiriAvailability"
+ "meIsLinwoodEnabled"
+ "neural"
+ "personalContentTVSetting"
+ "personalContentTV_"
+ "removeAccessory:"
+ "root.siri.personalSiriEnabled"
+ "setCompanionIFPCapableDevice:"
+ "setCompanionLinwoodCapableDevice:"
+ "setCompanionSiriAvailability:"
+ "syncPersonalContentSetting:iCloudAltDSID:homeUniqueIdentifier:accessoryIdentifier:completion:"
+ "syncVoiceTriggerStateToHomeKit"
+ "updateAssistantAccessControl:forHome:completionHandler:"
+ "updateCurrentUserPersonalContentSettingForHome:accessoryIdentifier:enabled:completion:"
+ "v52@0:8B16@20@28@36@?44"
- "%s Setting companion Linwood enablement on new deviceOwner (%{bool}d)"
- "%s Unable to subscribe voice %@, error: %@"
- "/\t"
- "2"
- "?2"
- "MobileAssistantDaemons-3605.30.1.1.1"
- "initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:"
```
