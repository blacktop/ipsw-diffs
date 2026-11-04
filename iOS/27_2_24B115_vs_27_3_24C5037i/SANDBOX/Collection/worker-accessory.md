## worker-accessory

> Group: 🆕 NEW

```scheme
(version 1)
(%extends-builtin "container")

;; (default) inherited from parent profile "container"
(delegate default)

(deny coalition-info
	(require-not (process-attribute is-apple-signed-executable))
)

(deny file-read-data
	(require-all
		(vnode-type SOCKET)
		(literal "${FRONT_USER_HOME}/Library/ExternalAccessory/ea*")
	)
)

(deny file-write-data
	(require-all
		(vnode-type SOCKET)
		(literal "${FRONT_USER_HOME}/Library/ExternalAccessory/ea*")
	)
)

(deny file-write-setugid)

(deny iokit-open-user-client
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

(deny job-creation)

(allow mach-derive-port)

(deny mach-lookup
	(require-any
		(global-name "com.apple.ExternalAccessory.distributednotification.server")
		(global-name "com.apple.accessories.externalaccessory-server")
		(global-name "com.apple.accessories.transport-server")
		(global-name "com.apple.bluetooth*")
		(global-name "com.apple.cvmsServ")
		(global-name "com.apple.developer.wifi-infrastructure*")
		(global-name "com.apple.gpumemd.source")
		(global-name "com.apple.gputools.producer")
		(global-name "com.apple.gputools.service")
		(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
		(global-name "com.apple.iap2d.xpc")
		(global-name "com.apple.iapd.xpc")
		(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
		(global-name "com.apple.networking.captivenetworksupport")
		(global-name "com.apple.private.corewifi*")
		(global-name "com.apple.replayd")
		(global-name "com.apple.server.bluetooth*")
		(global-name "com.apple.wifi*")
		(xpc-service-name "com.apple.AGXCompilerService*")
		(xpc-service-name "com.apple.MTLCompilerService")
		(xpc-service-name "com.apple.WebKit.GPU")
		(xpc-service-name "com.apple.externalaccessory.WACEAService")
	)
)

(allow mach-task-inspect
	(target self)
)

(allow mach-task-name
	(target self)
)

(allow mach-task-read
	(target self)
)

(allow mach-task-special-port-get
	(target self)
)

(deny network-outbound
	(require-all
		(vnode-type SOCKET)
		(literal "${FRONT_USER_HOME}/Library/ExternalAccessory/ea*")
	)
)

(allow process-codesigning)

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
		SYS_getumask
		SYS_issetugid
		SYS___pthread_kill
		SYS_terminate_with_payload
		SYS_abort_with_payload)
)

(allow syscall-mig
	(kernel-mig-routine
		mach_exception_raise
		mach_exception_raise_state
		mach_exception_raise_state_identity)
)

(deny system-kas-info)

(allow system-privilege)

(allow exception-entitlement)

(allow process-exec-update-label)
```
