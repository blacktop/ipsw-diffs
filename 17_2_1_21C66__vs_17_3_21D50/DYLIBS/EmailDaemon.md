## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3774.300.61.2.4
-  __TEXT.__text: 0x1aa05c
+3774.400.21.0.0
+  __TEXT.__text: 0x1aa5b4
   __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x1007c
-  __TEXT.__gcc_except_tab: 0x34234
+  __TEXT.__objc_methlist: 0x100a4
+  __TEXT.__gcc_except_tab: 0x342d0
   __TEXT.__const: 0x2d2
-  __TEXT.__cstring: 0x1983b
-  __TEXT.__oslogstring: 0x11baa
+  __TEXT.__cstring: 0x1981b
+  __TEXT.__oslogstring: 0x11bfa
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x2c
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0xc598
+  __TEXT.__unwind_info: 0xc5c0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x2723
-  __TEXT.__objc_methname: 0x2eaf8
+  __TEXT.__objc_methname: 0x2eb54
   __TEXT.__objc_methtype: 0x6bbb
-  __TEXT.__objc_stubs: 0x1ede0
+  __TEXT.__objc_stubs: 0x1ee60
   __DATA_CONST.__got: 0x680
   __DATA_CONST.__const: 0x79f0
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c1e8
-  __DATA_CONST.__objc_selrefs: 0x9a00
+  __DATA_CONST.__objc_const: 0x1c218
+  __DATA_CONST.__objc_selrefs: 0x9a18
   __DATA_CONST.__objc_arraydata: 0x750
   __AUTH_CONST.__objc_const: 0x280
-  __AUTH_CONST.__cfstring: 0xe580
+  __AUTH_CONST.__cfstring: 0xe560
   __AUTH_CONST.__objc_intobj: 0x7f8
-  __AUTH_CONST.__const: 0x9b8
+  __AUTH_CONST.__const: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x70

   __DATA.__objc_protorefs: 0x90
   __DATA.__objc_classrefs: 0xdf0
   __DATA.__objc_superrefs: 0x590
-  __DATA.__objc_ivar: 0x1410
+  __DATA.__objc_ivar: 0x1414
   __DATA.__data: 0x25c0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xe8
-  __DATA_DIRTY.__const: 0x15e0
+  __DATA_DIRTY.__const: 0x15c0
   __DATA_DIRTY.__objc_const: 0x5a30
   __DATA_DIRTY.__objc_data: 0x4ab0
   __DATA_DIRTY.__data: 0x58

   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B1AC902A-EF83-3FA7-A56B-F68B22C2C121
-  Functions: 7660
-  Symbols:   28861
-  CStrings:  13650
+  UUID: 8B70887B-46F6-357B-9E96-9C027FBA102C
+  Functions: 7668
+  Symbols:   28885
+  CStrings:  13655
 
Symbols:
+ -[EDPersistenceDatabase _isIOError:]
+ -[EDPersistenceDatabase performWithOptions:caller:block:].cold.1
+ -[EDPersistenceDatabase performWithOptions:caller:block:].cold.2
+ -[EDPersistenceDatabaseConnection hadIOError]
+ -[EDPersistenceDatabaseConnection setHadIOError:]
+ -[EDVIPManager _partiallyRedactedVIPDictionary:]
+ _OBJC_IVAR_$_EDPersistenceDatabaseConnection._hadIOError
+ ___25-[EDVIPManager saveVIPs:]_block_invoke.60
+ ___48-[EDVIPManager _partiallyRedactedVIPDictionary:]_block_invoke
+ ___48-[EDVIPManager _partiallyRedactedVIPDictionary:]_block_invoke_2
+ ___78-[EDProtectedDatabasePersistence reconcileJournalsWithSchema:completionBlock:]_block_invoke.60
+ ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke.101
+ ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke.93
+ ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke_2.94
+ ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke_2.94.cold.1
+ ___block_literal_global.78
+ _objc_msgSend$_partiallyRedactedVIPDictionary:
+ _objc_msgSend$hadIOError
+ _objc_msgSend$open
+ _objc_msgSend$setHadIOError:
- ___25-[EDVIPManager saveVIPs:]_block_invoke.53
- ___78-[EDProtectedDatabasePersistence reconcileJournalsWithSchema:completionBlock:]_block_invoke.63
- ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke.104
- ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke.96
- ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke_2.97
- ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke_2.97.cold.1
CStrings:
+ "Got IOError for transaction, retrying once"
+ "Got IOError twice in a row, aborting"
+ "TB,N,V_hadIOError"
+ "_hadIOError"
+ "_partiallyRedactedVIPDictionary:"
+ "hadIOError"
+ "setHadIOError:"
- "Unable to detach protected database"

```
