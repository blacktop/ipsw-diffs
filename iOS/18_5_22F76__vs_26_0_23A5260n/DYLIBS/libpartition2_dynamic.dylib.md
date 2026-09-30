## libpartition2_dynamic.dylib

> `/usr/lib/libpartition2_dynamic.dylib`

```diff

-3196.122.1.0.0
-  __TEXT.__text: 0xb204
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x4e4
-  __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__oslogstring: 0x1202
-  __TEXT.__cstring: 0xc0d
-  __TEXT.__unwind_info: 0x200
+3476.0.6.0.1
+  __TEXT.__text: 0xaf10
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x584
+  __TEXT.__const: 0xc8
+  __TEXT.__oslogstring: 0x115f
+  __TEXT.__cstring: 0xc86
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0xab0
-  __TEXT.__objc_methtype: 0x118
-  __TEXT.__objc_stubs: 0xbe0
+  __TEXT.__objc_methname: 0xc41
+  __TEXT.__objc_methtype: 0x146
+  __TEXT.__objc_stubs: 0xd60
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x378
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x348
-  __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__objc_const: 0x3c0
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xac
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F18A58DF-5D51-3C48-8E15-C7A9FC71531B
-  Functions: 124
-  Symbols:   588
-  CStrings:  495
+  UUID: AA7D6A3B-E228-3D05-A90D-AC3BBA65D4A1
+  Functions: 143
+  Symbols:   647
+  CStrings:  537
 
Symbols:
+ +[LPAPFSContainer _containerWithPhysticalStoreRole:]
+ +[LPAPFSContainer recoveryContainer]
+ +[LPAPFSVolume enumerateRoleMetadataUsingBlock:]
+ +[LPAPFSVolume roleMetadataForRole:]
+ +[LPMedia(Private) IOMainPort]
+ -[LPAPFSContainer VMVolume]
+ -[LPAPFSContainer _matchVolumesWithRole:group:]
+ -[LPAPFSContainer hardwareVolume]
+ -[LPAPFSContainer volumeWithRole:group:]
+ -[LPAPFSContainer volumesWithRole:group:]
+ -[LPAPFSContainer xARTVolume]
+ -[LPAPFSVolume _pathIsTemporaryMount:]
+ -[LPAPFSVolume _pathIsTemporaryMount:].cold.1
+ -[LPAPFSVolume pairedVolumeWithRole:]
+ GCC_except_table13
+ GCC_except_table15
+ GCC_except_table9
+ _IORegistryEntryGetRegistryEntryID
+ _IOServiceMatchPropertyTable
+ __OBJC_$_PROP_LIST_LPAPFSContainer
+ ___20-[LPAPFSVolume role]_block_invoke
+ ___20-[LPAPFSVolume role]_block_invoke.122
+ ___34-[LPAPFSVolume setRole:withError:]_block_invoke
+ ___36+[LPAPFSVolume roleMetadataForRole:]_block_invoke
+ ___41-[LPAPFSContainer volumesWithRole:group:]_block_invoke
+ ___41-[LPAPFSContainer volumesWithRole:group:]_block_invoke.48
+ ___43+[LPAPFSVolume defaultVolumeNameGivenRole:]_block_invoke
+ ___block_descriptor_40_e8_32s_e8_v12?0I8l
+ ___block_descriptor_42_e8_32r_e17_v16?0r^{?=iS}8l
+ ___block_descriptor_44_e8_32r_e17_v16?0r^{?=iS}8l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0r^{?=iS}8l
+ ___block_literal_global.224
+ ___copy_helper_block_e8_32s40r
+ ___destroy_helper_block_e8_32s40r
+ _enumerateRoleMetadataUsingBlock:.sRoleMetadata
+ _objc_msgSend$IOMainPort
+ _objc_msgSend$_containerWithPhysticalStoreRole:
+ _objc_msgSend$_matchVolumesWithRole:group:
+ _objc_msgSend$_pathIsTemporaryMount:
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$containsString:
+ _objc_msgSend$enumerateRoleMetadataUsingBlock:
+ _objc_msgSend$pairedVolumeWithRole:
+ _objc_msgSend$roleMetadataForRole:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$volumeWithRole:group:
+ _objc_msgSend$volumesWithRole:group:
+ _objc_storeStrong
+ _rmdir
- _CFEqual
- ___26-[LPAPFSContainer volumes]_block_invoke
- ___26-[LPAPFSContainer volumes]_block_invoke.20
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___block_descriptor_44_e8_32r_e8_v12?0I8l
- ___block_literal_global.219
- _objc_msgSend$volumes
- _sLegacyVolumeNameMapping
- _sLegacyVolumeNameMappingCount
- _sRoleEncodingMapping
- _sRoleEncodingMappingCount
- _sRoleLookupTable
CStrings:
+ "+[LPAPFSContainer _containerWithPhysticalStoreRole:]"
+ "/mnt5"
+ "/tmp/"
+ "@28@0:8i16@20"
+ "Backup"
+ "Baseband data"
+ "Cleaned up temporary mount point"
+ "Enterprise data"
+ "Failed to clean up temporary mount point: %d"
+ "IOMainPort"
+ "IOParentMatch"
+ "IORegistryEntryID"
+ "Installer"
+ "RoleValue"
+ "SideCar"
+ "T@\"LPAPFSVolume\",R"
+ "TI,R"
+ "VM"
+ "VMVolume"
+ "_containerWithPhysticalStoreRole:"
+ "_matchVolumesWithRole:group:"
+ "_pathIsTemporaryMount:"
+ "caseInsensitiveCompare:"
+ "containsString:"
+ "enumerateRoleMetadataUsingBlock:"
+ "hardwareVolume"
+ "iDiags"
+ "pairedVolumeWithRole:"
+ "r^{?=iS@@}20@0:8i16"
+ "recoveryContainer"
+ "roleMetadataForRole:"
+ "stringByDeletingLastPathComponent"
+ "stringByResolvingSymlinksInPath"
+ "tmp-mount-"
+ "v16@?0r^{?=iS@@}8"
+ "v24@0:8@?16"
+ "volumeWithRole:group:"
+ "volumesWithRole:group:"
+ "xARTVolume"
- "%s : Container is missing UUID?"
- "+[LPAPFSContainer diagsContainer]"
- "-[LPAPFSPhysicalStore container]"
- "Error: More than one preboot volume found: %{private}@"
- "Error: More than one recovery volume found: %{private}@"
- "Error: More than one update volume found: %{private}@"
- "Failed to create container volumes iterator"
- "Logs"
- "Scratch"

```
