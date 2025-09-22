## AKAppSSOExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension`

```diff

-458.1.1.7.0
-  __TEXT.__text: 0x4a38
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x284
+464.5.0.0.0
+  __TEXT.__text: 0x5020
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x2a8
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x29f2
+  __TEXT.__cstring: 0x2a19
   __TEXT.__objc_classname: 0xc9
-  __TEXT.__objc_methname: 0xfe0
-  __TEXT.__objc_methtype: 0x27d
+  __TEXT.__objc_methname: 0x1090
+  __TEXT.__objc_methtype: 0x2a8
   __TEXT.__gcc_except_tab: 0x124
-  __TEXT.__oslogstring: 0x58d
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x198
-  __DATA_CONST.__got: 0x50
+  __TEXT.__oslogstring: 0x6fb
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x278
-  __DATA_CONST.__cfstring: 0x1460
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA.__objc_const: 0x9b0
-  __DATA.__objc_selrefs: 0x478
-  __DATA.__objc_classrefs: 0xe0
+  __DATA.__objc_selrefs: 0x4b0
+  __DATA.__objc_classrefs: 0xe8
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x140

   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO

   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92590ED1-DC7A-32CC-B254-638AD505E6C0
-  Functions: 78
-  Symbols:   150
-  CStrings:  563
+  UUID: CFD941DA-F134-3C2C-9F26-CD7F31A7219E
+  Functions: 84
+  Symbols:   159
+  CStrings:  585
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFRelease
+ _OBJC_CLASS_$_AKURLBag
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _kCFAllocatorDefault
+ _objc_retainAutorelease
CStrings:
+ "B32@0:8@16^{?=[8I]}24"
+ "B56@0:8{?=[8I]}16@48"
+ "Caller is not entitled for first party origin. Authorization request not handled."
+ "Entitlement %@ is not present"
+ "NO"
+ "Process hasEntitlement to %@: %@"
+ "SecTaskCopyValueForEntitlement failed for %@, error: %@"
+ "SecTaskCreateWithAuditToken failed for entitlement %@"
+ "Server has disabled the entitlement checks for first party URLs. Proceeding."
+ "Unexpected size of auditToken: %u"
+ "YES"
+ "_auditTokenFromData:auditToken:"
+ "_canProcessRequestForFirstParty:"
+ "auditTokenData"
+ "bytes"
+ "checkEntitlementForAuditToken:entitlement:"
+ "com.apple.developer.web-browser"
+ "isFirstPartyURLEntitlementCheckDisabled"
+ "sharedBag"

```
