## biomesyncd

> `usr/libexec/biomesyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-258.0.0.0.0
-  __TEXT.__text: 0x4b218
+259.0.0.0.0
+  __TEXT.__text: 0x4b580
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x8bc0
-  __TEXT.__objc_methlist: 0x3cf4
+  __TEXT.__objc_stubs: 0x8c60
+  __TEXT.__objc_methlist: 0x3d44
   __TEXT.__const: 0x1352
   __TEXT.__gcc_except_tab: 0x900
-  __TEXT.__objc_methname: 0xa7b2
+  __TEXT.__objc_methname: 0xa8a9
   __TEXT.__cstring: 0x5a7b
   __TEXT.__objc_classname: 0x7f2
   __TEXT.__objc_methtype: 0x1759
-  __TEXT.__oslogstring: 0x6ad4
-  __TEXT.__unwind_info: 0x1708
+  __TEXT.__oslogstring: 0x6b29
+  __TEXT.__unwind_info: 0x1728
   __DATA_CONST.__const: 0x1148
   __DATA_CONST.__cfstring: 0x4760
   __DATA_CONST.__objc_classlist: 0x1c0

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x450
-  __DATA.__objc_const: 0x7708
-  __DATA.__objc_selrefs: 0x2990
+  __DATA_CONST.__got: 0x458
+  __DATA.__objc_const: 0x7728
+  __DATA.__objc_selrefs: 0x29b8
   __DATA.__objc_ivar: 0x3ec
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x840

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1653
+  Functions: 1660
   Symbols:   358
-  CStrings:  3120
+  CStrings:  3128
 
CStrings:
+ "TB,R,N,GisSyncSessionInFlight"
+ "adoptMultiStreamManager:"
+ "adoptPrimarySyncManager:"
+ "failed to rebuild the sync stream manager to adopt a rotated local device identifier"
+ "isSyncSessionInFlight"
+ "rebuildPrimaryUserSyncStreamManagerIfIdentifierRotationIsDue"
+ "shouldRotateLocalDeviceIdentifierForPeerStatusTracker:database:"
+ "syncSessionInFlight"
```
