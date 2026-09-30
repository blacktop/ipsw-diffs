## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-1378.40.7.0.0
-  __TEXT.__text: 0xa668
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_stubs: 0x18a0
+1378.60.20.502.1
+  __TEXT.__text: 0xa254
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_stubs: 0x1860
   __TEXT.__objc_methlist: 0x5c4
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x34c
-  __TEXT.__cstring: 0x349d
-  __TEXT.__objc_methname: 0x2478
+  __TEXT.__cstring: 0x3309
+  __TEXT.__objc_methname: 0x2453
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methtype: 0x568
   __TEXT.__oslogstring: 0x142
-  __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__auth_got: 0x460
+  __TEXT.__unwind_info: 0x258
+  __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x18c0
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__cfstring: 0x17e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0xe18
-  __DATA.__objc_selrefs: 0x748
+  __DATA.__objc_selrefs: 0x738
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 166
-  Symbols:   237
-  CStrings:  655
+  Functions: 163
+  Symbols:   231
+  CStrings:  645
 
Symbols:
- _MGCopyAnswer
- _MIIsCompatibleWithAtLeastOneDeviceFamily
- _MIIsCompatibleWithDeviceFamily
- _MI_GenerativePlaygroundBundleID
- _OBJC_CLASS_$_NSConstantDictionary
- _objc_opt_respondsToSelector
CStrings:
- "Array of supported device families returned from MobileGestalt was not an array of numbers; got: %!@(MISSING)"
- "Couldn't fetch list of supported device families."
- "DeviceFamilyNotSupported"
- "LegacyErrorString"
- "MIIsApplicableToCurrentDeviceFamilyWithError"
- "SupportedDeviceFamilies"
- "This app was not built to support this device family; app is compatible with %!@(MISSING) but this device supports %!@(MISSING)"
- "com.apple.GenerativePlaygroundApp"
- "setWithObject:"
- "skipDeviceFamilyCheck"

```
