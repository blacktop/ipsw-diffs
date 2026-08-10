## platform

> Group: ⬆️ Updated

```diff

 		(_g18 "")
 	)
 ))
-(define (_g40 _)
-	(require-any
-	(file-attribute datavault)
-	(require-all
-		(%entitlement-is-present "com.apple.private.security.storage.tmp")
-		(literal "/.com.apple.mobile_container_manager.metadata.plist")
-		(file-attribute datavault)
-		(require-not (require-any
-			(subpath "${FRONT_USER_HOME}/tmp")
-			(subpath "/private/var/tmp")
-		))
-		(require-not (require-any
-			(subpath "${FRONT_USER_HOME}/Containers")
-			(subpath "/private/var/containers")
-		))
-	)
-	(require-all
-		(literal "/.com.apple.mobile_container_manager.metadata.plist")
-		(file-attribute datavault)
-		(require-not (require-any
-			(subpath "${FRONT_USER_HOME}/Containers")
-			(subpath "/private/var/containers")
-		))
-	)
-	(require-all
-		(require-not (storage-class "AppDataContainers"))
-		(require-any
-			(require-all
-				(require-not (file-attribute sip-protected))
-				(_g39 "")
-			)
-			(require-all
-				(storage-class "DiagnosticReports")
-				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.DiagnosticReports.read-only"))
-				(require-not (file-attribute sip-protected))
-				(_g39 "")
-			)
-			(require-all
-				(storage-class "os_eligibility")
-				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.os_eligibility.readonly"))
-				(require-not (file-attribute sip-protected))
-				(_g39 "")
-			)
-		)
-	)
-))
 (allow file-read-metadata
 	(require-all
 	(require-not (%entitlement-is-bool-true "com.apple.rootless.datavault.metadata"))
+	(require-not (storage-class-extension #f))
 	(require-any
+		(file-attribute datavault)
 		(require-all
-			(require-not (storage-class-extension #f))
-			(_g40 "")
+			(%entitlement-is-present "com.apple.private.security.storage.tmp")
+			(literal "/.com.apple.mobile_container_manager.metadata.plist")
+			(file-attribute datavault)
+			(require-not (require-any
+				(subpath "${FRONT_USER_HOME}/tmp")
+				(subpath "/private/var/tmp")
+			))
+			(require-not (require-any
+				(subpath "${FRONT_USER_HOME}/Containers")
+				(subpath "/private/var/containers")
+			))
 		)
 		(require-all
-			(signing-identifier "com.apple.deleted_helper")
-			(require-not (subpath "/private/var/dirs_cleaner"))
-			(require-not (storage-class-extension #f))
-			(_g40 "")
+			(literal "/.com.apple.mobile_container_manager.metadata.plist")
+			(file-attribute datavault)
+			(require-not (require-any
+				(subpath "${FRONT_USER_HOME}/Containers")
+				(subpath "/private/var/containers")
+			))
+		)
+		(require-all
+			(require-not (storage-class "AppDataContainers"))
+			(require-any
+				(require-all
+					(require-not (file-attribute sip-protected))
+					(_g39 "")
+				)
+				(require-all
+					(storage-class "DiagnosticReports")
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.DiagnosticReports.read-only"))
+					(require-not (file-attribute sip-protected))
+					(_g39 "")
+				)
+				(require-all
+					(storage-class "os_eligibility")
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.os_eligibility.readonly"))
+					(require-not (file-attribute sip-protected))
+					(_g39 "")
+				)
+			)
 		)
 	)
 )

 ))
 (deny file-write-unlink
 	(require-any
-	(require-all
-		(literal "/private/var/MobileSoftwareUpdate")
-		(require-any
-			(require-not (%entitlement-is-bool-true "com.apple.private.security.disk-device-access"))
-			(system-attribute restore-os)
-		)
-	)
+	(literal "/private/var/MobileSoftwareUpdate")
 	(require-all
 		(require-any
 			(literal "/private/tmp")

 			(require-all
 				(process-attribute is-sandboxed)
 				(require-any
+					(require-all
+						(global-name "com.apple.DriverKitAppServer")
+						(%entitlement-is-bool-true "com.apple.developer.system-extension.install")
+					)
 					(require-all
 						(global-name "com.apple.ScreenTimeAgent.Contacts")
 						(require-not (%entitlement-is-bool-true "com.apple.private.contactsui"))

 			(require-all
 				(process-attribute is-sandboxed)
 				(require-any
+					(require-all
+						(global-name "com.apple.DriverKitAppServer")
+						(%entitlement-is-bool-true "com.apple.developer.system-extension.install")
+					)
 					(require-all
 						(global-name "com.apple.ScreenTimeAgent.Contacts")
 						(require-not (%entitlement-is-bool-true "com.apple.private.contactsui"))

 			(require-all
 				(process-attribute is-sandboxed)
 				(require-any
+					(require-all
+						(global-name "com.apple.DriverKitAppServer")
+						(%entitlement-is-bool-true "com.apple.developer.system-extension.install")
+					)
 					(require-all
 						(global-name "com.apple.ScreenTimeAgent.Contacts")
 						(require-not (%entitlement-is-bool-true "com.apple.private.contactsui"))
```
