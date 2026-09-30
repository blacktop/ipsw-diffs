## com.apple.health.records.assembler

> Group: 🆕 NEW

```scheme
(version 1)
(disable-callouts)

(allow default)

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

(deny mach-lookup)

(deny process-exec*)

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
