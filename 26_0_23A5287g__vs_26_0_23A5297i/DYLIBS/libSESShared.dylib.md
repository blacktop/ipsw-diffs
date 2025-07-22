## libSESShared.dylib

> `/usr/lib/libSESShared.dylib`

```diff

-60.31.0.0.0
-  __TEXT.__text: 0xe174
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x900
-  __TEXT.__const: 0xa60
-  __TEXT.__cstring: 0xd0a
-  __TEXT.__oslogstring: 0x7d6
-  __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x3d0
-  __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x1530
-  __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__objc_stubs: 0x10a0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x68
+60.32.0.0.0
+  __TEXT.__text: 0xcc74
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x870
+  __TEXT.__const: 0xa50
+  __TEXT.__cstring: 0xa40
+  __TEXT.__oslogstring: 0x650
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__unwind_info: 0x380
+  __TEXT.__objc_classname: 0x11e
+  __TEXT.__objc_methname: 0x12bd
+  __TEXT.__objc_methtype: 0x482
+  __TEXT.__objc_stubs: 0xe40
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x730
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0xf38
+  __DATA_CONST.__objc_selrefs: 0x688
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_arraydata: 0x80
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0xd80
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x8
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24C33C23-0A56-38F3-9DC3-1645704CAA6C
-  Functions: 285
-  Symbols:   1058
-  CStrings:  778
+  UUID: DF6F12CA-9AF4-35FF-B6CE-B4EB84E061D9
+  Functions: 263
+  Symbols:   942
+  CStrings:  660
 
Symbols:
- +[SESTapToRadar getInstance]
- +[SESTapToRadar getInstance].cold.1
- +[SESTapToRadar handleCallback:]
- +[SESTapToRadar requestTapToRadar:client:]
- +[SESTapToRadar requestTapToRadar:client:fullArchive:]
- +[SESTapToRadar requestTapToRadarKML:client:]
- -[SESTapToRadar .cxx_destruct]
- -[SESTapToRadar _handleCallbackSync:]
- -[SESTapToRadar _requestTapToRadarSync:component:client:fullArchive:]
- -[SESTapToRadar init]
- -[SESTapToRadar setProhibitUntil:forClient:]
- GCC_except_table9
- _CFRunLoopAddSource
- _CFRunLoopGetMain
- _CFRunLoopRemoveSource
- _CFUserNotificationCreate
- _CFUserNotificationCreateRunLoopSource
- _NFTTRUserNotificationCallback
- _NSClassFromString
- _OBJC_CLASS_$_NSAssertionHandler
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSURLComponents
- _OBJC_CLASS_$_NSURLQueryItem
- _OBJC_CLASS_$_SESTapToRadar
- _OBJC_IVAR_$_SESTapToRadar._component
- _OBJC_IVAR_$_SESTapToRadar._lsApplicationWorkspace
- _OBJC_IVAR_$_SESTapToRadar._pendingRequestClient
- _OBJC_IVAR_$_SESTapToRadar._pendingRequestReason
- _OBJC_IVAR_$_SESTapToRadar._queue
- _OBJC_IVAR_$_SESTapToRadar._runLoopSource
- _OBJC_IVAR_$_SESTapToRadar._ttrOptions
- _OBJC_IVAR_$_SESTapToRadar._userDefaults
- _OBJC_IVAR_$_SESTapToRadar._userNotification
- _OBJC_METACLASS_$_SESTapToRadar
- _SpringBoardServicesLibraryCore
- _SpringBoardServicesLibraryCore.frameworkLibrary
- __OBJC_$_CLASS_METHODS_SESTapToRadar
- __OBJC_$_INSTANCE_METHODS_SESTapToRadar
- __OBJC_$_INSTANCE_VARIABLES_SESTapToRadar
- __OBJC_CLASS_RO_$_SESTapToRadar
- __OBJC_METACLASS_RO_$_SESTapToRadar
- ___28+[SESTapToRadar getInstance]_block_invoke
- ___32+[SESTapToRadar handleCallback:]_block_invoke
- ___45+[SESTapToRadar requestTapToRadarKML:client:]_block_invoke
- ___54+[SESTapToRadar requestTapToRadar:client:fullArchive:]_block_invoke
- ___NSDictionary0__struct
- ___SpringBoardServicesLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___getSBUserNotificationDismissOnLockSymbolLoc_block_invoke
- ___getSBUserNotificationDismissOnLockSymbolLoc_block_invoke.cold.1
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- __sl_dlopen
- _audit_stringSpringBoardServices
- _dispatch_async
- _dlerror
- _dlopen
- _dlsym
- _getSBUserNotificationDismissOnLock
- _getSBUserNotificationDismissOnLock.cold.1
- _getSBUserNotificationDismissOnLockSymbolLoc.ptr
- _kCFRunLoopCommonModes
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlertTopMostKey
- _kCFUserNotificationAlternateButtonTitleKey
- _kCFUserNotificationDefaultButtonTitleKey
- _kCFUserNotificationOtherButtonTitleKey
- _objc_msgSend$URL
- _objc_msgSend$_handleCallbackSync:
- _objc_msgSend$_requestTapToRadarSync:component:client:fullArchive:
- _objc_msgSend$compare:
- _objc_msgSend$currentHandler
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$distantFuture
- _objc_msgSend$handleCallback:
- _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$openURL:configuration:completionHandler:
- _objc_msgSend$queryItemWithName:value:
- _objc_msgSend$requestTapToRadar:client:fullArchive:
- _objc_msgSend$setHost:
- _objc_msgSend$setProhibitUntil:forClient:
- _objc_msgSend$setQueryItems:
- _objc_msgSend$setScheme:
- _objc_msgSend$synchronize
- _objc_retain_x27
CStrings:
- "#"
- "%s"
- "/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices"
- "1.0"
- "991522"
- "997328"
- "@\"NSUserDefaults\""
- "ALL"
- "AutoDiagnostics"
- "Classification"
- "ComponentID"
- "ComponentName"
- "ComponentVersion"
- "Couldn't create notification! %d"
- "Couldn't create runloop source"
- "Crash/Hang/Data Loss"
- "Description"
- "Discarding TTR request, already in flight"
- "Failed to dlopen %{public}s"
- "Failed to get class %{public}@"
- "File Radar"
- "I Didn't Try"
- "Ignoring TTR callback with no pending request"
- "KML"
- "LSApplicationWorkspace"
- "Missing SB notif key SBUserNotificationDismissOnLock"
- "NSString *getSBUserNotificationDismissOnLock(void)"
- "Never bother me again"
- "Not Now"
- "NotNow response"
- "Please file a Radar"
- "Reproducibility"
- "SBUserNotificationDismissOnLock"
- "SESTapToRadar"
- "SESTapToRadar.m"
- "SecureElementService"
- "SecureElementService Error Detected!"
- "SecureElementService KML TTR - %@"
- "SecureElementService TTR - %@"
- "Serious Bug"
- "TTR is prohibited until %{public}@"
- "TTR prompt created for %@"
- "TTR-Prohibit-Until-ByClient"
- "Title"
- "URL"
- "URL: %{public}@"
- "User canceled response for %@/%@"
- "^{__CFRunLoopSource=}"
- "^{__CFUserNotification=}"
- "_component"
- "_handleCallbackSync:"
- "_lsApplicationWorkspace"
- "_pendingRequestClient"
- "_pendingRequestReason"
- "_queue"
- "_requestTapToRadarSync:component:client:fullArchive:"
- "_runLoopSource"
- "_ttrOptions"
- "_userDefaults"
- "_userNotification"
- "com.apple.secureelementservice"
- "com.apple.sesd.TTR"
- "compare:"
- "currentHandler"
- "dateWithTimeIntervalSinceNow:"
- "defaultWorkspace"
- "distantFuture"
- "full-log-archive"
- "handleCallback:"
- "handleFailureInFunction:file:lineNumber:description:"
- "initWithFormat:"
- "new"
- "openURL:configuration:completionHandler:"
- "queryItemWithName:value:"
- "requestTapToRadar:client:"
- "requestTapToRadar:client:fullArchive:"
- "requestTapToRadarKML:client:"
- "setHost:"
- "setProhibitUntil:forClient:"
- "setQueryItems:"
- "setScheme:"
- "softlink:o:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
- "synchronize"
- "tap-to-radar"
- "v36@0:8@16@24B32"
- "v44@0:8@16@24@32B40"
- "void *SpringBoardServicesLibrary(void)"

```
