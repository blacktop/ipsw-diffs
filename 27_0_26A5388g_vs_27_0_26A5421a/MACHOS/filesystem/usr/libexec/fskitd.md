## fskitd

> `/usr/libexec/fskitd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-974.0.11.0.0
-  __TEXT.__text: 0x4a938
+974.0.13.0.2
+  __TEXT.__text: 0x4b1cc
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x4960
-  __TEXT.__objc_methlist: 0x1e4c
+  __TEXT.__objc_stubs: 0x49c0
+  __TEXT.__objc_methlist: 0x1e8c
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x19ec
-  __TEXT.__cstring: 0x3553
-  __TEXT.__oslogstring: 0x3e73
+  __TEXT.__gcc_except_tab: 0x1a7c
+  __TEXT.__cstring: 0x35b6
+  __TEXT.__oslogstring: 0x3f53
   __TEXT.__objc_classname: 0x1ce
-  __TEXT.__objc_methname: 0x6091
-  __TEXT.__objc_methtype: 0x271c
-  __TEXT.__unwind_info: 0x1048
-  __DATA_CONST.__const: 0x29a0
+  __TEXT.__objc_methname: 0x619e
+  __TEXT.__objc_methtype: 0x273e
+  __TEXT.__unwind_info: 0x1078
+  __DATA_CONST.__const: 0x29d0
   __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x338
-  __DATA.__objc_const: 0x1e38
-  __DATA.__objc_selrefs: 0x1708
-  __DATA.__objc_ivar: 0x13c
+  __DATA.__objc_const: 0x1e68
+  __DATA.__objc_selrefs: 0x1730
+  __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x718
   __DATA.__common: 0x80

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1416
+  Functions: 1423
   Symbols:   263
-  CStrings:  1916
+  CStrings:  1930
 
CStrings:
+ "%s: another mount is in flight or already mounted for bundleID (%@) resource (%@)"
+ "%s: another mountSingleVolume is in flight for bundleID (%@) resource (%@)"
+ "%s: resource (%@) already bound to instance (%@) for bundleID (%@)"
+ "-[fskitdExtensionManager addToInflightMountForBundle:user:resource:]"
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
```
