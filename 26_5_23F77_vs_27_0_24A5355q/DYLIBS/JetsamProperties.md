## JetsamProperties

> `/System/Library/PrivateFrameworks/JetsamProperties.framework/JetsamProperties`

```diff

-2648.120.18.0.0
-  __TEXT.__text: 0x239c
-  __TEXT.__auth_stubs: 0x2b0
+2996.0.0.502.2
+  __TEXT.__text: 0x20b0
   __TEXT.__objc_methlist: 0x384
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x460
+  __TEXT.__cstring: 0x464
   __TEXT.__oslogstring: 0x11a
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x38
-  __TEXT.__objc_methname: 0xad1
-  __TEXT.__objc_methtype: 0xd9
-  __TEXT.__objc_stubs: 0x740
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x330
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__objc_const: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x1c
   __DATA.__bss: 0x30

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 409BA9F4-D3B0-3D0C-BC40-07C43BB82E07
-  Functions: 99
-  Symbols:   393
-  CStrings:  294
+  UUID: 1A93426C-E22F-3126-9F36-54282751B524
+  Functions: 96
+  Symbols:   391
+  CStrings:  135
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSSet\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8C16C20"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "B16@0:8"
- "B24@0:8@16"
- "C20@0:8C16"
- "C24@0:8@16"
- "JPEntry"
- "JPLoader"
- "JPMemoryLimitsTransformer"
- "JPReader"
- "Q16@0:8"
- "Q24@0:8@16"
- "T@\"NSArray\",&,N,V_filteredProperties"
- "T@\"NSDictionary\",R,N,G_properties"
- "T@\"NSString\",&,N,V_overrideFullPath"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,G_path"
- "TB,R,N"
- "TB,R,N,GisAlwaysSIGTERMOnShutdown"
- "TB,R,N,GisEnablePressuredExit"
- "TB,R,N,GisFreezable"
- "TB,R,N,GisMSLActivatePostJetsam"
- "TB,R,N,GisMallocAggressiveMadvise"
- "TB,R,N,GisMallocEnableMSLAtLimitWarning"
- "TB,R,N,GisMallocLargeCache"
- "TB,R,N,GisMallocMediumZone"
- "TB,R,N,GisMallocNanoZone"
- "TB,R,N,GisMallocSpaceEfficient"
- "TB,R,N,GisRecoverOnCrash"
- "TQ,R,N"
- "_altStrength:"
- "_altType:"
- "_boolPropertyValueForKey:"
- "_config"
- "_entriesByType"
- "_fetchJetsamValuesForSection:fromPlist:"
- "_fetchJetsamValuesFromPlistValue:filteredProperties:"
- "_filteredProperties"
- "_globalByType"
- "_globalConfig"
- "_isMemoryLimitKey:"
- "_keyForType:strength:"
- "_loadJetsamProperties"
- "_overrideFullPath"
- "_path"
- "_prepareJetsamData:"
- "_properties"
- "_strengthForKey:"
- "_stringPropertyValueForKey:"
- "_typeForKey:"
- "_unsignedIntegerPropertyValueForKey:"
- "addEntriesFromDictionary:"
- "addressLimit"
- "alwaysSIGTERMOnShutdown"
- "arrayWithObjects:count:"
- "boolValue"
- "conclaveMemoryLimit"
- "config"
- "containsObject:"
- "containsString:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createReader"
- "darkBootSystemUIHardLimit"
- "decodeEncodedValue:forKey:"
- "dictionary"
- "enablePressuredExit"
- "encode:"
- "energyEfficiencyMode"
- "entryByOverlayingEntry:"
- "entryForExtensionPoint:instanceBundleID:"
- "entryForType:identifier:"
- "enumerateKeysAndObjectsUsingBlock:"
- "filteredProperties"
- "freezable"
- "globalConfig"
- "hardFileDescriptorLimit"
- "hardKqWorkloopLimit"
- "hardPortLimit"
- "hasPrefix:"
- "hasSuffix:"
- "init"
- "initPrivate"
- "initWithConfig:globalConfig:"
- "initWithContentsOfFile:"
- "initWithUTF8String:"
- "intValue"
- "integerValue"
- "isAlwaysSIGTERMOnShutdown"
- "isEnablePressuredExit"
- "isEqual:"
- "isEqualToString:"
- "isFreezable"
- "isMSLActivatePostJetsam"
- "isMallocAggressiveMadvise"
- "isMallocEnableMSLAtLimitWarning"
- "isMallocLargeCache"
- "isMallocMediumZone"
- "isMallocNanoZone"
- "isMallocSpaceEfficient"
- "isRecoverOnCrash"
- "kernelHighWaterMark"
- "logicalWritesLimit"
- "longValue"
- "mallocAggressiveMadvise"
- "mallocEnableMSLAtLimitWarning"
- "mallocLargeCache"
- "mallocMaxMagazines"
- "mallocMediumZone"
- "mallocNanoZone"
- "mallocSpaceEfficient"
- "memoryLimitForType:"
- "mutableCopy"
- "noExcResourceDuringAudio"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "overrideFullPath"
- "parse:"
- "priority"
- "recoverOnCrash"
- "self"
- "setFilteredProperties:"
- "setObject:forKeyedSubscript:"
- "setOverrideFullPath:"
- "setValue:forKey:"
- "setWithArray:"
- "softFileDescriptorLimit"
- "softKqWorkloopLimit"
- "softPortLimit"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "userReclaimableLimit"
- "v16@0:8"
- "v24@0:8@16"
- "valueForProperty:"
- "wiredMemoryLimit"
- "{JPMemoryLimit=iCC}20@0:8C16"

```
