## Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

-645.40.4.0.0
-  __TEXT.__text: 0xdf4
+645.40.12.0.0
+  __TEXT.__text: 0x14fc
   __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__oslogstring: 0xc8
-  __TEXT.__cstring: 0x28b
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__oslogstring: 0x13d
+  __TEXT.__cstring: 0x368
   __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x206
+  __TEXT.__objc_methname: 0x260
   __TEXT.__objc_methtype: 0xbd
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x140
-  __DATA.__objc_selrefs: 0xd0
+  __DATA.__objc_const: 0x180
+  __DATA.__objc_selrefs: 0xf0
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 14
+  Functions: 18
   Symbols:   55
-  CStrings:  63
+  CStrings:  73
 
CStrings:
+ "Verify PSD3 got response from corerepaird, error: %!@(MISSING)"
+ "updateBrunorDATFirmwareWithReply:"
+ "verifyPSD3WithReply:"
+ "Get response timeout from corerepaird for Brunor update"
+ "-[PearlFramesDecompressionController verifyPSD3]"
+ "Update Brunor firmware got response from corerepaird, error: %!@(MISSING)"
+ "verifyPSD3"
+ "Get response timeout from corerepaird for verify PSD3"
+ "updateBrunorDATFirmware"
+ "-[PearlFramesDecompressionController updateBrunorDATFirmware]"

```
