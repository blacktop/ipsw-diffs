## mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0xd1f0
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xb64
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x20ab
-  __TEXT.__objc_methname: 0x1dd6
-  __TEXT.__objc_classname: 0x29d
+921.0.34.0.0
+  __TEXT.__text: 0xd718
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1980
+  __TEXT.__objc_methlist: 0xbb4
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x2192
+  __TEXT.__objc_methname: 0x1e6f
+  __TEXT.__objc_classname: 0x29c
   __TEXT.__objc_methtype: 0x330
-  __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__oslogstring: 0x774
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__auth_got: 0x320
-  __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__cfstring: 0x2300
+  __TEXT.__gcc_except_tab: 0x468
+  __TEXT.__oslogstring: 0x7cf
+  __TEXT.__unwind_info: 0x2c0
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__cfstring: 0x2420
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x18a8
-  __DATA.__objc_selrefs: 0x7e8
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_const: 0x18a0
+  __DATA.__objc_selrefs: 0x818
+  __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x190
   __DATA.__bss: 0x138

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4B3FEA0-8B2E-33DE-A8A2-4F2F53C69BD9
-  Functions: 255
-  Symbols:   189
-  CStrings:  1045
+  UUID: 8DC4F229-7956-36E5-9E2F-A83453A66004
+  Functions: 256
+  Symbols:   188
+  CStrings:  1069
 
Symbols:
+ _CRErrorDomain
+ _IOPSGetBatteryHealthState
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
- __dispatch_queue_attr_concurrent
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
CStrings:
+ "Battery Health State%@"
+ "Failed to get battery health state (%x):%@\n"
+ "IOPSBatteryHealthState"
+ "Unsupported product"
+ "[%s] IOREG Auth Component Trusted"
+ "[%s] Unknown Part SN differs from Finish Repair SN"
+ "[%s] Upgrade to Finish Repair from Unknown Part"
+ "[%s] component has displayed follow up"
+ "[%s] component has not displayed finish repair"
+ "[%s] component pending repair"
+ "clearBootIntentAndReboot:"
+ "com.apple.accessories"
+ "com.apple.audio.hw.failure.codec"
+ "com.apple.audio.hw.failure.speaker"
+ "com.apple.camera.fdr"
+ "com.apple.camera.hw"
+ "deviceHasReducedBootPolicyWithReply:"
+ "errorWithDomain:code:userInfo:"
+ "isBatteryInServiceState:"
+ "isSetupStillRunning"
+ "mobilerepaird started: %s"
+ "objectForKeyedSubscript:"
- "-[MRBaseComponentHandler checkInAndHandleAuthStatus]_block_invoke"
- "Localizable-J481"
- "[%s] IOREG Auth Component Not Populated"
- "[%s] Retry Count:%d"
- "[%s] cleaning up corefollowup finally"
- "asyncQueue"
- "com.apple.mobilerepaird.asyncqueue"
- "mobilerepaird started"

```
