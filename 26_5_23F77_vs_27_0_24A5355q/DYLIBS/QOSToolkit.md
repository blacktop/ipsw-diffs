## QOSToolkit

> `/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit`

```diff

 2025.1.0.0.0
-  __TEXT.__text: 0x23398
-  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__text: 0x21c98
   __TEXT.__objc_methlist: 0x208
   __TEXT.__const: 0x2ea0
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0xbd5
+  __TEXT.__cstring: 0xba5
   __TEXT.__swift5_typeref: 0x7c2
   __TEXT.__swift5_fieldmd: 0xc8c
   __TEXT.__constg_swiftt: 0x91c

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift_as_cont: 0xac
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x178
-  __TEXT.__unwind_info: 0xb88
-  __TEXT.__eh_frame: 0x1290
-  __TEXT.__objc_classname: 0x202
-  __TEXT.__objc_methname: 0x60f
-  __TEXT.__objc_methtype: 0x272
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x140
+  __TEXT.__swift5_capture: 0x198
+  __TEXT.__unwind_info: 0xb68
+  __TEXT.__eh_frame: 0x1240
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x190
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x758
-  __AUTH_CONST.__const: 0x2389
+  __DATA_CONST.__got: 0x188
+  __AUTH_CONST.__const: 0x23d9
   __AUTH_CONST.__objc_const: 0xdc0
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0xc

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B2A6B56A-DC4C-3602-9F7B-7E494DD7AC43
-  Functions: 942
-  Symbols:   667
-  CStrings:  226
+  UUID: 87B94464-096C-3982-A83F-2FFC2166ACB2
+  Functions: 934
+  Symbols:   745
+  CStrings:  116
 
Symbols:
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.21
+ ___swift_closure_destructor.21Tm
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.4
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.9
+ ___swift_closure_destructor.9Tm
+ ___swift_closure_destructorTm
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_QOSToolkit
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x3
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
- _objectdestroy.22Tm
- _objectdestroy.9Tm
- _objectdestroyTm
- _swift_errorRetain
- _swift_setDeallocating
- _swift_unexpectedError
CStrings:
- ".cxx_destruct"
- "?"
- "@\"<ObjcQOSErrorMessageProtocolInternal>\""
- "@\"QOSAlertMessageInternal\""
- "@\"QOSAlertMessageInternal\"32@0:8@\"NSDictionary\"16@\"NSError\"24"
- "@\"QOSConfigInternal\""
- "@16@0:8"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@48@0:8@16@?24@?32@?40"
- "@56@0:8@16^@24@?32@?40@?48"
- "@?16@0:8"
- "ObjcQOSErrorMessageProtocolInternal"
- "QOSAlertMessage"
- "QOSAlertMessageInternal"
- "QOSConfig"
- "QOSConfigInternal"
- "QOSErrorMessage"
- "QOSErrorMessageInternal"
- "Swift/Dictionary.swift"
- "T@\"<ObjcQOSErrorMessageProtocolInternal>\",R,V_underlyingObject"
- "T@\"NSString\",N,R"
- "T@\"QOSAlertMessageInternal\",R,V_underlyingObject"
- "T@\"QOSConfigInternal\",R,V_underlyingObject"
- "T@?,N,R"
- "Tq,N,R,VappTarget"
- "URLCache"
- "_TtC10QOSToolkit15LocationService"
- "_TtC10QOSToolkit15TVIssuesService"
- "_TtC10QOSToolkit18MusicIssuesService"
- "_TtC10QOSToolkit22TVPlaybackErrorMessage"
- "_TtC10QOSToolkit25MusicPlaybackErrorMessage"
- "_TtC10QOSToolkit4Util"
- "_TtC10QOSToolkit7Network"
- "_TtC10QOSToolkit9QoSDevice"
- "_underlyingObject"
- "appTarget"
- "bagForProfile:profileVersion:"
- "bagTask"
- "bundleWithIdentifier:"
- "cache"
- "cachedResponseForRequest:"
- "code"
- "config"
- "configuration"
- "currentDevice"
- "data"
- "dateFormatter"
- "dateFromString:"
- "dealloc"
- "defaultAlert"
- "defaultSessionConfiguration"
- "description"
- "fetchLocalizedErrorMessageForItems::completionHandler:"
- "fetchLocalizedErrorMessageForItems:usingError:completionHandler:"
- "getLocalizedErrorMessageForItems::"
- "getLocalizedErrorMessageForItems:usingError:"
- "getObjcInstanceWithConfig:error:logger:metricsRecorder:defaultAlert:"
- "init"
- "initWithAppTarget:locale:"
- "initWithConfig:logger:metricsRecorder:defaultAlert:"
- "initWithTitle:body:"
- "integerForKey:"
- "invalidate"
- "issueRefreshFrequencyInSecs"
- "issuesUrl"
- "locationRefreshFrequencyInSecs"
- "locationService"
- "locationUrl"
- "logger"
- "mainBundle"
- "metricsRecorder"
- "model"
- "network"
- "q"
- "q16@0:8"
- "removeCachedResponseForRequest:"
- "response"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "service"
- "session"
- "sessionWithConfiguration:"
- "setDateFormat:"
- "setLocale:"
- "setLocalizedDateFormatFromTemplate:"
- "setTimeZone:"
- "sharedSession"
- "statusCode"
- "stringForKey:"
- "stringFromDate:"
- "syncStartDelayOffsetInSecs"
- "systemName"
- "systemVersion"
- "underlyingObject"
- "v16@0:8"
- "v16@?0@\"NSDictionary\"8"
- "v16@?0@\"NSTimer\"8"
- "v28@?0@\"NSNumber\"8B16@\"NSError\"20"
- "v28@?0@\"NSString\"8B16@\"NSError\"20"
- "v40@0:8@\"NSDictionary\"16@\"NSError\"24@?<v@?@\"QOSAlertMessageInternal\">32"
- "v40@0:8@16@24@?32"
- "valueForHTTPHeaderField:"
- "valueWithCompletion:"

```
