## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

 921.60.26.0.0
-  __TEXT.__text: 0x8844c
+  __TEXT.__text: 0x88f84
   __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_methlist: 0x3be4
+  __TEXT.__objc_methlist: 0x3c54
   __TEXT.__const: 0x7f8
-  __TEXT.__oslogstring: 0x9504
-  __TEXT.__cstring: 0x5b96
+  __TEXT.__oslogstring: 0x9563
+  __TEXT.__cstring: 0x5c0d
   __TEXT.__gcc_except_tab: 0x1758
-  __TEXT.__unwind_info: 0x1210
-  __TEXT.__objc_classname: 0x821
-  __TEXT.__objc_methname: 0x81fb
+  __TEXT.__unwind_info: 0x1220
+  __TEXT.__objc_classname: 0x83a
+  __TEXT.__objc_methname: 0x8210
   __TEXT.__objc_methtype: 0x154e
-  __TEXT.__objc_stubs: 0x6780
+  __TEXT.__objc_stubs: 0x67a0
   __DATA_CONST.__got: 0x568
   __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2090
+  __DATA_CONST.__objc_selrefs: 0x2098
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0xb10
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0xb38
   __AUTH_CONST.__auth_got: 0xb58
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x73c0
-  __AUTH_CONST.__objc_const: 0x5a50
-  __AUTH_CONST.__objc_arrayobj: 0x738
+  __AUTH_CONST.__cfstring: 0x74c0
+  __AUTH_CONST.__objc_const: 0x5ae0
+  __AUTH_CONST.__objc_arrayobj: 0x750
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0xf00
+  __AUTH.__objc_data: 0xf50
   __DATA.__objc_ivar: 0x2f0
   __DATA.__data: 0x690
   __DATA.__common: 0x30

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 5248DC17-7D9E-3292-B19D-A47E831DD0A3
-  Functions: 2302
-  Symbols:   7603
-  CStrings:  4871
+  UUID: 17152976-1EA1-3F12-85E7-463E5664641F
+  Functions: 2313
+  Symbols:   7632
+  CStrings:  4892
 
Symbols:
+ +[CRFDRWatch1DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRWatch1DeviceHandler isWatch1ProductType:]
+ -[CRFDRWatch1DeviceHandler copyWithZone:]
+ -[CRFDRWatch1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRWatch1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRWatch1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRWatch1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRWatch1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRWatch1DeviceHandler init]
+ -[CRFDRWatch1DeviceHandler performPostSealingStage:]
+ -[CRFDRWatch1DeviceHandler supportPatch]
+ _OBJC_CLASS_$_CRFDRWatch1DeviceHandler
+ _OBJC_METACLASS_$_CRFDRWatch1DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRWatch1DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRWatch1DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRWatch1DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRWatch1DeviceHandler
+ _objc_msgSend$isWatch1ProductType:
CStrings:
+ "ALCl"
+ "CRFDRWatch1DeviceHandler"
+ "Clearing SAGE calibration data"
+ "DPCl"
+ "SAGE data clearing unsuccessful, status: %@"
+ "SDCl"
+ "TPCl"
+ "WATCH COMP BATTERY"
+ "WATCH COMP DISPLAY"
+ "display-vsh-comp"
+ "isWatch1ProductType:"
+ "performPostSealingStage, class: %@"

```
