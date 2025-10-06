## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2205.40.9.0.0
-  __TEXT.__text: 0xb26dc
+2205.40.18.0.0
+  __TEXT.__text: 0xb3a58
   __TEXT.__auth_stubs: 0x1d40
   __TEXT.__objc_stubs: 0x7fe0
-  __TEXT.__objc_methlist: 0x3d94
+  __TEXT.__objc_methlist: 0x3dbc
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x2368
-  __TEXT.__objc_methname: 0x9168
-  __TEXT.__oslogstring: 0xf3c8
-  __TEXT.__cstring: 0x535e
-  __TEXT.__objc_classname: 0xbac
-  __TEXT.__objc_methtype: 0x210d
+  __TEXT.__gcc_except_tab: 0x23b8
+  __TEXT.__objc_methname: 0x9199
+  __TEXT.__oslogstring: 0xfa16
+  __TEXT.__cstring: 0x54b5
+  __TEXT.__objc_classname: 0xbbc
+  __TEXT.__objc_methtype: 0x2148
   __TEXT.__unwind_info: 0x1660
   __DATA_CONST.__auth_got: 0xeb0
   __DATA_CONST.__got: 0x770
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1d80
   __DATA_CONST.__cfstring: 0x2660
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x8060
+  __DATA.__objc_const: 0x8158
   __DATA.__objc_selrefs: 0x23a0
-  __DATA.__objc_ivar: 0x788
-  __DATA.__objc_data: 0x1860
+  __DATA.__objc_ivar: 0x794
+  __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xf80
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5979C00-6564-314D-8D72-FC2867819D5F
-  Functions: 1883
+  UUID: 9569AE80-D3A9-34FD-BE41-54CB04D244BF
+  Functions: 1888
   Symbols:   691
-  CStrings:  4321
+  CStrings:  4345
 
CStrings:
+ "%s: Added DeviceCommunication DIRECTLINK policy: %@"
+ "%s: Added DeviceCommunication account id policy: %@"
+ "%s: Added local networks policy: %@"
+ "%s: AoVPN addCellularServicesExceptionDataWithOrder succeeded for PrivilegedTunnel priority"
+ "%s: AoVPN addDeviceCommunicationExceptionWithOrder succeeded for PrivilegedTunnel priority"
+ "%s: AoVPN addPolicyICMPv6WithOrder succeeded for PrivilegedTunnel priority"
+ "%s: AoVPN addVoiceMailExceptionWithOrder succeeded for PrivilegedTunnel priority"
+ "%s: AoVPN setApplicationExceptionTunnelDataPolicies succeeded for PrivilegedTunnel priority"
+ "%s: Failed to add Application exceptions for data"
+ "%s: Failed to add Device Communication exceptions for data"
+ "%s: Failed to add VoiceMail exception for data"
+ "%s: Failed to add icmpv6 exception for data"
+ "%s: Failed to add policy for DeviceCommunication DIRECTLINK: %@"
+ "%s: Failed to add policy for DeviceCommunication account id: %@"
+ "%s: Failed to add policy for local networks: %@"
+ "%s: Policy IDs added %@: %@"
+ "%s: URLCHECK: FINAL RESULT: BATCH ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: BATCH ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: BATCH BLOCKED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: BATCH BLOCKED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: VPN addCellularServicesExceptionDataWithOrder succeeded for PrivilegedTunnel priority"
+ "%s: VPN addDeviceCommunicationExceptionWithOrder failed for PrivilegedTunnel priority"
+ "%s: VPN addDeviceCommunicationExceptionWithOrder succeeded for PrivilegedTunnel priority"
+ "%s: VPN addPolicyICMPv6WithOrder succeeded for PrivilegedTunnel priority"
+ "%s: VPN addVoiceMailExceptionWithOrder succeeded for PrivilegedTunnel priority"
+ "%s: tunnel data Policy IDs added %@: %@"
+ "-[NEPolicySession(AlwaysOnVPN) addDeviceCommunicationExceptionWithOrder:skipOrder:priority:policyIDList:]"
+ "-[NEPolicySession(AlwaysOnVPN) addListenerWithOrder:result:]"
+ "-[NEPolicySession(AlwaysOnVPN) addServiceExceptionsWithOrder:configuration:IMSUseIPSec:dropAllLevel:isHighPriority:]"
+ "-[NESMPolicySession setAOVPNTunnelDataPoliciesForInterfaceName:delegateInterfaceName:isSecondaryConnection:hasDNS:hasProxy:voiceMailExceptionAction:cellularServicesExceptionAction:deviceCommunicationExceptionAction:applicationExceptions:]_block_invoke"
+ "-[NESMPolicySession setTunnelDataPoliciesForInterfaceName:outgoingInterfaceName:hasDNS:hasProxy:hasExcludeLocalNetworks:hasExcludeCellularServices:hasExcludeDeviceCommunication:]_block_invoke"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSSet\""
+ "Control"
+ "Failed to handle APNS exception"
+ "Failed to handle CellularServices exception for %s priority"
+ "Failed to handle device communication exception for %s priority"
+ "Failed to handle local networks exception for %s priority"
+ "Installing VPN NonRankedInterfaces Exceptions - priority %s"
+ "Installing VPN Service Exceptions <APNS> - priority %s"
+ "Installing VPN Service Exceptions <AirPrint> - priority %s"
+ "Installing VPN Service Exceptions <Application> - priority %s"
+ "Installing VPN Service Exceptions <CellularServices> for %s priority"
+ "Installing VPN Service Exceptions <DeviceCommunication> for %s priority"
+ "Installing VPN Service Exceptions <LocalNetworks> for %s priority"
+ "Installing VPN Service Exceptions <Sharingd> - priority %s"
+ "Installing VPN Service Exceptions <VoiceMail> - priority %s"
+ "Installing VPN icmpv6 Exceptions - policies at High Priority"
+ "NEPIRBatchGroup"
+ "_dispatchGroup"
+ "_pending_urls"
+ "_requestBatchGroups"
+ "v24@0:8@?<v@?BB>16"
- "%s: Adding policy for TCP listeners"
- "%s: VPN addLocalNetworksExceptionWithOrder failed for Control priority"
- "%s: VPN addLocalNetworksExceptionWithOrder failed for HighRestricted priority"
- "-[NEPolicySession(AlwaysOnVPN) addDeviceCommunicationExceptionWithOrder:]"
- "-[NEPolicySession(AlwaysOnVPN) addServiceExceptionsWithOrder:configuration:IMSUseIPSec:dropAllLevel:]"
- "-[NESMPolicySession setTunnelDataPoliciesForInterfaceName:outgoingInterfaceName:hasDNS:hasProxy:hasExcludeLocalNetworks:hasExcludeCellularServices:]_block_invoke"
- "APNS "
- "Added DeviceCommunication DIRECTLINK policy: %@"
- "Added DeviceCommunication account id policy: %@"
- "Added local networks policy: %@"
- "AirPrint "
- "CellularServices "
- "Failed to add Application exceptions for data"
- "Failed to add CellularServices exception for data"
- "Failed to add VoiceMail exception for data"
- "Failed to add application exceptions- policies at High Priority"
- "Failed to add policy for DeviceCommunication DIRECTLINK: %@"
- "Failed to add policy for DeviceCommunication account id: %@"
- "Failed to add policy for local networks: %@"
- "Failed to handle CellularServices exception - Control"
- "Failed to handle CellularServices exception - policies at High Priority"
- "Failed to handle apsd exception"
- "Failed to handle device communication exception"
- "Installing VPN Application Exceptions - policies at High Priority %@"
- "Installing VPN Service Exceptions - policies at High Priority <%s%s>"
- "Installing VPN Service Exceptions <%s%s>"
- "Policy IDs added %@: %@"
- "Sharingd "
- "VoiceMail "

```
