## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-3.26.2.3.0
-  __TEXT.__text: 0x24c38
+3.26.3.6.0
+  __TEXT.__text: 0x24f5c
   __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x2d54
+  __TEXT.__objc_methlist: 0x2d9c
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x61c
-  __TEXT.__cstring: 0x2c8f
+  __TEXT.__cstring: 0x2d07
   __TEXT.__ustring: 0x46
-  __TEXT.__unwind_info: 0xc5c
-  __TEXT.__objc_classname: 0xa02
-  __TEXT.__objc_methname: 0xa75c
+  __TEXT.__unwind_info: 0xc64
+  __TEXT.__objc_classname: 0xa1b
+  __TEXT.__objc_methname: 0xa8e0
   __TEXT.__objc_methtype: 0x1eea
-  __TEXT.__objc_stubs: 0x7420
-  __DATA_CONST.__got: 0x290
+  __TEXT.__objc_stubs: 0x7560
+  __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x59d8
-  __DATA_CONST.__objc_selrefs: 0x2308
+  __DATA_CONST.__objc_const: 0x5a50
+  __DATA_CONST.__objc_selrefs: 0x2358
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__objc_const: 0x1408
-  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__objc_const: 0x1450
+  __AUTH_CONST.__cfstring: 0x24a0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x488
-  __AUTH.__objc_data: 0xfa0
+  __AUTH.__objc_data: 0xff0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x458
+  __DATA.__objc_classrefs: 0x468
   __DATA.__objc_superrefs: 0x140
-  __DATA.__objc_ivar: 0x2dc
+  __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0xae0
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1095
-  Symbols:   4371
-  CStrings:  2269
+  Functions: 1100
+  Symbols:   4399
+  CStrings:  2285
 
Symbols:
+ +[MCUISettingsWatchManager _isWatchYorktownEnrolled:]
+ +[MCUISettingsWatchManager hasAnyYorktownEnrolledWatches]
+ -[MCInstallProfileViewController _removeProfileWithIdentifier:isProtectedProfile:completionHandler:]
+ -[MCRemoveProfileViewController _hasYorktownWatch]
+ -[MCRemoveProfileViewController cachedHasYorktownWatch]
+ -[MCRemoveProfileViewController setCachedHasYorktownWatch:]
+ _NRDevicePropertyMDMManagementState
+ _OBJC_CLASS_$_MCUISettingsWatchManager
+ _OBJC_CLASS_$_NRPairedDeviceRegistry
+ _OBJC_IVAR_$_MCRemoveProfileViewController._cachedHasYorktownWatch
+ _OBJC_METACLASS_$_MCUISettingsWatchManager
+ __OBJC_$_CLASS_METHODS_MCUISettingsWatchManager
+ __OBJC_CLASS_RO_$_MCUISettingsWatchManager
+ __OBJC_METACLASS_RO_$_MCUISettingsWatchManager
+ ___100-[MCInstallProfileViewController _removeProfileWithIdentifier:isProtectedProfile:completionHandler:]_block_invoke
+ ___100-[MCInstallProfileViewController _removeProfileWithIdentifier:isProtectedProfile:completionHandler:]_block_invoke_2
+ _objc_msgSend$_hasYorktownWatch
+ _objc_msgSend$_isWatchYorktownEnrolled:
+ _objc_msgSend$_removeProfileWithIdentifier:isProtectedProfile:completionHandler:
+ _objc_msgSend$cachedHasYorktownWatch
+ _objc_msgSend$getAllDevicesWithArchivedDevicesMatching:
+ _objc_msgSend$hasAnyYorktownEnrolledWatches
+ _objc_msgSend$removeProtectedProfileAsyncWithIdentifier:installationType:completion:
+ _objc_msgSend$setCachedHasYorktownWatch:
+ _objc_msgSend$setupCompletedDevicesSelectorBlock
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$valueForProperty:
- -[MCInstallProfileViewController _removeProfileWithIdentifier:completionHandler:]
- ___81-[MCInstallProfileViewController _removeProfileWithIdentifier:completionHandler:]_block_invoke
- ___81-[MCInstallProfileViewController _removeProfileWithIdentifier:completionHandler:]_block_invoke_2
- _objc_msgSend$_removeProfileWithIdentifier:completionHandler:
CStrings:
+ "%@ %@"
+ "MCUISettingsWatchManager"
+ "MOBILE_DEVICE_MANAGEMENT_REMOVE_WARNING_YORKTOWN_ADDITIONAL"
+ "MOBILE_DEVICE_MANAGEMENT_REMOVE_WARNING_YORKTOWN_FULL"
+ "TQ,N,V_cachedHasYorktownWatch"
+ "_cachedHasYorktownWatch"
+ "_hasYorktownWatch"
+ "_isWatchYorktownEnrolled:"
+ "_removeProfileWithIdentifier:isProtectedProfile:completionHandler:"
+ "cachedHasYorktownWatch"
+ "getAllDevicesWithArchivedDevicesMatching:"
+ "hasAnyYorktownEnrolledWatches"
+ "removeProtectedProfileAsyncWithIdentifier:installationType:completion:"
+ "setCachedHasYorktownWatch:"
+ "setupCompletedDevicesSelectorBlock"
+ "unsignedIntegerValue"
+ "valueForProperty:"
- "_removeProfileWithIdentifier:completionHandler:"

```
