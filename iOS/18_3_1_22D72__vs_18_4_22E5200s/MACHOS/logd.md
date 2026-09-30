## logd

> `/usr/libexec/logd`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x22fc0
-  __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_stubs: 0x5e0
+1643.100.40.0.0
+  __TEXT.__text: 0x24034
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x3c4
-  __TEXT.__cstring: 0x36f3
-  __TEXT.__objc_methname: 0x3e2
+  __TEXT.__const: 0x2b8
+  __TEXT.__cstring: 0x3bef
+  __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x620
-  __DATA_CONST.__auth_got: 0xc30
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1d40
-  __DATA_CONST.__cfstring: 0x480
+  __TEXT.__unwind_info: 0x628
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__auth_got: 0xc80
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x1f08
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
   __DATA.__data: 0x1ccd
-  __DATA.__crash_info: 0x40
   __DATA.__os_assumes_log: 0x8
-  __DATA.__bss: 0xca60
+  __DATA.__crash_info: 0x40
+  __DATA.__bss: 0xca80
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 471
-  Symbols:   439
-  CStrings:  509
+  Functions: 483
+  Symbols:   454
+  CStrings:  547
 
Symbols:
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
+ _OBJC_CLASS_$_TapToRadarService
+ __dispatch_main_q
+ __dispatch_source_type_exclaves_notification
+ _dispatch_source_get_data
+ _dyld_for_each_installed_shared_cache
+ _dyld_shared_cache_copy_uuid
+ _dyld_shared_cache_for_each_file
+ _exclaves_notification_create
+ _objc_opt_class
+ _objc_retain_x26
+ _os_variant_is_recovery
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
- _objc_retain_x27
- _tb_message_decode_u32
- _tb_message_encode_bool
- _tb_message_encode_u32
- _tb_message_encode_u64
CStrings:
+ "A secure indicator violation has been detected by the system. Please describe what you were doing at the time. List any behaviors that may have used the camera or the microphone; taking a photo, invoking Siri, taking a phone call..."
+ "Completed flush before panic and blocked future writes"
+ "Copied ExclaveKit shared cache: %s"
+ "ExclaveKit"
+ "Exclaves"
+ "Fallback Indicator triggered"
+ "Fallback Indicator was triggered due to an unexpected policy violation. Please describe what you were doing at the time. List any behaviors that may have used the camera or the microphone; taking a photo, invoking Siri, taking a phone call, turning on/off display, phone in pocket, etc ..."
+ "Full sync was requested for %s"
+ "Initializing notifications from exclaves..."
+ "Logd was unable to fsync book: %s with error: %s (%d)"
+ "SILManager"
+ "Secure Indicator Violation Detected"
+ "Security Policy"
+ "Sending of completion of sync have failed."
+ "Snapshotting before panic admin handler is done"
+ "Starting a flush before panic!"
+ "Subscribed for notifications from exclaves"
+ "TB_ASSERT: (oslogdarwin_prefsbatch__raw_encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.PrefsBatch\""
+ "Unable to Create TTR draft: %s (%ld)"
+ "Unknown notification type: %lu"
+ "a fallback indicator was triggered"
+ "a secure indicator violation has been detected"
+ "all"
+ "com.apple.notification.logserver"
+ "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
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
- "BUG IN LIBTRACE: Invalid type"
- "TB_ASSERT: (oslogdarwin_prefsbatch__encode(&msg, prefs) == TB_ERROR_SUCCESS) && \"failed to encode type: OSLogDarwin.PrefsBatch\""

```
