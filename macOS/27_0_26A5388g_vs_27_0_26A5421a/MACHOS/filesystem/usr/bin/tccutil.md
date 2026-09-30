## tccutil

> `/usr/bin/tccutil`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`

```diff

-910.0.0.0.0
-  __TEXT.__text: 0x69c
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__cstring: 0x1bc
-  __TEXT.__objc_methname: 0xc0
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__const: 0x40
+913.3.3.0.0
+  __TEXT.__text: 0xe10
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x180
+  __TEXT.__cstring: 0x471
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__objc_methname: 0xfc
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x30
-  __DATA.__objc_selrefs: 0x48
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x48
+  __DATA.__objc_selrefs: 0x60
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemExtensions.framework/Versions/A/SystemExtensions
+  - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13
-  Symbols:   39
-  CStrings:  31
+  Functions: 28
+  Symbols:   65
+  CStrings:  43
 
Symbols:
+ _CP_DeviceIsEnrolledViaDEP
+ _CP_IsEnrolledWithMDMv1
+ __Block_object_assign
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ _getopt
+ _optarg
+ _optind
+ _strncmp
+ _tcc_authorization_record_get_authorization_right
+ _tcc_authorization_record_get_non_tcc_service_name
+ _tcc_authorization_record_get_service
+ _tcc_authorization_record_get_subject_identity
+ _tcc_identity_create
+ _tcc_identity_get_identifier
+ _tcc_message_options_create
+ _tcc_message_options_set_include_policy
+ _tcc_message_options_set_reply_handler_policy
+ _tcc_server_message_get_authorization_records_by_identity
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_server_singleton_default
+ _tcc_service_get_CF_name
+ _tcc_service_get_name
+ _tcc_service_singleton_for_CF_name
CStrings:
+ "Error: %s"
+ "Usage:\ntccutil reset SERVICE [BUNDLE_ID]\ntccutil list (-s SERVICE | -b BUNDLE_ID | -s SERVICE -b BUNDLE_ID)\n\nCommands:\n  reset SERVICE [BUNDLE_ID]          Reset TCC state for SERVICE (optionally for BUNDLE_ID)\n  list -s SERVICE                    Show all bundle IDs with a record for SERVICE\n  list -b BUNDLE_ID                  Show all services with a record for BUNDLE_ID\n  list -s SERVICE -b BUNDLE_ID       Show granted or denied for BUNDLE_ID and SERVICE\n  (SERVICE may omit the 'kTCCService' prefix)"
+ "Usage: tccutil list (-s SERVICE | -b BUNDLE_ID | -s SERVICE -b BUNDLE_ID)"
+ "denied"
+ "granted"
+ "isEqualToString:"
+ "kTCCService"
+ "list"
+ "localizedDescription"
+ "s:b:"
+ "stringWithUTF8String:"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
```
