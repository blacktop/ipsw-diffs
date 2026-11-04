## logd

> `/usr/libexec/logd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

-1966.40.15.0.2
-  __TEXT.__text: 0x273d4
+1966.60.6.0.0
+  __TEXT.__text: 0x27c40
   __TEXT.__auth_stubs: 0x1bd0
   __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x4b02
+  __TEXT.__const: 0x2c8
+  __TEXT.__cstring: 0x4c1b
   __TEXT.__objc_methname: 0x428
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x858
-  __DATA_CONST.__const: 0x2398
+  __TEXT.__unwind_info: 0x870
+  __DATA_CONST.__const: 0x23e8
   __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 516
+  Functions: 521
   Symbols:   501
-  CStrings:  641
+  CStrings:  649
 
CStrings:
+ ", stopped at a bad record"
+ ", the kernel's copy is incomplete"
+ "images"
+ "kern.oslog_metadata_version"
+ "kernel metadata: %s not restored: %d (%s)"
+ "kernel metadata: restored %u of %u %s%s%s"
+ "v16@?0r^{firehose_subsystem_record_s=SSCCS[0c]}8"
+ "v16@?0r^{firehose_uuid_record_s=SSC[3C][16C]QQ[0c]}8"
```
