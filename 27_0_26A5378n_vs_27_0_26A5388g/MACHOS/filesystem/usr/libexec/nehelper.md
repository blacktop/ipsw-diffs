## nehelper

> `/usr/libexec/nehelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2322.0.0.501.1
-  __TEXT.__text: 0x23448
+2331.0.0.0.1
+  __TEXT.__text: 0x22608
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_stubs: 0x2440
+  __TEXT.__objc_stubs: 0x2340
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x12c
-  __TEXT.__gcc_except_tab: 0x8e8
-  __TEXT.__objc_methname: 0x1cca
-  __TEXT.__cstring: 0x3392
-  __TEXT.__oslogstring: 0x4118
+  __TEXT.__gcc_except_tab: 0x858
+  __TEXT.__objc_methname: 0x1c16
+  __TEXT.__cstring: 0x30bb
+  __TEXT.__oslogstring: 0x40ca
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x280
-  __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__const: 0xd60
-  __DATA_CONST.__cfstring: 0x23e0
+  __TEXT.__unwind_info: 0x3e0
+  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__cfstring: 0x22e0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x718
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2a0
   __DATA.__objc_const: 0x17c8
-  __DATA.__objc_selrefs: 0x9b0
+  __DATA.__objc_selrefs: 0x970
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xcc

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 246
-  Symbols:   307
-  CStrings:  1257
+  Functions: 240
+  Symbols:   305
+  CStrings:  1233
 
Symbols:
- _OBJC_CLASS_$_NEAppRule
- _kNESafariSigningIdentifier
CStrings:
+ "%@: not platform entitled and no application ID is set, permission denied"
+ "Operation failed, client is not signed"
+ "setPermissionsIfNecessary"
- "B32@?0@8Q16^B24"
- "Failed to upgrade AppleConnect configuration %@: %@"
- "Failed to upgrade the WebKit rule for configuration %@: %@"
- "No signature found for configuration %@"
- "PluginType"
- "Upgrading AppleConnect configuration %@"
- "anchor apple generic and identifier \"com.cisco.anyconnect.macosext.networkextension\" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = DE8Y96K9QP)"
- "com.apple.WebKit.Networking"
- "com.apple.ac-anyconnect.applevpn.plugin"
- "com.apple.application-identifier"
- "com.apple.ist.ds.appleconnect2"
- "com.apple.preferences.internetaccounts.remoteservice"
- "com.apple.private.AuthorizationServices"
- "com.cisco.anyconnect.macosext.networkextension"
- "identifier \"com.apple.Safari\" and anchor apple"
- "indexOfObjectPassingTest:"
- "initWithObjectsAndKeys:"
- "matchDomains"
- "plugin-types"
- "providerBundleIdentifier"
- "replaceObjectAtIndex:withObject:"
- "setAppRules:"
- "setDesignatedRequirement:"
- "setMatchDomains:"
- "setProviderBundleIdentifier:"
- "upgrade-app-rules"
- "upgrade-apple-connect"
```
