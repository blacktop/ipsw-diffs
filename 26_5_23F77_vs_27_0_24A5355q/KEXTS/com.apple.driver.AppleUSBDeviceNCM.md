## com.apple.driver.AppleUSBDeviceNCM

> `com.apple.driver.AppleUSBDeviceNCM`

```diff

-375.100.5.0.0
-  __TEXT.__const: 0x67 sha256:ff9adc98307afd44f25c5e5d22988e497bf6f44f5ebfecc239fc1dabcf0a8979
-  __TEXT.__cstring: 0xae0 sha256:041e3dfd5cc62469a23871e3c278e32671a8750919d379a34c5730d3857e6a35
-  __TEXT_EXEC.__text: 0x70a8 sha256:95fe38596987e28d3b14d68c3759cc0879e2484e9efc66e56a5850bd6499239a
+391.0.0.0.0
+  __TEXT.__const: 0x88 sha256:b028c7b7925014b7d08d0ed096aa7b32be2d49ce3aa0e29aefef29383d574430
+  __TEXT.__cstring: 0x1027 sha256:01801700a62cc6479ac8e427ff4e13298ebf3f9ecda6ad0b4aac7f616dce17fb
+  __TEXT_EXEC.__text: 0x929c sha256:96eb10424f4eae7b941bb8100e23f3af1537683966c00bf634da89c7653750cc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:54aa836374565f0bd392e4be14a8d223edfcfc207c553cac1eaf2c39ae4c0be6
-  __DATA.__common: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __DATA_CONST.__auth_got: 0x308 sha256:3afe1d05018a18d071eba8208afe2b3fbe592ba689ee2c19c2f86471bab7e4d1
-  __DATA_CONST.__got: 0xb8 sha256:a4f93affed2603c165eb3d3c30aefbad831517929fda13368cc35f2c49339824
-  __DATA_CONST.__mod_init_func: 0x10 sha256:5ab26fb7d63ff194e6e4a8f0cb1b78343f51ba0bd9694e7c5c9f172faf45bf7e
-  __DATA_CONST.__mod_term_func: 0x10 sha256:8776de642e7115beac4c46599873ce16cc0b84dea1772a56a07dbe97bf394754
-  __DATA_CONST.__const: 0x1698 sha256:d63b2e1425a286942bd71eff855760c8058eac0aa03d18ae680e415a53623b3d
-  __DATA_CONST.__kalloc_type: 0xc0 sha256:5740c946913f670ddd753478ad406ddf226bd1a1fffbe1fc8123dd44b6116238
-  UUID: D9FF2D94-F479-3524-B2E9-F7BAD68C8383
-  Functions: 159
+  __DATA.__data: 0xc8 sha256:6b41a6af5f60d43474f3c2bb61c8d154954736e8a395ab7d4c54bc2c2236e015
+  __DATA.__common: 0xd8 sha256:a5645e7a3fa0866cde8842c4dab96567507c3d1a3c028b816bc63f6966367b70
+  __DATA_CONST.__mod_init_func: 0x20 sha256:2f4472f0c500c6c05c8a5690b29b994ed2611f05f0012dc74b2b28fc84b46343
+  __DATA_CONST.__mod_term_func: 0x20 sha256:c07fba1a46560a73985062671c6d378c38c6eb7e2aec8afa2c1200899f82327a
+  __DATA_CONST.__const: 0x25c8 sha256:c40552d1dafe104126146cd9e232a95e4eab323b370245161f6e23caefce94cf
+  __DATA_CONST.__kalloc_type: 0x140 sha256:5bdc78c1e7dd3040aa06f4d38a3b13b0f416b53325cfcda7ba9f76a061b32a8b
+  __DATA_CONST.__auth_got: 0x328 sha256:63843b469b11158ae1dbf6bf934a46e989866980b41494853608fd5adcef13ed
+  __DATA_CONST.__got: 0xb8 sha256:5633727df0dd3be27116ca3fbe2b003f7fc21f13cebbb415a16b29595f3f57e5
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
