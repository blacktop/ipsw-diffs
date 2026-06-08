## AppleDeviceQuerySupport

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport`

```diff

-408.120.3.0.0
-  __TEXT.__text: 0xb46c
-  __TEXT.__auth_stubs: 0x5b0
+458.0.0.0.0
+  __TEXT.__text: 0xba50
   __TEXT.__objc_methlist: 0x460
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__cstring: 0x474c
+  __TEXT.__gcc_except_tab: 0x45c
+  __TEXT.__cstring: 0x48ec
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0xf8a
-  __TEXT.__objc_methtype: 0x2fe
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x160
+  __TEXT.__unwind_info: 0x268
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x3520
+  __AUTH_CONST.__cfstring: 0x3640
   __AUTH_CONST.__objc_const: 0x718
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0xb40
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3DE49C1-E9A3-3C8F-A1A2-6FE6C3DC1634
-  Functions: 181
-  Symbols:   828
-  CStrings:  1160
+  UUID: 214F412D-EE25-3564-9030-1CF2F16EF3CB
+  Functions: 192
+  Symbols:   867
+  CStrings:  951
 
Symbols:
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table68
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.237
+ ___block_literal_global.258
+ ___getcryptex_copy_list_4MSMSymbolLoc_block_invoke
+ ___getcryptex_msm_array_destroySymbolLoc_block_invoke
+ ___getcryptex_msm_get_stringSymbolLoc_block_invoke
+ ___libcryptexLibraryCore_block_invoke
+ _getZhuGeCryptexPathsWithError
+ _getZhuGeCryptexPathsWithError.cold.1
+ _getZhuGeCryptexPathsWithError.cold.2
+ _getcryptex_copy_list_4MSMSymbolLoc
+ _getcryptex_copy_list_4MSMSymbolLoc.ptr
+ _getcryptex_msm_array_destroySymbolLoc
+ _getcryptex_msm_array_destroySymbolLoc.ptr
+ _getcryptex_msm_get_stringSymbolLoc
+ _getcryptex_msm_get_stringSymbolLoc.ptr
+ _libcryptexLibrary
+ _libcryptexLibraryCore
+ _libcryptexLibraryCore.frameworkLibrary
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _pcryptex_msm_get_string
+ _pcryptex_msm_get_string.cold.1
+ _strerror
- GCC_except_table48
- GCC_except_table52
- GCC_except_table54
- GCC_except_table56
- ___block_literal_global.228
- ___block_literal_global.249
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "(DEPRECATED SOON!)"
+ "/usr/lib/libcryptex.dylib"
+ "/usr/local/lib/libcryptex.dylib"
+ "Added %s to Cryptex paths array"
+ "DEPRECATED_SOON"
+ "Failed to copy cryptex list, error %d(%s)"
+ "Failed to get Cryptex paths"
+ "Failed to link libcryptex.dylib!"
+ "For key: \"%@\"%@, value: %@, error: %@"
+ "In bulk query, for key: \"%@\"%@, value: %@, error: %@"
+ "ZhuGe-458"
+ "com.apple.FactoryCryptexSupport"
+ "cryptexIdentifier pointer is nil!"
+ "cryptex_copy_list_4MSM"
+ "cryptex_msm_array_destroy"
+ "cryptex_msm_get_string"
+ "getZhuGeCryptexPathsWithError"
+ "is_deprecatedSoon"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"ZhuGeCache\""
- "@16@0:8"
- "@20@0:8c16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@28@0:8@16B24"
- "@32@0:8@16^@24"
- "@32@0:8Q16@24"
- "@40@0:8@16@24#32"
- "@40@0:8Q16Q24B32B36"
- "@48@0:8@16Q24q32B40B44"
- "B16@0:8"
- "B24@0:8@16"
- "B40@0:8@16@24^@32"
- "For key: \"%@\", value: %@, error: %@"
- "In bulk query, for key: \"%@\", value: %@, error: %@"
- "T#,R,V_cacheType"
- "T@\"NSMutableArray\",&"
- "T@\"NSMutableArray\",R,V_cacheList"
- "T@\"NSMutableDictionary\",R,V_cacheDict"
- "T@\"NSNumber\",R,V_capacity"
- "T@\"NSString\",R,V_name"
- "T@\"NSXPCConnection\",&"
- "T@\"ZhuGeCache\",&,V_keysCacheForCopyValue"
- "TB"
- "T^?,V_logHandler"
- "T^v"
- "UTF8String"
- "ZhuGe"
- "ZhuGe-408.120.3"
- "ZhuGeCache"
- "ZhuGeDescription"
- "ZhuGeInternalServiceProtocol"
- "ZhuGeInternalSupportAssistant"
- "ZhuGeLocker"
- "ZhuGeRestoreLog"
- "ZhuGeRestoreLogProtocol"
- "ZhuGeServiceProtocol"
- "ZhuGeSingleton"
- "ZhuGeSupportAssistant"
- "^?"
- "^?16@0:8"
- "^v16@0:8"
- "^v24@0:8^@16"
- "^{_opaque_pthread_mutex_t=q[56c]}16@0:8"
- "_ZhuGeDescriptionWithLayer:"
- "_cacheDict"
- "_cacheList"
- "_cacheType"
- "_capacity"
- "_keysCacheForCopyValue"
- "_logHandler"
- "_name"
- "aRecursiveMutex"
- "accessInstanceVariablesDirectly"
- "activate"
- "addEntriesFromDictionary:"
- "addObject:"
- "allKeys"
- "appendBytes:length:"
- "appendFormat:"
- "armoryClassName"
- "arrayFromShellCommandString:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "boolFromData:needNegate:"
- "boolValue"
- "bytes"
- "cStringUsingEncoding:"
- "cacheDict"
- "cacheList"
- "cacheType"
- "callStackSymbols"
- "capacity"
- "ccccValue"
- "characterAtIndex:"
- "characterSetWithCharactersInString:"
- "classList"
- "clearCache"
- "code"
- "componentsJoinedByString:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataFromHexString:"
- "dataWithLength:"
- "defaultManager"
- "delCacheForKey:"
- "description"
- "descriptionFromZhuGeErrorCode:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "dylibHandler"
- "errorWithDomain:code:userInfo:"
- "errorWithZhuGeErrorCode:underlyingError:"
- "executeCacheRefresh"
- "fileExistsAtPath:isDirectory:"
- "firstMatchInString:options:range:"
- "firstObject"
- "getBytes:range:"
- "getCacheForKey:"
- "getConfigOfKey:withError:"
- "getDylibHandlerWithError:"
- "getInternalSupportPath"
- "getObfuscatedKey:withError:"
- "getSharedInstanceByName:withError:"
- "getXpcProxyWithError:"
- "graphicInfoArrayFromArray:"
- "hasSuffix:"
- "helper"
- "hexStringFromData:"
- "init"
- "initData"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithData:encoding:"
- "initWithFormat:arguments:"
- "initWithName:andCapacity:andCacheType:"
- "initWithServiceName:"
- "intValue"
- "integerFromCInt:size:isSigned:needSwap:"
- "integerFromData:size:truncate:isSigned:needSwap:"
- "integerValue"
- "interfaceWithProtocol:"
- "isAtEnd"
- "isDataConvertibleToVisibleString:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isInternalAssistant"
- "isKey:withError:"
- "isXpcConnectionValid"
- "keysCacheForCopyValue"
- "lastPathComponent"
- "length"
- "logHandler"
- "macAddressStringFromData:"
- "macAddressStringFromSysconfigDataSixByte:"
- "mutableBytes"
- "name"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithShort:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pathWithComponents:"
- "printRemoteLog:withReply:"
- "processInfo"
- "processName"
- "queryKey:andOptions:andPreferences:withError:"
- "rangeAtIndex:"
- "recursiveMutex"
- "recursiveMutexForCopyValue"
- "registerCacheRefresh:"
- "regularExpressionWithPattern:options:error:"
- "remoteObjectInterface"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "scanHexInt:"
- "scanInt:"
- "scannerWithString:"
- "setBulkInternalKeys:getValuesAndError:"
- "setBulkInternalMGKeys:getValuesAndError:"
- "setBulkKeys:getValuesAndError:"
- "setBulkMGKeys:getValuesAndError:"
- "setCache:forKey:withError:"
- "setCacheList:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDylibHandler:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInternalKey:andOptions:andPreferences:getValueAndError:"
- "setInternalMGKey:getValueAndError:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsXpcConnectionValid:"
- "setKey:andOptions:andPreferences:getValueAndError:"
- "setKeysCacheForCopyValue:"
- "setLogHandler:"
- "setMGKey:getValueAndError:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "setXpcConnection:"
- "sharedInstance"
- "stringByLeftTrimmingCharacter:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringByRemovingCharactersInString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByRightTrimmingCharacter:"
- "stringByTrimmingCharactersInSet:"
- "stringByTrimmingCharactersInString:"
- "stringFromData:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8^?16"
- "v24@0:8^v16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24"
- "v32@0:8@16@?24"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "visibleStringFromData:"
- "xpcConnection"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"

```
