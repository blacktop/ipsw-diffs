## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-1338.80.37.0.0
-  __TEXT.__text: 0x8b934
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x8cac
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x7c3b
-  __TEXT.__oslogstring: 0x6619
-  __TEXT.__gcc_except_tab: 0x88c
+1345.100.155.0.0
+  __TEXT.__text: 0x9000c
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x8e58
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x7e56
+  __TEXT.__oslogstring: 0x6c05
+  __TEXT.__gcc_except_tab: 0x898
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x2638
-  __TEXT.__objc_classname: 0x1967
-  __TEXT.__objc_methname: 0xe0f9
-  __TEXT.__objc_methtype: 0x3f20
-  __TEXT.__objc_stubs: 0x97e0
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0x2080
-  __DATA_CONST.__objc_classlist: 0x6b0
+  __TEXT.__unwind_info: 0x2640
+  __TEXT.__objc_classname: 0x1984
+  __TEXT.__objc_methname: 0xe5a4
+  __TEXT.__objc_methtype: 0x3f8b
+  __TEXT.__objc_stubs: 0x9b00
+  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__const: 0x20b8
+  __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3150
+  __DATA_CONST.__objc_selrefs: 0x3250
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x6a0
+  __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x510
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x7400
-  __AUTH_CONST.__objc_const: 0x11e48
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x74c0
+  __AUTH_CONST.__objc_const: 0x12088
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x20d0
-  __DATA.__objc_ivar: 0xbdc
+  __DATA.__objc_ivar: 0xc00
   __DATA.__data: 0x40d
-  __DATA.__bss: 0x1a4b
-  __DATA_DIRTY.__objc_data: 0x2210
+  __DATA.__bss: 0x1a5b
+  __DATA_DIRTY.__objc_data: 0x2260
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: A70136D8-EBC7-39A1-A120-392DAAC6765F
-  Functions: 3928
-  Symbols:   12493
-  CStrings:  5865
+  UUID: E5D40E46-CE0C-39E6-BECC-8853F5DA5F99
+  Functions: 4032
+  Symbols:   12892
+  CStrings:  5970
 
Symbols:
+ -[UARPAccessoryMetadata dictionaryFromMetadata]
+ -[UARPAccessoryMetadata initWithDictionary:]
+ -[UARPAccessoryMetadata recordName]
+ -[UARPAccessoryMetadataStore .cxx_destruct]
+ -[UARPAccessoryMetadataStore accessQueue]
+ -[UARPAccessoryMetadataStore accessoryMetadataURLForFileIndex:]
+ -[UARPAccessoryMetadataStore accessoryMetadataURLForRecordName:]
+ -[UARPAccessoryMetadataStore clearAllMetadata]
+ -[UARPAccessoryMetadataStore copyMetadataForRecordName:]
+ -[UARPAccessoryMetadataStore copyMetadataForRecordName:].cold.1
+ -[UARPAccessoryMetadataStore copyiCloudToken]
+ -[UARPAccessoryMetadataStore hashRecordNameToFileIndex:]
+ -[UARPAccessoryMetadataStore iCloudChangeToken]
+ -[UARPAccessoryMetadataStore initWithDirectory:]
+ -[UARPAccessoryMetadataStore initWithDirectory:].cold.1
+ -[UARPAccessoryMetadataStore initWithDirectory:].cold.2
+ -[UARPAccessoryMetadataStore initWithDirectory:].cold.3
+ -[UARPAccessoryMetadataStore initWithDirectory:].cold.4
+ -[UARPAccessoryMetadataStore init]
+ -[UARPAccessoryMetadataStore isReadOnly]
+ -[UARPAccessoryMetadataStore loadMetadataFromPlist:]
+ -[UARPAccessoryMetadataStore loadMetadataFromPlist:].cold.1
+ -[UARPAccessoryMetadataStore loadMetadataFromPlistForFileIndex:]
+ -[UARPAccessoryMetadataStore loadMetadataFromPlistForRecordName:]
+ -[UARPAccessoryMetadataStore loadMetadataStore:]
+ -[UARPAccessoryMetadataStore log]
+ -[UARPAccessoryMetadataStore metadataCache]
+ -[UARPAccessoryMetadataStore metadataDirectoryURL]
+ -[UARPAccessoryMetadataStore saveMetadataToPlist:fileIndex:]
+ -[UARPAccessoryMetadataStore saveMetadataToPlist:fileIndex:].cold.1
+ -[UARPAccessoryMetadataStore saveMetadataToPlist:fileIndex:].cold.2
+ -[UARPAccessoryMetadataStore saveMetadataToPlist:fileIndex:].cold.3
+ -[UARPAccessoryMetadataStore saveMetadataToPlist:fileIndex:].cold.4
+ -[UARPAccessoryMetadataStore setICloudChangeToken:]
+ -[UARPAccessoryMetadataStore tokenFileURL]
+ -[UARPAccessoryMetadataStore updateCache:forKey:]
+ -[UARPAccessoryMetadataStore updateCache:forKey:].cold.1
+ -[UARPAccessoryMetadataStore updateMetadata:deleteMetadata:]
+ -[UARPAccessoryMetadataStore updateMetadata:deleteMetadata:].cold.1
+ -[UARPAccessoryMetadataStore updateMetadata:deleteMetadata:].cold.2
+ -[UARPAccessoryMetadataStore updateiCloudToken:]
+ -[UARPController availabilityNotificationForSupportedAccessoriesFilePosted:]
+ -[UARPController availabilityNotificationForSupportedAccessoriesFilePosted:].cold.1
+ -[UARPController availabilityNotificationForSupportedAccessoriesFilePosted:].cold.2
+ -[UARPController copyChipMetadataForRecordName:]
+ -[UARPController copyChipMetadataForRecordName:].cold.1
+ -[UARPController subscribeForChipSupportedAccessories]
+ -[UARPController subscribeForChipSupportedAccessories].cold.1
+ -[UARPController unregisterForSupportedAccessoriesFileAvailability:]
+ -[UARPControllerXPC getSupportedAccessoriesFileURL]
+ -[UARPControllerXPC getSupportedAccessoriesFileURL].cold.1
+ -[UARPUploaderUARP startTapToRadar:].cold.1
+ GCC_except_table185
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table220
+ GCC_except_table227
+ GCC_except_table67
+ _CC_SHA256
+ _OBJC_CLASS_$_UARPAccessoryMetadataStore
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._accessQueue
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._iCloudChangeToken
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._isReadOnly
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._log
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._metadataCache
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._metadataDirectoryURL
+ _OBJC_IVAR_$_UARPAccessoryMetadataStore._tokenFileURL
+ _OBJC_IVAR_$_UARPController._metadataStore
+ _OBJC_IVAR_$_UARPController._supportedAccessoryFileListToken
+ _OBJC_METACLASS_$_UARPAccessoryMetadataStore
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _UARPStringChipRecordCacheFilepath
+ _UARPStringChipRecordCacheFilepath.cold.1
+ _UARPStringChipRecordCacheFilepath.onceToken
+ _UARPStringChipRecordCacheFilepath.path
+ __OBJC_$_INSTANCE_METHODS_UARPAccessoryMetadataStore
+ __OBJC_$_INSTANCE_VARIABLES_UARPAccessoryMetadataStore
+ __OBJC_$_PROP_LIST_UARPAccessoryMetadataStore
+ __OBJC_CLASS_RO_$_UARPAccessoryMetadataStore
+ __OBJC_METACLASS_RO_$_UARPAccessoryMetadataStore
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke.119
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke_2.118
+ ___45-[UARPAccessoryMetadataStore copyiCloudToken]_block_invoke
+ ___46-[UARPAccessoryMetadataStore clearAllMetadata]_block_invoke
+ ___46-[UARPAccessoryMetadataStore clearAllMetadata]_block_invoke.cold.1
+ ___46-[UARPAccessoryMetadataStore clearAllMetadata]_block_invoke.cold.2
+ ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.139
+ ___48-[UARPAccessoryMetadataStore loadMetadataStore:]_block_invoke
+ ___48-[UARPAccessoryMetadataStore loadMetadataStore:]_block_invoke.cold.1
+ ___48-[UARPAccessoryMetadataStore updateiCloudToken:]_block_invoke
+ ___48-[UARPAccessoryMetadataStore updateiCloudToken:]_block_invoke.cold.1
+ ___48-[UARPController copyChipMetadataForRecordName:]_block_invoke
+ ___48-[UARPController copyChipMetadataForRecordName:]_block_invoke.cold.1
+ ___48-[UARPController copyChipMetadataForRecordName:]_block_invoke.cold.2
+ ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.147
+ ___51-[UARPControllerXPC getSupportedAccessoriesFileURL]_block_invoke
+ ___51-[UARPControllerXPC getSupportedAccessoriesFileURL]_block_invoke.141
+ ___54-[UARPController subscribeForChipSupportedAccessories]_block_invoke
+ ___56-[UARPAccessoryMetadataStore copyMetadataForRecordName:]_block_invoke
+ ___56-[UARPAccessoryMetadataStore copyMetadataForRecordName:]_block_invoke.cold.1
+ ___56-[UARPAccessoryMetadataStore copyMetadataForRecordName:]_block_invoke.cold.2
+ ___56-[UARPAccessoryMetadataStore copyMetadataForRecordName:]_block_invoke.cold.3
+ ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.149
+ ___60-[UARPAccessoryMetadataStore updateMetadata:deleteMetadata:]_block_invoke
+ ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.143
+ ___61-[UARPControllerXPC getSupportedAccessories:forProductGroup:]_block_invoke.145
+ ___UARPStringChipRecordCacheFilepath_block_invoke
+ ___block_descriptor_40_e8_32r_e15_v16?0"NSURL"8lr32l8
+ ___block_literal_global.1011
+ ___block_literal_global.1013
+ ___block_literal_global.1021
+ ___block_literal_global.1026
+ ___block_literal_global.1031
+ ___block_literal_global.923
+ ___block_literal_global.925
+ ___block_literal_global.930
+ ___block_literal_global.935
+ ___block_literal_global.940
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kUARPStringChipMetadata
+ _kUARPStringPersonalizationOptionProductType
+ _objc_autorelease
+ _objc_msgSend$accessQueue
+ _objc_msgSend$accessoryCategoryNumber
+ _objc_msgSend$accessoryInstallationGuideURL
+ _objc_msgSend$accessoryMarketingName
+ _objc_msgSend$accessoryMetadataURLForFileIndex:
+ _objc_msgSend$accessoryMetadataURLForRecordName:
+ _objc_msgSend$accessoryProductLabel
+ _objc_msgSend$availabilityNotificationForSupportedAccessoriesFilePosted:
+ _objc_msgSend$companyLegalName
+ _objc_msgSend$companyPreferredName
+ _objc_msgSend$copyMetadataForRecordName:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dictionaryFromMetadata
+ _objc_msgSend$getSupportedAccessoriesFileURL
+ _objc_msgSend$getSupportedAccessoriesFileURL:
+ _objc_msgSend$hashRecordNameToFileIndex:
+ _objc_msgSend$loadMetadataFromPlist:
+ _objc_msgSend$loadMetadataFromPlistForFileIndex:
+ _objc_msgSend$loadMetadataStore:
+ _objc_msgSend$recordName
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$saveMetadataToPlist:fileIndex:
+ _objc_msgSend$unregisterForSupportedAccessoriesFileAvailability:
+ _objc_msgSend$updateCache:forKey:
+ _objc_msgSend$vendorName
- GCC_except_table189
- GCC_except_table192
- GCC_except_table199
- GCC_except_table209
- GCC_except_table214
- GCC_except_table221
- GCC_except_table36
- GCC_except_table40
- ___34-[UARPControllerXPC xpcConnection]_block_invoke.113
- ___34-[UARPControllerXPC xpcConnection]_block_invoke_2.115
- ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.136
- ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.142
- ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.144
- ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.138
- ___61-[UARPControllerXPC getSupportedAccessories:forProductGroup:]_block_invoke.140
- ___block_literal_global.1008
- ___block_literal_global.1010
- ___block_literal_global.1018
- ___block_literal_global.1023
- ___block_literal_global.920
- ___block_literal_global.922
- ___block_literal_global.927
- ___block_literal_global.932
- ___block_literal_global.937
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%s: Cannot start Tap To Radar - urlForAssets directory is nil"
+ "%s: Cleaning UARP logs directory: %@ (removing files older than 3 days)"
+ "%s: Cleaning crash analytics logs directory: %@ (removing files older than 7 days)"
+ "%s: Cleaning tap-to-radar directory: %@ (removing all files)"
+ "%s: Completed cleanup of aged files for Tap To Radar"
+ "%s: Failed to load CHIP metadata cache from %{public}@"
+ "%s: Starting cleanup of aged files for Tap To Radar"
+ "%s: Unable to retrieve CHIP metadata cache"
+ "%s: availability notification for supported accessories file"
+ "%s: unregistered for SupportedAccessoriesFileAvailability"
+ "-[UARPController availabilityNotificationForSupportedAccessoriesFilePosted:]"
+ "-[UARPController copyChipMetadataForRecordName:]_block_invoke"
+ "-[UARPController unregisterForSupportedAccessoriesFileAvailability:]"
+ "-[UARPControllerXPC getSupportedAccessoriesFileURL]"
+ "-[UARPUploaderUARP startTapToRadar:]"
+ "@\"NSURL\"16@0:8"
+ "@\"UARPAccessoryMetadataStore\""
+ "Attempted to clear read-only metadata"
+ "Attempted to load external writable metadata store"
+ "Attempted to save read-only metadata"
+ "Attempted to set read-only iCloud token"
+ "Attempted to set read-only metadata"
+ "B32@0:8@16Q24"
+ "Could not read iCloud token"
+ "Empty recordName provided for Accessory Metadata lookup"
+ "Error deleting metadata directory with error %{public}@"
+ "Failed to clear cache files from %{public}@"
+ "Failed to create directory %{public}@ with error %{public}@"
+ "Failed to write iCloud token to file"
+ "Failed to write metadata to %{public}@ with %{public}@"
+ "Invalid record name %{public}@"
+ "LuckESeed"
+ "Missing file from metadata cache detected. Clearing iCloud token"
+ "No metadata file found for %{public}@"
+ "No metadata found for record name %{public}@"
+ "No metadata records provided for update"
+ "ProductType"
+ "Q24@0:8@16"
+ "Record %{public}@ missing metadata"
+ "T@\"NSData\",C,V_iCloudChangeToken"
+ "T@\"NSMutableDictionary\",R,V_metadataCache"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_accessQueue"
+ "T@\"NSObject<OS_os_log>\",R,V_log"
+ "T@\"NSURL\",R,V_metadataDirectoryURL"
+ "T@\"NSURL\",R,V_tokenFileURL"
+ "TB,R,V_isReadOnly"
+ "Token file does not exist at path %{public}@"
+ "UARPAccessoryMetadataStore"
+ "Writing %{public}lu records to file"
+ "_accessQueue"
+ "_dev"
+ "_iCloudChangeToken"
+ "_isReadOnly"
+ "_metadataCache"
+ "_metadataDirectoryURL"
+ "_metadataStore"
+ "_supportedAccessoryFileListToken"
+ "_tokenFileURL"
+ "accessQueue"
+ "accessoryMetadataURLForFileIndex:"
+ "accessoryMetadataURLForRecordName:"
+ "availabilityNotificationForSupportedAccessoriesFilePosted:"
+ "chipAccessoryMetadata-%lu.plist"
+ "chipAccessoryMetadataiCloud.token"
+ "chip_metadata"
+ "clearAllMetadata"
+ "com.apple.UARPAccessoryMetadataStore.access"
+ "com.apple.accessoryUpdater.uarp.supportedAccessoriesMetadataFileAvailable"
+ "copyChipMetadataForRecordName:"
+ "copyMetadataForRecordName:"
+ "copyiCloudToken"
+ "dataUsingEncoding:"
+ "dictionaryFromMetadata"
+ "getSupportedAccessoriesFileURL"
+ "getSupportedAccessoriesFileURL:"
+ "hashRecordNameToFileIndex:"
+ "iCloudChangeToken"
+ "initWithDirectory:"
+ "isReadOnly"
+ "legacy"
+ "loadMetadataFromPlist:"
+ "loadMetadataFromPlistForFileIndex:"
+ "loadMetadataFromPlistForRecordName:"
+ "loadMetadataStore:"
+ "metadataCache"
+ "metadataDirectoryURL"
+ "nil key passed to accessory metadata cache"
+ "recordName"
+ "removeItemAtURL:error:"
+ "saveMetadataToPlist:fileIndex:"
+ "setICloudChangeToken:"
+ "subscribeForChipSupportedAccessories"
+ "tokenFileURL"
+ "unregisterForSupportedAccessoriesFileAvailability:"
+ "updateCache:forKey:"
+ "updateMetadata:deleteMetadata:"
+ "updateiCloudToken:"
+ "v16@?0@\"NSURL\"8"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSURL\">16"
+ "\xf0q"
- "LuckD"
- "\xf0Q"

```
