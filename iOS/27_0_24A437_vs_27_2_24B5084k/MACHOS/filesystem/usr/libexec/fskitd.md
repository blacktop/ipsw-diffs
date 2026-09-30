## fskitd

> `/usr/libexec/fskitd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-974.0.13.0.2
-  __TEXT.__text: 0x4c5d8
+974.40.11.0.0
+  __TEXT.__text: 0x4ca90
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x5340
-  __TEXT.__objc_methlist: 0x22f4
-  __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x1fdc
-  __TEXT.__oslogstring: 0x4635
-  __TEXT.__cstring: 0x3963
-  __TEXT.__objc_classname: 0x1fa
-  __TEXT.__objc_methname: 0x68f2
-  __TEXT.__objc_methtype: 0x27f1
-  __TEXT.__unwind_info: 0x1870
+  __TEXT.__objc_stubs: 0x5380
+  __TEXT.__objc_methlist: 0x233c
+  __TEXT.__const: 0x130
+  __TEXT.__gcc_except_tab: 0x2034
+  __TEXT.__oslogstring: 0x4680
+  __TEXT.__cstring: 0x39e2
+  __TEXT.__objc_classname: 0x20a
+  __TEXT.__objc_methname: 0x6a18
+  __TEXT.__objc_methtype: 0x27ff
+  __TEXT.__unwind_info: 0x1878
   __DATA_CONST.__const: 0x26b0
-  __DATA_CONST.__cfstring: 0x900
+  __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x5b8
   __DATA_CONST.__got: 0x370
-  __DATA.__objc_const: 0x2320
-  __DATA.__objc_selrefs: 0x1940
-  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_const: 0x23a0
+  __DATA.__objc_selrefs: 0x1978
+  __DATA.__objc_ivar: 0x18c
   __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x718
+  __DATA.__data: 0x778
   __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1491
+  Functions: 1496
   Symbols:   304
-  CStrings:  2110
+  CStrings:  2127
 
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
