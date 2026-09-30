## rapportd

> `/usr/libexec/rapportd`

```diff

-610.71.1.0.0
-  __TEXT.__text: 0xb7488
+630.21.1.0.0
+  __TEXT.__text: 0xb83f8
   __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_stubs: 0xee20
-  __TEXT.__objc_methlist: 0x654c
-  __TEXT.__cstring: 0x28642
-  __TEXT.__objc_classname: 0x94d
-  __TEXT.__objc_methtype: 0x3819
-  __TEXT.__objc_methname: 0x150bf
+  __TEXT.__objc_stubs: 0xef40
+  __TEXT.__objc_methlist: 0x6594
+  __TEXT.__cstring: 0x28b82
+  __TEXT.__objc_classname: 0x94e
+  __TEXT.__objc_methtype: 0x3831
+  __TEXT.__objc_methname: 0x1521a
   __TEXT.__const: 0x207a
-  __TEXT.__gcc_except_tab: 0x1ca4
+  __TEXT.__gcc_except_tab: 0x1cd4
   __TEXT.__oslogstring: 0x496
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x41

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x1ef0
+  __TEXT.__unwind_info: 0x1f20
   __DATA_CONST.__auth_got: 0xc50
-  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x3ea0
-  __DATA_CONST.__cfstring: 0x5600
+  __DATA_CONST.__const: 0x3f50
+  __DATA_CONST.__cfstring: 0x5660
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xda10
-  __DATA.__objc_selrefs: 0x4538
-  __DATA.__objc_ivar: 0xd24
+  __DATA.__objc_const: 0xda80
+  __DATA.__objc_selrefs: 0x4580
+  __DATA.__objc_ivar: 0xd30
   __DATA.__objc_data: 0x1370
-  __DATA.__data: 0x1fd8
-  __DATA.__bss: 0x520
+  __DATA.__data: 0x1ff0
+  __DATA.__bss: 0x540
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3021
-  Symbols:   559
-  CStrings:  8191
+  Functions: 3037
+  Symbols:   560
+  CStrings:  8236
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
CStrings:
+ "\x11\x15\x12X#\x11\x13$\x13\"\x11\x12\x12\x12\x14\x11\x11\x14\x16\x14\x12=\x14\x11\x111\x11\x11\x1a"
+ "\x17\x12"
+ "### Failed to launch application with bundle '%!@(MISSING)': %!@(MISSING)\n"
+ "### Session start send failed: Service %!@(MISSING), destinationID %!@(MISSING), CSID 0x%!l(MISSING)lX, %!{(MISSING)error}\n"
+ "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
+ "-[RPCompanionLinkDaemon _handleContextCollectorProxyRequest:options:responseHandler:]"
+ "-[RPCompanionLinkDaemon _miscHandleLaunchAppRequest:responseHandler:]_block_invoke_3"
+ "-[RPCompanionLinkDaemon sessionStartSend:session:xpcID:destinationID:completion:]"
+ "-[RPCompanionLinkDaemon sessionStartSend:session:xpcID:destinationID:completion:]_block_invoke"
+ "-[RPNWListener hasTriggeredConnection]"
+ "/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices"
+ "/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience"
+ "630.21.1"
+ "AddUser"
+ "Already have outstanding triggered connection, not triggering this connection"
+ "Checking for existing triggered connection\n"
+ "FBSOpenApplicationOptionKeyActivateSuspended"
+ "FBSOpenApplicationOptions"
+ "FBSOpenApplicationService"
+ "FLOW: Found received incoming connection, triggering connection\n"
+ "HasService"
+ "LaunchOnDemand service type %!@(MISSING) payload %!@(MISSING)\n"
+ "MeDeviceIsMe override: %!s(MISSING) -> %!s(MISSING)\n"
+ "Missing proxy requestID"
+ "No outstanding triggered connection\n"
+ "No outstanding triggered connection, triggering this connection"
+ "Operating system version: %!@(MISSING)\n"
+ "PhotoSetup"
+ "ProxControlDeviceClose"
+ "Proxy request missing requestID"
+ "Sending proxy request %!@(MISSING) to context collector %!@(MISSING)"
+ "Session start received: Service %!@(MISSING), PeerID %!@(MISSING), SID 0x%!l(MISSING)lX, Token %!l(MISSING)ld persona %!@(MISSING)\n"
+ "Session start request: Service %!@(MISSING), destinationID %!@(MISSING), CSID 0x%!l(MISSING)lX connection %!@(MISSING)\n"
+ "Successfully launched application with bundle ID '%!@(MISSING)'\n"
+ "T@\"NSDate\",&,N,V_triggerTime"
+ "Triggered connection is stale, %!f(MISSING)s\n"
+ "Triggered connection outstanding, %!f(MISSING)s\n"
+ "_contextCollectorDevice"
+ "_ctxtCollProxy"
+ "_didFetchForLaunchID"
+ "_handleContextCollectorProxyRequest:options:responseHandler:"
+ "_lbg"
+ "_prefMeDeviceIsMeOverride"
+ "_triggerTime"
+ "clMeDeviceIsMeOverride"
+ "ctxCollProxyReq"
+ "hasTriggeredConnection"
+ "openApplication:withOptions:completion:"
+ "operatingSystemVersionForSelf"
+ "optionsWithDictionary:"
+ "processInfo"
+ "serviceWithDefaultShellEndpoint"
+ "sessionStartSend:session:xpcID:destinationID:completion:"
+ "setTriggerTime:"
+ "triggerTime"
+ "v24@?0@\"BSProcessHandle\"8@\"NSError\"16"
+ "v52@0:8@16@24I32@36@?44"
+ "\x81"
- "\x11\x15\x12X#\x11\x13$\x13\"\x11\x12\x12\x12\x14\x11\x11\x14\x16\x14\x12=\x14\x11A\x11\x11\x1a"
- "\x16\x12"
- "-[RPCompanionLinkDaemon sessionStartSend:session:xpcID:completion:]"
- "-[RPCompanionLinkDaemon sessionStartSend:session:xpcID:completion:]_block_invoke"
- ".%!@(MISSING)"
- "/System/Library/PrivateFrameworks/Celestial.framework/Celestial"
- "610.71.1"
- "PrecisionFindingFindeeHighPriority"
- "Session start received: Service %!@(MISSING), PeerID %!@(MISSING), SID 0x%!l(MISSING)lX, Token %!l(MISSING)ld\n"
- "Session start request: Service %!@(MISSING), PeerID %!@(MISSING), CSID 0x%!l(MISSING)lX\n"
- "openApplicationWithBundleID:"
- "sessionStartSend:session:xpcID:completion:"

```
