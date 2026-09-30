## fskitd

> `/usr/libexec/fskitd`

```diff

-737.0.17.0.2
-  __TEXT.__text: 0x445a0
+737.0.29.0.2
+  __TEXT.__text: 0x44500
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_stubs: 0x49c0
   __TEXT.__objc_methlist: 0x1efc
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x234c
-  __TEXT.__oslogstring: 0x3a21
-  __TEXT.__cstring: 0x2dbc
+  __TEXT.__gcc_except_tab: 0x2380
+  __TEXT.__oslogstring: 0x3a84
+  __TEXT.__cstring: 0x2d50
   __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methname: 0x5860
+  __TEXT.__objc_methname: 0x585c
   __TEXT.__objc_methtype: 0x1e88
   __TEXT.__unwind_info: 0xf88
   __DATA_CONST.__auth_got: 0x598
-  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x20f8
-  __DATA_CONST.__cfstring: 0x860
+  __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 92C6C9EE-8292-3589-BD64-4B4AB92AC6F8
+  UUID: 525F7BEA-3CF6-3507-B2F5-A5A7507FD0BA
   Functions: 1283
-  Symbols:   297
-  CStrings:  1950
+  Symbols:   294
+  CStrings:  1952
 
Symbols:
+ _SecTaskCopyTeamIdentifier
- _CFArrayGetTypeID
- _FSModuleIdentityAttributeSupportsKOIO
- _FSModuleIdentityAttributeSupportsKOIO_OLD
- ___NSArray0__struct
CStrings:
+ "%s did not find initiator ID"
+ "%s did not find team ID"
+ "%s: pid %d pidversion %d enableBlockResource %d"
+ "-[fskitdXPCServer getTeamIDForToken:]"
+ "About to filter"
+ "Got extensions %@"
+ "Received error '%@', errno %d, retrieving team ID"
+ "Returniong set %@"
+ "configureUserClient:pid:pidversion:supportBlockResource:"
+ "getTeamIDForToken:"
+ "teamID"
- "%s: caller has application-group: %@"
- "%s: pid %d pidversion %d supportsBlockResources %d supportsKOIO %d"
- "-[fskitdXPCServer _installedExtensionsForAuditToken:replyHandler:]"
- "-[fskitdXPCServer getApplicationGroups:]"
- "applicationGroup"
- "com.apple.security.application-groups"
- "configureUserClient:pid:pidversion:supportKOIO:"
- "getApplicationGroups:"

```
