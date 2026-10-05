## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3901.200.41.0.0
-  __TEXT.__text: 0xae8b68
-  __TEXT.__objc_methlist: 0x144bc
+3901.200.66.2.1
+  __TEXT.__text: 0xae6530
+  __TEXT.__objc_methlist: 0x144c4
   __TEXT.__const: 0x6b858
-  __TEXT.__gcc_except_tab: 0x370d4
-  __TEXT.__cstring: 0x314d6
+  __TEXT.__gcc_except_tab: 0x370c0
+  __TEXT.__cstring: 0x31576
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__oslogstring: 0x27ed0
+  __TEXT.__oslogstring: 0x27e80
   __TEXT.__ustring: 0x23ca
-  __TEXT.__swift5_typeref: 0x10d48
-  __TEXT.__swift5_capture: 0x33968
+  __TEXT.__swift5_typeref: 0x10d2c
+  __TEXT.__swift5_capture: 0x33938
   __TEXT.__constg_swiftt: 0xda74
-  __TEXT.__swift5_reflstr: 0xf380
+  __TEXT.__swift5_reflstr: 0xf390
   __TEXT.__swift5_fieldmd: 0x15508
   __TEXT.__swift5_builtin: 0xd70
   __TEXT.__swift5_assocty: 0x1d38

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x32528
-  __TEXT.__eh_frame: 0x18a7c
+  __TEXT.__unwind_info: 0x32520
+  __TEXT.__eh_frame: 0x18b4c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x154c8
+  __DATA_CONST.__const: 0x15470
   __DATA_CONST.__objc_classlist: 0xb68
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x540
+  __DATA_CONST.__objc_protolist: 0x530
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xb8c8
-  __DATA_CONST.__objc_protorefs: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0xb8c0
+  __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x678
   __DATA_CONST.__objc_arraydata: 0xeb8
   __DATA_CONST.__got: 0x2eb0
-  __AUTH_CONST.__const: 0xacce0
+  __AUTH_CONST.__const: 0xacc68
   __AUTH_CONST.__cfstring: 0x18740
-  __AUTH_CONST.__objc_const: 0x23118
+  __AUTH_CONST.__objc_const: 0x23108
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_arrayobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x4090
-  __AUTH.__objc_data: 0x6418
-  __AUTH.__data: 0xb5c8
+  __AUTH_CONST.__auth_got: 0x4098
+  __AUTH.__objc_data: 0x5e28
+  __AUTH.__data: 0xb5d0
   __DATA.__objc_ivar: 0x1388
-  __DATA.__data: 0xe978
+  __DATA.__data: 0xe9b8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xec9
-  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__bss: 0x310
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 48719
-  Symbols:   21368
-  CStrings:  8548
+  Functions: 48711
+  Symbols:   21355
+  CStrings:  8551
 
Symbols:
+ +[MFMessageKeychainManager _addAllIdentitiesToArray:matchingPolicy:fromSyncableKeychain:withError:]
+ +[MFMessageKeychainManager _copyAllIdentitiesMatchingPolicy:error:]
+ +[MFMessageKeychainManager _logIdentityCount:purpose:address:]
+ -[MFMessageChangeManager_iOS hasCompletedInitialSyncForMailboxURL:]
+ _kSecMatchPolicy
+ _symbolic So20EFProcessTransactionC
- +[MFMessageKeychainManager _addAllIdentitiesToArray:fromSyncableKeychain:withError:usingBlock:]
- +[MFMessageKeychainManager _copyAllIdentitiesWithError:usingBlock:]
- +[MFMessageKeychainManager _validateIdentity:forAddress:policy:usage:error:]
- +[MFMessageKeychainManager validateEncryptionIdentity:forAddress:error:]
- +[MFMessageKeychainManager validateSigningIdentity:forAddress:error:]
- _MFMessageKeychainManagerCertificateDeniedDomain
- _OBJC_CLASS_$_EDAccountDeletionDiagnostics
- __OBJC_$_PROTOCOL_REFS_OS_os_transaction
- __OBJC_LABEL_PROTOCOL_$_OS_os_transaction
- __OBJC_PROTOCOL_$_OS_os_transaction
- ___67+[MFMessageKeychainManager _copyAllIdentitiesWithError:usingBlock:]_block_invoke
- ___67+[MFMessageKeychainManager _copyAllIdentitiesWithError:usingBlock:]_block_invoke_2
- ___69+[MFMessageKeychainManager copyAllSigningIdentitiesForAddress:error:]_block_invoke
- ___72+[MFMessageKeychainManager copyAllEncryptionIdentitiesForAddress:error:]_block_invoke
- ___block_descriptor_40_e8_32b_e24_B16?0^{__SecIdentity=}8ls32l8
- ___block_descriptor_56_e8_32o40o48r_e24_B16?0^{__SecIdentity=}8lr48l8s32l8s40l8
- _flat unique So17OS_os_transaction_p
- _symbolic Spy_____SgG 9IMAP2MIME8BoundaryV
- _symbolic ______p So17OS_os_transactionP
CStrings:
+ "#SMIMEErrors Found %lu usable %{public}s identities for \"%@\""
+ "DELETE FROM properties WHERE key = 'com.apple.mail.searchableIndex.lastProcessedAttachmentIDKey';"
+ "RaveBBaseline"
+ "RaveResetBackFillMessageBodiesStages2"
+ "Resetting lastProcessedAttachmentID for attachment re-donation."
+ "encryption"
+ "signing"
- "#SMIMEErrors Found %lu (out of %lu) matching encryption identities for \"%@\""
- "#SMIMEErrors Found %lu (out of %lu) matching signing identities for \"%@\""
- "B16@?0^{__SecIdentity=}8"
- "MFMessageKeychainManagerCertificateDeniedDomain"
```
