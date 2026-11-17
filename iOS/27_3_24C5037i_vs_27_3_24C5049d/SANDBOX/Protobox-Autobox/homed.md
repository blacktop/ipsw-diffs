## homed

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleNVMeEAN")
 		(iokit-registry-entry-class "AppleSMCKeysEndpoint")
 		(iokit-registry-entry-class "AppleSPUHIDDriver")
+		(iokit-registry-entry-class "AppleSPUHIDEventDriver")
 		(iokit-registry-entry-class "AppleUserHIDDevice")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
 		(iokit-registry-entry-class "H1xANELoadBalancer")

 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.chrono.widgetcenterconnection"))
 		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.cksharingmanagementd"))
 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.userprofiles"))

 		(require-not (global-name "com.apple.audio.hapticd"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.airplay.receiver.mediaremote.services"))
+		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.securityd"))

 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_recvmsg_x
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
