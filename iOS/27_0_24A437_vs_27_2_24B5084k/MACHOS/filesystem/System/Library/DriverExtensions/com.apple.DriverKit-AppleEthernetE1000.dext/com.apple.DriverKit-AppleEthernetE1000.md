## com.apple.DriverKit-AppleEthernetE1000

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetE1000.dext/com.apple.DriverKit-AppleEthernetE1000`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-171.0.0.0.0
-  __TEXT.__text: 0x30814
+175.40.1.0.0
+  __TEXT.__text: 0x30b2c
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__const: 0xb78
-  __TEXT.__cstring: 0x1c71
-  __TEXT.__oslogstring: 0x19ab
-  __DATA_CONST.__const: 0x15b0
+  __TEXT.__cstring: 0x1c84
+  __TEXT.__oslogstring: 0x19de
+  __DATA_CONST.__const: 0x15e0
   __DATA_CONST.__osclassinfo: 0x28
   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x38

   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 899
-  Symbols:   1065
-  CStrings:  415
+  Functions: 903
+  Symbols:   1067
+  CStrings:  417
 
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/ApplePCINetworking_driverkit/install/TempContent/Objects/ApplePCINetworking.build/AppleEthernetE1000.build/Objects-normal/arm64e/DriverKit_AppleEthernetE1000-ecdbe59502542bd91aa5527189b8a013.o
+ __ZN28DriverKit_AppleEthernetE100018setHardwareAddressEP10ether_addr
+ __ZN34DriverKit_AppleEthernetE1000_IVars18setHardwareAddressEPK10ether_addr
+ __ZThn48_N28DriverKit_AppleEthernetE100018setHardwareAddressEP10ether_addr
+ ____ZN28DriverKit_AppleEthernetE100018setHardwareAddressEP10ether_addr_block_invoke
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/ApplePCINetworking_driverkit/install/TempContent/Objects/ApplePCINetworking.build/AppleEthernetE1000.build/Objects-normal/arm64e/DriverKit_AppleEthernetE1000-c892048fc23ab797230033903cf90c5f.o
- __ZN21IOUserNetworkEthernet18setHardwareAddressEP10ether_addr
- __ZThn48_N21IOUserNetworkEthernet18setHardwareAddressEP10ether_addr
CStrings:
+ "e1000::%s(%d): addr %02x:%02x:%02x:%02x:%02x:%02x\n"
+ "setHardwareAddress"
```
