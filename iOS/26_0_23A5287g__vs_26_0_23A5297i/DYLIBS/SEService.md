## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

```diff

-60.31.0.0.0
-  __TEXT.__text: 0xde6ec
-  __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_methlist: 0x3444
-  __TEXT.__const: 0x148d0
-  __TEXT.__cstring: 0x8691
-  __TEXT.__gcc_except_tab: 0x1dc4
-  __TEXT.__oslogstring: 0x2027
+60.32.0.0.0
+  __TEXT.__text: 0xdfcac
+  __TEXT.__auth_stubs: 0x1cf0
+  __TEXT.__objc_methlist: 0x34fc
+  __TEXT.__const: 0x148c0
+  __TEXT.__cstring: 0x8911
+  __TEXT.__gcc_except_tab: 0x1e3c
+  __TEXT.__oslogstring: 0x21c7
+  __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__swift5_typeref: 0x3caa
   __TEXT.__swift5_reflstr: 0x1452
   __TEXT.__swift5_assocty: 0x2d0

   __TEXT.__swift_as_entry: 0xdc
   __TEXT.__swift_as_ret: 0x9c
   __TEXT.__swift5_capture: 0x208
-  __TEXT.__unwind_info: 0x4428
+  __TEXT.__unwind_info: 0x4490
   __TEXT.__eh_frame: 0x4e14
-  __TEXT.__objc_classname: 0x5f2
-  __TEXT.__objc_methname: 0x7e02
-  __TEXT.__objc_methtype: 0x26e5
-  __TEXT.__objc_stubs: 0x3f20
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x1368
-  __DATA_CONST.__objc_classlist: 0x2b0
+  __TEXT.__objc_classname: 0x603
+  __TEXT.__objc_methname: 0x80b8
+  __TEXT.__objc_methtype: 0x27ae
+  __TEXT.__objc_stubs: 0x41e0
+  __DATA_CONST.__got: 0x5d0
+  __DATA_CONST.__const: 0x1418
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1860
+  __DATA_CONST.__objc_selrefs: 0x1920
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0xe28
-  __AUTH_CONST.__const: 0x8d30
-  __AUTH_CONST.__cfstring: 0x42c0
-  __AUTH_CONST.__objc_const: 0x7868
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0xc8
+  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__const: 0x8d50
+  __AUTH_CONST.__cfstring: 0x4680
+  __AUTH_CONST.__objc_const: 0x7a28
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xdc0
+  __AUTH.__objc_data: 0xe10
   __AUTH.__data: 0xc88
-  __DATA.__objc_ivar: 0x39c
+  __DATA.__objc_ivar: 0x3c0
   __DATA.__data: 0x43e8
-  __DATA.__bss: 0x22980
+  __DATA.__bss: 0x229a0
   __DATA.__common: 0xf0
   __DATA_DIRTY.__objc_data: 0x1710
   __DATA_DIRTY.__data: 0x238

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libAppleSSE.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F0623780-923B-36E5-AA4A-A827154C0BBD
-  Functions: 5862
-  Symbols:   5922
-  CStrings:  3229
+  UUID: FB75983F-9173-33D4-AE42-496CE55C94C6
+  Functions: 5888
+  Symbols:   6044
+  CStrings:  3347
 
Symbols:
+ +[SESTapToRadar getInstance]
+ +[SESTapToRadar getInstance].cold.1
+ +[SESTapToRadar handleCallback:]
+ +[SESTapToRadar isAllowedForClient:]
+ +[SESTapToRadar requestTapToRadar:client:]
+ +[SESTapToRadar requestTapToRadar:client:fullArchive:]
+ +[SESTapToRadar requestTapToRadarKML:client:]
+ -[SEFidoKeyService findAndAttest:challenge:usingSession:withSessionSEID:error:]
+ -[SESTapToRadar .cxx_destruct]
+ -[SESTapToRadar _handleCallbackSync:]
+ -[SESTapToRadar _requestTapToRadarSync:component:client:fullArchive:]
+ -[SESTapToRadar init]
+ -[SESTapToRadar isAllowedForClient:]
+ -[SESTapToRadar setProhibitUntil:forClient:]
+ _CFRunLoopAddSource
+ _CFRunLoopGetMain
+ _CFRunLoopRemoveSource
+ _CFUserNotificationCreate
+ _CFUserNotificationCreateRunLoopSource
+ _NFTTRUserNotificationCallback
+ _NSClassFromString
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_SESTapToRadar
+ _OBJC_IVAR_$_SESTapToRadar._component
+ _OBJC_IVAR_$_SESTapToRadar._lsApplicationWorkspace
+ _OBJC_IVAR_$_SESTapToRadar._pendingRequestClient
+ _OBJC_IVAR_$_SESTapToRadar._pendingRequestReason
+ _OBJC_IVAR_$_SESTapToRadar._queue
+ _OBJC_IVAR_$_SESTapToRadar._runLoopSource
+ _OBJC_IVAR_$_SESTapToRadar._ttrOptions
+ _OBJC_IVAR_$_SESTapToRadar._userDefaults
+ _OBJC_IVAR_$_SESTapToRadar._userNotification
+ _OBJC_METACLASS_$_SESTapToRadar
+ _SpringBoardServicesLibraryCore
+ _SpringBoardServicesLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_SESTapToRadar
+ __OBJC_$_INSTANCE_METHODS_SESTapToRadar
+ __OBJC_$_INSTANCE_VARIABLES_SESTapToRadar
+ __OBJC_CLASS_RO_$_SESTapToRadar
+ __OBJC_METACLASS_RO_$_SESTapToRadar
+ ___28+[SESTapToRadar getInstance]_block_invoke
+ ___32+[SESTapToRadar handleCallback:]_block_invoke
+ ___45+[SESTapToRadar requestTapToRadarKML:client:]_block_invoke
+ ___54+[SESTapToRadar requestTapToRadar:client:fullArchive:]_block_invoke
+ ___79-[SEFidoKeyService findAndAttest:challenge:usingSession:withSessionSEID:error:]_block_invoke
+ ___SpringBoardServicesLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___getSBUserNotificationDismissOnLockSymbolLoc_block_invoke
+ ___kCFBooleanFalse
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringSpringBoardServices
+ _dispatch_assert_queue$V2
+ _dlerror
+ _dlopen
+ _dlsym
+ _getInstance.instance
+ _getInstance.onceToken
+ _getSBUserNotificationDismissOnLock
+ _getSBUserNotificationDismissOnLock.cold.1
+ _getSBUserNotificationDismissOnLockSymbolLoc.ptr
+ _kCFRunLoopCommonModes
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlertTopMostKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kCFUserNotificationOtherButtonTitleKey
+ _objc_msgSend$URL
+ _objc_msgSend$_handleCallbackSync:
+ _objc_msgSend$_requestTapToRadarSync:component:client:fullArchive:
+ _objc_msgSend$compare:
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$distantFuture
+ _objc_msgSend$findAndAttest:challenge:usingProxy:callback:
+ _objc_msgSend$getInstance
+ _objc_msgSend$handleCallback:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$isAllowedForClient:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$requestTapToRadar:client:fullArchive:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setProhibitUntil:forClient:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$synchronize
CStrings:
+ "#"
+ "/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices"
+ "1.0"
+ "991522"
+ "997328"
+ "ALL"
+ "AutoDiagnostics"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Couldn't create notification! %d"
+ "Couldn't create runloop source"
+ "Crash/Hang/Data Loss"
+ "Description"
+ "Discarding TTR request, already in flight"
+ "Failed to dlopen %{public}s"
+ "Failed to get class %{public}@"
+ "File Radar"
+ "Find FiDO key %@"
+ "I Didn't Try"
+ "Ignoring TTR callback with no pending request"
+ "KML"
+ "LSApplicationWorkspace"
+ "Missing SB notif key SBUserNotificationDismissOnLock"
+ "Never bother me again"
+ "Not Now"
+ "NotNow response"
+ "Please file a Radar"
+ "Reproducibility"
+ "SBUserNotificationDismissOnLock"
+ "SESTapToRadar"
+ "SecureElementService Error Detected!"
+ "SecureElementService KML TTR - %@"
+ "SecureElementService TTR - %@"
+ "Serious Bug"
+ "TTR is prohibited until %{public}@"
+ "TTR prompt created for %@"
+ "TTR-Prohibit-Until-ByClient"
+ "Title"
+ "URL"
+ "URL: %{public}@"
+ "User canceled response for %@/%@"
+ "Vv48@0:8@\"SEFidoKeySearchParameters\"16@\"NSData\"24@\"<SEProxyInterface>\"32@?<v@?@\"SEFidoKey\"@\"NSError\">40"
+ "[SEFidoKeyService findAndAttest] -> findAndAttest"
+ "^{__CFRunLoopSource=}"
+ "^{__CFUserNotification=}"
+ "_component"
+ "_handleCallbackSync:"
+ "_lsApplicationWorkspace"
+ "_pendingRequestClient"
+ "_pendingRequestReason"
+ "_requestTapToRadarSync:component:client:fullArchive:"
+ "_runLoopSource"
+ "_ttrOptions"
+ "_userDefaults"
+ "_userNotification"
+ "com.apple.secureelementservice"
+ "com.apple.sesd.TTR"
+ "compare:"
+ "date"
+ "dateWithTimeIntervalSinceNow:"
+ "defaultWorkspace"
+ "distantFuture"
+ "findAndAttest:challenge:usingProxy:callback:"
+ "findAndAttest:challenge:usingSession:withSessionSEID:error:"
+ "full-log-archive"
+ "getInstance"
+ "handleCallback:"
+ "initWithFormat:"
+ "isAllowedForClient:"
+ "new"
+ "openURL:configuration:completionHandler:"
+ "queryItemWithName:value:"
+ "requestTapToRadar:client:"
+ "requestTapToRadar:client:fullArchive:"
+ "requestTapToRadarKML:client:"
+ "setHost:"
+ "setProhibitUntil:forClient:"
+ "setQueryItems:"
+ "setScheme:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
+ "synchronize"
+ "tap-to-radar"
+ "v24@0:8Q16"
+ "v36@0:8@16@24B32"
+ "v44@0:8@16@24@32B40"

```
