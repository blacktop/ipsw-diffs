## callintelligenced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_request_notification
 		host_get_special_port
 		clock_get_time
 		mach_exception_raise
```
