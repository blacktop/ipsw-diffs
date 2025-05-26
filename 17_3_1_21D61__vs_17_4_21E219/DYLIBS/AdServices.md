## AdServices

> `/System/Library/Frameworks/AdServices.framework/AdServices`

```diff

-500.4.0.0.0
-  __TEXT.__text: 0x14fc
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x1c0
+510.12.0.0.0
+  __TEXT.__text: 0x1b50
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0x1c8
   __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0x11d
+  __TEXT.__oslogstring: 0x2bb
   __TEXT.__cstring: 0x190
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0xd4
+  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x71
-  __TEXT.__objc_methname: 0x7ed
-  __TEXT.__objc_methtype: 0x2a8
-  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methname: 0x859
+  __TEXT.__objc_methtype: 0x2b0
+  __TEXT.__objc_stubs: 0x6a0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6a0
-  __DATA_CONST.__objc_selrefs: 0x208
+  __DATA_CONST.__objc_const: 0x6d0
+  __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__objc_const: 0x168
-  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__auth_got: 0x1a8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x50
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x30
+  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/APFoundation.framework/APFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 47
-  Symbols:   76
-  CStrings:  192
+  Functions: 45
+  Symbols:   81
+  CStrings:  210
 
Symbols:
+ _APLogForCategory
+ _APPerfLogForCategory
+ __os_signpost_emit_with_name_impl
+ _objc_release_x26
+ _objc_retain_x20
+ _objc_retain_x25
+ _os_signpost_enabled
+ _os_signpost_id_generate
- __os_log_error_impl
- _objc_retain_x23
- _objc_retain_x27
CStrings:
+ "Attribution Request"
+ "Connection Interrupted"
+ "Connection Interrupted id=%{public, name=id}lld"
+ "Q"
+ "Returning error to caller: %{public}@"
+ "Returning token to caller: %{public}@"
+ "T@\"NSString\",?,R,C"
+ "TQ,R,N,V_intervalId"
+ "Token Request XPC"
+ "Token Status"
+ "Token Status id=%{public, name=id}lld status=%{public, name=status}ld"
+ "_intervalId"
+ "attributionTokenRequestTimestamp:interval:completionHandler:"
+ "id=%{public, name=id}lld"
+ "id=%{public, name=id}lld retryCount=%{public, name=retryCount}ld"
+ "id=%{public, name=id}lld thread=%{public, name=thread}@"
+ "intervalId"
+ "localizedDescription"
+ "numberWithBool:"
+ "v40@0:8@\"NSDate\"16Q24@?<v@?@\"AAAttributionResult\">32"
+ "v40@0:8@16Q24@?32"
- "attributionTokenRequestTimestamp:completionHandler:"
- "v32@0:8@\"NSDate\"16@?<v@?@\"AAAttributionResult\">24"
- "v32@0:8@16@?24"

```
