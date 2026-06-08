## AudioDataAnalysis

> `/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis`

```diff

-819.603.0.0.0
-  __TEXT.__text: 0x69e4
-  __TEXT.__auth_stubs: 0x3e0
+879.1.0.0.0
+  __TEXT.__text: 0x6030
   __TEXT.__objc_methlist: 0x64c
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x9c1
-  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x9d6
   __TEXT.__oslogstring: 0x7e1
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0x11df
-  __TEXT.__objc_methtype: 0x423
-  __TEXT.__objc_stubs: 0xf80
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x3b0
+  __TEXT.__unwind_info: 0x210
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x580
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x9a0
+  __AUTH_CONST.__cfstring: 0x9c0
   __AUTH_CONST.__objc_const: 0x8a8
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x248
+  __DATA.__data: 0x240
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26D5A34F-8BA1-3968-8381-5E5593A4018A
-  Functions: 163
-  Symbols:   771
-  CStrings:  509
+  UUID: 75EA62FA-960E-34CF-87DD-6E822DECAED6
+  Functions: 125
+  Symbols:   641
+  CStrings:  232
 
Symbols:
+ GCC_except_table15
+ GCC_except_table19
+ GCC_except_table24
+ ___Block_byref_object_copy_.149
+ ___Block_byref_object_dispose_.150
+ ___block_literal_global.146
+ ___block_literal_global.32
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- +[ADAFUtil isProcessMediaserverd].cold.1
- +[ADASPreferenceStore sharedInstance].cold.1
- -[ADAMAudioDataReceiver handleAndLogError:].cold.1
- -[ADAMAudioDataReceiver handleAndLogError:].cold.2
- -[ADAMAudioDataReceiver receiveAudioSample:type:metadata:].cold.1
- -[ADAMAudioDataReceiver reconnect].cold.1
- -[ADASManager _clearCurrentVolumeLimit].cold.1
- -[ADASManager _clearCurrentVolumeLimit].cold.2
- -[ADASManager _getCurrentVolumeLimit].cold.1
- -[ADASManager _isDeviceMandatoryForHAENotification:].cold.1
- -[ADASManager getNanoPreferenceFor:].cold.1
- -[ADASManager getNanoPreferenceFor:].cold.2
- -[ADASManager getNanoPreferenceFor:].cold.3
- -[ADASManager getNanoPreferencesFor:].cold.1
- -[ADASManager getPreferenceFor:].cold.1
- -[ADASManager removeNanoPreferenceFor:notify:].cold.1
- -[ADASManager removeNanoPreferenceFor:notify:].cold.2
- -[ADASManager removeNanoPreferenceFor:notify:].cold.3
- -[ADASManager removePreferenceFor:notify:].cold.1
- -[ADASManager setNanoPreferenceFor:value:notify:].cold.1
- -[ADASManager setNanoPreferenceFor:value:notify:].cold.2
- -[ADASManager setNanoPreferenceFor:value:notify:].cold.3
- -[ADASManager setPreferenceFor:value:notify:].cold.1
- -[ADASManager setPreferenceFor:value:notify:].cold.2
- GCC_except_table25
- GCC_except_table30
- GCC_except_table34
- _ADAFLog.cold.1
- _AudioDataAnalysisFrameworkVersionNumber
- _AudioDataAnalysisFrameworkVersionString
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___33-[ADASManager getPreferencesFor:]_block_invoke.cold.1
- ___34-[ADAMAudioDataReceiver reconnect]_block_invoke.103.cold.1
- ___34-[ADAMAudioDataReceiver reconnect]_block_invoke.98.cold.1
- ___37-[ADASManager getNanoPreferencesFor:]_block_invoke.cold.1
- ___37-[ADASManager getNanoPreferencesFor:]_block_invoke.cold.2
- ___40-[ADAMAudioDataReceiver setupConnection]_block_invoke.97.cold.1
- ___40-[ADAMAudioDataReceiver setupConnection]_block_invoke.cold.1
- ___44-[ADASManager _migrateVolumeLimitThreshold:]_block_invoke.cold.1
- ___54-[ADAMAudioDataReceiver stopMeasuringAudioSampleType:]_block_invoke.cold.1
- ___54-[ADAMAudioDataReceiver stopReceivingAudioSampleType:]_block_invoke.cold.1
- ___55-[ADAMAudioDataReceiver startReceivingAudioSampleType:]_block_invoke_2.cold.1
- ___59-[ADAMAudioDataReceiver isMeasurementOnForAudioSampleType:]_block_invoke.cold.1
- ___64-[ADAMAudioDataReceiver configureAudioSampleType:configuration:]_block_invoke.cold.1
- ___67-[ADAMAudioDataReceiver getCurrentConfigurationForAudioSampleType:]_block_invoke.cold.1
- ___68-[ADAMAudioDataReceiver startReceivingAudioSampleType:withCallback:]_block_invoke.cold.1
- ___73-[ADAMAudioDataReceiver startMeasuringAudioSampleType:withConfiguration:]_block_invoke.cold.1
- _kADAMAudioDataAnalysisData
- _kADAMAudioDataAnalysisSampleDateInterval
- _kADAMAudioDataAnalysisSampleMetadata
- _kADAMAudioDataAnalysisSampleUUID
- _kADAMAudioDataAnalysisType
- _kADAMEnvironmentalDosageString
- _kADAMHeadphoneAudioExposureString
- _kADAMMicLevelString
- _kADAMSoundClassificationString
- _kADAMUnknownDataTypeString
- _kDefaultsKeyConnectedUnknownDeviceIsHeadphone
- _kDefaultsKeyHAEDisableMigrationAlert
- _kDefaultsKeyHAEEnableOtherDevices
- _kDefaultsKeyHAEMeasureLevel
- _kDefaultsKeyHAENDeviceProductTypeOverride
- _kDefaultsKeyHAENFeatureMandatory
- _kDefaultsKeyHAENFeatureMandatoryOverride
- _kDefaultsKeyHAENKnownAccessories
- _kDefaultsKeyHAENKnownAccessoryExpiryDays
- _kDefaultsKeyHAENRegionCodeOverride
- _kDefaultsKeyHAENotificationFeatureEnabled
- _kDefaultsKeyHAENotificationLiveMonitorInSeconds
- _kDefaultsKeyHAENotificationLiveThreshold
- _kDefaultsKeyHAESampleTransient
- _kDefaultsKeyLoudnessCompensationEnabled
- _kDefaultsKeyMXVolumeLimitOn
- _kDefaultsKeyMigrationAlertSurfaced
- _kDefaultsKeySurfaceMigrationAlert
- _kDefaultsKeyVolumeLimitEnabled
- _kDefaultsKeyVolumeLimitThreshold
- _kDefaultsKeyVolumeReductionDelta
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "MediaLevel"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ADAMAudioDataReceiverDelegate>\""
- "@\"ADASPreferenceStore\""
- "@\"NPSDomainAccessor\""
- "@\"NSDateInterval\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@44@0:8@16@24B32@36"
- "@44@0:8I16@20@28@36"
- "ADAFUtil"
- "ADAMAudioDataAnalysisSample"
- "ADAMAudioDataReceiver"
- "ADAMClientDelegate"
- "ADAMServerProtocol"
- "ADASManager"
- "ADASPreferenceStore"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Discoverability"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "Signals"
- "T#,R"
- "T@\"<ADAMAudioDataReceiverDelegate>\",W,N,Vdelegate"
- "T@\"NPSDomainAccessor\",&,N,V_coreAudioDeviceDomain"
- "T@\"NPSDomainAccessor\",&,N,V_coreAudioDomain"
- "T@\"NSDateInterval\",R,N,VdateInterval"
- "T@\"NSDictionary\",R,N,V_defaultValues"
- "T@\"NSDictionary\",R,N,V_keyMap"
- "T@\"NSDictionary\",R,N,V_specialDarwinKeys"
- "T@\"NSDictionary\",R,N,Vmetadata"
- "T@\"NSNumber\",R,N,Vdata"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUUID\",R,N,Vuuid"
- "TB,R"
- "TB,V_connectionDidInvalidate"
- "TI,R,N,Vtype"
- "TQ,R"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_callbacks"
- "_clearCurrentVolumeLimit"
- "_configs"
- "_connection"
- "_connectionDidInvalidate"
- "_coreAudioDeviceDomain"
- "_coreAudioDomain"
- "_defaultValues"
- "_donateSignalToTipsKit:"
- "_error:"
- "_featureFlagEnabled"
- "_getCurrentVolumeLimit"
- "_getDefaultsFor:"
- "_getDefaultsKey:"
- "_getDeviceSpecificDefaultsFor:"
- "_getSpecialKeys:nano:"
- "_isAlertSupported"
- "_isDeviceMandatoryForHAENotification:"
- "_keyMap"
- "_lock"
- "_migrateVolumeLimitThreshold:"
- "_name"
- "_notify:"
- "_npsDomainAccessorQueue"
- "_npsDomainLock"
- "_prefStore"
- "_sensorStatus"
- "_setChainedKeys:val:nano:modifiedKeys:"
- "_setDefaultValueIfNeeded:nano:sync:"
- "_setDefaultsFor:value:"
- "_setDeviceSpecificDefaultsFor:value:"
- "_specialDarwinKeys"
- "_sync"
- "_syncDeviceSpecificDomain"
- "_syncNanoDeviceSpecificForRead:"
- "_syncNanoForRead:"
- "_syncNanoForWrite:"
- "addObject:"
- "addObserver:selector:name:object:"
- "allocWithZone:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "class"
- "code"
- "configureAudioSampleType:configuration:"
- "configureAudioSampleTypeWithIdentifier:type:configuration:withReply:"
- "conformsToProtocol:"
- "connectionDidInvalidate"
- "containsObject:"
- "copy"
- "copyAttributeForKey:withValueOut:"
- "copyWithZone:"
- "coreAudioDeviceDomain"
- "coreAudioDomain"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dateInterval"
- "dealloc"
- "debugDescription"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultValues"
- "delegate"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjectsAndKeys:"
- "didSurfaceMigrationAlert"
- "doubleValue"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "floatValue"
- "getCurrentConfigurationForAudioSampleType:"
- "getCurrentConfigurationForAudioSampleType:withReply:"
- "getNanoPreferenceFor:"
- "getNanoPreferencesFor:"
- "getPreferenceFor:"
- "getPreferencesFor:"
- "handleAndLogError:"
- "hash"
- "init"
- "initAudioSampleWithType:data:dateInterval:metadata:"
- "initNPSDomain"
- "initWithCoder:"
- "initWithContentIdentifier:context:osBuild:userInfo:"
- "initWithDictionary:copyItems:"
- "initWithDomain:"
- "initWithIdentifier:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMeasurementOnForAudioSampleType:"
- "isMeasurementOnForAudioSampleType:withReply:"
- "isMemberOfClass:"
- "isProcessMediaserverd"
- "isProxy"
- "keyMap"
- "metadata"
- "migrateKeyEnableHAEHKMeasurement:"
- "nanoSettingsAvailable"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "pairedDeviceStateChanged:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "processName"
- "receiveAudioSample:"
- "receiveAudioSample:type:metadata:"
- "reconnect"
- "registerForNotifications"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeNanoPreferenceFor:"
- "removeNanoPreferenceFor:notify:"
- "removeObjectForKey:"
- "removePreferenceFor:"
- "removePreferenceFor:notify:"
- "reset"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "sendEvent:"
- "setAttribute:forKey:error:"
- "setAttributeForKey:andValue:"
- "setConnectionDidInvalidate:"
- "setCoreAudioDeviceDomain:"
- "setCoreAudioDomain:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNanoPreferenceFor:value:"
- "setNanoPreferenceFor:value:notify:"
- "setObject:forKey:"
- "setPreferenceFor:value:"
- "setPreferenceFor:value:notify:"
- "setRemoteObjectInterface:"
- "setWithArray:"
- "setWithObjects:"
- "setupConnection"
- "sharedAVSystemController"
- "sharedInstance"
- "shouldSufaceHAENotificationMigrationAlert"
- "source"
- "specialDarwinKeys"
- "startListeningToAudioSampleWithIdentifier:type:withReply:"
- "startMeasuringAudioSampleType:withConfiguration:"
- "startMeasuringAudioSampleTypeWithIdentifier:type:withConfiguration:andReply:"
- "startReceivingAudioSampleType:"
- "startReceivingAudioSampleType:withCallback:"
- "stopListeningToAudioSampleTypeWithIdentifier:type:withReply:"
- "stopMeasuringAudioSampleType:"
- "stopMeasuringAudioSampleTypeWithIdentifier:type:andReply:"
- "stopReceivingAudioSampleType:"
- "stringFromDataType:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "type"
- "unsignedIntegerValue"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"ADAMAudioDataAnalysisSample\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v28@0:8@16B24"
- "v28@0:8I16@20"
- "v28@0:8I16@?20"
- "v28@0:8I16@?<v@?@\"NSDictionary\">20"
- "v28@0:8I16@?<v@?B>20"
- "v36@0:8@\"NSNumber\"16I24@\"NSDictionary\"28"
- "v36@0:8@\"NSString\"16I24@?<v@?@\"NSError\">28"
- "v36@0:8@16I24@28"
- "v36@0:8@16I24@?28"
- "v44@0:8@\"NSString\"16I24@\"NSDictionary\"28@?<v@?@\"NSError\">36"
- "v44@0:8@16I24@28@?36"
- "verifyInvariants"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
