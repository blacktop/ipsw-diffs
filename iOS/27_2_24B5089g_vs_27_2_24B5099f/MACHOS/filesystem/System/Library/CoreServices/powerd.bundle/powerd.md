## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2043.40.44.0.0
-  __TEXT.__text: 0x77204
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_stubs: 0x5920
-  __TEXT.__objc_methlist: 0x2c8c
+2043.40.52.0.2
+  __TEXT.__text: 0x77548
+  __TEXT.__auth_stubs: 0x1c10
+  __TEXT.__objc_stubs: 0x59a0
+  __TEXT.__objc_methlist: 0x2cbc
   __TEXT.__const: 0x540
-  __TEXT.__cstring: 0x6ebc
-  __TEXT.__objc_methname: 0x722c
-  __TEXT.__oslogstring: 0xe258
+  __TEXT.__cstring: 0x6ee1
+  __TEXT.__objc_methname: 0x7303
+  __TEXT.__oslogstring: 0xe309
   __TEXT.__objc_classname: 0x3f3
   __TEXT.__objc_methtype: 0xaa4
   __TEXT.__gcc_except_tab: 0x50c
   __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x23b0
-  __DATA_CONST.__const: 0x26c0
-  __DATA_CONST.__cfstring: 0x7700
+  __TEXT.__unwind_info: 0x23b8
+  __DATA_CONST.__const: 0x2680
+  __DATA_CONST.__cfstring: 0x7720
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x278
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x390
-  __DATA_CONST.__auth_got: 0xe08
+  __DATA_CONST.__auth_got: 0xe18
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x56b8
-  __DATA.__objc_selrefs: 0x1c38
-  __DATA.__objc_ivar: 0x3d4
+  __DATA.__objc_const: 0x5718
+  __DATA.__objc_selrefs: 0x1c58
+  __DATA.__objc_ivar: 0x3dc
   __DATA.__objc_data: 0x910
   __DATA.__data: 0xbb4
   __DATA.__common: 0x1270

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2652
-  Symbols:   575
-  CStrings:  4077
+  Functions: 2658
+  Symbols:   577
+  CStrings:  4088
 
Symbols:
+ __CFPreferencesSetMultipleWithContainer
+ _objc_setProperty_nonatomic
CStrings:
+ "%@: collecting (connState=%u ncrs=%@ connChanged=%d ncrChanged=%d)"
+ "DataCollectOnNotChargingReasonChange"
+ "Failed to initialize new pack data (packId=%u status=0x%x)"
+ "Failed to write to CFPreferences (status=0x%x)"
+ "Not initializing due to auth not passing (packId=%u failedAuthServiceFlags=%llx)"
+ "T@\"NSMutableDictionary\",&,N,V_lastNotChargingReasons"
+ "TB,N,V_collectOnNCRChange"
+ "_collectOnNCRChange"
+ "_lastNotChargingReasons"
+ "collectOnNCRChange"
+ "lastNotChargingReasons"
+ "setCollectOnNCRChange:"
+ "setLastNotChargingReasons:"
- "Connected state changed to %u"
- "Failed to initialize new pack data (packId=%u)"
```
