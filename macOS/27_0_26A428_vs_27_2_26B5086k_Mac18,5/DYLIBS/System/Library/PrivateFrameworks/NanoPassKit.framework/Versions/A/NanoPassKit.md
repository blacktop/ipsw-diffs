## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/Versions/A/NanoPassKit`

```diff

-1347.0.0.0.0
-  __TEXT.__text: 0x117f94
+1353.0.0.0.0
+  __TEXT.__text: 0x117e20
   __TEXT.__objc_methlist: 0x198e4
-  __TEXT.__cstring: 0x8a04
+  __TEXT.__cstring: 0x89d4
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0x908
   __TEXT.__oslogstring: 0x45a6

   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5d50
+  __TEXT.__unwind_info: 0x5d28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0xe00
   __DATA_CONST.__got: 0x6e0
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x74a0
+  __AUTH_CONST.__cfstring: 0x7480
   __AUTH_CONST.__objc_const: 0x2a538
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 9129
-  Symbols:   16025
-  CStrings:  1504
+  Symbols:   16017
+  CStrings:  1502
 
Symbols:
+ NPKHomeDirectorySubpath
+ _NPKHomeDirectorySubpath
- NPKAutomaticProvisioningStateArchivePath
- NPKPassSyncEngineArchivePath
- NPKPaymentPassDirectoryPath
- NPKPaymentWebServiceBackgroundContextPath
- NPKPaymentWebServiceContextPath
- NPKPeerPaymentAccountPath
- NPKPeerPaymentWebServiceContextPath
- NPKPendingTransactionsCachePath
- NPKRasterizedPassCachePath
- _NPKRasterizedPassCachePath
Functions:
~ -[PKPass(NanoPassKit) npkSupportsRelevancy] : 276 -> 244
~ _NPKPaymentPassDirectoryPath : 60 -> 12
~ _NPKPaymentWebServiceContextPath -> _NPKHomeDirectorySubpath : 60 -> 96
~ _NPKPaymentWebServiceBackgroundContextPath -> _NPKPaymentWebServiceContextPath : 60 -> 12
~ _NPKPeerPaymentWebServiceContextPath -> _NPKPaymentWebServiceBackgroundContextPath : 60 -> 12
~ _NPKPeerPaymentAccountPath -> _NPKPeerPaymentWebServiceContextPath : 60 -> 12
~ _NPKRasterizedPassCachePath -> _NPKPeerPaymentAccountPath : 60 -> 12
~ _NPKPassSyncEngineArchivePath : 60 -> 12
~ _NPKAutomaticProvisioningStateArchivePath : 60 -> 12
~ _NPKPendingTransactionsCachePath : 60 -> 12
~ _NPKStorePathForPaymentPassWithUniqueID : 160 -> 168
CStrings:
- "IdentityStreamlinedPresentment"
- "RasterizedPasses"
```
