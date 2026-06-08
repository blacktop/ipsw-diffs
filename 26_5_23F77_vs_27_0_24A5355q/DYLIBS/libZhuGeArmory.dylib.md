## libZhuGeArmory.dylib

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`

```diff

-408.120.3.0.0
-  __TEXT.__text: 0x240ec
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x824
+458.0.0.0.0
+  __TEXT.__text: 0x23fe8
+  __TEXT.__objc_methlist: 0x834
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0xa53e
+  __TEXT.__cstring: 0xaa01
   __TEXT.__gcc_except_tab: 0x18c
-  __TEXT.__oslogstring: 0x1af
+  __TEXT.__oslogstring: 0x233
   __TEXT.__unwind_info: 0x3e8
-  __TEXT.__objc_classname: 0x181
-  __TEXT.__objc_methname: 0x1cfa
-  __TEXT.__objc_methtype: 0x32c
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x290
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x858
+  __DATA_CONST.__objc_selrefs: 0x868
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x7f8
-  __AUTH_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__objc_arraydata: 0x818
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x8160
+  __AUTH_CONST.__cfstring: 0x8320
   __AUTH_CONST.__objc_const: 0xe68
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x848
-  __AUTH_CONST.__objc_arrayobj: 0x840
+  __AUTH_CONST.__objc_arrayobj: 0x8a0
+  __AUTH_CONST.__auth_got: 0x508
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0xa24
-  __DATA.__bss: 0xf0
-  __DATA.__common: 0x18
+  __DATA.__data: 0xa20
+  __DATA.__bss: 0x100
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x110

   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libCentauriUpdater.dylib
-  UUID: ACBC8659-5498-3B4A-8EA0-7B7F4AA122A0
-  Functions: 347
-  Symbols:   1428
-  CStrings:  2640
+  UUID: 36D8153D-535F-3BF8-AC87-AE3CE3A311B6
+  Functions: 350
+  Symbols:   1449
+  CStrings:  2302
 
Symbols:
+ +[ZhuGeKeysActionArmory queryAIDTouchScreenCert:idx:withError:]
+ +[ZhuGeKeysActionArmory queryComponentAuthChipIDSN:withError:]
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table70
+ GCC_except_table71
+ _OUTLINED_FUNCTION_15
+ __MergedGlobals
+ ___block_literal_global.175
+ __connectHandle
+ __connectHandleRefCount
+ _fwrite
+ _getSensorProvisioningState.cold.1
+ _getSensorProvisioningState.cold.2
+ _getSensorProvisioningState.cold.3
+ _getSensorProvisioningState.cold.4
+ _initOrRetain
+ _initOrRetain.cold.1
+ _initOrRetain.cold.2
+ _initOrRetain.cold.3
+ _initOrRetain.cold.4
+ _initOrRetain.cold.5
+ _initOrRetain.cold.6
+ _initOrRetain.cold.7
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$longLongValue
+ _objc_msgSend$queryComponentAuthChipIDSN:withError:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _readPropertyFromComponentAuthService
+ _releaseOrDeinit
+ _releaseOrDeinit.cold.1
+ _releaseOrDeinit.cold.2
- +[ZhuGeKeysActionArmory queryAIDTouchScreenCert:withError:]
- GCC_except_table42
- GCC_except_table44
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table53
- GCC_except_table58
- GCC_except_table59
- _OSLogInit.onceToken
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- ___block_literal_global.176
- __connect
- __testMode
- __testProvisionState
- _initialize
- _initialize.cold.1
- _initialize.cold.2
- _kIOMasterPortDefault
- _objc_retain_x25
- _readPropertyFromMogulService
CStrings:
+ "!!! IMPL ERROR !!! RefCount is non-zero yet _connection is null!\n"
+ "!!! IMPL ERROR !!! RefCount is zero yet _connection is non-null!\n"
+ "\"%@\" of entry \"%@\" is class %@ while expecting Integer<NSNumber>"
+ "+[ZhuGeKeysActionArmory queryAIDTouchScreenCert:idx:withError:]"
+ "+[ZhuGeKeysActionArmory queryComponentAuthChipIDSN:withError:]"
+ "AppleBiometricServices io_service_t failed to be released!"
+ "ComponentIndex"
+ "Default component found"
+ "Error: Connection to AppleBiometricServices could not be initialized!"
+ "Error: RefCount equal to zero is trying to get decremented!"
+ "Error: RefCount reached its maximum value!"
+ "FSRsyiOWdf4OCG6zvks590DxmrR3/XoDhE85oTuP1f480"
+ "Get the component index number is : %@"
+ "IOObjectRelease(service) == 0 "
+ "Implementation error: Connection handle to AppleBiometricServices has a non-zero refcount and should be non-null but the handle is null!"
+ "Implementation error: Connection handle to AppleBiometricServices has a refcount of zero and should be null but the handle is non-null!"
+ "Integer \"%@\" of entry \"%@\" is %@ while expecting %@"
+ "MFTFDybYdMEa3t7lEekmZ0DVntZfm8FTx8hVssqp6sQ80"
+ "VlPZNgOg1p1oj0IEgDd6F10jh+is1Z1X+RW+DXL/lKQvY"
+ "YonkersIR1ChipID"
+ "YonkersIR1UID"
+ "YonkersIR2ChipID"
+ "YonkersIR2UID"
+ "_connectHandle != ((io_object_t) 0)"
+ "_connectHandleRefCount < 4294967295U"
+ "_connectHandleRefCount > 0"
+ "err != (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x1)"
+ "integer:"
+ "isComponentAuthChipAuthCPService"
+ "nJcmJi6nEp5Ll6CuYyaC+10jXex+M+8W1qy3xdu3e1OMA"
+ "readPropertyFromComponentAuthService"
+ "wasRetained"
- "#"
- "#16@0:8"
- "+[ZhuGeKeysActionArmory queryAIDTouchScreenCert:withError:]"
- "+[ZhuGeKeysActionArmory queryMogulIDSN:withError:]"
- ".cxx_destruct"
- "@\"CTMobileEquipmentInfoList\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@\"ZhuGeArmoryHelperArmory\""
- "@\"ZhuGeCacheArmory\""
- "@16@0:8"
- "@20@0:8c16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@28@0:8@16B24"
- "@28@0:8B16^@20"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@36@0:8@16B24^@28"
- "@40@0:8@16@24#32"
- "@40@0:8@16@24^@32"
- "@40@0:8Q16Q24B32B36"
- "@44@0:8@16q24B32^@36"
- "@44@0:8[512c]16[128c]24^{__CFString=}32I40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16Q24q32B40B44"
- "@48@0:8@16{_NSRange=QQ}24^@40"
- "@64@0:8@16@24@32@40@48^@56"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8i16i20"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8^@16@24@32"
- "JSONObjectWithData:options:error:"
- "T#,R,V_actionClass"
- "T#,R,V_cacheType"
- "T#,R,V_configClass"
- "T@\"CTMobileEquipmentInfoList\",&,V_mobileEquipInfoList"
- "T@\"NSArray\",R,V_flexibleList"
- "T@\"NSData\",&,V_eUICCPairingIdentifier"
- "T@\"NSDictionary\",&,V_firmwareSecurityInfo"
- "T@\"NSDictionary\",&,V_firmwareUpdateInfo"
- "T@\"NSDictionary\",&,V_postponementStatus"
- "T@\"NSDictionary\",R,V_aliasesMap"
- "T@\"NSDictionary\",R,V_config"
- "T@\"NSDictionary\",R,V_keysConfig"
- "T@\"NSDictionary\",R,V_option"
- "T@\"NSMutableArray\",&,V_dependencyPath"
- "T@\"NSMutableArray\",R,V_cacheList"
- "T@\"NSMutableDictionary\",R,V_cacheDict"
- "T@\"NSNumber\",R,V_capacity"
- "T@\"NSString\",&"
- "T@\"NSString\",R,V_key"
- "T@\"NSString\",R,V_name"
- "T@\"NSXPCConnection\",&,V_xpcConnection"
- "T@\"ZhuGeArmoryHelperArmory\",R,V_helper"
- "T@\"ZhuGeCacheArmory\",&,V_propertiesCache"
- "T^?,V_logHandler"
- "UTF8String"
- "ZhuGe"
- "ZhuGeArmoryHelperArmory"
- "ZhuGeBasebandArmory"
- "ZhuGeBasebandConnectionArmory"
- "ZhuGeBasebandFirmwareSecurityInfoArmory"
- "ZhuGeBasebandFirmwareUpdateInfoArmory"
- "ZhuGeBasebandPostponementStatusArmory"
- "ZhuGeCacheArmory"
- "ZhuGeDescription"
- "ZhuGeKeysActionArmory"
- "ZhuGeKeysConfigArmory"
- "ZhuGeLockerArmory"
- "ZhuGeMobileEquipmentInfoArmory"
- "ZhuGeModuleArmory"
- "ZhuGeSingletonArmory"
- "^?"
- "^?16@0:8"
- "^{__CTServerConnection=}16@0:8"
- "_ZhuGeDescriptionWithLayer:"
- "_actionClass"
- "_aliasesMap"
- "_cacheDict"
- "_cacheList"
- "_cacheType"
- "_capacity"
- "_config"
- "_configClass"
- "_dependencyPath"
- "_eUICCPairingIdentifier"
- "_firmwareSecurityInfo"
- "_firmwareUpdateInfo"
- "_flexibleList"
- "_helper"
- "_key"
- "_keysConfig"
- "_logHandler"
- "_mobileEquipInfoList"
- "_name"
- "_option"
- "_postponementStatus"
- "_propertiesCache"
- "_xpcConnection"
- "aRecursiveMutex"
- "accessInstanceVariablesDirectly"
- "actForKey:andName:andConfig:andOptions:andPreferences:withError:"
- "actionClass"
- "addObject:"
- "aliasesMap"
- "allKeys"
- "allValues"
- "appendBytes:length:"
- "appendFormat:"
- "arrayFromShellCommandString:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "base64EncodedDataWithOptions:"
- "boolFromData:needNegate:"
- "boolValue"
- "bytes"
- "cStringUsingEncoding:"
- "cacheDict"
- "cacheList"
- "cacheType"
- "capacity"
- "ccccValue"
- "characterAtIndex:"
- "characterSetWithCharactersInString:"
- "checkDependency:withError:"
- "clearCache"
- "code"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "config"
- "configClass"
- "containsObject:"
- "convertReturnValue:ByItselfAndError:AndRevalues:"
- "convertReturnValue:toCase:"
- "convertReturnValue:toFormat:"
- "convertToPostponementKey:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentLocale"
- "dataFromHexString:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithLength:"
- "delCacheForKey:"
- "dependencyPath"
- "description"
- "descriptionFromZhuGeErrorCode:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "domain"
- "eUICCPairingIdentifier"
- "embeddedSecureElementWithError:"
- "environment"
- "errorWithDomain:code:userInfo:"
- "errorWithZhuGeErrorCode:underlyingError:"
- "escapedPatternForString:"
- "firmwareSecurityInfo"
- "firmwareUpdateInfo"
- "firstMatchInString:options:range:"
- "firstObject"
- "flexibleList"
- "forUndefinedKey"
- "getBasebandClass"
- "getBytes:length:"
- "getBytes:range:"
- "getCTServerConnection"
- "getCacheForKey:"
- "getConfig"
- "getConfigOfKey:withError:"
- "getCoreTelephonyClient"
- "getEuiccData:"
- "getEuiccPairingIdentifier:"
- "getKeyAndOptionFromDependency:withError:"
- "getMobileEquipInfoIn:ofSlot:"
- "getMobileEquipmentInfo:"
- "getObfuscatedKey:withError:"
- "getPrimarykeyOfKey:withError:"
- "getPropertiesOfKey:withError:"
- "getProperty:inPlane:withName:withOption:"
- "getReturnValue:"
- "getSubkeyOfKey:withError:"
- "graphicInfoArrayFromArray:"
- "hasBaseband"
- "hasPrefix:"
- "hasSuffix:"
- "helper"
- "hexStringFromData:"
- "init"
- "initData"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithData:encoding:"
- "initWithError:"
- "initWithFormat:arguments:"
- "initWithLength:"
- "initWithName:andCapacity:andCacheType:"
- "initWithQueue:"
- "initWithRawConfig:"
- "intValue"
- "integerFromCInt:size:isSigned:needSwap:"
- "integerFromData:size:truncate:isSigned:needSwap:"
- "integerValue"
- "invocationWithMethodSignature:"
- "invoke"
- "isAtEnd"
- "isBasebandReady"
- "isDataConvertibleToVisibleString:"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKeyAlias:withError:"
- "isMogulAuthCPService"
- "key"
- "keysConfig"
- "lastPathComponent"
- "length"
- "loadEUICCPairingIdentifier:"
- "loadFirmwareSecurityInfoBootedOS:"
- "loadFirmwareSecurityInfoRestoreOS:"
- "loadFirmwareUpdateInfo:"
- "loadMobileEquipInfoList:"
- "loadPostponementStatus:"
- "logHandler"
- "lowercaseString"
- "lowercaseStringWithLocale:"
- "macAddressStringFromData:"
- "macAddressStringFromSysconfigDataSixByte:"
- "meInfoList"
- "methodReturnLength"
- "methodSignatureForSelector:"
- "mobileEquipInfoList"
- "mutableBytes"
- "name"
- "numberFromString:"
- "numberOfArguments"
- "numberOfRanges"
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
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "option"
- "pickFlexibleFromUnionizedConfig:withError:"
- "postponementStatus"
- "printRemoteLog:withReply:"
- "processInfo"
- "processName"
- "propertiesByKey:andSuperKeyRange:withError:"
- "propertiesCache"
- "propertiesOfKey:withError:"
- "q16@0:8"
- "query:forceCacheable:withError:"
- "query:isCachable:withError:"
- "query:ofSlot:isCachable:withError:"
- "query:withError:"
- "queryAIDTouchScreenCert:withError:"
- "queryFDRDeviceAsidMetadataIsVerified:withError:"
- "queryKey:andOptions:andPreferences:withError:"
- "queryMobileEquipInfo:byKey:withError:"
- "queryThreadRadioMacAddress64BitWithError:"
- "queryThreadRadioMacAddressForProvisioningWithError:"
- "queryTouchScreenCert:"
- "queryWLHWIdentifierInfoByProperty:withError:"
- "queryWLModuleSerialNumberWithError:"
- "rangeAtIndex:"
- "rangeOfString:"
- "readPropertyFromMogulService"
- "regularExpressionWithPattern:options:error:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "replaceBytesInRange:withBytes:"
- "runForKey:andOptions:andPreferences:withError:"
- "scanHexInt:"
- "scanInt:"
- "scannerWithString:"
- "serialNumber"
- "setArgument:atIndex:"
- "setCache:forKey:withError:"
- "setDependencyPath:"
- "setEUICCPairingIdentifier:"
- "setFirmwareSecurityInfo:"
- "setFirmwareUpdateInfo:"
- "setKey:"
- "setLogHandler:"
- "setMobileEquipInfoList:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setPostponementStatus:"
- "setPropertiesCache:"
- "setSelector:"
- "setTarget:"
- "setXpcConnection:"
- "sharedHardwareManager:"
- "sharedInstance"
- "sleepForTimeInterval:"
- "slotId"
- "sortAliasFromUnionizedConfig:withError:"
- "sortedArrayUsingComparator:"
- "stringByLeftTrimmingCharacter:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringByRemovingCharactersInString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByReplacingOccurrencesOfString:withString:options:range:"
- "stringByRightTrimmingCharacter:"
- "stringByTrimmingCharactersInSet:"
- "stringByTrimmingCharactersInString:"
- "stringFromData:"
- "stringValue"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemOSSerialNumber"
- "unionizeRawConfig:withError:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateChangeablePropertiesForKey:andOption:withError:"
- "uppercaseString"
- "uppercaseStringWithLocale:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8^?16"
- "valueForKey:"
- "valueForUndefinedKey:"
- "verifyDependencyWithError:"
- "visibleStringFromData:"
- "waitUntilBasebandReady:retryInterval:"
- "xpcConnection"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"

```
