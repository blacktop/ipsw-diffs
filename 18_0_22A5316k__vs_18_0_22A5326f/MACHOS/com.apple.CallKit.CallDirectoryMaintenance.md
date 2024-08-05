## com.apple.CallKit.CallDirectoryMaintenance

> `/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance`

```diff

-1268.100.11.0.0
-  __TEXT.__text: 0x1ce6c
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0x2380
-  __TEXT.__objc_methlist: 0x10c4
-  __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0xba7
-  __TEXT.__objc_methname: 0x372d
+1270.100.1.0.0
+  __TEXT.__text: 0x20f78
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x2540
+  __TEXT.__objc_methlist: 0x117c
+  __TEXT.__const: 0x2e8
+  __TEXT.__cstring: 0xf61
+  __TEXT.__objc_methname: 0x39b8
   __TEXT.__objc_classname: 0x3b9
-  __TEXT.__objc_methtype: 0xcaf
-  __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__oslogstring: 0x23a0
-  __TEXT.__constg_swiftt: 0x110
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_typeref: 0x1c6
-  __TEXT.__swift5_reflstr: 0xa2
-  __TEXT.__swift5_fieldmd: 0xb0
-  __TEXT.__swift5_capture: 0x7c
+  __TEXT.__objc_methtype: 0xd46
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__oslogstring: 0x24e0
+  __TEXT.__constg_swiftt: 0x13c
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_typeref: 0x232
+  __TEXT.__swift5_reflstr: 0x262
+  __TEXT.__swift5_fieldmd: 0x1b0
+  __TEXT.__swift5_capture: 0xdc
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x678
-  __TEXT.__eh_frame: 0x500
-  __DATA_CONST.__auth_got: 0x788
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x938
+  __TEXT.__unwind_info: 0x748
+  __TEXT.__eh_frame: 0x588
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__const: 0xaf8
   __DATA_CONST.__cfstring: 0x340
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2bb8
-  __DATA.__objc_selrefs: 0xbc0
-  __DATA.__objc_ivar: 0x12c
-  __DATA.__objc_data: 0x6e0
-  __DATA.__data: 0x738
+  __DATA.__objc_const: 0x2ee8
+  __DATA.__objc_selrefs: 0xc60
+  __DATA.__objc_ivar: 0x134
+  __DATA.__objc_data: 0x830
+  __DATA.__data: 0x828
   __DATA.__bss: 0x110
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/Frameworks/IdentityLookup.framework/IdentityLookup
   - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 669
-  Symbols:   230
-  CStrings:  940
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 749
+  Symbols:   242
+  CStrings:  1009
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$__TtC42com_apple_CallKit_CallDirectoryMaintenance21CoreAnalyticsReporter
+ _OBJC_METACLASS_$__TtC42com_apple_CallKit_CallDirectoryMaintenance21CoreAnalyticsReporter
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x03\x13"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"_TtC42com_apple_CallKit_CallDirectoryMaintenance21CoreAnalyticsReporter\""
+ "@52@0:8@16@24@32q40B48"
+ "Negative value is not representable"
+ "Swift/Integers.swift"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_liveLookupGroup"
+ "T@\"_TtC42com_apple_CallKit_CallDirectoryMaintenance21CoreAnalyticsReporter\",&,N,V_analyticsReporter"
+ "Warmed up BlastDoor interface"
+ "Warming up BlastDoor interface"
+ "_TtC42com_apple_CallKit_CallDirectoryMaintenance21CoreAnalyticsReporter"
+ "_analyticsReporter"
+ "_liveLookupGroup"
+ "analyticsEventPrefix"
+ "analyticsReporter"
+ "analyticsReporter"
+ "blastDoorErrorKey"
+ "blastDoorTimeKey"
+ "blockingCacheHitKey"
+ "blockingFetchErrorKey"
+ "blockingFetchTimeKey"
+ "blocking_cache_hit"
+ "blocking_fetch_error"
+ "blocking_fetch_time"
+ "callDirectoryHost:requestedFirstIdentificationEntriesForEnabledExtensionsWithPhoneNumbers:cacheOnly:completionHandler:"
+ "code"
+ "com.apple.calls.livecalleridlookup."
+ "disableErrorKey"
+ "disableTimeKey"
+ "enableErrorKey"
+ "enableTimeKey"
+ "extensionIdentifierFrom:"
+ "extensionIdentifierKey"
+ "fetchKey"
+ "fetchLiveIdentityInfoFor handle=%!@(MISSING) cacheOnly=%!d(MISSING)"
+ "fetchLiveIdentityInfoFor:cacheOnly:completionHandler:"
+ "fromCache"
+ "identificationEntryFrom:withName:withIconURL:withType:fromCache:"
+ "identifyFetchErrorKey"
+ "identifyFetchTimeKey"
+ "identityCacheHitKey"
+ "identity_cache_hit"
+ "identity_fetch_error"
+ "identity_fetch_time"
+ "initWithBool:"
+ "initWithDouble:"
+ "initWithString:"
+ "initWithUnsignedInteger:"
+ "installKey"
+ "installed extension does not have identifier: %!@(MISSING)"
+ "liveLookupGroup"
+ "not all previous fetches completed within %!l(MISSING)u second(s) continuing"
+ "register failed %!@(MISSING), ignoring"
+ "registrationKey"
+ "removed extension does not have identifier: %!@(MISSING)"
+ "sendBlastDoorWithError:for:"
+ "sendBlastDoorWithTimeInterval:for:"
+ "sendBlockingCacheHitFor:"
+ "sendBlockingWithError:for:"
+ "sendBlockingWithTimeInterval:for:"
+ "sendIdentityCacheHitFor:"
+ "sendIdentityWithError:for:"
+ "sendIdentityWithTimeInterval:for:"
+ "sending action: %!s(MISSING) payload: %!s(MISSING)"
+ "setAnalyticsReporter:"
+ "setFromCache:"
+ "setLiveLookupGroup:"
+ "timeIntervalSinceNow"
+ "uninstallKey"
+ "v32@0:8Q16@24"
+ "v32@0:8d16@24"
+ "v36@0:8@16B24@?28"
+ "v44@0:8@\"CXCallDirectoryHost\"16@\"NSArray\"24B32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@16@24B32@?36"
+ "warmUpGIFBytes"
- "\x03\x11"
- "@48@0:8@16@24@32q40"
- "callDirectoryHost:requestedFirstIdentificationEntriesForEnabledExtensionsWithPhoneNumbers:completionHandler:"
- "fetchLiveIdentityInfoFor handle=%!@(MISSING)"
- "fetchLiveIdentityInfoFor:completionHandler:"
- "identificationEntryFrom:withName:withIconURL:withType:"
- "objectAtIndexedSubscript:"
- "v40@0:8@\"CXCallDirectoryHost\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"

```
