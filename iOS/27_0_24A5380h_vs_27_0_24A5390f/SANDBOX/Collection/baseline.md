## baseline

> Group: ⬆️ Updated

```diff

 	(with report)
 	(profile-flag "disable-enforcement")
 )
+(allow iokit*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.system.diagnostics.iokit-properties")
+		(profile-flag "common-exception-entitlement-rules")
+	)
+)
+(allow iokit*
+	(require-all
+		(profile-flag "common-mobilegestalt-rules")
+		(iokit-property "IORegistryEntryPropertyKeys")
+	)
+)
 (deny iokit*)
 
 (allow iokit-get-properties
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow iokit-get-properties
-	(require-all
-		(%entitlement-is-bool-true "com.apple.system.diagnostics.iokit-properties")
-		(profile-flag "common-exception-entitlement-rules")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(profile-flag "common-mobilegestalt-rules")
-		(iokit-property "IORegistryEntryPropertyKeys")
-	)
-)
 (deny iokit-get-properties)
 
+(allow iokit-issue-extension
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(deny iokit-issue-extension)
+
+(allow iokit-open*
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(allow iokit-open*
+	(profile-flag "autobox-client-telemetry")
+)
+(autobox iokit-open*
+	(with restrictive-default)
+	(require-any
+		(profile-flag "autobox-client")
+		(profile-flag "autobox-client-no-exception-entitlements")
+	)
+)
+(deny iokit-open*)
+
 (allow iokit-open-user-client
 	(with report)
 	(profile-flag "disable-enforcement")

 	(profile-flag "autobox-client-telemetry")
 )
 (autobox iokit-open-user-client
-	(with restrictive-default)
 	(require-any
 		(profile-flag "autobox-client")
 		(profile-flag "autobox-client-no-exception-entitlements")

 )
 (deny iokit-open-user-client)
 
-(allow iokit-open-service
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow iokit-open-service
-	(profile-flag "autobox-client-telemetry")
-)
-(autobox iokit-open-service
-	(require-any
-		(profile-flag "autobox-client")
-		(profile-flag "autobox-client-no-exception-entitlements")
-	)
-)
-(deny iokit-open-service)
-
 (allow iokit-set-properties
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow iokit-set-properties
-	(profile-flag "autobox-client-telemetry")
-)
-(autobox iokit-set-properties
-	(with restrictive-default)
-	(require-any
-		(profile-flag "autobox-client")
-		(profile-flag "autobox-client-no-exception-entitlements")
-	)
-)
 (deny iokit-set-properties)
 
 (allow ipc*

 )
 (deny ipc*)
 
-(allow ipc-posix-sem-open
+(allow ipc-posix-sem-create
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow ipc-posix-sem-open
+(allow ipc-posix-sem-create
 	(require-all
 		(profile-flag "common-containermanagerd-rules")
 		(ipc-posix-name "containermanagerd.fb_check")
 	)
 )
-(allow ipc-posix-sem-open
+(allow ipc-posix-sem-create
 	(require-all
 		(ipc-posix-name "purplebuddy.sentinel")
 		(profile-flag "common-rules")
 	)
 )
-(deny ipc-posix-sem-open)
+(deny ipc-posix-sem-create)
+
+(allow ipc-posix-sem-wait
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(allow ipc-posix-sem-wait
+	(require-all
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(profile-flag "restrictive-extension")
+				(%entitlement-is-bool-true "get-task-allow")
+				(require-any
+					(ipc-posix-name "/FSM-*")
+					(ipc-posix-name "OA-*")
+					(ipc-posix-name "stack-logs*")
+				)
+			)
+			(require-any
+				(ipc-posix-name "/FSM-*")
+				(ipc-posix-name "OA-*")
+				(ipc-posix-name "stack-logs*")
+			)
+		)
+	)
+)
+(deny ipc-posix-sem-wait)
 
 (allow ipc-posix-shm*
 	(with report)
 	(profile-flag "disable-enforcement")
 )
+(allow ipc-posix-shm*
+	(require-all
+		(ipc-posix-name "apple.cfprefs.*")
+		(profile-flag "common-preferences-rules")
+	)
+)
+(allow ipc-posix-shm*
+	(require-all
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(profile-flag "restrictive-extension")
+				(%entitlement-is-bool-true "get-task-allow")
+				(require-any
+					(ipc-posix-name "gdt-[a-zA-Z0-9]")
+					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-c")
+					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-s")
+				)
+			)
+			(require-any
+				(ipc-posix-name "gdt-[a-zA-Z0-9]")
+				(ipc-posix-name #"gdt-([a-zA-Z0-9])+-c")
+				(ipc-posix-name #"gdt-([a-zA-Z0-9])+-s")
+			)
+		)
+	)
+)
 (allow ipc-posix-shm*
 	(require-all
 		(profile-flag "common-debugging-rules")

 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow ipc-posix-shm-read-data
-	(require-all
-		(ipc-posix-name "apple.cfprefs.*")
-		(profile-flag "common-preferences-rules")
-	)
-)
-(allow ipc-posix-shm-read-data
-	(require-all
-		(profile-flag "common-debugging-rules")
-		(require-any
-			(require-all
-				(profile-flag "restrictive-extension")
-				(%entitlement-is-bool-true "get-task-allow")
-				(require-any
-					(ipc-posix-name "gdt-[a-zA-Z0-9]")
-					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-c")
-					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-s")
-				)
-			)
-			(require-any
-				(ipc-posix-name "gdt-[a-zA-Z0-9]")
-				(ipc-posix-name #"gdt-([a-zA-Z0-9])+-c")
-				(ipc-posix-name #"gdt-([a-zA-Z0-9])+-s")
-			)
-		)
-	)
-)
 (allow ipc-posix-shm-read-data
 	(require-all
 		(profile-flag "common-debugging-rules")

 )
 (deny ipc-posix-shm-read-data)
 
+(allow ipc-posix-shm-write*
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(allow ipc-posix-shm-write*
+	(require-all
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(profile-flag "restrictive-extension")
+				(%entitlement-is-bool-true "get-task-allow")
+				(require-any
+					(ipc-posix-name "/FSM-*")
+					(ipc-posix-name "OA-*")
+					(ipc-posix-name "stack-logs*")
+				)
+			)
+			(require-any
+				(ipc-posix-name "/FSM-*")
+				(ipc-posix-name "OA-*")
+				(ipc-posix-name "stack-logs*")
+			)
+		)
+	)
+)
+(deny ipc-posix-shm-write*)
+
+(allow ipc-posix-shm-write-create
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(allow ipc-posix-shm-write-create
+	(require-all
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(profile-flag "restrictive-extension")
+				(%entitlement-is-bool-true "get-task-allow")
+				(require-any
+					(ipc-posix-name "/FSM-*")
+					(ipc-posix-name "OA-*")
+					(ipc-posix-name "stack-logs*")
+				)
+			)
+			(require-all
+				(require-any
+					(ipc-posix-name "gdt-[a-zA-Z0-9]")
+					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-c")
+					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-s")
+				)
+				(profile-flag "restrictive-extension")
+				(%entitlement-is-bool-true "get-task-allow")
+			)
+			(require-any
+				(ipc-posix-name "/FSM-*")
+				(ipc-posix-name "OA-*")
+				(ipc-posix-name "stack-logs*")
+			)
+		)
+	)
+)
+(deny ipc-posix-shm-write-create)
+
 (allow ipc-posix-shm-write-data
 	(with report)
 	(profile-flag "disable-enforcement")

 )
 (deny ipc-posix-shm-write-data)
 
-(allow ipc-posix-shm-write-unlink
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow ipc-posix-shm-write-unlink
-	(require-all
-		(profile-flag "common-debugging-rules")
-		(require-any
-			(require-all
-				(profile-flag "restrictive-extension")
-				(%entitlement-is-bool-true "get-task-allow")
-				(require-any
-					(ipc-posix-name "/FSM-*")
-					(ipc-posix-name "OA-*")
-					(ipc-posix-name "stack-logs*")
-				)
-			)
-			(require-all
-				(require-any
-					(ipc-posix-name "gdt-[a-zA-Z0-9]")
-					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-c")
-					(ipc-posix-name #"gdt-([a-zA-Z0-9])+-s")
-				)
-				(profile-flag "restrictive-extension")
-				(%entitlement-is-bool-true "get-task-allow")
-			)
-			(require-any
-				(ipc-posix-name "/FSM-*")
-				(ipc-posix-name "OA-*")
-				(ipc-posix-name "stack-logs*")
-			)
-		)
-	)
-)
-(deny ipc-posix-shm-write-unlink)
-
-(allow isp-command-send)
-(autobox isp-command-send
+(allow ipc-sysv-shm)
+(autobox ipc-sysv-shm
 	(require-any
 		(profile-flag "autobox-client")
 		(profile-flag "autobox-client-no-exception-entitlements")
 	)
 )
 
-(deny job-creation)
+(deny isp-command-send)
 
-(allow lsopen)
+(allow job-creation)
+
+(allow lsopen
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(deny lsopen)
 
 (allow mach*
 	(with report)

 )
 (deny mach*)
 
-(allow mach-derive-port)
+(allow mach-cross-domain-lookup)
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(with report)
 	(require-all
 		(profile-flag "common-apple-signed-executable-rules")

 		(global-name "com.apple.mobile.usermanagerd.xpc")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.pluginkit.pkd")
 		(profile-flag "common-pluginkit-support")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.system.logger")
 		(profile-flag "common-system-logging-rules")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-rules")
 		(%entitlement-is-present "com.apple.private.applemediaservices")

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.contactsd.support")
 		(%entitlement-is-present "com.apple.private.contacts")
 		(profile-flag "common-rules")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.managedconfiguration.profiled.public")
 		(profile-flag "common-managed-configuration-read-rules")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-pluginkit-support")
 		(extension "com.apple.pluginkit.plugin-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-pluginkit-support")
 		(global-name "com.apple.extensionkitservice")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(profile-flag "autobox-client-telemetry")
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-containermanagerd-rules")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.mobilegestalt.xpc")
 		(profile-flag "common-mobilegestalt-rules")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.coreduetd.people")
 		(%entitlement-is-bool-true "com.apple.coreduetd.people")
 		(profile-flag "common-rules")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-preferences-rules")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-debugging-rules")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-mach-lookups")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(profile-flag "common-apple-signed-executable-rules")
 		(process-attribute is-apple-signed-executable)

 		)
 	)
 )
-(autobox mach-lookup
+(autobox mach-issue-extension
 	(with restrictive-default)
 	(require-any
 		(profile-flag "autobox-client")
 		(profile-flag "autobox-client-no-exception-entitlements")
 	)
 )
-(deny mach-lookup)
+(deny mach-issue-extension)
 
-(allow mach-register
+(allow mach-priv-task-port
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow mach-register
+(allow mach-priv-task-port
 	(require-all
 		(profile-flag "generic-sandbox-extension-support")
 		(local-name "*")
 		(extension "com.apple.security.exception.mach-register.local-name")
 	)
 )
-(deny mach-register)
+(deny mach-priv-task-port)
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
+
+(allow mach-task-exception-port-set
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(allow mach-task-exception-port-set
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
+		(profile-flag "common-exception-entitlement-rules")
+	)
+)
+(allow mach-task-exception-port-set
+	(target self)
+)
+(deny mach-task-exception-port-set)
 
 (allow mach-task-inspect
 	(with report)

 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow mach-task-name
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-		(profile-flag "common-exception-entitlement-rules")
-	)
-)
 (allow mach-task-name
 	(target self)
 )
 (deny mach-task-name)
 
-(allow mach-task-read
+(allow necp-client-open
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow mach-task-read
-	(target self)
-)
-(deny mach-task-read)
-
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
+(deny necp-client-open)
 
 (allow network*
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(deny network*)
-
-(allow network-inbound
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow network-inbound
+(allow network*
 	(require-all
 		(vnode-type SOCKET)
 		(extension "com.apple.security.exception.files.absolute-path.bind")
 		(profile-flag "common-exception-entitlement-rules")
 	)
 )
-(deny network-inbound)
+(deny network*)
 
 (allow network-bind
 	(with report)
 	(profile-flag "disable-enforcement")
 )
+(allow network-bind
+	(control-name "com.apple.flow-divert")
+)
+(allow network-bind
+	(require-all
+		(profile-flag "common-system-logging-rules")
+		(literal "/private/var/run/syslog")
+	)
+)
 (allow network-bind
 	(require-all
 		(vnode-type SOCKET)
-		(extension "com.apple.security.exception.files.absolute-path.bind")
+		(extension "com.apple.security.exception.files.absolute-path.connect")
 		(profile-flag "common-exception-entitlement-rules")
 	)
 )

 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow network-outbound
-	(control-name "com.apple.flow-divert")
-)
-(allow network-outbound
-	(require-all
-		(profile-flag "common-system-logging-rules")
-		(literal "/private/var/run/syslog")
-	)
-)
-(allow network-outbound
-	(require-all
-		(vnode-type SOCKET)
-		(extension "com.apple.security.exception.files.absolute-path.connect")
-		(profile-flag "common-exception-entitlement-rules")
-	)
-)
 (deny network-outbound)
 
 (allow nvram*

 )
 (deny nvram*)
 
-(allow nvram-get
+(allow nvram-delete
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "emu")
 		(profile-flag "common-rules")
 	)
 )
-(deny nvram-get)
+(deny nvram-delete)
 
 (allow opendirectory-user-modify
 	(with report)

 )
 (deny opendirectory-user-modify)
 
-(allow process*
+(allow process*)
+
+(allow process-codesigning
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(deny process*)
+(deny process-codesigning)
 
-(allow process-codesigning)
+(allow process-exec*
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(deny process-exec*)
+
+(allow process-fork
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(allow process-fork
+	(with report)
+	(require-all
+		(profile-flag "hide-launchd")
+		(target initproc)
+		(profile-flag "disable-enforcement")
+	)
+)
+(deny process-fork
+	(with no-report)
+	(require-all
+		(profile-flag "hide-launchd")
+		(target initproc)
+		(profile-flag "disable-enforcement")
+	)
+)
+(deny process-fork)
 
 (allow process-info*
 	(with report)

 		(profile-flag "disable-enforcement")
 	)
 )
+(allow process-info*
+	(require-all
+		(profile-flag "common-exception-entitlement-rules")
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
+	)
+)
+(allow process-info*
+	(require-all
+		(profile-flag "common-rules")
+		(target self)
+	)
+)
 (deny process-info*
 	(with no-report)
 	(require-all

 		(profile-flag "disable-enforcement")
 	)
 )
-(allow process-info-codesignature
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-	)
-)
 (allow process-info-codesignature
 	(require-all
 		(profile-flag "common-rules")

 )
 (allow process-info-ledger
 	(require-all
-		(profile-flag "common-rules")
-		(target self)
+		(profile-flag "common-exception-entitlement-rules")
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
 	)
 )
 (deny process-info-ledger

 )
 (deny process-info-ledger)
 
-(allow process-info-listpids
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow process-info-listpids
-	(with report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(allow process-info-listpids
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-	)
-)
-(deny process-info-listpids
-	(with no-report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(deny process-info-listpids)
-
-(allow process-info-pidinfo
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow process-info-pidinfo
-	(with report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(allow process-info-pidinfo
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-	)
-)
-(allow process-info-pidinfo
-	(require-all
-		(profile-flag "common-rules")
-		(target self)
-	)
-)
-(deny process-info-pidinfo
-	(with no-report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(deny process-info-pidinfo)
-
-(allow process-info-pidfdinfo
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow process-info-pidfdinfo
-	(with report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(allow process-info-pidfdinfo
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-	)
-)
-(allow process-info-pidfdinfo
-	(require-all
-		(profile-flag "common-rules")
-		(target self)
-	)
-)
-(deny process-info-pidfdinfo
-	(with no-report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(deny process-info-pidfdinfo)
-
-(allow process-info-pidfileportinfo
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow process-info-pidfileportinfo
-	(with report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(allow process-info-pidfileportinfo
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-	)
-)
-(allow process-info-pidfileportinfo
-	(require-all
-		(profile-flag "common-rules")
-		(target self)
-	)
-)
-(deny process-info-pidfileportinfo
-	(with no-report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
-(deny process-info-pidfileportinfo)
-
 (allow process-info-rusage
 	(with report)
 	(profile-flag "disable-enforcement")
 )
-(allow process-info-rusage
-	(with report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
-)
 (allow process-info-rusage
 	(require-all
 		(profile-flag "common-exception-entitlement-rules")

 	)
 )
 (allow process-info-rusage
-	(require-all
-		(profile-flag "common-rules")
-		(target self)
-	)
-)
-(deny process-info-rusage
-	(with no-report)
-	(require-all
-		(profile-flag "hide-launchd")
-		(target initproc)
-		(profile-flag "disable-enforcement")
-	)
+	(target-signing-identifier "com.apple.lsd")
 )
 (deny process-info-rusage)
 

 	(profile-flag "disable-enforcement")
 )
 (allow process-info-sandbox-container
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-	)
-)
-(allow process-info-sandbox-container
-	(target-signing-identifier "com.apple.lsd")
-)
-(deny process-info-sandbox-container)
-
-(allow process-info-setcontrol
-	(with report)
-	(profile-flag "disable-enforcement")
-)
-(allow process-info-setcontrol
 	(with report)
 	(require-all
 		(profile-flag "hide-launchd")

 		(profile-flag "disable-enforcement")
 	)
 )
-(allow process-info-setcontrol
+(allow process-info-sandbox-container
 	(require-all
 		(profile-flag "common-rules")
 		(target self)
 	)
 )
-(deny process-info-setcontrol
+(deny process-info-sandbox-container
 	(with no-report)
 	(require-all
 		(profile-flag "hide-launchd")

 		(profile-flag "disable-enforcement")
 	)
 )
-(deny process-info-setcontrol)
+(deny process-info-sandbox-container)
 
-(allow process-iopolicy*)
+(allow process-iopolicy-set
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(deny process-iopolicy-set)
+
+(allow process-legacy-codesigning*
+	(with report)
+	(profile-flag "disable-enforcement")
+)
+(deny process-legacy-codesigning*)
 
 (allow pseudo-tty
 	(with report)

 				(sysctl-name "kern.wq_limit_cooperative_threads")
 				(sysctl-name "machdep.virtual_address_size")
 				(sysctl-name "security.mac.amfi.developer_mode_status")
+				(sysctl-name "security.mac.lockdown_mode_state_public")
 				(sysctl-name "security.mac.sandbox.sentinel")
 				(sysctl-name "sysctl.proc_translated")
 				(sysctl-name "vm.loadavg")

 		(profile-flag "disable-enforcement")
 	)
 )
+(allow system-info
+	(require-all
+		(info-type "vfs.disk-space")
+		(process-attribute is-apple-signed-executable)
+		(profile-flag "common-rules")
+	)
+)
 (deny system-info
 	(with no-report)
 	(require-all

 (deny user-preference-write)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
