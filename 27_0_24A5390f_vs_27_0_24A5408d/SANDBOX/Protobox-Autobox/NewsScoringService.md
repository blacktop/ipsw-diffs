## NewsScoringService

> Group: ⬆️ Updated

```diff

 (allow iokit-open-service
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
+		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
 		(iokit-registry-entry-class "H11ANEIn")

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))

 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_recvmsg
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_access
 		SYS_crossarch_trap
 		SYS_getppid

 		SYS_getgroups
 		SYS_dup2
 		SYS_fcntl
+		SYS_select
 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getsockopt
 		SYS_readv
 		SYS_writev
 		SYS_rename

 		SYS_setattrlist
 		SYS_getxattr
 		SYS_setxattr
+		SYS_fsetxattr
 		SYS_fsctl
 		SYS_ffsctl
 		SYS_shm_open

 		SYS_kevent_qos
 		SYS_kevent_id
 		SYS___mac_syscall
+		SYS_pselect
+		SYS_pselect_nocancel
 		SYS_read_nocancel
 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_recvmsg_nocancel
 		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
 		SYS_msync_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel

 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK
+		F_OFD_SETLKWTIMEOUT
 		F_SETCONFINED
 		F_GETCONFINED
 		F_ADDFILESIGS_RETURN

 (allow system-necp-client-action
 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
 		NECP_CLIENT_ACTION_REMOVE)
 )
 
```
