## GAXBackboardServer

> `/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1061.0.0.0.0
-  __TEXT.__text: 0x2acd8
+1064.0.0.0.0
+  __TEXT.__text: 0x2b560
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x6880
-  __TEXT.__objc_methlist: 0x2834
-  __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0x7e8
-  __TEXT.__objc_methname: 0x8b7f
-  __TEXT.__cstring: 0x460b
-  __TEXT.__oslogstring: 0x3ef4
+  __TEXT.__objc_stubs: 0x6940
+  __TEXT.__objc_methlist: 0x2894
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x84c
+  __TEXT.__objc_methname: 0x8d43
+  __TEXT.__cstring: 0x46b9
+  __TEXT.__oslogstring: 0x41e2
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methtype: 0x1868
-  __TEXT.__unwind_info: 0xa60
-  __DATA_CONST.__const: 0x16a0
-  __DATA_CONST.__cfstring: 0x3600
+  __TEXT.__objc_methtype: 0x186b
+  __TEXT.__unwind_info: 0xaa0
+  __DATA_CONST.__const: 0x16a8
+  __DATA_CONST.__cfstring: 0x36a0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x29c0
-  __DATA.__objc_selrefs: 0x1e98
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_const: 0x2a10
+  __DATA.__objc_selrefs: 0x1ec8
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x588
   __DATA.__bss: 0xa8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 955
-  Symbols:   580
-  CStrings:  2231
+  Functions: 965
+  Symbols:   581
+  CStrings:  2256
 
Symbols:
+ _GAXUIMessageKeyShouldDriveSiriAssessmentRestriction
CStrings:
+ "App-relaunch block-all-events exceeded 5 minutes without a terminal verification outcome; releasing to avoid stranding input"
+ "GAXBackboard creating userInterfaceClient with identifier %@ (this client is not invalidated until GAXBackboard is deallocated, which does not happen for this singleton)"
+ "GAXBackboard init starting"
+ "GAXBackboard sharedInstance first created. Caller: %@"
+ "NEW"
+ "OLD"
+ "Releasing app-relaunch block-all-events reason (%{public}@)"
+ "Session app is effective and active but device is restricted; lifting restriction"
+ "SessionDrivesSiriAssessmentRestriction"
+ "Siri assessment restriction ownership: entitlement=%{public}s (legacy=%d new=%d) -> GAX %{public}s drive Siri"
+ "T@\"AXDispatchTimer\",&,N,V_appRelaunchBlockAllEventsWatchdogTimer"
+ "Transitioned to GAXServerModeDisabled. userInterfaceClient %@ is not invalidated here (rdar://182430437) so its AXUIServer service registration remains active."
+ "WILL"
+ "_appRelaunchBlockAllEventsWatchdogTimer"
+ "_releaseVerifyAppRelaunchBlockAllEventsIfSetWithContext:"
+ "appRelaunchBlockAllEventsWatchdogTimer"
+ "applyUnmanagedSelfLockRestrictionsForStyle:shouldDriveSiriAssessmentRestriction:withUserInterfaceClient:"
+ "none"
+ "processWithAuditTokenOwnsSiriAssessmentRestriction:"
+ "removeUnmanagedSelfLockRestrictionsWithUserInterfaceClient:shouldDriveSiriAssessmentRestriction:"
+ "sessionDrivesSiriAssessmentRestriction"
+ "setAppRelaunchBlockAllEventsWatchdogTimer:"
+ "setSessionDrivesSiriAssessmentRestriction:"
+ "should drive siri assessment restriction"
+ "terminal verification event"
+ "v36@0:8q16B24@28"
+ "verification finished"
+ "watchdog timeout"
+ "will NOT"
- "Action button press blocked. Mode: %i"
- "applyUnmanagedSelfLockRestrictionsForStyle:withUserInterfaceClient:"
- "removeUnmanagedSelfLockRestrictionsWithUserInterfaceClient:"
- "v32@0:8q16@24"
```
