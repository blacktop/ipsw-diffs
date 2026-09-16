## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-2043.2.2.0.0
-  __TEXT.__text: 0x76f00
+2043.40.43.0.0
+  __TEXT.__text: 0x77204
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_stubs: 0x5900
-  __TEXT.__objc_methlist: 0x2c6c
+  __TEXT.__objc_stubs: 0x5920
+  __TEXT.__objc_methlist: 0x2c8c
   __TEXT.__const: 0x540
-  __TEXT.__cstring: 0x6ead
-  __TEXT.__objc_methname: 0x720c
-  __TEXT.__oslogstring: 0xe213
+  __TEXT.__cstring: 0x6ebc
+  __TEXT.__objc_methname: 0x722c
+  __TEXT.__oslogstring: 0xe258
   __TEXT.__objc_classname: 0x3f3
-  __TEXT.__objc_methtype: 0xaa0
-  __TEXT.__gcc_except_tab: 0x4fc
+  __TEXT.__objc_methtype: 0xaa4
+  __TEXT.__gcc_except_tab: 0x50c
   __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x2398
+  __TEXT.__unwind_info: 0x23b0
   __DATA_CONST.__const: 0x26c0
-  __DATA_CONST.__cfstring: 0x76c0
+  __DATA_CONST.__cfstring: 0x7700
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0xe08
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x56b0
-  __DATA.__objc_selrefs: 0x1c30
+  __DATA.__objc_const: 0x56b8
+  __DATA.__objc_selrefs: 0x1c38
   __DATA.__objc_ivar: 0x3d4
   __DATA.__objc_data: 0x910
-  __DATA.__data: 0xbbc
+  __DATA.__data: 0xbb4
   __DATA.__common: 0x1270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2649
+  Functions: 2652
   Symbols:   575
-  CStrings:  4074
+  CStrings:  4077
 
CStrings:
+ "@24@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}16"
+ "Failed to retrieve feature flags (packId=%u status=0x%x)"
+ "FeatureFlags"
+ "IONVRAM-SYNCNOW-PROPERTY"
+ "Retrieved feature flags (packId=%u flags=0x%llx status=0x%x)"
+ "Sender not entitled to read battery heatmap data\n"
+ "Sender not entitled to read cycle count data\n"
+ "i32@0:8@\"NSDictionary\"16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}24"
+ "i32@0:8@16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}24"
+ "i32@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}16^@24"
+ "serviceStateFusionGetFromPacks:"
- "@24@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}16"
- "AppleARMPMUPowerSource"
- "Setting NCCP cycle count based filtering to %d\n"
- "Setting NCCP cycle count based filtering to false\n"
- "failed to read battery feature flags rc:0x%x\n"
- "i32@0:8@\"NSDictionary\"16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}24"
- "i32@0:8@16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}24"
- "i32@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}16^@24"
```
