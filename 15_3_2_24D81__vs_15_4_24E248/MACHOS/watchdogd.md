## watchdogd

> `/usr/libexec/watchdogd`

```diff

-277.80.2.0.0
-  __TEXT.__text: 0xb164
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_stubs: 0xaa0
+299.100.5.0.0
+  __TEXT.__text: 0xbef8
+  __TEXT.__auth_stubs: 0xe80
+  __TEXT.__objc_stubs: 0xb40
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x4048
-  __TEXT.__oslogstring: 0x280
+  __TEXT.__cstring: 0x4953
+  __TEXT.__oslogstring: 0x2a1
   __TEXT.__objc_classname: 0x1
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_methname: 0x6d5
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x730
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7f8
+  __TEXT.__objc_methname: 0x72f
+  __TEXT.__unwind_info: 0x290
+  __DATA_CONST.__auth_got: 0x750
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x858
   __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x2a8
-  __DATA.__data: 0x5cb0
-  __DATA.__bss: 0xb30
+  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__data: 0x63d8
+  __DATA.__bss: 0xb38
   __DATA.__common: 0x90
   __INFO_FILTER.__disable: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/Versions/A/DiagnosticRequest
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics
   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis
+  - /usr/lib/libEndpointSecurity.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 319E58D0-52FA-34AB-ABD0-CB26AC542D7F
-  Functions: 183
-  Symbols:   288
-  CStrings:  637
+  UUID: 8858F516-95FE-3AEB-983C-226686D940C5
+  Functions: 214
+  Symbols:   292
+  CStrings:  671
 
Symbols:
+ _es_default_mute_path
+ _es_default_unmute_path
+ _es_delete_client
+ _es_new_client
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
