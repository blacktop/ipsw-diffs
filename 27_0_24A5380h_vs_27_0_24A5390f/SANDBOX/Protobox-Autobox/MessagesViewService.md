## MessagesViewService

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
 		(ipc-posix-name "/FBW1:com.apple.uikit.viewservi")
 		(ipc-posix-name "/FBW2:com.apple.uikit.viewservi")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(require-any
 		(ipc-posix-name "/FBW1:com.apple.uikit.viewservi")
 		(ipc-posix-name "/FBW2:com.apple.uikit.viewservi")
 	)
 )
 
-(deny ipc-posix-shm-write-unlink)
-(allow ipc-posix-shm-write-unlink
+(deny ipc-posix-shm-write-data)
+(allow ipc-posix-shm-write-data
 	(ipc-posix-name "/FBW1:com.apple.uikit.viewservi")
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
 		(require-not (global-name "com.apple.gamed"))

 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.coremedia.customurlloader.xpc"))
-		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.awdd"))
 		(require-not (local-name "com.apple.assistant.contextprovider.com.apple.mobilesms.compose"))
 		(require-not (global-name "com.apple.coremedia.assetimagegenerator.xpc"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.dprivacyd"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
-		(require-not (global-name "com.apple.spotlight.SearchAgent"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.coremedia.compressionsession"))
+		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.identityservicesd.nsxpc"))

 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.webprivacyd"))
-		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.coremedia.player.xpc"))

 		(require-not (global-name "com.apple.internal.InputTester"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.videotarget.xpc"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))

 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (xpc-service-name "*"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.system.logger"))

 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.dmd.policy"))
-		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.translationd"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.handwritingd.pkanalytics"))

 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.backboard.TouchDeliveryPolicyServer"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
+		(require-not (global-name "com.apple.coremedia.compressionsession"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (global-name "AccessibilityDebuggerServices"))
 		(require-not (system-attribute developer-mode))
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
```
