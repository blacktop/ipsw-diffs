## SUDaemonHelperService

> Group: 🆕 NEW

```scheme
(version 1)
(disable-callouts)

(allow default)

(deny file-ioctl)

(deny generic-issue-extension)

(deny iokit-get-properties)

(deny iokit-open*)
(allow iokit-open*
	(require-any
		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
	)
)

(deny iokit-open-service)

(deny iokit-set-properties)

(deny ipc*)

(allow ipc-sysv-shm)

(deny isp-command-send)

(deny mach-host-special-port-set)

(deny mach-issue-extension)

(deny process-codesigning)

(deny process-exec*)

(allow process-exec-interpreter)

(deny sysctl*
	(require-all
		(sysctl-name "vm.debug_range_enabled")
		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
		(require-not (system-attribute developer-mode))
	)
)

(deny system-fsctl)
(allow system-fsctl
	(fsctl-command FSIOC_CAS_BSDFLAGS)
)

(deny system-kas-info)

(allow process-exec-update-label)
```
