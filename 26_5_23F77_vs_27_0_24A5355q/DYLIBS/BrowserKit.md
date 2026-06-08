## BrowserKit

> `/System/Library/Frameworks/BrowserKit.framework/BrowserKit`

```diff

-624.2.5.10.4
-  __TEXT.__text: 0x121d0
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x7ac
-  __TEXT.__cstring: 0x8c8
+625.1.18.10.4
+  __TEXT.__text: 0x11780
+  __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0xa50
+  __TEXT.__cstring: 0x8d8
   __TEXT.__oslogstring: 0x3f
   __TEXT.__swift5_typeref: 0x609
   __TEXT.__swift5_reflstr: 0xe4

   __TEXT.__swift5_capture: 0x238
   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x718
-  __TEXT.__eh_frame: 0x9d0
-  __TEXT.__objc_classname: 0x28b
-  __TEXT.__objc_methname: 0x1067
-  __TEXT.__objc_methtype: 0x56f
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x110
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__swift_as_cont: 0x7c
+  __TEXT.__unwind_info: 0x738
+  __TEXT.__eh_frame: 0x9a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x310
+  __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x990
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x10c8
-  __AUTH.__objc_data: 0x738
+  __AUTH_CONST.__objc_const: 0x1198
+  __AUTH_CONST.__auth_got: 0x4a8
+  __AUTH.__objc_data: 0x788
   __AUTH.__data: 0x260
-  __DATA.__data: 0x4e8
+  __DATA.__objc_ivar: 0x4
+  __DATA.__data: 0x4d8
   __DATA.__bss: 0xc80
+  - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C3BD6571-2745-3940-9974-6F2CFACD3639
-  Functions: 617
-  Symbols:   536
-  CStrings:  256
+  UUID: ABB00DAB-792A-356B-855D-ECDC4C1161EF
+  Functions: 616
+  Symbols:   641
+  CStrings:  59
 
Symbols:
+ -[BEBrowserContentFilter .cxx_destruct]
+ -[BEBrowserContentFilter evaluateURL:completionHandler:]
+ -[BEBrowserContentFilter filter]
+ -[BEBrowserContentFilter setFilter:]
+ _OBJC_CLASS_$_BEBrowserContentFilter
+ _OBJC_CLASS_$_BEWebContentFilter
+ _OBJC_IVAR_$_BEBrowserContentFilter._filter
+ _OBJC_METACLASS_$_BEBrowserContentFilter
+ __OBJC_$_INSTANCE_METHODS_BEBrowserContentFilter
+ __OBJC_$_INSTANCE_VARIABLES_BEBrowserContentFilter
+ __OBJC_$_PROP_LIST_BEBrowserContentFilter
+ __OBJC_CLASS_RO_$_BEBrowserContentFilter
+ __OBJC_METACLASS_RO_$_BEBrowserContentFilter
+ __PROTOCOLS_BEExportMetadata.19
+ __PROTOCOLS_BEExportOptions.15
+ ___56-[BEBrowserContentFilter evaluateURL:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e19_v20?0B8"NSData"12ls32l8
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.15
+ ___swift_closure_destructor.15Tm
+ ___swift_closure_destructor.19
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.30Tm
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.36
+ ___swift_closure_destructor.37
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.42Tm
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.51
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.64
+ ___swift_closure_destructor.66
+ ___swift_closure_destructor.69
+ ___swift_closure_destructorTm
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_BrowserKit
+ _block_copy_helper.44
+ _block_copy_helper.52
+ _block_copy_helper.60
+ _block_copy_helper.68
+ _block_descriptor.46
+ _block_descriptor.54
+ _block_descriptor.62
+ _block_descriptor.70
+ _block_destroy_helper.45
+ _block_destroy_helper.53
+ _block_destroy_helper.61
+ _block_destroy_helper.69
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$evaluateURL:completionHandler:
+ _objc_msgSend$filter
+ _objc_msgSend$setFilter:
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_storeStrong
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x24
- __PROTOCOLS_BEExportMetadata.15
- __PROTOCOLS_BEExportOptions.11
- _block_copy_helper.40
- _block_copy_helper.48
- _block_copy_helper.56
- _block_copy_helper.64
- _block_descriptor.42
- _block_descriptor.50
- _block_descriptor.58
- _block_descriptor.66
- _block_destroy_helper.41
- _block_destroy_helper.49
- _block_destroy_helper.57
- _block_destroy_helper.65
- _objc_retain_x28
- _objectdestroy.15Tm
- _objectdestroy.26Tm
- _objectdestroy.38Tm
- _objectdestroyTm
CStrings:
+ "v20@?0B8@\"NSData\"12"
- ".cxx_destruct"
- "?"
- "@\"NSDate\""
- "@\"NSURL\""
- "@\"UIWindowScene\""
- "@\"_TtC10BrowserKit22BrowserKitServiceProxy\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@28@0:8B16Q20"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@52@0:8B16@20@28@36@44"
- "@52@0:8B16q20q28q36q44"
- "@88@0:8@16@24@32B40B44@48@56@64@72q80"
- "B"
- "B16@0:8"
- "BEAvailability"
- "BEBrowserData"
- "BEBrowserDataBookmark"
- "BEBrowserDataExportManager"
- "BEBrowserDataExtension"
- "BEBrowserDataHistoryVisit"
- "BEBrowserDataImportManager"
- "BEBrowserDataReadingListItem"
- "BEExportMetadata"
- "BEExportOptions"
- "BEImportMetadata"
- "BEImportOptions"
- "BEKIntermediaryProtocol"
- "NSCoding"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"NSDate\",N,R"
- "T@\"NSDate\",N,R,V_dateOfLastVisit"
- "T@\"NSDate\",N,R,V_redirectDestinationDateOfVisit"
- "T@\"NSDate\",N,R,V_redirectSourceDateOfVisit"
- "T@\"NSString\",N,C"
- "T@\"NSString\",N,R"
- "T@\"NSURL\",N,R"
- "T@\"NSURL\",N,R,V_redirectDestinationURL"
- "T@\"NSURL\",N,R,V_redirectSourceURL"
- "T@\"NSURL\",N,R,V_url"
- "T@\"UIWindowScene\",N,R,Vscene"
- "T@\"UIWindowScene\",N,W,VwindowScene"
- "T@\"_TtC10BrowserKit22BrowserKitServiceProxy\",N,R,VbrowserKitServiceProxy"
- "TB,N,R"
- "TB,N,R,VexportToFiles"
- "TB,N,R,VhttpGet"
- "TB,N,R,VisFolder"
- "TB,N,R,VloadedSuccessfully"
- "TB,N,R,VsupportExportToFiles"
- "TB,N,R,VsupportImportFromFiles"
- "TB,N,VimportFromFiles"
- "TB,R"
- "TQ,N,R,VdataTypes"
- "Tq,N,R,VbookmarksCount"
- "Tq,N,R,VextensionsCount"
- "Tq,N,R,VhistoryCount"
- "Tq,N,R,VreadingListCount"
- "Tq,N,R,VvisitCount"
- "_TtC10BrowserKit22BrowserKitServiceProxy"
- "_TtC10BrowserKit23BrowserKitServiceClient"
- "_TtP10BrowserKit25BrowserKitServiceProtocol_"
- "_TtP10BrowserKit31BrowserKitServiceClientProtocol_"
- "_TtP10BrowserKit38BrowserKitViewServicePresenterProtocol_"
- "_dateOfLastVisit"
- "_redirectDestinationDateOfVisit"
- "_redirectDestinationURL"
- "_redirectSourceDateOfVisit"
- "_redirectSourceURL"
- "_sceneIdentifier"
- "_sourceApplicationBundleIdentifier"
- "_sourceApplicationLocalizedName"
- "_url"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "bookmarksCount"
- "browserKitServiceProxy"
- "client"
- "connection"
- "continuationPool"
- "dataTypes"
- "dateOfLastVisit"
- "dealloc"
- "decodeBoolForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "developerName"
- "displayName"
- "encodeBool:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "exportBrowserData:completionHandler:"
- "exportFinishedWithCompletionHandler:"
- "exportFinishedWithReply:"
- "exportToFiles"
- "exportWithBrowserData:reply:"
- "extensionsCount"
- "getSceneIdentifierForPresentationAndReturnError:"
- "historyCount"
- "httpGet"
- "identifier"
- "importBlock"
- "importBrowserData:reply:"
- "importBrowserDataWithToken:importBlock:"
- "importBrowserDataWithToken:reply:"
- "importFromFiles"
- "init"
- "initAsFolder:title:identifier:url:parentIdentifier:"
- "initWithCoder:"
- "initWithDisplayName:developerName:identifier:storeIdentifier:"
- "initWithExportToFiles:dataTypes:"
- "initWithImportFromFiles:"
- "initWithMachServiceName:options:"
- "initWithScene:"
- "initWithServiceName:"
- "initWithSourceApplicationBundleIdentifier:sourceApplicationLocalizedName:"
- "initWithSupportForExportToFiles:bookmarksCount:readingListCount:historyCount:extensionsCount:"
- "initWithSupportForImportFromFiles:"
- "initWithTitle:url:dateOfLastVisit:"
- "initWithURL:dateOfLastVisit:title:loadedSuccessfully:httpGet:redirectSourceURL:redirectSourceDateOfVisit:redirectDestinationURL:redirectDestinationDateOfVisit:visitCount:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEligibleForContext:completionHandler:"
- "isFolder"
- "q"
- "q16@0:8"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "requestExportForMetadata:token:completionHandler:"
- "requestExportWithMetadata:token:sceneIdentifier:reply:"
- "requestImportForMetadata:completionHandler:"
- "requestImportWithMetadata:sceneIdentifier:reply:"
- "resume"
- "safari_privacyPreservingDescription"
- "scene"
- "setExportedInterface:"
- "setExportedObject:"
- "setImportFromFiles:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setWindowScene:"
- "set_sourceApplicationBundleIdentifier:"
- "set_sourceApplicationLocalizedName:"
- "storeIdentifier"
- "supportsSecureCoding"
- "title"
- "url"
- "userDidCancelBrowserDataExchange"
- "userDidElectToExportToFiles"
- "userDidElectToImportFromFiles"
- "userDidSelectExportingSourceWithApplicationIdentifier:"
- "userDidSelectImportingDestinationWithApplicationIdentifier:includeBookmarks:includeReadingList:includeHistory:includeExtensions:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@?0@\"BEExportOptions\"8@\"NSError\"16"
- "v24@?0@\"BEImportOptions\"8@\"NSError\"16"
- "v32@0:8@\"BEBrowserData\"16@?<v@?>24"
- "v32@0:8@\"BEBrowserData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"BEImportMetadata\"16@?<v@?@\"BEImportOptions\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?B@\"NSError\">24"
- "v40@0:8@\"BEExportMetadata\"16@\"NSUUID\"24@?<v@?@\"BEExportOptions\"@\"NSError\">32"
- "v40@0:8@\"BEImportMetadata\"16@\"NSString\"24@?<v@?@\"BEImportOptions\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16B24B28B32B36"
- "v40@0:8@16@24@?32"
- "v40@0:8@16B24B28B32B36"
- "v48@0:8@\"BEExportMetadata\"16@\"NSUUID\"24@\"NSString\"32@?<v@?@\"BEExportOptions\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v8@?0"
- "visitCount"
- "windowScene"

```
