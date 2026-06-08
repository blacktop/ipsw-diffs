## lskdP7d

> `/usr/libexec/lskdP7d`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0xd98888
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x380
+  __TEXT.__text: 0xe4c858
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0xb0
-  __TEXT.__cstring: 0xea
-  __TEXT.__const: 0x338400
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__objc_methname: 0x345
-  __TEXT.__objc_classname: 0x1b
+  __TEXT.__cstring: 0x118
+  __TEXT.__const: 0x363800
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__objc_methname: 0x410
+  __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x97
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__eh_frame: 0x238
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4a470
-  __DATA_CONST.__cfstring: 0xc0
+  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__eh_frame: 0x240
+  __DATA_CONST.__const: 0x4b4e8
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0x100
+  __DATA.__objc_selrefs: 0x128
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x21b0
+  __DATA.__data: 0x2688
   __DATA.__bss: 0x40
-  __DATA.__common: 0x44194
+  __DATA.__common: 0x9219c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F445D62C-9D0F-3AD4-B5A4-3C2270F04CCC
-  Functions: 420
-  Symbols:   165
-  CStrings:  71
+  UUID: 845495CC-5194-3B50-80D2-5022B2FC93A9
+  Functions: 412
+  Symbols:   199
+  CStrings:  79
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_NSString
+ _SecTaskCopySigningIdentifier
+ ___snprintf_chk
+ __xpc_error_connection_invalid
+ __xpc_error_peer_code_signing_requirement
+ __xpc_error_termination_imminent
+ __xpc_type_dictionary
+ __xpc_type_error
+ __xpc_type_int64
+ _getpid
+ _getprogname
+ _kSymptomDiagnosticReplySuccess
+ _objc_release_x19
+ _proc_pidpath
+ _snprintf
+ _strnlen
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create_mach_service
+ _xpc_connection_send_message
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_connection_set_event_handler
+ _xpc_connection_set_qos_class_floor
+ _xpc_connection_set_target_queue
+ _xpc_copy_description
+ _xpc_dictionary_create
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_audit_token
+ _xpc_dictionary_get_data
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_int64
+ _xpc_get_type
+ _xpc_int64_get_value
+ _xpc_release
- _bootstrap_look_up
CStrings:
+ "SDRDiagnosticReporter"
+ "boolValue"
+ "objectForKeyedSubscript:"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "stringWithUTF8String:"
+ "v16@?0@\"NSDictionary\"8"

```
