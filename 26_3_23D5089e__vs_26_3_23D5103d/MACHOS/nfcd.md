## nfcd

> `/usr/libexec/nfcd`

```diff

-363.6.0.0.0
-  __TEXT.__text: 0x27ad94
+363.8.1.0.0
+  __TEXT.__text: 0x27a98c
   __TEXT.__auth_stubs: 0x1850
-  __TEXT.__delay_stubs: 0x370
-  __TEXT.__delay_helper: 0x120c
-  __TEXT.__objc_stubs: 0xd4e0
-  __TEXT.__objc_methlist: 0x9ce0
+  __TEXT.__delay_stubs: 0x500
+  __TEXT.__delay_helper: 0x16bc
+  __TEXT.__objc_stubs: 0xd500
+  __TEXT.__objc_methlist: 0x9cf0
   __TEXT.__const: 0x13c0
-  __TEXT.__objc_methname: 0x17e18
-  __TEXT.__cstring: 0x2fa4f
+  __TEXT.__objc_methname: 0x17e49
+  __TEXT.__cstring: 0x2fa91
   __TEXT.__objc_classname: 0x1d5f
   __TEXT.__objc_methtype: 0x567d
-  __TEXT.__oslogstring: 0x26ad1
-  __TEXT.__unwind_info: 0x2c78
+  __TEXT.__oslogstring: 0x26b11
+  __TEXT.__unwind_info: 0x2c88
   __DATA_CONST.__auth_got: 0xcd0
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x18

   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_dictobj: 0xfa0
   __DATA.__objc_const: 0x14928
-  __DATA.__objc_selrefs: 0x55f8
+  __DATA.__objc_selrefs: 0x5608
   __DATA.__objc_ivar: 0x10ac
   __DATA.__objc_data: 0x3d90
   __DATA.__data: 0x2b94

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20BD4C3D-BDAF-3871-9EE3-1AC55649F7A3
-  Functions: 4163
+  UUID: 1B9EE180-FC88-3A3C-89B5-983F6BC15E5F
+  Functions: 4166
   Symbols:   593
-  CStrings:  14644
+  CStrings:  14646
 
CStrings:
+ "%c[%{public}s %{public}s]:%i activeSession=%d, activeSessionLockedSEAccess=%d,expressInProgress=%d,expressModesActive=%d"
+ "%c[%{public}s %{public}s]:%i expressInProgress=%d, expressIsActive=%d, requestorHoldsActiveSession=%d, activeSessionLockedSEAccess=%d"
+ "NFCD built from (B&I) Stockholm_Base-363.8.1"
+ "activateExpressSettings"
+ "isSEWiredAccessAvailable"
- "%c[%{public}s %{public}s]:%i activeSession=%d,expressInProgress=%d,expressModesActive=%d"
- "%c[%{public}s %{public}s]:%i expressInProgress=%d, expressIsActive=%d, requestorHoldsActiveSession=%d"
- "NFCD built from (B&I) Stockholm_Base-363.6"

```
