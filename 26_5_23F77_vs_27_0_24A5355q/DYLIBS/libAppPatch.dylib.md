## libAppPatch.dylib

> `/usr/lib/libAppPatch.dylib`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0x150c8
-  __TEXT.__auth_stubs: 0xd00
+1655.0.0.0.0
+  __TEXT.__text: 0x14b8c
   __TEXT.__objc_methlist: 0x4ec
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x5a79
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x5a7e
   __TEXT.__oslogstring: 0x23a
   __TEXT.__gcc_except_tab: 0x2f8
-  __TEXT.__unwind_info: 0x3d0
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0x1826
-  __TEXT.__objc_methtype: 0x44e
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x150
+  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3720
   __AUTH_CONST.__objc_const: 0x278
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5BC07FE-6338-3880-97A2-A43EFCC49937
-  Functions: 237
-  Symbols:   960
-  CStrings:  1274
+  UUID: 20D8CE59-BA20-3DD6-87A8-2B50CC6CB291
+  Functions: 235
+  Symbols:   957
+  CStrings:  1036
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"NSError\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8r*16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8r*16Q24"
- "@36@0:8@16B24@?28"
- "@36@0:8@16B24^@28"
- "@40@0:8@16B24B28^@32"
- "@44@0:8r*16@24B32^@36"
- "@48@0:8@16@24S32i36^@40"
- "@48@0:8@16q24@32^@40"
- "@52@0:8@16q24@32i40^@44"
- "@52@0:8@16q24i32@36^@44"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16^@24"
- "B36@0:8@16B24^@28"
- "B36@0:8@16I24^I28"
- "B36@0:8@16S24^@28"
- "B36@0:8r*16B24^@28"
- "B40@0:8@16@24^@32"
- "B40@0:8@16B24S28^@32"
- "B40@0:8@16I24I28^@32"
- "B40@0:8@16^i24^@32"
- "B40@0:8^{?=[16C][16c][1024c]}16@24^@32"
- "B44@0:8@16@24B32^@36"
- "B44@0:8@16@24C32^@36"
- "B44@0:8@16B24S28i32^@36"
- "B44@0:8@16B24^@28@?36"
- "B44@0:8@16i24@?28^@36"
- "B44@0:8S16@20@28^@36"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24^@32@?40"
- "B48@0:8r*16@24@32^@40"
- "B52@0:8@16@24@32i40^@44"
- "B52@0:8@16@24B32B36B40^@44"
- "B52@0:8@16@24i32@36^@44"
- "B56@0:8@16I24I28B32B36^B40^@48"
- "B56@0:8@16^{_BOMCopier=}24^Q32^Q40^@48"
- "B56@0:8r*16I24I28S32I36i40B44^@48"
- "B60@0:8r*16i24I28I32S36I40i44B48^@52"
- "B68@0:8@16@24@32i40I44I48^B52^@60"
- "B72@0:8@16@24@32I40I44i48B52^B56^@64"
- "B72@0:8@16@24@32i40I44I48i52^B56^@64"
- "MIBOMWrapper"
- "MIFileManager"
- "MIFileManagerCopyfileContext"
- "MI_allAccessURLs"
- "MI_dictionaryWithContentsOfURL:options:error:"
- "MI_writeToURL:format:options:error:"
- "MobileInstallationAdditions"
- "Q24@0:8@16"
- "T@\"NSError\",&,N,V_error"
- "TB,N,V_ignoreErrors"
- "TB,R"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "UTF8String"
- "_bulkSetPropertiesForPath:existingFD:UID:GID:mode:flags:dataProtectionClass:removeACL:error:"
- "_copyItemAtURL:toURL:failIfSrcMissing:alwaysClone:ignoreErrors:error:"
- "_countFilesAndBytesInArchiveAtURL:withBOMCopier:totalFiles:totalUncompressedBytes:error:"
- "_dataForExtendedAttributeNamed:length:onURL:orFD:error:"
- "_error"
- "_firstAvailableParentForURL:error:"
- "_ignoreErrors"
- "_insecureCachedAppIdentifierIfMarkedWithEAFlag:bundleURL:allowPlaceholders:error:"
- "_itemIsType:withDescription:atURL:error:"
- "_markEAFlag:forAppIdentifier:insecurelyCachedOnBundle:error:"
- "_moveItemAtURL:toURL:failIfSrcMissing:error:"
- "_realPathForURL:allowNonExistentPathComponents:"
- "_realPathWhatExistsInPath:isDirectory:"
- "_removeACLAtPath:isDir:error:"
- "_sanitizeFilePathForVarOrTmpSymlink:error:"
- "_setData:forExtendedAttributeNamed:onURL:orFD:error:"
- "_stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:"
- "_traverseUntilFirstAvailableParentOfURL:withBlock:"
- "_validateSymlink:withStartingDepth:andEndingDepth:"
- "aclTextFromURL:error:"
- "addObject:"
- "allKeys"
- "allObjects"
- "appendFormat:"
- "appendString:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "boolValue"
- "bulkSetPropertiesForPath:UID:GID:mode:flags:dataProtectionClass:removeACL:error:"
- "bulkSetPropertiesForPath:withOpenFD:UID:GID:mode:flags:dataProtectionClass:removeACL:error:"
- "bundleAtURLIsPlaceholder:"
- "bytes"
- "captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
- "clearExtendedAttributesAtURL:error:"
- "clearPlaceholderStatusForBundle:withError:"
- "code"
- "containsDotDotPathComponents"
- "containsObject:"
- "containsString:"
- "copy"
- "copyItemAtURL:toURL:alwaysClone:error:"
- "copyItemAtURL:toURL:error:"
- "copyItemIfExistsAtURL:toURL:error:"
- "copyItemIgnoringErrorsAtURL:toURL:error:"
- "copyVolumeInfo:forURL:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:class:error:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:error:"
- "createRelativeDirectoryPath:inBaseDirectory:mode:class:error:"
- "createSymbolicLinkAtURL:withDestinationURL:error:"
- "createTemporaryDirectoryInDirectoryURL:error:"
- "dataForExtendedAttributeNamed:length:fromFD:fdLocation:error:"
- "dataForExtendedAttributeNamed:length:fromURL:error:"
- "dataProtectionClassOfItemAtURL:class:error:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithContentsOfURL:options:error:"
- "dataWithLength:"
- "dateWithTimeIntervalSince1970:"
- "debugDescriptionForItemAtURL:"
- "defaultManager"
- "destinationOfSymbolicLinkAtURL:error:"
- "deviceForURLOrFirstAvailableParent:error:"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "diskUsageForURL:"
- "domain"
- "enumerateExtendedAttributeNamesAtURL:includeCompression:error:enumerator:"
- "enumerateExternalVolumesWithBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "extendedAttributesFromURL:error:"
- "extendedAttributesFromURL:includeCompression:error:"
- "extractZipArchiveAtURL:toURL:withError:"
- "extractZipArchiveAtURL:toURL:withError:extractionProgressBlock:"
- "fileHandleForReadingFromURL:error:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPathComponents:"
- "hasPrefix:"
- "hashTableWithOptions:"
- "i32@0:8@16^@24"
- "ignoreErrors"
- "initWithBytes:length:encoding:"
- "initWithContentsOfURL:options:error:"
- "initWithData:encoding:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithUUIDBytes:"
- "insecureCachedAppIdentifierIfAppClipForBundle:error:"
- "insecureCachedAppIdentifierIfValidatedByFreeProfileForBundle:error:"
- "installTypeFromExtendedAttributeOnBundle:error:"
- "isEqual:"
- "isEqualToString:"
- "itemDoesNotExistAtURL:"
- "itemDoesNotExistOrIsNotDirectoryAtURL:"
- "itemExistsAtURL:"
- "itemExistsAtURL:error:"
- "itemIsDirectoryAtURL:error:"
- "itemIsFIFOAtURL:error:"
- "itemIsFileAtURL:error:"
- "itemIsSocketAtURL:error:"
- "itemIsSymlinkAtURL:error:"
- "lastPathComponent"
- "length"
- "logAccessPermissionsForURL:"
- "markBundleAsPlaceholder:withError:"
- "modificationDateForURL:error:"
- "mountPointForURL:error:"
- "mountPointForVolumeUUID:error:"
- "moveItemAtURL:toURL:error:"
- "moveItemIfExistsAtURL:toURL:error:"
- "mutableBytes"
- "mutableCopy"
- "null"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "path"
- "pathComponents"
- "pathExtension"
- "pathWithComponents:"
- "propertyListWithData:options:format:error:"
- "readDataUpToLength:error:"
- "realPathForURL:allowNonExistentPathComponents:isDirectory:error:"
- "realPathForURL:ifChildOfURL:"
- "removeExtendedAttributeNamed:fromURL:error:"
- "removeItemAtURL:error:"
- "removeItemAtURL:keepParent:error:"
- "removeObjectForKey:"
- "secureRenameFromSourceURL:toDestinationURL:destinationStatus:error:"
- "setAppClipAppIdentifier:insecurelyCachedOnBundle:error:"
- "setData:forExtendedAttributeNamed:onFD:fdLocation:error:"
- "setData:forExtendedAttributeNamed:onURL:error:"
- "setDataProtectionClassOfItemAtURL:toClass:ifPredicate:error:"
- "setError:"
- "setIgnoreErrors:"
- "setInstallType:inExtendedAttributeOnBundle:error:"
- "setModificationDateToNowForURL:error:"
- "setObject:forKeyedSubscript:"
- "setOwnerOfURL:toUID:gid:error:"
- "setOwnershipAtURL:toUID:gid:error:"
- "setPermissionsForURL:toMode:error:"
- "setValidatedByFreeProfileAppIdentifier:insecurelyCachedOnBundle:error:"
- "setWithArray:"
- "stageURL:toItemName:inStagingDir:stagingMode:settingUID:gid:hasSymlink:error:"
- "stageURLByMoving:toItemName:inStagingDir:settingUID:gid:dataProtectionClass:breakHardlinks:hasSymlink:error:"
- "standardizeOwnershipAtURL:toUID:GID:removeACLs:setProtectionClass:foundSymlink:error:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringWithFileSystemRepresentation:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "traverseDirectoryAtURL:withBlock:"
- "unsignedLongLongValue"
- "upToFirstFourBytesFromURL:error:"
- "urlsForItemsInDirectoryAtURL:ignoringSymlinks:error:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateSymlinksInURLDoNotEscapeURL:error:"
- "volumeUUIDForURL:error:"

```
