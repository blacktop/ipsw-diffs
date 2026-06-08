## com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x1ebdc
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0x4160
+910.14.107.0.0
+  __TEXT.__text: 0x1e0b0
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x4320
   __TEXT.__objc_methlist: 0x1f30
   __TEXT.__const: 0xa0
-  __TEXT.__objc_classname: 0x2ad
-  __TEXT.__objc_methname: 0x4cd1
-  __TEXT.__objc_methtype: 0xab0
-  __TEXT.__oslogstring: 0x635
-  __TEXT.__cstring: 0x6b50
-  __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__unwind_info: 0x720
-  __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xbd0
-  __DATA_CONST.__cfstring: 0x5e60
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_catlist: 0x18
+  __TEXT.__objc_classname: 0x29b
+  __TEXT.__objc_methname: 0x4e80
+  __TEXT.__objc_methtype: 0xaca
+  __TEXT.__oslogstring: 0x6e8
+  __TEXT.__cstring: 0x6f3a
+  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__unwind_info: 0x6f8
+  __DATA_CONST.__const: 0xc38
+  __DATA_CONST.__cfstring: 0x61c0
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__objc_arraydata: 0x1c0
+  __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA.__objc_const: 0x2ab8
-  __DATA.__objc_selrefs: 0x13d0
-  __DATA.__objc_ivar: 0x208
-  __DATA.__objc_data: 0x5a0
+  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x2b40
+  __DATA.__objc_selrefs: 0x1448
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x558
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: D09A455E-39A7-3F4B-B163-F84AB7363027
-  Functions: 698
-  Symbols:   384
-  CStrings:  2747
+  UUID: EC3202D5-0CBE-3DB5-BADA-C16F9E87F240
+  Functions: 702
+  Symbols:   391
+  CStrings:  2825
 
Symbols:
+ _ACAccountDataclassSiri
+ _CPLAppBundleIdentifierForAppContainerIdentifier
+ _CPLAppContainerIdentifierForLibraryIdentifier
+ _CPLMainScopeIdentifierForApp
+ _NSUserName
+ _OBJC_CLASS_$_CPLInMemoryProcessStorage
+ _OBJC_CLASS_$_CPLLibraryParameters
+ _OBJC_CLASS_$_CPLLibraryParametersStorage
+ _OBJC_CLASS_$_CPLProcessStorage
+ _OBJC_CLASS_$_CPLTransportContainerConfiguration
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_METACLASS_$_CPLInMemoryProcessStorage
+ _OBJC_METACLASS_$_CPLLibraryParametersStorage
+ _OBJC_METACLASS_$_CPLProcessStorage
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x7
- _CPLAppBundleIdentifierForContainerIdentifier
- _CPLContainerIdentifierForLibraryIdentifier
- _CPLPrimaryScopeIdentifier
- _CPLPrimaryScopeIdentifierForCurrentUniverse
- _OBJC_CLASS_$_CPLEngineLibrary
- _OBJC_CLASS_$_CPLEngineParameters
- _OBJC_CLASS_$_CPLEngineParametersStorage
- _OBJC_METACLASS_$_CPLEngineParameters
- _OBJC_METACLASS_$_CPLEngineParametersStorage
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "  redacted %d nTime URLs in share participants"
+ "  redacted %d shares"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Daemon/CPLProcessStorage.m"
+ "/var/mobile/Library/Logs/com.apple.assetsd/PhotosCollectionShareMigration.aapbz"
+ "/var/mobile/Library/Logs/com.apple.assetsd/PhotosCollectionShareMigration.aapbz.old"
+ "00000000-0000-0000-0000-000000000001"
+ "@\"<CPLProcessStorage>\""
+ "@\"CPLLibraryParameters\""
+ "@\"CPLTransportContainerConfiguration\""
+ "@\"NSDictionary\"24@0:8@\"NSString\"16"
+ "@60@0:8@16Q24B32@36@44@52"
+ "@64@0:8@16@24@32Q40@48@56"
+ "Accessing user defaults for %{public}@ failed"
+ "CPLE2ETest"
+ "CPLInMemoryProcessStorage"
+ "CPLLibraryParametersStorage"
+ "CPLManateeTest"
+ "CPLPrivateEngineLibraryOptions"
+ "CPLProcessStorage"
+ "CPLTestManateeApp"
+ "Caches/search/leo.sqlite"
+ "Collecting Photos Search summary"
+ "Discarding invalid old engine info: %@"
+ "Discarding old engine info for %{public}@ as we have already upgraded"
+ "E2E"
+ "Finding %@"
+ "Identifying %@..."
+ "Invocation by %@(%d): %@"
+ "Logs-CollectionShareMigration"
+ "Manatee"
+ "Missing main bundle identifier"
+ "PLBackgroundJobProcessingSet.plist"
+ "Removing %{public}@ from process storage - last update was %{public}@: %@"
+ "Removing %{public}@ from process storage: %@"
+ "T@\"<CPLProcessStorage>\",R,N,V_processStorage"
+ "T@\"CPLLibraryParameters\",R,N"
+ "T@\"CPLLibraryParameters\",R,N,V_libraryParametersForPrivateEngine"
+ "T@\"CPLLibraryParameters\",R,N,V_parameters"
+ "T@\"CPLProcessStorage\",R,N"
+ "T@\"CPLTransportContainerConfiguration\",R,N,V_container"
+ "T@\"NSDate\",R,N,V_blockedDate"
+ "T@\"NSString\",R,N,V_blockingReason"
+ "To force wipe all engines, run '%@ daemon wipe-engines'"
+ "Unable to locate URL for group.com.apple.photolibraryd.private group container"
+ "Updating %{public}@ in process storage - last update was %{public}@: %@"
+ "Updating %{public}@ in process storage: %@"
+ "VisualIntelligence"
+ "_CPLLastUpdateFor"
+ "_blockedDate"
+ "_blockingReason"
+ "_container"
+ "_invocationArguments"
+ "_libraryParametersForPrivateEngine"
+ "_processStorage"
+ "_removeShareURLFromPhotosShare:"
+ "_storage"
+ "arguments"
+ "blockedDate"
+ "blockingReason"
+ "cloudphotodProcessStorage"
+ "collectConcurrencyLimiterRecordings"
+ "collectFetchRecordings"
+ "collectRecordingsWithSubcommand:label:filename:"
+ "com.apple.Photos.TestManatee"
+ "concurrency limiter recordings"
+ "concurrency_recording_paths.json"
+ "configurationForTestManateeContainer"
+ "container"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "defaultTransportContainerConfiguration"
+ "defaultTransportContainerConfigurationForE2E"
+ "e2eTests"
+ "engine.processstorage"
+ "error creating redactURLFunction function to remove Photos storage: remove shareURL from MomentShare"
+ "fetch recordings"
+ "getStatusForComponents:timeout:completionHandler:"
+ "group.com.apple.photolibraryd.private"
+ "initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:transportContainerConfiguration:"
+ "initWithName:mainScopeIdentifier:libraryIdentifier:libraryOptions:container:baseURL:"
+ "initWithName:universeName:libraryIdentifier:libraryOptions:container:baseURL:"
+ "initWithOldPlist:"
+ "initWithParameters:clientCount:isOpened:blockedDate:blockingReason:openError:"
+ "initWithProcessStorage:"
+ "initWithProcessStorage:supportedLibraryIdentifiers:"
+ "initWithSuiteName:"
+ "initialize"
+ "isCPLErrorWithCode:"
+ "isCPLLibraryParametersStorageKey:"
+ "libraryParameters"
+ "libraryParametersForPrivateEngine"
+ "locr"
+ "mainBundle"
+ "manateeTests"
+ "nTimeURL"
+ "now"
+ "participants"
+ "processStorage"
+ "putBrightF:arguments:"
+ "q24@?0@\"CPLLibraryParameters\"8@\"CPLLibraryParameters\"16"
+ "redactURLFunction"
+ "search/leo.sqlite"
+ "search_photos_summary.txt"
+ "search_syndication_summary.txt"
+ "setNTimeURL:"
+ "stringFromDateAgo:now:"
+ "testManateeApp"
+ "update ZSHARE set ZSHAREURL = redactURLFunction(ZSHAREURL), ZPREVIEWDATA = null, ZTHUMBNAILIMAGEDATA = null, ZCKSHAREDATA = null"
+ "update ZSHAREPARTICIPANT set ZNTIMEURL = redactURLFunction(ZNTIMEURL)"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSDictionary\"^B>16"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "~/Library/Logs/PhotosCollectionShareMigration.aapbz"
+ "~/Library/Logs/PhotosCollectionShareMigration.aapbz.old"
- "  redacted %d moment shares"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Daemon/CPLEngineParameters.m"
- "<%@ for %@ at %@>"
- "@\"CPLEngineParameters\""
- "@\"CPLEngineParameters\"24@0:8@\"NSString\"16"
- "@\"NSArray\"16@0:8"
- "@40@0:8@16@24@32"
- "@44@0:8@16Q24B32@36"
- "@56@0:8@16@24@32Q40@48"
- "@64@0:8@16@24@32@40@48Q56"
- "Automatically renaming %{public}@ to %@"
- "B32@0:8@\"CPLEngineParameters\"16^@24"
- "B32@0:8@\"NSString\"16^@24"
- "CPLEngineParameters"
- "CPLEngineParametersStorage"
- "CPLTestPrivateEngineDisableScopeSync"
- "Client asked to store some weird path for %@: %@"
- "Discarding old engine info for %{public}@"
- "Discarding old invalid engine info for %{public}@: %@"
- "Failed to serialize %@: %@"
- "Finding fetch recordings"
- "Identifying fetch recordings..."
- "Invalid plist from coder: %@"
- "MobileSlideShow"
- "T@\"CPLEngineParameters\",R,N,V_parameters"
- "T@\"NSString\",R,C,N,V_libraryIdentifier"
- "T@\"NSString\",R,C,N,V_mainScopeIdentifier"
- "T@\"NSURL\",R,C,N,V_clientLibraryBaseURL"
- "T@\"NSURL\",R,C,N,V_cloudLibraryResourceStorageURL"
- "T@\"NSURL\",R,C,N,V_cloudLibraryStateStorageURL"
- "TQ,R,N,V_options"
- "_CPLLibraryPathInsanityCheckDate."
- "_clientLibraryBaseURL"
- "_cloudLibraryResourceStorageURL"
- "_cloudLibraryStateStorageURL"
- "_keyForInsanityForLibraryIdentifier:"
- "_options"
- "_removeKeyForInsanityForLibraryIdentifier:"
- "_removeShareURLFromPhotosMomentShare:"
- "_setKeyForInsanityIfNecessaryForParameters:"
- "clientLibraryBasePath"
- "cloudLibraryResourceStoragePath"
- "cloudLibraryResourceStorageURL"
- "cloudLibraryStateStoragePath"
- "cloudLibraryStateStorageURL"
- "collectLOFetchRecordings"
- "data"
- "dictionaryForKey:"
- "error creating filterMomentShare function to remove Photos storage: remove shareURL from MomentShare"
- "filterMomentShareURL"
- "getStatusForComponents:completionHandler:"
- "initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:"
- "initWithName:mainScopeIdentifier:libraryIdentifier:libraryOptions:baseURL:"
- "initWithName:universeName:libraryIdentifier:libraryOptions:baseURL:"
- "initWithParameters:clientCount:isOpened:openError:"
- "initWithUserDefaults:bundleIdentifier:supportedLibraryIdentifiers:"
- "isCPLEngineParametersStorageKey:"
- "libraryManagerDidStartSynchronization:"
- "matchesParameters:"
- "q24@?0@\"CPLEngineParameters\"8@\"CPLEngineParameters\"16"
- "redactedDescription"
- "storage"
- "synchronize"
- "update ZSHARE set ZSHAREURL = filterMomentShareURL(ZSHAREURL), ZPREVIEWDATA = null, ZTHUMBNAILIMAGEDATA = null, ZCKSHAREDATA = null"

```
