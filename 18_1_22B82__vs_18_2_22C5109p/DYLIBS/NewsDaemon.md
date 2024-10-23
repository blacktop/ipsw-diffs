## NewsDaemon

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon`

```diff

-5593.0.0.0.0
-  __TEXT.__text: 0xaa2c
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0x62c
-  __TEXT.__const: 0x4d4
-  __TEXT.__cstring: 0xce9
+5604.1.0.0.0
+  __TEXT.__text: 0xc5f0
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x6ec
+  __TEXT.__const: 0x514
+  __TEXT.__cstring: 0xe99
   __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__oslogstring: 0x36f
+  __TEXT.__oslogstring: 0x5a9
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__swift5_typeref: 0x141
-  __TEXT.__swift5_fieldmd: 0x1a8
-  __TEXT.__constg_swiftt: 0xfc
-  __TEXT.__swift5_reflstr: 0x149
-  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_typeref: 0x1a3
+  __TEXT.__swift5_fieldmd: 0x1dc
+  __TEXT.__constg_swiftt: 0x128
+  __TEXT.__swift5_reflstr: 0x199
+  __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x458
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x1b3
-  __TEXT.__objc_methname: 0x13aa
-  __TEXT.__objc_methtype: 0x5f5
-  __TEXT.__objc_stubs: 0xf40
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__objc_classname: 0x1d6
+  __TEXT.__objc_methname: 0x151e
+  __TEXT.__objc_methtype: 0x69f
+  __TEXT.__objc_stubs: 0xfc0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x3a0
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c8
-  __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__auth_ptr: 0x170
-  __AUTH_CONST.__const: 0x348
-  __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x15c0
-  __AUTH.__objc_data: 0x1b0
-  __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x588
-  __DATA.__bss: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x520
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_ptr: 0x188
+  __AUTH_CONST.__const: 0x408
+  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__objc_const: 0x17f0
+  __AUTH.__objc_data: 0x2c8
+  __AUTH.__data: 0xf8
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0x670
+  __DATA.__bss: 0x6d0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x38

   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/NewsCore.framework/NewsCore
   - /System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation
   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 350
-  Symbols:   401
-  CStrings:  440
+  Functions: 397
+  Symbols:   438
+  CStrings:  486
 
Symbols:
+ _IOPMAssertionCreateWithDescription
+ _IOPMAssertionRelease
+ _NDScoringServiceXPCConnection
+ _NDScoringServiceXPCInterface
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_NDAssertion
+ _OBJC_CLASS_$_NDProxyScoringServiceConnection
+ _OBJC_CLASS_$_NTPBFeedItem
+ _OBJC_CLASS_$_NTPBFeedPersonalizingItem
+ _OBJC_CLASS_$_NTPBNotificationItem
+ _OBJC_METACLASS_$_NDAssertion
+ _OBJC_METACLASS_$_NDProxyScoringServiceConnection
+ __swiftEmptyArrayStorage
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_autorelease
+ _objc_exception_throw
+ _os_transaction_create
+ _swift_arrayDestroy
+ _swift_getTypeByMangledNameInContextInMetadataState2
CStrings:
+ "\x11"
+ "%!@(MISSING): %!s(MISSING)"
+ "-[NDAssertion init]"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Utilities/NDAssertion.m"
+ "@\"NSObject<OS_os_transaction>\""
+ "Do not call method"
+ "I"
+ "I16@0:8"
+ "NDAssertion"
+ "NDProxyScoringServiceConnection"
+ "NDScoringServiceType"
+ "PreventUserIdleSystemSleep"
+ "ProxyScoringServiceConnection XPC connection interrupted"
+ "ProxyScoringServiceConnection XPC connection invalidated"
+ "ProxyScoringServiceConnection failed to communicate with XPC service, error=%!{(MISSING)public}@"
+ "ProxyScoringServiceConnection failed to create synchronous proxy"
+ "ProxyScoringServiceConnection failed to establish XPC connection"
+ "ProxyScoringServiceConnection will establish XPC connection"
+ "ProxyScoringServiceConnection will invalidate XPC connection"
+ "T@\"NDProxyScoringServiceConnection\",N,R"
+ "T@\"NSObject<OS_os_transaction>\",R,N,V_transaction"
+ "TI,R,N,V_powerAssertionID"
+ "TimeoutActionTurnOff"
+ "UTF8String"
+ "_powerAssertionID"
+ "_transaction"
+ "com.apple.news.ScoringService"
+ "exceptionWithName:reason:userInfo:"
+ "failed to create a power assertion, name=%!{(MISSING)public}@"
+ "initWithName:"
+ "initWithName:options:"
+ "powerAssertionID"
+ "scoreFeedItems:configurationSet:completion:"
+ "scoreItems:configurationSet:completion:"
+ "scoreNotificationItems:completion:"
+ "sharedInstance"
+ "transaction"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v40@0:8@\"NSArray\"16q24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@16q24@?32"
+ "withScoringService:"

```
