## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1145.60.5.0.0
+1145.60.6.0.1
   __TEXT.__text: 0x2c28
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x34dd
+  __TEXT.__cstring: 0x3511
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xcad
   __TEXT.__objc_methtype: 0x2da

   __TEXT.__oslogstring: 0x53
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__const: 0x1088
-  __DATA_CONST.__cfstring: 0x5360
+  __DATA_CONST.__const: 0x1098
+  __DATA_CONST.__cfstring: 0x53c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x5a8
+  __DATA_CONST.__objc_arraydata: 0x5b0
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 70
-  Symbols:   770
-  CStrings:  844
+  Symbols:   772
+  CStrings:  847
 
Symbols:
+ _kMALastUIKCommitTimeKey
+ _kMASplunkUIKCommitTime
CStrings:
+ "LastUIKCommitTime"
+ "diagnosticscheckupd"
+ "uikCommitTime"
```
