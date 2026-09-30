## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-193.9.0.0.0
-  __TEXT.__text: 0xae108
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x98a4
-  __TEXT.__const: 0x276b
+194.22.1.1.1
+  __TEXT.__text: 0xb35f4
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_methlist: 0x9a84
+  __TEXT.__const: 0x27fb
   __TEXT.__oslogstring: 0x2678
-  __TEXT.__cstring: 0x143d8
-  __TEXT.__gcc_except_tab: 0x2cf4
+  __TEXT.__cstring: 0x14646
+  __TEXT.__gcc_except_tab: 0x2c68
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x1fb8
-  __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x728
-  __TEXT.__objc_methname: 0x157e3
-  __TEXT.__objc_methtype: 0x23cb
-  __TEXT.__objc_stubs: 0xb0a0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x5368
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__unwind_info: 0x21c0
+  __TEXT.__objc_classname: 0x754
+  __TEXT.__objc_methname: 0x15d11
+  __TEXT.__objc_methtype: 0x2407
+  __TEXT.__objc_stubs: 0xb3c0
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0x5120
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bf8
+  __DATA_CONST.__objc_selrefs: 0x4d00
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0xcb80
-  __AUTH_CONST.__objc_const: 0x10fa8
+  __AUTH_CONST.__auth_got: 0x9b8
+  __AUTH_CONST.__const: 0x420
+  __AUTH_CONST.__cfstring: 0xcd00
+  __AUTH_CONST.__objc_const: 0x11288
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0xeac
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0xec8
   __DATA.__data: 0xe68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x1d0
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x178
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D421E68F-F76B-32A6-916A-8BF91296C669
-  Functions: 4075
-  Symbols:   13155
-  CStrings:  9893
+  UUID: F012820F-70D4-3AAE-8CA1-5E2AA5995955
+  Functions: 4180
+  Symbols:   13405
+  CStrings:  9992
 
Symbols:
+ +[CBConnection selfConnectedPairAndReturnError:]
+ +[CBConnection selfConnectedPairAndReturnError:].cold.1
+ +[CBController bluetoothKeyboardDeviceCount]
+ +[CBController nonBluetoothKeyboardDeviceCount]
+ +[CBController numberOfKeyboardDevices]
+ +[CBController systemHasOnlyBluetoothKeyboardDevices]
+ -[CBAccessorySetupMetadata .cxx_destruct]
+ -[CBAccessorySetupMetadata manufacturerID]
+ -[CBAccessorySetupMetadata modelID]
+ -[CBAccessorySetupMetadata rssiOffsetProxPairing]
+ -[CBAccessorySetupMetadata setManufacturerID:]
+ -[CBAccessorySetupMetadata setModelID:]
+ -[CBAccessorySetupMetadata setRssiOffsetProxPairing:]
+ -[CBAdvertiser heySiriDeviceGroup]
+ -[CBAdvertiser heySiriQuantizedScore]
+ -[CBAdvertiser setHeySiriDeviceGroup:]
+ -[CBAdvertiser setHeySiriQuantizedScore:]
+ -[CBConnectionPair .cxx_destruct]
+ -[CBConnectionPair clientConnection]
+ -[CBConnectionPair serverConnection]
+ -[CBConnectionPair setClientConnection:]
+ -[CBConnectionPair setServerConnection:]
+ -[CBController LPMCompletionTimeoutSeconds]
+ -[CBDevice _clearProximityServiceManufacturerID]
+ -[CBDevice _clearProximityServiceModelID]
+ -[CBDevice _parseProximityPairingAppleTVRemotePtr:end:]
+ -[CBDevice _parseProximityPairingPtr:end:badType:badLen:]
+ -[CBDevice _parseProximityServiceAccessorySetupPtr:end:]
+ -[CBDevice _parseProximityServiceData:dataChanged:]
+ -[CBDevice _parseProximityServiceSubType:src:end:dataChanged:]
+ -[CBDevice heySiriDeviceGroup]
+ -[CBDevice heySiriQuantizedScore]
+ -[CBDevice proximityPairingClassicAddress]
+ -[CBDevice proximityPairingConnectionMethod]
+ -[CBDevice proximityServiceManufacturerID]
+ -[CBDevice proximityServiceModelID]
+ -[CBDevice setHeySiriDeviceGroup:]
+ -[CBDevice setHeySiriQuantizedScore:]
+ -[CBDevice setProximityPairingClassicAddress:]
+ -[CBDevice setProximityPairingConnectionMethod:]
+ -[CBDevice setProximityServiceManufacturerID:]
+ -[CBDevice setProximityServiceModelID:]
+ -[CBL2CAPChannel setSocketFD:]
+ GCC_except_table135
+ GCC_except_table148
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table405
+ GCC_except_table419
+ GCC_except_table474
+ GCC_except_table51
+ GCC_except_table59
+ GCC_except_table98
+ _CBCentralManagerScanOptionHeySiriElectionEndTimeNsec
+ _CBDiscoveryTypeFromString
+ _CBDiscoveryTypesAllCases
+ _CBDiscoveryTypesNeedsAccessorySetupMetadata
+ _CBDiscoveryTypesNeedsAccessorySetupMetadata.cold.1
+ _CBDiscoveryTypesProximityPairing
+ _CBDiscoveryTypesProximityPairing.cold.1
+ _CBNearbyActionFlagsToString
+ _CBNearbyActionTypeAllCases
+ _CBNearbyActionTypeFromString
+ _CBProximityServiceSubTypeToString
+ _CBUUIDSecureSensorIndicatorCharacteristicString
+ _CBUUIDSecureSensorInertialOdometryCharacteristicString
+ _CUPrintFlags
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_CBAccessorySetupMetadata
+ _OBJC_CLASS_$_CBConnectionPair
+ _OBJC_IVAR_$_CBAccessorySetupMetadata._manufacturerID
+ _OBJC_IVAR_$_CBAccessorySetupMetadata._modelID
+ _OBJC_IVAR_$_CBAccessorySetupMetadata._rssiOffsetProxPairing
+ _OBJC_IVAR_$_CBAdvertiser._heySiriDeviceGroup
+ _OBJC_IVAR_$_CBAdvertiser._heySiriQuantizedScore
+ _OBJC_IVAR_$_CBConnectionPair._clientConnection
+ _OBJC_IVAR_$_CBConnectionPair._serverConnection
+ _OBJC_IVAR_$_CBController._LPMCompletionTimeoutSeconds
+ _OBJC_METACLASS_$_CBAccessorySetupMetadata
+ _OBJC_METACLASS_$_CBConnectionPair
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ __OBJC_$_CLASS_METHODS_CBConnection
+ __OBJC_$_INSTANCE_METHODS_CBAccessorySetupMetadata
+ __OBJC_$_INSTANCE_METHODS_CBConnectionPair
+ __OBJC_$_INSTANCE_VARIABLES_CBAccessorySetupMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CBConnectionPair
+ __OBJC_$_PROP_LIST_CBAccessorySetupMetadata
+ __OBJC_$_PROP_LIST_CBConnectionPair
+ __OBJC_CLASS_RO_$_CBAccessorySetupMetadata
+ __OBJC_CLASS_RO_$_CBConnectionPair
+ __OBJC_METACLASS_RO_$_CBAccessorySetupMetadata
+ __OBJC_METACLASS_RO_$_CBConnectionPair
+ ___35-[CBDiscovery _activateDirectStart]_block_invoke.175
+ ___35-[CBDiscovery _activateDirectStart]_block_invoke_2.178
+ ___38-[CBAdvertiser setHeySiriDeviceGroup:]_block_invoke
+ ___41-[CBAdvertiser setHeySiriQuantizedScore:]_block_invoke
+ ___CBDiscoveryTypesNeedsAccessorySetupMetadata_block_invoke
+ ___CBDiscoveryTypesProximityPairing_block_invoke
+ ___block_literal_global.128
+ ___block_literal_global.138
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.480
+ ___block_literal_global.520
+ ___block_literal_global.74
+ ___block_literal_global.805
+ ___block_literal_global.853
+ ___block_literal_global.92
+ _objc_msgSend$_clearProximityServiceManufacturerID
+ _objc_msgSend$_clearProximityServiceModelID
+ _objc_msgSend$_parseProximityPairingAppleTVRemotePtr:end:
+ _objc_msgSend$_parseProximityPairingPtr:end:badType:badLen:
+ _objc_msgSend$_parseProximityServiceAccessorySetupPtr:end:
+ _objc_msgSend$_parseProximityServiceData:dataChanged:
+ _objc_msgSend$_parseProximityServiceSubType:src:end:dataChanged:
+ _objc_msgSend$heySiriDeviceGroup
+ _objc_msgSend$heySiriQuantizedScore
+ _objc_msgSend$proximityPairingClassicAddress
+ _objc_msgSend$proximityPairingConnectionMethod
+ _objc_msgSend$proximityServiceManufacturerID
+ _objc_msgSend$proximityServiceModelID
+ _objc_msgSend$setClientConnection:
+ _objc_msgSend$setHeySiriDeviceGroup:
+ _objc_msgSend$setHeySiriQuantizedScore:
+ _objc_msgSend$setProximityPairingClassicAddress:
+ _objc_msgSend$setProximityPairingConnectionMethod:
+ _objc_msgSend$setProximityServiceManufacturerID:
+ _objc_msgSend$setProximityServiceModelID:
+ _objc_msgSend$setServerConnection:
+ _objc_msgSend$setSocketFD:
+ _objc_msgSend$setTransmitPowerOne:
+ _objc_msgSend$setTransmitPowerThree:
+ _objc_msgSend$setTransmitPowerTwo:
+ _objc_msgSend$transmitPowerOne
+ _objc_msgSend$transmitPowerThree
+ _objc_msgSend$transmitPowerTwo
+ _socketpair
- -[CBAdvertiser heySiriProductType]
- -[CBAdvertiser setHeySiriProductType:]
- -[CBDevice _parseProximityServiceData:]
- -[CBDevice heySiriProductType]
- -[CBDevice isEqualToDevice:exactMatch:].cold.105
- -[CBDevice isEqualToDevice:exactMatch:].cold.106
- -[CBDevice isEqualToDevice:exactMatch:].cold.107
- -[CBDevice setHeySiriProductType:]
- GCC_except_table133
- GCC_except_table146
- GCC_except_table26
- GCC_except_table29
- GCC_except_table393
- GCC_except_table407
- GCC_except_table458
- GCC_except_table72
- GCC_except_table92
- _CBProximityPairingSubTypeToString
- _OBJC_IVAR_$_CBAdvertiser._heySiriProductType
- ___35-[CBDiscovery _activateDirectStart]_block_invoke.174
- ___35-[CBDiscovery _activateDirectStart]_block_invoke_2.177
- ___38-[CBAdvertiser setHeySiriProductType:]_block_invoke
- ___block_literal_global.127
- ___block_literal_global.137
- ___block_literal_global.266
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.280
- ___block_literal_global.282
- ___block_literal_global.284
- ___block_literal_global.439
- ___block_literal_global.457
- ___block_literal_global.73
- ___block_literal_global.784
- ___block_literal_global.792
- ___block_literal_global.91
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_parseProximityServiceData:
- _objc_msgSend$heySiriProductType
- _objc_msgSend$setHeySiriProductType:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ ", %@ %@"
+ ", %@ 0x%02X"
+ ", %s %d"
+ ", appID %@"
+ ", hsDG %u"
+ ", hsQS %u"
+ ", psMI <%@>"
+ ", psMf <%@>"
+ "12F99E346BFA4F6492CE33CBF59CA363.chargingcase.wireless.fill"
+ "711495D10BB643F6BDA3693886C0BCAF"
+ "@\"CBConnection\""
+ "ATVRemote1,3"
+ "ATVRemote1,4"
+ "Activated: CID 0x%X, XPC, State %s, Discoverable %s, Inquiry %s, Timeout 0x%X"
+ "AppleTVRemote"
+ "B24@0:8r^{?=[7C]}16"
+ "CBAccessorySetupMetadata"
+ "CBConnectionPair"
+ "CLink"
+ "CmpAuth"
+ "CompanionSetup"
+ "LPMCompletionTimeoutSeconds"
+ "MobileBluetooth-194.22.1.1.1"
+ "ProximityHandoffSource"
+ "ProximityHandoffTarget"
+ "ProximityServiceAccessorySetup"
+ "RDLink"
+ "Secure Sensor Indicator"
+ "Secure Sensor Inertial Odometry"
+ "T@\"CBConnection\",&,N,V_clientConnection"
+ "T@\"CBConnection\",&,N,V_serverConnection"
+ "T@\"NSData\",C,N,V_manufacturerID"
+ "T@\"NSData\",C,N,V_modelID"
+ "TC,N,V_heySiriDeviceClass"
+ "TC,N,V_heySiriDeviceGroup"
+ "TC,N,V_heySiriQuantizedScore"
+ "TC,R,N,V_LPMCompletionTimeoutSeconds"
+ "TVLatency"
+ "T^{?=[7C]},R,N"
+ "Tc,N,V_rssiOffsetProxPairing"
+ "ThirdPartyAudioSwitching"
+ "Ti,N,V_socketFD"
+ "^{?=[7C]}16@0:8"
+ "_LPMCompletionTimeoutSeconds"
+ "_clearProximityServiceManufacturerID"
+ "_clearProximityServiceModelID"
+ "_clientConnection"
+ "_heySiriDeviceGroup"
+ "_heySiriQuantizedScore"
+ "_manufacturerID"
+ "_modelID"
+ "_parseProximityPairingAppleTVRemotePtr:end:"
+ "_parseProximityPairingPtr:end:badType:badLen:"
+ "_parseProximityServiceAccessorySetupPtr:end:"
+ "_parseProximityServiceData:dataChanged:"
+ "_parseProximityServiceSubType:src:end:dataChanged:"
+ "_rssiOffsetProxPairing"
+ "_serverConnection"
+ "bluetoothKeyboardDeviceCount"
+ "clientConnection"
+ "df970512-e36f-4b5e-a9af-02a16d9a1400"
+ "df970612-e36f-4b5e-a9af-02a16d9a1400"
+ "heySiriDeviceGroup"
+ "heySiriDeviceGroup %u = %u"
+ "heySiriQuantizedScore"
+ "heySiriQuantizedScore %u = %u"
+ "hh"
+ "hsDG"
+ "hsDG: %u -> %u"
+ "hsQS"
+ "hsQS: %u -> %u"
+ "kCBScanOptionHeySiriElectionEndTimeNsec"
+ "lpmCTO"
+ "manufacturerID"
+ "modelID"
+ "nonBluetoothKeyboardDeviceCount"
+ "numberOfKeyboardDevices"
+ "ppCA"
+ "ppCM"
+ "proximityPairingClassicAddress"
+ "proximityPairingConnectionMethod"
+ "proximityServiceManufacturerID"
+ "proximityServiceModelID"
+ "psMI"
+ "psMf"
+ "rssiOffsetProxPairing"
+ "selfConnectedPairAndReturnError:"
+ "serverConnection"
+ "setClientConnection:"
+ "setHeySiriDeviceGroup:"
+ "setHeySiriQuantizedScore:"
+ "setManufacturerID:"
+ "setModelID:"
+ "setProximityPairingClassicAddress:"
+ "setProximityPairingConnectionMethod:"
+ "setProximityServiceManufacturerID:"
+ "setProximityServiceModelID:"
+ "setRssiOffsetProxPairing:"
+ "setServerConnection:"
+ "setSocketFD:"
+ "socketpair failed"
+ "systemHasOnlyBluetoothKeyboardDevices"
+ "v40@0:8C16r*20r*28B36"
+ "v40@0:8r*16r*24C32C36"
+ "{?=\"bitArray\"[7C]}"
- ", hsPT %s"
- "Activated: CID 0x%X, XPC, State %s, Discoverable %s, Inquiry %s"
- "B24@0:8r^{?=[6C]}16"
- "HomePodA"
- "HomePodMini"
- "MobileBluetooth-193.9"
- "TC,N,V_heySiriProductType"
- "TS,N,V_heySiriDeviceClass"
- "T^{?=[6C]},R,N"
- "^{?=[6C]}16@0:8"
- "_heySiriProductType"
- "_parseProximityServiceData:"
- "heySiriProductType"
- "heySiriProductType %s = %s"
- "hsPT"
- "hsPT: %s -> %s"
- "setHeySiriProductType:"
- "{?=\"bitArray\"[6C]}"

```
