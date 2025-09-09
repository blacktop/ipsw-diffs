## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

 921.0.120.0.0
-  __TEXT.__text: 0x3528
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__text: 0x3614
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__cstring: 0x52f
-  __TEXT.__oslogstring: 0x504
+  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__cstring: 0x55a
+  __TEXT.__oslogstring: 0x559
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x957
+  __TEXT.__objc_methname: 0x970
   __TEXT.__objc_methtype: 0x131
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x5c0
+  __DATA_CONST.__cfstring: 0x620
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x338
+  __DATA.__objc_selrefs: 0x340
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 47622DB0-77F2-3675-BA60-54DA878EBDAC
+  UUID: E5AAFD2A-84D4-3F69-A74E-07F87237F53D
   Functions: 48
-  Symbols:   112
-  CStrings:  297
+  Symbols:   113
+  CStrings:  305
 
Symbols:
+ _T200GetBoardIdFromDT
+ _objc_retain_x26
- _objc_retain_x25
Functions:
~ sub_100001758 : 1848 -> 2084
CStrings:
+ "0X%X"
+ "Failed to get BMU BoardId"
+ "Request Veridian fwURL & fwDigest with device serial number: %@ and battery code: %@"
+ "batteryCode"
+ "supportMultiBatteryTypes"

```
