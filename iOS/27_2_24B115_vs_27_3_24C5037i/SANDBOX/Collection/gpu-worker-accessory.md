## gpu-worker-accessory

> Group: 🆕 NEW

```scheme
(version 1)
(%extends-builtin "usernotifications-accessory")

;; (default) inherited from parent profile "usernotifications-accessory"
(delegate default)

(allow asr-parser-enter)

(allow coalition-info
	(process-attribute is-apple-signed-executable)
)
(deny coalition-info)

(allow consume-extension)

(allow file-graft)

(allow file-lock)

(allow file-read-metadata
	(require-any
		(literal "${HOME}")
		(literal "${HOME}/Library/Preferences")
	)
)

(allow file-ungraft)

(deny file-write-setugid)

(allow fs-info)

(allow iokit-get-properties
	(require-all
		(require-any
			(iokit-property "MetalPluginClassName")
			(iokit-property "MetalPluginName")
		)
		(iokit-registry-entry-class "IOAcceleratorES")
	)
)

(allow iokit-open-user-client
	(require-any
		(iokit-connection "IOGPU")
		(iokit-connection "IOGraphicsAccelerator2")
		(iokit-registry-entry-class "AGXCommandQueue")
		(iokit-registry-entry-class "AGXDevice")
		(iokit-registry-entry-class "AGXSharedUserClient")
		(iokit-registry-entry-class "IOAccelContext")
		(iokit-registry-entry-class "IOAccelContext2")
		(iokit-registry-entry-class "IOAccelDevice")
		(iokit-registry-entry-class "IOAccelDevice2")
		(iokit-registry-entry-class "IOAccelSharedUserClient")
		(iokit-registry-entry-class "IOAccelSharedUserClient2")
		(iokit-registry-entry-class "IOAccelSubmitter2")
		(iokit-registry-entry-class "IOGPUDeviceUserClient")
	)
)

(allow isp-command-send)

(deny job-creation)

(allow mach-derive-port)

(allow mach-lookup
	(require-any
		(global-name "com.apple.cvmsServ")
		(global-name "com.apple.gpumemd.source")
		(xpc-service-name "com.apple.AGXCompilerService*")
		(xpc-service-name "com.apple.MTLCompilerService")
	)
)
(deny mach-lookup
	(require-any
		(global-name "com.apple.chrono.accessoryLiveActivities")
		(global-name "com.apple.usernotifications.accessory.session")
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
		SYS_getpid
		SYS_getuid
		SYS_kill
		SYS_getgid
		SYS_umask
		SYS_flock
		SYS_sysctl
		SYS_getumask
		SYS_sysctlbyname
		SYS_issetugid
		SYS___pthread_kill
		SYS_terminate_with_payload
		SYS_abort_with_payload)
)

(allow syscall-mach
	(machtrap-number MSC_iokit_user_client_trap)
)

(allow syscall-mig)

(allow sysctl-read
	(require-all
		(sysctl-name "kern.bootsessionuuid")
		(signing-identifier "com.apple.*")
	)
)

(deny system-kas-info)

(allow system-privilege)

(allow user-preference-read
	(require-any
		(preference-domain "com.apple.Metal")
		(preference-domain "com.apple.opengl")
	)
)

(allow managed-preference-read
	(require-any
		(preference-domain "com.apple.Metal")
		(preference-domain "com.apple.opengl")
	)
)

(allow exception-entitlement)

(allow process-exec-update-label)
```
