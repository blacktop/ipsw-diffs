## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-438.36.4.2.4
-  __TEXT.__text: 0x20690
+438.36.4.2.9
+  __TEXT.__text: 0x222b0
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x25e4
+  __TEXT.__objc_methlist: 0x273c
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x26df
-  __TEXT.__cstring: 0x3f69
+  __TEXT.__oslogstring: 0x2a5c
+  __TEXT.__cstring: 0x4082
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x7b0
-  __TEXT.__objc_classname: 0x619
-  __TEXT.__objc_methname: 0x4d53
-  __TEXT.__objc_methtype: 0x1153
-  __TEXT.__objc_stubs: 0x3520
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x1190
-  __DATA_CONST.__objc_classlist: 0x130
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__objc_classname: 0x63d
+  __TEXT.__objc_methname: 0x507d
+  __TEXT.__objc_methtype: 0x11e6
+  __TEXT.__objc_stubs: 0x3780
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x1198
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e8
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x3a20
-  __AUTH_CONST.__objc_const: 0x6fa0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x200
+  __AUTH_CONST.__cfstring: 0x3ba0
+  __AUTH_CONST.__objc_const: 0x7270
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x21c
   __DATA.__data: 0x970
   __DATA.__bss: 0x128
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24D0E912-C74D-360C-86C2-E1F757DF563D
-  Functions: 959
-  Symbols:   3818
-  CStrings:  2314
+  UUID: 72BB8606-B2D7-3C06-835C-5D9C5269853F
+  Functions: 987
+  Symbols:   3937
+  CStrings:  2397
 
Symbols:
+ +[FMDSharedConfigurationFollowUpEntry supportsSecureCoding]
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:]
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.1
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.10
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.11
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.2
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.3
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.4
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.5
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.6
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.7
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.8
+ -[FMDSharedConfiguration _createAwarenessStringsDictionaryWithData:key:deviceClasses:].cold.9
+ -[FMDSharedConfiguration _createFollowUpStringsDictionaryWithData:key:deviceClasses:]
+ -[FMDSharedConfiguration _createFollowUpStringsDictionaryWithData:key:deviceClasses:].cold.1
+ -[FMDSharedConfiguration _createFollowUpStringsDictionaryWithData:key:deviceClasses:].cold.2
+ -[FMDSharedConfiguration _createFollowUpStringsDictionaryWithData:key:deviceClasses:].cold.3
+ -[FMDSharedConfiguration _createFollowUpStringsDictionaryWithData:key:deviceClasses:].cold.4
+ -[FMDSharedConfiguration clearFindMySignOutTimeFile]
+ -[FMDSharedConfiguration clearFindMySignOutTimeFile].cold.1
+ -[FMDSharedConfiguration clearFindMySignOutTimeFile].cold.2
+ -[FMDSharedConfiguration postTheftAndLossCFUWithEntry:reply:]
+ -[FMDSharedConfiguration readFindMySignOutTimeFromFile]
+ -[FMDSharedConfiguration readFindMySignOutTimeFromFile].cold.1
+ -[FMDSharedConfiguration sharedConfigurationDictionaryFromData:key:deviceClasses:]
+ -[FMDSharedConfiguration signOutTimestampFileURL]
+ -[FMDSharedConfiguration signOutTimestampFileURL].cold.1
+ -[FMDSharedConfiguration signOutTimestampFileURL].cold.2
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile]
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile].cold.1
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile].cold.2
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile].cold.3
+ -[FMDSharedConfigurationFollowUpEntry .cxx_destruct]
+ -[FMDSharedConfigurationFollowUpEntry category]
+ -[FMDSharedConfigurationFollowUpEntry encodeWithCoder:]
+ -[FMDSharedConfigurationFollowUpEntry idNumber]
+ -[FMDSharedConfigurationFollowUpEntry informativeText]
+ -[FMDSharedConfigurationFollowUpEntry initWithCoder:]
+ -[FMDSharedConfigurationFollowUpEntry init]
+ -[FMDSharedConfigurationFollowUpEntry message]
+ -[FMDSharedConfigurationFollowUpEntry reminderInMins]
+ -[FMDSharedConfigurationFollowUpEntry setCategory:]
+ -[FMDSharedConfigurationFollowUpEntry setIdNumber:]
+ -[FMDSharedConfigurationFollowUpEntry setInformativeText:]
+ -[FMDSharedConfigurationFollowUpEntry setMessage:]
+ -[FMDSharedConfigurationFollowUpEntry setReminderInMins:]
+ -[FMDSharedConfigurationFollowUpEntry setSubtitleText:]
+ -[FMDSharedConfigurationFollowUpEntry setTitle:]
+ -[FMDSharedConfigurationFollowUpEntry subtitleText]
+ -[FMDSharedConfigurationFollowUpEntry title]
+ _NSURLIsExcludedFromBackupKey
+ _OBJC_CLASS_$_FMDSharedConfigurationFollowUpEntry
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._category
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._idNumber
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._informativeText
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._message
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._reminderInMins
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._subtitleText
+ _OBJC_IVAR_$_FMDSharedConfigurationFollowUpEntry._title
+ _OBJC_METACLASS_$_FMDSharedConfigurationFollowUpEntry
+ __OBJC_$_CLASS_METHODS_FMDSharedConfigurationFollowUpEntry
+ __OBJC_$_CLASS_PROP_LIST_FMDSharedConfigurationFollowUpEntry
+ __OBJC_$_INSTANCE_METHODS_FMDSharedConfigurationFollowUpEntry
+ __OBJC_$_INSTANCE_VARIABLES_FMDSharedConfigurationFollowUpEntry
+ __OBJC_$_PROP_LIST_FMDSharedConfigurationFollowUpEntry
+ __OBJC_CLASS_PROTOCOLS_$_FMDSharedConfigurationFollowUpEntry
+ __OBJC_CLASS_RO_$_FMDSharedConfigurationFollowUpEntry
+ __OBJC_METACLASS_RO_$_FMDSharedConfigurationFollowUpEntry
+ ___33-[FMDFMIPManager disableLostMode]_block_invoke.28
+ ___38-[FMDFMIPManager enableFMIPInContext:]_block_invoke.54
+ ___39-[FMDFMIPManager clearData:completion:]_block_invoke.87
+ ___41-[FMDFMIPManager enableLostModeWithInfo:]_block_invoke.21
+ ___42-[FMDFMIPManager fmipStateWithCompletion:]_block_invoke.47
+ ___42-[FMDFMIPManager fmipStateWithCompletion:]_block_invoke.47.cold.1
+ ___43-[FMDFMIPManager didChangeFMIPAccountInfo:]_block_invoke.53
+ ___44-[FMDFMIPManager deviceActivationDidSucceed]_block_invoke.45
+ ___44-[FMDFMIPManager fmipAccountWithCompletion:]_block_invoke.49
+ ___44-[FMDFMIPManager fmipAccountWithCompletion:]_block_invoke.49.cold.1
+ ___46-[FMDFMIPManager pairingCheckWith:completion:]_block_invoke.172
+ ___47-[FMDFMIPManager fetchAccessoryConfigurations:]_block_invoke.164
+ ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.185
+ ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.185.cold.1
+ ___50-[FMDFMIPManager didReceiveLostModeExitAuthToken:]_block_invoke.71
+ ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.184
+ ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.184.cold.1
+ ___50-[FMDFMIPManager playSoundWithOptions:completion:]_block_invoke.42
+ ___51-[FMDFMIPManager isActivationLockedWithCompletion:]_block_invoke.67
+ ___51-[FMDFMIPManager isActivationLockedWithCompletion:]_block_invoke.67.cold.1
+ ___51-[FMDFMIPManager updatePairingLockInfo:completion:]_block_invoke.171
+ ___53-[FMDFMIPManager enableActivationLockWithCompletion:]_block_invoke.68
+ ___53-[FMDFMIPManager enableActivationLockWithCompletion:]_block_invoke.68.cold.1
+ ___53-[FMDFMIPManager simulatePushWithPayload:completion:]_block_invoke.193
+ ___54-[FMDFMIPManager _forceFMWUpgradeAlertWithCompletion:]_block_invoke.177
+ ___54-[FMDFMIPManager getConnectedAccessoriesDiscoveryIds:]_block_invoke.167
+ ___54-[FMDFMIPManager signatureHeadersWithData:completion:]_block_invoke.77
+ ___54-[FMDFMIPManager signatureHeadersWithData:completion:]_block_invoke.77.cold.1
+ ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.174
+ ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.174.cold.1
+ ___56-[FMDFMIPManager isActivationLockAllowedWithCompletion:]_block_invoke.65
+ ___56-[FMDFMIPManager isActivationLockAllowedWithCompletion:]_block_invoke.65.cold.1
+ ___56-[FMDFMIPManager isActivationLockEnabledWithCompletion:]_block_invoke.66
+ ___56-[FMDFMIPManager isActivationLockEnabledWithCompletion:]_block_invoke.66.cold.1
+ ___56-[FMDFMIPManager lowBatteryLocateEnabledWithCompletion:]_block_invoke.72
+ ___58-[FMDFMIPManager registerDeviceForPairingLock:completion:]_block_invoke.169
+ ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.178
+ ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.178.cold.1
+ ___60-[FMDFMIPManager removeAccessoryWithDiscoveryId:completion:]_block_invoke.165
+ ___60-[FMDFMIPManager setLowBatteryLocateEnabled:withCompletion:]_block_invoke.75
+ ___61-[FMDFMIPManager(Private) addNotificationRequest:completion:]_block_invoke.16
+ ___61-[FMDFMIPManager(Private) addNotificationRequest:completion:]_block_invoke.16.cold.1
+ ___61-[FMDSharedConfiguration postTheftAndLossCFUWithEntry:reply:]_block_invoke
+ ___61-[FMDSharedConfiguration postTheftAndLossCFUWithEntry:reply:]_block_invoke_2
+ ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.182
+ ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.182.cold.1
+ ___62-[FMDFMIPManager waitForRoutableAccessory:timeout:completion:]_block_invoke.82
+ ___62-[FMDFMIPManager waitForRoutableAccessory:timeout:completion:]_block_invoke.82.cold.1
+ ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.179
+ ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.179.cold.1
+ ___70-[FMDFMIPManager disableManagedLostModeWithLocatedMessage:completion:]_block_invoke.38
+ ___70-[FMDFMIPManager disableManagedLostModeWithLocatedMessage:completion:]_block_invoke.38.cold.1
+ ___71-[FMDFMIPManager setPhoneNumber:toAccessoryWithDiscoveryId:completion:]_block_invoke.166
+ ___71-[FMDFMIPManager(Private) disableBiometricIDForLostModeWithCompletion:]_block_invoke.12
+ ___71-[FMDFMIPManager(Private) disableBiometricIDForLostModeWithCompletion:]_block_invoke.12.cold.1
+ ___71-[FMDFMIPManager(Private) removeNotificationWithIdentifier:completion:]_block_invoke.17
+ ___71-[FMDFMIPManager(Private) removeNotificationWithIdentifier:completion:]_block_invoke.17.cold.1
+ ___73-[FMDFMIPManager _initiateLostModeExitAuthForIDSDeviceID:withCompletion:]_block_invoke.181
+ ___75-[FMDFMIPManager stopPlayingSoundForAccessory:rampDownDuration:completion:]_block_invoke.81
+ ___75-[FMDFMIPManager stopPlayingSoundForAccessory:rampDownDuration:completion:]_block_invoke.81.cold.1
+ ___76-[FMDFMIPManager disableFMIPForAccount:pairedDeviceWithUDID:withCompletion:]_block_invoke.61
+ ___76-[FMDFMIPManager disableFMIPForAccount:pairedDeviceWithUDID:withCompletion:]_block_invoke.61.cold.1
+ ___78-[FMDFMIPManager markPairedDeviceWithUDID:asMissingUsingToken:withCompletion:]_block_invoke.64
+ ___78-[FMDFMIPManager markPairedDeviceWithUDID:asMissingUsingToken:withCompletion:]_block_invoke.64.cold.1
+ ___79-[FMDFMIPManager disableFMIPUsingToken:forPairedDeviceWithUDID:withCompletion:]_block_invoke.60
+ ___79-[FMDFMIPManager disableFMIPUsingToken:forPairedDeviceWithUDID:withCompletion:]_block_invoke.60.cold.1
+ ___79-[FMDFMIPManager markAsMissingSupportedForPairedDeviceWithUDID:withCompletion:]_block_invoke.62
+ ___79-[FMDFMIPManager markAsMissingSupportedForPairedDeviceWithUDID:withCompletion:]_block_invoke.62.cold.1
+ ___92-[FMDFMIPManager startPlayingSoundForAccessory:duration:rampUpDuration:channels:completion:]_block_invoke.80
+ ___92-[FMDFMIPManager startPlayingSoundForAccessory:duration:rampUpDuration:channels:completion:]_block_invoke.80.cold.1
+ ___block_literal_global.159
+ ___block_literal_global.163
+ ___block_literal_global.176
+ ___block_literal_global.19
+ ___block_literal_global.27
+ ___block_literal_global.52
+ ___block_literal_global.70
+ ___block_literal_global.86
+ ___block_literal_global.90
+ _kFMDCoreFollowUpTheftAndLossReminderSignOutTimestampKey
+ _objc_msgSend$_createAwarenessStringsDictionaryWithData:key:deviceClasses:
+ _objc_msgSend$_createFollowUpStringsDictionaryWithData:key:deviceClasses:
+ _objc_msgSend$category
+ _objc_msgSend$date
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$idNumber
+ _objc_msgSend$informativeText
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$postTheftAndLossCFUWithEntry:reply:
+ _objc_msgSend$reminderInMins
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$setCategory:
+ _objc_msgSend$setIdNumber:
+ _objc_msgSend$setInformativeText:
+ _objc_msgSend$setReminderInMins:
+ _objc_msgSend$setResourceValue:forKey:error:
+ _objc_msgSend$setSubtitleText:
+ _objc_msgSend$sharedConfigurationDictionaryFromData:key:deviceClasses:
+ _objc_msgSend$signOutTimestampFileURL
+ _objc_msgSend$subtitleText
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:]
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.1
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.10
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.11
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.2
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.3
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.4
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.5
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.6
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.7
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.8
- -[FMDSharedConfiguration entryWithData:key:deviceClasses:].cold.9
- -[FMDSharedConfiguration requestTheftAndLossCFUWithReply:]
- ___33-[FMDFMIPManager disableLostMode]_block_invoke.22
- ___38-[FMDFMIPManager enableFMIPInContext:]_block_invoke.48
- ___39-[FMDFMIPManager clearData:completion:]_block_invoke.81
- ___41-[FMDFMIPManager enableLostModeWithInfo:]_block_invoke.15
- ___42-[FMDFMIPManager fmipStateWithCompletion:]_block_invoke.41
- ___42-[FMDFMIPManager fmipStateWithCompletion:]_block_invoke.41.cold.1
- ___43-[FMDFMIPManager didChangeFMIPAccountInfo:]_block_invoke.47
- ___44-[FMDFMIPManager deviceActivationDidSucceed]_block_invoke.39
- ___44-[FMDFMIPManager fmipAccountWithCompletion:]_block_invoke.43
- ___44-[FMDFMIPManager fmipAccountWithCompletion:]_block_invoke.43.cold.1
- ___46-[FMDFMIPManager pairingCheckWith:completion:]_block_invoke.166
- ___47-[FMDFMIPManager fetchAccessoryConfigurations:]_block_invoke.158
- ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.179
- ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.179.cold.1
- ___49-[FMDSharedConfiguration forceDownloadWithReply:]_block_invoke
- ___50-[FMDFMIPManager didReceiveLostModeExitAuthToken:]_block_invoke.65
- ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.178
- ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.178.cold.1
- ___50-[FMDFMIPManager playSoundWithOptions:completion:]_block_invoke.36
- ___51-[FMDFMIPManager isActivationLockedWithCompletion:]_block_invoke.61
- ___51-[FMDFMIPManager isActivationLockedWithCompletion:]_block_invoke.61.cold.1
- ___51-[FMDFMIPManager updatePairingLockInfo:completion:]_block_invoke.165
- ___53-[FMDFMIPManager enableActivationLockWithCompletion:]_block_invoke.62
- ___53-[FMDFMIPManager enableActivationLockWithCompletion:]_block_invoke.62.cold.1
- ___53-[FMDFMIPManager simulatePushWithPayload:completion:]_block_invoke.187
- ___54-[FMDFMIPManager _forceFMWUpgradeAlertWithCompletion:]_block_invoke.171
- ___54-[FMDFMIPManager getConnectedAccessoriesDiscoveryIds:]_block_invoke.161
- ___54-[FMDFMIPManager signatureHeadersWithData:completion:]_block_invoke.71
- ___54-[FMDFMIPManager signatureHeadersWithData:completion:]_block_invoke.71.cold.1
- ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.168
- ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.168.cold.1
- ___56-[FMDFMIPManager isActivationLockAllowedWithCompletion:]_block_invoke.59
- ___56-[FMDFMIPManager isActivationLockAllowedWithCompletion:]_block_invoke.59.cold.1
- ___56-[FMDFMIPManager isActivationLockEnabledWithCompletion:]_block_invoke.60
- ___56-[FMDFMIPManager isActivationLockEnabledWithCompletion:]_block_invoke.60.cold.1
- ___56-[FMDFMIPManager lowBatteryLocateEnabledWithCompletion:]_block_invoke.66
- ___58-[FMDFMIPManager registerDeviceForPairingLock:completion:]_block_invoke.163
- ___58-[FMDSharedConfiguration requestTheftAndLossCFUWithReply:]_block_invoke
- ___58-[FMDSharedConfiguration requestTheftAndLossCFUWithReply:]_block_invoke_2
- ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.172
- ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.172.cold.1
- ___60-[FMDFMIPManager removeAccessoryWithDiscoveryId:completion:]_block_invoke.159
- ___60-[FMDFMIPManager setLowBatteryLocateEnabled:withCompletion:]_block_invoke.69
- ___61-[FMDFMIPManager(Private) addNotificationRequest:completion:]_block_invoke.10
- ___61-[FMDFMIPManager(Private) addNotificationRequest:completion:]_block_invoke.10.cold.1
- ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.176
- ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.176.cold.1
- ___62-[FMDFMIPManager waitForRoutableAccessory:timeout:completion:]_block_invoke.76
- ___62-[FMDFMIPManager waitForRoutableAccessory:timeout:completion:]_block_invoke.76.cold.1
- ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.173
- ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.173.cold.1
- ___70-[FMDFMIPManager disableManagedLostModeWithLocatedMessage:completion:]_block_invoke.32
- ___70-[FMDFMIPManager disableManagedLostModeWithLocatedMessage:completion:]_block_invoke.32.cold.1
- ___71-[FMDFMIPManager setPhoneNumber:toAccessoryWithDiscoveryId:completion:]_block_invoke.160
- ___71-[FMDFMIPManager(Private) disableBiometricIDForLostModeWithCompletion:]_block_invoke.6
- ___71-[FMDFMIPManager(Private) disableBiometricIDForLostModeWithCompletion:]_block_invoke.6.cold.1
- ___71-[FMDFMIPManager(Private) removeNotificationWithIdentifier:completion:]_block_invoke.11
- ___71-[FMDFMIPManager(Private) removeNotificationWithIdentifier:completion:]_block_invoke.11.cold.1
- ___73-[FMDFMIPManager _initiateLostModeExitAuthForIDSDeviceID:withCompletion:]_block_invoke.175
- ___75-[FMDFMIPManager stopPlayingSoundForAccessory:rampDownDuration:completion:]_block_invoke.75
- ___75-[FMDFMIPManager stopPlayingSoundForAccessory:rampDownDuration:completion:]_block_invoke.75.cold.1
- ___76-[FMDFMIPManager disableFMIPForAccount:pairedDeviceWithUDID:withCompletion:]_block_invoke.55
- ___76-[FMDFMIPManager disableFMIPForAccount:pairedDeviceWithUDID:withCompletion:]_block_invoke.55.cold.1
- ___78-[FMDFMIPManager markPairedDeviceWithUDID:asMissingUsingToken:withCompletion:]_block_invoke.58
- ___78-[FMDFMIPManager markPairedDeviceWithUDID:asMissingUsingToken:withCompletion:]_block_invoke.58.cold.1
- ___79-[FMDFMIPManager disableFMIPUsingToken:forPairedDeviceWithUDID:withCompletion:]_block_invoke.54
- ___79-[FMDFMIPManager disableFMIPUsingToken:forPairedDeviceWithUDID:withCompletion:]_block_invoke.54.cold.1
- ___79-[FMDFMIPManager markAsMissingSupportedForPairedDeviceWithUDID:withCompletion:]_block_invoke.56
- ___79-[FMDFMIPManager markAsMissingSupportedForPairedDeviceWithUDID:withCompletion:]_block_invoke.56.cold.1
- ___92-[FMDFMIPManager startPlayingSoundForAccessory:duration:rampUpDuration:channels:completion:]_block_invoke.74
- ___92-[FMDFMIPManager startPlayingSoundForAccessory:duration:rampUpDuration:channels:completion:]_block_invoke.74.cold.1
- ___block_literal_global.13
- ___block_literal_global.153
- ___block_literal_global.157
- ___block_literal_global.170
- ___block_literal_global.46
- ___block_literal_global.64
- ___block_literal_global.78
- ___block_literal_global.9
- _objc_msgSend$entryWithData:key:deviceClasses:
- _objc_msgSend$requestTheftAndLossCFUWithReply:
CStrings:
+ "@\"NSNumber\""
+ "Entry found at %lu, but doesn't contain a remainder in mins"
+ "Entry found at %lu, but doesn't contain an id"
+ "Entry found at %lu, but id isn't a number: %@"
+ "Entry found at %lu, but it doesn't contain category"
+ "Entry found at %lu, but it doesn't contain informative text"
+ "Entry found at %lu, but it doesn't contain message"
+ "Entry found at %lu, but it doesn't contain subtitle text"
+ "Entry found at %lu, but it doesn't contain title"
+ "Entry found at %lu, but remainder in mins isn't a number: %@"
+ "Error excluding %@ from backup %@"
+ "FMDSharedConfigurationFollowUpEntry"
+ "Failed to parse awareness strings"
+ "Failed to read contents with error: %@"
+ "Failed to remove file (%@) with error %@."
+ "Failed to write the timestamp to %@ with error %@."
+ "Failure to request a CFU with error: %@, shouldEnable: %{public}@"
+ "Invalid URL (%@) for the timestamp file."
+ "No CFU requested"
+ "No contents"
+ "No record of the last sign out. Bailing."
+ "Removed (%@)."
+ "SignOutTimestamp"
+ "T@\"NSNumber\",C,N,V_idNumber"
+ "T@\"NSNumber\",C,N,V_reminderInMins"
+ "T@\"NSString\",C,N,V_category"
+ "T@\"NSString\",C,N,V_informativeText"
+ "T@\"NSString\",C,N,V_subtitleText"
+ "TNL_REMINDER_INFORMATIVE_TEXT_DEFAULT"
+ "TNL_REMINDER_MESSAGE_DEFAULT"
+ "TNL_REMINDER_SUBTITLE_TEXT_DEFAULT"
+ "TNL_REMINDER_TITLE_DEFAULT"
+ "Wrote (%@) to (%@)."
+ "_category"
+ "_createAwarenessStringsDictionaryWithData:key:deviceClasses:"
+ "_createFollowUpStringsDictionaryWithData:key:deviceClasses:"
+ "_idNumber"
+ "_informativeText"
+ "_reminderInMins"
+ "_subtitleText"
+ "clearFindMySignOutTimeFile"
+ "date"
+ "fileExistsAtPath:isDirectory:"
+ "followUpStrings"
+ "group.com.apple.icloud.findmydevice.followup"
+ "idNumber"
+ "informativeText"
+ "initWithInt:"
+ "lastPathComponent"
+ "postTheftAndLossCFUWithEntry:reply:"
+ "readFindMySignOutTimeFromFile"
+ "reminderInMins"
+ "removeItemAtPath:error:"
+ "requestTheftAndLossCFUWithString:andReply:"
+ "requestTheftAndLossCFUWithStrings:andReply:"
+ "setCategory:"
+ "setIdNumber:"
+ "setInformativeText:"
+ "setReminderInMins:"
+ "setResourceValue:forKey:error:"
+ "setSubtitleText:"
+ "sharedConfigurationDictionaryFromData:key:deviceClasses:"
+ "signOutTimestampFileURL"
+ "subtitleText"
+ "theftandloss.plist"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?B@\"NSError\">24"
+ "writeFindMySignOutTimeToFile"
- "entryWithData:key:deviceClasses:"
- "requestTheftAndLossCFU:"
- "requestTheftAndLossCFUWithReply:"

```
