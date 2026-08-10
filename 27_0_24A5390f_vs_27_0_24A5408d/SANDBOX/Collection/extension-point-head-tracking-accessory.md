## extension-point-head-tracking-accessory

> Group: 🆕 NEW

```scheme
(version 1)
(%extends-builtin "accessory-extension-point")

;; (default) inherited from parent profile "accessory-extension-point"

(allow asr-parser-enter)

(allow coalition-info
	(process-attribute is-apple-signed-executable)
)
(deny coalition-info)

(allow consume-extension)

(allow file-graft)

(allow file-lock)

(allow file-ungraft)

(deny file-write-setugid)

(allow fs-info)

(allow isp-command-send)

(deny job-creation)

(allow mach-derive-port)

(allow mach-lookup
	(require-any
		(global-name "com.apple.AudioAccessoryKit")
		(global-name "com.apple.AudioAccessorySensorDataWriter")
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
		SYS_getumask
		SYS_issetugid
		SYS___pthread_kill
		SYS_terminate_with_payload
		SYS_abort_with_payload)
)

(allow syscall-mig)

(deny system-kas-info)

(allow system-privilege)

(allow exception-entitlement)

(allow process-exec-update-label)
```
