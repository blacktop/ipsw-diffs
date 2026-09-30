## CSExattrCrypto

> `/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto`

```diff

-2400.22.0.0.0
-  __TEXT.__text: 0x88f4
-  __TEXT.__auth_stubs: 0x9d0
+2418.4.8.2.100
+  __TEXT.__text: 0x8870
+  __TEXT.__auth_stubs: 0x9b0
   __TEXT.__objc_methlist: 0x328
-  __TEXT.__const: 0xd0
+  __TEXT.__const: 0xd8
   __TEXT.__cstring: 0xa5c
   __TEXT.__oslogstring: 0x19f
   __TEXT.__gcc_except_tab: 0xfc
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methname: 0xcd8
   __TEXT.__objc_methtype: 0x4b8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__auth_got: 0x4e8
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__objc_const: 0x348

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F917D27-DA76-3720-9B66-5423FE0B8CF1
-  Functions: 156
-  Symbols:   784
+  UUID: F8B69401-E1D5-39BE-A410-520B7A300906
+  Functions: 159
+  Symbols:   788
   CStrings:  378
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ __MDItemSetPrivateAttributesForURL : 544 -> 556
~ ____MDItemSetPrivateAttributesForURL_block_invoke_2 : 456 -> 452
~ _copyConnection : 208 -> 220
~ __MDItemDecrypt : 412 -> 416
~ __MDItemFetchPrivateAttributesForURL : 356 -> 364
+ _OUTLINED_FUNCTION_0
~ _OUTLINED_FUNCTION_0 : 28 -> 24
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_0
~ -[MDPrivateXattrServices extractDecryptedDataWith:cryptoCallback:decryptableXids:intoDict:keyRing:xid:] : 1656 -> 1652
~ _copyUpdatedData : 3676 -> 3680
~ _serializeCFType : 1432 -> 1356
~ ____MDItemSetPrivateAttributesForURL_block_invoke_2.cold.1 : 72 -> 60
~ ____MDItemSetPrivateAttributesForURL_block_invoke_3.cold.1 : 128 -> 116
~ -[MDKeyRing fetchKeyFromKeychain:].cold.1 : 60 -> 44
~ -[MDKeyRing createKeychainItemForKey:].cold.1 : 60 -> 44
~ -[MDKeyRing createKeychainItemForKey:].cold.2 : 60 -> 44
~ -[MDKeyRing writeToKeychain:].cold.1 : 60 -> 44
~ -[MDKeyRing writeToKeychain:].cold.2 : 60 -> 44
~ -[MDKeyRing secItemFormatToDictionary:].cold.1 : 60 -> 44
~ -[MDKeyRing secItemFormatToDictionary:].cold.2 : 60 -> 44
~ _MDLabelGetTypeID.cold.1 : 20 -> 4

```
