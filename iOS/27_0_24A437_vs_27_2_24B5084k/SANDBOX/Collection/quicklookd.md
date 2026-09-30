## quicklookd

> Group: ⬆️ Updated

```diff

 )
 (allow iokit-open-user-client
 	(require-all
-		(iokit-registry-entry-class "IOHIDLibUserClient")
+		(extension "com.apple.tcc.kTCCServiceMotionSensors")
+		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
+	)
+)
+(allow iokit-open-user-client
+	(require-all
 		(process-attribute is-apple-signed-executable)
+		(iokit-registry-entry-class "IOHIDLibUserClient")
 	)
 )
 (allow iokit-open-user-client

 		(iokit-registry-entry-class "IOAccelSharedUserClient2")
 		(iokit-registry-entry-class "IOAccelSubmitter2")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
-		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
 		(iokit-registry-entry-class "IOMobileFramebufferUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.appmanagedfeatures.restrictions")
+		(%entitlement-is-present "com.apple.developer.appmanagedfeatures")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.ThreadNetwork.xpc")
-		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.appmanagedfeatures.restrictions")
-		(%entitlement-is-present "com.apple.developer.appmanagedfeatures")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.callkit.networkextension.voip")
-		(%entitlement-is-present "com.apple.developer.networking.networkextension")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.assessmentagent")
 		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.merchantd.identity")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.family.ageRange.xpc")
-		(%entitlement-is-present "com.apple.developer.declared-age-range")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.ExposureNotification")
-		(%entitlement-is-present "com.apple.developer.exposure-notification")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.SafetyKit")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.session")
-		(%entitlement-is-present "com.apple.developer.carkey.session")
+		(global-name "com.apple.callkit.networkextension.voip")
+		(%entitlement-is-present "com.apple.developer.networking.networkextension")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.merchantd.identity")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.ExposureNotification")
+		(%entitlement-is-present "com.apple.developer.exposure-notification")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.family.ageRange.xpc")
+		(%entitlement-is-present "com.apple.developer.declared-age-range")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.seserviced.session")
+		(%entitlement-is-present "com.apple.developer.carkey.session")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.MomentsUIService")
+		(%entitlement-is-present "com.apple.developer.journal.allow")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ServicesPaymentAngel")

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
+		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")
```
