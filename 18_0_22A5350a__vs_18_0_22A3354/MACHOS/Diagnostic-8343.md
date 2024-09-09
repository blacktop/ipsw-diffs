## Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0xdf4
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__text: 0x19f4
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x440
+  __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__oslogstring: 0xc8
-  __TEXT.__cstring: 0x28b
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__oslogstring: 0x26e
+  __TEXT.__cstring: 0x438
   __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x206
+  __TEXT.__objc_methname: 0x2eb
   __TEXT.__objc_methtype: 0xbd
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x140
-  __DATA.__objc_selrefs: 0xd0
+  __DATA.__objc_const: 0x180
+  __DATA.__objc_selrefs: 0x130
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 14
-  Symbols:   55
-  CStrings:  63
+  Functions: 18
+  Symbols:   65
+  CStrings:  95
 
Symbols:
+ _AMSupportLogSetHandler
+ __logHandler
+ _objc_release_x27
+ _objc_release_x26
+ _objc_release_x28
+ _objc_release_x25
+ _OBJC_CLASS_$_CRFDRUtils
+ _AMFDRSealingManifestCopyInstanceForClass
+ _AMFDRSealingMapCopyInstanceForClass
+ _OBJC_CLASS_$_NSNumber
CStrings:
+ "Failed to get Savage SN from sealing manifest"
+ "fileExistsAtPath:isDirectory:"
+ "numberWithInteger:"
+ "verifyPSD3WithReply:"
+ "Start to decompress Pearl frames ..."
+ "Verify PSD3 successfully"
+ "Update Brunor firmware got response from corerepaird, error: %!@(MISSING)"
+ "Verify PSD3 got response from corerepaird, error: %!@(MISSING)"
+ "description"
+ "isDataClassSupported:"
+ "userInfo"
+ "Pearl frames have been decompressed, but the folder is not found"
+ "Sealing map and sealing manifest Savage SN mismatch"
+ "Start to update Savage/Yonkers firmware ..."
+ "isEqualToString:"
+ "Failed to mount hardware partition"
+ "-[PearlFramesDecompressionController updateBrunorDATFirmware]"
+ "objectForKeyedSubscript:"
+ "verifyPSD3"
+ "Start to update Brunor/Yonkers firmware ..."
+ "Get response timeout from corerepaird for verify PSD3"
+ "Savage SN from sealing manifest: %!@(MISSING)"
+ "Update Savage/Yonkers firmware successfully"
+ "updateBrunorDATFirmware"
+ "Update Brunor/Yonkers firmware successfully"
+ "code"
+ "prf1"
+ "psd3"
+ "Savage SN from sealing map: %!@(MISSING)"
+ "-[PearlFramesDecompressionController verifyPSD3]"
+ "updateBrunorDATFirmwareWithReply:"
+ "Get response timeout from corerepaird for Brunor update"

```
