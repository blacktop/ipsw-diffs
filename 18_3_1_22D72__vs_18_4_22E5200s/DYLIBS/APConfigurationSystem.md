## APConfigurationSystem

> `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem`

```diff

-554.14.0.0.0
-  __TEXT.__text: 0x65bc
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x88c
+555.36.0.0.0
+  __TEXT.__text: 0x707c
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x885
-  __TEXT.__oslogstring: 0xa3d
+  __TEXT.__cstring: 0x9b5
+  __TEXT.__oslogstring: 0xa8d
   __TEXT.__gcc_except_tab: 0x90
   __TEXT.__swift5_typeref: 0x5c
   __TEXT.__constg_swiftt: 0xa4

   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0x375
-  __TEXT.__objc_methname: 0x192a
-  __TEXT.__objc_methtype: 0x387
-  __TEXT.__objc_stubs: 0x1520
-  __DATA_CONST.__got: 0x168
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_classname: 0x486
+  __TEXT.__objc_methname: 0x1e47
+  __TEXT.__objc_methtype: 0x398
+  __TEXT.__objc_stubs: 0x17c0
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_selrefs: 0x7b8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x10
-  __AUTH_CONST.__cfstring: 0x9a0
-  __AUTH_CONST.__objc_const: 0x27c0
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x54
+  __AUTH_CONST.__cfstring: 0xb40
+  __AUTH_CONST.__objc_const: 0x2fc8
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x248
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x140
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 176
-  Symbols:   228
-  CStrings:  559
+  Functions: 206
+  Symbols:   259
+  CStrings:  642
 
Symbols:
+ _OBJC_CLASS_$_APCSAnonymousSessionId
+ _OBJC_CLASS_$_APCSBucketId
+ _OBJC_CLASS_$_APCSExperimentationReport
+ _OBJC_CLASS_$_APCSODCAFeatureFlag
+ _OBJC_CLASS_$_APCSRotatedAnonymousId
+ _OBJC_CLASS_$_APCSSessionManagementIDs
+ _OBJC_CLASS_$_APECExperimentationPurposeConfig
+ _OBJC_CLASS_$_APECOnDeviceConversionPurposeConfig
+ _OBJC_CLASS_$_APJetServiceConfig
+ _OBJC_CLASS_$_APOnDeviceAttributionConfig
+ _OBJC_CLASS_$_APOnDeviceConversionConfig
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_METACLASS_$_APCSAnonymousSessionId
+ _OBJC_METACLASS_$_APCSBucketId
+ _OBJC_METACLASS_$_APCSExperimentationReport
+ _OBJC_METACLASS_$_APCSODCAFeatureFlag
+ _OBJC_METACLASS_$_APCSRotatedAnonymousId
+ _OBJC_METACLASS_$_APCSSessionManagementIDs
+ _OBJC_METACLASS_$_APECExperimentationPurposeConfig
+ _OBJC_METACLASS_$_APECOnDeviceConversionPurposeConfig
+ _OBJC_METACLASS_$_APJetServiceConfig
+ _OBJC_METACLASS_$_APOnDeviceAttributionConfig
+ _OBJC_METACLASS_$_APOnDeviceConversionConfig
+ _arc4random_uniform
+ _kAPActionStoreEnabled
+ _kAPExperimentationReportEnabled
+ _kAPModernDataCollectionEnabled
+ _kAPOnDeviceAttributionEnabled
+ _kAPOnDeviceConversionEnabled
+ _objc_retain_x4
CStrings:
+ "APCSAnonymousSessionId"
+ "APCSBucketId"
+ "APCSExperimentationReport"
+ "APCSODCAFeatureFlag"
+ "APCSRotatedAnonymousId"
+ "APCSSessionManagementIDs"
+ "APECExperimentationPurposeConfig"
+ "APECOnDeviceConversionPurposeConfig"
+ "APJetServiceConfig"
+ "APOnDeviceAttributionConfig"
+ "APOnDeviceConversionConfig"
+ "EventCollection/Purposes/8502"
+ "EventCollection/Purposes/8503"
+ "FeatureFlagRollout"
+ "Found existing rollout %@"
+ "Found new ODCA feature flag version. Re-slicing."
+ "Identifiers/AnonymousSessionId"
+ "Identifiers/BucketId"
+ "Identifiers/RotatedAnonymousId"
+ "Identifiers/SessionManagementIDsEnabled"
+ "JetService"
+ "ODCAFeatureFlag"
+ "OnDeviceAttribution"
+ "OnDeviceConversion"
+ "Reports/Experimentation"
+ "T@\"NSDictionary\",&,N,V_allProperties"
+ "T@\"NSDictionary\",&,N,V_configDictionary"
+ "T@\"NSDictionary\",R,N"
+ "TB,R,N"
+ "_allProperties"
+ "_clearRollout"
+ "_configDictionary"
+ "_fileSystemPath"
+ "_isSliceWithinEnablementPercentage:forFeature:"
+ "_knownRollout"
+ "_storeRolloutForFlag:isEnabled:slice:"
+ "actionStoreEnabled"
+ "actionStoreEnabledPercentage"
+ "aggregationWindows"
+ "allProperties"
+ "anonymousSessionIds"
+ "appOpenDelayInSeconds"
+ "bucketIds"
+ "cacheSizeLimit"
+ "createFileAtPath:contents:attributes:"
+ "dataWithPropertyList:format:options:error:"
+ "dictionaryWithDictionary:"
+ "doubleValue"
+ "enableSessionManagementIds"
+ "experimentationReportEnabled"
+ "experimentationReportEnabledPercentage"
+ "expirationOfData2024E"
+ "impressionLookback"
+ "incorporateJourneyMetrics"
+ "installSignals"
+ "interactionLookback"
+ "longValue"
+ "maximumTokenLifetime"
+ "modernDataCollectionEnabled"
+ "modernDataCollectionEnabledPercentage"
+ "numberWithLong:"
+ "numberWithUnsignedInt:"
+ "onDeviceAttributionEnabled"
+ "onDeviceAttributionEnabledPercentage"
+ "onDeviceConversionEnabled"
+ "onDeviceConversionEnabledPercentage"
+ "propertyListWithData:options:format:error:"
+ "reengagementSources"
+ "reportEnabled"
+ "reportSources"
+ "reportingWindows"
+ "rotatedAnonymousIds"
+ "setAllProperties:"
+ "setObject:forKeyedSubscript:"
+ "signingBackoffSchedule"
+ "signingHoldTransactionLimit"
+ "slice"
+ "supportedBundleIds"
+ "supportedPurposes"
+ "unsignedIntValue"
+ "uploadHoldTransactionLimit"
+ "urlPaths"
+ "v36@0:8@16B24@28"

```
