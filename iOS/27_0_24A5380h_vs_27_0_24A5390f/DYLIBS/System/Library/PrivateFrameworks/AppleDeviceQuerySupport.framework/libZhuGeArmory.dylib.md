## libZhuGeArmory.dylib

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-459.0.7.0.0
-  __TEXT.__text: 0x23f90
-  __TEXT.__objc_methlist: 0x834
+459.0.14.0.0
+  __TEXT.__text: 0x242c0
+  __TEXT.__objc_methlist: 0x84c
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0xaa01
+  __TEXT.__cstring: 0xab56
   __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__oslogstring: 0x233
-  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__unwind_info: 0x3f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x868
+  __DATA_CONST.__objc_selrefs: 0x888
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x818
   __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x8320
+  __AUTH_CONST.__cfstring: 0x83e0
   __AUTH_CONST.__objc_const: 0xe68
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x8a0
-  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_got: 0x518
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0xa20

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libVinylNonUpdater.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libCentauriUpdater.dylib
-  Functions: 350
-  Symbols:   958
-  CStrings:  1254
+  Functions: 352
+  Symbols:   964
+  CStrings:  1261
 
Symbols:
+ +[ZhuGeBasebandArmory isAppleBaseband]
+ +[ZhuGeBasebandArmory queryCHUnitSimMuxDualPhysicalStateWithError:]
+ GCC_except_table31
+ GCC_except_table35
+ _TelephonyRadiosGetRadioVendor
+ _objc_msgSend$isEuiccActiveWithError:
+ _objc_msgSend$supportsDynamicSIMConfigurationWithError:
+ _strtoimax
- GCC_except_table29
- GCC_except_table33
Functions:
+ +[ZhuGeBasebandArmory queryCHUnitSimMuxDualPhysicalStateWithError:]
+ +[ZhuGeBasebandArmory isAppleBaseband]
~ +[ZhuGeKeysActionArmory queryIOProperty:fromCriteria:withError:] : 8064 -> 8192
CStrings:
+ "\"%@\" is not a valid integer"
+ "+[ZhuGeBasebandArmory queryCHUnitSimMuxDualPhysicalStateWithError:]"
+ "Device does not support dynamic configuration"
+ "Failed to query isEuiccActive: %@"
+ "Failed to query supportsDynamicSIMConfiguration: %@"
+ "SIM_MUX verified: Device is in P+E configuration (expected P+P)"
+ "SIM_MUX verified: Device is in P+P configuration"
```
