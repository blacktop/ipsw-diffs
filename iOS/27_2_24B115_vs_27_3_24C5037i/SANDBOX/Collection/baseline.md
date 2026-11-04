## baseline

> Group: ⬆️ Updated

```diff

 (deny appleevent-send)
 
 (allow asr-parser-enter)
+(autobox asr-parser-enter
+	(require-any
+		(profile-flag "autobox-client")
+		(profile-flag "autobox-client-no-exception-entitlements")
+	)
+)
 
 (allow authorization-right-obtain
 	(with report)

 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.bin")
 				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.plist")
+				(literal "/private/var/protected/trustd/SharedAssets/AnalyticsAllowlist_Apps.bin")
+				(literal "/private/var/protected/trustd/SharedAssets/AnalyticsAllowlist_Domains.bin")
 			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")
 			)
-			(require-any
-				(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
-				(subpath "/private/var/db/datadetectors/sys")
-			)
 			(subpath "/Library/RegionFeatures")
 			(subpath "/System/Library")
+			(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
 			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+			(subpath "/private/var/db/datadetectors/sys")
 			(subpath "/private/var/db/timezone")
 			(subpath "/private/var/preferences/Logging")
 			(subpath "/usr/lib")

 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.bin")
 				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.plist")
+				(literal "/private/var/protected/trustd/SharedAssets/AnalyticsAllowlist_Apps.bin")
+				(literal "/private/var/protected/trustd/SharedAssets/AnalyticsAllowlist_Domains.bin")
 			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")
 			)
-			(require-any
-				(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
-				(subpath "/private/var/db/datadetectors/sys")
-			)
 			(subpath "/Library/RegionFeatures")
 			(subpath "/System/Library")
+			(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
 			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+			(subpath "/private/var/db/datadetectors/sys")
 			(subpath "/private/var/db/timezone")
 			(subpath "/private/var/preferences/Logging")
 			(subpath "/usr/lib")

 	(require-all
 		(profile-flag "common-debugging-rules")
 		(require-any
+			(global-name "com.apple.gputools.service")
 			(global-name "com.apple.hangtracerd")
 			(require-all
 				(global-name "com.apple.osanalytics.osanalyticshelper")

 				)
 			)
 			(require-any
-				(global-name "com.apple.gputools.service")
 				(global-name "com.apple.hangtelemetryd")
 				(global-name "com.apple.hangtracermonitor")
 			)

 		(extension "com.apple.security.exception.sysctl.read-only")
 	)
 )
+(allow sysctl-read
+	(require-all
+		(sysctl-name "vm.debug_range_enabled")
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(profile-flag "common-exception-entitlement-rules")
+				(extension "com.apple.security.exception.sysctl.read-only")
+			)
+			(system-attribute developer-mode)
+		)
+	)
+)
 (allow sysctl-read
 	(require-all
 		(require-any

 		)
 	)
 )
+(allow sysctl-read
+	(require-all
+		(profile-flag "common-exception-entitlement-rules")
+		(extension "com.apple.security.exception.sysctl.read-write")
+	)
+)
 (allow sysctl-read
 	(require-all
 		(profile-flag "common-sysctl-rules")

 				(sysctl-name "kern.usrstack64")
 				(sysctl-name "kern.waketime")
 				(sysctl-name "kern.wq_limit_cooperative_threads")
-				(sysctl-name "machdep.virtual_address_size")
-				(sysctl-name "security.mac.amfi.developer_mode_status")
 				(sysctl-name "security.mac.lockdown_mode_state_public")
 				(sysctl-name "security.mac.sandbox.sentinel")
 				(sysctl-name "sysctl.proc_translated")

 				(sysctl-name "kern.maxfilesperproc")
 				(sysctl-name "kern.osversion")
 			)
+			(require-any
+				(sysctl-name "machdep.virtual_address_size")
+				(sysctl-name "security.mac.amfi.developer_mode_status")
+			)
 			(sysctl-name "hw.cpusubfamily")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")

 		)
 	)
 )
-(allow sysctl-read
-	(require-all
-		(sysctl-name "kern.wq_limit_cooperative_threads")
-		(profile-flag "common-sysctl-rules")
-	)
-)
 (allow sysctl-read
 	(require-all
 		(profile-flag "common-exception-entitlement-rules")

 				(%entitlement-is-bool-true "com.apple.security.exception.process-info")
 				(require-any
 					(extension "com.apple.security.exception.sysctl.read-only")
-					(require-any
-						(sysctl-name "kern.proc.*")
-						(sysctl-name "kern.procargs2.*")
-					)
 					(require-any
 						(sysctl-name "sysctl.proc_cputype.*")
 						(sysctl-name "sysctl.proc_native.*")
 					)
+					(sysctl-name "kern.proc.*")
+					(sysctl-name "kern.procargs2.*")
 				)
 			)
 		)

 )
 (allow sysctl-read
 	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(extension "com.apple.security.exception.sysctl.read-write")
+		(sysctl-name "kern.wq_limit_cooperative_threads")
+		(profile-flag "common-sysctl-rules")
 	)
 )
 (allow sysctl-read
 	(require-all
-		(sysctl-name "vm.debug_range_enabled")
+		(sysctl-name "vm.native_hw_pagesize")
 		(require-any
 			(require-all
 				(profile-flag "common-debugging-rules")

 		(profile-flag "common-rules")
 		(require-any
 			(preference-domain "com.apple.Accessibility")
+			(preference-domain "com.apple.assistant.public")
 			(preference-domain "com.apple.da")
 			(preference-domain "kCFPreferencesAnyApplication")
 			(require-all

 		(profile-flag "common-rules")
 		(require-any
 			(preference-domain "com.apple.Accessibility")
+			(preference-domain "com.apple.assistant.public")
 			(preference-domain "com.apple.da")
 			(preference-domain "kCFPreferencesAnyApplication")
 			(require-all
```
