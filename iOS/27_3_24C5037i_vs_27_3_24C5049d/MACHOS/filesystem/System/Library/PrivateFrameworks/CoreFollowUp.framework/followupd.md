## followupd

> `/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.2.2.0.0
-  __TEXT.__text: 0xee70
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0x2c20
-  __TEXT.__objc_methlist: 0xbe4
+2027.2.4.0.0
+  __TEXT.__text: 0xf504
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_stubs: 0x2dc0
+  __TEXT.__objc_methlist: 0xc14
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__cstring: 0x1d39
-  __TEXT.__oslogstring: 0x1244
+  __TEXT.__cstring: 0x1d92
+  __TEXT.__oslogstring: 0x12b1
   __TEXT.__objc_classname: 0x162
-  __TEXT.__objc_methname: 0x294e
-  __TEXT.__objc_methtype: 0x8e2
-  __TEXT.__unwind_info: 0x590
-  __DATA_CONST.__const: 0x8b8
-  __DATA_CONST.__cfstring: 0xa40
+  __TEXT.__objc_methname: 0x2b04
+  __TEXT.__objc_methtype: 0x8f3
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__const: 0x938
+  __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_got: 0x450
+  __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x1740
-  __DATA.__objc_selrefs: 0xca8
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_const: 0x1760
+  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x2a8
   __DATA.__crash_info: 0x148

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 316
-  Symbols:   230
-  CStrings:  794
+  Functions: 322
+  Symbols:   236
+  CStrings:  819
 
Symbols:
+ _CC_SHA256
+ _FLTelemetrySnapshotTriggerDaily
+ _XPC_ACTIVITY_GRACE_PERIOD
+ _XPC_ACTIVITY_INTERVAL_4_HOURS
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ _objc_retain_x4
CStrings:
+ "\x1f"
+ "/"
+ "@\"NSArray\"8@?0"
+ "@40@0:8@16@24@32"
+ "Capturing daily telemetry snapshot"
+ "Existing UNNotification for %@ has no content fingerprint, comparing text"
+ "FLNotificationContentFingerprint"
+ "Users"
+ "_processName"
+ "_registerAnalyticsSnapshotActivity"
+ "base64EncodedStringWithOptions:"
+ "captureTelemetrySnapshotWithTrigger:"
+ "com.apple.followup.analytics"
+ "componentsJoinedByString:"
+ "contentFingerprintWithTitle:body:subtitle:"
+ "dataUsingEncoding:"
+ "fl_pathRedactingHomeFolder:"
+ "isDeliveredContent:outOfDateForItem:"
+ "objectAtIndexedSubscript:"
+ "pathComponents"
+ "pathWithComponents:"
+ "processItemPost:isNew:process:"
+ "processNotificationDelivery:reason:"
+ "processSnapshotWithItems:trigger:"
+ "sharedProcessor"
+ "stringByAppendingPathComponent:"
+ "subarrayWithRange:"
+ "~"
- "_telemetryProcessor"
- "initWithController:"
- "processItemAddition:"
```
