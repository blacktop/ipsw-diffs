## Siri AI

> Group: ⬆️ Updated

```diff

 			(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
 			(iokit-registry-entry-class "IOGPUDeviceUserClient")
 			(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
+			(iokit-registry-entry-class "IOHIDLibUserClient")
 			(iokit-registry-entry-class "IOMobileFramebufferUserClient")
 			(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 			(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")

 		(require-not (global-name "com.apple.Carousel.alertSuppression"))
 		(require-not (global-name "com.apple.carousel.sessionservice"))
 		(require-not (global-name "com.apple.TextInput.emoji"))
+		(require-not (global-name "com.apple.dictationengined"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.suggestd.contacts"))
 		(require-not (global-name "com.apple.handwritingd.pksettings"))

 		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.linkd.extension"))
 		(require-not (global-name "com.apple.assistant.client"))
+		(require-not (global-name "com.apple.siri.audio_message_service.xpc"))
 		(require-not (global-name "com.apple.tvremotecore.xpc"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.coremedia.capturesession"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.assetimagegenerator.xpc"))
 		(require-not (global-name "com.apple.rti-screencontinuity"))
 		(require-not (global-name "com.apple.siri.orchestration.prescribedaction"))
+		(require-not (require-any
+			(global-name "com.apple.products.productsd")
+			(global-name "com.apple.siri.flowtools_xpc_service")
+		))
 		(require-not (global-name "com.apple.intelligenceflow.uiContext"))
 		(require-not (require-any
 			(global-name "com.apple.generativeexperiences.ExternalPartnerCredentialStorage")

 		(require-not (global-name "com.apple.assistant.cdm"))
 		(require-not (global-name "com.apple.bird"))
 		(require-not (global-name "com.apple.Carousel.contextuallock"))
+		(require-not (global-name "com.apple.corespeech.corespeechd.endpointer.service"))
 		(require-not (require-any
 			(global-name "com.apple.findmy.FindingUIAngel.mach")
 			(global-name "com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite")

 		(require-not (global-name "com.apple.email.maild"))
 		(require-not (global-name "com.apple.biome.compute.publisher.service"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
+		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.public"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))

 		(require-not (global-name "com.apple.TextInput.shortcuts"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.mediaanalysisd.embeddingstore"))
+		(require-not (global-name "com.apple.iond.output"))
 		(require-not (global-name "com.apple.generativeexperiences.ExternalProviderTCCManagingXPC"))
 		(require-not (global-name "com.apple.sleepd.sleepserver"))
 		(require-not (global-name "com.apple.searchd.background"))
 		(require-not (global-name "com.apple.internal.InputTester"))
+		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (require-any

 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
+		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.contactsd.support"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.videotarget.xpc"))
 		(require-not (global-name "com.apple.proactive.appDirectory"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.xpc.amstoold"))

 		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.assistant.analytics"))
 		(require-not (global-name "com.apple.SharedWebCredentials"))
-		(require-not (global-name "com.apple.siri.flowtools_xpc_service"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (require-any
 			(global-name "com.apple.internal.SpotlightAutomationTester")

 		(require-not (xpc-service-name "com.apple.textkit.nsattributedstringagent"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-not (xpc-service-name "com.apple.BarcodeSupport.ParsingService"))
+		(require-not (xpc-service-name "com.navercorp.smartboard.extension"))
 		(require-not (require-any
 			(xpc-service-name "com.google.keyboard.KeyboardExtension")
 			(xpc-service-name "com.sogou.sogouinput.basekeyboard")

 		))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
 		(require-not (xpc-service-name "com.apple.weatherkit.authservice"))
+		(require-not (xpc-service-name "com.apple.appintents.LiveEntityService"))
+		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
 		(require-not (xpc-service-name "com.apple.datadetectors.AddToRecentsService"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (xpc-service-name "com.apple.Emporda.Emporda3PK"))
```
