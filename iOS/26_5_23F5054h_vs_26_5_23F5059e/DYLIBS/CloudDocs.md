## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-4479.120.7.0.1
-  __TEXT.__text: 0x85098
+4479.120.19.0.0
+  __TEXT.__text: 0x860f8
   __TEXT.__auth_stubs: 0x1410
-  __TEXT.__objc_methlist: 0x656c
+  __TEXT.__objc_methlist: 0x6594
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x4284
-  __TEXT.__cstring: 0xb2ec
-  __TEXT.__oslogstring: 0x8a99
+  __TEXT.__gcc_except_tab: 0x433c
+  __TEXT.__cstring: 0xb448
+  __TEXT.__oslogstring: 0x8b1e
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x25e0
+  __TEXT.__unwind_info: 0x2618
   __TEXT.__objc_classname: 0xd8a
-  __TEXT.__objc_methname: 0x10eeb
-  __TEXT.__objc_methtype: 0x3c05
-  __TEXT.__objc_stubs: 0xadc0
+  __TEXT.__objc_methname: 0x10fa1
+  __TEXT.__objc_methtype: 0x3c09
+  __TEXT.__objc_stubs: 0xae00
   __DATA_CONST.__got: 0x8b8
-  __DATA_CONST.__const: 0x2448
+  __DATA_CONST.__const: 0x24a0
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41a8
+  __DATA_CONST.__objc_selrefs: 0x41c8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0xa18
-  __AUTH_CONST.__const: 0x1040
-  __AUTH_CONST.__cfstring: 0x5e20
-  __AUTH_CONST.__objc_const: 0xc1c8
+  __AUTH_CONST.__const: 0x1060
+  __AUTH_CONST.__cfstring: 0x5ec0
+  __AUTH_CONST.__objc_const: 0xc1e0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D6266550-DE71-322B-98F2-545A4F04E617
-  Functions: 2986
-  Symbols:   10563
-  CStrings:  6131
+  UUID: 53F72ED2-7212-3A5C-8B65-F747C5FB26C1
+  Functions: 2997
+  Symbols:   10596
+  CStrings:  6151
 
Symbols:
+ +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:]
+ +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:].cold.1
+ +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:].cold.2
+ +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:].cold.3
+ +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:].cold.4
+ +[NSError(BRAdditions) brc_addPartialError:forFileProviderItemIdentifier:toError:]
+ +[NSError(BRAdditions) brc_addPartialError:forFileProviderItemIdentifier:toError:].cold.1
+ +[NSError(BRAdditions) brc_addPartialError:forFileProviderItemIdentifier:toError:].cold.2
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table127
+ _BRBulkCopyStructureRecordIDs
+ _BRBulkCopyStructureRecordIDs.cold.1
+ _BRGetStructureRecordIDsForFPItems
+ _BRPartialErrorsByItemIdentifierKey
+ ___BRBulkCopyStructureRecordIDs_block_invoke
+ ___BRBulkCopyStructureRecordIDs_block_invoke.107
+ ___BRBulkCopyStructureRecordIDs_block_invoke_2
+ ___BRBulkCopyStructureRecordIDs_block_invoke_2.108
+ ___BRBulkCopyStructureRecordIDs_block_invoke_2.cold.1
+ ___BRGetStructureRecordIDsForFPItems_block_invoke
+ ___BRGetStructureRecordIDsForFPItems_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48r56r_e32_v24?0"CKRecordID"8"NSError"16lr48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e69_v24?0"BRXPCAutomaticErrorProxy<BRItemServiceProtocol>"8"NSError"16lr48l8r56l8s32l8s40l8
+ ___block_literal_global.140
+ ___block_literal_global.142
+ ___block_literal_global.177
+ ___block_literal_global.182
+ ___block_literal_global.228
+ ___block_literal_global.242
+ ___block_literal_global.248
+ ___block_literal_global.428
+ ___block_literal_global.440
+ ___block_literal_global.473
+ ___block_literal_global.490
+ _objc_msgSend$copyStructureRecordIDWithReply:
+ _objc_msgSend$getStructureRecordIDsForFPItems:reply:
+ _objc_msgSend$matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:
- +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:]
- +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:].cold.1
- +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:].cold.2
- +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:].cold.3
- +[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:].cold.4
- GCC_except_table104
- GCC_except_table108
- GCC_except_table119
- GCC_except_table152
- ___block_literal_global.132
- ___block_literal_global.167
- ___block_literal_global.172
- ___block_literal_global.218
- ___block_literal_global.238
- ___block_literal_global.424
- ___block_literal_global.436
- ___block_literal_global.468
- ___block_literal_global.485
- _objc_msgSend$matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:
CStrings:
+ "+[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:]"
+ "+[NSError(BRAdditions) brc_addPartialError:forFileProviderItemIdentifier:toError:]"
+ "4479.120.19"
+ "@48@0:8@16@24^B32^@40"
+ "BRBulkCopyStructureRecordIDs"
+ "BRBulkCopyStructureRecordIDs_block_invoke_2"
+ "BRGetStructureRecordIDsForFPItems"
+ "BRPartialErrorsByItemIdentifierKey"
+ "Domain returned with empty storageURLs - %@"
+ "No domain found with ID %@"
+ "[CRIT] UNREACHABLE: Can't get domain volume UUID - no error provided%@"
+ "[CRIT] UNREACHABLE: No service proxy and no error%@"
+ "[ERROR] Failed to get domain volume UUID for domain %@: %@%@"
+ "brc_addPartialError:forFileProviderItemIdentifier:toError:"
+ "copyStructureRecordIDForItemIdentifier:reply:"
+ "copyStructureRecordIDWithReply:"
+ "getStructureRecordIDsForFPItems:reply:"
+ "matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:error:"
+ "unreachable: No service proxy and no error"
- "+[BRAccountDescriptor matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:]"
- "4479.120.7.0.1"
- "@40@0:8@16@24^B32"
- "[CRIT] UNREACHABLE: Can't get domain volume UUID%@"
- "matchDomainWithAccountAndStampDomainIfNeeded:withAccounts:persistDomain:"

```
