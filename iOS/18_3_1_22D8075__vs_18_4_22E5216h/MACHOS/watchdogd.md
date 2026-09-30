## watchdogd

> `/usr/libexec/watchdogd`

```diff

-277.80.2.0.0
-  __TEXT.__text: 0xa8fc
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_stubs: 0xa80
+299.100.4.0.0
+  __TEXT.__text: 0xb5f8
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_stubs: 0xb20
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x4255
-  __TEXT.__oslogstring: 0x280
+  __TEXT.__cstring: 0x4b60
+  __TEXT.__oslogstring: 0x2a1
   __TEXT.__objc_classname: 0x1
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_methname: 0x6bf
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x760
+  __TEXT.__objc_methname: 0x719
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x2a0
-  __DATA.__data: 0x95b0
-  __DATA.__bss: 0xae0
+  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__data: 0x9cd8
+  __DATA.__bss: 0xae8
   __DATA.__common: 0x90
   __INFO_FILTER.__disable: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
+  - /usr/lib/libEndpointSecurity.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 171
-  Symbols:   309
-  CStrings:  583
+  Functions: 194
+  Symbols:   312
+  CStrings:  617
 
Symbols:
+ _es_default_mute_path
+ _es_default_unmute_path
+ _es_delete_client
+ _es_new_client
+ _objc_retain_x23
- _objc_retain_x22
- _objc_retain_x28
CStrings:
+ "-o0"
+ "-o1"
+ "/usr/libexec/watchdogd"
+ "ESK seems not available"
+ "Faile to find previously stashed service info"
+ "Failed to allocate new optin service"
+ "Failed to create new ES client due to %u"
+ "Failed to mute service %s"
+ "Failed to query executable path of %s"
+ "Failed to unmute service %s"
+ "Faled to notify ESK about %s enrolled %d"
+ "Faled to notify ESK about %s unenrolled %d"
+ "Ignore incoming ES message %u"
+ "Not allowed to unregister static watchdog service %s"
+ "Notify ESK about %s enrolled"
+ "Notify ESK about %s unenrolled"
+ "Notify ESK about watchdogd enrolled"
+ "Notify ESK to mute service %s"
+ "Notify ESK to unmute service %s"
+ "Remaining stashed service %s"
+ "Try to remove service info from stash"
+ "Unregister: return WATCHDOG_SERVICE_REGISTRATION_ERROR_PARSE_FAILED"
+ "com.apple.watchdogtestoptin0"
+ "com.apple.watchdogtestoptin0.watchdog"
+ "com.apple.watchdogtestoptin1"
+ "com.apple.watchdogtestoptin1.watchdog"
+ "optin un-registration successful"
+ "program"
+ "removeObject:"
+ "seekToFileOffset:"
+ "service %s is going to be removed"
+ "systemDomain"
+ "truncateFileAtOffset:"
+ "useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:isSnapshotDead:"
+ "v24@?0^{es_client_s=}8r^{?=I{timespec=qq}QQ^{?}Qi(?={?=[32C]}{?=i(?=iI[32C])})i(?={?=i^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=B^{?}(?=[64C]{?=B})}{?=^{?}^{?}^{?}{?=Q*}Si[56C]}{?=i(?=^{?}{?=^{?}{?=Q*}S})[16C](?=[48C]{?=^{_acl}})}{?=[64C]}{?=^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{?}{?=Q*}(?=[64C]{?=^{?}^{?}iii})}{?=i[64C]}{?=^{?}^{?}^{?}{?=[8I]}[32C]}{?=^{?}{?=Q*}[64C]}{?=^{?}i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I{?=Q*}[64C]}{?={?=Q*}[64C]}{?={?=Q*}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=iiiQ^{?}[64C]}{?=^{statfs}i[60C]}{?=iQQ[64C]}{?=i^{?}[64C]}{?=^{?}ii[64C]}{?=^{?}i[64C]}{?=i[64C]}{?=i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}Qi[52C]}{?=^{?}i(?=^{?}{?=^{?}{?=Q*}})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}i(?=^{_acl})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I^{?}[64C]}{?=S^{?}[64C]}{?=II^{?}[64C]}{?=[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=II[64C]}{?=II[64C]}{?=i^{?}^{?}[56C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}S[64C]}{?=^{?}iii[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}[64C]}{?=^{?}{timespec=qq}{timespec=qq}[64C]}{?=^{?}[64C]}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?})^{?}Q[0Q]}16"
+ "wait for service %s to be un-enrolled"
+ "watchdogtestoptin0"
+ "watchdogtestoptin1"
- "com.apple.watchdogtestoptin"
- "com.apple.watchdogtestoptin.watchdog"
- "useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:"
- "watchdogtestoptin"

```
