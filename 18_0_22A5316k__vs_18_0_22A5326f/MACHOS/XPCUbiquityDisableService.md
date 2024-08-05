## XPCUbiquityDisableService

> `/private/var/staged_system_apps/Books.app/XPCServices/XPCUbiquityDisableService.xpc/XPCUbiquityDisableService`

```diff

-6183.0.0.0.0
-  __TEXT.__text: 0x804
-  __TEXT.__auth_stubs: 0x210
+6194.0.0.0.0
+  __TEXT.__text: 0x7dc
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x80
+  __TEXT.__objc_methlist: 0x5c
   __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methname: 0x2f2
-  __TEXT.__objc_methtype: 0x1c0
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x64
-  __TEXT.__oslogstring: 0x5d
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__objc_methname: 0x286
+  __TEXT.__objc_methtype: 0x160
+  __TEXT.__const: 0x18
+  __TEXT.__cstring: 0x6a
+  __TEXT.__oslogstring: 0x1a2
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x568
-  __DATA.__objc_selrefs: 0x80
+  __DATA.__objc_const: 0x508
+  __DATA.__objc_selrefs: 0x68
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16
-  Symbols:   55
-  CStrings:  80
+  Functions: 13
+  Symbols:   46
+  CStrings:  77
 
Symbols:
+ _BKDisableiCloudServiceLog
+ _dispatch_once
+ _objc_release_x1
+ _objc_release_x22
+ _objc_retainAutoreleaseReturnValue
- __NSConcreteStackBlock
- __Unwind_Resume
- ___objc_personality_v0
- __os_log_default
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x20
- _objc_retain_x23
- _objc_retain_x8
CStrings:
+ "Failed to set iCloud enabled to %!@(MISSING) for %!{(MISSING)public}@."
+ "Setting iCloud enabled to %!@(MISSING) for %!{(MISSING)public}@."
+ "_isServiceDisabled(%!{(MISSING)public}@): TCC returned a NULL array!"
+ "isLiverpoolAndUbiquityEnabled - Setting unknown liverpool value to %!{(MISSING)BOOL}d"
+ "isLiverpoolAndUbiquityEnabled - Skip setting unknown liverpool value because ubiquity is also unknown!"
+ "isLiverpoolAndUbiquityEnabled - liverpool OFF, ubiquity ON --> forcing liverpool ON"
+ "v8@?0"
- "Failed to set iCloud enabled to %!@(MISSING)."
- "Setting iCloud enabled to %!@(MISSING)."
- "TCC returned a NULL array!"
- "setLiverpoolEnabled:withReply:"
- "setUbiquityEnabled:liverpoolEnabled:withReply:"
- "setUbiquityEnabled:withReply:"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8B16B20@?24"
- "v32@0:8B16B20@?<v@?@\"NSError\">24"

```
