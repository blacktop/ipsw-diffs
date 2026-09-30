## Siri AI

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(deny iokit-issue-extension
+(deny iokit-get-properties
 	(process-attribute is-autoboxed)
 )
-(allow iokit-issue-extension
+(allow iokit-get-properties
 	(require-all
 		(process-attribute is-autoboxed)
 		(extension-class "com.apple.webkit.extension.iokit")
 	)
 )
 
-(deny iokit-open-user-client
+(deny iokit-open*
 	(process-attribute is-autoboxed)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
+(deny iokit-open-service
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
 (deny iokit-set-properties
 	(with no-report)
 	(process-attribute is-autoboxed)

 	(process-attribute is-autoboxed)
 )
 
-(deny ipc-posix-sem-open
+(deny ipc-posix-sem-create
 	(process-attribute is-autoboxed)
 )
-(allow ipc-posix-sem-open
+(allow ipc-posix-sem-create
 	(require-all
 		(process-attribute is-autoboxed)
 		(ipc-posix-name "hangtelemetryd.onceatboot")
 	)
 )
 
-(deny ipc-posix-shm-read-data
+(deny ipc-posix-shm*
 	(process-attribute is-autoboxed)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
-(deny ipc-posix-shm-write-data
+(deny ipc-posix-shm-write-create
 	(process-attribute is-autoboxed)
 )
-(allow ipc-posix-shm-write-data
+(allow ipc-posix-shm-write-create
 	(require-all
 		(process-attribute is-autoboxed)
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 	)
 )
 
-(deny job-creation
+(deny isp-command-send
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
-(deny mach-issue-extension
+(deny mach-host-special-port-set
 	(require-all
 		(process-attribute is-autoboxed)
 		(extension-class "com.apple.webkit.extension.mach")

 	)
 )
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(require-not (global-name "com.apple.storekitd"))
 		(require-not (global-name "com.apple.gamed"))

 		(require-not (xpc-service-name "com.apple.WebKit.GPU"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
-		(require-not (require-any
-			(xpc-service-name "app.spokenly.keyboard")
-			(xpc-service-name "com.Vince14Genius.IPA-Keyboard-iOS.IPA-Keyboard-Extension")
-			(xpc-service-name "com.apple.PrintKit.PrinterTool")
-			(xpc-service-name "com.apple.UIKit.SecureControlService")
-			(xpc-service-name "com.aquavoice.ios.keyboard")
-			(xpc-service-name "com.baidujp.Simeji.SimejiKB")
-			(xpc-service-name "com.can-jin.pokegenie.Poke-Genie-Keyboard")
-			(xpc-service-name "com.giphy.giphyformessenger.KeyboardExtension")
-			(xpc-service-name "com.monologue.MonologueApp.Keyboard")
-			(xpc-service-name "fontskeyboard.fonts.keyboard")
-			(xpc-service-name "ios.moe.TaiwaneseTaigi.KbExtension")
-			(xpc-service-name "me.blog.krazie99.dankeyplus.DanKeyboad")
-			(xpc-service-name "net.bytesize.wordboard.keyboard")
-			(xpc-service-name "vn.com.vng.labankey.keyboard")
-		))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.OSLogService"))
 		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))

 		))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
+		(require-not (require-any
+			(xpc-service-name "app.spokenly.keyboard")
+			(xpc-service-name "com.Vince14Genius.IPA-Keyboard-iOS.IPA-Keyboard-Extension")
+			(xpc-service-name "com.apple.PrintKit.PrinterTool")
+			(xpc-service-name "com.apple.UIKit.SecureControlService")
+			(xpc-service-name "com.aquavoice.ios.keyboard")
+			(xpc-service-name "com.baidujp.Simeji.SimejiKB")
+			(xpc-service-name "com.can-jin.pokegenie.Poke-Genie-Keyboard")
+			(xpc-service-name "com.giphy.giphyformessenger.KeyboardExtension")
+			(xpc-service-name "com.monologue.MonologueApp.Keyboard")
+			(xpc-service-name "fontskeyboard.fonts.keyboard")
+			(xpc-service-name "ios.moe.TaiwaneseTaigi.KbExtension")
+			(xpc-service-name "me.blog.krazie99.dankeyplus.DanKeyboad")
+			(xpc-service-name "net.bytesize.wordboard.keyboard")
+			(xpc-service-name "vn.com.vng.labankey.keyboard")
+		))
 		(require-not (xpc-service-name "com.apple.MapKit.SnapshotService"))
 		(require-not (xpc-service-name "com.baidu.inputMethod.keyboard"))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))

 	)
 )
 
-(deny process-exec*
+(deny process-codesigning
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
-(deny process-exec-interpreter
+(deny process-exec*
 	(require-all
 		(require-not (literal "/bin/bash"))
 		(process-attribute is-autoboxed)
```
