## Diagnostic-9016

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9016.appex/Diagnostic-9016`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1307.2.4.0.0
-  __TEXT.__text: 0x177c
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x5a0
+1307.40.46.0.0
+  __TEXT.__text: 0xf58
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x264
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__oslogstring: 0x17f
-  __TEXT.__cstring: 0x4c2
+  __TEXT.__cstring: 0x41c
   __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x677
+  __TEXT.__objc_methname: 0x564
   __TEXT.__objc_methtype: 0x25f
   __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x78
   __DATA.__objc_const: 0x3a8
-  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_selrefs: 0x210
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   Functions: 28
-  Symbols:   79
-  CStrings:  192
+  Symbols:   65
+  CStrings:  170
 
Symbols:
- _AMSupportLogSetHandler
- _OBJC_CLASS_$_CRDeviceMap
- _OBJC_CLASS_$_CRFDRUtils
- _OBJC_CLASS_$_CRUtils
- _OBJC_CLASS_$_NSNumber
- __logHandler
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retain
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x27
Functions:
~ sub_1000010b0 : 2496 -> 412
CStrings:
- "Missing required partSPC"
- "Unknown error updating YonkersIR"
- "Unknown error updating YonkersIR1"
- "Unknown error updating YonkersIR2"
- "addObject:"
- "allObjects"
- "code"
- "componentsJoinedByString:"
- "containsObject:"
- "failedSPC"
- "firstObject"
- "getInnermostNSError:"
- "intersectSet:"
- "isDataClassWithTypeInfoSupported:"
- "localizedDescription"
- "mutableCopy"
- "numberWithInteger:"
- "sealingMapCopyMultiInstanceForClassWithTypeInfo:error:"
- "supportSecureRCAM"
- "ycrt-innf"
- "ycrt-outf"
- "ycrt-rcam"
```
