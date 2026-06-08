## SpotlightDiagnostics

> `/System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x2ba0
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x170
+2444.104.0.0.0
+  __TEXT.__text: 0x30ec
+  __TEXT.__objc_methlist: 0x178
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__cstring: 0x35e
-  __TEXT.__oslogstring: 0x1dd
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x726
-  __TEXT.__objc_methtype: 0xff
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__gcc_except_tab: 0x210
+  __TEXT.__cstring: 0x3a8
+  __TEXT.__oslogstring: 0x2d3
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x228
+  __DATA_CONST.__objc_selrefs: 0x248
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x198
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x400
+  __DATA_CONST.__got: 0xc8
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x300
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x28
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1AC86FB-D618-316E-BAA0-3C45791B7267
-  Functions: 76
-  Symbols:   336
-  CStrings:  189
+  UUID: 5432C254-6F96-38CC-AE7E-114288F70F63
+  Functions: 92
+  Symbols:   385
+  CStrings:  102
 
Symbols:
+ -[SDCoreSpotlightDiagnosticClient getBuildHistoryData]
+ -[SDCoreSpotlightDiagnosticClient getBuildHistoryData].cold.1
+ -[SDCoreSpotlightDiagnosticClient getBuildHistoryData].cold.2
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ _OBJC_CLASS_$_NSUserDefaults
+ _SDDiagnosticDefaultPrivacyLevel
+ _SDDiagnosticDefaults
+ _SDDiagnosticDefaults.cold.1
+ _SDDiagnosticDefaults.defaults
+ _SDDiagnosticDefaults.once
+ _SDDiagnosticGateIsInternal
+ _SDDiagnosticGateIsInternal.cold.1
+ _SDDiagnosticGateIsInternal.once
+ _SDDiagnosticGateIsInternal.result
+ _SDDiagnosticGateIsSeedBuild
+ _SDDiagnosticGateIsSeedBuild.cold.1
+ _SDDiagnosticGateIsSeedBuild.once
+ _SDDiagnosticGateIsSeedBuild.result
+ _SDLogCategoryGeneral
+ _SDLogCategoryGeneral.cold.1
+ _SDLogCategoryGeneral.generalLog
+ _SDLogCategoryGeneral.onceToken
+ ___54-[SDCoreSpotlightDiagnosticClient getBuildHistoryData]_block_invoke
+ ___54-[SDCoreSpotlightDiagnosticClient getBuildHistoryData]_block_invoke.cold.1
+ ___54-[SDCoreSpotlightDiagnosticClient getBuildHistoryData]_block_invoke.cold.2
+ ___SDDiagnosticDefaults_block_invoke
+ ___SDDiagnosticGateIsInternal_block_invoke
+ ___SDDiagnosticGateIsSeedBuild_block_invoke
+ ___SDLogCategoryGeneral_block_invoke
+ ___block_literal_global.12
+ ___block_literal_global.4
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_issueDiagnose:bundleID:privacyLevel:completionHandler:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$objectForKey:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _os_variant_has_internal_diagnostics
- GCC_except_table15
- GCC_except_table22
- GCC_except_table27
- GCC_except_table29
- _MGCopyAnswer
- _SDIsAppleInternalInstall
- _SDIsAppleInternalInstall.cold.1
- _SDIsAppleInternalInstall.isInternalInstall
- _SDIsAppleInternalInstall.onceToken
- ___SDIsAppleInternalInstall_block_invoke
- _objc_msgSend$_issueDiagnose:bundleID:logQuery:completionHandler:
- _objc_opt_class
- _objc_opt_isKindOfClass
CStrings:
+ "General"
+ "IsInternal: %d"
+ "IsSeedBuild: %d"
+ "SDDiagnosticIsInternal"
+ "SDDiagnosticIsSeedBuild"
+ "analytics:builds"
+ "com.apple.searchd"
+ "error getting build history data for %@: %@"
+ "error getting build history data: %@"
+ "got build history data"
+ "got build history data for %@"
+ "timed out getting build history data"
+ "timed out getting build history data for %@"
- ".cxx_destruct"
- "@\"CSSearchableIndex\""
- "@\"NSArray\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8^B16"
- "@28@0:8@16I24"
- "@32@0:8@16@24"
- "@36@0:8I16@20@28"
- "@40@0:8@16@24@32"
- "@52@0:8@16@24@32B40B44B48"
- "B"
- "B16@0:8"
- "Internal"
- "ReleaseType"
- "SDCoreSpotlightDiagnosticClient"
- "SDDiagnosticClient"
- "SDDiagnosticClientSet"
- "UTF8String"
- "_bundleID"
- "_defaultClients"
- "_index"
- "_issueCommand:completionHandler:"
- "_issueDiagnose:bundleID:logQuery:completionHandler:"
- "_managed"
- "_managedClients"
- "_path"
- "_private"
- "_privateClients"
- "_protectionClass"
- "_setUser:"
- "_testIndex"
- "addObject:"
- "allObjects"
- "appendFormat:"
- "appendString:"
- "arrayWithObjects:count:"
- "bundleID"
- "bundleIdentifier"
- "caseInsensitiveCompare:"
- "componentsSeparatedByString:"
- "copy"
- "copySpotlightIndexDropsToDirectory:forDays:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "date"
- "dateByAddingTimeInterval:"
- "dateStringForDaysAgo:"
- "debugDescription"
- "defaultClientWithBundleID:protectionClass:"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateCoreSpotlightClientsWithDefaultBlock:privateBlock:managedBlock:completion:"
- "enumerateObjectsUsingBlock:"
- "findSpotlightIndexDropsForDays:"
- "getCurrentSpotlightVersionWithRoots:"
- "getSpotlightHeartbeatData"
- "getSpotlightVersionWithRoots:"
- "getStatus:protectionClasses:queue:completionHandler:"
- "indexPath"
- "init"
- "initWithBundleID:protectionClass:path:private:managed:test:"
- "initWithData:encoding:"
- "initWithDefaultClients:privateClients:managedClients:"
- "initWithDomain:code:userInfo:"
- "initWithName:protectionClass:bundleIdentifier:"
- "initWithPath:queryString:context:"
- "initWithQueryString:queryContext:"
- "isEqualToString:"
- "isManaged"
- "isPrivate"
- "isTestIndex"
- "issueDiagnose:privacyLevel:completionHandler:"
- "logsDirectory"
- "mainBundle"
- "nonPrivateCoreSpotlightClientsForUser:bundleID:protectionClass:"
- "privateClientWithBundleID:protectionClass:"
- "reason"
- "setActiveUser"
- "setAttribute:"
- "setChangedAttributesHandler:"
- "setClientBundleID:"
- "setCompletionHandler:"
- "setCountChangedHandler:"
- "setCounting:"
- "setDateFormat:"
- "setFetchAttributes:"
- "setFoundAttributesHandler:"
- "setPrivateBundleID:"
- "setPrivateIndex:"
- "setProtectionClasses:"
- "setUser:"
- "sortedArrayUsingSelector:"
- "start"
- "stringFromDate:"
- "stringWithFormat:"
- "testClientWithBundleID:protectionClass:"
- "v16@0:8"
- "v20@0:8I16"
- "v36@0:8i16Q20@?28"
- "v44@0:8B16@20@28@?36"
- "v48@0:8@?16@?24@?32@?40"

```
