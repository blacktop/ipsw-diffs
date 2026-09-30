## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs`

```diff

-5168.0.55.0.0
-  __TEXT.__text: 0x857c0
-  __TEXT.__objc_methlist: 0x672c
-  __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x3e2c
-  __TEXT.__cstring: 0xb1ce
-  __TEXT.__oslogstring: 0x8a0d
+5168.40.149.0.1
+  __TEXT.__text: 0x85090
+  __TEXT.__objc_methlist: 0x6764
+  __TEXT.__const: 0x1c0
+  __TEXT.__gcc_except_tab: 0x3ef0
+  __TEXT.__cstring: 0xb21c
+  __TEXT.__oslogstring: 0x8a63
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x30d8
+  __TEXT.__unwind_info: 0x30f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb18
+  __DATA_CONST.__const: 0xb30
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42a0
+  __DATA_CONST.__objc_selrefs: 0x42c8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x8d0
-  __AUTH_CONST.__const: 0x2da0
+  __DATA_CONST.__got: 0x8d8
+  __AUTH_CONST.__const: 0x2e00
   __AUTH_CONST.__cfstring: 0x5dc0
-  __AUTH_CONST.__objc_const: 0xdcb8
+  __AUTH_CONST.__objc_const: 0xdd10
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xa30
+  __AUTH_CONST.__auth_got: 0xa38
   __AUTH.__objc_data: 0x15b8
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x600
+  __DATA.__objc_ivar: 0x604
   __DATA.__data: 0xd30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x938

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3073
-  Symbols:   6726
-  CStrings:  2150
+  Functions: 3086
+  Symbols:   6739
+  CStrings:  2152
 
Symbols:
+ +[BRFileProviderHelper br_appHasNonUploadedFiles:completion:]
+ +[BRXPCClientUtils executeWithMaxRetries:retriableError:error:block:]
+ -[BRWaitForContainersDownloadOperation setUnregisterPriorityHintOnFinish:]
+ -[BRWaitForContainersDownloadOperation unregisterPriorityHintOnFinish]
+ OBJC_IVAR_$_BRWaitForContainersDownloadOperation._unregisterPriorityHintOnFinish
+ _ACErrorDomain
+ _FPAppHasNonUploadedFiles
+ __64-[ACAccountStore(BRAdditions) _br_getAllAppleAccountsWithError:]_block_invoke
+ ___57+[BRXPCClientUtils executeXPCWithMaxRetries:error:block:]_block_invoke
+ ___64-[ACAccountStore(BRAdditions) _br_getAllAppleAccountsWithError:]_block_invoke
+ ___64-[ACAccountStore(BRAdditions) _br_getAllAppleAccountsWithError:]_block_invoke_2
+ ___77-[NSFileProviderDomain(BRAdditions) br_volumeUUIDForDataSeparated:withError:]_block_invoke
+ ___block_descriptor_32_e17_B16?0"NSError"8l
+ _objc_msgSend$accountsWithAccountTypeIdentifiers:error:
+ _objc_msgSend$executeWithMaxRetries:retriableError:error:block:
+ _objc_msgSend$isActive
+ _objc_msgSend$setUnregisterPriorityHintOnFinish:
- _BRReadOnlyShareUploadErrorCategory
- _OUTLINED_FUNCTION_14
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
