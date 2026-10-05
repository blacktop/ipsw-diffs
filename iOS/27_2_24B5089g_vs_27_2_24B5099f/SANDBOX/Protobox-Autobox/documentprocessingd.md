## documentprocessingd

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

(deny mach-lookup
	(require-all
		(global-name "com.apple.dt.testmanagerd.uiprocess")
		(require-not (global-name "com.apple.mobileassetd.v2"))
		(require-not (global-name "com.apple.lsd.mapdb"))
		(require-not (global-name "com.apple.generativesearch.server.indexing"))
		(require-not (global-name "com.apple.mobileasset.autoasset"))
		(require-not (global-name "com.apple.logd.events"))
		(require-not (global-name "com.apple.logd"))
		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
		(require-not (global-name "com.apple.PowerManagement.control"))
		(require-not (system-attribute developer-mode))
	)
)

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
	(fsctl-command APFSIOC_DIR_STATS_OP FSIOC_CAS_BSDFLAGS)
)

(deny system-kas-info)

(allow process-exec-update-label)
```
