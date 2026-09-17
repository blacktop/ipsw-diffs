## neagent

> `/usr/libexec/neagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2340.1.2.0.0
-  __TEXT.__text: 0x1d99c
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0x2620
+2365.40.1.0.0
+  __TEXT.__text: 0x1dcbc
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x2700
   __TEXT.__objc_methlist: 0x1320
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x6c0
-  __TEXT.__objc_methname: 0x2e42
-  __TEXT.__oslogstring: 0x414d
-  __TEXT.__cstring: 0x1975
+  __TEXT.__objc_methname: 0x2f87
+  __TEXT.__oslogstring: 0x4210
+  __TEXT.__cstring: 0x19ff
   __TEXT.__objc_classname: 0x365
   __TEXT.__objc_methtype: 0x1019
   __TEXT.__unwind_info: 0x670
   __DATA_CONST.__const: 0x860
-  __DATA_CONST.__cfstring: 0xba0
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__auth_got: 0x428
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x210
-  __DATA.__objc_const: 0x23f8
-  __DATA.__objc_selrefs: 0xd50
-  __DATA.__objc_ivar: 0x190
+  __DATA.__objc_const: 0x2418
+  __DATA.__objc_selrefs: 0xd88
+  __DATA.__objc_ivar: 0x194
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x8a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 415
-  Symbols:   203
-  CStrings:  1210
+  Symbols:   205
+  CStrings:  1224
 
Symbols:
+ _NEGetConsoleUserUID
+ _getpwuid
Functions:
~ sub_100008b34 : 120 -> 124
~ sub_100008bb4 -> sub_100008bb8 : 4516 -> 5312
CStrings:
+ "%@: %s - Register with PIR Server (group <%@> use case <%@> PrivacyProxyFailOpen <%d> serverURL <%@> privacyPassIssuer <%@> pirEnforceSecurity <%d>"
+ "%@: %s - pirPrivacyPassIssuerURL does not match NSPIRConfiguration.PrivacyPassIssuerURL for %@"
+ "%@: %s - pirServerURL does not match NSPIRConfiguration.PIRServerURL for %@"
+ "-[NEPIRChecker validatePIRConfiguration:]"
+ "/Library/Managed Preferences"
+ "_pirEnforceSecurity"
+ "com.apple.networkextension.urlfilter.plist"
+ "dictionaryWithContentsOfFile:"
+ "infoPlistPIRServerURL"
+ "infoPlistPrivacyPassIssuerURL"
+ "initWithKeyExpirationMinutes:keyRotationBeforeExpirationMinutes:keyRotationIgnoreMissingEvaluationKey:useCases:networkConfig:requirePowerOfTwoShardCount:"
+ "setPirPrivacyPassIssuerURL:"
+ "setPirServerURL:"
+ "setUseUserTierTokenKey:"
+ "urlfilterProfileEnabled"
- "%@: %s - Register with PIR Server (group <%@> use case <%@> PrivacyProxyFailOpen <%d> serverURL <%@> privacyPassIssuer <%@>"
```
