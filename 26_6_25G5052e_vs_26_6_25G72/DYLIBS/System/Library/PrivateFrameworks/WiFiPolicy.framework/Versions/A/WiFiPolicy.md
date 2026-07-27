## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy`

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
- `__AUTH_CONST.__auth_got`
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

 1051.2.0.0.0
-  __TEXT.__text: 0xd9d64
+  __TEXT.__text: 0xd9d7c
   __TEXT.__auth_stubs: 0x1490
   __TEXT.__objc_methlist: 0x12150
   __TEXT.__const: 0x678
-  __TEXT.__cstring: 0x1e994
+  __TEXT.__cstring: 0x1e9d3
   __TEXT.__oslogstring: 0x3b79
   __TEXT.__gcc_except_tab: 0x1780
   __TEXT.__dlopen_cstrs: 0x52

   __DATA_CONST.__objc_arraydata: 0xb48
   __AUTH_CONST.__auth_got: 0xa60
   __AUTH_CONST.__const: 0x1e60
-  __AUTH_CONST.__cfstring: 0x1a7c0
+  __AUTH_CONST.__cfstring: 0x1a7e0
   __AUTH_CONST.__objc_const: 0x22a70
   __AUTH_CONST.__objc_intobj: 0x19e0
   __AUTH_CONST.__objc_arrayobj: 0x3d8

   - /usr/lib/libobjc.A.dylib
   Functions: 6481
   Symbols:   14167
-  CStrings:  13596
+  CStrings:  13597
 
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 936 -> 968
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1808 -> 1796
~ -[WiFiUsageSession _generateState] : 1088 -> 1092
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q4eYWr/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0Ll6qr/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
```
