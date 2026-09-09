## Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1307.2.4.0.0
-  __TEXT.__text: 0x17f8
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x420
+  __TEXT.__text: 0x1bdc
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__oslogstring: 0x235
-  __TEXT.__cstring: 0x473
+  __TEXT.__cstring: 0x4ce
   __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methname: 0x58d
+  __TEXT.__objc_methname: 0x5cf
   __TEXT.__objc_methtype: 0x25b
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x98
   __DATA.__objc_const: 0x388
-  __DATA.__objc_selrefs: 0x228
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   Functions: 25
-  Symbols:   71
-  CStrings:  164
+  Symbols:   77
+  CStrings:  170
 
Symbols:
+ _AMSupportLogSetHandler
+ _OBJC_CLASS_$_CRUtils
+ _OBJC_CLASS_$_NSNumber
+ __logHandler
+ _objc_release_x27
+ _objc_release_x28
Functions:
~ sub_100001074 : 412 -> 1408
CStrings:
+ "PearlFramesDecompressionLastSeenErrorCode"
+ "PearlFramesDecompressionLastSeenErrorDescription"
+ "code"
+ "getInnermostNSError:"
+ "localizedDescription"
+ "numberWithInteger:"
```
