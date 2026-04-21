## AppleDeviceQueryService

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

```diff

-408.120.2.0.0
-  __TEXT.__text: 0xbba4
+408.120.3.0.0
+  __TEXT.__text: 0xc1d4
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x648
+  __TEXT.__objc_stubs: 0x11c0
+  __TEXT.__objc_methlist: 0x678
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x52b9
+  __TEXT.__cstring: 0x535f
   __TEXT.__objc_classname: 0xfc
-  __TEXT.__objc_methname: 0x1115
+  __TEXT.__objc_methname: 0x1256
   __TEXT.__objc_methtype: 0x3b1
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__gcc_except_tab: 0x23c
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__cfstring: 0x35e0
+  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__cfstring: 0x3640
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x990
-  __DATA.__objc_selrefs: 0x598
-  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_const: 0xa10
+  __DATA.__objc_selrefs: 0x5d0
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x230
   __DATA.__data: 0xc00
-  __DATA.__bss: 0x278
+  __DATA.__bss: 0x258
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD230ED1-080D-3B70-A1A0-EDD9F4869B17
-  Functions: 198
-  Symbols:   224
-  CStrings:  1296
+  UUID: 0837D7A4-83F4-3494-9B9E-FD7FFFBB9EF8
+  Functions: 199
+  Symbols:   225
+  CStrings:  1313
 
Symbols:
+ OBJC_IVAR_$_ZhuGeLockerService.recursiveMutexForXpcConnections
CStrings:
+ "-[ZhuGeService isCallerEntitledForInternalService]"
+ "-[ZhuGeService isCallerEntitledForService]"
+ "Failed to validate ZhuGe internal service entitlement for current connection from pid %@!"
+ "Failed to validate ZhuGe internal service entitlement for queued connection from pid %@!"
+ "Failed to validate ZhuGe service entitlement for current connection from pid %@!"
+ "Failed to validate ZhuGe service entitlement for queued connection from pid %@!"
+ "T@\"NSMutableArray\",&,V_allXpcConnections"
+ "T@\"NSMutableArray\",&,V_areXpcConnectionsChecked"
+ "The caller failed entitlement check!"
+ "ZhuGe service bridge-connected for current connection from pid %@"
+ "ZhuGe service connected for current connection from pid %@"
+ "_allXpcConnections"
+ "_areXpcConnectionsChecked"
+ "allXpcConnections"
+ "areXpcConnectionsChecked"
+ "isCallerEntitledForInternalService"
+ "isCallerEntitledForService"
+ "objectAtIndex:"
+ "recursiveMutexForXpcConnections"
+ "removeObjectAtIndex:"
+ "replaceObjectAtIndex:withObject:"
+ "setAllXpcConnections:"
+ "setAreXpcConnectionsChecked:"
+ "\x83"
- "-[ZhuGeService assertCallerEntitledForInternalService]"
- "-[ZhuGeService assertCallerEntitledForInternalService]_block_invoke"
- "-[ZhuGeService assertCallerEntitledForService]"
- "-[ZhuGeService assertCallerEntitledForService]_block_invoke"
- "Failed to validate ZhuGe internal service entitlement for pid %@!"
- "Failed to validate ZhuGe service entitlement for pid %@!"
- "ZhuGe service bridge-connected for pid %@"
- "ZhuGe service connected for pid %@"
- "assertCallerEntitledForInternalService"
- "assertCallerEntitledForService"

```
