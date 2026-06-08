## FileProviderOverride

> `/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FileProviderOverride.bundle/FileProviderOverride`

```diff

-4018.120.24.0.0
-  __TEXT.__text: 0x27a0
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x314
+4780.0.0.502.1
+  __TEXT.__text: 0x2c38
+  __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__cstring: 0x19b
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x205
   __TEXT.__oslogstring: 0x1d0
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0x34
-  __TEXT.__objc_methname: 0xca2
-  __TEXT.__objc_methtype: 0x5f1
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x108
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x318
-  __AUTH_CONST.__auth_got: 0x200
+  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x2b8
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x2c0
+  __AUTH_CONST.__auth_got: 0x250
   __DATA.__data: 0xc0
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C5887A4-4D8A-3893-997D-FCF101AAE26D
-  Functions: 81
-  Symbols:   110
-  CStrings:  205
+  UUID: AA1982A0-8E38-3AEA-8107-88331E350D70
+  Functions: 82
+  Symbols:   123
+  CStrings:  54
 
Symbols:
+ _FPIsCiaoEnabled
+ _FPUserFSTrashURLForRootURL
+ _OBJC_CLASS_$_FPAppRegistry
+ _OBJC_CLASS_$_FPProviderDomainChangesReceiver
+ _OBJC_CLASS_$_NSURL
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "com.apple.FileProvider.LocalStorage"
+ "com.apple.filesystems.UserFS.FileProvider"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
- "#16@0:8"
- "@\"NSSet\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"NSURL\"16^@24"
- "@\"NSString\"40@0:8@\"NSURL\"16q24^@32"
- "@\"NSURL\"32@0:8@\"NSString\"16^@24"
- "@\"NSURL\"32@0:8@\"NSURL\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24^@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSURL\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSArray\"16@\"FPItem\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"NSMutableSet\"16@\"NSArray\"24@\"FPItem\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@16@\"NSString\"24@\"NSURL\"32^@40"
- "B48@0:8@16@24@32^@40"
- "FPAreUTIsImportable:toFolderItem:"
- "FPBookmarkableStringFromDocumentURL:completionHandler:"
- "FPBookmarkableStringFromDocumentURL:error:"
- "FPBookmarkableStringFromDocumentURL:options:error:"
- "FPDocumentURLFromBookmarkableString:completionHandler:"
- "FPDocumentURLFromBookmarkableString:error:"
- "FPDocumentURLFromUniversalBookmarkableString:completionHandler:"
- "FPEvictItemAtURL:completionHandler:"
- "FPExtendBookmarkForDocumentURL:forBundleID:completionHandler:"
- "FPFetchLatestVersionForFileAtURL:completionHandler:"
- "FPFileProviderModule"
- "FPFileProviderServiceEndpointCreatingForItemAtURL:completionHandler:"
- "FPFileProviderServiceEndpointCreatingForItemAtURL:synchronously:completionHandler:"
- "FPFileProviderServiceEndpointCreatingWithName:itemAtURL:synchronously:completionHandler:"
- "FPFilterActions:forDroppingItems:underItem:"
- "FPFrameworkOverriding"
- "FPGetPausedFilesList:completionHandler:"
- "FPPauseSyncForFileAtURL:timeout:options:completionHandler:"
- "FPResumeSyncForFileAtURL:resumeOptions:completionHandler:"
- "FPServerPackageExtensions"
- "FPSetValue:forAttribute:onItemAtURL:error:"
- "FPStateForDomainWithID:completionHandler:"
- "FPTrashURLForItemAtURL:error:"
- "FPURLIsInFileProvider:"
- "FPUniversalBookmarkableStringFromDocumentURL:completionHandler:"
- "FPValuesForAttributes:forItemAtURL:completionHandler:"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLByAppendingPathComponent:isDirectory:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_originalDocumentURLForURL:"
- "arrayWithObjects:count:"
- "autorelease"
- "bookmarkableStringFromDocumentURL:completionHandler:"
- "bookmarkableStringFromDocumentURL:options:completionHandler:"
- "boolValue"
- "callStackSymbols"
- "class"
- "code"
- "conformsToProtocol:"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "defaultManager"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "documentURLFromBookmarkableString:completionHandler:"
- "documentURLFromBookmarkableString:error:"
- "domain"
- "errorWithDomain:code:userInfo:"
- "evictItemAtURL:evenIfEnumeratingFP:andClearACLForConsumer:completionHandler:"
- "extendBookmarkForFileURL:toConsumerID:options:completionHandler:"
- "fetchServicesWithName:itemAtURL:synchronously:handler:"
- "fileSystemRepresentation"
- "fp_errorWithPOSIXCode:"
- "fp_fpfsRootURL"
- "fp_isPOSIXErrorCode:"
- "fp_matchesFileProviderHeuristics:options:"
- "fp_realpathURL"
- "fp_relationshipToItemAtURL:"
- "fp_unwrappedErrorForDomains:"
- "getResourceValue:forKey:error:"
- "hash"
- "initWithFormat:arguments:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "overridePriority"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q16@0:8"
- "rangeOfString:options:"
- "release"
- "remoteObjectProxyCreating"
- "respondsToSelector:"
- "responsibleForBookmarksInRealPathURL:"
- "retain"
- "retainCount"
- "self"
- "setObject:forKeyedSubscript:"
- "sharedConnection"
- "sharedConnectionProxy"
- "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:duration:event:payload:reply:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "stateForDomainWithID:completionHandler:"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringToIndex:"
- "superclass"
- "synchronousSharedConnectionProxy"
- "underlyingErrors"
- "userInfo"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"<NSXPCProxyCreating><NSFileProviderServiceEndpointCreating>\"@\"NSArray\"@?<v@?>@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSFileVersion\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v32@0:8@?<v@?@\"NSURL\">16@?<v@?@\"NSError\">24"
- "v36@0:8@\"NSURL\"16B24@?<v@?@\"<NSXPCProxyCreating><NSFileProviderServiceEndpointCreating>\"@\"NSArray\"@?<v@?>@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16Q24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v44@0:8@\"NSString\"16@\"NSURL\"24B32@?<v@?@\"<NSXPCProxyCreating><NSFileProviderServiceEndpointCreating>\"@?<v@?>@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"NSURL\"16d24Q32@?<v@?B@\"NSError\">40"
- "v48@0:8@16d24Q32@?40"
- "valuesForAttributes:forItemAtURL:error:"
- "zone"

```
