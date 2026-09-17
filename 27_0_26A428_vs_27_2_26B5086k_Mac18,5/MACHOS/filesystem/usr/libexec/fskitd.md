## fskitd

> `/usr/libexec/fskitd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-974.0.13.0.2
-  __TEXT.__text: 0x4a6b0
+974.40.11.0.0
+  __TEXT.__text: 0x4aba0
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x49c0
-  __TEXT.__objc_methlist: 0x1e8c
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x1a7c
-  __TEXT.__cstring: 0x35b6
-  __TEXT.__oslogstring: 0x3f53
-  __TEXT.__objc_classname: 0x1ce
-  __TEXT.__objc_methname: 0x619e
-  __TEXT.__objc_methtype: 0x273e
-  __TEXT.__unwind_info: 0x1750
+  __TEXT.__objc_stubs: 0x4a00
+  __TEXT.__objc_methlist: 0x1ed4
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x1ad4
+  __TEXT.__cstring: 0x3635
+  __TEXT.__oslogstring: 0x3f9e
+  __TEXT.__objc_classname: 0x1de
+  __TEXT.__objc_methname: 0x62c4
+  __TEXT.__objc_methtype: 0x274c
+  __TEXT.__unwind_info: 0x1758
   __DATA_CONST.__const: 0x29d0
-  __DATA_CONST.__cfstring: 0x720
+  __DATA_CONST.__cfstring: 0x760
   __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x338
-  __DATA.__objc_const: 0x1e68
-  __DATA.__objc_selrefs: 0x1730
-  __DATA.__objc_ivar: 0x140
+  __DATA_CONST.__got: 0x340
+  __DATA.__objc_const: 0x1ee8
+  __DATA.__objc_selrefs: 0x1768
+  __DATA.__objc_ivar: 0x148
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x718
+  __DATA.__data: 0x778
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1423
-  Symbols:   263
-  CStrings:  1930
+  Functions: 1428
+  Symbols:   264
+  CStrings:  1947
 
Symbols:
+ ___NSArray0__struct
CStrings:
+ "%s: dropping orphaned task %@ on connection invalidation"
+ "-[fskitdXPCServer handleInvalidated]"
+ "@24@0:8B16B20"
+ "FSClientFSCKXPC"
+ "FSClientFSCKXPCProtocols"
+ "Incomming connection, entitled %d, fsck-entitled %d"
+ "T@\"NSMutableSet\",&,V_fsckTaskUUIDs"
+ "TB,V_clientHasFSCKEntitlement"
+ "TB,V_clientHasLiveFSEntitlement"
+ "_clientHasFSCKEntitlement"
+ "_clientHasLiveFSEntitlement"
+ "_fsckTaskUUIDs"
+ "clientHasFSCKEntitlement"
+ "clientHasLiveFSEntitlement"
+ "com.apple.private.security.disk-device-access"
+ "com.apple.rootless.restricted-block-devices"
+ "fsckTaskUUIDs"
+ "initForEntitledClient:fsckEntitled:"
+ "removeAllObjects"
+ "setClientHasFSCKEntitlement:"
+ "setClientHasLiveFSEntitlement:"
+ "setFsckTaskUUIDs:"
- "Incomming connection, entitled %d"
- "TB,V_clientHasEntitlement"
- "_clientHasEntitlement"
- "clientHasEntitlement"
- "setClientHasEntitlement:"
```
