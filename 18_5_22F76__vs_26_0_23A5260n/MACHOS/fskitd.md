## fskitd

> `/usr/libexec/fskitd`

```diff

-531.120.18.0.2
-  __TEXT.__text: 0x404d8
+737.0.2.0.1
+  __TEXT.__text: 0x43648
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x4680
-  __TEXT.__objc_methlist: 0x1d14
+  __TEXT.__objc_stubs: 0x48e0
+  __TEXT.__objc_methlist: 0x1e74
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x1fec
-  __TEXT.__cstring: 0x25f5
-  __TEXT.__oslogstring: 0x33d0
-  __TEXT.__objc_classname: 0x21a
-  __TEXT.__objc_methname: 0x5390
-  __TEXT.__objc_methtype: 0x1fae
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__gcc_except_tab: 0x2344
+  __TEXT.__oslogstring: 0x3862
+  __TEXT.__cstring: 0x2c60
+  __TEXT.__objc_classname: 0x223
+  __TEXT.__objc_methname: 0x56d5
+  __TEXT.__objc_methtype: 0x1e6d
+  __TEXT.__unwind_info: 0xf60
   __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x1fc0
-  __DATA_CONST.__cfstring: 0x820
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0x20d0
+  __DATA_CONST.__cfstring: 0x860
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1fd8
-  __DATA.__objc_selrefs: 0x1548
+  __DATA.__objc_const: 0x2190
+  __DATA.__objc_selrefs: 0x1668
   __DATA.__objc_ivar: 0x170
-  __DATA.__objc_data: 0x550
-  __DATA.__data: 0x6c0
-  __DATA.__common: 0x74
-  __DATA.__bss: 0x31
+  __DATA.__objc_data: 0x5a0
+  __DATA.__data: 0x6b0
+  __DATA.__common: 0x88
+  __DATA.__bss: 0x51
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: D7A0953B-FBDE-33B5-91BC-5FFBD4D2482A
-  Functions: 1206
+  UUID: 88F24609-8235-39A1-8382-494DA74FE920
+  Functions: 1265
   Symbols:   293
-  CStrings:  1824
+  CStrings:  1926
 
Symbols:
+ _CFArrayGetTypeID
+ _OBJC_CLASS_$_FSPathURLResource
+ ___NSArray0__struct
+ _dispatch_sync
- _LiveFSMounterDomainContainsPhotos
- __dispatch_source_type_timer
- _dispatch_source_cancel
- _dispatch_source_set_timer
CStrings:
+ "%s: About to start check task UUID (%@) on resource (%@)"
+ "%s: About to start format task UUID (%@) on resource (%@)"
+ "%s: Can't mark task as done, the initator (%@:%@) isn't the same initator of the task (%@:%@)"
+ "%s: Check task UUID (%@) on resource (%@) is running"
+ "%s: Format task UUID (%@) on resource (%@) is running"
+ "%s: Invalid device name or volume names is nil"
+ "%s: No moduleIdentity found for fsShortName (%@)"
+ "%s: Removing mount entry transaction"
+ "%s: Setting transaction:%@"
+ "%s: Task UUID (%@), apply resource error (%@), activate volume error (%@)"
+ "%s: Task UUID (%@), apply resource error (%@), check resource error (%@)"
+ "%s: Task UUID (%@), apply resource error (%@), deactivate volume error (%@)"
+ "%s: Task UUID (%@), apply resource error (%@), format resource error (%@)"
+ "%s: Task UUID (%@), apply resource error (%@), load resource error (%@)"
+ "%s: Task UUID (%@), apply resource error (%@), probe resource error (%@)"
+ "%s: Task UUID (%@), apply resource error (%@), unload resource error (%@)"
+ "%s: caller has application-group: %@"
+ "%s: invalidate work transaction"
+ "%s: path is nil"
+ "%s: received a NULL error pointer"
+ "%s: setting up work transaction"
+ "%s: taskID (%@) not found in our tasks dictionary"
+ "%s:start:deviceName(%@):volumes(%@)"
+ "-[FPnfsMemFS mkMountPath:mountID:]"
+ "-[FPnfsMemNode readDirAtCookie:withVerifier:forBytes:andError:]"
+ "-[FSKitDaemon start]"
+ "-[LivefsSettings doneWork]"
+ "-[LivefsSettings startedWork]"
+ "-[fskitdXPCServer _activateVolume:usingIdentity:options:auditToken:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _activateVolume:usingIdentity:options:auditToken:replyHandler:]_block_invoke_4"
+ "-[fskitdXPCServer _checkResource:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _deactivateVolume:usingIdentity:numericOptions:auditToken:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _deactivateVolume:usingIdentity:numericOptions:auditToken:replyHandler:]_block_invoke_5"
+ "-[fskitdXPCServer _formatResource:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _installedExtensionsForAuditToken:replyHandler:]"
+ "-[fskitdXPCServer _loadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _loadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke_2"
+ "-[fskitdXPCServer _loadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke_5"
+ "-[fskitdXPCServer _probeResource:usingBundle:auditToken:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _unloadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer activateVolume:usingBundle:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer activateVolume:usingBundle:options:replyHandler:]"
+ "-[fskitdXPCServer applyResource:usingIdentity:instanceID:initiatorAuditToken:authorizingAuditToken:usingBlock:]"
+ "-[fskitdXPCServer deactivateVolume:usingBundle:numericOptions:auditToken:replyHandler:]"
+ "-[fskitdXPCServer deactivateVolume:usingBundle:numericOptions:replyHandler:]"
+ "-[fskitdXPCServer doneFSCKWithTask:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer getApplicationGroups:]"
+ "-[fskitdXPCServer getModuleIdentityFromShortName:]_block_invoke"
+ "-[fskitdXPCServer loadResource:usingBundle:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer loadResource:usingBundle:options:replyHandler:]"
+ "-[fskitdXPCServer startFSCKWithDevice:volumes:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer unloadResource:usingBundle:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer unloadResource:usingBundle:options:replyHandler:]"
+ "-[mountEntry dealloc]"
+ "-[mountEntry setCurrentState:]"
+ "/private/var/mobile/Library/%s"
+ "@64@0:8@16@24@32@40@48@?56"
+ "Attempt to start non-Apple extension %@ on behalf of root"
+ "Connection cannot be nil"
+ "Entry can't be nil"
+ "FPNfsPortStr"
+ "FSKitDaemon"
+ "Revoking resource (%@)"
+ "T@\"FPnfsMemFS\",&,N"
+ "T@\"FSAuditToken\",&,N"
+ "T@\"FSModuleHost\",&,N"
+ "T@\"FSResource\",&,V_resource"
+ "T@\"FSVolumeIdentifier\",&,V_volumeID"
+ "T@\"LivefsSettings\",R,N"
+ "T@\"NSCondition\",&,V_theLock"
+ "T@\"NSError\",&,V_lastConnectError"
+ "T@\"NSObject<LiveFSVolumeCore_FSFileName>\",&,V_fsObj"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N"
+ "T@\"NSString\",&,N"
+ "T@\"NSUUID\",&,V_mountTaskUUID"
+ "T@\"NSXPCConnection\",&,V_theConn"
+ "T@\"fskitdExtensionInstance\",&,V_instance"
+ "T@\"mountEntry\",&,N"
+ "T@\"mountTable\",R,N"
+ "TB,N"
+ "TB,R,N"
+ "Ti,N"
+ "Working on a task"
+ "_N_mntflags"
+ "_O_f_preallocate"
+ "_activateVolume:usingIdentity:options:auditToken:replyHandler:"
+ "_deactivateVolume:usingIdentity:numericOptions:auditToken:replyHandler:"
+ "_init"
+ "_lastConnectError"
+ "_loadResource:usingIdentity:options:auditToken:replyHandler:"
+ "_mountTransaction"
+ "_unloadResource:usingIdentity:options:auditToken:replyHandler:"
+ "_workTransaction"
+ "applicationGroup"
+ "applyResource:targetBundle:instanceID:initiatorAuditToken:authorizingAuditToken:usingBlock:"
+ "applyResource:usingIdentity:instanceID:initiatorAuditToken:authorizingAuditToken:usingBlock:"
+ "blockSize"
+ "bsdName can't be nil"
+ "callMountOnPath:mountFlags:mountArgs:"
+ "com.apple.security.application-groups"
+ "daemon"
+ "doneFSCKWithTask:replyHandler:"
+ "doneWork"
+ "error starting up the daemon"
+ "fsModuleHost"
+ "fsObj"
+ "fsObj cannot be nil"
+ "getApplicationGroups:"
+ "getModuleIdentityFromShortName:"
+ "i36@0:8r*16i24^{lifs_mntargs=Iiiiii[64c][1024c][1024c][64c]iIIS}28"
+ "initProxyForBSDName:"
+ "initProxyFrom:"
+ "instance"
+ "isInternalBuild"
+ "lifsQueue"
+ "liveFilesMountPath"
+ "loading settings"
+ "loopback"
+ "mount table cannot be nil"
+ "mountEntryTransaction:%@:%@:%@"
+ "mountTaskUUID"
+ "ownAuditToken"
+ "resource"
+ "saving settings"
+ "setFPNfsPortStr:"
+ "setFsModuleHost:"
+ "setFsObj:"
+ "setInstance:"
+ "setLastConnectError:"
+ "setLoopback:"
+ "setMountTaskUUID:"
+ "setOwnAuditToken:"
+ "setResource:"
+ "setTheConn:"
+ "setTheLock:"
+ "setTheRoot:"
+ "setTheRootEntry:"
+ "setVerbose:"
+ "setVolumeID:"
+ "settings"
+ "start"
+ "startFSCKWithDevice:volumes:replyHandler:"
+ "theConn"
+ "theLock"
+ "theMountTable"
+ "theRoot"
+ "theRootEntry"
+ "updateWorkTransaction"
+ "v24@?0@\"FSTaskDescription\"8@\"NSError\"16"
+ "v36@?0i8Q12@\"NSData\"20@\"NSData\"28"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
+ "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\">56"
+ "v84@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSString\"40@\"FSFileName\"48@\"NSString\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">76"
+ "verbose"
+ "\xd1"
+ "\xf0\xa1"
- "%s: Dispatched no-mounts timer"
- "%s: ERROR sending mach port to kernel: %d"
- "%s: Load resource failed, call checkResource"
- "%s: Load resource failed, call formatResource"
- "%s: No bundleID found for fsShortName (%@)"
- "-[LivefsSettings setIdleTimerLocked:]"
- "-[fskitdXPCServer _activateVolume:usingBundle:options:auditToken:replyHandler:]_block_invoke"
- "-[fskitdXPCServer _deactivateVolume:usingBundle:numericOptions:auditToken:replyHandler:]_block_invoke"
- "-[fskitdXPCServer _loadResource:usingBundle:options:auditToken:replyHandler:]_block_invoke"
- "-[fskitdXPCServer _loadResource:usingBundle:options:auditToken:replyHandler:]_block_invoke_5"
- "-[fskitdXPCServer _probeResource:usingBundle:auditToken:replyHandler:]_block_invoke_5"
- "-[fskitdXPCServer applyResource:targetBundle:instanceID:initiatorAuditToken:authorizingAuditToken:isProbe:usingBlock:]"
- "-[fskitdXPCServer getBundleIDFromShortName:]_block_invoke"
- "/private/var/mobile/Library/LiveFiles.ticotsord"
- "@\"NSObject<OS_dispatch_source>\""
- "@68@0:8@16@24@32@40@48B56@?60"
- "Format about to return err %@ uuid %@"
- "ReadDirAndAttrs on %@"
- "Readdir called on %@"
- "_activateVolume:usingBundle:options:auditToken:replyHandler:"
- "_deactivateVolume:usingBundle:numericOptions:auditToken:replyHandler:"
- "_idleTimerSource"
- "_loadResource:usingBundle:options:auditToken:replyHandler:"
- "_our_transaction"
- "_unloadResource:usingBundle:options:auditToken:replyHandler:"
- "applyResource:targetBundle:instanceID:initiatorAuditToken:authorizingAuditToken:isProbe:usingBlock:"
- "checkResource:options:connection:taskID:replyHandler:"
- "checkVolume:options:auditToken:connection:replyHandler:"
- "checkVolume:options:connection:replyHandler:"
- "exit"
- "extensionForDefaultBundle:user:replyHandler:"
- "formatResource:options:connection:taskID:replyHandler:"
- "fskitd has the base mountpoint"
- "getBundleIDFromShortName:"
- "getProgressPortForTask:replyHandler:"
- "main"
- "newWithDefaultInstanceForBundle:user:"
- "setContainsPhotos:"
- "setIdleTimer:"
- "setIdleTimerLocked:"
- "startedWorkLocked"
- "taskSetChanged"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"FSTaskDescription\"@\"NSError\">24"
- "v48@0:8@\"NSString\"16@\"FSTaskOptionsBundle\"24@\"FSMessageConnection\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ>48"
- "v56@0:8@\"NSString\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24Q32Q40@?<v@?i@\"NSData\">48"
- "v64@0:8@\"NSString\"16Q24Q32Q40Q48@?<v@?iqQ@\"NSData\">56"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i>56"
- "v72@0:8@\"NSString\"16Q24Q32Q40Q48Q56@?<v@?iqQ@\"NSData\">64"
- "v80@0:8@\"NSString\"16@\"FSTaskOptionsBundle\"24{?=[8I]}32@\"FSMessageConnection\"64@?<v@?@\"NSUUID\"@\"NSError\">72"
- "v80@0:8@16@24{?=[8I]}32@64@?72"
- "v84@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSString\"40@\"FSFileName\"48@\"NSString\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">76"
- "\xf0Q"

```
