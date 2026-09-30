## USBCAccessoryUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/USBCAccessoryUpdaterService.xpc/USBCAccessoryUpdaterService`

```diff

-46.0.0.0.0
-  __TEXT.__text: 0x150d0
+47.0.0.0.0
+  __TEXT.__text: 0x152cc
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0xec4
-  __TEXT.__objc_methname: 0x2762
-  __TEXT.__cstring: 0x3972
+  __TEXT.__objc_stubs: 0x1f20
+  __TEXT.__objc_methlist: 0xedc
+  __TEXT.__objc_methname: 0x289f
+  __TEXT.__cstring: 0x398c
   __TEXT.__objc_classname: 0x19a
-  __TEXT.__objc_methtype: 0xcd4
+  __TEXT.__objc_methtype: 0xd2a
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__unwind_info: 0x360
   __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__cfstring: 0x2f80
+  __DATA_CONST.__cfstring: 0x2fc0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x2838
-  __DATA.__objc_selrefs: 0xa38
+  __DATA.__objc_selrefs: 0xa48
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x240

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 331
+  Functions: 333
   Symbols:   217
-  CStrings:  1061
+  CStrings:  1067
 
CStrings:
+ "%s: Failed to execute iecsCommand(CFUp) for CFUp %@, status=0x%X"
+ "%s: Failed to execute iecsCommand(CFUp) for CFUp %@, taskResult=0x%X"
+ "disable"
+ "enable"
+ "executeIECSAtomicCommand:cmdBuffer:dataBuffer:extDataBuffer:returnDataBuffer:returnExtDataBuffer:inputDataLength:returnDataBufferLength:timeoutInSeconds:"
+ "i76@0:8C16^v20^v28^v36^v44^v52S60S64Q68"
+ "i88@0:8C16^v20^v28^v36^v44^v52S60S64Q68Q76I84"
+ "iecsAtomicCommand:cmdBuffer:dataBuffer:extDataBuffer:returnDataBuffer:returnExtDataBuffer:inputDataLength:returnDataBufferLength:timeoutInSeconds:forDevice:flags:"
- "%s: Failed to execute iecsCommand(CFUp) for CFUp enable/disable"
- "Failed to execute iecsWrite(DATA1) for CFUp enable/disable"

```
