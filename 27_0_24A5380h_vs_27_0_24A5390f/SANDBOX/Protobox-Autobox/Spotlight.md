## Spotlight

> Group: ⬆️ Updated

```diff

 	(extension-class "com.apple.webkit.mach-bootstrap")
 )
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleANS2CGNVMeController")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(ipc-posix-name "hangtelemetryd.onceatboot")
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(ipc-posix-name "/hop_85656")
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.storekitd"))

 		(require-not (global-name "com.apple.coremedia.remaker"))
 		(require-not (global-name "com.apple.businessservicesd"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.exchangesyncd"))
+		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
-		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
+		(require-not (global-name "com.apple.exchangesyncd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (require-any
 			(global-name "com.apple.internal.SpotlightAutomationTester")

 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
-		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.appstorecomponentsd.xpc"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))

 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.parsec-fbf"))
-		(require-not (global-name "com.apple.coremedia.compressionsession"))
+		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.coremedia.formatreader.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.KeyBoard.services")

 		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
-		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
+		(require-not (global-name "com.apple.coremedia.compressionsession"))
 		(require-not (global-name "com.apple.dataaccess.dataaccessd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
-		(require-not (global-name "com.apple.spaceattributiond"))
+		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.itunescloud.remote-request-execution-service"))
 		(require-not (global-name "com.apple.mobileactivationd"))

 			(global-name "com.apple.coremedia.mediaplaybackd.videocompositor.xpc")
 			(global-name "com.apple.coremedia.videocompositor")
 		))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callprovidermanager"))
 		(require-not (global-name "com.apple.siriknowledged"))
 		(require-not (global-name "com.apple.DataDeliveryServices.AssetService"))

 		(require-not (global-name "com.apple.siri.activation.service"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.StatusKit.subscribe"))
 		(require-not (global-name "com.apple.Music.MPMusicPlayerControllerInternal"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.paperboard.services"))
-		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (global-name "com.apple.cloudasset.cloudd"))
 		(require-not (global-name "com.apple.foundationmodels.languagemodelservice"))
 		(require-not (global-name "com.apple.voicebanking.services"))

 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))
-		(require-not (global-name "com.apple.dmd.policy"))
+		(require-not (global-name "com.apple.translationd"))
 		(require-not (global-name "com.apple.campo"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.pommesmld.pmldservice"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.coremedia.customurlloader.xpc"))
-		(require-not (local-name "com.apple.assistant.contextprovider.com.apple.Spotlight"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc"))

 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))
 		(require-not (global-name "com.apple.mediaartworkd.xpc"))
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.internal.studylogd"))
 		(require-not (global-name "com.apple.MapKit.SnapshotService"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
 		(require-not (global-name "com.apple.awdd"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (local-name "com.apple.assistant.contextprovider.com.apple.Spotlight"))
 		(require-not (global-name "com.apple.coremedia.assetimagegenerator.xpc"))
 		(require-not (global-name "com.apple.SafariBookmarksSyncAgent"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (global-name "com.apple.coremedia.routingsessionmanager.xpc"))
 		(require-not (global-name "com.apple.facetimemessagestored.service"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.email.maild"))
 		(require-not (global-name "com.apple.biome.compute.publisher.service"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
-		(require-not (global-name "com.apple.translationd"))
+		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (global-name "com.apple.proactive.visual-action-prediction"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))

 		(require-not (global-name "com.apple.WebBookmarks.webbookmarksd"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.spotlight.resources.assets"))
-		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.revisiond"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.SystemConfiguration.helper"))
-		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.coremedia.figvirtualcapturecard.xpc"))
 		(require-not (global-name "com.apple.photoanalysisd"))
 		(require-not (global-name "com.apple.webprivacyd"))
-		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.coremedia.player.xpc"))
-		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
+		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
 		(require-not (global-name "com.apple.sleepd.sleepserver"))
 		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (global-name "com.apple.searchd.background"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
-		(require-not (global-name "com.apple.coremedia.sandboxserver.xpc"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.proactive.visual-action-prediction"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-not (global-name "com.apple.coremedia.mutablecomposition.xpc"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.videotarget.xpc"))
 		(require-not (global-name "com.apple.proactive.appDirectory"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
+		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.handwritingd.pkanalytics"))
+		(require-not (global-name "com.apple.coremedia.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
-		(require-not (global-name "com.apple.revisiond"))
-		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.handwritingd.pkanalytics"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.group-activities.conversationmanagerhost"))
 		(require-not (global-name "com.apple.itunesstored.xpc"))
 		(require-not (global-name "com.apple.gputools.service"))
 		(require-not (global-name "com.apple.remindd"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
 		(require-not (global-name "com.apple.askpermissiond"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))

 		(require-not (global-name "com.apple.hid.PencilHaptics"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.nesessionmanager"))
+		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (global-name "AccessibilityDebuggerServices"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
```
