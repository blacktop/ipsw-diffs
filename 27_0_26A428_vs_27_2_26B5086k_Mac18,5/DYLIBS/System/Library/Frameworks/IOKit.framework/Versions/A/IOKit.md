## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100288.0.9.0.0
-  __TEXT.__text: 0xbae8c
+100288.40.8.0.1
+  __TEXT.__text: 0xbb530
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__cstring: 0xf292
+  __TEXT.__cstring: 0xf2ea
   __TEXT.__const: 0x10620
   __TEXT.__dlopen_cstrs: 0x57
-  __TEXT.__oslogstring: 0x564f
+  __TEXT.__oslogstring: 0x58e7
   __TEXT.__gcc_except_tab: 0x578
-  __TEXT.__unwind_info: 0x36d8
+  __TEXT.__unwind_info: 0x36f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2660
+  __DATA_CONST.__const: 0x26a8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x210
-  __AUTH_CONST.__const: 0x27e8
-  __AUTH_CONST.__cfstring: 0x82a0
+  __AUTH_CONST.__const: 0x2828
+  __AUTH_CONST.__cfstring: 0x82c0
   __AUTH_CONST.__objc_const: 0x508
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x11c8
+  __AUTH_CONST.__auth_got: 0x11d0
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x1c

   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x258
   __DATA_DIRTY.__common: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/system/libkxld.dylib
-  Functions: 3896
-  Symbols:   4656
-  CStrings:  2989
+  Functions: 3907
+  Symbols:   4669
+  CStrings:  2998
 
Symbols:
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ __IOHIDEventSystemCompareServiceFunction
+ __IOHIDEventSystemLoadSecurity.onceToken
+ __IOHIDEventSystemLoadTCC.onceToken
+ __IOHIDServiceGetTCCService
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
+ "OSKEXT_BUILD_DATE 22:33:34 Sep  3 2026"
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
- "OSKEXT_BUILD_DATE 13:55:47 Aug  8 2026"
- "XYZ"
```
