## locationd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.locationd")
-			(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
-			(subpath "${HOME}/Library/Caches/com.apple.pipelined")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.locationd")
+			(subpath "/private/var/tmp/com.apple.locationd")
 		)
 	)
 )

 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.locationd")
-			(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
-			(subpath "${HOME}/Library/Caches/com.apple.pipelined")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.locationd")
-			(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
-			(subpath "${HOME}/Library/Caches/com.apple.pipelined")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.locationd")
+			(subpath "/private/var/tmp/com.apple.locationd")
 		)
 	)
 )

 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.locationd")
-			(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
-			(subpath "${HOME}/Library/Caches/com.apple.pipelined")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.locationd")
+			(subpath "/private/var/tmp/com.apple.locationd")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.locationd")
+			(subpath "/private/var/tmp/com.apple.locationd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(extension "com.apple.sandbox.container")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.sandbox.container")
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				)
-			)
 			(require-any
 				(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.locationd")
 				(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.sandbox.container")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.quicklook.readonly")
-		(extension "com.apple.sandbox.container")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.quicklook.readonly")
 		(require-any
 			(extension "com.apple.sandbox.container")
 			(require-all

 					(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 					(subpath "${HOME}/Library/Caches/com.apple.pipelined")
 				)
-				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+				)
 			)
 		)
 	)

 (allow file-read*
 	(require-any
 		(extension "com.apple.sandbox.container")
+		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PayloadManifest.plist")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")
 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")

 		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")

 (allow file-read-data
 	(require-any
 		(extension "com.apple.sandbox.container")
+		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PayloadManifest.plist")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")
 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")

 		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")

 	(require-any
 		(extension "com.apple.sandbox.container")
 		(literal "${FRONT_USER_HOME}/Library/Caches")
+		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PayloadManifest.plist")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${HOME}")

 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")

 (allow file-read-xattr
 	(require-any
 		(extension "com.apple.sandbox.container")
+		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PayloadManifest.plist")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")
 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")

 		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.locationd*")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/raven")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.locationd*")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadManifest.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")

 		(subpath "${FRONT_USER_HOME}/Library/Caches/locationd")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/vision")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/pipelined")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/raven")
 		(subpath "${FRONT_USER_HOME}/Library/locationd")
 		(subpath "${HOME}/Library/Caches/com.apple.pipelined")
```
