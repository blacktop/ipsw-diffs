## trustdFileHelper

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
		(require-any
			(ipc-posix-name "apple.cfprefs.daemonv1")
			(ipc-posix-name "apple.cfprefs.user.daemonv1")
			(ipc-posix-name "apple.shm.notification_center")
		)
	)
)

(deny ipc-posix-shm-write-data
	(process-attribute is-autoboxed)
)
(allow ipc-posix-shm-write-data
	(require-all
		(process-attribute is-autoboxed)
		(require-any
			(ipc-posix-name "apple.cfprefs.daemonv1")
			(ipc-posix-name "apple.cfprefs.user.daemonv1")
		)
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
	(require-all
		(require-not (global-name "com.apple.system.notification_center"))
		(require-not (global-name "com.apple.system.logger"))
		(require-not (global-name "com.apple.diagnosticd"))
		(require-not (global-name "com.apple.logd"))
		(require-any
			(process-attribute is-autoboxed)
			(require-all
				(system-attribute developer-mode)
				(process-attribute is-autoboxed)
				(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
			)
		)
	)
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
