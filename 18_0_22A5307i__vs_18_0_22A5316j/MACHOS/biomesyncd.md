## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-153.0.7.0.0
-  __TEXT.__text: 0x4334c
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_stubs: 0x7680
-  __TEXT.__objc_methlist: 0x34cc
+153.2.0.1.0
+  __TEXT.__text: 0x439c8
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_stubs: 0x76c0
+  __TEXT.__objc_methlist: 0x34ec
   __TEXT.__const: 0x10c8
-  __TEXT.__gcc_except_tab: 0x908
-  __TEXT.__objc_methname: 0x938f
-  __TEXT.__cstring: 0x487d
+  __TEXT.__gcc_except_tab: 0x918
+  __TEXT.__objc_methname: 0x93a7
+  __TEXT.__cstring: 0x49cd
   __TEXT.__objc_classname: 0x820
-  __TEXT.__objc_methtype: 0x189f
-  __TEXT.__oslogstring: 0x5077
+  __TEXT.__objc_methtype: 0x1882
+  __TEXT.__oslogstring: 0x50f1
   __TEXT.__info_plist: 0x3e1
-  __TEXT.__unwind_info: 0xeb8
-  __DATA_CONST.__auth_got: 0x690
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xf08
-  __DATA_CONST.__cfstring: 0x3e80
+  __TEXT.__unwind_info: 0xed0
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0xfc0
+  __DATA_CONST.__cfstring: 0x4080
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7c60
-  __DATA.__objc_selrefs: 0x2440
-  __DATA.__objc_ivar: 0x3cc
+  __DATA.__objc_const: 0x7c40
+  __DATA.__objc_selrefs: 0x2450
+  __DATA.__objc_ivar: 0x3c8
   __DATA.__objc_data: 0x1130
   __DATA.__data: 0x840
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1474
+  Functions: 1479
   Symbols:   337
-  CStrings:  2857
+  CStrings:  2874
 
Symbols:
+ _dispatch_get_global_queue
- _OBJC_CLASS_$__PASSimpleCoalescingTimer
CStrings:
+ "\x01\x16"
+ "\x01\"\x12\x14"
+ "Asked to defer"
+ "BMRapportClient[%!@(MISSING)]: Must be inactive before creating and activating companion link client"
+ "BMRapportClient[%!@(MISSING)]: Requests must be added before activation"
+ "BMRapportClient[%!@(MISSING)]: Requests must be registered during activation"
+ "BMRapportClient[%!@(MISSING)]: Warning: ignoring response arriving after deallocation: %!@(MISSING)"
+ "BMRapportClient[%!@(MISSING)]: Warning: ignoring response arriving after invalidation: %!@(MISSING)"
+ "BMRapportClient[%!@(MISSING)]: Warning: ignoring response because no response handler is set: %!@(MISSING)"
+ "BMRapportClient[%!@(MISSING)]: register request"
+ "BMRapportDevice[%!@(MISSING)]: id=%!@(MISSING) bmID=%!@(MISSING) model=%!@(MISSING) name=%!@(MISSING) version=%!l(MISSING)d.%!l(MISSING)d.%!l(MISSING)d"
+ "BMRapportManager[%!@(MISSING)]: skipping RPCompanionLinkDevice failed validation: %!@(MISSING)"
+ "BMRapportManager[%!@(MISSING)]: skipping RPCompanionLinkDevice missing identifier: %!@(MISSING)"
+ "BMRapportManager[%!@(MISSING)]: skipping RPCompanionLinkDevice missing model: %!@(MISSING)"
+ "BMRapportSyncEngine%!@(MISSING): rejecting request from personal device to sync cross account %!@(MISSING)"
+ "Cancelled"
+ "Device"
+ "Device lost"
+ "Discovery timeout"
+ "Invalid parameter"
+ "Invalid state"
+ "Invalidated"
+ "Max request depth hit"
+ "Multiple errors"
+ "Not supported"
+ "Protocol version mismatch"
+ "Request timeout no devices nearby"
+ "Temporarily unavailable"
+ "Unknown error"
+ "Unknown error (code %!l(MISSING)d)"
+ "_startServerWithCompletion:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "operatingSystemVersion"
+ "resetEagerExitTimer"
+ "v32@?0@\"NSString\"8@\"NSError\"16^B24"
- "\x01\x17"
- "\x01\"\x11\x15"
- "@\"_PASSimpleCoalescingTimer\""
- "BMRapportClient: RequestID '%!@(MISSING)' already registered"
- "BMRapportClient: Requests must be added before activation"
- "BMRapportClient: register request"
- "BMRapportDevice[%!@(MISSING)]: id=%!@(MISSING) bmID=%!@(MISSING) model=%!@(MISSING) name=%!@(MISSING)"
- "BMRapportManager: skipping RPCompanionLinkDevice failed validation: %!@(MISSING)"
- "BMRapportManager: skipping RPCompanionLinkDevice missing identifier: %!@(MISSING)"
- "BMRapportManager: skipping RPCompanionLinkDevice missing model: %!@(MISSING)"
- "BMRappowrtSyncEngine%!@(MISSING): rejecting request from personal device to sync cross account %!@(MISSING)"
- "Eager-exit coalescing timer fired, will attempt to exit when clean"
- "Warning: ignoring response arriving after deallocation: %!@(MISSING)"
- "Warning: ignoring response arriving after invalidation: %!@(MISSING)"
- "Warning: ignoring response because no response handler is set: %!@(MISSING)"
- "_eagerExitTimer"
- "initWithQueue:operation:"
- "runAfterDelaySeconds:coalescingBehavior:"

```
