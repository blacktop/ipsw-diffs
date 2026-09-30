## proximitycontrold

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleJPEGDriver")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.storekitd"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.perceptiond.entitykit"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))

 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.userprofiles"))
+		(require-not (global-name "com.apple.TextInput.preferences"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
 		(require-not (require-any
 			(global-name "com.apple.findmy.findmylocate.friendshipservice")

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
```
