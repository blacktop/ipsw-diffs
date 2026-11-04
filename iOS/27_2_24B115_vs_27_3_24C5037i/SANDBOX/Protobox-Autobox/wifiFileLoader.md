## wifiFileLoader

> Group: ⬆️ Updated

```diff

 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "ACIWiFiDriver")
+)
 
 (deny iokit-set-properties)
 

 (allow syscall-unix
 	(syscall-number
 		SYS_exit
+		SYS_read
 		SYS_open
 		SYS_getfsstat
 		SYS_getpid

 		SYS_proc_info
 		SYS_stat64
 		SYS_fstat64
+		SYS_getdirentries64
 		SYS_getfsstat64
 		SYS_bsdthread_register
 		SYS_workq_open

 		SYS_kevent_qos
 		SYS_kevent_id
 		SYS___mac_syscall
+		SYS_read_nocancel
 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_fcntl_nocancel

 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
+		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
 		MSC_mk_timer_arm

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_iterator_next
+		io_service_close
 		io_service_open_extended
+		io_connect_method
 		io_server_version
+		io_service_get_matching_service_bin
 		io_service_add_notification_bin_64
+		io_registry_entry_get_property_bin_buf
 		mach_port_get_context_from_user
 		task_info_from_user
 		task_get_special_port_from_user
```
