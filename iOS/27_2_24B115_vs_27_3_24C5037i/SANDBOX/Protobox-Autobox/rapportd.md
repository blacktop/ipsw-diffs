## rapportd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
+		(require-not (require-any
+			(global-name "com.apple.ApplicationService.ServiceDiscovery")
+			(global-name "com.apple.CompanionLink.tandem")
+			(global-name "com.apple.SharingServices.tandem")
+			(global-name "com.apple.nearbyd.xpc.beacon")
+			(global-name "com.apple.rapport.NearbyInvitation")
+			(global-name "com.apple.rapport.siri-audio")
+			(global-name "com.apple.rapport.tandem")
+			(global-name "com.apple.sharingd.contactprovider")
+		))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.cdp.daemon"))
-		(require-not (require-any
-			(global-name "com.apple.ApplicationService.ServiceDiscovery")
-			(global-name "com.apple.nearbyd.xpc.beacon")
-			(global-name "com.apple.rapport.NearbyInvitation")
-			(global-name "com.apple.rapport.siri-audio")
-			(global-name "com.apple.sharingd.contactprovider")
-		))
 		(require-not (global-name "com.apple.corercd"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.homehubd.manage"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.PineBoardRiseServices"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.sirittsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.homed.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
 		(require-not (global-name "com.apple.sharingd.nsxpc"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
+		(require-not (xpc-service-name "com.apple.OSLogService"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-any
 			(require-all

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_setxattr
 		SYS_listxattr

 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
+		F_SETPROTECTIONCLASS
 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
