## AirPlaySenderKit

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/AirPlaySenderKit`

```diff

-800.68.1.0.0
-  __TEXT.__text: 0xbc00
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x2e4
+830.2.0.0.0
+  __TEXT.__text: 0xbff4
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x2648
+  __TEXT.__cstring: 0x2682
   __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0x8fa
-  __TEXT.__objc_methtype: 0x403
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x758
+  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__objc_classname: 0x75
+  __TEXT.__objc_methname: 0x96b
+  __TEXT.__objc_methtype: 0x445
+  __TEXT.__objc_stubs: 0x6e0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__const: 0x190
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0xa80
+  __AUTH_CONST.__objc_const: 0xb10
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x230
   __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 199
-  Symbols:   442
-  CStrings:  431
+  Functions: 203
+  Symbols:   460
+  CStrings:  445
 
Symbols:
+ _APSRealTimeSignalCreate
+ _APSRealTimeSignalRaise
+ _APSRingBufferCreate
+ _APSRingBufferDequeueBytes
+ _APSRingBufferEnqueueBytes
+ _APSRingBufferGetBytesFree
+ _APSRingBufferGetBytesUsed
+ _CMClockConvertHostTimeToSystemUnits
+ _CMClockMakeHostTimeFromSystemUnits
+ _OBJC_CLASS_$_NSMutableData
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_retain_x26
CStrings:
+ "@?16@0:8"
+ "AI"
+ "T@?,R,N"
+ "^{APSRealTimeSignalPrivate=}"
+ "^{APSRingBufferPrivate=}"
+ "_rtQueue"
+ "_rtRingBuffer"
+ "_rtRingBufferEntries"
+ "_rtSignal"
+ "apsksa_rtDispatchSignalHandler"
+ "c1"
+ "com.apple.apskstreamaudio.dataq"
+ "enqueueAudioDataBlock"
+ "i56@?0r^v8I16{?=qiIq}20Q44B52"
+ "initWithLength:"
+ "mutableBytes"
- "### Invalid audio format [%!{(MISSING)asbd}]"
- "c"

```
