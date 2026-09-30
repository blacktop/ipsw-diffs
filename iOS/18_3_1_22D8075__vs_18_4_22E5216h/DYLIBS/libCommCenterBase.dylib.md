## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-12227.1.2.0.0
-  __TEXT.__text: 0xba15c
-  __TEXT.__auth_stubs: 0x1720
+12320.0.0.0.0
+  __TEXT.__text: 0xba1e8
+  __TEXT.__auth_stubs: 0x1760
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__const: 0xddae
-  __TEXT.__gcc_except_tab: 0x10b84
-  __TEXT.__cstring: 0x11e64
-  __TEXT.__oslogstring: 0x1efb
-  __TEXT.__unwind_info: 0x4848
+  __TEXT.__const: 0xddbe
+  __TEXT.__cstring: 0x122e5
+  __TEXT.__gcc_except_tab: 0x11134
+  __TEXT.__oslogstring: 0x2017
+  __TEXT.__unwind_info: 0x4868
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x3bc
-  __TEXT.__objc_methtype: 0x354
+  __TEXT.__objc_methtype: 0x344
   __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x6ea8
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x6d98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xba0
+  __AUTH_CONST.__auth_got: 0xbc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x13420
-  __AUTH_CONST.__cfstring: 0x2b40
+  __AUTH_CONST.__const: 0x135c8
+  __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x80

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5395
-  Symbols:   7781
-  CStrings:  4133
+  Functions: 5384
+  Symbols:   7877
+  CStrings:  4221
 
Symbols:
+ _DNSServiceQueryRecord
+ _TelephonyUtilIsOversteerEnabled
+ __Z15read_rest_valueR21SatelliteSystemStatusRKN3xpc6objectE
+ __Z16write_rest_valueRK21SatelliteSystemStatus
+ __Z24isRedialNeededForEndCode8CSIError
+ __Z8asString16DNSResolverError
+ __Z8asString17InternetTransport
+ __Z8asString21DNSResolverClientType
+ __Z8asString29ConnectionFailureObserverType
+ __ZN17DNSServiceWrapper21dnsServiceQueryRecordEjjPKcttPFvP16_DNSServiceRef_tjjiS1_tttPKvjPvES6_
+ __ZN19CarrierEntitlements15setServiceTokenERKNSt3__110shared_ptrIK8RegistryEERK13PersonalityIDRKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_8optionalIN12entitlements16ServiceTokenTypeEEE
+ __ZN20FeatureConfiguration37isLTESignalBarTableMappingFlagEnabledEv
+ __ZN30TelephonyCapabilitiesInterfaceD0Ev
+ __ZN30TelephonyCapabilitiesInterfaceD1Ev
+ __ZN30TelephonyCapabilitiesInterfaceD2Ev
+ __ZN34LazuliCarrierEntitlementsInterfaceD0Ev
+ __ZN34LazuliCarrierEntitlementsInterfaceD1Ev
+ __ZN34LazuliCarrierEntitlementsInterfaceD2Ev
+ __ZN36CTGPSSatsVisibilityProviderInterfaceD0Ev
+ __ZN36CTGPSSatsVisibilityProviderInterfaceD1Ev
+ __ZN36CTGPSSatsVisibilityProviderInterfaceD2Ev
+ __ZN36RegistrationLocationManagerInterfaceD0Ev
+ __ZN36RegistrationLocationManagerInterfaceD1Ev
+ __ZN36RegistrationLocationManagerInterfaceD2Ev
+ __ZN4rest15read_rest_valueERNS_20PairedDeviceInfoListERKN3xpc6objectE
+ __ZN4rest15read_rest_valueERNS_22NanoRegistryDeviceInfoERKN3xpc6objectE
+ __ZN4rest15read_rest_valueERNS_29getDefaultDataUsageParametersERKN3xpc6objectE
+ __ZN4rest16write_rest_valueERKNS_20PairedDeviceInfoListE
+ __ZN4rest16write_rest_valueERKNS_22NanoRegistryDeviceInfoE
+ __ZN4rest16write_rest_valueERKNS_29getDefaultDataUsageParametersE
+ __ZN4rest29getDefaultDataUsageParametersC1EmbRKN3ctu2cf11CFSharedRefIK9__CFArrayEE
+ __ZN4rest29getDefaultDataUsageParametersC2EmbRKN3ctu2cf11CFSharedRefIK9__CFArrayEE
+ __ZN4rest8asStringENS_17DevicePairingModeE
+ __ZN4rest8asStringENS_17PairedDeviceStateE
+ __ZN4rest8asStringENS_18IDSConnectionStateE
+ __ZN4resteqERKNS_22NanoRegistryDeviceInfoES2_
+ __ZN4restneERKNS_22NanoRegistryDeviceInfoES2_
+ __ZNK17TrafficDescriptor13equalsTrafficERKS_
+ __ZNK3xpc6object9to_stringEv
+ __ZNK4rest20PairedDeviceInfoList15getActiveDeviceEv
+ __ZNK4rest20PairedDeviceInfoList18isAnyDeviceInStateENS_17PairedDeviceStateE
+ __ZNK4rest20PairedDeviceInfoList19getDeviceNameForCsnERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNK4rest20PairedDeviceInfoList23hasDeviceWithIdentifierERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNK8Registry24getTelephonyCapabilitiesEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTI16MockTimerService
+ __ZTI30TelephonyCapabilitiesInterface
+ __ZTI34LazuliCarrierEntitlementsInterface
+ __ZTI36CTGPSSatsVisibilityProviderInterface
+ __ZTI36RegistrationLocationManagerInterface
+ __ZTINSt3__117bad_function_callE
+ __ZTS30TelephonyCapabilitiesInterface
+ __ZTS34LazuliCarrierEntitlementsInterface
+ __ZTS36CTGPSSatsVisibilityProviderInterface
+ __ZTS36RegistrationLocationManagerInterface
+ __ZTV30TelephonyCapabilitiesInterface
+ __ZTV34LazuliCarrierEntitlementsInterface
+ __ZTV36CTGPSSatsVisibilityProviderInterface
+ __ZTV36RegistrationLocationManagerInterface
+ __ZTVNSt3__117bad_function_callE
+ __ZeqRK21SatelliteSystemStatusS1_
+ __ZneRK21SatelliteSystemStatusS1_
+ ___dynamic_cast
+ __os_feature_enabled_impl
+ __os_log_debug_impl
+ _isEmergencyEpsFbError
+ _kServiceTokenType
+ _kServiceTokenValue
+ _kVinylFwUpdatePairingState
- __ZN19CarrierEntitlements15setServiceTokenERKNSt3__110shared_ptrIK8RegistryEERK13PersonalityIDRKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNK8CallInfo41isRedialOverLegacyRATRequestedInErrorCodeEv
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- ___TUAssertTrigger
CStrings:
+ "#D DisplayStatus [isOn=%s, isLocked=%s, isCoversheetActive=%s, isPasscodeSet=%s]"
+ "#D Getting main bundle"
+ "#D Input(%s) = %f"
+ "#D Personality Info: %s - %s"
+ "#D Sending OTASP success dialogue to UI"
+ "#D ThumperID: %s, info: %p"
+ "#D [conn %p] Connection closed."
+ "#D [conn %p] Got REST message: %s"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"
+ "CoreTelephony"
+ "LTESignalBarTableMapping"
+ "cellular_supported"
+ "device_name"
+ "device_state"
+ "feth0"
+ "feth1"
+ "feth10"
+ "feth11"
+ "feth12"
+ "feth13"
+ "feth14"
+ "feth15"
+ "feth16"
+ "feth17"
+ "feth18"
+ "feth19"
+ "feth2"
+ "feth20"
+ "feth3"
+ "feth4"
+ "feth5"
+ "feth6"
+ "feth7"
+ "feth8"
+ "feth9"
+ "identifier"
+ "ids_connection_state"
+ "kAlreadyRegistered"
+ "kBadFlags"
+ "kBadInterfaceIndex"
+ "kBadKey"
+ "kBadParam"
+ "kBadReference"
+ "kBadSig"
+ "kBadState"
+ "kBadTime"
+ "kConfiguring"
+ "kConnected"
+ "kDefunctConnection"
+ "kDoubleNAT"
+ "kEPDG"
+ "kEthernet"
+ "kFirewall"
+ "kIMS"
+ "kIncompatible"
+ "kNATPortMappingDisabled"
+ "kNATPortMappingUnsupported"
+ "kNATTraversal"
+ "kNameConflict"
+ "kNoAuth"
+ "kNoMemory"
+ "kNoRouter"
+ "kNoSuchKey"
+ "kNoSuchName"
+ "kNoSuchRecord"
+ "kNotConnected"
+ "kNotInitialized"
+ "kNotPermitted"
+ "kPolicyDenied"
+ "kPollingMode"
+ "kProximity"
+ "kRCS"
+ "kRCSToken"
+ "kRefused"
+ "kServiceNotRunning"
+ "kStaleData"
+ "kTinker"
+ "kTransferAuthorizationForToken"
+ "kTransient"
+ "kUltraConstrained"
+ "kUnsupported"
+ "kVinylFwUpdatePairingState"
+ "model_identifier"
+ "not active"
+ "requiresResiliency"
+ "token"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@0:8@16"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}24@0:8@16"

```
