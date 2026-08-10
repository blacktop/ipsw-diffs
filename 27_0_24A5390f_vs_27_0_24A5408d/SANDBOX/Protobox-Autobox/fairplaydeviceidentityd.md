## fairplaydeviceidentityd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
+		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))

 		SYS_psynch_rw_upgrade
 		SYS_psynch_mutexwait
 		SYS_psynch_mutexdrop
+		SYS_psynch_cvbroad
+		SYS_psynch_cvsignal
+		SYS_psynch_cvwait
 		SYS_psynch_rw_rdlock
 		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
+		SYS_psynch_cvclrprepost
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask
```
