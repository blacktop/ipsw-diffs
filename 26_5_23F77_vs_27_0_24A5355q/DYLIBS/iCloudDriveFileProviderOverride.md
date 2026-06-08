## iCloudDriveFileProviderOverride

> `/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride`

```diff

-4479.122.1.0.0
-  __TEXT.__text: 0xb3c
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x68
+5044.0.0.0.0
+  __TEXT.__text: 0xad8
+  __TEXT.__objc_methlist: 0x2ac
+  __TEXT.__const: 0x60
   __TEXT.__cstring: 0x140
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x95d
-  __TEXT.__objc_methtype: 0x5f8
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x288
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x290
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x2b8
+  __AUTH_CONST.__objc_const: 0x2c0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 79140078-4213-3330-8F09-5D63B3331369
+  UUID: 17582EC5-8B4B-3541-986C-D948748F06FF
   Functions: 13
-  Symbols:   49
-  CStrings:  151
+  Symbols:   48
+  CStrings:  13
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release_x26
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
Functions:
~ sub_23e4b9eec -> sub_242448eec : 468 -> 448
~ sub_23e4ba0c0 -> sub_2424490ac : 952 -> 932
~ sub_23e4ba6d0 -> sub_2424496a8 : 168 -> 160
~ sub_23e4ba83c -> sub_24244980c : 320 -> 312
~ sub_23e4ba98c -> sub_242449954 : 136 -> 92
CStrings:
- "#16@0:8"
- "@\"NSSet\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"NSURL\"16^@24"
- "@\"NSString\"40@0:8@\"NSURL\"16q24^@32"
- "@\"NSURL\"32@0:8@\"NSString\"16^@24"
- "@\"NSURL\"32@0:8@\"NSURL\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
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
- "B40@0:8@16@24^@32"
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
- "ICDFileProviderFrameworkOverride"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLByDeletingLastPathComponent"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_isURLExcludedFromSync:syncRoot:error:"
- "addEntriesFromDictionary:"
- "arrayByAddingObject:"
- "autorelease"
- "bookmarkPrefix"
- "boolValue"
- "br_bookmarkableStringWithEtag:onlyAllowItemKnowByServer:completion:"
- "br_copy_if:"
- "br_documentURLFromBookmarkableString:completion:"
- "br_errorWithPOSIXCode:"
- "br_getSyncRootWithError:"
- "br_isExcludedWithMaximumDepth:"
- "br_isExistWithNonMateralizingIOPolicy:"
- "br_isIgnoredByFileProviderWithError:"
- "br_isInSyncedLocation"
- "br_realpathURL"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "debugDescription"
- "defaultConnection"
- "description"
- "errorWithDomain:code:userInfo:"
- "getSyncState:reply:"
- "hasPrefix:"
- "hash"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNetworkReachable"
- "isProxy"
- "lastPathComponent"
- "length"
- "overridePriority"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q16@0:8"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setObject:forKey:"
- "setValue:forKey:"
- "sharedConnection"
- "sharedReachabilityMonitor"
- "stringByAppendingString:"
- "substringFromIndex:"
- "superclass"
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
- "valueForKey:"
- "valuesForAttributes:forItemAtURL:error:"
- "zone"

```
