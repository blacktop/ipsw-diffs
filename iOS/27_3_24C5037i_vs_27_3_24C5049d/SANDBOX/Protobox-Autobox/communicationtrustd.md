## communicationtrustd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.StatusKit.publish"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.familycircle.agent"))
+		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
 		(require-not (global-name "com.apple.appprotectiond.read"))

 (deny process-exec*)
 
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
+)
 
 (deny syscall-unix
 	(require-all

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_request_notification
 		host_get_special_port
 		clock_get_time
 		mach_exception_raise

 (allow system-necp-client-action
 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
-		NECP_CLIENT_ACTION_REMOVE)
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW)
 )
 
 (allow process-exec-update-label)
```
