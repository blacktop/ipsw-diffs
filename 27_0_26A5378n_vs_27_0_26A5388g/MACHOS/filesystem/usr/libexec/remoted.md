## remoted

> `/usr/libexec/remoted`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-245.0.4.0.0
-  __TEXT.__text: 0x40fd8
+245.0.6.0.0
+  __TEXT.__text: 0x4109c
   __TEXT.__auth_stubs: 0x1800
   __TEXT.__objc_stubs: 0x2700
   __TEXT.__objc_methlist: 0x1828
   __TEXT.__const: 0x222
-  __TEXT.__oslogstring: 0x8976
+  __TEXT.__oslogstring: 0x89c5
   __TEXT.__cstring: 0x245d
   __TEXT.__objc_methname: 0x2976
   __TEXT.__objc_classname: 0x3c3
   __TEXT.__objc_methtype: 0x9e3
   __TEXT.__gcc_except_tab: 0x1054
-  __TEXT.__unwind_info: 0xe58
+  __TEXT.__unwind_info: 0xe60
   __DATA_CONST.__const: 0x14e0
   __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0xf8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1453
+  Functions: 1454
   Symbols:   489
-  CStrings:  1912
+  CStrings:  1913
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.42l6y3/Sources/RemoteServiceDiscovery_executables/remoted/modules/identity.m"
+ "get_local_device_description denied: missing entitlement (client=\"%{public}s\")"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.K1XCVP/Sources/RemoteServiceDiscovery_executables/remoted/modules/identity.m"
```
