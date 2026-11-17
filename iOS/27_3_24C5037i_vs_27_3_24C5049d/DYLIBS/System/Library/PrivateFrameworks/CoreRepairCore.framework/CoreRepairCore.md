## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-1307.60.20.0.0
-  __TEXT.__text: 0x9b82c
-  __TEXT.__objc_methlist: 0x50dc
-  __TEXT.__const: 0x880
-  __TEXT.__cstring: 0x812c
-  __TEXT.__oslogstring: 0xa7a5
+1307.60.23.0.0
+  __TEXT.__text: 0x9c480
+  __TEXT.__objc_methlist: 0x512c
+  __TEXT.__const: 0x888
+  __TEXT.__cstring: 0x8193
+  __TEXT.__oslogstring: 0xa99f
   __TEXT.__gcc_except_tab: 0x1afc
-  __TEXT.__unwind_info: 0x25c8
+  __TEXT.__unwind_info: 0x2608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe68
-  __DATA_CONST.__objc_classlist: 0x3d8
+  __DATA_CONST.__const: 0xf58
+  __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2968
+  __DATA_CONST.__objc_selrefs: 0x2998
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0xee8
-  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__got: 0x738
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x97e0
-  __AUTH_CONST.__objc_const: 0x7858
+  __AUTH_CONST.__cfstring: 0x98a0
+  __AUTH_CONST.__objc_const: 0x78f0
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0xb58
-  __AUTH_CONST.__auth_got: 0xbe8
-  __AUTH.__objc_data: 0x1720
+  __AUTH_CONST.__auth_got: 0xbf8
+  __AUTH.__objc_data: 0x1770
   __DATA.__objc_ivar: 0x3b4
   __DATA.__data: 0x6b8
   __DATA.__common: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 2832
-  Symbols:   709
-  CStrings:  2673
+  Functions: 2851
+  Symbols:   714
+  CStrings:  2686
 
Symbols:
+ _CRShipModeDDMStateWireValue
+ _OBJC_CLASS_$_CRShipModeDDMStatus
+ _OBJC_METACLASS_$_CRShipModeDDMStatus
+ _objc_retain_x10
+ _objc_retain_x7
CStrings:
+ "CRShipModeBatteryClient: fetch ship-mode undo-in-progress plumbing failure: %s"
+ "CRShipModeDDMStatus: fetchShipModeResumeState failed (attempt %lu/%lu): %{public}s"
+ "CRShipModeDDMStatus: fetchShipModeUndoInProgress failed (attempt %lu/%lu): %{public}s"
+ "CRShipModeDDMStatus: no ship-charge-limit state (0x%08x); ship mode not applicable"
+ "CRShipModeDDMStatus: reporting state=%{public}@"
+ "CRShipModeDDMStatus: shipped=%d chainInFlight=%d chainFailed=%d cannotShip=%d undoInProgress=%d → reporting state=%{public}@"
+ "Unable to get ClaimDataClasses"
+ "normal"
+ "notApplicable"
+ "preparing"
+ "reverting"
+ "shippable"
+ "v20@?0B8@\"NSError\"12"
```
