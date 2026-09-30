## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.0.31.0.1
-  __TEXT.__text: 0xfe48
+1837.0.53.0.0
+  __TEXT.__text: 0x1046c
   __TEXT.__auth_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x614
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x2265
+  __TEXT.__cstring: 0x2699
   __TEXT.__oslogstring: 0x1bc6
   __TEXT.__gcc_except_tab: 0x758
-  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0x11b1
+  __TEXT.__objc_methname: 0x11fe
   __TEXT.__objc_methtype: 0x3f3
-  __TEXT.__objc_stubs: 0x1360
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__objc_stubs: 0x13c0
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f0
+  __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x26e0
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x2d00
   __AUTH_CONST.__objc_const: 0x620
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x180
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 093152D0-5BF2-3BFB-AB2F-13643AC312F3
-  Functions: 168
-  Symbols:   884
-  CStrings:  1047
+  UUID: 6B03CA44-4373-30B2-9FD4-C3E0745755DC
+  Functions: 170
+  Symbols:   894
+  CStrings:  1149
 
Symbols:
+ -[SecureMobileAssetBundle initWithPath:].cold.1
+ GCC_except_table103
+ GCC_except_table13
+ GCC_except_table26
+ GCC_except_table34
+ GCC_except_table38
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table85
+ _OBJC_CLASS_$_SUCoreErrorInformation
+ ___40-[SecureMobileAssetBundle initWithPath:]_block_invoke
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1214
+ ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.404
+ ___block_literal_global.1201
+ ___block_literal_global.1209
+ ___block_literal_global.1342
+ ___block_literal_global.1605
+ ___block_literal_global.2065
+ ___block_literal_global.414
+ _initWithPath:.secureAssetErrorInfoOnce
+ _objc_msgSend$attributesOfErrorForDomain:withCode:codeName:
+ _objc_msgSend$integerValue
+ _objc_msgSend$setObject:forKey:
- GCC_except_table101
- GCC_except_table12
- GCC_except_table25
- GCC_except_table33
- GCC_except_table37
- GCC_except_table42
- GCC_except_table47
- GCC_except_table51
- GCC_except_table53
- GCC_except_table66
- GCC_except_table69
- GCC_except_table82
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1190
- ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.401
- ___block_literal_global.1185
- ___block_literal_global.1324
- ___block_literal_global.1584
- ___block_literal_global.1798
- ___block_literal_global.411
Functions:
~ -[SecureMobileAssetBundle initWithPath:] : 200 -> 224
+ ___40-[SecureMobileAssetBundle initWithPath:]_block_invoke
+ -[SecureMobileAssetBundle initWithPath:].cold.1
CStrings:
+ "Alloc"
+ "CommitManifests"
+ "Depersonalize"
+ "DiskImageAttach"
+ "DiskImageEject"
+ "ExclavesUnsupported"
+ "Graft"
+ "GraftCommittedTicketDataNil"
+ "GraftNotPersonalizedForExclaves"
+ "GraftPath"
+ "GraftPersonalizedBundleTicketDataNil"
+ "GraftTicketMismatch"
+ "InvalidArgument"
+ "InvalidCommand"
+ "MapToExclaves"
+ "MapToExclavesActivateManifestFailed"
+ "MapToExclavesCommittedTicketDataNil"
+ "MapToExclavesDetermineState"
+ "MapToExclavesInfoPlistDataNil"
+ "MapToExclavesInfoPlistPathNil"
+ "MapToExclavesIntegrityCatalogDataNil"
+ "MapToExclavesIntegrityCatalogPathNil"
+ "MapToExclavesNotPersonalizedForExclaves"
+ "MapToExclavesPersonalizedBundleTicketDataNil"
+ "MapToExclavesStoreManifestFailed"
+ "MapToExclavesTicketDataNil"
+ "MapToExclavesTicketMismatch"
+ "MapToExclavesTicketPathNil"
+ "MapToExclavesUnregisterExisting"
+ "Mount"
+ "MountAttachDiskImage"
+ "MountCommittedTicketDataNil"
+ "MountFindAPFSVolume"
+ "MountFindDevNodes"
+ "MountFoundMultipleAPFSVolumes"
+ "MountNotPersonalizedForExclaves"
+ "MountPath"
+ "MountPersonalizedBundleTicketDataNil"
+ "MountRootHash"
+ "MountTicket"
+ "MountTicketMismatch"
+ "None"
+ "Personalize"
+ "UnexpectedFailure"
+ "Ungraft"
+ "Unimplemented"
+ "UnmapFromExclaves"
+ "Unmount"
+ "Unsupported"
+ "attributesOfErrorForDomain:withCode:codeName:"
+ "integerValue"
+ "q"
+ "setObject:forKey:"

```
