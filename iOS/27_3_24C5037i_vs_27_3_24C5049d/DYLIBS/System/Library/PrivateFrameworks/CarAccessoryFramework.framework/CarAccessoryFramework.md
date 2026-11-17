## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-553.9.3.0.0
-  __TEXT.__text: 0xff354
-  __TEXT.__objc_methlist: 0x19ca4
+553.14.1.0.0
+  __TEXT.__text: 0x1007c8
+  __TEXT.__objc_methlist: 0x19ddc
   __TEXT.__const: 0x1b8
+  __TEXT.__cstring: 0x8318
+  __TEXT.__oslogstring: 0x3e53
   __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__oslogstring: 0x3e3a
-  __TEXT.__cstring: 0x8277
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x6878
+  __TEXT.__unwind_info: 0x68e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x28a8
-  __DATA_CONST.__objc_classlist: 0xe48
+  __DATA_CONST.__const: 0x2880
+  __DATA_CONST.__objc_classlist: 0xe50
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x660
+  __DATA_CONST.__objc_protolist: 0x670
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8150
-  __DATA_CONST.__objc_protorefs: 0x5f0
-  __DATA_CONST.__objc_superrefs: 0x830
-  __DATA_CONST.__objc_arraydata: 0xc8e8
-  __DATA_CONST.__got: 0xf80
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0xe560
-  __AUTH_CONST.__objc_const: 0x547d0
-  __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x81e0
+  __DATA_CONST.__objc_protorefs: 0x600
+  __DATA_CONST.__objc_superrefs: 0x848
+  __DATA_CONST.__objc_arraydata: 0xc9c8
+  __DATA_CONST.__got: 0xf98
+  __AUTH_CONST.__const: 0xb20
+  __AUTH_CONST.__cfstring: 0xe620
+  __AUTH_CONST.__objc_const: 0x550d0
   __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_intobj: 0x6a8
+  __AUTH_CONST.__objc_dictobj: 0x6cc0
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x6b80
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x6d0
-  __DATA.__data: 0x4ca0
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x6e0
+  __DATA.__data: 0x4d60
   __DATA_DIRTY.__objc_data: 0x8930
   __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7997
-  Symbols:   13613
-  CStrings:  2245
+  Functions: 8024
+  Symbols:   13669
+  CStrings:  2253
 
Symbols:
+ +[CAFASCAvailability all]
+ +[CAFASCAvailability availabilityWithAccessory:defaultsEnabled:denyIdentifier:capabilityMode:]
+ +[CAFASCAvailability availabilityWithAccessory:service:characteristic:defaultsEnabled:denyIdentifier:capabilityMode:]
+ +[CAFASCAvailability availabilityWithAccessory:service:defaultsEnabled:denyIdentifier:capabilityMode:]
+ +[CAFASCTree _removePath:fromDictionary:]
+ +[CAFDeviceLocale observerProtocol]
+ +[CAFDeviceLocale serviceIdentifier]
+ +[CAFDeviceSettings accessoryIdentifier]
+ +[CAFDeviceSettings observerProtocol]
+ +[CAFUserAuthorizationCharacteristic primaryCharacteristicFormat]
+ +[CAFUserAuthorizationCharacteristic secondaryCharacteristicFormats]
+ -[CAFASCAvailability .cxx_destruct]
+ -[CAFASCAvailability _initWithPath:defaultsEnabled:denyIdentifier:capabilityMode:]
+ -[CAFASCAvailability capabilityMode]
+ -[CAFASCAvailability defaultsEnabled]
+ -[CAFASCAvailability denyIdentifier]
+ -[CAFASCAvailability isDisabledForSessionConfig:featureDenyList:]
+ -[CAFASCAvailability path]
+ -[CAFASCTree userVisibleBrand]
+ -[CAFCar(Accessories) deviceSettings]
+ -[CAFDeviceLocale _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFDeviceLocale addObserver:]
+ -[CAFDeviceLocale name]
+ -[CAFDeviceLocale preferredLanguagesCharacteristic]
+ -[CAFDeviceLocale preferredLanguages]
+ -[CAFDeviceLocale registerObserver:]
+ -[CAFDeviceLocale registeredForPreferredLanguages]
+ -[CAFDeviceLocale removeObserver:]
+ -[CAFDeviceLocale setPreferredLanguages:]
+ -[CAFDeviceLocale unregisterObserver:]
+ -[CAFDeviceSettings addObserver:]
+ -[CAFDeviceSettings deviceLocaleService]
+ -[CAFDeviceSettings deviceLocale]
+ -[CAFDeviceSettings registerObserver:]
+ -[CAFDeviceSettings removeObserver:]
+ -[CAFDeviceSettings unregisterObserver:]
+ -[CAFMessages hasVehicleHandlingWithAI]
+ -[CAFMessages hasVehicleHandling]
+ -[CAFMessages registeredForVehicleHandlingWithAI]
+ -[CAFMessages registeredForVehicleHandling]
+ -[CAFMessages setVehicleHandling:]
+ -[CAFMessages setVehicleHandlingWithAI:]
+ -[CAFMessages vehicleHandlingCharacteristic]
+ -[CAFMessages vehicleHandlingWithAICharacteristic]
+ -[CAFMessages vehicleHandlingWithAI]
+ -[CAFMessages vehicleHandling]
+ -[CAFUserAuthorizationCharacteristic formattedValue]
+ -[CAFUserAuthorizationCharacteristic setUserAuthorizationValue:]
+ -[CAFUserAuthorizationCharacteristic userAuthorizationValue]
+ -[CAFVehicleInformation hasUserVisibleVehicleBrand]
+ -[CAFVehicleInformation hasVehicleUserVisibleLabel]
+ -[CAFVehicleInformation registeredForUserVisibleVehicleBrand]
+ -[CAFVehicleInformation userVisibleVehicleBrandCharacteristic]
+ -[CAFVehicleInformation userVisibleVehicleBrand]
+ GCC_except_table50
+ _CAFASCAvailabilityLogging
+ _CAFASCAvailabilityLogging.facility
+ _CAFASCAvailabilityLogging.onceToken
+ _CAFAccessoryTypeDeviceSettings
+ _CAFCharacteristicTypePreferredLanguages
+ _CAFCharacteristicTypeVehicleHandling
+ _CAFCharacteristicTypeVehicleHandlingWithAI
+ _CAFServiceTypeDeviceLocale
+ _NSStringFromUserAuthorization
+ _OBJC_CLASS_$_CAFASCAvailability
+ _OBJC_CLASS_$_CAFDeviceLocale
+ _OBJC_CLASS_$_CAFDeviceSettings
+ _OBJC_CLASS_$_CAFUserAuthorizationCharacteristic
+ _OBJC_CLASS_$_CRCarPlayFeatureDenyList
+ _OBJC_CLASS_$_CRCarPlayPreferences
+ _OBJC_IVAR_$_CAFASCAvailability._capabilityMode
+ _OBJC_IVAR_$_CAFASCAvailability._defaultsEnabled
+ _OBJC_IVAR_$_CAFASCAvailability._denyIdentifier
+ _OBJC_IVAR_$_CAFASCAvailability._path
+ _OBJC_IVAR_$_CAFASCTree._userVisibleBrand
+ _OBJC_METACLASS_$_CAFASCAvailability
+ _OBJC_METACLASS_$_CAFDeviceLocale
+ _OBJC_METACLASS_$_CAFDeviceSettings
+ _OBJC_METACLASS_$_CAFUserAuthorizationCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFASCAvailability
+ __OBJC_$_CLASS_METHODS_CAFDeviceLocale
+ __OBJC_$_CLASS_METHODS_CAFDeviceSettings
+ __OBJC_$_CLASS_METHODS_CAFUserAuthorizationCharacteristic
+ __OBJC_$_CLASS_PROP_LIST_CAFASCAvailability
+ __OBJC_$_INSTANCE_METHODS_CAFASCAvailability
+ __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
+ __OBJC_$_INSTANCE_METHODS_CAFDeviceLocale
+ __OBJC_$_INSTANCE_METHODS_CAFDeviceSettings
+ __OBJC_$_INSTANCE_METHODS_CAFUserAuthorizationCharacteristic
+ __OBJC_$_INSTANCE_VARIABLES_CAFASCAvailability
+ __OBJC_$_PROP_LIST_CAFASCAvailability
+ __OBJC_$_PROP_LIST_CAFDeviceLocale
+ __OBJC_$_PROP_LIST_CAFDeviceSettings
+ __OBJC_$_PROP_LIST_CAFUserAuthorizationCharacteristic
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFDeviceLocaleObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFDeviceLocaleObserver
+ __OBJC_$_PROTOCOL_REFS_CAFDeviceLocaleObserver
+ __OBJC_$_PROTOCOL_REFS_CAFDeviceSettingsObserver
+ __OBJC_CLASS_RO_$_CAFASCAvailability
+ __OBJC_CLASS_RO_$_CAFDeviceLocale
+ __OBJC_CLASS_RO_$_CAFDeviceSettings
+ __OBJC_CLASS_RO_$_CAFUserAuthorizationCharacteristic
+ __OBJC_LABEL_PROTOCOL_$_CAFDeviceLocaleObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFDeviceSettingsObserver
+ __OBJC_METACLASS_RO_$_CAFASCAvailability
+ __OBJC_METACLASS_RO_$_CAFDeviceLocale
+ __OBJC_METACLASS_RO_$_CAFDeviceSettings
+ __OBJC_METACLASS_RO_$_CAFUserAuthorizationCharacteristic
+ __OBJC_PROTOCOL_$_CAFDeviceLocaleObserver
+ __OBJC_PROTOCOL_$_CAFDeviceSettingsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFDeviceLocaleObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFDeviceSettingsObserver
+ ___25+[CAFASCAvailability all]_block_invoke
+ ___CAFASCAvailabilityLogging_block_invoke
+ _all.all
+ _all.onceToken
- +[CAFMessageAIProcessingCharacteristic primaryCharacteristicFormat]
- +[CAFMessageAIProcessingCharacteristic secondaryCharacteristicFormats]
- +[CAFMessageHandlingCharacteristic primaryCharacteristicFormat]
- +[CAFMessageHandlingCharacteristic secondaryCharacteristicFormats]
- +[CAFSyncContactsCharacteristic primaryCharacteristicFormat]
- +[CAFSyncContactsCharacteristic secondaryCharacteristicFormats]
- -[CAFASCTree routeSharingUserVisibleBrand]
- -[CAFMessageAIProcessingCharacteristic formattedValue]
- -[CAFMessageAIProcessingCharacteristic messageAIProcessingValue]
- -[CAFMessageAIProcessingCharacteristic setMessageAIProcessingValue:]
- -[CAFMessageHandlingCharacteristic formattedValue]
- -[CAFMessageHandlingCharacteristic messageHandlingValue]
- -[CAFMessageHandlingCharacteristic setMessageHandlingValue:]
- -[CAFMessages hasInterimBluetoothGroupMessaging]
- -[CAFMessages hasMessageAIProcessing]
- -[CAFMessages hasMessageHandling]
- -[CAFMessages interimBluetoothGroupMessagingCharacteristic]
- -[CAFMessages interimBluetoothGroupMessaging]
- -[CAFMessages messageAIProcessingCharacteristic]
- -[CAFMessages messageAIProcessing]
- -[CAFMessages messageHandlingCharacteristic]
- -[CAFMessages messageHandling]
- -[CAFMessages registeredForInterimBluetoothGroupMessaging]
- -[CAFMessages registeredForMessageAIProcessing]
- -[CAFMessages registeredForMessageHandling]
- -[CAFMessages setMessageAIProcessing:]
- -[CAFMessages setMessageHandling:]
- -[CAFSyncContactsCharacteristic formattedValue]
- -[CAFSyncContactsCharacteristic setSyncContactsValue:]
- -[CAFSyncContactsCharacteristic syncContactsValue]
- GCC_except_table49
- _CAFCharacteristicTypeInterimBluetoothGroupMessaging
- _CAFCharacteristicTypeMessageAIProcessing
- _CAFCharacteristicTypeMessageHandling
- _NSStringFromMessageAIProcessing
- _NSStringFromMessageHandling
- _NSStringFromSyncContacts
- _OBJC_CLASS_$_CAFMessageAIProcessingCharacteristic
- _OBJC_CLASS_$_CAFMessageHandlingCharacteristic
- _OBJC_CLASS_$_CAFSyncContactsCharacteristic
- _OBJC_IVAR_$_CAFASCTree._routeSharingUserVisibleBrand
- _OBJC_METACLASS_$_CAFMessageAIProcessingCharacteristic
- _OBJC_METACLASS_$_CAFMessageHandlingCharacteristic
- _OBJC_METACLASS_$_CAFSyncContactsCharacteristic
- __OBJC_$_CLASS_METHODS_CAFMessageAIProcessingCharacteristic
- __OBJC_$_CLASS_METHODS_CAFMessageHandlingCharacteristic
- __OBJC_$_CLASS_METHODS_CAFSyncContactsCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
- __OBJC_$_INSTANCE_METHODS_CAFMessageAIProcessingCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFMessageHandlingCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFSyncContactsCharacteristic
- __OBJC_$_PROP_LIST_CAFMessageAIProcessingCharacteristic
- __OBJC_$_PROP_LIST_CAFMessageHandlingCharacteristic
- __OBJC_$_PROP_LIST_CAFSyncContactsCharacteristic
- __OBJC_CLASS_RO_$_CAFMessageAIProcessingCharacteristic
- __OBJC_CLASS_RO_$_CAFMessageHandlingCharacteristic
- __OBJC_CLASS_RO_$_CAFSyncContactsCharacteristic
- __OBJC_METACLASS_RO_$_CAFMessageAIProcessingCharacteristic
- __OBJC_METACLASS_RO_$_CAFMessageHandlingCharacteristic
- __OBJC_METACLASS_RO_$_CAFSyncContactsCharacteristic
CStrings:
+ "%s %@ defaultsDisabled=%@ denyListDisabled=%@ capabilityMode=%ld"
+ "-[CAFASCAvailability isDisabledForSessionConfig:featureDenyList:]"
+ "."
+ "0x0000000001B00001"
+ "0x0000000027000002"
+ "0x0000000046000014"
+ "0x0000000053000006"
+ "0x0000000053000007"
+ "Accepted"
+ "CAFASCAvailability"
+ "Declined"
+ "DeviceLocale"
+ "DeviceSettings"
+ "PreferredLanguages"
+ "UserAuthorization"
+ "VehicleHandling"
+ "VehicleHandlingWithAI"
- "%s %@ routeSharing mode=%ld disabled=%@"
- "0x0000000053000002"
- "0x0000000053000003"
- "0x0000000053000004"
- "Authorized"
- "Denied"
- "InterimBluetoothGroupMessaging"
- "MessageAIProcessing"
- "MessageHandling"
```
