## promotedcontentd

> `/usr/libexec/promotedcontentd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-557.2.9.0.0
-  __TEXT.__text: 0x3ce100
-  __TEXT.__auth_stubs: 0x5d80
+557.2.13.0.0
+  __TEXT.__text: 0x3cb7d8
+  __TEXT.__auth_stubs: 0x5db0
   __TEXT.__objc_stubs: 0x1a220
   __TEXT.__objc_methlist: 0x151f8
-  __TEXT.__const: 0x2b45a
+  __TEXT.__const: 0x2b4ba
   __TEXT.__gcc_except_tab: 0x1348
-  __TEXT.__cstring: 0x15e95
+  __TEXT.__cstring: 0x15d35
   __TEXT.__objc_methname: 0x2711d
   __TEXT.__oslogstring: 0x113ac
-  __TEXT.__objc_classname: 0x4d87
+  __TEXT.__objc_classname: 0x4db7
   __TEXT.__objc_methtype: 0x518d
-  __TEXT.__constg_swiftt: 0x65bc
-  __TEXT.__swift5_typeref: 0x43d8
+  __TEXT.__constg_swiftt: 0x65d0
+  __TEXT.__swift5_typeref: 0x43ca
   __TEXT.__swift5_reflstr: 0x3846
-  __TEXT.__swift5_fieldmd: 0x4b5c
+  __TEXT.__swift5_fieldmd: 0x4b50
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x3d8
-  __TEXT.__swift5_proto: 0x870
+  __TEXT.__swift5_proto: 0x874
   __TEXT.__swift5_types: 0x5e0
   __TEXT.__swift5_capture: 0x1078
   __TEXT.__swift5_protos: 0x128
   __TEXT.__swift_as_entry: 0xd8
-  __TEXT.__swift_as_ret: 0x108
-  __TEXT.__swift_as_cont: 0x258
+  __TEXT.__swift_as_ret: 0x104
+  __TEXT.__swift_as_cont: 0x254
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x8770
-  __TEXT.__eh_frame: 0x48f4
-  __DATA_CONST.__const: 0x1c4f0
+  __TEXT.__unwind_info: 0x86f0
+  __TEXT.__eh_frame: 0x4874
+  __DATA_CONST.__const: 0x1c3b8
   __DATA_CONST.__cfstring: 0xf800
-  __DATA_CONST.__objc_classlist: 0x1010
+  __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xa50
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2ed0
-  __DATA_CONST.__got: 0x18e0
-  __DATA_CONST.__auth_ptr: 0x1628
-  __DATA.__objc_const: 0x2b750
+  __DATA_CONST.__auth_got: 0x2ee8
+  __DATA_CONST.__got: 0x18e8
+  __DATA_CONST.__auth_ptr: 0x1610
+  __DATA.__objc_const: 0x2b7e0
   __DATA.__objc_selrefs: 0x9490
   __DATA.__objc_ivar: 0x1458
   __DATA.__objc_data: 0x9908

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11786
+  Functions: 11756
   Symbols:   2300
-  CStrings:  11683
+  CStrings:  11682
 
CStrings:
+ "DELETE FROM Metric WHERE batch_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM Metric AS x WHERE x.batch_id = Metric.batch_id AND x.create_time >= ?) RETURNING rowid"
+ "SELECT rowid, * FROM Metric WHERE purpose = ? ORDER BY batch_id ASC, rowid ASC"
+ "_TtC7Metrics32EmptyObservabilitySignalDatabase"
- "DELETE FROM Metric WHERE batch_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM Metric AS x WHERE x.batch_id = Metric.batch_id AND x.create_time >= CAST(strftime('%s','now') AS INTEGER) - ?)"
- "INSERT INTO ObservabilitySignalsStore(timestamp,signal,report,param1,param2,param3) VALUES (?,?,?,?,?,?)"
- "SELECT COUNT(*) FROM Metric WHERE batch_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM Metric AS x WHERE x.batch_id = Metric.batch_id AND x.create_time >= CAST(strftime('%s','now') AS INTEGER) - ?)"
- "SELECT rowid, * FROM Metric WHERE purpose = ? ORDER BY COALESCE(batch_id, '') ASC, rowid ASC"
```
