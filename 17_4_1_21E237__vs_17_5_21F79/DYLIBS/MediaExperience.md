## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-140.21.1.1.0
-  __TEXT.__text: 0x19a994
-  __TEXT.__auth_stubs: 0x1e20
-  __TEXT.__objc_methlist: 0x39cc
-  __TEXT.__cstring: 0x24b0f
-  __TEXT.__const: 0x1968
-  __TEXT.__gcc_except_tab: 0x17e4
-  __TEXT.__oslogstring: 0x2ccff
+150.4.2.1.1
+  __TEXT.__text: 0x1a3548
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_methlist: 0x3e34
+  __TEXT.__cstring: 0x255bd
+  __TEXT.__const: 0x1970
+  __TEXT.__gcc_except_tab: 0x19a8
+  __TEXT.__oslogstring: 0x2e441
   __TEXT.__dlopen_cstrs: 0x503
-  __TEXT.__unwind_info: 0x3a18
-  __TEXT.__objc_classname: 0x3ce
-  __TEXT.__objc_methname: 0xfb88
-  __TEXT.__objc_methtype: 0x1903
-  __TEXT.__objc_stubs: 0x9b80
-  __DATA_CONST.__got: 0x808
-  __DATA_CONST.__const: 0x5d20
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__unwind_info: 0x3d8c
+  __TEXT.__objc_classname: 0x422
+  __TEXT.__objc_methname: 0x102c4
+  __TEXT.__objc_methtype: 0x196c
+  __TEXT.__objc_stubs: 0x9fe0
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__const: 0x5da0
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5ce8
-  __DATA_CONST.__objc_selrefs: 0x2a00
-  __DATA_CONST.__objc_classrefs: 0x238
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_const: 0x5ff0
+  __DATA_CONST.__objc_selrefs: 0x2b08
+  __DATA_CONST.__objc_classrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x154e0
-  __AUTH_CONST.__const: 0x33c8
-  __AUTH_CONST.__objc_const: 0xdc0
+  __AUTH_CONST.__cfstring: 0x157c0
+  __AUTH_CONST.__objc_const: 0x1048
+  __AUTH_CONST.__const: 0x3468
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xf28
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__auth_got: 0xf58
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x490
-  __DATA.__objc_ivar: 0x62c
-  __DATA.__data: 0x20a0
-  __DATA.__common: 0xb0
-  __DATA.__bss: 0x818
+  __DATA.__objc_ivar: 0x66c
+  __DATA.__data: 0x21a8
+  __DATA.__bss: 0x798
+  __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x188
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D034749-C77C-3F94-82F7-DB5174427439
-  Functions: 4888
-  Symbols:   15853
-  CStrings:  11538
+  UUID: 15D3CDE6-51DE-3F6E-9CCD-17C2F058C888
+  Functions: 4996
+  Symbols:   16202
+  CStrings:  11758
 
Symbols:
+ +[MXExclaves sensorStatusToString:]
+ +[MXExclaves sharedInstance]
+ +[MXSessionBase generateSessionID]
+ +[MXSessionBase getSetPropertiesOrder]
+ +[MXSessionBase isNonSerializedCopyProperty:]
+ +[MXSessionBase isNonSerializedSetProperty:]
+ +[MXSessionBase isNonSerializedSetPropertyWhenSessionIsInactive:]
+ +[MXSessionManagerSecure sharedInstance]
+ +[MXSessionSecure getSetPropertiesOrder]
+ +[MXSessionSecure initialize]
+ +[MXSessionSecure isNonSerializedCopyProperty:]
+ +[MXSessionSecure isNonSerializedSetProperty:]
+ +[MXSessionSecure isNonSerializedSetPropertyWhenSessionIsInactive:]
+ -[MXCoreSession hasEntitlementToSetIsUsingBuiltInMicForRecording]
+ -[MXCoreSession hasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime]
+ -[MXCoreSession isUsingBuiltInMicForRecording]
+ -[MXCoreSession isUsingExclaveSensor]
+ -[MXCoreSession preferredMinimumMicrophoneIndicatorLightOnTime]
+ -[MXCoreSession setHasEntitlementToSetIsUsingBuiltInMicForRecording:]
+ -[MXCoreSession setHasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime:]
+ -[MXCoreSession setIsUsingBuiltInMicForRecording:]
+ -[MXCoreSession setIsUsingExclaveSensor:]
+ -[MXCoreSession setPreferredMinimumMicrophoneIndicatorLightOnTime:]
+ -[MXCoreSessionSecure _beginInterruptionWithSecTask:andFlags:]
+ -[MXCoreSessionSecure _endInterruptionWithSecTask:andStatus:]
+ -[MXCoreSessionSecure addMXSessionSecure:]
+ -[MXCoreSessionSecure copyMXSessionSecureList]
+ -[MXCoreSessionSecure copyPropertyForKey:valueOut:]
+ -[MXCoreSessionSecure dealloc]
+ -[MXCoreSessionSecure hasEntitlementToSetEnrollmentMode]
+ -[MXCoreSessionSecure initWithOptions:]
+ -[MXCoreSessionSecure isolatedAudioUseCaseID]
+ -[MXCoreSessionSecure logDebugInfo]
+ -[MXCoreSessionSecure removeMXSessionSecure:]
+ -[MXCoreSessionSecure setHasEntitlementToSetEnrollmentMode:]
+ -[MXCoreSessionSecure setIsolatedAudioUseCaseID:]
+ -[MXCoreSessionSecure setPropertyForKey:value:]
+ -[MXCoreSessionSecure updateAudioBehaviourFromVARouteConfig:]
+ -[MXCoreSessionSecure updateEntitlements]
+ -[MXExclaves dealloc]
+ -[MXExclaves init]
+ -[MXExclaves logDebugInfo]
+ -[MXExclaves updateSensorStatus:reason:]
+ -[MXSessionBase ID]
+ -[MXSessionBase _beginInterruptionWithSecTask:andFlags:]
+ -[MXSessionBase _copyProperties:outPropertyErrors:]
+ -[MXSessionBase _copyPropertyForKey:valueOut:]
+ -[MXSessionBase _endInterruptionWithSecTask:andStatus:]
+ -[MXSessionBase _setOrderedProperties:usingErrorHandlingStrategy:outPropertiesErrors:]
+ -[MXSessionBase _setProperties:usingErrorHandlingStrategy:outPropertiesErrors:]
+ -[MXSessionBase _setPropertyForKey:value:]
+ -[MXSessionBase copyProperties:outPropertyErrors:]
+ -[MXSessionBase copyPropertiesInternal:outPropertyErrors:]
+ -[MXSessionBase copyPropertyForKey:valueOut:]
+ -[MXSessionBase copyPropertyForKeyInternal:valueOut:]
+ -[MXSessionBase dealloc]
+ -[MXSessionBase init]
+ -[MXSessionBase parentCoreSession]
+ -[MXSessionBase setID:]
+ -[MXSessionBase setOrderedProperties:usingErrorHandlingStrategy:outPropertiesErrors:]
+ -[MXSessionBase setOrderedPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:]
+ -[MXSessionBase setParentCoreSession:]
+ -[MXSessionBase setProperties:usingErrorHandlingStrategy:outPropertiesErrors:]
+ -[MXSessionBase setPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:]
+ -[MXSessionBase setPropertyForKey:value:]
+ -[MXSessionBase setPropertyForKeyInternal:value:fromPropertiesBatch:]
+ -[MXSessionManager(Utilities) updateExclaveSensorStatusIfNeeded]
+ -[MXSessionManager(VAUtilities) updateSecureSpeakerMuteState:]
+ -[MXSessionManagerSecure _beginInterruption:withSecTask:andFlags:]
+ -[MXSessionManagerSecure _endInterruption:withSecTask:andStatus:]
+ -[MXSessionManagerSecure addMXCoreSessionSecure:]
+ -[MXSessionManagerSecure copyActiveSessionsInfoForAdditiveRouting]
+ -[MXSessionManagerSecure copyMXCoreSessionSecureList]
+ -[MXSessionManagerSecure copySessionWithAudioSessionID:]
+ -[MXSessionManagerSecure dealloc]
+ -[MXSessionManagerSecure init]
+ -[MXSessionManagerSecure isSessionWithAudioModeActive:]
+ -[MXSessionManagerSecure logDebugInfo]
+ -[MXSessionManagerSecure removeMXCoreSessionSecure:]
+ -[MXSessionSecure _beginInterruptionWithSecTask:andFlags:]
+ -[MXSessionSecure _endInterruptionWithSecTask:andStatus:]
+ -[MXSessionSecure copyPropertyForKeyInternal:valueOut:]
+ -[MXSessionSecure dealloc]
+ -[MXSessionSecure initWithOptions:]
+ -[MXSessionSecure logDebugInfo]
+ -[MXSessionSecure setPropertyForKeyInternal:value:fromPropertiesBatch:]
+ GCC_except_table56
+ _CMSMDeviceState_DeviceHasExclaveCapability
+ _CMSMDeviceState_DeviceHasExclaveCapability.deviceHasExclaveCapability
+ _CMSMDeviceState_DeviceHasExclaveCapability.once
+ _MXSessionCreateWithOptions
+ _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled
+ _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled.onceToken
+ _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled.reduceRouteDiscoveryQueueHopping
+ _OBJC_CLASS_$_MXCoreSessionSecure
+ _OBJC_CLASS_$_MXExclaves
+ _OBJC_CLASS_$_MXSessionBase
+ _OBJC_CLASS_$_MXSessionManagerSecure
+ _OBJC_CLASS_$_MXSessionSecure
+ _OBJC_IVAR_$_MXCoreSession._hasEntitlementToSetIsUsingBuiltInMicForRecording
+ _OBJC_IVAR_$_MXCoreSession._hasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime
+ _OBJC_IVAR_$_MXCoreSession._isUsingBuiltInMicForRecording
+ _OBJC_IVAR_$_MXCoreSession._isUsingExclaveSensor
+ _OBJC_IVAR_$_MXCoreSession._preferredMinimumMicrophoneIndicatorLightOnTime
+ _OBJC_IVAR_$_MXCoreSessionSecure._hasEntitlementToSetEnrollmentMode
+ _OBJC_IVAR_$_MXCoreSessionSecure._isolatedAudioUseCaseID
+ _OBJC_IVAR_$_MXCoreSessionSecure.mMXSessionSecureList
+ _OBJC_IVAR_$_MXCoreSessionSecure.mMXSessionSecureListLock
+ _OBJC_IVAR_$_MXExclaves.mSensorAccessCount
+ _OBJC_IVAR_$_MXExclaves.mSensorPort
+ _OBJC_IVAR_$_MXExclaves.mSensorPortLock
+ _OBJC_IVAR_$_MXSessionBase._ID
+ _OBJC_IVAR_$_MXSessionBase._parentCoreSession
+ _OBJC_IVAR_$_MXSessionManagerSecure.mMXCoreSessionSecureList
+ _OBJC_IVAR_$_MXSessionManagerSecure.mMXCoreSessionSecureListLock
+ _OBJC_METACLASS_$_MXCoreSessionSecure
+ _OBJC_METACLASS_$_MXExclaves
+ _OBJC_METACLASS_$_MXSessionBase
+ _OBJC_METACLASS_$_MXSessionManagerSecure
+ _OBJC_METACLASS_$_MXSessionSecure
+ __OBJC_$_CLASS_METHODS_MXExclaves
+ __OBJC_$_CLASS_METHODS_MXSessionBase
+ __OBJC_$_CLASS_METHODS_MXSessionManagerSecure
+ __OBJC_$_CLASS_METHODS_MXSessionSecure
+ __OBJC_$_INSTANCE_METHODS_MXCoreSessionSecure
+ __OBJC_$_INSTANCE_METHODS_MXExclaves
+ __OBJC_$_INSTANCE_METHODS_MXSessionBase
+ __OBJC_$_INSTANCE_METHODS_MXSessionManagerSecure
+ __OBJC_$_INSTANCE_METHODS_MXSessionSecure
+ __OBJC_$_INSTANCE_VARIABLES_MXCoreSessionSecure
+ __OBJC_$_INSTANCE_VARIABLES_MXExclaves
+ __OBJC_$_INSTANCE_VARIABLES_MXSessionBase
+ __OBJC_$_INSTANCE_VARIABLES_MXSessionManagerSecure
+ __OBJC_$_PROP_LIST_MXCoreSessionSecure
+ __OBJC_$_PROP_LIST_MXSessionBase
+ __OBJC_CLASS_RO_$_MXCoreSessionSecure
+ __OBJC_CLASS_RO_$_MXExclaves
+ __OBJC_CLASS_RO_$_MXSessionBase
+ __OBJC_CLASS_RO_$_MXSessionManagerSecure
+ __OBJC_CLASS_RO_$_MXSessionSecure
+ __OBJC_METACLASS_RO_$_MXCoreSessionSecure
+ __OBJC_METACLASS_RO_$_MXExclaves
+ __OBJC_METACLASS_RO_$_MXSessionBase
+ __OBJC_METACLASS_RO_$_MXSessionManagerSecure
+ __OBJC_METACLASS_RO_$_MXSessionSecure
+ ___28+[MXExclaves sharedInstance]_block_invoke
+ ___40+[MXSessionManagerSecure sharedInstance]_block_invoke
+ ___41-[MXSessionBase setPropertyForKey:value:]_block_invoke
+ ___45-[MXSessionBase copyPropertyForKey:valueOut:]_block_invoke
+ ___50-[MXSessionBase copyProperties:outPropertyErrors:]_block_invoke
+ ___78-[MXSessionBase setProperties:usingErrorHandlingStrategy:outPropertiesErrors:]_block_invoke
+ ___85-[MXSessionBase setOrderedProperties:usingErrorHandlingStrategy:outPropertiesErrors:]_block_invoke
+ ___CMSMDeviceState_DeviceHasExclaveCapability_block_invoke
+ ___CMSMUtility_UpdateSharePlayVolumeBehaviours_block_invoke.415
+ ___FigRouteDiscovererCreate_block_invoke_2
+ ___FigRouteDiscovererCreate_block_invoke_3
+ ___MXCoreSessionSetProperty_block_invoke.118
+ ___MXCoreSessionSetProperty_block_invoke.127
+ ___MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled_block_invoke
+ ___block_descriptor_40_e8_32b_e5_v8?0ls32l8
+ ___block_literal_global.115
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.129
+ ___block_literal_global.148
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.199
+ ___block_literal_global.225
+ ___block_literal_global.268
+ ___block_literal_global.275
+ ___block_literal_global.279
+ ___block_literal_global.282
+ ___block_literal_global.38
+ ___block_literal_global.414
+ ___block_literal_global.423
+ ___block_literal_global.425
+ ___block_literal_global.48
+ ___block_literal_global.84
+ ___block_literal_global.87
+ ___block_literal_global.98
+ ___cmsmInitializeCMSessionManager_block_invoke.29
+ ___cmsmScreenIsBlankedChangedCallback_block_invoke.273
+ ___discoverer_SetProperty_block_invoke.48
+ ___discoverer_SetProperty_block_invoke_3
+ ___discoverer_SetProperty_block_invoke_4
+ ___discoveryManager_postNotificationToAllDiscoverers_block_invoke.45
+ ___discoveryManager_postNotificationToAllDiscoverers_block_invoke_2
+ ___discoveryManager_postNotificationToAllDiscoverers_block_invoke_3
+ ___vaemConnectedPortsPropertyListenerGuts_block_invoke
+ _exclaves_sensor_create
+ _exclaves_sensor_start
+ _exclaves_sensor_status
+ _exclaves_sensor_stop
+ _generateSessionID.sSessionID
+ _kMXSessionAudioMode_Enrollment
+ _kMXSessionCreationOption_AuditToken
+ _kMXSessionCreationOption_IsolatedAudioUseCaseID
+ _kMXSessionCreationOption_SessionType
+ _kMXSessionProperty_IsUsingBuiltInMicForRecording
+ _kMXSessionProperty_PreferredMinimumMicrophoneIndicatorLightOnTime
+ _kMXSessionReporterIDLog_IsSecureSession
+ _kVirtualAudioPlugInSessionDescriptionIsolatedUseCaseIDKey_CFString
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_msgSend$_beginInterruption:withSecTask:andFlags:
+ _objc_msgSend$_endInterruption:withSecTask:andStatus:
+ _objc_msgSend$addMXCoreSessionSecure:
+ _objc_msgSend$addMXSessionSecure:
+ _objc_msgSend$copyMXCoreSessionSecureList
+ _objc_msgSend$copyMXSessionSecureList
+ _objc_msgSend$generateSessionID
+ _objc_msgSend$getSetPropertiesOrder
+ _objc_msgSend$hasEntitlementToSetEnrollmentMode
+ _objc_msgSend$hasEntitlementToSetIsUsingBuiltInMicForRecording
+ _objc_msgSend$hasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$interruptAllSessionsAndSystemSounds:
+ _objc_msgSend$isSessionUsingBuiltInMic:
+ _objc_msgSend$isSessionWithAudioModeActive:
+ _objc_msgSend$isUsingBuiltInMicForRecording
+ _objc_msgSend$isUsingExclaveSensor
+ _objc_msgSend$isolatedAudioUseCaseID
+ _objc_msgSend$logDebugInfo
+ _objc_msgSend$parentCoreSession
+ _objc_msgSend$preferredMinimumMicrophoneIndicatorLightOnTime
+ _objc_msgSend$sensorStatusToString:
+ _objc_msgSend$setHasEntitlementToSetEnrollmentMode:
+ _objc_msgSend$setHasEntitlementToSetIsUsingBuiltInMicForRecording:
+ _objc_msgSend$setHasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime:
+ _objc_msgSend$setIsUsingBuiltInMicForRecording:
+ _objc_msgSend$setIsUsingExclaveSensor:
+ _objc_msgSend$setIsolatedAudioUseCaseID:
+ _objc_msgSend$setParentCoreSession:
+ _objc_msgSend$setPreferredMinimumMicrophoneIndicatorLightOnTime:
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$updateEntitlements
+ _objc_msgSend$updateExclaveSensorStatusIfNeeded
+ _objc_msgSend$updateSecureSpeakerMuteState:
+ _objc_msgSend$updateSensorStatus:reason:
+ _sOrderedMXSessionSecureProperties
+ _vaemConnectedPortsPropertyListenerGuts.onceToken
+ _xpc_copy_entitlement_for_token
- GCC_except_table26
- GCC_except_table32
- GCC_except_table55
- ___CMSMUtility_UpdateSharePlayVolumeBehaviours_block_invoke.412
- ___MXCoreSessionSetProperty_block_invoke.114
- ___MXCoreSessionSetProperty_block_invoke.117
- ___block_literal_global.105
- ___block_literal_global.108
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.119
- ___block_literal_global.135
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.212
- ___block_literal_global.219
- ___block_literal_global.255
- ___block_literal_global.262
- ___block_literal_global.266
- ___block_literal_global.269
- ___block_literal_global.32
- ___block_literal_global.411
- ___block_literal_global.420
- ___block_literal_global.422
- ___block_literal_global.55
- ___block_literal_global.85
- ___cmsmInitializeCMSessionManager_block_invoke.25
- ___cmsmScreenIsBlankedChangedCallback_block_invoke.260
- ___discoverer_SetProperty_block_invoke_2.48
CStrings:
+ "-CMSMDevState- %s: This device %{public}s have exclave capability"
+ "-CMSUtilities- %s: Client '%{public}@' failed to %{public}s recording with error=%d"
+ "-CMSessionMgr- %s: Client '%{public}@' changed isUsingBuiltInMicForRecording to '%{BOOL}u'"
+ "-CMSessionMgr- %s: Client '%{public}@' failed to change isRecordingMuted to %{BOOL}u with error=%d"
+ "-CMSessionMgr- %s: Client '%{public}@' failed to change isUsingBuiltInMicForRecording to '%{BOOL}u' with error=%d"
+ "-CMSessionMgr- %s: Client '%{public}@' failed to change wantsToShowMicrophoneIndicatorWhenNotRecording to %{BOOL}u with error=%d"
+ "-CMSessionMgr- %s: Client '%{public}@' setting %{public}@ to %{public}@"
+ "-CMSessionMgr- %s: Failed to update the sensor status for client '%{public}@'"
+ "-CMSessionMgr- %s: Skipping begin interruption for %{public}@ because there is an Enrollment session active"
+ "-FigRouteDiscoveryManager- %s: Time taken to run notification handler %fms. Time taken to post %{public}@ to all discoverers: %fms. Average time: %fms. Cache misses this iteration %d."
+ "-MXCoreSessionSecure- %s: \t\t\t MXSessionSecure sessions count=%lu"
+ "-MXCoreSessionSecure- %s: \t\t\t audioCategory: %{public}@"
+ "-MXCoreSessionSecure- %s: \t\t\t audioMode: %{public}@"
+ "-MXCoreSessionSecure- %s: \t\t\t isActive: %{BOOL}u"
+ "-MXCoreSessionSecure- %s: \t\t ############################## %{public}@ {clientName: '%{public}@', ID: %{public}@} ##############################"
+ "-MXCoreSessionSecure- %s: \t\t #####################################################################################################################################"
+ "-MXCoreSessionSecure- %s: \t\t {"
+ "-MXCoreSessionSecure- %s: \t\t }"
+ "-MXCoreSessionSecure- %s: Cannot create MXCoreSessionSecure on devices that don't have Exclave capability!"
+ "-MXCoreSessionSecure- %s: Client %{public}@ updating ReporterIDs to %{public}@"
+ "-MXCoreSessionSecure- %s: Client doesn't have the entitlement to create MXCoreSessionSecure!"
+ "-MXCoreSessionSecure- %s: Creation options dictionary cannot be nil!"
+ "-MXCoreSessionSecure- %s: Failed to copy '%{public}@' property with err=%d"
+ "-MXCoreSessionSecure- %s: Failed to set '%{public}@' property with err=%d"
+ "-MXCoreSessionSecure- %s: Insufficient information in virtualDeviceInfo = %{public}@, not amending audio behaviour dictionary"
+ "-MXCoreSessionSecure- %s: Invalid IsolatedAudio_UseCaseID %u"
+ "-MXCoreSessionSecure- %s: SoundAnalysis doesn't have the entitlement to set Enrollment mode!"
+ "-MXCoreSessionSecure- %s: Unrecognized property '%{public}@'"
+ "-MXCoreSessionSecure- %s: Updating audio behaviour to %{public}@ for %{public}@."
+ "-MXExclaves- %s: \t ================================================== %{public}@ Debug Info =================================================="
+ "-MXExclaves- %s: \t ======================================================================================================================================="
+ "-MXExclaves- %s: \t Failed to get the exclaves sensor status"
+ "-MXExclaves- %s: \t sensor access count = %d"
+ "-MXExclaves- %s: \t sensor status is '%{public}@'"
+ "-MXExclaves- %s: Cannot create MXExclaves on devices that don't have Exclave capability!"
+ "-MXExclaves- %s: Client '%{public}@' failed to start the exclaves sensor, sesnorStatus='%{public}@'"
+ "-MXExclaves- %s: Client '%{public}@' failed to stop the exclaves sensor, sesnorStatus='%{public}@'"
+ "-MXExclaves- %s: Client '%{public}@' started the exclaves sensor since %{public}@, sesnorStatus='%{public}@', sensorAccessCount = %d"
+ "-MXExclaves- %s: Client '%{public}@' stopped the exclaves sensor since %{public}@, sesnorStatus='%{public}@, sensorAccessCount = %d'"
+ "-MXExclaves- %s: Failed to create exclaves sensor!"
+ "-MXExclaves- %s: session cannot be nil!"
+ "-MXSessionBase- %s: Session '%{public}@' is copying properties batch"
+ "-MXSessionBase- %s: Session '%{public}@' is setting ordered properties batch"
+ "-MXSessionBase- %s: Session '%{public}@' is setting properties batch"
+ "-MXSessionManagerSecure- %s: \t ================================================== %{public}@ Debug Info =================================================="
+ "-MXSessionManagerSecure- %s: \t ======================================================================================================================================="
+ "-MXSessionManagerSecure- %s: \t MXCoreSessionSecure sessions count=%lu"
+ "-MXSessionManagerSecure- %s: Cannot create MXSessionManagerSecure on devices that don't have Exclave capability!"
+ "-MXSessionManagerSecure- %s: Enrollment session trying to go active while phone call is active"
+ "-MXSessionManagerSecure- %s: Failed to mute secure speaker"
+ "-MXSessionManagerSecure- %s: Failed to retrieve secure session info dictionary for %{public}@ [%p]."
+ "-MXSessionManagerSecure- %s: Failed to unmute secure speaker"
+ "-MXSessionManagerSecure- %s: MXCoreSessionSecure '%{public}@' going active"
+ "-MXSessionManagerSecure- %s: MXCoreSessionSecure '%{public}@' going inactive"
+ "-MXSessionManagerUtilities- %s: MXSessionManager INTERRUPTING '%{public}@' because updating sensor status failed with error =%d"
+ "-MXSessionManagerVAUtilities- %s: AudioObjectSetPropertyData( kVirtualAudioPortPropertySecureSpeakerOutputMute ) failed with err='%c%c%c%c'"
+ "-MXSessionManagerVAUtilities- %s: Invalid speaker port ID!"
+ "-MXSessionManagerVAUtilities- %s: kVirtualAudioPortPropertySecureSpeakerOutputMute is not supported!"
+ "-MXSessionSecure- %s: \t\t\t\t ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ %{public}@ {ID: %{public}@} ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
+ "-MXSessionSecure- %s: \t\t\t\t ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
+ "-MXSessionSecure- %s: \t\t\t\t {"
+ "-MXSessionSecure- %s: \t\t\t\t }"
+ "-MXSessionSecure- %s: Creation options dictionary cannot be nil!"
+ "-MXSessionSecure- %s: Failed to create parent CoreSession"
+ "-MXSession_CInterface- %s: Failed to create MXSessionSecure"
+ "-MXSession_CInterface- %s: Unknown SessionType '%d'"
+ "-MXSystemSounds- %s: Session with Enrollment mode is active, suppressing system sounds"
+ "-MX_FeatureFlags- %s: MediaExperience/ReduceRouteDiscoveryQueueHopping feature is %{public}s"
+ "-[MXCoreSessionSecure copyPropertyForKey:valueOut:]"
+ "-[MXCoreSessionSecure initWithOptions:]"
+ "-[MXCoreSessionSecure logDebugInfo]"
+ "-[MXCoreSessionSecure setPropertyForKey:value:]"
+ "-[MXCoreSessionSecure updateAudioBehaviourFromVARouteConfig:]"
+ "-[MXCoreSessionSecure updateEntitlements]"
+ "-[MXExclaves init]"
+ "-[MXExclaves logDebugInfo]"
+ "-[MXExclaves updateSensorStatus:reason:]"
+ "-[MXSessionBase copyProperties:outPropertyErrors:]"
+ "-[MXSessionBase copyPropertiesInternal:outPropertyErrors:]"
+ "-[MXSessionBase copyPropertyForKey:valueOut:]"
+ "-[MXSessionBase setOrderedProperties:usingErrorHandlingStrategy:outPropertiesErrors:]"
+ "-[MXSessionBase setOrderedPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:]"
+ "-[MXSessionBase setProperties:usingErrorHandlingStrategy:outPropertiesErrors:]"
+ "-[MXSessionBase setPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:]"
+ "-[MXSessionBase setPropertyForKey:value:]"
+ "-[MXSessionManager(Utilities) updateExclaveSensorStatusIfNeeded]"
+ "-[MXSessionManager(VAUtilities) updateSecureSpeakerMuteState:]"
+ "-[MXSessionManagerSecure _beginInterruption:withSecTask:andFlags:]"
+ "-[MXSessionManagerSecure _endInterruption:withSecTask:andStatus:]"
+ "-[MXSessionManagerSecure copyActiveSessionsInfoForAdditiveRouting]"
+ "-[MXSessionManagerSecure init]"
+ "-[MXSessionManagerSecure logDebugInfo]"
+ "-[MXSessionSecure initWithOptions:]"
+ "-[MXSessionSecure logDebugInfo]"
+ "22:22:58"
+ "@\"MXCoreSessionBase\""
+ "Active MXCoreSessionSecure has lost an on-demand VAD! Please file a radar against 'MediaExperience Session | All'"
+ "Allowed"
+ "Apr 16 2024"
+ "CMSMDeviceState_DeviceHasExclaveCapability_block_invoke"
+ "Control"
+ "Denied"
+ "Enrollment"
+ "ExclaveCapability"
+ "FigRouteDiscovererCreate_block_invoke"
+ "IsRecording property has changed"
+ "IsRecordingMuted property has changed"
+ "IsSecureSession"
+ "IsUsingBuiltInMicForRecording"
+ "IsUsingBuiltInMicForRecording property has changed"
+ "IsolatedAudioUseCaseID"
+ "MXCoreSessionSecure"
+ "MXCoreSessionTeardown"
+ "MXExclaves"
+ "MXSessionBase"
+ "MXSessionBase.m"
+ "MXSessionCreateWithOptions"
+ "MXSessionManagerSecure"
+ "MXSessionSecure"
+ "MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled_block_invoke"
+ "MicrophoneAttribution property has changed"
+ "PreferredMinimumMicrophoneIndicatorLightOnTime"
+ "ReduceRouteDiscoveryQueueHopping"
+ "Route has changed"
+ "SessionType"
+ "T@\"MXCoreSessionBase\",&,V_parentCoreSession"
+ "T@\"NSNumber\",&,V_preferredMinimumMicrophoneIndicatorLightOnTime"
+ "TB,N,V_hasEntitlementToSetEnrollmentMode"
+ "TB,N,V_hasEntitlementToSetIsUsingBuiltInMicForRecording"
+ "TB,N,V_hasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime"
+ "TB,N,V_isUsingBuiltInMicForRecording"
+ "TB,N,V_isUsingExclaveSensor"
+ "TI,N,V_isolatedAudioUseCaseID"
+ "_beginInterruption:withSecTask:andFlags:"
+ "_endInterruption:withSecTask:andStatus:"
+ "_hasEntitlementToSetEnrollmentMode"
+ "_hasEntitlementToSetIsUsingBuiltInMicForRecording"
+ "_hasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime"
+ "_isUsingBuiltInMicForRecording"
+ "_isUsingExclaveSensor"
+ "_isolatedAudioUseCaseID"
+ "_parentCoreSession"
+ "_preferredMinimumMicrophoneIndicatorLightOnTime"
+ "addMXCoreSessionSecure:"
+ "addMXSessionSecure:"
+ "com.apple.private.mediaexperience.enrollmentmode.allow"
+ "com.apple.private.mediaexperience.isusingbuiltinmicforrecording.allow"
+ "com.apple.private.mediaexperience.preferredminimummicrophoneindicatorlightontime.allow"
+ "com.apple.private.mediaexperience.usesecuresession"
+ "com.apple.sensors.mic"
+ "copyMXCoreSessionSecureList"
+ "copyMXSessionSecureList"
+ "discoveryManager_postNotificationToAllDiscoverers_block_invoke"
+ "discoveryManager_postNotificationToAllDiscoverers_block_invoke_2"
+ "generateSessionID"
+ "hasEntitlementToSetEnrollmentMode"
+ "hasEntitlementToSetIsUsingBuiltInMicForRecording"
+ "hasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime"
+ "i32@0:8^{__SecTask=}16@24"
+ "i40@0:8@16^{__SecTask=}24@32"
+ "i40@0:8@16^{__SecTask=}24Q32"
+ "initWithBytes:length:"
+ "isUsingBuiltInMicForRecording"
+ "isUsingBuiltInMicForRecording ="
+ "isUsingExclaveSensor"
+ "isUsingExclaveSensor ="
+ "isolated use case ID"
+ "isolatedAudioUseCaseID"
+ "logDebugInfo"
+ "mMXCoreSessionSecureList"
+ "mMXCoreSessionSecureListLock"
+ "mMXSessionSecureList"
+ "mMXSessionSecureListLock"
+ "mSensorAccessCount"
+ "mSensorPort"
+ "mSensorPortLock"
+ "parentCoreSession"
+ "preferredMinimumMicrophoneIndicatorLightOnTime"
+ "preferredMinimumMicrophoneIndicatorLightOnTime ="
+ "removeMXCoreSessionSecure:"
+ "removeMXSessionSecure:"
+ "secure enrollment session is going active"
+ "sensorStatusToString:"
+ "session is being released"
+ "setHasEntitlementToSetEnrollmentMode:"
+ "setHasEntitlementToSetIsUsingBuiltInMicForRecording:"
+ "setHasEntitlementToSetPreferredMinimumMicrophoneIndicatorLightOnTime:"
+ "setIsUsingBuiltInMicForRecording:"
+ "setIsUsingExclaveSensor:"
+ "setIsolatedAudioUseCaseID:"
+ "setParentCoreSession:"
+ "setPreferredMinimumMicrophoneIndicatorLightOnTime:"
+ "start"
+ "stop"
+ "unsignedCharValue"
+ "updateEntitlements"
+ "updateExclaveSensorStatusIfNeeded"
+ "updateSecureSpeakerMuteState:"
+ "updateSensorStatus:reason:"
- "00:16:22"
- "Mar  9 2024"

```
