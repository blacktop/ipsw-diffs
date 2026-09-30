## Netrb

> `/System/Library/PrivateFrameworks/Netrb.framework/Netrb`

```diff

-315.100.4.0.0
-  __TEXT.__text: 0x709c
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x19f3
+346.0.0.0.2
+  __TEXT.__text: 0x8af0
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__const: 0x73
+  __TEXT.__cstring: 0x200c
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x8a0
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0xe0
-  __DATA.__data: 0x2f8
-  __DATA.__bss: 0x10
+  __TEXT.__unwind_info: 0x1d0
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0xa48
+  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__const: 0x280
+  __DATA.__data: 0x378
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 95838E6A-9B69-3B2E-8501-AA370EA967FF
-  Functions: 106
-  Symbols:   462
-  CStrings:  242
+  UUID: 718305A1-4515-3A85-98DB-6DCE8506BDB9
+  Functions: 150
+  Symbols:   603
+  CStrings:  294
 
Symbols:
+ __NETRBCreateNetwork
+ __NETRBCreateNetwork.cold.1
+ __NETRBCreateNetworkConfiguration
+ __NETRBCreateNetworkConfiguration.cold.1
+ __NETRBDeserializeNetwork
+ __NETRBDeserializeNetwork.cold.1
+ __NETRBDeserializeNetworkConfig
+ __NETRBInterfaceGetMacAddr
+ __NETRBInterfaceGetMtu
+ __NETRBInterfaceGetSocketFd
+ __NETRBInterfaceGetTypeId.pred
+ __NETRBInterfaceGetUUID
+ __NETRBInterfaceTypeId
+ __NETRBNetworkAddDHCPReservation
+ __NETRBNetworkAddPortForwardingRule
+ __NETRBNetworkClient
+ __NETRBNetworkClientRefCnt
+ __NETRBNetworkCopy
+ __NETRBNetworkCopy.cold.1
+ __NETRBNetworkDisableDHCP
+ __NETRBNetworkDisableDNSProxy
+ __NETRBNetworkDisableNAT44
+ __NETRBNetworkDisableNAT66
+ __NETRBNetworkDisableRouterAdvertisement
+ __NETRBNetworkGetConfigHandle
+ __NETRBNetworkGetIPv4Subnet
+ __NETRBNetworkGetIPv6Prefix
+ __NETRBNetworkGetTypeId.pred
+ __NETRBNetworkSetExternalInterface
+ __NETRBNetworkSetFlags
+ __NETRBNetworkSetIPv4Addresses
+ __NETRBNetworkSetIPv6Prefix
+ __NETRBNetworkSetMtu
+ __NETRBNetworkStartVirtualMachineInterface
+ __NETRBNetworkStartVirtualMachineInterface.cold.1
+ __NETRBNetworkStartVirtualMachineInterface.cold.2
+ __NETRBNetworkTypeId
+ __NETRBSerializeNetwork
+ ___NETRBInterfaceRelease
+ ___NETRBInterfaceRelease.cold.1
+ ___NETRBNetworkCreateGlobalClient
+ ___NETRBNetworkCreateGlobalClient.cold.1
+ ___NETRBNetworkGetServiceQueue.__networkServiceQueue
+ ___NETRBNetworkGetServiceQueue.__networkServiceQueueName
+ ___NETRBNetworkGetServiceQueue.predNetworkQueue
+ ___NETRBNetworkRelease
+ ____NETRBCreateNetwork_block_invoke
+ ____NETRBCreateNetwork_block_invoke_2
+ ____NETRBInterfaceGetTypeId_block_invoke
+ ____NETRBNetworkGetTypeId_block_invoke
+ ____NETRBNetworkStartVirtualMachineInterface_block_invoke
+ ____NETRBNetworkStartVirtualMachineInterface_block_invoke_2
+ _____NETRBInterfaceRelease_block_invoke
+ _____NETRBNetworkCreateGlobalClient_block_invoke
+ _____NETRBNetworkCreateGlobalClient_block_invoke.cold.1
+ _____NETRBNetworkCreateGlobalClient_block_invoke_2
+ _____NETRBNetworkGetServiceQueue_block_invoke
+ _____NETRBNetworkReleaseGlobalClient_block_invoke
+ _____NETRBNetworkReleaseGlobalClient_block_invoke.cold.1
+ _____NETRBNetworkRelease_block_invoke
+ ___assert_rtn
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.145
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.149
+ ___block_descriptor_tmp.160
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.191
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.195
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.207
+ ___block_descriptor_tmp.225
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.255
+ ___block_descriptor_tmp.256
+ ___block_descriptor_tmp.261
+ ___block_descriptor_tmp.265
+ ___block_descriptor_tmp.269
+ ___block_descriptor_tmp.270
+ ___block_descriptor_tmp.273
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.281
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.71
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.88
+ ___block_descriptor_tmp.89
+ ___block_descriptor_tmp.92
+ ___block_descriptor_tmp.95
+ ___block_literal_global.205
+ ___block_literal_global.209
+ ___block_literal_global.258
+ ___block_literal_global.263
+ ___block_literal_global.267
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.280
+ ___block_literal_global.283
+ ___memcpy_chk
+ ___netrb_interface_class
+ ___netrb_network_class
+ ___strlcpy_chk
+ _in6addr_any
+ _malloc_type_malloc
+ _netrbClientRelayAuditToken
+ _netrbNetworkDHCPReservationIPAddr
+ _netrbNetworkDHCPReservationMacAddr
+ _netrbNetworkPortForwardingAddressFamily
+ _netrbNetworkPortForwardingExternalPort
+ _netrbNetworkPortForwardingInternalAddress
+ _netrbNetworkPortForwardingInternalPort
+ _netrbNetworkPortForwardingProtocol
+ _netrbXPCInterfaceId
+ _netrbXPCNetworkAuthorizationToken
+ _netrbXPCNetworkObject
+ _netrbXPCNetworkSerialization
+ _netrbXPCNetworkSerializationDHCPReservation
+ _netrbXPCNetworkSerializationPortForwarding
+ _netrbXPCRaPrefixLen
+ _netrbXPCRelayAuditToken
+ _uuid_compare
+ _uuid_copy
+ _xpc_dictionary_get_data
+ _xpc_dictionary_set_data
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.108
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.152
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.157
- ___block_descriptor_tmp.158
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.162
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.169
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.223
- ___block_descriptor_tmp.52
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.84
- ___block_descriptor_tmp.87
- ___block_descriptor_tmp.94
- ___block_descriptor_tmp.98
- ___block_descriptor_tmp.99
- ___block_literal_global.176
- ___block_literal_global.180
- _insert_interface_address_params
CStrings:
+ "%s SPI doesn't support bridged mode"
+ "%s: _CFRuntimeCreateInstance"
+ "%s: _NETRBClientCreate"
+ "%s: _NETRBClientNewInterface"
+ "%s: __NETRBNetworkCreateGlobalClient"
+ "%s: adding virtual interface to network %p"
+ "%s: failed"
+ "%s: interface creation failed"
+ "%s: invalid address family %u"
+ "%s: invalid network global client"
+ "%s: invalid operation mode"
+ "%s: invalid serialized network"
+ "%s: network handle mismatch"
+ "%s: network handle not returned"
+ "%s: no associated network"
+ "%s: no response from daemon"
+ "%s: unable to create framework queue"
+ "NETRB.c"
+ "NETRB_CLIENT"
+ "NETRB_INTERFACE"
+ "NETRB_NETWORK"
+ "_NETRBCreateNetwork"
+ "_NETRBCreateNetworkConfiguration"
+ "_NETRBCreateNetwork_block_invoke"
+ "_NETRBCreateNetwork_block_invoke_2"
+ "_NETRBDeserializeNetwork"
+ "_NETRBDeserializeNetworkConfig"
+ "_NETRBNetworkAddPortForwardingRule"
+ "_NETRBNetworkClientRefCnt > 0"
+ "_NETRBNetworkStartVirtualMachineInterface"
+ "_NETRBNetworkStartVirtualMachineInterface_block_invoke"
+ "_NETRBNetworkStartVirtualMachineInterface_block_invoke_2"
+ "__NETRBInterfaceRelease"
+ "__NETRBNetworkCreateGlobalClient_block_invoke"
+ "__NETRBNetworkRelease"
+ "__NETRBNetworkReleaseGlobalClient_block_invoke"
+ "building xpc request"
+ "i20@?0i8^v12"
+ "interfaceId"
+ "networkAuthorizationToken"
+ "networkObject"
+ "networkSerialization"
+ "networkSerializationDHCPReservation"
+ "networkSerializationPortForwarding"
+ "network_dhcp_reservation_ip_addr"
+ "network_dhcp_reservation_mac_addr"
+ "network_port_forwarding_address_family"
+ "network_port_forwarding_external_port"
+ "network_port_forwarding_internal_address"
+ "network_port_forwarding_internal_port"
+ "network_port_forwarding_protocol"
+ "relay audit token"
+ "relay_audit_token"
- "NETRB"

```
