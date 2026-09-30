## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd`

```diff

-805.60.2.0.0
-  __TEXT.__text: 0x16b6c
+805.60.5.0.0
+  __TEXT.__text: 0x16d18
   __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_stubs: 0x3000
   __TEXT.__objc_methlist: 0x16f4

   __TEXT.__objc_classname: 0x1f9
   __TEXT.__objc_methtype: 0x891
   __TEXT.__objc_methname: 0x22c9
-  __TEXT.__oslogstring: 0x14c6
+  __TEXT.__oslogstring: 0x1568
   __TEXT.__cstring: 0x15ab
   __TEXT.__gcc_except_tab: 0x2a0
-  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__unwind_info: 0x608
   __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x7e0

   - /System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75194A42-2CC7-3F42-B5CA-748E50657535
-  Functions: 655
+  UUID: 5E7AACF2-727A-3643-A2F4-8E1B23EBCB78
+  Functions: 657
   Symbols:   148
-  CStrings:  1395
+  CStrings:  1397
 
CStrings:
+ "escape: command failed with status 0x%02x, error 0x%02x"
+ "escape: no response received from transmitAndReceive"
+ "escape: payload data %{public}@"
+ "escape: unexpected message type 0x%02x, expected RDR_to_PC_Escape"
- "Failed to escape command."
- "escape: %{public}@"

```
