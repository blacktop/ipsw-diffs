## bioconvenienced

> Group: 🆕 NEW

```scheme
(version 1)
(disable-callouts)

(allow default)

(deny file-ioctl
	(process-attribute is-autoboxed)
)
(allow file-ioctl
	(require-all
		(process-attribute is-autoboxed)
		(ioctl-command (_IO "h" 4))
	)
)

(deny generic-issue-extension
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny iokit-issue-extension
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny iokit-open-user-client
	(process-attribute is-autoboxed)
)
(allow iokit-open-user-client
	(require-all
		(process-attribute is-autoboxed)
		(require-any
			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
		)
	)
)

(deny iokit-set-properties
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny ipc*
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny ipc-posix-shm-read-data
	(process-attribute is-autoboxed)
)
(allow ipc-posix-shm-read-data
	(require-all
		(process-attribute is-autoboxed)
		(ipc-posix-name "com.apple.featureflags.shm")
	)
)

(deny job-creation
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny mach-issue-extension
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny mach-lookup
	(process-attribute is-autoboxed)
)

(deny process-exec*
	(with no-report)
	(process-attribute is-autoboxed)
)

(deny sysctl*
	(require-all
		(process-attribute is-autoboxed)
		(sysctl-name "vm.debug_range_enabled")
		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
		(require-not (system-attribute developer-mode))
	)
)

(deny system-fsctl
	(process-attribute is-autoboxed)
)
(allow system-fsctl
	(require-all
		(process-attribute is-autoboxed)
		(fsctl-command FSIOC_CAS_BSDFLAGS)
	)
)

(deny system-kas-info)
```
