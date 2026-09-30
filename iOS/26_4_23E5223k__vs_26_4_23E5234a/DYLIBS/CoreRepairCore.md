## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

 921.100.266.0.0
-  __TEXT.__text: 0x8e23c
+  __TEXT.__text: 0x8ee68
   __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x3eb4
-  __TEXT.__const: 0x828
-  __TEXT.__oslogstring: 0x97ac
-  __TEXT.__cstring: 0x600f
+  __TEXT.__objc_methlist: 0x3ecc
+  __TEXT.__const: 0x848
+  __TEXT.__oslogstring: 0x9810
+  __TEXT.__cstring: 0x60d2
   __TEXT.__gcc_except_tab: 0x183c
-  __TEXT.__unwind_info: 0x15e8
+  __TEXT.__unwind_info: 0x15f8
   __TEXT.__objc_classname: 0x8af
-  __TEXT.__objc_methname: 0x8721
+  __TEXT.__objc_methname: 0x878f
   __TEXT.__objc_methtype: 0x15fb
-  __TEXT.__objc_stubs: 0x6c20
+  __TEXT.__objc_stubs: 0x6c80
   __DATA_CONST.__got: 0x598
   __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2220
+  __DATA_CONST.__objc_selrefs: 0x2238
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x218
-  __DATA_CONST.__objc_arraydata: 0xb70
+  __DATA_CONST.__objc_arraydata: 0xba8
   __AUTH_CONST.__auth_got: 0xb40
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x78a0
+  __AUTH_CONST.__cfstring: 0x7a00
   __AUTH_CONST.__objc_const: 0x6020
-  __AUTH_CONST.__objc_arrayobj: 0x7b0
+  __AUTH_CONST.__objc_arrayobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH.__objc_data: 0x1130

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: A0C0E5D5-E255-334A-BDEB-B8DF37CE9939
-  Functions: 2397
-  Symbols:   8210
-  CStrings:  5056
+  UUID: EC4E4629-D509-39B0-BD78-82917A52F79F
+  Functions: 2402
+  Symbols:   8223
+  CStrings:  5084
 
Symbols:
+ -[CRFDRDisplay2DeviceHandler _addMultiHmCAToMutableArrayWithPartSPC:dataClasses:dataInstances:error:]
+ -[CRFDRDisplay2DeviceHandler _addMultiHmCAToMutableArrayWithPartSPC:dataClasses:dataInstances:error:].cold.1
+ -[CRFDRDisplay2DeviceHandler _addMultiHmCAToMutableArrayWithPartSPC:dataClasses:dataInstances:error:].cold.2
+ -[CRFDRDisplay2DeviceHandler _hasMultiHmCA]
+ _objc_msgSend$_addMultiHmCAToMutableArrayWithPartSPC:dataClasses:dataInstances:error:
+ _objc_msgSend$_hasMultiHmCA
+ _objc_msgSend$removeObjectsAtIndexes:
CStrings:
+ "%d %d %d %d %d %d %d"
+ "%lu %@ to seal"
+ "%lu sealed %@"
+ "BATTERY"
+ "DpC3"
+ "ENCLOSURE"
+ "Failed to get multi instances of HmCA"
+ "Failed to get sealed %@ instances"
+ "Invalid SPCs"
+ "Missing front ALS instance"
+ "Missing live instance for front ALS: %@"
+ "Missing live instance for rear ALS: %@"
+ "Missing rear ALS instance"
+ "_addMultiHmCAToMutableArrayWithPartSPC:dataClasses:dataInstances:error:"
+ "_hasMultiHmCA"
+ "iCCl"
+ "removeObjectsAtIndexes:"

```
