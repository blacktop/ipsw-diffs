## AdPlatformsCommonUI

> `/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI`

```diff

-556.5.31.0.0
-  __TEXT.__text: 0x143c
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x304
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x136
-  __TEXT.__oslogstring: 0x19b
+557.1.16.0.0
+  __TEXT.__text: 0xa98
+  __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x98
-  __TEXT.__objc_methname: 0xb4a
-  __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__cstring: 0x18
+  __TEXT.__oslogstring: 0x152
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x48
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x320
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x3a0
+  __AUTH_CONST.__objc_const: 0x310
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x120
-  __DATA.__bss: 0x1
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1CE8358-C70C-3736-9F3E-11271491A845
-  Functions: 29
-  Symbols:   77
-  CStrings:  181
+  UUID: 2849033B-0632-3580-AB0F-7A94F1936D09
+  Functions: 23
+  Symbols:   60
+  CStrings:  8
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _APSimulateCrash
- _NSURLErrorDomain
- _OBJC_CLASS_$_APAnalytics
- _OBJC_CLASS_$_APSystemInternal
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSHTTPURLResponse
- _OBJC_CLASS_$_NSString
- ___CFConstantStringClassReference
- ___stack_chk_fail
- ___stack_chk_guard
- _gProxyIsRunning
- _objc_autorelease
- _objc_opt_self
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x23
CStrings:
- "%ld"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDictionary\"8@?0"
- "@16@0:8"
- "@24@0:8@16"
- "APClientInfoUI"
- "APGreenTeaLogger"
- "APGreenTeaLogging"
- "APWebProcessDelegate"
- "APWebProcessProxyProtocol"
- "APWebViewResourceLoadCAReporter"
- "AdEmptyDomainErrors"
- "AdHTTPErrors"
- "AdNilDomainErrors"
- "AdPlatformsCommonUI"
- "AdWebViewErrors"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "Redirection to URL with a scheme that is not HTTP(S)"
- "T@\"NSArray\",&,N,V_userKeyboards"
- "T^{ct_green_tea_logger_s=},R,N,V_logger"
- "WebKit custom protocols were not registered. Proxy is running: %d"
- "WebView (%{mask.hash}p) request failed: %{public}@:%ld. Host: %{public}@"
- "^{ct_green_tea_logger_s=}"
- "^{ct_green_tea_logger_s=}16@0:8"
- "_isHTTPOrHTTPSURL:"
- "_logger"
- "_parseResourceLoadResultForError:response:result:errorDomain:errorCode:"
- "_remoteObjectRegistry"
- "_setInputDelegate:"
- "_setObservedRenderingProgressEvents:"
- "_setRemoteInspectionNameOverride:"
- "_setResourceLoadDelegate:"
- "_userKeyboards"
- "_webView:focusShouldStartInputSession:"
- "actionDidFailWithErrorDescription:"
- "addObserver:selector:name:object:"
- "blob"
- "bounds"
- "caseInsensitiveCompare:"
- "code"
- "contentSizeDidChange:"
- "copy"
- "creativeStateDidChange:"
- "creativeVisibilityDidChange:"
- "currentDevice"
- "dealloc"
- "defaultCenter"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "error"
- "hasPrefix:"
- "host"
- "http"
- "https"
- "init"
- "initForTesting"
- "isAppleInternalInstall"
- "isEqualToString:"
- "isMainThread"
- "keyboards"
- "length"
- "logger"
- "mainScreen"
- "normalizedEnabledInputModeIdentifiers"
- "null"
- "numberWithDouble:"
- "numberWithInteger:"
- "object"
- "orientation"
- "orientationChanged:"
- "originalURL"
- "registerExportedObject:interface:"
- "registerExportedObjectInterface:"
- "remoteObjectInterfaceWithProtocol:"
- "remoteObjectProxyWithInterface"
- "remoteObjectProxyWithInterface:"
- "removeObserver:"
- "resetSession"
- "resetVideoTagPlaytime"
- "resourceSpecifier"
- "result"
- "scale"
- "scheme"
- "sendEventLazy:eventPayloadBuilder:"
- "setExpandedWidth:andHeight:"
- "setInterfaceIdiom:"
- "setOrientation:"
- "setRemoteInspectionNameOverride:"
- "setScale:"
- "setScreenHeight:"
- "setScreenWidth:"
- "setUserKeyboards:"
- "setWebViewProcessAdIdentifier:maxRequestCount:"
- "setupInternalProperties"
- "sharedInputModeController"
- "sharedInstance"
- "statusCode"
- "stringWithFormat:"
- "unregisterExportedObject:interface:"
- "updateActiveClientInfo"
- "userInterfaceIdiom"
- "userKeyboards"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\"B@\"NSDictionary\">16"
- "v24@0:8Q16"
- "v24@0:8f16f20"
- "v24@0:8q16"
- "v28@0:8B16f20f24"
- "v32@0:8@\"NSString\"16@\"NSNumber\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8d16d24"
- "v40@0:8@\"NSURL\"16d24d32"
- "v40@0:8@16d24d32"
- "v48@0:8@16@24@32@40"
- "v56@0:8@16@24^q32^@40^q48"
- "webProcessDiagnosticJSOStatusReported:status:"
- "webProcessMRAIDJSODidCallClose"
- "webProcessMRAIDJSODidCallCreateCalendarEvent:"
- "webProcessMRAIDJSODidCallExpand:withMaximumWidth:andHeight:"
- "webProcessMRAIDJSODidCallOpen:"
- "webProcessPlugInBrowserContextControllerGlobalObjectIsAvailableForFrame"
- "webProcessPlugInDidCreateBrowserContextController"
- "webProcessPlugInWillDestroyBrowserContextController"
- "webProcessVideoAdJSOCreativeViewLoaded"
- "webProcessVideoAdJSODidCallAudioMuted:"
- "webProcessVideoAdJSODidCallAudioUnmuted:volume:"
- "webProcessVideoAdJSODidCallExitFullScreenTapped:volume:"
- "webProcessVideoAdJSODidCallFullScreenTapped:volume:"
- "webProcessVideoAdJSODidCallMoreInfoTapped:volume:"
- "webProcessVideoAdJSODidCallPlayCompletedWithVolume:"
- "webProcessVideoAdJSODidCallPlayPaused:volume:"
- "webProcessVideoAdJSODidCallPlayProgressed:volume:"
- "webProcessVideoAdJSODidCallPlayResumed:volume:"
- "webProcessVideoAdJSODidCallPlayStarted:volume:"
- "webProcessVideoAdJSODidCallSkipAdTapped:volume:"
- "webProcessVideoAdJSODidCallVideoTapped:volume:"
- "webProcessVideoAdJSODidCallViewabilityChanged:playTime:volume:"
- "webProcessVideoAdJSODidCallVolumeChanged:playTime:"
- "webProcessVideoAdJSOGetVideoInfo:"
- "webProcessVideoAdJSOMediaPlaybackFailedWithErrorDescription:"
- "webView:resourceLoad:didCompleteWithError:response:"
- "willAccessLocation"
- "willTransmitLocationFor:"
- "wk.resource.error"
- "wk.resource.result"

```
