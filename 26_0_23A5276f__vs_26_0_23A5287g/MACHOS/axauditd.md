## axauditd

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd`

```diff

-182.0.0.0.0
-  __TEXT.__text: 0xb7c8
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_stubs: 0x2800
-  __TEXT.__objc_methlist: 0xc4c
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0x658
-  __TEXT.__objc_classname: 0xdc
-  __TEXT.__objc_methname: 0x302a
-  __TEXT.__objc_methtype: 0x996
-  __TEXT.__oslogstring: 0x1c1
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x520
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x560
-  __DATA_CONST.__cfstring: 0x940
+183.0.0.0.0
+  __TEXT.__text: 0xc194
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__objc_methlist: 0xc54
+  __TEXT.__const: 0x4c
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__cstring: 0x7ef
+  __TEXT.__objc_classname: 0xdb
+  __TEXT.__objc_methname: 0x31ce
+  __TEXT.__oslogstring: 0x2b8
+  __TEXT.__objc_methtype: 0x9a1
+  __TEXT.__unwind_info: 0x398
+  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0xd0
-  __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0xbe0
-  __DATA.__objc_selrefs: 0xcd8
-  __DATA.__objc_ivar: 0x84
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA.__objc_const: 0xc18
+  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x1f8
   __DATA.__bss: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FCD82D5-B514-34AD-8BE6-8FBEFDD494C9
-  Functions: 291
-  Symbols:   285
-  CStrings:  765
+  UUID: 7BFE2E11-9A65-33AD-8E25-43BE0FF20BDA
+  Functions: 293
+  Symbols:   282
+  CStrings:  798
 
Symbols:
+ _dispatch_get_global_queue
- __os_log_debug_impl
- _mach_task_self_
- _objc_retain_x27
- _task_for_pid
CStrings:
+ "#"
+ "%s"
+ "%s: Device was not actively targeted, forcing update of frontmost apps"
+ "%s: could not %@ for notification:%@. Error:%@"
+ "%s: could not update running apps, connection is valid: %@, hostAPIVersion: %ld"
+ "%s: running app change detected"
+ "%s: took too long for AX IPC calls"
+ "-[XADAuditServer _checkFrontmostAppPidChanged]"
+ "-[XADAuditServer connectionInterrupted]"
+ "-[XADAuditServer deviceDidGetTargeted]"
+ "-[XADAuditServer deviceRunningApplications]"
+ "-[XADAuditServer resume]"
+ "-[XADEventManager _handleAccessibilityNotification:forElement:]"
+ "-[XADEventManager _registerForAXNotifications:]"
+ "-[XADInspectorManager deviceDidGetTargeted]"
+ "@\"NSArray\""
+ "T@\"<XADEventManagerDelegate>\",W,N,V_delegateForInspectorManager"
+ "T@\"NSArray\",&,N,V_runningAXAuditApplications"
+ "TB,N,V__deviceActivelyTargeted"
+ "__deviceActivelyTargeted"
+ "_delegateForInspectorManager"
+ "_deviceActivelyTargeted"
+ "_runningAXAuditAppForPid:"
+ "_runningAXAuditApplications"
+ "delegateForInspectorManager"
+ "displayName"
+ "enumerateObjectsUsingBlock:"
+ "register"
+ "runningAXAuditApplications"
+ "setDelegateForInspectorManager:"
+ "setRunningAXAuditApplications:"
+ "set_deviceActivelyTargeted:"
+ "unregister"
+ "v32@?0@\"AXAuditApplication\"8Q16^B24"
- "\""
- "2"
- "Device got targeted!"
- "_registerForNotificationsIfNecessary:"

```
