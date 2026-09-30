## ospredictiond

> `/usr/libexec/ospredictiond`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 286.2.1.0.0
-  __TEXT.__text: 0x68834
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x98c0
-  __TEXT.__objc_methlist: 0x9388
-  __TEXT.__const: 0x458
+  __TEXT.__text: 0x690c4
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x9960
+  __TEXT.__objc_methlist: 0x93a0
+  __TEXT.__const: 0x468
   __TEXT.__cstring: 0x55b4
-  __TEXT.__objc_methname: 0x153ff
-  __TEXT.__oslogstring: 0x7327
+  __TEXT.__objc_methname: 0x15478
+  __TEXT.__oslogstring: 0x7474
   __TEXT.__objc_classname: 0xe10
   __TEXT.__objc_methtype: 0x248d
   __TEXT.__gcc_except_tab: 0x8d0
   __TEXT.__ustring: 0x2a
-  __TEXT.__unwind_info: 0x14e8
-  __DATA_CONST.__const: 0x1180
+  __TEXT.__unwind_info: 0x1500
+  __DATA_CONST.__const: 0x11c0
   __DATA_CONST.__cfstring: 0x62c0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_arrayobj: 0x480
   __DATA_CONST.__objc_doubleobj: 0x70
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x4c8
   __DATA.__objc_const: 0x10670
-  __DATA.__objc_selrefs: 0x3d78
+  __DATA.__objc_selrefs: 0x3da0
   __DATA.__objc_ivar: 0xdc4
   __DATA.__objc_data: 0x27b0
   __DATA.__data: 0x780

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3330
-  Symbols:   285
-  CStrings:  4793
+  Functions: 3339
+  Symbols:   287
+  CStrings:  4806
 
Symbols:
+ _MGIsDeviceOneOfType
+ _OBJC_CLASS_$_CBClient
CStrings:
+ "CBClient activate failed, reading lux from the system: %{public}@"
+ "Multiple displays: %{BOOL}d"
+ "No per-display lux: %{public}@"
+ "No valid per-display lux %{public}@"
+ "Only %lu display client(s), reading lux from the system"
+ "Per-display lux %{public}@, using max %d"
+ "Reading lux from %lu displays"
+ "activateWithError:"
+ "copyPropertyForKey:error:"
+ "luxReadingsFromDisplays:"
+ "newDisplayClientForID:%lu failed: %{public}@"
+ "newDisplayClientForID:withError:"
+ "perDisplayClients"
```
