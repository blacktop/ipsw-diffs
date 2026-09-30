## SystemConfiguration

> `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`

```diff

-1351.120.3.0.0
-  __TEXT.__text: 0x79ed0
-  __TEXT.__auth_stubs: 0x1f70
+1385.0.0.0.0
+  __TEXT.__text: 0x79f58
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x647d
+  __TEXT.__cstring: 0x64db
   __TEXT.__oslogstring: 0x58b0
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__unwind_info: 0xca0
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x2d08
-  __AUTH_CONST.__auth_got: 0xfb8
+  __DATA_CONST.__const: 0x2d38
+  __AUTH_CONST.__auth_got: 0xfc0
   __AUTH_CONST.__const: 0xbf0
-  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__cfstring: 0x6d20
   __DATA.__data: 0x158
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x210
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x370

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 0A7D6303-6D3F-3D08-8A86-D26A1225D785
-  Functions: 1290
-  Symbols:   3802
-  CStrings:  2900
+  UUID: BCFFF7AF-60DE-3CF2-86D0-2B67071E9AE7
+  Functions: 1286
+  Symbols:   3770
+  CStrings:  2913
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _IOBSDNameMatching
+ _kSCPropNetDNSEncryptedServerALPN
+ _kSCPropNetDNSEncryptedServerAddresses
+ _kSCPropNetDNSEncryptedServerAuthenticationDomainName
+ _kSCPropNetDNSEncryptedServerDoHPath
+ _kSCPropNetDNSEncryptedServerPort
+ _kSCPropNetDNSEncryptedServerServiceParameters
+ _kSCPropNetDNSEncryptedServerServicePriority
+ _kSCPropNetDNSEncryptedServers
+ _writen
- _CFAllocatorAllocate
- __SC_IONetworkInterfaceBSDNameMatching
- ___block_literal_global.64
- _findPerInterfaceConfiguration
- _isA_CFArray
- _isA_CFBoolean
- _isA_CFDictionary
Functions:
~ ___SCGetThreadSpecificData : 176 -> 192
~ __SCCopyDescription : 1804 -> 1836
~ __SC_cfstring_to_cstring_ext : 340 -> 348
~ ___SCPreferencesPath : 960 -> 968
~ __SC_string_to_sockaddr : 408 -> 420
~ _SCPreferencesLock : 2016 -> 2024
~ __SCSerializeMultiple : 540 -> 580
~ _SCNetworkSetCopyServices : 1404 -> 1420
~ __SCNetworkInterfaceCreateWithEntity : 4360 -> 4436
- __SC_IONetworkInterfaceBSDNameMatching
~ _SCNetworkSetCopyAll : 772 -> 796
~ __SCUnserializeMultiple : 536 -> 564
~ __SCCreatePropertyListFromResource : 720 -> 728
~ __SCDPluginSpawnCommand : 600 -> 616
~ __SCDPluginExecCommand2 : 956 -> 972
~ _SCPreferencesCopyKeyList : 332 -> 348
~ _SCPreferencesCommitChanges : 4076 -> 4012
+ _writen
~ ___SCNetworkConnectionCreatePrivate : 1272 -> 1292
- _isA_CFDictionary
- _isA_CFBoolean
~ _SCNetworkConnectionCanTunnelAddress : 728 -> 788
~ _SCNetworkConnectionSelectServiceWithOptions : 1692 -> 1740
~ ___copyMediaList : 876 -> 908
~ _SCNetworkInterfaceCopyMTU : 1484 -> 1492
~ _logConfiguration_NetworkInterfaces : 1084 -> 1076
~ ___SCNetworkInterfaceSupportsVLAN : 732 -> 740
~ __SCNetworkInterfaceCreateWithBSDName : 1132 -> 1156
~ _processSerialInterface : 1532 -> 1528
~ _SCNetworkInterfaceGetHardwareAddressString : 348 -> 356
~ _SCNetworkInterfaceSetPassword : 2532 -> 2548
~ _extendedConfigurationTypes : 492 -> 548
~ _get_number_value : 320 -> 384
~ _set_number_value : 432 -> 488
~ ___SCNetworkInterfaceCreateWithStorageEntity : 3260 -> 3228
- _findPerInterfaceConfiguration
~ _SCNetworkServiceCopyAll : 1304 -> 1328
~ _SCNetworkServiceCopyProtocols : 692 -> 716
~ _SCNetworkServiceSetName : 1480 -> 1484
~ __SCNetworkConfigurationMakePathIfNeeded : 824 -> 828
~ __SCNetworkConfigurationCheckValidityWithPreferences : 5992 -> 5892
- _isA_CFArray
~ __SCNetworkMigrationAreConfigurationsIdentical : 4076 -> 4100
~ _logMapping_one : 1100 -> 1112
~ __SCNetworkMigrationCreateServiceMappingUsingBSDNameMapping : 3236 -> 3256
~ _SCNetworkSignatureCopyActiveIdentifierForAddress : 620 -> 668
~ _validate_app_rule : 1048 -> 1044
CStrings:
+ "ALPN"
+ "AuthenticationDomainName"
+ "DoHPath"
+ "EncryptedServers"
+ "Port"
+ "ServiceParameters"
+ "ServicePriority"

```
