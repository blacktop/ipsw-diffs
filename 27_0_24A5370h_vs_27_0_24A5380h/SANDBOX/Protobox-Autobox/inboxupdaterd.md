## inboxupdaterd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.springboard.blockableservices"))
-		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.wifip2pd"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.private.corewifi-xpc"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.softwareupdateservicesd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.bluetooth.xpc"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.backboard.hid.services"))
-		(require-not (global-name "com.apple.nfcd.hwmanager"))
-		(require-not (global-name "com.apple.cloudd"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
-		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.datamigrator"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.diagnostics.launcher-service"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.softwareupdateservicesd"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.private.corewifi-xpc"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.bluetooth.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
+		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.diagnostics.launcher-service"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.springboard.blockableservices"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.wifip2pd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.datamigrator"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.MIBUFileServerHelper")
 			(xpc-service-name "com.apple.MIBULoopbackServerHelper")

 		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_fgetxattr
+		SYS_setxattr
 		SYS_fsetxattr
 		SYS_listxattr
 		SYS_fsctl

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_wait4_nocancel
 		SYS_recvmsg_nocancel
 		SYS_sendmsg_nocancel
 		SYS_recvfrom_nocancel

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_openat_nocancel
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_SINGLE_WRITER
+		F_OFD_SETLK
+		F_SETCONFINED
+		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 2))
-		)
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 1)
+		(require-not (mac-policy-name "vnguard"))
 	)
 )
 (deny system-mac-syscall
```
