## SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

-1856.2.2.0.0
-  __TEXT.__text: 0x1f60
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x680
+1856.42.1.0.0
+  __TEXT.__text: 0x2124
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_stubs: 0x6c0
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__cstring: 0x2d3
+  __TEXT.__cstring: 0x2f4
   __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methname: 0x806
-  __TEXT.__oslogstring: 0x34e
+  __TEXT.__objc_methname: 0x826
+  __TEXT.__oslogstring: 0x3b7
   __TEXT.__objc_methtype: 0x347
   __TEXT.__const: 0x8
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x30
-  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x968
-  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_selrefs: 0x210
   __DATA.__objc_classrefs: 0x90
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 20
-  Symbols:   367
-  CStrings:  183
+  Symbols:   370
+  CStrings:  188
 
Symbols:
+ _objc_msgSend$isValid
+ _objc_msgSend$scheduleUpdate:withError:
+ _objc_retain_x22
CStrings:
+ "%s: %@ is invalid, not adding key (%@)"
+ "%s: Canceling update for key %{public}@"
+ "Anomaly: No controller found to cancel declaration for key %{public}@"
+ "Canceled update, result = %d; error = %{public}@"
+ "Invalid declaration detected: %@"
+ "Scheduled update, result = %d, error = %{public}@"
+ "isValid"
+ "scheduleUpdate:withError:"
- "%s: About to remove declaration for key %{public}@"
- "Anomaly: No controller found to cancel declaration for key %@"
- "Scheduled update, result = %d"

```
