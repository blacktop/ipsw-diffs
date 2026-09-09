## com.apple.WebKit.GPU.Development

> Group: ⬆️ Updated

```diff

 )
 
 (deny darwin-notification-post)
-(allow darwin-notification-post
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow darwin-notification-post
 	(require-any
 		(notification-name "AppleDatePreferencesChangedNotification")

 (deny file-link)
 
 (deny file-map-executable)
-(allow file-map-executable
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow file-map-executable
 	(require-any
 		(extension "com.apple.sandbox.executable")

 		(extension "com.apple.webkit.camera")
 	)
 )
+(allow file-read*
+	(require-all
+		(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
+		(require-any
+			(literal "/dev/dtracehelper")
+			(literal "/dev/random")
+			(literal "/dev/urandom")
+			(literal "/private/etc/passwd")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(require-all
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+			)
+			(require-any
+				(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+				(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+				(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+				(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
+				(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+			)
+			(subpath "/")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+		)
+	)
+)
 (allow file-read*
 	(require-any
 		(extension "com.apple.app-sandbox.read")

 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
-		(literal "/dev/dtracehelper")
-		(literal "/dev/random")
-		(literal "/dev/urandom")
-		(literal "/private/etc/passwd")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
-		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
 		(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
 		(subpath "${HOME}/Library/Fonts")
-		(subpath "/")
 		(subpath "/Library/RegionFeatures")
 		(subpath "/System/Cryptexes/App")
 		(subpath "/System/Cryptexes/OS")
 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 
 (allow file-read-metadata)
 
+(allow file-read-xattr
+	(require-all
+		(require-not (xattr "com.apple.security.private.*"))
+		(require-any
+			(extension "com.apple.app-sandbox.read")
+			(extension "com.apple.app-sandbox.read-write")
+			(extension "com.apple.sandbox.executable")
+			(extension "com.apple.sharing.airdrop.readonly")
+			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
+			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
+			(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
+			(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
+			(require-all
+				(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
+				(require-any
+					(literal "/dev/dtracehelper")
+					(literal "/dev/random")
+					(literal "/dev/urandom")
+					(literal "/private/etc/passwd")
+					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
+					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+							(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+						)
+					)
+					(require-any
+						(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
+						(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
+						(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
+						(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
+						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
+						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+					)
+					(require-any
+						(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+						(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
+						(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+					)
+					(subpath "/")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+				)
+			)
+			(require-all
+				(subpath "/Library/CoreMediaIO/Plug-Ins/DAL")
+				(require-any
+					(extension "com.apple.webkit.camera")
+					(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
+				)
+			)
+			(require-any
+				(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.plist")
+			)
+			(require-any
+				(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
+				(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
+			)
+			(require-any
+				(subpath "/System/Cryptexes/App")
+				(subpath "/System/Cryptexes/OS")
+				(subpath "/private/preboot/Cryptexes/App")
+				(subpath "/private/preboot/Cryptexes/OS")
+			)
+			(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
+			(subpath "${HOME}/Library/Fonts")
+			(subpath "/Library/RegionFeatures")
+			(subpath "/System/Library")
+			(subpath "/private/var/db/timezone")
+			(subpath "/private/var/preferences/Logging")
+			(subpath "/usr/lib")
+			(subpath "/usr/share")
+		)
+	)
+)
+
 (allow file-write*
 	(extension "com.apple.app-sandbox.read-write")
 )
+(allow file-write*
+	(require-all
+		(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
+		(require-not (literal "${HOME}/Library/Preferences/com.apple.springboard.plist*"))
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+			(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+		)
+	)
+)
+
+(allow file-write-create
+	(require-all
+		(require-not (vnode-type SYMLINK))
+		(require-not (require-any
+			(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist*")
+			(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist*")
+		))
+		(require-any
+			(extension "com.apple.app-sandbox.read-write")
+			(require-all
+				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
+				(require-not (literal "${HOME}/Library/Preferences/com.apple.springboard.plist*"))
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+			)
+		)
+	)
+)
 
 (allow file-write-data
-	(require-any
-		(extension "com.apple.app-sandbox.read-write")
-		(literal "/dev/dtracehelper")
+	(require-all
+		(require-not (literal "/dev/urandom"))
+		(require-not (literal "/dev/random"))
+		(require-any
+			(extension "com.apple.app-sandbox.read-write")
+			(literal "/dev/dtracehelper")
+			(require-all
+				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
+				(require-not (literal "${HOME}/Library/Preferences/com.apple.springboard.plist*"))
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+			)
+		)
+	)
+)
+
+(allow file-write-xattr
+	(require-all
+		(require-not (xattr "com.apple.security.private.*"))
+		(require-any
+			(extension "com.apple.app-sandbox.read-write")
+			(require-all
+				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
+				(require-not (literal "${HOME}/Library/Preferences/com.apple.springboard.plist*"))
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+			)
+		)
 	)
 )
 

 (deny fs-snapshot-mount)
 
 (deny iokit-get-properties)
-(allow iokit-get-properties
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow iokit-get-properties
 	(require-all
-		(iokit-registry-entry-class "IOPlatformDevice")
 		(iokit-property "home-button-type")
+		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
 (allow iokit-get-properties

 	(iokit-connection "IOGPU")
 )
 
-(allow iokit-open-user-client
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow iokit-open-user-client
 	(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	(apply-message-filter

 		(allow iokit-external-trap)
 	)
 )
-(allow iokit-open-user-client
-	(iokit-registry-entry-class "AGXDeviceUserClient")
-)
 (allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(state-flag "local:tested_version_2.0")
 	)
 )
+(allow iokit-open-user-client
+	(require-any
+		(iokit-connection "IOGPU")
+		(iokit-registry-entry-class "AGXDeviceUserClient")
+	)
+)
 
 (deny iokit-open-service)
-(allow iokit-open-service
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow iokit-open-service
 	(require-any
+		(iokit-connection "IOGPU")
 		(iokit-registry-entry-class "AGXAcceleratorG*")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 		(iokit-registry-entry-class "AppleParavirtGPU")

 	(require-any
 		(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 		(global-name "com.apple.coremedia.sts")
-		(system-attribute developer-mode)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobilegestalt.xpc")
-		(extension "com.apple.webkit.extension.mach")
+		(global-name "com.apple.diagnosticd")
+		(require-not (process-attribute is-apple-signed-executable))
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.diagnosticd")
-		(require-not (process-attribute is-apple-signed-executable))
+		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))
+		(require-not (xpc-service-name "*"))
+		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-any
+			(global-name "com.apple.audio.AudioQueueServer")
+			(global-name "com.apple.logd")
+			(global-name "com.apple.logd.events")
+			(global-name "com.apple.runningboard")
+			(global-name "com.apple.system.notification_center")
+			(global-name "com.apple.systemstatus.activityattribution")
+			(global-name "com.apple.tccd")
+			(require-all
+				(global-name "com.apple.mobilegestalt.xpc")
+				(extension "com.apple.webkit.extension.mach")
+			)
+		)
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.airplay.apsynccontroller.xpc")
 		(global-name "com.apple.airplay.endpoint.xpc")
 		(global-name "com.apple.audio.AURemoteIOServer")
-		(global-name "com.apple.audio.AudioQueueServer")
 		(global-name "com.apple.audio.AudioSession")
 		(global-name "com.apple.coremedia.admin")
 		(global-name "com.apple.coremedia.capturesession")

 		(global-name "com.apple.coremedia.videocodecd.decompressionsession")
 		(global-name "com.apple.coremedia.videocodecd.decompressionsession.xpc")
 		(global-name "com.apple.coremedia.volumecontroller.xpc")
-		(global-name "com.apple.logd")
-		(global-name "com.apple.logd.events")
 		(global-name "com.apple.mediaexperience.endpoint.xpc")
 		(global-name "com.apple.mediaexperience.systemmediacastingcontroller.xpc")
 		(global-name "com.apple.mediaremoted.xpc")
-		(global-name "com.apple.runningboard")
-		(global-name "com.apple.system.notification_center")
-		(global-name "com.apple.systemstatus.activityattribution")
-		(global-name "com.apple.tccd")
 		(xpc-service-name "com.apple.MTLCompilerService")
 	)
 )

 
 (deny necp-client-open)
 
+(allow network-outbound
+	(control-name "com.apple.flow-divert")
+)
+
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
 	(target others self)
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
 	(target self)
 )
 
 (deny process-info-pidfileportinfo)
-(allow process-info-pidfileportinfo
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-pidfileportinfo
 	(target self)
 )
 
 (deny process-info-rusage)
-(allow process-info-rusage
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow process-info-rusage
 	(target self)
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

 (deny socket-option-set)
 
 (deny syscall-unix)
-(allow syscall-unix
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow syscall-unix
 	(require-all
 		(state-flag "local:FeatureCoreMLDisabled")

 		SYS_close
 		SYS_close_nocancel
 		SYS_connect
+		SYS_connect_nocancel
+		SYS_connectx
 		SYS_csops
 		SYS_csops_audittoken
 		SYS_dup

 		SYS_shared_region_check_np
 		SYS_shared_region_map_and_slide_2_np
 		SYS_shm_open
+		SYS_shm_unlink
 		SYS_sigaction
 		SYS_sigprocmask
 		SYS_socket

 		SYS_writev
 		SYS_writev_nocancel)
 )
+(deny syscall-unix
+	(with no-report)
+	(syscall-number SYS_crossarch_trap)
+)
+(deny syscall-unix)
 
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

 		mach_eventlink_associate)
 )
 
-(allow sysctl-read
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow sysctl-read
 	(require-any
 		(sysctl-name "hw.activecpu")

 		(sysctl-name "vm.malloc_ranges")
 	)
 )
+(deny sysctl-read
+	(with no-report)
+	(require-all
+		(require-not (sysctl-name "sysctl.proc_native"))
+		(sysctl-name "hw.tbfrequency_compat")
+	)
+)
+(deny sysctl-read
+	(require-all
+		(require-not (sysctl-name "sysctl.proc_native"))
+		(sysctl-name "hw.tbfrequency_compat")
+	)
+)
 
 (allow system-audit)
 
 (deny system-fcntl)
-(allow system-fcntl
-	(with report)
-	(system-attribute developer-mode)
-)
 (allow system-fcntl
 	(fcntl-command
 		F_SETFD

 		F_CHECK_LV)
 )
 
+(deny system-info
+	(with no-report)
+	(info-type "net.link.addr")
+)
+(deny system-info)
+
 (deny system-mac-syscall)
-(allow system-mac-syscall
-	(with report)
-	(system-attribute developer-mode)
+(with-filter (mac-policy-name "AMFI")
+	(allow system-mac-syscall
+		(mac-syscall-number 102 90)
+	)
 )
 (with-filter (mac-policy-name "Sandbox")
 	(allow system-mac-syscall
 		(mac-syscall-number 5 65)
 	)
 )
+(with-filter (mac-policy-name "Sandbox")
+	(allow system-mac-syscall
+		(mac-syscall-number 2 4 6 7 67)
+	)
+)
 
 (deny system-necp-client-action)
 

 	(%entitlement-is-bool-true "com.apple.private.kernel.override-cpumon")
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
