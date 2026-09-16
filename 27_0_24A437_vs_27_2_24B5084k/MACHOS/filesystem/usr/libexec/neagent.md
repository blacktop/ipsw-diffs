## neagent

> `/usr/libexec/neagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
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

-2340.0.0.0.4
-  __TEXT.__text: 0x1aae4
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_stubs: 0x25a0
+2365.40.1.0.0
+  __TEXT.__text: 0x1adac
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_stubs: 0x2680
   __TEXT.__objc_methlist: 0x1210
-  __TEXT.__const: 0xf0
+  __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x6bc
-  __TEXT.__objc_methname: 0x2db5
-  __TEXT.__oslogstring: 0x3efa
-  __TEXT.__cstring: 0x18d3
+  __TEXT.__objc_methname: 0x2efa
+  __TEXT.__oslogstring: 0x3fbd
+  __TEXT.__cstring: 0x195d
   __TEXT.__objc_classname: 0x354
   __TEXT.__objc_methtype: 0xef8
   __TEXT.__unwind_info: 0x5d0
   __DATA_CONST.__const: 0x690
-  __DATA_CONST.__cfstring: 0xb00
+  __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x1f0
-  __DATA.__objc_const: 0x21e8
-  __DATA.__objc_selrefs: 0xd30
-  __DATA.__objc_ivar: 0x174
+  __DATA.__objc_const: 0x2208
+  __DATA.__objc_selrefs: 0xd68
+  __DATA.__objc_ivar: 0x178
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x8a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 362
-  Symbols:   218
-  CStrings:  1175
+  Symbols:   220
+  CStrings:  1189
 
Symbols:
+ _NEGetConsoleUserUID
+ _getpwuid
Functions:
~ sub_100008520 : 116 -> 120
~ sub_10000859c -> sub_1000085a0 : 4304 -> 5012
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
