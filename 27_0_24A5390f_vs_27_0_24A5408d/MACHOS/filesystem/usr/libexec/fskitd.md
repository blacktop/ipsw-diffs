## fskitd

> `/usr/libexec/fskitd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-974.0.11.0.0
-  __TEXT.__text: 0x4c6ec
+974.0.13.0.2
+  __TEXT.__text: 0x4cef8
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x52e0
-  __TEXT.__objc_methlist: 0x22b4
+  __TEXT.__objc_stubs: 0x5340
+  __TEXT.__objc_methlist: 0x22f4
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x1f4c
-  __TEXT.__oslogstring: 0x4555
-  __TEXT.__cstring: 0x3900
+  __TEXT.__gcc_except_tab: 0x1fdc
+  __TEXT.__oslogstring: 0x4635
+  __TEXT.__cstring: 0x3963
   __TEXT.__objc_classname: 0x1fa
-  __TEXT.__objc_methname: 0x67e5
-  __TEXT.__objc_methtype: 0x27cf
-  __TEXT.__unwind_info: 0x1160
-  __DATA_CONST.__const: 0x2688
+  __TEXT.__objc_methname: 0x68f2
+  __TEXT.__objc_methtype: 0x27f1
+  __TEXT.__unwind_info: 0x1190
+  __DATA_CONST.__const: 0x26b0
   __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x5b8
   __DATA_CONST.__got: 0x370
-  __DATA.__objc_const: 0x22f0
-  __DATA.__objc_selrefs: 0x1918
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_const: 0x2320
+  __DATA.__objc_selrefs: 0x1940
+  __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x718
   __DATA.__common: 0x88

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1484
+  Functions: 1491
   Symbols:   304
-  CStrings:  2096
+  CStrings:  2110
 
CStrings:
+ "%s: another mount is in flight or already mounted for bundleID (%@) resource (%@)"
+ "%s: another mountSingleVolume is in flight for bundleID (%@) resource (%@)"
+ "%s: resource (%@) already bound to instance (%@) for bundleID (%@)"
+ "-[fskitdExtensionManager addToInflightMountForBundle:user:resource:]"
+ "-[fskitdXPCServer mountSingleVolumeForResource:bundleID:mountPath:options:replyHandler:]_block_invoke_4"
+ "@36@0:8@16I24@28"
+ "B40@0:8@16@24@32"
+ "T@\"NSMutableSet\",&,V_inFlightSingleVolumeMounts"
+ "_inFlightSingleVolumeMounts"
+ "addToInflightMountForBundle:user:resource:"
+ "inFlightSingleVolumeMounts"
+ "removeFromInflightMountForBundle:user:resource:"
+ "setInFlightSingleVolumeMounts:"
+ "singleVolumeMountKeyForBundle:uid:resource:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
- "-[fskitdXPCServer mountSingleVolumeForResource:bundleID:mountPath:options:replyHandler:]_block_invoke_3"
```
