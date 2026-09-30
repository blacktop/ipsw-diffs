## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-1025.82.1.0.0
-  __TEXT.__text: 0x26b14
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0xff8
+1043.100.28.0.0
+  __TEXT.__text: 0x26f0c
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x17b4
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x389e
-  __TEXT.__oslogstring: 0x3bfa
-  __TEXT.__gcc_except_tab: 0xa9c
+  __TEXT.__cstring: 0x3916
+  __TEXT.__oslogstring: 0x3cc4
+  __TEXT.__gcc_except_tab: 0xab4
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x870
+  __TEXT.__unwind_info: 0x880
   __TEXT.__objc_classname: 0x258
-  __TEXT.__objc_methname: 0x43e3
+  __TEXT.__objc_methname: 0x4410
   __TEXT.__objc_methtype: 0x1594
-  __TEXT.__objc_stubs: 0x29a0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__objc_stubs: 0x2a00
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x1ca0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_selrefs: 0xe50
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0x30d0
+  __AUTH_CONST.__cfstring: 0x3700
+  __AUTH_CONST.__objc_const: 0x2260
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x748
-  __DATA.__bss: 0xe8
+  __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 716
-  Symbols:   1998
-  CStrings:  1557
+  Functions: 737
+  Symbols:   2015
+  CStrings:  1567
 
Symbols:
+ _SANDBOX_CHECK_NO_REPORT
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _getpid
+ _sandbox_check
CStrings:
+ "[#ExternalAccessory] Client not entitled to EA service"
+ "[#ExternalAccessory] Client not sandboxed to EA service"
+ "[#ExternalAccessory] No EA protocols found"
+ "[#ExternalAccessory] Unable to create self task"
+ "com.apple.private.externalaccessory.showallaccessories"
+ "com.apple.security.exception.mach-lookup.global-name"
+ "hasEAEntitlement"
+ "hasEAProtocols"
+ "hasEASandbox"
+ "mach-lookup"

```
