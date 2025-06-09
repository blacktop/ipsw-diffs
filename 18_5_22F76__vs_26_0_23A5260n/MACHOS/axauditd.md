## axauditd

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd`

```diff

-165.2.0.0.0
-  __TEXT.__text: 0xb588
-  __TEXT.__auth_stubs: 0xa10
+179.0.0.0.0
+  __TEXT.__text: 0xb7c8
+  __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_stubs: 0x2800
   __TEXT.__objc_methlist: 0xc4c
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0x644
+  __TEXT.__cstring: 0x658
   __TEXT.__objc_classname: 0xdc
-  __TEXT.__objc_methname: 0x3031
+  __TEXT.__objc_methname: 0x302a
   __TEXT.__objc_methtype: 0x996
-  __TEXT.__oslogstring: 0x11c
+  __TEXT.__oslogstring: 0x1c1
   __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x518
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x500
-  __DATA_CONST.__cfstring: 0xa00
+  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices
   - /System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C12C392C-2B87-3555-A942-22EB2EFD9E16
-  Functions: 289
-  Symbols:   283
-  CStrings:  771
+  UUID: EA93F820-640B-3606-BEA0-E00CEE9E0FF0
+  Functions: 291
+  Symbols:   285
+  CStrings:  765
 
Symbols:
+ _OBJC_CLASS_$_AXAuditDevicesAppRemoteServer
+ _close
+ _remote_service_listen
- _iOSFrontmostApp
CStrings:
+ "%s: allowDeveloperAttributes: %@"
+ "-[XADInspectorManager _auditInspectorFocuseObject]"
+ "NO"
+ "RSD handler: Received checkin."
+ "RSD handler: Socket transport disconnect action fired. Closing socket."
+ "Starting RSD checkin handler."
+ "YES"
+ "com.apple.accessibility.axAuditDaemon.remoteAXService"
+ "initWithType:"
- "Actions"
- "Basic"
- "Element"
- "Hierarchy"
- "iOS_Actions_v1"
- "iOS_Basic_v1"
- "iOS_Element_v1"
- "iOS_Hierarchy_v1"
- "setIdentifier:"
- "setTitle:"

```
