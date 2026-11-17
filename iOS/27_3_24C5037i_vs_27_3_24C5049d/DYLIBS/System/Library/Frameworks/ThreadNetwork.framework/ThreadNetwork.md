## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-447.0.1.0.0
+447.0.2.0.0
   __TEXT.__text: 0xe23c
   __TEXT.__objc_methlist: 0xe38
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1762
+  __TEXT.__cstring: 0x176c
   __TEXT.__oslogstring: 0xa7b
   __TEXT.__gcc_except_tab: 0x190
   __TEXT.__unwind_info: 0x548
Symbols:
+ -[THNearbyNetworkCredentials initThreadCredentials:extendedPANID:borderAgentID:activeOperationalDataSet:PSKC:networkKey:channel:panID:creationDate:lastModificationDate:isForPreferredNetwork:]
+ -[THNearbyNetworkCredentials initThreadCredentials:isForPreferredNetwork:]
+ -[THNearbyNetworkCredentials initWithActiveDataSetRecord:isForPreferredNetwork:]
+ -[THNearbyNetworkCredentials isForPreferredNetwork]
+ _OBJC_IVAR_$_THNearbyNetworkCredentials._isForPreferredNetwork
- -[THNearbyNetworkCredentials initThreadCredentials:extendedPANID:borderAgentID:activeOperationalDataSet:PSKC:networkKey:channel:panID:creationDate:lastModificationDate:isPreferredNetworkCredentials:]
- -[THNearbyNetworkCredentials initThreadCredentials:isPreferredNetworkCredentials:]
- -[THNearbyNetworkCredentials initWithActiveDataSetRecord:isPreferredNetworkCredentials:]
- -[THNearbyNetworkCredentials isPreferredNetworkCredentials]
- _OBJC_IVAR_$_THNearbyNetworkCredentials._isPreferredNetworkCredentials
CStrings:
+ "THNearbyNetworkCredentials.isForPreferredNetwork"
- "THNearbyNetworkCredentials.isPreferred"
```
