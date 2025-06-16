## securityd

> `/usr/libexec/securityd`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x233c7c
-  __TEXT.__auth_stubs: 0x3980
-  __TEXT.__objc_stubs: 0x1ade0
-  __TEXT.__objc_methlist: 0x14694
+61439.140.8.0.0
+  __TEXT.__text: 0x2345f0
+  __TEXT.__auth_stubs: 0x39b0
+  __TEXT.__objc_stubs: 0x1ae40
+  __TEXT.__objc_methlist: 0x146dc
   __TEXT.__const: 0x3dd
-  __TEXT.__cstring: 0x1f928
-  __TEXT.__oslogstring: 0x294be
+  __TEXT.__cstring: 0x1f95a
+  __TEXT.__oslogstring: 0x29729
   __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__gcc_except_tab: 0xad08
   __TEXT.__objc_classname: 0x2289
-  __TEXT.__objc_methname: 0x2a0cb
-  __TEXT.__objc_methtype: 0x9d71
+  __TEXT.__objc_methname: 0x2a17e
+  __TEXT.__objc_methtype: 0x9d86
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6078
-  __DATA_CONST.__auth_got: 0x1cd0
+  __TEXT.__unwind_info: 0x6090
+  __DATA_CONST.__auth_got: 0x1ce8
   __DATA_CONST.__got: 0x1080
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x13748
+  __DATA_CONST.__const: 0x137b0
   __DATA_CONST.__cfstring: 0x1a8c0
   __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x68

   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x21900
-  __DATA.__objc_selrefs: 0x8bd8
+  __DATA.__objc_const: 0x21908
+  __DATA.__objc_selrefs: 0x8bf0
   __DATA.__objc_ivar: 0x1954
   __DATA.__objc_data: 0x5460
   __DATA.__data: 0x1ee8
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x9b8
+  __DATA.__bss: 0x9d0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3802EEE5-7D33-3A83-8FEB-0F5A95058D04
-  Functions: 9130
-  Symbols:   1473
-  CStrings:  18711
+  UUID: C09AE76E-59FD-3109-BDCD-45C2A859830E
+  Functions: 9139
+  Symbols:   1476
+  CStrings:  18730
 
Symbols:
+ _os_signpost_id_generate
+ _pthread_mutex_trylock
+ _qos_class_self
CStrings:
+ "Going for groups verifying, with resync if required"
+ "Going for groups verifying, without resync"
+ "Passed NULL StatCtx"
+ "Resync: Using already provided list of remote groups"
+ "Unable to allocate StatCtx: %{darwin.errno}d"
+ "Verify Groups, Resync is not requested, so returning"
+ "Verify Groups, Resync is requested, and we are NOT on par with CK; therefore going for resyncing"
+ "Verify Groups, Resync is requested, but we are on par with CK, therefore returning"
+ "com.apple.security.keychain_db.signposts"
+ "priority=%{public,signpost.telemetry:number1,name=priority}d  enableTelemetry=YES "
+ "read_connection_nowait"
+ "read_connection_wait"
+ "resyncFromRPC:privateRemoteZonesByZoneID:sharedRemoteZonesByZoneID:completion:"
+ "signpost"
+ "v44@0:8B16@20@28@?36"
+ "verifyGroupsInSyncAndResync:WithCompletion:"
+ "verifyGroupsInSyncAndResyncMissingGroupsWithCompletion:"
+ "write_connection_nowait"
+ "write_connection_wait"

```
