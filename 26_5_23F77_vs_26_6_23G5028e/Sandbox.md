## Sandbox Profiles

### Collection

#### Changed (25)

##### IMDPersistenceAgent

```diff

 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/PassKit")
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute carrier-build)

 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 		(literal "${HOME}/Library/PPTDevice")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${HOME}/Library/Caches")
 		(literal "${HOME}/Library/PPTDevice")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
```

##### IMTranscoderAgent

```diff

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "${HOME}/Library/Caches/Checkpoint.plist")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${HOME}/Library/Caches/Checkpoint.plist")
 		(literal "${HOME}/Library/PPTDevice")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
```

##### IMTransferAgent

```diff

 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "${HOME}/Library/Caches/.com.apple.persistentconnection.settings.lock.lock")
 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")

 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")
 		(literal "${HOME}/Library/PPTDevice")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
```

##### MobileSlideShow

```diff

 				(global-name "com.apple.SafetyKit")
 				(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 			)
-			(require-all
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-					(xpc-service-name "com.apple.ImageIOXPCService")
-				)
-			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 				(global-name "com.apple.SafetyKit")
 				(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 			)
-			(require-all
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-					(xpc-service-name "com.apple.ImageIOXPCService")
-				)
-			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 				(global-name "com.apple.SafetyKit")
 				(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 			)
-			(require-all
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-					(xpc-service-name "com.apple.ImageIOXPCService")
-				)
-			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")
```

##### app-extension-enhanced-security

```diff

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(literal "/private/etc/hosts")
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")
 				)
 			)
-			(require-any
+			(require-all
 				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
 				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
 			)
 			(require-any
 				(literal "/private/etc/group")

 							(literal "/dev/random")
 							(literal "/dev/urandom")
 							(literal "/dev/zero")
-							(literal "/private")
 							(literal "/private/etc/fstab")
 							(literal "/private/etc/hosts")
 							(literal "/private/etc/passwd")

 							(require-all
 								(file-mode #o0004)
 								(require-any
+									(literal "/private/etc/hosts")
 									(subpath "/System")
 									(subpath "/private/var/db/timezone")
 									(subpath "/usr/lib")
 									(subpath "/usr/share")
 								)
 							)
-							(require-any
+							(require-all
 								(literal "/System")
+								(process-attribute is-apple-signed-executable)
+							)
+							(require-all
+								(literal "/private")
+								(process-attribute is-apple-signed-executable)
+							)
+							(require-all
 								(literal "/private/preboot")
+								(process-attribute is-apple-signed-executable)
 							)
 							(require-any
 								(literal "/private/etc/group")

 					(literal "/dev/random")
 					(literal "/dev/urandom")
 					(literal "/dev/zero")
-					(literal "/private")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
+							(literal "/private/etc/hosts")
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")
 							(subpath "/usr/share")
 						)
 					)
-					(require-any
+					(require-all
 						(literal "/System")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
 						(literal "/private/preboot")
+						(process-attribute is-apple-signed-executable)
 					)
 					(require-any
 						(literal "/private/etc/group")

 
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### apple-cloud-enhanced-security

```diff

 		(extension "com.apple.app-sandbox.read")
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read*
 	(require-all
 		(file-mode #o0004)

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read*
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.coremedia.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.corevideo.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/kCFPreferencesAnyApplication.plist")
-		(literal "/System")
 		(literal "/dev/null")
 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
 		(literal "/private/etc/fstab")
 		(literal "/private/etc/group")
 		(literal "/private/etc/hosts")
 		(literal "/private/etc/passwd")
 		(literal "/private/etc/protocols")
 		(literal "/private/etc/services")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")

 		(extension "com.apple.app-sandbox.read")
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "/")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read-data
 	(require-all
 		(file-mode #o0004)

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read-data
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.coremedia.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.corevideo.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/kCFPreferencesAnyApplication.plist")
-		(literal "/System")
 		(literal "/dev/null")
 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
 		(literal "/private/etc/fstab")
 		(literal "/private/etc/group")
 		(literal "/private/etc/hosts")
 		(literal "/private/etc/passwd")
 		(literal "/private/etc/protocols")
 		(literal "/private/etc/services")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")

 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.cloudos.cb_bridged")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.logd.events")

 (deny mach-lookup
 	(require-any
 		(global-name "com.apple.CARenderServer")
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.audio.AudioComponentRegistrar")
 		(global-name "com.apple.coremedia.mediaparserd.utilities")
 		(global-name "com.apple.mobileassetd.v2")
```

##### baseline

```diff

 )
 (allow file-read*
 	(require-all
-		(literal "/dev/null")
+		(literal "/dev/dtracehelper")
 		(profile-flag "common-device-access")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(literal "/dev/zero")
-		(profile-flag "common-device-access")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
 	)
 )
 (allow file-read*

 			(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
 			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 			(require-all
+				(literal "/private/etc/master.passwd")
 				(uid 0)
-				(require-any
-					(literal "/private/etc/master.passwd")
-					(subpath "/private/var/preferences/Logging")
-				)
 			)
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.bin")

 )
 (allow file-read*
 	(require-all
-		(literal "/dev/dtracehelper")
+		(literal "/dev/zero")
 		(profile-flag "common-device-access")
 	)
 )

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "/dev/null")
+		(profile-flag "common-device-access")
+	)
+)
 (allow file-read*
 	(require-all
 		(profile-flag "common-device-access")

 )
 (allow file-read*
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(profile-flag "telemetry-for-transitd")

 			(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
 			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 			(require-all
+				(literal "/private/etc/master.passwd")
 				(uid 0)
-				(require-any
-					(literal "/private/etc/master.passwd")
-					(subpath "/private/var/preferences/Logging")
-				)
 			)
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.bin")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(profile-flag "common-system-logging-rules")
+		(literal "/private/var/run/syslog")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(profile-flag "common-rules")

 )
 (allow file-read-metadata
 	(require-all
-		(profile-flag "common-system-logging-rules")
-		(literal "/private/var/run/syslog")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(profile-flag "telemetry-for-transitd")

 	(with report)
 	(profile-flag "disable-enforcement")
 )
+(allow file-test-existence
+	(require-all
+		(extension "com.apple.security.exception.files.absolute-path.read-only")
+		(profile-flag "common-exception-entitlement-rules")
+	)
+)
+(allow file-test-existence
+	(require-all
+		(extension "com.apple.security.exception.files.home-relative-path.read-only")
+		(profile-flag "common-exception-entitlement-rules")
+	)
+)
 (allow file-test-existence
 	(require-all
 		(profile-flag "common-debugging-rules")

 		)
 	)
 )
-(allow file-test-existence
-	(require-all
-		(extension "com.apple.security.exception.files.absolute-path.read-only")
-		(profile-flag "common-exception-entitlement-rules")
-	)
-)
-(allow file-test-existence
-	(require-all
-		(extension "com.apple.security.exception.files.home-relative-path.read-only")
-		(profile-flag "common-exception-entitlement-rules")
-	)
-)
 (allow file-test-existence
 	(require-all
 		(profile-flag "common-rules")

 									(require-all
 										(%entitlement-is-present "com.apple.security.system-group-containers")
 										(require-any
+											(require-all
+												(subpath "/")
+												(process-attribute is-apple-signed-executable)
+											)
 											(require-all
 												(subpath "/private/var/containers/Shared/SystemGroup")
 												(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")

 										(%entitlement-is-present "com.apple.security.system-groups")
 										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 									)
+									(require-all
+										(subpath "/")
+										(process-attribute is-apple-signed-executable)
+									)
 								)
 							)
 							(require-all

 											(require-all
 												(%entitlement-is-present "com.apple.security.system-group-containers")
 												(require-any
+													(require-all
+														(subpath "/")
+														(process-attribute is-apple-signed-executable)
+													)
 													(require-all
 														(subpath "/private/var/containers/Shared/SystemGroup")
 														(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")

 												(%entitlement-is-present "com.apple.security.system-groups")
 												(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 											)
+											(require-all
+												(subpath "/")
+												(process-attribute is-apple-signed-executable)
+											)
 										)
 									)
 								)

 							(require-all
 								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(require-any
+									(require-all
+										(subpath "/")
+										(process-attribute is-apple-signed-executable)
+									)
 									(require-all
 										(subpath "/private/var/containers/Shared/SystemGroup")
 										(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")

 								(%entitlement-is-present "com.apple.security.system-groups")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 							)
+							(require-all
+								(subpath "/")
+								(process-attribute is-apple-signed-executable)
+							)
 						)
 					)
 				)

 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
 						(require-any
+							(require-all
+								(subpath "/")
+								(process-attribute is-apple-signed-executable)
+							)
 							(require-all
 								(subpath "/private/var/containers/Shared/SystemGroup")
 								(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")

 						(%entitlement-is-present "com.apple.security.system-groups")
 						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 					)
+					(require-all
+						(subpath "/")
+						(process-attribute is-apple-signed-executable)
+					)
 				)
 			)
+			(require-all
+				(subpath "/")
+				(process-attribute is-apple-signed-executable)
+			)
 			(subpath "/Library/RegionFeatures")
 			(subpath "/System/Library")
 		)
 	)
 )
 (allow file-test-existence
-	(require-any
-		(literal "/System")
+	(require-all
 		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-test-existence
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-test-existence
+	(require-all
 		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-test-existence
+	(require-any
 		(subpath "/")
 		(subpath "/System/Cryptexes")
 		(subpath "/private/preboot/Cryptexes")
```

##### blastdoor-airlock

```diff

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(literal "/private/etc/hosts")
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")
 				)
 			)
-			(require-any
+			(require-all
 				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
 				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
 			)
 			(require-any
 				(literal "/private/etc/group")

 					(literal "/dev/random")
 					(literal "/dev/urandom")
 					(literal "/dev/zero")
-					(literal "/private")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
+							(literal "/private/etc/hosts")
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")
 							(subpath "/usr/share")
 						)
 					)
-					(require-any
+					(require-all
 						(literal "/System")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
 						(literal "/private/preboot")
+						(process-attribute is-apple-signed-executable)
 					)
 					(require-any
 						(literal "/private/etc/group")

 					(literal "/dev/random")
 					(literal "/dev/urandom")
 					(literal "/dev/zero")
-					(literal "/private")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
+							(literal "/private/etc/hosts")
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")
 							(subpath "/usr/share")
 						)
 					)
-					(require-any
+					(require-all
 						(literal "/System")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
 						(literal "/private/preboot")
+						(process-attribute is-apple-signed-executable)
 					)
 					(require-any
 						(literal "/private/etc/group")

 									(literal "/dev/random")
 									(literal "/dev/urandom")
 									(literal "/dev/zero")
-									(literal "/private")
 									(literal "/private/etc/fstab")
 									(literal "/private/etc/hosts")
 									(literal "/private/etc/passwd")

 									(require-all
 										(file-mode #o0004)
 										(require-any
+											(literal "/private/etc/hosts")
 											(subpath "/System")
 											(subpath "/private/var/db/timezone")
 											(subpath "/usr/lib")
 											(subpath "/usr/share")
 										)
 									)
-									(require-any
+									(require-all
 										(literal "/System")
+										(process-attribute is-apple-signed-executable)
+									)
+									(require-all
+										(literal "/private")
+										(process-attribute is-apple-signed-executable)
+									)
+									(require-all
 										(literal "/private/preboot")
+										(process-attribute is-apple-signed-executable)
 									)
 									(require-any
 										(literal "/private/etc/group")

 
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-ids

```diff

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(literal "/private/etc/hosts")
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")
 				)
 			)
-			(require-any
+			(require-all
 				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
 				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
 			)
 			(require-any
 				(literal "/private/etc/group")

 					(literal "/dev/random")
 					(literal "/dev/urandom")
 					(literal "/dev/zero")
-					(literal "/private")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
+							(literal "/private/etc/hosts")
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")
 							(subpath "/usr/share")
 						)
 					)
-					(require-any
+					(require-all
 						(literal "/System")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
 						(literal "/private/preboot")
+						(process-attribute is-apple-signed-executable)
 					)
 					(require-any
 						(literal "/private/etc/group")

 	)
 )
 
+(allow mach-derive-port
+	(global-name "com.apple.analyticsd")
+)
+
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-messages

```diff

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(literal "/private/etc/hosts")
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")
 				)
 			)
-			(require-any
+			(require-all
 				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
 				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
 			)
 			(require-any
 				(literal "/private/etc/group")

 					(literal "/dev/random")
 					(literal "/dev/urandom")
 					(literal "/dev/zero")
-					(literal "/private")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
+							(literal "/private/etc/hosts")
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")
 							(subpath "/usr/share")
 						)
 					)
-					(require-any
+					(require-all
 						(literal "/System")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
 						(literal "/private/preboot")
+						(process-attribute is-apple-signed-executable)
 					)
 					(require-any
 						(literal "/private/etc/group")

 
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-thumbnails

```diff

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(literal "/private/etc/hosts")
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")
 				)
 			)
-			(require-any
+			(require-all
 				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
 				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
 			)
 			(require-any
 				(literal "/private/etc/group")

 					(literal "/dev/random")
 					(literal "/dev/urandom")
 					(literal "/dev/zero")
-					(literal "/private")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
+							(literal "/private/etc/hosts")
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")
 							(subpath "/usr/share")
 						)
 					)
-					(require-any
+					(require-all
 						(literal "/System")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
+					(require-all
 						(literal "/private/preboot")
+						(process-attribute is-apple-signed-executable)
 					)
 					(require-any
 						(literal "/private/etc/group")

 
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### com.apple.dext

```diff

 
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
 		(require-any
 			(subpath "/private/var/cores")
 			(subpath "/private/var/dextcores")
 		)
+		(vnode-type REGULAR-FILE)
 	)
 )
 (allow file-read*

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read*
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")

 
 (allow file-read-metadata
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
 		(require-any
 			(subpath "/private/var/cores")
 			(subpath "/private/var/dextcores")
 		)
+		(vnode-type REGULAR-FILE)
 	)
 )
 (allow file-read-metadata

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read-metadata
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "/dev/urandom")
 		(literal "/dev/zero")
 		(literal "/etc")
-		(literal "/private")
 		(literal "/private/etc/localtime")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var")

 	)
 )
 
+(allow file-test-existence
+	(require-all
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-test-existence
 	(require-all
 		(system-attribute internal-build)

 		)
 	)
 )
+(allow file-test-existence
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-test-existence
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-test-existence
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "/dev/urandom")
 		(literal "/dev/zero")
 		(literal "/etc")
-		(literal "/private")
 		(literal "/private/etc/localtime")
-		(literal "/private/preboot")
 		(literal "/private/var")
 		(literal "/private/var/MobileSoftwareUpdate")
 		(literal "/private/var/hardware")
```

##### com.apple.pdfextensionview

```diff

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 					(subpath "/usr/share")
 				)
 			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/System")
+					(literal "/private")
+					(literal "/private/etc/passwd")
+					(literal "/private/preboot")
+				)
+			)
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
-								(file-mode #o0004)
+								(process-attribute is-apple-signed-executable)
 								(require-any
-									(subpath "/System")
-									(subpath "/private/preboot/Cryptexes")
-									(subpath "/private/var/db/timezone")
-									(subpath "/usr/lib")
-									(subpath "/usr/share")
+									(literal "/System")
+									(literal "/private")
+									(literal "/private/etc/passwd")
+									(literal "/private/preboot")
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 									(require-all
-										(file-mode #o0004)
+										(process-attribute is-apple-signed-executable)
 										(require-any
-											(subpath "/System")
-											(subpath "/private/preboot/Cryptexes")
-											(subpath "/private/var/db/timezone")
-											(subpath "/usr/lib")
-											(subpath "/usr/share")
+											(literal "/System")
+											(literal "/private")
+											(literal "/private/etc/passwd")
+											(literal "/private/preboot")
 										)
 									)
 								)

 										(require-any
 											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 											(require-all
-												(file-mode #o0004)
+												(process-attribute is-apple-signed-executable)
 												(require-any
-													(subpath "/System")
-													(subpath "/private/preboot/Cryptexes")
-													(subpath "/private/var/db/timezone")
-													(subpath "/usr/lib")
-													(subpath "/usr/share")
+													(literal "/System")
+													(literal "/private")
+													(literal "/private/etc/passwd")
+													(literal "/private/preboot")
 												)
 											)
 										)

 						)
 					)
 					(require-all
-						(file-mode #o0004)
+						(process-attribute is-apple-signed-executable)
 						(require-any
-							(subpath "/System")
-							(subpath "/private/preboot/Cryptexes")
-							(subpath "/private/var/db/timezone")
-							(subpath "/usr/lib")
-							(subpath "/usr/share")
+							(literal "/System")
+							(literal "/private")
+							(literal "/private/etc/passwd")
+							(literal "/private/preboot")
 						)
 					)
 				)
 			)
-			(require-any
-				(literal "/System")
-				(literal "/private/preboot")
-			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 					(subpath "/usr/share")
 				)
 			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/System")
+					(literal "/private")
+					(literal "/private/etc/passwd")
+					(literal "/private/preboot")
+				)
+			)
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
-								(file-mode #o0004)
+								(process-attribute is-apple-signed-executable)
 								(require-any
-									(subpath "/System")
-									(subpath "/private/preboot/Cryptexes")
-									(subpath "/private/var/db/timezone")
-									(subpath "/usr/lib")
-									(subpath "/usr/share")
+									(literal "/System")
+									(literal "/private")
+									(literal "/private/etc/passwd")
+									(literal "/private/preboot")
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 									(require-all
-										(file-mode #o0004)
+										(process-attribute is-apple-signed-executable)
 										(require-any
-											(subpath "/System")
-											(subpath "/private/preboot/Cryptexes")
-											(subpath "/private/var/db/timezone")
-											(subpath "/usr/lib")
-											(subpath "/usr/share")
+											(literal "/System")
+											(literal "/private")
+											(literal "/private/etc/passwd")
+											(literal "/private/preboot")
 										)
 									)
 								)

 										(require-any
 											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 											(require-all
-												(file-mode #o0004)
+												(process-attribute is-apple-signed-executable)
 												(require-any
-													(subpath "/System")
-													(subpath "/private/preboot/Cryptexes")
-													(subpath "/private/var/db/timezone")
-													(subpath "/usr/lib")
-													(subpath "/usr/share")
+													(literal "/System")
+													(literal "/private")
+													(literal "/private/etc/passwd")
+													(literal "/private/preboot")
 												)
 											)
 										)

 						)
 					)
 					(require-all
-						(file-mode #o0004)
+						(process-attribute is-apple-signed-executable)
 						(require-any
-							(subpath "/System")
-							(subpath "/private/preboot/Cryptexes")
-							(subpath "/private/var/db/timezone")
-							(subpath "/usr/lib")
-							(subpath "/usr/share")
+							(literal "/System")
+							(literal "/private")
+							(literal "/private/etc/passwd")
+							(literal "/private/preboot")
 						)
 					)
 				)
 			)
-			(require-any
-				(literal "/System")
-				(literal "/private/preboot")
-			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 					(subpath "/usr/share")
 				)
 			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/System")
+					(literal "/private")
+					(literal "/private/etc/passwd")
+					(literal "/private/preboot")
+				)
+			)
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
-								(file-mode #o0004)
+								(process-attribute is-apple-signed-executable)
 								(require-any
-									(subpath "/System")
-									(subpath "/private/preboot/Cryptexes")
-									(subpath "/private/var/db/timezone")
-									(subpath "/usr/lib")
-									(subpath "/usr/share")
+									(literal "/System")
+									(literal "/private")
+									(literal "/private/etc/passwd")
+									(literal "/private/preboot")
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 									(require-all
-										(file-mode #o0004)
+										(process-attribute is-apple-signed-executable)
 										(require-any
-											(subpath "/System")
-											(subpath "/private/preboot/Cryptexes")
-											(subpath "/private/var/db/timezone")
-											(subpath "/usr/lib")
-											(subpath "/usr/share")
+											(literal "/System")
+											(literal "/private")
+											(literal "/private/etc/passwd")
+											(literal "/private/preboot")
 										)
 									)
 								)

 										(require-any
 											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 											(require-all
-												(file-mode #o0004)
+												(process-attribute is-apple-signed-executable)
 												(require-any
-													(subpath "/System")
-													(subpath "/private/preboot/Cryptexes")
-													(subpath "/private/var/db/timezone")
-													(subpath "/usr/lib")
-													(subpath "/usr/share")
+													(literal "/System")
+													(literal "/private")
+													(literal "/private/etc/passwd")
+													(literal "/private/preboot")
 												)
 											)
 										)

 						)
 					)
 					(require-all
-						(file-mode #o0004)
+						(process-attribute is-apple-signed-executable)
 						(require-any
-							(subpath "/System")
-							(subpath "/private/preboot/Cryptexes")
-							(subpath "/private/var/db/timezone")
-							(subpath "/usr/lib")
-							(subpath "/usr/share")
+							(literal "/System")
+							(literal "/private")
+							(literal "/private/etc/passwd")
+							(literal "/private/preboot")
 						)
 					)
 				)
 			)
-			(require-any
-				(literal "/System")
-				(literal "/private/preboot")
-			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")
```

##### container

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ThreadNetwork.xpc")
-		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.powerlog.plxpclogger.xpc")
-		(signing-identifier "com.apple.shortcuts")
+		(global-name "com.apple.ak.anisette.xpc")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.authkit.client")
+			(%entitlement-is-bool-true "com.apple.authkit.client.internal")
+			(%entitlement-is-bool-true "com.apple.authkit.client.private")
+			(process-attribute is-apple-signed-executable)
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(signing-identifier "com.apple.shortcuts")
+		(global-name "com.apple.browserkitd")
+		(%entitlement-is-present "com.apple.developer.web-browser")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
+		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
-			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
+			(require-any
+				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+				(signing-identifier "com.apple.shortcuts.watch")
+			)
+			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(signing-identifier "com.apple.shortcuts")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(global-name "com.apple.SharedWebCredentials")
+			(global-name "com.apple.dataaccess.dataaccessd")
+			(global-name "com.apple.exchangesyncd")
+			(xpc-service-name "com.apple.LORemoteUIPinService")
+			(xpc-service-name "com.apple.ctcategories.service")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.browserkitd")
-		(%entitlement-is-present "com.apple.developer.web-browser")
+		(global-name "com.apple.iokit.powerdxpc")
+		(signing-identifier "com.apple.shortcuts")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.enterprise.licensing")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.arkit.barcode-detection.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.camera-region.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
+			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
+			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
+			(%entitlement-is-bool-true "com.apple.developer.protected-content")
+			(%entitlement-is-bool-true "com.apple.developer.screen-capture.include-passthrough")
+			(%entitlement-is-bool-true "com.apple.developer.window-body-follow")
+			(%entitlement-is-present "com.apple.developer.app-compute-category")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.FileCoordination")
-		(signing-identifier "com.apple.Music")
+		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+		(require-any
+			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
+			(global-name "com.apple.SystemConfiguration.NetworkInformation")
+			(global-name "com.apple.SystemConfiguration.PPPController")
+			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
+			(global-name "com.apple.SystemConfiguration.configd")
+			(global-name "com.apple.SystemConfiguration.helper")
+			(global-name "com.apple.commcenter.cupolicy.xpc")
+			(global-name "com.apple.commcenter.xpc")
+			(global-name "com.apple.securityd")
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.symptomsd")
+			(global-name "com.apple.trustd")
+			(global-name "com.apple.usymptomsd")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.uikit.viewservice.*")
-		(require-any
-			(global-name "com.apple.cloudd.debug")
-			(global-name "com.apple.cloudkit.partlycloudd.debug")
-		)
+		(global-name "com.apple.PowerManagement.control")
+		(signing-identifier "com.apple.shortcuts")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.lsd.xpc")
-		(signing-identifier "com.apple.mobilesafari")
+		(xpc-service-name "com.apple.StreamingUnzipService")
+		(require-any
+			(signing-identifier "com.apple.Home")
+			(signing-identifier "com.apple.Home.HomeControlService")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(process-attribute is-apple-signed-executable)
+		(signing-identifier "com.apple.Maps")
 		(require-any
-			(global-name "com.apple.SharedWebCredentials")
-			(global-name "com.apple.dataaccess.dataaccessd")
-			(global-name "com.apple.exchangesyncd")
-			(xpc-service-name "com.apple.LORemoteUIPinService")
-			(xpc-service-name "com.apple.ctcategories.service")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.assistant.analytics")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
+			(global-name "com.apple.nanomaps.xpc.Navigation")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.Music")
+		(global-name "com.apple.mobilestoredemod")
+		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.StreamingUnzipService")
-		(require-any
-			(signing-identifier "com.apple.Home")
-			(signing-identifier "com.apple.Home.HomeControlService")
-		)
+		(global-name "com.apple.FileCoordination")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.mobilemail")
-		(require-any
-			(global-name "com.apple.backupd")
-			(global-name "com.apple.bulletindistributord.server")
-			(global-name "com.apple.harvestd.manager")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.mobilemail")
-			(global-name "com.apple.nanoprefsync")
-			(global-name "com.apple.routined.registration")
-			(global-name "com.apple.sharingd.nsxpc")
-		)
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(local-name "com.apple.iphone.axserver")
-		(%entitlement-is-bool-true "com.apple.accessibility.api")
+		(global-name "com.apple.uikit.viewservice.*")
+		(require-any
+			(global-name "com.apple.cloudd.debug")
+			(global-name "com.apple.cloudkit.partlycloudd.debug")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cache_delete")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
-			(%entitlement-is-present "com.apple.private.CacheDelete")
-		)
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.Maps")
+		(global-name "com.apple.cache_delete")
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.assistant.analytics")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
-			(global-name "com.apple.nanomaps.xpc.Navigation")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
+			(%entitlement-is-present "com.apple.private.CacheDelete")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+		(signing-identifier "com.apple.mobilemail")
 		(require-any
-			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
-			(global-name "com.apple.SystemConfiguration.NetworkInformation")
-			(global-name "com.apple.SystemConfiguration.PPPController")
-			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
-			(global-name "com.apple.SystemConfiguration.configd")
-			(global-name "com.apple.SystemConfiguration.helper")
-			(global-name "com.apple.commcenter.cupolicy.xpc")
-			(global-name "com.apple.commcenter.xpc")
-			(global-name "com.apple.securityd")
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.symptomsd")
-			(global-name "com.apple.trustd")
-			(global-name "com.apple.usymptomsd")
+			(global-name "com.apple.backupd")
+			(global-name "com.apple.bulletindistributord.server")
+			(global-name "com.apple.harvestd.manager")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.mobilemail")
+			(global-name "com.apple.nanoprefsync")
+			(global-name "com.apple.routined.registration")
+			(global-name "com.apple.sharingd.nsxpc")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-				(signing-identifier "com.apple.shortcuts.watch")
-			)
-			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(signing-identifier "com.apple.shortcuts")
-		)
+		(global-name "com.apple.safarifetcherd")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.enterprise.licensing")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.arkit.barcode-detection.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.camera-region.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
-			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
-			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
-			(%entitlement-is-bool-true "com.apple.developer.protected-content")
-			(%entitlement-is-bool-true "com.apple.developer.screen-capture.include-passthrough")
-			(%entitlement-is-bool-true "com.apple.developer.window-body-follow")
-			(%entitlement-is-present "com.apple.developer.app-compute-category")
-		)
+		(global-name "com.apple.lsd.xpc")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ak.anisette.xpc")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.authkit.client")
-			(%entitlement-is-bool-true "com.apple.authkit.client.internal")
-			(%entitlement-is-bool-true "com.apple.authkit.client.private")
-			(process-attribute is-apple-signed-executable)
-		)
+		(local-name "com.apple.iphone.axserver")
+		(%entitlement-is-bool-true "com.apple.accessibility.api")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
+		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
 		(require-any
-			(signing-identifier "com.apple.Health")
-			(signing-identifier "com.apple.PassbookUIService")
+			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
+			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(global-name "com.apple.nanoprefsync")
+		(require-any
+			(signing-identifier "com.apple.Health")
+			(signing-identifier "com.apple.PassbookUIService")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.merchantd.storage")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
+		(global-name "com.apple.nanoprefsync")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.safarifetcherd")
-		(signing-identifier "com.apple.mobilesafari")
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.personad.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
+		(global-name "com.apple.powerlog.plxpclogger.xpc")
 		(signing-identifier "com.apple.shortcuts")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobilestoredemod")
-		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
+		(global-name "com.apple.merchantd.storage")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
+		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")
```

##### hotspot-provider

```diff

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "/")

 		)
 	)
 )
+(allow file-test-existence
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-test-existence
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(subpath "/")
 		(subpath "/System/Cryptexes")
 		(subpath "/private/preboot/Cryptexes")
```

##### imagent

```diff

 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.MobileSMS")
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${HOME}/Library/Caches/Checkpoint.plist")
 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")
 		(literal "${HOME}/Library/Logs/MobileBackup/MobileBackup-imagent.log")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(system-attribute carrier-build)

 		(literal "${HOME}/Library/Logs/MobileBackup/MobileBackup-imagent.log")
 		(literal "${HOME}/Library/PPTDevice")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
```

##### mDNSResponder

```diff

 		(system-attribute carrier-build)
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/usr/local/lib")

 	(require-any
 		(literal "/Library/Preferences/com.apple.networkd.plist")
 		(literal "/Library/Preferences/com.apple.networkextension.uuidcache.plist")
-		(literal "/System")
 		(literal "/dev/aes_0")
 		(literal "/dev/dtracehelper")
 		(literal "/dev/null")
 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")

 		(system-attribute carrier-build)
 	)
 )
+(allow file-read-data
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "/usr/local/lib")

 		(literal "/Library/Preferences/SystemConfiguration/com.apple.PowerManagement.plist")
 		(literal "/Library/Preferences/com.apple.networkd.plist")
 		(literal "/Library/Preferences/com.apple.networkextension.uuidcache.plist")
-		(literal "/System")
 		(literal "/dev/aes_0")
 		(literal "/dev/console")
 		(literal "/dev/dtracehelper")

 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
 		(literal "/private/etc/hosts")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
```

##### maild

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ExposureNotification")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ThreadNetwork.xpc")
-		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.MusicKit.UI")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.anisette.xpc")

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.auth.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+		(global-name "com.apple.MusicKit.UI")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
+		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")
```

##### quicklook-thumbnail-secure

```diff

 	)
 )
 
+(allow file-read*
+	(require-all
+		(subpath "/")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read*
 	(require-any
 		(extension "com.apple.app-sandbox.read")
 		(extension "com.apple.sandbox.executable")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
-		(literal "/System")
 		(literal "/dev/dtracehelper")
 		(literal "/dev/null")
 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
 		(literal "/private/etc/fstab")
 		(literal "/private/etc/group")
 		(literal "/private/etc/hosts")
 		(literal "/private/etc/passwd")
 		(literal "/private/etc/protocols")
 		(literal "/private/etc/services")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")

 			(literal "/dev/random")
 			(literal "/dev/urandom")
 			(literal "/dev/zero")
-			(literal "/private")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 				(extension "com.apple.sandbox.application-group")
 				(require-not (literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*"))
 				(require-any
-					(literal "/private")
 					(require-all
 						(subpath "/private/var")
 						(require-any
 							(require-all
 								(extension "com.apple.sandbox.container")
 								(require-any
+									(require-all
+										(literal "/private")
+										(process-attribute is-apple-signed-executable)
+									)
 									(require-all
 										(subpath "/private/var")
 										(require-any

 								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\."))
 								(extension "com.apple.sandbox.container")
 								(require-any
+									(require-all
+										(literal "/private")
+										(process-attribute is-apple-signed-executable)
+									)
 									(require-all
 										(subpath "/private/var")
 										(require-any

 							)
 						)
 					)
+					(require-any
+						(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
+						(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
+					)
 				)
 			)
 			(require-all
 				(extension "com.apple.sandbox.container")
 				(require-any
+					(require-all
+						(literal "/private")
+						(process-attribute is-apple-signed-executable)
+					)
 					(require-all
 						(subpath "/private/var")
 						(require-any

 						(extension "com.apple.sandbox.application-group")
 						(require-not (literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*"))
 						(require-any
-							(literal "/private")
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(extension "com.apple.sandbox.container")
 										(require-any
+											(require-all
+												(literal "/private")
+												(process-attribute is-apple-signed-executable)
+											)
 											(require-all
 												(subpath "/private/var")
 												(require-any

 										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\."))
 										(extension "com.apple.sandbox.container")
 										(require-any
+											(require-all
+												(literal "/private")
+												(process-attribute is-apple-signed-executable)
+											)
 											(require-all
 												(subpath "/private/var")
 												(require-any

 									)
 								)
 							)
+							(require-any
+								(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
+								(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
+							)
 						)
 					)
 					(subpath "/System")

 					(subpath "/usr/share")
 				)
 			)
+			(require-all
+				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(subpath "/")
+				(process-attribute is-apple-signed-executable)
+			)
 			(require-all
 				(subpath "/private/var")
 				(extension "com.apple.sandbox.application-group")

 					)
 				)
 			)
-			(require-any
-				(literal "/System")
-				(literal "/private/preboot")
-			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "/")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(vnode-type DIRECTORY)
 		(process-attribute is-apple-signed-executable)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "/private/preboot")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read-metadata
 	(require-any
 		(extension "com.apple.app-sandbox.read")

 		(literal "${HOME}")
 		(literal "${HOME}/Library/Preferences")
 		(literal "/Library/Preferences")
-		(literal "/System")
 		(literal "/dev/dtracehelper")
 		(literal "/dev/null")
 		(literal "/dev/random")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
 		(literal "/etc")
-		(literal "/private")
 		(literal "/private/etc/fstab")
 		(literal "/private/etc/group")
 		(literal "/private/etc/hosts")

 		(literal "/private/etc/passwd")
 		(literal "/private/etc/protocols")
 		(literal "/private/etc/services")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
```

##### quicklookd

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.session")
-		(%entitlement-is-present "com.apple.developer.carkey.session")
+		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(global-name "com.apple.MomentsUIService")
+		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(global-name "com.apple.ExposureNotification")
+		(%entitlement-is-present "com.apple.developer.exposure-notification")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ThreadNetwork.xpc")
-		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.SafetyKit")
-		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+		(global-name "com.apple.seserviced.session")
+		(%entitlement-is-present "com.apple.developer.carkey.session")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ExposureNotification")
-		(%entitlement-is-present "com.apple.developer.exposure-notification")
+		(global-name "com.apple.SafetyKit")
+		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
+		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")
```

##### racoon

```diff

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(require-not (subpath "/usr/appleinternal/lib"))
+		(require-not (subpath "/usr/local/lib"))
+		(require-any
+			(require-all
+				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
+			)
+		)
+	)
+)
 (allow file-read*
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "/Library/Managed Preferences")
 		(literal "/Library/Managed Preferences/mobile")
 		(literal "/Library/Preferences")
-		(literal "/System")
 		(literal "/dev/aes_0")
 		(literal "/dev/dtracehelper")
 		(literal "/dev/null")

 		(literal "/dev/sha1_0")
 		(literal "/dev/urandom")
 		(literal "/dev/zero")
-		(literal "/private")
 		(literal "/private/etc/master.passwd")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(require-not (subpath "/usr/appleinternal/lib"))
+		(require-not (subpath "/usr/local/lib"))
+		(require-any
+			(require-all
+				(literal "/System")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(literal "/private/preboot")
+				(process-attribute is-apple-signed-executable)
+			)
+		)
+	)
+)
 (allow file-read-metadata
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(literal "/Library/Managed Preferences")
 		(literal "/Library/Managed Preferences/mobile")
 		(literal "/Library/Preferences")
-		(literal "/System")
 		(literal "/dev/aes_0")
 		(literal "/dev/dtracehelper")
 		(literal "/dev/null")

 		(literal "/dev/urandom")
 		(literal "/dev/zero")
 		(literal "/etc")
-		(literal "/private")
 		(literal "/private/etc/localtime")
 		(literal "/private/etc/master.passwd")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
```

##### safety-inference-extension

```diff

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "/")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-any
 		(literal "${HOME}")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "/")

 	)
 )
 
+(allow file-test-existence
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-test-existence
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(subpath "/")
 		(subpath "/System/Cryptexes")
 		(subpath "/private/preboot/Cryptexes")
```

##### secure-capture-extension

```diff

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "${HOME}/Library/Caches/Checkpoint.plist")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/EffectiveUserSettings.plist")

 		(literal "${HOME}")
 		(literal "${HOME}/Library/Caches/Checkpoint.plist")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")

 	)
 )
 
+(allow file-test-existence
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-test-existence
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(subpath "/")
 		(subpath "/System/Cryptexes")
 		(subpath "/private/preboot/Cryptexes")
```

##### temporary-sandbox

```diff

 	)
 )
 
-(allow file-issue-extension
+(define (_g0 _)
+	(require-all
+	(subpath "/private/var/tmp")
+	(signing-identifier "com.apple.Carousel")
+))
+(define (_g1 _)
+	(require-all
+	(subpath "${PROCESS_TEMP_DIR}")
+	(signing-identifier "com.apple.Carousel")
+))
+(define (_g2 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g1 "")
+		(require-all
+			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+			(require-any
+				(_g0 "")
+				(signing-identifier "com.apple.internal.livtipsd")
+			)
+		)
+	)
+))
+(define (_g3 _)
+	(require-all
+	(subpath "${HOME}/Library/Logs/Brook")
+	(signing-identifier "com.apple.Carousel")
+))
+(define (_g4 _)
+	(require-all
+	(subpath "/private/var")
+	(require-any
+		(_g3 "")
+		(require-all
+			(extension "com.apple.sandbox.application-group")
+			(require-any
+				(_g0 "")
+				(_g1 "")
+				(_g2 "")
+				(_g3 "")
+				(require-all
+					(subpath "${FRONT_USER_HOME}")
+					(require-any
+						(_g2 "")
+						(require-all
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(signing-identifier "com.apple.internal.livtipsd")
+						)
+					)
+				)
+			)
+		)
+	)
+))
+(define (_g5 _)
+	(signing-identifier "com.apple.FTLivePhotoService"))
+(define (_g6 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
+	(extension "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.FTLivePhotoService")
+))
+(define (_g7 _)
+	(require-all
+	(subpath "/private/var/tmp")
+	(signing-identifier "com.apple.facetimemessagestored")
+))
+(define (_g8 _)
+	(require-all
+	(require-any
+		(subpath "${HOME}/Library/Caches/com.apple.asktod")
+		(subpath "${HOME}/Library/com.apple.asktod")
+	)
+	(signing-identifier "com.apple.asktod")
+))
+(define (_g9 _)
+	(require-all
+	(subpath "${HOME}/Library/Application Support/com.apple.FaceTime/VideoMessaging/Outbox")
+	(require-any
+		(_g8 "")
+		(require-all
+			(subpath "${PROCESS_TEMP_DIR}")
+			(signing-identifier "com.apple.asktod")
+		)
+		(require-all
+			(subpath "/private/var/tmp")
+			(signing-identifier "com.apple.asktod")
+		)
+		(signing-identifier "com.apple.facetimemessagestored")
+	)
+))
+(define (_g10 _)
+	(require-all
+	(require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	)
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+))
+(define (_g11 _)
+	(require-all
+	(subpath "${HOME}/Library/VoiceTrigger")
+	(require-any
+		(require-all
+			(signing-identifier "com.apple.appplaceholdersyncd")
+			(subpath "/private/var")
+			(extension "com.apple.sandbox.container")
+			(require-any
+				(_g10 "")
+				(require-all
+					(subpath "/private/var/PersonaVolumes")
+					(require-any
+						(_g10 "")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
+					)
+				)
+			)
+		)
+		(signing-identifier "com.apple.corespeechd")
+	)
+))
+(define (_g12 _)
+	(require-all
+	(signing-identifier "com.apple.cloudpaird")
+	(require-any
+		(require-all
+			(extension-class "com.apple.app-sandbox.read")
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+			)
+			(signing-identifier "com.apple.chronod")
+		)
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+	)
+))
+(define (_g13 _)
+	(require-all
+	(require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	)
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+))
+(define (_g14 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(require-any
+		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+	)
+	(signing-identifier "com.apple.chronod")
+))
+(define (_g15 _)
+	(require-all
+	(require-any
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.anomalydetectiond")
+		(subpath "/private/var/tmp/com.apple.anomalydetectiond")
+	)
+	(signing-identifier "com.apple.anomalydetectiond")
+))
+(define (_g16 _)
+	(require-all
+	(require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	)
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+))
+(define (_g17 _)
+	(require-all
+	(subpath "${HOME}/Library/BulletinDistributor/Attachments")
+	(require-any
+		(require-all
+			(extension-class "com.apple.nsurlsessiond.readonly")
+			(require-any
+				(require-all
+					(require-any
+						(subpath "${PROCESS_TEMP_DIR}/com.apple.anomalydetectiond")
+						(subpath "/private/var/tmp/com.apple.anomalydetectiond")
+					)
+					(signing-identifier "com.apple.anomalydetectiond")
+				)
+				(require-all
+					(subpath "${HOME}/Library/com.apple.momentsd")
+					(signing-identifier "com.apple.momentsd")
+				)
+			)
+		)
+		(signing-identifier "com.apple.Carousel")
+	)
+))
+(define (_g18 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g19 _)
+	(require-any
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g20 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g19 "")
+))
+(define (_g21 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(_g19 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(_g18 "")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g22 _)
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(_g21 "")
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(_g21 "")
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
+(define (_g23 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g24 _)
+	(require-any
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g25 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g24 "")
+))
+(define (_g26 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(_g24 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(_g23 "")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g27 _)
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(_g26 "")
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(_g26 "")
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
+(define (_g28 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g29 _)
+	(require-any
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g30 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g29 "")
+))
+(define (_g31 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(_g29 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(_g28 "")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g32 _)
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(_g31 "")
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(_g31 "")
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
+(define (_g33 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g34 _)
+	(require-any
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g35 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g34 "")
+))
+(define (_g36 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(_g34 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(_g33 "")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g37 _)
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(_g36 "")
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(_g36 "")
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
+(define (_g38 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g39 _)
+	(require-any
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g40 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g39 "")
+))
+(define (_g41 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(_g39 "")
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(_g38 "")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g42 _)
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(_g41 "")
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(_g41 "")
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
+(define (_g43 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(require-any
+		(_g42 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g42 "")
+				(require-all
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
+					(require-any
+						(require-all
+							(require-any
+								(subpath "${FRONT_USER_HOME}")
+								(subpath "${HOME}")
+							)
+							(signing-identifier "com.apple.MTLAssetUpgraderD")
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(_g38 "")
+								(_g40 "")
+								(require-all
+									(subpath "/private/var")
+									(require-any
+										(_g40 "")
+										(require-all
+											(require-any
+												(subpath "${FRONT_USER_HOME}")
+												(subpath "${HOME}")
+											)
+											(require-any
+												(_g40 "")
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+		(require-all
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
+			(signing-identifier "com.apple.MTLAssetUpgraderD")
+		)
+	)
+))
+(define (_g44 _)
+	(require-all
+	(require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	)
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+))
+(define (_g45 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(require-any
+								(require-any
+									(subpath "/AppleInternal/Applications")
+									(subpath "/System/Developer/Applications")
+									(subpath "/private/var/factory_mount/[^/]+/Applications")
+									(subpath "/private/var/personalized_automation/Applications")
+									(subpath "/private/var/personalized_debug/Applications")
+									(subpath "/private/var/personalized_factory/[^/]+/Applications")
+								)
+								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+								(subpath "/Applications")
+								(subpath "/Developer/Applications")
+								(subpath "/private/var/containers/Bundle")
+							)
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(extension "com.apple.mediaserverd.read")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g46 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(require-any
+								(require-any
+									(subpath "/AppleInternal/Applications")
+									(subpath "/System/Developer/Applications")
+									(subpath "/private/var/factory_mount/[^/]+/Applications")
+									(subpath "/private/var/personalized_automation/Applications")
+									(subpath "/private/var/personalized_debug/Applications")
+									(subpath "/private/var/personalized_factory/[^/]+/Applications")
+								)
+								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+								(subpath "/Applications")
+								(subpath "/Developer/Applications")
+								(subpath "/private/var/containers/Bundle")
+							)
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(extension "com.apple.mediaserverd.read")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g47 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(require-any
+								(require-any
+									(subpath "/AppleInternal/Applications")
+									(subpath "/System/Developer/Applications")
+									(subpath "/private/var/factory_mount/[^/]+/Applications")
+									(subpath "/private/var/personalized_automation/Applications")
+									(subpath "/private/var/personalized_debug/Applications")
+									(subpath "/private/var/personalized_factory/[^/]+/Applications")
+								)
+								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+								(subpath "/Applications")
+								(subpath "/Developer/Applications")
+								(subpath "/private/var/containers/Bundle")
+							)
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(extension "com.apple.mediaserverd.read")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g48 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(extension "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.mediaserverd.read")
+					(require-any
+						(require-all
+							(signing-identifier "com.apple.linkd")
+							(require-any
+								(require-any
+									(subpath "/AppleInternal/Applications")
+									(subpath "/System/Developer/Applications")
+									(subpath "/private/var/factory_mount/[^/]+/Applications")
+									(subpath "/private/var/personalized_automation/Applications")
+									(subpath "/private/var/personalized_debug/Applications")
+									(subpath "/private/var/personalized_factory/[^/]+/Applications")
+								)
+								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+								(subpath "/Applications")
+								(subpath "/Developer/Applications")
+								(subpath "/private/var/containers/Bundle")
+							)
+						)
+						(require-all
+							(signing-identifier "com.apple.mediaplaybackd")
+							(require-any
+								(extension "com.apple.mediaserverd.read")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+							)
+						)
+					)
+				)
+			)
+		)
+		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	)
+))
+(define (_g49 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g50 _)
+	(require-any
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g51 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(require-all
+			(signing-identifier "com.apple.linkd")
+			(_g50 "")
+		)
+		(require-all
+			(signing-identifier "com.apple.mediaplaybackd")
+			(require-any
+				(_g49 "")
+				(extension "com.apple.mediaserverd.read")
+			)
+		)
+	)
+))
+(define (_g52 _)
+	(require-any
+	(_g51 "")
+	(extension "com.apple.mediaserverd.read-write")
+))
+(define (_g53 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read-write")
+	(signing-identifier "com.apple.mediaplaybackd")
+	(_g52 "")
+))
+(define (_g54 _)
+	(require-any
+	(_g53 "")
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+))
+(define (_g55 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(_g54 "")
+))
+(define (_g56 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g50 "")
+))
+(define (_g57 _)
+	(require-any
+	(_g49 "")
+	(_g56 "")
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(_g56 "")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(require-any
+					(_g56 "")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+				)
+			)
+		)
+	)
+))
+(define (_g58 _)
 	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-		(signing-identifier "com.apple.storagedatad")
+	(extension-class "com.apple.app-sandbox.read-write")
+	(signing-identifier "com.apple.mediaplaybackd")
+	(_g57 "")
+))
+(define (_g59 _)
+	(require-all
+	(extension-class "com.apple.aned.read-only")
+	(signing-identifier "com.apple.linkd")
+	(_g50 "")
+))
+(define (_g60 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.ClarityBoard")
+	(subpath "/private/var")
+	(subpath "${HOME}")
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+))
+(define (_g61 _)
+	(require-all
+	(signing-identifier "com.apple.avconferenced")
+	(require-any
+		(_g60 "")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
+			(subpath "/private/var/tmp/com.apple.avconferenced")
+		)
+	)
+))
+(define (_g62 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g61 "")
+		(require-all
+			(signing-identifier "com.apple.cameracaptured")
+			(extension "com.apple.mediaserverd.read")
+		)
+	)
+))
+(define (_g63 _)
+	(require-any
+	(_g62 "")
+	(extension "com.apple.mediaserverd.read-write")
+))
+(define (_g64 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read-write")
+	(signing-identifier "com.apple.cameracaptured")
+	(_g63 "")
+))
+(define (_g65 _)
+	(require-all
+	(require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	)
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+))
+(define (_g66 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read-write")
+	(extension "com.apple.security.exception.files.home-relative-path.read-write")
+))
+(define (_g67 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read-write")
+	(extension "com.apple.app-sandbox.read-write")
+))
+(define (_g68 _)
+	(require-any
+	(_g67 "")
+	(extension "com.apple.clouddocs.version")
+))
+(define (_g69 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+	(require-any
+		(_g67 "")
+		(require-all
+			(vnode-type REGULAR-FILE)
+			(_g68 "")
+		)
+	)
+))
+(define (_g70 _)
+	(require-all
+	(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
+	(vnode-type REGULAR-FILE)
+	(_g68 "")
+))
+(define (_g71 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read-write")
+	(extension "com.apple.app-sandbox.read-write")
+))
+(define (_g72 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(require-any
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/AppleInternal/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+))
+(define (_g73 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g72 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g74 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(require-any
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/AppleInternal/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+))
+(define (_g75 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(require-all
+			(subpath "/private/var/PersonaVolumes")
+			(require-any
+				(_g74 "")
+				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+			)
+		)
+	)
+))
+(define (_g76 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g75 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g77 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g74 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g74 "")
+				(require-all
+					(extension "com.apple.sandbox.application-group")
+					(require-any
+						(_g75 "")
+						(_g76 "")
+						(require-all
+							(subpath "${FRONT_USER_HOME}")
+							(require-any
+								(_g76 "")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+))
+(define (_g78 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(require-any
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/AppleInternal/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+))
+(define (_g79 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(require-all
+			(subpath "/private/var/PersonaVolumes")
+			(require-any
+				(_g78 "")
+				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+			)
+		)
+	)
+))
+(define (_g80 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g79 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g81 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g78 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g78 "")
+				(require-all
+					(extension "com.apple.sandbox.application-group")
+					(require-any
+						(_g79 "")
+						(_g80 "")
+						(require-all
+							(subpath "${FRONT_USER_HOME}")
+							(require-any
+								(_g80 "")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+))
+(define (_g82 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(require-any
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/AppleInternal/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+))
+(define (_g83 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(require-all
+			(subpath "/private/var/PersonaVolumes")
+			(require-any
+				(_g82 "")
+				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+			)
+		)
+	)
+))
+(define (_g84 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g83 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g85 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g82 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g82 "")
+				(require-all
+					(extension "com.apple.sandbox.application-group")
+					(require-any
+						(_g83 "")
+						(_g84 "")
+						(require-all
+							(subpath "${FRONT_USER_HOME}")
+							(require-any
+								(_g84 "")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+))
+(define (_g86 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(require-any
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/AppleInternal/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+))
+(define (_g87 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g86 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g88 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g87 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g89 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g88 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g90 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g86 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g86 "")
+				(require-all
+					(extension "com.apple.sandbox.application-group")
+					(require-any
+						(_g88 "")
+						(_g89 "")
+						(require-all
+							(subpath "${FRONT_USER_HOME}")
+							(require-any
+								(_g89 "")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+))
+(define (_g91 _)
+	(require-any
+	(_g86 "")
+	(_g87 "")
+	(_g88 "")
+))
+(define (_g92 _)
+	(require-all
+	(extension "com.apple.security.exception.files.home-relative-path.read-write")
+	(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+))
+(define (_g93 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g92 "")
+		(require-all
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+		)
+		(require-all
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+		)
+	)
+))
+(define (_g94 _)
+	(require-any
+	(_g93 "")
+	(require-any
+		(subpath "/AppleInternal/Applications")
+		(subpath "/System/Developer/Applications")
+		(subpath "/private/var/factory_mount/[^/]+/Applications")
+		(subpath "/private/var/personalized_automation/Applications")
+		(subpath "/private/var/personalized_debug/Applications")
+		(subpath "/private/var/personalized_factory/[^/]+/Applications")
+	)
+	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/Applications")
+	(subpath "/Developer/Applications")
+	(subpath "/private/var/containers/Bundle")
+))
+(define (_g95 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+	(_g94 "")
+))
+(define (_g96 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.tmpdir")
+	(require-any
+		(_g95 "")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+))
+(define (_g97 _)
+	(require-all
+	(extension "com.apple.sandbox.container")
+	(require-any
+		(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+		(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+	)
+))
+(define (_g98 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read-write")
+	(require-any
+		(require-all
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		)
+		(require-all
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		)
 	)
-)
-(allow file-issue-extension
+))
+(define (_g99 _)
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-		(signing-identifier "com.apple.storagedatad")
+	(extension "com.apple.assets.read")
+	(require-any
+		(require-all
+			(subpath "${HOME}/Library/Assets")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		)
+		(require-all
+			(subpath "/private/var/MobileAsset")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		)
 	)
-)
+))
 (allow file-issue-extension
+	(require-any
 	(require-all
-		(extension-class "com.apple.StreamingUnzipService")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
+			(_g66 "")
+			(_g71 "")
 			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(extension-class "com.apple.quicklook.readonly")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
 				(require-any
-					(literal "/private/var/containers/Data/System/[^/]+/Library/Caches/Scratch*")
+					(_g66 "")
+					(require-all
+						(subpath "${HOME}/Library/Mobile Documents")
+						(extension-class "com.apple.quicklook.readonly")
+					)
 					(require-all
-						(subpath "${HOME}/Library/VoiceTrigger")
+						(subpath "/private/var")
 						(require-any
+							(_g66 "")
 							(require-all
-								(signing-identifier "com.apple.appplaceholdersyncd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 								(require-any
+									(_g66 "")
 									(require-all
+										(subpath "${FRONT_USER_HOME}")
 										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
-											)
+											(extension-class "com.apple.aned.read-only")
+											(extension-class "com.apple.app-sandbox.read")
+											(extension-class "com.apple.app-sandbox.read-write")
+											(extension-class "com.apple.mediaserverd.read")
+											(extension-class "com.apple.mediaserverd.read-write")
+											(extension-class "com.apple.quicklook.readonly")
+											(extension-class "com.apple.sharing.airdrop.readonly")
 										)
 									)
 								)
 							)
-							(signing-identifier "com.apple.corespeechd")
 						)
 					)
-					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.installcoordinationd/Library/InstallCoordination/PromiseStaging")
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(extension-class "com.apple.quicklook.readonly")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+						(extension-class "com.apple.quicklook.readonly")
+					)
 				)
 			)
 			(require-all
-				(subpath "${HOME}/Library/VoiceTrigger")
+				(extension-class "com.apple.app-sandbox.read")
+				(extension "com.apple.app-sandbox.read-write")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(extension "com.apple.app-sandbox.read-write")
+					(extension "com.apple.security.exception.files.absolute-path.read-only")
+					(extension "com.apple.security.exception.files.absolute-path.read-write")
+					(extension "com.apple.security.exception.files.home-relative-path.read-only")
+					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				)
+			)
+			(require-all
+				(extension-class "com.apple.quicklook.readonly")
 				(require-any
+					(_g67 "")
+					(_g69 "")
+					(_g70 "")
+					(_g71 "")
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(extension "com.apple.app-sandbox.read-write")
+					)
 					(require-all
-						(signing-identifier "com.apple.appplaceholdersyncd")
 						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
 						(require-any
+							(_g70 "")
 							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
 								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
+									(_g69 "")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+										(extension "com.apple.clouddocs.version")
 									)
 								)
 							)
 						)
 					)
-					(signing-identifier "com.apple.corespeechd")
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+						(extension "com.apple.clouddocs.version")
+					)
 				)
 			)
+			(require-all
+				(extension-class "com.apple.sharing.airdrop.readonly")
+				(extension "com.apple.app-sandbox.read-write")
+			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.StreamingUnzipService")
 		(require-any
+			(_g11 "")
 			(require-all
-				(subpath "${HOME}/Library/Logs/Brook")
-				(signing-identifier "com.apple.Carousel")
-			)
-			(require-all
-				(subpath "${HOME}/Library/UserNotifications")
-				(signing-identifier "com.apple.usernotificationsd")
+				(signing-identifier "com.apple.managedappdistributiond")
+				(require-any
+					(_g11 "")
+					(literal "/private/var/containers/Data/System/[^/]+/Library/Caches/Scratch*")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.installcoordinationd/Library/InstallCoordination/PromiseStaging")
+				)
 			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.StreamingUnzipService")
+		(require-any
 			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
+				(signing-identifier "com.apple.appplaceholdersyncd")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
 				(require-any
+					(_g44 "")
 					(require-all
-						(subpath "/private/var/tmp")
-						(signing-identifier "com.apple.Carousel")
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(_g44 "")
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
+						)
 					)
-					(signing-identifier "com.apple.usernotificationsd")
 				)
 			)
 			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.usernotificationsd")
+				(signing-identifier "com.apple.assistantd")
+				(subpath "${HOME}/Library/Caches/VoiceTrigger")
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.StreamingUnzipService")
 		(require-any
 			(require-all
-				(extension "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.assistantd")
+				(subpath "${HOME}/Library/Caches/VoiceTrigger")
+			)
+			(require-all
+				(subpath "${HOME}/Library/VoiceTrigger")
 				(require-any
 					(require-all
-						(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+						(signing-identifier "com.apple.appplaceholdersyncd")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
 						(require-any
+							(_g16 "")
 							(require-all
-								(signing-identifier "com.apple.avconferenced")
+								(subpath "/private/var/PersonaVolumes")
 								(require-any
-									(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
-									(subpath "/private/var/tmp/com.apple.avconferenced")
+									(_g16 "")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 								)
 							)
-							(signing-identifier "com.apple.anomalydetectiond")
 						)
 					)
-					(signing-identifier "com.apple.cameracaptured")
-					(signing-identifier "com.apple.mediaplaybackd")
+					(signing-identifier "com.apple.corespeechd")
 				)
 			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.StreamingUnzipService")
+		(signing-identifier "com.apple.appplaceholdersyncd")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(_g65 "")
 			(require-all
-				(signing-identifier "com.apple.avconferenced")
+				(subpath "/private/var/PersonaVolumes")
 				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
-					(subpath "/private/var/tmp/com.apple.avconferenced")
+					(_g65 "")
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 				)
 			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(require-any
 			(require-all
-				(signing-identifier "com.apple.geoanalyticsd")
-				(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-			)
-			(require-all
-				(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+				(%entitlement-is-present "com.apple.security.ts.tmpdir")
 				(require-any
 					(require-all
-						(signing-identifier "com.apple.avconferenced")
+						(extension-class "com.apple.app-sandbox.read")
+						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 						(require-any
-							(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
-							(subpath "/private/var/tmp/com.apple.avconferenced")
+							(require-all
+								(extension-class "com.apple.mediaserverd.read")
+								(require-any
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+								)
+							)
+							(require-any
+								(subpath "/AppleInternal/Applications")
+								(subpath "/System/Developer/Applications")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
+							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
 					)
-					(signing-identifier "com.apple.anomalydetectiond")
+					(require-any
+						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					)
 				)
 			)
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(extension-class "com.apple.mediaserverd.read-write")
 				(require-any
 					(require-all
-						(signing-identifier "com.apple.avconferenced")
-						(require-any
-							(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
-							(subpath "/private/var/tmp/com.apple.avconferenced")
-						)
+						(extension "com.apple.security.exception.files.absolute-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+					)
+					(require-all
+						(extension "com.apple.security.exception.files.home-relative-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 					)
-					(signing-identifier "com.apple.momentsd")
 				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+		(signing-identifier "com.apple.storagedatad")
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
+			(_g72 "")
 			(require-all
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(signing-identifier "com.apple.cloudpaird")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-			)
-			(require-all
-				(subpath "/private/var")
+				(extension "com.apple.sandbox.application-group")
 				(require-any
+					(_g72 "")
 					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
+						(subpath "/private/var")
 						(require-any
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-								(signing-identifier "com.apple.storagedatad")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								(require-any
+									(_g73 "")
+									(subpath "${FRONT_USER_HOME}")
+								)
 							)
 							(require-all
-								(signing-identifier "com.apple.cloudpaird")
-								(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(_g73 "")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+								)
 							)
 						)
 					)
-					(require-all
-						(signing-identifier "com.apple.cloudpaird")
-						(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.StreamingUnzipService")
+		(extension-class "com.apple.aned.read-only")
+		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
 			(require-all
-				(signing-identifier "com.apple.assistantd")
-				(subpath "${HOME}/Library/Caches/VoiceTrigger")
-			)
-			(require-all
-				(subpath "${HOME}/Library/VoiceTrigger")
+				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
+					(_g37 "")
 					(require-all
-						(signing-identifier "com.apple.appplaceholdersyncd")
 						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
 						(require-any
+							(_g37 "")
 							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+										(signing-identifier "com.apple.MTLAssetUpgraderD")
+									)
+									(require-all
+										(signing-identifier "com.apple.mediaplaybackd")
+										(require-any
+											(_g33 "")
+											(_g35 "")
+											(require-all
+												(subpath "/private/var")
+												(require-any
+													(_g35 "")
+													(require-all
+														(require-any
+															(subpath "${FRONT_USER_HOME}")
+															(subpath "${HOME}")
+														)
+														(require-any
+															(_g35 "")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+														)
+													)
+												)
+											)
+										)
 									)
 								)
 							)
 						)
 					)
-					(signing-identifier "com.apple.corespeechd")
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
 				)
 			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(signing-identifier "com.apple.momentsd")
-		(subpath "${HOME}/Library/com.apple.momentsd")
-	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
+		(signing-identifier "com.apple.cloudpaird")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.app-sandbox.read")
 				(require-any
-					(require-all
-						(require-any
-							(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-						)
-						(signing-identifier "com.apple.chronod")
-					)
-					(require-all
-						(subpath "/private/var")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-						(signing-identifier "com.apple.chronod")
-					)
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
 				)
+				(signing-identifier "com.apple.chronod")
 			)
-			(require-all
-				(signing-identifier "com.apple.cloudpaird")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-			)
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 		)
 	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.aned.read-only")
+		(signing-identifier "com.apple.geoanalyticsd")
 		(require-any
 			(require-all
-				(subpath "${HOME}/Library/Logs/Brook")
-				(signing-identifier "com.apple.Carousel")
-			)
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(signing-identifier "com.apple.Carousel")
-			)
-			(require-all
-				(subpath "/private/var")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.cameracaptured")
 				(require-any
+					(extension "com.apple.mediaserverd.read-write")
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/BulletinDistributor")
+						(extension-class "com.apple.mediaserverd.read")
 						(require-any
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(signing-identifier "com.apple.Carousel")
+								(signing-identifier "com.apple.avconferenced")
+								(require-any
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(signing-identifier "com.apple.ClarityBoard")
+										(subpath "/private/var")
+										(subpath "${HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+									)
+									(require-any
+										(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
+										(subpath "/private/var/tmp/com.apple.avconferenced")
+									)
+								)
 							)
 							(require-all
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
-								(extension "com.apple.app-sandbox.read")
-								(signing-identifier "com.apple.FTLivePhotoService")
+								(signing-identifier "com.apple.cameracaptured")
+								(extension "com.apple.mediaserverd.read")
 							)
 						)
 					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
-						(extension "com.apple.app-sandbox.read")
-						(signing-identifier "com.apple.FTLivePhotoService")
-					)
 				)
 			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
-				(extension "com.apple.app-sandbox.read")
-				(signing-identifier "com.apple.FTLivePhotoService")
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.Carousel")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var")
+		(extension-class "com.apple.aned.read-only")
+		(signing-identifier "com.apple.momentsd")
 		(require-any
+			(_g48 "")
 			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-				(subpath "${HOME}")
-				(signing-identifier "com.apple.Carousel")
-			)
-			(require-all
-				(subpath "${HOME}/Library/BulletinDistributor/Attachments")
-				(signing-identifier "com.apple.Carousel")
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(require-any
+					(_g48 "")
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+				)
 			)
+			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.StreamingUnzipService")
+		(extension-class "com.apple.app-sandbox.read")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 		(require-any
 			(require-all
-				(signing-identifier "com.apple.appplaceholdersyncd")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
+				(%entitlement-is-present "com.apple.security.ts.tmpdir")
 				(require-any
 					(require-all
+						(extension-class "com.apple.app-sandbox.read")
+						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 							(require-all
+								(extension-class "com.apple.mediaserverd.read")
 								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
 								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
 							)
+							(require-any
+								(subpath "/AppleInternal/Applications")
+								(subpath "/System/Developer/Applications")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
+							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
 					)
+					(require-any
+						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					)
 				)
 			)
-			(require-all
-				(signing-identifier "com.apple.assistantd")
-				(subpath "${HOME}/Library/Caches/VoiceTrigger")
-			)
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.app-sandbox.read")
+		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(require-all
-				(subpath "${HOME}/Library/Application Support/com.apple.FaceTime/VideoMessaging/Outbox")
-				(signing-identifier "com.apple.facetimemessagestored")
-			)
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(signing-identifier "com.apple.FTLivePhotoService")
-			)
+			(_g81 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
+					(_g81 "")
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService/")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(require-all
-								(extension "com.apple.app-sandbox.read")
-								(signing-identifier "com.apple.FTLivePhotoService")
-							)
-							(require-all
-								(extension "com.apple.app-sandbox.read-write")
-								(signing-identifier "com.apple.FTLivePhotoService")
-							)
-						)
-					)
-					(require-all
-						(subpath "${HOME}/Library/Application Support/com.apple.FaceTime/VideoMessaging/Outbox")
-						(signing-identifier "com.apple.facetimemessagestored")
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
-				(extension "com.apple.app-sandbox.read")
-				(signing-identifier "com.apple.FTLivePhotoService")
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.FTLivePhotoService")
-			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(signing-identifier "com.apple.momentsd")
-		(require-any
-			(require-all
-				(extension-class "com.apple.app-sandbox.read-write")
-				(signing-identifier "com.apple.momentsd")
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+							(_g81 "")
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+				)
 			)
-			(subpath "${HOME}/Library/com.apple.momentsd")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.app-sandbox.read")
+		(extension "com.apple.sandbox.container")
 		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
-				(signing-identifier "com.apple.momentsd")
+				(extension-class "com.apple.mediaserverd.read-write")
 				(require-any
 					(require-all
-						(extension-class "com.apple.app-sandbox.read-write")
-						(signing-identifier "com.apple.momentsd")
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(extension "com.apple.security.exception.files.absolute-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+					)
+					(require-all
+						(extension "com.apple.security.exception.files.home-relative-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 					)
-					(subpath "${HOME}/Library/com.apple.momentsd")
 				)
 			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+		(signing-identifier "com.apple.storagedatad")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
 			(require-all
-				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
+					(_g27 "")
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
+						(subpath "/private/var")
 						(require-any
+							(_g27 "")
 							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(signing-identifier "com.apple.MTLAssetUpgraderD")
-							)
-							(require-all
-								(signing-identifier "com.apple.mediaplaybackd")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any
 									(require-all
-										(subpath "/private/var")
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+										(signing-identifier "com.apple.MTLAssetUpgraderD")
+									)
+									(require-all
+										(signing-identifier "com.apple.mediaplaybackd")
+										(require-any
+											(_g23 "")
+											(_g25 "")
+											(require-all
+												(subpath "/private/var")
+												(require-any
+													(_g25 "")
+													(require-all
+														(require-any
+															(subpath "${FRONT_USER_HOME}")
+															(subpath "${HOME}")
+														)
+														(require-any
+															(_g25 "")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+														)
+													)
+												)
+											)
+										)
 									)
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 								)
 							)
 						)
 					)
 					(require-all
-						(signing-identifier "com.apple.momentsd")
-						(require-any
-							(require-all
-								(extension-class "com.apple.app-sandbox.read-write")
-								(signing-identifier "com.apple.momentsd")
-								(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-							)
-							(subpath "${HOME}/Library/com.apple.momentsd")
-						)
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
 					)
 				)
 			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
-				(signing-identifier "com.apple.MTLAssetUpgraderD")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.cloudpaird")
 		(require-any
 			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
+				(extension-class "com.apple.app-sandbox.read")
 				(require-any
-					(signing-identifier "com.apple.FTLivePhotoService")
-					(signing-identifier "com.apple.announced")
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
 				)
+				(signing-identifier "com.apple.chronod")
 			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
-				(extension "com.apple.app-sandbox.read")
-				(signing-identifier "com.apple.FTLivePhotoService")
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.announced")
-			)
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension-class "com.apple.app-sandbox.read")
 		(signing-identifier "com.apple.geoanalyticsd")
-		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.identityservices.send")
 		(require-any
 			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.cameracaptured")
 				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.asktod")
-					(subpath "${HOME}/Library/com.apple.asktod")
+					(extension "com.apple.mediaserverd.read-write")
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.avconferenced")
+								(require-any
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(signing-identifier "com.apple.ClarityBoard")
+										(subpath "/private/var")
+										(subpath "${HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+									)
+									(require-any
+										(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
+										(subpath "/private/var/tmp/com.apple.avconferenced")
+									)
+								)
+							)
+							(require-all
+								(signing-identifier "com.apple.cameracaptured")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
 				)
-				(signing-identifier "com.apple.asktod")
-			)
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(signing-identifier "com.apple.asktod")
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.asktod")
 			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(signing-identifier "com.apple.cameracaptured")
-		(extension "com.apple.mediaserverd.read")
-	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.momentsd")
 		(require-any
+			(_g46 "")
 			(require-all
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.asktod")
-					(subpath "${HOME}/Library/com.apple.asktod")
+					(_g46 "")
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
 				)
-				(signing-identifier "com.apple.asktod")
-			)
-			(require-all
-				(subpath "${HOME}/Library/Application Support/com.apple.FaceTime/VideoMessaging/Outbox")
-				(signing-identifier "com.apple.facetimemessagestored")
-			)
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(signing-identifier "com.apple.facetimemessagestored")
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.facetimemessagestored")
 			)
+			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.corespotlightservice.read-write")
-		(signing-identifier "com.apple.health.records")
-		(subpath "${HOME}/Library/Caches/com.apple.health.records/com.apple.corespotlightservice")
-	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.StreamingUnzipService")
-		(signing-identifier "com.apple.appplaceholdersyncd")
+		(extension-class "com.apple.app-sandbox.read")
 		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
 		(require-any
 			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+				(subpath "${HOME}")
+				(signing-identifier "com.apple.Carousel")
 			)
 			(require-all
-				(subpath "/private/var/PersonaVolumes")
+				(subpath "${HOME}/Library/BulletinDistributor/Attachments")
 				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 					(require-all
+						(extension-class "com.apple.nsurlsessiond.readonly")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(require-all
+								(require-any
+									(subpath "${PROCESS_TEMP_DIR}/com.apple.anomalydetectiond")
+									(subpath "/private/var/tmp/com.apple.anomalydetectiond")
+								)
+								(signing-identifier "com.apple.anomalydetectiond")
+							)
+							(require-all
+								(subpath "${HOME}/Library/com.apple.momentsd")
+								(signing-identifier "com.apple.momentsd")
+							)
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
 					)
+					(signing-identifier "com.apple.Carousel")
 				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension-class "com.apple.app-sandbox.read-write")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 		(require-any
 			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
+				(%entitlement-is-present "com.apple.security.ts.tmpdir")
 				(require-any
 					(require-all
-						(extension-class "com.apple.mediaserverd.read-write")
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					)
-					(require-all
-						(subpath "${HOME}/Library/Mobile Documents")
-						(extension-class "com.apple.quicklook.readonly")
-					)
-					(require-all
-						(subpath "/private/var")
+						(extension-class "com.apple.app-sandbox.read")
+						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 						(require-any
 							(require-all
-								(extension-class "com.apple.mediaserverd.read-write")
-								(extension "com.apple.security.exception.files.home-relative-path.read-write")
-							)
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+								(extension-class "com.apple.mediaserverd.read")
 								(require-any
 									(require-all
-										(extension-class "com.apple.mediaserverd.read-write")
-										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(extension "com.apple.security.exception.files.absolute-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
 									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(extension-class "com.apple.aned.read-only")
-											(extension-class "com.apple.app-sandbox.read")
-											(extension-class "com.apple.app-sandbox.read-write")
-											(extension-class "com.apple.mediaserverd.read")
-											(extension-class "com.apple.mediaserverd.read-write")
-											(extension-class "com.apple.quicklook.readonly")
-											(extension-class "com.apple.sharing.airdrop.readonly")
-										)
+										(extension "com.apple.security.exception.files.home-relative-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
 								)
 							)
+							(require-any
+								(subpath "/AppleInternal/Applications")
+								(subpath "/System/Developer/Applications")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
+							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
 					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-						(extension-class "com.apple.quicklook.readonly")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-						(extension-class "com.apple.quicklook.readonly")
+					(require-any
+						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
 					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(extension "com.apple.app-sandbox.read-write")
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read-write")
-				(extension "com.apple.app-sandbox.read-write")
+				)
 			)
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(_g77 "")
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/private/var")
 				(require-any
-					(extension "com.apple.app-sandbox.read-write")
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+					(_g77 "")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(_g77 "")
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
 				)
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
-				(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			)
-			(require-all
-				(extension-class "com.apple.quicklook.readonly")
 				(require-any
 					(require-all
-						(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
-						(vnode-type REGULAR-FILE)
-						(extension "com.apple.clouddocs.version")
+						(extension "com.apple.security.exception.files.absolute-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+					)
+					(require-all
+						(extension "com.apple.security.exception.files.home-relative-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 					)
+				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(extension-class "com.apple.app-sandbox.read-write")
+				(require-any
+					(_g22 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
+							(_g22 "")
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(extension "com.apple.clouddocs.version")
+										(signing-identifier "com.apple.MTLAssetUpgraderD")
 									)
 									(require-all
-										(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-										(vnode-type REGULAR-FILE)
-										(extension "com.apple.clouddocs.version")
+										(signing-identifier "com.apple.mediaplaybackd")
+										(require-any
+											(_g18 "")
+											(_g20 "")
+											(require-all
+												(subpath "/private/var")
+												(require-any
+													(_g20 "")
+													(require-all
+														(require-any
+															(subpath "${FRONT_USER_HOME}")
+															(subpath "${HOME}")
+														)
+														(require-any
+															(_g20 "")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+														)
+													)
+												)
+											)
+										)
 									)
 								)
 							)
-							(require-all
-								(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
-								(vnode-type REGULAR-FILE)
-								(extension "com.apple.clouddocs.version")
-							)
 						)
 					)
 					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-						(vnode-type REGULAR-FILE)
-						(extension "com.apple.clouddocs.version")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-						(extension "com.apple.clouddocs.version")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
 					)
 				)
 			)
-			(require-all
-				(extension-class "com.apple.sharing.airdrop.readonly")
-				(extension "com.apple.app-sandbox.read-write")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.momentsd")
-		(subpath "${HOME}/Library/com.apple.momentsd")
+		(extension-class "com.apple.app-sandbox.read-write")
+		(signing-identifier "com.apple.cloudpaird")
+		(require-any
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(require-any
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+				)
+				(signing-identifier "com.apple.chronod")
+			)
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.app-sandbox.read-write")
+		(signing-identifier "com.apple.geoanalyticsd")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.cameracaptured")
 				(require-any
+					(extension "com.apple.mediaserverd.read-write")
 					(require-all
 						(extension-class "com.apple.mediaserverd.read")
 						(require-any
 							(require-all
-								(signing-identifier "com.apple.linkd")
+								(signing-identifier "com.apple.avconferenced")
 								(require-any
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(signing-identifier "com.apple.ClarityBoard")
+										(subpath "/private/var")
+										(subpath "${HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+									)
 									(require-any
-										(subpath "/AppleInternal/Applications")
-										(subpath "/System/Developer/Applications")
-										(subpath "/private/var/factory_mount/[^/]+/Applications")
-										(subpath "/private/var/personalized_automation/Applications")
-										(subpath "/private/var/personalized_debug/Applications")
-										(subpath "/private/var/personalized_factory/[^/]+/Applications")
+										(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
+										(subpath "/private/var/tmp/com.apple.avconferenced")
 									)
-									(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-									(subpath "/Applications")
-									(subpath "/Developer/Applications")
-									(subpath "/private/var/containers/Bundle")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.mediaplaybackd")
-								(require-any
-									(extension "com.apple.mediaserverd.read")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 								)
 							)
-						)
-					)
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(signing-identifier "com.apple.linkd")
-						(require-any
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-								(subpath "/private/var/factory_mount/[^/]+/Applications")
-								(subpath "/private/var/personalized_automation/Applications")
-								(subpath "/private/var/personalized_debug/Applications")
-								(subpath "/private/var/personalized_factory/[^/]+/Applications")
-							)
-							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-							(subpath "/Applications")
-							(subpath "/Developer/Applications")
-							(subpath "/private/var/containers/Bundle")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.momentsd")
-						(require-any
 							(require-all
-								(extension-class "com.apple.mediaserverd.read")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.linkd")
-										(require-any
-											(require-any
-												(subpath "/AppleInternal/Applications")
-												(subpath "/System/Developer/Applications")
-												(subpath "/private/var/factory_mount/[^/]+/Applications")
-												(subpath "/private/var/personalized_automation/Applications")
-												(subpath "/private/var/personalized_debug/Applications")
-												(subpath "/private/var/personalized_factory/[^/]+/Applications")
-											)
-											(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-											(subpath "/Applications")
-											(subpath "/Developer/Applications")
-											(subpath "/private/var/containers/Bundle")
-										)
-									)
-									(require-all
-										(signing-identifier "com.apple.mediaplaybackd")
-										(require-any
-											(extension "com.apple.mediaserverd.read")
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-										)
-									)
-								)
+								(signing-identifier "com.apple.cameracaptured")
+								(extension "com.apple.mediaserverd.read")
 							)
-							(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 						)
 					)
 				)
 			)
-			(require-all
-				(signing-identifier "com.apple.momentsd")
-				(subpath "${HOME}/Library/com.apple.momentsd")
-			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(signing-identifier "com.apple.momentsd")
 		(require-any
+			(_g45 "")
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(_g45 "")
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
 				)
 			)
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.corespotlightservice.read-write")
+		(signing-identifier "com.apple.health.records")
+		(subpath "${HOME}/Library/Caches/com.apple.health.records/com.apple.corespotlightservice")
+	)
+	(require-all
+		(extension-class "com.apple.identityservices.send")
 		(require-any
+			(_g3 "")
+			(_g4 "")
+			(_g6 "")
+			(_g8 "")
+			(_g9 "")
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+				(subpath "${HOME}/Library/UserNotifications")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
+			(require-all
+				(subpath "${PROCESS_TEMP_DIR}")
 				(require-any
+					(_g4 "")
 					(require-all
-						(%entitlement-is-present "com.apple.security.ts.tmpdir")
-						(require-any
-							(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-						)
+						(subpath "${PROCESS_TEMP_DIR}")
+						(signing-identifier "com.apple.internal.livtipsd")
 					)
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+					(require-all
+						(subpath "/private/var/tmp")
+						(signing-identifier "com.apple.internal.livtipsd")
+					)
+					(signing-identifier "com.apple.usernotificationsd")
 				)
 			)
 			(require-all
-				(extension "com.apple.sandbox.application-group")
+				(subpath "/private/var")
 				(require-any
+					(_g6 "")
 					(require-all
-						(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/BulletinDistributor")
 						(require-any
+							(_g6 "")
 							(require-all
-								(%entitlement-is-present "com.apple.security.ts.tmpdir")
+								(subpath "${FRONT_USER_HOME}")
 								(require-any
-									(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+									(_g6 "")
+									(require-all
+										(subpath "${PROCESS_TEMP_DIR}")
+										(require-any
+											(_g5 "")
+											(signing-identifier "com.apple.announced")
+										)
+									)
+									(require-all
+										(subpath "/private/var/tmp")
+										(signing-identifier "com.apple.announced")
+									)
+									(signing-identifier "com.apple.Carousel")
 								)
 							)
-							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 						)
 					)
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(_g9 "")
 					(require-all
-						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService/")
 						(require-any
+							(_g7 "")
+							(_g9 "")
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(_g7 "")
 									(require-all
-										(subpath "/private/var/PersonaVolumes")
+										(extension "com.apple.app-sandbox.read")
+										(signing-identifier "com.apple.FTLivePhotoService")
+									)
+									(require-all
+										(extension "com.apple.app-sandbox.read-write")
 										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-												(require-any
-													(require-all
-														(%entitlement-is-present "com.apple.security.ts.tmpdir")
-														(require-any
-															(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-															(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-														)
-													)
-													(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-												)
-											)
+											(_g5 "")
+											(_g7 "")
 										)
 									)
-									(subpath "${FRONT_USER_HOME}")
 								)
 							)
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-												(require-any
-													(require-all
-														(%entitlement-is-present "com.apple.security.ts.tmpdir")
-														(require-any
-															(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-															(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-														)
-													)
-													(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-												)
-											)
-										)
-									)
-								)
+								(subpath "${PROCESS_TEMP_DIR}")
+								(signing-identifier "com.apple.facetimemessagestored")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/tmp")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(_g12 "")
+			(require-all
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(_g12 "")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(_g12 "")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+								(signing-identifier "com.apple.storagedatad")
 							)
 						)
 					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
+			(_g14 "")
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
+				(extension-class "com.apple.aned.read-only")
 				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
 				)
+				(signing-identifier "com.apple.chronod")
 			)
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(require-any
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
+				(extension-class "com.apple.mediaserverd.read")
 				(require-any
 					(require-all
-						(extension-class "com.apple.app-sandbox.read")
-						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 						(require-any
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-								(subpath "/private/var/factory_mount/[^/]+/Applications")
-								(subpath "/private/var/personalized_automation/Applications")
-								(subpath "/private/var/personalized_debug/Applications")
-								(subpath "/private/var/personalized_factory/[^/]+/Applications")
-							)
-							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-							(subpath "/Applications")
-							(subpath "/Developer/Applications")
-							(subpath "/private/var/containers/Bundle")
+							(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
 						)
+						(signing-identifier "com.apple.chronod")
 					)
-					(require-any
-						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+						(signing-identifier "com.apple.chronod")
 					)
 				)
 			)
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(require-any
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
+				(signing-identifier "com.apple.cloudpaird")
 				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(_g14 "")
+					(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 				)
 			)
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 		)
 	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(extension "com.apple.sandbox.executable")
-	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(extension "com.apple.sandbox.application-group")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
+			(_g43 "")
 			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
+				(signing-identifier "com.apple.anomalydetectiond")
+				(require-any
+					(_g43 "")
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
+			(_g55 "")
 			(require-all
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-					(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-				)
+				(extension-class "com.apple.aned.read-only")
+				(signing-identifier "com.apple.momentsd")
+				(_g54 "")
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(signing-identifier "com.apple.momentsd")
+				(_g54 "")
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(require-any
+					(_g53 "")
+					(_g58 "")
+					(_g59 "")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+						(extension-class "com.apple.app-sandbox.read")
+						(signing-identifier "com.apple.mediaplaybackd")
+						(_g57 "")
+					)
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
 						(require-any
-							(extension "com.apple.security.exception.files.absolute-path.read-only")
-							(extension "com.apple.security.exception.files.absolute-path.read-write")
-							(extension "com.apple.security.exception.files.home-relative-path.read-only")
-							(extension "com.apple.security.exception.files.home-relative-path.read-write")
+							(_g51 "")
+							(_g58 "")
 							(require-all
-								(extension "com.apple.assets.read")
-								(require-any
-									(require-all
-										(subpath "${HOME}/Library/Assets")
-										(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-									)
-									(require-all
-										(subpath "/private/var/MobileAsset")
-										(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-									)
-								)
+								(signing-identifier "com.apple.mediaplaybackd")
+								(_g52 "")
 							)
 						)
 					)
 					(require-all
-						(extension "com.apple.assets.read")
+						(extension-class "com.apple.mediaserverd.read")
+						(signing-identifier "com.apple.linkd")
+						(_g50 "")
+					)
+					(require-all
+						(extension-class "com.apple.mediaserverd.read-write")
 						(require-any
+							(_g56 "")
+							(_g59 "")
 							(require-all
-								(subpath "${HOME}/Library/Assets")
-								(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-							)
-							(require-all
-								(subpath "/private/var/MobileAsset")
-								(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+								(signing-identifier "com.apple.mediaplaybackd")
+								(_g57 "")
 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.momentsd")
+						(_g54 "")
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.momentsd")
+				(_g54 "")
+			)
+			(require-all
+				(signing-identifier "com.apple.momentsd")
+				(require-any
+					(_g55 "")
+					(require-all
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(require-any
+							(_g55 "")
+							(extension-class "com.apple.mediaserverd.read")
+							(extension-class "com.apple.mediaserverd.read-write")
+						)
+					)
+					(subpath "${HOME}/Library/com.apple.momentsd")
 				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
+			(_g60 "")
+			(_g64 "")
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+				(extension-class "com.apple.mediaserverd.read")
 				(require-any
+					(_g62 "")
 					(require-all
-						(%entitlement-is-present "com.apple.security.ts.tmpdir")
+						(extension-class "com.apple.mediaserverd.read-write")
 						(require-any
-							(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+							(_g60 "")
+							(_g61 "")
 						)
 					)
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
-				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(require-all
+						(signing-identifier "com.apple.cameracaptured")
+						(_g63 "")
+					)
 				)
 			)
 			(require-all
-				(extension "com.apple.sandbox.container")
+				(signing-identifier "com.apple.geoanalyticsd")
 				(require-any
-					(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-					(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+					(_g64 "")
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 				)
 			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(_g90 "")
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension "com.apple.sandbox.application-group")
 				(require-any
+					(_g90 "")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+						(subpath "/private/var")
 						(require-any
+							(_g90 "")
 							(require-all
-								(extension-class "com.apple.mediaserverd.read")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 								(require-any
-									(require-all
-										(extension "com.apple.security.exception.files.absolute-path.read-only")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-									(require-all
-										(extension "com.apple.security.exception.files.home-relative-path.read-only")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-									(require-all
-										(extension "com.apple.security.exception.files.home-relative-path.read-write")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
+									(_g90 "")
+									(subpath "${FRONT_USER_HOME}")
 								)
 							)
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-								(subpath "/private/var/factory_mount/[^/]+/Applications")
-								(subpath "/private/var/personalized_automation/Applications")
-								(subpath "/private/var/personalized_debug/Applications")
-								(subpath "/private/var/personalized_factory/[^/]+/Applications")
-							)
-							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-							(subpath "/Applications")
-							(subpath "/Developer/Applications")
-							(subpath "/private/var/containers/Bundle")
 						)
 					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.application-group")
+				(_g91 "")
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.application-group")
+				(_g91 "")
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(_g95 "")
+			(_g96 "")
+			(require-all
+				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+				(require-any
+					(_g96 "")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+				)
+			)
+			(require-all
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+					(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 					(require-all
-						(extension-class "com.apple.mediaserverd.read")
+						(extension-class "com.apple.mediaserverd.read-write")
 						(require-any
 							(require-all
-								(extension "com.apple.security.exception.files.absolute-path.read-only")
-								(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-							)
-							(require-all
-								(extension "com.apple.security.exception.files.home-relative-path.read-only")
-								(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								(extension "com.apple.security.exception.files.absolute-path.read-write")
+								(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 							)
 							(require-all
 								(extension "com.apple.security.exception.files.home-relative-path.read-write")
-								(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 							)
 						)
 					)
 				)
 			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.mediaserverd.read-write")
-		(require-any
 			(require-all
-				(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+				(extension-class "com.apple.aned.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+				(_g94 "")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(_g93 "")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+						(_g94 "")
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
 				(require-any
+					(_g92 "")
+					(_g97 "")
 					(require-all
-						(signing-identifier "com.apple.avconferenced")
+						(extension "com.apple.security.exception.files.absolute-path.read-write")
 						(require-any
-							(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
-							(subpath "/private/var/tmp/com.apple.avconferenced")
+							(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+							(_g97 "")
 						)
 					)
-					(signing-identifier "com.apple.anomalydetectiond")
 				)
 			)
-			(signing-identifier "com.apple.cameracaptured")
-			(signing-identifier "com.apple.mediaplaybackd")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
+			(_g98 "")
 			(require-all
-				(extension "com.apple.sandbox.application-group")
+				(extension "com.apple.sandbox.container")
 				(require-any
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.security.ts.tmpdir")
-										(require-any
-											(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-											(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-										)
-									)
-									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-								)
-							)
-							(require-all
-								(subpath "/private/var")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.security.ts.tmpdir")
-												(require-any
-													(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-													(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-												)
-											)
-											(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-										)
-									)
-									(require-all
-										(extension "com.apple.sandbox.application-group")
-										(require-any
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																(require-any
-																	(require-all
-																		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																		(require-any
-																			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																		)
-																	)
-																	(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																)
-															)
-														)
-													)
-												)
-											)
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(require-any
-																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																				(require-any
-																					(require-all
-																						(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																						(require-any
-																							(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																						)
-																					)
-																					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																				)
-																			)
-																		)
-																	)
-																)
-															)
-														)
-													)
-												)
-											)
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																		(require-any
-																			(require-all
-																				(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																				(require-any
-																					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																				)
-																			)
-																			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																		)
-																	)
-																)
-															)
-														)
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var")
-						(require-any
-							(require-all
-								(extension-class "com.apple.mediaserverd.read")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.security.ts.tmpdir")
-												(require-any
-													(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-													(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-												)
-											)
-											(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-										)
-									)
-									(require-all
-										(subpath "/private/var")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-												(require-any
-													(require-all
-														(%entitlement-is-present "com.apple.security.ts.tmpdir")
-														(require-any
-															(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-															(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-														)
-													)
-													(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-												)
-											)
-											(require-all
-												(extension "com.apple.sandbox.application-group")
-												(require-any
-													(require-all
-														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																		(require-any
-																			(require-all
-																				(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																				(require-any
-																					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																				)
-																			)
-																			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																		)
-																	)
-																)
-															)
-														)
-													)
-													(require-all
-														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "${FRONT_USER_HOME}")
-																		(require-any
-																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "/private/var/PersonaVolumes")
-																				(require-any
-																					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					(require-all
-																						(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																						(require-any
-																							(require-all
-																								(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																								(require-any
-																									(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																								)
-																							)
-																							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																						)
-																					)
-																				)
-																			)
-																		)
-																	)
-																)
-															)
-														)
-													)
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(require-any
-																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																				(require-any
-																					(require-all
-																						(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																						(require-any
-																							(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																						)
-																					)
-																					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																				)
-																			)
-																		)
-																	)
-																)
-															)
-														)
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-								(require-any
-									(require-all
-										(extension-class "com.apple.mediaserverd.read")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-												(require-any
-													(require-all
-														(%entitlement-is-present "com.apple.security.ts.tmpdir")
-														(require-any
-															(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-															(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-														)
-													)
-													(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-												)
-											)
-											(require-all
-												(subpath "/private/var")
-												(require-any
-													(require-all
-														(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-														(require-any
-															(require-all
-																(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																(require-any
-																	(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																	(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																)
-															)
-															(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-														)
-													)
-													(require-all
-														(extension "com.apple.sandbox.application-group")
-														(require-any
-															(require-all
-																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(require-any
-																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																				(require-any
-																					(require-all
-																						(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																						(require-any
-																							(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																						)
-																					)
-																					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																				)
-																			)
-																		)
-																	)
-																)
-															)
-															(require-all
-																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(require-any
-																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "${FRONT_USER_HOME}")
-																				(require-any
-																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					(require-all
-																						(subpath "/private/var/PersonaVolumes")
-																						(require-any
-																							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																							(require-all
-																								(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																								(require-any
-																									(require-all
-																										(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																										(require-any
-																											(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																											(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																										)
-																									)
-																									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																								)
-																							)
-																						)
-																					)
-																				)
-																			)
-																		)
-																	)
-																)
-															)
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "${FRONT_USER_HOME}")
-																		(require-any
-																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "/private/var/PersonaVolumes")
-																				(require-any
-																					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					(require-all
-																						(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																						(require-any
-																							(require-all
-																								(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																								(require-any
-																									(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																								)
-																							)
-																							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																						)
-																					)
-																				)
-																			)
-																		)
-																	)
-																)
-															)
-														)
-													)
-												)
-											)
-										)
-									)
-									(subpath "${FRONT_USER_HOME}")
-								)
-							)
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+					(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+					(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+					(_g98 "")
 				)
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(require-any
+					(_g99 "")
 					(require-all
-						(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.security.ts.tmpdir")
-								(require-any
-									(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-								)
-							)
-							(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+							(_g99 "")
+							(extension "com.apple.security.exception.files.absolute-path.read-only")
+							(extension "com.apple.security.exception.files.absolute-path.read-write")
+							(extension "com.apple.security.exception.files.home-relative-path.read-only")
+							(extension "com.apple.security.exception.files.home-relative-path.read-write")
 						)
 					)
+				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(require-any
+			(require-all
+				(%entitlement-is-present "com.apple.security.ts.tmpdir")
+				(require-any
 					(require-all
-						(subpath "/private/var")
+						(extension-class "com.apple.app-sandbox.read")
+						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 						(require-any
 							(require-all
-								(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.security.ts.tmpdir")
-										(require-any
-											(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-											(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-										)
-									)
-									(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-								)
-							)
-							(require-all
-								(extension "com.apple.sandbox.application-group")
+								(extension-class "com.apple.mediaserverd.read")
 								(require-any
 									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-														(require-any
-															(require-all
-																(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																(require-any
-																	(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																	(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																)
-															)
-															(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-														)
-													)
-												)
-											)
-										)
+										(extension "com.apple.security.exception.files.absolute-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
 									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																		(require-any
-																			(require-all
-																				(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																				(require-any
-																					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																				)
-																			)
-																			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																		)
-																	)
-																)
-															)
-														)
-													)
-												)
-											)
-										)
+										(extension "com.apple.security.exception.files.home-relative-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
 									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-																(require-any
-																	(require-all
-																		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-																		(require-any
-																			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-																		)
-																	)
-																	(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-																)
-															)
-														)
-													)
-												)
-											)
-										)
+										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
 								)
 							)
+							(require-any
+								(subpath "/AppleInternal/Applications")
+								(subpath "/System/Developer/Applications")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
+							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
 					)
+					(require-any
+						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					)
 				)
 			)
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
+			(_g85 "")
 			(require-all
 				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(_g85 "")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(_g85 "")
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+				)
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(extension "com.apple.sandbox.application-group")

 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.application-group")
+		(extension-class "com.apple.mediaserverd.read-write")
+		(extension "com.apple.sandbox.container")
 		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-any
+					(require-all
+						(extension "com.apple.security.exception.files.absolute-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+					)
+					(require-all
+						(extension "com.apple.security.exception.files.home-relative-path.read-write")
+						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+					)
+				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sandbox.container-proxy")
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
-			(extension "com.apple.sandbox.application-group")
 			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
+				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
+					(_g32 "")
 					(require-all
+						(subpath "/private/var")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(_g32 "")
 							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(signing-identifier "com.apple.MTLAssetUpgraderD")
+									)
+									(require-all
+										(signing-identifier "com.apple.mediaplaybackd")
+										(require-any
+											(_g28 "")
+											(_g30 "")
+											(require-all
+												(subpath "/private/var")
+												(require-any
+													(_g30 "")
+													(require-all
+														(require-any
+															(subpath "${FRONT_USER_HOME}")
+															(subpath "${HOME}")
+														)
+														(require-any
+															(_g30 "")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+														)
+													)
+												)
+											)
+										)
+									)
 								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
 							)
 						)
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
 				)
 			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.quicklook.readonly")
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(signing-identifier "com.apple.ClarityBoard")
-		(subpath "/private/var")
-		(subpath "${HOME}")
 		(require-any
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-			)
-			(require-all
-				(extension-class "com.apple.quicklook.readonly")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-			)
-			(require-all
-				(extension-class "com.apple.usernotifications.attachments.read-only")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+				(require-any
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+				)
+				(signing-identifier "com.apple.chronod")
 			)
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.sandbox.application-group")
+		(signing-identifier "com.apple.geoanalyticsd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.cameracaptured")
+				(require-any
+					(extension "com.apple.mediaserverd.read-write")
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.avconferenced")
+								(require-any
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(signing-identifier "com.apple.ClarityBoard")
+										(subpath "/private/var")
+										(subpath "${HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+									)
+									(require-any
+										(subpath "${PROCESS_TEMP_DIR}/com.apple.avconferenced")
+										(subpath "/private/var/tmp/com.apple.avconferenced")
+									)
+								)
+							)
+							(require-all
+								(signing-identifier "com.apple.cameracaptured")
+								(extension "com.apple.mediaserverd.read")
+							)
+						)
+					)
+				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		(require-any
-			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(signing-identifier "com.apple.momentsd")
-		(subpath "${HOME}/Library/com.apple.momentsd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
 		(require-any
+			(_g47 "")
 			(require-all
-				(signing-identifier "com.apple.geoanalyticsd")
-				(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-			)
-			(require-all
-				(subpath "${HOME}/Library/com.apple.momentsd")
-				(signing-identifier "com.apple.momentsd")
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(require-any
+					(_g47 "")
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+				)
 			)
+			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(signing-identifier "com.apple.SurfBoard")
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(require-any
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-			)
-			(require-all
-				(extension-class "com.apple.quicklook.readonly")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-			)
-			(require-all
-				(extension-class "com.apple.usernotifications.attachments.read-only")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-			)
-		)
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(extension "com.apple.sandbox.executable")
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all
-				(extension-class "com.apple.aned.read-only")
-				(signing-identifier "com.apple.anomalydetectiond")
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(signing-identifier "com.apple.anomalydetectiond")
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read-write")
-				(signing-identifier "com.apple.anomalydetectiond")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(signing-identifier "com.apple.anomalydetectiond")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(signing-identifier "com.apple.anomalydetectiond")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")
 		(require-any
+			(_g15 "")
 			(require-all
+				(signing-identifier "com.apple.diagnosticextensionsd")
 				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/com.apple.anomalydetectiond")
-					(subpath "/private/var/tmp/com.apple.anomalydetectiond")
+					(_g15 "")
+					(subpath "${HOME}/Library/Logs/com.apple.diagnosticextensionsd")
 				)
-				(signing-identifier "com.apple.anomalydetectiond")
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.geoanalyticsd")
+				(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 			)
 			(require-all
 				(subpath "${HOME}/Library/com.apple.momentsd")

 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.usernotifications.attachments.read-only")
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(signing-identifier "com.apple.geoanalyticsd")
+		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+	)
+	(require-all
+		(extension-class "com.apple.quicklook.readonly")
+		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(require-all
-				(subpath "${HOME}/Library/BulletinDistributor/Attachments")
-				(signing-identifier "com.apple.Carousel")
-			)
 			(require-all
 				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-						(subpath "${HOME}")
-						(signing-identifier "com.apple.Carousel")
-					)
-					(require-all
-						(subpath "${HOME}/Library/BulletinDistributor/Attachments")
-						(signing-identifier "com.apple.Carousel")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")
 		(extension "com.apple.sandbox.container")

 			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 		)
 	)
-)
-(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.quicklook.readonly")
+		(signing-identifier "com.apple.ClarityBoard")
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+	)
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")
 		(subpath "/private/var")

 			)
 			(require-all
 				(subpath "${HOME}/Library/BulletinDistributor/Attachments")
-				(signing-identifier "com.apple.Carousel")
+				(require-any
+					(require-all
+						(extension-class "com.apple.nsurlsessiond.readonly")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${PROCESS_TEMP_DIR}/com.apple.anomalydetectiond")
+									(subpath "/private/var/tmp/com.apple.anomalydetectiond")
+								)
+								(signing-identifier "com.apple.anomalydetectiond")
+							)
+							(require-all
+								(subpath "${HOME}/Library/com.apple.momentsd")
+								(signing-identifier "com.apple.momentsd")
+							)
+						)
+					)
+					(signing-identifier "com.apple.Carousel")
+				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension-class "com.apple.sandbox.container-proxy")
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
 		(require-any
+			(extension "com.apple.sandbox.application-group")
 			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
 				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/com.apple.anomalydetectiond")
-					(subpath "/private/var/tmp/com.apple.anomalydetectiond")
+					(_g13 "")
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(_g13 "")
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						)
+					)
 				)
-				(signing-identifier "com.apple.anomalydetectiond")
 			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension "com.apple.sandbox.application-group")
+		(require-any
 			(require-all
-				(signing-identifier "com.apple.diagnosticextensionsd")
-				(subpath "${HOME}/Library/Logs/com.apple.diagnosticextensionsd")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.sandbox.container")
+		(extension-class "com.apple.spotlight-indexable")
+		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.usernotifications.attachments.read-only")
+		(require-any
+			(_g17 "")
+			(require-all
+				(subpath "/private/var")
 				(require-any
+					(_g17 "")
 					(require-all
-						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-					(require-all
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+						(subpath "${HOME}")
+						(signing-identifier "com.apple.Carousel")
 					)
 				)
 			)
 		)
 	)
-)
-(allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.spotlight-indexable")
+		(extension-class "com.apple.usernotifications.attachments.read-only")
+		(signing-identifier "com.apple.ClarityBoard")
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+	)
+	(require-all
+		(extension-class "com.apple.wcd.readonly")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all

 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
+	(require-all
+		(signing-identifier "com.apple.SurfBoard")
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(require-any
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+			)
+			(require-all
+				(extension-class "com.apple.quicklook.readonly")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+			)
+			(require-all
+				(extension-class "com.apple.usernotifications.attachments.read-only")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+			)
+		)
+	)
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		(require-any
+			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.mediaserverd.read-write")
+		)
+	)
+	(require-all
+		(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(signing-identifier "com.apple.anomalydetectiond")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.anomalydetectiond")
+			)
+		)
+	)
 )
-(allow file-issue-extension
+)
+(deny file-issue-extension
+	(require-any
 	(require-all
-		(extension-class "com.apple.wcd.readonly")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
 				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 				(subpath "${FRONT_USER_HOME}")
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-)
-(deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))
 		(require-not (extension "com.apple.app-sandbox.read-write"))

 		)
 	)
 )
-(deny file-issue-extension
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
 )
 
 (allow file-link)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
+		(literal "${FRONT_USER_HOME}")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
-		(process-attribute is-apple-signed-executable)
+		(subpath "/System/Library/Carrier Bundles")
+		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
+		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
-		(literal "${FRONT_USER_HOME}")
+		(subpath "/private/var/containers/Data/System/com.apple.geod")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
 (allow file-read-metadata

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 		(extension "com.apple.clouddocs.version")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(literal "/private/var/preferences/com.apple.security.plist")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var/containers/Data/System/com.apple.geod")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow file-read-metadata

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.airplayd")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")

 		(literal "/dev/bpf*")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.audiomxd")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.mediaserverd.read-write")

 )
 (allow file-read-metadata
 	(require-all
+		(signing-identifier "com.apple.audiomxd")
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.airplayd")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
+		(signing-identifier "com.apple.usernotificationsd")
+		(literal "${HOME}/Library/PPTDevice")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
+		(signing-identifier "com.apple.tursd")
 		(require-any
 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
 		)
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(subpath "/private/var")
 		(require-any
-			(extension "com.apple.sandbox.application-group")
 			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-							)
-						)
-					)
-				)
+				(signing-identifier "com.apple.tursd")
+				(subpath "${FRONT_USER_HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+			)
+			(require-all
+				(subpath "/private/var/log")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/tmp/powerlog")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/wireless/Library/Logs")
+				(signing-identifier "com.apple.storagedatad")
 			)
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+			(subpath "${FRONT_USER_HOME}/Library/AddressBook")
+			(subpath "${FRONT_USER_HOME}/Library/Contacts")
+			(subpath "${FRONT_USER_HOME}/Library/Health")
+			(subpath "${FRONT_USER_HOME}/Library/Mail")
+			(subpath "${FRONT_USER_HOME}/Library/NanoMailKit")
+			(subpath "${FRONT_USER_HOME}/Library/NanoPhotos")
+			(subpath "${FRONT_USER_HOME}/Library/Passes")
+			(subpath "${FRONT_USER_HOME}/Library/Recordings")
+			(subpath "${FRONT_USER_HOME}/Library/Reminders")
+			(subpath "${FRONT_USER_HOME}/Library/SMS")
+			(subpath "${FRONT_USER_HOME}/Library/Safari")
+			(subpath "${FRONT_USER_HOME}/Media/Books")
+			(subpath "${FRONT_USER_HOME}/Media/Downloads")
+			(subpath "${FRONT_USER_HOME}/Media/Recordings")
+			(subpath "${FRONT_USER_HOME}/Media/iTunes_Control")
 		)
+		(signing-identifier "com.apple.storagedatad")
 	)
 )
 (allow file-read-metadata

 		(signing-identifier "com.apple.MTLAssetUpgraderD")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
+(allow file-read-metadata
+	(require-all
+		(system-attribute developer-mode)
+		(literal "/mach.*")
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.dmd")
+		(vnode-type DIRECTORY REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
 			(require-all
-				(subpath "/private/var")
+				(extension "com.apple.revisiond.staging")
 				(require-any
 					(require-all
-						(extension "com.apple.sandbox.container")
 						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-										)
-									)
-								)
-							)
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)
+						(extension "com.apple.revisiond.revision")
+						(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					(require-any
+						(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+						(subpath "/private/var/.DocumentRevisions-V100/staging")
+						(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 					)
 				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.momentsd")
-		(require-any
 			(require-all
-				(vnode-type DIRECTORY)
 				(require-any
-					(require-any
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-						(subpath "${HOME}/Library/com.apple.momentsd")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-				(subpath "${HOME}/Library/com.apple.momentsd")
+				(extension "com.apple.revisiond.revision")
+				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 			)
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/Applications")
 		(require-any
-			(signing-identifier "com.apple.managedappdistributiond")
-			(signing-identifier "com.apple.storekitd")
+			(subpath "${FRONT_USER_HOME}/Library/Notes")
+			(subpath "${FRONT_USER_HOME}/Library/Voicemail")
 		)
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
+		(subpath "${PROCESS_TEMP_DIR}/powerlog")
+		(signing-identifier "com.apple.storagedatad")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/Developer/Applications")
+		(subpath "/private/var/containers/Bundle")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.cameracaptured")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
+		(subpath "/private/var")
 		(require-any
 			(require-all
-				(vnode-type DIRECTORY)
+				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.storagedatad")
+					)
 				)
 			)
 			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
 			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.linkd")
+		(extension "com.apple.assets.read")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+				(subpath "/private/var/MobileAsset")
 			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var/containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.mediaserverd.read")
+		(subpath "/Applications")
 		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.managedappdistributiond")
+			(signing-identifier "com.apple.storekitd")
 		)
 	)
 )

 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.mediaserverd.read")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(signing-identifier "com.apple.tursd")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(signing-identifier "com.apple.wapic")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.client")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.wapic")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(literal "${HOME}/Library")
+			(literal "${HOME}/Library/Mobile Documents")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(literal "${HOME}/Library")
-			(literal "${HOME}/Library/Mobile Documents")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(literal "${HOME}/Library/Preferences")

 		(signing-identifier "com.apple.geoanalyticsd")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		(signing-identifier "com.apple.geoanalyticsd")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")

 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		(signing-identifier "com.apple.geoanalyticsd")
+		)
 	)
 )
 (allow file-read-metadata

 		(signing-identifier "com.apple.anomalydetectiond")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "${HOME}/Library/PPTDevice")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.FTLivePhotoService")
+				(signing-identifier "com.apple.announced")
+			)
+			(signing-identifier "com.apple.Carousel")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(literal "${HOME}/Library/PPTDevice")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.FTLivePhotoService")
-				(signing-identifier "com.apple.announced")
-			)
-			(signing-identifier "com.apple.Carousel")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(signing-identifier "com.apple.cloudpaird")

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
-		)
+		(signing-identifier "com.apple.internal.livtipsd")
+		(literal "${HOME}/Library/PPTDevice")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(extension "com.apple.assets.read")
+		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
 			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(vnode-type DIRECTORY)
 				(require-any
-					(subpath "${HOME}/Library/Assets")
-					(subpath "/private/var/MobileAsset")
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
 			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.storagedatad")
+		(subpath "/private/var")
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
 			(require-all
-				(subpath "/private/var")
+				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
 				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
 			)
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/powerlog")
-		(signing-identifier "com.apple.storagedatad")
+		(signing-identifier "com.apple.momentsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(require-any
+					(require-any
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(subpath "${HOME}/Library/com.apple.momentsd")
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+				)
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(subpath "${HOME}/Library/com.apple.momentsd")
+			)
+		)
 	)
 )
 (allow file-read-metadata
 	(require-all
+		(signing-identifier "com.apple.linkd")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Notes")
-			(subpath "${FRONT_USER_HOME}/Library/Voicemail")
+			(require-any
+				(subpath "/AppleInternal/Applications")
+				(subpath "/System/Developer/Applications")
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
 		)
-		(signing-identifier "com.apple.storagedatad")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.usernotificationsd")
-		(literal "${HOME}/Library/PPTDevice")
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(signing-identifier "com.apple.dmd")
 		(require-any
 			(require-all
-				(extension "com.apple.revisiond.staging")
+				(subpath "/private/var")
 				(require-any
 					(require-all
+						(extension "com.apple.sandbox.container")
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+										)
+									)
+								)
+							)
 						)
-						(extension "com.apple.revisiond.revision")
-						(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 					)
-					(require-any
-						(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-						(subpath "/private/var/.DocumentRevisions-V100/staging")
-						(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 					)
 				)
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(vnode-type DIRECTORY)
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(literal "${HOME}/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+			)
+			(require-all
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+			)
 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.tursd")
+		(signing-identifier "com.apple.storagedatad")
 		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+			)
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(vnode-type DIRECTORY)
+		(require-any
+			(require-all
+				(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+$")
+				(subpath "${FRONT_USER_HOME}")
+				(process-attribute is-apple-signed-executable)
+			)
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
 )

 		(subpath "/private/var")
 		(require-any
 			(require-all
-				(signing-identifier "com.apple.tursd")
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-			)
-			(require-all
-				(subpath "/private/var/log")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/tmp/powerlog")
-				(signing-identifier "com.apple.storagedatad")
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
 			)
 			(require-all
-				(subpath "/private/var/wireless/Library/Logs")
-				(signing-identifier "com.apple.storagedatad")
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
 			)
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(system-attribute developer-mode)
-		(literal "/mach.*")
-		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+		(signing-identifier "com.apple.cameracaptured")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/AddressBook")
-			(subpath "${FRONT_USER_HOME}/Library/Contacts")
-			(subpath "${FRONT_USER_HOME}/Library/Health")
-			(subpath "${FRONT_USER_HOME}/Library/Mail")
-			(subpath "${FRONT_USER_HOME}/Library/NanoMailKit")
-			(subpath "${FRONT_USER_HOME}/Library/NanoPhotos")
-			(subpath "${FRONT_USER_HOME}/Library/Passes")
-			(subpath "${FRONT_USER_HOME}/Library/Recordings")
-			(subpath "${FRONT_USER_HOME}/Library/Reminders")
-			(subpath "${FRONT_USER_HOME}/Library/SMS")
-			(subpath "${FRONT_USER_HOME}/Library/Safari")
-			(subpath "${FRONT_USER_HOME}/Media/Books")
-			(subpath "${FRONT_USER_HOME}/Media/Downloads")
-			(subpath "${FRONT_USER_HOME}/Media/Recordings")
-			(subpath "${FRONT_USER_HOME}/Media/iTunes_Control")
+			(extension "com.apple.sandbox.application-group")
+			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
 		)
-		(signing-identifier "com.apple.storagedatad")
 	)
 )
 (allow file-read-metadata

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(vnode-type DIRECTORY)
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(literal "${HOME}/Library/Mobile Documents")
-				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-			)
-			(require-all
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(extension "com.apple.revisiond.revision")
-				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-			)
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(vnode-type SYMLINK)

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(vnode-type DIRECTORY)
-		(require-any
-			(require-all
-				(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
-				(process-attribute is-apple-signed-executable)
-			)
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+$")
-				(subpath "${FRONT_USER_HOME}")
-				(process-attribute is-apple-signed-executable)
-			)
-		)
-	)
-)
 (allow file-read-metadata
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")

 	(require-all
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(require-any
+			(require-any
+				(signing-identifier "com.apple.mediaplaybackd")
+				(signing-identifier "com.apple.videocodecd")
+			)
 			(signing-identifier "com.apple.airplayd")
 			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(signing-identifier "com.apple.videocodecd")
 		)
 	)
 )

 						(signing-identifier "com.apple.FTLivePhotoService")
 						(signing-identifier "com.apple.announced")
 					)
+					(require-any
+						(signing-identifier "com.apple.internal.livtipsd")
+						(signing-identifier "com.apple.usernotificationsd")
+					)
 					(signing-identifier "com.apple.Carousel")
 					(signing-identifier "com.apple.asktod")
 					(signing-identifier "com.apple.facetimemessagestored")
-					(signing-identifier "com.apple.usernotificationsd")
 				)
 			)
 			(require-all

 						(signing-identifier "com.apple.FTLivePhotoService")
 						(signing-identifier "com.apple.announced")
 					)
+					(require-any
+						(signing-identifier "com.apple.internal.livtipsd")
+						(signing-identifier "com.apple.usernotificationsd")
+					)
 					(signing-identifier "com.apple.Carousel")
 					(signing-identifier "com.apple.asktod")
 					(signing-identifier "com.apple.facetimemessagestored")
-					(signing-identifier "com.apple.usernotificationsd")
 				)
 			)
 			(require-all

 				(signing-identifier "com.apple.FTLivePhotoService")
 				(signing-identifier "com.apple.announced")
 			)
+			(require-any
+				(signing-identifier "com.apple.internal.livtipsd")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
 			(signing-identifier "com.apple.Carousel")
 			(signing-identifier "com.apple.asktod")
 			(signing-identifier "com.apple.facetimemessagestored")
-			(signing-identifier "com.apple.usernotificationsd")
 		)
 	)
 )

 				(signing-identifier "com.apple.FTLivePhotoService")
 				(signing-identifier "com.apple.announced")
 			)
+			(require-any
+				(signing-identifier "com.apple.internal.livtipsd")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
 			(signing-identifier "com.apple.Carousel")
 			(signing-identifier "com.apple.asktod")
 			(signing-identifier "com.apple.facetimemessagestored")
-			(signing-identifier "com.apple.usernotificationsd")
 		)
 	)
 )

 
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.itunescloudd.xpc")
-		(signing-identifier "com.apple.siriknowledged")
+		(global-name "com.apple.chrono.event-service.*")
+		(signing-identifier "com.apple.chronod")
 	)
 )
 (allow mach-lookup

 		(signing-identifier "com.apple.tursd")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
-		(signing-identifier "com.apple.usernotificationsd")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.marco")
-		(signing-identifier "com.apple.usernotificationsd")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
+		(global-name "com.apple.marco")
 		(require-any
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
+			(signing-identifier "com.apple.internal.livtipsd")
+			(signing-identifier "com.apple.usernotificationsd")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.chrono.event-service.*")
-		(signing-identifier "com.apple.chronod")
+		(global-name "com.apple.itunescloudd.xpc")
+		(signing-identifier "com.apple.siriknowledged")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(require-any
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-		)
+		(global-name "com.apple.marco")
+		(signing-identifier "com.apple.Carousel")
 	)
 )
 (allow mach-lookup

 		(signing-identifier "com.apple.chronod")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.marco")
-		(signing-identifier "com.apple.Carousel")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
-		(signing-identifier "com.apple.facetimemessagestored")
+		(require-any
+			(signing-identifier "com.apple.internal.livtipsd")
+			(signing-identifier "com.apple.usernotificationsd")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.networkscored")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(global-name "com.apple.identityservicesd.embedded.auth")
+		(signing-identifier "com.apple.facetimemessagestored")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.DiagnosticExtensions.*")
-		(signing-identifier "com.apple.diagnosticextensionsd")
+		(global-name "com.apple.marco")
+		(signing-identifier "com.apple.facetimemessagestored")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
-		(signing-identifier "com.apple.asktod")
+		(xpc-service-name "com.apple.DiagnosticExtensions.*")
+		(signing-identifier "com.apple.diagnosticextensionsd")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.marco")
-		(signing-identifier "com.apple.facetimemessagestored")
+		(global-name "com.apple.PowerManagement.control")
+		(require-any
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.ImageIOXPCService")
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(global-name "com.apple.iokit.powerdxpc")
+		(require-any
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+		)
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.trustd")
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.securityd")
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.quicklook.ThumbnailsAgent")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.locationd.synchronous")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(xpc-service-name "com.apple.ImageIOXPCService")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.locationd.spi")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(global-name "com.apple.identityservicesd.embedded.auth")
+		(signing-identifier "com.apple.asktod")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nesessionmanager")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(global-name "com.apple.trustd")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.securityd")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.AppSSO.service-xpc")
+		(global-name "com.apple.nesessionmanager")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.appleneuralengine")
-		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
+		(global-name "com.apple.locationd.spi")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.powerlog.plxpclogger.xpc")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+		(global-name "com.apple.networkscored")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+		(global-name "com.apple.AppSSO.service-xpc")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.ImageIOXPCService")
+		(global-name "com.apple.accountsd.accountmanager")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.accountsd.accountmanager")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(global-name "com.apple.locationd.synchronous")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.spotlight.IndexAgent")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(global-name "com.apple.cloudd")
+		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.spotlight.IndexDelegateAgent")
+		(xpc-service-name "com.apple.ImageIOXPCService")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(global-name "com.apple.audioanalyticsd")
-		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
+		(global-name "com.apple.appleneuralengine")
+		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ABDatabaseDoctor")
+		(global-name "com.apple.spotlight.IndexDelegateAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(global-name "com.apple.spotlight.IndexAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cmfsyncagent.embedded.auth")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(global-name "com.apple.geoanalyticsd")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.marco")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.audioanalyticsd")
+		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cloudd")
-		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
+		(global-name "com.apple.iokit.powerdxpc")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
+		(global-name "com.apple.PowerManagement.control")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.geoanalyticsd")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+		(global-name "com.apple.powerlog.plxpclogger.xpc")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.marco")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.locationd.registration")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(global-name "com.apple.ABDatabaseDoctor")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.private.appintents.delegate.*")
-		(signing-identifier "com.apple.linkd")
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.springboard-services")
-		(require-any
-			(global-name "com.apple.springboard.backgroundappservices")
-			(global-name "com.apple.springboard.services")
-			(global-name "com.apple.usernotifications.listener")
-			(global-name "com.apple.usernotifications.remotenotificationservice")
-			(global-name "com.apple.usernotifications.usernotificationservice")
-		)
+		(global-name "com.apple.cmfsyncagent.embedded.auth")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
+		(global-name "com.apple.locationd.registration")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.private.appintents.delegate.*")
+		(signing-identifier "com.apple.linkd")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(xpc-service-name "*")
 		(require-any
-			(global-name "com.apple.audio.AURemoteIOServer")
-			(xpc-service-name "com.apple.audio.AudioConverterService")
-			(xpc-service-name "com.apple.audio.AudioConverterService.HighCapacity")
-			(xpc-service-name "com.apple.audio.analytics.service")
+			(require-any
+				(signing-identifier "com.apple.InputUI")
+				(signing-identifier "com.apple.destinationd")
+				(signing-identifier "com.apple.donotdisturbd")
+				(signing-identifier "com.apple.locationpushd")
+				(signing-identifier "com.apple.symptomsd-diag")
+			)
+			(signing-identifier "com.apple.assistantd")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.usernotificationsd")
+		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(require-any
+				(xpc-service-name "com.apple.WebKit.Model")
+				(xpc-service-name "com.apple.WebKit.WebContent.CaptivePortal")
+				(xpc-service-name "com.apple.WebKit.WebContent.EnhancedSecurity")
+			)
+			(require-any
+				(xpc-service-name "com.apple.WebKit.Networking")
+				(xpc-service-name "com.apple.WebKit.WebContent")
+			)
+			(xpc-service-name "com.apple.WebKit.GPU")
+			(xpc-service-name "com.apple.WebKit.WebAuthn")
 		)
 	)
 )

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.awdd")
+		(require-any
+			(require-all
+				(global-name "com.apple.awdd")
+				(signing-identifier "com.apple.nanophoned")
+			)
+			(signing-identifier "com.apple.tursd")
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.power-assertions")

 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(%entitlement-is-bool-true "com.apple.security.ts.springboard-services")
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(global-name "com.apple.springboard.backgroundappservices")
+			(global-name "com.apple.springboard.services")
+			(global-name "com.apple.usernotifications.listener")
+			(global-name "com.apple.usernotifications.remotenotificationservice")
+			(global-name "com.apple.usernotifications.usernotificationservice")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(require-any
+			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
+			(global-name "com.apple.SystemConfiguration.NetworkInformation")
+			(global-name "com.apple.SystemConfiguration.PPPController")
+			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
+			(global-name "com.apple.SystemConfiguration.configd")
+			(global-name "com.apple.SystemConfiguration.helper")
+			(global-name "com.apple.commcenter.cupolicy.xpc")
+			(global-name "com.apple.commcenter.xpc")
+			(global-name "com.apple.securityd")
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.symptomsd")
+			(global-name "com.apple.trustd")
+			(global-name "com.apple.usymptomsd")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(signing-identifier "com.apple.internal.livtipsd")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(signing-identifier "com.apple.asktod")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
+		(require-any
+			(global-name "com.apple.audio.AURemoteIOServer")
+			(xpc-service-name "com.apple.audio.AudioConverterService")
+			(xpc-service-name "com.apple.audio.AudioConverterService.HighCapacity")
+			(xpc-service-name "com.apple.audio.analytics.service")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(signing-identifier "com.apple.Carousel")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(xpc-service-name "com.apple.*")
+		(signing-identifier "com.apple.assistantd")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(signing-identifier "com.apple.facetimemessagestored")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(xpc-service-name "com.apple.remotemanagement.*")
 		(require-any
-			(global-name "com.apple.mobileasset.autoasset")
-			(global-name "com.apple.mobileassetd")
-			(global-name "com.apple.mobileassetd.v2")
+			(signing-identifier "com.apple.RemoteManagementAgent")
+			(signing-identifier "com.apple.remotemanagementd")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(global-name "com.apple.usernotifications.delegate.*")
 		(require-any
-			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
-			(global-name "com.apple.SystemConfiguration.NetworkInformation")
-			(global-name "com.apple.SystemConfiguration.PPPController")
-			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
-			(global-name "com.apple.SystemConfiguration.configd")
-			(global-name "com.apple.SystemConfiguration.helper")
-			(global-name "com.apple.commcenter.cupolicy.xpc")
-			(global-name "com.apple.commcenter.xpc")
-			(global-name "com.apple.securityd")
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.symptomsd")
-			(global-name "com.apple.trustd")
-			(global-name "com.apple.usymptomsd")
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.SurfBoard")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.asktod")
+		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(require-any
+				(signing-identifier "com.apple.FTLivePhotoService")
+				(signing-identifier "com.apple.announced")
+			)
+			(signing-identifier "com.apple.Carousel")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+		(require-any
+			(global-name "com.apple.mobileasset.autoasset")
+			(global-name "com.apple.mobileassetd")
+			(global-name "com.apple.mobileassetd.v2")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "*")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.InputUI")
-				(signing-identifier "com.apple.destinationd")
-				(signing-identifier "com.apple.donotdisturbd")
-				(signing-identifier "com.apple.locationpushd")
-				(signing-identifier "com.apple.symptomsd-diag")
-			)
-			(signing-identifier "com.apple.assistantd")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(xpc-service-name "com.apple.*")
-		(signing-identifier "com.apple.assistantd")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(signing-identifier "com.apple.facetimemessagestored")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 		(require-any
 			(global-name "com.apple.PowerManagement.control")
 			(global-name "com.apple.iokit.powerdxpc")

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(xpc-service-name "com.apple.remotemanagement.*")
-		(require-any
-			(signing-identifier "com.apple.RemoteManagementAgent")
-			(signing-identifier "com.apple.remotemanagementd")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.usernotifications.delegate.*")
-		(require-any
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.SurfBoard")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any
-			(require-any
-				(signing-identifier "com.apple.FTLivePhotoService")
-				(signing-identifier "com.apple.announced")
-			)
-			(signing-identifier "com.apple.Carousel")
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.Carousel")
+		(signing-identifier "com.apple.usernotificationsd")
 		(require-any
 			(global-name "com.apple.PowerManagement.control")
 			(global-name "com.apple.iokit.powerdxpc")

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.awdd")
-		(require-any
-			(require-all
-				(global-name "com.apple.awdd")
-				(signing-identifier "com.apple.nanophoned")
-			)
-			(signing-identifier "com.apple.tursd")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.webkit-client")
-		(require-any
-			(require-any
-				(xpc-service-name "com.apple.WebKit.Model")
-				(xpc-service-name "com.apple.WebKit.WebContent.CaptivePortal")
-				(xpc-service-name "com.apple.WebKit.WebContent.EnhancedSecurity")
-			)
-			(require-any
-				(xpc-service-name "com.apple.WebKit.Networking")
-				(xpc-service-name "com.apple.WebKit.WebContent")
-			)
-			(xpc-service-name "com.apple.WebKit.GPU")
-			(xpc-service-name "com.apple.WebKit.WebAuthn")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.system.notification_center")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.Metal")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(preference-domain "com.apple.CFNetwork")
+		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.ids")
-		(require-any
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-		)
+		(preference-domain "com.apple.CloudKit")
+		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.CFNetwork")
-		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(preference-domain "com.apple.avfoundation")
+		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.avfoundation")
+		(preference-domain "com.apple.coreaudio")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.coreaudio")
+		(preference-domain "com.apple.corevideo")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
+		(require-any
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+		)
+	)
+)
 (allow managed-preference-read
 	(require-all
 		(preference-domain "com.apple.coremedia")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.carrier")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(preference-domain "com.apple.GEO")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.CloudKit")
-		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
+		(preference-domain "com.apple.itunesstored")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.conference")
+		(preference-domain "com.apple.ids")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.GEO")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+		(preference-domain "com.apple.conference")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.corevideo")
-		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		(preference-domain "com.apple.carrier")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
 (allow managed-preference-read

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.ids")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+		(preference-domain "com.apple.opengl")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.itunesstored")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
+		(preference-domain "com.apple.Metal")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.opengl")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(preference-domain "com.apple.logging")
+		(require-any
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(preference-domain "com.apple.conference")
 		(require-any
-			(preference-domain "com.apple.AOSNotification.public.notbackedup")
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.DataMigration")
-			(preference-domain "com.apple.PeoplePicker")
-			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
-			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
-			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
-			(require-all
-				(preference-domain "com.apple.CoreDuet")
-				(process-attribute is-apple-signed-executable)
+			(require-any
+				(signing-identifier "com.apple.FTLivePhotoService")
+				(signing-identifier "com.apple.announced")
 			)
+			(require-any
+				(signing-identifier "com.apple.internal.livtipsd")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+		(preference-domain "com.apple.CrashReporter")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.mediaplaybackd")
+				(signing-identifier "com.apple.videocodecd")
+			)
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
 			(preference-domain "com.apple.avfoundation")
 			(preference-domain "com.apple.coreaudio")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+		(preference-domain "com.apple.mobileipod")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any
-			(preference-domain "com.apple.avfoundation")
-			(preference-domain "com.apple.coreaudio")
-			(preference-domain "com.apple.coremedia")
-			(preference-domain "com.apple.corevideo")
+			(preference-domain "com.apple.AOSNotification.public.notbackedup")
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.DataMigration")
+			(preference-domain "com.apple.PeoplePicker")
+			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
+			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
+			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+			(require-all
+				(preference-domain "com.apple.CoreDuet")
+				(process-attribute is-apple-signed-executable)
+			)
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.conference")
+		(preference-domain "com.apple.marco")
 		(require-any
 			(require-any
 				(signing-identifier "com.apple.FTLivePhotoService")

 			(signing-identifier "com.apple.Carousel")
 			(signing-identifier "com.apple.asktod")
 			(signing-identifier "com.apple.facetimemessagestored")
-			(signing-identifier "com.apple.usernotificationsd")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.mobileipod")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.GEO")
-			(preference-domain "com.apple.locationd")
-		)
+		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.usernotificationsd")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.CrashReporter")
+		(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(signing-identifier "com.apple.videocodecd")
+			(preference-domain "com.apple.avfoundation")
+			(preference-domain "com.apple.coreaudio")
+			(preference-domain "com.apple.coremedia")
+			(preference-domain "com.apple.corevideo")
 		)
 	)
 )

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.internal.livtipsd")
 		(require-any
-			(require-any
-				(signing-identifier "com.apple.FTLivePhotoService")
-				(signing-identifier "com.apple.announced")
-			)
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-			(signing-identifier "com.apple.usernotificationsd")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )

 		)
 	)
 )
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.GEO")
+			(preference-domain "com.apple.locationd")
+		)
+	)
+)
 (allow managed-preference-read
 	(require-any
 		(preference-domain "com.apple.NanoRegistry")

 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.Metal")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(preference-domain "com.apple.CFNetwork")
+		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.ids")
-		(require-any
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-		)
+		(preference-domain "com.apple.CloudKit")
+		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.CFNetwork")
-		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(preference-domain "com.apple.avfoundation")
+		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.avfoundation")
+		(preference-domain "com.apple.coreaudio")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.coreaudio")
+		(preference-domain "com.apple.corevideo")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
+(allow user-preference-write
+	(require-all
+		(preference-domain "com.apple.ids")
+		(require-any
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+		)
+	)
+)
 (allow user-preference-write
 	(require-all
 		(preference-domain "com.apple.coremedia")

 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.carrier")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(preference-domain "com.apple.GEO")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.CloudKit")
-		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
+		(preference-domain "com.apple.itunesstored")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.conference")
+		(preference-domain "com.apple.ids")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.GEO")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+		(preference-domain "com.apple.conference")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.corevideo")
-		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		(preference-domain "com.apple.carrier")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
 (allow user-preference-write

 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.ids")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+		(preference-domain "com.apple.opengl")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.itunesstored")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
+		(preference-domain "com.apple.Metal")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.opengl")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(preference-domain "com.apple.logging")
+		(require-any
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+		)
 	)
 )
 (allow user-preference-write
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(preference-domain "com.apple.conference")
 		(require-any
-			(preference-domain "com.apple.AOSNotification.public.notbackedup")
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.DataMigration")
-			(preference-domain "com.apple.PeoplePicker")
-			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
-			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
-			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
-			(require-all
-				(preference-domain "com.apple.CoreDuet")
-				(process-attribute is-apple-signed-executable)
+			(require-any
+				(signing-identifier "com.apple.FTLivePhotoService")
+				(signing-identifier "com.apple.announced")
+			)
+			(require-any
+				(signing-identifier "com.apple.internal.livtipsd")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
+		)
+	)
+)
+(allow user-preference-write
+	(require-all
+		(preference-domain "com.apple.CrashReporter")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.mediaplaybackd")
+				(signing-identifier "com.apple.videocodecd")
 			)
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
 		)
 	)
 )
 (allow user-preference-write
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
 			(preference-domain "com.apple.avfoundation")
 			(preference-domain "com.apple.coreaudio")

 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+		(preference-domain "com.apple.mobileipod")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		)
 	)
 )
 (allow user-preference-write
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any
-			(preference-domain "com.apple.avfoundation")
-			(preference-domain "com.apple.coreaudio")
-			(preference-domain "com.apple.coremedia")
-			(preference-domain "com.apple.corevideo")
+			(preference-domain "com.apple.AOSNotification.public.notbackedup")
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.DataMigration")
+			(preference-domain "com.apple.PeoplePicker")
+			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
+			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
+			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+			(require-all
+				(preference-domain "com.apple.CoreDuet")
+				(process-attribute is-apple-signed-executable)
+			)
 		)
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.conference")
+		(preference-domain "com.apple.marco")
 		(require-any
 			(require-any
 				(signing-identifier "com.apple.FTLivePhotoService")

 			(signing-identifier "com.apple.Carousel")
 			(signing-identifier "com.apple.asktod")
 			(signing-identifier "com.apple.facetimemessagestored")
-			(signing-identifier "com.apple.usernotificationsd")
-		)
-	)
-)
-(allow user-preference-write
-	(require-all
-		(preference-domain "com.apple.mobileipod")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		)
 	)
 )
 (allow user-preference-write
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.GEO")
-			(preference-domain "com.apple.locationd")
-		)
+		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.usernotificationsd")
 	)
 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.CrashReporter")
+		(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(signing-identifier "com.apple.videocodecd")
+			(preference-domain "com.apple.avfoundation")
+			(preference-domain "com.apple.coreaudio")
+			(preference-domain "com.apple.coremedia")
+			(preference-domain "com.apple.corevideo")
 		)
 	)
 )

 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.internal.livtipsd")
 		(require-any
-			(require-any
-				(signing-identifier "com.apple.FTLivePhotoService")
-				(signing-identifier "com.apple.announced")
-			)
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-			(signing-identifier "com.apple.usernotificationsd")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )

 		)
 	)
 )
+(allow user-preference-write
+	(require-all
+		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		)
+	)
+)
+(allow user-preference-write
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.GEO")
+			(preference-domain "com.apple.locationd")
+		)
+	)
+)
 (allow user-preference-write
 	(require-any
 		(preference-domain "com.apple.NanoRegistry")
```

##### usernotifications-accessory

```diff

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read*
 	(require-any
 		(extension "com.apple.app-sandbox.read")
 		(extension "com.apple.mediaserverd.read")
 		(extension "com.apple.quicklook.readonly")
 		(extension "com.apple.sharing.airdrop.readonly")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "${HOME}/Library/Fonts")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-any
 		(extension "com.apple.app-sandbox.read")

 		(extension "com.apple.sharing.airdrop.readonly")
 		(literal "${HOME}")
 		(literal "${HOME}/Library/Preferences")
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(subpath "${HOME}/Library/Fonts")

 		)
 	)
 )
+(allow file-test-existence
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
 (allow file-test-existence
 	(require-any
-		(literal "/System")
-		(literal "/private")
-		(literal "/private/preboot")
 		(subpath "/")
 		(subpath "/System/Cryptexes")
 		(subpath "/private/preboot/Cryptexes")

 )
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.DeviceAccess.xpc")
 		(global-name "com.apple.chrono.accessoryLiveActivities")
 		(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
 		(global-name "com.apple.coremedia.mediaplaybackd.assetimagegenerator.xpc")
```

### Protobox/Autobox

#### New (1)

##### appleaccounttransparencyd

```scheme
(version 1)
(disable-callouts)

(allow default)

(allow device-camera)

(deny file-ioctl)

(deny generic-issue-extension)

(deny iokit-issue-extension)

(deny iokit-open-user-client)
(allow iokit-open-user-client
	(require-any
		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
	)
)

(deny iokit-set-properties)

(deny ipc*)

(deny job-creation)

(deny mach-issue-extension)

(deny mach-lookup
	(require-all
		(require-not (global-name "com.apple.cdp.daemon"))
		(require-not (global-name "com.apple.transparencyd.aet"))
		(require-not (global-name "com.apple.duetactivityscheduler"))
		(require-all
			(system-attribute developer-mode)
			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
		)
	)
)

(deny process-exec-interpreter)

(deny process-fork)

(deny sysctl-read
	(require-any
		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
		(sysctl-name "vm.footprint_suspend")
		(sysctl-name "vm.task_no_footprint_for_debug")
	)
)

(deny system*
	(require-any
		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
		(sysctl-name "vm.footprint_suspend")
		(sysctl-name "vm.task_no_footprint_for_debug")
	)
)

(deny system-info)
(allow system-info
	(fsctl-command FSIOC_CAS_BSDFLAGS)
)

(deny system-kext*)

(deny process-exec-update-label)
```

#### Changed (181)

##### ACCCarPlayService

```diff

 		io_service_open_extended
 		io_server_version
 		io_service_get_matching_services_bin
+		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user
```

##### ANECompilerService

```diff

 		SYS_symlink
 		SYS_readlink
 		SYS_umask
+		SYS_msync
 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise

 		SYS_fchown
 		SYS_fchmod
 		SYS_rename
+		SYS_flock
 		SYS_sendto
 		SYS_mkdir
 		SYS_rmdir

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_sendmsg_nocancel
+		SYS_msync_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
 		SYS_sigsuspend_nocancel
```

##### ANFDecoder

```diff

 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleParavirtGPU")
+		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )
 

 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
-		MSC_mk_timer_cancel)
+		MSC_mk_timer_cancel
+		MSC_iokit_user_client_trap)
 )
 
 (deny sysctl*)

 		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
```

##### ASPCarryLog

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### AccountSubscriber

```diff

 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### AppSSODaemon

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### AssetLoader

```diff

 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC__kernelrpc_mach_port_guard_trap
+		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri
```

##### AudioConverterHighCapacityService

```diff

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-memorystatus-control
 		(require-all
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```

##### AutomationModeUI

```diff

 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleParavirtGPU")
+		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )
 

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 

 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
-		MSC_mk_timer_cancel)
+		MSC_mk_timer_cancel
+		MSC_iokit_user_client_trap)
 )
 
 (deny sysctl*)

 		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
```

##### BTLEServer

```diff

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
 		SYS___channel_get_info
 		SYS___channel_sync
```

##### BrowserEngineKit.Intermediary

```diff

 
 (deny mach-issue-extension)
 
-(deny mach-lookup)
-(deny mach-lookup)
+(deny mach-lookup
+	(require-all
+		(require-not (global-name "com.apple.family.ageRange.xpc"))
+		(require-all
+			(system-attribute developer-mode)
+			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
+		)
+	)
+)
 
 (deny process-exec-interpreter)
 

 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```

##### BundleComplicationMigrationService

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 

 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_persona
 		SYS_getentropy
 		SYS_ulock_wait
 		SYS_ulock_wake
```

##### Camera

```diff

 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
+		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))

 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.internal.objc_trace"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
 		(require-not (global-name "com.apple.CameraOverlayAngel.application-service"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-all
```

##### ClarityBoard

```diff

 			(global-name "com.apple.usernotifications.delegate.com.apple.Passbook")
 			(global-name "com.apple.usernotifications.delegate.com.apple.iBooks")
 			(global-name "com.apple.usernotifications.delegate.com.apple.mobilemail")
+			(global-name "com.apple.usernotifications.delegate.com.apple.mobiletimer")
 			(global-name "com.apple.usernotifications.delegate.com.apple.tv")
 			(global-name "com.apple.usernotifications.delegate.com.apple.usernotifications.example")
 			(global-name "com.apple.usernotifications.delegate.com.apple.weather")
```

##### CloudTelemetryService

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### CommCenterMobileHelper

```diff

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### CommCenterRootHelper

```diff

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.tailspind"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### ContainerMetadataExtractor

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 	)
 )
 
```

##### CoreRoutineHelperService

```diff

 		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_getsockopt
 		SYS_readv
 		SYS_writev

 		thread_terminate
 		thread_suspend
 		thread_resume
+		thread_info
 		thread_policy
 		vm_map_external
 		vm_remap_external
```

##### CoreSpotlightService

```diff

 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
+		SYS_fsetattrlist
 		SYS_fgetxattr
 		SYS_listxattr
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_sysctlbyname
 		SYS_stat_extended
```

##### DumpPanic

```diff

 			(global-name "com.apple.dumppanic.sil-notification")
 			(global-name "com.apple.dumppanic.test-notification")
 		))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
```

##### EAUpdaterService

```diff

 		SYS_guarded_close_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat

 		task_set_exc_guard_behavior
 		vm_remap_external
 		vm_reallocate
+		mach_vm_copy
 		mach_vm_map_external
 		mach_vm_region_recurse
 		_mach_make_memory_entry

 	(deny system-memorystatus-control
 		(require-all
 			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
 		)
```

##### FindMyDeviceBTDiscoveryXPCService

```diff

 	(deny system-memorystatus-control
 		(require-all
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
 		)
```

##### GroupSessionService

```diff

 		SYS_guarded_close_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### IMDMessageServicesAgent

```diff

 	(require-all
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.coremedia.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.runningboard"))

 		SYS_change_fdguard_np
 		SYS_connectx
 		SYS_openat
+		SYS_faccessat
 		SYS_fchownat
 		SYS_fstatat
 		SYS_fstatat64
```

##### InputUI

```diff

 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
 		mach_port_get_service_port_info
+		task_threads_from_user
 		task_info_from_user
 		task_get_special_port_from_user
 		task_set_special_port
```

##### IntelligentLight

```diff

 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.dasd.end-prewarm"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
```

##### Managed Background Assets Helper Fetching Service

```diff

 		SYS_readv
 		SYS_writev
 		SYS_sendto
+		SYS_shutdown
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_sendmsg_nocancel
 		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 (deny system-fsctl)
 (allow system-fsctl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_SETFL
```

##### ManagedSettingsAgent

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### MomentsIntelligenceService

```diff

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.diagnosticd"))

 
 (deny system-kext*)
 
-(deny system-memorystatus-control
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-memorystatus-control
+		(require-all
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
 	)
 )
 (deny system-memorystatus-control
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```

##### NFUIService

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.SharingServices"))
```

##### NTKFaceSnapshotService

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### PerfPowerServicesExtended

```diff

 		(require-not (global-name "com.apple.backupd"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.OTATaskingAgent"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.basebandd.xpc"))
```

##### Photos

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
+		(iokit-registry-entry-class "IOReportUserClient")
 	)
 )
 

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.gamed"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.proactive.FaceSuggestions.xpc"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
 		(require-not (require-any
 			(xpc-service-name "com.grammarly.keyboard.extension")
-			(xpc-service-name "com.iflytek.inputime.keyboard")
+			(xpc-service-name "com.jimmy54.SuperWubi.Keyboard")
+			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
 			(xpc-service-name "com.riffsy.RiffsyKeyboard.RiffsyGIFKeyboard")
+			(xpc-service-name "com.superduper.superwhisper-ios.superwhisper-keyboard")
 			(xpc-service-name "com.tackgyulee.dinggul.dinggulkeyboard")
 			(xpc-service-name "com.willowvoice.ios.keyboard")
 			(xpc-service-name "com.wispr.flowapp.flowboard")
```

##### ProductKitService

```diff

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
```

##### ReportSystemMemory

```diff

 
 (deny system-kext*)
 
-(deny system-memorystatus-control
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-memorystatus-control
+		(require-all
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
 	)
 )
 (deny system-memorystatus-control
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```

##### SCHelper

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### SPIHelper-iOS

```diff

 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleAPFSContainer")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )
 

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.iapd.xpc"))

 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
-		MSC_mk_timer_cancel)
+		MSC_mk_timer_cancel
+		MSC_iokit_user_client_trap)
 )
 
 (deny sysctl*)

 		io_service_close
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
```

##### ScreenTimeAgent

```diff

 		(require-not (global-name "com.apple.FamilyControlsAgent.private"))
 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
```

##### SensorKitALSHelper

```diff

 		(require-not (global-name "com.apple.BluetoothCloudServices"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.bluetoothuser.xpc"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### SidebarFileDispatcherService

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
```

##### SoftwareUpdateSubscriber

```diff

 		SYS_guarded_close_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### SoftwareUpdateUIService

```diff

 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
+		(require-not (xpc-service-name "com.tencent.wetype.keyboard"))
 		(require-any
 			(require-all
 				(system-attribute developer-mode)
```

##### SpringBoard

```diff

 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.coremedia.cameraviewfinder"))
 		(require-not (global-name "com.apple.DragUI.druid.destination"))
-		(require-not (require-any
-			(global-name "UIASTNotificationCenter")
-			(global-name "com.apple.CarPlayApp.user-alerts-service")
-			(global-name "com.apple.CardBoard.KeyboardExtension")
-			(global-name "com.apple.DriverKitExtensionServer")
-			(global-name "com.apple.MRMediaSuggestionsService")
-			(global-name "com.apple.ModeEntityScorer")
-			(global-name "com.apple.PerformanceTrace.ptpassivecollectiond.collectionconfig")
-			(global-name "com.apple.ProactiveSummarization.feedbackServer")
-			(global-name "com.apple.ProactiveSummarization.server.testing")
-			(global-name "com.apple.PrototypeTools.prototypingserver")
-			(global-name "com.apple.SILManager.Debug")
-			(global-name "com.apple.ScreenSharingViewServiceHelper")
-			(global-name "com.apple.SiriHUD.service")
-			(global-name "com.apple.VoiceOverTouch.drag.xpc")
-			(global-name "com.apple.WorkoutHUD.service")
-			(global-name "com.apple.adaptivemusicd")
-			(global-name "com.apple.adpt.CorvidiaAngel.sessions")
-			(global-name "com.apple.adpt.CorvidiaApp.sessions")
-			(global-name "com.apple.adpt.CorvidiaApp.xpc")
-			(global-name "com.apple.assistant.announcement_state.service")
-			(global-name "com.apple.assistant.domain.system.service")
-			(global-name "com.apple.assistant.hearables-experience-manager")
-			(global-name "com.apple.assistant.request-dispatcher.gestures-bridge-service")
-			(global-name "com.apple.assistant.sva.system.service")
-			(global-name "com.apple.assistivetouchd.drag.xpc")
-			(global-name "com.apple.biomed.sensorium.publisherRegistration")
-			(global-name "com.apple.campo")
-			(global-name "com.apple.commandandcontrol.drag.xpc")
-			(global-name "com.apple.coreduetd.batterysaver")
-			(global-name "com.apple.coremedia.audioprocessingtap.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
-			(global-name "com.apple.coremedia.videoqueue")
-			(global-name "com.apple.coreservices.lsbestappsuggestionmanager.xpc")
-			(global-name "com.apple.devicedatareset.DeviceDataResetObservationService.NonLaunching")
-			(global-name "com.apple.dtracecartd.xpc")
-			(global-name "com.apple.duet.expertcenter")
-			(global-name "com.apple.findmylocaldevice")
-			(global-name "com.apple.fullkeyboardaccess.drag.xpc")
-			(global-name "com.apple.hid.Bongo")
-			(global-name "com.apple.hmidevicesd")
-			(global-name "com.apple.inputanalytics.testAppRelay")
-			(global-name "com.apple.inputservice.autofill")
-			(global-name "com.apple.inputui.frontboard")
-			(global-name "com.apple.internal.FloatingLogHUD.service")
-			(global-name "com.apple.internal.PerfPowerHUD.service")
-			(global-name "com.apple.internal.SystemLogHUD.service")
-			(global-name "com.apple.ixda.sad")
-			(global-name "com.apple.merchantd.internals")
-			(global-name "com.apple.nano.nanoresourcegrabber")
-			(global-name "com.apple.nfcd.wallet.presentation")
-			(global-name "com.apple.notifications.logging")
-			(global-name "com.apple.proactive.DefaultWidgetSuggester")
-			(global-name "com.apple.proactive.NotificationDigest.xpc")
-			(global-name "com.apple.proactive.SuggestedPages")
-			(global-name "com.apple.proactive.UserEducationSuggestion.server-listener.xpc")
-			(global-name "com.apple.proactive.hero.AppPrediction.predictions")
-			(global-name "com.apple.proactive.timeIntelligence")
-			(global-name "com.apple.reachd")
-			(global-name "com.apple.rti-autofill")
-			(global-name "com.apple.shortcuts.magic-service")
-			(global-name "com.apple.siri.session.service")
-			(global-name "com.apple.softwareupdateservicesd.justin")
-			(global-name "com.apple.softwareupdateservicesui.controller")
-			(global-name "com.apple.synapse.backlink-indicator-usage")
-			(global-name "com.apple.systemassistant.session.service")
-			(global-name "com.apple.uikit.eyedropperd.service")
-			(global-name "com.apple.uikit.viewservice.*")
-			(global-name "com.apple.usernotificationlistvendor.listener")
-			(global-name "com.apple.usernotifications.delegate.*")
-			(global-name "com.apple.usernotifications.event-service.launching")
-			(global-name "com.apple.usernotifications.subscriber-service.launching")
-			(global-name "com.apple.usernotifications.subscriber-service.non-launching")
-			(global-name "com.apple.usernotificationsserver.DefaultDataProviderFactory")
-			(global-name "com.apple.voiced")
-			(global-name "com.apple.voiceservices.keepalive")
-			(global-name "com.apple.vpg.TeaBoard.service")
-			(global-name "com.apple.watchdogd")
-			(global-name "com.appleinternal.FloatingLogHUD.service")
-		))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.coremedia.mutablecomposition.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))

 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (require-any
+			(global-name "UIASTNotificationCenter")
+			(global-name "com.apple.CarPlayApp.user-alerts-service")
+			(global-name "com.apple.CardBoard.KeyboardExtension")
+			(global-name "com.apple.DriverKitExtensionServer")
+			(global-name "com.apple.MRMediaSuggestionsService")
+			(global-name "com.apple.ModeEntityScorer")
+			(global-name "com.apple.PerformanceTrace.ptpassivecollectiond.collectionconfig")
+			(global-name "com.apple.ProactiveSummarization.feedbackServer")
+			(global-name "com.apple.ProactiveSummarization.server.testing")
+			(global-name "com.apple.PrototypeTools.prototypingserver")
+			(global-name "com.apple.SILManager.Debug")
+			(global-name "com.apple.ScreenSharingViewServiceHelper")
+			(global-name "com.apple.SiriHUD.service")
+			(global-name "com.apple.VoiceOverTouch.drag.xpc")
+			(global-name "com.apple.WorkoutHUD.service")
+			(global-name "com.apple.adaptivemusicd")
+			(global-name "com.apple.adpt.CorvidiaAngel.sessions")
+			(global-name "com.apple.adpt.CorvidiaApp.sessions")
+			(global-name "com.apple.adpt.CorvidiaApp.xpc")
+			(global-name "com.apple.assistant.announcement_state.service")
+			(global-name "com.apple.assistant.domain.system.service")
+			(global-name "com.apple.assistant.hearables-experience-manager")
+			(global-name "com.apple.assistant.request-dispatcher.gestures-bridge-service")
+			(global-name "com.apple.assistant.sva.system.service")
+			(global-name "com.apple.assistivetouchd.drag.xpc")
+			(global-name "com.apple.biomed.sensorium.publisherRegistration")
+			(global-name "com.apple.campo")
+			(global-name "com.apple.commandandcontrol.drag.xpc")
+			(global-name "com.apple.coreduetd.batterysaver")
+			(global-name "com.apple.coremedia.audioprocessingtap.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
+			(global-name "com.apple.coremedia.videoqueue")
+			(global-name "com.apple.coreservices.lsbestappsuggestionmanager.xpc")
+			(global-name "com.apple.devicedatareset.DeviceDataResetObservationService.NonLaunching")
+			(global-name "com.apple.dtracecartd.xpc")
+			(global-name "com.apple.duet.expertcenter")
+			(global-name "com.apple.findmylocaldevice")
+			(global-name "com.apple.fullkeyboardaccess.drag.xpc")
+			(global-name "com.apple.hid.Bongo")
+			(global-name "com.apple.hmidevicesd")
+			(global-name "com.apple.inputanalytics.testAppRelay")
+			(global-name "com.apple.inputservice.autofill")
+			(global-name "com.apple.inputui.frontboard")
+			(global-name "com.apple.internal.FloatingLogHUD.service")
+			(global-name "com.apple.internal.PerfPowerHUD.service")
+			(global-name "com.apple.internal.SystemLogHUD.service")
+			(global-name "com.apple.ixda.sad")
+			(global-name "com.apple.merchantd.internals")
+			(global-name "com.apple.nano.nanoresourcegrabber")
+			(global-name "com.apple.nfcd.wallet.presentation")
+			(global-name "com.apple.notifications.logging")
+			(global-name "com.apple.proactive.DefaultWidgetSuggester")
+			(global-name "com.apple.proactive.NotificationDigest.xpc")
+			(global-name "com.apple.proactive.SuggestedPages")
+			(global-name "com.apple.proactive.UserEducationSuggestion.server-listener.xpc")
+			(global-name "com.apple.proactive.hero.AppPrediction.predictions")
+			(global-name "com.apple.proactive.timeIntelligence")
+			(global-name "com.apple.reachd")
+			(global-name "com.apple.rti-autofill")
+			(global-name "com.apple.shortcuts.magic-service")
+			(global-name "com.apple.siri.session.service")
+			(global-name "com.apple.softwareupdateservicesd.justin")
+			(global-name "com.apple.softwareupdateservicesui.controller")
+			(global-name "com.apple.synapse.backlink-indicator-usage")
+			(global-name "com.apple.systemassistant.session.service")
+			(global-name "com.apple.uikit.eyedropperd.service")
+			(global-name "com.apple.uikit.viewservice.*")
+			(global-name "com.apple.usernotificationlistvendor.listener")
+			(global-name "com.apple.usernotifications.delegate.*")
+			(global-name "com.apple.usernotifications.event-service.launching")
+			(global-name "com.apple.usernotifications.subscriber-service.launching")
+			(global-name "com.apple.usernotifications.subscriber-service.non-launching")
+			(global-name "com.apple.usernotificationsserver.DefaultDataProviderFactory")
+			(global-name "com.apple.voiced")
+			(global-name "com.apple.voiceservices.keepalive")
+			(global-name "com.apple.vpg.TeaBoard.service")
+			(global-name "com.apple.watchdogd")
+			(global-name "com.appleinternal.FloatingLogHUD.service")
+			(global-name "com.rpetrich.rocketbootstrapd")
+		))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.proactive.FaceSuggestions.xpc"))

 		(literal "/bin/mv")
 		(literal "/bin/rm")
 		(literal "/bin/sh")
+		(literal "/dopamine-BYx8YN/procursus/usr/libexec/_rocketd_reenable")
 		(literal "/usr/bin/atos")
 		(literal "/usr/bin/pkill")
 	)

 		(literal "/bin/mv")
 		(literal "/bin/rm")
 		(literal "/bin/sh")
+		(literal "/dopamine-BYx8YN/procursus/usr/libexec/_rocketd_reenable")
 		(literal "/usr/bin/atos")
 		(literal "/usr/bin/pkill")
 	)

 		SYS_fchmod
 		SYS_rename
 		SYS_flock
+		SYS_mkfifo
 		SYS_sendto
 		SYS_shutdown
 		SYS_socketpair
```

##### StandaloneHIDAudService

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### ThreeBarsXPCService

```diff

 		SYS_connect
 		SYS_setsockopt
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_getsockopt
 		SYS_writev
 		SYS_rename

 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
+		MSC_thread_self_trap
 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
```

##### TodayFeedConfigDecoder

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### UVCAssistant

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### ViewHierarchyAgent

```diff

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_service_open_extended
+		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
```

##### WorkoutKitXPCService

```diff

 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
 		SYS_mremap_encrypted
+		SYS_persona
 		SYS_work_interval_ctl
 		SYS_getentropy
 		SYS_necp_open
```

##### activitysharingd

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_renameat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### adprivacyd

```diff

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (require-any
```

##### amfid

```diff

 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.online-auth-agent.xpc"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.misagent"))

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.datamigrator"))
```

##### amsaccountsd

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
+		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 		(iokit-registry-entry-class "ProvInfoIOKitUserClient")
 		(iokit-registry-entry-class "RootDomainUserClient")
 		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKitUserClient")

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "H1xANELoadBalancer")
 		(iokit-registry-entry-class "IOPMrootDomain")
+		(iokit-registry-entry-class "IOSurfaceRoot")
 		(iokit-registry-entry-class "ProvInfoIOKit")
 		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKit")
 	)

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.NPKCompanionAgent.library"))
+		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )

 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid
+		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_registry_entry_create_iterator
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
+		io_connect_set_notification_port_64
 		io_service_add_interest_notification_64
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_destroy
```

##### amsengagementd

```diff

 		(require-not (global-name "com.apple.amsondevicestoraged.xpc"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.extensionkitservice"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.lsd.extensions"))

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### announced

```diff

 )
 
 (deny system-nfssvc)
+(allow system-nfssvc
+	(necp-client-action NECP_CLIENT_ACTION_ADD)
+)
 
 (deny process-exec-update-label)
```

##### appleh13camerad

```diff

 	(deny system-memorystatus-control
 		(require-all
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
 		)
```

##### appleh16camerad

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### appstorecomponentsd

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### appstored

```diff

 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.SBUserNotification"))
```

##### apsd

```diff

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.ndoagent"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
+		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.biome.compute.source.user"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (require-any
 			(global-name "${ANY_UUID}")
 			(global-name "DeviceSpecificTopic1")

 			(global-name "com.apple.ubd.system-push")
 			(global-name "com.apple.usernotifications.aps")
 			(global-name "com.apple.usernotifications.aps.dev")
+			(global-name "com.apple.useroccupancyd.push")
 			(global-name "com.apple.videosubscriptionsd")
 			(global-name "com.apple.watchconnectivity.complication.push")
 			(global-name "com.apple.watchconnectivity.complication.push.development")

 			(global-name "com.apple.wte.aesd")
 			(global-name "dummy.delegate.port")
 		))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.biome.compute.source.user"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### askpermissiond

```diff

 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.Contacts"))

 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.biome.compute.source"))
+		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
```

##### atc

```diff

 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.businessservicesd"))
```

##### attributionkitd

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### audiomxd

```diff

 		(require-not (global-name "com.apple.accessories.transport-server"))
 		(require-not (require-any
 			(global-name "com.apple.BTAudioHALPluginAccessories.xpc")
-			(global-name "com.apple.BluetoothServices")
 			(global-name "com.apple.MXUIService")
 			(global-name "com.apple.accessories.audio")
 			(global-name "com.apple.continuitycaptureaudio.provider.xpc")

 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (global-name "com.apple.healthd.server"))
+		(require-not (global-name "com.apple.BluetoothServices"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService.Hardened"))
-		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.sleepd.sleepserver"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.systemstatus"))

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (xpc-service-name "com.apple.coreaudio.RemoteProcessingBlockRegistrar"))
+		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (global-name "com.apple.corercd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
-		(require-not (xpc-service-name "com.apple.CoreRepairCoreXPCService"))
+		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.systemstatus.activityattribution"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))

 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
-		(require-not (xpc-service-name "com.apple.siri.context.service"))
+		(require-not (xpc-service-name "com.apple.coreaudio.RemoteProcessingBlockRegistrar"))
 		(require-not (global-name "com.apple.soundanalysisd"))
 		(require-not (global-name "com.apple.videoconference.speechtranslation"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.tccd"))
-		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
-		(require-not (xpc-service-name "com.apple.ctcategories.service"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.CoreRepairCoreXPCService"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.ctcategories.service"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.usernotifications.listener"))

 		(require-not (global-name "com.apple.coremedia.endpointstream.xpc"))
 		(require-not (global-name "com.apple.SensorKit.writer"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-all

 		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
+		SYS_necp_session_action
 		SYS_os_fault_with_payload
 		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
```

##### avatarsd

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### bluetoothd

```diff

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (global-name "com.apple.BluetoothServices"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
```

##### caraccessoryd

```diff

 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.carkit.service"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))

 		SYS_fchown
 		SYS_fchmod
 		SYS_rename
+		SYS_flock
 		SYS_sendto
 		SYS_mkdir
 		SYS_rmdir

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### carkitd

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
 

 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid
+		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_service_open_extended
 		io_connect_method
 		io_connect_async_method
+		io_connect_set_notification_port_64
 		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
```

##### cdpd

```diff

 
 (deny socket-option*)
 (allow socket-option*
-	(ioctl-command CTLIOCGINFO)
+	(ioctl-command
+		CTLIOCGINFO
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
 )
 
 (deny syscall-mach)
```

##### chronod

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### cloudd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### com.apple.DiagnosticsSessionAvailibility

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### com.apple.NeighborhoodActivityConduitService

```diff

 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AGXAccelerator")
+	(require-any
+		(iokit-registry-entry-class "AGXAccelerator")
+		(iokit-registry-entry-class "IOSurfaceRoot")
+	)
 )
 
 (deny iokit-set-properties)

 		io_registry_entry_get_parent_iterator
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
```

##### com.apple.SensorKit.CHSupportService

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### com.apple.SharePlay.NearbyInvitationsService

```diff

 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat

 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_persona
 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
```

##### com.apple.Virtualization.VirtualMachine

```diff

 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 		(iokit-registry-entry-class "RootDomainUserClient")
+		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKitUserClient")
 	)
 )
 

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 

 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.lskdd"))
 		(require-not (global-name "com.apple.iap2d.distributednotification.server"))
+		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.PairingManager"))
 		(require-not (global-name "com.apple.carkit.dnd.service"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.remoted.virtualization"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))

 )
 
 (deny process-exec-interpreter)
+(allow process-exec-interpreter
+	(literal "/bin/rm")
+)
 
 (deny process-fork)
+(allow process-fork
+	(literal "/bin/rm")
+)
 
 (deny socket-option*)
 (allow socket-option*

 		SYS_open
 		SYS_close
 		SYS_wait4
+		SYS_link
+		SYS_unlink
 		SYS_getfsstat
 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_getsockname
 		SYS_access
 		SYS_kill

 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
+		SYS_fchmod
 		SYS_rename
 		SYS_flock
 		SYS_sendto
+		SYS_shutdown
 		SYS_socketpair
 		SYS_mkdir
 		SYS_pread

 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_openbyid_np
 		SYS_recvmsg_x
 		SYS_sendmsg_x
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_renameatx_np
 		SYS_work_interval_ctl
 		SYS_getentropy
 		SYS_ulock_wait
```

##### com.apple.accounts.dom

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### com.apple.dt.DTMLModelRunnerService

```diff

 		vm_remap_external
 		vm_reallocate
 		mach_vm_map_external
+		mach_vm_remap_external
 		_mach_make_memory_entry
 		mach_vm_range_create
 		mach_vm_reallocate
+		mach_memory_entry_ownership
 		task_restartable_ranges_register
 		task_restartable_ranges_synchronize)
 )
```

##### com.apple.photos.ImageConversionService

```diff

 		SYS_getentropy
 		SYS_ulock_wait
 		SYS_ulock_wake
+		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_setattrlistat
```

##### com.apple.weatherkit.authservice

```diff

 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
```

##### companion_proxy

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### contactsdonationagent

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.research.adtcd"))

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
```

##### coreidvd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### corerepaird

```diff

 	(require-all
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
```

##### dasd

```diff

 		))
 		(require-not (require-any
 			(sysctl-name "kern.memorystatus.freeze_shared_memory")
+			(sysctl-name "kern.trial.compressor_ripeness_age_s")
 			(sysctl-name "kern.trial.memorystatus_freeze_last_processes_thawed_cache_size")
 			(sysctl-name "kern.trial.memorystatus_freeze_last_processes_thawed_prevent_refreeze_seconds")
 			(sysctl-name "kern.trial.memorystatus_freeze_prevent_refreeze_of_recently_suspended")
 			(sysctl-name "kern.trial.memorystatus_freeze_prevent_refreeze_of_recently_thawed")
+			(sysctl-name "kern.trial.vm_compressor_scavenger_enabled")
 			(sysctl-name "vm.freeze_enabled")
 		))
 		(require-any
```

##### deleted_helper

```diff

 		MSC_thread_self_trap
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap

 		task_get_special_port_from_user
 		task_set_special_port
 		semaphore_create
+		semaphore_destroy
 		task_set_exc_guard_behavior
 		vm_map_external
 		vm_remap_external
```

##### deviceaccessd

```diff

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.appconduitd.device-connection"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
```

##### devicecheckd

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### diagnosticspushd

```diff

 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```

##### distnoted

```diff

 		host_info
 		host_get_clock_service
 		host_get_special_port
+		clock_get_time
 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
```

##### donotdisturbd

```diff

 		SYS_openat
 		SYS_openat_nocancel
 		SYS_renameat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### druid

```diff

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.analyticsd"))

 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid
+		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_registry_entry_get_name
 		io_service_close
 		io_registry_get_root_entry
+		io_registry_entry_create_iterator
 		io_service_open_extended
 		io_connect_method
 		io_connect_async_method
+		io_connect_set_notification_port_64
 		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
```

##### ecosystemanalyticsd

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### eyedropperd

```diff

 		io_registry_get_root_entry
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
 		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
```

##### feedbackd

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### fileproviderd

```diff

 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
```

##### findmybeaconingd

```diff

 		vm_reallocate
 		mach_vm_copy
 		mach_vm_map_external
+		mach_vm_remap_external
 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
```

##### fitcored

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### fitnesscoachingd

```diff

 		SYS_guarded_close_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### frauddefensed

```diff

 		mach_exception_raise_state_identity
 		io_iterator_next
 		io_registry_entry_from_path
+		io_registry_entry_get_property_bytes
 		io_registry_entry_get_child_iterator
 		io_service_close
 		io_registry_entry_create_iterator
```

##### gamed

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 	)
 )
 

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### gamesaved

```diff

 		SYS_psynch_mutexwait
 		SYS_psynch_mutexdrop
 		SYS_psynch_cvbroad
+		SYS_psynch_cvsignal
 		SYS_psynch_cvwait
 		SYS_psynch_rw_rdlock
 		SYS_psynch_rw_wrlock
```

##### generativeexperiencesd

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
```

##### geocorrectiond

```diff

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		thread_info
 		thread_policy
 		vm_remap_external
 		vm_reallocate
```

##### griddatad

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### healthappd

```diff

 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.donotdisturb.service"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))
```

##### healthd

```diff

 			(global-name "com.apple.coreaudio.adam.hae.notification")
 			(global-name "com.apple.depth.divingd")
 			(global-name "com.apple.healthappd")
+			(global-name "com.apple.internal.cognitionhealthd")
 			(global-name "com.apple.locationd.smoother")
 			(global-name "com.apple.schooltime.schedule")
 		))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))

 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (xpc-service-name "com.apple.datamigrator"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.routined.safetyMonitor"))
 		(require-not (global-name "com.apple.datamigrator"))

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
```

##### healthrecordsd

```diff

 		SYS_connectx
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### heard

```diff

 		SYS_connect
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_writev
 		SYS_fchown
 		SYS_fchmod
```

##### heartbeatd

```diff

 	(deny system-memorystatus-control
 		(require-all
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
 		)
```

##### homed

```diff

 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.network.IPConfiguration"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.mobileactivationd"))

 		SYS_listen
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
```

##### icloudmailagent

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.runningboard"))
```

##### icloudwebd

```diff

 		SYS_rename
 		SYS_sendto
 		SYS_shutdown
+		SYS_socketpair
 		SYS_mkdir
 		SYS_rmdir
 		SYS_pread

 		SYS_pwritev
 		SYS_preadv_nocancel
 		SYS_pwritev_nocancel
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 
```

##### intelligenceplatformd

```diff

 		SYS_connect
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_readv
 		SYS_writev
 		SYS_rename

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_info
 		vm_remap_external
 		mach_make_memory_entry_64
 		vm_reallocate
```

##### intelligentroutingd

```diff

 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.nearbyd.xpc.nearbyinteraction"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.research.adtcd"))

 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (xpc-service-name "com.apple.IntelligentRoutingDaemonLLMService"))
```

##### ioupsd

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### itunesstored

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### jetpackassetd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### keybagd

```diff

 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.darwindirectory")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### knowledgeconstructiond

```diff

 		SYS_connect
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_readv
 		SYS_writev
 		SYS_rename

 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
+		MSC_thread_self_trap
 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
```

##### launchCarDisplaySim

```diff

 	(require-any
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### liveactivitiesd

```diff

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.appconduitd.device-connection"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```

##### locationd

```diff

 		mach_make_memory_entry_64
 		vm_reallocate
 		mach_vm_read
+		mach_vm_write
 		mach_vm_copy
 		mach_vm_map_external
 		mach_vm_remap_external
```

##### locationpushd

```diff

 		task_get_special_port_from_user
 		task_set_special_port
 		semaphore_create
+		semaphore_destroy
 		task_set_exc_guard_behavior
 		thread_info
 		vm_copy
```

##### lsd

```diff

 		SYS_listxattr
 		SYS_flistxattr
 		SYS_fsctl
+		SYS_posix_spawn
 		SYS_ffsctl
 		SYS_shm_open
 		SYS_sem_open
```

##### lskdd

```diff

 		(require-not (global-name "com.apple.fpassetmanagerd"))
 		(require-not (global-name "com.apple.research.adtcd"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.fairplayd.xpc"))
+		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
```

##### managedappdistributiond

```diff

 		(require-not (global-name "com.apple.storekitd"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.pearld"))

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### medialibraryd

```diff

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### mediaremoted

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### merchantd

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### migrationd

```diff

 		SYS_write
 		SYS_open
 		SYS_close
+		SYS_link
 		SYS_unlink
 		SYS_chmod
 		SYS_getfsstat
```

##### milod

```diff

 		(require-not (global-name "com.apple.timesync.expositor"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.nearbyd.xpc.nearbyinteraction"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.SystemConfiguration.helper"))

 		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
```

##### mlhostd

```diff

 		task_get_special_port_from_user
 		task_set_special_port
 		semaphore_create
+		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
 		thread_terminate
```

##### mobileactivationd

```diff

 		SYS___pthread_fchdir
 		SYS_bsdthread_create
 		SYS_bsdthread_terminate
+		SYS_kqueue
 		SYS_kevent
 		SYS_bsdthread_register
 		SYS_workq_open

 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np
+		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_connectx

 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
 		SYS_preadv

 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
+		MSC_thread_self_trap
 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC_semaphore_signal_trap

 		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_service_get_matching_services_bin
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_destroy
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 		vm_remap_external
 		mach_make_memory_entry_64
 		vm_reallocate
+		mach_vm_read
 		mach_vm_copy
 		mach_vm_map_external
 		mach_vm_remap_external
```

##### mobilerepaird

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.lsd.open"))
```

##### mobiletimerd

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
 
```

##### momentsd

```diff

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_info
 		thread_policy
 		vm_remap_external
 		vm_reallocate
```

##### nanobackupd

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### nanomapscd

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
 
```

##### navd

```diff

 		SYS_proc_rlimit_control
 		SYS_clonefileat
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### nebulad

```diff

 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.carkit.app.service"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
```

##### newsd

```diff

 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figcpecryptor.xpc"))
 		(require-not (global-name "com.apple.carkit.app.service"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.coremedia.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
```

##### nfcd

```diff

 			(global-name "com.apple.accessoryd.nf-events")
 		))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
+		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
```

##### nsurlsessiond

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### pcapd

```diff

 		task_set_exc_guard_behavior
 		thread_info
 		vm_remap_external
+		mach_make_memory_entry_64
 		vm_reallocate
 		mach_vm_map_external
 		mach_vm_region

 	(deny system-memorystatus-control
 		(require-all
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
 		)
```

##### peakpowermanagerd

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### photosfaced

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.research.adtcd"))

 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.terminusd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### pppd

```diff

 		MSC__kernelrpc_mach_port_allocate_trap
 		MSC__kernelrpc_mach_port_deallocate_trap
 		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_member_trap
 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
```

##### privatecloudcomputed

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### progressd

```diff

 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```

##### promotedcontentd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_dup2
 		SYS_fcntl
 		SYS_select
 		SYS_fsync

 		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		thread_get_state_to_user
 		thread_suspend
 		thread_resume
+		thread_info
 		thread_policy
 		vm_remap_external
 		vm_reallocate
```

##### rapportd

```diff

 		SYS_proc_rlimit_control
 		SYS_connectx
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### replayd

```diff

 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
-		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-not (xpc-service-name "com.apple.DocumentManagerCore.Downloads"))
 		(require-any
 			(require-all
+				(require-not (global-name "com.apple.FileProvider"))
 				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 			(require-all
 				(xpc-service-name "*")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.FileProvider"))
 				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```

##### resourcegrabberd

```diff

 		SYS_setrlimit
 		SYS_mmap
 		SYS_lseek
+		SYS_ftruncate
 		SYS_sysctl
 		SYS_open_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
+		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_fgetxattr
 		SYS_setxattr
+		SYS_fsetxattr
 		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
```

##### restoreserviced

```diff

 		(iokit-registry-entry-class "AppleH10CamInUserClient")
 		(iokit-registry-entry-class "AppleH13CamInUserClient")
 		(iokit-registry-entry-class "AppleHPMUserClient")
+		(iokit-registry-entry-class "AppleMobileApNonceUserClient")
+		(iokit-registry-entry-class "AppleSEPUserClient")
 		(iokit-registry-entry-class "BongoDeviceUserClient")
 	)
 )

 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_get_refs
+		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
```

##### rtcreportingd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### runningboardd

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.lsd.xpc"))

 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### safetyalertsd

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
```

##### scrod

```diff

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.assistant.client"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
+		(require-not (global-name "com.apple.chronoservices"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
```

##### searchpartyd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### shazamd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### siriknowledged

```diff

 		task_set_exc_guard_behavior
 		task_create_identity_token
 		thread_terminate
+		thread_info
 		thread_policy
 		vm_copy
 		vm_remap_external
```

##### softwareupdateservicesd

```diff

 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.coreduetd.context"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.mobileassetd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))

 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid
+		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_service_open_extended
 		io_connect_method
 		io_connect_async_method
+		io_connect_set_notification_port_64
 		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
```

##### spaceattributiond

```diff

 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.research.adtcd"))
```

##### spindump

```diff

 		(literal "/usr/libexec/spindump_fileparser")
 		(literal "/usr/sbin/kextstat")
 		(literal "/usr/sbin/lsof")
+		(literal "/usr/sbin/spindump")
 	)
 )
 

 		(literal "/usr/libexec/spindump_fileparser")
 		(literal "/usr/sbin/kextstat")
 		(literal "/usr/sbin/lsof")
+		(literal "/usr/sbin/spindump")
 	)
 )
 
```

##### splashboardd

```diff

 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.carkit.app.service"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
```

##### storagedatad

```diff

 		task_set_special_port
 		semaphore_create
 		semaphore_destroy
+		task_create_identity_token
 		thread_info
 		vm_remap_external
 		vm_reallocate
```

##### storekitd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### symptomsd

```diff

 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
 		SIOCGIFINTERFACESTATE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFNETSIGNATURE
 		SIOCGIFPROBECONNECTIVITY
```

##### sysdiagnosed

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.springboard.statusbarservices"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.seeding.client"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 				))
 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
-				(require-not (literal "/usr/sbin/lsof"))
+				(require-not (require-any
+					(literal "/usr/sbin/lsof")
+					(literal "/usr/sbin/spindump")
+				))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (literal "/bin/ls"))

 				))
 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
-				(require-not (literal "/usr/sbin/lsof"))
+				(require-not (require-any
+					(literal "/usr/sbin/lsof")
+					(literal "/usr/sbin/spindump")
+				))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (literal "/bin/ls"))

 				))
 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
-				(require-not (literal "/usr/sbin/lsof"))
+				(require-not (require-any
+					(literal "/usr/sbin/lsof")
+					(literal "/usr/sbin/spindump")
+				))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (literal "/bin/ls"))

 				))
 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
-				(require-not (literal "/usr/sbin/lsof"))
+				(require-not (require-any
+					(literal "/usr/sbin/lsof")
+					(literal "/usr/sbin/spindump")
+				))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (literal "/bin/ls"))
```

##### terminusd

```diff

 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.mDNSResponder.control"))
```

##### toolkitd

```diff

 
 (allow device-camera)
 
-(deny mach-lookup)
+(deny mach-lookup
+	(require-all
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-all
+			(system-attribute developer-mode)
+			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
+		)
+	)
+)
 
 (deny system-kext*)
 
```

##### triald

```diff

 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))

 		SYS_flock
 		SYS_sendto
 		SYS_shutdown
+		SYS_socketpair
 		SYS_mkdir
 		SYS_rmdir
 		SYS_gethostuuid
```

##### uarpassetmanagerd

```diff

 		SYS_psynch_rw_upgrade
 		SYS_psynch_mutexwait
 		SYS_psynch_mutexdrop
+		SYS_psynch_cvbroad
+		SYS_psynch_cvsignal
+		SYS_psynch_cvwait
 		SYS_psynch_rw_rdlock
 		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
+		SYS_psynch_cvclrprepost
 		SYS_issetugid
 		SYS___pthread_kill
+		SYS___pthread_sigmask
 		SYS___sigwait
+		SYS___pthread_markcancel
+		SYS___pthread_canceled
 		SYS_proc_info
 		SYS_getdirentries64
 		SYS_getfsstat64
+		SYS___pthread_chdir
+		SYS___pthread_fchdir
 		SYS_thread_selfid
 		SYS___mac_syscall
 		SYS_read_nocancel
```

##### usernotificationsd

```diff

 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
```

##### videosubscriptionsd

```diff

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```

##### visioncompaniond

```diff

 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```

##### watchlistd

```diff

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### weatherd

```diff

 		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getrusage
 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
```

##### wirelessinsightsd

```diff

 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.geod"))
```
