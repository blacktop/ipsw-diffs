## ApplePushService

> `/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService`

```diff

-1138.100.1.0.0
-  __TEXT.__text: 0x1e380
+1138.200.21.0.0
+  __TEXT.__text: 0x20370
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x168c
+  __TEXT.__objc_methlist: 0x16a4
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x1def
-  __TEXT.__oslogstring: 0x266c
-  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__oslogstring: 0x268f
+  __TEXT.__gcc_except_tab: 0x198
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__unwind_info: 0x810
   __TEXT.__objc_classname: 0x19d
-  __TEXT.__objc_methname: 0x3271
+  __TEXT.__objc_methname: 0x3293
   __TEXT.__objc_methtype: 0x50b
-  __TEXT.__objc_stubs: 0x21c0
+  __TEXT.__objc_stubs: 0x2200
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0xe88
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea0
+  __DATA_CONST.__objc_selrefs: 0xeb0
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x748
   __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x28e0
+  __AUTH_CONST.__objc_const: 0x28f0
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x200
-  __DATA.__bss: 0x301
+  __DATA.__bss: 0x309
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4AB2661-79F8-38CE-8E07-49B91DEC0F19
-  Functions: 815
-  Symbols:   2716
-  CStrings:  1549
+  UUID: 89DF55BF-4261-360A-A4CB-CB73CBD62780
+  Functions: 818
+  Symbols:   2724
+  CStrings:  1552
 
Symbols:
+ +[APSLog reduceLogging]
+ +[APSLog shouldReduceLogging]
+ ___108-[APSConnection _initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:]_block_invoke.45
+ ___65-[APSConnection _asyncOnDelegateQueueWithBlock:requiresDelegate:]_block_invoke.59
+ ___block_literal_global.167
+ ___block_literal_global.175
+ __shouldReduceLogging
+ _aps_log_reduce_logging
+ _objc_msgSend$reduceLogging
+ _objc_msgSend$shouldReduceLogging
+ _objc_retain_x27
- ___108-[APSConnection _initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:]_block_invoke.44
- ___65-[APSConnection _asyncOnDelegateQueueWithBlock:requiresDelegate:]_block_invoke.58
- ___block_literal_global.154
- ___block_literal_global.163
- _objc_retain_x26
CStrings:
+ "reduceLogging"
+ "reduced logging has been requested"
+ "shouldReduceLogging"

```
