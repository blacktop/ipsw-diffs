## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-  __TEXT.__text: 0x267ec
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0x2ac0
-  __TEXT.__objc_methlist: 0x17f8
-  __TEXT.__const: 0xd50
-  __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__objc_methname: 0x4155
-  __TEXT.__cstring: 0xf85
-  __TEXT.__oslogstring: 0x2b11
-  __TEXT.__objc_classname: 0xd0b
-  __TEXT.__objc_methtype: 0x884
+  __TEXT.__text: 0x284c0
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__objc_stubs: 0x2fe0
+  __TEXT.__objc_methlist: 0x1b08
+  __TEXT.__const: 0xd78
+  __TEXT.__gcc_except_tab: 0x2b8
+  __TEXT.__objc_methname: 0x4aad
+  __TEXT.__cstring: 0xfeb
+  __TEXT.__oslogstring: 0x2c8d
+  __TEXT.__objc_classname: 0xd7a
+  __TEXT.__objc_methtype: 0xc96
   __TEXT.__dlopen_cstrs: 0x2ac
-  __TEXT.__constg_swiftt: 0x9e0
-  __TEXT.__swift5_typeref: 0xb38
+  __TEXT.__constg_swiftt: 0xa0c
+  __TEXT.__swift5_typeref: 0xb4e
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x4c6
+  __TEXT.__swift5_reflstr: 0x4ba
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x78
-  __TEXT.__swift5_fieldmd: 0x5c8
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift5_fieldmd: 0x5d8
   __TEXT.__swift5_capture: 0x3cc
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift_as_entry: 0x84
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x88
-  __TEXT.__unwind_info: 0xb48
+  __TEXT.__unwind_info: 0xbe0
   __TEXT.__eh_frame: 0xdfc
-  __DATA_CONST.__const: 0xfe0
-  __DATA_CONST.__cfstring: 0xac0
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__const: 0x1078
+  __DATA_CONST.__cfstring: 0xae0
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x848
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__auth_ptr: 0x188
-  __DATA.__objc_const: 0x34b0
-  __DATA.__objc_selrefs: 0xe98
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__objc_data: 0x1728
-  __DATA.__data: 0x1038
-  __DATA.__bss: 0x630
+  __DATA_CONST.__auth_got: 0x870
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__auth_ptr: 0x190
+  __DATA.__objc_const: 0x38b8
+  __DATA.__objc_selrefs: 0x10a8
+  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_data: 0x1828
+  __DATA.__data: 0x10c0
+  __DATA.__bss: 0x650
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppManagedFeatures.framework/AppManagedFeatures
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 860
-  Symbols:   403
-  CStrings:  1230
+  Functions: 918
+  Symbols:   416
+  CStrings:  1364
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _LSUserApplicationType
+ _MAEGetActivationStateWithError
+ _OBJC_CLASS_$_BuddyActivationConfiguration
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_LSApplicationIdentity
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_METACLASS_$_BuddyActivationConfiguration
+ _kMAActivationStateUnactivated
+ _objc_enumerationMutation
+ _swift_release_x28
CStrings:
+ "&"
+ "@\"CoreTelephonyClient\""
+ "@\"NSMutableSet\""
+ "Activation Configuration Delegates Queue"
+ "Activation State Queue"
+ "B24@0:8Q16"
+ "BuddyActivationConfiguration"
+ "BuddyMigrator: Persisting initial app state for partial-setup detection"
+ "CoreTelephonyClientDataDelegate"
+ "Failed to get activation state: %{public}@"
+ "Supports Cellular Activation: %d (method is %ld)"
+ "T@\"CoreTelephonyClient\",&,V_telephonyClient"
+ "T@\"NSMutableSet\",&,V_delegates"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_activationStateQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_delegateQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_telephonyQueue"
+ "TB,N,V_hasActivated"
+ "TB,N,V_initialActivationState"
+ "TB,R"
+ "TB,R,GisActivated"
+ "TB,V_activationMethodChanged"
+ "TQ,N,V_cellularActivationMethod"
+ "Telephony Queue"
+ "Unable to get availability status to see if cellular activation is supported: %{public}@"
+ "Unable to get bootstrap status to see if cellular activation is supported: %{public}@"
+ "Updating cellular activation method..."
+ "_TtC13BuddyMigrator20BuddyAppStateManager"
+ "_activationMethodChanged"
+ "_activationStateChanged"
+ "_activationStateQueue"
+ "_cellularActivationMethod"
+ "_delegateQueue"
+ "_delegates"
+ "_hasActivated"
+ "_initialActivationState"
+ "_registerForActivationStateNotification"
+ "_supportsCellularActivationForMethod:"
+ "_telephonyClient"
+ "_telephonyQueue"
+ "activated"
+ "activationConfigurationChanged:isActivated:"
+ "activationMethodChanged"
+ "activationStateQueue"
+ "addDelegate:"
+ "addObject:"
+ "anbrActivationState:enabled:"
+ "anbrBitrateRecommendation:bitrate:direction:"
+ "available"
+ "cellularActivationMethod"
+ "com.apple.mobile.lockdown.activation_state"
+ "connectionActivationError:connection:error:"
+ "connectionAvailability:availableConnections:"
+ "connectionStateChanged:connection:dataConnectionStatusInfo:"
+ "countByEnumeratingWithState:objects:count:"
+ "currentAppStates"
+ "currentDataServiceDescriptorChanged:"
+ "currentDataSimChanged:"
+ "dataRoamingSettingsChanged:status:"
+ "dataSettingsChanged:"
+ "dataStatus:dataStatusInfo:"
+ "delegateQueue"
+ "delegates"
+ "enumeratorWithOptions:"
+ "getConnectionAvailability:connectionType:error:"
+ "hasActivated"
+ "identities"
+ "identityString"
+ "initWithBuddyPreferencesExcludedFromBackup:"
+ "initWithQueue:"
+ "initialActivationState"
+ "internetConnectionActivationError:"
+ "internetConnectionAvailability:"
+ "internetConnectionStateChanged:"
+ "internetDataStatus:"
+ "internetDataStatusBasic:"
+ "isActivated"
+ "nextObject"
+ "notifyDelegatesConfigurationChanged:"
+ "notifyDelegatesConfigurationChanged:isActivated:"
+ "nrSliceAppStateChanged:status:trafficDescriptors:"
+ "nrSlicedRunningAppStateChanged:"
+ "persist:to:"
+ "preferredDataServiceDescriptorChanged:"
+ "preferredDataSimChanged:"
+ "pttSlicingCapabilityDidChange:"
+ "regDataModeChanged:dataMode:"
+ "removeDelegate:"
+ "removeObject:"
+ "serviceDisconnection:status:"
+ "servingNetworkChanged:"
+ "setActivationMethodChanged:"
+ "setActivationStateQueue:"
+ "setCellularActivationMethod:"
+ "setDelegateQueue:"
+ "setDelegates:"
+ "setHasActivated:"
+ "setInitialActivationState:"
+ "setTelephonyClient:"
+ "setTelephonyQueue:"
+ "supportsCellularActivation"
+ "telephonyClient"
+ "telephonyQueue"
+ "tetheringStatus:"
+ "tetheringStatus:connectionType:"
+ "typeForInstallMachinery"
+ "uniqueInstallIdentifier"
+ "usingBootstrapDataService:"
+ "v20@0:8i16"
+ "v24@0:8@\"CTDataConnectionStatus\"16"
+ "v24@0:8@\"CTDataSettings\"16"
+ "v24@0:8@\"CTDataStatus\"16"
+ "v24@0:8@\"CTDataStatusBasic\"16"
+ "v24@0:8@\"CTServiceDescriptor\"16"
+ "v24@0:8@\"CTSlicedRunningAppInfoContainer\"16"
+ "v24@0:8@\"CTTetheringStatus\"16"
+ "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8B16B20"
+ "v28@0:8@\"CTServiceDescriptor\"16B24"
+ "v28@0:8@\"CTTetheringStatus\"16i24"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
+ "v28@0:8@16B24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTDataStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTServiceDisconnectionStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28"
+ "v32@0:8@16@24"
+ "v32@0:8@16i24i28"
+ "v36@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24i32"
+ "v36@0:8@\"CTXPCServiceSubscriptionContext\"16i24@\"CTDataConnectionStatus\"28"
+ "v36@0:8@\"NSString\"16B24@\"CTTrafficDescriptorsContainer\"28"
+ "v36@0:8@16@24i32"
+ "v36@0:8@16B24@28"
+ "v36@0:8@16i24@28"
- "isNewMandatorySUFlowEnabled"
- "isNewMigrationSUFlowEnabled"
- "isNewRestoreSUFlowEnabled"

```
