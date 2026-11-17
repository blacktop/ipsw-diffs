## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3896.300.31.0.0
-  __TEXT.__text: 0x84020
-  __TEXT.__auth_stubs: 0x1210
+3896.300.71.2.4
+  __TEXT.__text: 0x845e4
+  __TEXT.__auth_stubs: 0x1220
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0xaca0
   __TEXT.__objc_methlist: 0x63b4
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0xea5c
-  __TEXT.__cstring: 0x3fab
+  __TEXT.__gcc_except_tab: 0xeb08
+  __TEXT.__cstring: 0x4345
   __TEXT.__objc_methname: 0xf717
   __TEXT.__objc_classname: 0xbd1
   __TEXT.__objc_methtype: 0x2fbd
-  __TEXT.__oslogstring: 0xfeb5
-  __TEXT.__unwind_info: 0x31d0
-  __DATA_CONST.__const: 0x1660
-  __DATA_CONST.__cfstring: 0x1ee0
+  __TEXT.__oslogstring: 0x100b4
+  __TEXT.__unwind_info: 0x3200
+  __DATA_CONST.__const: 0x1898
+  __DATA_CONST.__cfstring: 0x20e0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x920
+  __DATA_CONST.__auth_got: 0x928
   __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x9000

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2118
-  Symbols:   522
-  CStrings:  3949
+  Functions: 2121
+  Symbols:   523
+  CStrings:  3999
 
Symbols:
+ _sysctlbyname
CStrings:
+ "0x%08x (%@)"
+ "CS_ADHOC"
+ "CS_CHECK_EXPIRATION"
+ "CS_DATAVAULT_CONTROLLER"
+ "CS_DEBUGGED"
+ "CS_DEV_CODE"
+ "CS_ENFORCEMENT"
+ "CS_ENTITLEMENTS_VALIDATED"
+ "CS_EXEC_INHERIT_SIP"
+ "CS_EXEC_SET_ENFORCEMENT"
+ "CS_EXEC_SET_HARD"
+ "CS_EXEC_SET_KILL"
+ "CS_FORCED_LV"
+ "CS_GET_TASK_ALLOW"
+ "CS_HARD"
+ "CS_INSTALLER"
+ "CS_INVALID_ALLOWED"
+ "CS_KILL"
+ "CS_KILLED"
+ "CS_LINKER_SIGNED"
+ "CS_NO_UNTRUSTED_HELPERS"
+ "CS_NVRAM_UNRESTRICTED"
+ "CS_PLATFORM_BINARY"
+ "CS_PLATFORM_PATH"
+ "CS_REQUIRE_LV"
+ "CS_RESTRICT"
+ "CS_RUNTIME"
+ "CS_SIGNED"
+ "CS_VALID"
+ "CS_VALIDATION_CATEGORY_APP_STORE"
+ "CS_VALIDATION_CATEGORY_DEVELOPER_ID"
+ "CS_VALIDATION_CATEGORY_DEVELOPMENT"
+ "CS_VALIDATION_CATEGORY_ENTERPRISE"
+ "CS_VALIDATION_CATEGORY_INVALID"
+ "CS_VALIDATION_CATEGORY_LOCAL_SIGNING"
+ "CS_VALIDATION_CATEGORY_NONE"
+ "CS_VALIDATION_CATEGORY_OOPJIT"
+ "CS_VALIDATION_CATEGORY_PLATFORM"
+ "CS_VALIDATION_CATEGORY_ROSETTA"
+ "CS_VALIDATION_CATEGORY_TESTFLIGHT"
+ "Client %{public}@ (pid %d) validation category %{public}@, csFlags %{public}@"
+ "Code signing configuration 0x%08x relaxes trust evaluation. Not enforcing identity tiers"
+ "Failed to read code signing configuration, errno: %{darwin.errno}d. Enforcing identity tiers"
+ "Failed to read validation category for %@, error: %d. Treating client as unsigned"
+ "NDNWSession <%{public}@> Client tried to set an SZExtractor but is not a platform binary and is missing the %@ entitlement"
+ "NDSession <%{public}@> Client tried to set an SZExtractor but is not a platform binary and is missing the %@ entitlement"
+ "UNKNOWN(%u)"
+ "UNKNOWN(0x%08x)"
+ "com.apple.private.nsurlsession.custom-extractor"
+ "none"
+ "security.codesigning.config"
- "Failed to read validation category, error: %d. Treating client as unsigned"
```
