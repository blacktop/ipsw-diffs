## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

```diff

-1513.0.8.0.2
-  __TEXT.__text: 0x22418
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x1104
+1513.0.19.502.1
+  __TEXT.__text: 0x228a0
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x11bc
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x4cb2
+  __TEXT.__cstring: 0x4d21
   __TEXT.__gcc_except_tab: 0xb04
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0xb30
-  __TEXT.__objc_classname: 0x166
-  __TEXT.__objc_methname: 0x3fe6
-  __TEXT.__objc_methtype: 0x127c
-  __TEXT.__objc_stubs: 0x2a80
-  __DATA_CONST.__got: 0x1b8
+  __TEXT.__unwind_info: 0xb38
+  __TEXT.__objc_classname: 0x17d
+  __TEXT.__objc_methname: 0x40e7
+  __TEXT.__objc_methtype: 0x12bd
+  __TEXT.__objc_stubs: 0x2b20
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x958
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc78
+  __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2880
-  __AUTH_CONST.__objc_const: 0x1660
+  __AUTH_CONST.__cfstring: 0x2940
+  __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0xf8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0x240
   __DATA.__bss: 0x60
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82527B2E-C3B2-355A-B078-D3DFAD4E9744
-  Functions: 720
-  Symbols:   2240
-  CStrings:  1504
+  UUID: D34825A3-A3D7-3D34-B711-ED3B526CF83E
+  Functions: 731
+  Symbols:   2289
+  CStrings:  1530
 
Symbols:
+ +[MIStagedUpdateMetadata supportsSecureCoding]
+ -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:]
+ -[MIPlaceholderConstructor _minimumOSVersionIsHigherThanSixWithError:]
+ -[MIStagedUpdateMetadata .cxx_destruct]
+ -[MIStagedUpdateMetadata copyWithZone:]
+ -[MIStagedUpdateMetadata description]
+ -[MIStagedUpdateMetadata encodeWithCoder:]
+ -[MIStagedUpdateMetadata initForStagedIdentifier:diskUsage:]
+ -[MIStagedUpdateMetadata initWithCoder:]
+ -[MIStagedUpdateMetadata isEqual:]
+ -[MIStagedUpdateMetadata setStagedDiskUsage:]
+ -[MIStagedUpdateMetadata setStagedIdentifier:]
+ -[MIStagedUpdateMetadata stagedDiskUsage]
+ -[MIStagedUpdateMetadata stagedIdentifier]
+ GCC_except_table22
+ GCC_except_table276
+ GCC_except_table283
+ GCC_except_table291
+ GCC_except_table297
+ GCC_except_table305
+ GCC_except_table312
+ GCC_except_table316
+ GCC_except_table333
+ GCC_except_table348
+ GCC_except_table355
+ GCC_except_table361
+ GCC_except_table365
+ GCC_except_table375
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table399
+ _MIBundleHasMinimumOSApplicableToProductVersion
+ _MIBundleSupportedArchitecturesForPlaceholderInfoPlist
+ _MIExtensionPointIsWatchKitForInfoPlist
+ _MIMinimumOSVersionForBundleInfoPlist
+ _MobileInstallationInstallApp
+ _MobileInstallationStageApplicationUpdate
+ _OBJC_CLASS_$_MIStagedUpdateMetadata
+ _OBJC_IVAR_$_MIStagedUpdateMetadata._stagedDiskUsage
+ _OBJC_IVAR_$_MIStagedUpdateMetadata._stagedIdentifier
+ _OBJC_METACLASS_$_MIStagedUpdateMetadata
+ __OBJC_$_CLASS_METHODS_MIStagedUpdateMetadata
+ __OBJC_$_CLASS_PROP_LIST_MIStagedUpdateMetadata
+ __OBJC_$_INSTANCE_METHODS_MIStagedUpdateMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MIStagedUpdateMetadata
+ __OBJC_$_PROP_LIST_MIStagedUpdateMetadata
+ __OBJC_CLASS_PROTOCOLS_$_MIStagedUpdateMetadata
+ __OBJC_CLASS_RO_$_MIStagedUpdateMetadata
+ __OBJC_METACLASS_RO_$_MIStagedUpdateMetadata
+ ___MobileInstallationInstallApp_block_invoke
+ ___MobileInstallationInstallApp_block_invoke_2
+ ___MobileInstallationInstallApp_block_invoke_3
+ ___MobileInstallationInstallApp_block_invoke_4
+ ___MobileInstallationInstallApp_block_invoke_5
+ ___MobileInstallationStageApplicationUpdate_block_invoke
+ ___block_descriptor_48_e8_32r40r_e44_v24?0"MIStagedUpdateMetadata"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e44_v24?0"MIStagedUpdateMetadata"8"NSError"16ls32l8s40l8
+ _objc_msgSend$_minimumOSVersionIsHigherThanSixWithError:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$setStagedDiskUsage:
+ _objc_msgSend$setStagedIdentifier:
+ _objc_msgSend$stagedDiskUsage
+ _objc_msgSend$stagedIdentifier
- -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:onBehalfOf:error:]
- GCC_except_table278
- GCC_except_table287
- GCC_except_table293
- GCC_except_table303
- GCC_except_table307
- GCC_except_table314
- GCC_except_table332
- GCC_except_table347
- GCC_except_table350
- GCC_except_table357
- GCC_except_table363
- GCC_except_table373
- GCC_except_table381
- GCC_except_table385
- GCC_except_table390
- GCC_except_table413
- _MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError
- _MobileInstallationInstallApplicationWithIdentityWithError
- _MobileInstallationInstallForInstallCoordinationWithError
- _MobileInstallationStageApplicationUpdateWithIdentityWithError
- ___MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke
- ___MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke_2
- ___MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke_3
- ___MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke_4
- ___MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError_block_invoke_5
- ___MobileInstallationStageApplicationUpdateWithIdentityWithError_block_invoke
- ___block_descriptor_48_e8_32r40r_e30_v24?0"NSString"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
- _kMIInstallResultInstalledAppInfoArrayKey
- _objc_autorelease
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
CStrings:
+ "-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:]"
+ "-[MIStagedUpdateMetadata isEqual:]"
+ "6.0"
+ "@32@0:8@16Q24"
+ "@96@0:8@16@24@32@40@48{?=[8I]}56^@88"
+ "CF_MIPlaceholderConstructorVersion"
+ "MIPlaceholderArchitectures"
+ "MIStagedUpdateMetadata"
+ "MobileInstallationInstallApp"
+ "MobileInstallationStageApplicationUpdate"
+ "T@\"NSString\",C,N,V_stagedIdentifier"
+ "TQ,N,V_stagedDiskUsage"
+ "[%@/%llu]"
+ "_minimumOSVersionIsHigherThanSixWithError:"
+ "_stagedDiskUsage"
+ "_stagedIdentifier"
+ "createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:"
+ "initForStagedIdentifier:diskUsage:"
+ "numberWithUnsignedLongLong:"
+ "setStagedDiskUsage:"
+ "setStagedIdentifier:"
+ "stagedDiskUsage"
+ "stagedIdentifier"
+ "v24@?0@\"MIStagedUpdateMetadata\"8@\"NSError\"16"
+ "v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"MIStagedUpdateMetadata\"@\"NSError\">48"
- "-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:onBehalfOf:error:]"
- "MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError"
- "MobileInstallationStageApplicationUpdateWithIdentityWithError"
- "createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:onBehalfOf:error:"
- "dictionaryWithObjects:forKeys:count:"
- "v24@?0@\"NSString\"8@\"NSError\"16"
- "v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"NSString\"@\"NSError\">48"

```
