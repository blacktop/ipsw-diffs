## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1347.0.0.0.0
-  __TEXT.__text: 0x419f0
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_stubs: 0x7c60
-  __TEXT.__objc_methlist: 0x3580
+1353.0.0.0.0
+  __TEXT.__text: 0x421d0
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_stubs: 0x7e00
+  __TEXT.__objc_methlist: 0x35f8
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x1054
-  __TEXT.__cstring: 0x28ba
-  __TEXT.__objc_methname: 0xc547
-  __TEXT.__oslogstring: 0x9c0c
+  __TEXT.__gcc_except_tab: 0x1060
+  __TEXT.__cstring: 0x28bc
+  __TEXT.__objc_methname: 0xc725
+  __TEXT.__oslogstring: 0x9e4c
   __TEXT.__objc_classname: 0x6c3
-  __TEXT.__objc_methtype: 0x3606
+  __TEXT.__objc_methtype: 0x3629
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x11b0
+  __TEXT.__unwind_info: 0x11d0
   __DATA_CONST.__const: 0x1f48
   __DATA_CONST.__cfstring: 0x1200
   __DATA_CONST.__objc_classlist: 0x98

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x6c8
-  __DATA_CONST.__got: 0x6e8
-  __DATA.__objc_const: 0x5c20
-  __DATA.__objc_selrefs: 0x28c8
-  __DATA.__objc_ivar: 0x1bc
+  __DATA_CONST.__auth_got: 0x6d8
+  __DATA_CONST.__got: 0x6f0
+  __DATA.__objc_const: 0x5c60
+  __DATA.__objc_selrefs: 0x2928
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc68
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1155
-  Symbols:   450
-  CStrings:  2746
+  Functions: 1164
+  Symbols:   453
+  CStrings:  2766
 
Symbols:
+ _NPKPaymentWebServiceBackgroundContextPathForDevice
+ _NPKPeerPaymentAccountPathForDevice
+ _NPKPeerPaymentWebServiceContextPathForDevice
+ _NPKStorePathForPaymentPassWithUniqueIDForDevice
+ _OBJC_CLASS_$_NPKPassSignatureValidationCache
- _NPKHomeDirectoryPath
- _NPKStorePathForPaymentPassWithUniqueID
CStrings:
+ "@\"NPKPassSignatureValidationCache\""
+ "Error: Not creating pass sync service: no initialized device"
+ "Notice: No peer payment account path (no active paired device); skipping peer payment account lookup."
+ "Notice: No peer payment account path (no active paired device); skipping peer payment account write."
+ "Notice: [BarcodeEvent] No pending transactions cache path (no active paired device); skipping archive."
+ "Notice: [BarcodeEvent] No pending transactions cache path (no active paired device); skipping fetch."
+ "Warning: No secure element identifiers available; not requesting associated data for pass with uniqueID: %@"
+ "_paymentWebServiceBackgroundContextPath"
+ "_paymentWebServiceBackgroundContextPathForDevice:"
+ "_paymentWebServiceContextPath"
+ "_paymentWebServiceContextPathForDevice:"
+ "_peerPaymentAccountPath"
+ "_peerPaymentAccountPathForDevice:"
+ "_peerPaymentWebServiceContextPath"
+ "_peerPaymentWebServiceContextPathForDevice:"
+ "_signatureValidationCache"
+ "initWithCompanionPaymentPassDatabase:pairedDevice:"
+ "initWithDevice:"
+ "initWithPassSyncEngineRole:pairedDevice:"
+ "initWithPasses:device:signatureValidationCache:"
+ "invalidatePassWithUniqueID:"
- "initWithPassSyncEngineRole:"
```
