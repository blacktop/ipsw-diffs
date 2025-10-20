## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

 921.40.62.0.0
-  __TEXT.__text: 0x85608
+  __TEXT.__text: 0x861f4
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x3ae4
+  __TEXT.__objc_methlist: 0x3b04
   __TEXT.__const: 0x7f8
   __TEXT.__oslogstring: 0x92d9
-  __TEXT.__cstring: 0x5ac7
+  __TEXT.__cstring: 0x5b0c
   __TEXT.__gcc_except_tab: 0x1758
-  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__unwind_info: 0x11d8
   __TEXT.__objc_classname: 0x806
-  __TEXT.__objc_methname: 0x8118
+  __TEXT.__objc_methname: 0x816e
   __TEXT.__objc_methtype: 0x154e
-  __TEXT.__objc_stubs: 0x6680
+  __TEXT.__objc_stubs: 0x66c0
   __DATA_CONST.__got: 0x560
   __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2050
+  __DATA_CONST.__objc_selrefs: 0x2060
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0xa88
+  __DATA_CONST.__objc_arraydata: 0xaa0
   __AUTH_CONST.__auth_got: 0xb48
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x72c0
+  __AUTH_CONST.__cfstring: 0x7360
   __AUTH_CONST.__objc_const: 0x5948
   __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_dictobj: 0x230

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: A0AEF135-BE78-3F9D-B103-4E702EFC4877
-  Functions: 2271
-  Symbols:   7506
-  CStrings:  4831
+  UUID: 8AA45541-172C-374E-A166-004D193CA6AF
+  Functions: 2275
+  Symbols:   7518
+  CStrings:  4843
 
Symbols:
+ -[CRComponentSigning wcrtSign:outSignature:outDeviceNonce:outError:]
+ -[CRFDRiPad1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRFDRiPad1DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:]
+ -[CRUtils getPathForBagdemagusFirmwareWithError:]
+ GCC_except_table36
+ GCC_except_table41
+ _CoreRepairFDRSignLAS
+ _objc_msgSend$getPathForBagdemagusFirmwareWithError:
+ _objc_msgSend$wcrtSign:outSignature:outDeviceNonce:outError:
- GCC_except_table29
- GCC_except_table35
- GCC_except_table40
- GCC_except_table9
CStrings:
+ "/usr/standalone/update/Bagdemagus/"
+ "Brunor"
+ "LAS"
+ "OPEN CLOSE SENSOR"
+ "getPathForBagdemagusFirmwareWithError:"
+ "wcrt"
+ "wcrtSign:outSignature:outDeviceNonce:outError:"

```
