## CMCaptureDiagnosticExtension

> `/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension`

```diff

-587.140.9.0.0
-  __TEXT.__text: 0x560
-  __TEXT.__auth_stubs: 0x80
-  __TEXT.__objc_stubs: 0x160
+587.140.11.0.1
+  __TEXT.__text: 0x288
+  __TEXT.__auth_stubs: 0x40
+  __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x119
-  __TEXT.__oslogstring: 0xf0
+  __TEXT.__cstring: 0xdf
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methname: 0xfe
+  __TEXT.__objc_methname: 0xf8
   __TEXT.__objc_methtype: 0x13
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x48
+  __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x68
+  __DATA.__objc_selrefs: 0x60
   __DATA.__objc_data: 0x50
-  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFCD2663-B724-3570-B1A6-D8C547F6B0BB
+  UUID: 6C1E5F5D-A211-3602-B1ED-9DC0110D63DC
   Functions: 2
-  Symbols:   24
-  CStrings:  32
+  Symbols:   20
+  CStrings:  27
 
Symbols:
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
Functions:
~ sub_100000b6c -> sub_100000a7c : 1364 -> 636
CStrings:
- "-[CMCaptureDiagnosticExtension attachmentsForParameters:]"
- "<<<< CMCaptureDiagnosticExtension >>>> %s:    found item: %@"
- "<<<< CMCaptureDiagnosticExtension >>>> %s: attachmentsForParameters: checking path %@"
- "<<<< CMCaptureDiagnosticExtension >>>> %s: searching path: %@, contents.size = %lu, error=%@"
- "count"

```
