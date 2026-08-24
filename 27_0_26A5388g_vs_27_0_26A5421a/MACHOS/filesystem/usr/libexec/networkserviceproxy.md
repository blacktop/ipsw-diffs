## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-980.0.0.0.0
-  __TEXT.__text: 0xcf36c
+985.0.0.0.0
+  __TEXT.__text: 0xcf888
   __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_stubs: 0xd080
+  __TEXT.__objc_stubs: 0xd0e0
   __TEXT.__objc_methlist: 0x5044
   __TEXT.__const: 0x288
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3824
-  __TEXT.__oslogstring: 0x1154c
-  __TEXT.__cstring: 0xdef9
-  __TEXT.__objc_methname: 0x10261
+  __TEXT.__gcc_except_tab: 0x3854
+  __TEXT.__oslogstring: 0x116a5
+  __TEXT.__cstring: 0xdf49
+  __TEXT.__objc_methname: 0x102bb
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a60
-  __TEXT.__unwind_info: 0x19c8
-  __DATA_CONST.__const: 0x25c0
-  __DATA_CONST.__cfstring: 0x8b20
+  __TEXT.__unwind_info: 0x19c0
+  __DATA_CONST.__const: 0x25d8
+  __DATA_CONST.__cfstring: 0x8ba0
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__auth_got: 0xbb0
   __DATA_CONST.__got: 0x840
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb138
-  __DATA.__objc_selrefs: 0x3ac8
-  __DATA.__objc_ivar: 0x9f8
+  __DATA.__objc_const: 0xb158
+  __DATA.__objc_selrefs: 0x3ae0
+  __DATA.__objc_ivar: 0x9fc
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__bss: 0x218

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2255
+  Functions: 2254
   Symbols:   618
-  CStrings:  6290
+  CStrings:  6304
 
CStrings:
+ "Failed to write reboot fetch state to preference file"
+ "NSPRebootFetchCount"
+ "NSPRebootFetchLastDate"
+ "No previous server state in UEA, treating as first launch after boot"
+ "Reboot"
+ "Reboot config refresh is disabled by configuration"
+ "Skipping reboot config refresh, already fetched %u times today (max %u)"
+ "Triggering reboot config refresh (%u of %u allowed today)"
+ "_firstLaunchAfterBoot"
+ "cloud.llm.waitlist"
+ "hasMaxRebootFetchesPerDay"
+ "max reboot fetches per day changed to %u"
+ "maxRebootFetchesPerDay"
+ "startOfDayForDate:"
+ "v48@?0@\"NSPPrivacyProxySuccessResponse\"8@\"NSData\"16q24@\"NSString\"32@\"NSString\"40"
- "v40@?0@\"NSPPrivacyProxySuccessResponse\"8q16@\"NSString\"24@\"NSString\"32"
```
