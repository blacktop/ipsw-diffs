## replayd

> `/usr/libexec/replayd`

```diff

-590.4.0.0.0
-  __TEXT.__text: 0x53214
-  __TEXT.__auth_stubs: 0xec0
+590.6.0.0.0
+  __TEXT.__text: 0x5369c
+  __TEXT.__auth_stubs: 0xef0
   __TEXT.__objc_stubs: 0x7660
-  __TEXT.__objc_methlist: 0x35e0
+  __TEXT.__objc_methlist: 0x35f8
   __TEXT.__const: 0x194
-  __TEXT.__objc_methname: 0xb0fd
-  __TEXT.__cstring: 0xaf11
-  __TEXT.__oslogstring: 0x7ec7
+  __TEXT.__objc_methname: 0xb141
+  __TEXT.__cstring: 0xaf7d
+  __TEXT.__oslogstring: 0x7f41
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methtype: 0x1caa
+  __TEXT.__objc_methtype: 0x1cbe
   __TEXT.__gcc_except_tab: 0x6e8
-  __TEXT.__unwind_info: 0x1018
-  __DATA_CONST.__auth_got: 0x770
+  __TEXT.__unwind_info: 0x1020
+  __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__const: 0x1618
-  __DATA_CONST.__cfstring: 0x3300
+  __DATA_CONST.__cfstring: 0x3360
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x9a18
-  __DATA.__objc_selrefs: 0x24b8
+  __DATA.__objc_selrefs: 0x24c0
   __DATA.__objc_ivar: 0x4ec
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0xa38

   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1728
-  Symbols:   433
-  CStrings:  3568
+  Functions: 1730
+  Symbols:   436
+  CStrings:  3577
 
Symbols:
+ _SecTaskCreateWithAuditToken
+ _CFBooleanGetTypeID
+ _SecTaskCopyValueForEntitlement
CStrings:
+ " [DEBUG] %!{(MISSING)public}s:%!d(MISSING) reported eventType:%!d(MISSING) payloadDict=%!@(MISSING)"
+ " [INFO] %!{(MISSING)public}s:%!d(MISSING) parentPid=%!d(MISSING) for processId=%!d(MISSING)"
+ "v40@0:8@16B24B28Q32"
+ "reportAlertRTCEventWithClientBundelID:isLegacy:didAlert:methodType:"
+ " [INFO] %!{(MISSING)public}s:%!d(MISSING) processId=%!d(MISSING) has relatedPids=%!@(MISSING)"
+ " [INFO] %!{(MISSING)public}s:%!d(MISSING) process list obtained process=%!p(MISSING)"
+ "+[SCProcessUtility listAllRunningProcesses:]"
+ "+[SCProcessUtility parentProcessIdForProcessId:]"
+ "MTY"
+ "LGC"
+ "SCREENCAPTUREKIT_USER_ALERT_CONTINUE_TO_ALLOW"
+ "ALT"
- " [DEBUG] %!{(MISSING)public}s:%!d(MISSING) processId=%!d(MISSING) has relatedPids=%!@(MISSING)"
- "SCREENCAPTUREKIT_USER_ALERT_ALLOW_FOR_MONTH"
- " [INFO] %!{(MISSING)public}s:%!d(MISSING) reported eventType:%!d(MISSING)"

```
