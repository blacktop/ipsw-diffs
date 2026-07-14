## platform

> Group: ⬆️ Updated

```diff

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
 				(require-not (process-attribute is-initproc))

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
 				(require-not (process-attribute is-initproc))

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
+							(_g33 "")
+							(require-all
+								(process-attribute is-initproc)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g32 "")
+							)
+							(require-all
+								(process-attribute is-installer)
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g32 "")
+							)
+							(require-all
+								(signing-identifier "com.apple.logd")
+								(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+								(require-not (subpath "/private/var/db/sysdiagnose"))
+								(storage-class "sysdiagnose.sysdiagnose")
+								(_g32 "")
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
+						(_g35 "")
+						(require-all
+							(process-attribute is-initproc)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g34 "")
+						)
+						(require-all
+							(process-attribute is-installer)
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g34 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.logd")
+							(%entitlement-is-bool-true "com.apple.private.security.storage.sysdiagnose")
+							(require-not (subpath "/private/var/db/sysdiagnose"))
+							(storage-class "sysdiagnose.sysdiagnose")
+							(_g34 "")
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
 				(require-not (process-attribute is-initproc))

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
