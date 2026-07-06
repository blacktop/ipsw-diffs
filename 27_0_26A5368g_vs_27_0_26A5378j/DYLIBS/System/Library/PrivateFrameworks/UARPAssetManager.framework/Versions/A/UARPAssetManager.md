## UARPAssetManager

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/Versions/A/UARPAssetManager`

```diff

-  __TEXT.__text: 0x47f0
-  __TEXT.__objc_methlist: 0x74c
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x5c9
-  __TEXT.__gcc_except_tab: 0x1e8
-  __TEXT.__oslogstring: 0xc8
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__text: 0x5290
+  __TEXT.__objc_methlist: 0x834
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x62f
+  __TEXT.__gcc_except_tab: 0x1f4
+  __TEXT.__oslogstring: 0x11b
+  __TEXT.__unwind_info: 0x288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0xe40
+  __AUTH_CONST.__cfstring: 0x680
+  __AUTH_CONST.__objc_const: 0xfa0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x84
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 141
-  Symbols:   446
-  CStrings:  112
+  Functions: 159
+  Symbols:   483
+  CStrings:  125
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Symbols:
+ +[UARPEndpointPersonalityiCloud supportsSecureCoding]
+ -[UARPAssetManagerCacheConfiguration initWithModel:hwFusing:domain:assetVersion:filePath:usePallas:useiCloud:internalVersion:restoreVersion:]
+ -[UARPAssetManagerCacheConfiguration model]
+ -[UARPAssetManagerCacheConfiguration useiCloud]
+ -[UARPAssetManagerClient getAssetURLForPersonality:releaseNotes:]
+ -[UARPAssetManagerClient getReleaseNotesAssetURLForPersonality:]
+ -[UARPEndpointPersonalityiCloud .cxx_destruct]
+ -[UARPEndpointPersonalityiCloud containerID]
+ -[UARPEndpointPersonalityiCloud copyWithZone:]
+ -[UARPEndpointPersonalityiCloud description]
+ -[UARPEndpointPersonalityiCloud encodeWithCoder:]
+ -[UARPEndpointPersonalityiCloud hash]
+ -[UARPEndpointPersonalityiCloud initWithCoder:]
+ -[UARPEndpointPersonalityiCloud initWithProductGroup:productNumber:domain:]
+ -[UARPEndpointPersonalityiCloud isEqual:]
+ -[UARPEndpointPersonalityiCloud isPersonalityMatch:]
+ -[UARPEndpointPersonalityiCloud productGroup]
+ -[UARPEndpointPersonalityiCloud productNumber]
+ -[UARPEndpointPersonalityiCloud setContainerID:]
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table7
+ OBJC_IVAR_$_UARPAssetManagerCacheConfiguration._model
+ OBJC_IVAR_$_UARPAssetManagerCacheConfiguration._useiCloud
+ OBJC_IVAR_$_UARPEndpointPersonalityiCloud._containerID
+ OBJC_IVAR_$_UARPEndpointPersonalityiCloud._productGroup
+ OBJC_IVAR_$_UARPEndpointPersonalityiCloud._productNumber
+ _OBJC_CLASS_$_UARPEndpointPersonalityiCloud
+ _OBJC_METACLASS_$_UARPEndpointPersonalityiCloud
+ __OBJC_$_CLASS_METHODS_UARPEndpointPersonalityiCloud
+ __OBJC_$_INSTANCE_METHODS_UARPEndpointPersonalityiCloud
+ __OBJC_$_INSTANCE_VARIABLES_UARPEndpointPersonalityiCloud
+ __OBJC_$_PROP_LIST_UARPEndpointPersonalityiCloud
+ __OBJC_CLASS_RO_$_UARPEndpointPersonalityiCloud
+ __OBJC_METACLASS_RO_$_UARPEndpointPersonalityiCloud
+ ___62-[UARPAssetManagerClient getSandboxExtensionTokenForAssetURL:]_block_invoke_2
+ ___65-[UARPAssetManagerClient getAssetURLForPersonality:releaseNotes:]_block_invoke
+ ___65-[UARPAssetManagerClient getAssetURLForPersonality:releaseNotes:]_block_invoke_2
+ _createiCloudEndpointPersonality
+ _objc_msgSend$containerID
+ _objc_msgSend$getAssetURLForPersonality:releaseNotes:
+ _objc_msgSend$getAssetURLForPersonality:releaseNotes:reply:
+ _objc_msgSend$initWithModel:hwFusing:domain:assetVersion:filePath:usePallas:useiCloud:internalVersion:restoreVersion:
+ _objc_msgSend$initWithProductGroup:productNumber:domain:
+ _objc_msgSend$productGroup
+ _objc_msgSend$productNumber
+ _objc_msgSend$setContainerID:
+ createiCloudEndpointPersonality
- -[UARPAssetManagerCacheConfiguration appleModelNumber]
- -[UARPAssetManagerCacheConfiguration initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:internalVersion:restoreVersion:]
- GCC_except_table20
- GCC_except_table24
- GCC_except_table27
- OBJC_IVAR_$_UARPAssetManagerCacheConfiguration._appleModelNumber
- __52-[UARPAssetManagerClient getAssetURLForPersonality:]_block_invoke
- __62-[UARPAssetManagerClient getSandboxExtensionTokenForAssetURL:]_block_invoke
- ___52-[UARPAssetManagerClient getAssetURLForPersonality:]_block_invoke
- _objc_msgSend$getAssetURLForPersonality:reply:
- _objc_msgSend$initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:internalVersion:restoreVersion:
- createEndpointPersonality
CStrings:
+ "-[UARPAssetManagerClient getAssetURLForPersonality:releaseNotes:]"
+ "<%@: model=%@ fusing=%@ domain=%@ pallas=%d icloud=%d vers=%@ file=%@ internal=%d restoreVersion=%@>"
+ "<%@: pg/pn=%@ domain=%@ "
+ "Domain %@, Product Group %@, Product Number %@ required for personality"
+ "Model Number %@, Serial Number %@, HW Fusing %@, Domain %@ required for personality"
+ "container=%@ "
+ "containerID"
+ "model"
+ "productGroup"
+ "productNumber"
+ "useiCloud"
- "-[UARPAssetManagerClient getAssetURLForPersonality:]"
- "<%@: model=%@ fusing=%@ domain=%@ pallas=%d vers=%@ file=%@ internal=%d restoreVersion=%@>"
- "Model Number %@, Serial Number %@, HW Fusing %@ required for personality"
- "appleModelNumber"

```
