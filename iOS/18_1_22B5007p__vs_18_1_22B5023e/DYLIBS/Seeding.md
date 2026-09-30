## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-102.0.0.0.0
-  __TEXT.__text: 0x1e2c0
+104.0.0.0.0
+  __TEXT.__text: 0x1f7bc
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x1594
+  __TEXT.__objc_methlist: 0x15ac
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x658
-  __TEXT.__cstring: 0x1d1f
-  __TEXT.__oslogstring: 0x2cea
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__gcc_except_tab: 0x6a0
+  __TEXT.__cstring: 0x1e20
+  __TEXT.__oslogstring: 0x2e28
+  __TEXT.__unwind_info: 0x8a8
   __TEXT.__objc_classname: 0x256
-  __TEXT.__objc_methname: 0x3e83
-  __TEXT.__objc_methtype: 0x764
-  __TEXT.__objc_stubs: 0x3ac0
+  __TEXT.__objc_methname: 0x3eba
+  __TEXT.__objc_methtype: 0x7f9
+  __TEXT.__objc_stubs: 0x3b20
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xb08
+  __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a8
+  __DATA_CONST.__objc_selrefs: 0x10c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0x3968
+  __AUTH_CONST.__cfstring: 0x19a0
+  __AUTH_CONST.__objc_const: 0x3bd0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
   __DATA.__objc_ivar: 0xc4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 691
-  Symbols:   971
-  CStrings:  1359
+  Functions: 724
+  Symbols:   1005
+  CStrings:  1375
 
CStrings:
+ "-[SDBetaManager enrollDevice:withEnrollmentMetadata:completion:]"
+ "-[SDBetaManager enrolledBetaProgramForDevice:completion:]"
+ "Error device passed into %!{(MISSING)public}s"
+ "Error device passed into -[SDBetaManager enrollCurrentDeviceWithEnrollmentMetadata:]"
+ "Found a betaenrollmentdProxy that does not conform to SDDaemonXPCServer: %!{(MISSING)public}@."
+ "Found a remoteObjectProxy that does not conform to SDDaemonXPCServer: %!{(MISSING)public}@."
+ "Group container URL was null."
+ "_SDErrorForDaemonClientErrorType"
+ "__BLANK_ERROR_DEVICE__"
+ "betaenrollmentdProxyObjectWithCompletion:"
+ "blankDeviceWithErrorMessage:"
+ "com.apple.seeding.daemon-client"
+ "isErrorDevice"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SDDevice\"@\"NSError\">16"
+ "v24@?0@\"<SDDaemonXPCServer>\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"SDDevice\"8@\"NSError\"16"
+ "v32@0:8@\"SDDevice\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?@\"SDBetaProgram\"@\"NSError\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSArray\"@\"NSError\">24"
- "daemonRemoteObjectProxy"
- "daemonRemoteObjectProxyWithCompletion:"
- "v16@?0@\"SDBetaProgram\"8"
- "v24@0:8@?<v@?@\"SDDevice\">16"
- "v32@0:8@\"SDDevice\"16@?<v@?@\"SDBetaProgram\">24"
- "v32@0:8Q16@?<v@?@\"NSArray\">24"

```
