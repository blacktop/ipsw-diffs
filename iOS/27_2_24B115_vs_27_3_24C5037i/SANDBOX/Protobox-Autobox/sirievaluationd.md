## sirievaluationd

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
		(iokit-registry-entry-class "AppleKeyStoreUserClient")
	)
)

(deny iokit-set-properties)

(deny ipc*)

(deny job-creation)

(deny mach-issue-extension)

(deny mach-lookup
	(require-all
		(global-name "com.apple.dt.testmanagerd.uiprocess")
		(require-not (global-name "com.apple.assistant.client"))
		(require-not (global-name "com.apple.frontboard.systemappservices"))
		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
		(require-not (global-name "com.apple.geod"))
		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
		(require-not (global-name "com.apple.backboard.display.services"))
		(require-not (global-name "com.apple.assistant.analytics-observation"))
		(require-not (global-name "com.apple.logd.admin"))
		(require-not (global-name "com.apple.internal.xctestinternalangel.sessions"))
		(require-not (global-name "com.apple.testmanagerd"))
		(require-not (global-name "com.apple.assistant.analytics"))
		(require-not (global-name "com.apple.CARenderServer"))
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
	(fsctl-command FSIOC_CAS_BSDFLAGS)
)

(deny system-kas-info)

(allow process-exec-update-label)
```
