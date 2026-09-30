## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

 1050.2.0.0.0
-  __TEXT.__text: 0xd7f10
+  __TEXT.__text: 0xd7f28
   __TEXT.__auth_stubs: 0x1730
   __TEXT.__objc_methlist: 0x124d0
   __TEXT.__const: 0x6e8
-  __TEXT.__cstring: 0x202c5
+  __TEXT.__cstring: 0x20304
   __TEXT.__oslogstring: 0x4862
   __TEXT.__gcc_except_tab: 0x1920
   __TEXT.__dlopen_cstrs: 0xf3

   __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x1b2a0
+  __AUTH_CONST.__cfstring: 0x1b2c0
   __AUTH_CONST.__objc_const: 0x22ef0
   __AUTH_CONST.__objc_intobj: 0x19f8
   __AUTH_CONST.__objc_arrayobj: 0x3f0

   - /usr/lib/libobjc.A.dylib
   Functions: 6570
   Symbols:   14383
-  CStrings:  13919
+  CStrings:  13920
 
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 892 -> 924
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1756 -> 1744
~ -[WiFiUsageSession _generateState] : 1044 -> 1048
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
```
