## corerepaird

> `/usr/libexec/corerepaird`

```diff

-645.40.4.0.0
-  __TEXT.__text: 0x314d0
+645.40.12.0.0
+  __TEXT.__text: 0x32b1c
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_stubs: 0x2a00
-  __TEXT.__objc_methlist: 0x2a00
-  __TEXT.__oslogstring: 0xf6e
-  __TEXT.__cstring: 0x5314
+  __TEXT.__objc_stubs: 0x2aa0
+  __TEXT.__objc_methlist: 0x2a30
+  __TEXT.__oslogstring: 0x1203
+  __TEXT.__cstring: 0x5361
   __TEXT.__const: 0x3940
-  __TEXT.__objc_methname: 0x321f
+  __TEXT.__objc_methname: 0x32ff
   __TEXT.__objc_classname: 0xb84
   __TEXT.__objc_methtype: 0xab8
   __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__unwind_info: 0xd20
+  __TEXT.__unwind_info: 0xd30
   __DATA_CONST.__auth_got: 0x7c0
-  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0xe30
-  __DATA_CONST.__cfstring: 0x56c0
+  __DATA_CONST.__cfstring: 0x5740
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x58d0
-  __DATA.__objc_selrefs: 0xdd8
+  __DATA.__objc_const: 0x5910
+  __DATA.__objc_selrefs: 0xe10
   __DATA.__objc_ivar: 0x330
   __DATA.__objc_data: 0x16d0
   __DATA.__data: 0xa20

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 1091
-  Symbols:   330
-  CStrings:  2065
+  Functions: 1113
+  Symbols:   331
+  CStrings:  2100
 
Symbols:
+ _kBrunorTagResponseTicket
CStrings:
+ "perform next stage: %!@(MISSING)"
+ "verifyPSD3WithReply:"
+ "Get Brunor ticket failed"
+ "SavageUpdaterExecCommand failed: %!@(MISSING)"
+ "Get osBootHash failed"
+ "Updating Yonkers ..."
+ "Failed to create SavageUpdater: %!@(MISSING)"
+ "verifyFDRData %!p(MISSING) %!z(MISSING)u\n"
+ "Get prebootPath failed"
+ "SavageUpdater failed with error: %!@(MISSING)"
+ "psd3"
+ "Verify PSD3 failed"
+ "prpc"
+ "Failed to verify psd3, pearlStatus: %!d(MISSING)"
+ "Get Yonkers ticket failed"
+ "Create optionsDict failed"
+ "Verify psd3 successfully"
+ "Create updaterOptions failed"
+ "updateBrunorDATFirmware"
+ "powerCycleSensor failed with error: %!@(MISSING)"
+ "Update streaming DAT file failed"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "deviceInfoDict: %!@(MISSING)"
+ "powerCycleSensor:"
+ "updaterOptions: %!@(MISSING) updaterLoopCount: %!d(MISSING)"
+ "updateBrunorDATFirmwareWithReply:"
+ "Updating Brunor ..."
+ "verifyPSD3"
+ "verifyFDRData -> %!d(MISSING)\n"
+ "dataLength > 0"
+ "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
+ "SavageUpdater work done. LoopCounter = %!d(MISSING)."
+ "Get customAMAuthInstallRef failed"
+ "Failed to get local psd3, error: %!@(MISSING)"

```
