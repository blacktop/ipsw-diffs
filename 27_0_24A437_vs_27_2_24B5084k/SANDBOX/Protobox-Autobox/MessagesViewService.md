## MessagesViewService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (require-any
 			(global-name "com.apple.Emporda.Emporda3PK")
-			(global-name "com.apple.TextInput.shortcuts")
 			(global-name "com.apple.rapport.remote-text-input")
 			(global-name "com.apple.remote-text-editing")
 		))

 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
-		(require-not (xpc-service-name "*"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.coremedia.customurlloader.xpc"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.siri.vocabularyupdates"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.awdd"))
 		(require-not (local-name "com.apple.assistant.contextprovider.com.apple.mobilesms.compose"))
 		(require-not (global-name "com.apple.coremedia.assetimagegenerator.xpc"))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.spotlight.SearchAgent"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.dprivacyd"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
-		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.identityservicesd.nsxpc"))

 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.webprivacyd"))
-		(require-not (local-name "com.apple.accessibility.gax.client"))
+		(require-not (global-name "com.apple.TextInput.shortcuts"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.coremedia.player.xpc"))

 		(require-not (global-name "com.apple.internal.InputTester"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.videotarget.xpc"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))

 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.sage.textcomposition"))

 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.dmd.policy"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.translationd"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.handwritingd.pkanalytics"))

 		(require-not (global-name "com.apple.backboard.TouchDeliveryPolicyServer"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.coremedia.compressionsession"))
+		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "UIASTNotificationCenter"))

 				mach_vm_region_recurse
 				mach_vm_region
 				_mach_make_memory_entry
+				mach_vm_page_range_query
 				mach_vm_deferred_reclamation_buffer_allocate
 				mach_vm_deferred_reclamation_buffer_flush
 				mach_vm_range_create
```
