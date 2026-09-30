## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.33.50.0.0
-  __TEXT.__text: 0x76404
-  __TEXT.__auth_stubs: 0x1de0
+3.39.2.0.0
+  __TEXT.__text: 0x76f7c
+  __TEXT.__auth_stubs: 0x1df0
   __TEXT.__objc_stubs: 0x13c0
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x21d0
-  __TEXT.__const: 0x2c70
-  __TEXT.__cstring: 0x7eba
-  __TEXT.__oslogstring: 0x4d80
+  __TEXT.__gcc_except_tab: 0x21fc
+  __TEXT.__const: 0x2c80
+  __TEXT.__cstring: 0x7ea5
+  __TEXT.__oslogstring: 0x502b
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x153f
   __TEXT.__objc_methtype: 0x11e8
-  __TEXT.__unwind_info: 0x1418
+  __TEXT.__unwind_info: 0x1420
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0xf00
+  __DATA_CONST.__auth_got: 0xf08
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x6fc8
+  __DATA_CONST.__const: 0x6308
   __DATA_CONST.__cfstring: 0x2fe0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1494
-  Symbols:   849
-  CStrings:  1859
+  Functions: 1504
+  Symbols:   850
+  CStrings:  1873
 
Symbols:
+ _pthread_cond_timedwait_relative_np
CStrings:
+ "%!s(MISSING): Could not power off the ISP, res = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Could not power on the ISP, res = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Could not release channel, res = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Could not reserve channel, res = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Data file load failed, status = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Invalid connection\n"
+ "%!s(MISSING): Invalid data file arguments\n"
+ "%!s(MISSING): Savage Auth failed, res = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Savage Auth failed, status = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Savage Pre Auth failed, status = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Unable to get the remote connection object (pid %!{(MISSING)private}d)\n"
+ "2"
+ "3.39"
+ "ISP_SavageAuth"
+ "SPD:ERR: #%!d(MISSING) SPD(%!d(MISSING),%!d(MISSING)) stride=%!d(MISSING) scaleXY(%!d(MISSING),%!d(MISSING)) totSize=%!d(MISSING)\n"
+ "SPD:ERR: CSPD::SPD pContext->meta.geom.sizeX is not expected as an odd number!!!\n"
+ "Sent kIOReturnBusy reply to client: (pid %!{(MISSING)private}d), num pending requests = %!u(MISSING)\n"
- "3.33"
- "50"
- "pContext->meta.geom.sizeX %! (MISSING)== 0"

```
