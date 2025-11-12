## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.60.20.0.0
-  __TEXT.__text: 0x21814
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x80c
+1837.60.34.0.0
+  __TEXT.__text: 0x1f0ec
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x530
-  __TEXT.__cstring: 0x78d0
-  __TEXT.__oslogstring: 0x326c
-  __TEXT.__gcc_except_tab: 0xb88
-  __TEXT.__unwind_info: 0x5c0
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x1eb9
-  __TEXT.__objc_methtype: 0x503
-  __TEXT.__objc_stubs: 0x2100
-  __DATA_CONST.__got: 0x2a8
+  __TEXT.__cstring: 0x75c0
+  __TEXT.__oslogstring: 0x2dc3
+  __TEXT.__gcc_except_tab: 0x9a0
+  __TEXT.__unwind_info: 0x588
+  __TEXT.__objc_classname: 0x98
+  __TEXT.__objc_methname: 0x1a90
+  __TEXT.__objc_methtype: 0x250
+  __TEXT.__objc_stubs: 0x1ea0
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__const: 0xf50
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x880
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__cfstring: 0x8220
-  __AUTH_CONST.__objc_const: 0x9d0
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x8000
+  __AUTH_CONST.__objc_const: 0x848
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x44
-  __DATA.__data: 0x238
-  __DATA.__bss: 0x278
+  __DATA.__data: 0xb8
+  __DATA.__bss: 0x258
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C11854DF-E4A2-3076-B8A8-AB8FD522C162
-  Functions: 478
-  Symbols:   1669
-  CStrings:  2777
+  UUID: 927985FC-D3F1-33C0-B482-1A4AEEBBEF6F
+  Functions: 467
+  Symbols:   1592
+  CStrings:  2650
 
Symbols:
+ GCC_except_table109
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table72
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table89
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1179
+ ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.416
+ ___block_literal_global.1125
+ ___block_literal_global.1131
+ ___block_literal_global.1148
+ ___block_literal_global.1169
+ ___block_literal_global.1175
+ ___block_literal_global.1180
+ ___block_literal_global.1185
+ ___block_literal_global.1190
+ ___block_literal_global.1195
+ ___block_literal_global.1214
+ ___block_literal_global.1307
+ ___block_literal_global.1381
+ ___block_literal_global.1386
+ ___block_literal_global.1388
+ ___block_literal_global.1432
+ ___block_literal_global.1438
+ ___block_literal_global.1443
+ ___block_literal_global.1454
+ ___block_literal_global.1459
+ ___block_literal_global.1481
+ ___block_literal_global.1614
+ ___block_literal_global.2169
+ ___block_literal_global.2822
+ ___block_literal_global.2824
+ ___block_literal_global.2826
+ ___block_literal_global.2828
+ ___block_literal_global.2830
+ ___block_literal_global.2869
+ ___block_literal_global.2873
- +[SecureMobileAssetBundle _requiresLiveExclaveNonce]
- +[SecureMobileAssetBundle _requiresLiveExclaveNonce].cold.1
- +[SecureMobileAssetBundle _shouldUseConclave:]
- +[SecureMobileAssetBundle commitStagedManifestsToExclavesForSelectors:darwinOnly:error:]
- +[SecureMobileAssetBundle getExclaveManager:]
- -[SecureMobileAssetBundle _activateManifestInExclaves:error:]
- -[SecureMobileAssetBundle _storeManifestToExclaves:infoPlist:stage:error:]
- -[SecureMobileAssetBundle isPersonalizedForExclaves:staged:]
- GCC_except_table118
- GCC_except_table13
- GCC_except_table19
- GCC_except_table33
- GCC_except_table38
- GCC_except_table43
- GCC_except_table53
- GCC_except_table54
- GCC_except_table58
- GCC_except_table59
- GCC_except_table62
- GCC_except_table64
- GCC_except_table77
- GCC_except_table80
- GCC_except_table95
- GCC_except_table96
- GCC_except_table97
- _MABrainUtilityConclaveEnabled.answer
- _MABrainUtilityConclaveEnabled.cold.1
- _MABrainUtilityConclaveEnabled.onceToken
- _OBJC_CLASS_$_SecureMobileAssetExclaveManager
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceBaseProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceProtocol2
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceBaseProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceProtocol2
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceBaseProtocol
- __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceProtocol
- __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceProtocol2
- __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceBaseProtocol
- __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol
- __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol2
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceBaseProtocol
- __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol
- __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol2
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceBaseProtocol
- __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceProtocol2
- ___52+[SecureMobileAssetBundle _requiresLiveExclaveNonce]_block_invoke
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1261
- ___MABrainUtilityConclaveEnabled_block_invoke
- ___MABrainUtilityConclaveEnabled_block_invoke.cold.1
- ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.407
- ___block_literal_global.1116
- ___block_literal_global.1122
- ___block_literal_global.1139
- ___block_literal_global.1160
- ___block_literal_global.1166
- ___block_literal_global.1176
- ___block_literal_global.1181
- ___block_literal_global.1186
- ___block_literal_global.1205
- ___block_literal_global.1246
- ___block_literal_global.1256
- ___block_literal_global.1298
- ___block_literal_global.1372
- ___block_literal_global.1377
- ___block_literal_global.1379
- ___block_literal_global.1423
- ___block_literal_global.1429
- ___block_literal_global.1434
- ___block_literal_global.1445
- ___block_literal_global.1450
- ___block_literal_global.1472
- ___block_literal_global.1723
- ___block_literal_global.2300
- ___block_literal_global.2813
- ___block_literal_global.2815
- ___block_literal_global.2817
- ___block_literal_global.2819
- ___block_literal_global.2821
- ___block_literal_global.2860
- ___block_literal_global.2864
- ___block_literal_global.417
- __os_feature_enabled_impl
- __requiresLiveExclaveNonce.onceToken
- __requiresLiveExclaveNonce.required
- _objc_msgSend$_activateManifestInExclaves:error:
- _objc_msgSend$_requiresLiveExclaveNonce
- _objc_msgSend$_shouldUseConclave:
- _objc_msgSend$_storeManifestToExclaves:infoPlist:stage:error:
- _objc_msgSend$activateCommittedManifestForFSTag:specifier:error:
- _objc_msgSend$checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:
- _objc_msgSend$checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:
- _objc_msgSend$commitStagedManifestForFSTags:error:
- _objc_msgSend$commitStagedManifestForFSTags:specifiers:error:
- _objc_msgSend$commitStagedManifestsToExclavesForSelectors:darwinOnly:error:
- _objc_msgSend$conformsToProtocol:
- _objc_msgSend$darwinOnly
- _objc_msgSend$getExclaveManager:
- _objc_msgSend$integrityCatalogPath
- _objc_msgSend$isPersonalizedForExclaves:staged:
- _objc_msgSend$proposeNonce:
- _objc_msgSend$stageManifest:infoPlist:catalog:error:
- _objc_msgSend$stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:
- _objc_msgSend$storeManifest:infoPlist:catalog:error:
CStrings:
- "#16@0:8"
- "@\"NSDictionary\"24@0:8^@16"
- "@\"NSString\"16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "Activating committed manifest is not supported on this OS"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8I16B20"
- "B28@0:8I16^@20"
- "B32@0:8@\"NSArray\"16^@24"
- "B36@0:8I16@\"NSString\"20^@28"
- "B36@0:8I16@20^@28"
- "B40@0:8@\"NSArray\"16@\"NSArray\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@16@24B32^@36"
- "B48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32^@40"
- "B48@0:8@16@24@32^@40"
- "B60@0:8I16@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44^@52"
- "B60@0:8I16@20@28@36@44^@52"
- "B64@0:8I16B20@\"NSData\"24@\"NSData\"32@\"NSData\"40^B48^@56"
- "B64@0:8I16B20@24@32@40^B48^@56"
- "B72@0:8I16@\"NSString\"20I28@\"NSData\"32@\"NSData\"40@\"NSData\"48^B56^@64"
- "B72@0:8I16@20I28@32@40@48^B56^@64"
- "Cannot map to Exclaves: _storeManifestToExclaves failed"
- "Cannot map to Exclaves: info plist data is nil"
- "Cannot map to Exclaves: info plist path is nil"
- "Cannot map to Exclaves: ticket data is nil"
- "Cannot map to Exclaves: ticket path is nil"
- "Failed to activate committed manifest in Exclaves"
- "Failed to allocate NSNumber for fstag"
- "Failed to commit staged manifests to Exclaves"
- "Failed to get exclave nonces"
- "Failed to get shared instance of SecureMobileAssetExclave"
- "LiveStorageExclaveNonce"
- "MAExclaveManifestStorageServiceBaseProtocol"
- "MAExclaveManifestStorageServiceProtocol"
- "MAExclaveManifestStorageServiceProtocol2"
- "MobileAsset"
- "NSObject"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "[SMA] Activating committed manifest for %@:%@ fstag=%u"
- "[SMA] Activating committed manifest is not supported on this OS"
- "[SMA] Cannot map to Exclaves: activate manifest failed"
- "[SMA] Committing staged exclave manifests for fsTags and specifiers: [%@] [%@]"
- "[SMA] Committing staged exclave manifests for fsTags: %@"
- "[SMA] Failed to activate committed manifest because conclave manager instance is nil: %@"
- "[SMA] Failed to activate committed manifest for %@:%@ fstag=%u %@"
- "[SMA] Failed to allocate NSNumber for fstag=%d"
- "[SMA] Failed to commit staged manifests to Exclaves"
- "[SMA] Failed to get nonce dictionary from SecureMobileAssetExclave: %@"
- "[SMA] Failed to get shared instance of SecureMobileAssetExclave"
- "[SMA] Failed to get shared instance of SecureMobileAssetExclave: %@"
- "[SMA] Generating nonce proposal for exclaves"
- "[SMA] Operations will be restricted to darwin only"
- "[SMA] Successfully activated committed manifest for %@:%@ fstag=%u"
- "[SMA] Unable to get SecureMobileAssetExclave instance in this environment"
- "[SMA] Warning: MAExclaveManifestStorageService does not support staging, commit is a no-op"
- "[SMA] Warning: MAExclaveManifestStorageService does not support staging, storing manifest instead"
- "^{_NSZone=}16@0:8"
- "_activateManifestInExclaves:error:"
- "_requiresLiveExclaveNonce"
- "_shouldUseConclave:"
- "_storeManifestToExclaves:infoPlist:stage:error:"
- "activateCommittedManifestForFSTag:specifier:error:"
- "autorelease"
- "checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:"
- "checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:"
- "class"
- "com_apple_mobileassetd_conclave"
- "commitStagedManifestForFSTags:error:"
- "commitStagedManifestForFSTags:specifiers:error:"
- "commitStagedManifestsToExclavesForSelectors:darwinOnly:error:"
- "conformsToProtocol:"
- "debugDescription"
- "digestNonce"
- "failed to get integrity catalog path"
- "failed to read cryptex integrity catalog"
- "failed to stage manifest in Exclave Secure Storage"
- "failed to store manifest in Exclave Secure Storage"
- "getExclaveManager:"
- "hash"
- "invalidateManifestForFSTag:error:"
- "invalidateManifestForFSTag:specifier:error:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPersonalizedForExclaves:staged:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "proposeNonce:"
- "rawNonce"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "stageManifest:infoPlist:catalog:error:"
- "stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:"
- "storeManifest:infoPlist:catalog:error:"
- "superclass"
- "zone"

```
