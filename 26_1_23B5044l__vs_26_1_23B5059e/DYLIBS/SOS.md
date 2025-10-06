## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-656.100.5.0.0
-  __TEXT.__text: 0x37448
+656.200.1.0.0
+  __TEXT.__text: 0x3738c
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_methlist: 0x38a4
   __TEXT.__const: 0x266
-  __TEXT.__cstring: 0x4ac2
+  __TEXT.__cstring: 0x4a22
   __TEXT.__oslogstring: 0x62e9
   __TEXT.__gcc_except_tab: 0x918
   __TEXT.__dlopen_cstrs: 0x39f

   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xf98
+  __TEXT.__unwind_info: 0xfa8
   __TEXT.__objc_classname: 0x586
-  __TEXT.__objc_methname: 0xaa66
+  __TEXT.__objc_methname: 0xaa67
   __TEXT.__objc_methtype: 0x1acb
   __TEXT.__objc_stubs: 0x7660
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__got: 0x370
   __DATA_CONST.__const: 0x1100
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x4160
+  __AUTH_CONST.__cfstring: 0x40e0
   __AUTH_CONST.__objc_const: 0x4b78
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x120

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: E4943DAE-6020-38EC-8990-1B2F0A55CA1A
+  UUID: F7A62A89-48D5-3D94-B262-494B57A75D45
   Functions: 1432
-  Symbols:   5046
-  CStrings:  3553
+  Symbols:   5047
+  CStrings:  3545
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyIsAltAccount
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.904
+ ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.908
+ ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1018
+ ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.915
+ ___block_literal_global.1027
+ ___block_literal_global.1029
+ ___block_literal_global.1031
+ ___block_literal_global.880
+ ___block_literal_global.889
+ ___block_literal_global.917
+ _objc_msgSend$getActivePairedDeviceExcludingAltAccount
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$initWithDomain:pdrDevice:
- _NRDevicePropertyIsAltAccount
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.911
- ___101+[SOSUtilities setKappaTriggersEmergencySOS:isWristDetectionEnabled:confirmationDelegate:completion:]_block_invoke.915
- ___111+[SOSUtilities setKappaThirdPartyActive:forApp:forPairedDevice:presentConfirmationOnViewController:completion:]_block_invoke.1027
- ___77+[SOSUtilities setKappaTriggersEmergencySOS:confirmationDelegate:completion:]_block_invoke.922
- ___block_literal_global.1039
- ___block_literal_global.1041
- ___block_literal_global.1055
- ___block_literal_global.894
- ___block_literal_global.896
- ___block_literal_global.924
- _objc_msgSend$activeDeviceSelectorBlock
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithDomain:pairedDevice:
Functions:
~ +[SOSUtilities activeDeviceSupportsNewton] : 104 -> 64
~ +[SOSUtilities activeDeviceSupportsNewtonWorkoutsOnly] : 120 -> 80
~ +[SOSUtilities activeDevice] : 176 -> 132
~ +[SOSUtilities isKappaDetectionSupportedOnActiveWatch] : 104 -> 64
~ +[SOSUtilities activeDeviceSupportsMandrake] : 104 -> 64
~ +[SOSUtilities activeDeviceHasMandrake] : 360 -> 376
CStrings:
+ "getActivePairedDeviceExcludingAltAccount"
+ "getActivePairedDeviceIncludingAltAccount"
+ "initWithDomain:pdrDevice:"
- "4B46048D-CD7A-4E74-B615-D9376CBCBBFF"
- "891D0E88-9AB8-420F-8FB5-92A1D4C58DAE"
- "96B0DD78-1F0E-4F92-875F-DD6374FCCB10"
- "98409C1B-D02D-400B-9F63-33784EFEDA85"
- "activeDeviceSelectorBlock"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "initWithDomain:pairedDevice:"

```
