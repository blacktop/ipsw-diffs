## com.apple.tccd

> Group: ⬆️ Updated

```diff

 (allow file-write*
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+					(subpath "/private/var/tmp/com.apple.tccd")
+				)
+			)
+			(subpath "/private/var/tmp/com.apple.tccd")
 		)
 	)
 )

 		(literal "${HOME}/Library/Logs/awd/awd-tccd.log*")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		(subpath "${HOME}/Library/ManagedAppPrivacy")
 		(subpath "${HOME}/Library/TCC")
 		(subpath "/private/var/mobile/tmp/com.apple.tccd")
-		(subpath "/private/var/tmp/com.apple.tccd")
 	)
 )
 
 (allow file-write-create
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+					(subpath "/private/var/tmp/com.apple.tccd")
+				)
+			)
+			(subpath "/private/var/tmp/com.apple.tccd")
 		)
 	)
 )

 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
 			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
-			(literal "${HOME}/Library/Logs/awd")
 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any

 				(subpath "${FRONT_USER_HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 			)
+			(subpath "${HOME}/Library")
 		)
 	)
 )

 		(literal "${HOME}/Library/Logs/awd/awd-tccd.log*")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		(subpath "${HOME}/Library/ManagedAppPrivacy")
 		(subpath "${HOME}/Library/TCC")
 		(subpath "/private/var/mobile/tmp/com.apple.tccd")
-		(subpath "/private/var/tmp/com.apple.tccd")
 	)
 )
 
 (allow file-write-mode
 	(require-all
 		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 		(subpath "${FRONT_USER_HOME}")
-		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
-		)
 	)
 )
 (allow file-write-mode

 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
 					(subpath "/private/var/tmp/com.apple.tccd")
 				)
 			)

 		(literal "${HOME}/Library/Logs/awd/awd-tccd.log*")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		(subpath "${HOME}/Library/ManagedAppPrivacy")
 		(subpath "${HOME}/Library/TCC")
 		(subpath "/private/var/mobile/tmp/com.apple.tccd")
 	)

 (allow file-write-owner
 	(require-all
 		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 		(subpath "${FRONT_USER_HOME}")
-		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
-		)
 	)
 )
 (allow file-write-owner

 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
 					(subpath "/private/var/tmp/com.apple.tccd")
 				)
 			)

 		(literal "${HOME}/Library/Logs/awd/awd-tccd.log*")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		(subpath "${HOME}/Library/ManagedAppPrivacy")
 		(subpath "${HOME}/Library/TCC")
 		(subpath "/private/var/mobile/tmp/com.apple.tccd")
 	)

 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+					(subpath "/private/var/tmp/com.apple.tccd")
+				)
+			)
+			(subpath "/private/var/tmp/com.apple.tccd")
 		)
 	)
 )

 		(literal "${HOME}/Library/Logs/awd/awd-tccd.log*")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		(subpath "${HOME}/Library/ManagedAppPrivacy")
 		(subpath "${HOME}/Library/TCC")
 		(subpath "/private/var/mobile/tmp/com.apple.tccd")
-		(subpath "/private/var/tmp/com.apple.tccd")
 	)
 )
 

 (allow file-write-xattr
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.tccd\.sync")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.tccd($|/)")
+					(subpath "/private/var/tmp/com.apple.tccd")
+				)
+			)
+			(subpath "/private/var/tmp/com.apple.tccd")
 		)
 	)
 )

 		(literal "${HOME}/Library/Logs/awd/awd-tccd.log*")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		(subpath "${HOME}/Library/ManagedAppPrivacy")
 		(subpath "${HOME}/Library/TCC")
 		(subpath "/private/var/mobile/tmp/com.apple.tccd")
-		(subpath "/private/var/tmp/com.apple.tccd")
 	)
 )
 
```
