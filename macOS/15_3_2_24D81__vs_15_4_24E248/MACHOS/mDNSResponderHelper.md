## mDNSResponderHelper

> `/usr/sbin/mDNSResponderHelper`

```diff

-2559.80.8.0.0
-  __TEXT.__text: 0x4de8
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x179
-  __TEXT.__cstring: 0x68d
-  __TEXT.__oslogstring: 0x159a
-  __TEXT.__objc_methname: 0x41
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x3b0
+2600.100.147.0.0
+  __TEXT.__text: 0x52a8
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__const: 0x1ba
+  __TEXT.__cstring: 0x6ad
+  __TEXT.__oslogstring: 0x16f2
+  __TEXT.__objc_methname: 0x87
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x160
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x10
-  __DATA.__objc_classrefs: 0x8
+  __DATA.__objc_selrefs: 0x28
+  __DATA.__objc_classrefs: 0x18
   __DATA.__data: 0x40
-  __DATA.__bss: 0x19c
+  __DATA.__bss: 0x1ac
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CF252ED-9EFB-3C9B-A8BC-52F4D1A56914
-  Functions: 25
-  Symbols:   222
-  CStrings:  187
+  UUID: 90D8583E-F4C0-3FD5-B3BB-A1D501FF835C
+  Functions: 26
+  Symbols:   246
+  CStrings:  199
 
Symbols:
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSArray
+ __CFXPCCreateXPCObjectFromCFObject
+ ___mhs_log_block_invoke
+ __block_descriptor_tmp.81
+ __block_literal_global.79
+ __os_log_fault_impl
+ _audit_token_to_pid
+ _g_message_key_app_audit_token
+ _g_message_key_app_service_types
+ _mh_command_copy_app_service_types
+ _mhs_copy_app_service_types
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$bundleRecordForAuditToken:error:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_opt_class
+ _objc_release
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _xpc_dictionary_set_value
+ mhs_log.s_log
+ mhs_log.s_once
Functions:
~ _SetLocalAddressCacheEntry : 2712 -> 2664
~ _KeychainGetSecrets : 2696 -> 2736
~ _SendWakeupPacket : 1184 -> 1176
~ _SendKeepalive : 2220 -> 2204
~ ___accept_client_block_invoke : 2588 -> 2772
- sub_100009308
+ ___mhs_log_block_invoke
+ _mhs_copy_app_service_types
CStrings:
+ "Created bundle record -- pid %d, record: %{public}@"
+ "Failed to convert service types NSArray to XPC array: %{public}@"
+ "Failed to create bundle record -- pid: %d, error: %{public}@"
+ "Info dictionary has service types -- pid: %d, service types: %{public}@"
+ "NSBonjourServices"
+ "No info dictionary in bundle record -- pid: %d"
+ "No service types in info dictionary -- pid: %d"
+ "bundleRecordForAuditToken:error:"
+ "helper_server"
+ "infoDictionary"
+ "objectForKey:ofClass:"

```
