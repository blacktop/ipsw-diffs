## accessory-extension-point

> Group: 🆕 NEW

```scheme
(version 1)
(%extends-builtin "restrictive-extension")
(accept-profile-extension)
(enable-profile-flag "restrictive-extension")

;; (default) inherited from parent profile "restrictive-extension"

(allow asr-parser-enter)

(allow coalition-info
	(process-attribute is-apple-signed-executable)
)
(deny coalition-info)

(allow consume-extension)

(allow file-graft)

(allow file-issue-extension
	(require-all
		(extension-class "com.apple.mediaserverd.read")
		(require-any
			(extension "com.apple.app-sandbox.read")
			(extension "com.apple.mediaserverd.read")
			(extension "com.apple.quicklook.readonly")
			(extension "com.apple.sharing.airdrop.readonly")
		)
	)
)
(allow file-issue-extension
	(require-all
		(extension-class "com.apple.app-sandbox.read")
		(require-any
			(subpath "/System/Cryptexes")
			(subpath "/private/preboot/Cryptexes")
		)
	)
)
(allow file-issue-extension
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(require-any
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
						(require-any
							(extension-class "com.apple.aned.read-only")
							(extension-class "com.apple.app-sandbox.read")
							(extension-class "com.apple.mediaserverd.read")
						)
					)
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(require-any
							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
							(require-all
								(subpath "/private/var/PersonaVolumes")
								(require-any
									(require-all
										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
										(extension-class "com.apple.app-sandbox.read")
									)
									(require-all
										(subpath "${FRONT_USER_HOME}")
										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
										(require-any
											(extension-class "com.apple.aned.read-only")
											(extension-class "com.apple.app-sandbox.read")
											(extension-class "com.apple.mediaserverd.read")
										)
									)
								)
							)
						)
					)
					(require-all
						(subpath "/private/var/PersonaVolumes")
						(require-any
							(require-all
								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
								(extension-class "com.apple.app-sandbox.read")
							)
							(require-all
								(subpath "${FRONT_USER_HOME}")
								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
								(require-any
									(extension-class "com.apple.aned.read-only")
									(extension-class "com.apple.app-sandbox.read")
									(extension-class "com.apple.mediaserverd.read")
								)
							)
						)
					)
				)
			)
		)
	)
)
(deny file-issue-extension
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(require-any
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
						(require-any
							(extension-class "com.apple.aned.read-only")
							(extension-class "com.apple.app-sandbox.read")
							(extension-class "com.apple.mediaserverd.read")
						)
					)
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(require-any
							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
							(require-all
								(subpath "/private/var/PersonaVolumes")
								(require-any
									(require-all
										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
										(extension-class "com.apple.app-sandbox.read")
									)
									(require-all
										(subpath "${FRONT_USER_HOME}")
										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
										(require-any
											(extension-class "com.apple.aned.read-only")
											(extension-class "com.apple.app-sandbox.read")
											(extension-class "com.apple.mediaserverd.read")
										)
									)
								)
							)
						)
					)
					(require-all
						(subpath "/private/var/PersonaVolumes")
						(require-any
							(require-all
								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
								(extension-class "com.apple.app-sandbox.read")
							)
							(require-all
								(subpath "${FRONT_USER_HOME}")
								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
								(require-any
									(extension-class "com.apple.aned.read-only")
									(extension-class "com.apple.app-sandbox.read")
									(extension-class "com.apple.mediaserverd.read")
								)
							)
						)
					)
				)
			)
		)
	)
)

(allow file-lock)

(allow file-map-executable
	(require-any
		(subpath "/System/Cryptexes")
		(subpath "/private/preboot/Cryptexes")
	)
)

(allow file-read*
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(require-any
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
					)
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(require-any
							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
							(require-all
								(subpath "/private/var/PersonaVolumes")
								(require-any
									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
									(require-all
										(subpath "${FRONT_USER_HOME}")
										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
									)
								)
							)
						)
					)
					(require-all
						(subpath "/private/var/PersonaVolumes")
						(require-any
							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
							(require-all
								(subpath "${FRONT_USER_HOME}")
								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
							)
						)
					)
				)
			)
		)
	)
)
(allow file-read*
	(require-all
		(process-attribute is-apple-signed-executable)
		(require-any
			(literal "/System")
			(literal "/private")
			(literal "/private/preboot")
		)
	)
)
(allow file-read*
	(require-any
		(extension "com.apple.app-sandbox.read")
		(extension "com.apple.mediaserverd.read")
		(extension "com.apple.quicklook.readonly")
		(extension "com.apple.sharing.airdrop.readonly")
		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
		(subpath "${HOME}/Library/Fonts")
		(subpath "/")
		(subpath "/System/Cryptexes")
		(subpath "/private/preboot/Cryptexes")
	)
)
(deny file-read*
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(require-any
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
					)
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(require-any
							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
							(require-all
								(subpath "/private/var/PersonaVolumes")
								(require-any
									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
									(require-all
										(subpath "${FRONT_USER_HOME}")
										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
									)
								)
							)
						)
					)
					(require-all
						(subpath "/private/var/PersonaVolumes")
						(require-any
							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
							(require-all
								(subpath "${FRONT_USER_HOME}")
								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
							)
						)
					)
				)
			)
		)
	)
)

(allow file-read-metadata
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(require-any
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
					)
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(require-any
							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
							(require-all
								(subpath "/private/var/PersonaVolumes")
								(require-any
									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
									(require-all
										(subpath "${FRONT_USER_HOME}")
										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
									)
								)
							)
						)
					)
					(require-all
						(subpath "/private/var/PersonaVolumes")
						(require-any
							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
							(require-all
								(subpath "${FRONT_USER_HOME}")
								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
							)
						)
					)
				)
			)
		)
	)
)
(allow file-read-metadata
	(require-all
		(process-attribute is-apple-signed-executable)
		(require-any
			(literal "/System")
			(literal "/private")
			(literal "/private/preboot")
		)
	)
)
(allow file-read-metadata
	(require-any
		(extension "com.apple.app-sandbox.read")
		(extension "com.apple.mediaserverd.read")
		(extension "com.apple.quicklook.readonly")
		(extension "com.apple.sharing.airdrop.readonly")
		(literal "${HOME}")
		(literal "${HOME}/Library/Preferences")
		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
		(subpath "${HOME}/Library/Fonts")
		(subpath "/")
		(subpath "/System/Cryptexes")
		(subpath "/private/preboot/Cryptexes")
	)
)
(deny file-read-metadata
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(require-any
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
					)
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(require-any
							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
							(require-all
								(subpath "/private/var/PersonaVolumes")
								(require-any
									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
									(require-all
										(subpath "${FRONT_USER_HOME}")
										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
									)
								)
							)
						)
					)
					(require-all
						(subpath "/private/var/PersonaVolumes")
						(require-any
							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
							(require-all
								(subpath "${FRONT_USER_HOME}")
								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
							)
						)
					)
				)
			)
		)
	)
)

(allow file-test-existence
	(require-all
		(subpath "/private/var")
		(extension "com.apple.sandbox.application-group")
		(require-any
			(require-all
				(subpath "${FRONT_USER_HOME}")
				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
			)
			(require-all
				(subpath "/private/var/PersonaVolumes")
				(require-any
					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
					(require-all
						(subpath "${FRONT_USER_HOME}")
						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
					)
				)
			)
		)
	)
)
(allow file-test-existence
	(require-all
		(process-attribute is-apple-signed-executable)
		(require-any
			(literal "/System")
			(literal "/private")
			(literal "/private/preboot")
		)
	)
)
(allow file-test-existence
	(require-any
		(subpath "/")
		(subpath "/System/Cryptexes")
		(subpath "/private/preboot/Cryptexes")
	)
)

(allow file-ungraft)

(deny file-write*
	(require-all
		(extension "com.apple.sandbox.application-group")
		(require-any
			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
			(require-all
				(subpath "/private/var")
				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
				(subpath "${FRONT_USER_HOME}")
			)
		)
	)
)

(deny file-write-setugid)

(allow fs-info)

(allow iokit-get-properties
	(require-all
		(iokit-property "IOSurfaceAcceleratorCapabilitiesDict")
		(iokit-registry-entry-class "IOService")
	)
)
(allow iokit-get-properties
	(require-all
		(iokit-property "soc-generation")
		(iokit-registry-entry-class "IOPlatformDevice")
	)
)
(allow iokit-get-properties
	(require-all
		(iokit-registry-entry-class "AppleJPEGDriver")
		(require-any
			(iokit-property "AppleJPEGNumCores")
			(iokit-property "AppleJPEGSupportsAppleInterchangeFormats")
		)
	)
)

(allow iokit-open-user-client
	(require-all
		(system-attribute virtual-device)
		(require-any
			(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
			(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
		)
	)
)
(allow iokit-open-user-client
	(require-any
		(iokit-registry-entry-class "AGXDevice")
		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
		(iokit-registry-entry-class "IOMobileFramebufferUserClient")
		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
		(iokit-registry-entry-class "IOSurfaceRootUserClient")
	)
)

(allow iokit-open-service
	(require-any
		(iokit-registry-entry-class "AGXAcceleratorG*")
		(iokit-registry-entry-class "AppleCLCD*")
		(iokit-registry-entry-class "AppleJPEGDriver")
		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
		(iokit-registry-entry-class "AppleParavirtDisplay*")
		(iokit-registry-entry-class "AppleParavirtGPU*")
		(iokit-registry-entry-class "IOSurfaceRoot")
	)
)

(allow isp-command-send)

(deny job-creation)

(allow mach-derive-port)

(allow mach-lookup
	(require-all
		(global-name "com.apple.logd")
		(extension "com.apple.media-device-discovery.logging")
	)
)
(allow mach-lookup
	(require-all
		(global-name "com.apple.logd.events")
		(extension "com.apple.media-device-discovery.logging")
	)
)
(allow mach-lookup
	(require-any
		(global-name "com.apple.DeviceAccess.xpc")
		(global-name "com.apple.chrono.accessoryLiveActivities")
		(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
		(global-name "com.apple.coremedia.mediaplaybackd.assetimagegenerator.xpc")
		(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
		(global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc")
		(global-name "com.apple.usernotifications.accessory.session")
		(xpc-service-name "com.apple.ImageIOXPCService")
	)
)

(allow mach-task-exception-port-set)

(allow mach-task-inspect
	(target self)
)

(allow mach-task-name
	(target self)
)

(allow mach-task-read
	(target self)
)

(allow mach-task-special-port*)

(allow necp-client-open)

(allow process-codesigning)

(allow process-info-sandbox-container)

(allow process-iopolicy*)

(allow sandbox-check)

(allow signal
	(target self)
)

(allow syscall-unix
	(syscall-number
		SYS_exit
		SYS_open
		SYS_close
		SYS_getfsstat
		SYS_getpid
		SYS_getuid
		SYS_kill
		SYS_crossarch_trap
		SYS_dup
		SYS_getgid
		SYS_umask
		SYS_fcntl
		SYS_sysctl
		SYS_getumask
		SYS_sysctlbyname
		SYS_issetugid
		SYS___pthread_kill
		SYS_getfsstat64
		SYS___mac_syscall
		SYS_open_nocancel
		SYS_close_nocancel
		SYS_fcntl_nocancel
		SYS_memorystatus_control
		SYS_openat
		SYS_openat_nocancel
		SYS_fstatat
		SYS_fstatat64
		SYS_terminate_with_payload
		SYS_abort_with_payload
		SYS_map_with_linking_np)
)

(allow syscall-mach
	(machtrap-number MSC_iokit_user_client_trap)
)

(allow syscall-mig)

(allow system-fcntl
	(fcntl-command F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
)

(deny system-kas-info)

(with-filter (mac-policy-name "Sandbox")
	(allow system-mac-syscall
		(mac-syscall-number 2 5)
	)
)

(allow system-memorystatus-control)

(allow system-necp-client-action)

(allow system-privilege)

(allow user-preference-read
	(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
)

(allow managed-preference-read
	(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
)

(allow exception-entitlement)

(allow process-exec-update-label)
```
