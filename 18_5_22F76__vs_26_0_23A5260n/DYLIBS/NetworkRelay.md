## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-578.120.3.0.0
-  __TEXT.__text: 0x67654
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x1814
-  __TEXT.__const: 0x1f0
+658.0.0.0.2
+  __TEXT.__text: 0x6b4bc
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x1ad4
+  __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x8b4
-  __TEXT.__cstring: 0xdb0e
-  __TEXT.__oslogstring: 0x1237
-  __TEXT.__unwind_info: 0x890
-  __TEXT.__objc_classname: 0x325
-  __TEXT.__objc_methname: 0x4302
-  __TEXT.__objc_methtype: 0x74d
-  __TEXT.__objc_stubs: 0x2720
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0xd58
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__cstring: 0xe0e4
+  __TEXT.__oslogstring: 0x124c
+  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__objc_classname: 0x362
+  __TEXT.__objc_methname: 0x4948
+  __TEXT.__objc_methtype: 0x797
+  __TEXT.__objc_stubs: 0x2b20
+  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__const: 0xdd8
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd80
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_selrefs: 0xea0
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x45c0
-  __AUTH_CONST.__objc_const: 0x41d0
-  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0x590
+  __AUTH_CONST.__cfstring: 0x4b80
+  __AUTH_CONST.__objc_const: 0x4830
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x47c
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0x4d4
   __DATA.__data: 0x218
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x248
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x278
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8530ADD7-3CF0-3BEF-9BB1-B3B2D093A98A
-  Functions: 818
-  Symbols:   2997
-  CStrings:  3178
+  UUID: 6906435C-88B0-3DA7-9E5E-9EE86B0DDC79
+  Functions: 891
+  Symbols:   3258
+  CStrings:  3366
 
Symbols:
+ +[NRDeviceInfo supportsSecureCoding]
+ +[NRDeviceProxyInfo supportsSecureCoding]
+ -[NRDeviceInfo .cxx_destruct]
+ -[NRDeviceInfo connectedInterfaceName]
+ -[NRDeviceInfo connectedLinkSubtype]
+ -[NRDeviceInfo connectedLinkType]
+ -[NRDeviceInfo copyWithZone:]
+ -[NRDeviceInfo description]
+ -[NRDeviceInfo encodeWithCoder:]
+ -[NRDeviceInfo initWithCoder:]
+ -[NRDeviceInfo isEqual:]
+ -[NRDeviceInfo localEndpoint]
+ -[NRDeviceInfo nrDeviceIdentifier]
+ -[NRDeviceInfo proxyInfo]
+ -[NRDeviceInfo remoteEndpoint]
+ -[NRDeviceInfo setConnectedInterfaceName:]
+ -[NRDeviceInfo setConnectedLinkSubtype:]
+ -[NRDeviceInfo setConnectedLinkType:]
+ -[NRDeviceInfo setLocalEndpoint:]
+ -[NRDeviceInfo setNrDeviceIdentifier:]
+ -[NRDeviceInfo setProxyInfo:]
+ -[NRDeviceInfo setRemoteEndpoint:]
+ -[NRDeviceMonitor deviceInfo]
+ -[NRDeviceOperationalProperties allowsApplicationServiceConnections]
+ -[NRDeviceOperationalProperties flags]
+ -[NRDeviceOperationalProperties proxyProviderAuthMode]
+ -[NRDeviceOperationalProperties proxyProviderType]
+ -[NRDeviceOperationalProperties setAllowsApplicationServiceConnections:]
+ -[NRDeviceOperationalProperties setFlags:]
+ -[NRDeviceOperationalProperties setProxyProviderAuthMode:]
+ -[NRDeviceOperationalProperties setProxyProviderType:]
+ -[NRDevicePairingCriteria bluetoothRole]
+ -[NRDevicePairingCriteria serviceUUID]
+ -[NRDevicePairingCriteria setBluetoothRole:]
+ -[NRDevicePairingCriteria setServiceUUID:]
+ -[NRDeviceProxyInfo .cxx_destruct]
+ -[NRDeviceProxyInfo copyWithZone:]
+ -[NRDeviceProxyInfo description]
+ -[NRDeviceProxyInfo encodeWithCoder:]
+ -[NRDeviceProxyInfo httpConnectPSKIdentity]
+ -[NRDeviceProxyInfo httpConnectPSK]
+ -[NRDeviceProxyInfo httpConnectPassword]
+ -[NRDeviceProxyInfo httpConnectURLs]
+ -[NRDeviceProxyInfo httpConnectUserName]
+ -[NRDeviceProxyInfo initWithCoder:]
+ -[NRDeviceProxyInfo isEqual:]
+ -[NRDeviceProxyInfo proxyProviderType]
+ -[NRDeviceProxyInfo setHttpConnectPSK:]
+ -[NRDeviceProxyInfo setHttpConnectPSKIdentity:]
+ -[NRDeviceProxyInfo setHttpConnectPassword:]
+ -[NRDeviceProxyInfo setHttpConnectURLs:]
+ -[NRDeviceProxyInfo setHttpConnectUserName:]
+ -[NRDeviceProxyInfo setProxyProviderType:]
+ -[NREndpoint initInternalWithDeviceIdentifier:portString:dataProtectionClass:service:]
+ -[NREndpoint initWithDeviceIdentifier:portString:dataProtectionClass:service:]
+ -[NREndpoint service]
+ -[NREndpoint usesASQUIC]
+ -[NRParametersServiceConnection initWithDeviceIdentifier:dataProtectionClass:options:]
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table24
+ GCC_except_table265
+ GCC_except_table320
+ GCC_except_table345
+ GCC_except_table422
+ GCC_except_table433
+ GCC_except_table67
+ GCC_except_table671
+ GCC_except_table675
+ GCC_except_table679
+ GCC_except_table683
+ GCC_except_table705
+ GCC_except_table708
+ GCC_except_table712
+ GCC_except_table717
+ GCC_except_table719
+ GCC_except_table721
+ GCC_except_table724
+ GCC_except_table726
+ GCC_except_table78
+ _CFRelease
+ _NRConvertMachTimeToMicroseconds
+ _NRCreateLocalIdentity
+ _NRDiffMachTimeInSeconds
+ _NRDiffMicroTimeInSeconds
+ _NREndpointCopyDictionary
+ _NREndpointUsesASQUIC
+ _NRParametersOptionAllowsQR
+ _OBJC_CLASS_$_NRDeviceInfo
+ _OBJC_CLASS_$_NRDeviceProxyInfo
+ _OBJC_CLASS_$_NRParametersServiceConnection
+ _OBJC_CLASS_$_NWEndpoint
+ _OBJC_IVAR_$_NRDeviceIdentifier._internalEphemeralBluetoothUUID
+ _OBJC_IVAR_$_NRDeviceInfo._connectedInterfaceName
+ _OBJC_IVAR_$_NRDeviceInfo._connectedLinkSubtype
+ _OBJC_IVAR_$_NRDeviceInfo._connectedLinkType
+ _OBJC_IVAR_$_NRDeviceInfo._localEndpoint
+ _OBJC_IVAR_$_NRDeviceInfo._nrDeviceIdentifier
+ _OBJC_IVAR_$_NRDeviceInfo._proxyInfo
+ _OBJC_IVAR_$_NRDeviceInfo._remoteEndpoint
+ _OBJC_IVAR_$_NRDeviceMonitor._internalDeviceInfo
+ _OBJC_IVAR_$_NRDeviceOperationalProperties._flags
+ _OBJC_IVAR_$_NRDeviceOperationalProperties._proxyProviderAuthMode
+ _OBJC_IVAR_$_NRDeviceOperationalProperties._proxyProviderType
+ _OBJC_IVAR_$_NRDevicePairingCriteria._bluetoothRole
+ _OBJC_IVAR_$_NRDevicePairingCriteria._serviceUUID
+ _OBJC_IVAR_$_NRDeviceProxyInfo._httpConnectPSK
+ _OBJC_IVAR_$_NRDeviceProxyInfo._httpConnectPSKIdentity
+ _OBJC_IVAR_$_NRDeviceProxyInfo._httpConnectPassword
+ _OBJC_IVAR_$_NRDeviceProxyInfo._httpConnectURLs
+ _OBJC_IVAR_$_NRDeviceProxyInfo._httpConnectUserName
+ _OBJC_IVAR_$_NRDeviceProxyInfo._proxyProviderType
+ _OBJC_IVAR_$_NREndpoint._service
+ _OBJC_IVAR_$_NREndpoint._usesASQUIC
+ _OBJC_METACLASS_$_NRDeviceInfo
+ _OBJC_METACLASS_$_NRDeviceProxyInfo
+ _OBJC_METACLASS_$_NRParametersServiceConnection
+ _SecGenerateSelfSignedCertificate
+ _SecIdentityCreate
+ _SecKeyCopyPublicKey
+ _SecKeyCreateRandomKey
+ __OBJC_$_CLASS_METHODS_NRDeviceInfo
+ __OBJC_$_CLASS_METHODS_NRDeviceProxyInfo
+ __OBJC_$_CLASS_PROP_LIST_NRDeviceInfo
+ __OBJC_$_CLASS_PROP_LIST_NRDeviceProxyInfo
+ __OBJC_$_INSTANCE_METHODS_NRDeviceInfo
+ __OBJC_$_INSTANCE_METHODS_NRDeviceProxyInfo
+ __OBJC_$_INSTANCE_METHODS_NRParametersServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_NRDeviceInfo
+ __OBJC_$_INSTANCE_VARIABLES_NRDeviceProxyInfo
+ __OBJC_$_PROP_LIST_NRDeviceInfo
+ __OBJC_$_PROP_LIST_NRDeviceProxyInfo
+ __OBJC_CLASS_PROTOCOLS_$_NRDeviceInfo
+ __OBJC_CLASS_PROTOCOLS_$_NRDeviceProxyInfo
+ __OBJC_CLASS_RO_$_NRDeviceInfo
+ __OBJC_CLASS_RO_$_NRDeviceProxyInfo
+ __OBJC_CLASS_RO_$_NRParametersServiceConnection
+ __OBJC_METACLASS_RO_$_NRDeviceInfo
+ __OBJC_METACLASS_RO_$_NRDeviceProxyInfo
+ __OBJC_METACLASS_RO_$_NRParametersServiceConnection
+ ___86-[NRParametersServiceConnection initWithDeviceIdentifier:dataProtectionClass:options:]_block_invoke
+ ___Block_byref_object_copy_.1143
+ ___Block_byref_object_copy_.1936
+ ___Block_byref_object_copy_.2772
+ ___Block_byref_object_dispose_.1144
+ ___Block_byref_object_dispose_.1937
+ ___Block_byref_object_dispose_.2773
+ ___NSArray0__struct
+ ___NSDictionary0__struct
+ ___block_descriptor_32_e42_v16?0"NSObject<OS_nw_protocol_options>"8l
+ ___block_descriptor_54_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.100
+ ___block_literal_global.1054
+ ___block_literal_global.1128
+ ___block_literal_global.114
+ ___block_literal_global.1230
+ ___block_literal_global.1529
+ ___block_literal_global.1709
+ ___block_literal_global.1915
+ ___block_literal_global.1949
+ ___block_literal_global.1970
+ ___block_literal_global.228
+ ___block_literal_global.2749
+ ___block_literal_global.29
+ ___block_literal_global.2935
+ ___block_literal_global.346
+ ___block_literal_global.408
+ ___block_literal_global.435
+ ___block_literal_global.442
+ ___block_literal_global.467
+ ___block_literal_global.512
+ ___block_literal_global.516
+ ___block_literal_global.525
+ ___block_literal_global.560
+ ___block_literal_global.663
+ ___block_literal_global.676
+ ___block_literal_global.70
+ ___block_literal_global.810
+ ___block_literal_global.84
+ ___block_literal_global.91
+ ___block_literal_global.96
+ ___block_literal_global.972
+ ___nrCopyClassCIdentity_block_invoke
+ ___nrCopyClassDIdentity_block_invoke
+ ___nrCopyLogObj_block_invoke.1061
+ ___nrCopyLogObj_block_invoke.1136
+ ___nrCopyLogObj_block_invoke.1222
+ ___nrCopyLogObj_block_invoke.1533
+ ___nrCopyLogObj_block_invoke.166
+ ___nrCopyLogObj_block_invoke.1714
+ ___nrCopyLogObj_block_invoke.1871
+ ___nrCopyLogObj_block_invoke.1958
+ ___nrCopyLogObj_block_invoke.1981
+ ___nrCopyLogObj_block_invoke.236
+ ___nrCopyLogObj_block_invoke.2760
+ ___nrCopyLogObj_block_invoke.2916
+ ___nrCopyLogObj_block_invoke.350
+ ___nrCopyLogObj_block_invoke.403
+ ___nrCopyLogObj_block_invoke.471
+ ___nrCopyLogObj_block_invoke.566
+ ___nrCopyLogObj_block_invoke.680
+ ___nrCopyLogObj_block_invoke.78
+ ___nrCopyLogObj_block_invoke.818
+ ___nrCopyLogObj_block_invoke.976
+ ___nr_get_mach_timebase_block_invoke
+ _createStringFromNRDeviceProxyProviderAuthMode
+ _createStringFromNRDeviceProxyProviderType
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _mach_absolute_time
+ _mach_continuous_time
+ _mach_timebase_info
+ _nrCopyClassCIdentity.classCIdentity
+ _nrCopyClassCIdentity.onceToken
+ _nrCopyClassDIdentity.classDIdentity
+ _nrCopyClassDIdentity.onceToken
+ _nrCopyLogObj.1074
+ _nrCopyLogObj.1145
+ _nrCopyLogObj.117
+ _nrCopyLogObj.1215
+ _nrCopyLogObj.1523
+ _nrCopyLogObj.1697
+ _nrCopyLogObj.1862
+ _nrCopyLogObj.1961
+ _nrCopyLogObj.2174
+ _nrCopyLogObj.22
+ _nrCopyLogObj.237
+ _nrCopyLogObj.2752
+ _nrCopyLogObj.2909
+ _nrCopyLogObj.336
+ _nrCopyLogObj.408
+ _nrCopyLogObj.461
+ _nrCopyLogObj.560
+ _nrCopyLogObj.672
+ _nrCopyLogObj.68
+ _nrCopyLogObj.823
+ _nrCopyLogObj.onceToken.1053
+ _nrCopyLogObj.onceToken.1127
+ _nrCopyLogObj.onceToken.113
+ _nrCopyLogObj.onceToken.1219
+ _nrCopyLogObj.onceToken.1528
+ _nrCopyLogObj.onceToken.1708
+ _nrCopyLogObj.onceToken.1866
+ _nrCopyLogObj.onceToken.1948
+ _nrCopyLogObj.onceToken.1969
+ _nrCopyLogObj.onceToken.227
+ _nrCopyLogObj.onceToken.2757
+ _nrCopyLogObj.onceToken.2913
+ _nrCopyLogObj.onceToken.345
+ _nrCopyLogObj.onceToken.400
+ _nrCopyLogObj.onceToken.466
+ _nrCopyLogObj.onceToken.563
+ _nrCopyLogObj.onceToken.675
+ _nrCopyLogObj.onceToken.75
+ _nrCopyLogObj.onceToken.809
+ _nrCopyLogObj.onceToken.971
+ _nrCopyLogObj.sNRLogObj.1055
+ _nrCopyLogObj.sNRLogObj.1129
+ _nrCopyLogObj.sNRLogObj.115
+ _nrCopyLogObj.sNRLogObj.1220
+ _nrCopyLogObj.sNRLogObj.1530
+ _nrCopyLogObj.sNRLogObj.1710
+ _nrCopyLogObj.sNRLogObj.1867
+ _nrCopyLogObj.sNRLogObj.1950
+ _nrCopyLogObj.sNRLogObj.1971
+ _nrCopyLogObj.sNRLogObj.229
+ _nrCopyLogObj.sNRLogObj.2758
+ _nrCopyLogObj.sNRLogObj.2914
+ _nrCopyLogObj.sNRLogObj.347
+ _nrCopyLogObj.sNRLogObj.401
+ _nrCopyLogObj.sNRLogObj.468
+ _nrCopyLogObj.sNRLogObj.564
+ _nrCopyLogObj.sNRLogObj.677
+ _nrCopyLogObj.sNRLogObj.76
+ _nrCopyLogObj.sNRLogObj.811
+ _nrCopyLogObj.sNRLogObj.973
+ _nrXPCCompanionSetCompanionAPLForTesting
+ _nrXPCCompanionSetSimulateSlicingEnabled
+ _nrXPCCopyResolvedEndpointWithMetadata
+ _nrXPCKeyDeviceInfo
+ _nrXPCKeySimulateSlicingEnabled
+ _nrXPCKeyTestCompanionAPL
+ _nrXPCKeyUseASQUIC
+ _nr_absolute_time
+ _nr_continuous_time
+ _nr_get_mach_timebase.info
+ _nr_get_mach_timebase.once
+ _nw_endpoint_create_application_service
+ _nw_endpoint_set_device_id
+ _nw_parameters_create_application_service_quic_using_identity
+ _nw_parameters_set_account_id
+ _nw_parameters_set_local_only
+ _nw_parameters_set_multipath_service
+ _nw_parameters_set_prohibit_joining_protocols
+ _nw_parameters_set_prohibited_netagent_classes
+ _nw_protocol_options_is_quic
+ _nw_protocol_stack_iterate_application_protocols
+ _nw_quic_connection_set_keepalive_count
+ _nw_quic_set_idle_timeout
+ _objc_msgSend$connectedInterfaceName
+ _objc_msgSend$connectedLinkSubtype
+ _objc_msgSend$connectedLinkType
+ _objc_msgSend$copyEndpoint
+ _objc_msgSend$deviceInfo
+ _objc_msgSend$deviceInfoDidChange:deviceInfo:
+ _objc_msgSend$endpointWithCEndpoint:
+ _objc_msgSend$httpConnectPSK
+ _objc_msgSend$httpConnectPSKIdentity
+ _objc_msgSend$httpConnectPassword
+ _objc_msgSend$httpConnectURLs
+ _objc_msgSend$httpConnectUserName
+ _objc_msgSend$localEndpoint
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$proxyInfo
+ _objc_msgSend$proxyProviderAuthMode
+ _objc_msgSend$proxyProviderType
+ _objc_msgSend$remoteEndpoint
+ _objc_msgSend$service
+ _objc_msgSend$serviceUUID
+ _objc_msgSend$setAllowsApplicationServiceConnections:
+ _objc_msgSend$setConnectedInterfaceName:
+ _objc_msgSend$setConnectedLinkSubtype:
+ _objc_msgSend$setConnectedLinkType:
+ _objc_msgSend$setHttpConnectPSK:
+ _objc_msgSend$setHttpConnectPSKIdentity:
+ _objc_msgSend$setHttpConnectPassword:
+ _objc_msgSend$setHttpConnectURLs:
+ _objc_msgSend$setHttpConnectUserName:
+ _objc_msgSend$setLocalEndpoint:
+ _objc_msgSend$setProxyInfo:
+ _objc_msgSend$setProxyProviderAuthMode:
+ _objc_msgSend$setProxyProviderType:
+ _objc_msgSend$setRemoteEndpoint:
+ _objc_msgSend$setServiceUUID:
+ _objc_msgSend$usesASQUIC
+ _sec_identity_create
+ _uuid_generate
- -[NREndpoint setDataProtectionClass:]
- -[NREndpoint setDeviceIdentifier:]
- -[NREndpoint setPortString:]
- GCC_except_table113
- GCC_except_table116
- GCC_except_table125
- GCC_except_table127
- GCC_except_table21
- GCC_except_table261
- GCC_except_table316
- GCC_except_table341
- GCC_except_table376
- GCC_except_table387
- GCC_except_table592
- GCC_except_table597
- GCC_except_table604
- GCC_except_table611
- GCC_except_table615
- GCC_except_table619
- GCC_except_table623
- GCC_except_table64
- GCC_except_table645
- GCC_except_table648
- GCC_except_table659
- GCC_except_table661
- GCC_except_table666
- GCC_except_table75
- ___Block_byref_object_copy_.1710
- ___Block_byref_object_copy_.2375
- ___Block_byref_object_copy_.964
- ___Block_byref_object_dispose_.1711
- ___Block_byref_object_dispose_.2376
- ___Block_byref_object_dispose_.965
- ___block_descriptor_53_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.1046
- ___block_literal_global.115
- ___block_literal_global.1305
- ___block_literal_global.1487
- ___block_literal_global.1689
- ___block_literal_global.1723
- ___block_literal_global.1744
- ___block_literal_global.220
- ___block_literal_global.2354
- ___block_literal_global.2514
- ___block_literal_global.26
- ___block_literal_global.335
- ___block_literal_global.398
- ___block_literal_global.424
- ___block_literal_global.439
- ___block_literal_global.455
- ___block_literal_global.455.1036
- ___block_literal_global.489
- ___block_literal_global.493
- ___block_literal_global.626
- ___block_literal_global.640
- ___block_literal_global.69
- ___block_literal_global.778
- ___block_literal_global.85
- ___block_literal_global.875
- ___block_literal_global.949
- ___nrCopyLogObj_block_invoke.1039
- ___nrCopyLogObj_block_invoke.1309
- ___nrCopyLogObj_block_invoke.1492
- ___nrCopyLogObj_block_invoke.1648
- ___nrCopyLogObj_block_invoke.172
- ___nrCopyLogObj_block_invoke.1732
- ___nrCopyLogObj_block_invoke.1755
- ___nrCopyLogObj_block_invoke.228
- ___nrCopyLogObj_block_invoke.2365
- ___nrCopyLogObj_block_invoke.2518
- ___nrCopyLogObj_block_invoke.339
- ___nrCopyLogObj_block_invoke.392
- ___nrCopyLogObj_block_invoke.459
- ___nrCopyLogObj_block_invoke.537
- ___nrCopyLogObj_block_invoke.644
- ___nrCopyLogObj_block_invoke.787
- ___nrCopyLogObj_block_invoke.79
- ___nrCopyLogObj_block_invoke.882
- ___nrCopyLogObj_block_invoke.957
- _nrCopyLogObj.1031
- _nrCopyLogObj.120
- _nrCopyLogObj.1299
- _nrCopyLogObj.1475
- _nrCopyLogObj.1639
- _nrCopyLogObj.1735
- _nrCopyLogObj.19
- _nrCopyLogObj.1935
- _nrCopyLogObj.229
- _nrCopyLogObj.2356
- _nrCopyLogObj.2509
- _nrCopyLogObj.325
- _nrCopyLogObj.397
- _nrCopyLogObj.449
- _nrCopyLogObj.531
- _nrCopyLogObj.636
- _nrCopyLogObj.69
- _nrCopyLogObj.792
- _nrCopyLogObj.895
- _nrCopyLogObj.onceToken.1035
- _nrCopyLogObj.onceToken.114
- _nrCopyLogObj.onceToken.1304
- _nrCopyLogObj.onceToken.1486
- _nrCopyLogObj.onceToken.1643
- _nrCopyLogObj.onceToken.1722
- _nrCopyLogObj.onceToken.1743
- _nrCopyLogObj.onceToken.219
- _nrCopyLogObj.onceToken.2362
- _nrCopyLogObj.onceToken.2513
- _nrCopyLogObj.onceToken.334
- _nrCopyLogObj.onceToken.389
- _nrCopyLogObj.onceToken.454
- _nrCopyLogObj.onceToken.534
- _nrCopyLogObj.onceToken.639
- _nrCopyLogObj.onceToken.76
- _nrCopyLogObj.onceToken.777
- _nrCopyLogObj.onceToken.874
- _nrCopyLogObj.onceToken.948
- _nrCopyLogObj.sNRLogObj.1037
- _nrCopyLogObj.sNRLogObj.116
- _nrCopyLogObj.sNRLogObj.1306
- _nrCopyLogObj.sNRLogObj.1488
- _nrCopyLogObj.sNRLogObj.1644
- _nrCopyLogObj.sNRLogObj.1724
- _nrCopyLogObj.sNRLogObj.1745
- _nrCopyLogObj.sNRLogObj.221
- _nrCopyLogObj.sNRLogObj.2363
- _nrCopyLogObj.sNRLogObj.2515
- _nrCopyLogObj.sNRLogObj.336
- _nrCopyLogObj.sNRLogObj.390
- _nrCopyLogObj.sNRLogObj.456
- _nrCopyLogObj.sNRLogObj.535
- _nrCopyLogObj.sNRLogObj.641
- _nrCopyLogObj.sNRLogObj.77
- _nrCopyLogObj.sNRLogObj.779
- _nrCopyLogObj.sNRLogObj.876
- _nrCopyLogObj.sNRLogObj.950
- _nrXPCCopyResolvedEndpoint
- _objc_msgSend$copyNWEndpoint
- _objc_msgSend$setDataProtectionClass:
- _objc_msgSend$setDeviceIdentifier:
- _objc_msgSend$setPortString:
CStrings:
+ " (Epml)"
+ " service %@"
+ "#"
+ "%@, "
+ "%s called with null deviceIdentifier"
+ "%s called with null privateKey"
+ "%s called with null publicKey"
+ "%s%.30s:%-4d %@: Dealloc"
+ "%s%.30s:%-4d %@: Registering pairing manager failed: %@"
+ "%s%.30s:%-4d %@: Requesting auth method %zu for %@ failed: %@"
+ "%s%.30s:%-4d %@: Requesting auth method %zu for %@ succeeded"
+ "%s%.30s:%-4d %@: Starting pairing discovery failed: %@"
+ "%s%.30s:%-4d %@: Starting pairing failed: %@"
+ "%s%.30s:%-4d %@: State change: %@ -> %@"
+ "%s%.30s:%-4d %@: State changed while registering pairing manager"
+ "%s%.30s:%-4d %@: State changed while starting pairing"
+ "%s%.30s:%-4d %@: State changed while starting pairing discovery"
+ "%s%.30s:%-4d %@: State changed while stopping pairing"
+ "%s%.30s:%-4d %@: State changed while stopping pairing discovery"
+ "%s%.30s:%-4d %@: Stopping pairing discovery failed: %@"
+ "%s%.30s:%-4d %@: Stopping pairing failed: %@"
+ "%s%.30s:%-4d %@: Unregistering pairing manager failed: %@"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties must either have wasInitiallySetupUsingIDSPairing or outOfBandKey or isExternalPairing"
+ "%s%.30s:%-4d Got NRUUID %@ from daemon for bluetoothUUID %@%s"
+ "%s%.30s:%-4d Informing client that %@ has deviceInfo %@"
+ "%s%.30s:%-4d Received %supdate %sregistered %sabled %snearby %sconnected %scloudConnected %sclassCConnected %shasUnpairedBluetooth %s %@(%@) prx %@ thermal %@ %spluggedIn deviceInfo(%@) for %@"
+ "%s%.30s:%-4d SecGenerateSelfSignedCertificate() failed"
+ "%s%.30s:%-4d SecIdentityCreate() failed"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties must either have wasInitiallySetupUsingIDSPairing or outOfBandKey or isExternalPairing"
+ ", fl %#llx"
+ ", prx-type:%@ prx-auth:%@"
+ "-[NRDeviceInfo initWithCoder:]"
+ "-[NRDeviceProxyInfo initWithCoder:]"
+ "-[NREndpoint initInternalWithDeviceIdentifier:portString:dataProtectionClass:service:]"
+ "-[NRParametersServiceConnection initWithDeviceIdentifier:dataProtectionClass:options:]"
+ "."
+ "@\"NRDeviceInfo\""
+ "@\"NRDeviceProxyInfo\""
+ "@36@0:8@16C24@28"
+ "@44@0:8@16@24C32@36"
+ "AddrData"
+ "AllowsQR"
+ "Default"
+ "DeviceInfo"
+ "HTTPConnect"
+ "IKE_FOLLOWUP_KE"
+ "IKE_INTERMEDIATE"
+ "ImportedPSK"
+ "MASQUE"
+ "NRCreateLocalIdentity"
+ "NRDeviceInfo"
+ "NRDeviceInfo["
+ "NRDeviceProxyInfo"
+ "NRDeviceProxyInfo["
+ "NREndpointCopyDictionary"
+ "NRParametersServiceConnection"
+ "RapportNetworkAgent"
+ "RawPSK"
+ "SHOES"
+ "SetCompanionAPLForTesting"
+ "SimulateSlicingEnabled"
+ "T@\"NRDeviceIdentifier\",&,N,V_nrDeviceIdentifier"
+ "T@\"NRDeviceInfo\",R,N"
+ "T@\"NRDeviceProxyInfo\",&,N,V_proxyInfo"
+ "T@\"NSArray\",&,N,V_httpConnectURLs"
+ "T@\"NSData\",&,N,V_httpConnectPSK"
+ "T@\"NSData\",&,N,V_httpConnectPSKIdentity"
+ "T@\"NSString\",&,N,V_connectedInterfaceName"
+ "T@\"NSString\",&,N,V_httpConnectPassword"
+ "T@\"NSString\",&,N,V_httpConnectUserName"
+ "T@\"NSUUID\",&,N,V_serviceUUID"
+ "T@\"NWAddressEndpoint\",&,N,V_localEndpoint"
+ "T@\"NWAddressEndpoint\",&,N,V_remoteEndpoint"
+ "TC,N,V_connectedLinkSubtype"
+ "TC,N,V_connectedLinkType"
+ "TQ,N,V_proxyProviderAuthMode"
+ "TQ,N,V_proxyProviderType"
+ "TestCompanionAPL"
+ "Unknown(%llu)"
+ "UseASQUIC"
+ "_connectedInterfaceName"
+ "_connectedLinkSubtype"
+ "_connectedLinkType"
+ "_httpConnectPSK"
+ "_httpConnectPSKIdentity"
+ "_httpConnectPassword"
+ "_httpConnectURLs"
+ "_httpConnectUserName"
+ "_internalDeviceInfo"
+ "_internalEphemeralBluetoothUUID"
+ "_proxyInfo"
+ "_proxyProviderAuthMode"
+ "_proxyProviderType"
+ "_service"
+ "_serviceUUID"
+ "_usesASQUIC"
+ "allowsApplicationServiceConnections"
+ "c"
+ "com.apple.networkrelay.encoded"
+ "com.apple.rapport"
+ "connectedInterfaceName"
+ "connectedLinkSubtype"
+ "connectedLinkType"
+ "deviceID"
+ "deviceInfo"
+ "deviceInfoDidChange:deviceInfo:"
+ "endpointWithCEndpoint:"
+ "httpConnectPSK"
+ "httpConnectPSKIdentity"
+ "httpConnectPassword"
+ "httpConnectURLs"
+ "httpConnectUserName"
+ "identity:%@, "
+ "initWithDeviceIdentifier:dataProtectionClass:options:"
+ "initWithDeviceIdentifier:portString:dataProtectionClass:service:"
+ "ip-header-offset"
+ "l"
+ "link: %@ (%@)"
+ "local: %@, "
+ "localEndpoint"
+ "lrbIOVecLen=0 tlvLen=%u filledInLinkReadBufferBytes=%u handledLinkReadBufferBytes=%u"
+ "nrXPCCompanionSetCompanionAPLForTesting"
+ "nrXPCCompanionSetSimulateSlicingEnabled"
+ "nrXPCCopyResolvedEndpointWithMetadata"
+ "numberWithInt:"
+ "outOfBandKey was nil and !wasInitiallySetupUsingIDSPairing and !isExternalPairing"
+ "password: %@ "
+ "proxyInfo"
+ "proxyProviderAuthMode"
+ "proxyProviderType"
+ "psk: %@, "
+ "r"
+ "remote: %@, "
+ "remoteEndpoint"
+ "service"
+ "serviceUUID"
+ "setAllowsApplicationServiceConnections:"
+ "setConnectedInterfaceName:"
+ "setConnectedLinkSubtype:"
+ "setConnectedLinkType:"
+ "setHttpConnectPSK:"
+ "setHttpConnectPSKIdentity:"
+ "setHttpConnectPassword:"
+ "setHttpConnectURLs:"
+ "setHttpConnectUserName:"
+ "setLocalEndpoint:"
+ "setProxyInfo:"
+ "setProxyProviderAuthMode:"
+ "setProxyProviderType:"
+ "setRemoteEndpoint:"
+ "setServiceUUID:"
+ "type:%@, "
+ "urls:%@, "
+ "username:%@, "
+ "usesASQUIC"
+ "v16@?0@\"NSObject<OS_nw_protocol_options>\"8"
- "\""
- "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties must either have wasInitiallySetupUsingIDSPairing or outOfBandKey"
- "%s%.30s:%-4d Got NRUUID %@ from daemon for bluetoothUUID %@"
- "%s%.30s:%-4d Manager state change: %@ -> %@"
- "%s%.30s:%-4d Received %supdate %sregistered %sabled %snearby %sconnected %scloudConnected %sclassCConnected %shasUnpairedBluetooth %s %@(%@) prx %@ thermal %@ %spluggedIn for %@"
- "%s%.30s:%-4d Registering pairing manager failed: %@"
- "%s%.30s:%-4d Requesting auth method %zu for %@ failed: %@"
- "%s%.30s:%-4d Requesting auth method %zu for %@ succeeded"
- "%s%.30s:%-4d Starting pairing discovery failed: %@"
- "%s%.30s:%-4d Starting pairing failed: %@"
- "%s%.30s:%-4d State changed while registering pairing manager"
- "%s%.30s:%-4d State changed while starting pairing"
- "%s%.30s:%-4d State changed while starting pairing discovery"
- "%s%.30s:%-4d State changed while stopping pairing"
- "%s%.30s:%-4d State changed while stopping pairing discovery"
- "%s%.30s:%-4d Stopping pairing discovery failed: %@"
- "%s%.30s:%-4d Stopping pairing failed: %@"
- "%s%.30s:%-4d Unregistering pairing manager failed: %@"
- "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties must either have wasInitiallySetupUsingIDSPairing or outOfBandKey"
- "+[NRDeviceIdentifier(Internal) copyBestTestingDeviceIdentifier]"
- "-[NREndpoint initWithDeviceIdentifier:portString:dataProtectionClass:]"
- "NREndpointResolveData"
- "T@\"NSString\",&,N,V_portString"
- "TC,N,V_dataProtectionClass"
- "a"
- "nrXPCCopyResolvedEndpoint"
- "outOfBandKey was nil and !wasInitiallySetupUsingIDSPairing"
- "setDataProtectionClass:"
- "setPortString:"

```
