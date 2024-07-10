## AppleIDSSOAuthentication

> `/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/Versions/A/AppleIDSSOAuthentication`

```diff

-103.0.0.0.0
-  __TEXT.__text: 0x2df58
+100.2.0.0.0
+  __TEXT.__text: 0x2d788
   __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x540
-  __TEXT.__const: 0xe30
-  __TEXT.__cstring: 0x334
-  __TEXT.__oslogstring: 0xbdb
+  __TEXT.__objc_methlist: 0x4f0
+  __TEXT.__const: 0xe20
+  __TEXT.__cstring: 0x314
+  __TEXT.__oslogstring: 0x9dc
   __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x15db
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_classname: 0xec
+  __TEXT.__objc_methname: 0x146f
   __TEXT.__objc_methtype: 0x3e2
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x258
+  __TEXT.__objc_stubs: 0xea0
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x550
+  __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20

   __AUTH_CONST.__objc_const: 0xe18
   __DATA.__objc_ivar: 0x58
   __DATA.__data: 0x290
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x40
   __DATA.__common: 0x64
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 199
-  Symbols:   620
-  CStrings:  45
+  Functions: 193
+  Symbols:   595
+  CStrings:  44
 
Symbols:
+ GCC_except_table17
+ GCC_except_table24
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table57
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSMutableArray
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __45+[AIDAServiceOwnersManager supportedServices]_block_invoke.cold.1
+ __45+[AIDAServiceOwnersManager supportedServices]_block_invoke.cold.2
+ __45+[AIDAServiceOwnersManager supportedServices]_block_invoke.cold.3
+ __45+[AIDAServiceOwnersManager supportedServices]_block_invoke.cold.4
+ __53-[AIDAServiceOwnersManager _buildServiceOwnerMapping]_block_invoke.cold.4
+ __69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.103
+ __69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.105
+ __70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.113
+ __70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.115
+ __70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke_2.114
+ __84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.102
+ __84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.95
+ __84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.96
+ ___45+[AIDAServiceOwnersManager supportedServices]_block_invoke
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSBundle"8^B16l
+ __block_literal_global.117
+ _objc_msgSend$addObjectsFromArray:
- +[AIDAServiceOwnersManager _loadServiceOwnerBundlesIfNeeded]
- +[AIDAServiceOwnersManager _loadServiceOwnerBundles]
- +[AIDAServiceOwnersManager _rejectionlistedBundleIDs]
- +[AIDAServiceOwnersManager _set_loadServiceOwnerBundlesIfNeeded_onceToken:]
- +[AIDAServiceOwnersManager _supplementalServiceTypes]
- +[AIDAServiceOwnersManager configureProcessSpecificServiceOwnerRejectionlist:]
- +[AIDAServiceOwnersManager configureProcessSpecificSupplementalServiceTypes:]
- +[AIDAServiceOwnersManager supportedServices].cold.1
- +[AIDAServiceOwnersManager supportedServices].cold.2
- GCC_except_table25
- GCC_except_table32
- GCC_except_table44
- GCC_except_table45
- GCC_except_table59
- GCC_except_table64
- GCC_except_table65
- _OBJC_CLASS_$_AAFDeviceInfo
- _OBJC_CLASS_$_AFUtilities
- _OBJC_CLASS_$_NSMutableOrderedSet
- __52+[AIDAServiceOwnersManager _loadServiceOwnerBundles]_block_invoke.cold.1
- __52+[AIDAServiceOwnersManager _loadServiceOwnerBundles]_block_invoke.cold.2
- __52+[AIDAServiceOwnersManager _loadServiceOwnerBundles]_block_invoke.cold.3
- __69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.110
- __69-[AIDAServiceOwnersManager signInToServices:usingContext:completion:]_block_invoke.113
- __70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.118
- __70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke.120
- __70-[AIDAServiceOwnersManager signOutOfServices:usingContext:completion:]_block_invoke_2.119
- __84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.100
- __84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.101
- __84-[AIDAServiceOwnersManager signInToAllServicesInBackground:usingContext:completion:]_block_invoke.107
- __AIDAServiceOwnersManagerRejectionlist
- __AIDAServiceOwnersManagerSupplementalServiceTypes
- ___52+[AIDAServiceOwnersManager _loadServiceOwnerBundles]_block_invoke
- ___60+[AIDAServiceOwnersManager _loadServiceOwnerBundlesIfNeeded]_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32s_e31_24?0"NSString"8"NSBundle"16l
- __block_literal_global.122
- __loadServiceOwnerBundlesIfNeededOnceToken
- __os_log_fault_impl
- _loadServiceOwnerBundlesIfNeeded.bundles
- _objc_msgSend$_loadServiceOwnerBundles
- _objc_msgSend$_loadServiceOwnerBundlesIfNeeded
- _objc_msgSend$_rejectionlistedBundleIDs
- _objc_msgSend$_supplementalServiceTypes
- _objc_msgSend$aaf_map:
- _objc_msgSend$allKeys
- _objc_msgSend$array
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$defaultStore
- _objc_msgSend$isInternalBuild
- _objc_msgSend$isLoaded
- _objc_msgSend$isVirtualMachine
- _objc_msgSend$orderedSetWithArray:
- _objc_msgSend$unionSet:
CStrings:
- "@24@?0@\"NSString\"8@\"NSBundle\"16"

```
