## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.40.63.0.0
-  __TEXT.__text: 0x201f4
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x74c
+1837.40.71.0.0
+  __TEXT.__text: 0x21814
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_methlist: 0x80c
   __TEXT.__const: 0x530
-  __TEXT.__cstring: 0x7643
-  __TEXT.__oslogstring: 0x31ce
-  __TEXT.__gcc_except_tab: 0xb4c
-  __TEXT.__unwind_info: 0x568
-  __TEXT.__objc_classname: 0x106
-  __TEXT.__objc_methname: 0x1c7c
-  __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__objc_stubs: 0x1fa0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xea8
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__cstring: 0x78d0
+  __TEXT.__oslogstring: 0x326c
+  __TEXT.__gcc_except_tab: 0xb88
+  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__objc_classname: 0x11e
+  __TEXT.__objc_methname: 0x1eb9
+  __TEXT.__objc_methtype: 0x503
+  __TEXT.__objc_stubs: 0x2100
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0xf50
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x918
+  __DATA_CONST.__objc_selrefs: 0x9a0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x668
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x7fe0
-  __AUTH_CONST.__objc_const: 0x840
-  __AUTH_CONST.__objc_intobj: 0x8a0
+  __AUTH_CONST.__auth_got: 0x680
+  __AUTH_CONST.__const: 0x530
+  __AUTH_CONST.__cfstring: 0x8220
+  __AUTH_CONST.__objc_const: 0x9d0
+  __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x34
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x238
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB88236C-C8D9-31DF-AAA0-5B0C894674C0
-  Functions: 448
-  Symbols:   1566
-  CStrings:  2710
+  UUID: 5B861667-8B88-3721-9F26-948B823E8F0F
+  Functions: 478
+  Symbols:   1669
+  CStrings:  2777
 
Symbols:
+ +[MAAssetTypeDescriptor _assetTypeDescriptors]
+ +[MAAssetTypeDescriptor _assetTypeDescriptors].cold.1
+ +[MAAssetTypeDescriptor _loadDescriptorsFromPath:intoDictionary:]
+ +[MAAssetTypeDescriptor _secureAssetTypeDescriptors]
+ +[MAAssetTypeDescriptor _secureAssetTypeDescriptors].cold.1
+ +[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]
+ +[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]
+ +[MAAssetTypeDescriptor descriptorForAssetType:]
+ +[MAAssetTypeDescriptor typeDescriptorsToDataVault]
+ +[MAAssetTypeDescriptor typeDescriptorsToRemoveV1Assets]
+ -[MAAssetTypeDescriptor .cxx_destruct]
+ -[MAAssetTypeDescriptor assetProperties]
+ -[MAAssetTypeDescriptor assetSpecifiers]
+ -[MAAssetTypeDescriptor assetType]
+ -[MAAssetTypeDescriptor description]
+ -[MAAssetTypeDescriptor initWithAssetType:]
+ -[MAAssetTypeDescriptor isSecure]
+ -[MAAssetTypeDescriptor shouldMakeDataVault]
+ -[MAAssetTypeDescriptor shouldRemoveV1Assets]
+ -[SecureMobileAssetBundle bundleAccessPermitted:]
+ -[SecureMobileAssetBundle typeDescriptor]
+ GCC_except_table118
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table97
+ _MAAssetTypeDescriptorKeyAssetSpecifiers
+ _MAAssetTypeDescriptorKeyAssetType
+ _MAAssetTypeDescriptorKeyMakeDataVault
+ _MAAssetTypeDescriptorKeyMobileAssetProperties
+ _MAAssetTypeDescriptorKeyRemoveV1Assets
+ _NSURLIsRegularFileKey
+ _OBJC_CLASS_$_MAAssetTypeDescriptor
+ _OBJC_CLASS_$_SUCoreDevice
+ _OBJC_IVAR_$_MAAssetTypeDescriptor._assetType
+ _OBJC_IVAR_$_MAAssetTypeDescriptor._isSecure
+ _OBJC_IVAR_$_MAAssetTypeDescriptor._typeDescriptor
+ _OBJC_IVAR_$_SecureMobileAssetBundle._typeDescriptor
+ _OBJC_METACLASS_$_MAAssetTypeDescriptor
+ __OBJC_$_CLASS_METHODS_MAAssetTypeDescriptor
+ __OBJC_$_INSTANCE_METHODS_MAAssetTypeDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MAAssetTypeDescriptor
+ __OBJC_$_PROP_LIST_MAAssetTypeDescriptor
+ __OBJC_CLASS_RO_$_MAAssetTypeDescriptor
+ __OBJC_METACLASS_RO_$_MAAssetTypeDescriptor
+ ___46+[MAAssetTypeDescriptor _assetTypeDescriptors]_block_invoke
+ ___52+[MAAssetTypeDescriptor _secureAssetTypeDescriptors]_block_invoke
+ ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke
+ ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke_2
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1261
+ ___79+[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e29_v32?08"NSDictionary"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_literal_global.1116
+ ___block_literal_global.1122
+ ___block_literal_global.1139
+ ___block_literal_global.1160
+ ___block_literal_global.1166
+ ___block_literal_global.1171
+ ___block_literal_global.1176
+ ___block_literal_global.1181
+ ___block_literal_global.1186
+ ___block_literal_global.1205
+ ___block_literal_global.1246
+ ___block_literal_global.1256
+ ___block_literal_global.1298
+ ___block_literal_global.1372
+ ___block_literal_global.1377
+ ___block_literal_global.1379
+ ___block_literal_global.1423
+ ___block_literal_global.1429
+ ___block_literal_global.1434
+ ___block_literal_global.1445
+ ___block_literal_global.1450
+ ___block_literal_global.1472
+ ___block_literal_global.1723
+ ___block_literal_global.2300
+ ___block_literal_global.2813
+ ___block_literal_global.2815
+ ___block_literal_global.2817
+ ___block_literal_global.2819
+ ___block_literal_global.2821
+ ___block_literal_global.2860
+ ___block_literal_global.2864
+ __assetTypeDescriptors.assetTypeDescriptors
+ __assetTypeDescriptors.onceToken
+ __secureAssetTypeDescriptors.onceToken
+ __secureAssetTypeDescriptors.secureAssetTypeDescriptors
+ _deviceOSBuildVersion
+ _kMobileAssetPreferencesFakeDeviceOSBuildVersion
+ _objc_msgSend$buildVersion
+ _objc_msgSend$bundleAccessPermitted:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$descriptorForAssetType:
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$initWithAssetType:
+ _objc_msgSend$isSecure
+ _objc_msgSend$sharedDevice
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$verifyPlist:manifest:manifestType:result:error:
+ _objc_opt_self
+ _objc_retainBlock
+ _objc_retain_x24
- GCC_except_table116
- GCC_except_table42
- GCC_except_table46
- GCC_except_table51
- GCC_except_table56
- GCC_except_table61
- GCC_except_table63
- GCC_except_table76
- GCC_except_table79
- GCC_except_table94
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1269
- ___block_literal_global.1125
- ___block_literal_global.1131
- ___block_literal_global.1169
- ___block_literal_global.1175
- ___block_literal_global.1180
- ___block_literal_global.1185
- ___block_literal_global.1190
- ___block_literal_global.1195
- ___block_literal_global.1214
- ___block_literal_global.1255
- ___block_literal_global.1264
- ___block_literal_global.1307
- ___block_literal_global.1378
- ___block_literal_global.1383
- ___block_literal_global.1385
- ___block_literal_global.1432
- ___block_literal_global.1438
- ___block_literal_global.1443
- ___block_literal_global.1454
- ___block_literal_global.1459
- ___block_literal_global.1481
- ___block_literal_global.1712
- ___block_literal_global.2268
- ___block_literal_global.2822
- ___block_literal_global.2824
- ___block_literal_global.2826
- ___block_literal_global.2828
- ___block_literal_global.2830
- ___block_literal_global.2869
- ___block_literal_global.2872
CStrings:
+ "/System/Library/AssetTypeDescriptors/"
+ "/System/Library/SecureAssetTypeDescriptors/"
+ "<MAAssetTypeDescriptor: %p>: (AssetType: %@, Secure: %d)"
+ "@\"MAAssetTypeDescriptor\""
+ "AccessNotPermitted"
+ "Asset Specifiers"
+ "Asset Type"
+ "CompatibilityVersionMismatch"
+ "CryptexInfo plist is missing its asset-type defined in: %@"
+ "Failed to load asset descriptors from path %{public}@. %@"
+ "Failed to parse CryptexInfo as a plist."
+ "Failed to validate cryptex info plist with manifest from disk."
+ "FakeDeviceOSBuildVersion"
+ "MAAssetTypeDescriptor"
+ "Make Repository Data Vault"
+ "N"
+ "RemoveV1Assets"
+ "Secure cryptex info plist (%@) is missing on the bundle."
+ "Stored personalized manifest ticket (%@) could not be read"
+ "T@\"MAAssetTypeDescriptor\",R,V_typeDescriptor"
+ "T@\"NSArray\",R,D,N"
+ "T@\"NSDictionary\",R,D,N"
+ "T@\"NSString\",R,N,V_assetType"
+ "TB,R,D,N"
+ "TB,R,N,V_isSecure"
+ "Unable to read cryptex info path %@"
+ "Y"
+ "[SMA] Cannot create an MAAssetTypeDescriptor because assetType is nil for bundle: %{public}@"
+ "[SMA] [SecureMAHelper]: Successfully recorded graft entry | assetType:%@ | grafted:%@"
+ "_isSecure"
+ "_typeDescriptor"
+ "assetProperties"
+ "assetSpecifiers"
+ "buildVersion"
+ "bundleAccessPermitted:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "descriptorForAssetType:"
+ "dictionaryWithContentsOfURL:"
+ "getResourceValue:forKey:error:"
+ "initWithAssetType:"
+ "isSecure"
+ "sharedDevice"
+ "shouldMakeDataVault"
+ "shouldRemoveV1Assets"
+ "stringByDeletingPathExtension"
+ "typeDescriptor"
+ "typeDescriptorsToDataVault"
+ "typeDescriptorsToRemoveV1Assets"
+ "v16@?0@\"NSDictionary\"8"
+ "v32@?0@8@\"NSDictionary\"16^B24"
- "[SMA] [SecureMAHelper]: Successfully recorded graft entry for asset of type %@"

```
