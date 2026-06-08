## com.apple.driver.AppleUSBDeviceNCM

> `com.apple.driver.AppleUSBDeviceNCM`

```diff

-375.100.5.0.0
-  __TEXT.__const: 0x67
-  __TEXT.__cstring: 0xae0
-  __TEXT_EXEC.__text: 0x70a8
+391.0.0.0.0
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1027
+  __TEXT_EXEC.__text: 0x929c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0x308
+  __DATA.__common: 0xd8
+  __DATA_CONST.__mod_init_func: 0x20
+  __DATA_CONST.__mod_term_func: 0x20
+  __DATA_CONST.__const: 0x25c8
+  __DATA_CONST.__kalloc_type: 0x140
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__mod_init_func: 0x10
-  __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x1698
-  __DATA_CONST.__kalloc_type: 0xc0
-  UUID: D9FF2D94-F479-3524-B2E9-F7BAD68C8383
-  Functions: 159
+  UUID: E0E1FD39-8C8A-391F-88B3-6DD3896015D2
+  Functions: 226
   Symbols:   0
-  CStrings:  109
+  CStrings:  133
 
CStrings:
+ "%06lu.%06u %s::%s: NCM 1.1 NO-OP for reportLinkRate\n"
+ "%06lu.%06u %s::%s: bRequest 0x%x, handlerStatus 0x%x\n"
+ "%06lu.%06u %s::%s: featureSelector 0x%x reqStatus 0x%x returning 0x%x\n"
+ "%06lu.%06u %s::%s: featureSelector 0x%x returning 0x%x\n"
+ "%06lu.%06u %s::%s: isExtendedRequest cmd 0x%lx returning 0x%x\n"
+ "%06lu.%06u [0x%llx] %s::%s: "
+ "%06lu.%06u [0x%llx] %s::%s: AppleUSBNCM host version %#x (%s)\n"
+ "%06lu.%06u [0x%llx] %s::%s: EP0 OUT data phase %s due to %s=%d\n"
+ "%06lu.%06u [0x%llx] %s::%s: EP0 OUT data phase disabled due to %s\n"
+ "%06lu.%06u [0x%llx] %s::%s: device-mac-address not found for device in the device-tree, generating a fake one\n"
+ "%06lu.%06u [0x%llx] %s::%s: host-mac-address not found for host in the device-tree, generating a fake one\n"
+ "%06lu.%06u [0x%llx] %s::%s: iMACAddress %d\n"
+ "%06lu.%06u [0x%llx] %s::%s: interface interrupt disabled = %d\n"
+ "%06lu.%06u [0x%llx] %s::%s: status %d\n"
+ "%06lu.%06u [0x%llx] %s::%s: use ECID %d\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: \n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: %d\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: %s\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: %s (%s)\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: %s curr = %d, alt = %d\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: %s, %s\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: IN 0x%x\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: IN 0x%x, status 0x%x, transferSize %d\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: OUT 0x%x\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: OUT 0x%x, status 0x%x, transferSize %d\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: applying 0x%08x flags on interface\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: baseCommand 0x%x, featureSelector 0x%x, commandStatus 0x%x\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetCRCMode\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetMaxDatagramSize\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetNTBFormat\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetNTBInputSize\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetNetworkAddress\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: kSet_Ethernet_Packet_Filter\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: status %d\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: unable to acquire ifnet pointer\n"
+ "%06lu.%06u [0x%llx][%s] %s::%s: warning - gave up waiting: _pendingInCount %d, _pendingOutCount %d, _pendingLinkChange %d\n"
+ "1211111212221212111111122121111111111111111111222222222221122221211222"
+ "121111121222121211111122222222222222"
+ "121111121222121211111122222222222222222222222"
+ "AppleUSBDeviceNCM11Control"
+ "AppleUSBDeviceNCM11Data"
+ "buildExtendedCapabilityDescriptor"
+ "completeSetExtendedFeature"
+ "controlRequestCompletion"
+ "device-ncm-ctrl-debug"
+ "handleSetExtendedFeature"
+ "reportLinkRate"
+ "site.AppleUSBDeviceNCM11Control"
+ "site.AppleUSBDeviceNCM11Data"
- "%06lu.%06u %s::%s: \n"
- "%06lu.%06u %s::%s: %d\n"
- "%06lu.%06u %s::%s: %s\n"
- "%06lu.%06u %s::%s: %s (%s)\n"
- "%06lu.%06u %s::%s: %s curr = %d, alt = %d\n"
- "%06lu.%06u %s::%s: %s, %s\n"
- "%06lu.%06u %s::%s: AppleUSBNCM host version %#x (%s)\n"
- "%06lu.%06u %s::%s: EP0 OUT data phase %s due to %s=%d\n"
- "%06lu.%06u %s::%s: EP0 OUT data phase disabled due to %s\n"
- "%06lu.%06u %s::%s: applying 0x%08x flags on interface\n"
- "%06lu.%06u %s::%s: device-mac-address not found for device in the device-tree, generating a fake one\n"
- "%06lu.%06u %s::%s: host-mac-address not found for host in the device-tree, generating a fake one\n"
- "%06lu.%06u %s::%s: interface interrupt disabled = %d\n"
- "%06lu.%06u %s::%s: kNCMCommandSetCRCMode\n"
- "%06lu.%06u %s::%s: kNCMCommandSetMaxDatagramSize\n"
- "%06lu.%06u %s::%s: kNCMCommandSetNTBFormat\n"
- "%06lu.%06u %s::%s: kNCMCommandSetNTBInputSize\n"
- "%06lu.%06u %s::%s: kNCMCommandSetNetworkAddress\n"
- "%06lu.%06u %s::%s: kSet_Ethernet_Packet_Filter\n"
- "%06lu.%06u %s::%s: status %d\n"
- "%06lu.%06u %s::%s: unable to acquire ifnet pointer\n"
- "%06lu.%06u %s::%s: use ECID %d\n"
- "1211111212221212111111122121111111111111111111222222222211222212112"
- "1211111212221212111111222222222222"
- "warning - gave up waiting: _pendingInCount %d, _pendingOutCount %d\n"

```
