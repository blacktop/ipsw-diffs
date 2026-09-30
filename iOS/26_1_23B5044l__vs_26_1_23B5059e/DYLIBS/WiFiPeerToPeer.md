## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-835.3.0.0.0
-  __TEXT.__text: 0x20e3c
+835.7.0.0.0
+  __TEXT.__text: 0x21084
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x3374
+  __TEXT.__objc_methlist: 0x33a4
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x5467
-  __TEXT.__oslogstring: 0x7e2
+  __TEXT.__oslogstring: 0x85f
   __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__unwind_info: 0x968
+  __TEXT.__unwind_info: 0x970
   __TEXT.__objc_classname: 0x779
-  __TEXT.__objc_methname: 0x811a
-  __TEXT.__objc_methtype: 0x1b7d
-  __TEXT.__objc_stubs: 0x4180
+  __TEXT.__objc_methname: 0x820d
+  __TEXT.__objc_methtype: 0x1ba1
+  __TEXT.__objc_stubs: 0x41c0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1718
+  __DATA_CONST.__objc_selrefs: 0x1738
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x3500
-  __AUTH_CONST.__objc_const: 0x5910
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__objc_const: 0x5920
+  __AUTH.__objc_data: 0x1b8
   __DATA.__objc_ivar: 0x42c
   __DATA.__data: 0x900
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0xac8
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84D4068D-BB88-32FF-B2EF-B89BE4A37D24
-  Functions: 1034
-  Symbols:   3695
-  CStrings:  2424
+  UUID: D97F0FDE-3ABD-3FDC-9F28-80F46ECCC039
+  Functions: 1036
+  Symbols:   3701
+  CStrings:  2432
 
Symbols:
+ -[WiFiAwareDataSession datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:]
+ -[WiFiAwarePublisher publishPairingDidSucceedWithPairingKeyStoreID:deviceID:]
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.121
+ _objc_msgSend$pairingRequestCompletedForDataSession:pairingKeyStoreID:deviceID:
+ _objc_msgSend$pairingRequestCompletedForPublisher:pairingKeyStoreID:deviceID:
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.115
Functions:
+ -[WiFiAwareDataSession datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:]
+ -[WiFiAwarePublisher publishPairingDidSucceedWithPairingKeyStoreID:deviceID:]
CStrings:
+ "datapathPairingDidSucceed PairingKeyStoreID: %@ DeviceID: %llu"
+ "datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:"
+ "pairingRequestCompletedForDataSession:pairingKeyStoreID:deviceID:"
+ "pairingRequestCompletedForPublisher:pairingKeyStoreID:deviceID:"
+ "publishPairingDidSucceed PairingKeyStoreID: %@ DeviceID: %llu"
+ "publishPairingDidSucceedWithPairingKeyStoreID:deviceID:"
+ "v32@0:8@\"NSUUID\"16Q24"
+ "v32@0:8@16Q24"

```
