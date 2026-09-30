## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1527.40.4.502.1
-  __TEXT.__text: 0x3a510
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x58c
-  __TEXT.__const: 0x400
-  __TEXT.__gcc_except_tab: 0x830
-  __TEXT.__oslogstring: 0x238e
-  __TEXT.__cstring: 0x2fb94
+1527.40.7.0.0
+  __TEXT.__text: 0x3a86c
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_stubs: 0x1640
+  __TEXT.__objc_methlist: 0x594
+  __TEXT.__const: 0x3f0
+  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__oslogstring: 0x2407
+  __TEXT.__cstring: 0x2fba8
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x2ac
-  __TEXT.__objc_methname: 0x15ee
-  __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__auth_got: 0x5f8
+  __TEXT.__objc_methname: 0x160a
+  __TEXT.__unwind_info: 0x590
+  __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0xa0
+  __DATA_CONST.__auth_ptr: 0xa8
   __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x1ba0
+  __DATA_CONST.__cfstring: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_selrefs: 0x600
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions
   - /System/Library/PrivateFrameworks/Proximity.framework/Proximity
+  - /System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 3621CE75-6BDA-392B-AAF2-0B4BAEC78BA7
-  Functions: 343
-  Symbols:   257
-  CStrings:  4385
+  UUID: 703FC6FE-B1A0-3F7E-9598-4BC3BA2A4654
+  Functions: 348
+  Symbols:   258
+  CStrings:  4391
 
Symbols:
+ _rrd_store_config_sysdiagnose
CStrings:
+ "RRD SPI timed out"
+ "RRD sysdiagnose SPI not found"
+ "RRD task encountered error when calling rrd_store_config_sysdiagnose: %@"
+ "RRDTaskWithDir:withTimeout:"
+ "TASK_TYPE_RRD_STATE"

```
