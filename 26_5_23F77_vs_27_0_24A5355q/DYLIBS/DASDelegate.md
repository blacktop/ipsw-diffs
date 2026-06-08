## DASDelegate

> `/System/Library/PrivateFrameworks/DASDelegate.framework/DASDelegate`

```diff

-2109.120.16.0.0
-  __TEXT.__text: 0xc24
-  __TEXT.__auth_stubs: 0x180
+2463.0.0.502.1
+  __TEXT.__text: 0xbb4
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0xdc
+  __TEXT.__cstring: 0xde
   __TEXT.__oslogstring: 0x125
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x29
-  __TEXT.__objc_methname: 0x20e
-  __TEXT.__objc_methtype: 0xde
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x128
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F873B653-97CD-360F-A768-CF3FD369673D
+  UUID: 344E7D38-CF31-3662-B81E-6AA5C5F771EF
   Functions: 22
-  Symbols:   121
-  CStrings:  49
+  Symbols:   126
+  CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
- _objc_release
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[DASDelegate connect] : 204 -> 196
~ -[DASDelegate disconnect] : 132 -> 128
~ -[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:] : 388 -> 396
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke : 128 -> 124
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.13 : 268 -> 264
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.15 : 160 -> 156
~ -[DASDelegate evaluateTailspinAt:withReply:] : 292 -> 296
~ ___44-[DASDelegate evaluateTailspinAt:withReply:]_block_invoke : 132 -> 128
~ ___44-[DASDelegate evaluateTailspinAt:withReply:]_block_invoke.20 : 516 -> 524
~ -[DASDelegate setLog:] : 64 -> 12
~ -[DASDelegate setConnectionToService:] : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@\"NSObject<OS_os_log>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "DASDelegateServiceProtocol"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "T@\"NSXPCConnection\",&,N,V_connectionToService"
- "_connectionToService"
- "_log"
- "appLaunchResumeInfoWithStartDate:withEndDate:withReply:"
- "connect"
- "connectionToService"
- "countByEnumeratingWithState:objects:count:"
- "disconnect"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "evaluateTailspinAt:withReply:"
- "init"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "log"
- "resume"
- "setConnectionToService:"
- "setLog:"
- "setRemoteObjectInterface:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSArray\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@16@24@?32"

```
