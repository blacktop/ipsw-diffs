## com.apple.driver.AppleHIDTransportSPI

> `com.apple.driver.AppleHIDTransportSPI`

```diff

-10400.35.1.0.0
+10400.38.1.0.0
   __TEXT.__const: 0x338 sha256:f4f5dd6c07c60941b35bb157d1604431b91cc5e27fe86256ca5e4eb3b4a167c5
-  __TEXT.__cstring: 0x7d4e sha256:7f3d86caa6422254b7397826bcc560867caa1133f9c58a7cfc69f3e07a5fc35e
-  __TEXT_EXEC.__text: 0x3f468 sha256:1e70cb5f6b2146d027c3f011ae5ad58d38a5a67a4d5c1163bca7c30578556c92
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:cf758a27b93cd16d2adeac7edc5588fa505c8d6b494005d2987dff4845dfbbcb
+  __TEXT.__cstring: 0x7d4e sha256:75db8687ecfc611cd614d3ecac4a6f28478002b865f6bfe041765d89931b73a6
+  __TEXT_EXEC.__text: 0x3f53c sha256:102aea1ee86c25743a35c75c6c60e4e10c8b4b6dac5a6fbfafba5e1b21e0bd41
+  __TEXT_EXEC.__auth_stubs: 0x620 sha256:de9a31bee3c6ed6f2803fab3780bea358cfd4f90cda8b734b6aaec6f66a50ddc
+  __DATA.__data: 0xc8 sha256:46d936b1b8523e0b03d9566f650fd9ad6f1654433a07dbeb066770b28125e63c
   __DATA.__common: 0xd8 sha256:a5645e7a3fa0866cde8842c4dab96567507c3d1a3c028b816bc63f6966367b70
-  __DATA_CONST.__mod_init_func: 0x28 sha256:c3362498cac0edcaeb9960595a90d78b262a1cb8de18d7d040d4a9ece8ce0bcd
-  __DATA_CONST.__mod_term_func: 0x28 sha256:cbf9f9c2320c8e68092fecff2b8efe1341fa80552885ddaa45e0485cea84dd9e
-  __DATA_CONST.__const: 0x4598 sha256:dfeb7a6bc3fd8b74651bf4f9edc11d7acca3af417f2cdd904681a6d24d01eba8
-  __DATA_CONST.__kalloc_type: 0xa80 sha256:c47c893586dea2d5448acafe4751c16e6cbdf553cb4ded29c32fcd41788a24e4
-  __DATA_CONST.__kalloc_var: 0x320 sha256:b27f8c164eb3c7ff256c3c77d5cd154448ed66a20c9a4e3115f29bac3b76bc4c
-  __DATA_CONST.__auth_got: 0x310 sha256:1763ae431d4aabcc1315a19aa674147b85542c0a0d25923ef2ae91e4b3d06c41
-  __DATA_CONST.__got: 0x188 sha256:b83943c4b017c21a9c9fdddb61836afbd640f3c0f408aaa1aa7465f15ec75e7f
-  UUID: 7B2A3F02-5D1B-3815-B127-8F59275A9C73
-  Functions: 1073
-  Symbols:   1878
+  __DATA_CONST.__mod_init_func: 0x28 sha256:128c929575931b1458d79eca73d2775b9a9e2662ff94210032fce78004983557
+  __DATA_CONST.__mod_term_func: 0x28 sha256:ec047e86934f18da7646d0e3444ee5fc81e756bff037eb4f41941c22a5cd9de2
+  __DATA_CONST.__const: 0x45a8 sha256:e462ba58abc3089595b0b1fcff73f61ffba6e88384b8a68ac2713e3c7cd1d861
+  __DATA_CONST.__kalloc_type: 0xa80 sha256:f92c1a6aeb7060505c327429285bde95667ab5c43c2ac3feb56a6b91e9e4031d
+  __DATA_CONST.__kalloc_var: 0x320 sha256:d5ee7746a11be7f859b68975cf2dc272096b6cc73c0291bba1b516285ca0bb3f
+  __DATA_CONST.__auth_got: 0x310 sha256:6a06cfaab97831b6207c690a6c466a23eb3fbe96e1a7a9aa0503ca0f9d614ddf
+  __DATA_CONST.__got: 0x188 sha256:20cda1748fdb566fcdf684f44cdd19b2e0186dd7d7024929c84da917c3a103f9
+  UUID: E04727A0-7F14-369C-A169-F14E2483B362
+  Functions: 1075
+  Symbols:   1880
   CStrings:  853
 
Symbols:
+ __ZN23AppleHIDTransportDevice16drainPollingFifoEP18IOMemoryDescriptorPyP8OSString
+ __ZN23AppleHIDTransportDevice19endDrainPollingFifoEP8OSString
+ __ZN23AppleHIDTransportDevice21beginDrainPollingFifoEP8OSString
+ __ZN25AppleHIDTransportProtocol16drainPollingFifoEP18IOMemoryDescriptorPyP8OSString
+ __ZN25AppleHIDTransportProtocol19endDrainPollingFifoEP8OSString
+ __ZN25AppleHIDTransportProtocol20drainNonPollingFifosEv
+ __ZN25AppleHIDTransportProtocol21beginDrainPollingFifoEP8OSString
+ __ZN26AppleHIDTransportDeviceSPI22createEnumerationCacheEv
- __ZN23AppleHIDTransportDevice12endDrainFifoEP8OSString
- __ZN23AppleHIDTransportDevice14beginDrainFifoEP8OSString
- __ZN23AppleHIDTransportDevice22createEnumerationCacheEv
- __ZN23AppleHIDTransportDevice8pollDataEP18IOMemoryDescriptorPyP8OSString
- __ZN25AppleHIDTransportProtocol12endDrainFifoEP8OSString
- __ZN25AppleHIDTransportProtocol14beginDrainFifoEP8OSString
- __ZN25AppleHIDTransportProtocol8pollDataEP18IOMemoryDescriptorPyP8OSString
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Library/Caches/com.apple.xbs/TemporaryDirectory.oMjaQI/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/AppleHIDTransportBootloaderHBPP.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Library/Caches/com.apple.xbs/TemporaryDirectory.oMjaQI/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/AppleHIDTransportDeviceSPI.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Library/Caches/com.apple.xbs/TemporaryDirectory.oMjaQI/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/AppleHIDTransportProtocolZ2.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Library/Caches/com.apple.xbs/TemporaryDirectory.oMjaQI/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/HIDSPI/AppleHIDTransportProtocolHIDSPI.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDsugB_WgU49KhiN56yHT17kzpeSJuH_vqTk-o/Library/Caches/com.apple.xbs/TemporaryDirectory.oMjaQI/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/OTP.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Library/Caches/com.apple.xbs/TemporaryDirectory.DBf8rr/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/AppleHIDTransportBootloaderHBPP.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Library/Caches/com.apple.xbs/TemporaryDirectory.DBf8rr/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/AppleHIDTransportDeviceSPI.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Library/Caches/com.apple.xbs/TemporaryDirectory.DBf8rr/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/AppleHIDTransportProtocolZ2.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Library/Caches/com.apple.xbs/TemporaryDirectory.DBf8rr/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/HIDSPI/AppleHIDTransportProtocolHIDSPI.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAiTygsm01ktt1nPwCpMDYGlqEy6qPBTFE/Library/Caches/com.apple.xbs/TemporaryDirectory.DBf8rr/Sources/AppleInputDeviceSupport_AppleHIDTransport/AppleHIDTransport/SPI/OTP.cpp"

```
