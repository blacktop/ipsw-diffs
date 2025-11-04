## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-1338.40.31.0.1
-  __TEXT.__text: 0x1f068
+1338.60.16.0.0
+  __TEXT.__text: 0x1f16c
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x384
-  __TEXT.__cstring: 0x5df3
+  __TEXT.__objc_methlist: 0x3b4
+  __TEXT.__cstring: 0x5e5a
   __TEXT.__const: 0x240
   __TEXT.__oslogstring: 0x7
   __TEXT.__unwind_info: 0x790
   __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0x9f0
-  __TEXT.__objc_methtype: 0x83c
-  __TEXT.__objc_stubs: 0x940
+  __TEXT.__objc_methname: 0xa27
+  __TEXT.__objc_methtype: 0x852
+  __TEXT.__objc_stubs: 0x980
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x298
+  __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x460
-  __AUTH_CONST.__cfstring: 0xf00
+  __AUTH_CONST.__cfstring: 0xf20
   __AUTH_CONST.__objc_const: 0x918
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5237BEAF-CF27-3F2B-B257-ABBD7C2EBE95
-  Functions: 940
-  Symbols:   1643
-  CStrings:  982
+  UUID: 5E100613-7EF5-3295-B206-F763A23D4CA7
+  Functions: 944
+  Symbols:   1653
+  CStrings:  991
 
Symbols:
+ -[UARPSoCUpdaterInstance setLogicUnitNumber:]
+ -[UARPSoCUpdaterInstance setRouterID:]
+ -[UARPSoCUpdaterInstance setUpdaterMode:]
+ -[UARPSoCUpdaterInstance updaterLog:]
+ _objc_msgSend$setLogicUnitNumber:
+ _objc_msgSend$setRouterID:
+ _objc_msgSend$updaterLog:
- _objc_msgSend$initWithLogicUnitNumber:helper:options:
CStrings:
+ "-[Ace3UpdateController createUpdaterInstanceFor:helper:options:]"
+ "Finished init Restore UARP Query Info"
+ "TC,V_routerID"
+ "TI,V_logicUnitNumber"
+ "Ti,V_updaterMode"
+ "setLogicUnitNumber:"
+ "setRouterID:"
+ "setUpdaterMode:"
+ "updaterLog:"
+ "v20@0:8C16"
+ "v20@0:8i16"
- "TC,R,V_routerID"
- "TI,R,V_logicUnitNumber"
- "Ti,R,V_updaterMode"

```
