## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-  __TEXT.__cstring: 0x3e62
-  __TEXT.__os_log: 0x89ce
+  __TEXT.__cstring: 0x3e8f
+  __TEXT.__os_log: 0x8aa6
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x30ca0
+  __TEXT_EXEC.__text: 0x30d40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x688

   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1483
   Symbols:   0
-  CStrings:  721
+  CStrings:  724
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
Functions:
~ __ZN20IOTimeSyncUserClient12initWithTaskEP4taskPvjP12OSDictionary : 276 -> 356
~ __ZN32IOTimeSyncClockManagerUserClient12initWithTaskEP4taskPvjP12OSDictionary : 1204 -> 1284
CStrings:
+ "IOTimeSyncClockManagerUserClient::initWithTask: missing entitlement com.apple.private.timesync.direct-userclient\n"
+ "IOTimeSyncUserClient::initWithTask: missing entitlement com.apple.private.timesync.direct-userclient\n"
+ "com.apple.private.timesync.direct-userclient"

```
