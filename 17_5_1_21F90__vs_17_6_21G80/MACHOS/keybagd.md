## keybagd

> `/usr/libexec/keybagd`

```diff

-625.120.3.0.0
-  __TEXT.__text: 0x1cdf4
-  __TEXT.__auth_stubs: 0x13d0
+625.140.5.0.0
+  __TEXT.__text: 0x1d308
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x480
-  __TEXT.__cstring: 0x7cbe
+  __TEXT.__objc_methlist: 0x488
+  __TEXT.__cstring: 0x7ecb
   __TEXT.__const: 0xd1
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__objc_methname: 0x175b
+  __TEXT.__objc_methname: 0x177b
   __TEXT.__objc_classname: 0xa7
   __TEXT.__objc_methtype: 0x925
   __TEXT.__dlopen_cstrs: 0x16a
   __TEXT.__oslogstring: 0x16a
-  __TEXT.__unwind_info: 0x618
-  __DATA_CONST.__auth_got: 0x9f8
+  __TEXT.__unwind_info: 0x628
+  __DATA_CONST.__auth_got: 0xa00
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xe40
-  __DATA_CONST.__cfstring: 0x4ba0
+  __DATA_CONST.__const: 0xf08
+  __DATA_CONST.__cfstring: 0x4c60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_classrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0xef0
-  __DATA.__objc_selrefs: 0x570
+  __DATA.__objc_const: 0xf10
+  __DATA.__objc_selrefs: 0x578
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x1f8
   __DATA.__common: 0x30
   __DATA.__bss: 0x148
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 449
-  Symbols:   376
-  CStrings:  1325
+  Functions: 459
+  Symbols:   377
+  CStrings:  1340
 
Symbols:
+ _aks_get_seconds_since_passcode_change
CStrings:
+ "AnalyticsEvent: days_since_passcode_change: %llu, passcode_reset_expired: %llu, passcode_reset_exists: %llu"
+ "WA: Preserving SE KUD since stash is committed"
+ "analytics_is_event_persisted"
+ "analytics_iterate_persisted_eventsWithBlock"
+ "analytics_persist_event failed"
+ "analytics_send_forgotten_passcode_event"
+ "com.apple.mobile.keybagd.forgotten_passcode"
+ "days_since_passcode_change"
+ "event %@ is already persisted: %d"
+ "event already persisted"
+ "forgottenPasscodeEventWithReply:"
+ "keybagd_forgottenPasscodeEvent_block_invoke"
+ "not de-"
+ "passcode_reset_exists"
+ "passcode_reset_expired"

```
