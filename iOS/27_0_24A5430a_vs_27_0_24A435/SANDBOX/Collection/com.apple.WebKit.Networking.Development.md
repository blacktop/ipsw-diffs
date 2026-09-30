## com.apple.WebKit.Networking.Development

> Group: ⬆️ Updated

```diff

 (deny default)
 
 (deny darwin-notification-post)
-(allow darwin-notification-post
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow darwin-notification-post
 	(require-any
 		(notification-name "AppleDatePreferencesChangedNotification")

 		(notification-name "AppleTemperatureUnitPreferencesChangedNotification")
 		(notification-name "AppleTextBehaviorPreferencesChangedNotification")
 		(notification-name "AppleTimePreferencesChangedNotification")
+		(notification-name "com.apple.CFNetwork*")
 		(notification-name "com.apple.CFPreferences._domainsChangedExternally")
 		(notification-name "com.apple.LaunchServices.database")
 		(notification-name "com.apple.WebKit.Cache.dump")

 	)
 )
 
+(allow file-ioctl
+	(literal "/dev/dtracehelper")
+)
+
 (allow file-issue-extension
 	(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
 )

 )
 
 (deny file-map-executable)
-(allow file-map-executable
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow file-map-executable
 	(require-any
 		(extension "com.apple.sandbox.executable")

 
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-bool-true "com.apple.private.networkextension.configuration")
+		(require-not (literal "/private/etc/group"))
+		(require-any
+			(extension "com.apple.app-sandbox.read")
+			(extension "com.apple.app-sandbox.read-write")
+			(literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist")
+			(literal "/private/etc/hosts")
+			(literal "/private/etc/passwd")
+			(literal "/private/etc/services")
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist")
+			(literal "/private/var/db/com.apple.networkextension.*")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+				(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
+				(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+			)
+			(subpath "/")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+		)
 	)
 )
 (allow file-read*
 	(require-any
-		(extension "com.apple.app-sandbox.read")
-		(extension "com.apple.app-sandbox.read-write")
 		(extension "com.apple.sandbox.executable")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist")
+		(literal "/dev/dtracehelper")
 		(literal "/dev/urandom")
-		(literal "/private/etc/hosts")
-		(literal "/private/etc/passwd")
-		(literal "/private/etc/services")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(literal "/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-		(literal "/private/var/db/com.apple.networkextension.*")
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
 		(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
-		(subpath "/")
 		(subpath "/Library/RegionFeatures")
 		(subpath "/System/Cryptexes/App")
 		(subpath "/System/Cryptexes/OS")

 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_WebContentRestrictions")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 
 (allow file-read-data
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-bool-true "com.apple.private.networkextension.configuration")
+		(require-not (literal "/private/etc/group"))
+		(require-any
+			(extension "com.apple.app-sandbox.read")
+			(extension "com.apple.app-sandbox.read-write")
+			(literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist")
+			(literal "/private/etc/hosts")
+			(literal "/private/etc/passwd")
+			(literal "/private/etc/services")
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist")
+			(literal "/private/var/db/com.apple.networkextension.*")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+				(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
+				(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+			)
+			(subpath "/")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+		)
 	)
 )
 (allow file-read-data
 	(require-any
-		(extension "com.apple.app-sandbox.read")
-		(extension "com.apple.app-sandbox.read-write")
 		(extension "com.apple.sandbox.executable")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist")
+		(literal "/dev/dtracehelper")
 		(literal "/dev/urandom")
-		(literal "/private/etc/hosts")
-		(literal "/private/etc/passwd")
-		(literal "/private/etc/services")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(literal "/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-		(literal "/private/var/db/com.apple.networkextension.*")
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 		(literal "/usr/local/lib/log")
-		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
 		(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
-		(subpath "/")
 		(subpath "/Library/RegionFeatures")
 		(subpath "/System/Cryptexes/App")
 		(subpath "/System/Cryptexes/OS")

 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_WebContentRestrictions")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 	)
 )
 
-(allow file-read-metadata)
+(allow file-read-metadata
+	(require-all
+		(require-not (literal "${HOME}/Library/Caches/powerlog.launchd"))
+		(require-any
+			(literal "${HOME}")
+			(literal "${HOME}/Library/Preferences")
+			(require-not (literal "/private/var/run/syslog"))
+			(vnode-type SYMLINK)
+		)
+	)
+)
 
 (allow file-write*
 	(extension "com.apple.app-sandbox.read-write")
 )
 
+(allow file-write-create
+	(extension "com.apple.app-sandbox.read-write")
+)
+(deny file-write-create
+	(require-all
+		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
+			(vnode-type SYMLINK)
+		)
+	)
+)
+
+(allow file-write-data
+	(require-any
+		(extension "com.apple.app-sandbox.read-write")
+		(literal "/dev/dtracehelper")
+	)
+)
+
 (deny fs-quota*)
 
 (deny fs-snapshot-mount)
 
 (deny iokit-get-properties)
-(allow iokit-get-properties
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow iokit-get-properties
 	(iokit-property "IORegistryEntryPropertyKeys")
 )
 
-(allow iokit-open-user-client
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow iokit-open-user-client
 	(iokit-registry-entry-class "AppleKeyStoreUserClient")
 )
 
 (deny iokit-open-service)
-(allow iokit-open-service
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow iokit-open-service
 	(iokit-registry-entry-class "AppleKeyStore")
 )

 
 (deny mach-cross-domain-lookup)
 
-(allow mach-lookup
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.diagnosticd")
-		(require-not (process-attribute is-apple-signed-executable))
+		(global-name "com.apple.imagent.EnhancedLinkSecurityStore")
+		(require-not (state-flag "BlockEnhancedSecurityLinks"))
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.imagent.EnhancedLinkSecurityStore")
-		(require-not (state-flag "BlockEnhancedSecurityLinks"))
+		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
+		(require-not (global-name "com.apple.hangtracerd"))
+		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.aggregated"))
+		(require-not (xpc-service-name "*"))
+		(require-any
+			(global-name "com.apple.ProgressReporting")
+			(global-name "com.apple.containermanagerd")
+			(global-name "com.apple.containermanagerd.system")
+			(global-name "com.apple.ctcategories.service")
+			(global-name "com.apple.duetactivityscheduler")
+			(global-name "com.apple.logd")
+			(global-name "com.apple.logd.events")
+			(global-name "com.apple.lsd.mapdb")
+			(global-name "com.apple.mobileasset.autoasset")
+			(global-name "com.apple.nesessionmanager.content-filter")
+			(global-name "com.apple.passd.in-app-payment")
+			(global-name "com.apple.passd.library")
+			(global-name "com.apple.runningboard")
+			(global-name "com.apple.siri.context.service")
+			(global-name "com.apple.system.libinfo.muser")
+			(global-name "com.apple.system.notification_center")
+			(global-name "com.apple.tccd")
+			(global-name "com.apple.webprivacyd")
+			(require-any
+				(global-name "com.apple.WebPrivacy.Service")
+				(global-name "com.apple.ciphermld")
+				(global-name "com.apple.webkit.adattributiond.service")
+				(global-name "com.apple.webkit.webpushd.service")
+			)
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.diagnosticd")
+		(require-any
+			(require-all
+				(require-not (xpc-service-name "*"))
+				(require-any
+					(global-name "com.apple.ProgressReporting")
+					(global-name "com.apple.containermanagerd")
+					(global-name "com.apple.containermanagerd.system")
+					(global-name "com.apple.ctcategories.service")
+					(global-name "com.apple.duetactivityscheduler")
+					(global-name "com.apple.logd")
+					(global-name "com.apple.logd.events")
+					(global-name "com.apple.lsd.mapdb")
+					(global-name "com.apple.mobileasset.autoasset")
+					(global-name "com.apple.nesessionmanager.content-filter")
+					(global-name "com.apple.passd.in-app-payment")
+					(global-name "com.apple.passd.library")
+					(global-name "com.apple.runningboard")
+					(global-name "com.apple.siri.context.service")
+					(global-name "com.apple.system.libinfo.muser")
+					(global-name "com.apple.system.notification_center")
+					(global-name "com.apple.tccd")
+					(global-name "com.apple.webprivacyd")
+					(require-any
+						(global-name "com.apple.WebPrivacy.Service")
+						(global-name "com.apple.ciphermld")
+						(global-name "com.apple.webkit.adattributiond.service")
+						(global-name "com.apple.webkit.webpushd.service")
+					)
+				)
+			)
+			(require-not (process-attribute is-apple-signed-executable))
+		)
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.AppSSO.service-xpc")
 		(global-name "com.apple.FileProvider")
 		(global-name "com.apple.GSSCred")
-		(global-name "com.apple.ProgressReporting")
 		(global-name "com.apple.SystemConfiguration.NetworkInformation")
 		(global-name "com.apple.SystemConfiguration.configd")
-		(global-name "com.apple.WebPrivacy.Service")
 		(global-name "com.apple.accountsd.accountmanager")
 		(global-name "com.apple.appstored.xpc")
 		(global-name "com.apple.appstored.xpc.request")
 		(global-name "com.apple.cfnetwork.AuthBrokerAgent")
 		(global-name "com.apple.cfnetwork.cfnetworkagent")
-		(global-name "com.apple.ciphermld")
-		(global-name "com.apple.containermanagerd")
-		(global-name "com.apple.containermanagerd.system")
-		(global-name "com.apple.ctcategories.service")
 		(global-name "com.apple.dnssd.service")
-		(global-name "com.apple.duetactivityscheduler")
-		(global-name "com.apple.logd")
-		(global-name "com.apple.logd.events")
-		(global-name "com.apple.lsd.mapdb")
-		(global-name "com.apple.mobileasset.autoasset")
 		(global-name "com.apple.nehelper")
 		(global-name "com.apple.nesessionmanager")
-		(global-name "com.apple.nesessionmanager.content-filter")
 		(global-name "com.apple.networkserviceproxy.fetch-token")
-		(global-name "com.apple.passd.in-app-payment")
-		(global-name "com.apple.passd.library")
-		(global-name "com.apple.runningboard")
-		(global-name "com.apple.siri.context.service")
 		(global-name "com.apple.symptoms.symptomsd.managed_events")
-		(global-name "com.apple.system.libinfo.muser")
-		(global-name "com.apple.system.notification_center")
-		(global-name "com.apple.tccd")
 		(global-name "com.apple.trustd")
 		(global-name "com.apple.usymptomsd")
-		(global-name "com.apple.webkit.adattributiond.service")
-		(global-name "com.apple.webkit.webpushd.service")
-		(global-name "com.apple.webprivacyd")
 		(xpc-service-name "com.apple.BrowserEngineKit.Intermediary")
 	)
 )

 )
 
 (allow network-outbound
-	(require-any
-		(control-name "com.apple.flow-divert")
-		(control-name "com.apple.netsrc")
-		(literal "/private/var/run/mDNSResponder")
-		(local tcp "*:*")
-		(local udp "*:*")
-		(remote tcp "*:*")
-		(remote udp "*:*")
+	(control-name "com.apple.flow-divert")
+)
+(allow network-outbound
+	(require-all
+		(require-not (remote tcp "localhost:62078"))
+		(require-any
+			(control-name "com.apple.netsrc")
+			(literal "/private/var/run/mDNSResponder")
+			(local tcp "*:*")
+			(local udp "*:*")
+			(remote tcp "*:*")
+			(remote tcp "*:*")
+			(remote udp "*:*")
+			(remote udp "*:*")
+			(require-all
+				(state-flag "BlockNetworkAccess")
+				(local tcp "*:*")
+				(require-not (remote udp "*:*"))
+				(require-not (remote tcp "*:*"))
+				(require-not (literal "/private/var/run/mDNSResponder"))
+			)
+		)
 	)
 )
 
 (deny nvram*)
 
 (deny process-info*)
-(allow process-info*
-	(with report)
-	(system-attribute developer-mode)
-)
 
 (deny process-info-codesignature)
-(allow process-info-codesignature
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-codesignature
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.exception.process-info")

 )
 
 (deny process-info-dirtycontrol)
-(allow process-info-dirtycontrol
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-dirtycontrol
 	(target self)
 )
 
+(allow process-info-pidinfo)
+
 (deny process-info-pidfdinfo)
-(allow process-info-pidfdinfo
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-pidfdinfo
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.exception.process-info")

 )
 
 (deny process-info-pidfileportinfo)
-(allow process-info-pidfileportinfo
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-pidfileportinfo
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.exception.process-info")

 )
 
 (deny process-info-rusage)
-(allow process-info-rusage
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-rusage
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.exception.process-info")

 	)
 )
 
+(allow process-info-sandbox-container)
+
 (deny process-info-setcontrol)
-(allow process-info-setcontrol
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-setcontrol
 	(target self)
 )

 	(target self)
 )
 
+(deny socket-option-get)
 (allow socket-option-get
 	(with report)
 )
+(allow socket-option-get
+	(require-all
+		(socket-option-level IPPROTO_IP)
+		(socket-option-name 25)
+	)
+)
+(allow socket-option-get
+	(require-all
+		(socket-option-level IPPROTO_IPV6)
+		(socket-option-name 125)
+	)
+)
+(allow socket-option-get
+	(require-all
+		(socket-option-level IPPROTO_TCP)
+		(require-any
+			(socket-option-name (_IO "" 6))
+			(socket-option-name SO_REUSEPORT)
+		)
+	)
+)
+(allow socket-option-get
+	(socket-option-name SO_NREAD SO_SNDBUF)
+)
 
+(deny socket-option-set)
 (allow socket-option-set
 	(with report)
 )
+(allow socket-option-set
+	(require-all
+		(socket-option-level IPPROTO_IPV6)
+		(socket-option-name 27 35 36 61 62)
+	)
+)
+(allow socket-option-set
+	(require-all
+		(socket-option-level SOL_SOCKET)
+		(require-any
+			(socket-option-name 0)
+			(socket-option-name SO_DELEGATED)
+			(socket-option-name SO_MARK_KNOWN_TRACKER)
+			(socket-option-name SO_MARK_KNOWN_TRACKER_NON_APP_INITIATED)
+			(socket-option-name SO_NECP_ATTRIBUTES)
+			(socket-option-name SO_NECP_CLIENTUUID)
+			(socket-option-name SO_NECP_LISTENUUID)
+			(socket-option-name SO_NOSIGPIPE)
+			(socket-option-name SO_RCVBUF)
+			(socket-option-name SO_REUSEADDR)
+			(socket-option-name SO_REUSEPORT)
+			(socket-option-name SO_TIMESTAMP)
+		)
+	)
+)
+(allow socket-option-set
+	(require-all
+		(socket-option-level IPPROTO_TCP)
+		(socket-option-name (_IO "" 1))
+	)
+)
+(allow socket-option-set
+	(socket-option-name 7 20 27)
+)
 
 (deny syscall-unix)
-(allow syscall-unix
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow syscall-unix
 	(syscall-number
 		SYS_exit

 		SYS_fsctl
 		SYS_ffsctl
 		SYS_shm_open
+		SYS_shm_unlink
 		SYS_sem_open
 		SYS_sem_close
 		SYS_sysctlbyname

 		SYS_ulock_wait2
 		SYS_map_with_linking_np)
 )
+(deny syscall-unix
+	(with no-report)
+	(require-all
+		(require-not (syscall-number SYS___nexus_set_opt))
+		(syscall-number SYS_crossarch_trap)
+	)
+)
+(deny syscall-unix
+	(require-all
+		(require-not (syscall-number SYS___nexus_set_opt))
+		(syscall-number SYS_crossarch_trap)
+	)
+)
 
 (deny syscall-mach)
-(allow syscall-mach
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow syscall-mach
 	(machtrap-number
 		MSC__kernelrpc_mach_vm_allocate_trap

 )
 
 (deny syscall-mig)
-(allow syscall-mig
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow syscall-mig
 	(kernel-mig-routine
 		host_info

 	(extension "com.apple.security.exception.sysctl.read-write")
 )
 
-(allow sysctl-read
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow sysctl-read
 	(require-all
 		(require-any

 (allow system-audit)
 
 (deny system-fcntl)
-(allow system-fcntl
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow system-fcntl
 	(fcntl-command
 		F_GETFD

 		F_CHECK_LV)
 )
 
-(deny system-mac-syscall)
-(allow system-mac-syscall
-	(with report)
-	(system-attribute developer-mode)
+(deny system-info
+	(with no-report)
+	(info-type "net.link.addr")
 )
+(deny system-info)
+
+(deny system-mac-syscall)
 (with-filter (mac-policy-name "Sandbox")
 	(allow system-mac-syscall
-		(mac-syscall-number 5)
+		(mac-syscall-number 5 65)
+	)
+)
+(with-filter (mac-policy-name "AMFI")
+	(allow system-mac-syscall
+		(mac-syscall-number 102 90)
 	)
 )
 (with-filter (mac-policy-name "vnguard")

 		(mac-syscall-number 1)
 	)
 )
+(with-filter (mac-policy-name "Sandbox")
+	(allow system-mac-syscall
+		(mac-syscall-number 2 4 6 7 67)
+	)
+)
 
 (deny system-privilege)
 (allow system-privilege

 	)
 )
 
-(allow user-preference-read
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow user-preference-read
 	(require-any
 		(extension "com.apple.security.exception.shared-preference.read-only")

 	)
 )
 
-(allow managed-preference-read
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow managed-preference-read
 	(require-any
 		(extension "com.apple.security.exception.managed-preference.read-only")
```
