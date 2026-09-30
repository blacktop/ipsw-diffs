## platform

> Group: ⬆️ Updated

```diff

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g4 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-not (process-attribute is-datavault-controller))

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g6 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g5 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g5 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g5 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 (define (_g5 _)
 	(require-any
 	(_g4 "")
-	(require-all
-		(process-attribute is-datavault-controller)
-		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
-		(require-not (subpath "/private/var/db/sysdiagnose"))
-		(process-attribute is-installer)
-		(storage-class "sysdiagnose.sysdiagnose")
-		(_g3 "")
-	)
 	(require-all
 		(process-attribute is-initproc)
 		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")

 		(storage-class "sysdiagnose.sysdiagnose")
 		(_g3 "")
 	)
-	(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.MobileAssetGenerativeModels"))
+	(require-all
+		(signing-identifier "com.apple.logd")
+		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+		(require-not (subpath "/private/var/db/sysdiagnose"))
+		(process-attribute is-installer)
+		(storage-class "sysdiagnose.sysdiagnose")
+		(_g3 "")
+	)
+	(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
 ))
 (define (_g6 _)
 	(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable")))

 			)
 			(require-all
 				(process-attribute is-installer)
-				(storage-class "MobileAssetGenerativeModels")
+				(storage-class "LogdPreferencesCache")
 				(_g5 "")
 			)
 			(require-all

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(_g5 "")
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-not (process-attribute is-datavault-controller))

 			)
 			(require-all
 				(storage-class "MobileAssetGenerativeModels")
-				(_g5 "")
+				(require-any
+					(_g4 "")
+					(require-all
+						(process-attribute is-datavault-controller)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(process-attribute is-installer)
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(process-attribute is-installer)
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(process-attribute is-installer)
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.MobileAssetGenerativeModels"))
+				)
 			)
 			(require-all
 				(storage-class "MobileBackup")

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g6 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g5 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g5 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g5 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 (define (_g20 _)
 	(require-any
 	(_g19 "")
-	(require-all
-		(process-attribute is-datavault-controller)
-		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
-		(require-not (subpath "/private/var/db/sysdiagnose"))
-		(process-attribute is-installer)
-		(storage-class "sysdiagnose.sysdiagnose")
-		(_g18 "")
-	)
 	(require-all
 		(process-attribute is-initproc)
 		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")

 		(storage-class "sysdiagnose.sysdiagnose")
 		(_g18 "")
 	)
-	(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.MobileAssetGenerativeModels"))
+	(require-all
+		(signing-identifier "com.apple.logd")
+		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+		(require-not (subpath "/private/var/db/sysdiagnose"))
+		(process-attribute is-installer)
+		(storage-class "sysdiagnose.sysdiagnose")
+		(_g18 "")
+	)
+	(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
 ))
 (define (_g21 _)
 	(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable")))

 					)
 					(require-all
 						(process-attribute is-installer)
-						(storage-class "MobileAssetGenerativeModels")
+						(storage-class "LogdPreferencesCache")
 						(_g20 "")
 					)
 					(require-all

 							(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 						)
 					)
+					(require-all
+						(storage-class "LogdPreferencesCache")
+						(_g20 "")
+					)
 					(require-all
 						(storage-class "Mail")
 						(require-any

 					)
 					(require-all
 						(storage-class "MobileAssetGenerativeModels")
-						(_g20 "")
+						(require-any
+							(_g19 "")
+							(require-all
+								(process-attribute is-datavault-controller)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(process-attribute is-installer)
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g18 "")
+							)
+							(require-all
+								(process-attribute is-initproc)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(process-attribute is-installer)
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g18 "")
+							)
+							(require-all
+								(process-attribute is-installer)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(process-attribute is-installer)
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g18 "")
+							)
+							(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.MobileAssetGenerativeModels"))
+						)
 					)
 					(require-all
 						(storage-class "MobileAssetManifestStorage")

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g4 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-not (process-attribute is-datavault-controller))

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g4 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-not (process-attribute is-datavault-controller))

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g10 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g9 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g9 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g9 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-any

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g31 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g13 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 							(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 						)
 					)
+					(require-all
+						(storage-class "LogdPreferencesCache")
+						(require-any
+							(_g34 "")
+							(require-all
+								(process-attribute is-initproc)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g33 "")
+							)
+							(require-all
+								(process-attribute is-installer)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g33 "")
+							)
+							(require-all
+								(signing-identifier "com.apple.logd")
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g33 "")
+							)
+							(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+						)
+					)
 					(require-all
 						(storage-class "Mail")
 						(require-any

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g15 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g14 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g14 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g14 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-any

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g36 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g35 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g35 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g35 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g19 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g18 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g18 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g18 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g31 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g13 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g31 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g13 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g34 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g33 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g33 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g33 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g17 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g16 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g16 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g16 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g31 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g13 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g4 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g3 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-not (process-attribute is-datavault-controller))

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g31 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g13 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(require-any
+					(_g19 "")
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g18 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g18 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.logd")
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g18 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+				)
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-any

 (define (_g34 _)
 	(require-any
 	(_g33 "")
-	(require-all
-		(process-attribute is-datavault-controller)
-		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
-		(require-not (subpath "/private/var/db/sysdiagnose"))
-		(process-attribute is-installer)
-		(storage-class "sysdiagnose.sysdiagnose")
-		(_g32 "")
-	)
 	(require-all
 		(process-attribute is-initproc)
 		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")

 		(storage-class "sysdiagnose.sysdiagnose")
 		(_g32 "")
 	)
-	(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.MobileAssetGenerativeModels"))
+	(require-all
+		(signing-identifier "com.apple.logd")
+		(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+		(require-not (subpath "/private/var/db/sysdiagnose"))
+		(process-attribute is-installer)
+		(storage-class "sysdiagnose.sysdiagnose")
+		(_g32 "")
+	)
+	(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
 ))
 (define (_g35 _)
 	(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable")))

 			)
 			(require-all
 				(process-attribute is-installer)
-				(storage-class "MobileAssetGenerativeModels")
+				(storage-class "LogdPreferencesCache")
 				(_g34 "")
 			)
 			(require-all

 					(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 				)
 			)
+			(require-all
+				(storage-class "LogdPreferencesCache")
+				(_g34 "")
+			)
 			(require-all
 				(storage-class "Mail")
 				(require-any

 			)
 			(require-all
 				(storage-class "MobileAssetGenerativeModels")
-				(_g34 "")
+				(require-any
+					(_g33 "")
+					(require-all
+						(process-attribute is-datavault-controller)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(process-attribute is-installer)
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g32 "")
+					)
+					(require-all
+						(process-attribute is-initproc)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(process-attribute is-installer)
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g32 "")
+					)
+					(require-all
+						(process-attribute is-installer)
+						(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+						(require-not (subpath "/private/var/db/sysdiagnose"))
+						(process-attribute is-installer)
+						(storage-class "sysdiagnose.sysdiagnose")
+						(_g32 "")
+					)
+					(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.MobileAssetGenerativeModels"))
+				)
 			)
 			(require-all
 				(storage-class "MobileAssetManifestStorage")

 						(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 					)
 				)
+				(require-all
+					(storage-class "LogdPreferencesCache")
+					(require-any
+						(_g31 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g30 "")
+						)
+						(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+					)
+				)
 				(require-all
 					(storage-class "Mail")
 					(require-any

 				(require-not (require-ancestor-with-entitlement "com.apple.private.security.storage-exempt.heritable"))
 			)
 		)
+		(require-all
+			(storage-class "LogdPreferencesCache")
+			(require-any
+				(_g13 "")
+				(require-all
+					(process-attribute is-initproc)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(process-attribute is-installer)
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-all
+					(signing-identifier "com.apple.logd")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+					(require-not (subpath "/private/var/db/sysdiagnose"))
+					(storage-class "sysdiagnose.sysdiagnose")
+					(_g12 "")
+				)
+				(require-not (%entitlement-is-bool-true "com.apple.private.security.storage.LogdPreferencesCache"))
+			)
+		)
 		(require-all
 			(storage-class "Mail")
 			(require-any

 		(_g15 "")
 	)
 ))
-(deny iokit-open-user-client
+(deny iokit-open*
 	(require-any
 	(require-all
 		(process-attribute is-sandboxed)

 )
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-not (process-attribute is-sandboxed))
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(with authority)
 	(ipc-posix-name "com.apple.featureflags.shm")
 )
-(allow ipc-posix-shm-read-data)
+(allow ipc-posix-shm*)
+
+(allow ipc-posix-shm-read-data
+	(require-not (ipc-posix-name "com.apple.featureflags.shm"))
+)
 
 (allow ipc-posix-shm-write*
 	(require-not (ipc-posix-name "com.apple.featureflags.shm"))
 )
 
-(deny mach-cross-domain-lookup)
-(allow mach-cross-domain-lookup
+(deny mach-bootstrap)
+(allow mach-bootstrap
 	(require-any
 		(global-name "com.apple.AssetCacheLocatorService")
 		(global-name "com.apple.CommCenter")

 	)
 )
 
-(deny mach-host-exception-port-set)
-(allow mach-host-exception-port-set
+(deny mach-host*)
+(allow mach-host*
 	(require-any
 		(%entitlement-is-bool-true "com.apple.private.host-exception-port-override")
 		(process-attribute is-initproc)
 	)
 )
 
-(allow mach-host-special-port-set
+(allow mach-host-exception-port-set
 	(with report)
 	(require-all
 		(require-not (process-attribute is-initproc))

 	)
 )
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(with authority)
 	(require-all
 		(process-attribute is-platform-binary)

 								(require-not (%entitlement-is-present "com.apple.private.biome.read-only"))
 								(require-not (%entitlement-is-present "com.apple.private.intelligenceplatform.use-cases"))
 								(require-any
-									(global-name "com.apple.cloudasset.cloudd")
-									(global-name "com.apple.copresence.conversationmanagerhost")
+									(global-name "com.apple.matter.framework.xpc")
+									(global-name "com.apple.matter.native.xpc")
 								)
-								(require-not (%entitlement-is-present "com.apple.developer.group-session"))
+								(require-not (%entitlement-is-present "com.apple.developer.homekit"))
 								(xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner")
 								(require-not (%entitlement-is-present "com.apple.shortcuts.background-running"))
 								(require-not (%entitlement-is-present "com.apple.siri.VoiceShortcuts.xpc"))

 							)
 							(require-all
 								(require-any
-									(global-name "com.apple.cloudasset.cloudd")
-									(global-name "com.apple.copresence.conversationmanagerhost")
+									(global-name "com.apple.matter.framework.xpc")
+									(global-name "com.apple.matter.native.xpc")
 								)
-								(require-not (%entitlement-is-present "com.apple.developer.group-session"))
+								(require-not (%entitlement-is-present "com.apple.developer.homekit"))
 								(xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner")
 								(require-not (%entitlement-is-present "com.apple.shortcuts.background-running"))
 								(require-not (%entitlement-is-present "com.apple.siri.VoiceShortcuts.xpc"))

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-not (process-attribute is-sandboxed))
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(process-attribute is-platform-binary)
 		(xpc-service-name "com.apple.WebKit.*")

 								(require-not (%entitlement-is-present "com.apple.private.biome.read-only"))
 								(require-not (%entitlement-is-present "com.apple.private.intelligenceplatform.use-cases"))
 								(require-any
-									(global-name "com.apple.cloudasset.cloudd")
-									(global-name "com.apple.copresence.conversationmanagerhost")
+									(global-name "com.apple.matter.framework.xpc")
+									(global-name "com.apple.matter.native.xpc")
 								)
-								(require-not (%entitlement-is-present "com.apple.developer.group-session"))
+								(require-not (%entitlement-is-present "com.apple.developer.homekit"))
 								(xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner")
 								(require-not (%entitlement-is-present "com.apple.shortcuts.background-running"))
 								(require-not (%entitlement-is-present "com.apple.siri.VoiceShortcuts.xpc"))

 							)
 							(require-all
 								(require-any
-									(global-name "com.apple.cloudasset.cloudd")
-									(global-name "com.apple.copresence.conversationmanagerhost")
+									(global-name "com.apple.matter.framework.xpc")
+									(global-name "com.apple.matter.native.xpc")
 								)
-								(require-not (%entitlement-is-present "com.apple.developer.group-session"))
+								(require-not (%entitlement-is-present "com.apple.developer.homekit"))
 								(xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner")
 								(require-not (%entitlement-is-present "com.apple.shortcuts.background-running"))
 								(require-not (%entitlement-is-present "com.apple.siri.VoiceShortcuts.xpc"))

 		)
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(process-attribute is-platform-binary)
 		(xpc-service-name "com.apple.WebKit.*")

 								(require-not (%entitlement-is-present "com.apple.private.biome.read-only"))
 								(require-not (%entitlement-is-present "com.apple.private.intelligenceplatform.use-cases"))
 								(require-any
-									(global-name "com.apple.cloudasset.cloudd")
-									(global-name "com.apple.copresence.conversationmanagerhost")
+									(global-name "com.apple.matter.framework.xpc")
+									(global-name "com.apple.matter.native.xpc")
 								)
-								(require-not (%entitlement-is-present "com.apple.developer.group-session"))
+								(require-not (%entitlement-is-present "com.apple.developer.homekit"))
 								(xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner")
 								(require-not (%entitlement-is-present "com.apple.shortcuts.background-running"))
 								(require-not (%entitlement-is-present "com.apple.siri.VoiceShortcuts.xpc"))

 							)
 							(require-all
 								(require-any
-									(global-name "com.apple.cloudasset.cloudd")
-									(global-name "com.apple.copresence.conversationmanagerhost")
+									(global-name "com.apple.matter.framework.xpc")
+									(global-name "com.apple.matter.native.xpc")
 								)
-								(require-not (%entitlement-is-present "com.apple.developer.group-session"))
+								(require-not (%entitlement-is-present "com.apple.developer.homekit"))
 								(xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner")
 								(require-not (%entitlement-is-present "com.apple.shortcuts.background-running"))
 								(require-not (%entitlement-is-present "com.apple.siri.VoiceShortcuts.xpc"))

 	)
 )
 
+(allow necp-client-open
+	(require-not (process-attribute is-sandboxed))
+)
+
 (allow network*
 	(require-not (process-attribute is-sandboxed))
 )
 
-(allow nvram-delete
+(allow nvram*
 	(require-all
 		(nvram-variable "srd-prov*")
 		(require-not (system-attribute restore-os))

 	)
 )
 
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "srd-prov*")
 		(require-any

 	)
 )
 
-(allow nvram-set
+(define (_g0 _)
 	(require-all
-		(nvram-variable "srd-prov*")
-		(require-not (system-attribute restore-os))
-		(require-not (system-attribute recovery-os))
-		(require-not (system-attribute security-research-device-extended-research-mode))
+	(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging/exec")
+	(signing-identifier "com.apple.xpc.proxy")
+	(require-not (process-path "/private/var/db/com.apple.xpc.roleaccountd.staging/exec/"))
+	(require-not (process-attribute is-initproc))
+	(require-not (require-any
+		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
+		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
+		(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
+	))
+	(require-not (subpath "/private/var"))
+))
+(define (_g1 _)
+	(require-any
+	(_g0 "")
+	(require-all
+		(subpath "/Applications")
+		(signing-identifier "com.apple.xpc.proxy")
+		(require-not (require-any
+			(literal ".app/[^/]")
+			(regex #".app/([^/])+")
+		))
+		(require-not (require-any
+			(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
+			(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
+			(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
+		))
+		(require-not (subpath "/private/var"))
 	)
+))
+(define (_g2 _)
+	(require-all
+	(require-not (require-any
+		(subpath "/Developer")
+		(subpath "/System/Developer")
+		(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
+		(subpath "/private/var/containers/Bundle")
+		(subpath "/private/var/factory_mount")
+		(subpath "/private/var/personalized_automation")
+		(subpath "/private/var/personalized_debug")
+		(subpath "/private/var/personalized_demo")
+		(subpath "/private/var/personalized_factory")
+		(subpath "/private/var/personalized_quality")
+		(subpath "/private/var/personalized_repair")
+		(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
+	))
+	(require-any
+		(_g0 "")
+		(require-all
+			(%entitlement-is-bool-true "com.apple.private.security.storage.driverkitd")
+			(require-not (subpath "/private/var/db/driverkitd"))
+			(vnode-type REGULAR-FILE)
+			(_g1 "")
+		)
+		(require-all
+			(require-any
+				(signing-identifier "com.apple.AskPermissionUI")
+				(signing-identifier "com.apple.Diagnostics.Canary")
+				(signing-identifier "com.apple.Home.HomeUIService")
+				(signing-identifier "com.apple.MusicUIService")
+				(signing-identifier "com.apple.PhotosViewService")
+				(signing-identifier "com.apple.SharedWebCredentialViewService")
+				(signing-identifier "com.apple.SharingViewService")
+				(signing-identifier "com.apple.TapToRadar")
+				(signing-identifier "com.apple.TrustMe")
+				(signing-identifier "com.apple.family")
+				(signing-identifier "com.apple.fieldtest")
+				(signing-identifier "com.apple.mobilesms.compose")
+				(signing-identifier "com.apple.mobiletimer")
+				(signing-identifier "com.apple.social.SLGoogleAuth")
+				(signing-identifier "com.apple.social.SLYahooAuth")
+				(signing-identifier "com.apple.susuiservice")
+			)
+			(require-not (subpath "/Applications"))
+			(%entitlement-is-bool-true "com.apple.private.security.storage.driverkitd")
+			(require-not (subpath "/private/var/db/driverkitd"))
+			(vnode-type REGULAR-FILE)
+			(_g1 "")
+		)
+		(require-all
+			(require-any
+				(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
+				(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
+			)
+			(signing-identifier "com.apple.xpc.proxy")
+			(require-not (process-attribute is-initproc))
+			(require-not (require-any
+				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
+				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
+				(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
+			))
+			(require-not (subpath "/private/var"))
+		)
+		(require-all
+			(require-not (require-any
+				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
+				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
+				(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
+			))
+			(require-not (subpath "/private/var"))
+		)
+		(require-all
+			(signing-identifier "com.apple.xpc.proxy")
+			(require-not (require-any
+				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
+				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
+				(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
+			))
+			(require-not (subpath "/private/var"))
+		)
+		(require-all
+			(subpath "/private/var/PersonaVolumes")
+			(require-not (regex #"^/private/var/PersonaVolumes/[^/]+(/|$)"))
+			(%entitlement-is-bool-true "com.apple.private.security.storage.driverkitd")
+			(require-not (subpath "/private/var/db/driverkitd"))
+			(vnode-type REGULAR-FILE)
+			(_g1 "")
+		)
+		(require-all
+			(vnode-type REGULAR-FILE)
+			(_g1 "")
+		)
+		(require-any
+			(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
+			(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging/exec")
+			(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
+		)
+	)
+))
+(define (_g3 _)
+	(require-any
+	(_g2 "")
+	(require-any
+		(subpath "/private/var/CipherMLAssets")
+		(subpath "/private/var/MLModels")
+	)
+))
+(define (_g4 _)
+	(require-all
+	(signing-identifier "com.apple.logd_helper")
+	(system-attribute darwin-os)
+	(require-not (require-any
+		(subpath "/private/var/BMCSupport")
+		(subpath "/private/var/BMCSupportInternalAdditions")
+		(subpath "/private/var/DarwinDataCenterSupportImage")
+		(subpath "/private/var/ServerRestoreSupport")
+	))
+	(system-attribute private-cloud-os)
+	(require-not (require-any
+		(subpath "/private/var/DarwinDataCenterSupportImage")
+		(subpath "/private/var/PCCApps")
+		(subpath "/private/var/PrivateCloudSupport")
+		(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+	))
+	(_g3 "")
+))
+(define (_g5 _)
+	(require-all
+	(system-attribute darwin-os)
+	(require-not (require-any
+		(subpath "/private/var/BMCSupport")
+		(subpath "/private/var/BMCSupportInternalAdditions")
+		(subpath "/private/var/DarwinDataCenterSupportImage")
+		(subpath "/private/var/ServerRestoreSupport")
+	))
+	(system-attribute private-cloud-os)
+	(require-not (require-any
+		(subpath "/private/var/DarwinDataCenterSupportImage")
+		(subpath "/private/var/PCCApps")
+		(subpath "/private/var/PrivateCloudSupport")
+		(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+	))
+	(_g3 "")
+))
+(define (_g6 _)
+	(require-any
+	(_g4 "")
+	(_g5 "")
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.erm.supplemental")
+		(system-attribute darwin-os)
+		(require-not (require-any
+			(subpath "/private/var/BMCSupport")
+			(subpath "/private/var/BMCSupportInternalAdditions")
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/ServerRestoreSupport")
+		))
+		(system-attribute private-cloud-os)
+		(require-not (require-any
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/PCCApps")
+			(subpath "/private/var/PrivateCloudSupport")
+			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+		))
+		(_g3 "")
+	)
+	(require-all
+		(process-attribute is-initproc)
+		(system-attribute darwin-os)
+		(require-not (require-any
+			(subpath "/private/var/BMCSupport")
+			(subpath "/private/var/BMCSupportInternalAdditions")
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/ServerRestoreSupport")
+		))
+		(system-attribute private-cloud-os)
+		(require-not (require-any
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/PCCApps")
+			(subpath "/private/var/PrivateCloudSupport")
+			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+		))
+		(_g3 "")
+	)
+	(require-all
+		(subpath "/private/preboot/Cryptexes/Supplemental")
+		(process-path "/private/preboot/Cryptexes/Supplemental/")
+		(system-attribute darwin-os)
+		(require-not (require-any
+			(subpath "/private/var/BMCSupport")
+			(subpath "/private/var/BMCSupportInternalAdditions")
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/ServerRestoreSupport")
+		))
+		(system-attribute private-cloud-os)
+		(require-not (require-any
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/PCCApps")
+			(subpath "/private/var/PrivateCloudSupport")
+			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+		))
+		(_g3 "")
+	)
+	(require-all
+		(system-attribute internal-build)
+		(require-any
+			(_g4 "")
+			(require-all
+				(process-attribute is-datavault-controller)
+				(system-attribute darwin-os)
+				(require-not (require-any
+					(subpath "/private/var/BMCSupport")
+					(subpath "/private/var/BMCSupportInternalAdditions")
+					(subpath "/private/var/DarwinDataCenterSupportImage")
+					(subpath "/private/var/ServerRestoreSupport")
+				))
+				(system-attribute private-cloud-os)
+				(require-not (require-any
+					(subpath "/private/var/DarwinDataCenterSupportImage")
+					(subpath "/private/var/PCCApps")
+					(subpath "/private/var/PrivateCloudSupport")
+					(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+				))
+				(_g3 "")
+			)
+		)
+	)
+))
+(define (_g7 _)
+	(require-all
+	(require-any
+		(subpath "/Applications")
+		(subpath "/Developer")
+		(subpath "/System")
+		(subpath "/bin")
+		(subpath "/private/preboot/Cryptexes/App")
+		(subpath "/private/preboot/Cryptexes/OS")
+		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
+		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
+		(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
+		(subpath "/private/var/containers/Bundle")
+		(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging/exec")
+		(subpath "/private/var/db/driverkitd")
+		(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
+		(subpath "/sbin")
+		(subpath "/usr/bin")
+		(subpath "/usr/libexec")
+		(subpath "/usr/sbin")
+	)
+	(system-attribute darwin-os)
+	(require-not (require-any
+		(subpath "/private/var/BMCSupport")
+		(subpath "/private/var/BMCSupportInternalAdditions")
+		(subpath "/private/var/DarwinDataCenterSupportImage")
+		(subpath "/private/var/ServerRestoreSupport")
+	))
+	(system-attribute private-cloud-os)
+	(require-not (require-any
+		(subpath "/private/var/DarwinDataCenterSupportImage")
+		(subpath "/private/var/PCCApps")
+		(subpath "/private/var/PrivateCloudSupport")
+		(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+	))
+	(_g3 "")
+))
+(define (_g8 _)
+	(require-all
+	(literal "${ANY_USER_HOME}/Library/perfExtra.sh")
+	(require-any
+		(subpath "/private/preboot/Cryptexes/Supplemental")
+		(subpath "/private/var/PTSupport")
+		(subpath "/private/var/RPSupport")
+	)
+	(require-not (system-attribute security-research-device-extended-research-mode))
+	(_g6 "")
+))
+(define (_g9 _)
+	(require-any
+	(_g2 "")
+	(_g5 "")
+	(_g7 "")
+	(_g8 "")
+	(require-all
+		(process-path "/usr/libexec/xpcproxy")
+		(require-any
+			(_g8 "")
+			(require-all
+				(subpath "/private/preboot/Cryptexes/Supplemental")
+				(require-not (system-attribute security-research-device-extended-research-mode))
+				(_g6 "")
+			)
+			(require-all
+				(subpath "/private/var/MobileSoftwareUpdate")
+				(system-attribute darwin-os)
+				(require-not (require-any
+					(subpath "/private/var/BMCSupport")
+					(subpath "/private/var/BMCSupportInternalAdditions")
+					(subpath "/private/var/DarwinDataCenterSupportImage")
+					(subpath "/private/var/ServerRestoreSupport")
+				))
+				(system-attribute private-cloud-os)
+				(require-not (require-any
+					(subpath "/private/var/DarwinDataCenterSupportImage")
+					(subpath "/private/var/PCCApps")
+					(subpath "/private/var/PrivateCloudSupport")
+					(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+				))
+				(_g3 "")
+			)
+			(require-all
+				(subpath "/private/var/RPSupport")
+				(require-not (system-attribute security-research-device-extended-research-mode))
+				(_g6 "")
+			)
+			(require-all
+				(subpath "/private/var/personalized_factory")
+				(system-attribute darwin-os)
+				(require-not (require-any
+					(subpath "/private/var/BMCSupport")
+					(subpath "/private/var/BMCSupportInternalAdditions")
+					(subpath "/private/var/DarwinDataCenterSupportImage")
+					(subpath "/private/var/ServerRestoreSupport")
+				))
+				(system-attribute private-cloud-os)
+				(require-not (require-any
+					(subpath "/private/var/DarwinDataCenterSupportImage")
+					(subpath "/private/var/PCCApps")
+					(subpath "/private/var/PrivateCloudSupport")
+					(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+				))
+				(_g3 "")
+			)
+		)
+	)
+	(require-all
+		(require-any
+			(process-path "/AppleInternal/")
+			(process-path "/System/AppleInternal*")
+			(process-path "/bin/bash")
+			(process-path "/bin/zsh")
+			(process-path "/usr/appleinternal/")
+			(process-path "/usr/bin/env")
+			(process-path "/usr/bin/login")
+			(process-path "/usr/bin/nohup")
+			(process-path "/usr/local/")
+		)
+		(require-any
+			(subpath "/private/preboot/Cryptexes/Supplemental")
+			(subpath "/private/var/PTSupport")
+			(subpath "/private/var/RPSupport")
+		)
+		(require-not (system-attribute security-research-device-extended-research-mode))
+		(_g6 "")
+	)
+	(require-all
+		(require-any
+			(subpath "/AppleInternal")
+			(subpath "/ERSupport")
+			(subpath "/Library/Python")
+			(subpath "/private/var/green-restore")
+			(subpath "/private/var/mobile")
+			(subpath "/private/var/root")
+			(subpath "/private/var/tmp")
+			(subpath "/usr/appleinternal")
+			(subpath "/usr/local")
+		)
+		(system-attribute darwin-os)
+		(require-not (require-any
+			(subpath "/private/var/BMCSupport")
+			(subpath "/private/var/BMCSupportInternalAdditions")
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/ServerRestoreSupport")
+		))
+		(system-attribute private-cloud-os)
+		(require-not (require-any
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/PCCApps")
+			(subpath "/private/var/PrivateCloudSupport")
+			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+		))
+		(_g3 "")
+	)
+	(require-all
+		(require-any
+			(subpath "/private/preboot/Cryptexes/Supplemental")
+			(subpath "/private/var/PTSupport")
+			(subpath "/private/var/RPSupport")
+		)
+		(require-not (system-attribute security-research-device-extended-research-mode))
+		(_g6 "")
+	)
+	(require-all
+		(system-attribute developer-mode)
+		(require-any
+			(_g7 "")
+			(require-all
+				(subpath "${ANY_USER_HOME}/XcodeBuiltProducts")
+				(require-any
+					(_g7 "")
+					(require-all
+						(require-any
+							(process-path "/System/Developer/usr/libexec/dtappserviced")
+							(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+							(process-path "/usr/libexec/xpcproxy")
+						)
+						(require-any
+							(subpath "/private/preboot/Cryptexes/Supplemental")
+							(subpath "/private/var/PTSupport")
+							(subpath "/private/var/RPSupport")
+						)
+						(require-not (system-attribute security-research-device-extended-research-mode))
+						(_g6 "")
+					)
+				)
+			)
+		)
+	)
+	(require-all
+		(system-attribute private-cloud-os)
+		(require-not (require-any
+			(subpath "/private/var/DarwinDataCenterSupportImage")
+			(subpath "/private/var/PCCApps")
+			(subpath "/private/var/PrivateCloudSupport")
+			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
+		))
+		(_g3 "")
+	)
+))
+(allow process-codesigning
+	(require-all
+	(require-not (%entitlement-is-bool-true "com.apple.private.security.no-container"))
+	(require-not (%entitlement-is-bool-true "com.apple.private.security.no-sandbox"))
+	(require-any
+		(require-all
+			(%entitlement-load "com.apple.private.security.container-required")
+			(require-not (%entitlement-boolean #f))
+			(require-not (%entitlement-boolean #t))
+			(require-not (%entitlement-string "*"))
+			(require-not (system-attribute restore-os))
+			(require-not (subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_GuardrailFramework"))
+			(_g9 "")
+		)
+		(require-all
+			(require-not (system-attribute restore-os))
+			(require-not (subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_GuardrailFramework"))
+			(_g9 "")
+		)
+	)
+)
+)
+(deny process-codesigning
+	(subpath "/[^/]+/SC_Info")
 )
 
 (define (_g0 _)

 )
 )
 (deny process-exec*
-	(subpath "/[^/]+/SC_Info")
-)
-
-(define (_g0 _)
-	(require-all
-	(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging/exec")
-	(signing-identifier "com.apple.xpc.proxy")
-	(require-not (process-path "/private/var/db/com.apple.xpc.roleaccountd.staging/exec/"))
-	(require-not (process-attribute is-initproc))
-	(require-not (require-any
-		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
-		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
-		(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
-	))
-	(require-not (subpath "/private/var"))
-))
-(define (_g1 _)
-	(require-any
-	(_g0 "")
-	(require-all
-		(subpath "/Applications")
-		(signing-identifier "com.apple.xpc.proxy")
-		(require-not (require-any
-			(literal ".app/[^/]")
-			(regex #".app/([^/])+")
-		))
-		(require-not (require-any
-			(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
-			(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
-			(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
-		))
-		(require-not (subpath "/private/var"))
-	)
-))
-(define (_g2 _)
-	(require-all
-	(require-not (require-any
-		(subpath "/Developer")
-		(subpath "/System/Developer")
-		(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
-		(subpath "/private/var/containers/Bundle")
-		(subpath "/private/var/factory_mount")
-		(subpath "/private/var/personalized_automation")
-		(subpath "/private/var/personalized_debug")
-		(subpath "/private/var/personalized_demo")
-		(subpath "/private/var/personalized_factory")
-		(subpath "/private/var/personalized_quality")
-		(subpath "/private/var/personalized_repair")
-		(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
-	))
-	(require-any
-		(_g0 "")
-		(require-all
-			(%entitlement-is-bool-true "com.apple.private.security.storage.driverkitd")
-			(require-not (subpath "/private/var/db/driverkitd"))
-			(vnode-type REGULAR-FILE)
-			(_g1 "")
-		)
-		(require-all
-			(require-any
-				(signing-identifier "com.apple.AskPermissionUI")
-				(signing-identifier "com.apple.Diagnostics.Canary")
-				(signing-identifier "com.apple.Home.HomeUIService")
-				(signing-identifier "com.apple.MusicUIService")
-				(signing-identifier "com.apple.PhotosViewService")
-				(signing-identifier "com.apple.SharedWebCredentialViewService")
-				(signing-identifier "com.apple.SharingViewService")
-				(signing-identifier "com.apple.TapToRadar")
-				(signing-identifier "com.apple.TrustMe")
-				(signing-identifier "com.apple.family")
-				(signing-identifier "com.apple.fieldtest")
-				(signing-identifier "com.apple.mobilesms.compose")
-				(signing-identifier "com.apple.mobiletimer")
-				(signing-identifier "com.apple.social.SLGoogleAuth")
-				(signing-identifier "com.apple.social.SLYahooAuth")
-				(signing-identifier "com.apple.susuiservice")
-			)
-			(require-not (subpath "/Applications"))
-			(%entitlement-is-bool-true "com.apple.private.security.storage.driverkitd")
-			(require-not (subpath "/private/var/db/driverkitd"))
-			(vnode-type REGULAR-FILE)
-			(_g1 "")
-		)
-		(require-all
-			(require-any
-				(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
-				(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
-			)
-			(signing-identifier "com.apple.xpc.proxy")
-			(require-not (process-attribute is-initproc))
-			(require-not (require-any
-				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
-				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
-				(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
-			))
-			(require-not (subpath "/private/var"))
-		)
-		(require-all
-			(require-not (require-any
-				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
-				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
-				(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
-			))
-			(require-not (subpath "/private/var"))
-		)
-		(require-all
-			(signing-identifier "com.apple.xpc.proxy")
-			(require-not (require-any
-				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
-				(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
-				(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging")
-			))
-			(require-not (subpath "/private/var"))
-		)
-		(require-all
-			(subpath "/private/var/PersonaVolumes")
-			(require-not (regex #"^/private/var/PersonaVolumes/[^/]+(/|$)"))
-			(%entitlement-is-bool-true "com.apple.private.security.storage.driverkitd")
-			(require-not (subpath "/private/var/db/driverkitd"))
-			(vnode-type REGULAR-FILE)
-			(_g1 "")
-		)
-		(require-all
-			(vnode-type REGULAR-FILE)
-			(_g1 "")
-		)
-		(require-any
-			(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
-			(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging/exec")
-			(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
-		)
-	)
-))
-(define (_g3 _)
-	(require-any
-	(_g2 "")
-	(require-any
-		(subpath "/private/var/CipherMLAssets")
-		(subpath "/private/var/MLModels")
-	)
-))
-(define (_g4 _)
-	(require-all
-	(signing-identifier "com.apple.logd_helper")
-	(system-attribute darwin-os)
-	(require-not (require-any
-		(subpath "/private/var/BMCSupport")
-		(subpath "/private/var/BMCSupportInternalAdditions")
-		(subpath "/private/var/DarwinDataCenterSupportImage")
-		(subpath "/private/var/ServerRestoreSupport")
-	))
-	(system-attribute private-cloud-os)
-	(require-not (require-any
-		(subpath "/private/var/DarwinDataCenterSupportImage")
-		(subpath "/private/var/PCCApps")
-		(subpath "/private/var/PrivateCloudSupport")
-		(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-	))
-	(_g3 "")
-))
-(define (_g5 _)
-	(require-all
-	(system-attribute darwin-os)
-	(require-not (require-any
-		(subpath "/private/var/BMCSupport")
-		(subpath "/private/var/BMCSupportInternalAdditions")
-		(subpath "/private/var/DarwinDataCenterSupportImage")
-		(subpath "/private/var/ServerRestoreSupport")
-	))
-	(system-attribute private-cloud-os)
-	(require-not (require-any
-		(subpath "/private/var/DarwinDataCenterSupportImage")
-		(subpath "/private/var/PCCApps")
-		(subpath "/private/var/PrivateCloudSupport")
-		(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-	))
-	(_g3 "")
-))
-(define (_g6 _)
-	(require-any
-	(_g4 "")
-	(_g5 "")
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.erm.supplemental")
-		(system-attribute darwin-os)
-		(require-not (require-any
-			(subpath "/private/var/BMCSupport")
-			(subpath "/private/var/BMCSupportInternalAdditions")
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/ServerRestoreSupport")
-		))
-		(system-attribute private-cloud-os)
-		(require-not (require-any
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/PCCApps")
-			(subpath "/private/var/PrivateCloudSupport")
-			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-		))
-		(_g3 "")
-	)
-	(require-all
-		(process-attribute is-initproc)
-		(system-attribute darwin-os)
-		(require-not (require-any
-			(subpath "/private/var/BMCSupport")
-			(subpath "/private/var/BMCSupportInternalAdditions")
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/ServerRestoreSupport")
-		))
-		(system-attribute private-cloud-os)
-		(require-not (require-any
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/PCCApps")
-			(subpath "/private/var/PrivateCloudSupport")
-			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-		))
-		(_g3 "")
-	)
-	(require-all
-		(subpath "/private/preboot/Cryptexes/Supplemental")
-		(process-path "/private/preboot/Cryptexes/Supplemental/")
-		(system-attribute darwin-os)
-		(require-not (require-any
-			(subpath "/private/var/BMCSupport")
-			(subpath "/private/var/BMCSupportInternalAdditions")
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/ServerRestoreSupport")
-		))
-		(system-attribute private-cloud-os)
-		(require-not (require-any
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/PCCApps")
-			(subpath "/private/var/PrivateCloudSupport")
-			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-		))
-		(_g3 "")
-	)
-	(require-all
-		(system-attribute internal-build)
-		(require-any
-			(_g4 "")
-			(require-all
-				(process-attribute is-datavault-controller)
-				(system-attribute darwin-os)
-				(require-not (require-any
-					(subpath "/private/var/BMCSupport")
-					(subpath "/private/var/BMCSupportInternalAdditions")
-					(subpath "/private/var/DarwinDataCenterSupportImage")
-					(subpath "/private/var/ServerRestoreSupport")
-				))
-				(system-attribute private-cloud-os)
-				(require-not (require-any
-					(subpath "/private/var/DarwinDataCenterSupportImage")
-					(subpath "/private/var/PCCApps")
-					(subpath "/private/var/PrivateCloudSupport")
-					(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-				))
-				(_g3 "")
-			)
-		)
-	)
-))
-(define (_g7 _)
-	(require-all
-	(require-any
-		(subpath "/Applications")
-		(subpath "/Developer")
-		(subpath "/System")
-		(subpath "/bin")
-		(subpath "/private/preboot/Cryptexes/App")
-		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2")
-		(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/MobileAssetBrain")
-		(subpath "/private/var/boot/com.apple.security.cryptexd/mnt")
-		(subpath "/private/var/containers/Bundle")
-		(subpath "/private/var/db/com.apple.xpc.roleaccountd.staging/exec")
-		(subpath "/private/var/db/driverkitd")
-		(subpath "/private/var/run/com.apple.security.cryptexd/mnt")
-		(subpath "/sbin")
-		(subpath "/usr/bin")
-		(subpath "/usr/libexec")
-		(subpath "/usr/sbin")
-	)
-	(system-attribute darwin-os)
-	(require-not (require-any
-		(subpath "/private/var/BMCSupport")
-		(subpath "/private/var/BMCSupportInternalAdditions")
-		(subpath "/private/var/DarwinDataCenterSupportImage")
-		(subpath "/private/var/ServerRestoreSupport")
-	))
-	(system-attribute private-cloud-os)
-	(require-not (require-any
-		(subpath "/private/var/DarwinDataCenterSupportImage")
-		(subpath "/private/var/PCCApps")
-		(subpath "/private/var/PrivateCloudSupport")
-		(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-	))
-	(_g3 "")
-))
-(define (_g8 _)
-	(require-all
-	(literal "${ANY_USER_HOME}/Library/perfExtra.sh")
-	(require-any
-		(subpath "/private/preboot/Cryptexes/Supplemental")
-		(subpath "/private/var/PTSupport")
-		(subpath "/private/var/RPSupport")
-	)
-	(require-not (system-attribute security-research-device-extended-research-mode))
-	(_g6 "")
-))
-(define (_g9 _)
-	(require-any
-	(_g2 "")
-	(_g5 "")
-	(_g7 "")
-	(_g8 "")
-	(require-all
-		(process-path "/usr/libexec/xpcproxy")
-		(require-any
-			(_g8 "")
-			(require-all
-				(subpath "/private/preboot/Cryptexes/Supplemental")
-				(require-not (system-attribute security-research-device-extended-research-mode))
-				(_g6 "")
-			)
-			(require-all
-				(subpath "/private/var/MobileSoftwareUpdate")
-				(system-attribute darwin-os)
-				(require-not (require-any
-					(subpath "/private/var/BMCSupport")
-					(subpath "/private/var/BMCSupportInternalAdditions")
-					(subpath "/private/var/DarwinDataCenterSupportImage")
-					(subpath "/private/var/ServerRestoreSupport")
-				))
-				(system-attribute private-cloud-os)
-				(require-not (require-any
-					(subpath "/private/var/DarwinDataCenterSupportImage")
-					(subpath "/private/var/PCCApps")
-					(subpath "/private/var/PrivateCloudSupport")
-					(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-				))
-				(_g3 "")
-			)
-			(require-all
-				(subpath "/private/var/RPSupport")
-				(require-not (system-attribute security-research-device-extended-research-mode))
-				(_g6 "")
-			)
-			(require-all
-				(subpath "/private/var/personalized_factory")
-				(system-attribute darwin-os)
-				(require-not (require-any
-					(subpath "/private/var/BMCSupport")
-					(subpath "/private/var/BMCSupportInternalAdditions")
-					(subpath "/private/var/DarwinDataCenterSupportImage")
-					(subpath "/private/var/ServerRestoreSupport")
-				))
-				(system-attribute private-cloud-os)
-				(require-not (require-any
-					(subpath "/private/var/DarwinDataCenterSupportImage")
-					(subpath "/private/var/PCCApps")
-					(subpath "/private/var/PrivateCloudSupport")
-					(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-				))
-				(_g3 "")
-			)
-		)
-	)
-	(require-all
-		(require-any
-			(process-path "/AppleInternal/")
-			(process-path "/System/AppleInternal*")
-			(process-path "/bin/bash")
-			(process-path "/bin/zsh")
-			(process-path "/usr/appleinternal/")
-			(process-path "/usr/bin/env")
-			(process-path "/usr/bin/login")
-			(process-path "/usr/bin/nohup")
-			(process-path "/usr/local/")
-		)
-		(require-any
-			(subpath "/private/preboot/Cryptexes/Supplemental")
-			(subpath "/private/var/PTSupport")
-			(subpath "/private/var/RPSupport")
-		)
-		(require-not (system-attribute security-research-device-extended-research-mode))
-		(_g6 "")
-	)
-	(require-all
-		(require-any
-			(subpath "/AppleInternal")
-			(subpath "/ERSupport")
-			(subpath "/Library/Python")
-			(subpath "/private/var/green-restore")
-			(subpath "/private/var/mobile")
-			(subpath "/private/var/root")
-			(subpath "/private/var/tmp")
-			(subpath "/usr/appleinternal")
-			(subpath "/usr/local")
-		)
-		(system-attribute darwin-os)
-		(require-not (require-any
-			(subpath "/private/var/BMCSupport")
-			(subpath "/private/var/BMCSupportInternalAdditions")
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/ServerRestoreSupport")
-		))
-		(system-attribute private-cloud-os)
-		(require-not (require-any
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/PCCApps")
-			(subpath "/private/var/PrivateCloudSupport")
-			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-		))
-		(_g3 "")
-	)
-	(require-all
-		(require-any
-			(subpath "/private/preboot/Cryptexes/Supplemental")
-			(subpath "/private/var/PTSupport")
-			(subpath "/private/var/RPSupport")
-		)
-		(require-not (system-attribute security-research-device-extended-research-mode))
-		(_g6 "")
-	)
-	(require-all
-		(system-attribute developer-mode)
-		(require-any
-			(_g7 "")
-			(require-all
-				(subpath "${ANY_USER_HOME}/XcodeBuiltProducts")
-				(require-any
-					(_g7 "")
-					(require-all
-						(require-any
-							(process-path "/System/Developer/usr/libexec/dtappserviced")
-							(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
-							(process-path "/usr/libexec/xpcproxy")
-						)
-						(require-any
-							(subpath "/private/preboot/Cryptexes/Supplemental")
-							(subpath "/private/var/PTSupport")
-							(subpath "/private/var/RPSupport")
-						)
-						(require-not (system-attribute security-research-device-extended-research-mode))
-						(_g6 "")
-					)
-				)
-			)
-		)
-	)
-	(require-all
-		(system-attribute private-cloud-os)
-		(require-not (require-any
-			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/PCCApps")
-			(subpath "/private/var/PrivateCloudSupport")
-			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
-		))
-		(_g3 "")
-	)
-))
-(allow process-exec-interpreter
-	(require-all
-	(require-not (%entitlement-is-bool-true "com.apple.private.security.no-container"))
-	(require-not (%entitlement-is-bool-true "com.apple.private.security.no-sandbox"))
-	(require-any
-		(require-all
-			(%entitlement-load "com.apple.private.security.container-required")
-			(require-not (%entitlement-boolean #f))
-			(require-not (%entitlement-boolean #t))
-			(require-not (%entitlement-string "*"))
-			(require-not (system-attribute restore-os))
-			(require-not (subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_GuardrailFramework"))
-			(_g9 "")
-		)
-		(require-all
-			(require-not (system-attribute restore-os))
-			(require-not (subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_GuardrailFramework"))
-			(_g9 "")
-		)
-	)
-)
-)
-(deny process-exec-interpreter
 	(require-any
 	(require-not (system-attribute internal-build))
 	(subpath "/[^/]+/SC_Info")
 )
 )
 
-(allow pseudo-tty
+(allow process-legacy-codesigning-text-offset-get
 	(require-not (process-attribute is-sandboxed))
 )
 

 	(with assign-storage-class "Lockdown")
 	(subpath "/private/var/root/Library/Lockdown")
 )
+(allow storage-class-map
+	(with assign-storage-class "LogdPreferencesCache")
+	(subpath "/private/var/db/diagnostics/logd")
+)
 (allow storage-class-map
 	(with assign-storage-class "Mail")
 	(subpath "${FRONT_USER_HOME}/Library/Mail")
```
