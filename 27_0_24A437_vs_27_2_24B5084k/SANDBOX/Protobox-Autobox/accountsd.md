## accountsd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.appleidsetupd")
 			(global-name "com.apple.coreidvd.system-notifications")
 			(global-name "com.apple.icloud.fmflocatord")
+			(global-name "com.apple.imtransferservices.IMTransferAgent")
 			(global-name "com.apple.transparencyd.accounts-support")
 		))
 		(require-not (global-name "com.apple.adid.xpc"))

 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.audioanalyticsd"))

 		(require-not (global-name "com.apple.cloudkit.partlycloudd"))
 		(require-not (global-name "com.apple.amsaccountsd.multiuser"))
 		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
 		(require-not (global-name "com.apple.dataaccess.dataaccessd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.passd.cloud-store"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.identityservicesd.pds"))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))

 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.AssetCacheLocatorService"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.persistence"))
 		(require-not (global-name "com.apple.eligibilityd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 		(require-not (global-name "com.apple.xpc.amstreatmentstoreservice"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.SafariBookmarksSyncAgent"))
-		(require-not (global-name "com.apple.exchangesyncd"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.xpc.amsserverdatacacheservice"))
 		(require-not (global-name "com.apple.calaccessd"))

 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.groupkitd.xpc.groupservice"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.spotlight.IndexDelegateAgent"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.ak.walrus.xpc"))

 		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (global-name "com.apple.ckdiscretionaryd"))
 		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
+		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.Maps.mapspushd"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.icloud.findmydeviced"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.spotlight.IndexDelegateAgent"))
+		(require-not (global-name "com.apple.exchangesyncd"))
 		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.NPKCompanionAgent.Server"))
 		(require-not (global-name "com.apple.SharedWebCredentials"))

 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.aggregated"))
-		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))

 		SIOCGIFFUNCTIONALTYPE
 		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
-		SIOCGIFULTRACONSTRAINED)
+		SIOCGIFULTRACONSTRAINED
+		TIOCGETA)
 )
 
 (deny syscall-unix)

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
 		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
```
