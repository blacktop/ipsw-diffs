## TrustedPeers

> `/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0x2e9b0
+61439.100.301.0.0
+  __TEXT.__text: 0x2f1e4
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x34bc
+  __TEXT.__objc_methlist: 0x36ac
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xa10
+  __TEXT.__gcc_except_tab: 0xa04
   __TEXT.__cstring: 0xcc7
-  __TEXT.__oslogstring: 0x18f2
-  __TEXT.__unwind_info: 0xb60
+  __TEXT.__oslogstring: 0x18f1
+  __TEXT.__unwind_info: 0xb48
   __TEXT.__objc_classname: 0x4f8
-  __TEXT.__objc_methname: 0x6448
+  __TEXT.__objc_methname: 0x64c6
   __TEXT.__objc_methtype: 0xcfd
-  __TEXT.__objc_stubs: 0x4300
+  __TEXT.__objc_stubs: 0x4360
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1748
+  __DATA_CONST.__objc_selrefs: 0x17f8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x4ce8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x2d8
-  __DATA.__data: 0x2b8
+  __DATA.__data: 0x2c0
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1176
-  Symbols:   1505
-  CStrings:  1631
+  Functions: 1177
+  Symbols:   1519
+  CStrings:  1637
 
Symbols:
+ _TPCheckHMACCount
+ _TPCheckSigCount
+ _TPCheckSignatureGenerationCount
+ _TPStartTrackingCheckSigCount
+ _TPStartTrackingHMACCount
+ _TPStartTrackingSignatureGenerationCount
+ _TPStopTrackingCheckSigCount
+ _TPStopTrackingHMACCount
+ _TPStopTrackingSignatureGenerationCount
- _checkSigCount
- _startTrackingCheckSigCount
- _stopTrackingCheckSigCount
CStrings:
+ "Excluding not-trusted RKs: %{public}@"
+ "Failed to iterate peers to check recovery keys, not changing RK trust: %{public}@"
+ "countOfDistrustedRecoveryKeys"
+ "countTotalNumberOfRecoveryKeys"
+ "countTotalTrustedCustodians"
+ "initWithInt:"
+ "intValue"
+ "numberWithInt:"
- "Error determining whether recovery key is excluded: %{public}@"
- "Error finding peers with current recovery key: %{public}@"

```
