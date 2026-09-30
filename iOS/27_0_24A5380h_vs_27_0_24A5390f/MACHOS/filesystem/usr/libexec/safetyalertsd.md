## safetyalertsd

> `/usr/libexec/safetyalertsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-70.0.17.0.0
-  __TEXT.__text: 0xfdb50
-  __TEXT.__auth_stubs: 0x10c0
+70.0.19.0.0
+  __TEXT.__text: 0xfe188
+  __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0x3760
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0x9870
-  __TEXT.__cstring: 0x7a52
-  __TEXT.__gcc_except_tab: 0xeed4
-  __TEXT.__oslogstring: 0x432c5
+  __TEXT.__cstring: 0x7a5a
+  __TEXT.__gcc_except_tab: 0xef60
+  __TEXT.__oslogstring: 0x4359a
   __TEXT.__objc_methname: 0x3e58
   __TEXT.__objc_classname: 0x1e9
   __TEXT.__objc_methtype: 0x1cdf
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x43d0
-  __DATA_CONST.__const: 0x89d8
+  __TEXT.__unwind_info: 0x4408
+  __DATA_CONST.__const: 0x89b8
   __DATA_CONST.__cfstring: 0x72c0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x870
-  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1248
   __DATA.__objc_selrefs: 0x1260

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3602
-  Symbols:   470
-  CStrings:  5100
+  Functions: 3605
+  Symbols:   469
+  CStrings:  5108
 
Symbols:
- _dispatch_after
CStrings:
+ "cleanupStaleAlertsAndNotifications"
+ "{\"msg%{public}.0s\":\"#chNg,#getRBDChannelsListForAlertType,invalid locationd\"}"
+ "{\"msg%{public}.0s\":\"#daemon,cleanupGeoAlertCache,completed\", \"removedCount\":%{public}lu, \"remainingCount\":%{public}lu, \"writeSucceeded\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,writeGeoAlertCacheFile,emptyPath\"}"
+ "{\"msg%{public}.0s\":\"#daemon,writeGeoAlertCacheFile,emptySerialization\"}"
+ "{\"msg%{public}.0s\":\"#daemon,writeGeoAlertCacheFile,nilCache\"}"
+ "{\"msg%{public}.0s\":\"#main,Daemon not supported, idling and letting launchd manage lifecycle\", \"isSupportedDevice\":%{private}hhd, \"isSupportedOSType\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#notif,removeExpiredDeliveredNotifications,saMatch\", \"notifId\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#notif,removeExpiredDeliveredNotifications,totalDelivered\", \"totalDelivered\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#notif,removeExpiredDeliveredNotifications,zeroDelivered\", \"bundleId\":%{private, location:escape_only}s}"
- "removeExpiredNotifications"
- "{\"msg%{public}.0s\":\"#main,Daemon not supported, shutdown sequence will be initiated after idle timeout\", \"shutdownIdleTimeoutSeconds\":%{private}d, \"isSupportedDevice\":%{private}hhd, \"isSupportedOSType\":%{private}hhd}"
```
