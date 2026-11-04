## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-914.42.1.0.0
-  __TEXT.__text: 0x7b6a4
-  __TEXT.__objc_methlist: 0x1ff4
+914.60.11.0.0
+  __TEXT.__text: 0x7d2ac
+  __TEXT.__objc_methlist: 0x21ac
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0xbbc
-  __TEXT.__cstring: 0x107bc
+  __TEXT.__gcc_except_tab: 0xbb0
+  __TEXT.__cstring: 0x10a91
   __TEXT.__oslogstring: 0x13a9
-  __TEXT.__unwind_info: 0xeb0
+  __TEXT.__unwind_info: 0xee0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xda0
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__const: 0xdc8
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1100
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_selrefs: 0x11e0
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__got: 0x288
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0x5230
+  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__objc_const: 0x55a8
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x7a0
-  __DATA.__objc_ivar: 0x564
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x59c
   __DATA.__data: 0x18
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__data: 0x200
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1074
-  Symbols:   2302
-  CStrings:  2008
+  Functions: 1112
+  Symbols:   2365
+  CStrings:  2030
 
Symbols:
+ +[NRMeshTerminusLinkInfo supportsSecureCoding]
+ -[NRDeviceMeshParticipantInfo activeMeshLinks]
+ -[NRDeviceMeshParticipantInfo buildVersion]
+ -[NRDeviceMeshParticipantInfo productType]
+ -[NRDeviceMeshParticipantInfo respondedWithinTimeout]
+ -[NRDeviceMeshParticipantInfo roomName]
+ -[NRDeviceMeshParticipantInfo setActiveMeshLinks:]
+ -[NRDeviceMeshParticipantInfo setBuildVersion:]
+ -[NRDeviceMeshParticipantInfo setProductType:]
+ -[NRDeviceMeshParticipantInfo setRespondedWithinTimeout:]
+ -[NRDeviceMeshParticipantInfo setRoomName:]
+ -[NRDeviceOperationalProperties setUsesPSKForMASQUE:]
+ -[NRDeviceOperationalProperties usesPSKForMASQUE]
+ -[NRMeshMonitor initiateQueryForDirectLinks]
+ -[NRMeshTerminusLinkInfo .cxx_destruct]
+ -[NRMeshTerminusLinkInfo copyWithZone:]
+ -[NRMeshTerminusLinkInfo description]
+ -[NRMeshTerminusLinkInfo encodeWithCoder:]
+ -[NRMeshTerminusLinkInfo initWithCoder:]
+ -[NRMeshTerminusLinkInfo isLinkWithDistributee]
+ -[NRMeshTerminusLinkInfo isLinkWithPrimaryAssistDevice]
+ -[NRMeshTerminusLinkInfo linkSubtype]
+ -[NRMeshTerminusLinkInfo linkType]
+ -[NRMeshTerminusLinkInfo peerApplicationIdentifier]
+ -[NRMeshTerminusLinkInfo peerDeviceIdentifier]
+ -[NRMeshTerminusLinkInfo peerName]
+ -[NRMeshTerminusLinkInfo setIsLinkWithDistributee:]
+ -[NRMeshTerminusLinkInfo setIsLinkWithPrimaryAssistDevice:]
+ -[NRMeshTerminusLinkInfo setLinkSubtype:]
+ -[NRMeshTerminusLinkInfo setLinkType:]
+ -[NRMeshTerminusLinkInfo setPeerApplicationIdentifier:]
+ -[NRMeshTerminusLinkInfo setPeerDeviceIdentifier:]
+ -[NRMeshTerminusLinkInfo setPeerName:]
+ -[NRMeshTerminusLinkInfo setWifiAwareRSSI:]
+ -[NRMeshTerminusLinkInfo wifiAwareRSSI]
+ GCC_except_table488
+ GCC_except_table499
+ GCC_except_table739
+ GCC_except_table747
+ GCC_except_table756
+ GCC_except_table761
+ GCC_except_table768
+ GCC_except_table774
+ GCC_except_table778
+ GCC_except_table782
+ GCC_except_table786
+ GCC_except_table807
+ GCC_except_table810
+ GCC_except_table814
+ GCC_except_table819
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table825
+ GCC_except_table827
+ GCC_except_table830
+ GCC_except_table832
+ GCC_except_table834
+ GCC_except_table892
+ GCC_except_table894
+ GCC_except_table909
+ _OBJC_CLASS_$_NRMeshTerminusLinkInfo
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._activeMeshLinks
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._buildVersion
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._productType
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._respondedWithinTimeout
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._roomName
+ _OBJC_IVAR_$_NRMeshPreferences._cancelled
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._isLinkWithDistributee
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._isLinkWithPrimaryAssistDevice
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._linkSubtype
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._linkType
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._peerApplicationIdentifier
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._peerDeviceIdentifier
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._peerName
+ _OBJC_IVAR_$_NRMeshTerminusLinkInfo._wifiAwareRSSI
+ _OBJC_METACLASS_$_NRMeshTerminusLinkInfo
+ __OBJC_$_CLASS_METHODS_NRMeshTerminusLinkInfo
+ __OBJC_$_CLASS_PROP_LIST_NRMeshTerminusLinkInfo
+ __OBJC_$_INSTANCE_METHODS_NRMeshTerminusLinkInfo
+ __OBJC_$_INSTANCE_VARIABLES_NRMeshTerminusLinkInfo
+ __OBJC_$_PROP_LIST_NRMeshTerminusLinkInfo
+ __OBJC_CLASS_PROTOCOLS_$_NRMeshTerminusLinkInfo
+ __OBJC_CLASS_RO_$_NRMeshTerminusLinkInfo
+ __OBJC_METACLASS_RO_$_NRMeshTerminusLinkInfo
+ ___44-[NRMeshMonitor initiateQueryForDirectLinks]_block_invoke
+ ___block_descriptor_40_e8_32s_e32_v24?0"NSError"8"NRMeshInfo"16ls32l8
+ ___nrXPCQueryActiveMeshLinks_block_invoke
+ _nrXPCEntitlementMeshMonitor_block_invoke_3.sNRXPCConnection
+ _nrXPCQueryActiveMeshLinks
- GCC_except_table456
- GCC_except_table467
- GCC_except_table705
- GCC_except_table713
- GCC_except_table718
- GCC_except_table722
- GCC_except_table727
- GCC_except_table734
- GCC_except_table740
- GCC_except_table744
- GCC_except_table748
- GCC_except_table773
- GCC_except_table776
- GCC_except_table780
- GCC_except_table785
- GCC_except_table787
- GCC_except_table789
- GCC_except_table791
- GCC_except_table793
- GCC_except_table796
- GCC_except_table798
- GCC_except_table800
- GCC_except_table856
- GCC_except_table858
- GCC_except_table873
- _nrXPCEntitlementMeshMonitor_block_invoke_2.sNRXPCConnection
CStrings:
+ "%s%.30s:%-4d %@ cancelling connection because preferences were cancelled"
+ "%s%.30s:%-4d Mesh delegate does not implement didCompleteQueryForDirectLinks:error:meshMonitor:"
+ "-[NRMeshMonitor initiateQueryForDirectLinks]_block_invoke"
+ "-[NRMeshTerminusLinkInfo initWithCoder:]"
+ "MeshMonitorQueryActiveLinks"
+ "Missing mesh info in XPC response"
+ "NRMeshParticipantInfo[appID=%@ primaryAssistCapable=%@ selectedAsPrimaryAssist=%@ currentRouteThroughPrimaryAssist=%@ responded=%@ product=%@ build=%@ room=%@ activeMeshLinks=%@]"
+ "NRMeshTerminusLinkInfo[peer=%@ name=%@ appID=%@ link=%@(%@) rssi=%@ withPA=%@ withDistributee=%@]"
+ "activeMeshLinks"
+ "buildVersion"
+ "isLinkWithDistributee"
+ "isLinkWithPrimaryAssistDevice"
+ "linkSubtype"
+ "linkType"
+ "nrXPCQueryActiveMeshLinks"
+ "nrXPCQueryActiveMeshLinks_block_invoke"
+ "peerApplicationIdentifier"
+ "peerDeviceIdentifier"
+ "peerName"
+ "productType"
+ "respondedWithinTimeout"
+ "roomName"
+ "v24@?0@\"NSError\"8@\"NRMeshInfo\"16"
+ "wifiAwareRSSI"
- "%s%.30s:%-4d %@ cancelling connection because multicastAddress list is empty"
- "NRMeshParticipantInfo[appID=%@ primaryAssistCapable=%@ selectedAsPrimaryAssist=%@ currentRouteThroughPrimaryAssist=%@]"
```
