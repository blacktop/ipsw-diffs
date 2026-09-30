## SettingsFoundation

> `/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation`

```diff

-1086.0.0.0.0
-  __TEXT.__text: 0x11920
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x664
-  __TEXT.__const: 0x7f8
-  __TEXT.__cstring: 0x1ac8
+1087.0.0.0.0
+  __TEXT.__text: 0x12244
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x67c
+  __TEXT.__const: 0x800
+  __TEXT.__cstring: 0x1b63
   __TEXT.__ustring: 0x78
-  __TEXT.__oslogstring: 0x1670
+  __TEXT.__oslogstring: 0x182c
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methname: 0x1e8c
-  __TEXT.__objc_methtype: 0x161
-  __TEXT.__objc_stubs: 0x1e80
+  __TEXT.__objc_methname: 0x1f58
+  __TEXT.__objc_methtype: 0x16f
+  __TEXT.__objc_stubs: 0x1f40
   __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x908
+  __DATA_CONST.__objc_selrefs: 0x938
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x2300
+  __AUTH_CONST.__cfstring: 0x2380
   __AUTH_CONST.__objc_const: 0x950
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x48
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x28
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x178
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA0B078E-0865-38AC-9B68-443F9B8A3936
-  Functions: 337
-  Symbols:   1290
-  CStrings:  1054
+  UUID: B975447E-72B1-3B9D-8A15-EBFD3DFDDDF8
+  Functions: 345
+  Symbols:   1321
+  CStrings:  1079
 
Symbols:
+ -[SFDeviceRegulatoryAttributes _resolveDeviceAttributes:].cold.2
+ -[SFDeviceRegulatoryAttributes _resolveOTARegulatoryCatalog:]
+ -[SFDeviceRegulatoryAttributes _resolveOTARegulatoryCatalog:].cold.1
+ -[SFDeviceRegulatoryAttributes _resolveOTARegulatoryCatalog:].cold.2
+ -[SFDeviceRegulatoryAttributes _resolveOTARegulatoryCatalog:].cold.3
+ -[SFDeviceRegulatoryAttributes _resolveOTARegulatoryCatalog:].cold.4
+ -[SFDeviceRegulatoryAttributes _unarchiveRegulatoryCatalogBundleAtPath:toURL:]
+ _AAArchiveStreamClose
+ _AAArchiveStreamProcess
+ _AAByteStreamClose
+ _AADecodeArchiveInputStreamOpen
+ _AADecompressionInputStreamOpen
+ _AAExtractArchiveOutputStreamOpen
+ _AAFileStreamOpenWithPath
+ _OUTLINED_FUNCTION_4
+ __SFBuiltInRegulatoryImage.styleSensitiveImage.389
+ ___block_literal_global.124
+ ___block_literal_global.130
+ _objc_msgSend$_resolveOTARegulatoryCatalog:
+ _objc_msgSend$_unarchiveRegulatoryCatalogBundleAtPath:toURL:
+ _objc_msgSend$absoluteString
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$writeToURL:options:error:
- __SFBuiltInRegulatoryImage.styleSensitiveImage.372
- ___block_literal_global.110
- ___block_literal_global.113
- ___block_literal_global.116
CStrings:
+ "%{Public}s: Empty regulatoryCatalog: '%@'"
+ "%{Public}s: Found regulatory image in Regulatory Catalog OTA path"
+ "%{Public}s: Image is null when looking into .car"
+ "%{Public}s: Regulatory Catalog data is empty"
+ "%{Public}s: There was an error writing bundle to %{public}@"
+ "%{Public}s: Wrote aar  to %{public}@"
+ "%{Public}s: Wrote bundle  %{public}@"
+ "%{public}s: There was an error writing the regulatory catalog to aar %{public}@"
+ "-[SFDeviceRegulatoryAttributes _resolveOTARegulatoryCatalog:]"
+ "B32@0:8@16@24"
+ "Extracted %ld entries to %@"
+ "RegulatoryCatalog"
+ "RegulatoryCatalog-%@.aar"
+ "RegulatoryCatalog-%@.bundle"
+ "RegulatoryModelNumber"
+ "_resolveOTARegulatoryCatalog:"
+ "_unarchiveRegulatoryCatalogBundleAtPath:toURL:"
+ "absoluteString"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "temporaryDirectory"
+ "writeToURL:options:error:"

```
