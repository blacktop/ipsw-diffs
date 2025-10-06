## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1270.40.12.0.0
-  __TEXT.__text: 0x92b9c
+1270.60.4.0.0
+  __TEXT.__text: 0x92a44
   __TEXT.__auth_stubs: 0x1300
-  __TEXT.__objc_methlist: 0x4088
+  __TEXT.__objc_methlist: 0x40a0
   __TEXT.__const: 0xdf70
   __TEXT.__gcc_except_tab: 0x924
-  __TEXT.__cstring: 0x14b92
+  __TEXT.__cstring: 0x14aaa
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__unwind_info: 0x11a4
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x55e
-  __TEXT.__objc_methname: 0xc3b7
-  __TEXT.__objc_methtype: 0x1631
-  __TEXT.__objc_stubs: 0x7a40
+  __TEXT.__objc_methname: 0xc41b
+  __TEXT.__objc_methtype: 0x163f
+  __TEXT.__objc_stubs: 0x7a80
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x1190
   __DATA_CONST.__objc_classlist: 0x1c0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5d60
-  __DATA_CONST.__objc_selrefs: 0x2428
+  __DATA_CONST.__objc_selrefs: 0x2438
   __DATA_CONST.__objc_arraydata: 0x9a0
-  __AUTH_CONST.__cfstring: 0xb920
+  __AUTH_CONST.__cfstring: 0xb8e0
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x4a50
+  __AUTH_CONST.__const: 0x4ad0
   __AUTH_CONST.__objc_dictobj: 0x11a8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x90

   __DATA.__data: 0x10a8
   __DATA.__bss: 0x80
   __DATA.__common: 0x30
-  __DATA_DIRTY.__const: 0x280
+  __DATA_DIRTY.__const: 0x200
   __DATA_DIRTY.__objc_const: 0x1c88
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4B12F17-723B-3121-8B41-7767F01E76B8
-  Functions: 1721
-  Symbols:   6002
-  CStrings:  5520
+  UUID: 479B839C-1A01-3B69-B9AD-254D55F18284
+  Functions: 1723
+  Symbols:   6008
+  CStrings:  5518
 
Symbols:
+ -[MIBundle _filterExtensionBundles:forValidationFlags:]
+ -[MIBundle driverKitBundlesPerformingPlatformValidation:withError:]
+ ___67-[MIBundle driverKitBundlesPerformingPlatformValidation:withError:]_block_invoke
+ ___block_literal_global.187
+ ___block_literal_global.326
+ ___block_literal_global.372
+ ___block_literal_global.377
+ __unnamed_array_storage.363
+ __unnamed_array_storage.416
+ __unnamed_array_storage.417
+ __unnamed_array_storage.453
+ __unnamed_array_storage.454
+ __unnamed_array_storage.478
+ __unnamed_array_storage.479
+ __unnamed_array_storage.489
+ _objc_msgSend$_filterExtensionBundles:forValidationFlags:
+ _objc_msgSend$driverKitBundlesPerformingPlatformValidation:withError:
- ___47-[MIBundle driverKitExtensionBundlesWithError:]_block_invoke
- ___block_literal_global.177
- ___block_literal_global.332
- ___block_literal_global.378
- ___block_literal_global.383
- __unnamed_array_storage.369
- __unnamed_array_storage.428
- __unnamed_array_storage.429
- __unnamed_array_storage.465
- __unnamed_array_storage.466
- __unnamed_array_storage.490
- __unnamed_array_storage.491
- __unnamed_array_storage.500
- __unnamed_array_storage.501
CStrings:
+ "-[MIAppIdentity _eligiblePersonaForBundle:error:]"
+ "-[MIBundle _filterExtensionBundles:forValidationFlags:]"
+ "@28@0:8@16C24"
+ "Failed to find executable bundle in container %@. Relying on UM instead of module specific logic for persona resolution."
+ "Failed to set unique install ID on DriverKit extension %@"
+ "Ignoring %@ %@ because it is not applicable to this device's capabilities: %@"
+ "Ignoring %@ at %@ because it doesn't work on this OS version"
+ "_filterExtensionBundles:forValidationFlags:"
+ "driverKitBundlesPerformingPlatformValidation:withError:"
- "-[MIBundle driverKitExtensionBundlesWithError:]"
- "-[MIBundle extensionKitBundlesPerformingPlatformValidation:withError:]"
- "-[MIBundle pluginKitBundlesPerformingPlatformValidation:withError:]"
- "Ignoring DriverKit %@ because it is not applicable to this device's capabilities: %@"
- "Ignoring DriverKit bundle at %@ because it is not compatible with this OS version"
- "Ignoring extension %@ because it is not applicable to this device's capabilities: %@"
- "Ignoring extension at \"%@\" because it doesn't work on this OS version"
- "Ignoring plugin %@ because it is not applicable to this device's capabilities: %@"
- "Ignoring plugin at %@ because it doesn't work on this OS version"

```
