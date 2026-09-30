## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-478.0.0.0.0
-  __TEXT.__text: 0x176f0
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x360
+480.0.0.0.0
+  __TEXT.__text: 0x18074
+  __TEXT.__auth_stubs: 0x15d0
+  __TEXT.__objc_stubs: 0x480
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2990
+  __TEXT.__cstring: 0x2ad1
   __TEXT.__const: 0x70
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methname: 0x354
+  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__objc_classname: 0x2b
+  __TEXT.__objc_methname: 0x400
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x550
-  __DATA_CONST.__auth_got: 0xae8
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x578
+  __DATA_CONST.__auth_got: 0xaf8
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xab0
-  __DATA_CONST.__cfstring: 0x1b00
+  __DATA_CONST.__const: 0xae8
+  __DATA_CONST.__cfstring: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1d0
-  __DATA.__objc_selrefs: 0x118
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 471
-  Symbols:   388
-  CStrings:  577
+  Functions: 475
+  Symbols:   395
+  CStrings:  598
 
Symbols:
+ _OBJC_CLASS_$_FSAuditToken
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ _objc_alloc_init
+ _objc_release_x2
+ _objc_release_x28
+ _objc_retain_x27
- _OBJC_CLASS_$_FSModuleHost
- _objc_retain
- _objc_retain_x25
CStrings:
+ "%!@(MISSING)_fskit"
+ "DAMountUserFSVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
+ "FSImplementation"
+ "FSModule missing information"
+ "FSShortName"
+ "FSSupportsBlockResources"
+ "Found FSModule: %!@(MISSING)"
+ "Unable to retrieve FSModules for uid %!u(MISSING): %!@(MISSING)"
+ "Unable to retrieve FSModules for uid %!u(MISSING): infrastructure issues"
+ "addObject:"
+ "attributes"
+ "audit_token"
+ "boolValue"
+ "checkResource:usingBundle:options:auditToken:connection:replyHandler:"
+ "installedExtensionsForUser:replyHandler:"
+ "kext"
+ "nofollow"
+ "numberWithBool:"
+ "objectForKeyedSubscript:"
+ "probeResource:usingBundle:auditToken:replyHandler:"
+ "setValue:forKey:"
+ "staged fsmodule, id = %!@(MISSING), with %!@(MISSING), success."
+ "stringWithFormat:"
+ "tokenWithRuid:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@?0@\"FSModuleIdentity\"8Q16^B24"
- " Reprobing disk %!@(MISSING)"
- "DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:"
- "checkResource:usingBundle:options:connection:replyHandler:"
- "installedExtensionPropertiesSync"
- "probeResourceSync:usingBundle:replyHandler:"

```
