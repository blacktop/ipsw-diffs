## accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.1.3.0.0
-  __TEXT.__text: 0xdd02c
+1587.40.26.0.0
+  __TEXT.__text: 0xdd364
   __TEXT.__auth_stubs: 0x2230
-  __TEXT.__objc_stubs: 0x8c80
-  __TEXT.__objc_methlist: 0x43e0
-  __TEXT.__const: 0x1a3f0
-  __TEXT.__objc_methname: 0xabc9
-  __TEXT.__cstring: 0x215d3
+  __TEXT.__objc_stubs: 0x8c00
+  __TEXT.__objc_methlist: 0x43d0
+  __TEXT.__const: 0x1a400
+  __TEXT.__objc_methname: 0xaba4
+  __TEXT.__cstring: 0x2161f
   __TEXT.__objc_classname: 0x7ac
   __TEXT.__objc_methtype: 0x20fb
   __TEXT.__oslogstring: 0x7bfa

   __TEXT.__ustring: 0x16
   __TEXT.__unwind_info: 0x4258
   __TEXT.__eh_frame: 0x1e0
-  __DATA_CONST.__const: 0x7440
-  __DATA_CONST.__cfstring: 0x11100
+  __DATA_CONST.__const: 0x7458
+  __DATA_CONST.__cfstring: 0x11120
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__got: 0x578
   __DATA_CONST.__auth_ptr: 0x98
   __DATA.__objc_const: 0xaad8
-  __DATA.__objc_selrefs: 0x2a10
+  __DATA.__objc_selrefs: 0x29f0
   __DATA.__objc_ivar: 0x624
   __DATA.__objc_data: 0x1090
   __DATA.__data: 0x138d

   - /usr/lib/libcrypto.35.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5590
+  Functions: 5592
   Symbols:   726
-  CStrings:  7699
+  CStrings:  7697
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _os_variant_has_internal_content
- _CFBundleGetInfoDictionary
- ___kCFBooleanFalse
CStrings:
+ "-[AMSupportStaticURLSession _defaultSessionConfigurationWithIdentifier:]"
+ "ATS: OS is internal."
+ "ATS: disabled per request on allowed build type."
+ "NSAllowsArbitraryLoads"
+ "RequestHTTPAllowed"
+ "com.apple.libamsupport.amsupporturlsession"
+ "dataWithPropertyList:format:options:error:"
+ "libauthinstall-1155.40.6"
+ "set_atsContext:"
- "-[AMSupportStaticURLSession _urlRequestForHTTPMessage:]"
- "Leaving custom port as is: %@"
- "NSAppTransportSecurity"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "libauthinstall-1155.0.5"
- "port"
- "scheme"
- "setPort:"
- "setScheme:"
- "shouldUpgrateToHTTPS"
- "using ATS, upgraded requestURL to https: %@"
```
