## logd

> `/usr/libexec/logd`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x227a0
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x5e0
+1643.100.44.0.0
+  __TEXT.__text: 0x24b44
+  __TEXT.__auth_stubs: 0x1790
+  __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x334
-  __TEXT.__cstring: 0x346f
-  __TEXT.__objc_methname: 0x3e2
+  __TEXT.__const: 0x258
+  __TEXT.__cstring: 0x3e5b
+  __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x658
-  __DATA_CONST.__auth_got: 0xae0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1dc8
-  __DATA_CONST.__cfstring: 0x480
+  __TEXT.__unwind_info: 0x698
+  __DATA_CONST.__auth_got: 0xbd0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x21e0
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1c64
-  __DATA.__crash_info: 0x40
   __DATA.__os_assumes_log: 0x8
-  __DATA.__bss: 0xce49
+  __DATA.__crash_info: 0x40
+  __DATA.__bss: 0xce69
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9628E7F0-412E-31BA-A558-78396F9C404F
-  Functions: 482
-  Symbols:   396
-  CStrings:  551
+  - /usr/lib/libz.1.dylib
+  - @rpath/AppleInternal/Library/Frameworks/Tightbeam.framework/Versions/A/Tightbeam
+  UUID: E2463456-E23F-34B3-B893-EDF53D8D0A9E
+  Functions: 510
+  Symbols:   433
+  CStrings:  617
 
Symbols:
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
+ _OBJC_CLASS_$_TapToRadarService
+ __dispatch_main_q
+ __dispatch_source_type_exclaves_notification
+ __xpc_bool_true
+ _crc32
+ _dispatch_source_get_data
+ _dyld_for_each_installed_shared_cache
+ _dyld_shared_cache_copy_uuid
+ _dyld_shared_cache_for_each_file
+ _exclaves_lookup_service
+ _exclaves_notification_create
+ _objc_opt_class
+ _tb_client_connection_activate
+ _tb_client_connection_create
+ _tb_client_connection_create_with_endpoint
+ _tb_client_connection_message_construct
+ _tb_client_connection_message_destruct
+ _tb_connection_send_query
+ _tb_endpoint_create_with_data
+ _tb_endpoint_set_interface_identifier
+ _tb_message_complete
+ _tb_message_configure_received
+ _tb_message_construct
+ _tb_message_decode_u64
+ _tb_message_decode_u8
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
+ _tb_message_subrange
+ _tb_transport_message_buffer_wrap_buffer
+ _xpc_copy_entitlement_for_token
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/logd.build/DerivedSources/OSLogDarwin_C.c"
+ "A secure indicator violation has been detected by the system. Please describe what you were doing at the time. List any behaviors that may have used the camera or the microphone; taking a photo, invoking Siri, taking a phone call..."
+ "B32@?0Q8^{oslogdarwin_prefsvalue_s={oslogbase_logsubsystem_s=II}Q}16Q24"
+ "Completed flush before panic and blocked future writes"
+ "Copied ExclaveKit shared cache: %s"
+ "ExclaveKit"
+ "Exclaves"
+ "Exclaves log server not available"
+ "Failed to initialize config admin client"
+ "Fallback Indicator triggered"
+ "Fallback Indicator was triggered due to an unexpected policy violation. Please describe what you were doing at the time. List any behaviors that may have used the camera or the microphone; taking a photo, invoking Siri, taking a phone call, turning on/off display, phone in pocket, etc ..."
+ "Full sync was requested for %s"
+ "I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8"
+ "Initializing notifications from exclaves..."
+ "Logd was unable to fsync book: %s with error: %s (%d)"
+ "SILManager"
+ "Secure Indicator Violation Detected"
+ "Security Policy"
+ "Sending of completion of sync have failed."
+ "Snapshotting before panic admin handler is done"
+ "Starting a flush before panic!"
+ "Subscribed for notifications from exclaves"
+ "TB_ASSERT: (err == TB_ERROR_SUCCESS) && \"failed to wrap packed buffer\""
+ "TB_ASSERT: (oslogdarwin_prefsbatch__raw_encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.PrefsBatch\""
+ "TB_ASSERT: (vErr == TB_ERROR_SUCCESS) && \"tb_message_subrange failed\""
+ "TB_FATAL: invalid tag in array metadata: 0x%x"
+ "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid value: unexpected case value, %llx"
+ "TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n"
+ "Unable to Create TTR draft: %s (%ld)"
+ "Unknown notification type: %lu"
+ "a fallback indicator was triggered"
+ "a secure indicator violation has been detected"
+ "all"
+ "com.apple.notification.logserver"
+ "com.apple.private.logging.allow-devhash"
+ "com.apple.service.LogServer_xnuproxy"
+ "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
+ "failed to set preferences in exclaves: full cache"
+ "failed to set preferences in exclaves: invalid subsystem id"
+ "initWithName:version:identifier:"
+ "localizedDescription"
+ "received an exclave notification %lu"
+ "setAttachments:"
+ "setClassification:"
+ "setComponent:"
+ "setDeleteOnAttach:"
+ "setDeviceIDs:"
+ "setDiagnosticExtensionIDs:"
+ "setProblemDescription:"
+ "setTitle:"
+ "shared"
+ "v16@?0@\"NSError\"8"
+ "v16@?0^{dyld_shared_cache_s=}8"
+ "v16@?0r*8"
+ "v24@?0Q8r^{oslogdarwin_prefsvalue_s={oslogbase_logsubsystem_s=II}Q}16"
+ "v24@?0{oslogdarwin_configadmin_setpreferences__result_s=C(?={oslogdarwin_configerror_s=Q})}8"
- "BUG IN LIBTRACE: Invalid type"

```
