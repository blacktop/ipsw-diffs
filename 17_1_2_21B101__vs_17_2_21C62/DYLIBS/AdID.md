## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-602.0.0.0.0
-  __TEXT.__text: 0x18350
+608.0.0.0.0
+  __TEXT.__text: 0x18344
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xde4
+  __TEXT.__objc_methlist: 0xdcc
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x4e4
-  __TEXT.__cstring: 0x665a
-  __TEXT.__unwind_info: 0x55c
+  __TEXT.__gcc_except_tab: 0x4dc
+  __TEXT.__cstring: 0x6692
+  __TEXT.__unwind_info: 0x564
   __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x3f4d
+  __TEXT.__objc_methname: 0x3f1b
   __TEXT.__objc_methtype: 0x6f2
-  __TEXT.__objc_stubs: 0x3fe0
+  __TEXT.__objc_stubs: 0x3f80
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x9d8
+  __DATA_CONST.__const: 0xa28
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2388
-  __DATA_CONST.__objc_selrefs: 0x1210
+  __DATA_CONST.__objc_selrefs: 0x11f8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x4080
+  __AUTH_CONST.__cfstring: 0x4060
   __AUTH_CONST.__objc_const: 0x6f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB5D9315-CB02-33D6-9D6B-1B64471C3F0E
+  UUID: BBCB77E0-D2F0-3D0A-B82A-E9B4D8714F17
   Functions: 406
-  Symbols:   1916
-  CStrings:  1885
+  Symbols:   1915
+  CStrings:  1882
 
Symbols:
+ GCC_except_table10
+ ___52-[ADJingleRequest sendJingleRequest:withCompletion:]_block_invoke_2
+ ___58-[ADAMSBagManager authenticateAccountThroughAMSOperation:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e43_v24?0"AMSAuthenticateResult"8"NSError"16lr40l8s32l8
- -[DSIDRecord(Private) resetiAdIDsAndDPID:]
- -[DSIDRecord(Private) resetiAdIDs]
- ___34-[DSIDRecord(Private) resetiAdIDs]_block_invoke
- ___42-[DSIDRecord(Private) resetiAdIDsAndDPID:]_block_invoke
- _objc_msgSend$resetDPID:
- _objc_msgSend$resetiAdIDs
- _objc_msgSend$resultWithError:
CStrings:
+ "[FILE A RADAR] We failed to authenticate in time."
+ "v24@?0@\"AMSAuthenticateResult\"8@\"NSError\"16"
+ "v24@?0@8@\"NSError\"16"
- "Error resetting DPID: %@"
- "Resetting IDs for DSID record %@."
- "resetiAdIDs"
- "resetiAdIDsAndDPID:"
- "resultWithError:"

```
