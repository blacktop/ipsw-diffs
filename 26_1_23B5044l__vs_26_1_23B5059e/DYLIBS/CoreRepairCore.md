## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.40.47.0.0
-  __TEXT.__text: 0x84290
+921.40.58.0.0
+  __TEXT.__text: 0x85608
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x3a7c
+  __TEXT.__objc_methlist: 0x3ae4
   __TEXT.__const: 0x7f8
-  __TEXT.__oslogstring: 0x917f
-  __TEXT.__cstring: 0x5ab3
+  __TEXT.__oslogstring: 0x92d9
+  __TEXT.__cstring: 0x5ac7
   __TEXT.__gcc_except_tab: 0x1758
-  __TEXT.__unwind_info: 0x11c0
-  __TEXT.__objc_classname: 0x7f0
-  __TEXT.__objc_methname: 0x7f7d
-  __TEXT.__objc_methtype: 0x1538
-  __TEXT.__objc_stubs: 0x64e0
+  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__objc_classname: 0x806
+  __TEXT.__objc_methname: 0x8118
+  __TEXT.__objc_methtype: 0x154e
+  __TEXT.__objc_stubs: 0x6680
   __DATA_CONST.__got: 0x560
   __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe0
+  __DATA_CONST.__objc_selrefs: 0x2050
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0xa60
+  __DATA_CONST.__objc_arraydata: 0xa88
   __AUTH_CONST.__auth_got: 0xb48
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x7280
-  __AUTH_CONST.__objc_const: 0x58b8
-  __AUTH_CONST.__objc_arrayobj: 0x660
+  __AUTH_CONST.__cfstring: 0x72c0
+  __AUTH_CONST.__objc_const: 0x5948
+  __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0xe60
+  __AUTH.__objc_data: 0xeb0
   __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x690
   __DATA.__common: 0x30

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: E428B5BD-8B9A-38B9-96FF-FE18EC6A7B81
-  Functions: 2260
-  Symbols:   7466
-  CStrings:  4799
+  UUID: 24EEFC21-81E6-319D-806E-30F38158CA60
+  Functions: 2271
+  Symbols:   7506
+  CStrings:  4831
 
Symbols:
+ +[CRFDRUtils getSealedInstancesWithClass:error:]
+ +[CRFDRUtils getSealedInstancesWithClass:error:].cold.1
+ +[CRLocalization localizedStringWithKey:].cold.2
+ +[CRRepairStateSnapshot _deserializeRepairData:]
+ +[CRRepairStateSnapshot _determineHWChangeWithOldData:newRepairData:unsealedData:]
+ +[CRRepairStateSnapshot _getChangedDataFromRCHL]
+ +[CRRepairStateSnapshot _getCurrentUnsealedData]
+ +[CRRepairStateSnapshot _getMergedRepairDataWithRCHL:unsealedData:]
+ +[CRRepairStateSnapshot _serializeRepairData:]
+ +[CRRepairStateSnapshot _serializeRepairData:].cold.1
+ +[CRRepairStateSnapshot isHardwareChangedFromOldState:newState:options:error:]
+ _OBJC_CLASS_$_CRRepairStateSnapshot
+ _OBJC_METACLASS_$_CRRepairStateSnapshot
+ __OBJC_$_CLASS_METHODS_CRRepairStateSnapshot
+ __OBJC_CLASS_RO_$_CRRepairStateSnapshot
+ __OBJC_METACLASS_RO_$_CRRepairStateSnapshot
+ _objc_msgSend$_deserializeRepairData:
+ _objc_msgSend$_determineHWChangeWithOldData:newRepairData:unsealedData:
+ _objc_msgSend$_getChangedDataFromRCHL
+ _objc_msgSend$_getCurrentUnsealedData
+ _objc_msgSend$_getMergedRepairDataWithRCHL:unsealedData:
+ _objc_msgSend$_serializeRepairData:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$getSealedInstancesWithClass:error:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$sortedArrayUsingSelector:
CStrings:
+ ";"
+ "B48@0:8@16^@24@32^@40"
+ "CRRepairStateSnapshot"
+ "Data %@ changed after MLB is sealed. old: %@. new: %@."
+ "HW changed: %d"
+ "Key %@ has repaired instances: %@"
+ "Key is not string"
+ "Loc bundle not found"
+ "MLB is sealed"
+ "New repair snapshot: %@"
+ "No merged repair data"
+ "Not a value of array of %@"
+ "Old repair snapshot: %@"
+ "PART_FRONT_CAMERA"
+ "Unsupported element type in array for key '%@': %@"
+ "_deserializeRepairData:"
+ "_determineHWChangeWithOldData:newRepairData:unsealedData:"
+ "_getChangedDataFromRCHL"
+ "_getCurrentUnsealedData"
+ "_getMergedRepairDataWithRCHL:unsealedData:"
+ "_serializeRepairData:"
+ "arrayWithCapacity:"
+ "componentsJoinedByString:"
+ "failed to get sealed instances of %@: %@"
+ "getSealedInstancesWithClass:error:"
+ "isEqualToArray:"
+ "isEqualToDictionary:"
+ "isHardwareChangedFromOldState:newState:options:error:"
+ "sortUsingSelector:"
+ "sortedArrayUsingSelector:"

```
