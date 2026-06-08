## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.122.1.0.0
-  __TEXT.__text: 0x1f120
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x55c
-  __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x6c54
-  __TEXT.__oslogstring: 0x2cf6
-  __TEXT.__gcc_except_tab: 0x964
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x1908
-  __TEXT.__objc_methtype: 0x250
-  __TEXT.__objc_stubs: 0x1e00
-  __DATA_CONST.__got: 0x2c0
+2215.0.0.502.1
+  __TEXT.__text: 0x1e420
+  __TEXT.__objc_methlist: 0x56c
+  __TEXT.__const: 0x510
+  __TEXT.__cstring: 0x6e91
+  __TEXT.__oslogstring: 0x2e15
+  __TEXT.__gcc_except_tab: 0x9a8
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc50
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__const: 0x450
-  __AUTH_CONST.__cfstring: 0x7720
+  __DATA_CONST.__objc_arraydata: 0x340
+  __DATA_CONST.__got: 0x2c8
+  __AUTH_CONST.__const: 0x470
+  __AUTH_CONST.__cfstring: 0x7920
   __AUTH_CONST.__objc_const: 0x6e8
   __AUTH_CONST.__objc_intobj: 0x948
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x688
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0xb8
-  __DATA.__bss: 0x208
+  __DATA.__bss: 0x218
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03012D41-A4A8-3F09-8B23-23278B1A9D9E
-  Functions: 426
-  Symbols:   1388
-  CStrings:  2485
+  UUID: 0544EAC1-AE45-39FE-9751-F986F317CB79
+  Functions: 430
+  Symbols:   1407
+  CStrings:  2185
 
Symbols:
+ -[SecureMobileAssetBundle _graftedContentsContainAppBundle]
+ -[SecureMobileAssetBundle ungraftOrUnmount:force:ungraftingError:]
+ -[SecureMobileAssetBundle ungraftWithForce:error:]
+ -[SecureMobileAssetBundle unmountWithForce:error:]
+ GCC_except_table116
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table73
+ GCC_except_table90
+ _NSURLFileSizeKey
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1322
+ ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.503
+ ___block_literal_global.1269
+ ___block_literal_global.1275
+ ___block_literal_global.1313
+ ___block_literal_global.1314
+ ___block_literal_global.1351
+ ___block_literal_global.1357
+ ___block_literal_global.1362
+ ___block_literal_global.1367
+ ___block_literal_global.1372
+ ___block_literal_global.1377
+ ___block_literal_global.1382
+ ___block_literal_global.1401
+ ___block_literal_global.1494
+ ___block_literal_global.1616
+ ___block_literal_global.1622
+ ___block_literal_global.1627
+ ___block_literal_global.1638
+ ___block_literal_global.1643
+ ___block_literal_global.1665
+ ___block_literal_global.1769
+ ___block_literal_global.2324
+ ___block_literal_global.3033
+ ___block_literal_global.3035
+ ___block_literal_global.3037
+ ___block_literal_global.3039
+ ___block_literal_global.3041
+ ___block_literal_global.3080
+ ___block_literal_global.3093
+ ___fileAlignmentAssetTypes_block_invoke
+ _fileAlignmentAssetTypes
+ _fileAlignmentAssetTypes.cold.1
+ _fileAlignmentAssetTypes.fileAlignmentAssetTypes
+ _fileAlignmentAssetTypes.once
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$ungraftOrUnmount:force:ungraftingError:
+ _objc_msgSend$ungraftWithForce:error:
+ _objc_msgSend$unmountWithForce:error:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _totalSizeOfDirectoryAtPath
- -[SecureMobileAssetBundle ungraft:]
- -[SecureMobileAssetBundle ungraftOrUnmount:ungraftingError:]
- -[SecureMobileAssetBundle unmount:]
- GCC_except_table109
- GCC_except_table114
- GCC_except_table47
- GCC_except_table50
- GCC_except_table55
- GCC_except_table57
- GCC_except_table72
- GCC_except_table87
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1281
- ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.479
- ___block_literal_global.1227
- ___block_literal_global.1233
- ___block_literal_global.1268
- ___block_literal_global.1273
- ___block_literal_global.1274
- ___block_literal_global.1279
- ___block_literal_global.1284
- ___block_literal_global.1289
- ___block_literal_global.1294
- ___block_literal_global.1299
- ___block_literal_global.1318
- ___block_literal_global.1411
- ___block_literal_global.1533
- ___block_literal_global.1539
- ___block_literal_global.1544
- ___block_literal_global.1555
- ___block_literal_global.1560
- ___block_literal_global.1582
- ___block_literal_global.1713
- ___block_literal_global.2268
- ___block_literal_global.2950
- ___block_literal_global.2952
- ___block_literal_global.2954
- ___block_literal_global.2956
- ___block_literal_global.2958
- ___block_literal_global.2997
- ___block_literal_global.3010
- _objc_msgSend$ungraft:
- _objc_msgSend$ungraftOrUnmount:ungraftingError:
- _objc_msgSend$unmount:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Applications"
+ "AutoSet-CheckMetadata"
+ "BuildIdentities"
+ "[SMA] Checked %@ for .app bundles: found=%@"
+ "[SMA] Cryptex at %@ has unexpected protection class (expected Class D)"
+ "[SMA] Failed to list contents of %@: %@"
+ "[SMA] Ungrafting %@ with force=%@"
+ "[SMA] Unmounting %@ with force=%@"
+ "app"
+ "com.apple.MobileAsset.PSUSConfig.AutoAssetSetTargets"
+ "com.apple.MobileAsset.SecureAssetManager01.Test"
+ "com.apple.MobileAsset.SecureAssetManager02.Test"
+ "com.apple.MobileAsset.SecureAssetManager03.Test"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.FM.Visual"
+ "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.Integration.Test"
+ "com.apple.MobileAsset.UAF.Photos.MagicCleanup"
+ "com.apple.MobileAsset.UAF.Siri.Understanding"
+ "totalSizeOfDirectoryAtPath: failed to get file size for %@: \n%@"
+ "unmountFlags"
- ".cxx_destruct"
- "@\"MAAssetTypeDescriptor\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"SecureMobileAssetManifestVerifier\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^?16"
- "@24@0:8^@16"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8^I16"
- "B24@0:8^q16"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8^q16^@24"
- "B36@0:8@16B24^@28"
- "B40@0:8@16^q24^@32"
- "B40@0:8^I16@24@32"
- "B44@0:8@16Q24B32^@36"
- "B44@0:8Q16I24^@28^@36"
- "B48@0:8Q16^@24^@32^@40"
- "B56@0:8@16@24Q32^@40^@48"
- "I16@0:8"
- "MASecureMobileAssetTypes"
- "Q"
- "Q16@0:8"
- "SMABundleAccessOptions"
- "SecureMAHelper"
- "SecureMobileAssetBundle"
- "SecureMobileAssetManifestVerifier"
- "T@\"MAAssetTypeDescriptor\",R,V_typeDescriptor"
- "T@\"NSDictionary\",&,V_types"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableDictionary\",&,V_cachedManifestVerificationResults"
- "T@\"NSObject<OS_dispatch_queue>\",R"
- "T@\"NSSet\",&,N,V_pathsToPurgeOnGraftFailureInEarlyBootTask"
- "T@\"NSString\",R"
- "T@\"NSString\",R,N"
- "T@\"SecureMobileAssetManifestVerifier\",&,V_manifestVerifier"
- "TB,N,V_darwinOnly"
- "TB,R,N"
- "TI,R"
- "TQ,N,V_flags"
- "TQ,R,D,N"
- "T^?,N,V_logger"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "^?"
- "^?16@0:8"
- "_assetAttributes"
- "_assetBundlePath"
- "_assetInfoPlist"
- "_assetSpecifier"
- "_assetType"
- "_beginAccessWithOptions_nowait:accessMechanismPtr:errorPtr:"
- "_cachedManifestVerificationResults"
- "_cryptexInfoPlist"
- "_darwinOnly"
- "_flags"
- "_generateNonceProposalForHandle:digest:nonce:error:"
- "_loadTypes"
- "_logBase64Data:description:"
- "_logger"
- "_manifestDataFromStoredTicket:manifestType:"
- "_manifestDigest:"
- "_manifestVerifier"
- "_pathsToPurgeOnGraftFailureInEarlyBootTask"
- "_personalize:error:"
- "_personalizedBundleTicketData"
- "_queryNonceForHandle:domain:digest:error:"
- "_shouldForcePersonalizationFailure"
- "_storeManifest:manifestType:stage:error:"
- "_typeDescriptor"
- "_types"
- "_verifyPlist:manifest:manifestType:result:"
- "accessPath"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "allObjects"
- "appendFormat:"
- "appendString:"
- "arrayWithObjects:count:"
- "assetAttributes"
- "assetBundlePath"
- "assetIsSecureMobileAsset:"
- "assetSpecifier"
- "assetValues"
- "attach:error:"
- "attributesOfErrorForDomain:withCode:codeName:"
- "base64EncodedStringWithOptions:"
- "beginAccessWithOptions:accessMechanismPtr:errorPtr:"
- "boolValue"
- "buildVersion"
- "bundleAccessPermitted:"
- "bundleWithPath:"
- "bytes"
- "cachedManifestVerificationResults"
- "characterSetWithCharactersInString:"
- "checkedDescription"
- "clearBootTaskPlist"
- "clearBootTaskPlist:"
- "commitStagedManifestsForSelectors:darwinOnly:error:"
- "commitStagedManifestsForSelectors:error:"
- "commonPrefixWithString:options:"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "componentsSeparatedByString:"
- "containsObject:"
- "containsString:"
- "copy"
- "copyBootTaskPlist:"
- "copyItemAtPath:toPath:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createSymbolicLinkAtPath:withDestinationPath:error:"
- "currentCalendar"
- "currentTotalWritten"
- "darwinOnly"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithContentsOfFile:options:error:"
- "dataWithContentsOfURL:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dateByAddingComponents:toDate:options:"
- "dateFromString:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "depersonalize:"
- "description"
- "descriptorForAssetType:"
- "devnodesForDiskImageID:error:"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "doubleValue"
- "endAccessWithOptions:accessMechanismPtr:errorPtr:"
- "endAccessWithOptions_nowait:accessMechanismPtr:errorPtr:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumeratorAtPath:"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "filterUsingPredicate:"
- "finishDecoding"
- "flags"
- "fsTag:forAssetType:specifier:"
- "getBootTaskPlistLock"
- "getSigningServerURL:"
- "graft:"
- "graftOrMount:graftingError:"
- "graftSecureAssetsFromLastBootSession"
- "graftdmgType"
- "hasPrefix:"
- "hasSuffix:"
- "host"
- "i48@0:8@16@24Q32^@40"
- "init"
- "initForReadingFromData:error:"
- "initWithArray:"
- "initWithBase64EncodedString:options:"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithCapacity:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithLocaleIdentifier:"
- "initWithLogger:"
- "initWithLong:"
- "initWithPath:"
- "initWithString:"
- "insecureInfoPlist"
- "insecureInfoPlistPath"
- "insertObject:atIndex:"
- "intValue"
- "integerValue"
- "integrityCatalogPath"
- "invertedSet"
- "isAccessible"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isErrorDueToDeviceBeingLocked:"
- "isGrafted"
- "isGraftedPath:"
- "isMappableToExclaves:"
- "isMounted"
- "isPersonalized"
- "isPersonalized:"
- "isPersonalizedManifestStaged"
- "isPersonalizedManifestStaged:"
- "isSecureMobileAsset"
- "keyEnumerator"
- "lastPathComponent"
- "length"
- "loadTrustCache:"
- "localizedDescription"
- "log:"
- "logger"
- "longLongValue"
- "longValue"
- "lowercaseString"
- "manifestPathForAssetType:specifier:"
- "manifestType"
- "manifestVerifier"
- "mapToExclaves:"
- "mount:"
- "mutableCopy"
- "nextObject"
- "numNoLongerStalled"
- "numStalled"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pathComponents"
- "pathExtension"
- "pathForResource:ofType:"
- "pathWithComponents:"
- "pathsToPurgeOnGraftFailureInEarlyBootTask"
- "personalizationQueue"
- "personalize:completionQueue:completion:"
- "personalize:error:"
- "predicateWithBlock:"
- "propertyListWithData:options:format:error:"
- "rangeOfCharacterFromSet:"
- "rangeOfString:"
- "readBootTaskPlist:"
- "recordAssetGraftStateForEarlyBootTask:options:"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObjectForKey:"
- "replaceOccurrencesOfString:withString:options:range:"
- "scheme"
- "secureAssetDataPath"
- "secureInfoPlist"
- "secureInfoPlistPath"
- "secureMountAuthType"
- "set"
- "setByAddingObjectsFromSet:"
- "setCachedManifestVerificationResults:"
- "setDarwinOnly:"
- "setDateFormat:"
- "setDay:"
- "setFlags:"
- "setLocale:"
- "setLogger:"
- "setManifestVerifier:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPathsToPurgeOnGraftFailureInEarlyBootTask:"
- "setSafeObject:forKey:"
- "setTimeZone:"
- "setTypes:"
- "setValue:forKey:"
- "setWithArray:"
- "sharedCore"
- "sharedDevice"
- "sharedInstance"
- "skipDescendants"
- "stageManifest:infoPlist:error:"
- "stagedManifestPathForAssetType:specifier:"
- "stagedPersonalizedManifestPath"
- "storeManifest:infoPlist:error:"
- "storeManifest:manifestType:infoPlist:stage:error:"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringFromDate:"
- "stringIsEqual:to:"
- "stringValue"
- "stringWithCString:encoding:"
- "stringWithCapacity:"
- "stringWithContentsOfFile:encoding:error:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringWithRange:"
- "supportsDarwin:"
- "supportsLoadableTrustCache:"
- "timeZoneWithAbbreviation:"
- "typeDescriptor"
- "types"
- "ungraft:"
- "ungraftOrUnmount:ungraftingError:"
- "unmapFromExclaves:"
- "unmount:"
- "unsignedIntValue"
- "useDomain:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^?16"
- "v28@0:8B16@20"
- "v32@0:8@16@24"
- "v40@0:8@16@24@?32"
- "verifyManifest:manifestType:"
- "verifyPlist:manifest:manifestType:result:error:"
- "whitespaceAndNewlineCharacterSet"
- "writeToFile:atomically:"
- "writeToFile:atomically:encoding:error:"
- "writeToFile:options:error:"

```
