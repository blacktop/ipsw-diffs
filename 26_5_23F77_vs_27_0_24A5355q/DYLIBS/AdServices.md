## AdServices

> `/System/Library/Frameworks/AdServices.framework/AdServices`

```diff

-556.5.31.0.0
-  __TEXT.__text: 0x1d58
-  __TEXT.__auth_stubs: 0x360
+557.1.16.0.0
+  __TEXT.__text: 0x1b28
   __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0xc8
   __TEXT.__oslogstring: 0x2cc
-  __TEXT.__cstring: 0x190
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x71
-  __TEXT.__objc_methname: 0x887
-  __TEXT.__objc_methtype: 0x2c0
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__cstring: 0x195
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x5e8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E754BFB-6391-3927-AADE-AC0FBC0D8D28
+  UUID: 3BFD5F9C-47F2-35FE-892E-04FE275CCBC4
   Functions: 50
   Symbols:   79
-  CStrings:  227
+  CStrings:  52
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x26
- _objc_release_x27
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x23
- _objc_retain_x27
Functions:
~ sub_23ca96e00 -> sub_23f2bde00 : 548 -> 484
~ sub_23ca97024 -> sub_23f2bdfe4 : 84 -> 68
~ sub_23ca97078 -> sub_23f2be028 : 140 -> 136
~ sub_23ca97148 -> sub_23f2be0f4 : 2880 -> 2720
~ sub_23ca97ca0 -> sub_23f2bebac : 148 -> 144
~ sub_23ca97d34 -> sub_23f2bec3c : 156 -> 148
~ sub_23ca97dd0 -> sub_23f2becd0 : 56 -> 60
~ sub_23ca97e08 -> sub_23f2bed0c : 424 -> 380
~ sub_23ca97fb0 -> sub_23f2bee88 : 524 -> 496
~ sub_23ca981d0 -> sub_23f2bf08c : 224 -> 216
~ sub_23ca982b0 -> sub_23f2bf164 : 164 -> 160
~ sub_23ca9836c -> sub_23f2bf21c : 64 -> 12
~ sub_23ca983d4 -> sub_23f2bf250 : 64 -> 12
~ sub_23ca984c4 -> sub_23f2bf30c : 196 -> 212
~ sub_23ca98590 -> sub_23f2bf3e8 : 284 -> 268
~ sub_23ca986ac -> sub_23f2bf4f4 : 312 -> 300
~ sub_23ca98824 -> sub_23f2bf660 : 64 -> 12
~ sub_23ca988d4 -> sub_23f2bf6dc : 476 -> 420
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AAAttribution_XPC>\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSError\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24q32"
- "@52@0:8@16@24B32@36q44"
- "AAAttribution"
- "AAAttributionRequester"
- "AAAttributionResult"
- "AAAttribution_XPC"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<AAAttribution_XPC>\",&,N,V_remoteProxy"
- "T@\"NSData\",R,N,V_tokenKey"
- "T@\"NSDate\",&,N,V_requestTime"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSString\",&,N,V_storeFront"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_token"
- "TB,N,V_connectionInterrupted"
- "TB,N,V_isMainThread"
- "TB,R"
- "TB,R,N,V_success"
- "TQ,R"
- "TQ,R,N,V_intervalId"
- "Td,N,V_daemonRunningTime"
- "Tq,R,N,V_source"
- "T{os_unfair_lock_s=I},N,V_unfairLock"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_connectionInterrupted"
- "_createInternalError"
- "_daemonRunningTime"
- "_error"
- "_findBucketForDaemonRunningTime:"
- "_intervalId"
- "_isMainThread"
- "_remoteProxy"
- "_reportTokenStatus:storeFront:daemonRunningTime:"
- "_requestTime"
- "_sendAnalyticsAndInvalidateConnection:end:"
- "_source"
- "_storeFront"
- "_success"
- "_token"
- "_tokenKey"
- "_tokenStatusFromTokenSource:"
- "_unfairLock"
- "attributionAnalytics:end:Handler:"
- "attributionTokenRequestTimestamp:interval:completionHandler:"
- "attributionTokenWithError:"
- "autorelease"
- "cStringUsingEncoding:"
- "class"
- "code"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connectionInterrupted"
- "copy"
- "count"
- "d"
- "d16@0:8"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "firstObject"
- "hash"
- "init"
- "initWithCoder:"
- "initWithError:"
- "initWithMachServiceName:options:"
- "initWithToken:tokenKey:source:"
- "initWithToken:tokenKey:success:error:source:"
- "interfaceWithProtocol:"
- "intervalId"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isProxy"
- "localizedDescription"
- "mutableCopy"
- "now"
- "numberWithBool:"
- "numberWithInteger:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "q24@0:8d16"
- "q24@0:8q16"
- "release"
- "remoteObjectProxy"
- "remoteProxy"
- "requestTime"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setConnectionInterrupted:"
- "setDaemonRunningTime:"
- "setInterruptionHandler:"
- "setIsMainThread:"
- "setObject:forKey:"
- "setRemoteObjectInterface:"
- "setRemoteProxy:"
- "setRequestTime:"
- "setStoreFront:"
- "setUnfairLock:"
- "setupXPCConnection"
- "superclass"
- "supportsSecureCoding"
- "timeIntervalSinceDate:"
- "tokenKey"
- "unfairLock"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v32@0:8Q16Q24"
- "v40@0:8@\"NSDate\"16Q24@?<v@?@\"AAAttributionResult\">32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16Q24@?32"
- "v40@0:8Q16Q24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@24d32"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
