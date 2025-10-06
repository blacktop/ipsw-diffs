## storagekitd

> `/usr/libexec/storagekitd`

```diff

-854.100.13.0.0
-  __TEXT.__text: 0x29fd0
+854.120.9.0.0
+  __TEXT.__text: 0x2a3a4
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_stubs: 0x5720
-  __TEXT.__objc_methlist: 0x2078
+  __TEXT.__objc_stubs: 0x5840
+  __TEXT.__objc_methlist: 0x20c0
   __TEXT.__objc_classname: 0x4c7
-  __TEXT.__objc_methname: 0x5806
-  __TEXT.__objc_methtype: 0xeca
+  __TEXT.__objc_methname: 0x5922
+  __TEXT.__objc_methtype: 0xe95
   __TEXT.__gcc_except_tab: 0x80c
-  __TEXT.__cstring: 0x2419
-  __TEXT.__oslogstring: 0x1e8c
+  __TEXT.__cstring: 0x253f
+  __TEXT.__oslogstring: 0x1ff3
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x9b8
+  __TEXT.__unwind_info: 0x9a8
   __DATA_CONST.__auth_got: 0x600
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0xfe8
-  __DATA_CONST.__cfstring: 0x1a80
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0xf68
+  __DATA_CONST.__cfstring: 0x1ac0
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5fa8
-  __DATA.__objc_selrefs: 0x18d0
-  __DATA.__objc_ivar: 0x25c
+  __DATA.__objc_const: 0x6008
+  __DATA.__objc_selrefs: 0x1920
+  __DATA.__objc_ivar: 0x264
   __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x6d8
   __DATA.__bss: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 436406A5-496D-305C-BBF0-3BAA023A1237
-  Functions: 822
-  Symbols:   363
-  CStrings:  2097
+  UUID: 28E02DBC-D6AF-3807-AB31-FD425A350A41
+  Functions: 824
+  Symbols:   364
+  CStrings:  2126
 
Symbols:
+ _kDADiskDescriptionMediaRemovableKey
CStrings:
+ "%s: %@ is already mounted, returning success"
+ "%s: Client %d asks to mount %@ with %@ option"
+ "%s: Client is allowed to mount to %@"
+ "%s: Client is not the owner of %@. clientUID = %d, path_info.st_uid = %d, asking for permission"
+ "%s: Multiple disks to mount, cannot specify mount point"
+ "%s: Not allowed for non-root users on this platform"
+ "%s: Nothing to mount on recursive mount, returning success"
+ "%s: Reached with invalid disk (%@) or init failed (%@)"
+ "%s: Stat failed on %@, errno %d"
+ "-[SKBaseDiskArbOperation initWithTarget:options:callbackBlock:]"
+ "-[SKDaemonConnection authorizeRequestForRoot]"
+ "-[SKMountOperation filterEFIWithDisks:]"
+ "-[SKMountOperation initWithDisk:options:connection:completionBlock:]"
+ "-[SKMountOperation validateMountOptionsWithDisk:]"
+ "-[SKMountOperation validateMountPointWithConnection:error:]"
+ "@32@0:8@?16@24"
+ "@60@0:8@16q24@32r*40B48@?52"
+ "B52@0:8@16q24@32r*40B48"
+ "SKBaseDiskArbOperation.m"
+ "TB,N,V_authenticateOnInit"
+ "TI,R,N,V_clientUID"
+ "Unknown audit token, denying use of mount point"
+ "_authenticateOnInit"
+ "_clientUID"
+ "anyObject"
+ "authenticateOnInit"
+ "authorizeRequestForRoot"
+ "caseInsensitiveCompare:"
+ "clientUID"
+ "dev"
+ "filterEFIWithDisks:"
+ "isTrusted"
+ "mountDisk:options:completionBlock:"
+ "nilWithBlock:error:"
+ "preflightRequestWithDisksArr:entitlementLevel:completionUUID:prettyFunc:requireRootForInternal:failResGenFunc:"
+ "preflightRequestWithSKDisk:entitlementLevel:completionUUID:prettyFunc:authorizationNeeded:"
+ "setAuthenticateOnInit:"
+ "setIsRemovable:"
+ "suid"
+ "validateMountOptionsWithDisk:"
- "-[SKMountOperation filterEFIWithDisks:connection:]"
- "B48@0:8@16q24@32r*40"
- "SKDaemonManager.m"
- "Tried to eject a disk with no DADiskRef!"
- "Tried to mount a disk with no DADiskRef!"
- "Tried to rename a disk with no DADiskRef!"
- "Tried to unmount a disk with no DADiskRef!"
- "filterEFIWithDisks:connection:"
- "mountDisk:options:connection:completionBlock:"
- "preflightRequestWithDisksArr:entitlementLevel:completionUUID:prettyFunc:failResGenFunc:"
- "preflightRequestWithSKDisk:entitlementLevel:completionUUID:prettyFunc:"
- "v48@0:8@\"SKDisk\"16@\"NSDictionary\"24@\"SKDaemonConnection\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
