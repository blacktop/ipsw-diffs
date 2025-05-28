## transparency-sysdiagnose

> `/usr/libexec/transparency-sysdiagnose`

```diff

-867.2.1.0.0
-  __TEXT.__text: 0x1010
+948.0.0.0.1
+  __TEXT.__text: 0xc58
   __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x500
+  __TEXT.__objc_stubs: 0x420
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1e6
-  __TEXT.__objc_methname: 0x309
-  __TEXT.__unwind_info: 0x74
+  __TEXT.__cstring: 0x19b
+  __TEXT.__objc_methname: 0x265
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x108
   __DATA.__objc_classrefs: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12
-  Symbols:   63
-  CStrings:  72
+  Functions: 8
+  Symbols:   62
+  CStrings:  62
 
Symbols:
+ _OBJC_CLASS_$_KTOptInManager
+ _OBJC_CLASS_$_KTOptInStateRequest
+ _OBJC_CLASS_$_TransparencySettings
- _OBJC_CLASS_$_KTStatus
- _OBJC_CLASS_$_TransparencyAnalytics
- _OBJC_CLASS_$_TransparencyAuditorReport
- _kTransparencyAuditorReportsSysdiagnoseKey
CStrings:
+ "allowsInternalSecurityPolicies"
+ "altDSID"
+ "getOptInState:completion:"
+ "state"
+ "tbs"
+ "tbsKTIDSRegistrationData"
+ "v24@?0@\"KTOptInState\"8@\"NSError\"16"
- "auditorError"
- "base64EncodedStringWithOptions:"
- "count"
- "dictionaryWithDictionary:"
- "enumerateObjectsUsingBlock:"
- "getReportForUUID:completionBlock:"
- "getStatus:"
- "hasInternalDiagnostics"
- "initWithAuditorId:"
- "optInState"
- "recentFailedEventIds"
- "redacted"
- "setRecentFailedEventIds:"
- "subarrayWithRange:"
- "uri"
- "v24@?0@\"KTStatusResult\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v32@?0@\"NSUUID\"8Q16^B24"

```
