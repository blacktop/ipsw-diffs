## keybagd

> `/usr/libexec/keybagd`

```diff

-640.60.3.0.0
-  __TEXT.__text: 0x1e4f4
-  __TEXT.__auth_stubs: 0x1410
+640.80.3.0.0
+  __TEXT.__text: 0x1eb30
+  __TEXT.__auth_stubs: 0x1420
   __TEXT.__objc_stubs: 0xfe0
   __TEXT.__objc_methlist: 0x4a0
-  __TEXT.__cstring: 0x9026
+  __TEXT.__cstring: 0x91ac
   __TEXT.__const: 0x171
   __TEXT.__gcc_except_tab: 0x468
   __TEXT.__objc_methname: 0x177b

   __TEXT.__objc_methtype: 0x925
   __TEXT.__dlopen_cstrs: 0x16a
   __TEXT.__oslogstring: 0x16a
-  __TEXT.__unwind_info: 0x648
-  __DATA_CONST.__auth_got: 0xa18
+  __TEXT.__unwind_info: 0x660
+  __DATA_CONST.__auth_got: 0xa20
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xf68
-  __DATA_CONST.__cfstring: 0x4c40
+  __DATA_CONST.__const: 0xf88
+  __DATA_CONST.__cfstring: 0x4d60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 465
-  Symbols:   389
-  CStrings:  1411
+  Functions: 471
+  Symbols:   390
+  CStrings:  1426
 
Symbols:
+ _abort
CStrings:
+ "AnalyticsEvent: days_since_passcode_change: %llu, passcode_reset_expired: %llu, passcode_reset_exists: %llu, days_since_lock: %llu, days_since_unlock: %llu"
+ "HealthPlistSetLockDate"
+ "HealthPlistSetUnlockDate"
+ "_DLD"
+ "_DULD"
+ "cant set ld"
+ "cant set uld"
+ "days_since_lock"
+ "days_since_unlock"
+ "failed to copy or create health plist"
+ "fetch_lock_unlock_dates_block_invoke"
+ "invalid ld timestamp"
+ "invalid uld timestamp"
+ "keybagd_health_plist_set_date_block_invoke"
+ "ld time stamp is of wrong type"
+ "uld time stamp is of wrong type"
- "AnalyticsEvent: days_since_passcode_change: %llu, passcode_reset_expired: %llu, passcode_reset_exists: %llu"

```
