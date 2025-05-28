## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-104.0.0.0.0
-  __TEXT.__text: 0x2b848
+104.0.1.0.0
+  __TEXT.__text: 0x2bf54
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x2d58
-  __TEXT.__cstring: 0x13b3
-  __TEXT.__oslogstring: 0x5d24
+  __TEXT.__objc_methlist: 0x2d90
+  __TEXT.__cstring: 0x140d
+  __TEXT.__oslogstring: 0x5e85
   __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__const: 0x60
-  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__const: 0x68
+  __TEXT.__unwind_info: 0x7b8
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x58f
-  __TEXT.__objc_methname: 0x864d
+  __TEXT.__objc_methname: 0x8739
   __TEXT.__objc_methtype: 0x10f9
-  __TEXT.__objc_stubs: 0x6100
+  __TEXT.__objc_stubs: 0x61c0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f58
-  __DATA_CONST.__objc_selrefs: 0x1bb0
-  __AUTH_CONST.__cfstring: 0x1ea0
+  __DATA_CONST.__objc_const: 0x4f88
+  __DATA_CONST.__objc_selrefs: 0x1be0
+  __AUTH_CONST.__cfstring: 0x1f20
   __AUTH_CONST.__objc_const: 0xe00
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x1c8

   __AUTH.__data: 0x8
   __DATA.__objc_classrefs: 0x270
   __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x3ec
+  __DATA.__objc_ivar: 0x3f0
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 975
-  Symbols:   3568
-  CStrings:  2099
+  Functions: 980
+  Symbols:   3585
+  CStrings:  2114
 
Symbols:
+ -[SADevice isAirPodsCase]
+ -[SADeviceRecord _updateLatestCaseAdvertisementDate:]
+ -[SADeviceRecord getLatestCaseAdvertisementDate:]
+ -[SASingleDeviceRecord latestCaseAdvertisementDate]
+ -[SASingleDeviceRecord updateLatestCaseAdvertisementDate:]
+ _OBJC_IVAR_$_SASingleDeviceRecord._latestCaseAdvertisementDate
+ _objc_msgSend$_updateLatestCaseAdvertisementDate:
+ _objc_msgSend$getBatteryState
+ _objc_msgSend$getLatestCaseAdvertisementDate:
+ _objc_msgSend$isAirPodsCase
+ _objc_msgSend$latestCaseAdvertisementDate
+ _objc_msgSend$updateLatestCaseAdvertisementDate:
CStrings:
+ "\x1266"
+ "T@\"NSDate\",R,N,V_latestCaseAdvertisementDate"
+ "_latestCaseAdvertisementDate"
+ "_updateLatestCaseAdvertisementDate:"
+ "getBatteryState"
+ "getLatestCaseAdvertisementDate:"
+ "isAirPodsCase"
+ "lastAlertBatteryState"
+ "lastBatteryStateBeforeAlert"
+ "latestCaseAdvertisementDate"
+ "noCaseAdvSuppressed"
+ "reunionBatteryState"
+ "updateLatestCaseAdvertisementDate:"
+ "{\"msg%{public}.0s\":\"#sa separation for device with no recent case advertisement - suppressing alert\", \"device\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa separation for device with recent case advertisement\", \"device\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa separation for device with too old case advertisement - suppressing alert\", \"device\":\"%{private}@\"}"
- "\x1256"

```
