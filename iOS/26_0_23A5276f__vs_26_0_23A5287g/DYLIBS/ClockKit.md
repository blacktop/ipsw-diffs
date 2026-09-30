## ClockKit

> `/System/Library/Frameworks/ClockKit.framework/ClockKit`

```diff

-2483.297.0.0.0
-  __TEXT.__text: 0x6a5fc
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x93b4
+2483.306.0.0.0
+  __TEXT.__text: 0x6a13c
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x9454
   __TEXT.__const: 0xaae
-  __TEXT.__cstring: 0x401e
-  __TEXT.__oslogstring: 0x27cd
-  __TEXT.__gcc_except_tab: 0x1084
-  __TEXT.__dlopen_cstrs: 0x39f
+  __TEXT.__cstring: 0x3e1b
+  __TEXT.__oslogstring: 0x27cf
+  __TEXT.__gcc_except_tab: 0x1040
+  __TEXT.__dlopen_cstrs: 0x349
   __TEXT.__ustring: 0x80
   __TEXT.__constg_swiftt: 0xd0
   __TEXT.__swift5_typeref: 0xab

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x2438
-  __TEXT.__objc_classname: 0x1e34
-  __TEXT.__objc_methname: 0xf2aa
-  __TEXT.__objc_methtype: 0x1b83
-  __TEXT.__objc_stubs: 0x8f60
-  __DATA_CONST.__got: 0x6f0
-  __DATA_CONST.__const: 0x1c60
+  __TEXT.__unwind_info: 0x2428
+  __TEXT.__objc_classname: 0x1e35
+  __TEXT.__objc_methname: 0xf4d4
+  __TEXT.__objc_methtype: 0x1b9b
+  __TEXT.__objc_stubs: 0x9060
+  __DATA_CONST.__got: 0x6f8
+  __DATA_CONST.__const: 0x1c20
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33c0
+  __DATA_CONST.__objc_selrefs: 0x3438
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x4f0
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0xef8
-  __AUTH_CONST.__cfstring: 0x53c0
-  __AUTH_CONST.__objc_const: 0xf698
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0xf38
+  __AUTH_CONST.__cfstring: 0x5280
+  __AUTH_CONST.__objc_const: 0xf788
   __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH_CONST.__objc_doubleobj: 0x350
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3660
-  __DATA.__objc_ivar: 0xac0
+  __DATA.__objc_ivar: 0xad0
   __DATA.__data: 0x678
-  __DATA.__bss: 0xb90
+  __DATA.__bss: 0xbb0
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1b8
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 810F0F00-3910-37BA-87DE-529129A41FCC
-  Functions: 3772
-  Symbols:   11928
-  CStrings:  4477
+  UUID: F07397D3-0453-30D5-9515-20728277EEF2
+  Functions: 3783
+  Symbols:   11956
+  CStrings:  4478
 
Symbols:
+ +[CLKDevice CLKDeviceUUIDForPDRDevice:]
+ +[CLKDevice PDRDeviceIsRunningDaytonaOrLater:]
+ +[CLKDevice PDRProductVersionForPDRDevice:]
+ +[CLKDevice _createCurrentDeviceWithPDRDevice:]
+ +[CLKDevice _createCurrentDeviceWithPDRDevice:].cold.1
+ +[CLKDevice _handlePDRDeviceChanged:]
+ +[CLKDevice _pdrCapabilityFromNRDeviceCapability:]
+ +[CLKDevice _pdrCapabilityFromNRDeviceCapability:].cold.1
+ +[CLKDevice _uint32FromHexString:]
+ +[CLKDevice activePDRDevice]
+ +[CLKDevice activePDRDevice].cold.1
+ +[CLKDevice activePDRDevice].cold.2
+ +[CLKDevice deviceForPDRDevice:]
+ +[CLKDevice deviceForPDRDevice:forced:]
+ +[CLKDevice deviceForPairingID:]
+ +[CLKDevice deviceForPairingID:forced:]
+ +[CLKDevice pdrDeviceForPairingID:]
+ -[CLKDevice cachedCapabilitiesLock]
+ -[CLKDevice initWithPDRDevice:]
+ -[CLKDevice isRunningGloryBOrLater]
+ -[CLKDevice isRunningGloryEOrLater]
+ -[CLKDevice pairingID]
+ -[CLKDevice pdrDeviceVersion]
+ -[CLKDevice pdrDevice]
+ -[CLKDevice supportsPDRCapability:]
+ -[CLKDeviceDescriptor initWithPairingID:]
+ -[CLKDeviceDescriptor pairingID]
+ GCC_except_table139
+ GCC_except_table28
+ _CLKDeviceIsPDRDevicePaired
+ _OBJC_CLASS_$_PDRDarwinNotifications
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_IVAR_$_CLKDevice._cachedCapabilitiesLock
+ _OBJC_IVAR_$_CLKDevice._isRunningGloryBOrLater
+ _OBJC_IVAR_$_CLKDevice._isRunningGloryEOrLater
+ _OBJC_IVAR_$_CLKDevice._pdrDevice
+ _OBJC_IVAR_$_CLKDeviceDescriptor._pairingID
+ _PDRDevicePropertyKeyDeviceBrand
+ _PDRDevicePropertyKeyDeviceHousingColor
+ _PDRDevicePropertyKeyDeviceSubBrand
+ _PDRDevicePropertyKeyDmin
+ _PDRDevicePropertyKeyIsAltAccount
+ _PDRDevicePropertyKeyMainScreenClass
+ _PDRDevicePropertyKeyProductType
+ _PDRDidActivateNotification
+ _PDRDidPairNotification
+ _PDRNotificationKeyDevice
+ _PDRVersionIsGreaterThanOrEqual
+ _PDRWatchOSVersionForRemoteDevice
+ ___37+[CLKDevice _handlePDRDeviceChanged:]_block_invoke
+ ___50+[CLKDevice _pdrCapabilityFromNRDeviceCapability:]_block_invoke
+ ___block_literal_global.312
+ ___block_literal_global.42
+ ___block_literal_global.51
+ ___block_literal_global.636
+ ___block_literal_global.676
+ ___block_literal_global.679
+ __pdrCapabilityFromNRDeviceCapability:.__lock
+ __pdrCapabilityFromNRDeviceCapability:.__lookup
+ __pdrCapabilityFromNRDeviceCapability:.onceToken
+ _objc_msgSend$CLKDeviceUUIDForPDRDevice:
+ _objc_msgSend$PDRDeviceIsRunningDaytonaOrLater:
+ _objc_msgSend$PDRProductVersionForPDRDevice:
+ _objc_msgSend$_createCurrentDeviceWithPDRDevice:
+ _objc_msgSend$_handlePDRDeviceChanged:
+ _objc_msgSend$_pdrCapabilityFromNRDeviceCapability:
+ _objc_msgSend$_uint32FromHexString:
+ _objc_msgSend$activePDRDevice
+ _objc_msgSend$deviceForPDRDevice:forced:
+ _objc_msgSend$deviceForPairingID:
+ _objc_msgSend$deviceForPairingID:forced:
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$initWithDomain:pdrDevice:
+ _objc_msgSend$initWithPDRDevice:
+ _objc_msgSend$initWithPairingID:
+ _objc_msgSend$isPaired
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$pairedDeviceDidChangeCapabilities
+ _objc_msgSend$pdrDevice
+ _objc_msgSend$pdrDeviceForPairingID:
+ _objc_msgSend$pdrDeviceVersion
+ _objc_msgSend$scanHexInt:
+ _objc_msgSend$supportsPDRCapability:
+ _objc_msgSend$unsignedIntValue
- +[CLKDevice NRDeviceIsRunningDaytonaOrLater:]
- +[CLKDevice _createCurrentDeviceWithNRDevice:]
- +[CLKDevice _createCurrentDeviceWithNRDevice:].cold.1
- +[CLKDevice _handleNRDeviceChanged:]
- +[CLKDevice activeNRDevice]
- +[CLKDevice activeNRDevice].cold.1
- +[CLKDevice activeNRDevice].cold.2
- +[CLKDevice nrDeviceForNRDeviceUUID:]
- +[CLKDevice nrDeviceForNRDeviceUUID:].cold.1
- +[CLKDevice nrDeviceForNRDeviceUUID:].cold.2
- -[CLKDevice initWithNRDevice:]
- -[CLKDevice setNrDevice:]
- -[CLKDeviceDescriptor initWithNRDevice:]
- -[CLKDeviceDescriptor initWithNRDeviceUUID:]
- -[CLKDeviceDescriptor nrDeviceUUID]
- GCC_except_table123
- _CLKActiveComplicationsFromPairedDevice.cold.1
- _CLKActiveComplicationsFromPairedDevice.cold.2
- _NRDevicePropertyDeviceBrand
- _NRDevicePropertyDeviceHousingColor
- _NRDevicePropertyDeviceSubBrand
- _NRDevicePropertyDmin
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyMainScreenClass
- _NRDevicePropertyProductType
- _NRPairedDeviceRegistryDevice
- _NRPairedDeviceRegistryDeviceDidBecomeActive
- _NRPairedDeviceRegistryDeviceDidPairNotification
- _NRPairedDeviceRegistryPairedDeviceDidChangeCapabilitiesDarwinNotification
- _NanoRegistryLibrary
- _NanoRegistryLibraryCore.frameworkLibrary
- _OBJC_IVAR_$_CLKDeviceDescriptor._nrDeviceUUID
- __OBJC_$_PROP_LIST_CLKDevice
- ___37+[CLKDevice nrDeviceForNRDeviceUUID:]_block_invoke
- ___NanoRegistryLibraryCore_block_invoke
- ___block_descriptor_40_e8_32s_e18_B16?0"NRDevice"8ls32l8
- ___block_literal_global.57
- ___block_literal_global.630
- ___block_literal_global.670
- ___block_literal_global.673
- ___getNRVersionIsGreaterThanOrEqualSymbolLoc_block_invoke
- ___getNRWatchOSVersionForRemoteDeviceSymbolLoc_block_invoke
- _audit_stringNanoRegistry
- _getNRVersionIsGreaterThanOrEqualSymbolLoc.ptr
- _getNRWatchOSVersionForRemoteDeviceSymbolLoc.ptr
- _objc_msgSend$NRDeviceIsRunningDaytonaOrLater:
- _objc_msgSend$_createCurrentDeviceWithNRDevice:
- _objc_msgSend$_handleNRDeviceChanged:
- _objc_msgSend$activeNRDevice
- _objc_msgSend$activePairedDeviceSelectorBlock
- _objc_msgSend$deviceForNRDeviceUUID:
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithDomain:pairedDevice:
- _objc_msgSend$initWithNRDevice:
- _objc_msgSend$initWithNRDeviceUUID:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$nrDevice
- _objc_msgSend$nrDeviceForNRDeviceUUID:
- _objc_msgSend$nrDeviceUUID
- _objc_msgSend$nrDeviceVersion
- _objc_msgSend$setNrDevice:
CStrings:
+ "+[CLKDevice activePDRDevice]"
+ "+[PDRDarwinNotifications pairedDeviceDidChangeCapabilities] capabilities changed sending CLKActiveDeviceChangedNotification for CLKDevice: %@"
+ "@\"PDRDevice\""
+ "B20@0:8I16"
+ "CLKDeviceUUIDForPDRDevice:"
+ "Creating a CLKDevice without an PDRDevice: %@"
+ "Creating a CLKDevice. pdrDevice: %{public}@"
+ "Got +[PDRDarwinNotifications pairedDeviceDidChangeCapabilities] refresh CLKDevice: %@"
+ "NR Capability: %@ - %08x"
+ "PDRDeviceIsRunningDaytonaOrLater:"
+ "PDRProductVersionForPDRDevice:"
+ "Received device paired notification, but skipping PDRDevice update because UUID is nil"
+ "Resetting current device with pdrDevice %{public}@ - isNil:%lu hasEntitlement:%lu"
+ "T@\"NRDevice\",R,N"
+ "T@\"NSUUID\",R,N,V_pairingID"
+ "T@\"PDRDevice\",R,N,V_pdrDevice"
+ "TB,R,N,V_isRunningGloryBOrLater"
+ "TB,R,N,V_isRunningGloryEOrLater"
+ "TQ,N"
+ "T{os_unfair_lock_s=I},R,N,V_cachedCapabilitiesLock"
+ "_cachedCapabilitiesLock"
+ "_createCurrentDeviceWithPDRDevice:"
+ "_handlePDRDeviceChanged:"
+ "_isRunningGloryBOrLater"
+ "_isRunningGloryEOrLater"
+ "_pairingID"
+ "_pdrCapabilityFromNRDeviceCapability:"
+ "_pdrDevice"
+ "_uint32FromHexString:"
+ "activePDRDevice"
+ "cachedCapabilitiesLock"
+ "deviceForPDRDevice:"
+ "deviceForPDRDevice:forced:"
+ "deviceForPairingID:"
+ "deviceForPairingID:forced:"
+ "getActivePairedDeviceIncludingAltAccount"
+ "initWithDomain:pdrDevice:"
+ "initWithPDRDevice:"
+ "initWithPairingID:"
+ "isRunningGloryBOrLater"
+ "isRunningGloryEOrLater"
+ "new PDRDevice became active - %{public}@"
+ "numberWithUnsignedInt:"
+ "pairedDeviceDidChangeCapabilities"
+ "pdrDevice"
+ "pdrDeviceForPairingID:"
+ "pdrDeviceVersion"
+ "scanHexInt:"
+ "supportsPDRCapability:"
+ "unsignedIntValue"
- "+[CLKDevice activeNRDevice]"
- "+[CLKDevice nrDeviceForNRDeviceUUID:]"
- "35165B81-461F-4423-8903-A50CEFB1C204"
- "46526F47-0B4B-41FF-A959-AC358550958C"
- "4AA3FF3B-3224-42E6-995E-481F49AE9260"
- "873627CA-D131-46F4-B477-E653F7445DF9"
- "887DC9F2-A55D-41F6-8639-64776A041BF1"
- "AB764CE8-D4DF-4DB6-991C-3A298E380BD1"
- "B16@?0@\"NRDevice\"8"
- "Creating a CLKDevice without an NRDevice: %@"
- "Creating a CLKDevice. nrDevice: %{public}@"
- "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
- "DAB81146-4105-445B-94AD-14033A199AC4"
- "E553D9C1-2587-4142-B286-C556E89F51F3"
- "E7B1CD81-445C-4840-9F24-3A32B510B6A1"
- "FEBBC201-B013-4680-94B0-7F4129F4CCB8"
- "Got NRPairedDeviceRegistryPairedDeviceDidChangeCapabilitiesDarwinNotification refresh CLKDevice: %@"
- "NRDeviceIsRunningDaytonaOrLater:"
- "NRPairedDeviceRegistryPairedDeviceDidChangeCapabilitiesDarwinNotification capabilities changed sending CLKActiveDeviceChangedNotification for CLKDevice: %@"
- "NRVersionIsGreaterThanOrEqual"
- "NRWatchOSVersionForRemoteDevice"
- "Received device paired notification, but skipping NRDevice update because UUID is nil"
- "Resetting current device with nrdevice %{public}@ - isNil:%lu hasEntitlement:%lu"
- "T@\"NRDevice\",&,N,V_nrDevice"
- "T@\"NSUUID\",R,N,V_nrDeviceUUID"
- "_createCurrentDeviceWithNRDevice:"
- "_handleNRDeviceChanged:"
- "_nrDeviceUUID"
- "activeNRDevice"
- "activePairedDeviceSelectorBlock"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "initWithDomain:pairedDevice:"
- "initWithNRDevice:"
- "initWithNRDeviceUUID:"
- "initWithUUIDString:"
- "new NRDevice became active - %{public}@"
- "nrDeviceForNRDeviceUUID:"
- "setNrDevice:"
- "softlink:r:path:/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry"
- "\xd4"

```
