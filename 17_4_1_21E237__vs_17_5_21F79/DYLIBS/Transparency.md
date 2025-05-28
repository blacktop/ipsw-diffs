## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1033.100.65.0.0
-  __TEXT.__text: 0x33b50
+1033.120.12.0.0
+  __TEXT.__text: 0x33e80
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x2b5c
-  __TEXT.__cstring: 0x1e23
-  __TEXT.__const: 0x160
+  __TEXT.__objc_methlist: 0x2b8c
+  __TEXT.__cstring: 0x1f10
+  __TEXT.__const: 0x168
   __TEXT.__gcc_except_tab: 0x4a0
   __TEXT.__oslogstring: 0x169b
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__unwind_info: 0x10a0
   __TEXT.__objc_classname: 0x59a
-  __TEXT.__objc_methname: 0x614c
+  __TEXT.__objc_methname: 0x6198
   __TEXT.__objc_methtype: 0x1928
-  __TEXT.__objc_stubs: 0x49c0
+  __TEXT.__objc_stubs: 0x4a20
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x11a8
+  __DATA_CONST.__const: 0x11d0
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5018
-  __DATA_CONST.__objc_selrefs: 0x1850
+  __DATA_CONST.__objc_const: 0x5078
+  __DATA_CONST.__objc_selrefs: 0x1860
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__cfstring: 0x2fe0
+  __AUTH_CONST.__cfstring: 0x3100
   __AUTH_CONST.__objc_const: 0x280
-  __AUTH_CONST.__const: 0xb80
+  __AUTH_CONST.__const: 0xb20
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__auth_got: 0x338
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x2b0
-  __DATA.__data: 0x598
+  __DATA.__objc_ivar: 0x2b8
+  __DATA.__data: 0x5c0
   __DATA.__bss: 0x20
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__const: 0x11e0
+  __DATA_DIRTY.__const: 0x1240
   __DATA_DIRTY.__objc_const: 0x1628
-  __DATA_DIRTY.__objc_data: 0xf00
-  __DATA_DIRTY.__bss: 0x1b8
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__bss: 0x190
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1420
-  Symbols:   4894
-  CStrings:  1908
+  Functions: 1425
+  Symbols:   4910
+  CStrings:  1921
 
Symbols:
+ -[KTSelfStatusResult idsAccountStatus]
+ -[KTSelfStatusResult setIdsAccountStatus:]
+ -[KTStatusResult idsAccountStatus]
+ -[KTStatusResult setIdsAccountStatus:]
+ GCC_except_table64
+ _KTIDSAccountStatusGetString
+ _OBJC_IVAR_$_KTSelfStatusResult._idsAccountStatus
+ _OBJC_IVAR_$_KTStatusResult._idsAccountStatus
+ ___22-[KTStatus getStatus:]_block_invoke.264
+ ___22-[KTStatus getStatus:]_block_invoke.267
+ ___22-[KTStatus getStatus:]_block_invoke_2.268
+ ___26-[KTStatus getSelfStatus:]_block_invoke.273
+ ___26-[KTStatus getSelfStatus:]_block_invoke.276
+ ___26-[KTStatus getSelfStatus:]_block_invoke_2.277
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.301
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.304
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.305
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.310
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.313
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.314
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.282
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.285
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.287
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.292
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.295
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.296
+ ___block_literal_global.256
+ ___block_literal_global.263
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.284
+ ___block_literal_global.291
+ ___block_literal_global.294
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.303
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.312
+ ___block_literal_global.88
+ ___block_literal_global.91
+ ___block_literal_global.93
+ _kKTStatusIDSAccount
+ _kTransparencyMaxmimumServerRPCWaitTime
+ _objc_msgSend$formatEventName:application:
+ _objc_msgSend$idsAccountStatus
+ _objc_msgSend$setIdsAccountStatus:
- GCC_except_table59
- ___22-[KTStatus getStatus:]_block_invoke.244
- ___22-[KTStatus getStatus:]_block_invoke.247
- ___22-[KTStatus getStatus:]_block_invoke_2.248
- ___26-[KTStatus getSelfStatus:]_block_invoke.253
- ___26-[KTStatus getSelfStatus:]_block_invoke.256
- ___26-[KTStatus getSelfStatus:]_block_invoke_2.257
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.281
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.284
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.285
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.290
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.293
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.294
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.262
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.265
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.267
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.272
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.275
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.276
- ___block_literal_global.236
- ___block_literal_global.243
- ___block_literal_global.250
- ___block_literal_global.252
- ___block_literal_global.259
- ___block_literal_global.261
- ___block_literal_global.269
- ___block_literal_global.271
- ___block_literal_global.278
- ___block_literal_global.283
- ___block_literal_global.287
- ___block_literal_global.292
- ___block_literal_global.296
- ___block_literal_global.78
- ___block_literal_global.80
- ___block_literal_global.87
CStrings:
+ "IDSAccountStatusInvalid"
+ "IDSAccountStatusValidAppleID"
+ "IDSAccountStatusValidPhoneInvalidAppleID"
+ "IDSAccountStatusValidPhoneOnly"
+ "KTStatus: optIn = %@, everOptIn = %d, serverOptIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@, idsAccountStatus = %@, pendingChanges: %@\n"
+ "KTStatus: optIn = %@, serverOptIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@, idsAccountStatus = %@, pendingChanges: %@\n"
+ "PV2OptInBoth"
+ "PeerV2OptIn"
+ "TQ,V_idsAccountStatus"
+ "_idsAccountStatus"
+ "idsAccountStatus"
+ "ktIDSPV2OptIn"
+ "peerOptIn"
+ "r"
+ "setIdsAccountStatus:"
- "KTStatus: optIn = %@, everOptIn = %d, serverOptIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@, pendingChanges: %@\n"
- "KTStatus: optIn = %@, serverOptIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@, pendingChanges: %@\n"
- "R"

```
