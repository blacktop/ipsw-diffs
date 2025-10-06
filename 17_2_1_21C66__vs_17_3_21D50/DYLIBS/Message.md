## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3774.300.61.2.4
-  __TEXT.__text: 0x9e3ca4
-  __TEXT.__auth_stubs: 0x72a0
-  __TEXT.__objc_methlist: 0x117c4
-  __TEXT.__gcc_except_tab: 0x3178c
+3774.400.21.0.0
+  __TEXT.__text: 0x9e3c38
+  __TEXT.__auth_stubs: 0x72b0
+  __TEXT.__objc_methlist: 0x117ec
+  __TEXT.__gcc_except_tab: 0x31780
   __TEXT.__const: 0x42a70
-  __TEXT.__cstring: 0x3c83b
-  __TEXT.__oslogstring: 0xe258
+  __TEXT.__cstring: 0x3c7ab
+  __TEXT.__oslogstring: 0xe276
   __TEXT.__ustring: 0x22b2
   __TEXT.__swift5_typeref: 0xe780
   __TEXT.__constg_swiftt: 0xac9c

   __TEXT.__swift5_types: 0x1310
   __TEXT.__swift5_mpenum: 0xaf4
   __TEXT.__swift5_protos: 0x5c
-  __TEXT.__unwind_info: 0x300cc
+  __TEXT.__unwind_info: 0x300d0
   __TEXT.__eh_frame: 0x21480
   __TEXT.__objc_classname: 0x286a
-  __TEXT.__objc_methname: 0x2cf15
+  __TEXT.__objc_methname: 0x2cf53
   __TEXT.__objc_methtype: 0x6324
-  __TEXT.__objc_stubs: 0x23ea0
+  __TEXT.__objc_stubs: 0x23f00
   __DATA_CONST.__got: 0x1730
   __DATA_CONST.__const: 0x14e10
   __DATA_CONST.__objc_classlist: 0xa98

   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1bcf8
-  __DATA_CONST.__objc_selrefs: 0xae20
+  __DATA_CONST.__objc_selrefs: 0xae38
   __DATA_CONST.__objc_arraydata: 0xee8
   __AUTH_CONST.__cfstring: 0x17f20
   __AUTH_CONST.__const: 0x866f0

   __AUTH_CONST.__objc_arrayobj: 0xb58
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3968
+  __AUTH_CONST.__auth_got: 0x3970
   __AUTH.__objc_data: 0x4e90
   __AUTH.__data: 0x6408
   __DATA.__objc_protorefs: 0x110

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5DFE228A-84DF-38FB-8289-12B2150785AD
+  UUID: 8EEC9E39-CE49-36D3-AB90-A6BD77D4221A
   Functions: 63998
-  Symbols:   42154
+  Symbols:   42158
   CStrings:  19240
 
Symbols:
+ -[IMAPAccount _fetchAndSetSeparatorChar]
+ -[IMAPAccount _repairMailboxCache]
+ -[MFPersistenceDatabaseConnection_iOS _handleProtectedDataIOError].cold.2
+ -[MailAccount _repairMailboxCache]
+ GCC_except_table377
+ _EFContentProtectionStateDescription
+ ___block_literal_global.926
+ ___block_literal_global.929
+ ___block_literal_global.932
+ _objc_msgSend$_fetchAndSetSeparatorChar
+ _objc_msgSend$_repairMailboxCache
+ _objc_msgSend$setHadIOError:
- -[MFPersistenceDatabaseConnection_iOS _handleDetachedDatabaseIOError]
- -[MFPersistenceDatabaseConnection_iOS _handleDetachedDatabaseIOError].cold.1
- -[MFPersistenceDatabaseConnection_iOS _handleDetachedDatabaseIOError].cold.2
- GCC_except_table320
- GCC_except_table330
- GCC_except_table367
- ___69-[MFPersistenceDatabaseConnection_iOS _handleDetachedDatabaseIOError]_block_invoke
- ___block_literal_global.925
- ___block_literal_global.928
- ___block_literal_global.931
CStrings:
+ "Got back IO error with protected database attached.  Protection state = %{public}@"
+ "_fetchAndSetSeparatorChar"
+ "_repairMailboxCache"
+ "setHadIOError:"
- "-[MFPersistenceDatabaseConnection_iOS _handleDetachedDatabaseIOError]"
- "0 && \"protected database went missing\""
- "Abort if mobilemail: protected database went missing"
- "protected database went missing"

```
