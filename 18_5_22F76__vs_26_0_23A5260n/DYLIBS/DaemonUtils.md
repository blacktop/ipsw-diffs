## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0xabf4
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x13b0
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x777
+2005.0.13.0.0
+  __TEXT.__text: 0xa898
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_methlist: 0x1320
+  __TEXT.__const: 0x160
+  __TEXT.__cstring: 0x6fd
   __TEXT.__oslogstring: 0xab6
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x460
-  __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x2c64
-  __TEXT.__objc_methtype: 0x83b
-  __TEXT.__objc_stubs: 0x23a0
+  __TEXT.__unwind_info: 0x448
+  __TEXT.__objc_classname: 0x2bd
+  __TEXT.__objc_methname: 0x2ac0
+  __TEXT.__objc_methtype: 0x81b
+  __TEXT.__objc_stubs: 0x22c0
   __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__const: 0x258
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc28
+  __DATA_CONST.__objc_selrefs: 0xba8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2eb8
-  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x2e70
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x16c
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x360
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x5a0
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
-  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3034A88F-5806-33D3-BC52-846436B4E51A
-  Functions: 405
-  Symbols:   1659
-  CStrings:  913
+  UUID: C54B8311-226A-345F-B0F1-0E460FEDC7EA
+  Functions: 399
+  Symbols:   1624
+  CStrings:  885
 
Symbols:
+ -[EvaluationRequest isPurposeSecureUIRecording]
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:]
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.1
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.2
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.3
+ -[LAAnalyticsDTO _dtoResultFromLAResult:error:locationState:].cold.4
+ -[LAAnalyticsDTO _eventForLocationState:familiarLocationEvent:familiarLocationWithoutFullConfirmationEvent:unfamiliarLocationEvent:]
+ -[LAAnalyticsDTO initForOneOffDTOAnalyticsWithEvaluationRequest:dtoEnvironment:]
+ -[LAAnalyticsEvaluation biometryStarted]
+ -[LAAnalyticsEvaluation passcodeStarted]
+ -[PasscodeInvalidationSource configurationDidReceivePasscodeChangedNotification:userInfo:]
+ -[StorageRequest initWithStorageDomain:key:acl:options:contextID:connection:]
+ -[StorageRequest options]
+ GCC_except_table13
+ _LACBiomeEvaluationDTOStateFromLAAnalyticsDTOState
+ _LACDTOLocationStateRawValueInFamiliarLocation
+ _LACDTOLocationStateRawValueInFamiliarLocationWithoutFullConfirmation
+ _LACPolicyOptionSecureUIRecording
+ _OBJC_CLASS_$_LACAuditToken
+ _OBJC_CLASS_$_LACManagedConfiguration
+ _OBJC_IVAR_$_StorageRequest._options
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACManagedConfigurationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACManagedConfigurationObserver
+ __OBJC_$_PROTOCOL_REFS_LACManagedConfigurationObserver
+ __OBJC_LABEL_PROTOCOL_$_LACManagedConfigurationObserver
+ __OBJC_PROTOCOL_$_LACManagedConfigurationObserver
+ ___block_literal_global.131
+ ___block_literal_global.201
+ _objc_msgSend$_dtoResultFromLAResult:error:locationState:
+ _objc_msgSend$_eventForLocationState:familiarLocationEvent:familiarLocationWithoutFullConfirmationEvent:unfamiliarLocationEvent:
+ _objc_msgSend$biometryStarted
+ _objc_msgSend$data
+ _objc_msgSend$initWithRawValue:
+ _objc_msgSend$isDTOPolicy:options:
+ _objc_msgSend$locationState
+ _objc_msgSend$passcodeStarted
+ _objc_retain_x25
- +[LANVRAM sharedInstance]
- +[LANVRAM sharedInstance].cold.1
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:]
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.1
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.2
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.3
- -[LAAnalyticsDTO _dtoResultFromLAResult:error:inFamiliarLocation:].cold.4
- -[LANVRAM boolForKey:]
- -[LANVRAM byteForKey:]
- -[LANVRAM dataForKey:]
- -[LANVRAM dataForKey:nameSpace:]
- -[LANVRAM setData:forKey:]
- -[LANVRAM setString:forKey:]
- -[LANVRAM stringForKey:]
- -[LANVRAM unsignedIntForKey:]
- -[LANVRAM unsignedLongLongForKey:]
- -[PasscodeInvalidationSource profileConnectionDidReceivePasscodeChangedNotification:userInfo:]
- -[StorageRequest initWithStorageDomain:key:contextID:]
- -[StorageRequest initWithStorageDomain:key:contextID:acl:]
- GCC_except_table17
- _CFDataGetTypeID
- _CFGetTypeID
- _CFRelease
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IORegistryEntryFromPath
- _IORegistryEntrySetCFProperty
- _LANVRAMNamespaceStartupManager
- _NSLog
- _OBJC_CLASS_$_LANVRAM
- _OBJC_CLASS_$_LAUtils
- _OBJC_CLASS_$_MCProfileConnection
- _OBJC_METACLASS_$_LANVRAM
- __OBJC_$_CLASS_METHODS_LANVRAM
- __OBJC_$_INSTANCE_METHODS_LANVRAM
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MCProfileConnectionObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_MCProfileConnectionObserver
- __OBJC_$_PROTOCOL_REFS_MCProfileConnectionObserver
- __OBJC_CLASS_RO_$_LANVRAM
- __OBJC_LABEL_PROTOCOL_$_MCProfileConnectionObserver
- __OBJC_METACLASS_RO_$_LANVRAM
- __OBJC_PROTOCOL_$_MCProfileConnectionObserver
- ___25+[LANVRAM sharedInstance]_block_invoke
- ___block_literal_global.137
- ___block_literal_global.198
- _kCFAllocatorDefault
- _kIOMainPortDefault
- _objc_msgSend$_dtoResultFromLAResult:error:inFamiliarLocation:
- _objc_msgSend$auditTokenToData:
- _objc_msgSend$byteForKey:
- _objc_msgSend$dataForKey:
- _objc_msgSend$dataForKey:nameSpace:
- _objc_msgSend$dataUsingEncoding:
- _objc_msgSend$getBytes:length:
- _objc_msgSend$inFamiliarLocation
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$initWithStorageDomain:key:contextID:acl:
- _objc_msgSend$isLocationBasedPolicy:
- _objc_msgSend$registerObserver:
- _objc_msgSend$setData:forKey:
- _objc_msgSend$sharedConnection
- _objc_msgSend$unregisterObserver:
- _sharedInstance.instance
CStrings:
+ "@64@0:8q16q24@32@40@48@56"
+ "LACManagedConfigurationObserver"
+ "TB,R,N,V_biometryStarted"
+ "TB,R,N,V_passcodeStarted"
+ "_dtoResultFromLAResult:error:locationState:"
+ "_eventForLocationState:familiarLocationEvent:familiarLocationWithoutFullConfirmationEvent:unfamiliarLocationEvent:"
+ "biometryStarted"
+ "configurationDidReceivePasscodeChangedNotification:userInfo:"
+ "data"
+ "initForOneOffDTOAnalyticsWithEvaluationRequest:dtoEnvironment:"
+ "initWithRawValue:"
+ "initWithStorageDomain:key:acl:options:contextID:connection:"
+ "isDTOPolicy:options:"
+ "isPurposeSecureUIRecording"
+ "locationState"
+ "passcodeStarted"
+ "q40@0:8@16@24q32"
+ "q48@0:8q16q24q32q40"
+ "v32@0:8@\"<LACManagedConfiguration>\"16@\"NSDictionary\"24"
- "%@:%@"
- "5EEB160F-45FB-4CE9-B4E3-610359ABF6F8"
- "@40@0:8q16q24@32"
- "@48@0:8q16q24@32@40"
- "B32@0:8@16@24"
- "C24@0:8@16"
- "Error setting NVRAM variable: %d"
- "I24@0:8@16"
- "IODeviceTree:/options"
- "IONVRAM-DELETE-PROPERTY"
- "LANVRAM"
- "MCProfileConnectionObserver"
- "Q24@0:8@16"
- "_dtoResultFromLAResult:error:inFamiliarLocation:"
- "auditTokenToData:"
- "boolForKey:"
- "byteForKey:"
- "dataForKey:"
- "dataForKey:nameSpace:"
- "dataUsingEncoding:"
- "getBytes:length:"
- "inFamiliarLocation"
- "initWithData:encoding:"
- "initWithStorageDomain:key:contextID:"
- "initWithStorageDomain:key:contextID:acl:"
- "isLocationBasedPolicy:"
- "profileConnectionDidReceiveAppWhitelistChangedNotification:userInfo:"
- "profileConnectionDidReceiveDefaultsChangedNotification:userInfo:"
- "profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:"
- "profileConnectionDidReceivePasscodeChangedNotification:userInfo:"
- "profileConnectionDidReceivePasscodePolicyChangedNotification:userInfo:"
- "profileConnectionDidReceiveProfileListChangedNotification:userInfo:"
- "profileConnectionDidReceiveRestrictionChangedNotification:userInfo:"
- "q36@0:8@16@24B32"
- "registerObserver:"
- "setData:forKey:"
- "setString:forKey:"
- "sharedConnection"
- "stringForKey:"
- "unregisterObserver:"
- "unsignedIntForKey:"
- "unsignedLongLongForKey:"
- "v32@0:8@\"MCProfileConnection\"16@\"NSDictionary\"24"

```
