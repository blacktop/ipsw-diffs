## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-553.12.2.0.0
-  __TEXT.__text: 0x42f78
+553.17.5.0.0
+  __TEXT.__text: 0x43e70
   __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x4064
+  __TEXT.__objc_methlist: 0x409c
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x4201
-  __TEXT.__gcc_except_tab: 0x72c
-  __TEXT.__oslogstring: 0x45a3
+  __TEXT.__cstring: 0x429d
+  __TEXT.__gcc_except_tab: 0x728
+  __TEXT.__oslogstring: 0x4791
   __TEXT.__ustring: 0x62
   __TEXT.__dlopen_cstrs: 0x15e
-  __TEXT.__unwind_info: 0x12ec
-  __TEXT.__objc_classname: 0x900
-  __TEXT.__objc_methname: 0xd1b8
-  __TEXT.__objc_methtype: 0x1cc7
-  __TEXT.__objc_stubs: 0x7e60
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x1a30
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __TEXT.__unwind_info: 0x132c
+  __TEXT.__objc_classname: 0x93e
+  __TEXT.__objc_methname: 0xd252
+  __TEXT.__objc_methtype: 0x1cee
+  __TEXT.__objc_stubs: 0x7ee0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x1ad0
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb558
-  __DATA_CONST.__objc_selrefs: 0x2a18
-  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_const: 0xb908
+  __DATA_CONST.__objc_selrefs: 0x2a30
+  __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_classrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x4700
-  __AUTH_CONST.__objc_const: 0x18a8
-  __AUTH_CONST.__const: 0x11e0
+  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__objc_const: 0x18f0
+  __AUTH_CONST.__const: 0x1240
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x558
-  __AUTH.__objc_data: 0xc30
+  __AUTH.__objc_data: 0xb40
   __DATA.__objc_ivar: 0x598
-  __DATA.__data: 0xe48
-  __DATA.__bss: 0x2c8
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA.__data: 0xec8
+  __DATA.__bss: 0x2b8
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2081
-  Symbols:   7264
-  CStrings:  3438
+  Functions: 2106
+  Symbols:   7344
+  CStrings:  3455
 
Symbols:
+ +[CRCertificationOverridesClient _servicePerformBlock:errorHandler:]
+ +[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]
+ +[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]
+ -[CARSession _handleViewAreaChangeWithPayload:].cold.1
+ -[CARSession _handleViewAreaChangeWithPayload:].cold.2
+ -[CRVehicle copyWithZone:]
+ _CarCertificationOverrideLogging
+ _CarCertificationOverrideLogging.facility
+ _CarCertificationOverrideLogging.onceToken
+ _OBJC_CLASS_$_CRCertificationOverridesClient
+ _OBJC_METACLASS_$_CRCertificationOverridesClient
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_CRCertificationOverridesClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRCertificationOverridesService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRCertificationOverridesService
+ __OBJC_$_PROTOCOL_REFS_CRCertificationOverridesService
+ __OBJC_CLASS_RO_$_CRCertificationOverridesClient
+ __OBJC_LABEL_PROTOCOL_$_CRCertificationOverridesService
+ __OBJC_METACLASS_RO_$_CRCertificationOverridesClient
+ __OBJC_PROTOCOL_$_CRCertificationOverridesService
+ __OBJC_PROTOCOL_REFERENCE_$_CRCertificationOverridesService
+ ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.232
+ ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.232.cold.1
+ ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.233
+ ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.233.cold.1
+ ___68+[CRCertificationOverridesClient _servicePerformBlock:errorHandler:]_block_invoke
+ ___68+[CRCertificationOverridesClient _servicePerformBlock:errorHandler:]_block_invoke_2
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke.29
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke.29.cold.1
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke.32
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke.32.cold.1
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke.9
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke.9.cold.1
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke_2
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke_2.cold.1
+ ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke
+ ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke.12
+ ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke.12.cold.1
+ ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke_2
+ ___CRFetchInstrumentClusterURLs_block_invoke
+ ___CarCertificationOverrideLogging_block_invoke
+ ___block_descriptor_40_e8_32bs_e52_v24?0"<CRCertificationOverridesService>"8?<v?>16ls32l8
+ ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32bs40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e52_v24?0"<CRCertificationOverridesService>"8?<v?>16ls32l8s40l8
+ ___block_literal_global.14
+ ___block_literal_global.31
+ ___kCFBooleanFalse
+ _objc_msgSend$_servicePerformBlock:errorHandler:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:
+ _objc_msgSend$setNextSessionOverrideAirPlayFeatureStrings:completion:
+ _objc_msgSend$supportedAirPlayFeaturesForVehicleIdentifier:reply:
- ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.229
- ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.229.cold.1
- ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.230
- ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.230.cold.1
- ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke.28
- ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke.28.cold.1
- ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke_2.cold.2
- ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke.31
- ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke.31.cold.1
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
- ___block_literal_global.30
- _objc_msgSend$supportedCarPlayFeaturesForVehicleIdentifier:reply:
CStrings:
+ "\x13\x1b\x18\x12"
+ "CRCertificationOverridesClient"
+ "CRCertificationOverridesService"
+ "CertificationOverrides"
+ "Request for view area index %{public}@, which is out of range for screen %@"
+ "Resetting to first view area for for view area index %{public}@, which is out of range for screen %@."
+ "T@\"NSNumber\",&,N,V_supportsStartSessionRequest"
+ "_servicePerformBlock:errorHandler:"
+ "com.apple.carkit.certificationOverrides.service"
+ "connecting to CRCertificationOverridesService"
+ "fetchNextSessionOverrideAirPlayFeatureStrings: %{public}@ error: %{public}@"
+ "fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion failed: %{public}@"
+ "fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:"
+ "kCPSessionVehicleInformationKey"
+ "setNextSessionOverrideAirPlayFeatureStrings failed: %{public}@"
+ "setNextSessionOverrideAirPlayFeatureStrings succeeded"
+ "setNextSessionOverrideAirPlayFeatureStrings: %{public}@"
+ "setNextSessionOverrideAirPlayFeatureStrings:completion:"
+ "supportedAirPlayFeaturesForVehicleIdentifier call failed: %@"
+ "supportedAirPlayFeaturesForVehicleIdentifier: call failed: %{public}@"
+ "supportedAirPlayFeaturesForVehicleIdentifier:reply:"
+ "v24@?0@\"<CRCertificationOverridesService>\"8@?<v@?>16"
+ "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "\x13\x1b\x16\x11\x12"
- "T@\"NSNumber\",N,V_supportsStartSessionRequest"
- "supportedCarPlayFeaturesForVehicleIdentifier call failed: %@"
- "supportedCarPlayFeaturesForVehicleIdentifier: %{public}lu"
- "supportedCarPlayFeaturesForVehicleIdentifier: call failed: %{public}@"
- "supportedCarPlayFeaturesForVehicleIdentifier:reply:"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\"@\"NSError\">24"

```
