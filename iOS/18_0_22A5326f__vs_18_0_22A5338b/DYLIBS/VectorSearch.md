## VectorSearch

> `/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x637d4
-  __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__objc_methlist: 0x894
-  __TEXT.__const: 0x1ed8
-  __TEXT.__cstring: 0x3ec3
-  __TEXT.__constg_swiftt: 0xf0c
-  __TEXT.__swift5_typeref: 0x10b8
-  __TEXT.__swift5_fieldmd: 0xcac
+27.0.0.0.0
+  __TEXT.__text: 0x5e2ac
+  __TEXT.__auth_stubs: 0x1a80
+  __TEXT.__objc_methlist: 0x83c
+  __TEXT.__const: 0x1e38
+  __TEXT.__cstring: 0x41e3
+  __TEXT.__constg_swiftt: 0xec8
+  __TEXT.__swift5_typeref: 0xe5a
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xb15
-  __TEXT.__swift5_capture: 0x4f4
+  __TEXT.__swift5_reflstr: 0xae5
+  __TEXT.__swift5_fieldmd: 0xc6c
+  __TEXT.__swift5_types: 0xe0
+  __TEXT.__swift5_capture: 0x47c
   __TEXT.__swift5_proto: 0x184
-  __TEXT.__swift5_types: 0xe4
-  __TEXT.__oslogstring: 0xdd8
+  __TEXT.__oslogstring: 0xcf8
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x1560
-  __TEXT.__eh_frame: 0x37d0
+  __TEXT.__unwind_info: 0x14a0
+  __TEXT.__eh_frame: 0x3500
   __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methname: 0x17e5
-  __TEXT.__objc_methtype: 0x502
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__objc_methname: 0x16dd
+  __TEXT.__objc_methtype: 0x4c0
+  __TEXT.__objc_stubs: 0x7a0
+  __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_selrefs: 0x3c8
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xd60
-  __AUTH_CONST.__auth_ptr: 0x460
-  __AUTH_CONST.__const: 0x1de0
+  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__auth_ptr: 0x440
+  __AUTH_CONST.__const: 0x1cc0
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x1a60
+  __AUTH_CONST.__objc_const: 0x1a00
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x6b8
-  __AUTH.__data: 0x2c0
-  __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0x7f0
-  __DATA.__bss: 0x1700
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x480
-  __DATA_DIRTY.__data: 0xfe8
-  __DATA_DIRTY.__bss: 0x1300
-  __DATA_DIRTY.__common: 0x68
+  __AUTH.__objc_data: 0x340
+  __AUTH.__data: 0x248
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x500
+  __DATA.__bss: 0x1780
+  __DATA_DIRTY.__objc_data: 0x7f8
+  __DATA_DIRTY.__data: 0x1128
+  __DATA_DIRTY.__bss: 0x1200
+  __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1729
-  Symbols:   237
-  CStrings:  630
+  Functions: 1644
+  Symbols:   238
+  CStrings:  623
 
Symbols:
+ _BNNSDirectApplyTopK
+ _swift_stdlib_isStackAllocationSafe
+ _vDSP_maxvi
+ _vDSP_minvi
+ _vDSP_vdiv
+ _vDSP_vmma
+ _vDSP_vsmul
- _log2
- _swift_allocateGenericValueMetadata
- _vDSP_maxviD
- _vDSP_minviD
- _vDSP_vdivD
- _vDSP_vmmaD
CStrings:
+ "\x03"
+ "\x04"
+ "    ALTER TABLE attributes_temp RENAME TO attributes"
+ "    ALTER TABLE documents_temp RENAME TO documents"
+ "    ALTER TABLE observations_temp RENAME TO observations"
+ "    CREATE TABLE "
+ "    DROP TABLE attributes"
+ "    DROP TABLE attributes_fts"
+ "    DROP TABLE documents"
+ "    DROP TABLE identifiers"
+ "    DROP TABLE observations"
+ "    SELECT f0.asset_id, f0.document\n    "
+ "    WHERE f0.asset_id in ("
+ " (\n        asset_id        TEXT PRIMARY KEY"
+ " (\n        asset_id        TEXT PRIMARY KEY,\n        document        BLOB\n    ) STRICT"
+ " (\n        asset_id TEXT PRIMARY KEY\n        "
+ " (\n        id INTEGER PRIMARY KEY AUTOINCREMENT\n    ) STRICT"
+ " (\n        partition       INTEGER NOT NULL,\n        id              INTEGER NOT NULL,\n        embedding       BLOB NOT NULL,\n        observationid   TEXT NOT NULL,\n        PRIMARY KEY (partition, id)\n    ) STRICT, WITHOUT ROWID;"
+ " (\n        partition       INTEGER NOT NULL,\n        id              INTEGER NOT NULL,\n        observationid   INTEGER NOT NULL,\n        embedding       BLOB NOT NULL,\n        PRIMARY KEY (partition, id)\n    ) STRICT"
+ " (\n        partition       INTEGER NOT NULL,\n        id              INTEGER NOT NULL,\n        observationid   TEXT NOT NULL,\n        embedding       BLOB NOT NULL,\n        PRIMARY KEY (partition, id)\n    ) STRICT, WITHOUT ROWID"
+ " (asset_id, document)\n    SELECT CAST(f1.asset_id AS TEXT), f0.document\n    FROM "
+ " (partition, id, embedding, observationid)\n    SELECT f0.partition, f0.id, f0.embedding, CAST(f1.asset_id AS TEXT)\n    FROM "
+ " AND f0.asset_id in ("
+ " as f0\n    INNER JOIN identifiers f1 ON f0.asset_id = f1.rowid"
+ " as f0\n    INNER JOIN identifiers f1 ON f0.observationid = f1.rowid"
+ ")\n    SELECT CAST(f1.asset_id AS TEXT) "
+ ", but expected: "
+ "@48@0:8@16@24q32@40"
+ "Found stored embedding of size: "
+ "Mismatched list size found."
+ "Row did not have all required fields: embedding, observationid, and partition"
+ "Row did not have all required fields: id"
+ "SELECT observationid, embedding, partition\nFROM "
+ "VectorDatabaseConfig:migrate no-op for initial migration"
+ "initWithIdentifier:payload:metric:value:"
+ "observations_temp"
+ "stringIdentifiers"
- "\n    WHERE (\n        rowid in ("
- "\n    WHERE asset_id = ?"
- "\x13"
- "\x14"
- "            CREATE TABLE IF NOT EXISTS "
- "    DELETE FROM identifiers"
- "    DELETE FROM identifiers\n    WHERE rowid = ?"
- "    DROP TABLE IF EXISTS identifiers"
- "    SELECT asset_id, rowid\n    FROM "
- "    SELECT f1.rowid, f1.asset_id, f0.document\n    "
- "    SELECT rowid\n    FROM "
- "    WHERE f1.rowid in ("
- " (\n                id INTEGER PRIMARY KEY AUTOINCREMENT\n            ) STRICT"
- " (\n        asset_id\n    ) VALUES (?)"
- " (\n        asset_id        INTEGER PRIMARY KEY"
- " (\n        partition       INTEGER NOT NULL,\n        id              INTEGER NOT NULL,\n        observationid   INTEGER NOT NULL,\n        embedding       BLOB NOT NULL,\n        PRIMARY KEY (partition, id)\n    ) STRICT, WITHOUT ROWID"
- " AND f1.rowid in ("
- "@48@0:8q16@24@32@40"
- "@48@0:8q16@24@32@40"
- "@48@0:8q16@24q32@40"
- "@56@0:8@16q24@32@40@48"
- "@56@0:8q16@24@32q40@48"
- "Cannot compute top K matches over empty observations."
- "Errors while searching for identifier for multiple batches. Errors: "
- "Executing with batching SQL: %!{(MISSING)private}s, bindingValues: %!{(MISSING)private}s"
- "FROM identifiers f0"
- "INNER JOIN identifiers f1 ON f0.asset_id = f1.rowid\n"
- "Identifier lookup failed"
- "Internal error: No internal identifier set. Something very wrong, this should not happen."
- "Mismatched sorted list size found."
- "Row did not have all required fields: id, embedding, observationid, and partition"
- "SELECT observationid, embedding, partition, id\nFROM "
- "Tq,N,V_assetIdentifier"
- "Tq,N,V_identifier"
- "_assetIdentifier"
- "_identifier"
- "assetIdentifier"
- "getAssets: identifiers: %!{(MISSING)private}s -- attribute filters: %!{(MISSING)private}s -- pagination: limit (0 is unset) %!l(MISSING)d offset (0 is unset): %!l(MISSING)d -- orderBy: %!{(MISSING)private}s"
- "getIdentifiers: attribute filters: %!{(MISSING)private}s"
- "identifier"
- "initWithAssetIdentifier:payload:metric:value:"
- "initWithAssetIdentifier:stringIdentifier:payload:metric:value:"
- "initWithStringIdentifier:identifier:vectors:attributes:payload:"
- "setAssetIdentifier:"
- "setIdentifier:"

```
