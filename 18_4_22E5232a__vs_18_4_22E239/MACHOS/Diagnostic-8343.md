## Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

 696.100.57.0.0
-  __TEXT.__text: 0x14fc
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__text: 0x1d00
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_stubs: 0x480
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__oslogstring: 0x13d
-  __TEXT.__cstring: 0x368
+  __TEXT.__oslogstring: 0x295
+  __TEXT.__cstring: 0x4c6
   __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x260
+  __TEXT.__objc_methname: 0x316
   __TEXT.__objc_methtype: 0xbd
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0xe8
-  __DATA.__objc_selrefs: 0x100
+  __DATA.__objc_selrefs: 0x150
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   Functions: 18
-  Symbols:   55
-  CStrings:  73
+  Symbols:   68
+  CStrings:  102
 
Symbols:
+ _AMFDRSealingManifestCopyInstanceForClass
+ _AMFDRSealingMapCopyInstanceForClass
+ _AMSupportLogSetHandler
+ _OBJC_CLASS_$_CRFDRUtils
+ _OBJC_CLASS_$_CRUtils
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSUserDefaults
+ __logHandler
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _sleep
CStrings:
+ "Failed to get Savage SN from sealing manifest"
+ "Failed to mount hardware partition"
+ "Firmware has already been updated once"
+ "Pearl frames have been decompressed, but the folder is not found"
+ "PearlFramesDecompressionLastSeenErrorCode"
+ "PearlFramesDecompressionLastSeenErrorDescription"
+ "Savage SN from sealing manifest: %@"
+ "Savage SN from sealing map: %@"
+ "Sealing map and sealing manifest Savage SN mismatch"
+ "Start to decompress Pearl frames ..."
+ "Start to update Brunor/Yonkers firmware ..."
+ "Start to update Savage/Yonkers firmware ..."
+ "Update Brunor/Yonkers firmware successfully"
+ "Update Savage/Yonkers firmware successfully"
+ "Verify PSD3 successfully"
+ "boolForKey:"
+ "code"
+ "com.apple.Diagnostic-8343"
+ "fileExistsAtPath:isDirectory:"
+ "finalPersonalizationDone"
+ "getInnermostNSError:"
+ "initWithSuiteName:"
+ "isDataClassSupported:"
+ "isEqualToString:"
+ "localizedDescription"
+ "numberWithInteger:"
+ "prf1"
+ "psd3"
+ "setBool:forKey:"

```
