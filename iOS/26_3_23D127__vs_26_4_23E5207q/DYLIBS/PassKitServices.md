## PassKitServices

> `/System/Library/PrivateFrameworks/PassKitServices.framework/PassKitServices`

```diff

-1642.4.3.0.0
-  __TEXT.__text: 0x1f80
-  __TEXT.__auth_stubs: 0x350
+1642.5.12.3.0
+  __TEXT.__text: 0x1ffc
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x7c

   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x440
   __AUTH_CONST.__objc_intobj: 0x30

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B28664DE-EE9F-317B-8367-84784028CA65
+  UUID: 15E6EEC6-7B2C-35E8-93F7-A7855D3DC412
   Functions: 39
-  Symbols:   258
+  Symbols:   257
   CStrings:  148
 
Symbols:
+ _objc_release_x2
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_release_x27
- _objc_retain_x1
- _objc_retain_x25
- _objc_retain_x8
Functions:
~ -[PKPassKitServicesXPCService init] : 100 -> 104
~ -[PKPassKitServicesXPCService snapshotDataForPassUniqueIdentifier:size:completion:] : 264 -> 260
~ ___83-[PKPassKitServicesXPCService snapshotDataForPassUniqueIdentifier:size:completion:]_block_invoke : 208 -> 212
~ -[PKPassKitServicesXPCService imageDataForTransaction:size:completion:] : 256 -> 252
~ ___71-[PKPassKitServicesXPCService imageDataForTransaction:size:completion:]_block_invoke : 208 -> 212
~ -[PKPassKitServicesXPCService imageDataForRecurringPaymentMemo:size:completion:] : 256 -> 252
~ ___80-[PKPassKitServicesXPCService imageDataForRecurringPaymentMemo:size:completion:]_block_invoke : 208 -> 212
~ -[PKPassKitServicesXPCService _createConnection] : 408 -> 412
~ ___48-[PKPassKitServicesXPCService _createConnection]_block_invoke : 216 -> 220
~ ___48-[PKPassKitServicesXPCService _createConnection]_block_invoke_2 : 216 -> 220
~ -[PKServicePaymentTransactionImageGenerator cachedImageDataForKey:] : 384 -> 388
~ -[PKServicePaymentTransactionImageGenerator setCachedImageData:forKey:] : 692 -> 704
~ -[PKServicePaymentTransactionImageGenerator _nextIndexToUseAndEvictIfNeeded] : 428 -> 440
~ -[PKServicePaymentTransactionImageGenerator _updateNextKeyToEvict] : 312 -> 316
~ ___66-[PKServicePaymentTransactionImageGenerator _updateNextKeyToEvict]_block_invoke : 248 -> 272
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke : 672 -> 700
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_2 : 228 -> 240
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_3 : 152 -> 156
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_4 : 420 -> 440
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_5 : 244 -> 232

```
