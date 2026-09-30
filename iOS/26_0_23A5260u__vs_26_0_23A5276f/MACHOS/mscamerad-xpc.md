## mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc`

```diff

-2013.0.0.0.0
-  __TEXT.__text: 0x204b4
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_stubs: 0x3cc0
-  __TEXT.__objc_methlist: 0x1bd4
-  __TEXT.__const: 0x44
-  __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__objc_methname: 0x4d22
-  __TEXT.__cstring: 0x2fae
-  __TEXT.__oslogstring: 0x3f
+2016.0.0.0.0
+  __TEXT.__text: 0x21c14
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_stubs: 0x3ce0
+  __TEXT.__objc_methlist: 0x1bec
+  __TEXT.__const: 0x4c
+  __TEXT.__gcc_except_tab: 0x7a8
+  __TEXT.__objc_methname: 0x4d9c
+  __TEXT.__cstring: 0x30c6
+  __TEXT.__oslogstring: 0x80
   __TEXT.__objc_classname: 0x23a
   __TEXT.__objc_methtype: 0x9b2
-  __TEXT.__ustring: 0x280
-  __TEXT.__unwind_info: 0x5c8
-  __DATA_CONST.__auth_got: 0x4d8
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x680
-  __DATA_CONST.__cfstring: 0x3ea0
+  __TEXT.__ustring: 0x28e
+  __TEXT.__unwind_info: 0x628
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__cfstring: 0x3fa0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_dictobj: 0x21c0
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0x26f0
-  __DATA.__objc_selrefs: 0x14d8
+  __DATA.__objc_selrefs: 0x14e8
   __DATA.__objc_ivar: 0x1f4
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x3d0

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A929AA0E-E707-3BE5-AC07-4ADB9ECCEBBB
-  Functions: 609
-  Symbols:   248
-  CStrings:  2107
+  UUID: 734112D8-B00E-3F91-AA3A-1572678BA320
+  Functions: 621
+  Symbols:   265
+  CStrings:  2129
 
Symbols:
+ _CFErrorCopyDescription
+ __os_feature_enabled_impl
+ __os_log_default
+ _kTCCServiceExternalCameraMedia
+ _tcc_attributed_entity_get_path
+ _tcc_authorization_record_get_authorization_value
+ _tcc_authorization_record_get_service
+ _tcc_authorization_record_get_subject_attributed_entity
+ _tcc_authorization_record_get_subject_identity
+ _tcc_identity_create
+ _tcc_identity_get_identifier
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_identity
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_server_message_set_authorization_value
+ _tcc_service_get_name
+ _tcc_service_singleton_for_CF_name
CStrings:
+ "(check) ---> New kTCCServiceExternalCameraMedia Service"
+ "???"
+ "Bundle:%s -- value: %llu"
+ "ImageCapture"
+ "No work performed in new TCC path"
+ "TCCServiceExternalCameraMedia_iOS"
+ "captureUserIntentForControlWithBundleIdentifier:withNotification:"
+ "control_informed"
+ "displayAlertForControlWithNotification:completionBlock:"
+ "entity"
+ "tcc_server_message_get_authorization_records_by_service error %@"
+ "v16@?0^{__CFError=}8"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "value"

```
