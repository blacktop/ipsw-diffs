## appconduitd

> Group: ⬆️ Updated

```diff

 
 (allow file-graft)
 
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.executable")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.StreamingUnzipService")

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.executable")
+	)
+)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))

 		(subpath "/private/var/personalized_debug/Applications")
 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 		(subpath "/private/var/tmp")
+		(subpath "/private/var/tmp/com.apple.AppConduit.staging")
 	)
 )
 (deny file-read*

 		(subpath "/private/var/personalized_debug/Applications")
 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 		(subpath "/private/var/tmp")
+		(subpath "/private/var/tmp/com.apple.AppConduit.staging")
 	)
 )
 (deny file-read-metadata

 (allow file-write*
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"((((^/private/var/(mobile|euser[0-9]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/((com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd)|com\.apple\.sockpuppet\.activeComplications)|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/AppConduit($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"((((^/private/var/(mobile|euser[0-9]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/((com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd)|com\.apple\.sockpuppet\.activeComplications)|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/AppConduit($|/)")
+					(subpath "/private/var/tmp")
+				)
+			)
+			(subpath "/private/var/tmp")
 		)
 	)
 )

 		(subpath "${HOME}/Library/Logs/AirTraffic")
 		(subpath "${HOME}/Library/Logs/AppConduit")
 		(subpath "${PROCESS_TEMP_DIR}")
-		(subpath "/private/var/tmp")
+		(subpath "/private/var/tmp/com.apple.AppConduit.staging")
 	)
 )
 
 (allow file-write-create
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"((((^/private/var/(mobile|euser[0-9]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/((com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd)|com\.apple\.sockpuppet\.activeComplications)|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/AppConduit($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"((((^/private/var/(mobile|euser[0-9]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/((com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd)|com\.apple\.sockpuppet\.activeComplications)|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/AppConduit($|/)")
+					(subpath "/private/var/tmp")
+				)
+			)
+			(subpath "/private/var/tmp")
 		)
 	)
 )

 		(subpath "${HOME}/Library/Logs/AirTraffic")
 		(subpath "${HOME}/Library/Logs/AppConduit")
 		(subpath "${PROCESS_TEMP_DIR}")
-		(subpath "/private/var/tmp")
+		(subpath "/private/var/tmp/com.apple.AppConduit.staging")
 	)
 )
 (deny file-write-create

 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"((((^/private/var/(mobile|euser[0-9]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/((com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd)|com\.apple\.sockpuppet\.activeComplications)|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/AppConduit($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"((((^/private/var/(mobile|euser[0-9]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/((com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd)|com\.apple\.sockpuppet\.activeComplications)|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/[-0-9A-F]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.appconduitd\.gizmostate|com\.apple\.companionappd))|^/private/var/Users/[^/]+/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.sockpuppet\.activeComplications)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/AppConduit($|/)")
+					(subpath "/private/var/tmp")
+				)
+			)
+			(subpath "/private/var/tmp")
 		)
 	)
 )

 		(subpath "${HOME}/Library/Logs/AirTraffic")
 		(subpath "${HOME}/Library/Logs/AppConduit")
 		(subpath "${PROCESS_TEMP_DIR}")
-		(subpath "/private/var/tmp")
+		(subpath "/private/var/tmp/com.apple.AppConduit.staging")
 	)
 )
 
```
