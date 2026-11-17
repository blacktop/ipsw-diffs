## assetsd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")
 		(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")

 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
+		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.biome.compute.source"))
 		(require-not (global-name "com.apple.mediaanalysisd.analysis"))

 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))

 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.systemstatus.publisher"))
 		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.coremedia.deferredmedia.photoprocessor"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.corespotlight.receiver.checkin"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.photoanalysisd"))
 		(require-not (global-name "com.apple.coremedia.player.xpc"))

 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.bulletinboard.observerconnection"))

 	(ioctl-command
 		CTLIOCGINFO
 		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 		SYS_ioctl
 		SYS_symlink
 		SYS_readlink
+		SYS_execve
 		SYS_umask
 		SYS_msync
 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
 		SYS_mincore
+		SYS_setitimer
 		SYS_dup2
 		SYS_fcntl
 		SYS_select

 		SYS_fchmod
 		SYS_rename
 		SYS_flock
+		SYS_mkfifo
 		SYS_sendto
 		SYS_shutdown
 		SYS_socketpair
```
