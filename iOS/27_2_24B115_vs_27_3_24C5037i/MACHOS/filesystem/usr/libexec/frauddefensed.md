## frauddefensed

> `/usr/libexec/frauddefensed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-106.1.0.0.0
-  __TEXT.__text: 0x1025b0
-  __TEXT.__auth_stubs: 0x25a0
-  __TEXT.__objc_stubs: 0x1260
+107.4.0.0.0
+  __TEXT.__text: 0x100a34
+  __TEXT.__auth_stubs: 0x25b0
+  __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x5f8
-  __TEXT.__const: 0xce18
-  __TEXT.__swift5_typeref: 0x2832
-  __TEXT.__swift5_capture: 0xd10
-  __TEXT.__cstring: 0xa35c
+  __TEXT.__const: 0xce38
+  __TEXT.__swift5_typeref: 0x2848
+  __TEXT.__swift5_capture: 0xca8
+  __TEXT.__cstring: 0xa2bc
   __TEXT.__objc_methtype: 0x7de
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3248
+  __TEXT.__constg_swiftt: 0x3250
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x35e5
   __TEXT.__swift5_fieldmd: 0x4de8

   __TEXT.__swift5_proto: 0x848
   __TEXT.__swift5_types: 0x41c
   __TEXT.__objc_classname: 0x7dd
-  __TEXT.__swift_as_entry: 0x368
-  __TEXT.__swift_as_ret: 0x570
-  __TEXT.__swift_as_cont: 0xb58
-  __TEXT.__objc_methname: 0x16c2
+  __TEXT.__swift_as_entry: 0x360
+  __TEXT.__swift_as_ret: 0x564
+  __TEXT.__swift_as_cont: 0xb44
+  __TEXT.__objc_methname: 0x1692
   __TEXT.__swift5_protos: 0x78
   __TEXT.__oslogstring: 0xc4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4ee8
-  __TEXT.__eh_frame: 0xd128
-  __DATA_CONST.__const: 0xa180
+  __TEXT.__unwind_info: 0x4e88
+  __TEXT.__eh_frame: 0xcf94
+  __DATA_CONST.__const: 0xa068
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__auth_got: 0x12d8
-  __DATA_CONST.__got: 0x680
-  __DATA_CONST.__auth_ptr: 0x8c8
+  __DATA_CONST.__auth_got: 0x12e0
+  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__auth_ptr: 0x8d0
   __DATA.__objc_const: 0x2040
-  __DATA.__objc_selrefs: 0x5e8
+  __DATA.__objc_selrefs: 0x5e0
   __DATA.__objc_data: 0xf90
   __DATA.__data: 0x53f0
   __DATA.__common: 0x228

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4572
-  Symbols:   946
-  CStrings:  1229
+  Functions: 4553
+  Symbols:   950
+  CStrings:  1226
 
Symbols:
+ _$ss17FixedWidthIntegerPsE12littleEndianxvg
+ _$ss17FixedWidthIntegerPsE12littleEndianxvpMV
+ _$ss5Int64VN
+ _$ss5Int64Vs23CustomStringConvertiblesWP
+ _$ss6UInt32Vs17FixedWidthIntegersMc
+ _sqlite3_bind_int64
+ _sqlite3_column_int64
- _$sScP10backgroundScPvgZ
- _$ss6UInt32VSEsWP
- _$ss6UInt32VSesWP
CStrings:
+ " ORDER BY rowid LIMIT ?"
+ "CREATE TABLE IF NOT EXISTS CKSignatures (\n    id VARCHAR NOT NULL,\n    signature_id VARCHAR,\n    signature BLOB,\n    threshold REAL,\n    zone_name VARCHAR NOT NULL DEFAULT '',\n    modification_date VARCHAR,\n    metadata VARCHAR,\n    PRIMARY KEY (id, zone_name)\n);"
+ "Failed to bind rowid parameter. { error="
+ "Fetched page of records. { count="
+ "INSERT INTO CKSignatures (id, signature_id, signature, threshold, zone_name, modification_date, metadata)\nVALUES (?, ?, ?, ?, ?, ?, ?)\nON CONFLICT(id, zone_name) DO UPDATE SET\n    signature_id = excluded.signature_id,\n    signature = excluded.signature,\n    threshold = excluded.threshold,\n    modification_date = excluded.modification_date,\n    metadata = excluded.metadata"
+ "SELECT *, rowid FROM CKSignatures"
+ "Skipped empty signatures during search. { emptySignaturesCount="
+ "TrustKit_Signatures_v7.sqlite"
- ", assetConfiguration { "
- "CREATE TABLE IF NOT EXISTS CKSignatures (\n    id VARCHAR NOT NULL,\n    signature_id VARCHAR,\n    signature BLOB,\n    signature_size INTEGER,\n    threshold REAL,\n    zone_name VARCHAR NOT NULL DEFAULT '',\n    modification_date VARCHAR,\n    metadata VARCHAR,\n    PRIMARY KEY (id, zone_name)\n);"
- "Failed to bind Int to query. { error="
- "Failed to bind OFFSET parameter. { error="
- "Failed to unsubscribe to asset set. { error="
- "INSERT INTO CKSignatures (id, signature_id, signature, signature_size, threshold, zone_name, modification_date, metadata)\nVALUES (?, ?, ?, ?, ?, ?, ?, ?)\nON CONFLICT(id, zone_name) DO UPDATE SET\n    signature_id = excluded.signature_id,\n    signature = excluded.signature,\n    signature_size = excluded.signature_size,\n    threshold = excluded.threshold,\n    modification_date = excluded.modification_date,\n    metadata = excluded.metadata"
- "SELECT * FROM CKSignatures"
- "TrustKit_Signatures_v6.sqlite"
- "Unsubscribed from UAF asset set. { assetConfiguration { "
- "id = ? AND zone_name = ?"
- "unsubscribe:subscriptionNames:queue:completion:"
```
