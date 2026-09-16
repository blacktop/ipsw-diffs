## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-5168.0.55.0.0
-  __TEXT.__text: 0x7c9f4
-  __TEXT.__objc_methlist: 0x66e4
+5168.40.149.0.1
+  __TEXT.__text: 0x7c284
+  __TEXT.__objc_methlist: 0x6724
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x3b68
-  __TEXT.__cstring: 0xb89c
-  __TEXT.__oslogstring: 0x8d22
+  __TEXT.__gcc_except_tab: 0x3c28
+  __TEXT.__cstring: 0xb8ea
+  __TEXT.__oslogstring: 0x8d78
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x3040
+  __TEXT.__unwind_info: 0x3058
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24a8
+  __DATA_CONST.__const: 0x24e8
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4248
+  __DATA_CONST.__objc_selrefs: 0x4270
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x8d8
-  __AUTH_CONST.__const: 0x1060
+  __DATA_CONST.__got: 0x8e0
+  __AUTH_CONST.__const: 0x10c0
   __AUTH_CONST.__cfstring: 0x5f60
-  __AUTH_CONST.__objc_const: 0xdb30
+  __AUTH_CONST.__objc_const: 0xdb88
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__auth_got: 0xa68
   __AUTH.__objc_data: 0x16d0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x5e8
+  __DATA.__objc_ivar: 0x5ec
   __DATA.__data: 0xd30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3032
-  Symbols:   6519
-  CStrings:  2202
+  Functions: 3045
+  Symbols:   6533
+  CStrings:  2204
 
Symbols:
+ +[BRFileProviderHelper br_appHasNonUploadedFiles:completion:]
+ +[BRXPCClientUtils executeWithMaxRetries:retriableError:error:block:]
+ -[BRWaitForContainersDownloadOperation setUnregisterPriorityHintOnFinish:]
+ -[BRWaitForContainersDownloadOperation unregisterPriorityHintOnFinish]
+ _ACErrorDomain
+ _FPAppHasNonUploadedFiles
+ _OBJC_IVAR_$_BRWaitForContainersDownloadOperation._unregisterPriorityHintOnFinish
+ ___57+[BRXPCClientUtils executeXPCWithMaxRetries:error:block:]_block_invoke
+ ___64-[ACAccountStore(BRAdditions) _br_getAllAppleAccountsWithError:]_block_invoke
+ ___64-[ACAccountStore(BRAdditions) _br_getAllAppleAccountsWithError:]_block_invoke_2
+ ___77-[NSFileProviderDomain(BRAdditions) br_volumeUUIDForDataSeparated:withError:]_block_invoke
+ ___block_descriptor_32_e17_B16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40r_e9_B16?0^8lr40l8s32l8
+ _objc_msgSend$accountsWithAccountTypeIdentifiers:error:
+ _objc_msgSend$executeWithMaxRetries:retriableError:error:block:
+ _objc_msgSend$isActive
+ _objc_msgSend$setUnregisterPriorityHintOnFinish:
- _BRReadOnlyShareUploadErrorCategory
- _objc_msgSend$accountTypeWithAccountTypeIdentifier:
- _objc_msgSend$accountsWithAccountType:
CStrings:
+ "+[BRXPCClientUtils executeWithMaxRetries:retriableError:error:block:]"
+ "5168.40.149.0.1"
+ "B16@?0@\"NSError\"8"
+ "Failed fetching the apple accounts from the accounts store: %@"
+ "Got a nil accounts array back from the accounts store without an error"
+ "[NOTICE] Accounts store returned %lu apple accounts, %lu of them active%@"
+ "[NOTICE] Block execution failed with a retriable error - retrying: %@%@"
- "+[BRXPCClientUtils executeXPCWithMaxRetries:error:block:]"
- "5168.0.55"
- "Got nil accounts array back from Accounts Store accountsWithAccountType"
- "[NOTICE] Block execution failed because of XPC - retrying%@"
- "readOnlyShareUpload"
```
