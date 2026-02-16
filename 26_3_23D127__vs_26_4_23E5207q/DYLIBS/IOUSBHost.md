## IOUSBHost

> `/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`

```diff

-1504.80.40.0.0
-  __TEXT.__text: 0x17fc4
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0xea8
+1504.100.57.0.0
+  __TEXT.__text: 0x18350
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0xec0
   __TEXT.__const: 0xcc
-  __TEXT.__cstring: 0x212f
-  __TEXT.__oslogstring: 0x2a4
-  __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__cstring: 0x21ec
+  __TEXT.__oslogstring: 0x2f4
+  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0x145
-  __TEXT.__objc_methname: 0x28f8
+  __TEXT.__objc_methname: 0x295c
   __TEXT.__objc_methtype: 0xed5
-  __TEXT.__objc_stubs: 0x1940
+  __TEXT.__objc_stubs: 0x1980
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__const: 0x718
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x848
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x18c0
+  __AUTH_CONST.__objc_const: 0x18f0
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0xa0
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55999C36-6F68-3756-88CC-3D216E0822E1
-  Functions: 468
-  Symbols:   1526
-  CStrings:  1035
+  UUID: BB6B42F1-1B21-3A40-BF1A-FDC9A3F41ABC
+  Functions: 492
+  Symbols:   1577
+  CStrings:  1040
 
Symbols:
+ -[IOUSBHostControllerInterface dealloc].cold.1
+ -[IOUSBHostControllerInterface ioConnectAsyncPending]
+ -[IOUSBHostControllerInterface setIoConnectAsyncPending:]
+ _OBJC_IVAR_$_IOUSBHostControllerInterface._ioConnectAsyncPending
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _objc_msgSend$ioConnectAsyncPending
+ _objc_msgSend$setIoConnectAsyncPending:
+ _objc_retainAutoreleasedReturnValue
- _IOUSBHostCIControllerStateToString.namedValues
- _IOUSBHostCIDeviceStateToString.namedValues
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "/Library/Caches/com.apple.xbs/D36D1B9C-BF6E-4B84-8689-4A518151B108/TemporaryDirectory.y8A7IY/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostInterface.m"
+ "/Library/Caches/com.apple.xbs/D36D1B9C-BF6E-4B84-8689-4A518151B108/TemporaryDirectory.y8A7IY/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostObject.m"
+ "/Library/Caches/com.apple.xbs/D36D1B9C-BF6E-4B84-8689-4A518151B108/TemporaryDirectory.y8A7IY/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostPipe.m"
+ "TQ,N,V_ioConnectAsyncPending"
+ "_ioConnectAsyncPending"
+ "dealloc IOUSBHostControllerInterface with UUID %@ without first calling destroy"
+ "ioConnectAsyncPending"
+ "setIoConnectAsyncPending:"
- "/Library/Caches/com.apple.xbs/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostInterface.m"
- "/Library/Caches/com.apple.xbs/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostObject.m"
- "/Library/Caches/com.apple.xbs/Sources/IOUSBHostFamily/IOUSBHostFramework/IOUSBHostPipe.m"

```
