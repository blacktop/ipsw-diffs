## CarPlay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.linkd.extension"))
 		(require-not (global-name "com.apple.assistant.client"))
-		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.hangtracerd"))

 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.backboard.system-app-server"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.contactsd.support"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.sharingd.nsxpc"))
 		(require-not (global-name "com.apple.siri.uaf.service"))

 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.siri.UnifiedSiriTest.TestingEventService"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.hangtracermonitor"))

 		(require-not (global-name "com.apple.donotdisturb.service.non-launching"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.CarPlayApp.cluster-theme-service"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.gputools.service"))

 		(require-not (global-name "com.apple.assistant.analytics"))
 		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.familycircle.agent"))
+		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.CARenderServer"))
+				(require-not (global-name "com.apple.AttentionAwareness"))
 				(require-not (global-name "com.apple.ABDatabaseDoctor"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.CARenderServer"))
+				(require-not (global-name "com.apple.AttentionAwareness"))
 				(require-not (global-name "com.apple.ABDatabaseDoctor"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))

 		SYS_writev_nocancel
 		SYS_sendto_nocancel
 		SYS_pread_nocancel
+		SYS_pwrite_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
 		SYS_fileport_makeport

 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np
+		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
+		SYS_guarded_writev_np
 		SYS_persona
 		SYS_work_interval_ctl
 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
+		SYS___channel_get_info
+		SYS___channel_sync
+		SYS___channel_get_opt
+		SYS___channel_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_fclonefileat

 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
 		SYS_shared_region_map_and_slide_2_np
+		SYS_pwritev
+		SYS_pwritev_nocancel
 		SYS_ulock_wait2
 		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall

 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
-		NECP_CLIENT_ACTION_REMOVE_FLOW)
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
 (allow process-exec-update-label)
```
