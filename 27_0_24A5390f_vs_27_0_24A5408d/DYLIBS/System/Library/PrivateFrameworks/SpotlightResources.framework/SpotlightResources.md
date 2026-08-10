## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x29f40
-  __TEXT.__objc_methlist: 0x1628
-  __TEXT.__const: 0x128
+2459.102.0.0.0
+  __TEXT.__text: 0x2a018
+  __TEXT.__objc_methlist: 0x1630
+  __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0xf4c
-  __TEXT.__cstring: 0x22fc
-  __TEXT.__oslogstring: 0x24ec
-  __TEXT.__unwind_info: 0x9c0
+  __TEXT.__cstring: 0x2304
+  __TEXT.__oslogstring: 0x2506
+  __TEXT.__unwind_info: 0x9e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1108
+  __DATA_CONST.__objc_selrefs: 0x1110
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x930
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x45e0
+  __AUTH_CONST.__cfstring: 0x4600
   __AUTH_CONST.__objc_const: 0x2380
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 820
-  Symbols:   1796
-  CStrings:  875
+  Functions: 821
+  Symbols:   1797
+  CStrings:  876
 
Symbols:
+ +[SRResourcesManager trialSpotlightUITreatmentID]
CStrings:
+ ".xctest"
+ "Before loading namespace %@: _hasActiveExperiment = %@ (treatmentID: %s), _hasRollout = %@, _hasOverride = %@"
+ "ns:%s, exp:%d, trt:%s, ro:%d, over:%d"
- "Before loading namespace %@: _hasActiveExperiment = %@, _hasRollout = %@, _hasOverride = %@"
- "ns:%s, exp:%d, ro:%d, over:%d"
```
