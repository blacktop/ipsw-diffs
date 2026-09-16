## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100288.0.9.0.0
-  __TEXT.__text: 0xa15d4
+100288.40.8.0.1
+  __TEXT.__text: 0xa1c78
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104bc
-  __TEXT.__oslogstring: 0x5630
-  __TEXT.__cstring: 0xbe08
-  __TEXT.__unwind_info: 0x30d0
+  __TEXT.__oslogstring: 0x58c8
+  __TEXT.__cstring: 0xbe60
+  __TEXT.__unwind_info: 0x30f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2ce8
+  __DATA_CONST.__const: 0x2d30
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x1e0
-  __AUTH_CONST.__const: 0x1e58
-  __AUTH_CONST.__cfstring: 0x75c0
+  __AUTH_CONST.__const: 0x1e98
+  __AUTH_CONST.__cfstring: 0x75e0
   __AUTH_CONST.__objc_const: 0x508
-  __AUTH_CONST.__auth_got: 0x10b8
+  __AUTH_CONST.__auth_got: 0x10c0
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x1c

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3575
-  Symbols:   3963
-  CStrings:  2587
+  Functions: 3586
+  Symbols:   3972
+  CStrings:  2596
 
Symbols:
+ __IOHIDServiceGetTCCService
+ ___IOHIDEventSystemLoadSecurity.onceToken
+ ___IOHIDEventSystemLoadTCC.onceToken
+ _____IOHIDEventSystemLoadSecurity_block_invoke
+ _____IOHIDEventSystemLoadTCC_block_invoke
+ ___secTaskCreateWithAuditTokenFunc
+ ___secTaskGetCodeSignStatusFunc
+ ___tccCheckAuditTokenFunc
+ _audit_token_to_pid
CStrings:
+ "/System/Library/Frameworks/Security.framework/Security"
+ "Connection: %@ TCC check for service %@: %@ returned right:%llu"
+ "Connection: %@ denied match of service %@: TCC %@ right:%llu"
+ "Failed to create event at index=%d , eventDataSize: %u < minimum size: %u for type: %u"
+ "IOHIDEventSystem TCC matching: SecTask code sign status SPI unavailable, gating disabled"
+ "IOHIDEventSystem TCC matching: could not load Security.framework, gating disabled"
+ "IOHIDEventSystem TCC matching: could not load TCC.framework, gating disabled"
+ "IOHIDEventSystem TCC matching: tcc_authorization_check_audit_token unavailable, gating disabled"
+ "OSKEXT_BUILD_DATE 00:55:48 Sep  4 2026"
+ "SecTaskCreateWithAuditToken"
+ "SecTaskCreateWithAuditToken failed for pid:%d"
+ "SecTaskGetCodeSignStatus"
+ "TCCService"
+ "[%#llx] Invalid kIOHIDTCCServiceKey property, expected String"
+ "tcc_authorization_check_audit_token"
- "ColorComponent0:"
- "ColorComponent1:"
- "ColorComponent2:"
- "ColorSpace:"
- "OSKEXT_BUILD_DATE 14:15:26 Aug  8 2026"
- "XYZ"
```
